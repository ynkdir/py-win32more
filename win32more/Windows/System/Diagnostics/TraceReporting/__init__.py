from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import Annotated, Generic, K, MulticastDelegate, SZArray, T, TProgress, TResult, TSender, V, WinRT_String, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation.Collections
import win32more.Windows.System.Diagnostics.TraceReporting
import win32more.Windows.Win32.System.WinRT
class IPlatformDiagnosticActionsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Diagnostics.TraceReporting.IPlatformDiagnosticActionsStatics'
    _iid_ = Guid('{c1145cfa-9292-4267-890a-9ea3ed072312}')
    @winrt_commethod(6)
    def IsScenarioEnabled(self, scenarioId: Guid) -> Boolean: ...
    @winrt_commethod(7)
    def TryEscalateScenario(self, scenarioId: Guid, escalationType: win32more.Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticEscalationType, outputDirectory: WinRT_String, timestampOutputDirectory: Boolean, forceEscalationUpload: Boolean, triggers: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]) -> Boolean: ...
    @winrt_commethod(8)
    def DownloadLatestSettingsForNamespace(self, partner: WinRT_String, feature: WinRT_String, isScenarioNamespace: Boolean, downloadOverCostedNetwork: Boolean, downloadOverBattery: Boolean) -> win32more.Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticActionState: ...
    @winrt_commethod(9)
    def GetActiveScenarioList(self) -> win32more.Windows.Foundation.Collections.IVectorView[Guid]: ...
    @winrt_commethod(10)
    def ForceUpload(self, latency: win32more.Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticEventBufferLatencies, uploadOverCostedNetwork: Boolean, uploadOverBattery: Boolean) -> win32more.Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticActionState: ...
    @winrt_commethod(11)
    def IsTraceRunning(self, slotType: win32more.Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticTraceSlotType, scenarioId: Guid, traceProfileHash: UInt64) -> win32more.Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticTraceSlotState: ...
    @winrt_commethod(12)
    def GetActiveTraceRuntime(self, slotType: win32more.Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticTraceSlotType) -> win32more.Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticTraceRuntimeInfo: ...
    @winrt_commethod(13)
    def GetKnownTraceList(self, slotType: win32more.Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticTraceSlotType) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticTraceInfo]: ...
class IPlatformDiagnosticTraceInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Diagnostics.TraceReporting.IPlatformDiagnosticTraceInfo'
    _iid_ = Guid('{f870ed97-d597-4bf7-88dc-cf5c7dc2a1d2}')
    @winrt_commethod(6)
    def get_ScenarioId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_ProfileHash(self) -> UInt64: ...
    @winrt_commethod(8)
    def get_IsExclusive(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsAutoLogger(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_MaxTraceDurationFileTime(self) -> Int64: ...
    @winrt_commethod(11)
    def get_Priority(self) -> win32more.Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticTracePriority: ...
    ScenarioId = property(get_ScenarioId, None)
    ProfileHash = property(get_ProfileHash, None)
    IsExclusive = property(get_IsExclusive, None)
    IsAutoLogger = property(get_IsAutoLogger, None)
    MaxTraceDurationFileTime = property(get_MaxTraceDurationFileTime, None)
    Priority = property(get_Priority, None)
class IPlatformDiagnosticTraceRuntimeInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Diagnostics.TraceReporting.IPlatformDiagnosticTraceRuntimeInfo'
    _iid_ = Guid('{3d4d5e2d-01d8-4768-8554-1eb1ca610986}')
    @winrt_commethod(6)
    def get_RuntimeFileTime(self) -> Int64: ...
    @winrt_commethod(7)
    def get_EtwRuntimeFileTime(self) -> Int64: ...
    RuntimeFileTime = property(get_RuntimeFileTime, None)
    EtwRuntimeFileTime = property(get_EtwRuntimeFileTime, None)
PlatformDiagnosticActionState = Int32
PlatformDiagnosticActionState_Success: PlatformDiagnosticActionState = 0
PlatformDiagnosticActionState_FreeNetworkNotAvailable: PlatformDiagnosticActionState = 1
PlatformDiagnosticActionState_ACPowerNotAvailable: PlatformDiagnosticActionState = 2
class PlatformDiagnosticActions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticActions'
    @winrt_classmethod
    def IsScenarioEnabled(cls: win32more.Windows.System.Diagnostics.TraceReporting.IPlatformDiagnosticActionsStatics, scenarioId: Guid) -> Boolean: ...
    @winrt_classmethod
    def TryEscalateScenario(cls: win32more.Windows.System.Diagnostics.TraceReporting.IPlatformDiagnosticActionsStatics, scenarioId: Guid, escalationType: win32more.Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticEscalationType, outputDirectory: WinRT_String, timestampOutputDirectory: Boolean, forceEscalationUpload: Boolean, triggers: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]) -> Boolean: ...
    @winrt_classmethod
    def DownloadLatestSettingsForNamespace(cls: win32more.Windows.System.Diagnostics.TraceReporting.IPlatformDiagnosticActionsStatics, partner: WinRT_String, feature: WinRT_String, isScenarioNamespace: Boolean, downloadOverCostedNetwork: Boolean, downloadOverBattery: Boolean) -> win32more.Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticActionState: ...
    @winrt_classmethod
    def GetActiveScenarioList(cls: win32more.Windows.System.Diagnostics.TraceReporting.IPlatformDiagnosticActionsStatics) -> win32more.Windows.Foundation.Collections.IVectorView[Guid]: ...
    @winrt_classmethod
    def ForceUpload(cls: win32more.Windows.System.Diagnostics.TraceReporting.IPlatformDiagnosticActionsStatics, latency: win32more.Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticEventBufferLatencies, uploadOverCostedNetwork: Boolean, uploadOverBattery: Boolean) -> win32more.Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticActionState: ...
    @winrt_classmethod
    def IsTraceRunning(cls: win32more.Windows.System.Diagnostics.TraceReporting.IPlatformDiagnosticActionsStatics, slotType: win32more.Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticTraceSlotType, scenarioId: Guid, traceProfileHash: UInt64) -> win32more.Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticTraceSlotState: ...
    @winrt_classmethod
    def GetActiveTraceRuntime(cls: win32more.Windows.System.Diagnostics.TraceReporting.IPlatformDiagnosticActionsStatics, slotType: win32more.Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticTraceSlotType) -> win32more.Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticTraceRuntimeInfo: ...
    @winrt_classmethod
    def GetKnownTraceList(cls: win32more.Windows.System.Diagnostics.TraceReporting.IPlatformDiagnosticActionsStatics, slotType: win32more.Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticTraceSlotType) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticTraceInfo]: ...
