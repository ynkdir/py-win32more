from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer, ConstantLazyLoader
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
WHV_PROCESSOR_FEATURES_BANKS_COUNT: UInt32 = 2
WHV_SYNTHETIC_PROCESSOR_FEATURES_BANKS_COUNT: UInt32 = 1
WHV_READ_WRITE_GPA_RANGE_MAX_SIZE: UInt32 = 16
WHV_HYPERCALL_CONTEXT_MAX_XMM_REGISTERS: UInt32 = 6
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
@winfunctype('WinHvPlatform.dll')
def WHvGetCapability(CapabilityCode: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE, CapabilityBuffer: VoidPtr, CapabilityBufferSizeInBytes: UInt32, WrittenSizeInBytes: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvCreatePartition(Partition: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvSetupPartition(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvResetPartition(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvDeletePartition(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvGetPartitionProperty(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, PropertyCode: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE, PropertyBuffer: VoidPtr, PropertyBufferSizeInBytes: UInt32, WrittenSizeInBytes: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvSetPartitionProperty(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, PropertyCode: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE, PropertyBuffer: VoidPtr, PropertyBufferSizeInBytes: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvSuspendPartitionTime(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvResumePartitionTime(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvMapGpaRange(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, SourceAddress: VoidPtr, GuestAddress: UInt64, SizeInBytes: UInt64, Flags: win32more.Windows.Win32.System.Hypervisor.WHV_MAP_GPA_RANGE_FLAGS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvMapGpaRange2(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, Process: win32more.Windows.Win32.Foundation.HANDLE, SourceAddress: VoidPtr, GuestAddress: UInt64, SizeInBytes: UInt64, Flags: win32more.Windows.Win32.System.Hypervisor.WHV_MAP_GPA_RANGE_FLAGS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvUnmapGpaRange(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, GuestAddress: UInt64, SizeInBytes: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvTranslateGva(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, Gva: UInt64, TranslateFlags: win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_FLAGS, TranslationResult: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_RESULT), Gpa: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvCreateVirtualProcessor(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, Flags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvCreateVirtualProcessor2(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, Properties: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_VIRTUAL_PROCESSOR_PROPERTY), PropertyCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvDeleteVirtualProcessor(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvRunVirtualProcessor(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, ExitContext: VoidPtr, ExitContextSizeInBytes: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvCancelRunVirtualProcessor(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, Flags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvGetVirtualProcessorRegisters(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, RegisterNames: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME), RegisterCount: UInt32, RegisterValues: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_VALUE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvSetVirtualProcessorRegisters(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, RegisterNames: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME), RegisterCount: UInt32, RegisterValues: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_VALUE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvGetVirtualProcessorInterruptControllerState(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, State: VoidPtr, StateSize: UInt32, WrittenSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvSetVirtualProcessorInterruptControllerState(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, State: VoidPtr, StateSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvRequestInterrupt(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, Interrupt: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_INTERRUPT_CONTROL), InterruptControlSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvGetVirtualProcessorXsaveState(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, Buffer: VoidPtr, BufferSizeInBytes: UInt32, BytesWritten: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvSetVirtualProcessorXsaveState(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, Buffer: VoidPtr, BufferSizeInBytes: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvQueryGpaRangeDirtyBitmap(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, GuestAddress: UInt64, RangeSizeInBytes: UInt64, Bitmap: POINTER(UInt64), BitmapSizeInBytes: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvGetPartitionCounters(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, CounterSet: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_COUNTER_SET, Buffer: VoidPtr, BufferSizeInBytes: UInt32, BytesWritten: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvGetVirtualProcessorCounters(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, CounterSet: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_COUNTER_SET, Buffer: VoidPtr, BufferSizeInBytes: UInt32, BytesWritten: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvGetVirtualProcessorInterruptControllerState2(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, State: VoidPtr, StateSize: UInt32, WrittenSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvSetVirtualProcessorInterruptControllerState2(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, State: VoidPtr, StateSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvRegisterPartitionDoorbellEvent(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, MatchData: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_DOORBELL_MATCH_DATA), EventHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvUnregisterPartitionDoorbellEvent(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, MatchData: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_DOORBELL_MATCH_DATA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvAdviseGpaRange(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, GpaRanges: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_MEMORY_RANGE_ENTRY), GpaRangesCount: UInt32, Advice: win32more.Windows.Win32.System.Hypervisor.WHV_ADVISE_GPA_RANGE_CODE, AdviceBuffer: VoidPtr, AdviceBufferSizeInBytes: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvReadGpaRange(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, GuestAddress: UInt64, Controls: win32more.Windows.Win32.System.Hypervisor.WHV_ACCESS_GPA_CONTROLS, Data: VoidPtr, DataSizeInBytes: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvWriteGpaRange(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, GuestAddress: UInt64, Controls: win32more.Windows.Win32.System.Hypervisor.WHV_ACCESS_GPA_CONTROLS, Data: VoidPtr, DataSizeInBytes: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvSignalVirtualProcessorSynicEvent(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, SynicEvent: win32more.Windows.Win32.System.Hypervisor.WHV_SYNIC_EVENT_PARAMETERS, NewlySignaled: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvGetVirtualProcessorState(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, StateType: win32more.Windows.Win32.System.Hypervisor.WHV_VIRTUAL_PROCESSOR_STATE_TYPE, Buffer: VoidPtr, BufferSizeInBytes: UInt32, BytesWritten: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvSetVirtualProcessorState(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, StateType: win32more.Windows.Win32.System.Hypervisor.WHV_VIRTUAL_PROCESSOR_STATE_TYPE, Buffer: VoidPtr, BufferSizeInBytes: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvAllocateVpciResource(ProviderId: POINTER(Guid), Flags: win32more.Windows.Win32.System.Hypervisor.WHV_ALLOCATE_VPCI_RESOURCE_FLAGS, ResourceDescriptor: VoidPtr, ResourceDescriptorSizeInBytes: UInt32, VpciResource: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvCreateVpciDevice(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, LogicalDeviceId: UInt64, VpciResource: win32more.Windows.Win32.Foundation.HANDLE, Flags: win32more.Windows.Win32.System.Hypervisor.WHV_CREATE_VPCI_DEVICE_FLAGS, NotificationEventHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvDeleteVpciDevice(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, LogicalDeviceId: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvGetVpciDeviceProperty(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, LogicalDeviceId: UInt64, PropertyCode: win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_DEVICE_PROPERTY_CODE, PropertyBuffer: VoidPtr, PropertyBufferSizeInBytes: UInt32, WrittenSizeInBytes: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvGetVpciDeviceNotification(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, LogicalDeviceId: UInt64, Notification: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_DEVICE_NOTIFICATION), NotificationSizeInBytes: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvMapVpciDeviceMmioRanges(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, LogicalDeviceId: UInt64, MappingCount: POINTER(UInt32), Mappings: POINTER(POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_MMIO_MAPPING))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvUnmapVpciDeviceMmioRanges(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, LogicalDeviceId: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvSetVpciDevicePowerState(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, LogicalDeviceId: UInt64, PowerState: win32more.Windows.Win32.System.Power.DEVICE_POWER_STATE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvReadVpciDeviceRegister(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, LogicalDeviceId: UInt64, Register: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_DEVICE_REGISTER), Data: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvWriteVpciDeviceRegister(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, LogicalDeviceId: UInt64, Register: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_DEVICE_REGISTER), Data: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvMapVpciDeviceInterrupt(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, LogicalDeviceId: UInt64, Index: UInt32, MessageCount: UInt32, Target: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_INTERRUPT_TARGET), MsiAddress: POINTER(UInt64), MsiData: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvUnmapVpciDeviceInterrupt(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, LogicalDeviceId: UInt64, Index: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvRetargetVpciDeviceInterrupt(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, LogicalDeviceId: UInt64, MsiAddress: UInt64, MsiData: UInt32, Target: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_INTERRUPT_TARGET)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvRequestVpciDeviceInterrupt(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, LogicalDeviceId: UInt64, MsiAddress: UInt64, MsiData: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvGetVpciDeviceInterruptTarget(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, LogicalDeviceId: UInt64, Index: UInt32, MultiMessageNumber: UInt32, Target: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_INTERRUPT_TARGET), TargetSizeInBytes: UInt32, BytesWritten: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvCreateTrigger(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, Parameters: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_TRIGGER_PARAMETERS), TriggerHandle: POINTER(VoidPtr), EventHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvUpdateTriggerParameters(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, Parameters: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_TRIGGER_PARAMETERS), TriggerHandle: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvDeleteTrigger(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, TriggerHandle: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvCreateNotificationPort(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, Parameters: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_NOTIFICATION_PORT_PARAMETERS), EventHandle: win32more.Windows.Win32.Foundation.HANDLE, PortHandle: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvSetNotificationPortProperty(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, PortHandle: VoidPtr, PropertyCode: win32more.Windows.Win32.System.Hypervisor.WHV_NOTIFICATION_PORT_PROPERTY_CODE, PropertyValue: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvDeleteNotificationPort(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, PortHandle: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvPostVirtualProcessorSynicMessage(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, SintIndex: UInt32, Message: VoidPtr, MessageSizeInBytes: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvGetVirtualProcessorCpuidOutput(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, Eax: UInt32, Ecx: UInt32, CpuidOutput: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_CPUID_OUTPUT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvGetInterruptTargetVpSet(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, Destination: UInt64, DestinationMode: win32more.Windows.Win32.System.Hypervisor.WHV_INTERRUPT_DESTINATION_MODE, TargetVps: POINTER(UInt32), VpCount: UInt32, TargetVpCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvStartPartitionMigration(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE, MigrationHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvCancelPartitionMigration(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvCompletePartitionMigration(Partition: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvAcceptPartitionMigration(MigrationHandle: win32more.Windows.Win32.Foundation.HANDLE, Partition: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvEmulation.dll')
def WHvEmulatorCreateEmulator(Callbacks: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_EMULATOR_CALLBACKS), Emulator: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvEmulation.dll')
def WHvEmulatorDestroyEmulator(Emulator: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvEmulation.dll')
def WHvEmulatorTryIoEmulation(Emulator: VoidPtr, Context: VoidPtr, VpContext: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_VP_EXIT_CONTEXT), IoInstructionContext: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_X64_IO_PORT_ACCESS_CONTEXT), EmulatorReturnStatus: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_EMULATOR_STATUS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WinHvEmulation.dll')
def WHvEmulatorTryMmioEmulation(Emulator: VoidPtr, Context: VoidPtr, VpContext: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_VP_EXIT_CONTEXT), MmioInstructionContext: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_MEMORY_ACCESS_CONTEXT), EmulatorReturnStatus: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_EMULATOR_STATUS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
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
class DOS_IMAGE_INFO(EasyCastStructure):
    PdbName: win32more.Windows.Win32.Foundation.PSTR
    ImageBaseAddress: UInt64
    ImageSize: UInt32
    Timestamp: UInt32
@winfunctype_pointer
def FOUND_IMAGE_CALLBACK(Context: VoidPtr, ImageInfo: POINTER(win32more.Windows.Win32.System.Hypervisor.DOS_IMAGE_INFO)) -> win32more.Windows.Win32.Foundation.BOOL: ...
class GPA_MEMORY_CHUNK(EasyCastStructure):
    GuestPhysicalStartPageIndex: UInt64
    PageCount: UInt64
class GUEST_OS_INFO(EasyCastUnion):
    AsUINT64: UInt64
    ClosedSource: _ClosedSource_e__Struct
    OpenSource: _OpenSource_e__Struct
    class _ClosedSource_e__Struct(EasyCastStructure):
        _bitfield: UInt64
    class _OpenSource_e__Struct(EasyCastStructure):
        _bitfield: UInt64
GUEST_OS_MICROSOFT_IDS = Int32
GUEST_OS_MICROSOFT_IDS_GuestOsMicrosoftUndefined: win32more.Windows.Win32.System.Hypervisor.GUEST_OS_MICROSOFT_IDS = 0
GUEST_OS_MICROSOFT_IDS_GuestOsMicrosoftMSDOS: win32more.Windows.Win32.System.Hypervisor.GUEST_OS_MICROSOFT_IDS = 1
GUEST_OS_MICROSOFT_IDS_GuestOsMicrosoftWindows3x: win32more.Windows.Win32.System.Hypervisor.GUEST_OS_MICROSOFT_IDS = 2
GUEST_OS_MICROSOFT_IDS_GuestOsMicrosoftWindows9x: win32more.Windows.Win32.System.Hypervisor.GUEST_OS_MICROSOFT_IDS = 3
GUEST_OS_MICROSOFT_IDS_GuestOsMicrosoftWindowsNT: win32more.Windows.Win32.System.Hypervisor.GUEST_OS_MICROSOFT_IDS = 4
GUEST_OS_MICROSOFT_IDS_GuestOsMicrosoftWindowsCE: win32more.Windows.Win32.System.Hypervisor.GUEST_OS_MICROSOFT_IDS = 5
GUEST_OS_OPENSOURCE_IDS = Int32
GUEST_OS_OPENSOURCE_IDS_GuestOsOpenSourceUndefined: win32more.Windows.Win32.System.Hypervisor.GUEST_OS_OPENSOURCE_IDS = 0
GUEST_OS_OPENSOURCE_IDS_GuestOsOpenSourceLinux: win32more.Windows.Win32.System.Hypervisor.GUEST_OS_OPENSOURCE_IDS = 1
GUEST_OS_OPENSOURCE_IDS_GuestOsOpenSourceFreeBSD: win32more.Windows.Win32.System.Hypervisor.GUEST_OS_OPENSOURCE_IDS = 2
GUEST_OS_OPENSOURCE_IDS_GuestOsOpenSourceXen: win32more.Windows.Win32.System.Hypervisor.GUEST_OS_OPENSOURCE_IDS = 3
GUEST_OS_OPENSOURCE_IDS_GuestOsOpenSourceIllumos: win32more.Windows.Win32.System.Hypervisor.GUEST_OS_OPENSOURCE_IDS = 4
GUEST_OS_VENDOR = Int32
GUEST_OS_VENDOR_GuestOsVendorUndefined: win32more.Windows.Win32.System.Hypervisor.GUEST_OS_VENDOR = 0
GUEST_OS_VENDOR_GuestOsVendorMicrosoft: win32more.Windows.Win32.System.Hypervisor.GUEST_OS_VENDOR = 1
GUEST_OS_VENDOR_GuestOsVendorHPE: win32more.Windows.Win32.System.Hypervisor.GUEST_OS_VENDOR = 2
GUEST_OS_VENDOR_GuestOsVendorLANCOM: win32more.Windows.Win32.System.Hypervisor.GUEST_OS_VENDOR = 512
@winfunctype_pointer
def GUEST_SYMBOLS_PROVIDER_DEBUG_INFO_CALLBACK(InfoMessage: win32more.Windows.Win32.Foundation.PSTR) -> Void: ...
HDV_DEVICE_HOST_FLAGS = Int32
HDV_DEVICE_HOST_FLAGS_HdvDeviceHostFlagNone: win32more.Windows.Win32.System.Hypervisor.HDV_DEVICE_HOST_FLAGS = 0
HDV_DEVICE_HOST_FLAGS_HdvDeviceHostFlagInitializeComSecurity: win32more.Windows.Win32.System.Hypervisor.HDV_DEVICE_HOST_FLAGS = 1
HDV_DEVICE_TYPE = Int32
HDV_DEVICE_TYPE_HdvDeviceTypeUndefined: win32more.Windows.Win32.System.Hypervisor.HDV_DEVICE_TYPE = 0
HDV_DEVICE_TYPE_HdvDeviceTypePCI: win32more.Windows.Win32.System.Hypervisor.HDV_DEVICE_TYPE = 1
HDV_DOORBELL_FLAGS = Int32
HDV_DOORBELL_FLAG_TRIGGER_SIZE_ANY: win32more.Windows.Win32.System.Hypervisor.HDV_DOORBELL_FLAGS = 0
HDV_DOORBELL_FLAG_TRIGGER_SIZE_BYTE: win32more.Windows.Win32.System.Hypervisor.HDV_DOORBELL_FLAGS = 1
HDV_DOORBELL_FLAG_TRIGGER_SIZE_WORD: win32more.Windows.Win32.System.Hypervisor.HDV_DOORBELL_FLAGS = 2
HDV_DOORBELL_FLAG_TRIGGER_SIZE_DWORD: win32more.Windows.Win32.System.Hypervisor.HDV_DOORBELL_FLAGS = 3
HDV_DOORBELL_FLAG_TRIGGER_SIZE_QWORD: win32more.Windows.Win32.System.Hypervisor.HDV_DOORBELL_FLAGS = 4
HDV_DOORBELL_FLAG_TRIGGER_ANY_VALUE: win32more.Windows.Win32.System.Hypervisor.HDV_DOORBELL_FLAGS = -2147483648
HDV_MMIO_MAPPING_FLAGS = Int32
HDV_MMIO_MAPPING_FLAGS_HdvMmioMappingFlagNone: win32more.Windows.Win32.System.Hypervisor.HDV_MMIO_MAPPING_FLAGS = 0
HDV_MMIO_MAPPING_FLAGS_HdvMmioMappingFlagWriteable: win32more.Windows.Win32.System.Hypervisor.HDV_MMIO_MAPPING_FLAGS = 1
HDV_MMIO_MAPPING_FLAGS_HdvMmioMappingFlagExecutable: win32more.Windows.Win32.System.Hypervisor.HDV_MMIO_MAPPING_FLAGS = 2
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
class HDV_PCI_DEVICE_INTERFACE(EasyCastStructure):
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
HDV_PCI_INTERFACE_VERSION_HdvPciDeviceInterfaceVersionInvalid: win32more.Windows.Win32.System.Hypervisor.HDV_PCI_INTERFACE_VERSION = 0
HDV_PCI_INTERFACE_VERSION_HdvPciDeviceInterfaceVersion1: win32more.Windows.Win32.System.Hypervisor.HDV_PCI_INTERFACE_VERSION = 1
class HDV_PCI_PNP_ID(EasyCastStructure):
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
class HVSOCKET_ADDRESS_INFO(EasyCastStructure):
    SystemId: Guid
    VirtualMachineId: Guid
    SiloId: Guid
    Flags: UInt32
class MODULE_INFO(EasyCastStructure):
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
class SOCKADDR_HV(EasyCastStructure):
    Family: win32more.Windows.Win32.Networking.WinSock.ADDRESS_FAMILY
    Reserved: UInt16
    VmId: Guid
    ServiceId: Guid
VIRTUAL_PROCESSOR_ARCH = Int32
Arch_Unknown: win32more.Windows.Win32.System.Hypervisor.VIRTUAL_PROCESSOR_ARCH = 0
Arch_x86: win32more.Windows.Win32.System.Hypervisor.VIRTUAL_PROCESSOR_ARCH = 1
Arch_x64: win32more.Windows.Win32.System.Hypervisor.VIRTUAL_PROCESSOR_ARCH = 2
Arch_Armv8: win32more.Windows.Win32.System.Hypervisor.VIRTUAL_PROCESSOR_ARCH = 3
class VIRTUAL_PROCESSOR_REGISTER(EasyCastUnion):
    Reg64: UInt64
    Reg32: UInt32
    Reg16: UInt16
    Reg8: Byte
    Reg128: _Reg128_e__Struct
    X64: _X64_e__Union
    class _Reg128_e__Struct(EasyCastStructure):
        Low64: UInt64
        High64: UInt64
    class _X64_e__Union(EasyCastUnion):
        Segment: _Segment_e__Struct
        Table: _Table_e__Struct
        FpControlStatus: _FpControlStatus_e__Struct
        XmmControlStatus: _XmmControlStatus_e__Struct
        class _Segment_e__Struct(EasyCastStructure):
            Base: UInt64
            Limit: UInt32
            Selector: UInt16
            Anonymous: _Anonymous_e__Union
            class _Anonymous_e__Union(EasyCastUnion):
                Attributes: UInt16
                Anonymous: _Anonymous_e__Struct
                class _Anonymous_e__Struct(EasyCastStructure):
                    _bitfield: UInt16
        class _Table_e__Struct(EasyCastStructure):
            Limit: UInt16
            Base: UInt64
        class _FpControlStatus_e__Struct(EasyCastStructure):
            FpControl: UInt16
            FpStatus: UInt16
            FpTag: Byte
            Reserved: Byte
            LastFpOp: UInt16
            Anonymous: _Anonymous_e__Union
            class _Anonymous_e__Union(EasyCastUnion):
                LastFpRip: UInt64
                Anonymous: _Anonymous_e__Struct
                class _Anonymous_e__Struct(EasyCastStructure):
                    LastFpEip: UInt32
                    LastFpCs: UInt16
        class _XmmControlStatus_e__Struct(EasyCastStructure):
            Anonymous: _Anonymous_e__Union
            XmmStatusControl: UInt32
            XmmStatusControlMask: UInt32
            class _Anonymous_e__Union(EasyCastUnion):
                LastFpRdp: UInt64
                Anonymous: _Anonymous_e__Struct
                class _Anonymous_e__Struct(EasyCastStructure):
                    LastFpDp: UInt32
                    LastFpDs: UInt16
VIRTUAL_PROCESSOR_VENDOR = Int32
ProcessorVendor_Unknown: win32more.Windows.Win32.System.Hypervisor.VIRTUAL_PROCESSOR_VENDOR = 0
ProcessorVendor_Amd: win32more.Windows.Win32.System.Hypervisor.VIRTUAL_PROCESSOR_VENDOR = 1
ProcessorVendor_Intel: win32more.Windows.Win32.System.Hypervisor.VIRTUAL_PROCESSOR_VENDOR = 2
ProcessorVendor_Hygon: win32more.Windows.Win32.System.Hypervisor.VIRTUAL_PROCESSOR_VENDOR = 3
ProcessorVendor_Arm: win32more.Windows.Win32.System.Hypervisor.VIRTUAL_PROCESSOR_VENDOR = 4
class VM_GENCOUNTER(EasyCastStructure):
    GenerationCount: UInt64
    GenerationCountHigh: UInt64
class WHV_ACCESS_GPA_CONTROLS(EasyCastUnion):
    AsUINT64: UInt64
    Anonymous: _Anonymous_e__Struct
    class _Anonymous_e__Struct(EasyCastStructure):
        CacheType: win32more.Windows.Win32.System.Hypervisor.WHV_CACHE_TYPE
        Reserved: UInt32
class WHV_ADVISE_GPA_RANGE(EasyCastUnion):
    Populate: win32more.Windows.Win32.System.Hypervisor.WHV_ADVISE_GPA_RANGE_POPULATE
WHV_ADVISE_GPA_RANGE_CODE = Int32
WHV_ADVISE_GPA_RANGE_CODE_WHvAdviseGpaRangeCodePopulate: win32more.Windows.Win32.System.Hypervisor.WHV_ADVISE_GPA_RANGE_CODE = 0
WHV_ADVISE_GPA_RANGE_CODE_WHvAdviseGpaRangeCodePin: win32more.Windows.Win32.System.Hypervisor.WHV_ADVISE_GPA_RANGE_CODE = 1
WHV_ADVISE_GPA_RANGE_CODE_WHvAdviseGpaRangeCodeUnpin: win32more.Windows.Win32.System.Hypervisor.WHV_ADVISE_GPA_RANGE_CODE = 2
class WHV_ADVISE_GPA_RANGE_POPULATE(EasyCastStructure):
    Flags: win32more.Windows.Win32.System.Hypervisor.WHV_ADVISE_GPA_RANGE_POPULATE_FLAGS
    AccessType: win32more.Windows.Win32.System.Hypervisor.WHV_MEMORY_ACCESS_TYPE
class WHV_ADVISE_GPA_RANGE_POPULATE_FLAGS(EasyCastUnion):
    AsUINT32: UInt32
    Anonymous: _Anonymous_e__Struct
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
WHV_ALLOCATE_VPCI_RESOURCE_FLAGS = Int32
WHV_ALLOCATE_VPCI_RESOURCE_FLAGS_WHvAllocateVpciResourceFlagNone: win32more.Windows.Win32.System.Hypervisor.WHV_ALLOCATE_VPCI_RESOURCE_FLAGS = 0
WHV_ALLOCATE_VPCI_RESOURCE_FLAGS_WHvAllocateVpciResourceFlagAllowDirectP2P: win32more.Windows.Win32.System.Hypervisor.WHV_ALLOCATE_VPCI_RESOURCE_FLAGS = 1
WHV_CACHE_TYPE = Int32
WHV_CACHE_TYPE_WHvCacheTypeUncached: win32more.Windows.Win32.System.Hypervisor.WHV_CACHE_TYPE = 0
WHV_CACHE_TYPE_WHvCacheTypeWriteCombining: win32more.Windows.Win32.System.Hypervisor.WHV_CACHE_TYPE = 1
WHV_CACHE_TYPE_WHvCacheTypeWriteThrough: win32more.Windows.Win32.System.Hypervisor.WHV_CACHE_TYPE = 4
WHV_CACHE_TYPE_WHvCacheTypeWriteBack: win32more.Windows.Win32.System.Hypervisor.WHV_CACHE_TYPE = 6
class WHV_CAPABILITY(EasyCastUnion):
    HypervisorPresent: win32more.Windows.Win32.Foundation.BOOL
    Features: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_FEATURES
    ExtendedVmExits: win32more.Windows.Win32.System.Hypervisor.WHV_EXTENDED_VM_EXITS
    ProcessorVendor: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_VENDOR
    ProcessorFeatures: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_FEATURES
    SyntheticProcessorFeaturesBanks: win32more.Windows.Win32.System.Hypervisor.WHV_SYNTHETIC_PROCESSOR_FEATURES_BANKS
    ProcessorXsaveFeatures: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_XSAVE_FEATURES
    ProcessorClFlushSize: Byte
    ExceptionExitBitmap: UInt64
    X64MsrExitBitmap: win32more.Windows.Win32.System.Hypervisor.WHV_X64_MSR_EXIT_BITMAP
    ProcessorClockFrequency: UInt64
    InterruptClockFrequency: UInt64
    ProcessorFeaturesBanks: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_FEATURES_BANKS
    GpaRangePopulateFlags: win32more.Windows.Win32.System.Hypervisor.WHV_ADVISE_GPA_RANGE_POPULATE_FLAGS
    ProcessorFrequencyCap: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_PROCESSOR_FREQUENCY_CAP
    ProcessorPerfmonFeatures: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_PERFMON_FEATURES
    SchedulerFeatures: win32more.Windows.Win32.System.Hypervisor.WHV_SCHEDULER_FEATURES
WHV_CAPABILITY_CODE = Int32
WHV_CAPABILITY_CODE_WHvCapabilityCodeHypervisorPresent: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 0
WHV_CAPABILITY_CODE_WHvCapabilityCodeFeatures: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 1
WHV_CAPABILITY_CODE_WHvCapabilityCodeExtendedVmExits: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 2
WHV_CAPABILITY_CODE_WHvCapabilityCodeExceptionExitBitmap: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 3
WHV_CAPABILITY_CODE_WHvCapabilityCodeX64MsrExitBitmap: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 4
WHV_CAPABILITY_CODE_WHvCapabilityCodeGpaRangePopulateFlags: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 5
WHV_CAPABILITY_CODE_WHvCapabilityCodeSchedulerFeatures: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 6
WHV_CAPABILITY_CODE_WHvCapabilityCodeProcessorVendor: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 4096
WHV_CAPABILITY_CODE_WHvCapabilityCodeProcessorFeatures: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 4097
WHV_CAPABILITY_CODE_WHvCapabilityCodeProcessorClFlushSize: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 4098
WHV_CAPABILITY_CODE_WHvCapabilityCodeProcessorXsaveFeatures: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 4099
WHV_CAPABILITY_CODE_WHvCapabilityCodeProcessorClockFrequency: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 4100
WHV_CAPABILITY_CODE_WHvCapabilityCodeInterruptClockFrequency: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 4101
WHV_CAPABILITY_CODE_WHvCapabilityCodeProcessorFeaturesBanks: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 4102
WHV_CAPABILITY_CODE_WHvCapabilityCodeProcessorFrequencyCap: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 4103
WHV_CAPABILITY_CODE_WHvCapabilityCodeSyntheticProcessorFeaturesBanks: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 4104
WHV_CAPABILITY_CODE_WHvCapabilityCodeProcessorPerfmonFeatures: win32more.Windows.Win32.System.Hypervisor.WHV_CAPABILITY_CODE = 4105
class WHV_CAPABILITY_FEATURES(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUINT64: UInt64
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt64
class WHV_CAPABILITY_PROCESSOR_FREQUENCY_CAP(EasyCastStructure):
    _bitfield: UInt32
    HighestFrequencyMhz: UInt32
    NominalFrequencyMhz: UInt32
    LowestFrequencyMhz: UInt32
    FrequencyStepMhz: UInt32
class WHV_CPUID_OUTPUT(EasyCastStructure):
    Eax: UInt32
    Ebx: UInt32
    Ecx: UInt32
    Edx: UInt32
WHV_CREATE_VPCI_DEVICE_FLAGS = Int32
WHV_CREATE_VPCI_DEVICE_FLAGS_WHvCreateVpciDeviceFlagNone: win32more.Windows.Win32.System.Hypervisor.WHV_CREATE_VPCI_DEVICE_FLAGS = 0
WHV_CREATE_VPCI_DEVICE_FLAGS_WHvCreateVpciDeviceFlagPhysicallyBacked: win32more.Windows.Win32.System.Hypervisor.WHV_CREATE_VPCI_DEVICE_FLAGS = 1
WHV_CREATE_VPCI_DEVICE_FLAGS_WHvCreateVpciDeviceFlagUseLogicalInterrupts: win32more.Windows.Win32.System.Hypervisor.WHV_CREATE_VPCI_DEVICE_FLAGS = 2
class WHV_DOORBELL_MATCH_DATA(EasyCastStructure):
    GuestAddress: UInt64
    Value: UInt64
    Length: UInt32
    _bitfield: UInt32
class WHV_EMULATOR_CALLBACKS(EasyCastStructure):
    Size: UInt32
    Reserved: UInt32
    WHvEmulatorIoPortCallback: win32more.Windows.Win32.System.Hypervisor.WHV_EMULATOR_IO_PORT_CALLBACK
    WHvEmulatorMemoryCallback: win32more.Windows.Win32.System.Hypervisor.WHV_EMULATOR_MEMORY_CALLBACK
    WHvEmulatorGetVirtualProcessorRegisters: win32more.Windows.Win32.System.Hypervisor.WHV_EMULATOR_GET_VIRTUAL_PROCESSOR_REGISTERS_CALLBACK
    WHvEmulatorSetVirtualProcessorRegisters: win32more.Windows.Win32.System.Hypervisor.WHV_EMULATOR_SET_VIRTUAL_PROCESSOR_REGISTERS_CALLBACK
    WHvEmulatorTranslateGvaPage: win32more.Windows.Win32.System.Hypervisor.WHV_EMULATOR_TRANSLATE_GVA_PAGE_CALLBACK
@winfunctype_pointer
def WHV_EMULATOR_GET_VIRTUAL_PROCESSOR_REGISTERS_CALLBACK(Context: VoidPtr, RegisterNames: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME), RegisterCount: UInt32, RegisterValues: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_VALUE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class WHV_EMULATOR_IO_ACCESS_INFO(EasyCastStructure):
    Direction: Byte
    Port: UInt16
    AccessSize: UInt16
    Data: UInt32
@winfunctype_pointer
def WHV_EMULATOR_IO_PORT_CALLBACK(Context: VoidPtr, IoAccess: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_EMULATOR_IO_ACCESS_INFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class WHV_EMULATOR_MEMORY_ACCESS_INFO(EasyCastStructure):
    GpaAddress: UInt64
    Direction: Byte
    AccessSize: Byte
    Data: Byte * 8
@winfunctype_pointer
def WHV_EMULATOR_MEMORY_CALLBACK(Context: VoidPtr, MemoryAccess: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_EMULATOR_MEMORY_ACCESS_INFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def WHV_EMULATOR_SET_VIRTUAL_PROCESSOR_REGISTERS_CALLBACK(Context: VoidPtr, RegisterNames: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME), RegisterCount: UInt32, RegisterValues: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_VALUE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class WHV_EMULATOR_STATUS(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUINT32: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
@winfunctype_pointer
def WHV_EMULATOR_TRANSLATE_GVA_PAGE_CALLBACK(Context: VoidPtr, Gva: UInt64, TranslateFlags: win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_FLAGS, TranslationResult: POINTER(win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_RESULT_CODE), Gpa: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
WHV_EXCEPTION_TYPE = Int32
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeDivideErrorFault: win32more.Windows.Win32.System.Hypervisor.WHV_EXCEPTION_TYPE = 0
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeDebugTrapOrFault: win32more.Windows.Win32.System.Hypervisor.WHV_EXCEPTION_TYPE = 1
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeBreakpointTrap: win32more.Windows.Win32.System.Hypervisor.WHV_EXCEPTION_TYPE = 3
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeOverflowTrap: win32more.Windows.Win32.System.Hypervisor.WHV_EXCEPTION_TYPE = 4
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeBoundRangeFault: win32more.Windows.Win32.System.Hypervisor.WHV_EXCEPTION_TYPE = 5
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeInvalidOpcodeFault: win32more.Windows.Win32.System.Hypervisor.WHV_EXCEPTION_TYPE = 6
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeDeviceNotAvailableFault: win32more.Windows.Win32.System.Hypervisor.WHV_EXCEPTION_TYPE = 7
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeDoubleFaultAbort: win32more.Windows.Win32.System.Hypervisor.WHV_EXCEPTION_TYPE = 8
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeInvalidTaskStateSegmentFault: win32more.Windows.Win32.System.Hypervisor.WHV_EXCEPTION_TYPE = 10
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeSegmentNotPresentFault: win32more.Windows.Win32.System.Hypervisor.WHV_EXCEPTION_TYPE = 11
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeStackFault: win32more.Windows.Win32.System.Hypervisor.WHV_EXCEPTION_TYPE = 12
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeGeneralProtectionFault: win32more.Windows.Win32.System.Hypervisor.WHV_EXCEPTION_TYPE = 13
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypePageFault: win32more.Windows.Win32.System.Hypervisor.WHV_EXCEPTION_TYPE = 14
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeFloatingPointErrorFault: win32more.Windows.Win32.System.Hypervisor.WHV_EXCEPTION_TYPE = 16
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeAlignmentCheckFault: win32more.Windows.Win32.System.Hypervisor.WHV_EXCEPTION_TYPE = 17
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeMachineCheckAbort: win32more.Windows.Win32.System.Hypervisor.WHV_EXCEPTION_TYPE = 18
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeSimdFloatingPointFault: win32more.Windows.Win32.System.Hypervisor.WHV_EXCEPTION_TYPE = 19
class WHV_EXTENDED_VM_EXITS(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUINT64: UInt64
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt64
class WHV_HYPERCALL_CONTEXT(EasyCastStructure):
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
class WHV_INTERNAL_ACTIVITY_REGISTER(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUINT64: UInt64
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt64
class WHV_INTERRUPT_CONTROL(EasyCastStructure):
    _bitfield: UInt64
    Destination: UInt32
    Vector: UInt32
WHV_INTERRUPT_DESTINATION_MODE = Int32
WHV_INTERRUPT_DESTINATION_MODE_WHvX64InterruptDestinationModePhysical: win32more.Windows.Win32.System.Hypervisor.WHV_INTERRUPT_DESTINATION_MODE = 0
WHV_INTERRUPT_DESTINATION_MODE_WHvX64InterruptDestinationModeLogical: win32more.Windows.Win32.System.Hypervisor.WHV_INTERRUPT_DESTINATION_MODE = 1
WHV_INTERRUPT_TRIGGER_MODE = Int32
WHV_INTERRUPT_TRIGGER_MODE_WHvX64InterruptTriggerModeEdge: win32more.Windows.Win32.System.Hypervisor.WHV_INTERRUPT_TRIGGER_MODE = 0
WHV_INTERRUPT_TRIGGER_MODE_WHvX64InterruptTriggerModeLevel: win32more.Windows.Win32.System.Hypervisor.WHV_INTERRUPT_TRIGGER_MODE = 1
WHV_INTERRUPT_TYPE = Int32
WHV_INTERRUPT_TYPE_WHvX64InterruptTypeFixed: win32more.Windows.Win32.System.Hypervisor.WHV_INTERRUPT_TYPE = 0
WHV_INTERRUPT_TYPE_WHvX64InterruptTypeLowestPriority: win32more.Windows.Win32.System.Hypervisor.WHV_INTERRUPT_TYPE = 1
WHV_INTERRUPT_TYPE_WHvX64InterruptTypeNmi: win32more.Windows.Win32.System.Hypervisor.WHV_INTERRUPT_TYPE = 4
WHV_INTERRUPT_TYPE_WHvX64InterruptTypeInit: win32more.Windows.Win32.System.Hypervisor.WHV_INTERRUPT_TYPE = 5
WHV_INTERRUPT_TYPE_WHvX64InterruptTypeSipi: win32more.Windows.Win32.System.Hypervisor.WHV_INTERRUPT_TYPE = 6
WHV_INTERRUPT_TYPE_WHvX64InterruptTypeLocalInt1: win32more.Windows.Win32.System.Hypervisor.WHV_INTERRUPT_TYPE = 9
WHV_MAP_GPA_RANGE_FLAGS = Int32
WHV_MAP_GPA_RANGE_FLAGS_WHvMapGpaRangeFlagNone: win32more.Windows.Win32.System.Hypervisor.WHV_MAP_GPA_RANGE_FLAGS = 0
WHV_MAP_GPA_RANGE_FLAGS_WHvMapGpaRangeFlagRead: win32more.Windows.Win32.System.Hypervisor.WHV_MAP_GPA_RANGE_FLAGS = 1
WHV_MAP_GPA_RANGE_FLAGS_WHvMapGpaRangeFlagWrite: win32more.Windows.Win32.System.Hypervisor.WHV_MAP_GPA_RANGE_FLAGS = 2
WHV_MAP_GPA_RANGE_FLAGS_WHvMapGpaRangeFlagExecute: win32more.Windows.Win32.System.Hypervisor.WHV_MAP_GPA_RANGE_FLAGS = 4
WHV_MAP_GPA_RANGE_FLAGS_WHvMapGpaRangeFlagTrackDirtyPages: win32more.Windows.Win32.System.Hypervisor.WHV_MAP_GPA_RANGE_FLAGS = 8
class WHV_MEMORY_ACCESS_CONTEXT(EasyCastStructure):
    InstructionByteCount: Byte
    Reserved: Byte * 3
    InstructionBytes: Byte * 16
    AccessInfo: win32more.Windows.Win32.System.Hypervisor.WHV_MEMORY_ACCESS_INFO
    Gpa: UInt64
    Gva: UInt64
class WHV_MEMORY_ACCESS_INFO(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUINT32: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
WHV_MEMORY_ACCESS_TYPE = Int32
WHV_MEMORY_ACCESS_TYPE_WHvMemoryAccessRead: win32more.Windows.Win32.System.Hypervisor.WHV_MEMORY_ACCESS_TYPE = 0
WHV_MEMORY_ACCESS_TYPE_WHvMemoryAccessWrite: win32more.Windows.Win32.System.Hypervisor.WHV_MEMORY_ACCESS_TYPE = 1
WHV_MEMORY_ACCESS_TYPE_WHvMemoryAccessExecute: win32more.Windows.Win32.System.Hypervisor.WHV_MEMORY_ACCESS_TYPE = 2
class WHV_MEMORY_RANGE_ENTRY(EasyCastStructure):
    GuestAddress: UInt64
    SizeInBytes: UInt64
WHV_MSR_ACTION = Int32
WHV_MSR_ACTION_WHvMsrActionArchitectureDefault: win32more.Windows.Win32.System.Hypervisor.WHV_MSR_ACTION = 0
WHV_MSR_ACTION_WHvMsrActionIgnoreWriteReadZero: win32more.Windows.Win32.System.Hypervisor.WHV_MSR_ACTION = 1
WHV_MSR_ACTION_WHvMsrActionExit: win32more.Windows.Win32.System.Hypervisor.WHV_MSR_ACTION = 2
class WHV_MSR_ACTION_ENTRY(EasyCastStructure):
    Index: UInt32
    ReadAction: Byte
    WriteAction: Byte
    Reserved: UInt16
class WHV_NOTIFICATION_PORT_PARAMETERS(EasyCastStructure):
    NotificationPortType: win32more.Windows.Win32.System.Hypervisor.WHV_NOTIFICATION_PORT_TYPE
    Reserved: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Doorbell: win32more.Windows.Win32.System.Hypervisor.WHV_DOORBELL_MATCH_DATA
        Event: _Event_e__Struct
        class _Event_e__Struct(EasyCastStructure):
            ConnectionId: UInt32
WHV_NOTIFICATION_PORT_PROPERTY_CODE = Int32
WHV_NOTIFICATION_PORT_PROPERTY_CODE_WHvNotificationPortPropertyPreferredTargetVp: win32more.Windows.Win32.System.Hypervisor.WHV_NOTIFICATION_PORT_PROPERTY_CODE = 1
WHV_NOTIFICATION_PORT_PROPERTY_CODE_WHvNotificationPortPropertyPreferredTargetDuration: win32more.Windows.Win32.System.Hypervisor.WHV_NOTIFICATION_PORT_PROPERTY_CODE = 5
WHV_NOTIFICATION_PORT_TYPE = Int32
WHV_NOTIFICATION_PORT_TYPE_WHvNotificationPortTypeEvent: win32more.Windows.Win32.System.Hypervisor.WHV_NOTIFICATION_PORT_TYPE = 2
WHV_NOTIFICATION_PORT_TYPE_WHvNotificationPortTypeDoorbell: win32more.Windows.Win32.System.Hypervisor.WHV_NOTIFICATION_PORT_TYPE = 4
WHV_PARTITION_COUNTER_SET = Int32
WHV_PARTITION_COUNTER_SET_WHvPartitionCounterSetMemory: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_COUNTER_SET = 0
WHV_PARTITION_HANDLE = IntPtr
class WHV_PARTITION_MEMORY_COUNTERS(EasyCastStructure):
    Mapped4KPageCount: UInt64
    Mapped2MPageCount: UInt64
    Mapped1GPageCount: UInt64
class WHV_PARTITION_PROPERTY(EasyCastUnion):
    ExtendedVmExits: win32more.Windows.Win32.System.Hypervisor.WHV_EXTENDED_VM_EXITS
    ProcessorFeatures: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_FEATURES
    SyntheticProcessorFeaturesBanks: win32more.Windows.Win32.System.Hypervisor.WHV_SYNTHETIC_PROCESSOR_FEATURES_BANKS
    ProcessorXsaveFeatures: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_XSAVE_FEATURES
    ProcessorClFlushSize: Byte
    ProcessorCount: UInt32
    CpuidExitList: UInt32 * 1
    CpuidResultList: win32more.Windows.Win32.System.Hypervisor.WHV_X64_CPUID_RESULT * 1
    CpuidResultList2: win32more.Windows.Win32.System.Hypervisor.WHV_X64_CPUID_RESULT2 * 1
    MsrActionList: win32more.Windows.Win32.System.Hypervisor.WHV_MSR_ACTION_ENTRY * 1
    UnimplementedMsrAction: win32more.Windows.Win32.System.Hypervisor.WHV_MSR_ACTION
    ExceptionExitBitmap: UInt64
    LocalApicEmulationMode: win32more.Windows.Win32.System.Hypervisor.WHV_X64_LOCAL_APIC_EMULATION_MODE
    SeparateSecurityDomain: win32more.Windows.Win32.Foundation.BOOL
    NestedVirtualization: win32more.Windows.Win32.Foundation.BOOL
    X64MsrExitBitmap: win32more.Windows.Win32.System.Hypervisor.WHV_X64_MSR_EXIT_BITMAP
    ProcessorClockFrequency: UInt64
    InterruptClockFrequency: UInt64
    ApicRemoteRead: win32more.Windows.Win32.Foundation.BOOL
    ProcessorFeaturesBanks: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_FEATURES_BANKS
    ReferenceTime: UInt64
    PrimaryNumaNode: UInt16
    CpuReserve: UInt32
    CpuCap: UInt32
    CpuWeight: UInt32
    CpuGroupId: UInt64
    ProcessorFrequencyCap: UInt32
    AllowDeviceAssignment: win32more.Windows.Win32.Foundation.BOOL
    ProcessorPerfmonFeatures: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_PERFMON_FEATURES
    DisableSmt: win32more.Windows.Win32.Foundation.BOOL
WHV_PARTITION_PROPERTY_CODE = Int32
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeExtendedVmExits: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 1
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeExceptionExitBitmap: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 2
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeSeparateSecurityDomain: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 3
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeNestedVirtualization: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 4
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeX64MsrExitBitmap: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 5
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodePrimaryNumaNode: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 6
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeCpuReserve: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 7
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeCpuCap: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 8
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeCpuWeight: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 9
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeCpuGroupId: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 10
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeProcessorFrequencyCap: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 11
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeAllowDeviceAssignment: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 12
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeDisableSmt: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 13
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeProcessorFeatures: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 4097
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeProcessorClFlushSize: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 4098
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeCpuidExitList: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 4099
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeCpuidResultList: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 4100
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeLocalApicEmulationMode: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 4101
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeProcessorXsaveFeatures: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 4102
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeProcessorClockFrequency: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 4103
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeInterruptClockFrequency: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 4104
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeApicRemoteReadSupport: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 4105
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeProcessorFeaturesBanks: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 4106
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeReferenceTime: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 4107
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeSyntheticProcessorFeaturesBanks: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 4108
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeCpuidResultList2: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 4109
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeProcessorPerfmonFeatures: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 4110
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeMsrActionList: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 4111
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeUnimplementedMsrAction: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 4112
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeProcessorCount: win32more.Windows.Win32.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE = 8191
class WHV_PROCESSOR_APIC_COUNTERS(EasyCastStructure):
    MmioAccessCount: UInt64
    EoiAccessCount: UInt64
    TprAccessCount: UInt64
    SentIpiCount: UInt64
    SelfIpiCount: UInt64
WHV_PROCESSOR_COUNTER_SET = Int32
WHV_PROCESSOR_COUNTER_SET_WHvProcessorCounterSetRuntime: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_COUNTER_SET = 0
WHV_PROCESSOR_COUNTER_SET_WHvProcessorCounterSetIntercepts: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_COUNTER_SET = 1
WHV_PROCESSOR_COUNTER_SET_WHvProcessorCounterSetEvents: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_COUNTER_SET = 2
WHV_PROCESSOR_COUNTER_SET_WHvProcessorCounterSetApic: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_COUNTER_SET = 3
WHV_PROCESSOR_COUNTER_SET_WHvProcessorCounterSetSyntheticFeatures: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_COUNTER_SET = 4
class WHV_PROCESSOR_EVENT_COUNTERS(EasyCastStructure):
    PageFaultCount: UInt64
    ExceptionCount: UInt64
    InterruptCount: UInt64
class WHV_PROCESSOR_FEATURES(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUINT64: UInt64
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt64
class WHV_PROCESSOR_FEATURES1(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUINT64: UInt64
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt64
class WHV_PROCESSOR_FEATURES_BANKS(EasyCastStructure):
    BanksCount: UInt32
    Reserved0: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Anonymous: _Anonymous_e__Struct
        AsUINT64: UInt64 * 2
        class _Anonymous_e__Struct(EasyCastStructure):
            Bank0: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_FEATURES
            Bank1: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_FEATURES1
class WHV_PROCESSOR_INTERCEPT_COUNTER(EasyCastStructure):
    Count: UInt64
    Time100ns: UInt64
class WHV_PROCESSOR_INTERCEPT_COUNTERS(EasyCastStructure):
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
class WHV_PROCESSOR_PERFMON_FEATURES(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUINT64: UInt64
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt64
class WHV_PROCESSOR_RUNTIME_COUNTERS(EasyCastStructure):
    TotalRuntime100ns: UInt64
    HypervisorRuntime100ns: UInt64
class WHV_PROCESSOR_SYNTHETIC_FEATURES_COUNTERS(EasyCastStructure):
    SyntheticInterruptsCount: UInt64
    LongSpinWaitHypercallsCount: UInt64
    OtherHypercallsCount: UInt64
    SyntheticInterruptHypercallsCount: UInt64
    VirtualInterruptHypercallsCount: UInt64
    VirtualMmuHypercallsCount: UInt64
WHV_PROCESSOR_VENDOR = Int32
WHV_PROCESSOR_VENDOR_WHvProcessorVendorAmd: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_VENDOR = 0
WHV_PROCESSOR_VENDOR_WHvProcessorVendorIntel: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_VENDOR = 1
WHV_PROCESSOR_VENDOR_WHvProcessorVendorHygon: win32more.Windows.Win32.System.Hypervisor.WHV_PROCESSOR_VENDOR = 2
class WHV_PROCESSOR_XSAVE_FEATURES(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUINT64: UInt64
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt64
WHV_REGISTER_NAME = Int32
WHV_REGISTER_NAME_WHvX64RegisterRax: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 0
WHV_REGISTER_NAME_WHvX64RegisterRcx: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 1
WHV_REGISTER_NAME_WHvX64RegisterRdx: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 2
WHV_REGISTER_NAME_WHvX64RegisterRbx: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 3
WHV_REGISTER_NAME_WHvX64RegisterRsp: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4
WHV_REGISTER_NAME_WHvX64RegisterRbp: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 5
WHV_REGISTER_NAME_WHvX64RegisterRsi: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 6
WHV_REGISTER_NAME_WHvX64RegisterRdi: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 7
WHV_REGISTER_NAME_WHvX64RegisterR8: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8
WHV_REGISTER_NAME_WHvX64RegisterR9: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 9
WHV_REGISTER_NAME_WHvX64RegisterR10: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 10
WHV_REGISTER_NAME_WHvX64RegisterR11: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 11
WHV_REGISTER_NAME_WHvX64RegisterR12: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12
WHV_REGISTER_NAME_WHvX64RegisterR13: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 13
WHV_REGISTER_NAME_WHvX64RegisterR14: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 14
WHV_REGISTER_NAME_WHvX64RegisterR15: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 15
WHV_REGISTER_NAME_WHvX64RegisterRip: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 16
WHV_REGISTER_NAME_WHvX64RegisterRflags: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 17
WHV_REGISTER_NAME_WHvX64RegisterEs: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 18
WHV_REGISTER_NAME_WHvX64RegisterCs: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 19
WHV_REGISTER_NAME_WHvX64RegisterSs: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 20
WHV_REGISTER_NAME_WHvX64RegisterDs: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 21
WHV_REGISTER_NAME_WHvX64RegisterFs: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 22
WHV_REGISTER_NAME_WHvX64RegisterGs: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 23
WHV_REGISTER_NAME_WHvX64RegisterLdtr: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 24
WHV_REGISTER_NAME_WHvX64RegisterTr: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 25
WHV_REGISTER_NAME_WHvX64RegisterIdtr: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 26
WHV_REGISTER_NAME_WHvX64RegisterGdtr: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 27
WHV_REGISTER_NAME_WHvX64RegisterCr0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 28
WHV_REGISTER_NAME_WHvX64RegisterCr2: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 29
WHV_REGISTER_NAME_WHvX64RegisterCr3: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 30
WHV_REGISTER_NAME_WHvX64RegisterCr4: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 31
WHV_REGISTER_NAME_WHvX64RegisterCr8: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 32
WHV_REGISTER_NAME_WHvX64RegisterDr0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 33
WHV_REGISTER_NAME_WHvX64RegisterDr1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 34
WHV_REGISTER_NAME_WHvX64RegisterDr2: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 35
WHV_REGISTER_NAME_WHvX64RegisterDr3: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 36
WHV_REGISTER_NAME_WHvX64RegisterDr6: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 37
WHV_REGISTER_NAME_WHvX64RegisterDr7: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 38
WHV_REGISTER_NAME_WHvX64RegisterXCr0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 39
WHV_REGISTER_NAME_WHvX64RegisterVirtualCr0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 40
WHV_REGISTER_NAME_WHvX64RegisterVirtualCr3: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 41
WHV_REGISTER_NAME_WHvX64RegisterVirtualCr4: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 42
WHV_REGISTER_NAME_WHvX64RegisterVirtualCr8: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 43
WHV_REGISTER_NAME_WHvX64RegisterXmm0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4096
WHV_REGISTER_NAME_WHvX64RegisterXmm1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4097
WHV_REGISTER_NAME_WHvX64RegisterXmm2: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4098
WHV_REGISTER_NAME_WHvX64RegisterXmm3: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4099
WHV_REGISTER_NAME_WHvX64RegisterXmm4: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4100
WHV_REGISTER_NAME_WHvX64RegisterXmm5: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4101
WHV_REGISTER_NAME_WHvX64RegisterXmm6: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4102
WHV_REGISTER_NAME_WHvX64RegisterXmm7: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4103
WHV_REGISTER_NAME_WHvX64RegisterXmm8: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4104
WHV_REGISTER_NAME_WHvX64RegisterXmm9: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4105
WHV_REGISTER_NAME_WHvX64RegisterXmm10: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4106
WHV_REGISTER_NAME_WHvX64RegisterXmm11: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4107
WHV_REGISTER_NAME_WHvX64RegisterXmm12: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4108
WHV_REGISTER_NAME_WHvX64RegisterXmm13: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4109
WHV_REGISTER_NAME_WHvX64RegisterXmm14: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4110
WHV_REGISTER_NAME_WHvX64RegisterXmm15: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4111
WHV_REGISTER_NAME_WHvX64RegisterFpMmx0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4112
WHV_REGISTER_NAME_WHvX64RegisterFpMmx1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4113
WHV_REGISTER_NAME_WHvX64RegisterFpMmx2: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4114
WHV_REGISTER_NAME_WHvX64RegisterFpMmx3: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4115
WHV_REGISTER_NAME_WHvX64RegisterFpMmx4: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4116
WHV_REGISTER_NAME_WHvX64RegisterFpMmx5: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4117
WHV_REGISTER_NAME_WHvX64RegisterFpMmx6: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4118
WHV_REGISTER_NAME_WHvX64RegisterFpMmx7: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4119
WHV_REGISTER_NAME_WHvX64RegisterFpControlStatus: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4120
WHV_REGISTER_NAME_WHvX64RegisterXmmControlStatus: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 4121
WHV_REGISTER_NAME_WHvX64RegisterTsc: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8192
WHV_REGISTER_NAME_WHvX64RegisterEfer: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8193
WHV_REGISTER_NAME_WHvX64RegisterKernelGsBase: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8194
WHV_REGISTER_NAME_WHvX64RegisterApicBase: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8195
WHV_REGISTER_NAME_WHvX64RegisterPat: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8196
WHV_REGISTER_NAME_WHvX64RegisterSysenterCs: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8197
WHV_REGISTER_NAME_WHvX64RegisterSysenterEip: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8198
WHV_REGISTER_NAME_WHvX64RegisterSysenterEsp: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8199
WHV_REGISTER_NAME_WHvX64RegisterStar: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8200
WHV_REGISTER_NAME_WHvX64RegisterLstar: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8201
WHV_REGISTER_NAME_WHvX64RegisterCstar: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8202
WHV_REGISTER_NAME_WHvX64RegisterSfmask: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8203
WHV_REGISTER_NAME_WHvX64RegisterInitialApicId: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8204
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrCap: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8205
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrDefType: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8206
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBase0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8208
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBase1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8209
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBase2: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8210
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBase3: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8211
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBase4: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8212
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBase5: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8213
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBase6: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8214
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBase7: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8215
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBase8: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8216
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBase9: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8217
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBaseA: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8218
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBaseB: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8219
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBaseC: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8220
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBaseD: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8221
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBaseE: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8222
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBaseF: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8223
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMask0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8256
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMask1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8257
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMask2: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8258
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMask3: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8259
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMask4: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8260
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMask5: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8261
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMask6: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8262
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMask7: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8263
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMask8: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8264
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMask9: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8265
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMaskA: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8266
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMaskB: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8267
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMaskC: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8268
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMaskD: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8269
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMaskE: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8270
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMaskF: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8271
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrFix64k00000: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8304
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrFix16k80000: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8305
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrFix16kA0000: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8306
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrFix4kC0000: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8307
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrFix4kC8000: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8308
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrFix4kD0000: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8309
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrFix4kD8000: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8310
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrFix4kE0000: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8311
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrFix4kE8000: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8312
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrFix4kF0000: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8313
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrFix4kF8000: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8314
WHV_REGISTER_NAME_WHvX64RegisterTscAux: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8315
WHV_REGISTER_NAME_WHvX64RegisterBndcfgs: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8316
WHV_REGISTER_NAME_WHvX64RegisterMCount: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8318
WHV_REGISTER_NAME_WHvX64RegisterACount: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8319
WHV_REGISTER_NAME_WHvX64RegisterSpecCtrl: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8324
WHV_REGISTER_NAME_WHvX64RegisterPredCmd: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8325
WHV_REGISTER_NAME_WHvX64RegisterTscVirtualOffset: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8327
WHV_REGISTER_NAME_WHvX64RegisterTsxCtrl: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8328
WHV_REGISTER_NAME_WHvX64RegisterXss: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8331
WHV_REGISTER_NAME_WHvX64RegisterUCet: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8332
WHV_REGISTER_NAME_WHvX64RegisterSCet: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8333
WHV_REGISTER_NAME_WHvX64RegisterSsp: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8334
WHV_REGISTER_NAME_WHvX64RegisterPl0Ssp: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8335
WHV_REGISTER_NAME_WHvX64RegisterPl1Ssp: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8336
WHV_REGISTER_NAME_WHvX64RegisterPl2Ssp: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8337
WHV_REGISTER_NAME_WHvX64RegisterPl3Ssp: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8338
WHV_REGISTER_NAME_WHvX64RegisterInterruptSspTableAddr: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8339
WHV_REGISTER_NAME_WHvX64RegisterTscDeadline: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8341
WHV_REGISTER_NAME_WHvX64RegisterTscAdjust: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8342
WHV_REGISTER_NAME_WHvX64RegisterUmwaitControl: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8344
WHV_REGISTER_NAME_WHvX64RegisterXfd: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8345
WHV_REGISTER_NAME_WHvX64RegisterXfdErr: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 8346
WHV_REGISTER_NAME_WHvX64RegisterApicId: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12290
WHV_REGISTER_NAME_WHvX64RegisterApicVersion: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12291
WHV_REGISTER_NAME_WHvX64RegisterApicTpr: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12296
WHV_REGISTER_NAME_WHvX64RegisterApicPpr: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12298
WHV_REGISTER_NAME_WHvX64RegisterApicEoi: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12299
WHV_REGISTER_NAME_WHvX64RegisterApicLdr: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12301
WHV_REGISTER_NAME_WHvX64RegisterApicSpurious: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12303
WHV_REGISTER_NAME_WHvX64RegisterApicIsr0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12304
WHV_REGISTER_NAME_WHvX64RegisterApicIsr1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12305
WHV_REGISTER_NAME_WHvX64RegisterApicIsr2: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12306
WHV_REGISTER_NAME_WHvX64RegisterApicIsr3: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12307
WHV_REGISTER_NAME_WHvX64RegisterApicIsr4: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12308
WHV_REGISTER_NAME_WHvX64RegisterApicIsr5: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12309
WHV_REGISTER_NAME_WHvX64RegisterApicIsr6: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12310
WHV_REGISTER_NAME_WHvX64RegisterApicIsr7: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12311
WHV_REGISTER_NAME_WHvX64RegisterApicTmr0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12312
WHV_REGISTER_NAME_WHvX64RegisterApicTmr1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12313
WHV_REGISTER_NAME_WHvX64RegisterApicTmr2: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12314
WHV_REGISTER_NAME_WHvX64RegisterApicTmr3: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12315
WHV_REGISTER_NAME_WHvX64RegisterApicTmr4: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12316
WHV_REGISTER_NAME_WHvX64RegisterApicTmr5: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12317
WHV_REGISTER_NAME_WHvX64RegisterApicTmr6: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12318
WHV_REGISTER_NAME_WHvX64RegisterApicTmr7: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12319
WHV_REGISTER_NAME_WHvX64RegisterApicIrr0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12320
WHV_REGISTER_NAME_WHvX64RegisterApicIrr1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12321
WHV_REGISTER_NAME_WHvX64RegisterApicIrr2: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12322
WHV_REGISTER_NAME_WHvX64RegisterApicIrr3: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12323
WHV_REGISTER_NAME_WHvX64RegisterApicIrr4: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12324
WHV_REGISTER_NAME_WHvX64RegisterApicIrr5: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12325
WHV_REGISTER_NAME_WHvX64RegisterApicIrr6: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12326
WHV_REGISTER_NAME_WHvX64RegisterApicIrr7: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12327
WHV_REGISTER_NAME_WHvX64RegisterApicEse: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12328
WHV_REGISTER_NAME_WHvX64RegisterApicIcr: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12336
WHV_REGISTER_NAME_WHvX64RegisterApicLvtTimer: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12338
WHV_REGISTER_NAME_WHvX64RegisterApicLvtThermal: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12339
WHV_REGISTER_NAME_WHvX64RegisterApicLvtPerfmon: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12340
WHV_REGISTER_NAME_WHvX64RegisterApicLvtLint0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12341
WHV_REGISTER_NAME_WHvX64RegisterApicLvtLint1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12342
WHV_REGISTER_NAME_WHvX64RegisterApicLvtError: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12343
WHV_REGISTER_NAME_WHvX64RegisterApicInitCount: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12344
WHV_REGISTER_NAME_WHvX64RegisterApicCurrentCount: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12345
WHV_REGISTER_NAME_WHvX64RegisterApicDivide: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12350
WHV_REGISTER_NAME_WHvX64RegisterApicSelfIpi: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 12351
WHV_REGISTER_NAME_WHvRegisterSint0: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 16384
WHV_REGISTER_NAME_WHvRegisterSint1: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 16385
WHV_REGISTER_NAME_WHvRegisterSint2: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 16386
WHV_REGISTER_NAME_WHvRegisterSint3: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 16387
WHV_REGISTER_NAME_WHvRegisterSint4: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 16388
WHV_REGISTER_NAME_WHvRegisterSint5: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 16389
WHV_REGISTER_NAME_WHvRegisterSint6: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 16390
WHV_REGISTER_NAME_WHvRegisterSint7: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 16391
WHV_REGISTER_NAME_WHvRegisterSint8: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 16392
WHV_REGISTER_NAME_WHvRegisterSint9: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 16393
WHV_REGISTER_NAME_WHvRegisterSint10: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 16394
WHV_REGISTER_NAME_WHvRegisterSint11: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 16395
WHV_REGISTER_NAME_WHvRegisterSint12: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 16396
WHV_REGISTER_NAME_WHvRegisterSint13: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 16397
WHV_REGISTER_NAME_WHvRegisterSint14: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 16398
WHV_REGISTER_NAME_WHvRegisterSint15: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 16399
WHV_REGISTER_NAME_WHvRegisterScontrol: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 16400
WHV_REGISTER_NAME_WHvRegisterSversion: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 16401
WHV_REGISTER_NAME_WHvRegisterSiefp: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 16402
WHV_REGISTER_NAME_WHvRegisterSimp: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 16403
WHV_REGISTER_NAME_WHvRegisterEom: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 16404
WHV_REGISTER_NAME_WHvRegisterVpRuntime: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 20480
WHV_REGISTER_NAME_WHvX64RegisterHypercall: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 20481
WHV_REGISTER_NAME_WHvRegisterGuestOsId: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 20482
WHV_REGISTER_NAME_WHvRegisterVpAssistPage: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 20499
WHV_REGISTER_NAME_WHvRegisterReferenceTsc: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 20503
WHV_REGISTER_NAME_WHvRegisterReferenceTscSequence: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = 20506
WHV_REGISTER_NAME_WHvRegisterPendingInterruption: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = -2147483648
WHV_REGISTER_NAME_WHvRegisterInterruptState: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = -2147483647
WHV_REGISTER_NAME_WHvRegisterPendingEvent: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = -2147483646
WHV_REGISTER_NAME_WHvX64RegisterDeliverabilityNotifications: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = -2147483644
WHV_REGISTER_NAME_WHvRegisterInternalActivityState: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = -2147483643
WHV_REGISTER_NAME_WHvX64RegisterPendingDebugException: win32more.Windows.Win32.System.Hypervisor.WHV_REGISTER_NAME = -2147483642
class WHV_REGISTER_VALUE(EasyCastUnion):
    Reg128: win32more.Windows.Win32.System.Hypervisor.WHV_UINT128
    Reg64: UInt64
    Reg32: UInt32
    Reg16: UInt16
    Reg8: Byte
    Fp: win32more.Windows.Win32.System.Hypervisor.WHV_X64_FP_REGISTER
    FpControlStatus: win32more.Windows.Win32.System.Hypervisor.WHV_X64_FP_CONTROL_STATUS_REGISTER
    XmmControlStatus: win32more.Windows.Win32.System.Hypervisor.WHV_X64_XMM_CONTROL_STATUS_REGISTER
    Segment: win32more.Windows.Win32.System.Hypervisor.WHV_X64_SEGMENT_REGISTER
    Table: win32more.Windows.Win32.System.Hypervisor.WHV_X64_TABLE_REGISTER
    InterruptState: win32more.Windows.Win32.System.Hypervisor.WHV_X64_INTERRUPT_STATE_REGISTER
    PendingInterruption: win32more.Windows.Win32.System.Hypervisor.WHV_X64_PENDING_INTERRUPTION_REGISTER
    DeliverabilityNotifications: win32more.Windows.Win32.System.Hypervisor.WHV_X64_DELIVERABILITY_NOTIFICATIONS_REGISTER
    ExceptionEvent: win32more.Windows.Win32.System.Hypervisor.WHV_X64_PENDING_EXCEPTION_EVENT
    ExtIntEvent: win32more.Windows.Win32.System.Hypervisor.WHV_X64_PENDING_EXT_INT_EVENT
    InternalActivity: win32more.Windows.Win32.System.Hypervisor.WHV_INTERNAL_ACTIVITY_REGISTER
    PendingDebugException: win32more.Windows.Win32.System.Hypervisor.WHV_X64_PENDING_DEBUG_EXCEPTION
class WHV_RUN_VP_CANCELED_CONTEXT(EasyCastStructure):
    CancelReason: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_CANCEL_REASON
WHV_RUN_VP_CANCEL_REASON = Int32
WHV_RUN_VP_CANCEL_REASON_WHvRunVpCancelReasonUser: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_CANCEL_REASON = 0
class WHV_RUN_VP_EXIT_CONTEXT(EasyCastStructure):
    ExitReason: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON
    Reserved: UInt32
    VpContext: win32more.Windows.Win32.System.Hypervisor.WHV_VP_EXIT_CONTEXT
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        MemoryAccess: win32more.Windows.Win32.System.Hypervisor.WHV_MEMORY_ACCESS_CONTEXT
        IoPortAccess: win32more.Windows.Win32.System.Hypervisor.WHV_X64_IO_PORT_ACCESS_CONTEXT
        MsrAccess: win32more.Windows.Win32.System.Hypervisor.WHV_X64_MSR_ACCESS_CONTEXT
        CpuidAccess: win32more.Windows.Win32.System.Hypervisor.WHV_X64_CPUID_ACCESS_CONTEXT
        VpException: win32more.Windows.Win32.System.Hypervisor.WHV_VP_EXCEPTION_CONTEXT
        InterruptWindow: win32more.Windows.Win32.System.Hypervisor.WHV_X64_INTERRUPTION_DELIVERABLE_CONTEXT
        UnsupportedFeature: win32more.Windows.Win32.System.Hypervisor.WHV_X64_UNSUPPORTED_FEATURE_CONTEXT
        CancelReason: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_CANCELED_CONTEXT
        ApicEoi: win32more.Windows.Win32.System.Hypervisor.WHV_X64_APIC_EOI_CONTEXT
        ReadTsc: win32more.Windows.Win32.System.Hypervisor.WHV_X64_RDTSC_CONTEXT
        ApicSmi: win32more.Windows.Win32.System.Hypervisor.WHV_X64_APIC_SMI_CONTEXT
        Hypercall: win32more.Windows.Win32.System.Hypervisor.WHV_HYPERCALL_CONTEXT
        ApicInitSipi: win32more.Windows.Win32.System.Hypervisor.WHV_X64_APIC_INIT_SIPI_CONTEXT
        ApicWrite: win32more.Windows.Win32.System.Hypervisor.WHV_X64_APIC_WRITE_CONTEXT
        SynicSintDeliverable: win32more.Windows.Win32.System.Hypervisor.WHV_SYNIC_SINT_DELIVERABLE_CONTEXT
WHV_RUN_VP_EXIT_REASON = Int32
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonNone: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = 0
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonMemoryAccess: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = 1
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64IoPortAccess: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = 2
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonUnrecoverableException: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = 4
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonInvalidVpRegisterValue: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = 5
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonUnsupportedFeature: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = 6
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64InterruptWindow: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = 7
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64Halt: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = 8
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64ApicEoi: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = 9
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonSynicSintDeliverable: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = 10
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64MsrAccess: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = 4096
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64Cpuid: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = 4097
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonException: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = 4098
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64Rdtsc: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = 4099
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64ApicSmiTrap: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = 4100
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonHypercall: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = 4101
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64ApicInitSipiTrap: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = 4102
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64ApicWriteTrap: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = 4103
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonCanceled: win32more.Windows.Win32.System.Hypervisor.WHV_RUN_VP_EXIT_REASON = 8193
class WHV_SCHEDULER_FEATURES(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUINT64: UInt64
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt64
class WHV_SRIOV_RESOURCE_DESCRIPTOR(EasyCastStructure):
    PnpInstanceId: Char * 200
    VirtualFunctionId: win32more.Windows.Win32.Foundation.LUID
    VirtualFunctionIndex: UInt16
    Reserved: UInt16
class WHV_SYNIC_EVENT_PARAMETERS(EasyCastStructure):
    VpIndex: UInt32
    TargetSint: Byte
    Reserved: Byte
    FlagNumber: UInt16
class WHV_SYNIC_SINT_DELIVERABLE_CONTEXT(EasyCastStructure):
    DeliverableSints: UInt16
    Reserved1: UInt16
    Reserved2: UInt32
class WHV_SYNTHETIC_PROCESSOR_FEATURES(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUINT64: UInt64
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt64
class WHV_SYNTHETIC_PROCESSOR_FEATURES_BANKS(EasyCastStructure):
    BanksCount: UInt32
    Reserved0: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Anonymous: _Anonymous_e__Struct
        AsUINT64: UInt64 * 1
        class _Anonymous_e__Struct(EasyCastStructure):
            Bank0: win32more.Windows.Win32.System.Hypervisor.WHV_SYNTHETIC_PROCESSOR_FEATURES
WHV_TRANSLATE_GVA_FLAGS = Int32
WHV_TRANSLATE_GVA_FLAGS_WHvTranslateGvaFlagNone: win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_FLAGS = 0
WHV_TRANSLATE_GVA_FLAGS_WHvTranslateGvaFlagValidateRead: win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_FLAGS = 1
WHV_TRANSLATE_GVA_FLAGS_WHvTranslateGvaFlagValidateWrite: win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_FLAGS = 2
WHV_TRANSLATE_GVA_FLAGS_WHvTranslateGvaFlagValidateExecute: win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_FLAGS = 4
WHV_TRANSLATE_GVA_FLAGS_WHvTranslateGvaFlagPrivilegeExempt: win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_FLAGS = 8
WHV_TRANSLATE_GVA_FLAGS_WHvTranslateGvaFlagSetPageTableBits: win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_FLAGS = 16
WHV_TRANSLATE_GVA_FLAGS_WHvTranslateGvaFlagEnforceSmap: win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_FLAGS = 256
WHV_TRANSLATE_GVA_FLAGS_WHvTranslateGvaFlagOverrideSmap: win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_FLAGS = 512
class WHV_TRANSLATE_GVA_RESULT(EasyCastStructure):
    ResultCode: win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_RESULT_CODE
    Reserved: UInt32
WHV_TRANSLATE_GVA_RESULT_CODE = Int32
WHV_TRANSLATE_GVA_RESULT_CODE_WHvTranslateGvaResultSuccess: win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_RESULT_CODE = 0
WHV_TRANSLATE_GVA_RESULT_CODE_WHvTranslateGvaResultPageNotPresent: win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_RESULT_CODE = 1
WHV_TRANSLATE_GVA_RESULT_CODE_WHvTranslateGvaResultPrivilegeViolation: win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_RESULT_CODE = 2
WHV_TRANSLATE_GVA_RESULT_CODE_WHvTranslateGvaResultInvalidPageTableFlags: win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_RESULT_CODE = 3
WHV_TRANSLATE_GVA_RESULT_CODE_WHvTranslateGvaResultGpaUnmapped: win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_RESULT_CODE = 4
WHV_TRANSLATE_GVA_RESULT_CODE_WHvTranslateGvaResultGpaNoReadAccess: win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_RESULT_CODE = 5
WHV_TRANSLATE_GVA_RESULT_CODE_WHvTranslateGvaResultGpaNoWriteAccess: win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_RESULT_CODE = 6
WHV_TRANSLATE_GVA_RESULT_CODE_WHvTranslateGvaResultGpaIllegalOverlayAccess: win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_RESULT_CODE = 7
WHV_TRANSLATE_GVA_RESULT_CODE_WHvTranslateGvaResultIntercept: win32more.Windows.Win32.System.Hypervisor.WHV_TRANSLATE_GVA_RESULT_CODE = 8
class WHV_TRIGGER_PARAMETERS(EasyCastStructure):
    TriggerType: win32more.Windows.Win32.System.Hypervisor.WHV_TRIGGER_TYPE
    Reserved: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Interrupt: win32more.Windows.Win32.System.Hypervisor.WHV_INTERRUPT_CONTROL
        SynicEvent: win32more.Windows.Win32.System.Hypervisor.WHV_SYNIC_EVENT_PARAMETERS
        DeviceInterrupt: _DeviceInterrupt_e__Struct
        class _DeviceInterrupt_e__Struct(EasyCastStructure):
            LogicalDeviceId: UInt64
            MsiAddress: UInt64
            MsiData: UInt32
            Reserved: UInt32
WHV_TRIGGER_TYPE = Int32
WHV_TRIGGER_TYPE_WHvTriggerTypeInterrupt: win32more.Windows.Win32.System.Hypervisor.WHV_TRIGGER_TYPE = 0
WHV_TRIGGER_TYPE_WHvTriggerTypeSynicEvent: win32more.Windows.Win32.System.Hypervisor.WHV_TRIGGER_TYPE = 1
WHV_TRIGGER_TYPE_WHvTriggerTypeDeviceInterrupt: win32more.Windows.Win32.System.Hypervisor.WHV_TRIGGER_TYPE = 2
class WHV_UINT128(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    Dword: UInt32 * 4
    class _Anonymous_e__Struct(EasyCastStructure):
        Low64: UInt64
        High64: UInt64
class WHV_VIRTUAL_PROCESSOR_PROPERTY(EasyCastStructure):
    PropertyCode: win32more.Windows.Win32.System.Hypervisor.WHV_VIRTUAL_PROCESSOR_PROPERTY_CODE
    Reserved: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        NumaNode: UInt16
        Padding: UInt64
WHV_VIRTUAL_PROCESSOR_PROPERTY_CODE = Int32
WHV_VIRTUAL_PROCESSOR_PROPERTY_CODE_WHvVirtualProcessorPropertyCodeNumaNode: win32more.Windows.Win32.System.Hypervisor.WHV_VIRTUAL_PROCESSOR_PROPERTY_CODE = 0
WHV_VIRTUAL_PROCESSOR_STATE_TYPE = Int32
WHV_VIRTUAL_PROCESSOR_STATE_TYPE_WHvVirtualProcessorStateTypeSynicMessagePage: win32more.Windows.Win32.System.Hypervisor.WHV_VIRTUAL_PROCESSOR_STATE_TYPE = 0
WHV_VIRTUAL_PROCESSOR_STATE_TYPE_WHvVirtualProcessorStateTypeSynicEventFlagPage: win32more.Windows.Win32.System.Hypervisor.WHV_VIRTUAL_PROCESSOR_STATE_TYPE = 1
WHV_VIRTUAL_PROCESSOR_STATE_TYPE_WHvVirtualProcessorStateTypeSynicTimerState: win32more.Windows.Win32.System.Hypervisor.WHV_VIRTUAL_PROCESSOR_STATE_TYPE = 2
WHV_VIRTUAL_PROCESSOR_STATE_TYPE_WHvVirtualProcessorStateTypeInterruptControllerState2: win32more.Windows.Win32.System.Hypervisor.WHV_VIRTUAL_PROCESSOR_STATE_TYPE = 4096
WHV_VIRTUAL_PROCESSOR_STATE_TYPE_WHvVirtualProcessorStateTypeXsaveState: win32more.Windows.Win32.System.Hypervisor.WHV_VIRTUAL_PROCESSOR_STATE_TYPE = 4097
class WHV_VPCI_DEVICE_NOTIFICATION(EasyCastStructure):
    NotificationType: win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_DEVICE_NOTIFICATION_TYPE
    Reserved1: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Reserved2: UInt64
WHV_VPCI_DEVICE_NOTIFICATION_TYPE = Int32
WHV_VPCI_DEVICE_NOTIFICATION_TYPE_WHvVpciDeviceNotificationUndefined: win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_DEVICE_NOTIFICATION_TYPE = 0
WHV_VPCI_DEVICE_NOTIFICATION_TYPE_WHvVpciDeviceNotificationMmioRemapping: win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_DEVICE_NOTIFICATION_TYPE = 1
WHV_VPCI_DEVICE_NOTIFICATION_TYPE_WHvVpciDeviceNotificationSurpriseRemoval: win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_DEVICE_NOTIFICATION_TYPE = 2
WHV_VPCI_DEVICE_PROPERTY_CODE = Int32
WHV_VPCI_DEVICE_PROPERTY_CODE_WHvVpciDevicePropertyCodeUndefined: win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_DEVICE_PROPERTY_CODE = 0
WHV_VPCI_DEVICE_PROPERTY_CODE_WHvVpciDevicePropertyCodeHardwareIDs: win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_DEVICE_PROPERTY_CODE = 1
WHV_VPCI_DEVICE_PROPERTY_CODE_WHvVpciDevicePropertyCodeProbedBARs: win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_DEVICE_PROPERTY_CODE = 2
class WHV_VPCI_DEVICE_REGISTER(EasyCastStructure):
    Location: win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_DEVICE_REGISTER_SPACE
    SizeInBytes: UInt32
    OffsetInBytes: UInt64
WHV_VPCI_DEVICE_REGISTER_SPACE = Int32
WHV_VPCI_DEVICE_REGISTER_SPACE_WHvVpciConfigSpace: win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_DEVICE_REGISTER_SPACE = -1
WHV_VPCI_DEVICE_REGISTER_SPACE_WHvVpciBar0: win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_DEVICE_REGISTER_SPACE = 0
WHV_VPCI_DEVICE_REGISTER_SPACE_WHvVpciBar1: win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_DEVICE_REGISTER_SPACE = 1
WHV_VPCI_DEVICE_REGISTER_SPACE_WHvVpciBar2: win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_DEVICE_REGISTER_SPACE = 2
WHV_VPCI_DEVICE_REGISTER_SPACE_WHvVpciBar3: win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_DEVICE_REGISTER_SPACE = 3
WHV_VPCI_DEVICE_REGISTER_SPACE_WHvVpciBar4: win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_DEVICE_REGISTER_SPACE = 4
WHV_VPCI_DEVICE_REGISTER_SPACE_WHvVpciBar5: win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_DEVICE_REGISTER_SPACE = 5
class WHV_VPCI_HARDWARE_IDS(EasyCastStructure):
    VendorID: UInt16
    DeviceID: UInt16
    RevisionID: Byte
    ProgIf: Byte
    SubClass: Byte
    BaseClass: Byte
    SubVendorID: UInt16
    SubSystemID: UInt16
class WHV_VPCI_INTERRUPT_TARGET(EasyCastStructure):
    Vector: UInt32
    Flags: win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_INTERRUPT_TARGET_FLAGS
    ProcessorCount: UInt32
    Processors: UInt32 * 1
WHV_VPCI_INTERRUPT_TARGET_FLAGS = Int32
WHV_VPCI_INTERRUPT_TARGET_FLAGS_WHvVpciInterruptTargetFlagNone: win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_INTERRUPT_TARGET_FLAGS = 0
WHV_VPCI_INTERRUPT_TARGET_FLAGS_WHvVpciInterruptTargetFlagMulticast: win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_INTERRUPT_TARGET_FLAGS = 1
class WHV_VPCI_MMIO_MAPPING(EasyCastStructure):
    Location: win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_DEVICE_REGISTER_SPACE
    Flags: win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_MMIO_RANGE_FLAGS
    SizeInBytes: UInt64
    OffsetInBytes: UInt64
    VirtualAddress: VoidPtr
WHV_VPCI_MMIO_RANGE_FLAGS = Int32
WHV_VPCI_MMIO_RANGE_FLAGS_WHvVpciMmioRangeFlagReadAccess: win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_MMIO_RANGE_FLAGS = 1
WHV_VPCI_MMIO_RANGE_FLAGS_WHvVpciMmioRangeFlagWriteAccess: win32more.Windows.Win32.System.Hypervisor.WHV_VPCI_MMIO_RANGE_FLAGS = 2
class WHV_VPCI_PROBED_BARS(EasyCastStructure):
    Value: UInt32 * 6
class WHV_VP_EXCEPTION_CONTEXT(EasyCastStructure):
    InstructionByteCount: Byte
    Reserved: Byte * 3
    InstructionBytes: Byte * 16
    ExceptionInfo: win32more.Windows.Win32.System.Hypervisor.WHV_VP_EXCEPTION_INFO
    ExceptionType: Byte
    Reserved2: Byte * 3
    ErrorCode: UInt32
    ExceptionParameter: UInt64
class WHV_VP_EXCEPTION_INFO(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUINT32: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class WHV_VP_EXIT_CONTEXT(EasyCastStructure):
    ExecutionState: win32more.Windows.Win32.System.Hypervisor.WHV_X64_VP_EXECUTION_STATE
    _bitfield: Byte
    Reserved: Byte
    Reserved2: UInt32
    Cs: win32more.Windows.Win32.System.Hypervisor.WHV_X64_SEGMENT_REGISTER
    Rip: UInt64
    Rflags: UInt64
class WHV_X64_APIC_EOI_CONTEXT(EasyCastStructure):
    InterruptVector: UInt32
class WHV_X64_APIC_INIT_SIPI_CONTEXT(EasyCastStructure):
    ApicIcr: UInt64
class WHV_X64_APIC_SMI_CONTEXT(EasyCastStructure):
    ApicIcr: UInt64
class WHV_X64_APIC_WRITE_CONTEXT(EasyCastStructure):
    Type: win32more.Windows.Win32.System.Hypervisor.WHV_X64_APIC_WRITE_TYPE
    Reserved: UInt32
    WriteValue: UInt64
WHV_X64_APIC_WRITE_TYPE = Int32
WHV_X64_APIC_WRITE_TYPE_WHvX64ApicWriteTypeLdr: win32more.Windows.Win32.System.Hypervisor.WHV_X64_APIC_WRITE_TYPE = 208
WHV_X64_APIC_WRITE_TYPE_WHvX64ApicWriteTypeDfr: win32more.Windows.Win32.System.Hypervisor.WHV_X64_APIC_WRITE_TYPE = 224
WHV_X64_APIC_WRITE_TYPE_WHvX64ApicWriteTypeSvr: win32more.Windows.Win32.System.Hypervisor.WHV_X64_APIC_WRITE_TYPE = 240
WHV_X64_APIC_WRITE_TYPE_WHvX64ApicWriteTypeLint0: win32more.Windows.Win32.System.Hypervisor.WHV_X64_APIC_WRITE_TYPE = 848
WHV_X64_APIC_WRITE_TYPE_WHvX64ApicWriteTypeLint1: win32more.Windows.Win32.System.Hypervisor.WHV_X64_APIC_WRITE_TYPE = 864
class WHV_X64_CPUID_ACCESS_CONTEXT(EasyCastStructure):
    Rax: UInt64
    Rcx: UInt64
    Rdx: UInt64
    Rbx: UInt64
    DefaultResultRax: UInt64
    DefaultResultRcx: UInt64
    DefaultResultRdx: UInt64
    DefaultResultRbx: UInt64
class WHV_X64_CPUID_RESULT(EasyCastStructure):
    Function: UInt32
    Reserved: UInt32 * 3
    Eax: UInt32
    Ebx: UInt32
    Ecx: UInt32
    Edx: UInt32
class WHV_X64_CPUID_RESULT2(EasyCastStructure):
    Function: UInt32
    Index: UInt32
    VpIndex: UInt32
    Flags: win32more.Windows.Win32.System.Hypervisor.WHV_X64_CPUID_RESULT2_FLAGS
    Output: win32more.Windows.Win32.System.Hypervisor.WHV_CPUID_OUTPUT
    Mask: win32more.Windows.Win32.System.Hypervisor.WHV_CPUID_OUTPUT
WHV_X64_CPUID_RESULT2_FLAGS = Int32
WHV_X64_CPUID_RESULT2_FLAGS_WHvX64CpuidResult2FlagSubleafSpecific: win32more.Windows.Win32.System.Hypervisor.WHV_X64_CPUID_RESULT2_FLAGS = 1
WHV_X64_CPUID_RESULT2_FLAGS_WHvX64CpuidResult2FlagVpSpecific: win32more.Windows.Win32.System.Hypervisor.WHV_X64_CPUID_RESULT2_FLAGS = 2
class WHV_X64_DELIVERABILITY_NOTIFICATIONS_REGISTER(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUINT64: UInt64
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt64
class WHV_X64_FP_CONTROL_STATUS_REGISTER(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUINT128: win32more.Windows.Win32.System.Hypervisor.WHV_UINT128
    class _Anonymous_e__Struct(EasyCastStructure):
        FpControl: UInt16
        FpStatus: UInt16
        FpTag: Byte
        Reserved: Byte
        LastFpOp: UInt16
        Anonymous: _Anonymous_e__Union
        class _Anonymous_e__Union(EasyCastUnion):
            LastFpRip: UInt64
            Anonymous: _Anonymous_e__Struct
            class _Anonymous_e__Struct(EasyCastStructure):
                LastFpEip: UInt32
                LastFpCs: UInt16
                Reserved2: UInt16
class WHV_X64_FP_REGISTER(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUINT128: win32more.Windows.Win32.System.Hypervisor.WHV_UINT128
    class _Anonymous_e__Struct(EasyCastStructure):
        Mantissa: UInt64
        _bitfield: UInt64
class WHV_X64_INTERRUPTION_DELIVERABLE_CONTEXT(EasyCastStructure):
    DeliverableType: win32more.Windows.Win32.System.Hypervisor.WHV_X64_PENDING_INTERRUPTION_TYPE
class WHV_X64_INTERRUPT_STATE_REGISTER(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUINT64: UInt64
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt64
class WHV_X64_IO_PORT_ACCESS_CONTEXT(EasyCastStructure):
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
class WHV_X64_IO_PORT_ACCESS_INFO(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUINT32: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
WHV_X64_LOCAL_APIC_EMULATION_MODE = Int32
WHV_X64_LOCAL_APIC_EMULATION_MODE_WHvX64LocalApicEmulationModeNone: win32more.Windows.Win32.System.Hypervisor.WHV_X64_LOCAL_APIC_EMULATION_MODE = 0
WHV_X64_LOCAL_APIC_EMULATION_MODE_WHvX64LocalApicEmulationModeXApic: win32more.Windows.Win32.System.Hypervisor.WHV_X64_LOCAL_APIC_EMULATION_MODE = 1
WHV_X64_LOCAL_APIC_EMULATION_MODE_WHvX64LocalApicEmulationModeX2Apic: win32more.Windows.Win32.System.Hypervisor.WHV_X64_LOCAL_APIC_EMULATION_MODE = 2
class WHV_X64_MSR_ACCESS_CONTEXT(EasyCastStructure):
    AccessInfo: win32more.Windows.Win32.System.Hypervisor.WHV_X64_MSR_ACCESS_INFO
    MsrNumber: UInt32
    Rax: UInt64
    Rdx: UInt64
class WHV_X64_MSR_ACCESS_INFO(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUINT32: UInt32
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
class WHV_X64_MSR_EXIT_BITMAP(EasyCastUnion):
    AsUINT64: UInt64
    Anonymous: _Anonymous_e__Struct
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt64
class WHV_X64_PENDING_DEBUG_EXCEPTION(EasyCastUnion):
    AsUINT64: UInt64
    Anonymous: _Anonymous_e__Struct
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt64
WHV_X64_PENDING_EVENT_TYPE = Int32
WHV_X64_PENDING_EVENT_TYPE_WHvX64PendingEventException: win32more.Windows.Win32.System.Hypervisor.WHV_X64_PENDING_EVENT_TYPE = 0
WHV_X64_PENDING_EVENT_TYPE_WHvX64PendingEventExtInt: win32more.Windows.Win32.System.Hypervisor.WHV_X64_PENDING_EVENT_TYPE = 5
class WHV_X64_PENDING_EXCEPTION_EVENT(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUINT128: win32more.Windows.Win32.System.Hypervisor.WHV_UINT128
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
        ErrorCode: UInt32
        ExceptionParameter: UInt64
class WHV_X64_PENDING_EXT_INT_EVENT(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUINT128: win32more.Windows.Win32.System.Hypervisor.WHV_UINT128
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt64
        Reserved2: UInt64
class WHV_X64_PENDING_INTERRUPTION_REGISTER(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUINT64: UInt64
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt32
        ErrorCode: UInt32
WHV_X64_PENDING_INTERRUPTION_TYPE = Int32
WHV_X64_PENDING_INTERRUPTION_TYPE_WHvX64PendingInterrupt: win32more.Windows.Win32.System.Hypervisor.WHV_X64_PENDING_INTERRUPTION_TYPE = 0
WHV_X64_PENDING_INTERRUPTION_TYPE_WHvX64PendingNmi: win32more.Windows.Win32.System.Hypervisor.WHV_X64_PENDING_INTERRUPTION_TYPE = 2
WHV_X64_PENDING_INTERRUPTION_TYPE_WHvX64PendingException: win32more.Windows.Win32.System.Hypervisor.WHV_X64_PENDING_INTERRUPTION_TYPE = 3
class WHV_X64_RDTSC_CONTEXT(EasyCastStructure):
    TscAux: UInt64
    VirtualOffset: UInt64
    Tsc: UInt64
    ReferenceTime: UInt64
    RdtscInfo: win32more.Windows.Win32.System.Hypervisor.WHV_X64_RDTSC_INFO
class WHV_X64_RDTSC_INFO(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUINT64: UInt64
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt64
class WHV_X64_SEGMENT_REGISTER(EasyCastStructure):
    Base: UInt64
    Limit: UInt32
    Selector: UInt16
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Anonymous: _Anonymous_e__Struct
        Attributes: UInt16
        class _Anonymous_e__Struct(EasyCastStructure):
            _bitfield: UInt16
class WHV_X64_TABLE_REGISTER(EasyCastStructure):
    Pad: UInt16 * 3
    Limit: UInt16
    Base: UInt64
WHV_X64_UNSUPPORTED_FEATURE_CODE = Int32
WHV_X64_UNSUPPORTED_FEATURE_CODE_WHvUnsupportedFeatureIntercept: win32more.Windows.Win32.System.Hypervisor.WHV_X64_UNSUPPORTED_FEATURE_CODE = 1
WHV_X64_UNSUPPORTED_FEATURE_CODE_WHvUnsupportedFeatureTaskSwitchTss: win32more.Windows.Win32.System.Hypervisor.WHV_X64_UNSUPPORTED_FEATURE_CODE = 2
class WHV_X64_UNSUPPORTED_FEATURE_CONTEXT(EasyCastStructure):
    FeatureCode: win32more.Windows.Win32.System.Hypervisor.WHV_X64_UNSUPPORTED_FEATURE_CODE
    Reserved: UInt32
    FeatureParameter: UInt64
class WHV_X64_VP_EXECUTION_STATE(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUINT16: UInt16
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UInt16
class WHV_X64_XMM_CONTROL_STATUS_REGISTER(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    AsUINT128: win32more.Windows.Win32.System.Hypervisor.WHV_UINT128
    class _Anonymous_e__Struct(EasyCastStructure):
        Anonymous: _Anonymous_e__Union
        XmmStatusControl: UInt32
        XmmStatusControlMask: UInt32
        class _Anonymous_e__Union(EasyCastUnion):
            LastFpRdp: UInt64
            Anonymous: _Anonymous_e__Struct
            class _Anonymous_e__Struct(EasyCastStructure):
                LastFpDp: UInt32
                LastFpDs: UInt16
                Reserved: UInt16


make_ready(__name__)
