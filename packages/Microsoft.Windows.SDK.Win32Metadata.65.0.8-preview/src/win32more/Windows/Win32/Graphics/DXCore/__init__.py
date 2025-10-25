from __future__ import annotations
from win32more._prelude import *
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.DXCore
import win32more.Windows.Win32.System.Com
_FACDXCORE: UInt32 = 2176
DXCORE_ADAPTER_ATTRIBUTE_D3D11_GRAPHICS: Guid = Guid('{8c47866b-7583-450d-f0f0-6bada895af4b}')
DXCORE_ADAPTER_ATTRIBUTE_D3D12_GRAPHICS: Guid = Guid('{0c9ece4d-2f6e-4f01-8c96-e89e331b47b1}')
DXCORE_ADAPTER_ATTRIBUTE_D3D12_CORE_COMPUTE: Guid = Guid('{248e2800-a793-4724-abaa-23a6de1be090}')
DXCORE_ADAPTER_ATTRIBUTE_D3D12_GENERIC_ML: Guid = Guid('{b71b0d41-1088-422f-a27c-0250b7d3a988}')
DXCORE_ADAPTER_ATTRIBUTE_D3D12_GENERIC_MEDIA: Guid = Guid('{8eb2c848-82f6-4b49-aa87-aecfcf0174c6}')
DXCORE_HARDWARE_TYPE_ATTRIBUTE_GPU: Guid = Guid('{b69eb219-3ded-4464-979f-a00bd4687006}')
DXCORE_HARDWARE_TYPE_ATTRIBUTE_COMPUTE_ACCELERATOR: Guid = Guid('{e0b195da-58ef-4a22-90f1-1f28169cab8d}')
DXCORE_HARDWARE_TYPE_ATTRIBUTE_NPU: Guid = Guid('{d46140c4-add7-451b-9e56-06fe8c3b58ed}')
DXCORE_HARDWARE_TYPE_ATTRIBUTE_MEDIA_ACCELERATOR: Guid = Guid('{66bdb96a-050b-44c7-a4fd-d144ce0ab443}')
@winfunctype('DXCORE.dll')
def DXCoreCreateAdapterFactory(riid: POINTER(Guid), ppvFactory: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class DXCoreAdapterEngineIndex(Structure):
    physicalAdapterIndex: UInt32
    engineIndex: UInt32
class DXCoreAdapterMemoryBudget(Structure):
    budget: UInt64
    currentUsage: UInt64
    availableForReservation: UInt64
    currentReservation: UInt64
class DXCoreAdapterMemoryBudgetNodeSegmentGroup(Structure):
    nodeIndex: UInt32
    segmentGroup: win32more.Windows.Win32.Graphics.DXCore.DXCoreSegmentGroup
DXCoreAdapterPreference = UInt32
Hardware: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterPreference = 0
MinimumPower: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterPreference = 1
HighPerformance: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterPreference = 2
class DXCoreAdapterProcessSetQueryInput(Structure):
    arraySize: UInt32
    processIds: POINTER(UInt32)
class DXCoreAdapterProcessSetQueryOutput(Structure):
    processesWritten: UInt32
    processesTotal: UInt32
DXCoreAdapterProperty = UInt32
InstanceLuid: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterProperty = 0
DriverVersion: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterProperty = 1
DriverDescription: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterProperty = 2
HardwareID: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterProperty = 3
KmdModelVersion: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterProperty = 4
ComputePreemptionGranularity: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterProperty = 5
GraphicsPreemptionGranularity: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterProperty = 6
DedicatedAdapterMemory: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterProperty = 7
DedicatedSystemMemory: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterProperty = 8
SharedSystemMemory: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterProperty = 9
AcgCompatible: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterProperty = 10
IsHardware: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterProperty = 11
IsIntegrated: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterProperty = 12
IsDetachable: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterProperty = 13
HardwareIDParts: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterProperty = 14
PhysicalAdapterCount: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterProperty = 15
AdapterEngineCount: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterProperty = 16
AdapterEngineName: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterProperty = 17
DXCoreAdapterState = UInt32
IsDriverUpdateInProgress: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterState = 0
AdapterMemoryBudget: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterState = 1
AdapterMemoryUsageBytes: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterState = 2
AdapterMemoryUsageByProcessBytes: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterState = 3
AdapterEngineRunningTimeMicroseconds: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterState = 4
AdapterEngineRunningTimeByProcessMicroseconds: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterState = 5
AdapterTemperatureCelsius: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterState = 6
AdapterInUseProcessCount: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterState = 7
AdapterInUseProcessSet: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterState = 8
AdapterEngineFrequencyHertz: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterState = 9
AdapterMemoryFrequencyHertz: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterState = 10
class DXCoreEngineNamePropertyInput(Structure):
    adapterEngineIndex: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterEngineIndex
    engineNameLength: UInt32
    engineName: win32more.Windows.Win32.Foundation.PWSTR
class DXCoreEngineNamePropertyOutput(Structure):
    engineNameLength: UInt32
class DXCoreEngineQueryInput(Structure):
    adapterEngineIndex: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterEngineIndex
    processId: UInt32
class DXCoreEngineQueryOutput(Structure):
    runningTime: UInt64
    processQuerySucceeded: Byte
class DXCoreFrequencyQueryOutput(Structure):
    frequency: UInt64
    maxFrequency: UInt64
    maxOverclockedFrequency: UInt64
class DXCoreHardwareID(Structure):
    vendorID: UInt32
    deviceID: UInt32
    subSysID: UInt32
    revision: UInt32
class DXCoreHardwareIDParts(Structure):
    vendorID: UInt32
    deviceID: UInt32
    subSystemID: UInt32
    subVendorID: UInt32
    revisionID: UInt32
DXCoreHardwareTypeFilterFlags = UInt32
None_: win32more.Windows.Win32.Graphics.DXCore.DXCoreHardwareTypeFilterFlags = 0
GPU: win32more.Windows.Win32.Graphics.DXCore.DXCoreHardwareTypeFilterFlags = 1
ComputeAccelerator: win32more.Windows.Win32.Graphics.DXCore.DXCoreHardwareTypeFilterFlags = 2
NPU: win32more.Windows.Win32.Graphics.DXCore.DXCoreHardwareTypeFilterFlags = 4
MediaAccelerator: win32more.Windows.Win32.Graphics.DXCore.DXCoreHardwareTypeFilterFlags = 8
class DXCoreMemoryQueryInput(Structure):
    physicalAdapterIndex: UInt32
    memoryType: win32more.Windows.Win32.Graphics.DXCore.DXCoreMemoryType
DXCoreMemoryType = UInt32
Dedicated: win32more.Windows.Win32.Graphics.DXCore.DXCoreMemoryType = 0
Shared: win32more.Windows.Win32.Graphics.DXCore.DXCoreMemoryType = 1
class DXCoreMemoryUsage(Structure):
    committed: UInt64
    resident: UInt64
DXCoreNotificationType = UInt32
AdapterListStale: win32more.Windows.Win32.Graphics.DXCore.DXCoreNotificationType = 0
AdapterNoLongerValid: win32more.Windows.Win32.Graphics.DXCore.DXCoreNotificationType = 1
AdapterBudgetChange: win32more.Windows.Win32.Graphics.DXCore.DXCoreNotificationType = 2
AdapterHardwareContentProtectionTeardown: win32more.Windows.Win32.Graphics.DXCore.DXCoreNotificationType = 3
class DXCoreProcessMemoryQueryInput(Structure):
    physicalAdapterIndex: UInt32
    memoryType: win32more.Windows.Win32.Graphics.DXCore.DXCoreMemoryType
    processId: UInt32
class DXCoreProcessMemoryQueryOutput(Structure):
    memoryUsage: win32more.Windows.Win32.Graphics.DXCore.DXCoreMemoryUsage
    processQuerySucceeded: Byte
DXCoreRuntimeFilterFlags = UInt32
None_: win32more.Windows.Win32.Graphics.DXCore.DXCoreRuntimeFilterFlags = 0
D3D11: win32more.Windows.Win32.Graphics.DXCore.DXCoreRuntimeFilterFlags = 1
D3D12: win32more.Windows.Win32.Graphics.DXCore.DXCoreRuntimeFilterFlags = 2
DXCoreSegmentGroup = UInt32
Local: win32more.Windows.Win32.Graphics.DXCore.DXCoreSegmentGroup = 0
NonLocal: win32more.Windows.Win32.Graphics.DXCore.DXCoreSegmentGroup = 1
DXCoreWorkload = UInt32
Graphics: win32more.Windows.Win32.Graphics.DXCore.DXCoreWorkload = 0
Compute: win32more.Windows.Win32.Graphics.DXCore.DXCoreWorkload = 1
Media: win32more.Windows.Win32.Graphics.DXCore.DXCoreWorkload = 2
MachineLearning: win32more.Windows.Win32.Graphics.DXCore.DXCoreWorkload = 3
class IDXCoreAdapter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f0db4c7f-fe5a-42a2-bd62-f2a6cf6fc83e}')
    @commethod(3)
    def IsValid(self) -> Boolean: ...
    @commethod(4)
    def IsAttributeSupported(self, attributeGUID: POINTER(Guid)) -> Boolean: ...
    @commethod(5)
    def IsPropertySupported(self, property: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterProperty) -> Boolean: ...
    @commethod(6)
    def GetProperty(self, property: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterProperty, bufferSize: UIntPtr, propertyData: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetPropertySize(self, property: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterProperty, bufferSize: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def IsQueryStateSupported(self, property: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterState) -> Boolean: ...
    @commethod(9)
    def QueryState(self, state: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterState, inputStateDetailsSize: UIntPtr, inputStateDetails: VoidPtr, outputBufferSize: UIntPtr, outputBuffer: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def IsSetStateSupported(self, property: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterState) -> Boolean: ...
    @commethod(11)
    def SetState(self, state: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterState, inputStateDetailsSize: UIntPtr, inputStateDetails: VoidPtr, inputDataSize: UIntPtr, inputData: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetFactory(self, riid: POINTER(Guid), ppvFactory: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDXCoreAdapter1(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DXCore.IDXCoreAdapter
    _iid_ = Guid('{a0783366-cfa3-43be-9d79-55b2da97c63c}')
    @commethod(13)
    def GetPropertyWithInput(self, property: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterProperty, inputPropertyDetailsSize: UIntPtr, inputPropertyDetails: VoidPtr, outputBufferSize: UIntPtr, outputBuffer: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDXCoreAdapterFactory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{78ee5945-c36e-4b13-a669-005dd11c0f06}')
    @commethod(3)
    def CreateAdapterList(self, numAttributes: UInt32, filterAttributes: POINTER(Guid), riid: POINTER(Guid), ppvAdapterList: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAdapterByLuid(self, adapterLUID: POINTER(win32more.Windows.Win32.Foundation.LUID), riid: POINTER(Guid), ppvAdapter: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def IsNotificationTypeSupported(self, notificationType: win32more.Windows.Win32.Graphics.DXCore.DXCoreNotificationType) -> Boolean: ...
    @commethod(6)
    def RegisterEventNotification(self, dxCoreObject: win32more.Windows.Win32.System.Com.IUnknown, notificationType: win32more.Windows.Win32.Graphics.DXCore.DXCoreNotificationType, callbackFunction: win32more.Windows.Win32.Graphics.DXCore.PFN_DXCORE_NOTIFICATION_CALLBACK, callbackContext: VoidPtr, eventCookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def UnregisterEventNotification(self, eventCookie: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDXCoreAdapterFactory1(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DXCore.IDXCoreAdapterFactory
    _iid_ = Guid('{d5682e19-6d21-401c-827a-9a51a4ea35d7}')
    @commethod(8)
    def CreateAdapterListByWorkload(self, workload: win32more.Windows.Win32.Graphics.DXCore.DXCoreWorkload, runtimeFilter: win32more.Windows.Win32.Graphics.DXCore.DXCoreRuntimeFilterFlags, hardwareTypeFilter: win32more.Windows.Win32.Graphics.DXCore.DXCoreHardwareTypeFilterFlags, riid: POINTER(Guid), ppvAdapterList: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDXCoreAdapterList(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{526c7776-40e9-459b-b711-f32ad76dfc28}')
    @commethod(3)
    def GetAdapter(self, index: UInt32, riid: POINTER(Guid), ppvAdapter: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAdapterCount(self) -> UInt32: ...
    @commethod(5)
    def IsStale(self) -> Boolean: ...
    @commethod(6)
    def GetFactory(self, riid: POINTER(Guid), ppvFactory: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Sort(self, numPreferences: UInt32, preferences: POINTER(win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterPreference)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def IsAdapterPreferenceSupported(self, preference: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterPreference) -> Boolean: ...
@winfunctype_pointer
def PFN_DXCORE_NOTIFICATION_CALLBACK(notificationType: win32more.Windows.Win32.Graphics.DXCore.DXCoreNotificationType, object: win32more.Windows.Win32.System.Com.IUnknown, context: VoidPtr) -> Void: ...


make_ready(__name__)