PlatformDiagnosticEscalationType = Int32
PlatformDiagnosticEscalationType_OnCompletion: PlatformDiagnosticEscalationType = 0
PlatformDiagnosticEscalationType_OnFailure: PlatformDiagnosticEscalationType = 1
PlatformDiagnosticEventBufferLatencies = UInt32
PlatformDiagnosticEventBufferLatencies_Normal: PlatformDiagnosticEventBufferLatencies = 1
PlatformDiagnosticEventBufferLatencies_CostDeferred: PlatformDiagnosticEventBufferLatencies = 2
PlatformDiagnosticEventBufferLatencies_Realtime: PlatformDiagnosticEventBufferLatencies = 4
class PlatformDiagnosticTraceInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.Diagnostics.TraceReporting.IPlatformDiagnosticTraceInfo
    _classid_ = 'Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticTraceInfo'
    @winrt_mixinmethod
    def get_ScenarioId(self: win32more.Windows.System.Diagnostics.TraceReporting.IPlatformDiagnosticTraceInfo) -> Guid: ...
    @winrt_mixinmethod
    def get_ProfileHash(self: win32more.Windows.System.Diagnostics.TraceReporting.IPlatformDiagnosticTraceInfo) -> UInt64: ...
    @winrt_mixinmethod
    def get_IsExclusive(self: win32more.Windows.System.Diagnostics.TraceReporting.IPlatformDiagnosticTraceInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsAutoLogger(self: win32more.Windows.System.Diagnostics.TraceReporting.IPlatformDiagnosticTraceInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_MaxTraceDurationFileTime(self: win32more.Windows.System.Diagnostics.TraceReporting.IPlatformDiagnosticTraceInfo) -> Int64: ...
    @winrt_mixinmethod
    def get_Priority(self: win32more.Windows.System.Diagnostics.TraceReporting.IPlatformDiagnosticTraceInfo) -> win32more.Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticTracePriority: ...
    ScenarioId = property(get_ScenarioId, None)
    ProfileHash = property(get_ProfileHash, None)
    IsExclusive = property(get_IsExclusive, None)
    IsAutoLogger = property(get_IsAutoLogger, None)
    MaxTraceDurationFileTime = property(get_MaxTraceDurationFileTime, None)
    Priority = property(get_Priority, None)
PlatformDiagnosticTracePriority = Int32
PlatformDiagnosticTracePriority_Normal: PlatformDiagnosticTracePriority = 0
PlatformDiagnosticTracePriority_UserElevated: PlatformDiagnosticTracePriority = 1
class PlatformDiagnosticTraceRuntimeInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.Diagnostics.TraceReporting.IPlatformDiagnosticTraceRuntimeInfo
    _classid_ = 'Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticTraceRuntimeInfo'
    @winrt_mixinmethod
    def get_RuntimeFileTime(self: win32more.Windows.System.Diagnostics.TraceReporting.IPlatformDiagnosticTraceRuntimeInfo) -> Int64: ...
    @winrt_mixinmethod
    def get_EtwRuntimeFileTime(self: win32more.Windows.System.Diagnostics.TraceReporting.IPlatformDiagnosticTraceRuntimeInfo) -> Int64: ...
    RuntimeFileTime = property(get_RuntimeFileTime, None)
    EtwRuntimeFileTime = property(get_EtwRuntimeFileTime, None)
PlatformDiagnosticTraceSlotState = Int32
PlatformDiagnosticTraceSlotState_NotRunning: PlatformDiagnosticTraceSlotState = 0
PlatformDiagnosticTraceSlotState_Running: PlatformDiagnosticTraceSlotState = 1
PlatformDiagnosticTraceSlotState_Throttled: PlatformDiagnosticTraceSlotState = 2
PlatformDiagnosticTraceSlotType = Int32
PlatformDiagnosticTraceSlotType_Alternative: PlatformDiagnosticTraceSlotType = 0
PlatformDiagnosticTraceSlotType_AlwaysOn: PlatformDiagnosticTraceSlotType = 1
PlatformDiagnosticTraceSlotType_Mini: PlatformDiagnosticTraceSlotType = 2


make_ready(__name__)
