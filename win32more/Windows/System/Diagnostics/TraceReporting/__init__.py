from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
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
    IsAutoLogger = property(get_IsAutoLogger, None)
    IsExclusive = property(get_IsExclusive, None)
    MaxTraceDurationFileTime = property(get_MaxTraceDurationFileTime, None)
    Priority = property(get_Priority, None)
    ProfileHash = property(get_ProfileHash, None)
    ScenarioId = property(get_ScenarioId, None)
class IPlatformDiagnosticTraceRuntimeInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Diagnostics.TraceReporting.IPlatformDiagnosticTraceRuntimeInfo'
    _iid_ = Guid('{3d4d5e2d-01d8-4768-8554-1eb1ca610986}')
    @winrt_commethod(6)
    def get_RuntimeFileTime(self) -> Int64: ...
    @winrt_commethod(7)
    def get_EtwRuntimeFileTime(self) -> Int64: ...
    EtwRuntimeFileTime = property(get_EtwRuntimeFileTime, None)
    RuntimeFileTime = property(get_RuntimeFileTime, None)
class PlatformDiagnosticActionState(Enum, Int32):
    Success = 0
    FreeNetworkNotAvailable = 1
    ACPowerNotAvailable = 2
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
class PlatformDiagnosticEscalationType(Enum, Int32):
    OnCompletion = 0
    OnFailure = 1
class PlatformDiagnosticEventBufferLatencies(Enum, UInt32):
    Normal = 1
    CostDeferred = 2
    Realtime = 4
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
    IsAutoLogger = property(get_IsAutoLogger, None)
    IsExclusive = property(get_IsExclusive, None)
    MaxTraceDurationFileTime = property(get_MaxTraceDurationFileTime, None)
    Priority = property(get_Priority, None)
    ProfileHash = property(get_ProfileHash, None)
    ScenarioId = property(get_ScenarioId, None)
class PlatformDiagnosticTracePriority(Enum, Int32):
    Normal = 0
    UserElevated = 1
class PlatformDiagnosticTraceRuntimeInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.Diagnostics.TraceReporting.IPlatformDiagnosticTraceRuntimeInfo
    _classid_ = 'Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticTraceRuntimeInfo'
    @winrt_mixinmethod
    def get_RuntimeFileTime(self: win32more.Windows.System.Diagnostics.TraceReporting.IPlatformDiagnosticTraceRuntimeInfo) -> Int64: ...
    @winrt_mixinmethod
    def get_EtwRuntimeFileTime(self: win32more.Windows.System.Diagnostics.TraceReporting.IPlatformDiagnosticTraceRuntimeInfo) -> Int64: ...
    EtwRuntimeFileTime = property(get_EtwRuntimeFileTime, None)
    RuntimeFileTime = property(get_RuntimeFileTime, None)
class PlatformDiagnosticTraceSlotState(Enum, Int32):
    NotRunning = 0
    Running = 1
    Throttled = 2
class PlatformDiagnosticTraceSlotType(Enum, Int32):
    Alternative = 0
    AlwaysOn = 1
    Mini = 2


make_ready(__name__)
