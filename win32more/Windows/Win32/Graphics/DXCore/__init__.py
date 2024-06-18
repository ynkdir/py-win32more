from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.DXCore
import win32more.Windows.Win32.System.Com
_FACDXCORE: UInt32 = 2176
DXCORE_ADAPTER_ATTRIBUTE_D3D11_GRAPHICS: Guid = Guid('{8c47866b-7583-450d-f0f0-6bada895af4b}')
DXCORE_ADAPTER_ATTRIBUTE_D3D12_GRAPHICS: Guid = Guid('{0c9ece4d-2f6e-4f01-8c96-e89e331b47b1}')
DXCORE_ADAPTER_ATTRIBUTE_D3D12_CORE_COMPUTE: Guid = Guid('{248e2800-a793-4724-abaa-23a6de1be090}')
@winfunctype('DXCORE.dll')
def DXCoreCreateAdapterFactory(riid: POINTER(Guid), ppvFactory: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
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
DXCoreAdapterState = UInt32
IsDriverUpdateInProgress: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterState = 0
AdapterMemoryBudget: win32more.Windows.Win32.Graphics.DXCore.DXCoreAdapterState = 1
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
DXCoreNotificationType = UInt32
AdapterListStale: win32more.Windows.Win32.Graphics.DXCore.DXCoreNotificationType = 0
AdapterNoLongerValid: win32more.Windows.Win32.Graphics.DXCore.DXCoreNotificationType = 1
AdapterBudgetChange: win32more.Windows.Win32.Graphics.DXCore.DXCoreNotificationType = 2
AdapterHardwareContentProtectionTeardown: win32more.Windows.Win32.Graphics.DXCore.DXCoreNotificationType = 3
DXCoreSegmentGroup = UInt32
Local: win32more.Windows.Win32.Graphics.DXCore.DXCoreSegmentGroup = 0
NonLocal: win32more.Windows.Win32.Graphics.DXCore.DXCoreSegmentGroup = 1
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
