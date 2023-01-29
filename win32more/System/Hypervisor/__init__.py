from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Networking.WinSock
import win32more.System.HostComputeSystem
import win32more.System.Hypervisor
import win32more.System.Power
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        if name in _arch_optional:
            return None
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
HVSOCKET_CONNECT_TIMEOUT: UInt32 = 1
HVSOCKET_CONNECT_TIMEOUT_MAX: UInt32 = 300000
HVSOCKET_CONTAINER_PASSTHRU: UInt32 = 2
HVSOCKET_CONNECTED_SUSPEND: UInt32 = 4
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
HV_GUID_ZERO: Guid = Guid('00000000-0000-0000-00-00-00-00-00-00-00-00')
HV_GUID_BROADCAST: Guid = Guid('ffffffff-ffff-ffff-ff-ff-ff-ff-ff-ff-ff-ff')
HV_GUID_CHILDREN: Guid = Guid('90db8b89-0d35-4f79-8c-e9-49-ea-0a-c8-b7-cd')
HV_GUID_LOOPBACK: Guid = Guid('e0e16197-dd56-4a10-91-95-5e-e7-a1-55-a8-38')
HV_GUID_PARENT: Guid = Guid('a42e7cda-d03f-480c-9c-c2-a4-de-20-ab-b8-78')
HV_GUID_SILOHOST: Guid = Guid('36bd0c5c-7276-4223-88-ba-7d-03-b6-54-c5-68')
HV_GUID_VSOCK_TEMPLATE: Guid = Guid('00000000-facb-11e6-bd-58-64-00-6a-79-86-d3')
GUID_DEVINTERFACE_VM_GENCOUNTER: Guid = Guid('3ff2c92b-6598-4e60-8e-1c-0c-cf-49-27-e3-19')
@winfunctype('WinHvPlatform.dll')
def WHvGetCapability(CapabilityCode: win32more.System.Hypervisor.WHV_CAPABILITY_CODE, CapabilityBuffer: c_void_p, CapabilityBufferSizeInBytes: UInt32, WrittenSizeInBytes: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvCreatePartition(Partition: POINTER(win32more.System.Hypervisor.WHV_PARTITION_HANDLE)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvSetupPartition(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvResetPartition(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvDeletePartition(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvGetPartitionProperty(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, PropertyCode: win32more.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE, PropertyBuffer: c_void_p, PropertyBufferSizeInBytes: UInt32, WrittenSizeInBytes: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvSetPartitionProperty(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, PropertyCode: win32more.System.Hypervisor.WHV_PARTITION_PROPERTY_CODE, PropertyBuffer: c_void_p, PropertyBufferSizeInBytes: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvSuspendPartitionTime(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvResumePartitionTime(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvMapGpaRange(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, SourceAddress: c_void_p, GuestAddress: UInt64, SizeInBytes: UInt64, Flags: win32more.System.Hypervisor.WHV_MAP_GPA_RANGE_FLAGS) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvMapGpaRange2(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, Process: win32more.Foundation.HANDLE, SourceAddress: c_void_p, GuestAddress: UInt64, SizeInBytes: UInt64, Flags: win32more.System.Hypervisor.WHV_MAP_GPA_RANGE_FLAGS) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvUnmapGpaRange(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, GuestAddress: UInt64, SizeInBytes: UInt64) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvTranslateGva(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, Gva: UInt64, TranslateFlags: win32more.System.Hypervisor.WHV_TRANSLATE_GVA_FLAGS, TranslationResult: POINTER(win32more.System.Hypervisor.WHV_TRANSLATE_GVA_RESULT_head), Gpa: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvCreateVirtualProcessor(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, Flags: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvCreateVirtualProcessor2(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, Properties: POINTER(win32more.System.Hypervisor.WHV_VIRTUAL_PROCESSOR_PROPERTY_head), PropertyCount: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvDeleteVirtualProcessor(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvRunVirtualProcessor(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, ExitContext: c_void_p, ExitContextSizeInBytes: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvCancelRunVirtualProcessor(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, Flags: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvGetVirtualProcessorRegisters(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, RegisterNames: POINTER(win32more.System.Hypervisor.WHV_REGISTER_NAME), RegisterCount: UInt32, RegisterValues: POINTER(win32more.System.Hypervisor.WHV_REGISTER_VALUE_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvSetVirtualProcessorRegisters(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, RegisterNames: POINTER(win32more.System.Hypervisor.WHV_REGISTER_NAME), RegisterCount: UInt32, RegisterValues: POINTER(win32more.System.Hypervisor.WHV_REGISTER_VALUE_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvGetVirtualProcessorInterruptControllerState(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, State: c_void_p, StateSize: UInt32, WrittenSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvSetVirtualProcessorInterruptControllerState(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, State: c_void_p, StateSize: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvRequestInterrupt(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, Interrupt: POINTER(win32more.System.Hypervisor.WHV_INTERRUPT_CONTROL_head), InterruptControlSize: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvGetVirtualProcessorXsaveState(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, Buffer: c_void_p, BufferSizeInBytes: UInt32, BytesWritten: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvSetVirtualProcessorXsaveState(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, Buffer: c_void_p, BufferSizeInBytes: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvQueryGpaRangeDirtyBitmap(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, GuestAddress: UInt64, RangeSizeInBytes: UInt64, Bitmap: POINTER(UInt64), BitmapSizeInBytes: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvGetPartitionCounters(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, CounterSet: win32more.System.Hypervisor.WHV_PARTITION_COUNTER_SET, Buffer: c_void_p, BufferSizeInBytes: UInt32, BytesWritten: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvGetVirtualProcessorCounters(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, CounterSet: win32more.System.Hypervisor.WHV_PROCESSOR_COUNTER_SET, Buffer: c_void_p, BufferSizeInBytes: UInt32, BytesWritten: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvGetVirtualProcessorInterruptControllerState2(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, State: c_void_p, StateSize: UInt32, WrittenSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvSetVirtualProcessorInterruptControllerState2(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, State: c_void_p, StateSize: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvRegisterPartitionDoorbellEvent(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, MatchData: POINTER(win32more.System.Hypervisor.WHV_DOORBELL_MATCH_DATA_head), EventHandle: win32more.Foundation.HANDLE) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvUnregisterPartitionDoorbellEvent(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, MatchData: POINTER(win32more.System.Hypervisor.WHV_DOORBELL_MATCH_DATA_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvAdviseGpaRange(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, GpaRanges: POINTER(win32more.System.Hypervisor.WHV_MEMORY_RANGE_ENTRY_head), GpaRangesCount: UInt32, Advice: win32more.System.Hypervisor.WHV_ADVISE_GPA_RANGE_CODE, AdviceBuffer: c_void_p, AdviceBufferSizeInBytes: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvReadGpaRange(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, GuestAddress: UInt64, Controls: win32more.System.Hypervisor.WHV_ACCESS_GPA_CONTROLS, Data: c_void_p, DataSizeInBytes: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvWriteGpaRange(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, GuestAddress: UInt64, Controls: win32more.System.Hypervisor.WHV_ACCESS_GPA_CONTROLS, Data: c_void_p, DataSizeInBytes: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvSignalVirtualProcessorSynicEvent(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, SynicEvent: win32more.System.Hypervisor.WHV_SYNIC_EVENT_PARAMETERS, NewlySignaled: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvGetVirtualProcessorState(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, StateType: win32more.System.Hypervisor.WHV_VIRTUAL_PROCESSOR_STATE_TYPE, Buffer: c_void_p, BufferSizeInBytes: UInt32, BytesWritten: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvSetVirtualProcessorState(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, StateType: win32more.System.Hypervisor.WHV_VIRTUAL_PROCESSOR_STATE_TYPE, Buffer: c_void_p, BufferSizeInBytes: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvAllocateVpciResource(ProviderId: POINTER(Guid), Flags: win32more.System.Hypervisor.WHV_ALLOCATE_VPCI_RESOURCE_FLAGS, ResourceDescriptor: c_void_p, ResourceDescriptorSizeInBytes: UInt32, VpciResource: POINTER(win32more.Foundation.HANDLE)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvCreateVpciDevice(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, LogicalDeviceId: UInt64, VpciResource: win32more.Foundation.HANDLE, Flags: win32more.System.Hypervisor.WHV_CREATE_VPCI_DEVICE_FLAGS, NotificationEventHandle: win32more.Foundation.HANDLE) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvDeleteVpciDevice(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, LogicalDeviceId: UInt64) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvGetVpciDeviceProperty(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, LogicalDeviceId: UInt64, PropertyCode: win32more.System.Hypervisor.WHV_VPCI_DEVICE_PROPERTY_CODE, PropertyBuffer: c_void_p, PropertyBufferSizeInBytes: UInt32, WrittenSizeInBytes: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvGetVpciDeviceNotification(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, LogicalDeviceId: UInt64, Notification: POINTER(win32more.System.Hypervisor.WHV_VPCI_DEVICE_NOTIFICATION_head), NotificationSizeInBytes: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvMapVpciDeviceMmioRanges(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, LogicalDeviceId: UInt64, MappingCount: POINTER(UInt32), Mappings: POINTER(POINTER(win32more.System.Hypervisor.WHV_VPCI_MMIO_MAPPING_head))) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvUnmapVpciDeviceMmioRanges(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, LogicalDeviceId: UInt64) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvSetVpciDevicePowerState(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, LogicalDeviceId: UInt64, PowerState: win32more.System.Power.DEVICE_POWER_STATE) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvReadVpciDeviceRegister(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, LogicalDeviceId: UInt64, Register: POINTER(win32more.System.Hypervisor.WHV_VPCI_DEVICE_REGISTER_head), Data: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvWriteVpciDeviceRegister(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, LogicalDeviceId: UInt64, Register: POINTER(win32more.System.Hypervisor.WHV_VPCI_DEVICE_REGISTER_head), Data: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvMapVpciDeviceInterrupt(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, LogicalDeviceId: UInt64, Index: UInt32, MessageCount: UInt32, Target: POINTER(win32more.System.Hypervisor.WHV_VPCI_INTERRUPT_TARGET_head), MsiAddress: POINTER(UInt64), MsiData: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvUnmapVpciDeviceInterrupt(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, LogicalDeviceId: UInt64, Index: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvRetargetVpciDeviceInterrupt(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, LogicalDeviceId: UInt64, MsiAddress: UInt64, MsiData: UInt32, Target: POINTER(win32more.System.Hypervisor.WHV_VPCI_INTERRUPT_TARGET_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvRequestVpciDeviceInterrupt(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, LogicalDeviceId: UInt64, MsiAddress: UInt64, MsiData: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvGetVpciDeviceInterruptTarget(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, LogicalDeviceId: UInt64, Index: UInt32, MultiMessageNumber: UInt32, Target: POINTER(win32more.System.Hypervisor.WHV_VPCI_INTERRUPT_TARGET_head), TargetSizeInBytes: UInt32, BytesWritten: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvCreateTrigger(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, Parameters: POINTER(win32more.System.Hypervisor.WHV_TRIGGER_PARAMETERS_head), TriggerHandle: POINTER(c_void_p), EventHandle: POINTER(win32more.Foundation.HANDLE)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvUpdateTriggerParameters(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, Parameters: POINTER(win32more.System.Hypervisor.WHV_TRIGGER_PARAMETERS_head), TriggerHandle: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvDeleteTrigger(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, TriggerHandle: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvCreateNotificationPort(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, Parameters: POINTER(win32more.System.Hypervisor.WHV_NOTIFICATION_PORT_PARAMETERS_head), EventHandle: win32more.Foundation.HANDLE, PortHandle: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvSetNotificationPortProperty(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, PortHandle: c_void_p, PropertyCode: win32more.System.Hypervisor.WHV_NOTIFICATION_PORT_PROPERTY_CODE, PropertyValue: UInt64) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvDeleteNotificationPort(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, PortHandle: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvPostVirtualProcessorSynicMessage(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, SintIndex: UInt32, Message: c_void_p, MessageSizeInBytes: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvGetVirtualProcessorCpuidOutput(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, VpIndex: UInt32, Eax: UInt32, Ecx: UInt32, CpuidOutput: POINTER(win32more.System.Hypervisor.WHV_CPUID_OUTPUT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvGetInterruptTargetVpSet(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, Destination: UInt64, DestinationMode: win32more.System.Hypervisor.WHV_INTERRUPT_DESTINATION_MODE, TargetVps: POINTER(UInt32), VpCount: UInt32, TargetVpCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvStartPartitionMigration(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE, MigrationHandle: POINTER(win32more.Foundation.HANDLE)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvCancelPartitionMigration(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvCompletePartitionMigration(Partition: win32more.System.Hypervisor.WHV_PARTITION_HANDLE) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvPlatform.dll')
def WHvAcceptPartitionMigration(MigrationHandle: win32more.Foundation.HANDLE, Partition: POINTER(win32more.System.Hypervisor.WHV_PARTITION_HANDLE)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvEmulation.dll')
def WHvEmulatorCreateEmulator(Callbacks: POINTER(win32more.System.Hypervisor.WHV_EMULATOR_CALLBACKS_head), Emulator: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvEmulation.dll')
def WHvEmulatorDestroyEmulator(Emulator: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvEmulation.dll')
def WHvEmulatorTryIoEmulation(Emulator: c_void_p, Context: c_void_p, VpContext: POINTER(win32more.System.Hypervisor.WHV_VP_EXIT_CONTEXT_head), IoInstructionContext: POINTER(win32more.System.Hypervisor.WHV_X64_IO_PORT_ACCESS_CONTEXT_head), EmulatorReturnStatus: POINTER(win32more.System.Hypervisor.WHV_EMULATOR_STATUS_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WinHvEmulation.dll')
def WHvEmulatorTryMmioEmulation(Emulator: c_void_p, Context: c_void_p, VpContext: POINTER(win32more.System.Hypervisor.WHV_VP_EXIT_CONTEXT_head), MmioInstructionContext: POINTER(win32more.System.Hypervisor.WHV_MEMORY_ACCESS_CONTEXT_head), EmulatorReturnStatus: POINTER(win32more.System.Hypervisor.WHV_EMULATOR_STATUS_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('vmdevicehost.dll')
def HdvInitializeDeviceHost(computeSystem: win32more.System.HostComputeSystem.HCS_SYSTEM, deviceHostHandle: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('vmdevicehost.dll')
def HdvTeardownDeviceHost(deviceHostHandle: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('vmdevicehost.dll')
def HdvCreateDeviceInstance(deviceHostHandle: c_void_p, deviceType: win32more.System.Hypervisor.HDV_DEVICE_TYPE, deviceClassId: POINTER(Guid), deviceInstanceId: POINTER(Guid), deviceInterface: c_void_p, deviceContext: c_void_p, deviceHandle: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('vmdevicehost.dll')
def HdvReadGuestMemory(requestor: c_void_p, guestPhysicalAddress: UInt64, byteCount: UInt32, buffer: c_char_p_no) -> win32more.Foundation.HRESULT: ...
@winfunctype('vmdevicehost.dll')
def HdvWriteGuestMemory(requestor: c_void_p, guestPhysicalAddress: UInt64, byteCount: UInt32, buffer: c_char_p_no) -> win32more.Foundation.HRESULT: ...
@winfunctype('vmdevicehost.dll')
def HdvCreateGuestMemoryAperture(requestor: c_void_p, guestPhysicalAddress: UInt64, byteCount: UInt32, writeProtected: win32more.Foundation.BOOL, mappedAddress: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('vmdevicehost.dll')
def HdvDestroyGuestMemoryAperture(requestor: c_void_p, mappedAddress: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('vmdevicehost.dll')
def HdvDeliverGuestInterrupt(requestor: c_void_p, msiAddress: UInt64, msiData: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('vmdevicehost.dll')
def HdvRegisterDoorbell(requestor: c_void_p, BarIndex: win32more.System.Hypervisor.HDV_PCI_BAR_SELECTOR, BarOffset: UInt64, TriggerValue: UInt64, Flags: UInt64, DoorbellEvent: win32more.Foundation.HANDLE) -> win32more.Foundation.HRESULT: ...
@winfunctype('vmdevicehost.dll')
def HdvUnregisterDoorbell(requestor: c_void_p, BarIndex: win32more.System.Hypervisor.HDV_PCI_BAR_SELECTOR, BarOffset: UInt64, TriggerValue: UInt64, Flags: UInt64) -> win32more.Foundation.HRESULT: ...
@winfunctype('vmdevicehost.dll')
def HdvCreateSectionBackedMmioRange(requestor: c_void_p, barIndex: win32more.System.Hypervisor.HDV_PCI_BAR_SELECTOR, offsetInPages: UInt64, lengthInPages: UInt64, MappingFlags: win32more.System.Hypervisor.HDV_MMIO_MAPPING_FLAGS, sectionHandle: win32more.Foundation.HANDLE, sectionOffsetInPages: UInt64) -> win32more.Foundation.HRESULT: ...
@winfunctype('vmdevicehost.dll')
def HdvDestroySectionBackedMmioRange(requestor: c_void_p, barIndex: win32more.System.Hypervisor.HDV_PCI_BAR_SELECTOR, offsetInPages: UInt64) -> win32more.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def LocateSavedStateFiles(vmName: win32more.Foundation.PWSTR, snapshotName: win32more.Foundation.PWSTR, binPath: POINTER(win32more.Foundation.PWSTR), vsvPath: POINTER(win32more.Foundation.PWSTR), vmrsPath: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def LoadSavedStateFile(vmrsFile: win32more.Foundation.PWSTR, vmSavedStateDumpHandle: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def ApplyPendingSavedStateFileReplayLog(vmrsFile: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def LoadSavedStateFiles(binFile: win32more.Foundation.PWSTR, vsvFile: win32more.Foundation.PWSTR, vmSavedStateDumpHandle: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def ReleaseSavedStateFiles(vmSavedStateDumpHandle: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def GetGuestEnabledVirtualTrustLevels(vmSavedStateDumpHandle: c_void_p, virtualTrustLevels: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def GetGuestOsInfo(vmSavedStateDumpHandle: c_void_p, virtualTrustLevel: Byte, guestOsInfo: POINTER(win32more.System.Hypervisor.GUEST_OS_INFO_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def GetVpCount(vmSavedStateDumpHandle: c_void_p, vpCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def GetArchitecture(vmSavedStateDumpHandle: c_void_p, vpId: UInt32, architecture: POINTER(win32more.System.Hypervisor.VIRTUAL_PROCESSOR_ARCH)) -> win32more.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def ForceArchitecture(vmSavedStateDumpHandle: c_void_p, vpId: UInt32, architecture: win32more.System.Hypervisor.VIRTUAL_PROCESSOR_ARCH) -> win32more.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def GetActiveVirtualTrustLevel(vmSavedStateDumpHandle: c_void_p, vpId: UInt32, virtualTrustLevel: c_char_p_no) -> win32more.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def GetEnabledVirtualTrustLevels(vmSavedStateDumpHandle: c_void_p, vpId: UInt32, virtualTrustLevels: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def ForceActiveVirtualTrustLevel(vmSavedStateDumpHandle: c_void_p, vpId: UInt32, virtualTrustLevel: Byte) -> win32more.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def IsActiveVirtualTrustLevelEnabled(vmSavedStateDumpHandle: c_void_p, vpId: UInt32, activeVirtualTrustLevelEnabled: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def IsNestedVirtualizationEnabled(vmSavedStateDumpHandle: c_void_p, enabled: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def GetNestedVirtualizationMode(vmSavedStateDumpHandle: c_void_p, vpId: UInt32, enabled: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def ForceNestedHostMode(vmSavedStateDumpHandle: c_void_p, vpId: UInt32, hostMode: win32more.Foundation.BOOL, oldMode: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def InKernelSpace(vmSavedStateDumpHandle: c_void_p, vpId: UInt32, inKernelSpace: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def GetRegisterValue(vmSavedStateDumpHandle: c_void_p, vpId: UInt32, registerId: UInt32, registerValue: POINTER(win32more.System.Hypervisor.VIRTUAL_PROCESSOR_REGISTER_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def GetPagingMode(vmSavedStateDumpHandle: c_void_p, vpId: UInt32, pagingMode: POINTER(win32more.System.Hypervisor.PAGING_MODE)) -> win32more.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def ForcePagingMode(vmSavedStateDumpHandle: c_void_p, vpId: UInt32, pagingMode: win32more.System.Hypervisor.PAGING_MODE) -> win32more.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def ReadGuestPhysicalAddress(vmSavedStateDumpHandle: c_void_p, physicalAddress: UInt64, buffer: c_void_p, bufferSize: UInt32, bytesRead: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def GuestVirtualAddressToPhysicalAddress(vmSavedStateDumpHandle: c_void_p, vpId: UInt32, virtualAddress: UInt64, physicalAddress: POINTER(UInt64), unmappedRegionSize: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def GetGuestPhysicalMemoryChunks(vmSavedStateDumpHandle: c_void_p, memoryChunkPageSize: POINTER(UInt64), memoryChunks: POINTER(win32more.System.Hypervisor.GPA_MEMORY_CHUNK_head), memoryChunkCount: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def GuestPhysicalAddressToRawSavedMemoryOffset(vmSavedStateDumpHandle: c_void_p, physicalAddress: UInt64, rawSavedMemoryOffset: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def ReadGuestRawSavedMemory(vmSavedStateDumpHandle: c_void_p, rawSavedMemoryOffset: UInt64, buffer: c_void_p, bufferSize: UInt32, bytesRead: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def GetGuestRawSavedMemorySize(vmSavedStateDumpHandle: c_void_p, guestRawSavedMemorySize: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def SetMemoryBlockCacheLimit(vmSavedStateDumpHandle: c_void_p, memoryBlockCacheLimit: UInt64) -> win32more.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def GetMemoryBlockCacheLimit(vmSavedStateDumpHandle: c_void_p, memoryBlockCacheLimit: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def ApplyGuestMemoryFix(vmSavedStateDumpHandle: c_void_p, vpId: UInt32, virtualAddress: UInt64, fixBuffer: c_void_p, fixBufferSize: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def LoadSavedStateSymbolProvider(vmSavedStateDumpHandle: c_void_p, userSymbols: win32more.Foundation.PWSTR, force: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def ReleaseSavedStateSymbolProvider(vmSavedStateDumpHandle: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def GetSavedStateSymbolProviderHandle(vmSavedStateDumpHandle: c_void_p) -> win32more.Foundation.HANDLE: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def SetSavedStateSymbolProviderDebugInfoCallback(vmSavedStateDumpHandle: c_void_p, Callback: win32more.System.Hypervisor.GUEST_SYMBOLS_PROVIDER_DEBUG_INFO_CALLBACK) -> win32more.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def LoadSavedStateModuleSymbols(vmSavedStateDumpHandle: c_void_p, imageName: win32more.Foundation.PSTR, moduleName: win32more.Foundation.PSTR, baseAddress: UInt64, sizeOfBase: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def LoadSavedStateModuleSymbolsEx(vmSavedStateDumpHandle: c_void_p, imageName: win32more.Foundation.PSTR, imageTimestamp: UInt32, moduleName: win32more.Foundation.PSTR, baseAddress: UInt64, sizeOfBase: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def ResolveSavedStateGlobalVariableAddress(vmSavedStateDumpHandle: c_void_p, vpId: UInt32, globalName: win32more.Foundation.PSTR, virtualAddress: POINTER(UInt64), size: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def ReadSavedStateGlobalVariable(vmSavedStateDumpHandle: c_void_p, vpId: UInt32, globalName: win32more.Foundation.PSTR, buffer: c_void_p, bufferSize: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def GetSavedStateSymbolTypeSize(vmSavedStateDumpHandle: c_void_p, vpId: UInt32, typeName: win32more.Foundation.PSTR, size: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def FindSavedStateSymbolFieldInType(vmSavedStateDumpHandle: c_void_p, vpId: UInt32, typeName: win32more.Foundation.PSTR, fieldName: win32more.Foundation.PWSTR, offset: POINTER(UInt32), found: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def GetSavedStateSymbolFieldInfo(vmSavedStateDumpHandle: c_void_p, vpId: UInt32, typeName: win32more.Foundation.PSTR, typeFieldInfoMap: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def ScanMemoryForDosImages(vmSavedStateDumpHandle: c_void_p, vpId: UInt32, startAddress: UInt64, endAddress: UInt64, callbackContext: c_void_p, foundImageCallback: win32more.System.Hypervisor.FOUND_IMAGE_CALLBACK, standaloneAddress: POINTER(UInt64), standaloneAddressCount: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('VmSavedStateDumpProvider.dll')
def CallStackUnwind(vmSavedStateDumpHandle: c_void_p, vpId: UInt32, imageInfo: POINTER(win32more.System.Hypervisor.MODULE_INFO_head), imageInfoCount: UInt32, frameCount: UInt32, callStack: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
class DOS_IMAGE_INFO(Structure):
    PdbName: win32more.Foundation.PSTR
    ImageBaseAddress: UInt64
    ImageSize: UInt32
    Timestamp: UInt32
@winfunctype_pointer
def FOUND_IMAGE_CALLBACK(Context: c_void_p, ImageInfo: POINTER(win32more.System.Hypervisor.DOS_IMAGE_INFO_head)) -> win32more.Foundation.BOOL: ...
class GPA_MEMORY_CHUNK(Structure):
    GuestPhysicalStartPageIndex: UInt64
    PageCount: UInt64
class GUEST_OS_INFO(Union):
    AsUINT64: UInt64
    ClosedSource: _ClosedSource_e__Struct
    OpenSource: _OpenSource_e__Struct
    class _ClosedSource_e__Struct(Structure):
        _bitfield: UInt64
    class _OpenSource_e__Struct(Structure):
        _bitfield: UInt64
GUEST_OS_MICROSOFT_IDS = Int32
GUEST_OS_MICROSOFT_IDS_GuestOsMicrosoftUndefined: GUEST_OS_MICROSOFT_IDS = 0
GUEST_OS_MICROSOFT_IDS_GuestOsMicrosoftMSDOS: GUEST_OS_MICROSOFT_IDS = 1
GUEST_OS_MICROSOFT_IDS_GuestOsMicrosoftWindows3x: GUEST_OS_MICROSOFT_IDS = 2
GUEST_OS_MICROSOFT_IDS_GuestOsMicrosoftWindows9x: GUEST_OS_MICROSOFT_IDS = 3
GUEST_OS_MICROSOFT_IDS_GuestOsMicrosoftWindowsNT: GUEST_OS_MICROSOFT_IDS = 4
GUEST_OS_MICROSOFT_IDS_GuestOsMicrosoftWindowsCE: GUEST_OS_MICROSOFT_IDS = 5
GUEST_OS_OPENSOURCE_IDS = Int32
GUEST_OS_OPENSOURCE_IDS_GuestOsOpenSourceUndefined: GUEST_OS_OPENSOURCE_IDS = 0
GUEST_OS_OPENSOURCE_IDS_GuestOsOpenSourceLinux: GUEST_OS_OPENSOURCE_IDS = 1
GUEST_OS_OPENSOURCE_IDS_GuestOsOpenSourceFreeBSD: GUEST_OS_OPENSOURCE_IDS = 2
GUEST_OS_OPENSOURCE_IDS_GuestOsOpenSourceXen: GUEST_OS_OPENSOURCE_IDS = 3
GUEST_OS_OPENSOURCE_IDS_GuestOsOpenSourceIllumos: GUEST_OS_OPENSOURCE_IDS = 4
GUEST_OS_VENDOR = Int32
GUEST_OS_VENDOR_GuestOsVendorUndefined: GUEST_OS_VENDOR = 0
GUEST_OS_VENDOR_GuestOsVendorMicrosoft: GUEST_OS_VENDOR = 1
GUEST_OS_VENDOR_GuestOsVendorHPE: GUEST_OS_VENDOR = 2
GUEST_OS_VENDOR_GuestOsVendorLANCOM: GUEST_OS_VENDOR = 512
@winfunctype_pointer
def GUEST_SYMBOLS_PROVIDER_DEBUG_INFO_CALLBACK(InfoMessage: win32more.Foundation.PSTR) -> Void: ...
HDV_DEVICE_TYPE = Int32
HDV_DEVICE_TYPE_HdvDeviceTypeUndefined: HDV_DEVICE_TYPE = 0
HDV_DEVICE_TYPE_HdvDeviceTypePCI: HDV_DEVICE_TYPE = 1
HDV_DOORBELL_FLAGS = Int32
HDV_DOORBELL_FLAG_TRIGGER_SIZE_ANY: HDV_DOORBELL_FLAGS = 0
HDV_DOORBELL_FLAG_TRIGGER_SIZE_BYTE: HDV_DOORBELL_FLAGS = 1
HDV_DOORBELL_FLAG_TRIGGER_SIZE_WORD: HDV_DOORBELL_FLAGS = 2
HDV_DOORBELL_FLAG_TRIGGER_SIZE_DWORD: HDV_DOORBELL_FLAGS = 3
HDV_DOORBELL_FLAG_TRIGGER_SIZE_QWORD: HDV_DOORBELL_FLAGS = 4
HDV_DOORBELL_FLAG_TRIGGER_ANY_VALUE: HDV_DOORBELL_FLAGS = -2147483648
HDV_MMIO_MAPPING_FLAGS = UInt32
HDV_MMIO_MAPPING_FLAGS_HdvMmioMappingFlagNone: HDV_MMIO_MAPPING_FLAGS = 0
HDV_MMIO_MAPPING_FLAGS_HdvMmioMappingFlagWriteable: HDV_MMIO_MAPPING_FLAGS = 1
HDV_MMIO_MAPPING_FLAGS_HdvMmioMappingFlagExecutable: HDV_MMIO_MAPPING_FLAGS = 2
HDV_PCI_BAR_SELECTOR = Int32
HDV_PCI_BAR0: HDV_PCI_BAR_SELECTOR = 0
HDV_PCI_BAR1: HDV_PCI_BAR_SELECTOR = 1
HDV_PCI_BAR2: HDV_PCI_BAR_SELECTOR = 2
HDV_PCI_BAR3: HDV_PCI_BAR_SELECTOR = 3
HDV_PCI_BAR4: HDV_PCI_BAR_SELECTOR = 4
HDV_PCI_BAR5: HDV_PCI_BAR_SELECTOR = 5
@winfunctype_pointer
def HDV_PCI_DEVICE_GET_DETAILS(deviceContext: c_void_p, pnpId: POINTER(win32more.System.Hypervisor.HDV_PCI_PNP_ID_head), probedBarsCount: UInt32, probedBars: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def HDV_PCI_DEVICE_INITIALIZE(deviceContext: c_void_p) -> win32more.Foundation.HRESULT: ...
class HDV_PCI_DEVICE_INTERFACE(Structure):
    Version: win32more.System.Hypervisor.HDV_PCI_INTERFACE_VERSION
    Initialize: win32more.System.Hypervisor.HDV_PCI_DEVICE_INITIALIZE
    Teardown: win32more.System.Hypervisor.HDV_PCI_DEVICE_TEARDOWN
    SetConfiguration: win32more.System.Hypervisor.HDV_PCI_DEVICE_SET_CONFIGURATION
    GetDetails: win32more.System.Hypervisor.HDV_PCI_DEVICE_GET_DETAILS
    Start: win32more.System.Hypervisor.HDV_PCI_DEVICE_START
    Stop: win32more.System.Hypervisor.HDV_PCI_DEVICE_STOP
    ReadConfigSpace: win32more.System.Hypervisor.HDV_PCI_READ_CONFIG_SPACE
    WriteConfigSpace: win32more.System.Hypervisor.HDV_PCI_WRITE_CONFIG_SPACE
    ReadInterceptedMemory: win32more.System.Hypervisor.HDV_PCI_READ_INTERCEPTED_MEMORY
    WriteInterceptedMemory: win32more.System.Hypervisor.HDV_PCI_WRITE_INTERCEPTED_MEMORY
@winfunctype_pointer
def HDV_PCI_DEVICE_SET_CONFIGURATION(deviceContext: c_void_p, configurationValueCount: UInt32, configurationValues: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def HDV_PCI_DEVICE_START(deviceContext: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def HDV_PCI_DEVICE_STOP(deviceContext: c_void_p) -> Void: ...
@winfunctype_pointer
def HDV_PCI_DEVICE_TEARDOWN(deviceContext: c_void_p) -> Void: ...
HDV_PCI_INTERFACE_VERSION = Int32
HDV_PCI_INTERFACE_VERSION_HdvPciDeviceInterfaceVersionInvalid: HDV_PCI_INTERFACE_VERSION = 0
HDV_PCI_INTERFACE_VERSION_HdvPciDeviceInterfaceVersion1: HDV_PCI_INTERFACE_VERSION = 1
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
def HDV_PCI_READ_CONFIG_SPACE(deviceContext: c_void_p, offset: UInt32, value: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def HDV_PCI_READ_INTERCEPTED_MEMORY(deviceContext: c_void_p, barIndex: win32more.System.Hypervisor.HDV_PCI_BAR_SELECTOR, offset: UInt64, length: UInt64, value: c_char_p_no) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def HDV_PCI_WRITE_CONFIG_SPACE(deviceContext: c_void_p, offset: UInt32, value: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def HDV_PCI_WRITE_INTERCEPTED_MEMORY(deviceContext: c_void_p, barIndex: win32more.System.Hypervisor.HDV_PCI_BAR_SELECTOR, offset: UInt64, length: UInt64, value: c_char_p_no) -> win32more.Foundation.HRESULT: ...
class HVSOCKET_ADDRESS_INFO(Structure):
    SystemId: Guid
    VirtualMachineId: Guid
    SiloId: Guid
    Flags: UInt32
class MODULE_INFO(Structure):
    ProcessImageName: win32more.Foundation.PSTR
    Image: win32more.System.Hypervisor.DOS_IMAGE_INFO
PAGING_MODE = Int32
Paging_Invalid: PAGING_MODE = 0
Paging_NonPaged: PAGING_MODE = 1
Paging_32Bit: PAGING_MODE = 2
Paging_Pae: PAGING_MODE = 3
Paging_Long: PAGING_MODE = 4
Paging_Armv8: PAGING_MODE = 5
REGISTER_ID = Int32
X64_RegisterRax: REGISTER_ID = 0
X64_RegisterRcx: REGISTER_ID = 1
X64_RegisterRdx: REGISTER_ID = 2
X64_RegisterRbx: REGISTER_ID = 3
X64_RegisterRsp: REGISTER_ID = 4
X64_RegisterRbp: REGISTER_ID = 5
X64_RegisterRsi: REGISTER_ID = 6
X64_RegisterRdi: REGISTER_ID = 7
X64_RegisterR8: REGISTER_ID = 8
X64_RegisterR9: REGISTER_ID = 9
X64_RegisterR10: REGISTER_ID = 10
X64_RegisterR11: REGISTER_ID = 11
X64_RegisterR12: REGISTER_ID = 12
X64_RegisterR13: REGISTER_ID = 13
X64_RegisterR14: REGISTER_ID = 14
X64_RegisterR15: REGISTER_ID = 15
X64_RegisterRip: REGISTER_ID = 16
X64_RegisterRFlags: REGISTER_ID = 17
X64_RegisterXmm0: REGISTER_ID = 18
X64_RegisterXmm1: REGISTER_ID = 19
X64_RegisterXmm2: REGISTER_ID = 20
X64_RegisterXmm3: REGISTER_ID = 21
X64_RegisterXmm4: REGISTER_ID = 22
X64_RegisterXmm5: REGISTER_ID = 23
X64_RegisterXmm6: REGISTER_ID = 24
X64_RegisterXmm7: REGISTER_ID = 25
X64_RegisterXmm8: REGISTER_ID = 26
X64_RegisterXmm9: REGISTER_ID = 27
X64_RegisterXmm10: REGISTER_ID = 28
X64_RegisterXmm11: REGISTER_ID = 29
X64_RegisterXmm12: REGISTER_ID = 30
X64_RegisterXmm13: REGISTER_ID = 31
X64_RegisterXmm14: REGISTER_ID = 32
X64_RegisterXmm15: REGISTER_ID = 33
X64_RegisterFpMmx0: REGISTER_ID = 34
X64_RegisterFpMmx1: REGISTER_ID = 35
X64_RegisterFpMmx2: REGISTER_ID = 36
X64_RegisterFpMmx3: REGISTER_ID = 37
X64_RegisterFpMmx4: REGISTER_ID = 38
X64_RegisterFpMmx5: REGISTER_ID = 39
X64_RegisterFpMmx6: REGISTER_ID = 40
X64_RegisterFpMmx7: REGISTER_ID = 41
X64_RegisterFpControlStatus: REGISTER_ID = 42
X64_RegisterXmmControlStatus: REGISTER_ID = 43
X64_RegisterCr0: REGISTER_ID = 44
X64_RegisterCr2: REGISTER_ID = 45
X64_RegisterCr3: REGISTER_ID = 46
X64_RegisterCr4: REGISTER_ID = 47
X64_RegisterCr8: REGISTER_ID = 48
X64_RegisterEfer: REGISTER_ID = 49
X64_RegisterDr0: REGISTER_ID = 50
X64_RegisterDr1: REGISTER_ID = 51
X64_RegisterDr2: REGISTER_ID = 52
X64_RegisterDr3: REGISTER_ID = 53
X64_RegisterDr6: REGISTER_ID = 54
X64_RegisterDr7: REGISTER_ID = 55
X64_RegisterEs: REGISTER_ID = 56
X64_RegisterCs: REGISTER_ID = 57
X64_RegisterSs: REGISTER_ID = 58
X64_RegisterDs: REGISTER_ID = 59
X64_RegisterFs: REGISTER_ID = 60
X64_RegisterGs: REGISTER_ID = 61
X64_RegisterLdtr: REGISTER_ID = 62
X64_RegisterTr: REGISTER_ID = 63
X64_RegisterIdtr: REGISTER_ID = 64
X64_RegisterGdtr: REGISTER_ID = 65
X64_RegisterMax: REGISTER_ID = 66
ARM64_RegisterX0: REGISTER_ID = 67
ARM64_RegisterX1: REGISTER_ID = 68
ARM64_RegisterX2: REGISTER_ID = 69
ARM64_RegisterX3: REGISTER_ID = 70
ARM64_RegisterX4: REGISTER_ID = 71
ARM64_RegisterX5: REGISTER_ID = 72
ARM64_RegisterX6: REGISTER_ID = 73
ARM64_RegisterX7: REGISTER_ID = 74
ARM64_RegisterX8: REGISTER_ID = 75
ARM64_RegisterX9: REGISTER_ID = 76
ARM64_RegisterX10: REGISTER_ID = 77
ARM64_RegisterX11: REGISTER_ID = 78
ARM64_RegisterX12: REGISTER_ID = 79
ARM64_RegisterX13: REGISTER_ID = 80
ARM64_RegisterX14: REGISTER_ID = 81
ARM64_RegisterX15: REGISTER_ID = 82
ARM64_RegisterX16: REGISTER_ID = 83
ARM64_RegisterX17: REGISTER_ID = 84
ARM64_RegisterX18: REGISTER_ID = 85
ARM64_RegisterX19: REGISTER_ID = 86
ARM64_RegisterX20: REGISTER_ID = 87
ARM64_RegisterX21: REGISTER_ID = 88
ARM64_RegisterX22: REGISTER_ID = 89
ARM64_RegisterX23: REGISTER_ID = 90
ARM64_RegisterX24: REGISTER_ID = 91
ARM64_RegisterX25: REGISTER_ID = 92
ARM64_RegisterX26: REGISTER_ID = 93
ARM64_RegisterX27: REGISTER_ID = 94
ARM64_RegisterX28: REGISTER_ID = 95
ARM64_RegisterXFp: REGISTER_ID = 96
ARM64_RegisterXLr: REGISTER_ID = 97
ARM64_RegisterPc: REGISTER_ID = 98
ARM64_RegisterSpEl0: REGISTER_ID = 99
ARM64_RegisterSpEl1: REGISTER_ID = 100
ARM64_RegisterCpsr: REGISTER_ID = 101
ARM64_RegisterQ0: REGISTER_ID = 102
ARM64_RegisterQ1: REGISTER_ID = 103
ARM64_RegisterQ2: REGISTER_ID = 104
ARM64_RegisterQ3: REGISTER_ID = 105
ARM64_RegisterQ4: REGISTER_ID = 106
ARM64_RegisterQ5: REGISTER_ID = 107
ARM64_RegisterQ6: REGISTER_ID = 108
ARM64_RegisterQ7: REGISTER_ID = 109
ARM64_RegisterQ8: REGISTER_ID = 110
ARM64_RegisterQ9: REGISTER_ID = 111
ARM64_RegisterQ10: REGISTER_ID = 112
ARM64_RegisterQ11: REGISTER_ID = 113
ARM64_RegisterQ12: REGISTER_ID = 114
ARM64_RegisterQ13: REGISTER_ID = 115
ARM64_RegisterQ14: REGISTER_ID = 116
ARM64_RegisterQ15: REGISTER_ID = 117
ARM64_RegisterQ16: REGISTER_ID = 118
ARM64_RegisterQ17: REGISTER_ID = 119
ARM64_RegisterQ18: REGISTER_ID = 120
ARM64_RegisterQ19: REGISTER_ID = 121
ARM64_RegisterQ20: REGISTER_ID = 122
ARM64_RegisterQ21: REGISTER_ID = 123
ARM64_RegisterQ22: REGISTER_ID = 124
ARM64_RegisterQ23: REGISTER_ID = 125
ARM64_RegisterQ24: REGISTER_ID = 126
ARM64_RegisterQ25: REGISTER_ID = 127
ARM64_RegisterQ26: REGISTER_ID = 128
ARM64_RegisterQ27: REGISTER_ID = 129
ARM64_RegisterQ28: REGISTER_ID = 130
ARM64_RegisterQ29: REGISTER_ID = 131
ARM64_RegisterQ30: REGISTER_ID = 132
ARM64_RegisterQ31: REGISTER_ID = 133
ARM64_RegisterFpStatus: REGISTER_ID = 134
ARM64_RegisterFpControl: REGISTER_ID = 135
ARM64_RegisterEsrEl1: REGISTER_ID = 136
ARM64_RegisterSpsrEl1: REGISTER_ID = 137
ARM64_RegisterFarEl1: REGISTER_ID = 138
ARM64_RegisterParEl1: REGISTER_ID = 139
ARM64_RegisterElrEl1: REGISTER_ID = 140
ARM64_RegisterTtbr0El1: REGISTER_ID = 141
ARM64_RegisterTtbr1El1: REGISTER_ID = 142
ARM64_RegisterVbarEl1: REGISTER_ID = 143
ARM64_RegisterSctlrEl1: REGISTER_ID = 144
ARM64_RegisterActlrEl1: REGISTER_ID = 145
ARM64_RegisterTcrEl1: REGISTER_ID = 146
ARM64_RegisterMairEl1: REGISTER_ID = 147
ARM64_RegisterAmairEl1: REGISTER_ID = 148
ARM64_RegisterTpidrEl0: REGISTER_ID = 149
ARM64_RegisterTpidrroEl0: REGISTER_ID = 150
ARM64_RegisterTpidrEl1: REGISTER_ID = 151
ARM64_RegisterContextIdrEl1: REGISTER_ID = 152
ARM64_RegisterCpacrEl1: REGISTER_ID = 153
ARM64_RegisterCsselrEl1: REGISTER_ID = 154
ARM64_RegisterCntkctlEl1: REGISTER_ID = 155
ARM64_RegisterCntvCvalEl0: REGISTER_ID = 156
ARM64_RegisterCntvCtlEl0: REGISTER_ID = 157
ARM64_RegisterMax: REGISTER_ID = 158
class SOCKADDR_HV(Structure):
    Family: win32more.Networking.WinSock.ADDRESS_FAMILY
    Reserved: UInt16
    VmId: Guid
    ServiceId: Guid
VIRTUAL_PROCESSOR_ARCH = Int32
Arch_Unknown: VIRTUAL_PROCESSOR_ARCH = 0
Arch_x86: VIRTUAL_PROCESSOR_ARCH = 1
Arch_x64: VIRTUAL_PROCESSOR_ARCH = 2
Arch_Armv8: VIRTUAL_PROCESSOR_ARCH = 3
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
            class _Anonymous_e__Union(Union):
                Attributes: UInt16
                Anonymous: _Anonymous_e__Struct
                class _Anonymous_e__Struct(Structure):
                    _bitfield: UInt16
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
            class _Anonymous_e__Union(Union):
                LastFpRip: UInt64
                Anonymous: _Anonymous_e__Struct
                class _Anonymous_e__Struct(Structure):
                    LastFpEip: UInt32
                    LastFpCs: UInt16
        class _XmmControlStatus_e__Struct(Structure):
            Anonymous: _Anonymous_e__Union
            XmmStatusControl: UInt32
            XmmStatusControlMask: UInt32
            class _Anonymous_e__Union(Union):
                LastFpRdp: UInt64
                Anonymous: _Anonymous_e__Struct
                class _Anonymous_e__Struct(Structure):
                    LastFpDp: UInt32
                    LastFpDs: UInt16
VIRTUAL_PROCESSOR_VENDOR = Int32
ProcessorVendor_Unknown: VIRTUAL_PROCESSOR_VENDOR = 0
ProcessorVendor_Amd: VIRTUAL_PROCESSOR_VENDOR = 1
ProcessorVendor_Intel: VIRTUAL_PROCESSOR_VENDOR = 2
ProcessorVendor_Hygon: VIRTUAL_PROCESSOR_VENDOR = 3
ProcessorVendor_Arm: VIRTUAL_PROCESSOR_VENDOR = 4
class VM_GENCOUNTER(Structure):
    GenerationCount: UInt64
    GenerationCountHigh: UInt64
class WHV_ACCESS_GPA_CONTROLS(Union):
    AsUINT64: UInt64
    Anonymous: _Anonymous_e__Struct
    class _Anonymous_e__Struct(Structure):
        CacheType: win32more.System.Hypervisor.WHV_CACHE_TYPE
        Reserved: UInt32
class WHV_ADVISE_GPA_RANGE(Union):
    Populate: win32more.System.Hypervisor.WHV_ADVISE_GPA_RANGE_POPULATE
WHV_ADVISE_GPA_RANGE_CODE = Int32
WHV_ADVISE_GPA_RANGE_CODE_WHvAdviseGpaRangeCodePopulate: WHV_ADVISE_GPA_RANGE_CODE = 0
WHV_ADVISE_GPA_RANGE_CODE_WHvAdviseGpaRangeCodePin: WHV_ADVISE_GPA_RANGE_CODE = 1
WHV_ADVISE_GPA_RANGE_CODE_WHvAdviseGpaRangeCodeUnpin: WHV_ADVISE_GPA_RANGE_CODE = 2
class WHV_ADVISE_GPA_RANGE_POPULATE(Structure):
    Flags: win32more.System.Hypervisor.WHV_ADVISE_GPA_RANGE_POPULATE_FLAGS
    AccessType: win32more.System.Hypervisor.WHV_MEMORY_ACCESS_TYPE
class WHV_ADVISE_GPA_RANGE_POPULATE_FLAGS(Union):
    AsUINT32: UInt32
    Anonymous: _Anonymous_e__Struct
    class _Anonymous_e__Struct(Structure):
        _bitfield: UInt32
WHV_ALLOCATE_VPCI_RESOURCE_FLAGS = UInt32
WHV_ALLOCATE_VPCI_RESOURCE_FLAGS_WHvAllocateVpciResourceFlagNone: WHV_ALLOCATE_VPCI_RESOURCE_FLAGS = 0
WHV_ALLOCATE_VPCI_RESOURCE_FLAGS_WHvAllocateVpciResourceFlagAllowDirectP2P: WHV_ALLOCATE_VPCI_RESOURCE_FLAGS = 1
WHV_CACHE_TYPE = Int32
WHV_CACHE_TYPE_WHvCacheTypeUncached: WHV_CACHE_TYPE = 0
WHV_CACHE_TYPE_WHvCacheTypeWriteCombining: WHV_CACHE_TYPE = 1
WHV_CACHE_TYPE_WHvCacheTypeWriteThrough: WHV_CACHE_TYPE = 4
WHV_CACHE_TYPE_WHvCacheTypeWriteBack: WHV_CACHE_TYPE = 6
class WHV_CAPABILITY(Union):
    HypervisorPresent: win32more.Foundation.BOOL
    Features: win32more.System.Hypervisor.WHV_CAPABILITY_FEATURES
    ExtendedVmExits: win32more.System.Hypervisor.WHV_EXTENDED_VM_EXITS
    ProcessorVendor: win32more.System.Hypervisor.WHV_PROCESSOR_VENDOR
    ProcessorFeatures: win32more.System.Hypervisor.WHV_PROCESSOR_FEATURES
    SyntheticProcessorFeaturesBanks: win32more.System.Hypervisor.WHV_SYNTHETIC_PROCESSOR_FEATURES_BANKS
    ProcessorXsaveFeatures: win32more.System.Hypervisor.WHV_PROCESSOR_XSAVE_FEATURES
    ProcessorClFlushSize: Byte
    ExceptionExitBitmap: UInt64
    X64MsrExitBitmap: win32more.System.Hypervisor.WHV_X64_MSR_EXIT_BITMAP
    ProcessorClockFrequency: UInt64
    InterruptClockFrequency: UInt64
    ProcessorFeaturesBanks: win32more.System.Hypervisor.WHV_PROCESSOR_FEATURES_BANKS
    GpaRangePopulateFlags: win32more.System.Hypervisor.WHV_ADVISE_GPA_RANGE_POPULATE_FLAGS
    ProcessorFrequencyCap: win32more.System.Hypervisor.WHV_CAPABILITY_PROCESSOR_FREQUENCY_CAP
    ProcessorPerfmonFeatures: win32more.System.Hypervisor.WHV_PROCESSOR_PERFMON_FEATURES
    SchedulerFeatures: win32more.System.Hypervisor.WHV_SCHEDULER_FEATURES
WHV_CAPABILITY_CODE = Int32
WHV_CAPABILITY_CODE_WHvCapabilityCodeHypervisorPresent: WHV_CAPABILITY_CODE = 0
WHV_CAPABILITY_CODE_WHvCapabilityCodeFeatures: WHV_CAPABILITY_CODE = 1
WHV_CAPABILITY_CODE_WHvCapabilityCodeExtendedVmExits: WHV_CAPABILITY_CODE = 2
WHV_CAPABILITY_CODE_WHvCapabilityCodeExceptionExitBitmap: WHV_CAPABILITY_CODE = 3
WHV_CAPABILITY_CODE_WHvCapabilityCodeX64MsrExitBitmap: WHV_CAPABILITY_CODE = 4
WHV_CAPABILITY_CODE_WHvCapabilityCodeGpaRangePopulateFlags: WHV_CAPABILITY_CODE = 5
WHV_CAPABILITY_CODE_WHvCapabilityCodeSchedulerFeatures: WHV_CAPABILITY_CODE = 6
WHV_CAPABILITY_CODE_WHvCapabilityCodeProcessorVendor: WHV_CAPABILITY_CODE = 4096
WHV_CAPABILITY_CODE_WHvCapabilityCodeProcessorFeatures: WHV_CAPABILITY_CODE = 4097
WHV_CAPABILITY_CODE_WHvCapabilityCodeProcessorClFlushSize: WHV_CAPABILITY_CODE = 4098
WHV_CAPABILITY_CODE_WHvCapabilityCodeProcessorXsaveFeatures: WHV_CAPABILITY_CODE = 4099
WHV_CAPABILITY_CODE_WHvCapabilityCodeProcessorClockFrequency: WHV_CAPABILITY_CODE = 4100
WHV_CAPABILITY_CODE_WHvCapabilityCodeInterruptClockFrequency: WHV_CAPABILITY_CODE = 4101
WHV_CAPABILITY_CODE_WHvCapabilityCodeProcessorFeaturesBanks: WHV_CAPABILITY_CODE = 4102
WHV_CAPABILITY_CODE_WHvCapabilityCodeProcessorFrequencyCap: WHV_CAPABILITY_CODE = 4103
WHV_CAPABILITY_CODE_WHvCapabilityCodeSyntheticProcessorFeaturesBanks: WHV_CAPABILITY_CODE = 4104
WHV_CAPABILITY_CODE_WHvCapabilityCodeProcessorPerfmonFeatures: WHV_CAPABILITY_CODE = 4105
class WHV_CAPABILITY_FEATURES(Union):
    Anonymous: _Anonymous_e__Struct
    AsUINT64: UInt64
    class _Anonymous_e__Struct(Structure):
        _bitfield: UInt64
class WHV_CAPABILITY_PROCESSOR_FREQUENCY_CAP(Structure):
    _bitfield: UInt32
    HighestFrequencyMhz: UInt32
    NominalFrequencyMhz: UInt32
    LowestFrequencyMhz: UInt32
    FrequencyStepMhz: UInt32
class WHV_CPUID_OUTPUT(Structure):
    Eax: UInt32
    Ebx: UInt32
    Ecx: UInt32
    Edx: UInt32
WHV_CREATE_VPCI_DEVICE_FLAGS = UInt32
WHV_CREATE_VPCI_DEVICE_FLAGS_WHvCreateVpciDeviceFlagNone: WHV_CREATE_VPCI_DEVICE_FLAGS = 0
WHV_CREATE_VPCI_DEVICE_FLAGS_WHvCreateVpciDeviceFlagPhysicallyBacked: WHV_CREATE_VPCI_DEVICE_FLAGS = 1
WHV_CREATE_VPCI_DEVICE_FLAGS_WHvCreateVpciDeviceFlagUseLogicalInterrupts: WHV_CREATE_VPCI_DEVICE_FLAGS = 2
class WHV_DOORBELL_MATCH_DATA(Structure):
    GuestAddress: UInt64
    Value: UInt64
    Length: UInt32
    _bitfield: UInt32
class WHV_EMULATOR_CALLBACKS(Structure):
    Size: UInt32
    Reserved: UInt32
    WHvEmulatorIoPortCallback: win32more.System.Hypervisor.WHV_EMULATOR_IO_PORT_CALLBACK
    WHvEmulatorMemoryCallback: win32more.System.Hypervisor.WHV_EMULATOR_MEMORY_CALLBACK
    WHvEmulatorGetVirtualProcessorRegisters: win32more.System.Hypervisor.WHV_EMULATOR_GET_VIRTUAL_PROCESSOR_REGISTERS_CALLBACK
    WHvEmulatorSetVirtualProcessorRegisters: win32more.System.Hypervisor.WHV_EMULATOR_SET_VIRTUAL_PROCESSOR_REGISTERS_CALLBACK
    WHvEmulatorTranslateGvaPage: win32more.System.Hypervisor.WHV_EMULATOR_TRANSLATE_GVA_PAGE_CALLBACK
@winfunctype_pointer
def WHV_EMULATOR_GET_VIRTUAL_PROCESSOR_REGISTERS_CALLBACK(Context: c_void_p, RegisterNames: POINTER(win32more.System.Hypervisor.WHV_REGISTER_NAME), RegisterCount: UInt32, RegisterValues: POINTER(win32more.System.Hypervisor.WHV_REGISTER_VALUE_head)) -> win32more.Foundation.HRESULT: ...
class WHV_EMULATOR_IO_ACCESS_INFO(Structure):
    Direction: Byte
    Port: UInt16
    AccessSize: UInt16
    Data: UInt32
@winfunctype_pointer
def WHV_EMULATOR_IO_PORT_CALLBACK(Context: c_void_p, IoAccess: POINTER(win32more.System.Hypervisor.WHV_EMULATOR_IO_ACCESS_INFO_head)) -> win32more.Foundation.HRESULT: ...
class WHV_EMULATOR_MEMORY_ACCESS_INFO(Structure):
    GpaAddress: UInt64
    Direction: Byte
    AccessSize: Byte
    Data: Byte * 8
@winfunctype_pointer
def WHV_EMULATOR_MEMORY_CALLBACK(Context: c_void_p, MemoryAccess: POINTER(win32more.System.Hypervisor.WHV_EMULATOR_MEMORY_ACCESS_INFO_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def WHV_EMULATOR_SET_VIRTUAL_PROCESSOR_REGISTERS_CALLBACK(Context: c_void_p, RegisterNames: POINTER(win32more.System.Hypervisor.WHV_REGISTER_NAME), RegisterCount: UInt32, RegisterValues: POINTER(win32more.System.Hypervisor.WHV_REGISTER_VALUE_head)) -> win32more.Foundation.HRESULT: ...
class WHV_EMULATOR_STATUS(Union):
    Anonymous: _Anonymous_e__Struct
    AsUINT32: UInt32
    class _Anonymous_e__Struct(Structure):
        _bitfield: UInt32
@winfunctype_pointer
def WHV_EMULATOR_TRANSLATE_GVA_PAGE_CALLBACK(Context: c_void_p, Gva: UInt64, TranslateFlags: win32more.System.Hypervisor.WHV_TRANSLATE_GVA_FLAGS, TranslationResult: POINTER(win32more.System.Hypervisor.WHV_TRANSLATE_GVA_RESULT_CODE), Gpa: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
WHV_EXCEPTION_TYPE = Int32
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeDivideErrorFault: WHV_EXCEPTION_TYPE = 0
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeDebugTrapOrFault: WHV_EXCEPTION_TYPE = 1
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeBreakpointTrap: WHV_EXCEPTION_TYPE = 3
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeOverflowTrap: WHV_EXCEPTION_TYPE = 4
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeBoundRangeFault: WHV_EXCEPTION_TYPE = 5
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeInvalidOpcodeFault: WHV_EXCEPTION_TYPE = 6
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeDeviceNotAvailableFault: WHV_EXCEPTION_TYPE = 7
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeDoubleFaultAbort: WHV_EXCEPTION_TYPE = 8
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeInvalidTaskStateSegmentFault: WHV_EXCEPTION_TYPE = 10
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeSegmentNotPresentFault: WHV_EXCEPTION_TYPE = 11
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeStackFault: WHV_EXCEPTION_TYPE = 12
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeGeneralProtectionFault: WHV_EXCEPTION_TYPE = 13
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypePageFault: WHV_EXCEPTION_TYPE = 14
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeFloatingPointErrorFault: WHV_EXCEPTION_TYPE = 16
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeAlignmentCheckFault: WHV_EXCEPTION_TYPE = 17
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeMachineCheckAbort: WHV_EXCEPTION_TYPE = 18
WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeSimdFloatingPointFault: WHV_EXCEPTION_TYPE = 19
class WHV_EXTENDED_VM_EXITS(Union):
    Anonymous: _Anonymous_e__Struct
    AsUINT64: UInt64
    class _Anonymous_e__Struct(Structure):
        _bitfield: UInt64
class WHV_HYPERCALL_CONTEXT(Structure):
    Rax: UInt64
    Rbx: UInt64
    Rcx: UInt64
    Rdx: UInt64
    R8: UInt64
    Rsi: UInt64
    Rdi: UInt64
    Reserved0: UInt64
    XmmRegisters: win32more.System.Hypervisor.WHV_UINT128 * 6
    Reserved1: UInt64 * 2
class WHV_INTERNAL_ACTIVITY_REGISTER(Union):
    Anonymous: _Anonymous_e__Struct
    AsUINT64: UInt64
    class _Anonymous_e__Struct(Structure):
        _bitfield: UInt64
class WHV_INTERRUPT_CONTROL(Structure):
    _bitfield: UInt64
    Destination: UInt32
    Vector: UInt32
WHV_INTERRUPT_DESTINATION_MODE = Int32
WHV_INTERRUPT_DESTINATION_MODE_WHvX64InterruptDestinationModePhysical: WHV_INTERRUPT_DESTINATION_MODE = 0
WHV_INTERRUPT_DESTINATION_MODE_WHvX64InterruptDestinationModeLogical: WHV_INTERRUPT_DESTINATION_MODE = 1
WHV_INTERRUPT_TRIGGER_MODE = Int32
WHV_INTERRUPT_TRIGGER_MODE_WHvX64InterruptTriggerModeEdge: WHV_INTERRUPT_TRIGGER_MODE = 0
WHV_INTERRUPT_TRIGGER_MODE_WHvX64InterruptTriggerModeLevel: WHV_INTERRUPT_TRIGGER_MODE = 1
WHV_INTERRUPT_TYPE = Int32
WHV_INTERRUPT_TYPE_WHvX64InterruptTypeFixed: WHV_INTERRUPT_TYPE = 0
WHV_INTERRUPT_TYPE_WHvX64InterruptTypeLowestPriority: WHV_INTERRUPT_TYPE = 1
WHV_INTERRUPT_TYPE_WHvX64InterruptTypeNmi: WHV_INTERRUPT_TYPE = 4
WHV_INTERRUPT_TYPE_WHvX64InterruptTypeInit: WHV_INTERRUPT_TYPE = 5
WHV_INTERRUPT_TYPE_WHvX64InterruptTypeSipi: WHV_INTERRUPT_TYPE = 6
WHV_INTERRUPT_TYPE_WHvX64InterruptTypeLocalInt1: WHV_INTERRUPT_TYPE = 9
WHV_MAP_GPA_RANGE_FLAGS = UInt32
WHV_MAP_GPA_RANGE_FLAGS_WHvMapGpaRangeFlagNone: WHV_MAP_GPA_RANGE_FLAGS = 0
WHV_MAP_GPA_RANGE_FLAGS_WHvMapGpaRangeFlagRead: WHV_MAP_GPA_RANGE_FLAGS = 1
WHV_MAP_GPA_RANGE_FLAGS_WHvMapGpaRangeFlagWrite: WHV_MAP_GPA_RANGE_FLAGS = 2
WHV_MAP_GPA_RANGE_FLAGS_WHvMapGpaRangeFlagExecute: WHV_MAP_GPA_RANGE_FLAGS = 4
WHV_MAP_GPA_RANGE_FLAGS_WHvMapGpaRangeFlagTrackDirtyPages: WHV_MAP_GPA_RANGE_FLAGS = 8
class WHV_MEMORY_ACCESS_CONTEXT(Structure):
    InstructionByteCount: Byte
    Reserved: Byte * 3
    InstructionBytes: Byte * 16
    AccessInfo: win32more.System.Hypervisor.WHV_MEMORY_ACCESS_INFO
    Gpa: UInt64
    Gva: UInt64
class WHV_MEMORY_ACCESS_INFO(Union):
    Anonymous: _Anonymous_e__Struct
    AsUINT32: UInt32
    class _Anonymous_e__Struct(Structure):
        _bitfield: UInt32
WHV_MEMORY_ACCESS_TYPE = Int32
WHV_MEMORY_ACCESS_TYPE_WHvMemoryAccessRead: WHV_MEMORY_ACCESS_TYPE = 0
WHV_MEMORY_ACCESS_TYPE_WHvMemoryAccessWrite: WHV_MEMORY_ACCESS_TYPE = 1
WHV_MEMORY_ACCESS_TYPE_WHvMemoryAccessExecute: WHV_MEMORY_ACCESS_TYPE = 2
class WHV_MEMORY_RANGE_ENTRY(Structure):
    GuestAddress: UInt64
    SizeInBytes: UInt64
WHV_MSR_ACTION = Int32
WHV_MSR_ACTION_WHvMsrActionArchitectureDefault: WHV_MSR_ACTION = 0
WHV_MSR_ACTION_WHvMsrActionIgnoreWriteReadZero: WHV_MSR_ACTION = 1
WHV_MSR_ACTION_WHvMsrActionExit: WHV_MSR_ACTION = 2
class WHV_MSR_ACTION_ENTRY(Structure):
    Index: UInt32
    ReadAction: Byte
    WriteAction: Byte
    Reserved: UInt16
class WHV_NOTIFICATION_PORT_PARAMETERS(Structure):
    NotificationPortType: win32more.System.Hypervisor.WHV_NOTIFICATION_PORT_TYPE
    Reserved: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Doorbell: win32more.System.Hypervisor.WHV_DOORBELL_MATCH_DATA
        Event: _Event_e__Struct
        class _Event_e__Struct(Structure):
            ConnectionId: UInt32
WHV_NOTIFICATION_PORT_PROPERTY_CODE = Int32
WHV_NOTIFICATION_PORT_PROPERTY_CODE_WHvNotificationPortPropertyPreferredTargetVp: WHV_NOTIFICATION_PORT_PROPERTY_CODE = 1
WHV_NOTIFICATION_PORT_PROPERTY_CODE_WHvNotificationPortPropertyPreferredTargetDuration: WHV_NOTIFICATION_PORT_PROPERTY_CODE = 5
WHV_NOTIFICATION_PORT_TYPE = Int32
WHV_NOTIFICATION_PORT_TYPE_WHvNotificationPortTypeEvent: WHV_NOTIFICATION_PORT_TYPE = 2
WHV_NOTIFICATION_PORT_TYPE_WHvNotificationPortTypeDoorbell: WHV_NOTIFICATION_PORT_TYPE = 4
WHV_PARTITION_COUNTER_SET = Int32
WHV_PARTITION_COUNTER_SET_WHvPartitionCounterSetMemory: WHV_PARTITION_COUNTER_SET = 0
WHV_PARTITION_HANDLE = IntPtr
class WHV_PARTITION_MEMORY_COUNTERS(Structure):
    Mapped4KPageCount: UInt64
    Mapped2MPageCount: UInt64
    Mapped1GPageCount: UInt64
class WHV_PARTITION_PROPERTY(Union):
    ExtendedVmExits: win32more.System.Hypervisor.WHV_EXTENDED_VM_EXITS
    ProcessorFeatures: win32more.System.Hypervisor.WHV_PROCESSOR_FEATURES
    SyntheticProcessorFeaturesBanks: win32more.System.Hypervisor.WHV_SYNTHETIC_PROCESSOR_FEATURES_BANKS
    ProcessorXsaveFeatures: win32more.System.Hypervisor.WHV_PROCESSOR_XSAVE_FEATURES
    ProcessorClFlushSize: Byte
    ProcessorCount: UInt32
    CpuidExitList: UInt32 * 1
    CpuidResultList: win32more.System.Hypervisor.WHV_X64_CPUID_RESULT * 1
    CpuidResultList2: win32more.System.Hypervisor.WHV_X64_CPUID_RESULT2 * 1
    MsrActionList: win32more.System.Hypervisor.WHV_MSR_ACTION_ENTRY * 1
    UnimplementedMsrAction: win32more.System.Hypervisor.WHV_MSR_ACTION
    ExceptionExitBitmap: UInt64
    LocalApicEmulationMode: win32more.System.Hypervisor.WHV_X64_LOCAL_APIC_EMULATION_MODE
    SeparateSecurityDomain: win32more.Foundation.BOOL
    NestedVirtualization: win32more.Foundation.BOOL
    X64MsrExitBitmap: win32more.System.Hypervisor.WHV_X64_MSR_EXIT_BITMAP
    ProcessorClockFrequency: UInt64
    InterruptClockFrequency: UInt64
    ApicRemoteRead: win32more.Foundation.BOOL
    ProcessorFeaturesBanks: win32more.System.Hypervisor.WHV_PROCESSOR_FEATURES_BANKS
    ReferenceTime: UInt64
    PrimaryNumaNode: UInt16
    CpuReserve: UInt32
    CpuCap: UInt32
    CpuWeight: UInt32
    CpuGroupId: UInt64
    ProcessorFrequencyCap: UInt32
    AllowDeviceAssignment: win32more.Foundation.BOOL
    ProcessorPerfmonFeatures: win32more.System.Hypervisor.WHV_PROCESSOR_PERFMON_FEATURES
    DisableSmt: win32more.Foundation.BOOL
WHV_PARTITION_PROPERTY_CODE = Int32
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeExtendedVmExits: WHV_PARTITION_PROPERTY_CODE = 1
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeExceptionExitBitmap: WHV_PARTITION_PROPERTY_CODE = 2
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeSeparateSecurityDomain: WHV_PARTITION_PROPERTY_CODE = 3
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeNestedVirtualization: WHV_PARTITION_PROPERTY_CODE = 4
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeX64MsrExitBitmap: WHV_PARTITION_PROPERTY_CODE = 5
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodePrimaryNumaNode: WHV_PARTITION_PROPERTY_CODE = 6
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeCpuReserve: WHV_PARTITION_PROPERTY_CODE = 7
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeCpuCap: WHV_PARTITION_PROPERTY_CODE = 8
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeCpuWeight: WHV_PARTITION_PROPERTY_CODE = 9
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeCpuGroupId: WHV_PARTITION_PROPERTY_CODE = 10
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeProcessorFrequencyCap: WHV_PARTITION_PROPERTY_CODE = 11
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeAllowDeviceAssignment: WHV_PARTITION_PROPERTY_CODE = 12
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeDisableSmt: WHV_PARTITION_PROPERTY_CODE = 13
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeProcessorFeatures: WHV_PARTITION_PROPERTY_CODE = 4097
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeProcessorClFlushSize: WHV_PARTITION_PROPERTY_CODE = 4098
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeCpuidExitList: WHV_PARTITION_PROPERTY_CODE = 4099
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeCpuidResultList: WHV_PARTITION_PROPERTY_CODE = 4100
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeLocalApicEmulationMode: WHV_PARTITION_PROPERTY_CODE = 4101
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeProcessorXsaveFeatures: WHV_PARTITION_PROPERTY_CODE = 4102
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeProcessorClockFrequency: WHV_PARTITION_PROPERTY_CODE = 4103
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeInterruptClockFrequency: WHV_PARTITION_PROPERTY_CODE = 4104
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeApicRemoteReadSupport: WHV_PARTITION_PROPERTY_CODE = 4105
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeProcessorFeaturesBanks: WHV_PARTITION_PROPERTY_CODE = 4106
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeReferenceTime: WHV_PARTITION_PROPERTY_CODE = 4107
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeSyntheticProcessorFeaturesBanks: WHV_PARTITION_PROPERTY_CODE = 4108
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeCpuidResultList2: WHV_PARTITION_PROPERTY_CODE = 4109
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeProcessorPerfmonFeatures: WHV_PARTITION_PROPERTY_CODE = 4110
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeMsrActionList: WHV_PARTITION_PROPERTY_CODE = 4111
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeUnimplementedMsrAction: WHV_PARTITION_PROPERTY_CODE = 4112
WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeProcessorCount: WHV_PARTITION_PROPERTY_CODE = 8191
class WHV_PROCESSOR_APIC_COUNTERS(Structure):
    MmioAccessCount: UInt64
    EoiAccessCount: UInt64
    TprAccessCount: UInt64
    SentIpiCount: UInt64
    SelfIpiCount: UInt64
WHV_PROCESSOR_COUNTER_SET = Int32
WHV_PROCESSOR_COUNTER_SET_WHvProcessorCounterSetRuntime: WHV_PROCESSOR_COUNTER_SET = 0
WHV_PROCESSOR_COUNTER_SET_WHvProcessorCounterSetIntercepts: WHV_PROCESSOR_COUNTER_SET = 1
WHV_PROCESSOR_COUNTER_SET_WHvProcessorCounterSetEvents: WHV_PROCESSOR_COUNTER_SET = 2
WHV_PROCESSOR_COUNTER_SET_WHvProcessorCounterSetApic: WHV_PROCESSOR_COUNTER_SET = 3
WHV_PROCESSOR_COUNTER_SET_WHvProcessorCounterSetSyntheticFeatures: WHV_PROCESSOR_COUNTER_SET = 4
class WHV_PROCESSOR_EVENT_COUNTERS(Structure):
    PageFaultCount: UInt64
    ExceptionCount: UInt64
    InterruptCount: UInt64
class WHV_PROCESSOR_FEATURES(Union):
    Anonymous: _Anonymous_e__Struct
    AsUINT64: UInt64
    class _Anonymous_e__Struct(Structure):
        _bitfield: UInt64
class WHV_PROCESSOR_FEATURES_BANKS(Structure):
    BanksCount: UInt32
    Reserved0: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        AsUINT64: UInt64 * 2
        class _Anonymous_e__Struct(Structure):
            Bank0: win32more.System.Hypervisor.WHV_PROCESSOR_FEATURES
            Bank1: win32more.System.Hypervisor.WHV_PROCESSOR_FEATURES1
class WHV_PROCESSOR_FEATURES1(Union):
    Anonymous: _Anonymous_e__Struct
    AsUINT64: UInt64
    class _Anonymous_e__Struct(Structure):
        _bitfield: UInt64
class WHV_PROCESSOR_INTERCEPT_COUNTER(Structure):
    Count: UInt64
    Time100ns: UInt64
class WHV_PROCESSOR_INTERCEPT_COUNTERS(Structure):
    PageInvalidations: win32more.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER
    ControlRegisterAccesses: win32more.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER
    IoInstructions: win32more.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER
    HaltInstructions: win32more.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER
    CpuidInstructions: win32more.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER
    MsrAccesses: win32more.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER
    OtherIntercepts: win32more.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER
    PendingInterrupts: win32more.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER
    EmulatedInstructions: win32more.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER
    DebugRegisterAccesses: win32more.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER
    PageFaultIntercepts: win32more.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER
    NestedPageFaultIntercepts: win32more.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER
    Hypercalls: win32more.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER
    RdpmcInstructions: win32more.System.Hypervisor.WHV_PROCESSOR_INTERCEPT_COUNTER
class WHV_PROCESSOR_PERFMON_FEATURES(Union):
    Anonymous: _Anonymous_e__Struct
    AsUINT64: UInt64
    class _Anonymous_e__Struct(Structure):
        _bitfield: UInt64
class WHV_PROCESSOR_RUNTIME_COUNTERS(Structure):
    TotalRuntime100ns: UInt64
    HypervisorRuntime100ns: UInt64
class WHV_PROCESSOR_SYNTHETIC_FEATURES_COUNTERS(Structure):
    SyntheticInterruptsCount: UInt64
    LongSpinWaitHypercallsCount: UInt64
    OtherHypercallsCount: UInt64
    SyntheticInterruptHypercallsCount: UInt64
    VirtualInterruptHypercallsCount: UInt64
    VirtualMmuHypercallsCount: UInt64
WHV_PROCESSOR_VENDOR = Int32
WHV_PROCESSOR_VENDOR_WHvProcessorVendorAmd: WHV_PROCESSOR_VENDOR = 0
WHV_PROCESSOR_VENDOR_WHvProcessorVendorIntel: WHV_PROCESSOR_VENDOR = 1
WHV_PROCESSOR_VENDOR_WHvProcessorVendorHygon: WHV_PROCESSOR_VENDOR = 2
class WHV_PROCESSOR_XSAVE_FEATURES(Union):
    Anonymous: _Anonymous_e__Struct
    AsUINT64: UInt64
    class _Anonymous_e__Struct(Structure):
        _bitfield: UInt64
WHV_REGISTER_NAME = Int32
WHV_REGISTER_NAME_WHvX64RegisterRax: WHV_REGISTER_NAME = 0
WHV_REGISTER_NAME_WHvX64RegisterRcx: WHV_REGISTER_NAME = 1
WHV_REGISTER_NAME_WHvX64RegisterRdx: WHV_REGISTER_NAME = 2
WHV_REGISTER_NAME_WHvX64RegisterRbx: WHV_REGISTER_NAME = 3
WHV_REGISTER_NAME_WHvX64RegisterRsp: WHV_REGISTER_NAME = 4
WHV_REGISTER_NAME_WHvX64RegisterRbp: WHV_REGISTER_NAME = 5
WHV_REGISTER_NAME_WHvX64RegisterRsi: WHV_REGISTER_NAME = 6
WHV_REGISTER_NAME_WHvX64RegisterRdi: WHV_REGISTER_NAME = 7
WHV_REGISTER_NAME_WHvX64RegisterR8: WHV_REGISTER_NAME = 8
WHV_REGISTER_NAME_WHvX64RegisterR9: WHV_REGISTER_NAME = 9
WHV_REGISTER_NAME_WHvX64RegisterR10: WHV_REGISTER_NAME = 10
WHV_REGISTER_NAME_WHvX64RegisterR11: WHV_REGISTER_NAME = 11
WHV_REGISTER_NAME_WHvX64RegisterR12: WHV_REGISTER_NAME = 12
WHV_REGISTER_NAME_WHvX64RegisterR13: WHV_REGISTER_NAME = 13
WHV_REGISTER_NAME_WHvX64RegisterR14: WHV_REGISTER_NAME = 14
WHV_REGISTER_NAME_WHvX64RegisterR15: WHV_REGISTER_NAME = 15
WHV_REGISTER_NAME_WHvX64RegisterRip: WHV_REGISTER_NAME = 16
WHV_REGISTER_NAME_WHvX64RegisterRflags: WHV_REGISTER_NAME = 17
WHV_REGISTER_NAME_WHvX64RegisterEs: WHV_REGISTER_NAME = 18
WHV_REGISTER_NAME_WHvX64RegisterCs: WHV_REGISTER_NAME = 19
WHV_REGISTER_NAME_WHvX64RegisterSs: WHV_REGISTER_NAME = 20
WHV_REGISTER_NAME_WHvX64RegisterDs: WHV_REGISTER_NAME = 21
WHV_REGISTER_NAME_WHvX64RegisterFs: WHV_REGISTER_NAME = 22
WHV_REGISTER_NAME_WHvX64RegisterGs: WHV_REGISTER_NAME = 23
WHV_REGISTER_NAME_WHvX64RegisterLdtr: WHV_REGISTER_NAME = 24
WHV_REGISTER_NAME_WHvX64RegisterTr: WHV_REGISTER_NAME = 25
WHV_REGISTER_NAME_WHvX64RegisterIdtr: WHV_REGISTER_NAME = 26
WHV_REGISTER_NAME_WHvX64RegisterGdtr: WHV_REGISTER_NAME = 27
WHV_REGISTER_NAME_WHvX64RegisterCr0: WHV_REGISTER_NAME = 28
WHV_REGISTER_NAME_WHvX64RegisterCr2: WHV_REGISTER_NAME = 29
WHV_REGISTER_NAME_WHvX64RegisterCr3: WHV_REGISTER_NAME = 30
WHV_REGISTER_NAME_WHvX64RegisterCr4: WHV_REGISTER_NAME = 31
WHV_REGISTER_NAME_WHvX64RegisterCr8: WHV_REGISTER_NAME = 32
WHV_REGISTER_NAME_WHvX64RegisterDr0: WHV_REGISTER_NAME = 33
WHV_REGISTER_NAME_WHvX64RegisterDr1: WHV_REGISTER_NAME = 34
WHV_REGISTER_NAME_WHvX64RegisterDr2: WHV_REGISTER_NAME = 35
WHV_REGISTER_NAME_WHvX64RegisterDr3: WHV_REGISTER_NAME = 36
WHV_REGISTER_NAME_WHvX64RegisterDr6: WHV_REGISTER_NAME = 37
WHV_REGISTER_NAME_WHvX64RegisterDr7: WHV_REGISTER_NAME = 38
WHV_REGISTER_NAME_WHvX64RegisterXCr0: WHV_REGISTER_NAME = 39
WHV_REGISTER_NAME_WHvX64RegisterVirtualCr0: WHV_REGISTER_NAME = 40
WHV_REGISTER_NAME_WHvX64RegisterVirtualCr3: WHV_REGISTER_NAME = 41
WHV_REGISTER_NAME_WHvX64RegisterVirtualCr4: WHV_REGISTER_NAME = 42
WHV_REGISTER_NAME_WHvX64RegisterVirtualCr8: WHV_REGISTER_NAME = 43
WHV_REGISTER_NAME_WHvX64RegisterXmm0: WHV_REGISTER_NAME = 4096
WHV_REGISTER_NAME_WHvX64RegisterXmm1: WHV_REGISTER_NAME = 4097
WHV_REGISTER_NAME_WHvX64RegisterXmm2: WHV_REGISTER_NAME = 4098
WHV_REGISTER_NAME_WHvX64RegisterXmm3: WHV_REGISTER_NAME = 4099
WHV_REGISTER_NAME_WHvX64RegisterXmm4: WHV_REGISTER_NAME = 4100
WHV_REGISTER_NAME_WHvX64RegisterXmm5: WHV_REGISTER_NAME = 4101
WHV_REGISTER_NAME_WHvX64RegisterXmm6: WHV_REGISTER_NAME = 4102
WHV_REGISTER_NAME_WHvX64RegisterXmm7: WHV_REGISTER_NAME = 4103
WHV_REGISTER_NAME_WHvX64RegisterXmm8: WHV_REGISTER_NAME = 4104
WHV_REGISTER_NAME_WHvX64RegisterXmm9: WHV_REGISTER_NAME = 4105
WHV_REGISTER_NAME_WHvX64RegisterXmm10: WHV_REGISTER_NAME = 4106
WHV_REGISTER_NAME_WHvX64RegisterXmm11: WHV_REGISTER_NAME = 4107
WHV_REGISTER_NAME_WHvX64RegisterXmm12: WHV_REGISTER_NAME = 4108
WHV_REGISTER_NAME_WHvX64RegisterXmm13: WHV_REGISTER_NAME = 4109
WHV_REGISTER_NAME_WHvX64RegisterXmm14: WHV_REGISTER_NAME = 4110
WHV_REGISTER_NAME_WHvX64RegisterXmm15: WHV_REGISTER_NAME = 4111
WHV_REGISTER_NAME_WHvX64RegisterFpMmx0: WHV_REGISTER_NAME = 4112
WHV_REGISTER_NAME_WHvX64RegisterFpMmx1: WHV_REGISTER_NAME = 4113
WHV_REGISTER_NAME_WHvX64RegisterFpMmx2: WHV_REGISTER_NAME = 4114
WHV_REGISTER_NAME_WHvX64RegisterFpMmx3: WHV_REGISTER_NAME = 4115
WHV_REGISTER_NAME_WHvX64RegisterFpMmx4: WHV_REGISTER_NAME = 4116
WHV_REGISTER_NAME_WHvX64RegisterFpMmx5: WHV_REGISTER_NAME = 4117
WHV_REGISTER_NAME_WHvX64RegisterFpMmx6: WHV_REGISTER_NAME = 4118
WHV_REGISTER_NAME_WHvX64RegisterFpMmx7: WHV_REGISTER_NAME = 4119
WHV_REGISTER_NAME_WHvX64RegisterFpControlStatus: WHV_REGISTER_NAME = 4120
WHV_REGISTER_NAME_WHvX64RegisterXmmControlStatus: WHV_REGISTER_NAME = 4121
WHV_REGISTER_NAME_WHvX64RegisterTsc: WHV_REGISTER_NAME = 8192
WHV_REGISTER_NAME_WHvX64RegisterEfer: WHV_REGISTER_NAME = 8193
WHV_REGISTER_NAME_WHvX64RegisterKernelGsBase: WHV_REGISTER_NAME = 8194
WHV_REGISTER_NAME_WHvX64RegisterApicBase: WHV_REGISTER_NAME = 8195
WHV_REGISTER_NAME_WHvX64RegisterPat: WHV_REGISTER_NAME = 8196
WHV_REGISTER_NAME_WHvX64RegisterSysenterCs: WHV_REGISTER_NAME = 8197
WHV_REGISTER_NAME_WHvX64RegisterSysenterEip: WHV_REGISTER_NAME = 8198
WHV_REGISTER_NAME_WHvX64RegisterSysenterEsp: WHV_REGISTER_NAME = 8199
WHV_REGISTER_NAME_WHvX64RegisterStar: WHV_REGISTER_NAME = 8200
WHV_REGISTER_NAME_WHvX64RegisterLstar: WHV_REGISTER_NAME = 8201
WHV_REGISTER_NAME_WHvX64RegisterCstar: WHV_REGISTER_NAME = 8202
WHV_REGISTER_NAME_WHvX64RegisterSfmask: WHV_REGISTER_NAME = 8203
WHV_REGISTER_NAME_WHvX64RegisterInitialApicId: WHV_REGISTER_NAME = 8204
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrCap: WHV_REGISTER_NAME = 8205
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrDefType: WHV_REGISTER_NAME = 8206
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBase0: WHV_REGISTER_NAME = 8208
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBase1: WHV_REGISTER_NAME = 8209
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBase2: WHV_REGISTER_NAME = 8210
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBase3: WHV_REGISTER_NAME = 8211
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBase4: WHV_REGISTER_NAME = 8212
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBase5: WHV_REGISTER_NAME = 8213
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBase6: WHV_REGISTER_NAME = 8214
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBase7: WHV_REGISTER_NAME = 8215
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBase8: WHV_REGISTER_NAME = 8216
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBase9: WHV_REGISTER_NAME = 8217
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBaseA: WHV_REGISTER_NAME = 8218
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBaseB: WHV_REGISTER_NAME = 8219
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBaseC: WHV_REGISTER_NAME = 8220
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBaseD: WHV_REGISTER_NAME = 8221
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBaseE: WHV_REGISTER_NAME = 8222
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysBaseF: WHV_REGISTER_NAME = 8223
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMask0: WHV_REGISTER_NAME = 8256
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMask1: WHV_REGISTER_NAME = 8257
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMask2: WHV_REGISTER_NAME = 8258
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMask3: WHV_REGISTER_NAME = 8259
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMask4: WHV_REGISTER_NAME = 8260
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMask5: WHV_REGISTER_NAME = 8261
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMask6: WHV_REGISTER_NAME = 8262
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMask7: WHV_REGISTER_NAME = 8263
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMask8: WHV_REGISTER_NAME = 8264
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMask9: WHV_REGISTER_NAME = 8265
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMaskA: WHV_REGISTER_NAME = 8266
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMaskB: WHV_REGISTER_NAME = 8267
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMaskC: WHV_REGISTER_NAME = 8268
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMaskD: WHV_REGISTER_NAME = 8269
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMaskE: WHV_REGISTER_NAME = 8270
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrPhysMaskF: WHV_REGISTER_NAME = 8271
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrFix64k00000: WHV_REGISTER_NAME = 8304
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrFix16k80000: WHV_REGISTER_NAME = 8305
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrFix16kA0000: WHV_REGISTER_NAME = 8306
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrFix4kC0000: WHV_REGISTER_NAME = 8307
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrFix4kC8000: WHV_REGISTER_NAME = 8308
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrFix4kD0000: WHV_REGISTER_NAME = 8309
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrFix4kD8000: WHV_REGISTER_NAME = 8310
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrFix4kE0000: WHV_REGISTER_NAME = 8311
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrFix4kE8000: WHV_REGISTER_NAME = 8312
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrFix4kF0000: WHV_REGISTER_NAME = 8313
WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrFix4kF8000: WHV_REGISTER_NAME = 8314
WHV_REGISTER_NAME_WHvX64RegisterTscAux: WHV_REGISTER_NAME = 8315
WHV_REGISTER_NAME_WHvX64RegisterBndcfgs: WHV_REGISTER_NAME = 8316
WHV_REGISTER_NAME_WHvX64RegisterMCount: WHV_REGISTER_NAME = 8318
WHV_REGISTER_NAME_WHvX64RegisterACount: WHV_REGISTER_NAME = 8319
WHV_REGISTER_NAME_WHvX64RegisterSpecCtrl: WHV_REGISTER_NAME = 8324
WHV_REGISTER_NAME_WHvX64RegisterPredCmd: WHV_REGISTER_NAME = 8325
WHV_REGISTER_NAME_WHvX64RegisterTscVirtualOffset: WHV_REGISTER_NAME = 8327
WHV_REGISTER_NAME_WHvX64RegisterTsxCtrl: WHV_REGISTER_NAME = 8328
WHV_REGISTER_NAME_WHvX64RegisterXss: WHV_REGISTER_NAME = 8331
WHV_REGISTER_NAME_WHvX64RegisterUCet: WHV_REGISTER_NAME = 8332
WHV_REGISTER_NAME_WHvX64RegisterSCet: WHV_REGISTER_NAME = 8333
WHV_REGISTER_NAME_WHvX64RegisterSsp: WHV_REGISTER_NAME = 8334
WHV_REGISTER_NAME_WHvX64RegisterPl0Ssp: WHV_REGISTER_NAME = 8335
WHV_REGISTER_NAME_WHvX64RegisterPl1Ssp: WHV_REGISTER_NAME = 8336
WHV_REGISTER_NAME_WHvX64RegisterPl2Ssp: WHV_REGISTER_NAME = 8337
WHV_REGISTER_NAME_WHvX64RegisterPl3Ssp: WHV_REGISTER_NAME = 8338
WHV_REGISTER_NAME_WHvX64RegisterInterruptSspTableAddr: WHV_REGISTER_NAME = 8339
WHV_REGISTER_NAME_WHvX64RegisterTscDeadline: WHV_REGISTER_NAME = 8341
WHV_REGISTER_NAME_WHvX64RegisterTscAdjust: WHV_REGISTER_NAME = 8342
WHV_REGISTER_NAME_WHvX64RegisterUmwaitControl: WHV_REGISTER_NAME = 8344
WHV_REGISTER_NAME_WHvX64RegisterXfd: WHV_REGISTER_NAME = 8345
WHV_REGISTER_NAME_WHvX64RegisterXfdErr: WHV_REGISTER_NAME = 8346
WHV_REGISTER_NAME_WHvX64RegisterApicId: WHV_REGISTER_NAME = 12290
WHV_REGISTER_NAME_WHvX64RegisterApicVersion: WHV_REGISTER_NAME = 12291
WHV_REGISTER_NAME_WHvX64RegisterApicTpr: WHV_REGISTER_NAME = 12296
WHV_REGISTER_NAME_WHvX64RegisterApicPpr: WHV_REGISTER_NAME = 12298
WHV_REGISTER_NAME_WHvX64RegisterApicEoi: WHV_REGISTER_NAME = 12299
WHV_REGISTER_NAME_WHvX64RegisterApicLdr: WHV_REGISTER_NAME = 12301
WHV_REGISTER_NAME_WHvX64RegisterApicSpurious: WHV_REGISTER_NAME = 12303
WHV_REGISTER_NAME_WHvX64RegisterApicIsr0: WHV_REGISTER_NAME = 12304
WHV_REGISTER_NAME_WHvX64RegisterApicIsr1: WHV_REGISTER_NAME = 12305
WHV_REGISTER_NAME_WHvX64RegisterApicIsr2: WHV_REGISTER_NAME = 12306
WHV_REGISTER_NAME_WHvX64RegisterApicIsr3: WHV_REGISTER_NAME = 12307
WHV_REGISTER_NAME_WHvX64RegisterApicIsr4: WHV_REGISTER_NAME = 12308
WHV_REGISTER_NAME_WHvX64RegisterApicIsr5: WHV_REGISTER_NAME = 12309
WHV_REGISTER_NAME_WHvX64RegisterApicIsr6: WHV_REGISTER_NAME = 12310
WHV_REGISTER_NAME_WHvX64RegisterApicIsr7: WHV_REGISTER_NAME = 12311
WHV_REGISTER_NAME_WHvX64RegisterApicTmr0: WHV_REGISTER_NAME = 12312
WHV_REGISTER_NAME_WHvX64RegisterApicTmr1: WHV_REGISTER_NAME = 12313
WHV_REGISTER_NAME_WHvX64RegisterApicTmr2: WHV_REGISTER_NAME = 12314
WHV_REGISTER_NAME_WHvX64RegisterApicTmr3: WHV_REGISTER_NAME = 12315
WHV_REGISTER_NAME_WHvX64RegisterApicTmr4: WHV_REGISTER_NAME = 12316
WHV_REGISTER_NAME_WHvX64RegisterApicTmr5: WHV_REGISTER_NAME = 12317
WHV_REGISTER_NAME_WHvX64RegisterApicTmr6: WHV_REGISTER_NAME = 12318
WHV_REGISTER_NAME_WHvX64RegisterApicTmr7: WHV_REGISTER_NAME = 12319
WHV_REGISTER_NAME_WHvX64RegisterApicIrr0: WHV_REGISTER_NAME = 12320
WHV_REGISTER_NAME_WHvX64RegisterApicIrr1: WHV_REGISTER_NAME = 12321
WHV_REGISTER_NAME_WHvX64RegisterApicIrr2: WHV_REGISTER_NAME = 12322
WHV_REGISTER_NAME_WHvX64RegisterApicIrr3: WHV_REGISTER_NAME = 12323
WHV_REGISTER_NAME_WHvX64RegisterApicIrr4: WHV_REGISTER_NAME = 12324
WHV_REGISTER_NAME_WHvX64RegisterApicIrr5: WHV_REGISTER_NAME = 12325
WHV_REGISTER_NAME_WHvX64RegisterApicIrr6: WHV_REGISTER_NAME = 12326
WHV_REGISTER_NAME_WHvX64RegisterApicIrr7: WHV_REGISTER_NAME = 12327
WHV_REGISTER_NAME_WHvX64RegisterApicEse: WHV_REGISTER_NAME = 12328
WHV_REGISTER_NAME_WHvX64RegisterApicIcr: WHV_REGISTER_NAME = 12336
WHV_REGISTER_NAME_WHvX64RegisterApicLvtTimer: WHV_REGISTER_NAME = 12338
WHV_REGISTER_NAME_WHvX64RegisterApicLvtThermal: WHV_REGISTER_NAME = 12339
WHV_REGISTER_NAME_WHvX64RegisterApicLvtPerfmon: WHV_REGISTER_NAME = 12340
WHV_REGISTER_NAME_WHvX64RegisterApicLvtLint0: WHV_REGISTER_NAME = 12341
WHV_REGISTER_NAME_WHvX64RegisterApicLvtLint1: WHV_REGISTER_NAME = 12342
WHV_REGISTER_NAME_WHvX64RegisterApicLvtError: WHV_REGISTER_NAME = 12343
WHV_REGISTER_NAME_WHvX64RegisterApicInitCount: WHV_REGISTER_NAME = 12344
WHV_REGISTER_NAME_WHvX64RegisterApicCurrentCount: WHV_REGISTER_NAME = 12345
WHV_REGISTER_NAME_WHvX64RegisterApicDivide: WHV_REGISTER_NAME = 12350
WHV_REGISTER_NAME_WHvX64RegisterApicSelfIpi: WHV_REGISTER_NAME = 12351
WHV_REGISTER_NAME_WHvRegisterSint0: WHV_REGISTER_NAME = 16384
WHV_REGISTER_NAME_WHvRegisterSint1: WHV_REGISTER_NAME = 16385
WHV_REGISTER_NAME_WHvRegisterSint2: WHV_REGISTER_NAME = 16386
WHV_REGISTER_NAME_WHvRegisterSint3: WHV_REGISTER_NAME = 16387
WHV_REGISTER_NAME_WHvRegisterSint4: WHV_REGISTER_NAME = 16388
WHV_REGISTER_NAME_WHvRegisterSint5: WHV_REGISTER_NAME = 16389
WHV_REGISTER_NAME_WHvRegisterSint6: WHV_REGISTER_NAME = 16390
WHV_REGISTER_NAME_WHvRegisterSint7: WHV_REGISTER_NAME = 16391
WHV_REGISTER_NAME_WHvRegisterSint8: WHV_REGISTER_NAME = 16392
WHV_REGISTER_NAME_WHvRegisterSint9: WHV_REGISTER_NAME = 16393
WHV_REGISTER_NAME_WHvRegisterSint10: WHV_REGISTER_NAME = 16394
WHV_REGISTER_NAME_WHvRegisterSint11: WHV_REGISTER_NAME = 16395
WHV_REGISTER_NAME_WHvRegisterSint12: WHV_REGISTER_NAME = 16396
WHV_REGISTER_NAME_WHvRegisterSint13: WHV_REGISTER_NAME = 16397
WHV_REGISTER_NAME_WHvRegisterSint14: WHV_REGISTER_NAME = 16398
WHV_REGISTER_NAME_WHvRegisterSint15: WHV_REGISTER_NAME = 16399
WHV_REGISTER_NAME_WHvRegisterScontrol: WHV_REGISTER_NAME = 16400
WHV_REGISTER_NAME_WHvRegisterSversion: WHV_REGISTER_NAME = 16401
WHV_REGISTER_NAME_WHvRegisterSiefp: WHV_REGISTER_NAME = 16402
WHV_REGISTER_NAME_WHvRegisterSimp: WHV_REGISTER_NAME = 16403
WHV_REGISTER_NAME_WHvRegisterEom: WHV_REGISTER_NAME = 16404
WHV_REGISTER_NAME_WHvRegisterVpRuntime: WHV_REGISTER_NAME = 20480
WHV_REGISTER_NAME_WHvX64RegisterHypercall: WHV_REGISTER_NAME = 20481
WHV_REGISTER_NAME_WHvRegisterGuestOsId: WHV_REGISTER_NAME = 20482
WHV_REGISTER_NAME_WHvRegisterVpAssistPage: WHV_REGISTER_NAME = 20499
WHV_REGISTER_NAME_WHvRegisterReferenceTsc: WHV_REGISTER_NAME = 20503
WHV_REGISTER_NAME_WHvRegisterReferenceTscSequence: WHV_REGISTER_NAME = 20506
WHV_REGISTER_NAME_WHvRegisterPendingInterruption: WHV_REGISTER_NAME = -2147483648
WHV_REGISTER_NAME_WHvRegisterInterruptState: WHV_REGISTER_NAME = -2147483647
WHV_REGISTER_NAME_WHvRegisterPendingEvent: WHV_REGISTER_NAME = -2147483646
WHV_REGISTER_NAME_WHvX64RegisterDeliverabilityNotifications: WHV_REGISTER_NAME = -2147483644
WHV_REGISTER_NAME_WHvRegisterInternalActivityState: WHV_REGISTER_NAME = -2147483643
WHV_REGISTER_NAME_WHvX64RegisterPendingDebugException: WHV_REGISTER_NAME = -2147483642
class WHV_REGISTER_VALUE(Union):
    Reg128: win32more.System.Hypervisor.WHV_UINT128
    Reg64: UInt64
    Reg32: UInt32
    Reg16: UInt16
    Reg8: Byte
    Fp: win32more.System.Hypervisor.WHV_X64_FP_REGISTER
    FpControlStatus: win32more.System.Hypervisor.WHV_X64_FP_CONTROL_STATUS_REGISTER
    XmmControlStatus: win32more.System.Hypervisor.WHV_X64_XMM_CONTROL_STATUS_REGISTER
    Segment: win32more.System.Hypervisor.WHV_X64_SEGMENT_REGISTER
    Table: win32more.System.Hypervisor.WHV_X64_TABLE_REGISTER
    InterruptState: win32more.System.Hypervisor.WHV_X64_INTERRUPT_STATE_REGISTER
    PendingInterruption: win32more.System.Hypervisor.WHV_X64_PENDING_INTERRUPTION_REGISTER
    DeliverabilityNotifications: win32more.System.Hypervisor.WHV_X64_DELIVERABILITY_NOTIFICATIONS_REGISTER
    ExceptionEvent: win32more.System.Hypervisor.WHV_X64_PENDING_EXCEPTION_EVENT
    ExtIntEvent: win32more.System.Hypervisor.WHV_X64_PENDING_EXT_INT_EVENT
    InternalActivity: win32more.System.Hypervisor.WHV_INTERNAL_ACTIVITY_REGISTER
    PendingDebugException: win32more.System.Hypervisor.WHV_X64_PENDING_DEBUG_EXCEPTION
WHV_RUN_VP_CANCEL_REASON = Int32
WHV_RUN_VP_CANCEL_REASON_WHvRunVpCancelReasonUser: WHV_RUN_VP_CANCEL_REASON = 0
class WHV_RUN_VP_CANCELED_CONTEXT(Structure):
    CancelReason: win32more.System.Hypervisor.WHV_RUN_VP_CANCEL_REASON
class WHV_RUN_VP_EXIT_CONTEXT(Structure):
    ExitReason: win32more.System.Hypervisor.WHV_RUN_VP_EXIT_REASON
    Reserved: UInt32
    VpContext: win32more.System.Hypervisor.WHV_VP_EXIT_CONTEXT
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        MemoryAccess: win32more.System.Hypervisor.WHV_MEMORY_ACCESS_CONTEXT
        IoPortAccess: win32more.System.Hypervisor.WHV_X64_IO_PORT_ACCESS_CONTEXT
        MsrAccess: win32more.System.Hypervisor.WHV_X64_MSR_ACCESS_CONTEXT
        CpuidAccess: win32more.System.Hypervisor.WHV_X64_CPUID_ACCESS_CONTEXT
        VpException: win32more.System.Hypervisor.WHV_VP_EXCEPTION_CONTEXT
        InterruptWindow: win32more.System.Hypervisor.WHV_X64_INTERRUPTION_DELIVERABLE_CONTEXT
        UnsupportedFeature: win32more.System.Hypervisor.WHV_X64_UNSUPPORTED_FEATURE_CONTEXT
        CancelReason: win32more.System.Hypervisor.WHV_RUN_VP_CANCELED_CONTEXT
        ApicEoi: win32more.System.Hypervisor.WHV_X64_APIC_EOI_CONTEXT
        ReadTsc: win32more.System.Hypervisor.WHV_X64_RDTSC_CONTEXT
        ApicSmi: win32more.System.Hypervisor.WHV_X64_APIC_SMI_CONTEXT
        Hypercall: win32more.System.Hypervisor.WHV_HYPERCALL_CONTEXT
        ApicInitSipi: win32more.System.Hypervisor.WHV_X64_APIC_INIT_SIPI_CONTEXT
        ApicWrite: win32more.System.Hypervisor.WHV_X64_APIC_WRITE_CONTEXT
        SynicSintDeliverable: win32more.System.Hypervisor.WHV_SYNIC_SINT_DELIVERABLE_CONTEXT
WHV_RUN_VP_EXIT_REASON = Int32
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonNone: WHV_RUN_VP_EXIT_REASON = 0
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonMemoryAccess: WHV_RUN_VP_EXIT_REASON = 1
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64IoPortAccess: WHV_RUN_VP_EXIT_REASON = 2
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonUnrecoverableException: WHV_RUN_VP_EXIT_REASON = 4
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonInvalidVpRegisterValue: WHV_RUN_VP_EXIT_REASON = 5
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonUnsupportedFeature: WHV_RUN_VP_EXIT_REASON = 6
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64InterruptWindow: WHV_RUN_VP_EXIT_REASON = 7
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64Halt: WHV_RUN_VP_EXIT_REASON = 8
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64ApicEoi: WHV_RUN_VP_EXIT_REASON = 9
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonSynicSintDeliverable: WHV_RUN_VP_EXIT_REASON = 10
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64MsrAccess: WHV_RUN_VP_EXIT_REASON = 4096
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64Cpuid: WHV_RUN_VP_EXIT_REASON = 4097
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonException: WHV_RUN_VP_EXIT_REASON = 4098
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64Rdtsc: WHV_RUN_VP_EXIT_REASON = 4099
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64ApicSmiTrap: WHV_RUN_VP_EXIT_REASON = 4100
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonHypercall: WHV_RUN_VP_EXIT_REASON = 4101
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64ApicInitSipiTrap: WHV_RUN_VP_EXIT_REASON = 4102
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64ApicWriteTrap: WHV_RUN_VP_EXIT_REASON = 4103
WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonCanceled: WHV_RUN_VP_EXIT_REASON = 8193
class WHV_SCHEDULER_FEATURES(Union):
    Anonymous: _Anonymous_e__Struct
    AsUINT64: UInt64
    class _Anonymous_e__Struct(Structure):
        _bitfield: UInt64
class WHV_SRIOV_RESOURCE_DESCRIPTOR(Structure):
    PnpInstanceId: Char * 200
    VirtualFunctionId: win32more.Foundation.LUID
    VirtualFunctionIndex: UInt16
    Reserved: UInt16
class WHV_SYNIC_EVENT_PARAMETERS(Structure):
    VpIndex: UInt32
    TargetSint: Byte
    Reserved: Byte
    FlagNumber: UInt16
class WHV_SYNIC_SINT_DELIVERABLE_CONTEXT(Structure):
    DeliverableSints: UInt16
    Reserved1: UInt16
    Reserved2: UInt32
class WHV_SYNTHETIC_PROCESSOR_FEATURES(Union):
    Anonymous: _Anonymous_e__Struct
    AsUINT64: UInt64
    class _Anonymous_e__Struct(Structure):
        _bitfield: UInt64
class WHV_SYNTHETIC_PROCESSOR_FEATURES_BANKS(Structure):
    BanksCount: UInt32
    Reserved0: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        AsUINT64: UInt64 * 1
        class _Anonymous_e__Struct(Structure):
            Bank0: win32more.System.Hypervisor.WHV_SYNTHETIC_PROCESSOR_FEATURES
WHV_TRANSLATE_GVA_FLAGS = UInt32
WHV_TRANSLATE_GVA_FLAGS_WHvTranslateGvaFlagNone: WHV_TRANSLATE_GVA_FLAGS = 0
WHV_TRANSLATE_GVA_FLAGS_WHvTranslateGvaFlagValidateRead: WHV_TRANSLATE_GVA_FLAGS = 1
WHV_TRANSLATE_GVA_FLAGS_WHvTranslateGvaFlagValidateWrite: WHV_TRANSLATE_GVA_FLAGS = 2
WHV_TRANSLATE_GVA_FLAGS_WHvTranslateGvaFlagValidateExecute: WHV_TRANSLATE_GVA_FLAGS = 4
WHV_TRANSLATE_GVA_FLAGS_WHvTranslateGvaFlagPrivilegeExempt: WHV_TRANSLATE_GVA_FLAGS = 8
WHV_TRANSLATE_GVA_FLAGS_WHvTranslateGvaFlagSetPageTableBits: WHV_TRANSLATE_GVA_FLAGS = 16
WHV_TRANSLATE_GVA_FLAGS_WHvTranslateGvaFlagEnforceSmap: WHV_TRANSLATE_GVA_FLAGS = 256
WHV_TRANSLATE_GVA_FLAGS_WHvTranslateGvaFlagOverrideSmap: WHV_TRANSLATE_GVA_FLAGS = 512
class WHV_TRANSLATE_GVA_RESULT(Structure):
    ResultCode: win32more.System.Hypervisor.WHV_TRANSLATE_GVA_RESULT_CODE
    Reserved: UInt32
WHV_TRANSLATE_GVA_RESULT_CODE = Int32
WHV_TRANSLATE_GVA_RESULT_CODE_WHvTranslateGvaResultSuccess: WHV_TRANSLATE_GVA_RESULT_CODE = 0
WHV_TRANSLATE_GVA_RESULT_CODE_WHvTranslateGvaResultPageNotPresent: WHV_TRANSLATE_GVA_RESULT_CODE = 1
WHV_TRANSLATE_GVA_RESULT_CODE_WHvTranslateGvaResultPrivilegeViolation: WHV_TRANSLATE_GVA_RESULT_CODE = 2
WHV_TRANSLATE_GVA_RESULT_CODE_WHvTranslateGvaResultInvalidPageTableFlags: WHV_TRANSLATE_GVA_RESULT_CODE = 3
WHV_TRANSLATE_GVA_RESULT_CODE_WHvTranslateGvaResultGpaUnmapped: WHV_TRANSLATE_GVA_RESULT_CODE = 4
WHV_TRANSLATE_GVA_RESULT_CODE_WHvTranslateGvaResultGpaNoReadAccess: WHV_TRANSLATE_GVA_RESULT_CODE = 5
WHV_TRANSLATE_GVA_RESULT_CODE_WHvTranslateGvaResultGpaNoWriteAccess: WHV_TRANSLATE_GVA_RESULT_CODE = 6
WHV_TRANSLATE_GVA_RESULT_CODE_WHvTranslateGvaResultGpaIllegalOverlayAccess: WHV_TRANSLATE_GVA_RESULT_CODE = 7
WHV_TRANSLATE_GVA_RESULT_CODE_WHvTranslateGvaResultIntercept: WHV_TRANSLATE_GVA_RESULT_CODE = 8
class WHV_TRIGGER_PARAMETERS(Structure):
    TriggerType: win32more.System.Hypervisor.WHV_TRIGGER_TYPE
    Reserved: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Interrupt: win32more.System.Hypervisor.WHV_INTERRUPT_CONTROL
        SynicEvent: win32more.System.Hypervisor.WHV_SYNIC_EVENT_PARAMETERS
        DeviceInterrupt: _DeviceInterrupt_e__Struct
        class _DeviceInterrupt_e__Struct(Structure):
            LogicalDeviceId: UInt64
            MsiAddress: UInt64
            MsiData: UInt32
            Reserved: UInt32
WHV_TRIGGER_TYPE = Int32
WHV_TRIGGER_TYPE_WHvTriggerTypeInterrupt: WHV_TRIGGER_TYPE = 0
WHV_TRIGGER_TYPE_WHvTriggerTypeSynicEvent: WHV_TRIGGER_TYPE = 1
WHV_TRIGGER_TYPE_WHvTriggerTypeDeviceInterrupt: WHV_TRIGGER_TYPE = 2
class WHV_UINT128(Union):
    Anonymous: _Anonymous_e__Struct
    Dword: UInt32 * 4
    class _Anonymous_e__Struct(Structure):
        Low64: UInt64
        High64: UInt64
class WHV_VIRTUAL_PROCESSOR_PROPERTY(Structure):
    PropertyCode: win32more.System.Hypervisor.WHV_VIRTUAL_PROCESSOR_PROPERTY_CODE
    Reserved: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        NumaNode: UInt16
        Padding: UInt64
WHV_VIRTUAL_PROCESSOR_PROPERTY_CODE = Int32
WHV_VIRTUAL_PROCESSOR_PROPERTY_CODE_WHvVirtualProcessorPropertyCodeNumaNode: WHV_VIRTUAL_PROCESSOR_PROPERTY_CODE = 0
WHV_VIRTUAL_PROCESSOR_STATE_TYPE = Int32
WHV_VIRTUAL_PROCESSOR_STATE_TYPE_WHvVirtualProcessorStateTypeSynicMessagePage: WHV_VIRTUAL_PROCESSOR_STATE_TYPE = 0
WHV_VIRTUAL_PROCESSOR_STATE_TYPE_WHvVirtualProcessorStateTypeSynicEventFlagPage: WHV_VIRTUAL_PROCESSOR_STATE_TYPE = 1
WHV_VIRTUAL_PROCESSOR_STATE_TYPE_WHvVirtualProcessorStateTypeSynicTimerState: WHV_VIRTUAL_PROCESSOR_STATE_TYPE = 2
WHV_VIRTUAL_PROCESSOR_STATE_TYPE_WHvVirtualProcessorStateTypeInterruptControllerState2: WHV_VIRTUAL_PROCESSOR_STATE_TYPE = 4096
WHV_VIRTUAL_PROCESSOR_STATE_TYPE_WHvVirtualProcessorStateTypeXsaveState: WHV_VIRTUAL_PROCESSOR_STATE_TYPE = 4097
class WHV_VP_EXCEPTION_CONTEXT(Structure):
    InstructionByteCount: Byte
    Reserved: Byte * 3
    InstructionBytes: Byte * 16
    ExceptionInfo: win32more.System.Hypervisor.WHV_VP_EXCEPTION_INFO
    ExceptionType: Byte
    Reserved2: Byte * 3
    ErrorCode: UInt32
    ExceptionParameter: UInt64
class WHV_VP_EXCEPTION_INFO(Union):
    Anonymous: _Anonymous_e__Struct
    AsUINT32: UInt32
    class _Anonymous_e__Struct(Structure):
        _bitfield: UInt32
class WHV_VP_EXIT_CONTEXT(Structure):
    ExecutionState: win32more.System.Hypervisor.WHV_X64_VP_EXECUTION_STATE
    _bitfield: Byte
    Reserved: Byte
    Reserved2: UInt32
    Cs: win32more.System.Hypervisor.WHV_X64_SEGMENT_REGISTER
    Rip: UInt64
    Rflags: UInt64
class WHV_VPCI_DEVICE_NOTIFICATION(Structure):
    NotificationType: win32more.System.Hypervisor.WHV_VPCI_DEVICE_NOTIFICATION_TYPE
    Reserved1: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Reserved2: UInt64
WHV_VPCI_DEVICE_NOTIFICATION_TYPE = Int32
WHV_VPCI_DEVICE_NOTIFICATION_TYPE_WHvVpciDeviceNotificationUndefined: WHV_VPCI_DEVICE_NOTIFICATION_TYPE = 0
WHV_VPCI_DEVICE_NOTIFICATION_TYPE_WHvVpciDeviceNotificationMmioRemapping: WHV_VPCI_DEVICE_NOTIFICATION_TYPE = 1
WHV_VPCI_DEVICE_NOTIFICATION_TYPE_WHvVpciDeviceNotificationSurpriseRemoval: WHV_VPCI_DEVICE_NOTIFICATION_TYPE = 2
WHV_VPCI_DEVICE_PROPERTY_CODE = Int32
WHV_VPCI_DEVICE_PROPERTY_CODE_WHvVpciDevicePropertyCodeUndefined: WHV_VPCI_DEVICE_PROPERTY_CODE = 0
WHV_VPCI_DEVICE_PROPERTY_CODE_WHvVpciDevicePropertyCodeHardwareIDs: WHV_VPCI_DEVICE_PROPERTY_CODE = 1
WHV_VPCI_DEVICE_PROPERTY_CODE_WHvVpciDevicePropertyCodeProbedBARs: WHV_VPCI_DEVICE_PROPERTY_CODE = 2
class WHV_VPCI_DEVICE_REGISTER(Structure):
    Location: win32more.System.Hypervisor.WHV_VPCI_DEVICE_REGISTER_SPACE
    SizeInBytes: UInt32
    OffsetInBytes: UInt64
WHV_VPCI_DEVICE_REGISTER_SPACE = Int32
WHV_VPCI_DEVICE_REGISTER_SPACE_WHvVpciConfigSpace: WHV_VPCI_DEVICE_REGISTER_SPACE = -1
WHV_VPCI_DEVICE_REGISTER_SPACE_WHvVpciBar0: WHV_VPCI_DEVICE_REGISTER_SPACE = 0
WHV_VPCI_DEVICE_REGISTER_SPACE_WHvVpciBar1: WHV_VPCI_DEVICE_REGISTER_SPACE = 1
WHV_VPCI_DEVICE_REGISTER_SPACE_WHvVpciBar2: WHV_VPCI_DEVICE_REGISTER_SPACE = 2
WHV_VPCI_DEVICE_REGISTER_SPACE_WHvVpciBar3: WHV_VPCI_DEVICE_REGISTER_SPACE = 3
WHV_VPCI_DEVICE_REGISTER_SPACE_WHvVpciBar4: WHV_VPCI_DEVICE_REGISTER_SPACE = 4
WHV_VPCI_DEVICE_REGISTER_SPACE_WHvVpciBar5: WHV_VPCI_DEVICE_REGISTER_SPACE = 5
class WHV_VPCI_HARDWARE_IDS(Structure):
    VendorID: UInt16
    DeviceID: UInt16
    RevisionID: Byte
    ProgIf: Byte
    SubClass: Byte
    BaseClass: Byte
    SubVendorID: UInt16
    SubSystemID: UInt16
class WHV_VPCI_INTERRUPT_TARGET(Structure):
    Vector: UInt32
    Flags: win32more.System.Hypervisor.WHV_VPCI_INTERRUPT_TARGET_FLAGS
    ProcessorCount: UInt32
    Processors: UInt32 * 1
WHV_VPCI_INTERRUPT_TARGET_FLAGS = UInt32
WHV_VPCI_INTERRUPT_TARGET_FLAGS_WHvVpciInterruptTargetFlagNone: WHV_VPCI_INTERRUPT_TARGET_FLAGS = 0
WHV_VPCI_INTERRUPT_TARGET_FLAGS_WHvVpciInterruptTargetFlagMulticast: WHV_VPCI_INTERRUPT_TARGET_FLAGS = 1
class WHV_VPCI_MMIO_MAPPING(Structure):
    Location: win32more.System.Hypervisor.WHV_VPCI_DEVICE_REGISTER_SPACE
    Flags: win32more.System.Hypervisor.WHV_VPCI_MMIO_RANGE_FLAGS
    SizeInBytes: UInt64
    OffsetInBytes: UInt64
    VirtualAddress: c_void_p
WHV_VPCI_MMIO_RANGE_FLAGS = UInt32
WHV_VPCI_MMIO_RANGE_FLAGS_WHvVpciMmioRangeFlagReadAccess: WHV_VPCI_MMIO_RANGE_FLAGS = 1
WHV_VPCI_MMIO_RANGE_FLAGS_WHvVpciMmioRangeFlagWriteAccess: WHV_VPCI_MMIO_RANGE_FLAGS = 2
class WHV_VPCI_PROBED_BARS(Structure):
    Value: UInt32 * 6
class WHV_X64_APIC_EOI_CONTEXT(Structure):
    InterruptVector: UInt32
class WHV_X64_APIC_INIT_SIPI_CONTEXT(Structure):
    ApicIcr: UInt64
class WHV_X64_APIC_SMI_CONTEXT(Structure):
    ApicIcr: UInt64
class WHV_X64_APIC_WRITE_CONTEXT(Structure):
    Type: win32more.System.Hypervisor.WHV_X64_APIC_WRITE_TYPE
    Reserved: UInt32
    WriteValue: UInt64
WHV_X64_APIC_WRITE_TYPE = Int32
WHV_X64_APIC_WRITE_TYPE_WHvX64ApicWriteTypeLdr: WHV_X64_APIC_WRITE_TYPE = 208
WHV_X64_APIC_WRITE_TYPE_WHvX64ApicWriteTypeDfr: WHV_X64_APIC_WRITE_TYPE = 224
WHV_X64_APIC_WRITE_TYPE_WHvX64ApicWriteTypeSvr: WHV_X64_APIC_WRITE_TYPE = 240
WHV_X64_APIC_WRITE_TYPE_WHvX64ApicWriteTypeLint0: WHV_X64_APIC_WRITE_TYPE = 848
WHV_X64_APIC_WRITE_TYPE_WHvX64ApicWriteTypeLint1: WHV_X64_APIC_WRITE_TYPE = 864
class WHV_X64_CPUID_ACCESS_CONTEXT(Structure):
    Rax: UInt64
    Rcx: UInt64
    Rdx: UInt64
    Rbx: UInt64
    DefaultResultRax: UInt64
    DefaultResultRcx: UInt64
    DefaultResultRdx: UInt64
    DefaultResultRbx: UInt64
class WHV_X64_CPUID_RESULT(Structure):
    Function: UInt32
    Reserved: UInt32 * 3
    Eax: UInt32
    Ebx: UInt32
    Ecx: UInt32
    Edx: UInt32
class WHV_X64_CPUID_RESULT2(Structure):
    Function: UInt32
    Index: UInt32
    VpIndex: UInt32
    Flags: win32more.System.Hypervisor.WHV_X64_CPUID_RESULT2_FLAGS
    Output: win32more.System.Hypervisor.WHV_CPUID_OUTPUT
    Mask: win32more.System.Hypervisor.WHV_CPUID_OUTPUT
WHV_X64_CPUID_RESULT2_FLAGS = UInt32
WHV_X64_CPUID_RESULT2_FLAGS_WHvX64CpuidResult2FlagSubleafSpecific: WHV_X64_CPUID_RESULT2_FLAGS = 1
WHV_X64_CPUID_RESULT2_FLAGS_WHvX64CpuidResult2FlagVpSpecific: WHV_X64_CPUID_RESULT2_FLAGS = 2
class WHV_X64_DELIVERABILITY_NOTIFICATIONS_REGISTER(Union):
    Anonymous: _Anonymous_e__Struct
    AsUINT64: UInt64
    class _Anonymous_e__Struct(Structure):
        _bitfield: UInt64
class WHV_X64_FP_CONTROL_STATUS_REGISTER(Union):
    Anonymous: _Anonymous_e__Struct
    AsUINT128: win32more.System.Hypervisor.WHV_UINT128
    class _Anonymous_e__Struct(Structure):
        FpControl: UInt16
        FpStatus: UInt16
        FpTag: Byte
        Reserved: Byte
        LastFpOp: UInt16
        Anonymous: _Anonymous_e__Union
        class _Anonymous_e__Union(Union):
            LastFpRip: UInt64
            Anonymous: _Anonymous_e__Struct
            class _Anonymous_e__Struct(Structure):
                LastFpEip: UInt32
                LastFpCs: UInt16
                Reserved2: UInt16
class WHV_X64_FP_REGISTER(Union):
    Anonymous: _Anonymous_e__Struct
    AsUINT128: win32more.System.Hypervisor.WHV_UINT128
    class _Anonymous_e__Struct(Structure):
        Mantissa: UInt64
        _bitfield: UInt64
class WHV_X64_INTERRUPT_STATE_REGISTER(Union):
    Anonymous: _Anonymous_e__Struct
    AsUINT64: UInt64
    class _Anonymous_e__Struct(Structure):
        _bitfield: UInt64
class WHV_X64_INTERRUPTION_DELIVERABLE_CONTEXT(Structure):
    DeliverableType: win32more.System.Hypervisor.WHV_X64_PENDING_INTERRUPTION_TYPE
class WHV_X64_IO_PORT_ACCESS_CONTEXT(Structure):
    InstructionByteCount: Byte
    Reserved: Byte * 3
    InstructionBytes: Byte * 16
    AccessInfo: win32more.System.Hypervisor.WHV_X64_IO_PORT_ACCESS_INFO
    PortNumber: UInt16
    Reserved2: UInt16 * 3
    Rax: UInt64
    Rcx: UInt64
    Rsi: UInt64
    Rdi: UInt64
    Ds: win32more.System.Hypervisor.WHV_X64_SEGMENT_REGISTER
    Es: win32more.System.Hypervisor.WHV_X64_SEGMENT_REGISTER
class WHV_X64_IO_PORT_ACCESS_INFO(Union):
    Anonymous: _Anonymous_e__Struct
    AsUINT32: UInt32
    class _Anonymous_e__Struct(Structure):
        _bitfield: UInt32
WHV_X64_LOCAL_APIC_EMULATION_MODE = Int32
WHV_X64_LOCAL_APIC_EMULATION_MODE_WHvX64LocalApicEmulationModeNone: WHV_X64_LOCAL_APIC_EMULATION_MODE = 0
WHV_X64_LOCAL_APIC_EMULATION_MODE_WHvX64LocalApicEmulationModeXApic: WHV_X64_LOCAL_APIC_EMULATION_MODE = 1
WHV_X64_LOCAL_APIC_EMULATION_MODE_WHvX64LocalApicEmulationModeX2Apic: WHV_X64_LOCAL_APIC_EMULATION_MODE = 2
class WHV_X64_MSR_ACCESS_CONTEXT(Structure):
    AccessInfo: win32more.System.Hypervisor.WHV_X64_MSR_ACCESS_INFO
    MsrNumber: UInt32
    Rax: UInt64
    Rdx: UInt64
class WHV_X64_MSR_ACCESS_INFO(Union):
    Anonymous: _Anonymous_e__Struct
    AsUINT32: UInt32
    class _Anonymous_e__Struct(Structure):
        _bitfield: UInt32
class WHV_X64_MSR_EXIT_BITMAP(Union):
    AsUINT64: UInt64
    Anonymous: _Anonymous_e__Struct
    class _Anonymous_e__Struct(Structure):
        _bitfield: UInt64
class WHV_X64_PENDING_DEBUG_EXCEPTION(Union):
    AsUINT64: UInt64
    Anonymous: _Anonymous_e__Struct
    class _Anonymous_e__Struct(Structure):
        _bitfield: UInt64
WHV_X64_PENDING_EVENT_TYPE = Int32
WHV_X64_PENDING_EVENT_TYPE_WHvX64PendingEventException: WHV_X64_PENDING_EVENT_TYPE = 0
WHV_X64_PENDING_EVENT_TYPE_WHvX64PendingEventExtInt: WHV_X64_PENDING_EVENT_TYPE = 5
class WHV_X64_PENDING_EXCEPTION_EVENT(Union):
    Anonymous: _Anonymous_e__Struct
    AsUINT128: win32more.System.Hypervisor.WHV_UINT128
    class _Anonymous_e__Struct(Structure):
        _bitfield: UInt32
        ErrorCode: UInt32
        ExceptionParameter: UInt64
class WHV_X64_PENDING_EXT_INT_EVENT(Union):
    Anonymous: _Anonymous_e__Struct
    AsUINT128: win32more.System.Hypervisor.WHV_UINT128
    class _Anonymous_e__Struct(Structure):
        _bitfield: UInt64
        Reserved2: UInt64
class WHV_X64_PENDING_INTERRUPTION_REGISTER(Union):
    Anonymous: _Anonymous_e__Struct
    AsUINT64: UInt64
    class _Anonymous_e__Struct(Structure):
        _bitfield: UInt32
        ErrorCode: UInt32
WHV_X64_PENDING_INTERRUPTION_TYPE = Int32
WHV_X64_PENDING_INTERRUPTION_TYPE_WHvX64PendingInterrupt: WHV_X64_PENDING_INTERRUPTION_TYPE = 0
WHV_X64_PENDING_INTERRUPTION_TYPE_WHvX64PendingNmi: WHV_X64_PENDING_INTERRUPTION_TYPE = 2
WHV_X64_PENDING_INTERRUPTION_TYPE_WHvX64PendingException: WHV_X64_PENDING_INTERRUPTION_TYPE = 3
class WHV_X64_RDTSC_CONTEXT(Structure):
    TscAux: UInt64
    VirtualOffset: UInt64
    Tsc: UInt64
    ReferenceTime: UInt64
    RdtscInfo: win32more.System.Hypervisor.WHV_X64_RDTSC_INFO
class WHV_X64_RDTSC_INFO(Union):
    Anonymous: _Anonymous_e__Struct
    AsUINT64: UInt64
    class _Anonymous_e__Struct(Structure):
        _bitfield: UInt64
class WHV_X64_SEGMENT_REGISTER(Structure):
    Base: UInt64
    Limit: UInt32
    Selector: UInt16
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        Attributes: UInt16
        class _Anonymous_e__Struct(Structure):
            _bitfield: UInt16
class WHV_X64_TABLE_REGISTER(Structure):
    Pad: UInt16 * 3
    Limit: UInt16
    Base: UInt64
WHV_X64_UNSUPPORTED_FEATURE_CODE = Int32
WHV_X64_UNSUPPORTED_FEATURE_CODE_WHvUnsupportedFeatureIntercept: WHV_X64_UNSUPPORTED_FEATURE_CODE = 1
WHV_X64_UNSUPPORTED_FEATURE_CODE_WHvUnsupportedFeatureTaskSwitchTss: WHV_X64_UNSUPPORTED_FEATURE_CODE = 2
class WHV_X64_UNSUPPORTED_FEATURE_CONTEXT(Structure):
    FeatureCode: win32more.System.Hypervisor.WHV_X64_UNSUPPORTED_FEATURE_CODE
    Reserved: UInt32
    FeatureParameter: UInt64
class WHV_X64_VP_EXECUTION_STATE(Union):
    Anonymous: _Anonymous_e__Struct
    AsUINT16: UInt16
    class _Anonymous_e__Struct(Structure):
        _bitfield: UInt16
class WHV_X64_XMM_CONTROL_STATUS_REGISTER(Union):
    Anonymous: _Anonymous_e__Struct
    AsUINT128: win32more.System.Hypervisor.WHV_UINT128
    class _Anonymous_e__Struct(Structure):
        Anonymous: _Anonymous_e__Union
        XmmStatusControl: UInt32
        XmmStatusControlMask: UInt32
        class _Anonymous_e__Union(Union):
            LastFpRdp: UInt64
            Anonymous: _Anonymous_e__Struct
            class _Anonymous_e__Struct(Structure):
                LastFpDp: UInt32
                LastFpDs: UInt16
                Reserved: UInt16
make_head(_module, 'DOS_IMAGE_INFO')
make_head(_module, 'FOUND_IMAGE_CALLBACK')
make_head(_module, 'GPA_MEMORY_CHUNK')
make_head(_module, 'GUEST_OS_INFO')
make_head(_module, 'GUEST_SYMBOLS_PROVIDER_DEBUG_INFO_CALLBACK')
make_head(_module, 'HDV_PCI_DEVICE_GET_DETAILS')
make_head(_module, 'HDV_PCI_DEVICE_INITIALIZE')
make_head(_module, 'HDV_PCI_DEVICE_INTERFACE')
make_head(_module, 'HDV_PCI_DEVICE_SET_CONFIGURATION')
make_head(_module, 'HDV_PCI_DEVICE_START')
make_head(_module, 'HDV_PCI_DEVICE_STOP')
make_head(_module, 'HDV_PCI_DEVICE_TEARDOWN')
make_head(_module, 'HDV_PCI_PNP_ID')
make_head(_module, 'HDV_PCI_READ_CONFIG_SPACE')
make_head(_module, 'HDV_PCI_READ_INTERCEPTED_MEMORY')
make_head(_module, 'HDV_PCI_WRITE_CONFIG_SPACE')
make_head(_module, 'HDV_PCI_WRITE_INTERCEPTED_MEMORY')
make_head(_module, 'HVSOCKET_ADDRESS_INFO')
make_head(_module, 'MODULE_INFO')
make_head(_module, 'SOCKADDR_HV')
make_head(_module, 'VIRTUAL_PROCESSOR_REGISTER')
make_head(_module, 'VM_GENCOUNTER')
make_head(_module, 'WHV_ACCESS_GPA_CONTROLS')
make_head(_module, 'WHV_ADVISE_GPA_RANGE')
make_head(_module, 'WHV_ADVISE_GPA_RANGE_POPULATE')
make_head(_module, 'WHV_ADVISE_GPA_RANGE_POPULATE_FLAGS')
make_head(_module, 'WHV_CAPABILITY')
make_head(_module, 'WHV_CAPABILITY_FEATURES')
make_head(_module, 'WHV_CAPABILITY_PROCESSOR_FREQUENCY_CAP')
make_head(_module, 'WHV_CPUID_OUTPUT')
make_head(_module, 'WHV_DOORBELL_MATCH_DATA')
make_head(_module, 'WHV_EMULATOR_CALLBACKS')
make_head(_module, 'WHV_EMULATOR_GET_VIRTUAL_PROCESSOR_REGISTERS_CALLBACK')
make_head(_module, 'WHV_EMULATOR_IO_ACCESS_INFO')
make_head(_module, 'WHV_EMULATOR_IO_PORT_CALLBACK')
make_head(_module, 'WHV_EMULATOR_MEMORY_ACCESS_INFO')
make_head(_module, 'WHV_EMULATOR_MEMORY_CALLBACK')
make_head(_module, 'WHV_EMULATOR_SET_VIRTUAL_PROCESSOR_REGISTERS_CALLBACK')
make_head(_module, 'WHV_EMULATOR_STATUS')
make_head(_module, 'WHV_EMULATOR_TRANSLATE_GVA_PAGE_CALLBACK')
make_head(_module, 'WHV_EXTENDED_VM_EXITS')
make_head(_module, 'WHV_HYPERCALL_CONTEXT')
make_head(_module, 'WHV_INTERNAL_ACTIVITY_REGISTER')
make_head(_module, 'WHV_INTERRUPT_CONTROL')
make_head(_module, 'WHV_MEMORY_ACCESS_CONTEXT')
make_head(_module, 'WHV_MEMORY_ACCESS_INFO')
make_head(_module, 'WHV_MEMORY_RANGE_ENTRY')
make_head(_module, 'WHV_MSR_ACTION_ENTRY')
make_head(_module, 'WHV_NOTIFICATION_PORT_PARAMETERS')
make_head(_module, 'WHV_PARTITION_MEMORY_COUNTERS')
make_head(_module, 'WHV_PARTITION_PROPERTY')
make_head(_module, 'WHV_PROCESSOR_APIC_COUNTERS')
make_head(_module, 'WHV_PROCESSOR_EVENT_COUNTERS')
make_head(_module, 'WHV_PROCESSOR_FEATURES')
make_head(_module, 'WHV_PROCESSOR_FEATURES_BANKS')
make_head(_module, 'WHV_PROCESSOR_FEATURES1')
make_head(_module, 'WHV_PROCESSOR_INTERCEPT_COUNTER')
make_head(_module, 'WHV_PROCESSOR_INTERCEPT_COUNTERS')
make_head(_module, 'WHV_PROCESSOR_PERFMON_FEATURES')
make_head(_module, 'WHV_PROCESSOR_RUNTIME_COUNTERS')
make_head(_module, 'WHV_PROCESSOR_SYNTHETIC_FEATURES_COUNTERS')
make_head(_module, 'WHV_PROCESSOR_XSAVE_FEATURES')
make_head(_module, 'WHV_REGISTER_VALUE')
make_head(_module, 'WHV_RUN_VP_CANCELED_CONTEXT')
make_head(_module, 'WHV_RUN_VP_EXIT_CONTEXT')
make_head(_module, 'WHV_SCHEDULER_FEATURES')
make_head(_module, 'WHV_SRIOV_RESOURCE_DESCRIPTOR')
make_head(_module, 'WHV_SYNIC_EVENT_PARAMETERS')
make_head(_module, 'WHV_SYNIC_SINT_DELIVERABLE_CONTEXT')
make_head(_module, 'WHV_SYNTHETIC_PROCESSOR_FEATURES')
make_head(_module, 'WHV_SYNTHETIC_PROCESSOR_FEATURES_BANKS')
make_head(_module, 'WHV_TRANSLATE_GVA_RESULT')
make_head(_module, 'WHV_TRIGGER_PARAMETERS')
make_head(_module, 'WHV_UINT128')
make_head(_module, 'WHV_VIRTUAL_PROCESSOR_PROPERTY')
make_head(_module, 'WHV_VP_EXCEPTION_CONTEXT')
make_head(_module, 'WHV_VP_EXCEPTION_INFO')
make_head(_module, 'WHV_VP_EXIT_CONTEXT')
make_head(_module, 'WHV_VPCI_DEVICE_NOTIFICATION')
make_head(_module, 'WHV_VPCI_DEVICE_REGISTER')
make_head(_module, 'WHV_VPCI_HARDWARE_IDS')
make_head(_module, 'WHV_VPCI_INTERRUPT_TARGET')
make_head(_module, 'WHV_VPCI_MMIO_MAPPING')
make_head(_module, 'WHV_VPCI_PROBED_BARS')
make_head(_module, 'WHV_X64_APIC_EOI_CONTEXT')
make_head(_module, 'WHV_X64_APIC_INIT_SIPI_CONTEXT')
make_head(_module, 'WHV_X64_APIC_SMI_CONTEXT')
make_head(_module, 'WHV_X64_APIC_WRITE_CONTEXT')
make_head(_module, 'WHV_X64_CPUID_ACCESS_CONTEXT')
make_head(_module, 'WHV_X64_CPUID_RESULT')
make_head(_module, 'WHV_X64_CPUID_RESULT2')
make_head(_module, 'WHV_X64_DELIVERABILITY_NOTIFICATIONS_REGISTER')
make_head(_module, 'WHV_X64_FP_CONTROL_STATUS_REGISTER')
make_head(_module, 'WHV_X64_FP_REGISTER')
make_head(_module, 'WHV_X64_INTERRUPT_STATE_REGISTER')
make_head(_module, 'WHV_X64_INTERRUPTION_DELIVERABLE_CONTEXT')
make_head(_module, 'WHV_X64_IO_PORT_ACCESS_CONTEXT')
make_head(_module, 'WHV_X64_IO_PORT_ACCESS_INFO')
make_head(_module, 'WHV_X64_MSR_ACCESS_CONTEXT')
make_head(_module, 'WHV_X64_MSR_ACCESS_INFO')
make_head(_module, 'WHV_X64_MSR_EXIT_BITMAP')
make_head(_module, 'WHV_X64_PENDING_DEBUG_EXCEPTION')
make_head(_module, 'WHV_X64_PENDING_EXCEPTION_EVENT')
make_head(_module, 'WHV_X64_PENDING_EXT_INT_EVENT')
make_head(_module, 'WHV_X64_PENDING_INTERRUPTION_REGISTER')
make_head(_module, 'WHV_X64_RDTSC_CONTEXT')
make_head(_module, 'WHV_X64_RDTSC_INFO')
make_head(_module, 'WHV_X64_SEGMENT_REGISTER')
make_head(_module, 'WHV_X64_TABLE_REGISTER')
make_head(_module, 'WHV_X64_UNSUPPORTED_FEATURE_CONTEXT')
make_head(_module, 'WHV_X64_VP_EXECUTION_STATE')
make_head(_module, 'WHV_X64_XMM_CONTROL_STATUS_REGISTER')
__all__ = [
    "ARM64_RegisterActlrEl1",
    "ARM64_RegisterAmairEl1",
    "ARM64_RegisterCntkctlEl1",
    "ARM64_RegisterCntvCtlEl0",
    "ARM64_RegisterCntvCvalEl0",
    "ARM64_RegisterContextIdrEl1",
    "ARM64_RegisterCpacrEl1",
    "ARM64_RegisterCpsr",
    "ARM64_RegisterCsselrEl1",
    "ARM64_RegisterElrEl1",
    "ARM64_RegisterEsrEl1",
    "ARM64_RegisterFarEl1",
    "ARM64_RegisterFpControl",
    "ARM64_RegisterFpStatus",
    "ARM64_RegisterMairEl1",
    "ARM64_RegisterMax",
    "ARM64_RegisterParEl1",
    "ARM64_RegisterPc",
    "ARM64_RegisterQ0",
    "ARM64_RegisterQ1",
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
    "ARM64_RegisterQ2",
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
    "ARM64_RegisterQ3",
    "ARM64_RegisterQ30",
    "ARM64_RegisterQ31",
    "ARM64_RegisterQ4",
    "ARM64_RegisterQ5",
    "ARM64_RegisterQ6",
    "ARM64_RegisterQ7",
    "ARM64_RegisterQ8",
    "ARM64_RegisterQ9",
    "ARM64_RegisterSctlrEl1",
    "ARM64_RegisterSpEl0",
    "ARM64_RegisterSpEl1",
    "ARM64_RegisterSpsrEl1",
    "ARM64_RegisterTcrEl1",
    "ARM64_RegisterTpidrEl0",
    "ARM64_RegisterTpidrEl1",
    "ARM64_RegisterTpidrroEl0",
    "ARM64_RegisterTtbr0El1",
    "ARM64_RegisterTtbr1El1",
    "ARM64_RegisterVbarEl1",
    "ARM64_RegisterX0",
    "ARM64_RegisterX1",
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
    "ARM64_RegisterX2",
    "ARM64_RegisterX20",
    "ARM64_RegisterX21",
    "ARM64_RegisterX22",
    "ARM64_RegisterX23",
    "ARM64_RegisterX24",
    "ARM64_RegisterX25",
    "ARM64_RegisterX26",
    "ARM64_RegisterX27",
    "ARM64_RegisterX28",
    "ARM64_RegisterX3",
    "ARM64_RegisterX4",
    "ARM64_RegisterX5",
    "ARM64_RegisterX6",
    "ARM64_RegisterX7",
    "ARM64_RegisterX8",
    "ARM64_RegisterX9",
    "ARM64_RegisterXFp",
    "ARM64_RegisterXLr",
    "ApplyGuestMemoryFix",
    "ApplyPendingSavedStateFileReplayLog",
    "Arch_Armv8",
    "Arch_Unknown",
    "Arch_x64",
    "Arch_x86",
    "CallStackUnwind",
    "DOS_IMAGE_INFO",
    "FOUND_IMAGE_CALLBACK",
    "FindSavedStateSymbolFieldInType",
    "ForceActiveVirtualTrustLevel",
    "ForceArchitecture",
    "ForceNestedHostMode",
    "ForcePagingMode",
    "GPA_MEMORY_CHUNK",
    "GUEST_OS_INFO",
    "GUEST_OS_MICROSOFT_IDS",
    "GUEST_OS_MICROSOFT_IDS_GuestOsMicrosoftMSDOS",
    "GUEST_OS_MICROSOFT_IDS_GuestOsMicrosoftUndefined",
    "GUEST_OS_MICROSOFT_IDS_GuestOsMicrosoftWindows3x",
    "GUEST_OS_MICROSOFT_IDS_GuestOsMicrosoftWindows9x",
    "GUEST_OS_MICROSOFT_IDS_GuestOsMicrosoftWindowsCE",
    "GUEST_OS_MICROSOFT_IDS_GuestOsMicrosoftWindowsNT",
    "GUEST_OS_OPENSOURCE_IDS",
    "GUEST_OS_OPENSOURCE_IDS_GuestOsOpenSourceFreeBSD",
    "GUEST_OS_OPENSOURCE_IDS_GuestOsOpenSourceIllumos",
    "GUEST_OS_OPENSOURCE_IDS_GuestOsOpenSourceLinux",
    "GUEST_OS_OPENSOURCE_IDS_GuestOsOpenSourceUndefined",
    "GUEST_OS_OPENSOURCE_IDS_GuestOsOpenSourceXen",
    "GUEST_OS_VENDOR",
    "GUEST_OS_VENDOR_GuestOsVendorHPE",
    "GUEST_OS_VENDOR_GuestOsVendorLANCOM",
    "GUEST_OS_VENDOR_GuestOsVendorMicrosoft",
    "GUEST_OS_VENDOR_GuestOsVendorUndefined",
    "GUEST_SYMBOLS_PROVIDER_DEBUG_INFO_CALLBACK",
    "GUID_DEVINTERFACE_VM_GENCOUNTER",
    "GetActiveVirtualTrustLevel",
    "GetArchitecture",
    "GetEnabledVirtualTrustLevels",
    "GetGuestEnabledVirtualTrustLevels",
    "GetGuestOsInfo",
    "GetGuestPhysicalMemoryChunks",
    "GetGuestRawSavedMemorySize",
    "GetMemoryBlockCacheLimit",
    "GetNestedVirtualizationMode",
    "GetPagingMode",
    "GetRegisterValue",
    "GetSavedStateSymbolFieldInfo",
    "GetSavedStateSymbolProviderHandle",
    "GetSavedStateSymbolTypeSize",
    "GetVpCount",
    "GuestPhysicalAddressToRawSavedMemoryOffset",
    "GuestVirtualAddressToPhysicalAddress",
    "HDV_DEVICE_TYPE",
    "HDV_DEVICE_TYPE_HdvDeviceTypePCI",
    "HDV_DEVICE_TYPE_HdvDeviceTypeUndefined",
    "HDV_DOORBELL_FLAGS",
    "HDV_DOORBELL_FLAG_TRIGGER_ANY_VALUE",
    "HDV_DOORBELL_FLAG_TRIGGER_SIZE_ANY",
    "HDV_DOORBELL_FLAG_TRIGGER_SIZE_BYTE",
    "HDV_DOORBELL_FLAG_TRIGGER_SIZE_DWORD",
    "HDV_DOORBELL_FLAG_TRIGGER_SIZE_QWORD",
    "HDV_DOORBELL_FLAG_TRIGGER_SIZE_WORD",
    "HDV_MMIO_MAPPING_FLAGS",
    "HDV_MMIO_MAPPING_FLAGS_HdvMmioMappingFlagExecutable",
    "HDV_MMIO_MAPPING_FLAGS_HdvMmioMappingFlagNone",
    "HDV_MMIO_MAPPING_FLAGS_HdvMmioMappingFlagWriteable",
    "HDV_PCI_BAR0",
    "HDV_PCI_BAR1",
    "HDV_PCI_BAR2",
    "HDV_PCI_BAR3",
    "HDV_PCI_BAR4",
    "HDV_PCI_BAR5",
    "HDV_PCI_BAR_COUNT",
    "HDV_PCI_BAR_SELECTOR",
    "HDV_PCI_DEVICE_GET_DETAILS",
    "HDV_PCI_DEVICE_INITIALIZE",
    "HDV_PCI_DEVICE_INTERFACE",
    "HDV_PCI_DEVICE_SET_CONFIGURATION",
    "HDV_PCI_DEVICE_START",
    "HDV_PCI_DEVICE_STOP",
    "HDV_PCI_DEVICE_TEARDOWN",
    "HDV_PCI_INTERFACE_VERSION",
    "HDV_PCI_INTERFACE_VERSION_HdvPciDeviceInterfaceVersion1",
    "HDV_PCI_INTERFACE_VERSION_HdvPciDeviceInterfaceVersionInvalid",
    "HDV_PCI_PNP_ID",
    "HDV_PCI_READ_CONFIG_SPACE",
    "HDV_PCI_READ_INTERCEPTED_MEMORY",
    "HDV_PCI_WRITE_CONFIG_SPACE",
    "HDV_PCI_WRITE_INTERCEPTED_MEMORY",
    "HVSOCKET_ADDRESS_FLAG_PASSTHRU",
    "HVSOCKET_ADDRESS_INFO",
    "HVSOCKET_CONNECTED_SUSPEND",
    "HVSOCKET_CONNECT_TIMEOUT",
    "HVSOCKET_CONNECT_TIMEOUT_MAX",
    "HVSOCKET_CONTAINER_PASSTHRU",
    "HV_GUID_BROADCAST",
    "HV_GUID_CHILDREN",
    "HV_GUID_LOOPBACK",
    "HV_GUID_PARENT",
    "HV_GUID_SILOHOST",
    "HV_GUID_VSOCK_TEMPLATE",
    "HV_GUID_ZERO",
    "HV_PROTOCOL_RAW",
    "HdvCreateDeviceInstance",
    "HdvCreateGuestMemoryAperture",
    "HdvCreateSectionBackedMmioRange",
    "HdvDeliverGuestInterrupt",
    "HdvDestroyGuestMemoryAperture",
    "HdvDestroySectionBackedMmioRange",
    "HdvInitializeDeviceHost",
    "HdvReadGuestMemory",
    "HdvRegisterDoorbell",
    "HdvTeardownDeviceHost",
    "HdvUnregisterDoorbell",
    "HdvWriteGuestMemory",
    "IOCTL_VMGENCOUNTER_READ",
    "InKernelSpace",
    "IsActiveVirtualTrustLevelEnabled",
    "IsNestedVirtualizationEnabled",
    "LoadSavedStateFile",
    "LoadSavedStateFiles",
    "LoadSavedStateModuleSymbols",
    "LoadSavedStateModuleSymbolsEx",
    "LoadSavedStateSymbolProvider",
    "LocateSavedStateFiles",
    "MODULE_INFO",
    "PAGING_MODE",
    "Paging_32Bit",
    "Paging_Armv8",
    "Paging_Invalid",
    "Paging_Long",
    "Paging_NonPaged",
    "Paging_Pae",
    "ProcessorVendor_Amd",
    "ProcessorVendor_Arm",
    "ProcessorVendor_Hygon",
    "ProcessorVendor_Intel",
    "ProcessorVendor_Unknown",
    "REGISTER_ID",
    "ReadGuestPhysicalAddress",
    "ReadGuestRawSavedMemory",
    "ReadSavedStateGlobalVariable",
    "ReleaseSavedStateFiles",
    "ReleaseSavedStateSymbolProvider",
    "ResolveSavedStateGlobalVariableAddress",
    "SOCKADDR_HV",
    "ScanMemoryForDosImages",
    "SetMemoryBlockCacheLimit",
    "SetSavedStateSymbolProviderDebugInfoCallback",
    "VIRTUAL_PROCESSOR_ARCH",
    "VIRTUAL_PROCESSOR_REGISTER",
    "VIRTUAL_PROCESSOR_VENDOR",
    "VM_GENCOUNTER",
    "VM_GENCOUNTER_SYMBOLIC_LINK_NAME",
    "WHV_ACCESS_GPA_CONTROLS",
    "WHV_ADVISE_GPA_RANGE",
    "WHV_ADVISE_GPA_RANGE_CODE",
    "WHV_ADVISE_GPA_RANGE_CODE_WHvAdviseGpaRangeCodePin",
    "WHV_ADVISE_GPA_RANGE_CODE_WHvAdviseGpaRangeCodePopulate",
    "WHV_ADVISE_GPA_RANGE_CODE_WHvAdviseGpaRangeCodeUnpin",
    "WHV_ADVISE_GPA_RANGE_POPULATE",
    "WHV_ADVISE_GPA_RANGE_POPULATE_FLAGS",
    "WHV_ALLOCATE_VPCI_RESOURCE_FLAGS",
    "WHV_ALLOCATE_VPCI_RESOURCE_FLAGS_WHvAllocateVpciResourceFlagAllowDirectP2P",
    "WHV_ALLOCATE_VPCI_RESOURCE_FLAGS_WHvAllocateVpciResourceFlagNone",
    "WHV_ANY_VP",
    "WHV_CACHE_TYPE",
    "WHV_CACHE_TYPE_WHvCacheTypeUncached",
    "WHV_CACHE_TYPE_WHvCacheTypeWriteBack",
    "WHV_CACHE_TYPE_WHvCacheTypeWriteCombining",
    "WHV_CACHE_TYPE_WHvCacheTypeWriteThrough",
    "WHV_CAPABILITY",
    "WHV_CAPABILITY_CODE",
    "WHV_CAPABILITY_CODE_WHvCapabilityCodeExceptionExitBitmap",
    "WHV_CAPABILITY_CODE_WHvCapabilityCodeExtendedVmExits",
    "WHV_CAPABILITY_CODE_WHvCapabilityCodeFeatures",
    "WHV_CAPABILITY_CODE_WHvCapabilityCodeGpaRangePopulateFlags",
    "WHV_CAPABILITY_CODE_WHvCapabilityCodeHypervisorPresent",
    "WHV_CAPABILITY_CODE_WHvCapabilityCodeInterruptClockFrequency",
    "WHV_CAPABILITY_CODE_WHvCapabilityCodeProcessorClFlushSize",
    "WHV_CAPABILITY_CODE_WHvCapabilityCodeProcessorClockFrequency",
    "WHV_CAPABILITY_CODE_WHvCapabilityCodeProcessorFeatures",
    "WHV_CAPABILITY_CODE_WHvCapabilityCodeProcessorFeaturesBanks",
    "WHV_CAPABILITY_CODE_WHvCapabilityCodeProcessorFrequencyCap",
    "WHV_CAPABILITY_CODE_WHvCapabilityCodeProcessorPerfmonFeatures",
    "WHV_CAPABILITY_CODE_WHvCapabilityCodeProcessorVendor",
    "WHV_CAPABILITY_CODE_WHvCapabilityCodeProcessorXsaveFeatures",
    "WHV_CAPABILITY_CODE_WHvCapabilityCodeSchedulerFeatures",
    "WHV_CAPABILITY_CODE_WHvCapabilityCodeSyntheticProcessorFeaturesBanks",
    "WHV_CAPABILITY_CODE_WHvCapabilityCodeX64MsrExitBitmap",
    "WHV_CAPABILITY_FEATURES",
    "WHV_CAPABILITY_PROCESSOR_FREQUENCY_CAP",
    "WHV_CPUID_OUTPUT",
    "WHV_CREATE_VPCI_DEVICE_FLAGS",
    "WHV_CREATE_VPCI_DEVICE_FLAGS_WHvCreateVpciDeviceFlagNone",
    "WHV_CREATE_VPCI_DEVICE_FLAGS_WHvCreateVpciDeviceFlagPhysicallyBacked",
    "WHV_CREATE_VPCI_DEVICE_FLAGS_WHvCreateVpciDeviceFlagUseLogicalInterrupts",
    "WHV_DOORBELL_MATCH_DATA",
    "WHV_EMULATOR_CALLBACKS",
    "WHV_EMULATOR_GET_VIRTUAL_PROCESSOR_REGISTERS_CALLBACK",
    "WHV_EMULATOR_IO_ACCESS_INFO",
    "WHV_EMULATOR_IO_PORT_CALLBACK",
    "WHV_EMULATOR_MEMORY_ACCESS_INFO",
    "WHV_EMULATOR_MEMORY_CALLBACK",
    "WHV_EMULATOR_SET_VIRTUAL_PROCESSOR_REGISTERS_CALLBACK",
    "WHV_EMULATOR_STATUS",
    "WHV_EMULATOR_TRANSLATE_GVA_PAGE_CALLBACK",
    "WHV_EXCEPTION_TYPE",
    "WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeAlignmentCheckFault",
    "WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeBoundRangeFault",
    "WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeBreakpointTrap",
    "WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeDebugTrapOrFault",
    "WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeDeviceNotAvailableFault",
    "WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeDivideErrorFault",
    "WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeDoubleFaultAbort",
    "WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeFloatingPointErrorFault",
    "WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeGeneralProtectionFault",
    "WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeInvalidOpcodeFault",
    "WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeInvalidTaskStateSegmentFault",
    "WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeMachineCheckAbort",
    "WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeOverflowTrap",
    "WHV_EXCEPTION_TYPE_WHvX64ExceptionTypePageFault",
    "WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeSegmentNotPresentFault",
    "WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeSimdFloatingPointFault",
    "WHV_EXCEPTION_TYPE_WHvX64ExceptionTypeStackFault",
    "WHV_EXTENDED_VM_EXITS",
    "WHV_HYPERCALL_CONTEXT",
    "WHV_HYPERCALL_CONTEXT_MAX_XMM_REGISTERS",
    "WHV_INTERNAL_ACTIVITY_REGISTER",
    "WHV_INTERRUPT_CONTROL",
    "WHV_INTERRUPT_DESTINATION_MODE",
    "WHV_INTERRUPT_DESTINATION_MODE_WHvX64InterruptDestinationModeLogical",
    "WHV_INTERRUPT_DESTINATION_MODE_WHvX64InterruptDestinationModePhysical",
    "WHV_INTERRUPT_TRIGGER_MODE",
    "WHV_INTERRUPT_TRIGGER_MODE_WHvX64InterruptTriggerModeEdge",
    "WHV_INTERRUPT_TRIGGER_MODE_WHvX64InterruptTriggerModeLevel",
    "WHV_INTERRUPT_TYPE",
    "WHV_INTERRUPT_TYPE_WHvX64InterruptTypeFixed",
    "WHV_INTERRUPT_TYPE_WHvX64InterruptTypeInit",
    "WHV_INTERRUPT_TYPE_WHvX64InterruptTypeLocalInt1",
    "WHV_INTERRUPT_TYPE_WHvX64InterruptTypeLowestPriority",
    "WHV_INTERRUPT_TYPE_WHvX64InterruptTypeNmi",
    "WHV_INTERRUPT_TYPE_WHvX64InterruptTypeSipi",
    "WHV_MAP_GPA_RANGE_FLAGS",
    "WHV_MAP_GPA_RANGE_FLAGS_WHvMapGpaRangeFlagExecute",
    "WHV_MAP_GPA_RANGE_FLAGS_WHvMapGpaRangeFlagNone",
    "WHV_MAP_GPA_RANGE_FLAGS_WHvMapGpaRangeFlagRead",
    "WHV_MAP_GPA_RANGE_FLAGS_WHvMapGpaRangeFlagTrackDirtyPages",
    "WHV_MAP_GPA_RANGE_FLAGS_WHvMapGpaRangeFlagWrite",
    "WHV_MAX_DEVICE_ID_SIZE_IN_CHARS",
    "WHV_MEMORY_ACCESS_CONTEXT",
    "WHV_MEMORY_ACCESS_INFO",
    "WHV_MEMORY_ACCESS_TYPE",
    "WHV_MEMORY_ACCESS_TYPE_WHvMemoryAccessExecute",
    "WHV_MEMORY_ACCESS_TYPE_WHvMemoryAccessRead",
    "WHV_MEMORY_ACCESS_TYPE_WHvMemoryAccessWrite",
    "WHV_MEMORY_RANGE_ENTRY",
    "WHV_MSR_ACTION",
    "WHV_MSR_ACTION_ENTRY",
    "WHV_MSR_ACTION_WHvMsrActionArchitectureDefault",
    "WHV_MSR_ACTION_WHvMsrActionExit",
    "WHV_MSR_ACTION_WHvMsrActionIgnoreWriteReadZero",
    "WHV_NOTIFICATION_PORT_PARAMETERS",
    "WHV_NOTIFICATION_PORT_PROPERTY_CODE",
    "WHV_NOTIFICATION_PORT_PROPERTY_CODE_WHvNotificationPortPropertyPreferredTargetDuration",
    "WHV_NOTIFICATION_PORT_PROPERTY_CODE_WHvNotificationPortPropertyPreferredTargetVp",
    "WHV_NOTIFICATION_PORT_TYPE",
    "WHV_NOTIFICATION_PORT_TYPE_WHvNotificationPortTypeDoorbell",
    "WHV_NOTIFICATION_PORT_TYPE_WHvNotificationPortTypeEvent",
    "WHV_PARTITION_COUNTER_SET",
    "WHV_PARTITION_COUNTER_SET_WHvPartitionCounterSetMemory",
    "WHV_PARTITION_HANDLE",
    "WHV_PARTITION_MEMORY_COUNTERS",
    "WHV_PARTITION_PROPERTY",
    "WHV_PARTITION_PROPERTY_CODE",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeAllowDeviceAssignment",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeApicRemoteReadSupport",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeCpuCap",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeCpuGroupId",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeCpuReserve",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeCpuWeight",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeCpuidExitList",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeCpuidResultList",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeCpuidResultList2",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeDisableSmt",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeExceptionExitBitmap",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeExtendedVmExits",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeInterruptClockFrequency",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeLocalApicEmulationMode",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeMsrActionList",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeNestedVirtualization",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodePrimaryNumaNode",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeProcessorClFlushSize",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeProcessorClockFrequency",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeProcessorCount",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeProcessorFeatures",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeProcessorFeaturesBanks",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeProcessorFrequencyCap",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeProcessorPerfmonFeatures",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeProcessorXsaveFeatures",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeReferenceTime",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeSeparateSecurityDomain",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeSyntheticProcessorFeaturesBanks",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeUnimplementedMsrAction",
    "WHV_PARTITION_PROPERTY_CODE_WHvPartitionPropertyCodeX64MsrExitBitmap",
    "WHV_PROCESSOR_APIC_COUNTERS",
    "WHV_PROCESSOR_COUNTER_SET",
    "WHV_PROCESSOR_COUNTER_SET_WHvProcessorCounterSetApic",
    "WHV_PROCESSOR_COUNTER_SET_WHvProcessorCounterSetEvents",
    "WHV_PROCESSOR_COUNTER_SET_WHvProcessorCounterSetIntercepts",
    "WHV_PROCESSOR_COUNTER_SET_WHvProcessorCounterSetRuntime",
    "WHV_PROCESSOR_COUNTER_SET_WHvProcessorCounterSetSyntheticFeatures",
    "WHV_PROCESSOR_EVENT_COUNTERS",
    "WHV_PROCESSOR_FEATURES",
    "WHV_PROCESSOR_FEATURES1",
    "WHV_PROCESSOR_FEATURES_BANKS",
    "WHV_PROCESSOR_FEATURES_BANKS_COUNT",
    "WHV_PROCESSOR_INTERCEPT_COUNTER",
    "WHV_PROCESSOR_INTERCEPT_COUNTERS",
    "WHV_PROCESSOR_PERFMON_FEATURES",
    "WHV_PROCESSOR_RUNTIME_COUNTERS",
    "WHV_PROCESSOR_SYNTHETIC_FEATURES_COUNTERS",
    "WHV_PROCESSOR_VENDOR",
    "WHV_PROCESSOR_VENDOR_WHvProcessorVendorAmd",
    "WHV_PROCESSOR_VENDOR_WHvProcessorVendorHygon",
    "WHV_PROCESSOR_VENDOR_WHvProcessorVendorIntel",
    "WHV_PROCESSOR_XSAVE_FEATURES",
    "WHV_READ_WRITE_GPA_RANGE_MAX_SIZE",
    "WHV_REGISTER_NAME",
    "WHV_REGISTER_NAME_WHvRegisterEom",
    "WHV_REGISTER_NAME_WHvRegisterGuestOsId",
    "WHV_REGISTER_NAME_WHvRegisterInternalActivityState",
    "WHV_REGISTER_NAME_WHvRegisterInterruptState",
    "WHV_REGISTER_NAME_WHvRegisterPendingEvent",
    "WHV_REGISTER_NAME_WHvRegisterPendingInterruption",
    "WHV_REGISTER_NAME_WHvRegisterReferenceTsc",
    "WHV_REGISTER_NAME_WHvRegisterReferenceTscSequence",
    "WHV_REGISTER_NAME_WHvRegisterScontrol",
    "WHV_REGISTER_NAME_WHvRegisterSiefp",
    "WHV_REGISTER_NAME_WHvRegisterSimp",
    "WHV_REGISTER_NAME_WHvRegisterSint0",
    "WHV_REGISTER_NAME_WHvRegisterSint1",
    "WHV_REGISTER_NAME_WHvRegisterSint10",
    "WHV_REGISTER_NAME_WHvRegisterSint11",
    "WHV_REGISTER_NAME_WHvRegisterSint12",
    "WHV_REGISTER_NAME_WHvRegisterSint13",
    "WHV_REGISTER_NAME_WHvRegisterSint14",
    "WHV_REGISTER_NAME_WHvRegisterSint15",
    "WHV_REGISTER_NAME_WHvRegisterSint2",
    "WHV_REGISTER_NAME_WHvRegisterSint3",
    "WHV_REGISTER_NAME_WHvRegisterSint4",
    "WHV_REGISTER_NAME_WHvRegisterSint5",
    "WHV_REGISTER_NAME_WHvRegisterSint6",
    "WHV_REGISTER_NAME_WHvRegisterSint7",
    "WHV_REGISTER_NAME_WHvRegisterSint8",
    "WHV_REGISTER_NAME_WHvRegisterSint9",
    "WHV_REGISTER_NAME_WHvRegisterSversion",
    "WHV_REGISTER_NAME_WHvRegisterVpAssistPage",
    "WHV_REGISTER_NAME_WHvRegisterVpRuntime",
    "WHV_REGISTER_NAME_WHvX64RegisterACount",
    "WHV_REGISTER_NAME_WHvX64RegisterApicBase",
    "WHV_REGISTER_NAME_WHvX64RegisterApicCurrentCount",
    "WHV_REGISTER_NAME_WHvX64RegisterApicDivide",
    "WHV_REGISTER_NAME_WHvX64RegisterApicEoi",
    "WHV_REGISTER_NAME_WHvX64RegisterApicEse",
    "WHV_REGISTER_NAME_WHvX64RegisterApicIcr",
    "WHV_REGISTER_NAME_WHvX64RegisterApicId",
    "WHV_REGISTER_NAME_WHvX64RegisterApicInitCount",
    "WHV_REGISTER_NAME_WHvX64RegisterApicIrr0",
    "WHV_REGISTER_NAME_WHvX64RegisterApicIrr1",
    "WHV_REGISTER_NAME_WHvX64RegisterApicIrr2",
    "WHV_REGISTER_NAME_WHvX64RegisterApicIrr3",
    "WHV_REGISTER_NAME_WHvX64RegisterApicIrr4",
    "WHV_REGISTER_NAME_WHvX64RegisterApicIrr5",
    "WHV_REGISTER_NAME_WHvX64RegisterApicIrr6",
    "WHV_REGISTER_NAME_WHvX64RegisterApicIrr7",
    "WHV_REGISTER_NAME_WHvX64RegisterApicIsr0",
    "WHV_REGISTER_NAME_WHvX64RegisterApicIsr1",
    "WHV_REGISTER_NAME_WHvX64RegisterApicIsr2",
    "WHV_REGISTER_NAME_WHvX64RegisterApicIsr3",
    "WHV_REGISTER_NAME_WHvX64RegisterApicIsr4",
    "WHV_REGISTER_NAME_WHvX64RegisterApicIsr5",
    "WHV_REGISTER_NAME_WHvX64RegisterApicIsr6",
    "WHV_REGISTER_NAME_WHvX64RegisterApicIsr7",
    "WHV_REGISTER_NAME_WHvX64RegisterApicLdr",
    "WHV_REGISTER_NAME_WHvX64RegisterApicLvtError",
    "WHV_REGISTER_NAME_WHvX64RegisterApicLvtLint0",
    "WHV_REGISTER_NAME_WHvX64RegisterApicLvtLint1",
    "WHV_REGISTER_NAME_WHvX64RegisterApicLvtPerfmon",
    "WHV_REGISTER_NAME_WHvX64RegisterApicLvtThermal",
    "WHV_REGISTER_NAME_WHvX64RegisterApicLvtTimer",
    "WHV_REGISTER_NAME_WHvX64RegisterApicPpr",
    "WHV_REGISTER_NAME_WHvX64RegisterApicSelfIpi",
    "WHV_REGISTER_NAME_WHvX64RegisterApicSpurious",
    "WHV_REGISTER_NAME_WHvX64RegisterApicTmr0",
    "WHV_REGISTER_NAME_WHvX64RegisterApicTmr1",
    "WHV_REGISTER_NAME_WHvX64RegisterApicTmr2",
    "WHV_REGISTER_NAME_WHvX64RegisterApicTmr3",
    "WHV_REGISTER_NAME_WHvX64RegisterApicTmr4",
    "WHV_REGISTER_NAME_WHvX64RegisterApicTmr5",
    "WHV_REGISTER_NAME_WHvX64RegisterApicTmr6",
    "WHV_REGISTER_NAME_WHvX64RegisterApicTmr7",
    "WHV_REGISTER_NAME_WHvX64RegisterApicTpr",
    "WHV_REGISTER_NAME_WHvX64RegisterApicVersion",
    "WHV_REGISTER_NAME_WHvX64RegisterBndcfgs",
    "WHV_REGISTER_NAME_WHvX64RegisterCr0",
    "WHV_REGISTER_NAME_WHvX64RegisterCr2",
    "WHV_REGISTER_NAME_WHvX64RegisterCr3",
    "WHV_REGISTER_NAME_WHvX64RegisterCr4",
    "WHV_REGISTER_NAME_WHvX64RegisterCr8",
    "WHV_REGISTER_NAME_WHvX64RegisterCs",
    "WHV_REGISTER_NAME_WHvX64RegisterCstar",
    "WHV_REGISTER_NAME_WHvX64RegisterDeliverabilityNotifications",
    "WHV_REGISTER_NAME_WHvX64RegisterDr0",
    "WHV_REGISTER_NAME_WHvX64RegisterDr1",
    "WHV_REGISTER_NAME_WHvX64RegisterDr2",
    "WHV_REGISTER_NAME_WHvX64RegisterDr3",
    "WHV_REGISTER_NAME_WHvX64RegisterDr6",
    "WHV_REGISTER_NAME_WHvX64RegisterDr7",
    "WHV_REGISTER_NAME_WHvX64RegisterDs",
    "WHV_REGISTER_NAME_WHvX64RegisterEfer",
    "WHV_REGISTER_NAME_WHvX64RegisterEs",
    "WHV_REGISTER_NAME_WHvX64RegisterFpControlStatus",
    "WHV_REGISTER_NAME_WHvX64RegisterFpMmx0",
    "WHV_REGISTER_NAME_WHvX64RegisterFpMmx1",
    "WHV_REGISTER_NAME_WHvX64RegisterFpMmx2",
    "WHV_REGISTER_NAME_WHvX64RegisterFpMmx3",
    "WHV_REGISTER_NAME_WHvX64RegisterFpMmx4",
    "WHV_REGISTER_NAME_WHvX64RegisterFpMmx5",
    "WHV_REGISTER_NAME_WHvX64RegisterFpMmx6",
    "WHV_REGISTER_NAME_WHvX64RegisterFpMmx7",
    "WHV_REGISTER_NAME_WHvX64RegisterFs",
    "WHV_REGISTER_NAME_WHvX64RegisterGdtr",
    "WHV_REGISTER_NAME_WHvX64RegisterGs",
    "WHV_REGISTER_NAME_WHvX64RegisterHypercall",
    "WHV_REGISTER_NAME_WHvX64RegisterIdtr",
    "WHV_REGISTER_NAME_WHvX64RegisterInitialApicId",
    "WHV_REGISTER_NAME_WHvX64RegisterInterruptSspTableAddr",
    "WHV_REGISTER_NAME_WHvX64RegisterKernelGsBase",
    "WHV_REGISTER_NAME_WHvX64RegisterLdtr",
    "WHV_REGISTER_NAME_WHvX64RegisterLstar",
    "WHV_REGISTER_NAME_WHvX64RegisterMCount",
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrCap",
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrDefType",
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
    "WHV_REGISTER_NAME_WHvX64RegisterMsrMtrrFix64k00000",
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
    "WHV_REGISTER_NAME_WHvX64RegisterPat",
    "WHV_REGISTER_NAME_WHvX64RegisterPendingDebugException",
    "WHV_REGISTER_NAME_WHvX64RegisterPl0Ssp",
    "WHV_REGISTER_NAME_WHvX64RegisterPl1Ssp",
    "WHV_REGISTER_NAME_WHvX64RegisterPl2Ssp",
    "WHV_REGISTER_NAME_WHvX64RegisterPl3Ssp",
    "WHV_REGISTER_NAME_WHvX64RegisterPredCmd",
    "WHV_REGISTER_NAME_WHvX64RegisterR10",
    "WHV_REGISTER_NAME_WHvX64RegisterR11",
    "WHV_REGISTER_NAME_WHvX64RegisterR12",
    "WHV_REGISTER_NAME_WHvX64RegisterR13",
    "WHV_REGISTER_NAME_WHvX64RegisterR14",
    "WHV_REGISTER_NAME_WHvX64RegisterR15",
    "WHV_REGISTER_NAME_WHvX64RegisterR8",
    "WHV_REGISTER_NAME_WHvX64RegisterR9",
    "WHV_REGISTER_NAME_WHvX64RegisterRax",
    "WHV_REGISTER_NAME_WHvX64RegisterRbp",
    "WHV_REGISTER_NAME_WHvX64RegisterRbx",
    "WHV_REGISTER_NAME_WHvX64RegisterRcx",
    "WHV_REGISTER_NAME_WHvX64RegisterRdi",
    "WHV_REGISTER_NAME_WHvX64RegisterRdx",
    "WHV_REGISTER_NAME_WHvX64RegisterRflags",
    "WHV_REGISTER_NAME_WHvX64RegisterRip",
    "WHV_REGISTER_NAME_WHvX64RegisterRsi",
    "WHV_REGISTER_NAME_WHvX64RegisterRsp",
    "WHV_REGISTER_NAME_WHvX64RegisterSCet",
    "WHV_REGISTER_NAME_WHvX64RegisterSfmask",
    "WHV_REGISTER_NAME_WHvX64RegisterSpecCtrl",
    "WHV_REGISTER_NAME_WHvX64RegisterSs",
    "WHV_REGISTER_NAME_WHvX64RegisterSsp",
    "WHV_REGISTER_NAME_WHvX64RegisterStar",
    "WHV_REGISTER_NAME_WHvX64RegisterSysenterCs",
    "WHV_REGISTER_NAME_WHvX64RegisterSysenterEip",
    "WHV_REGISTER_NAME_WHvX64RegisterSysenterEsp",
    "WHV_REGISTER_NAME_WHvX64RegisterTr",
    "WHV_REGISTER_NAME_WHvX64RegisterTsc",
    "WHV_REGISTER_NAME_WHvX64RegisterTscAdjust",
    "WHV_REGISTER_NAME_WHvX64RegisterTscAux",
    "WHV_REGISTER_NAME_WHvX64RegisterTscDeadline",
    "WHV_REGISTER_NAME_WHvX64RegisterTscVirtualOffset",
    "WHV_REGISTER_NAME_WHvX64RegisterTsxCtrl",
    "WHV_REGISTER_NAME_WHvX64RegisterUCet",
    "WHV_REGISTER_NAME_WHvX64RegisterUmwaitControl",
    "WHV_REGISTER_NAME_WHvX64RegisterVirtualCr0",
    "WHV_REGISTER_NAME_WHvX64RegisterVirtualCr3",
    "WHV_REGISTER_NAME_WHvX64RegisterVirtualCr4",
    "WHV_REGISTER_NAME_WHvX64RegisterVirtualCr8",
    "WHV_REGISTER_NAME_WHvX64RegisterXCr0",
    "WHV_REGISTER_NAME_WHvX64RegisterXfd",
    "WHV_REGISTER_NAME_WHvX64RegisterXfdErr",
    "WHV_REGISTER_NAME_WHvX64RegisterXmm0",
    "WHV_REGISTER_NAME_WHvX64RegisterXmm1",
    "WHV_REGISTER_NAME_WHvX64RegisterXmm10",
    "WHV_REGISTER_NAME_WHvX64RegisterXmm11",
    "WHV_REGISTER_NAME_WHvX64RegisterXmm12",
    "WHV_REGISTER_NAME_WHvX64RegisterXmm13",
    "WHV_REGISTER_NAME_WHvX64RegisterXmm14",
    "WHV_REGISTER_NAME_WHvX64RegisterXmm15",
    "WHV_REGISTER_NAME_WHvX64RegisterXmm2",
    "WHV_REGISTER_NAME_WHvX64RegisterXmm3",
    "WHV_REGISTER_NAME_WHvX64RegisterXmm4",
    "WHV_REGISTER_NAME_WHvX64RegisterXmm5",
    "WHV_REGISTER_NAME_WHvX64RegisterXmm6",
    "WHV_REGISTER_NAME_WHvX64RegisterXmm7",
    "WHV_REGISTER_NAME_WHvX64RegisterXmm8",
    "WHV_REGISTER_NAME_WHvX64RegisterXmm9",
    "WHV_REGISTER_NAME_WHvX64RegisterXmmControlStatus",
    "WHV_REGISTER_NAME_WHvX64RegisterXss",
    "WHV_REGISTER_VALUE",
    "WHV_RUN_VP_CANCELED_CONTEXT",
    "WHV_RUN_VP_CANCEL_REASON",
    "WHV_RUN_VP_CANCEL_REASON_WHvRunVpCancelReasonUser",
    "WHV_RUN_VP_EXIT_CONTEXT",
    "WHV_RUN_VP_EXIT_REASON",
    "WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonCanceled",
    "WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonException",
    "WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonHypercall",
    "WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonInvalidVpRegisterValue",
    "WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonMemoryAccess",
    "WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonNone",
    "WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonSynicSintDeliverable",
    "WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonUnrecoverableException",
    "WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonUnsupportedFeature",
    "WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64ApicEoi",
    "WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64ApicInitSipiTrap",
    "WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64ApicSmiTrap",
    "WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64ApicWriteTrap",
    "WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64Cpuid",
    "WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64Halt",
    "WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64InterruptWindow",
    "WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64IoPortAccess",
    "WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64MsrAccess",
    "WHV_RUN_VP_EXIT_REASON_WHvRunVpExitReasonX64Rdtsc",
    "WHV_SCHEDULER_FEATURES",
    "WHV_SRIOV_RESOURCE_DESCRIPTOR",
    "WHV_SYNIC_EVENT_PARAMETERS",
    "WHV_SYNIC_MESSAGE_SIZE",
    "WHV_SYNIC_SINT_DELIVERABLE_CONTEXT",
    "WHV_SYNTHETIC_PROCESSOR_FEATURES",
    "WHV_SYNTHETIC_PROCESSOR_FEATURES_BANKS",
    "WHV_SYNTHETIC_PROCESSOR_FEATURES_BANKS_COUNT",
    "WHV_TRANSLATE_GVA_FLAGS",
    "WHV_TRANSLATE_GVA_FLAGS_WHvTranslateGvaFlagEnforceSmap",
    "WHV_TRANSLATE_GVA_FLAGS_WHvTranslateGvaFlagNone",
    "WHV_TRANSLATE_GVA_FLAGS_WHvTranslateGvaFlagOverrideSmap",
    "WHV_TRANSLATE_GVA_FLAGS_WHvTranslateGvaFlagPrivilegeExempt",
    "WHV_TRANSLATE_GVA_FLAGS_WHvTranslateGvaFlagSetPageTableBits",
    "WHV_TRANSLATE_GVA_FLAGS_WHvTranslateGvaFlagValidateExecute",
    "WHV_TRANSLATE_GVA_FLAGS_WHvTranslateGvaFlagValidateRead",
    "WHV_TRANSLATE_GVA_FLAGS_WHvTranslateGvaFlagValidateWrite",
    "WHV_TRANSLATE_GVA_RESULT",
    "WHV_TRANSLATE_GVA_RESULT_CODE",
    "WHV_TRANSLATE_GVA_RESULT_CODE_WHvTranslateGvaResultGpaIllegalOverlayAccess",
    "WHV_TRANSLATE_GVA_RESULT_CODE_WHvTranslateGvaResultGpaNoReadAccess",
    "WHV_TRANSLATE_GVA_RESULT_CODE_WHvTranslateGvaResultGpaNoWriteAccess",
    "WHV_TRANSLATE_GVA_RESULT_CODE_WHvTranslateGvaResultGpaUnmapped",
    "WHV_TRANSLATE_GVA_RESULT_CODE_WHvTranslateGvaResultIntercept",
    "WHV_TRANSLATE_GVA_RESULT_CODE_WHvTranslateGvaResultInvalidPageTableFlags",
    "WHV_TRANSLATE_GVA_RESULT_CODE_WHvTranslateGvaResultPageNotPresent",
    "WHV_TRANSLATE_GVA_RESULT_CODE_WHvTranslateGvaResultPrivilegeViolation",
    "WHV_TRANSLATE_GVA_RESULT_CODE_WHvTranslateGvaResultSuccess",
    "WHV_TRIGGER_PARAMETERS",
    "WHV_TRIGGER_TYPE",
    "WHV_TRIGGER_TYPE_WHvTriggerTypeDeviceInterrupt",
    "WHV_TRIGGER_TYPE_WHvTriggerTypeInterrupt",
    "WHV_TRIGGER_TYPE_WHvTriggerTypeSynicEvent",
    "WHV_UINT128",
    "WHV_VIRTUAL_PROCESSOR_PROPERTY",
    "WHV_VIRTUAL_PROCESSOR_PROPERTY_CODE",
    "WHV_VIRTUAL_PROCESSOR_PROPERTY_CODE_WHvVirtualProcessorPropertyCodeNumaNode",
    "WHV_VIRTUAL_PROCESSOR_STATE_TYPE",
    "WHV_VIRTUAL_PROCESSOR_STATE_TYPE_WHvVirtualProcessorStateTypeInterruptControllerState2",
    "WHV_VIRTUAL_PROCESSOR_STATE_TYPE_WHvVirtualProcessorStateTypeSynicEventFlagPage",
    "WHV_VIRTUAL_PROCESSOR_STATE_TYPE_WHvVirtualProcessorStateTypeSynicMessagePage",
    "WHV_VIRTUAL_PROCESSOR_STATE_TYPE_WHvVirtualProcessorStateTypeSynicTimerState",
    "WHV_VIRTUAL_PROCESSOR_STATE_TYPE_WHvVirtualProcessorStateTypeXsaveState",
    "WHV_VPCI_DEVICE_NOTIFICATION",
    "WHV_VPCI_DEVICE_NOTIFICATION_TYPE",
    "WHV_VPCI_DEVICE_NOTIFICATION_TYPE_WHvVpciDeviceNotificationMmioRemapping",
    "WHV_VPCI_DEVICE_NOTIFICATION_TYPE_WHvVpciDeviceNotificationSurpriseRemoval",
    "WHV_VPCI_DEVICE_NOTIFICATION_TYPE_WHvVpciDeviceNotificationUndefined",
    "WHV_VPCI_DEVICE_PROPERTY_CODE",
    "WHV_VPCI_DEVICE_PROPERTY_CODE_WHvVpciDevicePropertyCodeHardwareIDs",
    "WHV_VPCI_DEVICE_PROPERTY_CODE_WHvVpciDevicePropertyCodeProbedBARs",
    "WHV_VPCI_DEVICE_PROPERTY_CODE_WHvVpciDevicePropertyCodeUndefined",
    "WHV_VPCI_DEVICE_REGISTER",
    "WHV_VPCI_DEVICE_REGISTER_SPACE",
    "WHV_VPCI_DEVICE_REGISTER_SPACE_WHvVpciBar0",
    "WHV_VPCI_DEVICE_REGISTER_SPACE_WHvVpciBar1",
    "WHV_VPCI_DEVICE_REGISTER_SPACE_WHvVpciBar2",
    "WHV_VPCI_DEVICE_REGISTER_SPACE_WHvVpciBar3",
    "WHV_VPCI_DEVICE_REGISTER_SPACE_WHvVpciBar4",
    "WHV_VPCI_DEVICE_REGISTER_SPACE_WHvVpciBar5",
    "WHV_VPCI_DEVICE_REGISTER_SPACE_WHvVpciConfigSpace",
    "WHV_VPCI_HARDWARE_IDS",
    "WHV_VPCI_INTERRUPT_TARGET",
    "WHV_VPCI_INTERRUPT_TARGET_FLAGS",
    "WHV_VPCI_INTERRUPT_TARGET_FLAGS_WHvVpciInterruptTargetFlagMulticast",
    "WHV_VPCI_INTERRUPT_TARGET_FLAGS_WHvVpciInterruptTargetFlagNone",
    "WHV_VPCI_MMIO_MAPPING",
    "WHV_VPCI_MMIO_RANGE_FLAGS",
    "WHV_VPCI_MMIO_RANGE_FLAGS_WHvVpciMmioRangeFlagReadAccess",
    "WHV_VPCI_MMIO_RANGE_FLAGS_WHvVpciMmioRangeFlagWriteAccess",
    "WHV_VPCI_PROBED_BARS",
    "WHV_VPCI_TYPE0_BAR_COUNT",
    "WHV_VP_EXCEPTION_CONTEXT",
    "WHV_VP_EXCEPTION_INFO",
    "WHV_VP_EXIT_CONTEXT",
    "WHV_X64_APIC_EOI_CONTEXT",
    "WHV_X64_APIC_INIT_SIPI_CONTEXT",
    "WHV_X64_APIC_SMI_CONTEXT",
    "WHV_X64_APIC_WRITE_CONTEXT",
    "WHV_X64_APIC_WRITE_TYPE",
    "WHV_X64_APIC_WRITE_TYPE_WHvX64ApicWriteTypeDfr",
    "WHV_X64_APIC_WRITE_TYPE_WHvX64ApicWriteTypeLdr",
    "WHV_X64_APIC_WRITE_TYPE_WHvX64ApicWriteTypeLint0",
    "WHV_X64_APIC_WRITE_TYPE_WHvX64ApicWriteTypeLint1",
    "WHV_X64_APIC_WRITE_TYPE_WHvX64ApicWriteTypeSvr",
    "WHV_X64_CPUID_ACCESS_CONTEXT",
    "WHV_X64_CPUID_RESULT",
    "WHV_X64_CPUID_RESULT2",
    "WHV_X64_CPUID_RESULT2_FLAGS",
    "WHV_X64_CPUID_RESULT2_FLAGS_WHvX64CpuidResult2FlagSubleafSpecific",
    "WHV_X64_CPUID_RESULT2_FLAGS_WHvX64CpuidResult2FlagVpSpecific",
    "WHV_X64_DELIVERABILITY_NOTIFICATIONS_REGISTER",
    "WHV_X64_FP_CONTROL_STATUS_REGISTER",
    "WHV_X64_FP_REGISTER",
    "WHV_X64_INTERRUPTION_DELIVERABLE_CONTEXT",
    "WHV_X64_INTERRUPT_STATE_REGISTER",
    "WHV_X64_IO_PORT_ACCESS_CONTEXT",
    "WHV_X64_IO_PORT_ACCESS_INFO",
    "WHV_X64_LOCAL_APIC_EMULATION_MODE",
    "WHV_X64_LOCAL_APIC_EMULATION_MODE_WHvX64LocalApicEmulationModeNone",
    "WHV_X64_LOCAL_APIC_EMULATION_MODE_WHvX64LocalApicEmulationModeX2Apic",
    "WHV_X64_LOCAL_APIC_EMULATION_MODE_WHvX64LocalApicEmulationModeXApic",
    "WHV_X64_MSR_ACCESS_CONTEXT",
    "WHV_X64_MSR_ACCESS_INFO",
    "WHV_X64_MSR_EXIT_BITMAP",
    "WHV_X64_PENDING_DEBUG_EXCEPTION",
    "WHV_X64_PENDING_EVENT_TYPE",
    "WHV_X64_PENDING_EVENT_TYPE_WHvX64PendingEventException",
    "WHV_X64_PENDING_EVENT_TYPE_WHvX64PendingEventExtInt",
    "WHV_X64_PENDING_EXCEPTION_EVENT",
    "WHV_X64_PENDING_EXT_INT_EVENT",
    "WHV_X64_PENDING_INTERRUPTION_REGISTER",
    "WHV_X64_PENDING_INTERRUPTION_TYPE",
    "WHV_X64_PENDING_INTERRUPTION_TYPE_WHvX64PendingException",
    "WHV_X64_PENDING_INTERRUPTION_TYPE_WHvX64PendingInterrupt",
    "WHV_X64_PENDING_INTERRUPTION_TYPE_WHvX64PendingNmi",
    "WHV_X64_RDTSC_CONTEXT",
    "WHV_X64_RDTSC_INFO",
    "WHV_X64_SEGMENT_REGISTER",
    "WHV_X64_TABLE_REGISTER",
    "WHV_X64_UNSUPPORTED_FEATURE_CODE",
    "WHV_X64_UNSUPPORTED_FEATURE_CODE_WHvUnsupportedFeatureIntercept",
    "WHV_X64_UNSUPPORTED_FEATURE_CODE_WHvUnsupportedFeatureTaskSwitchTss",
    "WHV_X64_UNSUPPORTED_FEATURE_CONTEXT",
    "WHV_X64_VP_EXECUTION_STATE",
    "WHV_X64_XMM_CONTROL_STATUS_REGISTER",
    "WHvAcceptPartitionMigration",
    "WHvAdviseGpaRange",
    "WHvAllocateVpciResource",
    "WHvCancelPartitionMigration",
    "WHvCancelRunVirtualProcessor",
    "WHvCompletePartitionMigration",
    "WHvCreateNotificationPort",
    "WHvCreatePartition",
    "WHvCreateTrigger",
    "WHvCreateVirtualProcessor",
    "WHvCreateVirtualProcessor2",
    "WHvCreateVpciDevice",
    "WHvDeleteNotificationPort",
    "WHvDeletePartition",
    "WHvDeleteTrigger",
    "WHvDeleteVirtualProcessor",
    "WHvDeleteVpciDevice",
    "WHvEmulatorCreateEmulator",
    "WHvEmulatorDestroyEmulator",
    "WHvEmulatorTryIoEmulation",
    "WHvEmulatorTryMmioEmulation",
    "WHvGetCapability",
    "WHvGetInterruptTargetVpSet",
    "WHvGetPartitionCounters",
    "WHvGetPartitionProperty",
    "WHvGetVirtualProcessorCounters",
    "WHvGetVirtualProcessorCpuidOutput",
    "WHvGetVirtualProcessorInterruptControllerState",
    "WHvGetVirtualProcessorInterruptControllerState2",
    "WHvGetVirtualProcessorRegisters",
    "WHvGetVirtualProcessorState",
    "WHvGetVirtualProcessorXsaveState",
    "WHvGetVpciDeviceInterruptTarget",
    "WHvGetVpciDeviceNotification",
    "WHvGetVpciDeviceProperty",
    "WHvMapGpaRange",
    "WHvMapGpaRange2",
    "WHvMapVpciDeviceInterrupt",
    "WHvMapVpciDeviceMmioRanges",
    "WHvPostVirtualProcessorSynicMessage",
    "WHvQueryGpaRangeDirtyBitmap",
    "WHvReadGpaRange",
    "WHvReadVpciDeviceRegister",
    "WHvRegisterPartitionDoorbellEvent",
    "WHvRequestInterrupt",
    "WHvRequestVpciDeviceInterrupt",
    "WHvResetPartition",
    "WHvResumePartitionTime",
    "WHvRetargetVpciDeviceInterrupt",
    "WHvRunVirtualProcessor",
    "WHvSetNotificationPortProperty",
    "WHvSetPartitionProperty",
    "WHvSetVirtualProcessorInterruptControllerState",
    "WHvSetVirtualProcessorInterruptControllerState2",
    "WHvSetVirtualProcessorRegisters",
    "WHvSetVirtualProcessorState",
    "WHvSetVirtualProcessorXsaveState",
    "WHvSetVpciDevicePowerState",
    "WHvSetupPartition",
    "WHvSignalVirtualProcessorSynicEvent",
    "WHvStartPartitionMigration",
    "WHvSuspendPartitionTime",
    "WHvTranslateGva",
    "WHvUnmapGpaRange",
    "WHvUnmapVpciDeviceInterrupt",
    "WHvUnmapVpciDeviceMmioRanges",
    "WHvUnregisterPartitionDoorbellEvent",
    "WHvUpdateTriggerParameters",
    "WHvWriteGpaRange",
    "WHvWriteVpciDeviceRegister",
    "X64_RegisterCr0",
    "X64_RegisterCr2",
    "X64_RegisterCr3",
    "X64_RegisterCr4",
    "X64_RegisterCr8",
    "X64_RegisterCs",
    "X64_RegisterDr0",
    "X64_RegisterDr1",
    "X64_RegisterDr2",
    "X64_RegisterDr3",
    "X64_RegisterDr6",
    "X64_RegisterDr7",
    "X64_RegisterDs",
    "X64_RegisterEfer",
    "X64_RegisterEs",
    "X64_RegisterFpControlStatus",
    "X64_RegisterFpMmx0",
    "X64_RegisterFpMmx1",
    "X64_RegisterFpMmx2",
    "X64_RegisterFpMmx3",
    "X64_RegisterFpMmx4",
    "X64_RegisterFpMmx5",
    "X64_RegisterFpMmx6",
    "X64_RegisterFpMmx7",
    "X64_RegisterFs",
    "X64_RegisterGdtr",
    "X64_RegisterGs",
    "X64_RegisterIdtr",
    "X64_RegisterLdtr",
    "X64_RegisterMax",
    "X64_RegisterR10",
    "X64_RegisterR11",
    "X64_RegisterR12",
    "X64_RegisterR13",
    "X64_RegisterR14",
    "X64_RegisterR15",
    "X64_RegisterR8",
    "X64_RegisterR9",
    "X64_RegisterRFlags",
    "X64_RegisterRax",
    "X64_RegisterRbp",
    "X64_RegisterRbx",
    "X64_RegisterRcx",
    "X64_RegisterRdi",
    "X64_RegisterRdx",
    "X64_RegisterRip",
    "X64_RegisterRsi",
    "X64_RegisterRsp",
    "X64_RegisterSs",
    "X64_RegisterTr",
    "X64_RegisterXmm0",
    "X64_RegisterXmm1",
    "X64_RegisterXmm10",
    "X64_RegisterXmm11",
    "X64_RegisterXmm12",
    "X64_RegisterXmm13",
    "X64_RegisterXmm14",
    "X64_RegisterXmm15",
    "X64_RegisterXmm2",
    "X64_RegisterXmm3",
    "X64_RegisterXmm4",
    "X64_RegisterXmm5",
    "X64_RegisterXmm6",
    "X64_RegisterXmm7",
    "X64_RegisterXmm8",
    "X64_RegisterXmm9",
    "X64_RegisterXmmControlStatus",
]
_arch_optional = [
]
