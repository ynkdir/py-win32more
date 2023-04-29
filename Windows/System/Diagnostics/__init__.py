from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.Data.Json
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.System
import Windows.System.Diagnostics
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class DiagnosticActionResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.Diagnostics.DiagnosticActionResult'
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.System.Diagnostics.IDiagnosticActionResult) -> Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_Results(self: Windows.System.Diagnostics.IDiagnosticActionResult) -> Windows.Foundation.Collections.ValueSet: ...
    ExtendedError = property(get_ExtendedError, None)
    Results = property(get_Results, None)
DiagnosticActionState = Int32
DiagnosticActionState_Initializing: DiagnosticActionState = 0
DiagnosticActionState_Downloading: DiagnosticActionState = 1
DiagnosticActionState_VerifyingTrust: DiagnosticActionState = 2
DiagnosticActionState_Detecting: DiagnosticActionState = 3
DiagnosticActionState_Resolving: DiagnosticActionState = 4
DiagnosticActionState_VerifyingResolution: DiagnosticActionState = 5
DiagnosticActionState_Executing: DiagnosticActionState = 6
class DiagnosticInvoker(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.Diagnostics.DiagnosticInvoker'
    @winrt_mixinmethod
    def RunDiagnosticActionAsync(self: Windows.System.Diagnostics.IDiagnosticInvoker, context: Windows.Data.Json.JsonObject) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.System.Diagnostics.DiagnosticActionResult, Windows.System.Diagnostics.DiagnosticActionState]: ...
    @winrt_mixinmethod
    def RunDiagnosticActionFromStringAsync(self: Windows.System.Diagnostics.IDiagnosticInvoker2, context: WinRT_String) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.System.Diagnostics.DiagnosticActionResult, Windows.System.Diagnostics.DiagnosticActionState]: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.System.Diagnostics.IDiagnosticInvokerStatics) -> Windows.System.Diagnostics.DiagnosticInvoker: ...
    @winrt_classmethod
    def GetForUser(cls: Windows.System.Diagnostics.IDiagnosticInvokerStatics, user: Windows.System.User) -> Windows.System.Diagnostics.DiagnosticInvoker: ...
    @winrt_classmethod
    def get_IsSupported(cls: Windows.System.Diagnostics.IDiagnosticInvokerStatics) -> Boolean: ...
    IsSupported = property(get_IsSupported, None)
class IDiagnosticActionResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c265a296-e73b-4097-b2-8f-34-42-f0-3d-d8-31')
    @winrt_commethod(6)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    @winrt_commethod(7)
    def get_Results(self) -> Windows.Foundation.Collections.ValueSet: ...
    ExtendedError = property(get_ExtendedError, None)
    Results = property(get_Results, None)
class IDiagnosticInvoker(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('187b270a-02e3-4f86-84-fc-fd-d8-92-b5-94-0f')
    @winrt_commethod(6)
    def RunDiagnosticActionAsync(self, context: Windows.Data.Json.JsonObject) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.System.Diagnostics.DiagnosticActionResult, Windows.System.Diagnostics.DiagnosticActionState]: ...
class IDiagnosticInvoker2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e3bf945c-155a-4b52-a8-ec-07-0c-44-f9-50-00')
    @winrt_commethod(6)
    def RunDiagnosticActionFromStringAsync(self, context: WinRT_String) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.System.Diagnostics.DiagnosticActionResult, Windows.System.Diagnostics.DiagnosticActionState]: ...
class IDiagnosticInvokerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5cfad8de-f15c-4554-a8-13-c1-13-c3-88-1b-09')
    @winrt_commethod(6)
    def GetDefault(self) -> Windows.System.Diagnostics.DiagnosticInvoker: ...
    @winrt_commethod(7)
    def GetForUser(self, user: Windows.System.User) -> Windows.System.Diagnostics.DiagnosticInvoker: ...
    @winrt_commethod(8)
    def get_IsSupported(self) -> Boolean: ...
    IsSupported = property(get_IsSupported, None)
