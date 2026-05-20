from __future__ import annotations
from win32more._prelude import *
import win32more.Windows.Wdk.Devices.HumanInterfaceDevice
import win32more.Windows.Win32.Foundation
@winfunctype('VhfUm.DLL')
def VhfCreate(VhfConfig: POINTER(win32more.Windows.Wdk.Devices.HumanInterfaceDevice.VHF_CONFIG), VhfHandle: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('VhfUm.DLL')
def VhfStart(VhfHandle: VoidPtr) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('VhfUm.DLL')
def VhfDelete(VhfHandle: VoidPtr, Wait: win32more.Windows.Win32.Foundation.BOOLEAN) -> Void: ...
@winfunctype('VhfUm.DLL')
def VhfReadReportSubmit(VhfHandle: VoidPtr, HidTransferPacket: POINTER(win32more.Windows.Wdk.Devices.HumanInterfaceDevice.HID_XFER_PACKET)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('VhfUm.DLL')
def VhfAsyncOperationComplete(VhfOperationHandle: VoidPtr, CompletionStatus: win32more.Windows.Win32.Foundation.NTSTATUS) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype_pointer
def EVT_VHF_ASYNC_OPERATION(VhfClientContext: VoidPtr, VhfOperationHandle: VoidPtr, VhfOperationContext: VoidPtr, HidTransferPacket: POINTER(win32more.Windows.Wdk.Devices.HumanInterfaceDevice.HID_XFER_PACKET)) -> Void: ...
@winfunctype_pointer
def EVT_VHF_CLEANUP(VhfClientContext: VoidPtr) -> Void: ...
@winfunctype_pointer
def EVT_VHF_READY_FOR_NEXT_READ_REPORT(VhfClientContext: VoidPtr) -> Void: ...
class HID_XFER_PACKET(Structure):
    reportBuffer: POINTER(Byte)
    reportBufferLen: UInt32
    reportId: Byte
class VHF_CONFIG(Structure):
    Size: UInt32
    VhfClientContext: VoidPtr
    OperationContextSize: UInt32
    FileHandle: win32more.Windows.Win32.Foundation.HANDLE
    VendorID: UInt16
    ProductID: UInt16
    VersionNumber: UInt16
    ContainerID: Guid
    InstanceIDLength: UInt16
    InstanceID: win32more.Windows.Win32.Foundation.PWSTR
    ReportDescriptorLength: UInt16
    ReportDescriptor: POINTER(Byte)
    EvtVhfReadyForNextReadReport: win32more.Windows.Wdk.Devices.HumanInterfaceDevice.EVT_VHF_READY_FOR_NEXT_READ_REPORT
    EvtVhfAsyncOperationGetFeature: win32more.Windows.Wdk.Devices.HumanInterfaceDevice.EVT_VHF_ASYNC_OPERATION
    EvtVhfAsyncOperationSetFeature: win32more.Windows.Wdk.Devices.HumanInterfaceDevice.EVT_VHF_ASYNC_OPERATION
    EvtVhfAsyncOperationWriteReport: win32more.Windows.Wdk.Devices.HumanInterfaceDevice.EVT_VHF_ASYNC_OPERATION
    EvtVhfAsyncOperationGetInputReport: win32more.Windows.Wdk.Devices.HumanInterfaceDevice.EVT_VHF_ASYNC_OPERATION
    EvtVhfCleanup: win32more.Windows.Wdk.Devices.HumanInterfaceDevice.EVT_VHF_CLEANUP
    HardwareIDsLength: UInt16
    HardwareIDs: win32more.Windows.Win32.Foundation.PWSTR


make_ready(__name__)
