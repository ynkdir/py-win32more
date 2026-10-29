from __future__ import annotations
from win32more._prelude import *
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Networking.WinSock
import win32more.Windows.Win32.System.HostComputeSystem
import win32more.Windows.Win32.System.Hypervisor
import win32more.Windows.Win32.System.Power
HVSOCKET_CONNECT_TIMEOUT: UInt32 = 1
HVSOCKET_CONNECT_TIMEOUT_MAX: UInt32 = 300000
HVSOCKET_CONNECTED_SUSPEND: UInt32 = 4
HVSOCKET_HIGH_VTL: UInt32 = 8
HV_PROTOCOL_RAW: UInt32 = 1
HVSOCKET_ADDRESS_FLAG_PASSTHRU: UInt32 = 1
WHV_EXTENDED_VM_EXITS_RESERVED_BITFIELD_COUNT: UInt32 = 49
WHV_PROCESSOR_FEATURES_BANKS_COUNT: UInt32 = 2
WHV_SYNTHETIC_PROCESSOR_FEATURES_RESERVED_BITFIELD_COUNT: UInt32 = 17
WHV_SYNTHETIC_PROCESSOR_FEATURES_BANKS_COUNT: UInt32 = 1
WHV_VTL_ALL: UInt32 = 15
WHV_READ_WRITE_GPA_RANGE_MAX_SIZE: UInt32 = 16
WHV_HYPERCALL_CONTEXT_MAX_XMM_REGISTERS: UInt32 = 6
WHV_ARM64_GLOBAL_INTERRUPT_CONTROLLER_STATE_VERSION_CURRENT: UInt32 = 1
WHV_ARM64_INTERRUPT_CONTROLLER_STATE_VERSION_CURRENT: UInt32 = 1
WHV_MAX_DEVICE_ID_SIZE_IN_CHARS: UInt32 = 200
WHV_VPCI_TYPE0_BAR_COUNT: UInt32 = 6
WHV_ANY_VP: UInt32 = 4294967295
WHV_SYNIC_MESSAGE_SIZE: UInt32 = 256
VM_GENCOUNTER_SYMBOLIC_LINK_NAME: String = '\\VmGenerationCounter'
IOCTL_VMGENCOUNTER_READ: UInt32 = 3325956
HDV_PCI_BAR_COUNT: UInt32 = 6
HV_GUID_ZERO: Guid = Guid('{00000000-0000-0000-0000-000000000000}')
HV_GUID_BROADCAST: Guid = Guid('{ffffffff-ffff-ffff-ffff-ffffffffffff}')
HV_GUID_CHILDREN: Guid = Guid('{90db8b89-0d35-4f79-8ce9-49ea0ac8b7cd}')
HV_GUID_LOOPBACK: Guid = Guid('{e0e16197-dd56-4a10-9195-5ee7a155a838}')
HV_GUID_PARENT: Guid = Guid('{a42e7cda-d03f-480c-9cc2-a4de20abb878}')
HV_GUID_SILOHOST: Guid = Guid('{36bd0c5c-7276-4223-88ba-7d03b654c568}')
HV_GUID_VSOCK_TEMPLATE: Guid = Guid('{00000000-facb-11e6-bd58-64006a7986d3}')
GUID_DEVINTERFACE_VM_GENCOUNTER: Guid = Guid('{3ff2c92b-6598-4e60-8e1c-0ccf4927e319}')
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvGetCapability(CapabilityCode: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE, CapabilityBuffer: VoidPtr, CapabilityBufferSizeInBytes: UInt32, WrittenSizeInBytes: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvCreatePartition(Partition: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvSetupPartition(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvResetPartition(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvDeletePartition(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvGetPartitionProperty(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, PropertyCode: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE, PropertyBuffer: VoidPtr, PropertyBufferSizeInBytes: UInt32, WrittenSizeInBytes: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvSetPartitionProperty(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, PropertyCode: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE, PropertyBuffer: VoidPtr, PropertyBufferSizeInBytes: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvSuspendPartitionTime(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvResumePartitionTime(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvMapGpaRange(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, SourceAddress: VoidPtr, GuestAddress: UInt64, SizeInBytes: UInt64, Flags: win32more.Windows.Win32.System.Hypervisor.WHV_MAP_GPA_RANGE_FLAGS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvMapGpaRange2(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, Process: win32more.Windows.Win32.Foundation.HANDLE, SourceAddress: VoidPtr, GuestAddress: UInt64, SizeInBytes: UInt64, Flags: win32more.Windows.Win32.System.Hypervisor.WHV_MAP_GPA_RANGE_FLAGS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvUnmapGpaRange(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, GuestAddress: UInt64, SizeInBytes: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvTranslateGva(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, Gva: UInt64, TranslateFlags: win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_FLAGS, TranslationResult: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_RESULT), Gpa: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvCreateVirtualProcessor(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, Flags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvCreateVirtualProcessor2(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, Properties: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_VIRTUAL_PROCESSOR_PROPERTY), PropertyCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvDeleteVirtualProcessor(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvRunVirtualProcessor(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, ExitContext: VoidPtr, ExitContextSizeInBytes: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvCancelRunVirtualProcessor(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, Flags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvGetVirtualProcessorRegisters(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, RegisterNames: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME), RegisterCount: UInt32, RegisterValues: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_VALUE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvSetVirtualProcessorRegisters(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, RegisterNames: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME), RegisterCount: UInt32, RegisterValues: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_VALUE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64':
    @winfunctype('WinHvPlatform.dll')
    def WHvGetVirtualProcessorInterruptControllerState(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, State: VoidPtr, StateSize: UInt32, WrittenSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64':
    @winfunctype('WinHvPlatform.dll')
    def WHvSetVirtualProcessorInterruptControllerState(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, State: VoidPtr, StateSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvRequestInterrupt(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, Interrupt: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_INTERRUPT_CONTROL), InterruptControlSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64':
    @winfunctype('WinHvPlatform.dll')
    def WHvGetVirtualProcessorXsaveState(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, Buffer: VoidPtr, BufferSizeInBytes: UInt32, BytesWritten: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64':
    @winfunctype('WinHvPlatform.dll')
    def WHvSetVirtualProcessorXsaveState(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, Buffer: VoidPtr, BufferSizeInBytes: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvQueryGpaRangeDirtyBitmap(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, GuestAddress: UInt64, RangeSizeInBytes: UInt64, Bitmap: POINTER(UInt64), BitmapSizeInBytes: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvGetPartitionCounters(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, CounterSet: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_COUNTER_SET, Buffer: VoidPtr, BufferSizeInBytes: UInt32, BytesWritten: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvGetVirtualProcessorCounters(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, CounterSet: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_COUNTER_SET, Buffer: VoidPtr, BufferSizeInBytes: UInt32, BytesWritten: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64':
    @winfunctype('WinHvPlatform.dll')
    def WHvGetVirtualProcessorInterruptControllerState2(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, State: VoidPtr, StateSize: UInt32, WrittenSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64':
    @winfunctype('WinHvPlatform.dll')
    def WHvSetVirtualProcessorInterruptControllerState2(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, State: VoidPtr, StateSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvRegisterPartitionDoorbellEvent(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, MatchData: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_DOORBELL_MATCH_DATA), EventHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvUnregisterPartitionDoorbellEvent(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, MatchData: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_DOORBELL_MATCH_DATA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvAdviseGpaRange(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, GpaRanges: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_MEMORY_RANGE_ENTRY), GpaRangesCount: UInt32, Advice: win32more.Windows.Win32.System.Hypervisor.WHV_ADVISE_GPA_RANGE_CODE, AdviceBuffer: VoidPtr, AdviceBufferSizeInBytes: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvReadGpaRange(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, GuestAddress: UInt64, Controls: win32more.Windows.Win32.System.Hypervisor.WHV_ACCESS_GPA_CONTROLS, Data: VoidPtr, DataSizeInBytes: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvWriteGpaRange(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, GuestAddress: UInt64, Controls: win32more.Windows.Win32.System.Hypervisor.WHV_ACCESS_GPA_CONTROLS, Data: VoidPtr, DataSizeInBytes: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvSignalVirtualProcessorSynicEvent(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, SynicEvent: win32more.Windows.Win32.System.Hypervisor.WHV_SYNIC_EVENT_PARAMETERS, NewlySignaled: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvGetVirtualProcessorState(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, StateType: win32more.Windows.Win32.System.Hypervisor.WHV_VIRTUAL_PROCESSOR_STATE_TYPE, Buffer: VoidPtr, BufferSizeInBytes: UInt32, BytesWritten: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvSetVirtualProcessorState(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, StateType: win32more.Windows.Win32.System.Hypervisor.WHV_VIRTUAL_PROCESSOR_STATE_TYPE, Buffer: VoidPtr, BufferSizeInBytes: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvAllocateVpciResource(ProviderId: POINTER(Guid), Flags: win32more.Windows.Win32.System.Hypervisor.WHV_ALLOCATE_VPCI_RESOURCE_FLAGS, ResourceDescriptor: VoidPtr, ResourceDescriptorSizeInBytes: UInt32, VpciResource: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvCreateVpciDevice(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, LogicalDeviceId: UInt64, VpciResource: win32more.Windows.Win32.Foundation.HANDLE, Flags: win32more.Windows.Win32.System.Hypervisor.WHV_CREATE_VPCI_DEVICE_FLAGS, NotificationEventHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvDeleteVpciDevice(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, LogicalDeviceId: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvGetVpciDeviceProperty(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, LogicalDeviceId: UInt64, PropertyCode: win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_DEVICE_PROPERTY_CODE, PropertyBuffer: VoidPtr, PropertyBufferSizeInBytes: UInt32, WrittenSizeInBytes: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvGetVpciDeviceNotification(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, LogicalDeviceId: UInt64, Notification: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_DEVICE_NOTIFICATION), NotificationSizeInBytes: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvMapVpciDeviceMmioRanges(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, LogicalDeviceId: UInt64, MappingCount: POINTER(UInt32), Mappings: POINTER(POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_MMIO_MAPPING))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvUnmapVpciDeviceMmioRanges(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, LogicalDeviceId: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvSetVpciDevicePowerState(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, LogicalDeviceId: UInt64, PowerState: win32more.Windows.Win32.System.Power.DEVICE_POWER_STATE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvReadVpciDeviceRegister(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, LogicalDeviceId: UInt64, Register: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_DEVICE_REGISTER), Data: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvWriteVpciDeviceRegister(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, LogicalDeviceId: UInt64, Register: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_DEVICE_REGISTER), Data: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvMapVpciDeviceInterrupt(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, LogicalDeviceId: UInt64, Index: UInt32, MessageCount: UInt32, Target: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_INTERRUPT_TARGET), MsiAddress: POINTER(UInt64), MsiData: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvUnmapVpciDeviceInterrupt(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, LogicalDeviceId: UInt64, Index: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvRetargetVpciDeviceInterrupt(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, LogicalDeviceId: UInt64, MsiAddress: UInt64, MsiData: UInt32, Target: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_INTERRUPT_TARGET)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvRequestVpciDeviceInterrupt(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, LogicalDeviceId: UInt64, MsiAddress: UInt64, MsiData: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvGetVpciDeviceInterruptTarget(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, LogicalDeviceId: UInt64, Index: UInt32, MultiMessageNumber: UInt32, Target: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_INTERRUPT_TARGET), TargetSizeInBytes: UInt32, BytesWritten: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvCreateTrigger(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, Parameters: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_TRIGGER_PARAMETERS), TriggerHandle: POINTER(VoidPtr), EventHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvUpdateTriggerParameters(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, Parameters: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_TRIGGER_PARAMETERS), TriggerHandle: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvDeleteTrigger(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, TriggerHandle: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvCreateNotificationPort(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, Parameters: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_NOTIFICATION_PORT_PARAMETERS), EventHandle: win32more.Windows.Win32.Foundation.HANDLE, PortHandle: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvSetNotificationPortProperty(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, PortHandle: VoidPtr, PropertyCode: win32more.Windows.Win32.System.Hypervisor.WHV_NOTIFICATION_PORT_PROPERTY_CODE, PropertyValue: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvDeleteNotificationPort(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, PortHandle: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvPostVirtualProcessorSynicMessage(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, SintIndex: UInt32, Message: VoidPtr, MessageSizeInBytes: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64':
    @winfunctype('WinHvPlatform.dll')
    def WHvGetVirtualProcessorCpuidOutput(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, Eax: UInt32, Ecx: UInt32, CpuidOutput: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_CPUID_OUTPUT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64':
    @winfunctype('WinHvPlatform.dll')
    def WHvGetInterruptTargetVpSet(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, Destination: UInt64, DestinationMode: win32more.Windows.Win32.System.Hypervisor.WHV_INTERRUPT_DESTINATION_MODE, TargetVps: POINTER(UInt32), VpCount: UInt32, TargetVpCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvStartPartitionMigration(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, MigrationHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvCancelPartitionMigration(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvCompletePartitionMigration(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    @winfunctype('WinHvPlatform.dll')
    def WHvAcceptPartitionMigration(MigrationHandle: win32more.Windows.Win32.Foundation.HANDLE, Partition: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64':
    @winfunctype('WinHvEmulation.dll')
    def WHvEmulatorCreateEmulator(Callbacks: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_EMULATOR_CALLBACKS), Emulator: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64':
    @winfunctype('WinHvEmulation.dll')
    def WHvEmulatorDestroyEmulator(Emulator: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64':
    @winfunctype('WinHvEmulation.dll')
    def WHvEmulatorTryIoEmulation(Emulator: VoidPtr, Context: VoidPtr, VpContext: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_X64_VP_EXIT_CONTEXT), IoInstructionContext: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_X64_IO_PORT_ACCESS_CONTEXT), EmulatorReturnStatus: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_EMULATOR_STATUS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64':
    @winfunctype('WinHvEmulation.dll')
    def WHvEmulatorTryMmioEmulation(Emulator: VoidPtr, Context: VoidPtr, VpContext: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_X64_VP_EXIT_CONTEXT), MmioInstructionContext: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_MEMORY_ACCESS_CONTEXT), EmulatorReturnStatus: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_EMULATOR_STATUS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('vmdevicehost.dll')
def HdvInitializeDeviceHost(computeSystem: win32more.Windows.Win32.System.HostComputeSystem.HCS_SYSTEM, deviceHostHandle: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('vmdevicehost.dll')
def HdvInitializeDeviceHostEx(computeSystem: win32more.Windows.Win32.System.HostComputeSystem.HCS_SYSTEM, flags: win32more.Windows.Win32.System.Hypervisor.HDV_DEVICE_HOST_FLAGS, deviceHostHandle: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('vmdevicehost.dll')
def HdvTeardownDeviceHost(deviceHostHandle: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('vmdevicehost.dll')
def HdvCreateDeviceInstance(deviceHostHandle: VoidPtr, deviceType: win32more.Windows.Win32.System.Hypervisor.HDV_DEVICE_TYPE, deviceClassId: POINTER(Guid), deviceInstanceId: POINTER(Guid), deviceInterface: VoidPtr, deviceContext: VoidPtr, deviceHandle: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('vmdevicehost.dll')
def HdvReadGuestMemory(requestor: VoidPtr, guestPhysicalAddress: UInt64, byteCount: UInt32, buffer: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('vmdevicehost.dll')
def HdvWriteGuestMemory(requestor: VoidPtr, guestPhysicalAddress: UInt64, byteCount: UInt32, buffer: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('vmdevicehost.dll')
def HdvCreateGuestMemoryAperture(requestor: VoidPtr, guestPhysicalAddress: UInt64, byteCount: UInt32, writeProtected: win32more.Windows.Win32.Foundation.BOOL, mappedAddress: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('vmdevicehost.dll')
def HdvDestroyGuestMemoryAperture(requestor: VoidPtr, mappedAddress: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('vmdevicehost.dll')
def HdvDeliverGuestInterrupt(requestor: VoidPtr, msiAddress: UInt64, msiData: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('vmdevicehost.dll')
def HdvRegisterDoorbell(requestor: VoidPtr, BarIndex: win32more.Windows.Win32.System.Hypervisor.HDV_PCI_BAR_SELECTOR, BarOffset: UInt64, TriggerValue: UInt64, Flags: UInt64, DoorbellEvent: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('vmdevicehost.dll')
def HdvUnregisterDoorbell(requestor: VoidPtr, BarIndex: win32more.Windows.Win32.System.Hypervisor.HDV_PCI_BAR_SELECTOR, BarOffset: UInt64, TriggerValue: UInt64, Flags: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('vmdevicehost.dll')
def HdvCreateSectionBackedMmioRange(requestor: VoidPtr, barIndex: win32more.Windows.Win32.System.Hypervisor.HDV_PCI_BAR_SELECTOR, offsetInPages: UInt64, lengthInPages: UInt64, MappingFlags: win32more.Windows.Win32.System.Hypervisor.HDV_MMIO_MAPPING_FLAGS, sectionHandle: win32more.Windows.Win32.Foundation.HANDLE, sectionOffsetInPages: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('vmdevicehost.dll')
def HdvDestroySectionBackedMmioRange(requestor: VoidPtr, barIndex: win32more.Windows.Win32.System.Hypervisor.HDV_PCI_BAR_SELECTOR, offsetInPages: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def LocateSavedStateFiles(vmName: win32more.Windows.Win32.Foundation.PWSTR, snapshotName: win32more.Windows.Win32.Foundation.PWSTR, binPath: POINTER(win32more.Windows.Win32.Foundation.PWSTR), vsvPath: POINTER(win32more.Windows.Win32.Foundation.PWSTR), vmrsPath: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def LoadSavedStateFile(vmrsFile: win32more.Windows.Win32.Foundation.PWSTR, vmSavedStateDumpHandle: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def ApplyPendingSavedStateFileReplayLog(vmrsFile: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def LoadSavedStateFiles(binFile: win32more.Windows.Win32.Foundation.PWSTR, vsvFile: win32more.Windows.Win32.Foundation.PWSTR, vmSavedStateDumpHandle: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def ReleaseSavedStateFiles(vmSavedStateDumpHandle: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def GetGuestEnabledVirtualTrustLevels(vmSavedStateDumpHandle: VoidPtr, virtualTrustLevels: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def GetGuestOsInfo(vmSavedStateDumpHandle: VoidPtr, virtualTrustLevel: Byte, guestOsInfo: POINTER(win32more.Windows.Win32.System.Hypervisor.GUEST_OS_INFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def GetVpCount(vmSavedStateDumpHandle: VoidPtr, vpCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def GetArchitecture(vmSavedStateDumpHandle: VoidPtr, vpId: UInt32, architecture: POINTER(win32more.Windows.Win32.System.Hypervisor.VIRTUAL_PROCESSOR_ARCH)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def ForceArchitecture(vmSavedStateDumpHandle: VoidPtr, vpId: UInt32, architecture: win32more.Windows.Win32.System.Hypervisor.VIRTUAL_PROCESSOR_ARCH) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def GetActiveVirtualTrustLevel(vmSavedStateDumpHandle: VoidPtr, vpId: UInt32, virtualTrustLevel: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def GetEnabledVirtualTrustLevels(vmSavedStateDumpHandle: VoidPtr, vpId: UInt32, virtualTrustLevels: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def ForceActiveVirtualTrustLevel(vmSavedStateDumpHandle: VoidPtr, vpId: UInt32, virtualTrustLevel: Byte) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def IsActiveVirtualTrustLevelEnabled(vmSavedStateDumpHandle: VoidPtr, vpId: UInt32, activeVirtualTrustLevelEnabled: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def IsNestedVirtualizationEnabled(vmSavedStateDumpHandle: VoidPtr, enabled: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def GetNestedVirtualizationMode(vmSavedStateDumpHandle: VoidPtr, vpId: UInt32, enabled: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def ForceNestedHostMode(vmSavedStateDumpHandle: VoidPtr, vpId: UInt32, hostMode: win32more.Windows.Win32.Foundation.BOOL, oldMode: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def InKernelSpace(vmSavedStateDumpHandle: VoidPtr, vpId: UInt32, inKernelSpace: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def GetRegisterValue(vmSavedStateDumpHandle: VoidPtr, vpId: UInt32, registerId: UInt32, registerValue: POINTER(win32more.Windows.Win32.System.Hypervisor.VIRTUAL_PROCESSOR_REGISTER)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def GetPagingMode(vmSavedStateDumpHandle: VoidPtr, vpId: UInt32, pagingMode: POINTER(win32more.Windows.Win32.System.Hypervisor.PAGING_MODE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def ForcePagingMode(vmSavedStateDumpHandle: VoidPtr, vpId: UInt32, pagingMode: win32more.Windows.Win32.System.Hypervisor.PAGING_MODE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def ReadGuestPhysicalAddress(vmSavedStateDumpHandle: VoidPtr, physicalAddress: UInt64, buffer: VoidPtr, bufferSize: UInt32, bytesRead: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def GuestVirtualAddressToPhysicalAddress(vmSavedStateDumpHandle: VoidPtr, vpId: UInt32, virtualAddress: UInt64, physicalAddress: POINTER(UInt64), unmappedRegionSize: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def GetGuestPhysicalMemoryChunks(vmSavedStateDumpHandle: VoidPtr, memoryChunkPageSize: POINTER(UInt64), memoryChunks: POINTER(win32more.Windows.Win32.System.Hypervisor.GPA_MEMORY_CHUNK), memoryChunkCount: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def GuestPhysicalAddressToRawSavedMemoryOffset(vmSavedStateDumpHandle: VoidPtr, physicalAddress: UInt64, rawSavedMemoryOffset: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def ReadGuestRawSavedMemory(vmSavedStateDumpHandle: VoidPtr, rawSavedMemoryOffset: UInt64, buffer: VoidPtr, bufferSize: UInt32, bytesRead: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def GetGuestRawSavedMemorySize(vmSavedStateDumpHandle: VoidPtr, guestRawSavedMemorySize: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def SetMemoryBlockCacheLimit(vmSavedStateDumpHandle: VoidPtr, memoryBlockCacheLimit: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def GetMemoryBlockCacheLimit(vmSavedStateDumpHandle: VoidPtr, memoryBlockCacheLimit: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def ApplyGuestMemoryFix(vmSavedStateDumpHandle: VoidPtr, vpId: UInt32, virtualAddress: UInt64, fixBuffer: VoidPtr, fixBufferSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def LoadSavedStateSymbolProvider(vmSavedStateDumpHandle: VoidPtr, userSymbols: win32more.Windows.Win32.Foundation.PWSTR, force: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def ReleaseSavedStateSymbolProvider(vmSavedStateDumpHandle: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def GetSavedStateSymbolProviderHandle(vmSavedStateDumpHandle: VoidPtr) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def SetSavedStateSymbolProviderDebugInfoCallback(vmSavedStateDumpHandle: VoidPtr, Callback: win32more.Windows.Win32.System.Hypervisor.GUEST_SYMBOLS_PROVIDER_DEBUG_INFO_CALLBACK) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def LoadSavedStateModuleSymbols(vmSavedStateDumpHandle: VoidPtr, imageName: win32more.Windows.Win32.Foundation.PSTR, moduleName: win32more.Windows.Win32.Foundation.PSTR, baseAddress: UInt64, sizeOfBase: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def LoadSavedStateModuleSymbolsEx(vmSavedStateDumpHandle: VoidPtr, imageName: win32more.Windows.Win32.Foundation.PSTR, imageTimestamp: UInt32, moduleName: win32more.Windows.Win32.Foundation.PSTR, baseAddress: UInt64, sizeOfBase: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def ResolveSavedStateGlobalVariableAddress(vmSavedStateDumpHandle: VoidPtr, vpId: UInt32, globalName: win32more.Windows.Win32.Foundation.PSTR, virtualAddress: POINTER(UInt64), size: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def ReadSavedStateGlobalVariable(vmSavedStateDumpHandle: VoidPtr, vpId: UInt32, globalName: win32more.Windows.Win32.Foundation.PSTR, buffer: VoidPtr, bufferSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def GetSavedStateSymbolTypeSize(vmSavedStateDumpHandle: VoidPtr, vpId: UInt32, typeName: win32more.Windows.Win32.Foundation.PSTR, size: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def FindSavedStateSymbolFieldInType(vmSavedStateDumpHandle: VoidPtr, vpId: UInt32, typeName: win32more.Windows.Win32.Foundation.PSTR, fieldName: win32more.Windows.Win32.Foundation.PWSTR, offset: POINTER(UInt32), found: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def GetSavedStateSymbolFieldInfo(vmSavedStateDumpHandle: VoidPtr, vpId: UInt32, typeName: win32more.Windows.Win32.Foundation.PSTR, typeFieldInfoMap: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def ScanMemoryForDosImages(vmSavedStateDumpHandle: VoidPtr, vpId: UInt32, startAddress: UInt64, endAddress: UInt64, callbackContext: VoidPtr, foundImageCallback: win32more.Windows.Win32.System.Hypervisor.FOUND_IMAGE_CALLBACK, standaloneAddress: POINTER(UInt64), standaloneAddressCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def CallStackUnwind(vmSavedStateDumpHandle: VoidPtr, vpId: UInt32, imageInfo: POINTER(win32more.Windows.Win32.System.Hypervisor.MODULE_INFO), imageInfoCount: UInt32, frameCount: UInt32, callStack: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class DOS_IMAGE_INFO(Structure):
    PdbName: win32more.Windows.Win32.Foundation.PSTR
    ImageBaseAddress: UInt64
    ImageSize: UInt32
    Timestamp: UInt32
@winfunctype_pointer
def FOUND_IMAGE_CALLBACK(Context: VoidPtr, ImageInfo: POINTER(win32more.Windows.Win32.System.Hypervisor.DOS_IMAGE_INFO)) -> win32more.Windows.Win32.Foundation.BOOL: ...
class GPA_MEMORY_CHUNK(Structure):
    GuestPhysicalStartPageIndex: UInt64
    PageCount: UInt64
class GUEST_OS_INFO(Union):
    AsUINT64: UInt64
    ClosedSource: _ClosedSource_e__Struct
    OpenSource: _OpenSource_e__Struct
    class _ClosedSource_e__Struct(Structure):
        BuildNumber: Annotated[UInt64, NativeBitfieldAttribute(16)]
        ServiceVersion: Annotated[UInt64, NativeBitfieldAttribute(8)]
        MinorVersion: Annotated[UInt64, NativeBitfieldAttribute(8)]
        MajorVersion: Annotated[UInt64, NativeBitfieldAttribute(8)]
        OsId: Annotated[UInt64, NativeBitfieldAttribute(8)]
        VendorId: Annotated[UInt64, NativeBitfieldAttribute(16)]
    class _OpenSource_e__Struct(Structure):
        VendorSpecific1: Annotated[UInt64, NativeBitfieldAttribute(16)]
        Version: Annotated[UInt64, NativeBitfieldAttribute(32)]
        VendorSpecific2: Annotated[UInt64, NativeBitfieldAttribute(8)]
        OsId: Annotated[UInt64, NativeBitfieldAttribute(7)]
        IsOpenSource: Annotated[UInt64, NativeBitfieldAttribute(1)]
GUEST_OS_MICROSOFT_IDS = Int32
GuestOsMicrosoftUndefined: win32more.Windows.Win32.System.Hypervisor.GUEST_OS_MICROSOFT_IDS = 0
GuestOsMicrosoftMSDOS: win32more.Windows.Win32.System.Hypervisor.GUEST_OS_MICROSOFT_IDS = 1
GuestOsMicrosoftWindows3x: win32more.Windows.Win32.System.Hypervisor.GUEST_OS_MICROSOFT_IDS = 2
GuestOsMicrosoftWindows9x: win32more.Windows.Win32.System.Hypervisor.GUEST_OS_MICROSOFT_IDS = 3
GuestOsMicrosoftWindowsNT: win32more.Windows.Win32.System.Hypervisor.GUEST_OS_MICROSOFT_IDS = 4
GuestOsMicrosoftWindowsCE: win32more.Windows.Win32.System.Hypervisor.GUEST_OS_MICROSOFT_IDS = 5
GUEST_OS_OPENSOURCE_IDS = Int32
GuestOsOpenSourceUndefined: win32more.Windows.Win32.System.Hypervisor.GUEST_OS_OPENSOURCE_IDS = 0
GuestOsOpenSourceLinux: win32more.Windows.Win32.System.Hypervisor.GUEST_OS_OPENSOURCE_IDS = 1
GuestOsOpenSourceFreeBSD: win32more.Windows.Win32.System.Hypervisor.GUEST_OS_OPENSOURCE_IDS = 2
GuestOsOpenSourceXen: win32more.Windows.Win32.System.Hypervisor.GUEST_OS_OPENSOURCE_IDS = 3
GuestOsOpenSourceIllumos: win32more.Windows.Win32.System.Hypervisor.GUEST_OS_OPENSOURCE_IDS = 4
GUEST_OS_VENDOR = Int32
GuestOsVendorUndefined: win32more.Windows.Win32.System.Hypervisor.GUEST_OS_VENDOR = 0
GuestOsVendorMicrosoft: win32more.Windows.Win32.System.Hypervisor.GUEST_OS_VENDOR = 1
GuestOsVendorHPE: win32more.Windows.Win32.System.Hypervisor.GUEST_OS_VENDOR = 2
GuestOsVendorLANCOM: win32more.Windows.Win32.System.Hypervisor.GUEST_OS_VENDOR = 512
@winfunctype_pointer
def GUEST_SYMBOLS_PROVIDER_DEBUG_INFO_CALLBACK(InfoMessage: win32more.Windows.Win32.Foundation.PSTR) -> Void: ...
HDV_DEVICE_HOST_FLAGS = Int32
HdvDeviceHostFlagNone: win32more.Windows.Win32.System.Hypervisor.HDV_DEVICE_HOST_FLAGS = 0
HdvDeviceHostFlagInitializeComSecurity: win32more.Windows.Win32.System.Hypervisor.HDV_DEVICE_HOST_FLAGS = 1
HDV_DEVICE_TYPE = Int32
HdvDeviceTypeUndefined: win32more.Windows.Win32.System.Hypervisor.HDV_DEVICE_TYPE = 0
HdvDeviceTypePCI: win32more.Windows.Win32.System.Hypervisor.HDV_DEVICE_TYPE = 1
HDV_DOORBELL_FLAGS = Int32
HDV_DOORBELL_FLAG_TRIGGER_SIZE_ANY: win32more.Windows.Win32.System.Hypervisor.HDV_DOORBELL_FLAGS = 0
HDV_DOORBELL_FLAG_TRIGGER_SIZE_BYTE: win32more.Windows.Win32.System.Hypervisor.HDV_DOORBELL_FLAGS = 1
HDV_DOORBELL_FLAG_TRIGGER_SIZE_WORD: win32more.Windows.Win32.System.Hypervisor.HDV_DOORBELL_FLAGS = 2
HDV_DOORBELL_FLAG_TRIGGER_SIZE_DWORD: win32more.Windows.Win32.System.Hypervisor.HDV_DOORBELL_FLAGS = 3
HDV_DOORBELL_FLAG_TRIGGER_SIZE_QWORD: win32more.Windows.Win32.System.Hypervisor.HDV_DOORBELL_FLAGS = 4
HDV_DOORBELL_FLAG_TRIGGER_ANY_VALUE: win32more.Windows.Win32.System.Hypervisor.HDV_DOORBELL_FLAGS = -2147483648
HDV_MMIO_MAPPING_FLAGS = Int32
HdvMmioMappingFlagNone: win32more.Windows.Win32.System.Hypervisor.HDV_MMIO_MAPPING_FLAGS = 0
HdvMmioMappingFlagWriteable: win32more.Windows.Win32.System.Hypervisor.HDV_MMIO_MAPPING_FLAGS = 1
HdvMmioMappingFlagExecutable: win32more.Windows.Win32.System.Hypervisor.HDV_MMIO_MAPPING_FLAGS = 2
HDV_PCI_BAR_SELECTOR = Int32
HDV_PCI_BAR0: win32more.Windows.Win32.System.Hypervisor.HDV_PCI_BAR_SELECTOR = 0
HDV_PCI_BAR1: win32more.Windows.Win32.System.Hypervisor.HDV_PCI_BAR_SELECTOR = 1
HDV_PCI_BAR2: win32more.Windows.Win32.System.Hypervisor.HDV_PCI_BAR_SELECTOR = 2
HDV_PCI_BAR3: win32more.Windows.Win32.System.Hypervisor.HDV_PCI_BAR_SELECTOR = 3
HDV_PCI_BAR4: win32more.Windows.Win32.System.Hypervisor.HDV_PCI_BAR_SELECTOR = 4
HDV_PCI_BAR5: win32more.Windows.Win32.System.Hypervisor.HDV_PCI_BAR_SELECTOR = 5
@winfunctype_pointer
def HDV_PCI_DEVICE_GET_DETAILS(deviceContext: VoidPtr, pnpId: POINTER(win32more.Windows.Win32.System.Hypervisor.HDV_PCI_PNP_ID), probedBarsCount: UInt32, probedBars: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def HDV_PCI_DEVICE_INITIALIZE(deviceContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class HDV_PCI_DEVICE_INTERFACE(Structure):
    Version: win32more.Windows.Win32.System.Hypervisor.HDV_PCI_INTERFACE_VERSION
    Initialize: win32more.Windows.Win32.System.Hypervisor.HDV_PCI_DEVICE_INITIALIZE
    Teardown: win32more.Windows.Win32.System.Hypervisor.HDV_PCI_DEVICE_TEARDOWN
    SetConfiguration: win32more.Windows.Win32.System.Hypervisor.HDV_PCI_DEVICE_SET_CONFIGURATION
    GetDetails: win32more.Windows.Win32.System.Hypervisor.HDV_PCI_DEVICE_GET_DETAILS
    Start: win32more.Windows.Win32.System.Hypervisor.HDV_PCI_DEVICE_START
    Stop: win32more.Windows.Win32.System.Hypervisor.HDV_PCI_DEVICE_STOP
    ReadConfigSpace: win32more.Windows.Win32.System.Hypervisor.HDV_PCI_READ_CONFIG_SPACE
    WriteConfigSpace: win32more.Windows.Win32.System.Hypervisor.HDV_PCI_WRITE_CONFIG_SPACE
    ReadInterceptedMemory: win32more.Windows.Win32.System.Hypervisor.HDV_PCI_READ_INTERCEPTED_MEMORY
    WriteInterceptedMemory: win32more.Windows.Win32.System.Hypervisor.HDV_PCI_WRITE_INTERCEPTED_MEMORY
@winfunctype_pointer
def HDV_PCI_DEVICE_SET_CONFIGURATION(deviceContext: VoidPtr, configurationValueCount: UInt32, configurationValues: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def HDV_PCI_DEVICE_START(deviceContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def HDV_PCI_DEVICE_STOP(deviceContext: VoidPtr) -> Void: ...
@winfunctype_pointer
def HDV_PCI_DEVICE_TEARDOWN(deviceContext: VoidPtr) -> Void: ...
HDV_PCI_INTERFACE_VERSION = Int32
HdvPciDeviceInterfaceVersionInvalid: win32more.Windows.Win32.System.Hypervisor.HDV_PCI_INTERFACE_VERSION = 0
HdvPciDeviceInterfaceVersion1: win32more.Windows.Win32.System.Hypervisor.HDV_PCI_INTERFACE_VERSION = 1
class HDV_PCI_PNP_ID(Structure):
    VendorID: UInt16
    DeviceID: UInt16
    RevisionID: Byte
    ProgIf: Byte
    SubClass: Byte
    BaseClass: Byte
    SubVendorID: UInt16
    SubSystemID: UInt16
@winfunctype_pointer
def HDV_PCI_READ_CONFIG_SPACE(deviceContext: VoidPtr, offset: UInt32, value: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def HDV_PCI_READ_INTERCEPTED_MEMORY(deviceContext: VoidPtr, barIndex: win32more.Windows.Win32.System.Hypervisor.HDV_PCI_BAR_SELECTOR, offset: UInt64, length: UInt64, value: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def HDV_PCI_WRITE_CONFIG_SPACE(deviceContext: VoidPtr, offset: UInt32, value: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def HDV_PCI_WRITE_INTERCEPTED_MEMORY(deviceContext: VoidPtr, barIndex: win32more.Windows.Win32.System.Hypervisor.HDV_PCI_BAR_SELECTOR, offset: UInt64, length: UInt64, value: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class HVSOCKET_ADDRESS_INFO(Structure):
    SystemId: Guid
    VirtualMachineId: Guid
    SiloId: Guid
    Flags: UInt32
class MODULE_INFO(Structure):
    ProcessImageName: win32more.Windows.Win32.Foundation.PSTR
    Image: win32more.Windows.Win32.System.Hypervisor.DOS_IMAGE_INFO
PAGING_MODE = Int32
Paging_Invalid: win32more.Windows.Win32.System.Hypervisor.PAGING_MODE = 0
Paging_NonPaged: win32more.Windows.Win32.System.Hypervisor.PAGING_MODE = 1
Paging_32Bit: win32more.Windows.Win32.System.Hypervisor.PAGING_MODE = 2
Paging_Pae: win32more.Windows.Win32.System.Hypervisor.PAGING_MODE = 3
Paging_Long: win32more.Windows.Win32.System.Hypervisor.PAGING_MODE = 4
Paging_Armv8: win32more.Windows.Win32.System.Hypervisor.PAGING_MODE = 5
REGISTER_ID = Int32
X64_RegisterRax: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 0
X64_RegisterRcx: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 1
X64_RegisterRdx: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 2
X64_RegisterRbx: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 3
X64_RegisterRsp: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 4
X64_RegisterRbp: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 5
X64_RegisterRsi: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 6
X64_RegisterRdi: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 7
X64_RegisterR8: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 8
X64_RegisterR9: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 9
X64_RegisterR10: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 10
X64_RegisterR11: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 11
X64_RegisterR12: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 12
X64_RegisterR13: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 13
X64_RegisterR14: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 14
X64_RegisterR15: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 15
X64_RegisterRip: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 16
X64_RegisterRFlags: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 17
X64_RegisterXmm0: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 18
X64_RegisterXmm1: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 19
X64_RegisterXmm2: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 20
X64_RegisterXmm3: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 21
X64_RegisterXmm4: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 22
X64_RegisterXmm5: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 23
X64_RegisterXmm6: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 24
X64_RegisterXmm7: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 25
X64_RegisterXmm8: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 26
X64_RegisterXmm9: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 27
X64_RegisterXmm10: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 28
X64_RegisterXmm11: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 29
X64_RegisterXmm12: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 30
X64_RegisterXmm13: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 31
X64_RegisterXmm14: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 32
X64_RegisterXmm15: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 33
X64_RegisterFpMmx0: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 34
X64_RegisterFpMmx1: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 35
X64_RegisterFpMmx2: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 36
X64_RegisterFpMmx3: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 37
X64_RegisterFpMmx4: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 38
X64_RegisterFpMmx5: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 39
X64_RegisterFpMmx6: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 40
X64_RegisterFpMmx7: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 41
X64_RegisterFpControlStatus: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 42
X64_RegisterXmmControlStatus: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 43
X64_RegisterCr0: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 44
X64_RegisterCr2: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 45
X64_RegisterCr3: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 46
X64_RegisterCr4: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 47
X64_RegisterCr8: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 48
X64_RegisterEfer: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 49
X64_RegisterDr0: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 50
X64_RegisterDr1: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 51
X64_RegisterDr2: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 52
X64_RegisterDr3: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 53
X64_RegisterDr6: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 54
X64_RegisterDr7: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 55
X64_RegisterEs: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 56
X64_RegisterCs: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 57
X64_RegisterSs: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 58
X64_RegisterDs: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 59
X64_RegisterFs: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 60
X64_RegisterGs: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 61
X64_RegisterLdtr: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 62
X64_RegisterTr: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 63
X64_RegisterIdtr: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 64
X64_RegisterGdtr: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 65
X64_RegisterMax: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 66
ARM64_RegisterX0: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 67
ARM64_RegisterX1: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 68
ARM64_RegisterX2: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 69
ARM64_RegisterX3: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 70
ARM64_RegisterX4: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 71
ARM64_RegisterX5: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 72
ARM64_RegisterX6: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 73
ARM64_RegisterX7: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 74
ARM64_RegisterX8: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 75
ARM64_RegisterX9: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 76
ARM64_RegisterX10: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 77
ARM64_RegisterX11: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 78
ARM64_RegisterX12: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 79
ARM64_RegisterX13: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 80
ARM64_RegisterX14: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 81
ARM64_RegisterX15: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 82
ARM64_RegisterX16: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 83
ARM64_RegisterX17: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 84
ARM64_RegisterX18: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 85
ARM64_RegisterX19: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 86
ARM64_RegisterX20: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 87
ARM64_RegisterX21: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 88
ARM64_RegisterX22: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 89
ARM64_RegisterX23: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 90
ARM64_RegisterX24: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 91
ARM64_RegisterX25: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 92
ARM64_RegisterX26: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 93
ARM64_RegisterX27: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 94
ARM64_RegisterX28: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 95
ARM64_RegisterXFp: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 96
ARM64_RegisterXLr: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 97
ARM64_RegisterPc: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 98
ARM64_RegisterSpEl0: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 99
ARM64_RegisterSpEl1: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 100
ARM64_RegisterCpsr: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 101
ARM64_RegisterQ0: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 102
ARM64_RegisterQ1: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 103
ARM64_RegisterQ2: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 104
ARM64_RegisterQ3: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 105
ARM64_RegisterQ4: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 106
ARM64_RegisterQ5: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 107
ARM64_RegisterQ6: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 108
ARM64_RegisterQ7: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 109
ARM64_RegisterQ8: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 110
ARM64_RegisterQ9: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 111
ARM64_RegisterQ10: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 112
ARM64_RegisterQ11: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 113
ARM64_RegisterQ12: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 114
ARM64_RegisterQ13: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 115
ARM64_RegisterQ14: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 116
ARM64_RegisterQ15: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 117
ARM64_RegisterQ16: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 118
ARM64_RegisterQ17: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 119
ARM64_RegisterQ18: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 120
ARM64_RegisterQ19: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 121
ARM64_RegisterQ20: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 122
ARM64_RegisterQ21: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 123
ARM64_RegisterQ22: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 124
ARM64_RegisterQ23: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 125
ARM64_RegisterQ24: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 126
ARM64_RegisterQ25: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 127
ARM64_RegisterQ26: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 128
ARM64_RegisterQ27: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 129
ARM64_RegisterQ28: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 130
ARM64_RegisterQ29: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 131
ARM64_RegisterQ30: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 132
ARM64_RegisterQ31: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 133
ARM64_RegisterFpStatus: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 134
ARM64_RegisterFpControl: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 135
ARM64_RegisterEsrEl1: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 136
ARM64_RegisterSpsrEl1: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 137
ARM64_RegisterFarEl1: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 138
ARM64_RegisterParEl1: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 139
ARM64_RegisterElrEl1: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 140
ARM64_RegisterTtbr0El1: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 141
ARM64_RegisterTtbr1El1: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 142
ARM64_RegisterVbarEl1: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 143
ARM64_RegisterSctlrEl1: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 144
ARM64_RegisterActlrEl1: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 145
ARM64_RegisterTcrEl1: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 146
ARM64_RegisterMairEl1: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 147
ARM64_RegisterAmairEl1: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 148
ARM64_RegisterTpidrEl0: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 149
ARM64_RegisterTpidrroEl0: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 150
ARM64_RegisterTpidrEl1: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 151
ARM64_RegisterContextIdrEl1: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 152
ARM64_RegisterCpacrEl1: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 153
ARM64_RegisterCsselrEl1: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 154
ARM64_RegisterCntkctlEl1: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 155
ARM64_RegisterCntvCvalEl0: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 156
ARM64_RegisterCntvCtlEl0: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 157
ARM64_RegisterMax: win32more.Windows.Win32.System.Hypervisor.REGISTER_ID = 158
class SOCKADDR_HV(Structure):
    Family: win32more.Windows.Win32.Networking.WinSock.ADDRESS_FAMILY
    Reserved: UInt16
    VmId: Guid
    ServiceId: Guid
VIRTUAL_PROCESSOR_ARCH = Int32
Arch_Unknown: win32more.Windows.Win32.System.Hypervisor.VIRTUAL_PROCESSOR_ARCH = 0
Arch_x86: win32more.Windows.Win32.System.Hypervisor.VIRTUAL_PROCESSOR_ARCH = 1
Arch_x64: win32more.Windows.Win32.System.Hypervisor.VIRTUAL_PROCESSOR_ARCH = 2
Arch_Armv8: win32more.Windows.Win32.System.Hypervisor.VIRTUAL_PROCESSOR_ARCH = 3
class VIRTUAL_PROCESSOR_REGISTER(Union):
    Reg64: UInt64
    Reg32: UInt32
    Reg16: UInt16
    Reg8: Byte
    Reg128: _Reg128_e__Struct
    X64: _X64_e__Union
    class _Reg128_e__Struct(Structure):
        Low64: UInt64
        High64: UInt64
    class _X64_e__Union(Union):
        Segment: _Segment_e__Struct
        Table: _Table_e__Struct
        FpControlStatus: _FpControlStatus_e__Struct
        XmmControlStatus: _XmmControlStatus_e__Struct
        class _Segment_e__Struct(Structure):
            Base: UInt64
            Limit: UInt32
            Selector: UInt16
            Anonymous: _Anonymous_e__Union
            _anonymous_ = ('Anonymous',)
            class _Anonymous_e__Union(Union):
                Attributes: UInt16
                Anonymous: _Anonymous_e__Struct
                _anonymous_ = ('Anonymous',)
                class _Anonymous_e__Struct(Structure):
                    SegmentType: Annotated[UInt16, NativeBitfieldAttribute(4)]
                    NonSystemSegment: Annotated[UInt16, NativeBitfieldAttribute(1)]
                    DescriptorPrivilegeLevel: Annotated[UInt16, NativeBitfieldAttribute(2)]
                    Present: Annotated[UInt16, NativeBitfieldAttribute(1)]
                    Reserved: Annotated[UInt16, NativeBitfieldAttribute(4)]
                    Available: Annotated[UInt16, NativeBitfieldAttribute(1)]
                    Long: Annotated[UInt16, NativeBitfieldAttribute(1)]
                    Default: Annotated[UInt16, NativeBitfieldAttribute(1)]
                    Granularity: Annotated[UInt16, NativeBitfieldAttribute(1)]
        class _Table_e__Struct(Structure):
            Limit: UInt16
            Base: UInt64
        class _FpControlStatus_e__Struct(Structure):
            FpControl: UInt16
            FpStatus: UInt16
            FpTag: Byte
            Reserved: Byte
            LastFpOp: UInt16
            Anonymous: _Anonymous_e__Union
            _anonymous_ = ('Anonymous',)
            class _Anonymous_e__Union(Union):
                LastFpRip: UInt64
                Anonymous: _Anonymous_e__Struct
                _anonymous_ = ('Anonymous',)
                class _Anonymous_e__Struct(Structure):
                    LastFpEip: UInt32
                    LastFpCs: UInt16
        class _XmmControlStatus_e__Struct(Structure):
            Anonymous: _Anonymous_e__Union
            XmmStatusControl: UInt32
            XmmStatusControlMask: UInt32
            _anonymous_ = ('Anonymous',)
            class _Anonymous_e__Union(Union):
                LastFpRdp: UInt64
                Anonymous: _Anonymous_e__Struct
                _anonymous_ = ('Anonymous',)
                class _Anonymous_e__Struct(Structure):
                    LastFpDp: UInt32
                    LastFpDs: UInt16
VIRTUAL_PROCESSOR_VENDOR = Int32
ProcessorVendor_Unknown: win32more.Windows.Win32.System.Hypervisor.VIRTUAL_PROCESSOR_VENDOR = 0
ProcessorVendor_Amd: win32more.Windows.Win32.System.Hypervisor.VIRTUAL_PROCESSOR_VENDOR = 1
ProcessorVendor_Intel: win32more.Windows.Win32.System.Hypervisor.VIRTUAL_PROCESSOR_VENDOR = 2
ProcessorVendor_Hygon: win32more.Windows.Win32.System.Hypervisor.VIRTUAL_PROCESSOR_VENDOR = 3
ProcessorVendor_Arm: win32more.Windows.Win32.System.Hypervisor.VIRTUAL_PROCESSOR_VENDOR = 4
class VM_GENCOUNTER(Structure):
    GenerationCount: UInt64
    GenerationCountHigh: UInt64
if ARCH in 'X64,ARM64':
    class WHV_ACCESS_GPA_CONTROLS(Union):
        AsUINT64: UInt64
        Anonymous: _Anonymous_e__Struct
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            CacheType: win32more.Windows.Win32.System.Hypervisor.WHV_CACHE_TYPE
            InputVtl: win32more.Windows.Win32.System.Hypervisor.WHV_INPUT_VTL
            Reserved: Byte
            Reserved1: UInt16
if ARCH in 'X64,ARM64':
    class WHV_ADVISE_GPA_RANGE(Union):
        Populate: win32more.Windows.Win32.System.Hypervisor.WHV_ADVISE_GPA_RANGE_POPULATE
if ARCH in 'X64,ARM64':
    WHV_ADVISE_GPA_RANGE_CODE = Int32
    WHvAdviseGpaRangeCodePopulate: win32more.Windows.Win32.System.Hypervisor.WHV_ADVISE_GPA_RANGE_CODE = 0
    WHvAdviseGpaRangeCodePin: win32more.Windows.Win32.System.Hypervisor.WHV_ADVISE_GPA_RANGE_CODE = 1
    WHvAdviseGpaRangeCodeUnpin: win32more.Windows.Win32.System.Hypervisor.WHV_ADVISE_GPA_RANGE_CODE = 2
if ARCH in 'X64,ARM64':
    class WHV_ADVISE_GPA_RANGE_POPULATE(Structure):
        Flags: win32more.Windows.Win32.System.Hypervisor.WHV_ADVISE_GPA_RANGE_POPULATE_FLAGS
        AccessType: win32more.Windows.Win32.System.Hypervisor.WHV_MEMORY_ACCESS_TYPE
if ARCH in 'X64,ARM64':
    class WHV_ADVISE_GPA_RANGE_POPULATE_FLAGS(Union):
        AsUINT32: UInt32
        Anonymous: _Anonymous_e__Struct
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            Prefetch: Annotated[UInt32, NativeBitfieldAttribute(1)]
            AvoidHardFaults: Annotated[UInt32, NativeBitfieldAttribute(1)]
            Reserved: Annotated[UInt32, NativeBitfieldAttribute(30)]
if ARCH in 'X64,ARM64':
    WHV_ALLOCATE_VPCI_RESOURCE_FLAGS = Int32
    WHvAllocateVpciResourceFlagNone: win32more.Windows.Win32.System.Hypervisor.WHV_ALLOCATE_VPCI_RESOURCE_FLAGS = 0
    WHvAllocateVpciResourceFlagAllowDirectP2P: win32more.Windows.Win32.System.Hypervisor.WHV_ALLOCATE_VPCI_RESOURCE_FLAGS = 1
if ARCH in 'ARM64':
    class WHV_ARM64_GLOBAL_INTERRUPT_CONTROLLER_STATE(Structure):
        Version: Byte
        GicVersion: Byte
        Reserved0: Byte * 2
        NumInterrupts: UInt32
        GicdCtlrEnableGrp1A: UInt64
        Interrupts: FlexibleArray[win32more.Windows.Win32.System.Hypervisor.WHV_ARM64_GLOBAL_INTERRUPT_STATE]
if ARCH in 'ARM64':
    class WHV_ARM64_GLOBAL_INTERRUPT_STATE(Structure):
        InterruptId: UInt32
        ActiveVpIndex: UInt32
        Anonymous: _Anonymous_e__Union
        InterruptState: win32more.Windows.Win32.System.Hypervisor.WHV_ARM64_INTERRUPT_STATE
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Union(Union):
            TargetMpidr: UInt32
            TargetVpIndex: UInt32
if ARCH in 'ARM64':
    class WHV_ARM64_HYPERCALL_CONTEXT(Structure):
        Header: win32more.Windows.Win32.System.Hypervisor.WHV_INTERCEPT_MESSAGE_HEADER
        Immediate: UInt16
        Reserved1: UInt16
        Reserved2: UInt32
        X: UInt64 * 18
if ARCH in 'ARM64':
    WHV_ARM64_IC_EMULATION_MODE = Int32
    WHvArm64IcEmulationModeNone: win32more.Windows.Win32.System.Hypervisor.WHV_ARM64_IC_EMULATION_MODE = 0
    WHvArm64IcEmulationModeGicV3: win32more.Windows.Win32.System.Hypervisor.WHV_ARM64_IC_EMULATION_MODE = 1
if ARCH in 'ARM64':
    class WHV_ARM64_IC_GIC_V3_PARAMETERS(Structure):
        GicdBaseAddress: UInt64
        GitsTranslaterBaseAddress: UInt64
        Reserved: UInt32
        GicLpiIntIdBits: UInt32
        GicPpiOverflowInterruptFromCntv: UInt32
        GicPpiPerformanceMonitorsInterrupt: UInt32
        Reserved1: UInt32 * 6
if ARCH in 'ARM64':
    class WHV_ARM64_IC_PARAMETERS(Structure):
        EmulationMode: win32more.Windows.Win32.System.Hypervisor.WHV_ARM64_IC_EMULATION_MODE
        Reserved: UInt32
        Anonymous: _Anonymous_e__Union
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Union(Union):
            GicV3Parameters: win32more.Windows.Win32.System.Hypervisor.WHV_ARM64_IC_GIC_V3_PARAMETERS
if ARCH in 'ARM64':
    class WHV_ARM64_INTERRUPT_STATE(Structure):
        Anonymous: _Anonymous_e__Struct
        GicrIpriorityrConfigured: Byte
        GicrIpriorityrActive: Byte
        Reserved1: Byte
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            Enabled: Annotated[Byte, NativeBitfieldAttribute(1)]
            EdgeTriggered: Annotated[Byte, NativeBitfieldAttribute(1)]
            Asserted: Annotated[Byte, NativeBitfieldAttribute(1)]
            SetPending: Annotated[Byte, NativeBitfieldAttribute(1)]
            Active: Annotated[Byte, NativeBitfieldAttribute(1)]
            Direct: Annotated[Byte, NativeBitfieldAttribute(1)]
            Reserved0: Annotated[Byte, NativeBitfieldAttribute(2)]
if ARCH in 'ARM64':
    class WHV_ARM64_LOCAL_INTERRUPT_CONTROLLER_STATE(Structure):
        Version: Byte
        GicVersion: Byte
        Reserved0: Byte * 6
        IccIgrpen1El1: UInt64
        GicrCtlrEnableLpis: UInt64
        IccBpr1El1: UInt64
        IccPmrEl1: UInt64
        GicrPropbaser: UInt64
        GicrPendbaser: UInt64
        IchAp1REl2: UInt32 * 4
        BankedInterruptState: win32more.Windows.Win32.System.Hypervisor.WHV_ARM64_INTERRUPT_STATE * 32
if ARCH in 'ARM64':
    class WHV_ARM64_PENDING_EVENT(Union):
        Anonymous1: _Anonymous1_e__Struct
        Anonymous2: _Anonymous2_e__Struct
        Exception: win32more.Windows.Win32.System.Hypervisor.WHV_ARM64_PENDING_EXCEPTION_EVENT
        SyntheticException: win32more.Windows.Win32.System.Hypervisor.WHV_ARM64_PENDING_SYNTHETIC_EXCEPTION_EVENT
        _anonymous_ = ('Anonymous1', 'Anonymous2')
        class _Anonymous1_e__Struct(Structure):
            Reg0: win32more.Windows.Win32.System.Hypervisor.WHV_UINT128
            Reg1: win32more.Windows.Win32.System.Hypervisor.WHV_UINT128
        class _Anonymous2_e__Struct(Structure):
            EventPending: Annotated[Byte, NativeBitfieldAttribute(1)]
            EventType: Annotated[Byte, NativeBitfieldAttribute(3)]
            Reserved: Annotated[Byte, NativeBitfieldAttribute(4)]
            EventData: Byte * 15
if ARCH in 'ARM64':
    WHV_ARM64_PENDING_EVENT_TYPE = Int32
    WHvArm64PendingEventException: win32more.Windows.Win32.System.Hypervisor.WHV_ARM64_PENDING_EVENT_TYPE = 0
    WHvArm64PendingEventSyntheticException: win32more.Windows.Win32.System.Hypervisor.WHV_ARM64_PENDING_EVENT_TYPE = 1
if ARCH in 'ARM64':
    class WHV_ARM64_PENDING_EXCEPTION_EVENT(Union):
        AsUINT64: UInt64 * 3
        Anonymous: _Anonymous_e__Struct
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            EventPending: Annotated[Byte, NativeBitfieldAttribute(1)]
            EventType: Annotated[Byte, NativeBitfieldAttribute(3)]
            Reserved: Annotated[Byte, NativeBitfieldAttribute(4)]
            Reserved1: Byte
            Reserved2: UInt16
            Reserved3: UInt32
            EsrElx: UInt64
            FarElx: UInt64
if ARCH in 'ARM64':
    class WHV_ARM64_PENDING_SYNTHETIC_EXCEPTION_EVENT(Union):
        AsUINT64: UInt64 * 2
        Anonymous: _Anonymous_e__Struct
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            EventPending: Annotated[Byte, NativeBitfieldAttribute(1)]
            EventType: Annotated[Byte, NativeBitfieldAttribute(3)]
            Reserved: Annotated[Byte, NativeBitfieldAttribute(4)]
            Reserved1: Byte
            Reserved2: UInt16
            ExceptionType: UInt32
            Context: UInt64
if ARCH in 'ARM64':
    class WHV_ARM64_PROCESSOR_FEATURES(Union):
        Anonymous: _Anonymous_e__Struct
        AsUINT64: UInt64
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            Asid16: Annotated[UInt64, NativeBitfieldAttribute(1)]
            TGran16: Annotated[UInt64, NativeBitfieldAttribute(1)]
            TGran64: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Haf: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Hdbs: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Pan: Annotated[UInt64, NativeBitfieldAttribute(1)]
            AtS1E1: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Uao: Annotated[UInt64, NativeBitfieldAttribute(1)]
            El0Aarch32: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Fp: Annotated[UInt64, NativeBitfieldAttribute(1)]
            FpHp: Annotated[UInt64, NativeBitfieldAttribute(1)]
            AdvSimd: Annotated[UInt64, NativeBitfieldAttribute(1)]
            AdvSimdHp: Annotated[UInt64, NativeBitfieldAttribute(1)]
            GicV3V4: Annotated[UInt64, NativeBitfieldAttribute(1)]
            GicV41: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Ras: Annotated[UInt64, NativeBitfieldAttribute(1)]
            PmuV3: Annotated[UInt64, NativeBitfieldAttribute(1)]
            PmuV3ArmV81: Annotated[UInt64, NativeBitfieldAttribute(1)]
            PmuV3ArmV84: Annotated[UInt64, NativeBitfieldAttribute(1)]
            PmuV3ArmV85: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Aes: Annotated[UInt64, NativeBitfieldAttribute(1)]
            PolyMul: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Sha1: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Sha256: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Sha512: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Crc32: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Atomic: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Rdm: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Sha3: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Sm3: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Sm4: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Dp: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Fhm: Annotated[UInt64, NativeBitfieldAttribute(1)]
            DcCvap: Annotated[UInt64, NativeBitfieldAttribute(1)]
            DcCvadp: Annotated[UInt64, NativeBitfieldAttribute(1)]
            ApaBase: Annotated[UInt64, NativeBitfieldAttribute(1)]
            ApaEp: Annotated[UInt64, NativeBitfieldAttribute(1)]
            ApaEp2: Annotated[UInt64, NativeBitfieldAttribute(1)]
            ApaEp2Fp: Annotated[UInt64, NativeBitfieldAttribute(1)]
            ApaEp2Fpc: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Jscvt: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Fcma: Annotated[UInt64, NativeBitfieldAttribute(1)]
            RcpcV83: Annotated[UInt64, NativeBitfieldAttribute(1)]
            RcpcV84: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Gpa: Annotated[UInt64, NativeBitfieldAttribute(1)]
            L1ipPipt: Annotated[UInt64, NativeBitfieldAttribute(1)]
            DzPermitted: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Ssbs: Annotated[UInt64, NativeBitfieldAttribute(1)]
            SsbsRw: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved49: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved50: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved51: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved52: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Csv2: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Csv3: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Sb: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Idc: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Dic: Annotated[UInt64, NativeBitfieldAttribute(1)]
            TlbiOs: Annotated[UInt64, NativeBitfieldAttribute(1)]
            TlbiOsRange: Annotated[UInt64, NativeBitfieldAttribute(1)]
            FlagsM: Annotated[UInt64, NativeBitfieldAttribute(1)]
            FlagsM2: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Bf16: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Ebf16: Annotated[UInt64, NativeBitfieldAttribute(1)]
if ARCH in 'ARM64':
    class WHV_ARM64_PROCESSOR_FEATURES1(Union):
        Anonymous: _Anonymous_e__Struct
        AsUINT64: UInt64
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            SveBf16: Annotated[UInt64, NativeBitfieldAttribute(1)]
            SveEbf16: Annotated[UInt64, NativeBitfieldAttribute(1)]
            I8mm: Annotated[UInt64, NativeBitfieldAttribute(1)]
            SveI8mm: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Frintts: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Specres: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved6: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Rpres: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Exs: Annotated[UInt64, NativeBitfieldAttribute(1)]
            SpecSei: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Ets: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Afp: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Iesb: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Rng: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Lse2: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Idst: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved16: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved17: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved18: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved19: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved20: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved21: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Ccidx: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved23: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved24: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Ecv: Annotated[UInt64, NativeBitfieldAttribute(1)]
            EcvPoff: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved27: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved28: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved29: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved30: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved31: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved32: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved33: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved34: Annotated[UInt64, NativeBitfieldAttribute(1)]
            TtCnp: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Hpds: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Sve: Annotated[UInt64, NativeBitfieldAttribute(1)]
            SveV2: Annotated[UInt64, NativeBitfieldAttribute(1)]
            SveV2P1: Annotated[UInt64, NativeBitfieldAttribute(1)]
            SpecFpacc: Annotated[UInt64, NativeBitfieldAttribute(1)]
            SveAes: Annotated[UInt64, NativeBitfieldAttribute(1)]
            SveBitPerm: Annotated[UInt64, NativeBitfieldAttribute(1)]
            SveSha3: Annotated[UInt64, NativeBitfieldAttribute(1)]
            SveSm4: Annotated[UInt64, NativeBitfieldAttribute(1)]
            E0PD: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Gpa3: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Apa3Base: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Apa3Ep: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Apa3Ep2: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Apa3Ep2Fp: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Apa3Ep2Fpc: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Lrcpc3: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Sme: Annotated[UInt64, NativeBitfieldAttribute(1)]
            SmeF32F32: Annotated[UInt64, NativeBitfieldAttribute(1)]
            SmeB16F32: Annotated[UInt64, NativeBitfieldAttribute(1)]
            SmeF16F32: Annotated[UInt64, NativeBitfieldAttribute(1)]
            SmeI8I32: Annotated[UInt64, NativeBitfieldAttribute(1)]
            SmeF64F64: Annotated[UInt64, NativeBitfieldAttribute(1)]
            SmeI16I64: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved: Annotated[UInt64, NativeBitfieldAttribute(4)]
if ARCH in 'ARM64':
    class WHV_ARM64_RESET_CONTEXT(Structure):
        Header: win32more.Windows.Win32.System.Hypervisor.WHV_INTERCEPT_MESSAGE_HEADER
        ResetType: win32more.Windows.Win32.System.Hypervisor.WHV_ARM64_RESET_TYPE
        Reserved: UInt32
if ARCH in 'ARM64':
    WHV_ARM64_RESET_TYPE = Int32
    WHvArm64ResetTypePowerOff: win32more.Windows.Win32.System.Hypervisor.WHV_ARM64_RESET_TYPE = 0
    WHvArm64ResetTypeReboot: win32more.Windows.Win32.System.Hypervisor.WHV_ARM64_RESET_TYPE = 1
if ARCH in 'ARM64':
    WHV_ARM64_SYNTHETIC_EXCEPTION_TYPE = Int32
    WHvArm64SyntheticExceptionTypeSmc: win32more.Windows.Win32.System.Hypervisor.WHV_ARM64_SYNTHETIC_EXCEPTION_TYPE = 0
    WHvArm64SyntheticExceptionTypeSecure: win32more.Windows.Win32.System.Hypervisor.WHV_ARM64_SYNTHETIC_EXCEPTION_TYPE = 1
    WHvArm64SyntheticExceptionTypeCrashdump: win32more.Windows.Win32.System.Hypervisor.WHV_ARM64_SYNTHETIC_EXCEPTION_TYPE = 2
    WHvArm64SyntheticExceptionTypeVirtualizationFault: win32more.Windows.Win32.System.Hypervisor.WHV_ARM64_SYNTHETIC_EXCEPTION_TYPE = 3
    WHvArm64SyntheticExceptionTypeMax: win32more.Windows.Win32.System.Hypervisor.WHV_ARM64_SYNTHETIC_EXCEPTION_TYPE = 64
if ARCH in 'ARM64':
    class WHV_ARM64_VP_STATE_SME(Structure):
        Version: UInt16
        RegisterDataOffset: UInt16
        StreamingVectorLength: UInt32
        Reserved0: UInt64
if ARCH in 'ARM64':
    class WHV_ARM64_VP_STATE_SVE(Structure):
        Version: UInt16
        RegisterDataOffset: UInt16
        VectorLength: UInt32
        Reserved0: UInt64
if ARCH in 'ARM64':
    WHV_CACHE_TYPE = Int32
    WHvCacheTypeUncached: win32more.Windows.Win32.System.Hypervisor.WHV_CACHE_TYPE = 0
    WHvCacheTypeWriteCombining: win32more.Windows.Win32.System.Hypervisor.WHV_CACHE_TYPE = 1
    WHvCacheTypeWriteThrough: win32more.Windows.Win32.System.Hypervisor.WHV_CACHE_TYPE = 4
    WHvCacheTypeWriteBack: win32more.Windows.Win32.System.Hypervisor.WHV_CACHE_TYPE = 6
elif ARCH in 'X64':
    WHV_CACHE_TYPE = Int32
    WHvCacheTypeUncached: win32more.Windows.Win32.System.Hypervisor.WHV_CACHE_TYPE = 0
    WHvCacheTypeWriteCombining: win32more.Windows.Win32.System.Hypervisor.WHV_CACHE_TYPE = 1
    WHvCacheTypeWriteThrough: win32more.Windows.Win32.System.Hypervisor.WHV_CACHE_TYPE = 4
    WHvCacheTypeWriteProtected: win32more.Windows.Win32.System.Hypervisor.WHV_CACHE_TYPE = 5
    WHvCacheTypeWriteBack: win32more.Windows.Win32.System.Hypervisor.WHV_CACHE_TYPE = 6
if ARCH in 'ARM64':
    class WHV_CAPABILITY(Union):
        HypervisorPresent: win32more.Windows.Win32.Foundation.BOOL
        Features: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_FEATURES
        ExtendedVmExits: win32more.Windows.Win32.System.Hypervisor.WHV_EXTENDED_VM_EXITS
        ProcessorVendor: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_VENDOR
        ProcessorFeatures: win32more.Windows.Win32.System.Hypervisor.WHV_ARM64_PROCESSOR_FEATURES
        SyntheticProcessorFeaturesBanks: win32more.Windows.Win32.System.Hypervisor.WHV_SYNTHETIC_PROCESSOR_FEATURES_BANKS
        ProcessorClFlushSize: Byte
        ProcessorClockFrequency: UInt64
        ProcessorFeaturesBanks: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_FEATURES_BANKS
        GpaRangePopulateFlags: win32more.Windows.Win32.System.Hypervisor.WHV_ADVISE_GPA_RANGE_POPULATE_FLAGS
        ProcessorFrequencyCap: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_PROCESSOR_FREQUENCY_CAP
        SchedulerFeatures: win32more.Windows.Win32.System.Hypervisor.WHV_SCHEDULER_FEATURES
        PhysicalAddressWidth: UInt32
        NestedFeatureRegister: UInt64
        GicLpiIntIdBits: UInt32
        MaxSveVectorLength: UInt32
        MaxSmeStreamingVectorLength: UInt32
elif ARCH in 'X64':
    class WHV_CAPABILITY(Union):
        HypervisorPresent: win32more.Windows.Win32.Foundation.BOOL
        Features: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_FEATURES
        ExtendedVmExits: win32more.Windows.Win32.System.Hypervisor.WHV_EXTENDED_VM_EXITS
        ProcessorVendor: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_VENDOR
        ProcessorFeatures: win32more.Windows.Win32.System.Hypervisor.WHV_X64_PROCESSOR_FEATURES
        SyntheticProcessorFeaturesBanks: win32more.Windows.Win32.System.Hypervisor.WHV_SYNTHETIC_PROCESSOR_FEATURES_BANKS
        ProcessorClFlushSize: Byte
        ProcessorClockFrequency: UInt64
        ProcessorFeaturesBanks: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_FEATURES_BANKS
        GpaRangePopulateFlags: win32more.Windows.Win32.System.Hypervisor.WHV_ADVISE_GPA_RANGE_POPULATE_FLAGS
        ProcessorFrequencyCap: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_PROCESSOR_FREQUENCY_CAP
        SchedulerFeatures: win32more.Windows.Win32.System.Hypervisor.WHV_SCHEDULER_FEATURES
        PhysicalAddressWidth: UInt32
        NestedFeatureRegister: UInt64
        ProcessorXsaveFeatures: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_XSAVE_FEATURES
        InterruptClockFrequency: UInt64
        ProcessorPerfmonFeatures: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_PERFMON_FEATURES
        X64MsrExitBitmap: win32more.Windows.Win32.System.Hypervisor.WHV_X64_MSR_EXIT_BITMAP
        ExceptionExitBitmap: UInt64
if ARCH in 'ARM64':
    WHV_CAPABILITY_CODE = Int32
    WHvCapabilityCodeHypervisorPresent: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 0
    WHvCapabilityCodeFeatures: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 1
    WHvCapabilityCodeExtendedVmExits: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 2
    WHvCapabilityCodeGpaRangePopulateFlags: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 5
    WHvCapabilityCodeSchedulerFeatures: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 6
    WHvCapabilityCodeProcessorVendor: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 4096
    WHvCapabilityCodeProcessorFeatures: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 4097
    WHvCapabilityCodeProcessorClFlushSize: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 4098
    WHvCapabilityCodeProcessorClockFrequency: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 4100
    WHvCapabilityCodeProcessorFeaturesBanks: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 4102
    WHvCapabilityCodeProcessorFrequencyCap: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 4103
    WHvCapabilityCodeSyntheticProcessorFeaturesBanks: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 4104
    WHvCapabilityCodePhysicalAddressWidth: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 4106
    WHvCapabilityCodeGicLpiIntIdBits: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 8209
    WHvCapabilityCodeMaxSveVectorLength: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 8210
    WHvCapabilityCodeMaxSmeStreamingVectorLength: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 8211
elif ARCH in 'X64':
    WHV_CAPABILITY_CODE = Int32
    WHvCapabilityCodeHypervisorPresent: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 0
    WHvCapabilityCodeFeatures: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 1
    WHvCapabilityCodeExtendedVmExits: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 2
    WHvCapabilityCodeExceptionExitBitmap: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 3
    WHvCapabilityCodeX64MsrExitBitmap: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 4
    WHvCapabilityCodeGpaRangePopulateFlags: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 5
    WHvCapabilityCodeSchedulerFeatures: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 6
    WHvCapabilityCodeProcessorVendor: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 4096
    WHvCapabilityCodeProcessorFeatures: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 4097
    WHvCapabilityCodeProcessorClFlushSize: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 4098
    WHvCapabilityCodeProcessorXsaveFeatures: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 4099
    WHvCapabilityCodeProcessorClockFrequency: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 4100
    WHvCapabilityCodeInterruptClockFrequency: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 4101
    WHvCapabilityCodeProcessorFeaturesBanks: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 4102
    WHvCapabilityCodeProcessorFrequencyCap: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 4103
    WHvCapabilityCodeSyntheticProcessorFeaturesBanks: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 4104
    WHvCapabilityCodeProcessorPerfmonFeatures: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 4105
    WHvCapabilityCodePhysicalAddressWidth: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 4106
    WHvCapabilityCodeVmxBasic: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 8192
    WHvCapabilityCodeVmxPinbasedCtls: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 8193
    WHvCapabilityCodeVmxProcbasedCtls: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 8194
    WHvCapabilityCodeVmxExitCtls: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 8195
    WHvCapabilityCodeVmxEntryCtls: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 8196
    WHvCapabilityCodeVmxMisc: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 8197
    WHvCapabilityCodeVmxCr0Fixed0: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 8198
    WHvCapabilityCodeVmxCr0Fixed1: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 8199
    WHvCapabilityCodeVmxCr4Fixed0: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 8200
    WHvCapabilityCodeVmxCr4Fixed1: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 8201
    WHvCapabilityCodeVmxVmcsEnum: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 8202
    WHvCapabilityCodeVmxProcbasedCtls2: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 8203
    WHvCapabilityCodeVmxEptVpidCap: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 8204
    WHvCapabilityCodeVmxTruePinbasedCtls: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 8205
    WHvCapabilityCodeVmxTrueProcbasedCtls: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 8206
    WHvCapabilityCodeVmxTrueExitCtls: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 8207
    WHvCapabilityCodeVmxTrueEntryCtls: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 8208
if ARCH in 'X64,ARM64':
    class WHV_CAPABILITY_FEATURES(Union):
        Anonymous: _Anonymous_e__Struct
        AsUINT64: UInt64
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            PartialUnmap: Annotated[UInt64, NativeBitfieldAttribute(1)]
            LocalApicEmulation: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Xsave: Annotated[UInt64, NativeBitfieldAttribute(1)]
            DirtyPageTracking: Annotated[UInt64, NativeBitfieldAttribute(1)]
            SpeculationControl: Annotated[UInt64, NativeBitfieldAttribute(1)]
            ApicRemoteRead: Annotated[UInt64, NativeBitfieldAttribute(1)]
            IdleSuspend: Annotated[UInt64, NativeBitfieldAttribute(1)]
            VirtualPciDeviceSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            IommuSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            VpHotAddRemove: Annotated[UInt64, NativeBitfieldAttribute(1)]
            DeviceAccessTracking: Annotated[UInt64, NativeBitfieldAttribute(1)]
            ReservedX640: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved: Annotated[UInt64, NativeBitfieldAttribute(52)]
if ARCH in 'X64,ARM64':
    class WHV_CAPABILITY_PROCESSOR_FREQUENCY_CAP(Structure):
        IsSupported: Annotated[UInt32, NativeBitfieldAttribute(1)]
        Reserved: Annotated[UInt32, NativeBitfieldAttribute(31)]
        HighestFrequencyMhz: UInt32
        NominalFrequencyMhz: UInt32
        LowestFrequencyMhz: UInt32
        FrequencyStepMhz: UInt32
if ARCH in 'X64':
    class WHV_CPUID_OUTPUT(Structure):
        Eax: UInt32
        Ebx: UInt32
        Ecx: UInt32
        Edx: UInt32
if ARCH in 'X64,ARM64':
    WHV_CREATE_VPCI_DEVICE_FLAGS = Int32
    WHvCreateVpciDeviceFlagNone: win32more.Windows.Win32.System.Hypervisor.WHV_CREATE_VPCI_DEVICE_FLAGS = 0
    WHvCreateVpciDeviceFlagPhysicallyBacked: win32more.Windows.Win32.System.Hypervisor.WHV_CREATE_VPCI_DEVICE_FLAGS = 1
    WHvCreateVpciDeviceFlagUseLogicalInterrupts: win32more.Windows.Win32.System.Hypervisor.WHV_CREATE_VPCI_DEVICE_FLAGS = 2
if ARCH in 'X64,ARM64':
    class WHV_DELIVERABILITY_NOTIFICATIONS_REGISTER(Union):
        Anonymous: _Anonymous_e__Struct
        AsUINT64: UInt64
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            NmiNotification: Annotated[UInt64, NativeBitfieldAttribute(1)]
            InterruptNotification: Annotated[UInt64, NativeBitfieldAttribute(1)]
            InterruptPriority: Annotated[UInt64, NativeBitfieldAttribute(4)]
            Reserved: Annotated[UInt64, NativeBitfieldAttribute(42)]
            Sint: Annotated[UInt64, NativeBitfieldAttribute(16)]
if ARCH in 'X64,ARM64':
    class WHV_DISABLE_PARTITION_VTL_FLAGS(Union):
        AsUINT8: Byte
        Anonymous: _Anonymous_e__Struct
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            ScrubOnly: Annotated[Byte, NativeBitfieldAttribute(1)]
            Reserved: Annotated[Byte, NativeBitfieldAttribute(7)]
if ARCH in 'X64,ARM64':
    class WHV_DISABLE_VP_VTL_FLAGS(Union):
        AsUINT8: Byte
        Anonymous: _Anonymous_e__Struct
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            ScrubOnly: Annotated[Byte, NativeBitfieldAttribute(1)]
            Reserved: Annotated[Byte, NativeBitfieldAttribute(7)]
if ARCH in 'X64,ARM64':
    class WHV_DOORBELL_MATCH_DATA(Structure):
        GuestAddress: UInt64
        Value: UInt64
        Length: UInt32
        MatchOnValue: Annotated[UInt32, NativeBitfieldAttribute(1)]
        MatchOnLength: Annotated[UInt32, NativeBitfieldAttribute(1)]
        Reserved: Annotated[UInt32, NativeBitfieldAttribute(30)]
if ARCH in 'X64':
    class WHV_EMULATOR_CALLBACKS(Structure):
        Size: UInt32
        Reserved: UInt32
        WHvEmulatorIoPortCallback: win32more.Windows.Win32.System.Hypervisor.WHV_EMULATOR_IO_PORT_CALLBACK
        WHvEmulatorMemoryCallback: win32more.Windows.Win32.System.Hypervisor.WHV_EMULATOR_MEMORY_CALLBACK
        WHvEmulatorGetVirtualProcessorRegisters: win32more.Windows.Win32.System.Hypervisor.WHV_EMULATOR_GET_VIRTUAL_PROCESSOR_REGISTERS_CALLBACK
        WHvEmulatorSetVirtualProcessorRegisters: win32more.Windows.Win32.System.Hypervisor.WHV_EMULATOR_SET_VIRTUAL_PROCESSOR_REGISTERS_CALLBACK
        WHvEmulatorTranslateGvaPage: win32more.Windows.Win32.System.Hypervisor.WHV_EMULATOR_TRANSLATE_GVA_PAGE_CALLBACK
if ARCH in 'X64':
    @winfunctype_pointer
    def WHV_EMULATOR_GET_VIRTUAL_PROCESSOR_REGISTERS_CALLBACK(Context: VoidPtr, RegisterNames: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME), RegisterCount: UInt32, RegisterValues: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_VALUE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64':
    class WHV_EMULATOR_IO_ACCESS_INFO(Structure):
        Direction: Byte
        Port: UInt16
        AccessSize: UInt16
        Data: UInt32
if ARCH in 'X64':
    @winfunctype_pointer
    def WHV_EMULATOR_IO_PORT_CALLBACK(Context: VoidPtr, IoAccess: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_EMULATOR_IO_ACCESS_INFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64':
    class WHV_EMULATOR_MEMORY_ACCESS_INFO(Structure):
        GpaAddress: UInt64
        Direction: Byte
        AccessSize: Byte
        Data: Byte * 8
if ARCH in 'X64':
    @winfunctype_pointer
    def WHV_EMULATOR_MEMORY_CALLBACK(Context: VoidPtr, MemoryAccess: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_EMULATOR_MEMORY_ACCESS_INFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64':
    @winfunctype_pointer
    def WHV_EMULATOR_SET_VIRTUAL_PROCESSOR_REGISTERS_CALLBACK(Context: VoidPtr, RegisterNames: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME), RegisterCount: UInt32, RegisterValues: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_VALUE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64':
    class WHV_EMULATOR_STATUS(Union):
        Anonymous: _Anonymous_e__Struct
        AsUINT32: UInt32
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            EmulationSuccessful: Annotated[UInt32, NativeBitfieldAttribute(1)]
            InternalEmulationFailure: Annotated[UInt32, NativeBitfieldAttribute(1)]
            IoPortCallbackFailed: Annotated[UInt32, NativeBitfieldAttribute(1)]
            MemoryCallbackFailed: Annotated[UInt32, NativeBitfieldAttribute(1)]
            TranslateGvaPageCallbackFailed: Annotated[UInt32, NativeBitfieldAttribute(1)]
            TranslateGvaPageCallbackGpaIsNotAligned: Annotated[UInt32, NativeBitfieldAttribute(1)]
            GetVirtualProcessorRegistersCallbackFailed: Annotated[UInt32, NativeBitfieldAttribute(1)]
            SetVirtualProcessorRegistersCallbackFailed: Annotated[UInt32, NativeBitfieldAttribute(1)]
            InterruptCausedIntercept: Annotated[UInt32, NativeBitfieldAttribute(1)]
            GuestCannotBeFaulted: Annotated[UInt32, NativeBitfieldAttribute(1)]
            Reserved: Annotated[UInt32, NativeBitfieldAttribute(22)]
if ARCH in 'X64':
    @winfunctype_pointer
    def WHV_EMULATOR_TRANSLATE_GVA_PAGE_CALLBACK(Context: VoidPtr, Gva: UInt64, TranslateFlags: win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_FLAGS, TranslationResult: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_RESULT_CODE), Gpa: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    class WHV_ENABLE_PARTITION_VTL_FLAGS(Union):
        AsUINT8: Byte
        Anonymous: _Anonymous_e__Struct
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            EnableMbec: Annotated[Byte, NativeBitfieldAttribute(1)]
            EnableSupervisorShadowStack: Annotated[Byte, NativeBitfieldAttribute(1)]
            EnableHardwareHvpt: Annotated[Byte, NativeBitfieldAttribute(1)]
            Reserved: Annotated[Byte, NativeBitfieldAttribute(5)]
if ARCH in 'X64':
    WHV_EXCEPTION_TYPE = Int32
    WHvX64ExceptionTypeDivideErrorFault: win32more.Windows.Win32.System.Hypervisor.WHV_EXCEPTION_TYPE = 0
    WHvX64ExceptionTypeDebugTrapOrFault: win32more.Windows.Win32.System.Hypervisor.WHV_EXCEPTION_TYPE = 1
    WHvX64ExceptionTypeBreakpointTrap: win32more.Windows.Win32.System.Hypervisor.WHV_EXCEPTION_TYPE = 3
    WHvX64ExceptionTypeOverflowTrap: win32more.Windows.Win32.System.Hypervisor.WHV_EXCEPTION_TYPE = 4
    WHvX64ExceptionTypeBoundRangeFault: win32more.Windows.Win32.System.Hypervisor.WHV_EXCEPTION_TYPE = 5
    WHvX64ExceptionTypeInvalidOpcodeFault: win32more.Windows.Win32.System.Hypervisor.WHV_EXCEPTION_TYPE = 6
    WHvX64ExceptionTypeDeviceNotAvailableFault: win32more.Windows.Win32.System.Hypervisor.WHV_EXCEPTION_TYPE = 7
    WHvX64ExceptionTypeDoubleFaultAbort: win32more.Windows.Win32.System.Hypervisor.WHV_EXCEPTION_TYPE = 8
    WHvX64ExceptionTypeInvalidTaskStateSegmentFault: win32more.Windows.Win32.System.Hypervisor.WHV_EXCEPTION_TYPE = 10
    WHvX64ExceptionTypeSegmentNotPresentFault: win32more.Windows.Win32.System.Hypervisor.WHV_EXCEPTION_TYPE = 11
    WHvX64ExceptionTypeStackFault: win32more.Windows.Win32.System.Hypervisor.WHV_EXCEPTION_TYPE = 12
    WHvX64ExceptionTypeGeneralProtectionFault: win32more.Windows.Win32.System.Hypervisor.WHV_EXCEPTION_TYPE = 13
    WHvX64ExceptionTypePageFault: win32more.Windows.Win32.System.Hypervisor.WHV_EXCEPTION_TYPE = 14
    WHvX64ExceptionTypeFloatingPointErrorFault: win32more.Windows.Win32.System.Hypervisor.WHV_EXCEPTION_TYPE = 16
    WHvX64ExceptionTypeAlignmentCheckFault: win32more.Windows.Win32.System.Hypervisor.WHV_EXCEPTION_TYPE = 17
    WHvX64ExceptionTypeMachineCheckAbort: win32more.Windows.Win32.System.Hypervisor.WHV_EXCEPTION_TYPE = 18
    WHvX64ExceptionTypeSimdFloatingPointFault: win32more.Windows.Win32.System.Hypervisor.WHV_EXCEPTION_TYPE = 19
    WHvX64ExceptionTypeControlProtectionFault: win32more.Windows.Win32.System.Hypervisor.WHV_EXCEPTION_TYPE = 21
if ARCH in 'X64,ARM64':
    class WHV_EXTENDED_VM_EXITS(Union):
        Anonymous: _Anonymous_e__Struct
        AsUINT64: UInt64
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            X64CpuidExit: Annotated[UInt64, NativeBitfieldAttribute(1)]
            X64MsrExit: Annotated[UInt64, NativeBitfieldAttribute(1)]
            ExceptionExit: Annotated[UInt64, NativeBitfieldAttribute(1)]
            X64RdtscExit: Annotated[UInt64, NativeBitfieldAttribute(1)]
            X64ApicSmiExitTrap: Annotated[UInt64, NativeBitfieldAttribute(1)]
            HypercallExit: Annotated[UInt64, NativeBitfieldAttribute(1)]
            X64ApicInitSipiExitTrap: Annotated[UInt64, NativeBitfieldAttribute(1)]
            X64ApicWriteLint0ExitTrap: Annotated[UInt64, NativeBitfieldAttribute(1)]
            X64ApicWriteLint1ExitTrap: Annotated[UInt64, NativeBitfieldAttribute(1)]
            X64ApicWriteSvrExitTrap: Annotated[UInt64, NativeBitfieldAttribute(1)]
            UnknownSynicConnection: Annotated[UInt64, NativeBitfieldAttribute(1)]
            RetargetUnknownVpciDevice: Annotated[UInt64, NativeBitfieldAttribute(1)]
            X64ApicWriteLdrExitTrap: Annotated[UInt64, NativeBitfieldAttribute(1)]
            X64ApicWriteDfrExitTrap: Annotated[UInt64, NativeBitfieldAttribute(1)]
            GpaAccessFaultExit: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved: Annotated[UInt64, NativeBitfieldAttribute(49)]
if ARCH in 'ARM64':
    class WHV_INITIAL_VP_CONTEXT(Structure):
        Pc: UInt64
        Sp_ELh: UInt64
        SCTLR_EL1: UInt64
        MAIR_EL1: UInt64
        TCR_EL1: UInt64
        VBAR_EL1: UInt64
        TTBR0_EL1: UInt64
        TTBR1_EL1: UInt64
        X18: UInt64
elif ARCH in 'X64':
    class WHV_INITIAL_VP_CONTEXT(Structure):
        Rip: UInt64
        Rsp: UInt64
        Rflags: UInt64
        Cs: win32more.Windows.Win32.System.Hypervisor.WHV_X64_SEGMENT_REGISTER
        Ds: win32more.Windows.Win32.System.Hypervisor.WHV_X64_SEGMENT_REGISTER
        Es: win32more.Windows.Win32.System.Hypervisor.WHV_X64_SEGMENT_REGISTER
        Fs: win32more.Windows.Win32.System.Hypervisor.WHV_X64_SEGMENT_REGISTER
        Gs: win32more.Windows.Win32.System.Hypervisor.WHV_X64_SEGMENT_REGISTER
        Ss: win32more.Windows.Win32.System.Hypervisor.WHV_X64_SEGMENT_REGISTER
        Tr: win32more.Windows.Win32.System.Hypervisor.WHV_X64_SEGMENT_REGISTER
        Ldtr: win32more.Windows.Win32.System.Hypervisor.WHV_X64_SEGMENT_REGISTER
        Idtr: win32more.Windows.Win32.System.Hypervisor.WHV_X64_TABLE_REGISTER
        Gdtr: win32more.Windows.Win32.System.Hypervisor.WHV_X64_TABLE_REGISTER
        Efer: UInt64
        Cr0: UInt64
        Cr3: UInt64
        Cr4: UInt64
        MsrCrPat: UInt64
if ARCH in 'X64,ARM64':
    class WHV_INPUT_VTL(Union):
        AsUINT8: Byte
        Anonymous: _Anonymous_e__Struct
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            TargetVtl: Annotated[Byte, NativeBitfieldAttribute(4)]
            UseTargetVtl: Annotated[Byte, NativeBitfieldAttribute(1)]
            Reserved: Annotated[Byte, NativeBitfieldAttribute(3)]
if ARCH in 'ARM64':
    class WHV_INTERCEPT_MESSAGE_HEADER(Structure):
        VpIndex: UInt32
        InstructionLength: Byte
        InterceptAccessType: Byte
        ExecutionState: win32more.Windows.Win32.System.Hypervisor.WHV_VP_EXECUTION_STATE
        Pc: UInt64
        Cpsr: UInt64
if ARCH in 'X64,ARM64':
    class WHV_INTERNAL_ACTIVITY_REGISTER(Union):
        Anonymous: _Anonymous_e__Struct
        AsUINT64: UInt64
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            StartupSuspend: Annotated[UInt64, NativeBitfieldAttribute(1)]
            HaltSuspend: Annotated[UInt64, NativeBitfieldAttribute(1)]
            IdleSuspend: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved: Annotated[UInt64, NativeBitfieldAttribute(61)]
if ARCH in 'ARM64':
    class WHV_INTERRUPT_CONTROL(Structure):
        TargetPartition: UInt64
        InterruptControl: win32more.Windows.Win32.System.Hypervisor.WHV_INTERRUPT_CONTROL2
        DestinationAddress: UInt64
        RequestedVector: UInt32
        TargetVtl: Byte
        ReservedZ0: Byte
        ReservedZ1: UInt16
elif ARCH in 'X64':
    class WHV_INTERRUPT_CONTROL(Structure):
        Type: Annotated[UInt64, NativeBitfieldAttribute(8)]
        DestinationMode: Annotated[UInt64, NativeBitfieldAttribute(4)]
        TriggerMode: Annotated[UInt64, NativeBitfieldAttribute(4)]
        TargetVtl: Annotated[UInt64, NativeBitfieldAttribute(8)]
        Reserved: Annotated[UInt64, NativeBitfieldAttribute(40)]
        Destination: UInt32
        Vector: UInt32
if ARCH in 'ARM64':
    class WHV_INTERRUPT_CONTROL2(Union):
        AsUINT64: UInt64
        Anonymous: _Anonymous_e__Struct
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            InterruptType: win32more.Windows.Win32.System.Hypervisor.WHV_INTERRUPT_TYPE
            Reserved1: Annotated[UInt32, NativeBitfieldAttribute(2)]
            Asserted: Annotated[UInt32, NativeBitfieldAttribute(1)]
            Retarget: Annotated[UInt32, NativeBitfieldAttribute(1)]
            Reserved2: Annotated[UInt32, NativeBitfieldAttribute(28)]
if ARCH in 'X64':
    WHV_INTERRUPT_DESTINATION_MODE = Int32
    WHvX64InterruptDestinationModePhysical: win32more.Windows.Win32.System.Hypervisor.WHV_INTERRUPT_DESTINATION_MODE = 0
    WHvX64InterruptDestinationModeLogical: win32more.Windows.Win32.System.Hypervisor.WHV_INTERRUPT_DESTINATION_MODE = 1
if ARCH in 'X64':
    WHV_INTERRUPT_TRIGGER_MODE = Int32
    WHvX64InterruptTriggerModeEdge: win32more.Windows.Win32.System.Hypervisor.WHV_INTERRUPT_TRIGGER_MODE = 0
    WHvX64InterruptTriggerModeLevel: win32more.Windows.Win32.System.Hypervisor.WHV_INTERRUPT_TRIGGER_MODE = 1
if ARCH in 'ARM64':
    WHV_INTERRUPT_TYPE = Int32
    WHvArm64InterruptTypeFixed: win32more.Windows.Win32.System.Hypervisor.WHV_INTERRUPT_TYPE = 0
    WHvArm64InterruptTypeMaximum: win32more.Windows.Win32.System.Hypervisor.WHV_INTERRUPT_TYPE = 8
elif ARCH in 'X64':
    WHV_INTERRUPT_TYPE = Int32
    WHvX64InterruptTypeFixed: win32more.Windows.Win32.System.Hypervisor.WHV_INTERRUPT_TYPE = 0
    WHvX64InterruptTypeLowestPriority: win32more.Windows.Win32.System.Hypervisor.WHV_INTERRUPT_TYPE = 1
    WHvX64InterruptTypeNmi: win32more.Windows.Win32.System.Hypervisor.WHV_INTERRUPT_TYPE = 4
    WHvX64InterruptTypeInit: win32more.Windows.Win32.System.Hypervisor.WHV_INTERRUPT_TYPE = 5
    WHvX64InterruptTypeSipi: win32more.Windows.Win32.System.Hypervisor.WHV_INTERRUPT_TYPE = 6
    WHvX64InterruptTypeLocalInt1: win32more.Windows.Win32.System.Hypervisor.WHV_INTERRUPT_TYPE = 9
if ARCH in 'ARM64':
    class WHV_INVALID_VP_REGISTER_CONTEXT(Structure):
        VpIndex: UInt32
        Reserved: UInt32
if ARCH in 'X64,ARM64':
    WHV_MAP_GPA_RANGE_FLAGS = Int32
    WHvMapGpaRangeFlagNone: win32more.Windows.Win32.System.Hypervisor.WHV_MAP_GPA_RANGE_FLAGS = 0
    WHvMapGpaRangeFlagRead: win32more.Windows.Win32.System.Hypervisor.WHV_MAP_GPA_RANGE_FLAGS = 1
    WHvMapGpaRangeFlagWrite: win32more.Windows.Win32.System.Hypervisor.WHV_MAP_GPA_RANGE_FLAGS = 2
    WHvMapGpaRangeFlagExecute: win32more.Windows.Win32.System.Hypervisor.WHV_MAP_GPA_RANGE_FLAGS = 4
    WHvMapGpaRangeFlagTrackDirtyPages: win32more.Windows.Win32.System.Hypervisor.WHV_MAP_GPA_RANGE_FLAGS = 8
if ARCH in 'ARM64':
    class WHV_MEMORY_ACCESS_CONTEXT(Structure):
        Header: win32more.Windows.Win32.System.Hypervisor.WHV_INTERCEPT_MESSAGE_HEADER
        Reserved0: UInt32
        InstructionByteCount: Byte
        AccessInfo: win32more.Windows.Win32.System.Hypervisor.WHV_MEMORY_ACCESS_INFO
        Reserved1: UInt16
        InstructionBytes: Byte * 4
        Reserved2: UInt32
        Gva: UInt64
        Gpa: UInt64
        Syndrome: UInt64
elif ARCH in 'X64':
    class WHV_MEMORY_ACCESS_CONTEXT(Structure):
        InstructionByteCount: Byte
        Reserved: Byte * 3
        InstructionBytes: Byte * 16
        AccessInfo: win32more.Windows.Win32.System.Hypervisor.WHV_MEMORY_ACCESS_INFO
        Gpa: UInt64
        Gva: UInt64
if ARCH in 'ARM64':
    class WHV_MEMORY_ACCESS_INFO(Union):
        AsUINT8: Byte
        Anonymous: _Anonymous_e__Struct
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            GvaValid: Annotated[Byte, NativeBitfieldAttribute(1)]
            GvaGpaValid: Annotated[Byte, NativeBitfieldAttribute(1)]
            HypercallOutputPending: Annotated[Byte, NativeBitfieldAttribute(1)]
            Reserved: Annotated[Byte, NativeBitfieldAttribute(5)]
elif ARCH in 'X64':
    class WHV_MEMORY_ACCESS_INFO(Union):
        Anonymous: _Anonymous_e__Struct
        AsUINT32: UInt32
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            AccessType: Annotated[UInt32, NativeBitfieldAttribute(2)]
            GpaUnmapped: Annotated[UInt32, NativeBitfieldAttribute(1)]
            GvaValid: Annotated[UInt32, NativeBitfieldAttribute(1)]
            Reserved: Annotated[UInt32, NativeBitfieldAttribute(28)]
if ARCH in 'X64,ARM64':
    WHV_MEMORY_ACCESS_TYPE = Int32
    WHvMemoryAccessRead: win32more.Windows.Win32.System.Hypervisor.WHV_MEMORY_ACCESS_TYPE = 0
    WHvMemoryAccessWrite: win32more.Windows.Win32.System.Hypervisor.WHV_MEMORY_ACCESS_TYPE = 1
    WHvMemoryAccessExecute: win32more.Windows.Win32.System.Hypervisor.WHV_MEMORY_ACCESS_TYPE = 2
if ARCH in 'X64,ARM64':
    class WHV_MEMORY_RANGE_ENTRY(Structure):
        GuestAddress: UInt64
        SizeInBytes: UInt64
if ARCH in 'X64':
    WHV_MSR_ACTION = Int32
    WHvMsrActionArchitectureDefault: win32more.Windows.Win32.System.Hypervisor.WHV_MSR_ACTION = 0
    WHvMsrActionIgnoreWriteReadZero: win32more.Windows.Win32.System.Hypervisor.WHV_MSR_ACTION = 1
    WHvMsrActionExit: win32more.Windows.Win32.System.Hypervisor.WHV_MSR_ACTION = 2
if ARCH in 'X64':
    class WHV_MSR_ACTION_ENTRY(Structure):
        Index: UInt32
        ReadAction: Byte
        WriteAction: Byte
        Reserved: UInt16
if ARCH in 'X64,ARM64':
    class WHV_NESTED_ENLIGHTENMENTS_CONTROL(Structure):
        Features: _Features_e__Union
        HypercallControls: _HypercallControls_e__Union
        class _Features_e__Union(Union):
            AsUINT32: UInt32
            Anonymous: _Anonymous_e__Struct
            _anonymous_ = ('Anonymous',)
            class _Anonymous_e__Struct(Structure):
                DirectHypercall: Annotated[UInt32, NativeBitfieldAttribute(1)]
                VirtualizationException: Annotated[UInt32, NativeBitfieldAttribute(1)]
                Reserved: Annotated[UInt32, NativeBitfieldAttribute(30)]
        class _HypercallControls_e__Union(Union):
            AsUINT32: UInt32
            Anonymous: _Anonymous_e__Struct
            _anonymous_ = ('Anonymous',)
            class _Anonymous_e__Struct(Structure):
                InterPartitionCommunication: Annotated[UInt32, NativeBitfieldAttribute(1)]
                Reserved: Annotated[UInt32, NativeBitfieldAttribute(31)]
if ARCH in 'X64,ARM64':
    WHV_NESTED_STATE_TYPE = Int32
    WHvNestedStateTypeVmx: win32more.Windows.Win32.System.Hypervisor.WHV_NESTED_STATE_TYPE = 0
    WHvNestedStateTypeSvm: win32more.Windows.Win32.System.Hypervisor.WHV_NESTED_STATE_TYPE = 1
if ARCH in 'X64,ARM64':
    class WHV_NOTIFICATION_PORT_PARAMETERS(Structure):
        NotificationPortType: win32more.Windows.Win32.System.Hypervisor.WHV_NOTIFICATION_PORT_TYPE
        Reserved: UInt16
        Reserved1: Byte
        ConnectionVtl: Byte
        Anonymous: _Anonymous_e__Union
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Union(Union):
            Doorbell: win32more.Windows.Win32.System.Hypervisor.WHV_DOORBELL_MATCH_DATA
            Event: _Event_e__Struct
            class _Event_e__Struct(Structure):
                ConnectionId: UInt32
if ARCH in 'X64,ARM64':
    WHV_NOTIFICATION_PORT_PROPERTY_CODE = Int32
    WHvNotificationPortPropertyPreferredTargetVp: win32more.Windows.Win32.System.Hypervisor.WHV_NOTIFICATION_PORT_PROPERTY_CODE = 1
    WHvNotificationPortPropertyPreferredTargetDuration: win32more.Windows.Win32.System.Hypervisor.WHV_NOTIFICATION_PORT_PROPERTY_CODE = 5
if ARCH in 'X64,ARM64':
    WHV_NOTIFICATION_PORT_TYPE = Int32
    WHvNotificationPortTypeEvent: win32more.Windows.Win32.System.Hypervisor.WHV_NOTIFICATION_PORT_TYPE = 2
    WHvNotificationPortTypeDoorbell: win32more.Windows.Win32.System.Hypervisor.WHV_NOTIFICATION_PORT_TYPE = 4
if ARCH in 'X64,ARM64':
    WHV_PARTITION_COUNTER_SET = Int32
    WHvPartitionCounterSetMemory: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_COUNTER_SET = 0
WHV_PARTITION_HANDLE = IntPtr
if ARCH in 'X64,ARM64':
    class WHV_PARTITION_MEMORY_COUNTERS(Structure):
        Mapped4KPageCount: UInt64
        Mapped2MPageCount: UInt64
        Mapped1GPageCount: UInt64
if ARCH in 'ARM64':
    class WHV_PARTITION_PROPERTY(Union):
        ExtendedVmExits: win32more.Windows.Win32.System.Hypervisor.WHV_EXTENDED_VM_EXITS
        ProcessorFeatures: win32more.Windows.Win32.System.Hypervisor.WHV_ARM64_PROCESSOR_FEATURES
        SyntheticProcessorFeaturesBanks: win32more.Windows.Win32.System.Hypervisor.WHV_SYNTHETIC_PROCESSOR_FEATURES_BANKS
        ProcessorClFlushSize: Byte
        ProcessorCount: UInt32
        SeparateSecurityDomain: win32more.Windows.Win32.Foundation.BOOL
        NestedVirtualization: win32more.Windows.Win32.Foundation.BOOL
        ProcessorClockFrequency: UInt64
        ProcessorFeaturesBanks: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_FEATURES_BANKS
        ReferenceTime: UInt64
        PrimaryNumaNode: UInt16
        CpuReserve: UInt32
        CpuCap: UInt32
        CpuWeight: UInt32
        CpuGroupId: UInt64
        ProcessorFrequencyCap: UInt32
        AllowDeviceAssignment: win32more.Windows.Win32.Foundation.BOOL
        DisableSmt: win32more.Windows.Win32.Foundation.BOOL
        PhysicalAddressWidth: UInt32
        Arm64IcParameters: win32more.Windows.Win32.System.Hypervisor.WHV_ARM64_IC_PARAMETERS
elif ARCH in 'X64':
    class WHV_PARTITION_PROPERTY(Union):
        ExtendedVmExits: win32more.Windows.Win32.System.Hypervisor.WHV_EXTENDED_VM_EXITS
        ProcessorFeatures: win32more.Windows.Win32.System.Hypervisor.WHV_X64_PROCESSOR_FEATURES
        SyntheticProcessorFeaturesBanks: win32more.Windows.Win32.System.Hypervisor.WHV_SYNTHETIC_PROCESSOR_FEATURES_BANKS
        ProcessorClFlushSize: Byte
        ProcessorCount: UInt32
        SeparateSecurityDomain: win32more.Windows.Win32.Foundation.BOOL
        NestedVirtualization: win32more.Windows.Win32.Foundation.BOOL
        ProcessorClockFrequency: UInt64
        ProcessorFeaturesBanks: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_FEATURES_BANKS
        ReferenceTime: UInt64
        PrimaryNumaNode: UInt16
        CpuReserve: UInt32
        CpuCap: UInt32
        CpuWeight: UInt32
        CpuGroupId: UInt64
        ProcessorFrequencyCap: UInt32
        AllowDeviceAssignment: win32more.Windows.Win32.Foundation.BOOL
        DisableSmt: win32more.Windows.Win32.Foundation.BOOL
        PhysicalAddressWidth: UInt32
        ProcessorXsaveFeatures: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_XSAVE_FEATURES
        CpuidExitList: UInt32 * 1
        ExceptionExitBitmap: UInt64
        ApicRemoteRead: win32more.Windows.Win32.Foundation.BOOL
        X64MsrExitBitmap: win32more.Windows.Win32.System.Hypervisor.WHV_X64_MSR_EXIT_BITMAP
        ProcessorPerfmonFeatures: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_PERFMON_FEATURES
        InterruptClockFrequency: UInt64
        CpuidResultList: win32more.Windows.Win32.System.Hypervisor.WHV_X64_CPUID_RESULT * 1
        CpuidResultList2: win32more.Windows.Win32.System.Hypervisor.WHV_X64_CPUID_RESULT2 * 1
        MsrActionList: win32more.Windows.Win32.System.Hypervisor.WHV_MSR_ACTION_ENTRY * 1
        UnimplementedMsrAction: win32more.Windows.Win32.System.Hypervisor.WHV_MSR_ACTION
        LocalApicEmulationMode: win32more.Windows.Win32.System.Hypervisor.WHV_X64_LOCAL_APIC_EMULATION_MODE
if ARCH in 'ARM64':
    WHV_PARTITION_PROPERTY_CODE = Int32
    WHvPartitionPropertyCodeExtendedVmExits: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 1
    WHvPartitionPropertyCodeSeparateSecurityDomain: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 3
    WHvPartitionPropertyCodeNestedVirtualization: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 4
    WHvPartitionPropertyCodePrimaryNumaNode: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 6
    WHvPartitionPropertyCodeCpuReserve: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 7
    WHvPartitionPropertyCodeCpuCap: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 8
    WHvPartitionPropertyCodeCpuWeight: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 9
    WHvPartitionPropertyCodeCpuGroupId: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 10
    WHvPartitionPropertyCodeProcessorFrequencyCap: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 11
    WHvPartitionPropertyCodeAllowDeviceAssignment: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 12
    WHvPartitionPropertyCodeDisableSmt: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 13
    WHvPartitionPropertyCodeProcessorFeatures: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 4097
    WHvPartitionPropertyCodeProcessorClFlushSize: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 4098
    WHvPartitionPropertyCodeProcessorClockFrequency: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 4103
    WHvPartitionPropertyCodeProcessorFeaturesBanks: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 4106
    WHvPartitionPropertyCodeReferenceTime: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 4107
    WHvPartitionPropertyCodeSyntheticProcessorFeaturesBanks: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 4108
    WHvPartitionPropertyCodePhysicalAddressWidth: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 4113
    WHvPartitionPropertyCodeArm64IcParameters: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 4114
    WHvPartitionPropertyCodeProcessorCount: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 8191
elif ARCH in 'X64':
    WHV_PARTITION_PROPERTY_CODE = Int32
    WHvPartitionPropertyCodeExtendedVmExits: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 1
    WHvPartitionPropertyCodeExceptionExitBitmap: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 2
    WHvPartitionPropertyCodeSeparateSecurityDomain: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 3
    WHvPartitionPropertyCodeNestedVirtualization: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 4
    WHvPartitionPropertyCodeX64MsrExitBitmap: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 5
    WHvPartitionPropertyCodePrimaryNumaNode: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 6
    WHvPartitionPropertyCodeCpuReserve: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 7
    WHvPartitionPropertyCodeCpuCap: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 8
    WHvPartitionPropertyCodeCpuWeight: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 9
    WHvPartitionPropertyCodeCpuGroupId: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 10
    WHvPartitionPropertyCodeProcessorFrequencyCap: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 11
    WHvPartitionPropertyCodeAllowDeviceAssignment: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 12
    WHvPartitionPropertyCodeDisableSmt: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 13
    WHvPartitionPropertyCodeProcessorFeatures: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 4097
    WHvPartitionPropertyCodeProcessorClFlushSize: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 4098
    WHvPartitionPropertyCodeCpuidExitList: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 4099
    WHvPartitionPropertyCodeCpuidResultList: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 4100
    WHvPartitionPropertyCodeLocalApicEmulationMode: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 4101
    WHvPartitionPropertyCodeProcessorXsaveFeatures: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 4102
    WHvPartitionPropertyCodeProcessorClockFrequency: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 4103
    WHvPartitionPropertyCodeInterruptClockFrequency: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 4104
    WHvPartitionPropertyCodeApicRemoteReadSupport: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 4105
    WHvPartitionPropertyCodeProcessorFeaturesBanks: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 4106
    WHvPartitionPropertyCodeReferenceTime: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 4107
    WHvPartitionPropertyCodeSyntheticProcessorFeaturesBanks: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 4108
    WHvPartitionPropertyCodeCpuidResultList2: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 4109
    WHvPartitionPropertyCodeProcessorPerfmonFeatures: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 4110
    WHvPartitionPropertyCodeMsrActionList: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 4111
    WHvPartitionPropertyCodeUnimplementedMsrAction: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 4112
    WHvPartitionPropertyCodePhysicalAddressWidth: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 4113
    WHvPartitionPropertyCodeProcessorCount: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 8191
if ARCH in 'X64':
    class WHV_PROCESSOR_APIC_COUNTERS(Structure):
        MmioAccessCount: UInt64
        EoiAccessCount: UInt64
        TprAccessCount: UInt64
        SentIpiCount: UInt64
        SelfIpiCount: UInt64
if ARCH in 'ARM64':
    WHV_PROCESSOR_COUNTER_SET = Int32
    WHvProcessorCounterSetRuntime: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_COUNTER_SET = 0
    WHvProcessorCounterSetIntercepts: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_COUNTER_SET = 1
    WHvProcessorCounterSetEvents: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_COUNTER_SET = 2
    WHvProcessorCounterSetSyntheticFeatures: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_COUNTER_SET = 4
elif ARCH in 'X64':
    WHV_PROCESSOR_COUNTER_SET = Int32
    WHvProcessorCounterSetRuntime: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_COUNTER_SET = 0
    WHvProcessorCounterSetIntercepts: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_COUNTER_SET = 1
    WHvProcessorCounterSetEvents: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_COUNTER_SET = 2
    WHvProcessorCounterSetApic: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_COUNTER_SET = 3
    WHvProcessorCounterSetSyntheticFeatures: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_COUNTER_SET = 4
if ARCH in 'X64,ARM64':
    class WHV_PROCESSOR_EVENT_COUNTERS(Structure):
        PageFaultCount: UInt64
        ExceptionCount: UInt64
        InterruptCount: UInt64
if ARCH in 'X64,ARM64':
    class WHV_PROCESSOR_FEATURES_BANKS(Structure):
        BanksCount: UInt32
        Reserved0: UInt32
        Anonymous: _Anonymous_e__Union
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Union(Union):
            Anonymous: _Anonymous_e__Struct
            AsUINT64: UInt64 * 2
            _anonymous_ = ('Anonymous',)
            class _Anonymous_e__Struct(Structure):
                Bank0: win32more.Windows.Win32.System.Hypervisor.WHV_X64_PROCESSOR_FEATURES
                Bank1: win32more.Windows.Win32.System.Hypervisor.WHV_X64_PROCESSOR_FEATURES1
if ARCH in 'X64,ARM64':
    class WHV_PROCESSOR_INTERCEPT_COUNTER(Structure):
        Count: UInt64
        Time100ns: UInt64
if ARCH in 'ARM64':
    class WHV_PROCESSOR_INTERCEPT_COUNTERS(Structure):
        OtherIntercepts: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER
        PendingInterrupts: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER
        NestedPageFaultIntercepts: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER
        Hypercalls: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER
        Reserved: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER * 10
elif ARCH in 'X64':
    class WHV_PROCESSOR_INTERCEPT_COUNTERS(Structure):
        PageInvalidations: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER
        ControlRegisterAccesses: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER
        IoInstructions: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER
        HaltInstructions: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER
        CpuidInstructions: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER
        MsrAccesses: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER
        OtherIntercepts: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER
        PendingInterrupts: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER
        EmulatedInstructions: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER
        DebugRegisterAccesses: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER
        PageFaultIntercepts: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER
        NestedPageFaultIntercepts: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER
        Hypercalls: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER
        RdpmcInstructions: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER
if ARCH in 'X64':
    class WHV_PROCESSOR_PERFMON_FEATURES(Union):
        Anonymous: _Anonymous_e__Struct
        AsUINT64: UInt64
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            PmuSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            LbrSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved: Annotated[UInt64, NativeBitfieldAttribute(62)]
if ARCH in 'X64,ARM64':
    class WHV_PROCESSOR_RUNTIME_COUNTERS(Structure):
        TotalRuntime100ns: UInt64
        HypervisorRuntime100ns: UInt64
if ARCH in 'X64,ARM64':
    class WHV_PROCESSOR_SYNTHETIC_FEATURES_COUNTERS(Structure):
        SyntheticInterruptsCount: UInt64
        LongSpinWaitHypercallsCount: UInt64
        OtherHypercallsCount: UInt64
        SyntheticInterruptHypercallsCount: UInt64
        VirtualInterruptHypercallsCount: UInt64
        VirtualMmuHypercallsCount: UInt64
if ARCH in 'X64,ARM64':
    WHV_PROCESSOR_VENDOR = Int32
    WHvProcessorVendorAmd: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_VENDOR = 0
    WHvProcessorVendorIntel: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_VENDOR = 1
    WHvProcessorVendorHygon: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_VENDOR = 2
    WHvProcessorVendorArm: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_VENDOR = 16
if ARCH in 'X64':
    class WHV_PROCESSOR_XSAVE_FEATURES(Union):
        Anonymous: _Anonymous_e__Struct
        AsUINT64: UInt64
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            XsaveSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            XsaveoptSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            AvxSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Avx2Support: Annotated[UInt64, NativeBitfieldAttribute(1)]
            FmaSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            MpxSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Avx512Support: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Avx512DQSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Avx512CDSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Avx512BWSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Avx512VLSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            XsaveCompSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            XsaveSupervisorSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Xcr1Support: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Avx512BitalgSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Avx512IfmaSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Avx512VBmiSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Avx512VBmi2Support: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Avx512VnniSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            GfniSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            VaesSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Avx512VPopcntdqSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            VpclmulqdqSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Avx512Bf16Support: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Avx512Vp2IntersectSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Avx512Fp16Support: Annotated[UInt64, NativeBitfieldAttribute(1)]
            XfdSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            AmxTileSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            AmxBf16Support: Annotated[UInt64, NativeBitfieldAttribute(1)]
            AmxInt8Support: Annotated[UInt64, NativeBitfieldAttribute(1)]
            AvxVnniSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            AvxIfmaSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            AvxNeConvertSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            AvxVnniInt8Support: Annotated[UInt64, NativeBitfieldAttribute(1)]
            AvxVnniInt16Support: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Avx10_1_256Support: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Avx10_1_512Support: Annotated[UInt64, NativeBitfieldAttribute(1)]
            AmxFp16Support: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved: Annotated[UInt64, NativeBitfieldAttribute(26)]
if ARCH in 'ARM64':
    class WHV_REGISTER_ACCESS_INFO(Union):
        SourceValue: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_VALUE
        DestinationRegister: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME
if ARCH in 'ARM64':
    class WHV_REGISTER_CONTEXT(Structure):
        Header: win32more.Windows.Win32.System.Hypervisor.WHV_INTERCEPT_MESSAGE_HEADER
        Anonymous: _Anonymous_e__Struct
        Reserved8: Byte
        Reserved16: UInt16
        RegisterName: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME
        AccessInfo: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_ACCESS_INFO
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            IsMemoryOp: Annotated[Byte, NativeBitfieldAttribute(1)]
            Reserved: Annotated[Byte, NativeBitfieldAttribute(7)]
if ARCH in 'ARM64':
    WHV_REGISTER_NAME = Int32
    WHvArm64RegisterX0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 131072
    WHvArm64RegisterX1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 131073
    WHvArm64RegisterX2: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 131074
    WHvArm64RegisterX3: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 131075
    WHvArm64RegisterX4: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 131076
    WHvArm64RegisterX5: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 131077
    WHvArm64RegisterX6: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 131078
    WHvArm64RegisterX7: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 131079
    WHvArm64RegisterX8: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 131080
    WHvArm64RegisterX9: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 131081
    WHvArm64RegisterX10: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 131082
    WHvArm64RegisterX11: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 131083
    WHvArm64RegisterX12: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 131084
    WHvArm64RegisterX13: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 131085
    WHvArm64RegisterX14: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 131086
    WHvArm64RegisterX15: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 131087
    WHvArm64RegisterX16: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 131088
    WHvArm64RegisterX17: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 131089
    WHvArm64RegisterX18: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 131090
    WHvArm64RegisterX19: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 131091
    WHvArm64RegisterX20: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 131092
    WHvArm64RegisterX21: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 131093
    WHvArm64RegisterX22: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 131094
    WHvArm64RegisterX23: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 131095
    WHvArm64RegisterX24: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 131096
    WHvArm64RegisterX25: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 131097
    WHvArm64RegisterX26: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 131098
    WHvArm64RegisterX27: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 131099
    WHvArm64RegisterX28: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 131100
    WHvArm64RegisterFp: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 131101
    WHvArm64RegisterLr: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 131102
    WHvArm64RegisterPc: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 131106
    WHvArm64RegisterQ0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 196608
    WHvArm64RegisterQ1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 196609
    WHvArm64RegisterQ2: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 196610
    WHvArm64RegisterQ3: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 196611
    WHvArm64RegisterQ4: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 196612
    WHvArm64RegisterQ5: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 196613
    WHvArm64RegisterQ6: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 196614
    WHvArm64RegisterQ7: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 196615
    WHvArm64RegisterQ8: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 196616
    WHvArm64RegisterQ9: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 196617
    WHvArm64RegisterQ10: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 196618
    WHvArm64RegisterQ11: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 196619
    WHvArm64RegisterQ12: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 196620
    WHvArm64RegisterQ13: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 196621
    WHvArm64RegisterQ14: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 196622
    WHvArm64RegisterQ15: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 196623
    WHvArm64RegisterQ16: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 196624
    WHvArm64RegisterQ17: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 196625
    WHvArm64RegisterQ18: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 196626
    WHvArm64RegisterQ19: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 196627
    WHvArm64RegisterQ20: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 196628
    WHvArm64RegisterQ21: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 196629
    WHvArm64RegisterQ22: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 196630
    WHvArm64RegisterQ23: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 196631
    WHvArm64RegisterQ24: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 196632
    WHvArm64RegisterQ25: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 196633
    WHvArm64RegisterQ26: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 196634
    WHvArm64RegisterQ27: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 196635
    WHvArm64RegisterQ28: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 196636
    WHvArm64RegisterQ29: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 196637
    WHvArm64RegisterQ30: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 196638
    WHvArm64RegisterQ31: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 196639
    WHvArm64RegisterPstate: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 131107
    WHvArm64RegisterElrEl1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 262165
    WHvArm64RegisterFpcr: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 262162
    WHvArm64RegisterFpsr: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 262163
    WHvArm64RegisterSp: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 131103
    WHvArm64RegisterSpEl0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 131104
    WHvArm64RegisterSpEl1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 131105
    WHvArm64RegisterSpsrEl1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 262164
    WHvArm64RegisterIdMidrEl1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139264
    WHvArm64RegisterIdRes01El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139265
    WHvArm64RegisterIdRes02El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139266
    WHvArm64RegisterIdRes03El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139267
    WHvArm64RegisterIdRes04El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139268
    WHvArm64RegisterIdMpidrEl1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139269
    WHvArm64RegisterIdRevidrEl1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139270
    WHvArm64RegisterIdRes07El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139271
    WHvArm64RegisterIdPfr0El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139272
    WHvArm64RegisterIdPfr1El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139273
    WHvArm64RegisterIdDfr0El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139274
    WHvArm64RegisterIdRes13El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139275
    WHvArm64RegisterIdMmfr0El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139276
    WHvArm64RegisterIdMmfr1El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139277
    WHvArm64RegisterIdMmfr2El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139278
    WHvArm64RegisterIdMmfr3El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139279
    WHvArm64RegisterIdIsar0El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139280
    WHvArm64RegisterIdIsar1El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139281
    WHvArm64RegisterIdIsar2El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139282
    WHvArm64RegisterIdIsar3El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139283
    WHvArm64RegisterIdIsar4El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139284
    WHvArm64RegisterIdIsar5El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139285
    WHvArm64RegisterIdRes26El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139286
    WHvArm64RegisterIdRes27El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139287
    WHvArm64RegisterIdMvfr0El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139288
    WHvArm64RegisterIdMvfr1El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139289
    WHvArm64RegisterIdMvfr2El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139290
    WHvArm64RegisterIdRes33El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139291
    WHvArm64RegisterIdPfr2El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139292
    WHvArm64RegisterIdRes35El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139293
    WHvArm64RegisterIdRes36El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139294
    WHvArm64RegisterIdRes37El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139295
    WHvArm64RegisterIdAa64Pfr0El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139296
    WHvArm64RegisterIdAa64Pfr1El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139297
    WHvArm64RegisterIdAa64Pfr2El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139298
    WHvArm64RegisterIdRes43El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139299
    WHvArm64RegisterIdAa64Zfr0El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139300
    WHvArm64RegisterIdAa64Smfr0El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139301
    WHvArm64RegisterIdRes46El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139302
    WHvArm64RegisterIdRes47El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139303
    WHvArm64RegisterIdAa64Dfr0El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139304
    WHvArm64RegisterIdAa64Dfr1El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139305
    WHvArm64RegisterIdRes52El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139306
    WHvArm64RegisterIdRes53El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139307
    WHvArm64RegisterIdRes54El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139308
    WHvArm64RegisterIdRes55El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139309
    WHvArm64RegisterIdRes56El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139310
    WHvArm64RegisterIdRes57El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139311
    WHvArm64RegisterIdAa64Isar0El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139312
    WHvArm64RegisterIdAa64Isar1El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139313
    WHvArm64RegisterIdAa64Isar2El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139314
    WHvArm64RegisterIdRes63El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139315
    WHvArm64RegisterIdRes64El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139316
    WHvArm64RegisterIdRes65El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139317
    WHvArm64RegisterIdRes66El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139318
    WHvArm64RegisterIdRes67El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139319
    WHvArm64RegisterIdAa64Mmfr0El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139320
    WHvArm64RegisterIdAa64Mmfr1El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139321
    WHvArm64RegisterIdAa64Mmfr2El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139322
    WHvArm64RegisterIdAa64Mmfr3El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139323
    WHvArm64RegisterIdAa64Mmfr4El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139324
    WHvArm64RegisterIdRes75El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139325
    WHvArm64RegisterIdRes76El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139326
    WHvArm64RegisterIdRes77El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139327
    WHvArm64RegisterIdRes80El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139328
    WHvArm64RegisterIdRes81El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139329
    WHvArm64RegisterIdRes82El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139330
    WHvArm64RegisterIdRes83El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139331
    WHvArm64RegisterIdRes84El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139332
    WHvArm64RegisterIdRes85El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139333
    WHvArm64RegisterIdRes86El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139334
    WHvArm64RegisterIdRes87El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139335
    WHvArm64RegisterIdRes90El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139336
    WHvArm64RegisterIdRes91El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139337
    WHvArm64RegisterIdRes92El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139338
    WHvArm64RegisterIdRes93El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139339
    WHvArm64RegisterIdRes94El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139340
    WHvArm64RegisterIdRes95El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139341
    WHvArm64RegisterIdRes96El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139342
    WHvArm64RegisterIdRes97El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139343
    WHvArm64RegisterIdRes100El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139344
    WHvArm64RegisterIdRes101El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139345
    WHvArm64RegisterIdRes102El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139346
    WHvArm64RegisterIdRes103El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139347
    WHvArm64RegisterIdRes104El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139348
    WHvArm64RegisterIdRes105El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139349
    WHvArm64RegisterIdRes106El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139350
    WHvArm64RegisterIdRes107El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139351
    WHvArm64RegisterIdRes110El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139352
    WHvArm64RegisterIdRes111El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139353
    WHvArm64RegisterIdRes112El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139354
    WHvArm64RegisterIdRes113El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139355
    WHvArm64RegisterIdRes114El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139356
    WHvArm64RegisterIdRes115El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139357
    WHvArm64RegisterIdRes116El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139358
    WHvArm64RegisterIdRes117El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139359
    WHvArm64RegisterIdRes120El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139360
    WHvArm64RegisterIdRes121El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139361
    WHvArm64RegisterIdRes122El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139362
    WHvArm64RegisterIdRes123El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139363
    WHvArm64RegisterIdRes124El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139364
    WHvArm64RegisterIdRes125El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139365
    WHvArm64RegisterIdRes126El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139366
    WHvArm64RegisterIdRes127El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139367
    WHvArm64RegisterIdRes130El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139368
    WHvArm64RegisterIdRes131El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139369
    WHvArm64RegisterIdRes132El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139370
    WHvArm64RegisterIdRes133El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139371
    WHvArm64RegisterIdRes134El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139372
    WHvArm64RegisterIdRes135El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139373
    WHvArm64RegisterIdRes136El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139374
    WHvArm64RegisterIdRes137El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139375
    WHvArm64RegisterIdRes140El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139376
    WHvArm64RegisterIdRes141El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139377
    WHvArm64RegisterIdRes142El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139378
    WHvArm64RegisterIdRes143El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139379
    WHvArm64RegisterIdRes144El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139380
    WHvArm64RegisterIdRes145El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139381
    WHvArm64RegisterIdRes146El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139382
    WHvArm64RegisterIdRes147El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139383
    WHvArm64RegisterIdRes150El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139384
    WHvArm64RegisterIdRes151El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139385
    WHvArm64RegisterIdRes152El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139386
    WHvArm64RegisterIdRes153El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139387
    WHvArm64RegisterIdRes154El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139388
    WHvArm64RegisterIdRes155El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139389
    WHvArm64RegisterIdRes156El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139390
    WHvArm64RegisterIdRes157El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 139391
    WHvArm64RegisterActlrEl1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 262147
    WHvArm64RegisterApdAKeyHiEl1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 262182
    WHvArm64RegisterApdAKeyLoEl1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 262183
    WHvArm64RegisterApdBKeyHiEl1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 262184
    WHvArm64RegisterApdBKeyLoEl1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 262185
    WHvArm64RegisterApgAKeyHiEl1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 262186
    WHvArm64RegisterApgAKeyLoEl1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 262187
    WHvArm64RegisterApiAKeyHiEl1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 262188
    WHvArm64RegisterApiAKeyLoEl1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 262189
    WHvArm64RegisterApiBKeyHiEl1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 262190
    WHvArm64RegisterApiBKeyLoEl1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 262191
    WHvArm64RegisterContextidrEl1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 262157
    WHvArm64RegisterCpacrEl1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 262148
    WHvArm64RegisterCsselrEl1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 262197
    WHvArm64RegisterEsrEl1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 262152
    WHvArm64RegisterFarEl1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 262153
    WHvArm64RegisterMairEl1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 262155
    WHvArm64RegisterMidrEl1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 262225
    WHvArm64RegisterMpidrEl1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 262145
    WHvArm64RegisterParEl1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 262154
    WHvArm64RegisterSctlrEl1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 262146
    WHvArm64RegisterSmcrEl1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 262237
    WHvArm64RegisterSmidrEl1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 262239
    WHvArm64RegisterSmpriEl1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 262240
    WHvArm64RegisterSvcr: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 262274
    WHvArm64RegisterTcrEl1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 262151
    WHvArm64RegisterTpidr2El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 262246
    WHvArm64RegisterTpidrEl0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 262161
    WHvArm64RegisterTpidrEl1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 262158
    WHvArm64RegisterTpidrroEl0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 262160
    WHvArm64RegisterTtbr0El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 262149
    WHvArm64RegisterTtbr1El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 262150
    WHvArm64RegisterVbarEl1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 262156
    WHvArm64RegisterZcrEl1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 262257
    WHvArm64RegisterDbgbcr0El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327680
    WHvArm64RegisterDbgbcr1El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327681
    WHvArm64RegisterDbgbcr2El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327682
    WHvArm64RegisterDbgbcr3El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327683
    WHvArm64RegisterDbgbcr4El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327684
    WHvArm64RegisterDbgbcr5El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327685
    WHvArm64RegisterDbgbcr6El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327686
    WHvArm64RegisterDbgbcr7El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327687
    WHvArm64RegisterDbgbcr8El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327688
    WHvArm64RegisterDbgbcr9El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327689
    WHvArm64RegisterDbgbcr10El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327690
    WHvArm64RegisterDbgbcr11El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327691
    WHvArm64RegisterDbgbcr12El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327692
    WHvArm64RegisterDbgbcr13El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327693
    WHvArm64RegisterDbgbcr14El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327694
    WHvArm64RegisterDbgbcr15El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327695
    WHvArm64RegisterDbgbvr0El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327712
    WHvArm64RegisterDbgbvr1El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327713
    WHvArm64RegisterDbgbvr2El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327714
    WHvArm64RegisterDbgbvr3El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327715
    WHvArm64RegisterDbgbvr4El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327716
    WHvArm64RegisterDbgbvr5El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327717
    WHvArm64RegisterDbgbvr6El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327718
    WHvArm64RegisterDbgbvr7El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327719
    WHvArm64RegisterDbgbvr8El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327720
    WHvArm64RegisterDbgbvr9El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327721
    WHvArm64RegisterDbgbvr10El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327722
    WHvArm64RegisterDbgbvr11El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327723
    WHvArm64RegisterDbgbvr12El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327724
    WHvArm64RegisterDbgbvr13El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327725
    WHvArm64RegisterDbgbvr14El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327726
    WHvArm64RegisterDbgbvr15El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327727
    WHvArm64RegisterDbgprcrEl1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327749
    WHvArm64RegisterDbgwcr0El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327696
    WHvArm64RegisterDbgwcr1El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327697
    WHvArm64RegisterDbgwcr2El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327698
    WHvArm64RegisterDbgwcr3El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327699
    WHvArm64RegisterDbgwcr4El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327700
    WHvArm64RegisterDbgwcr5El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327701
    WHvArm64RegisterDbgwcr6El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327702
    WHvArm64RegisterDbgwcr7El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327703
    WHvArm64RegisterDbgwcr8El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327704
    WHvArm64RegisterDbgwcr9El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327705
    WHvArm64RegisterDbgwcr10El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327706
    WHvArm64RegisterDbgwcr11El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327707
    WHvArm64RegisterDbgwcr12El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327708
    WHvArm64RegisterDbgwcr13El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327709
    WHvArm64RegisterDbgwcr14El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327710
    WHvArm64RegisterDbgwcr15El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327711
    WHvArm64RegisterDbgwvr0El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327728
    WHvArm64RegisterDbgwvr1El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327729
    WHvArm64RegisterDbgwvr2El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327730
    WHvArm64RegisterDbgwvr3El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327731
    WHvArm64RegisterDbgwvr4El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327732
    WHvArm64RegisterDbgwvr5El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327733
    WHvArm64RegisterDbgwvr6El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327734
    WHvArm64RegisterDbgwvr7El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327735
    WHvArm64RegisterDbgwvr8El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327736
    WHvArm64RegisterDbgwvr9El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327737
    WHvArm64RegisterDbgwvr10El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327738
    WHvArm64RegisterDbgwvr11El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327739
    WHvArm64RegisterDbgwvr12El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327740
    WHvArm64RegisterDbgwvr13El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327741
    WHvArm64RegisterDbgwvr14El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327742
    WHvArm64RegisterDbgwvr15El1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327743
    WHvArm64RegisterMdrarEl1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327756
    WHvArm64RegisterMdscrEl1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327757
    WHvArm64RegisterOsdlrEl1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327758
    WHvArm64RegisterOslarEl1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327762
    WHvArm64RegisterOslsrEl1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 327763
    WHvArm64RegisterPmccfiltrEl0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335872
    WHvArm64RegisterPmccntrEl0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335873
    WHvArm64RegisterPmceid0El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335874
    WHvArm64RegisterPmceid1El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335875
    WHvArm64RegisterPmcntenclrEl0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335876
    WHvArm64RegisterPmcntensetEl0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335877
    WHvArm64RegisterPmcrEl0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335878
    WHvArm64RegisterPmevcntr0El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335879
    WHvArm64RegisterPmevcntr1El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335880
    WHvArm64RegisterPmevcntr2El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335881
    WHvArm64RegisterPmevcntr3El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335882
    WHvArm64RegisterPmevcntr4El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335883
    WHvArm64RegisterPmevcntr5El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335884
    WHvArm64RegisterPmevcntr6El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335885
    WHvArm64RegisterPmevcntr7El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335886
    WHvArm64RegisterPmevcntr8El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335887
    WHvArm64RegisterPmevcntr9El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335888
    WHvArm64RegisterPmevcntr10El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335889
    WHvArm64RegisterPmevcntr11El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335890
    WHvArm64RegisterPmevcntr12El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335891
    WHvArm64RegisterPmevcntr13El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335892
    WHvArm64RegisterPmevcntr14El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335893
    WHvArm64RegisterPmevcntr15El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335894
    WHvArm64RegisterPmevcntr16El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335895
    WHvArm64RegisterPmevcntr17El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335896
    WHvArm64RegisterPmevcntr18El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335897
    WHvArm64RegisterPmevcntr19El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335898
    WHvArm64RegisterPmevcntr20El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335899
    WHvArm64RegisterPmevcntr21El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335900
    WHvArm64RegisterPmevcntr22El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335901
    WHvArm64RegisterPmevcntr23El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335902
    WHvArm64RegisterPmevcntr24El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335903
    WHvArm64RegisterPmevcntr25El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335904
    WHvArm64RegisterPmevcntr26El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335905
    WHvArm64RegisterPmevcntr27El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335906
    WHvArm64RegisterPmevcntr28El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335907
    WHvArm64RegisterPmevcntr29El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335908
    WHvArm64RegisterPmevcntr30El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335909
    WHvArm64RegisterPmevtyper0El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335910
    WHvArm64RegisterPmevtyper1El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335911
    WHvArm64RegisterPmevtyper2El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335912
    WHvArm64RegisterPmevtyper3El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335913
    WHvArm64RegisterPmevtyper4El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335914
    WHvArm64RegisterPmevtyper5El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335915
    WHvArm64RegisterPmevtyper6El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335916
    WHvArm64RegisterPmevtyper7El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335917
    WHvArm64RegisterPmevtyper8El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335918
    WHvArm64RegisterPmevtyper9El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335919
    WHvArm64RegisterPmevtyper10El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335920
    WHvArm64RegisterPmevtyper11El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335921
    WHvArm64RegisterPmevtyper12El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335922
    WHvArm64RegisterPmevtyper13El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335923
    WHvArm64RegisterPmevtyper14El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335924
    WHvArm64RegisterPmevtyper15El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335925
    WHvArm64RegisterPmevtyper16El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335926
    WHvArm64RegisterPmevtyper17El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335927
    WHvArm64RegisterPmevtyper18El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335928
    WHvArm64RegisterPmevtyper19El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335929
    WHvArm64RegisterPmevtyper20El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335930
    WHvArm64RegisterPmevtyper21El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335931
    WHvArm64RegisterPmevtyper22El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335932
    WHvArm64RegisterPmevtyper23El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335933
    WHvArm64RegisterPmevtyper24El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335934
    WHvArm64RegisterPmevtyper25El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335935
    WHvArm64RegisterPmevtyper26El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335936
    WHvArm64RegisterPmevtyper27El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335937
    WHvArm64RegisterPmevtyper28El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335938
    WHvArm64RegisterPmevtyper29El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335939
    WHvArm64RegisterPmevtyper30El0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335940
    WHvArm64RegisterPmintenclrEl1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335941
    WHvArm64RegisterPmintensetEl1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335942
    WHvArm64RegisterPmovsclrEl0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335944
    WHvArm64RegisterPmovssetEl0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335945
    WHvArm64RegisterPmselrEl0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335946
    WHvArm64RegisterPmuserenrEl0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 335948
    WHvArm64RegisterCntkctlEl1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 360456
    WHvArm64RegisterCntvCtlEl0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 360462
    WHvArm64RegisterCntvCvalEl0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 360463
    WHvArm64RegisterCntvctEl0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 360465
    WHvArm64RegisterGicrBaseGpa: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 405504
    WHvRegisterSint0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 655360
    WHvRegisterSint1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 655361
    WHvRegisterSint2: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 655362
    WHvRegisterSint3: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 655363
    WHvRegisterSint4: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 655364
    WHvRegisterSint5: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 655365
    WHvRegisterSint6: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 655366
    WHvRegisterSint7: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 655367
    WHvRegisterSint8: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 655368
    WHvRegisterSint9: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 655369
    WHvRegisterSint10: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 655370
    WHvRegisterSint11: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 655371
    WHvRegisterSint12: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 655372
    WHvRegisterSint13: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 655373
    WHvRegisterSint14: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 655374
    WHvRegisterSint15: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 655375
    WHvRegisterScontrol: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 655376
    WHvRegisterSversion: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 655377
    WHvRegisterSifp: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 655378
    WHvRegisterSipp: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 655379
    WHvRegisterEom: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 655380
    WHvRegisterHypervisorVersion: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 256
    WHvRegisterPrivilegesAndFeaturesInfo: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 512
    WHvRegisterFeaturesInfo: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 513
    WHvRegisterImplementationLimitsInfo: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 514
    WHvRegisterHardwareFeaturesInfo: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 515
    WHvRegisterCpuManagementFeaturesInfo: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 516
    WHvRegisterPasidFeaturesInfo: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 517
    WHvRegisterGuestCrashP0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 528
    WHvRegisterGuestCrashP1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 529
    WHvRegisterGuestCrashP2: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 530
    WHvRegisterGuestCrashP3: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 531
    WHvRegisterGuestCrashP4: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 532
    WHvRegisterGuestCrashCtl: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 533
    WHvRegisterVpRuntime: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 589824
    WHvRegisterGuestOsId: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 589826
    WHvRegisterVpAssistPage: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 589843
    WHvArm64RegisterPartitionInfoPage: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 589845
    WHvRegisterReferenceTsc: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 589847
    WHvRegisterReferenceTscSequence: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 589850
    WHvRegisterPendingEvent0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 65540
    WHvRegisterPendingEvent1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 65541
    WHvRegisterDeliverabilityNotifications: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 65542
    WHvRegisterInternalActivityState: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4
    WHvRegisterPendingEvent2: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 65544
    WHvRegisterPendingEvent3: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 65545
elif ARCH in 'X64':
    WHV_REGISTER_NAME = Int32
    WHvX64RegisterRax: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 0
    WHvX64RegisterRcx: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 1
    WHvX64RegisterRdx: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 2
    WHvX64RegisterRbx: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 3
    WHvX64RegisterRsp: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4
    WHvX64RegisterRbp: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 5
    WHvX64RegisterRsi: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 6
    WHvX64RegisterRdi: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 7
    WHvX64RegisterR8: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8
    WHvX64RegisterR9: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 9
    WHvX64RegisterR10: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 10
    WHvX64RegisterR11: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 11
    WHvX64RegisterR12: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12
    WHvX64RegisterR13: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 13
    WHvX64RegisterR14: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 14
    WHvX64RegisterR15: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 15
    WHvX64RegisterRip: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 16
    WHvX64RegisterRflags: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 17
    WHvX64RegisterEs: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 18
    WHvX64RegisterCs: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 19
    WHvX64RegisterSs: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 20
    WHvX64RegisterDs: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 21
    WHvX64RegisterFs: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 22
    WHvX64RegisterGs: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 23
    WHvX64RegisterLdtr: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 24
    WHvX64RegisterTr: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 25
    WHvX64RegisterIdtr: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 26
    WHvX64RegisterGdtr: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 27
    WHvX64RegisterCr0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 28
    WHvX64RegisterCr2: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 29
    WHvX64RegisterCr3: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 30
    WHvX64RegisterCr4: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 31
    WHvX64RegisterCr8: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 32
    WHvX64RegisterDr0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 33
    WHvX64RegisterDr1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 34
    WHvX64RegisterDr2: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 35
    WHvX64RegisterDr3: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 36
    WHvX64RegisterDr6: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 37
    WHvX64RegisterDr7: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 38
    WHvX64RegisterXCr0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 39
    WHvX64RegisterVirtualCr0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 40
    WHvX64RegisterVirtualCr3: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 41
    WHvX64RegisterVirtualCr4: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 42
    WHvX64RegisterVirtualCr8: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 43
    WHvX64RegisterXmm0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4096
    WHvX64RegisterXmm1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4097
    WHvX64RegisterXmm2: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4098
    WHvX64RegisterXmm3: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4099
    WHvX64RegisterXmm4: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4100
    WHvX64RegisterXmm5: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4101
    WHvX64RegisterXmm6: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4102
    WHvX64RegisterXmm7: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4103
    WHvX64RegisterXmm8: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4104
    WHvX64RegisterXmm9: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4105
    WHvX64RegisterXmm10: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4106
    WHvX64RegisterXmm11: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4107
    WHvX64RegisterXmm12: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4108
    WHvX64RegisterXmm13: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4109
    WHvX64RegisterXmm14: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4110
    WHvX64RegisterXmm15: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4111
    WHvX64RegisterFpMmx0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4112
    WHvX64RegisterFpMmx1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4113
    WHvX64RegisterFpMmx2: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4114
    WHvX64RegisterFpMmx3: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4115
    WHvX64RegisterFpMmx4: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4116
    WHvX64RegisterFpMmx5: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4117
    WHvX64RegisterFpMmx6: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4118
    WHvX64RegisterFpMmx7: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4119
    WHvX64RegisterFpControlStatus: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4120
    WHvX64RegisterXmmControlStatus: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4121
    WHvX64RegisterTsc: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8192
    WHvX64RegisterEfer: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8193
    WHvX64RegisterKernelGsBase: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8194
    WHvX64RegisterApicBase: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8195
    WHvX64RegisterPat: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8196
    WHvX64RegisterSysenterCs: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8197
    WHvX64RegisterSysenterEip: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8198
    WHvX64RegisterSysenterEsp: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8199
    WHvX64RegisterStar: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8200
    WHvX64RegisterLstar: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8201
    WHvX64RegisterCstar: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8202
    WHvX64RegisterSfmask: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8203
    WHvX64RegisterInitialApicId: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8204
    WHvX64RegisterMsrMtrrCap: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8205
    WHvX64RegisterMsrMtrrDefType: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8206
    WHvX64RegisterMsrMtrrPhysBase0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8208
    WHvX64RegisterMsrMtrrPhysBase1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8209
    WHvX64RegisterMsrMtrrPhysBase2: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8210
    WHvX64RegisterMsrMtrrPhysBase3: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8211
    WHvX64RegisterMsrMtrrPhysBase4: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8212
    WHvX64RegisterMsrMtrrPhysBase5: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8213
    WHvX64RegisterMsrMtrrPhysBase6: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8214
    WHvX64RegisterMsrMtrrPhysBase7: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8215
    WHvX64RegisterMsrMtrrPhysBase8: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8216
    WHvX64RegisterMsrMtrrPhysBase9: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8217
    WHvX64RegisterMsrMtrrPhysBaseA: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8218
    WHvX64RegisterMsrMtrrPhysBaseB: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8219
    WHvX64RegisterMsrMtrrPhysBaseC: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8220
    WHvX64RegisterMsrMtrrPhysBaseD: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8221
    WHvX64RegisterMsrMtrrPhysBaseE: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8222
    WHvX64RegisterMsrMtrrPhysBaseF: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8223
    WHvX64RegisterMsrMtrrPhysMask0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8256
    WHvX64RegisterMsrMtrrPhysMask1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8257
    WHvX64RegisterMsrMtrrPhysMask2: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8258
    WHvX64RegisterMsrMtrrPhysMask3: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8259
    WHvX64RegisterMsrMtrrPhysMask4: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8260
    WHvX64RegisterMsrMtrrPhysMask5: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8261
    WHvX64RegisterMsrMtrrPhysMask6: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8262
    WHvX64RegisterMsrMtrrPhysMask7: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8263
    WHvX64RegisterMsrMtrrPhysMask8: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8264
    WHvX64RegisterMsrMtrrPhysMask9: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8265
    WHvX64RegisterMsrMtrrPhysMaskA: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8266
    WHvX64RegisterMsrMtrrPhysMaskB: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8267
    WHvX64RegisterMsrMtrrPhysMaskC: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8268
    WHvX64RegisterMsrMtrrPhysMaskD: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8269
    WHvX64RegisterMsrMtrrPhysMaskE: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8270
    WHvX64RegisterMsrMtrrPhysMaskF: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8271
    WHvX64RegisterMsrMtrrFix64k00000: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8304
    WHvX64RegisterMsrMtrrFix16k80000: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8305
    WHvX64RegisterMsrMtrrFix16kA0000: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8306
    WHvX64RegisterMsrMtrrFix4kC0000: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8307
    WHvX64RegisterMsrMtrrFix4kC8000: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8308
    WHvX64RegisterMsrMtrrFix4kD0000: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8309
    WHvX64RegisterMsrMtrrFix4kD8000: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8310
    WHvX64RegisterMsrMtrrFix4kE0000: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8311
    WHvX64RegisterMsrMtrrFix4kE8000: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8312
    WHvX64RegisterMsrMtrrFix4kF0000: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8313
    WHvX64RegisterMsrMtrrFix4kF8000: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8314
    WHvX64RegisterTscAux: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8315
    WHvX64RegisterBndcfgs: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8316
    WHvX64RegisterMCount: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8318
    WHvX64RegisterACount: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8319
    WHvX64RegisterSpecCtrl: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8324
    WHvX64RegisterPredCmd: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8325
    WHvX64RegisterTscVirtualOffset: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8327
    WHvX64RegisterTsxCtrl: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8328
    WHvX64RegisterXss: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8331
    WHvX64RegisterUCet: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8332
    WHvX64RegisterSCet: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8333
    WHvX64RegisterSsp: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8334
    WHvX64RegisterPl0Ssp: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8335
    WHvX64RegisterPl1Ssp: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8336
    WHvX64RegisterPl2Ssp: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8337
    WHvX64RegisterPl3Ssp: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8338
    WHvX64RegisterInterruptSspTableAddr: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8339
    WHvX64RegisterTscDeadline: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8341
    WHvX64RegisterTscAdjust: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8342
    WHvX64RegisterUmwaitControl: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8344
    WHvX64RegisterXfd: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8345
    WHvX64RegisterXfdErr: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8346
    WHvX64RegisterMsrIa32MiscEnable: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8352
    WHvX64RegisterIa32FeatureControl: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8353
    WHvX64RegisterIa32VmxBasic: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8354
    WHvX64RegisterIa32VmxPinbasedCtls: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8355
    WHvX64RegisterIa32VmxProcbasedCtls: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8356
    WHvX64RegisterIa32VmxExitCtls: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8357
    WHvX64RegisterIa32VmxEntryCtls: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8358
    WHvX64RegisterIa32VmxMisc: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8359
    WHvX64RegisterIa32VmxCr0Fixed0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8360
    WHvX64RegisterIa32VmxCr0Fixed1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8361
    WHvX64RegisterIa32VmxCr4Fixed0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8362
    WHvX64RegisterIa32VmxCr4Fixed1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8363
    WHvX64RegisterIa32VmxVmcsEnum: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8364
    WHvX64RegisterIa32VmxProcbasedCtls2: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8365
    WHvX64RegisterIa32VmxEptVpidCap: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8366
    WHvX64RegisterIa32VmxTruePinbasedCtls: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8367
    WHvX64RegisterIa32VmxTrueProcbasedCtls: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8368
    WHvX64RegisterIa32VmxTrueExitCtls: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8369
    WHvX64RegisterIa32VmxTrueEntryCtls: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8370
    WHvX64RegisterAmdVmHsavePa: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8371
    WHvX64RegisterAmdVmCr: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8372
    WHvX64RegisterApicId: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12290
    WHvX64RegisterApicVersion: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12291
    WHvX64RegisterApicTpr: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12296
    WHvX64RegisterApicPpr: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12298
    WHvX64RegisterApicEoi: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12299
    WHvX64RegisterApicLdr: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12301
    WHvX64RegisterApicSpurious: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12303
    WHvX64RegisterApicIsr0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12304
    WHvX64RegisterApicIsr1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12305
    WHvX64RegisterApicIsr2: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12306
    WHvX64RegisterApicIsr3: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12307
    WHvX64RegisterApicIsr4: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12308
    WHvX64RegisterApicIsr5: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12309
    WHvX64RegisterApicIsr6: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12310
    WHvX64RegisterApicIsr7: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12311
    WHvX64RegisterApicTmr0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12312
    WHvX64RegisterApicTmr1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12313
    WHvX64RegisterApicTmr2: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12314
    WHvX64RegisterApicTmr3: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12315
    WHvX64RegisterApicTmr4: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12316
    WHvX64RegisterApicTmr5: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12317
    WHvX64RegisterApicTmr6: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12318
    WHvX64RegisterApicTmr7: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12319
    WHvX64RegisterApicIrr0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12320
    WHvX64RegisterApicIrr1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12321
    WHvX64RegisterApicIrr2: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12322
    WHvX64RegisterApicIrr3: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12323
    WHvX64RegisterApicIrr4: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12324
    WHvX64RegisterApicIrr5: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12325
    WHvX64RegisterApicIrr6: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12326
    WHvX64RegisterApicIrr7: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12327
    WHvX64RegisterApicEse: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12328
    WHvX64RegisterApicIcr: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12336
    WHvX64RegisterApicLvtTimer: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12338
    WHvX64RegisterApicLvtThermal: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12339
    WHvX64RegisterApicLvtPerfmon: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12340
    WHvX64RegisterApicLvtLint0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12341
    WHvX64RegisterApicLvtLint1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12342
    WHvX64RegisterApicLvtError: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12343
    WHvX64RegisterApicInitCount: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12344
    WHvX64RegisterApicCurrentCount: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12345
    WHvX64RegisterApicDivide: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12350
    WHvX64RegisterApicSelfIpi: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12351
    WHvRegisterSint0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 16384
    WHvRegisterSint1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 16385
    WHvRegisterSint2: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 16386
    WHvRegisterSint3: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 16387
    WHvRegisterSint4: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 16388
    WHvRegisterSint5: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 16389
    WHvRegisterSint6: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 16390
    WHvRegisterSint7: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 16391
    WHvRegisterSint8: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 16392
    WHvRegisterSint9: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 16393
    WHvRegisterSint10: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 16394
    WHvRegisterSint11: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 16395
    WHvRegisterSint12: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 16396
    WHvRegisterSint13: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 16397
    WHvRegisterSint14: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 16398
    WHvRegisterSint15: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 16399
    WHvRegisterScontrol: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 16400
    WHvRegisterSversion: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 16401
    WHvRegisterSiefp: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 16402
    WHvRegisterSimp: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 16403
    WHvRegisterEom: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 16404
    WHvRegisterVpRuntime: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 20480
    WHvX64RegisterHypercall: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 20481
    WHvRegisterGuestOsId: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 20482
    WHvRegisterVpAssistPage: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 20499
    WHvRegisterReferenceTsc: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 20503
    WHvRegisterReferenceTscSequence: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 20506
    WHvX64RegisterNestedGuestState: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 20560
    WHvX64RegisterNestedCurrentVmGpa: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 20561
    WHvX64RegisterNestedVmxInvEpt: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 20562
    WHvX64RegisterNestedVmxInvVpid: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 20563
    WHvRegisterPendingInterruption: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = -2147483648
    WHvRegisterInterruptState: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = -2147483647
    WHvRegisterPendingEvent: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = -2147483646
    WHvRegisterPendingEvent1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = -2147483645
    WHvX64RegisterDeliverabilityNotifications: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = -2147483644
    WHvRegisterDeliverabilityNotifications: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = -2147483644
    WHvRegisterInternalActivityState: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = -2147483643
    WHvX64RegisterPendingDebugException: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = -2147483642
    WHvRegisterPendingEvent2: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = -2147483641
    WHvRegisterPendingEvent3: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = -2147483640
if ARCH in 'ARM64':
    class WHV_REGISTER_VALUE(Union):
        Reg128: win32more.Windows.Win32.System.Hypervisor.WHV_UINT128
        Reg64: UInt64
        Reg32: UInt32
        Reg16: UInt16
        Reg8: Byte
        InternalActivity: win32more.Windows.Win32.System.Hypervisor.WHV_INTERNAL_ACTIVITY_REGISTER
        DeliverabilityNotifications: win32more.Windows.Win32.System.Hypervisor.WHV_DELIVERABILITY_NOTIFICATIONS_REGISTER
elif ARCH in 'X64':
    class WHV_REGISTER_VALUE(Union):
        Reg128: win32more.Windows.Win32.System.Hypervisor.WHV_UINT128
        Reg64: UInt64
        Reg32: UInt32
        Reg16: UInt16
        Reg8: Byte
        InternalActivity: win32more.Windows.Win32.System.Hypervisor.WHV_INTERNAL_ACTIVITY_REGISTER
        DeliverabilityNotifications: win32more.Windows.Win32.System.Hypervisor.WHV_DELIVERABILITY_NOTIFICATIONS_REGISTER
        Fp: win32more.Windows.Win32.System.Hypervisor.WHV_X64_FP_REGISTER
        FpControlStatus: win32more.Windows.Win32.System.Hypervisor.WHV_X64_FP_CONTROL_STATUS_REGISTER
        XmmControlStatus: win32more.Windows.Win32.System.Hypervisor.WHV_X64_XMM_CONTROL_STATUS_REGISTER
        Segment: win32more.Windows.Win32.System.Hypervisor.WHV_X64_SEGMENT_REGISTER
        Table: win32more.Windows.Win32.System.Hypervisor.WHV_X64_TABLE_REGISTER
        InterruptState: win32more.Windows.Win32.System.Hypervisor.WHV_X64_INTERRUPT_STATE_REGISTER
        PendingInterruption: win32more.Windows.Win32.System.Hypervisor.WHV_X64_PENDING_INTERRUPTION_REGISTER
        ExceptionEvent: win32more.Windows.Win32.System.Hypervisor.WHV_X64_PENDING_EXCEPTION_EVENT
        ExtIntEvent: win32more.Windows.Win32.System.Hypervisor.WHV_X64_PENDING_EXT_INT_EVENT
        PendingDebugException: win32more.Windows.Win32.System.Hypervisor.WHV_X64_PENDING_DEBUG_EXCEPTION
        NestedState: win32more.Windows.Win32.System.Hypervisor.WHV_X64_NESTED_GUEST_STATE
        InvEpt: win32more.Windows.Win32.System.Hypervisor.WHV_X64_NESTED_INVEPT_REGISTER
        InvVpid: win32more.Windows.Win32.System.Hypervisor.WHV_X64_NESTED_INVVPID_REGISTER
        SvmNestedExit0: win32more.Windows.Win32.System.Hypervisor.WHV_X64_PENDING_SVM_NESTED_EXIT_EVENT0
        SvmNestedExit1: win32more.Windows.Win32.System.Hypervisor.WHV_X64_PENDING_SVM_NESTED_EXIT_EVENT1
        SvmNestedExit2: win32more.Windows.Win32.System.Hypervisor.WHV_X64_PENDING_SVM_NESTED_EXIT_EVENT2
        SvmNestedExit3: win32more.Windows.Win32.System.Hypervisor.WHV_X64_PENDING_SVM_NESTED_EXIT_EVENT3
        VmxNestedExit0: win32more.Windows.Win32.System.Hypervisor.WHV_X64_PENDING_VMX_NESTED_EXIT_EVENT0
        VmxNestedExit1: win32more.Windows.Win32.System.Hypervisor.WHV_X64_PENDING_VMX_NESTED_EXIT_EVENT1
        VmxNestedExit2: win32more.Windows.Win32.System.Hypervisor.WHV_X64_PENDING_VMX_NESTED_EXIT_EVENT2
        VmxNestedExit3: win32more.Windows.Win32.System.Hypervisor.WHV_X64_PENDING_VMX_NESTED_EXIT_EVENT3
if ARCH in 'X64,ARM64':
    class WHV_RUN_VP_CANCELED_CONTEXT(Structure):
        CancelReason: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_CANCEL_REASON
if ARCH in 'X64,ARM64':
    WHV_RUN_VP_CANCEL_REASON = Int32
    WHvRunVpCancelReasonUser: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_CANCEL_REASON = 0
if ARCH in 'ARM64':
    class WHV_RUN_VP_EXIT_CONTEXT(Structure):
        ExitReason: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON
        Reserved: UInt32
        Reserved1: UInt64
        Anonymous: _Anonymous_e__Union
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Union(Union):
            MemoryAccess: win32more.Windows.Win32.System.Hypervisor.WHV_MEMORY_ACCESS_CONTEXT
            CancelReason: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_CANCELED_CONTEXT
            Hypercall: win32more.Windows.Win32.System.Hypervisor.WHV_ARM64_HYPERCALL_CONTEXT
            SynicSintDeliverable: win32more.Windows.Win32.System.Hypervisor.WHV_SYNIC_SINT_DELIVERABLE_CONTEXT
            UnrecoverableException: win32more.Windows.Win32.System.Hypervisor.WHV_UNRECOVERABLE_EXCEPTION_CONTEXT
            InvalidVpRegister: win32more.Windows.Win32.System.Hypervisor.WHV_INVALID_VP_REGISTER_CONTEXT
            Register: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_CONTEXT
            Arm64Reset: win32more.Windows.Win32.System.Hypervisor.WHV_ARM64_RESET_CONTEXT
            AsUINT64: UInt64 * 32
elif ARCH in 'X64':
    class WHV_RUN_VP_EXIT_CONTEXT(Structure):
        ExitReason: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON
        Reserved: UInt32
        VpContext: win32more.Windows.Win32.System.Hypervisor.WHV_X64_VP_EXIT_CONTEXT
        Anonymous: _Anonymous_e__Union
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Union(Union):
            MemoryAccess: win32more.Windows.Win32.System.Hypervisor.WHV_MEMORY_ACCESS_CONTEXT
            CancelReason: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_CANCELED_CONTEXT
            Hypercall: win32more.Windows.Win32.System.Hypervisor.WHV_X64_HYPERCALL_CONTEXT
            SynicSintDeliverable: win32more.Windows.Win32.System.Hypervisor.WHV_SYNIC_SINT_DELIVERABLE_CONTEXT
            IoPortAccess: win32more.Windows.Win32.System.Hypervisor.WHV_X64_IO_PORT_ACCESS_CONTEXT
            MsrAccess: win32more.Windows.Win32.System.Hypervisor.WHV_X64_MSR_ACCESS_CONTEXT
            CpuidAccess: win32more.Windows.Win32.System.Hypervisor.WHV_X64_CPUID_ACCESS_CONTEXT
            VpException: win32more.Windows.Win32.System.Hypervisor.WHV_VP_EXCEPTION_CONTEXT
            InterruptWindow: win32more.Windows.Win32.System.Hypervisor.WHV_X64_INTERRUPTION_DELIVERABLE_CONTEXT
            UnsupportedFeature: win32more.Windows.Win32.System.Hypervisor.WHV_X64_UNSUPPORTED_FEATURE_CONTEXT
            ApicEoi: win32more.Windows.Win32.System.Hypervisor.WHV_X64_APIC_EOI_CONTEXT
            ReadTsc: win32more.Windows.Win32.System.Hypervisor.WHV_X64_RDTSC_CONTEXT
            ApicSmi: win32more.Windows.Win32.System.Hypervisor.WHV_X64_APIC_SMI_CONTEXT
            ApicInitSipi: win32more.Windows.Win32.System.Hypervisor.WHV_X64_APIC_INIT_SIPI_CONTEXT
            ApicWrite: win32more.Windows.Win32.System.Hypervisor.WHV_X64_APIC_WRITE_CONTEXT
            AsUINT64: UInt64 * 22
if ARCH in 'ARM64':
    WHV_RUN_VP_EXIT_REASON = Int32
    WHvRunVpExitReasonNone: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = 0
    WHvRunVpExitReasonUnmappedGpa: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = -2147483648
    WHvRunVpExitReasonGpaIntercept: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = -2147483647
    WHvRunVpExitReasonUnrecoverableException: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = -2147483615
    WHvRunVpExitReasonInvalidVpRegisterValue: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = -2147483616
    WHvRunVpExitReasonUnsupportedFeature: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = -2147483614
    WHvRunVpExitReasonSynicSintDeliverable: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = -2147483550
    WHvMessageTypeRegisterIntercept: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = -2147418106
    WHvRunVpExitReasonArm64Reset: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = -2147418100
    WHvRunVpExitReasonHypercall: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = -2147483568
    WHvRunVpExitReasonCanceled: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = -1
elif ARCH in 'X64':
    WHV_RUN_VP_EXIT_REASON = Int32
    WHvRunVpExitReasonNone: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = 0
    WHvRunVpExitReasonMemoryAccess: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = 1
    WHvRunVpExitReasonX64IoPortAccess: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = 2
    WHvRunVpExitReasonUnrecoverableException: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = 4
    WHvRunVpExitReasonInvalidVpRegisterValue: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = 5
    WHvRunVpExitReasonUnsupportedFeature: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = 6
    WHvRunVpExitReasonX64InterruptWindow: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = 7
    WHvRunVpExitReasonX64Halt: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = 8
    WHvRunVpExitReasonX64ApicEoi: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = 9
    WHvRunVpExitReasonSynicSintDeliverable: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = 10
    WHvRunVpExitReasonX64MsrAccess: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = 4096
    WHvRunVpExitReasonX64Cpuid: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = 4097
    WHvRunVpExitReasonException: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = 4098
    WHvRunVpExitReasonX64Rdtsc: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = 4099
    WHvRunVpExitReasonX64ApicSmiTrap: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = 4100
    WHvRunVpExitReasonHypercall: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = 4101
    WHvRunVpExitReasonX64ApicInitSipiTrap: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = 4102
    WHvRunVpExitReasonX64ApicWriteTrap: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = 4103
    WHvRunVpExitReasonCanceled: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = 8193
if ARCH in 'X64,ARM64':
    class WHV_SCHEDULER_FEATURES(Union):
        Anonymous: _Anonymous_e__Struct
        AsUINT64: UInt64
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            CpuReserve: Annotated[UInt64, NativeBitfieldAttribute(1)]
            CpuCap: Annotated[UInt64, NativeBitfieldAttribute(1)]
            CpuWeight: Annotated[UInt64, NativeBitfieldAttribute(1)]
            CpuGroupId: Annotated[UInt64, NativeBitfieldAttribute(1)]
            DisableSmt: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved: Annotated[UInt64, NativeBitfieldAttribute(59)]
if ARCH in 'X64,ARM64':
    class WHV_SRIOV_RESOURCE_DESCRIPTOR(Structure):
        PnpInstanceId: Char * 200
        VirtualFunctionId: win32more.Windows.Win32.Foundation.LUID
        VirtualFunctionIndex: UInt16
        Reserved: UInt16
if ARCH in 'X64,ARM64':
    class WHV_SVM_NESTED_HOST_STATE(Structure):
        Rip: UInt64
        Rsp: UInt64
        Rflags: UInt64
        Rax: UInt64
        Es: win32more.Windows.Win32.System.Hypervisor.WHV_SVM_VMCB_SELECTOR
        Cs: win32more.Windows.Win32.System.Hypervisor.WHV_SVM_VMCB_SELECTOR
        Ss: win32more.Windows.Win32.System.Hypervisor.WHV_SVM_VMCB_SELECTOR
        Ds: win32more.Windows.Win32.System.Hypervisor.WHV_SVM_VMCB_SELECTOR
        Gdtr: win32more.Windows.Win32.System.Hypervisor.WHV_SVM_VMCB_SELECTOR
        Idtr: win32more.Windows.Win32.System.Hypervisor.WHV_SVM_VMCB_SELECTOR
        Efer: UInt64
        Cr0: UInt64
        Cr3: UInt64
        Cr4: UInt64
        VirtualTpr: UInt64
        Reserved: UInt64 * 6
if ARCH in 'X64,ARM64':
    class WHV_SVM_VMCB_SELECTOR(Structure):
        Selector: UInt16
        Attrib: UInt16
        Limit: UInt32
        Base: UInt64
        _pack_ = 1
if ARCH in 'X64,ARM64':
    class WHV_SYNIC_EVENT_PARAMETERS(Structure):
        VpIndex: UInt32
        TargetSint: Byte
        TargetVtl: Byte
        FlagNumber: UInt16
if ARCH in 'ARM64':
    class WHV_SYNIC_SINT_DELIVERABLE_CONTEXT(Structure):
        Header: win32more.Windows.Win32.System.Hypervisor.WHV_INTERCEPT_MESSAGE_HEADER
        DeliverableSints: UInt16
        Reserved1: UInt16
        Reserved2: UInt32
elif ARCH in 'X64':
    class WHV_SYNIC_SINT_DELIVERABLE_CONTEXT(Structure):
        DeliverableSints: UInt16
        Reserved1: UInt16
        Reserved2: UInt32
if ARCH in 'X64,ARM64':
    class WHV_SYNTHETIC_PROCESSOR_FEATURES(Union):
        Anonymous: _Anonymous_e__Struct
        AsUINT64: UInt64
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            HypervisorPresent: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Hv1: Annotated[UInt64, NativeBitfieldAttribute(1)]
            AccessVpRunTimeReg: Annotated[UInt64, NativeBitfieldAttribute(1)]
            AccessPartitionReferenceCounter: Annotated[UInt64, NativeBitfieldAttribute(1)]
            AccessSynicRegs: Annotated[UInt64, NativeBitfieldAttribute(1)]
            AccessSyntheticTimerRegs: Annotated[UInt64, NativeBitfieldAttribute(1)]
            AccessIntrCtrlRegs: Annotated[UInt64, NativeBitfieldAttribute(1)]
            AccessHypercallRegs: Annotated[UInt64, NativeBitfieldAttribute(1)]
            AccessVpIndex: Annotated[UInt64, NativeBitfieldAttribute(1)]
            AccessPartitionReferenceTsc: Annotated[UInt64, NativeBitfieldAttribute(1)]
            AccessGuestIdleReg: Annotated[UInt64, NativeBitfieldAttribute(1)]
            AccessFrequencyRegs: Annotated[UInt64, NativeBitfieldAttribute(1)]
            ReservedZ12: Annotated[UInt64, NativeBitfieldAttribute(1)]
            ReservedZ13: Annotated[UInt64, NativeBitfieldAttribute(1)]
            ReservedZ14: Annotated[UInt64, NativeBitfieldAttribute(1)]
            EnableExtendedGvaRangesForFlushVirtualAddressList: Annotated[UInt64, NativeBitfieldAttribute(1)]
            ReservedZ16: Annotated[UInt64, NativeBitfieldAttribute(1)]
            ReservedZ17: Annotated[UInt64, NativeBitfieldAttribute(1)]
            FastHypercallOutput: Annotated[UInt64, NativeBitfieldAttribute(1)]
            ReservedZ19: Annotated[UInt64, NativeBitfieldAttribute(1)]
            ReservedZ20: Annotated[UInt64, NativeBitfieldAttribute(1)]
            ReservedZ21: Annotated[UInt64, NativeBitfieldAttribute(1)]
            DirectSyntheticTimers: Annotated[UInt64, NativeBitfieldAttribute(1)]
            ReservedZ23: Annotated[UInt64, NativeBitfieldAttribute(1)]
            ExtendedProcessorMasks: Annotated[UInt64, NativeBitfieldAttribute(1)]
            TbFlushHypercalls: Annotated[UInt64, NativeBitfieldAttribute(1)]
            SyntheticClusterIpi: Annotated[UInt64, NativeBitfieldAttribute(1)]
            NotifyLongSpinWait: Annotated[UInt64, NativeBitfieldAttribute(1)]
            QueryNumaDistance: Annotated[UInt64, NativeBitfieldAttribute(1)]
            SignalEvents: Annotated[UInt64, NativeBitfieldAttribute(1)]
            RetargetDeviceInterrupt: Annotated[UInt64, NativeBitfieldAttribute(1)]
            RestoreTime: Annotated[UInt64, NativeBitfieldAttribute(1)]
            EnlightenedVmcs: Annotated[UInt64, NativeBitfieldAttribute(1)]
            NestedDebugCtl: Annotated[UInt64, NativeBitfieldAttribute(1)]
            SyntheticTimeUnhaltedTimer: Annotated[UInt64, NativeBitfieldAttribute(1)]
            IdleSpecCtrl: Annotated[UInt64, NativeBitfieldAttribute(1)]
            ReservedZ36: Annotated[UInt64, NativeBitfieldAttribute(1)]
            WakeVps: Annotated[UInt64, NativeBitfieldAttribute(1)]
            AccessVpRegs: Annotated[UInt64, NativeBitfieldAttribute(1)]
            ReservedZ39: Annotated[UInt64, NativeBitfieldAttribute(1)]
            ReservedZ40: Annotated[UInt64, NativeBitfieldAttribute(1)]
            ReservedZ41: Annotated[UInt64, NativeBitfieldAttribute(1)]
            ReservedZ42: Annotated[UInt64, NativeBitfieldAttribute(1)]
            ReservedZ43: Annotated[UInt64, NativeBitfieldAttribute(1)]
            ReservedZ44: Annotated[UInt64, NativeBitfieldAttribute(1)]
            ReservedZ45: Annotated[UInt64, NativeBitfieldAttribute(1)]
            ReservedZ46: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved: Annotated[UInt64, NativeBitfieldAttribute(17)]
if ARCH in 'X64,ARM64':
    class WHV_SYNTHETIC_PROCESSOR_FEATURES_BANKS(Structure):
        BanksCount: UInt32
        Reserved0: UInt32
        Anonymous: _Anonymous_e__Union
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Union(Union):
            Anonymous: _Anonymous_e__Struct
            AsUINT64: FlexibleArray[UInt64]
            _anonymous_ = ('Anonymous',)
            class _Anonymous_e__Struct(Structure):
                Bank0: win32more.Windows.Win32.System.Hypervisor.WHV_SYNTHETIC_PROCESSOR_FEATURES
if ARCH in 'X64,ARM64':
    class WHV_TRANSLATE_GVA_2_FLAGS(Union):
        Anonymous: _Anonymous_e__Struct
        AsUINT64: UInt64
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            ValidateRead: Annotated[UInt64, NativeBitfieldAttribute(1)]
            ValidateWrite: Annotated[UInt64, NativeBitfieldAttribute(1)]
            ValidateExecute: Annotated[UInt64, NativeBitfieldAttribute(1)]
            PrivilegeExempt: Annotated[UInt64, NativeBitfieldAttribute(1)]
            SetPageTableBits: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved1: Annotated[UInt64, NativeBitfieldAttribute(3)]
            EnforceSmap: Annotated[UInt64, NativeBitfieldAttribute(1)]
            OverrideSmap: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved4: Annotated[UInt64, NativeBitfieldAttribute(46)]
            InputVtl: Annotated[UInt64, NativeBitfieldAttribute(8)]
if ARCH in 'ARM64':
    WHV_TRANSLATE_GVA_FLAGS = Int32
    WHvTranslateGvaFlagNone: win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_FLAGS = 0
    WHvTranslateGvaFlagValidateRead: win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_FLAGS = 1
    WHvTranslateGvaFlagValidateWrite: win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_FLAGS = 2
    WHvTranslateGvaFlagValidateExecute: win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_FLAGS = 4
    WHvTranslateGvaFlagSetPageTableBits: win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_FLAGS = 16
elif ARCH in 'X64':
    WHV_TRANSLATE_GVA_FLAGS = Int32
    WHvTranslateGvaFlagNone: win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_FLAGS = 0
    WHvTranslateGvaFlagValidateRead: win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_FLAGS = 1
    WHvTranslateGvaFlagValidateWrite: win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_FLAGS = 2
    WHvTranslateGvaFlagValidateExecute: win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_FLAGS = 4
    WHvTranslateGvaFlagPrivilegeExempt: win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_FLAGS = 8
    WHvTranslateGvaFlagSetPageTableBits: win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_FLAGS = 16
    WHvTranslateGvaFlagEnforceSmap: win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_FLAGS = 256
    WHvTranslateGvaFlagOverrideSmap: win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_FLAGS = 512
if ARCH in 'X64,ARM64':
    class WHV_TRANSLATE_GVA_RESULT(Structure):
        ResultCode: win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_RESULT_CODE
        Reserved: UInt32
if ARCH in 'X64,ARM64':
    WHV_TRANSLATE_GVA_RESULT_CODE = Int32
    WHvTranslateGvaResultSuccess: win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_RESULT_CODE = 0
    WHvTranslateGvaResultPageNotPresent: win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_RESULT_CODE = 1
    WHvTranslateGvaResultPrivilegeViolation: win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_RESULT_CODE = 2
    WHvTranslateGvaResultInvalidPageTableFlags: win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_RESULT_CODE = 3
    WHvTranslateGvaResultGpaUnmapped: win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_RESULT_CODE = 4
    WHvTranslateGvaResultGpaNoReadAccess: win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_RESULT_CODE = 5
    WHvTranslateGvaResultGpaNoWriteAccess: win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_RESULT_CODE = 6
    WHvTranslateGvaResultGpaIllegalOverlayAccess: win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_RESULT_CODE = 7
    WHvTranslateGvaResultIntercept: win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_RESULT_CODE = 8
if ARCH in 'X64,ARM64':
    class WHV_TRIGGER_PARAMETERS(Structure):
        TriggerType: win32more.Windows.Win32.System.Hypervisor.WHV_TRIGGER_TYPE
        Reserved: UInt32
        Anonymous: _Anonymous_e__Union
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Union(Union):
            Interrupt: win32more.Windows.Win32.System.Hypervisor.WHV_INTERRUPT_CONTROL
            SynicEvent: win32more.Windows.Win32.System.Hypervisor.WHV_SYNIC_EVENT_PARAMETERS
            DeviceInterrupt: _DeviceInterrupt_e__Struct
            class _DeviceInterrupt_e__Struct(Structure):
                LogicalDeviceId: UInt64
                MsiAddress: UInt64
                MsiData: UInt32
                Reserved: UInt32
if ARCH in 'ARM64':
    WHV_TRIGGER_TYPE = Int32
    WHvTriggerTypeSynicEvent: win32more.Windows.Win32.System.Hypervisor.WHV_TRIGGER_TYPE = 1
    WHvTriggerTypeDeviceInterrupt: win32more.Windows.Win32.System.Hypervisor.WHV_TRIGGER_TYPE = 2
elif ARCH in 'X64':
    WHV_TRIGGER_TYPE = Int32
    WHvTriggerTypeInterrupt: win32more.Windows.Win32.System.Hypervisor.WHV_TRIGGER_TYPE = 0
    WHvTriggerTypeSynicEvent: win32more.Windows.Win32.System.Hypervisor.WHV_TRIGGER_TYPE = 1
    WHvTriggerTypeDeviceInterrupt: win32more.Windows.Win32.System.Hypervisor.WHV_TRIGGER_TYPE = 2
if ARCH in 'X64,ARM64':
    class WHV_UINT128(Union):
        Anonymous: _Anonymous_e__Struct
        Dword: UInt32 * 4
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            Low64: UInt64
            High64: UInt64
if ARCH in 'ARM64':
    class WHV_UNRECOVERABLE_EXCEPTION_CONTEXT(Structure):
        Header: win32more.Windows.Win32.System.Hypervisor.WHV_INTERCEPT_MESSAGE_HEADER
if ARCH in 'X64,ARM64':
    class WHV_VIRTUAL_PROCESSOR_PROPERTY(Structure):
        PropertyCode: win32more.Windows.Win32.System.Hypervisor.WHV_VIRTUAL_PROCESSOR_PROPERTY_CODE
        Reserved: UInt32
        Anonymous: _Anonymous_e__Union
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Union(Union):
            NumaNode: UInt16
            Padding: UInt64
if ARCH in 'X64,ARM64':
    WHV_VIRTUAL_PROCESSOR_PROPERTY_CODE = Int32
    WHvVirtualProcessorPropertyCodeNumaNode: win32more.Windows.Win32.System.Hypervisor.WHV_VIRTUAL_PROCESSOR_PROPERTY_CODE = 0
if ARCH in 'ARM64':
    WHV_VIRTUAL_PROCESSOR_STATE_TYPE = Int32
    WHvVirtualProcessorStateTypeInterruptControllerState: win32more.Windows.Win32.System.Hypervisor.WHV_VIRTUAL_PROCESSOR_STATE_TYPE = -2147483648
    WHvVirtualProcessorStateTypeSynicMessagePage: win32more.Windows.Win32.System.Hypervisor.WHV_VIRTUAL_PROCESSOR_STATE_TYPE = -2147483646
    WHvVirtualProcessorStateTypeSynicEventFlagPage: win32more.Windows.Win32.System.Hypervisor.WHV_VIRTUAL_PROCESSOR_STATE_TYPE = -2147483645
    WHvVirtualProcessorStateTypeSynicTimerState: win32more.Windows.Win32.System.Hypervisor.WHV_VIRTUAL_PROCESSOR_STATE_TYPE = 4
    WHvVirtualProcessorStateTypeGlobalInterruptState: win32more.Windows.Win32.System.Hypervisor.WHV_VIRTUAL_PROCESSOR_STATE_TYPE = -1073741818
    WHvVirtualProcessorStateTypeSveState: win32more.Windows.Win32.System.Hypervisor.WHV_VIRTUAL_PROCESSOR_STATE_TYPE = -2147483641
    WHvVirtualProcessorStateTypeSmeState: win32more.Windows.Win32.System.Hypervisor.WHV_VIRTUAL_PROCESSOR_STATE_TYPE = -2147483640
elif ARCH in 'X64':
    WHV_VIRTUAL_PROCESSOR_STATE_TYPE = Int32
    WHvVirtualProcessorStateTypeSynicMessagePage: win32more.Windows.Win32.System.Hypervisor.WHV_VIRTUAL_PROCESSOR_STATE_TYPE = 0
    WHvVirtualProcessorStateTypeSynicEventFlagPage: win32more.Windows.Win32.System.Hypervisor.WHV_VIRTUAL_PROCESSOR_STATE_TYPE = 1
    WHvVirtualProcessorStateTypeSynicTimerState: win32more.Windows.Win32.System.Hypervisor.WHV_VIRTUAL_PROCESSOR_STATE_TYPE = 2
    WHvVirtualProcessorStateTypeInterruptControllerState2: win32more.Windows.Win32.System.Hypervisor.WHV_VIRTUAL_PROCESSOR_STATE_TYPE = 4096
    WHvVirtualProcessorStateTypeXsaveState: win32more.Windows.Win32.System.Hypervisor.WHV_VIRTUAL_PROCESSOR_STATE_TYPE = 4097
    WHvVirtualProcessorStateTypeNestedState: win32more.Windows.Win32.System.Hypervisor.WHV_VIRTUAL_PROCESSOR_STATE_TYPE = 4098
if ARCH in 'X64,ARM64':
    class WHV_VPCI_DEVICE_NOTIFICATION(Structure):
        NotificationType: win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_DEVICE_NOTIFICATION_TYPE
        Reserved1: UInt32
        Anonymous: _Anonymous_e__Union
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Union(Union):
            Reserved2: UInt64
if ARCH in 'X64,ARM64':
    WHV_VPCI_DEVICE_NOTIFICATION_TYPE = Int32
    WHvVpciDeviceNotificationUndefined: win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_DEVICE_NOTIFICATION_TYPE = 0
    WHvVpciDeviceNotificationMmioRemapping: win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_DEVICE_NOTIFICATION_TYPE = 1
    WHvVpciDeviceNotificationSurpriseRemoval: win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_DEVICE_NOTIFICATION_TYPE = 2
if ARCH in 'X64,ARM64':
    WHV_VPCI_DEVICE_PROPERTY_CODE = Int32
    WHvVpciDevicePropertyCodeUndefined: win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_DEVICE_PROPERTY_CODE = 0
    WHvVpciDevicePropertyCodeHardwareIDs: win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_DEVICE_PROPERTY_CODE = 1
    WHvVpciDevicePropertyCodeProbedBARs: win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_DEVICE_PROPERTY_CODE = 2
if ARCH in 'X64,ARM64':
    class WHV_VPCI_DEVICE_REGISTER(Structure):
        Location: win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_DEVICE_REGISTER_SPACE
        SizeInBytes: UInt32
        OffsetInBytes: UInt64
if ARCH in 'X64,ARM64':
    WHV_VPCI_DEVICE_REGISTER_SPACE = Int32
    WHvVpciConfigSpace: win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_DEVICE_REGISTER_SPACE = -1
    WHvVpciBar0: win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_DEVICE_REGISTER_SPACE = 0
    WHvVpciBar1: win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_DEVICE_REGISTER_SPACE = 1
    WHvVpciBar2: win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_DEVICE_REGISTER_SPACE = 2
    WHvVpciBar3: win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_DEVICE_REGISTER_SPACE = 3
    WHvVpciBar4: win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_DEVICE_REGISTER_SPACE = 4
    WHvVpciBar5: win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_DEVICE_REGISTER_SPACE = 5
if ARCH in 'X64,ARM64':
    class WHV_VPCI_HARDWARE_IDS(Structure):
        VendorID: UInt16
        DeviceID: UInt16
        RevisionID: Byte
        ProgIf: Byte
        SubClass: Byte
        BaseClass: Byte
        SubVendorID: UInt16
        SubSystemID: UInt16
if ARCH in 'X64,ARM64':
    class WHV_VPCI_INTERRUPT_TARGET(Structure):
        Vector: UInt32
        Flags: win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_INTERRUPT_TARGET_FLAGS
        ProcessorCount: UInt32
        Processors: FlexibleArray[UInt32]
if ARCH in 'X64,ARM64':
    WHV_VPCI_INTERRUPT_TARGET_FLAGS = Int32
    WHvVpciInterruptTargetFlagNone: win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_INTERRUPT_TARGET_FLAGS = 0
    WHvVpciInterruptTargetFlagMulticast: win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_INTERRUPT_TARGET_FLAGS = 1
if ARCH in 'X64,ARM64':
    class WHV_VPCI_MMIO_MAPPING(Structure):
        Location: win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_DEVICE_REGISTER_SPACE
        Flags: win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_MMIO_RANGE_FLAGS
        SizeInBytes: UInt64
        OffsetInBytes: UInt64
        VirtualAddress: VoidPtr
if ARCH in 'X64,ARM64':
    WHV_VPCI_MMIO_RANGE_FLAGS = Int32
    WHvVpciMmioRangeFlagReadAccess: win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_MMIO_RANGE_FLAGS = 1
    WHvVpciMmioRangeFlagWriteAccess: win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_MMIO_RANGE_FLAGS = 2
if ARCH in 'X64,ARM64':
    class WHV_VPCI_PROBED_BARS(Structure):
        Value: UInt32 * 6
if ARCH in 'X64':
    class WHV_VP_EXCEPTION_CONTEXT(Structure):
        InstructionByteCount: Byte
        Reserved: Byte * 3
        InstructionBytes: Byte * 16
        ExceptionInfo: win32more.Windows.Win32.System.Hypervisor.WHV_VP_EXCEPTION_INFO
        ExceptionType: Byte
        Reserved2: Byte * 3
        ErrorCode: UInt32
        ExceptionParameter: UInt64
if ARCH in 'X64':
    class WHV_VP_EXCEPTION_INFO(Union):
        Anonymous: _Anonymous_e__Struct
        AsUINT32: UInt32
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            ErrorCodeValid: Annotated[UInt32, NativeBitfieldAttribute(1)]
            SoftwareException: Annotated[UInt32, NativeBitfieldAttribute(1)]
            Reserved: Annotated[UInt32, NativeBitfieldAttribute(30)]
if ARCH in 'ARM64':
    class WHV_VP_EXECUTION_STATE(Union):
        AsUINT16: UInt16
        Anonymous: _Anonymous_e__Struct
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            Cpl: Annotated[UInt16, NativeBitfieldAttribute(2)]
            DebugActive: Annotated[UInt16, NativeBitfieldAttribute(1)]
            InterruptionPending: Annotated[UInt16, NativeBitfieldAttribute(1)]
            Vtl: Annotated[UInt16, NativeBitfieldAttribute(4)]
            VirtualizationFaultActive: Annotated[UInt16, NativeBitfieldAttribute(1)]
            Reserved: Annotated[UInt16, NativeBitfieldAttribute(7)]
if ARCH in 'X64,ARM64':
    class WHV_VTL_PERMISSION_SET(Union):
        AsUINT32: UInt32
        Anonymous: _Anonymous_e__Struct
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            VtlPermissionFrom1: UInt16 * 2
if ARCH in 'X64':
    class WHV_X64_APIC_EOI_CONTEXT(Structure):
        InterruptVector: UInt32
if ARCH in 'X64':
    class WHV_X64_APIC_INIT_SIPI_CONTEXT(Structure):
        ApicIcr: UInt64
if ARCH in 'X64':
    class WHV_X64_APIC_SMI_CONTEXT(Structure):
        ApicIcr: UInt64
if ARCH in 'X64':
    class WHV_X64_APIC_WRITE_CONTEXT(Structure):
        Type: win32more.Windows.Win32.System.Hypervisor.WHV_X64_APIC_WRITE_TYPE
        Reserved: UInt32
        WriteValue: UInt64
if ARCH in 'X64':
    WHV_X64_APIC_WRITE_TYPE = Int32
    WHvX64ApicWriteTypeLdr: win32more.Windows.Win32.System.Hypervisor.WHV_X64_APIC_WRITE_TYPE = 208
    WHvX64ApicWriteTypeDfr: win32more.Windows.Win32.System.Hypervisor.WHV_X64_APIC_WRITE_TYPE = 224
    WHvX64ApicWriteTypeSvr: win32more.Windows.Win32.System.Hypervisor.WHV_X64_APIC_WRITE_TYPE = 240
    WHvX64ApicWriteTypeLint0: win32more.Windows.Win32.System.Hypervisor.WHV_X64_APIC_WRITE_TYPE = 848
    WHvX64ApicWriteTypeLint1: win32more.Windows.Win32.System.Hypervisor.WHV_X64_APIC_WRITE_TYPE = 864
if ARCH in 'X64':
    class WHV_X64_CPUID_ACCESS_CONTEXT(Structure):
        Rax: UInt64
        Rcx: UInt64
        Rdx: UInt64
        Rbx: UInt64
        DefaultResultRax: UInt64
        DefaultResultRcx: UInt64
        DefaultResultRdx: UInt64
        DefaultResultRbx: UInt64
if ARCH in 'X64':
    class WHV_X64_CPUID_RESULT(Structure):
        Function: UInt32
        Reserved: UInt32 * 3
        Eax: UInt32
        Ebx: UInt32
        Ecx: UInt32
        Edx: UInt32
if ARCH in 'X64':
    class WHV_X64_CPUID_RESULT2(Structure):
        Function: UInt32
        Index: UInt32
        VpIndex: UInt32
        Flags: win32more.Windows.Win32.System.Hypervisor.WHV_X64_CPUID_RESULT2_FLAGS
        Output: win32more.Windows.Win32.System.Hypervisor.WHV_CPUID_OUTPUT
        Mask: win32more.Windows.Win32.System.Hypervisor.WHV_CPUID_OUTPUT
if ARCH in 'X64':
    WHV_X64_CPUID_RESULT2_FLAGS = Int32
    WHvX64CpuidResult2FlagSubleafSpecific: win32more.Windows.Win32.System.Hypervisor.WHV_X64_CPUID_RESULT2_FLAGS = 1
    WHvX64CpuidResult2FlagVpSpecific: win32more.Windows.Win32.System.Hypervisor.WHV_X64_CPUID_RESULT2_FLAGS = 2
if ARCH in 'X64':
    class WHV_X64_FP_CONTROL_STATUS_REGISTER(Union):
        Anonymous: _Anonymous_e__Struct
        AsUINT128: win32more.Windows.Win32.System.Hypervisor.WHV_UINT128
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            FpControl: UInt16
            FpStatus: UInt16
            FpTag: Byte
            Reserved: Byte
            LastFpOp: UInt16
            Anonymous: _Anonymous_e__Union
            _anonymous_ = ('Anonymous',)
            class _Anonymous_e__Union(Union):
                LastFpRip: UInt64
                Anonymous: _Anonymous_e__Struct
                _anonymous_ = ('Anonymous',)
                class _Anonymous_e__Struct(Structure):
                    LastFpEip: UInt32
                    LastFpCs: UInt16
                    Reserved2: UInt16
if ARCH in 'X64':
    class WHV_X64_FP_REGISTER(Union):
        Anonymous: _Anonymous_e__Struct
        AsUINT128: win32more.Windows.Win32.System.Hypervisor.WHV_UINT128
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            Mantissa: UInt64
            BiasedExponent: Annotated[UInt64, NativeBitfieldAttribute(15)]
            Sign: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved: Annotated[UInt64, NativeBitfieldAttribute(48)]
if ARCH in 'X64':
    class WHV_X64_HYPERCALL_CONTEXT(Structure):
        Rax: UInt64
        Rbx: UInt64
        Rcx: UInt64
        Rdx: UInt64
        R8: UInt64
        Rsi: UInt64
        Rdi: UInt64
        Reserved0: UInt64
        XmmRegisters: win32more.Windows.Win32.System.Hypervisor.WHV_UINT128 * 6
        Reserved1: UInt64 * 2
if ARCH in 'X64':
    class WHV_X64_INTERRUPTION_DELIVERABLE_CONTEXT(Structure):
        DeliverableType: win32more.Windows.Win32.System.Hypervisor.WHV_X64_PENDING_INTERRUPTION_TYPE
if ARCH in 'X64':
    class WHV_X64_INTERRUPT_STATE_REGISTER(Union):
        Anonymous: _Anonymous_e__Struct
        AsUINT64: UInt64
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            InterruptShadow: Annotated[UInt64, NativeBitfieldAttribute(1)]
            NmiMasked: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved: Annotated[UInt64, NativeBitfieldAttribute(62)]
if ARCH in 'X64':
    class WHV_X64_IO_PORT_ACCESS_CONTEXT(Structure):
        InstructionByteCount: Byte
        Reserved: Byte * 3
        InstructionBytes: Byte * 16
        AccessInfo: win32more.Windows.Win32.System.Hypervisor.WHV_X64_IO_PORT_ACCESS_INFO
        PortNumber: UInt16
        Reserved2: UInt16 * 3
        Rax: UInt64
        Rcx: UInt64
        Rsi: UInt64
        Rdi: UInt64
        Ds: win32more.Windows.Win32.System.Hypervisor.WHV_X64_SEGMENT_REGISTER
        Es: win32more.Windows.Win32.System.Hypervisor.WHV_X64_SEGMENT_REGISTER
if ARCH in 'X64':
    class WHV_X64_IO_PORT_ACCESS_INFO(Union):
        Anonymous: _Anonymous_e__Struct
        AsUINT32: UInt32
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            IsWrite: Annotated[UInt32, NativeBitfieldAttribute(1)]
            AccessSize: Annotated[UInt32, NativeBitfieldAttribute(3)]
            StringOp: Annotated[UInt32, NativeBitfieldAttribute(1)]
            RepPrefix: Annotated[UInt32, NativeBitfieldAttribute(1)]
            Reserved: Annotated[UInt32, NativeBitfieldAttribute(26)]
if ARCH in 'X64':
    WHV_X64_LOCAL_APIC_EMULATION_MODE = Int32
    WHvX64LocalApicEmulationModeNone: win32more.Windows.Win32.System.Hypervisor.WHV_X64_LOCAL_APIC_EMULATION_MODE = 0
    WHvX64LocalApicEmulationModeXApic: win32more.Windows.Win32.System.Hypervisor.WHV_X64_LOCAL_APIC_EMULATION_MODE = 1
    WHvX64LocalApicEmulationModeX2Apic: win32more.Windows.Win32.System.Hypervisor.WHV_X64_LOCAL_APIC_EMULATION_MODE = 2
if ARCH in 'X64':
    class WHV_X64_MSR_ACCESS_CONTEXT(Structure):
        AccessInfo: win32more.Windows.Win32.System.Hypervisor.WHV_X64_MSR_ACCESS_INFO
        MsrNumber: UInt32
        Rax: UInt64
        Rdx: UInt64
if ARCH in 'X64':
    class WHV_X64_MSR_ACCESS_INFO(Union):
        Anonymous: _Anonymous_e__Struct
        AsUINT32: UInt32
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            IsWrite: Annotated[UInt32, NativeBitfieldAttribute(1)]
            Reserved: Annotated[UInt32, NativeBitfieldAttribute(31)]
if ARCH in 'X64':
    class WHV_X64_MSR_EXIT_BITMAP(Union):
        AsUINT64: UInt64
        Anonymous: _Anonymous_e__Struct
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            UnhandledMsrs: Annotated[UInt64, NativeBitfieldAttribute(1)]
            TscMsrWrite: Annotated[UInt64, NativeBitfieldAttribute(1)]
            TscMsrRead: Annotated[UInt64, NativeBitfieldAttribute(1)]
            ApicBaseMsrWrite: Annotated[UInt64, NativeBitfieldAttribute(1)]
            MiscEnableMsrRead: Annotated[UInt64, NativeBitfieldAttribute(1)]
            McUpdatePatchLevelMsrRead: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved: Annotated[UInt64, NativeBitfieldAttribute(58)]
if ARCH in 'X64':
    class WHV_X64_NESTED_GUEST_STATE(Union):
        Anonymous: _Anonymous_e__Struct
        AsUINT128: win32more.Windows.Win32.System.Hypervisor.WHV_UINT128
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            NestedVirtActive: Annotated[UInt64, NativeBitfieldAttribute(1)]
            NestedGuestMode: Annotated[UInt64, NativeBitfieldAttribute(1)]
            VmEntryPending: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved0: Annotated[UInt64, NativeBitfieldAttribute(61)]
            Reserved1: UInt64
if ARCH in 'X64':
    class WHV_X64_NESTED_INVEPT_REGISTER(Union):
        Anonymous: _Anonymous_e__Struct
        AsUINT128: win32more.Windows.Win32.System.Hypervisor.WHV_UINT128
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            Type: Byte
            Reserved: Byte * 7
            Eptp: UInt64
if ARCH in 'X64':
    class WHV_X64_NESTED_INVVPID_REGISTER(Union):
        Anonymous: _Anonymous_e__Struct
        AsUINT128: win32more.Windows.Win32.System.Hypervisor.WHV_UINT128
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            Type: Byte
            Reserved: Byte * 3
            Vpid: UInt32
            LinearAddress: UInt64
if ARCH in 'X64,ARM64':
    class WHV_X64_NESTED_STATE(Union):
        Vmx: win32more.Windows.Win32.System.Hypervisor.WHV_X64_VMX_NESTED_STATE
        Svm: win32more.Windows.Win32.System.Hypervisor.WHV_X64_SVM_NESTED_STATE
if ARCH in 'X64':
    class WHV_X64_PENDING_DEBUG_EXCEPTION(Union):
        AsUINT64: UInt64
        Anonymous: _Anonymous_e__Struct
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            Breakpoint0: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Breakpoint1: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Breakpoint2: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Breakpoint3: Annotated[UInt64, NativeBitfieldAttribute(1)]
            SingleStep: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved0: Annotated[UInt64, NativeBitfieldAttribute(59)]
if ARCH in 'X64':
    WHV_X64_PENDING_EVENT_TYPE = Int32
    WHvX64PendingEventException: win32more.Windows.Win32.System.Hypervisor.WHV_X64_PENDING_EVENT_TYPE = 0
    WHvX64PendingEventExtInt: win32more.Windows.Win32.System.Hypervisor.WHV_X64_PENDING_EVENT_TYPE = 5
    WHvX64PendingEventSvmNestedExit: win32more.Windows.Win32.System.Hypervisor.WHV_X64_PENDING_EVENT_TYPE = 7
    WHvX64PendingEventVmxNestedExit: win32more.Windows.Win32.System.Hypervisor.WHV_X64_PENDING_EVENT_TYPE = 8
if ARCH in 'X64':
    class WHV_X64_PENDING_EXCEPTION_EVENT(Union):
        Anonymous: _Anonymous_e__Struct
        AsUINT128: win32more.Windows.Win32.System.Hypervisor.WHV_UINT128
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            EventPending: Annotated[UInt32, NativeBitfieldAttribute(1)]
            EventType: Annotated[UInt32, NativeBitfieldAttribute(3)]
            Reserved0: Annotated[UInt32, NativeBitfieldAttribute(4)]
            DeliverErrorCode: Annotated[UInt32, NativeBitfieldAttribute(1)]
            Reserved1: Annotated[UInt32, NativeBitfieldAttribute(7)]
            Vector: Annotated[UInt32, NativeBitfieldAttribute(16)]
            ErrorCode: UInt32
            ExceptionParameter: UInt64
if ARCH in 'X64':
    class WHV_X64_PENDING_EXT_INT_EVENT(Union):
        Anonymous: _Anonymous_e__Struct
        AsUINT128: win32more.Windows.Win32.System.Hypervisor.WHV_UINT128
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            EventPending: Annotated[UInt64, NativeBitfieldAttribute(1)]
            EventType: Annotated[UInt64, NativeBitfieldAttribute(3)]
            Reserved0: Annotated[UInt64, NativeBitfieldAttribute(4)]
            Vector: Annotated[UInt64, NativeBitfieldAttribute(8)]
            Reserved1: Annotated[UInt64, NativeBitfieldAttribute(48)]
            Reserved2: UInt64
if ARCH in 'X64':
    class WHV_X64_PENDING_INTERRUPTION_REGISTER(Union):
        Anonymous: _Anonymous_e__Struct
        AsUINT64: UInt64
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            InterruptionPending: Annotated[UInt32, NativeBitfieldAttribute(1)]
            InterruptionType: Annotated[UInt32, NativeBitfieldAttribute(3)]
            DeliverErrorCode: Annotated[UInt32, NativeBitfieldAttribute(1)]
            InstructionLength: Annotated[UInt32, NativeBitfieldAttribute(4)]
            NestedEvent: Annotated[UInt32, NativeBitfieldAttribute(1)]
            Reserved: Annotated[UInt32, NativeBitfieldAttribute(6)]
            InterruptionVector: Annotated[UInt32, NativeBitfieldAttribute(16)]
            ErrorCode: UInt32
if ARCH in 'X64':
    WHV_X64_PENDING_INTERRUPTION_TYPE = Int32
    WHvX64PendingInterrupt: win32more.Windows.Win32.System.Hypervisor.WHV_X64_PENDING_INTERRUPTION_TYPE = 0
    WHvX64PendingNmi: win32more.Windows.Win32.System.Hypervisor.WHV_X64_PENDING_INTERRUPTION_TYPE = 2
    WHvX64PendingException: win32more.Windows.Win32.System.Hypervisor.WHV_X64_PENDING_INTERRUPTION_TYPE = 3
if ARCH in 'X64':
    class WHV_X64_PENDING_SVM_NESTED_EXIT_EVENT0(Union):
        Anonymous: _Anonymous_e__Struct
        AsUINT128: win32more.Windows.Win32.System.Hypervisor.WHV_UINT128
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            EventPending: Annotated[UInt64, NativeBitfieldAttribute(1)]
            EventType: Annotated[UInt64, NativeBitfieldAttribute(4)]
            Reserved0: Annotated[UInt64, NativeBitfieldAttribute(3)]
            InstructionBytesValid: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved1: Annotated[UInt64, NativeBitfieldAttribute(55)]
            ExitCode: UInt64
if ARCH in 'X64':
    class WHV_X64_PENDING_SVM_NESTED_EXIT_EVENT1(Union):
        Anonymous: _Anonymous_e__Struct
        AsUINT128: win32more.Windows.Win32.System.Hypervisor.WHV_UINT128
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            ExitInfo1: UInt64
            ExitInfo2: UInt64
if ARCH in 'X64':
    class WHV_X64_PENDING_SVM_NESTED_EXIT_EVENT2(Union):
        Anonymous: _Anonymous_e__Struct
        AsUINT128: win32more.Windows.Win32.System.Hypervisor.WHV_UINT128
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            NextRip: UInt64
            InstructionBytesFetchedCount: Byte
            InstructionBytes: Byte * 7
if ARCH in 'X64':
    class WHV_X64_PENDING_SVM_NESTED_EXIT_EVENT3(Union):
        Anonymous: _Anonymous_e__Struct
        AsUINT128: win32more.Windows.Win32.System.Hypervisor.WHV_UINT128
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            InstructionBytes: Byte * 8
            Reserved2: UInt64
if ARCH in 'X64':
    class WHV_X64_PENDING_VMX_NESTED_EXIT_EVENT0(Union):
        Anonymous: _Anonymous_e__Struct
        AsUINT128: win32more.Windows.Win32.System.Hypervisor.WHV_UINT128
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            EventPending: Annotated[UInt32, NativeBitfieldAttribute(1)]
            EventType: Annotated[UInt32, NativeBitfieldAttribute(4)]
            Reserved0: Annotated[UInt32, NativeBitfieldAttribute(27)]
            ExitReason: UInt32
            ExitQualification: UInt64
if ARCH in 'X64':
    class WHV_X64_PENDING_VMX_NESTED_EXIT_EVENT1(Union):
        Anonymous: _Anonymous_e__Struct
        AsUINT128: win32more.Windows.Win32.System.Hypervisor.WHV_UINT128
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            InstructionLength: UInt32
            InstructionInfo: UInt32
            ExitInterruptionInfo: UInt32
            ExitExceptionErrorCode: UInt32
if ARCH in 'X64':
    class WHV_X64_PENDING_VMX_NESTED_EXIT_EVENT2(Union):
        Anonymous: _Anonymous_e__Struct
        AsUINT128: win32more.Windows.Win32.System.Hypervisor.WHV_UINT128
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            GuestLinearAddress: UInt64
            GuestPhysicalAddress: UInt64
if ARCH in 'X64':
    class WHV_X64_PENDING_VMX_NESTED_EXIT_EVENT3(Union):
        Anonymous: _Anonymous_e__Struct
        AsUINT128: win32more.Windows.Win32.System.Hypervisor.WHV_UINT128
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            MsrData: UInt64
if ARCH in 'X64':
    class WHV_X64_PROCESSOR_FEATURES(Union):
        Anonymous: _Anonymous_e__Struct
        AsUINT64: UInt64
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            Sse3Support: Annotated[UInt64, NativeBitfieldAttribute(1)]
            LahfSahfSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Ssse3Support: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Sse4_1Support: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Sse4_2Support: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Sse4aSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            XopSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            PopCntSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Cmpxchg16bSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Altmovcr8Support: Annotated[UInt64, NativeBitfieldAttribute(1)]
            LzcntSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            MisAlignSseSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            MmxExtSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Amd3DNowSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            ExtendedAmd3DNowSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Page1GbSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            AesSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            PclmulqdqSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            PcidSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Fma4Support: Annotated[UInt64, NativeBitfieldAttribute(1)]
            F16CSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            RdRandSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            RdWrFsGsSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            SmepSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            EnhancedFastStringSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Bmi1Support: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Bmi2Support: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved1: Annotated[UInt64, NativeBitfieldAttribute(2)]
            MovbeSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Npiep1Support: Annotated[UInt64, NativeBitfieldAttribute(1)]
            DepX87FPUSaveSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            RdSeedSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            AdxSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            IntelPrefetchSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            SmapSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            HleSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            RtmSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            RdtscpSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            ClflushoptSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            ClwbSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            ShaSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            X87PointersSavedSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            InvpcidSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            IbrsSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            StibpSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            IbpbSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            UnrestrictedGuestSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            SsbdSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            FastShortRepMovSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved3: Annotated[UInt64, NativeBitfieldAttribute(1)]
            RdclNo: Annotated[UInt64, NativeBitfieldAttribute(1)]
            IbrsAllSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved4: Annotated[UInt64, NativeBitfieldAttribute(1)]
            SsbNo: Annotated[UInt64, NativeBitfieldAttribute(1)]
            RsbANo: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved5: Annotated[UInt64, NativeBitfieldAttribute(1)]
            RdPidSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            UmipSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            MdsNoSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            MdClearSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            TaaNoSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            TsxCtrlSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved6: Annotated[UInt64, NativeBitfieldAttribute(1)]
if ARCH in 'X64':
    class WHV_X64_PROCESSOR_FEATURES1(Union):
        Anonymous: _Anonymous_e__Struct
        AsUINT64: UInt64
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            ACountMCountSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            TscInvariantSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            ClZeroSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            RdpruSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            La57Support: Annotated[UInt64, NativeBitfieldAttribute(1)]
            MbecSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            NestedVirtSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            PsfdSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            CetSsSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            CetIbtSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            VmxExceptionInjectSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved2: Annotated[UInt64, NativeBitfieldAttribute(1)]
            UmwaitTpauseSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            MovdiriSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Movdir64bSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            CldemoteSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            SerializeSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            TscDeadlineTmrSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            TscAdjustSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            FZLRepMovsb: Annotated[UInt64, NativeBitfieldAttribute(1)]
            FSRepStosb: Annotated[UInt64, NativeBitfieldAttribute(1)]
            FSRepCmpsb: Annotated[UInt64, NativeBitfieldAttribute(1)]
            TsxLdTrkSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            VmxInsOutsExitInfoSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved3: Annotated[UInt64, NativeBitfieldAttribute(1)]
            SbdrSsdpNoSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            FbsdpNoSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            PsdpNoSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            FbClearSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            BtcNoSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            IbpbRsbFlushSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            StibpAlwaysOnSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            PerfGlobalCtrlSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            NptExecuteOnlySupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            NptADFlagsSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Npt1GbPageSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved4: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved5: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved6: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved7: Annotated[UInt64, NativeBitfieldAttribute(1)]
            CmpccxaddSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved8: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved9: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved10: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved11: Annotated[UInt64, NativeBitfieldAttribute(1)]
            PrefetchISupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Sha512Support: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved12: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved13: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved14: Annotated[UInt64, NativeBitfieldAttribute(1)]
            SM3Support: Annotated[UInt64, NativeBitfieldAttribute(1)]
            SM4Support: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved15: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved16: Annotated[UInt64, NativeBitfieldAttribute(1)]
            SbpbSupported: Annotated[UInt64, NativeBitfieldAttribute(1)]
            IbpbBrTypeSupported: Annotated[UInt64, NativeBitfieldAttribute(1)]
            SrsoNoSupported: Annotated[UInt64, NativeBitfieldAttribute(1)]
            SrsoUserKernelNoSupported: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved17: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved18: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved19: Annotated[UInt64, NativeBitfieldAttribute(1)]
            LassSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            IdleHltInterceptSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
            MsrListSupport: Annotated[UInt64, NativeBitfieldAttribute(1)]
if ARCH in 'X64':
    class WHV_X64_RDTSC_CONTEXT(Structure):
        TscAux: UInt64
        VirtualOffset: UInt64
        Tsc: UInt64
        ReferenceTime: UInt64
        RdtscInfo: win32more.Windows.Win32.System.Hypervisor.WHV_X64_RDTSC_INFO
if ARCH in 'X64':
    class WHV_X64_RDTSC_INFO(Union):
        Anonymous: _Anonymous_e__Struct
        AsUINT64: UInt64
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            IsRdtscp: Annotated[UInt64, NativeBitfieldAttribute(1)]
            Reserved: Annotated[UInt64, NativeBitfieldAttribute(63)]
if ARCH in 'X64':
    class WHV_X64_SEGMENT_REGISTER(Structure):
        Base: UInt64
        Limit: UInt32
        Selector: UInt16
        Anonymous: _Anonymous_e__Union
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Union(Union):
            Anonymous: _Anonymous_e__Struct
            Attributes: UInt16
            _anonymous_ = ('Anonymous',)
            class _Anonymous_e__Struct(Structure):
                SegmentType: Annotated[UInt16, NativeBitfieldAttribute(4)]
                NonSystemSegment: Annotated[UInt16, NativeBitfieldAttribute(1)]
                DescriptorPrivilegeLevel: Annotated[UInt16, NativeBitfieldAttribute(2)]
                Present: Annotated[UInt16, NativeBitfieldAttribute(1)]
                Reserved: Annotated[UInt16, NativeBitfieldAttribute(4)]
                Available: Annotated[UInt16, NativeBitfieldAttribute(1)]
                Long: Annotated[UInt16, NativeBitfieldAttribute(1)]
                Default: Annotated[UInt16, NativeBitfieldAttribute(1)]
                Granularity: Annotated[UInt16, NativeBitfieldAttribute(1)]
if ARCH in 'X64,ARM64':
    class WHV_X64_SVM_NESTED_STATE(Structure):
        Vendor: win32more.Windows.Win32.System.Hypervisor.WHV_NESTED_STATE_TYPE
        Flags: _Flags_e__Struct
        NestedEnlightenmentsControl: win32more.Windows.Win32.System.Hypervisor.WHV_NESTED_ENLIGHTENMENTS_CONTROL
        HostSaveGpa: UInt64
        VmControlMsr: UInt64
        VirtualTscRatioMsr: UInt64
        VmcbGpa: UInt64
        HostState: win32more.Windows.Win32.System.Hypervisor.WHV_SVM_NESTED_HOST_STATE
        Reserved: Byte * 3832
        VmcbBytes: Byte * 4096
        class _Flags_e__Struct(Structure):
            GuestMode: Annotated[UInt32, NativeBitfieldAttribute(1)]
            VmEntryPending: Annotated[UInt32, NativeBitfieldAttribute(1)]
            HostSaveGpaValid: Annotated[UInt32, NativeBitfieldAttribute(1)]
            CurrentVmcbValid: Annotated[UInt32, NativeBitfieldAttribute(1)]
            Reserved: Annotated[UInt32, NativeBitfieldAttribute(28)]
if ARCH in 'X64':
    class WHV_X64_TABLE_REGISTER(Structure):
        Pad: UInt16 * 3
        Limit: UInt16
        Base: UInt64
if ARCH in 'X64':
    WHV_X64_UNSUPPORTED_FEATURE_CODE = Int32
    WHvUnsupportedFeatureIntercept: win32more.Windows.Win32.System.Hypervisor.WHV_X64_UNSUPPORTED_FEATURE_CODE = 1
    WHvUnsupportedFeatureTaskSwitchTss: win32more.Windows.Win32.System.Hypervisor.WHV_X64_UNSUPPORTED_FEATURE_CODE = 2
if ARCH in 'X64':
    class WHV_X64_UNSUPPORTED_FEATURE_CONTEXT(Structure):
        FeatureCode: win32more.Windows.Win32.System.Hypervisor.WHV_X64_UNSUPPORTED_FEATURE_CODE
        Reserved: UInt32
        FeatureParameter: UInt64
if ARCH in 'X64,ARM64':
    class WHV_X64_VMX_NESTED_STATE(Structure):
        Vendor: win32more.Windows.Win32.System.Hypervisor.WHV_NESTED_STATE_TYPE
        Flags: _Flags_e__Struct
        NestedEnlightenmentsControl: win32more.Windows.Win32.System.Hypervisor.WHV_NESTED_ENLIGHTENMENTS_CONTROL
        Pdpt: UInt64 * 4
        VmxonRegionGpa: UInt64
        VmcsGpa: UInt64
        CurrentEnlightenedVmcs: UInt64
        VirtualApicRegs: _VirtualApicRegs_e__Struct
        Reserved: Byte * 3944
        VmcsBytes: Byte * 4096
        class _Flags_e__Struct(Structure):
            GuestMode: Annotated[UInt32, NativeBitfieldAttribute(1)]
            Vmxon: Annotated[UInt32, NativeBitfieldAttribute(1)]
            CurrentVmcsValid: Annotated[UInt32, NativeBitfieldAttribute(1)]
            VmEntryPending: Annotated[UInt32, NativeBitfieldAttribute(1)]
            VmcsEnlightened: Annotated[UInt32, NativeBitfieldAttribute(1)]
            EnlightenedVmEntry: Annotated[UInt32, NativeBitfieldAttribute(1)]
            Reserved: Annotated[UInt32, NativeBitfieldAttribute(26)]
        class _VirtualApicRegs_e__Struct(Structure):
            Tpr: UInt32
            Ppr: UInt32
            Isr: UInt32 * 8
            Irr: UInt32 * 8
            IcrLow: UInt32
            IcrHigh: UInt32
if ARCH in 'X64':
    class WHV_X64_VP_EXECUTION_STATE(Union):
        Anonymous: _Anonymous_e__Struct
        AsUINT16: UInt16
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            Cpl: Annotated[UInt16, NativeBitfieldAttribute(2)]
            Cr0Pe: Annotated[UInt16, NativeBitfieldAttribute(1)]
            Cr0Am: Annotated[UInt16, NativeBitfieldAttribute(1)]
            EferLma: Annotated[UInt16, NativeBitfieldAttribute(1)]
            DebugActive: Annotated[UInt16, NativeBitfieldAttribute(1)]
            InterruptionPending: Annotated[UInt16, NativeBitfieldAttribute(1)]
            Reserved0: Annotated[UInt16, NativeBitfieldAttribute(5)]
            InterruptShadow: Annotated[UInt16, NativeBitfieldAttribute(1)]
            Reserved1: Annotated[UInt16, NativeBitfieldAttribute(3)]
if ARCH in 'X64':
    class WHV_X64_VP_EXIT_CONTEXT(Structure):
        ExecutionState: win32more.Windows.Win32.System.Hypervisor.WHV_X64_VP_EXECUTION_STATE
        InstructionLength: Annotated[Byte, NativeBitfieldAttribute(4)]
        Cr8: Annotated[Byte, NativeBitfieldAttribute(4)]
        Reserved: Byte
        Reserved2: UInt32
        Cs: win32more.Windows.Win32.System.Hypervisor.WHV_X64_SEGMENT_REGISTER
        Rip: UInt64
        Rflags: UInt64
if ARCH in 'X64':
    class WHV_X64_XMM_CONTROL_STATUS_REGISTER(Union):
        Anonymous: _Anonymous_e__Struct
        AsUINT128: win32more.Windows.Win32.System.Hypervisor.WHV_UINT128
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            Anonymous: _Anonymous_e__Union
            XmmStatusControl: UInt32
            XmmStatusControlMask: UInt32
            _anonymous_ = ('Anonymous',)
            class _Anonymous_e__Union(Union):
                LastFpRdp: UInt64
                Anonymous: _Anonymous_e__Struct
                _anonymous_ = ('Anonymous',)
                class _Anonymous_e__Struct(Structure):
                    LastFpDp: UInt32
                    LastFpDs: UInt16
                    Reserved: UInt16


make_ready(__name__)