class IProcessCpuUsage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0bbb2472-c8bf-423a-a8-10-b5-59-ae-43-54-e2')
    @winrt_commethod(6)
    def GetReport(self) -> Windows.System.Diagnostics.ProcessCpuUsageReport: ...
class IProcessCpuUsageReport(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8a6d9cac-3987-4e2f-a1-19-6b-5f-a2-14-f1-b4')
    @winrt_commethod(6)
    def get_KernelTime(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def get_UserTime(self) -> Windows.Foundation.TimeSpan: ...
    KernelTime = property(get_KernelTime, None)
    UserTime = property(get_UserTime, None)
class IProcessDiagnosticInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e830b04b-300e-4ee6-a0-ab-5b-5f-52-31-b4-34')
    @winrt_commethod(6)
    def get_ProcessId(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_ExecutableFileName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Parent(self) -> Windows.System.Diagnostics.ProcessDiagnosticInfo: ...
    @winrt_commethod(9)
    def get_ProcessStartTime(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(10)
    def get_DiskUsage(self) -> Windows.System.Diagnostics.ProcessDiskUsage: ...
    @winrt_commethod(11)
    def get_MemoryUsage(self) -> Windows.System.Diagnostics.ProcessMemoryUsage: ...
    @winrt_commethod(12)
    def get_CpuUsage(self) -> Windows.System.Diagnostics.ProcessCpuUsage: ...
    ProcessId = property(get_ProcessId, None)
    ExecutableFileName = property(get_ExecutableFileName, None)
    Parent = property(get_Parent, None)
    ProcessStartTime = property(get_ProcessStartTime, None)
    DiskUsage = property(get_DiskUsage, None)
    MemoryUsage = property(get_MemoryUsage, None)
    CpuUsage = property(get_CpuUsage, None)
class IProcessDiagnosticInfo2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9558cb1a-3d0b-49ec-ab-70-4f-7a-11-28-05-de')
    @winrt_commethod(6)
    def GetAppDiagnosticInfos(self) -> Windows.Foundation.Collections.IVector[Windows.System.AppDiagnosticInfo]: ...
    @winrt_commethod(7)
    def get_IsPackaged(self) -> Boolean: ...
    IsPackaged = property(get_IsPackaged, None)
class IProcessDiagnosticInfoStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2f41b260-b49f-428c-aa-0e-84-74-4f-49-ca-95')
    @winrt_commethod(6)
    def GetForProcesses(self) -> Windows.Foundation.Collections.IVectorView[Windows.System.Diagnostics.ProcessDiagnosticInfo]: ...
    @winrt_commethod(7)
    def GetForCurrentProcess(self) -> Windows.System.Diagnostics.ProcessDiagnosticInfo: ...
class IProcessDiagnosticInfoStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4a869897-9899-4a44-a2-9b-09-16-63-be-09-b6')
    @winrt_commethod(6)
    def TryGetForProcessId(self, processId: UInt32) -> Windows.System.Diagnostics.ProcessDiagnosticInfo: ...
class IProcessDiskUsage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5ad78bfd-7e51-4e53-bf-aa-5a-6e-e1-aa-bb-f8')
    @winrt_commethod(6)
    def GetReport(self) -> Windows.System.Diagnostics.ProcessDiskUsageReport: ...
class IProcessDiskUsageReport(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('401627fd-535d-4c1f-81-b8-da-54-e1-be-63-5e')
    @winrt_commethod(6)
    def get_ReadOperationCount(self) -> Int64: ...
    @winrt_commethod(7)
    def get_WriteOperationCount(self) -> Int64: ...
    @winrt_commethod(8)
    def get_OtherOperationCount(self) -> Int64: ...
    @winrt_commethod(9)
    def get_BytesReadCount(self) -> Int64: ...
    @winrt_commethod(10)
    def get_BytesWrittenCount(self) -> Int64: ...
    @winrt_commethod(11)
    def get_OtherBytesCount(self) -> Int64: ...
    ReadOperationCount = property(get_ReadOperationCount, None)
    WriteOperationCount = property(get_WriteOperationCount, None)
    OtherOperationCount = property(get_OtherOperationCount, None)
    BytesReadCount = property(get_BytesReadCount, None)
    BytesWrittenCount = property(get_BytesWrittenCount, None)
    OtherBytesCount = property(get_OtherBytesCount, None)
class IProcessMemoryUsage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f50b229b-827c-42b7-b0-7c-0e-32-62-7e-6b-3e')
    @winrt_commethod(6)
    def GetReport(self) -> Windows.System.Diagnostics.ProcessMemoryUsageReport: ...
class IProcessMemoryUsageReport(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c2c77cba-1951-4685-85-32-7e-74-9e-cf-8e-eb')
    @winrt_commethod(6)
    def get_NonPagedPoolSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(7)
    def get_PageFaultCount(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_PageFileSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(9)
    def get_PagedPoolSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(10)
    def get_PeakNonPagedPoolSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(11)
    def get_PeakPageFileSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(12)
    def get_PeakPagedPoolSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(13)
    def get_PeakVirtualMemorySizeInBytes(self) -> UInt64: ...
    @winrt_commethod(14)
    def get_PeakWorkingSetSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(15)
    def get_PrivatePageCount(self) -> UInt64: ...
    @winrt_commethod(16)
    def get_VirtualMemorySizeInBytes(self) -> UInt64: ...
    @winrt_commethod(17)
    def get_WorkingSetSizeInBytes(self) -> UInt64: ...
    NonPagedPoolSizeInBytes = property(get_NonPagedPoolSizeInBytes, None)
    PageFaultCount = property(get_PageFaultCount, None)
    PageFileSizeInBytes = property(get_PageFileSizeInBytes, None)
    PagedPoolSizeInBytes = property(get_PagedPoolSizeInBytes, None)
    PeakNonPagedPoolSizeInBytes = property(get_PeakNonPagedPoolSizeInBytes, None)
    PeakPageFileSizeInBytes = property(get_PeakPageFileSizeInBytes, None)
    PeakPagedPoolSizeInBytes = property(get_PeakPagedPoolSizeInBytes, None)
    PeakVirtualMemorySizeInBytes = property(get_PeakVirtualMemorySizeInBytes, None)
    PeakWorkingSetSizeInBytes = property(get_PeakWorkingSetSizeInBytes, None)
    PrivatePageCount = property(get_PrivatePageCount, None)
    VirtualMemorySizeInBytes = property(get_VirtualMemorySizeInBytes, None)
    WorkingSetSizeInBytes = property(get_WorkingSetSizeInBytes, None)
class ISystemCpuUsage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6037b3ac-02d6-4234-83-62-7f-e3-ad-c8-1f-5f')
    @winrt_commethod(6)
    def GetReport(self) -> Windows.System.Diagnostics.SystemCpuUsageReport: ...
class ISystemCpuUsageReport(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2c26d0b2-9483-4f62-ab-57-82-b2-9d-97-19-b8')
    @winrt_commethod(6)
    def get_KernelTime(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def get_UserTime(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(8)
    def get_IdleTime(self) -> Windows.Foundation.TimeSpan: ...
    KernelTime = property(get_KernelTime, None)
    UserTime = property(get_UserTime, None)
    IdleTime = property(get_IdleTime, None)
class ISystemDiagnosticInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a290fe05-dff3-407f-9a-1b-0b-2b-31-7c-a8-00')
    @winrt_commethod(6)
    def get_MemoryUsage(self) -> Windows.System.Diagnostics.SystemMemoryUsage: ...
    @winrt_commethod(7)
    def get_CpuUsage(self) -> Windows.System.Diagnostics.SystemCpuUsage: ...
    MemoryUsage = property(get_MemoryUsage, None)
    CpuUsage = property(get_CpuUsage, None)
class ISystemDiagnosticInfoStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d404ac21-fc7d-45f0-9a-3f-39-20-3a-ed-9f-7e')
    @winrt_commethod(6)
    def GetForCurrentSystem(self) -> Windows.System.Diagnostics.SystemDiagnosticInfo: ...
class ISystemDiagnosticInfoStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('79ded189-6af9-4da9-a4-22-15-f7-32-55-b3-eb')
    @winrt_commethod(6)
    def IsArchitectureSupported(self, type: Windows.System.ProcessorArchitecture) -> Boolean: ...
    @winrt_commethod(7)
    def get_PreferredArchitecture(self) -> Windows.System.ProcessorArchitecture: ...
    PreferredArchitecture = property(get_PreferredArchitecture, None)
class ISystemMemoryUsage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('17ffc595-1702-49cf-aa-27-2f-0a-32-59-14-04')
    @winrt_commethod(6)
    def GetReport(self) -> Windows.System.Diagnostics.SystemMemoryUsageReport: ...
class ISystemMemoryUsageReport(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('38663c87-2a9f-403a-bd-19-2c-f3-e8-16-95-00')
    @winrt_commethod(6)
    def get_TotalPhysicalSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(7)
    def get_AvailableSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(8)
    def get_CommittedSizeInBytes(self) -> UInt64: ...
    TotalPhysicalSizeInBytes = property(get_TotalPhysicalSizeInBytes, None)
    AvailableSizeInBytes = property(get_AvailableSizeInBytes, None)
    CommittedSizeInBytes = property(get_CommittedSizeInBytes, None)
class ProcessCpuUsage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.Diagnostics.ProcessCpuUsage'
    @winrt_mixinmethod
    def GetReport(self: Windows.System.Diagnostics.IProcessCpuUsage) -> Windows.System.Diagnostics.ProcessCpuUsageReport: ...
class ProcessCpuUsageReport(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.Diagnostics.ProcessCpuUsageReport'
    @winrt_mixinmethod
    def get_KernelTime(self: Windows.System.Diagnostics.IProcessCpuUsageReport) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_UserTime(self: Windows.System.Diagnostics.IProcessCpuUsageReport) -> Windows.Foundation.TimeSpan: ...
    KernelTime = property(get_KernelTime, None)
    UserTime = property(get_UserTime, None)
class ProcessDiagnosticInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.Diagnostics.ProcessDiagnosticInfo'
    @winrt_mixinmethod
    def get_ProcessId(self: Windows.System.Diagnostics.IProcessDiagnosticInfo) -> UInt32: ...
    @winrt_mixinmethod
    def get_ExecutableFileName(self: Windows.System.Diagnostics.IProcessDiagnosticInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Parent(self: Windows.System.Diagnostics.IProcessDiagnosticInfo) -> Windows.System.Diagnostics.ProcessDiagnosticInfo: ...
    @winrt_mixinmethod
    def get_ProcessStartTime(self: Windows.System.Diagnostics.IProcessDiagnosticInfo) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_DiskUsage(self: Windows.System.Diagnostics.IProcessDiagnosticInfo) -> Windows.System.Diagnostics.ProcessDiskUsage: ...
    @winrt_mixinmethod
    def get_MemoryUsage(self: Windows.System.Diagnostics.IProcessDiagnosticInfo) -> Windows.System.Diagnostics.ProcessMemoryUsage: ...
    @winrt_mixinmethod
    def get_CpuUsage(self: Windows.System.Diagnostics.IProcessDiagnosticInfo) -> Windows.System.Diagnostics.ProcessCpuUsage: ...
    @winrt_mixinmethod
    def GetAppDiagnosticInfos(self: Windows.System.Diagnostics.IProcessDiagnosticInfo2) -> Windows.Foundation.Collections.IVector[Windows.System.AppDiagnosticInfo]: ...
    @winrt_mixinmethod
    def get_IsPackaged(self: Windows.System.Diagnostics.IProcessDiagnosticInfo2) -> Boolean: ...
    @winrt_classmethod
    def TryGetForProcessId(cls: Windows.System.Diagnostics.IProcessDiagnosticInfoStatics2, processId: UInt32) -> Windows.System.Diagnostics.ProcessDiagnosticInfo: ...
    @winrt_classmethod
    def GetForProcesses(cls: Windows.System.Diagnostics.IProcessDiagnosticInfoStatics) -> Windows.Foundation.Collections.IVectorView[Windows.System.Diagnostics.ProcessDiagnosticInfo]: ...
    @winrt_classmethod
    def GetForCurrentProcess(cls: Windows.System.Diagnostics.IProcessDiagnosticInfoStatics) -> Windows.System.Diagnostics.ProcessDiagnosticInfo: ...
    ProcessId = property(get_ProcessId, None)
    ExecutableFileName = property(get_ExecutableFileName, None)
    Parent = property(get_Parent, None)
    ProcessStartTime = property(get_ProcessStartTime, None)
    DiskUsage = property(get_DiskUsage, None)
    MemoryUsage = property(get_MemoryUsage, None)
    CpuUsage = property(get_CpuUsage, None)
    IsPackaged = property(get_IsPackaged, None)
class ProcessDiskUsage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.Diagnostics.ProcessDiskUsage'
    @winrt_mixinmethod
    def GetReport(self: Windows.System.Diagnostics.IProcessDiskUsage) -> Windows.System.Diagnostics.ProcessDiskUsageReport: ...
class ProcessDiskUsageReport(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.Diagnostics.ProcessDiskUsageReport'
    @winrt_mixinmethod
    def get_ReadOperationCount(self: Windows.System.Diagnostics.IProcessDiskUsageReport) -> Int64: ...
    @winrt_mixinmethod
    def get_WriteOperationCount(self: Windows.System.Diagnostics.IProcessDiskUsageReport) -> Int64: ...
    @winrt_mixinmethod
    def get_OtherOperationCount(self: Windows.System.Diagnostics.IProcessDiskUsageReport) -> Int64: ...
    @winrt_mixinmethod
    def get_BytesReadCount(self: Windows.System.Diagnostics.IProcessDiskUsageReport) -> Int64: ...
    @winrt_mixinmethod
    def get_BytesWrittenCount(self: Windows.System.Diagnostics.IProcessDiskUsageReport) -> Int64: ...
    @winrt_mixinmethod
    def get_OtherBytesCount(self: Windows.System.Diagnostics.IProcessDiskUsageReport) -> Int64: ...
    ReadOperationCount = property(get_ReadOperationCount, None)
    WriteOperationCount = property(get_WriteOperationCount, None)
    OtherOperationCount = property(get_OtherOperationCount, None)
    BytesReadCount = property(get_BytesReadCount, None)
    BytesWrittenCount = property(get_BytesWrittenCount, None)
    OtherBytesCount = property(get_OtherBytesCount, None)
class ProcessMemoryUsage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.Diagnostics.ProcessMemoryUsage'
    @winrt_mixinmethod
    def GetReport(self: Windows.System.Diagnostics.IProcessMemoryUsage) -> Windows.System.Diagnostics.ProcessMemoryUsageReport: ...
class ProcessMemoryUsageReport(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.Diagnostics.ProcessMemoryUsageReport'
    @winrt_mixinmethod
    def get_NonPagedPoolSizeInBytes(self: Windows.System.Diagnostics.IProcessMemoryUsageReport) -> UInt64: ...
    @winrt_mixinmethod
    def get_PageFaultCount(self: Windows.System.Diagnostics.IProcessMemoryUsageReport) -> UInt32: ...
    @winrt_mixinmethod
    def get_PageFileSizeInBytes(self: Windows.System.Diagnostics.IProcessMemoryUsageReport) -> UInt64: ...
    @winrt_mixinmethod
    def get_PagedPoolSizeInBytes(self: Windows.System.Diagnostics.IProcessMemoryUsageReport) -> UInt64: ...
    @winrt_mixinmethod
    def get_PeakNonPagedPoolSizeInBytes(self: Windows.System.Diagnostics.IProcessMemoryUsageReport) -> UInt64: ...
    @winrt_mixinmethod
    def get_PeakPageFileSizeInBytes(self: Windows.System.Diagnostics.IProcessMemoryUsageReport) -> UInt64: ...
    @winrt_mixinmethod
    def get_PeakPagedPoolSizeInBytes(self: Windows.System.Diagnostics.IProcessMemoryUsageReport) -> UInt64: ...
    @winrt_mixinmethod
    def get_PeakVirtualMemorySizeInBytes(self: Windows.System.Diagnostics.IProcessMemoryUsageReport) -> UInt64: ...
    @winrt_mixinmethod
    def get_PeakWorkingSetSizeInBytes(self: Windows.System.Diagnostics.IProcessMemoryUsageReport) -> UInt64: ...
    @winrt_mixinmethod
    def get_PrivatePageCount(self: Windows.System.Diagnostics.IProcessMemoryUsageReport) -> UInt64: ...
    @winrt_mixinmethod
    def get_VirtualMemorySizeInBytes(self: Windows.System.Diagnostics.IProcessMemoryUsageReport) -> UInt64: ...
    @winrt_mixinmethod
    def get_WorkingSetSizeInBytes(self: Windows.System.Diagnostics.IProcessMemoryUsageReport) -> UInt64: ...
    NonPagedPoolSizeInBytes = property(get_NonPagedPoolSizeInBytes, None)
    PageFaultCount = property(get_PageFaultCount, None)
    PageFileSizeInBytes = property(get_PageFileSizeInBytes, None)
    PagedPoolSizeInBytes = property(get_PagedPoolSizeInBytes, None)
    PeakNonPagedPoolSizeInBytes = property(get_PeakNonPagedPoolSizeInBytes, None)
    PeakPageFileSizeInBytes = property(get_PeakPageFileSizeInBytes, None)
    PeakPagedPoolSizeInBytes = property(get_PeakPagedPoolSizeInBytes, None)
    PeakVirtualMemorySizeInBytes = property(get_PeakVirtualMemorySizeInBytes, None)
    PeakWorkingSetSizeInBytes = property(get_PeakWorkingSetSizeInBytes, None)
    PrivatePageCount = property(get_PrivatePageCount, None)
    VirtualMemorySizeInBytes = property(get_VirtualMemorySizeInBytes, None)
    WorkingSetSizeInBytes = property(get_WorkingSetSizeInBytes, None)
class SystemCpuUsage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.Diagnostics.SystemCpuUsage'
    @winrt_mixinmethod
    def GetReport(self: Windows.System.Diagnostics.ISystemCpuUsage) -> Windows.System.Diagnostics.SystemCpuUsageReport: ...
class SystemCpuUsageReport(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.Diagnostics.SystemCpuUsageReport'
    @winrt_mixinmethod
    def get_KernelTime(self: Windows.System.Diagnostics.ISystemCpuUsageReport) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_UserTime(self: Windows.System.Diagnostics.ISystemCpuUsageReport) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_IdleTime(self: Windows.System.Diagnostics.ISystemCpuUsageReport) -> Windows.Foundation.TimeSpan: ...
    KernelTime = property(get_KernelTime, None)
    UserTime = property(get_UserTime, None)
    IdleTime = property(get_IdleTime, None)
class SystemDiagnosticInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.Diagnostics.SystemDiagnosticInfo'
    @winrt_mixinmethod
    def get_MemoryUsage(self: Windows.System.Diagnostics.ISystemDiagnosticInfo) -> Windows.System.Diagnostics.SystemMemoryUsage: ...
    @winrt_mixinmethod
    def get_CpuUsage(self: Windows.System.Diagnostics.ISystemDiagnosticInfo) -> Windows.System.Diagnostics.SystemCpuUsage: ...
    @winrt_classmethod
    def IsArchitectureSupported(cls: Windows.System.Diagnostics.ISystemDiagnosticInfoStatics2, type: Windows.System.ProcessorArchitecture) -> Boolean: ...
    @winrt_classmethod
    def get_PreferredArchitecture(cls: Windows.System.Diagnostics.ISystemDiagnosticInfoStatics2) -> Windows.System.ProcessorArchitecture: ...
    @winrt_classmethod
    def GetForCurrentSystem(cls: Windows.System.Diagnostics.ISystemDiagnosticInfoStatics) -> Windows.System.Diagnostics.SystemDiagnosticInfo: ...
    MemoryUsage = property(get_MemoryUsage, None)
    CpuUsage = property(get_CpuUsage, None)
    PreferredArchitecture = property(get_PreferredArchitecture, None)
class SystemMemoryUsage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.Diagnostics.SystemMemoryUsage'
    @winrt_mixinmethod
    def GetReport(self: Windows.System.Diagnostics.ISystemMemoryUsage) -> Windows.System.Diagnostics.SystemMemoryUsageReport: ...
class SystemMemoryUsageReport(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.Diagnostics.SystemMemoryUsageReport'
    @winrt_mixinmethod
    def get_TotalPhysicalSizeInBytes(self: Windows.System.Diagnostics.ISystemMemoryUsageReport) -> UInt64: ...
    @winrt_mixinmethod
    def get_AvailableSizeInBytes(self: Windows.System.Diagnostics.ISystemMemoryUsageReport) -> UInt64: ...
    @winrt_mixinmethod
    def get_CommittedSizeInBytes(self: Windows.System.Diagnostics.ISystemMemoryUsageReport) -> UInt64: ...
    TotalPhysicalSizeInBytes = property(get_TotalPhysicalSizeInBytes, None)
    AvailableSizeInBytes = property(get_AvailableSizeInBytes, None)
    CommittedSizeInBytes = property(get_CommittedSizeInBytes, None)
make_head(_module, 'DiagnosticActionResult')
make_head(_module, 'DiagnosticInvoker')
make_head(_module, 'IDiagnosticActionResult')
make_head(_module, 'IDiagnosticInvoker')
make_head(_module, 'IDiagnosticInvoker2')
make_head(_module, 'IDiagnosticInvokerStatics')
make_head(_module, 'IProcessCpuUsage')
make_head(_module, 'IProcessCpuUsageReport')
make_head(_module, 'IProcessDiagnosticInfo')
make_head(_module, 'IProcessDiagnosticInfo2')
make_head(_module, 'IProcessDiagnosticInfoStatics')
make_head(_module, 'IProcessDiagnosticInfoStatics2')
make_head(_module, 'IProcessDiskUsage')
make_head(_module, 'IProcessDiskUsageReport')
make_head(_module, 'IProcessMemoryUsage')
make_head(_module, 'IProcessMemoryUsageReport')
make_head(_module, 'ISystemCpuUsage')
make_head(_module, 'ISystemCpuUsageReport')
make_head(_module, 'ISystemDiagnosticInfo')
make_head(_module, 'ISystemDiagnosticInfoStatics')
make_head(_module, 'ISystemDiagnosticInfoStatics2')
make_head(_module, 'ISystemMemoryUsage')
make_head(_module, 'ISystemMemoryUsageReport')
make_head(_module, 'ProcessCpuUsage')
make_head(_module, 'ProcessCpuUsageReport')
make_head(_module, 'ProcessDiagnosticInfo')
make_head(_module, 'ProcessDiskUsage')
make_head(_module, 'ProcessDiskUsageReport')
make_head(_module, 'ProcessMemoryUsage')
make_head(_module, 'ProcessMemoryUsageReport')
make_head(_module, 'SystemCpuUsage')
make_head(_module, 'SystemCpuUsageReport')
make_head(_module, 'SystemDiagnosticInfo')
make_head(_module, 'SystemMemoryUsage')
make_head(_module, 'SystemMemoryUsageReport')
