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
import Windows.Foundation.Collections
import Windows.System.Diagnostics.TraceReporting
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IPlatformDiagnosticActionsStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{c1145cfa-9292-4267-890a-9ea3ed072312}')
    @winrt_commethod(6)
    def IsScenarioEnabled(self, scenarioId: Guid) -> Boolean: ...
    @winrt_commethod(7)
    def TryEscalateScenario(self, scenarioId: Guid, escalationType: Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticEscalationType, outputDirectory: WinRT_String, timestampOutputDirectory: Boolean, forceEscalationUpload: Boolean, triggers: Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]) -> Boolean: ...
    @winrt_commethod(8)
    def DownloadLatestSettingsForNamespace(self, partner: WinRT_String, feature: WinRT_String, isScenarioNamespace: Boolean, downloadOverCostedNetwork: Boolean, downloadOverBattery: Boolean) -> Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticActionState: ...
    @winrt_commethod(9)
    def GetActiveScenarioList(self) -> Windows.Foundation.Collections.IVectorView[Guid]: ...
    @winrt_commethod(10)
    def ForceUpload(self, latency: Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticEventBufferLatencies, uploadOverCostedNetwork: Boolean, uploadOverBattery: Boolean) -> Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticActionState: ...
    @winrt_commethod(11)
    def IsTraceRunning(self, slotType: Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticTraceSlotType, scenarioId: Guid, traceProfileHash: UInt64) -> Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticTraceSlotState: ...
    @winrt_commethod(12)
    def GetActiveTraceRuntime(self, slotType: Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticTraceSlotType) -> Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticTraceRuntimeInfo: ...
    @winrt_commethod(13)
    def GetKnownTraceList(self, slotType: Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticTraceSlotType) -> Windows.Foundation.Collections.IVectorView[Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticTraceInfo]: ...
class IPlatformDiagnosticTraceInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    def get_Priority(self) -> Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticTracePriority: ...
    ScenarioId = property(get_ScenarioId, None)
    ProfileHash = property(get_ProfileHash, None)
    IsExclusive = property(get_IsExclusive, None)
    IsAutoLogger = property(get_IsAutoLogger, None)
    MaxTraceDurationFileTime = property(get_MaxTraceDurationFileTime, None)
    Priority = property(get_Priority, None)
class IPlatformDiagnosticTraceRuntimeInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticActions'
    @winrt_classmethod
    def IsScenarioEnabled(cls: Windows.System.Diagnostics.TraceReporting.IPlatformDiagnosticActionsStatics, scenarioId: Guid) -> Boolean: ...
    @winrt_classmethod
    def TryEscalateScenario(cls: Windows.System.Diagnostics.TraceReporting.IPlatformDiagnosticActionsStatics, scenarioId: Guid, escalationType: Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticEscalationType, outputDirectory: WinRT_String, timestampOutputDirectory: Boolean, forceEscalationUpload: Boolean, triggers: Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]) -> Boolean: ...
    @winrt_classmethod
    def DownloadLatestSettingsForNamespace(cls: Windows.System.Diagnostics.TraceReporting.IPlatformDiagnosticActionsStatics, partner: WinRT_String, feature: WinRT_String, isScenarioNamespace: Boolean, downloadOverCostedNetwork: Boolean, downloadOverBattery: Boolean) -> Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticActionState: ...
    @winrt_classmethod
    def GetActiveScenarioList(cls: Windows.System.Diagnostics.TraceReporting.IPlatformDiagnosticActionsStatics) -> Windows.Foundation.Collections.IVectorView[Guid]: ...
    @winrt_classmethod
    def ForceUpload(cls: Windows.System.Diagnostics.TraceReporting.IPlatformDiagnosticActionsStatics, latency: Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticEventBufferLatencies, uploadOverCostedNetwork: Boolean, uploadOverBattery: Boolean) -> Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticActionState: ...
    @winrt_classmethod
    def IsTraceRunning(cls: Windows.System.Diagnostics.TraceReporting.IPlatformDiagnosticActionsStatics, slotType: Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticTraceSlotType, scenarioId: Guid, traceProfileHash: UInt64) -> Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticTraceSlotState: ...
    @winrt_classmethod
    def GetActiveTraceRuntime(cls: Windows.System.Diagnostics.TraceReporting.IPlatformDiagnosticActionsStatics, slotType: Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticTraceSlotType) -> Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticTraceRuntimeInfo: ...
    @winrt_classmethod
    def GetKnownTraceList(cls: Windows.System.Diagnostics.TraceReporting.IPlatformDiagnosticActionsStatics, slotType: Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticTraceSlotType) -> Windows.Foundation.Collections.IVectorView[Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticTraceInfo]: ...
PlatformDiagnosticEscalationType = Int32
PlatformDiagnosticEscalationType_OnCompletion: PlatformDiagnosticEscalationType = 0
PlatformDiagnosticEscalationType_OnFailure: PlatformDiagnosticEscalationType = 1
PlatformDiagnosticEventBufferLatencies = UInt32
PlatformDiagnosticEventBufferLatencies_Normal: PlatformDiagnosticEventBufferLatencies = 1
PlatformDiagnosticEventBufferLatencies_CostDeferred: PlatformDiagnosticEventBufferLatencies = 2
PlatformDiagnosticEventBufferLatencies_Realtime: PlatformDiagnosticEventBufferLatencies = 4
class PlatformDiagnosticTraceInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticTraceInfo'
    @winrt_mixinmethod
    def get_ScenarioId(self: Windows.System.Diagnostics.TraceReporting.IPlatformDiagnosticTraceInfo) -> Guid: ...
    @winrt_mixinmethod
    def get_ProfileHash(self: Windows.System.Diagnostics.TraceReporting.IPlatformDiagnosticTraceInfo) -> UInt64: ...
    @winrt_mixinmethod
    def get_IsExclusive(self: Windows.System.Diagnostics.TraceReporting.IPlatformDiagnosticTraceInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsAutoLogger(self: Windows.System.Diagnostics.TraceReporting.IPlatformDiagnosticTraceInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_MaxTraceDurationFileTime(self: Windows.System.Diagnostics.TraceReporting.IPlatformDiagnosticTraceInfo) -> Int64: ...
    @winrt_mixinmethod
    def get_Priority(self: Windows.System.Diagnostics.TraceReporting.IPlatformDiagnosticTraceInfo) -> Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticTracePriority: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticTraceRuntimeInfo'
    @winrt_mixinmethod
    def get_RuntimeFileTime(self: Windows.System.Diagnostics.TraceReporting.IPlatformDiagnosticTraceRuntimeInfo) -> Int64: ...
    @winrt_mixinmethod
    def get_EtwRuntimeFileTime(self: Windows.System.Diagnostics.TraceReporting.IPlatformDiagnosticTraceRuntimeInfo) -> Int64: ...
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
make_head(_module, 'IPlatformDiagnosticActionsStatics')
make_head(_module, 'IPlatformDiagnosticTraceInfo')
make_head(_module, 'IPlatformDiagnosticTraceRuntimeInfo')
make_head(_module, 'PlatformDiagnosticActions')
make_head(_module, 'PlatformDiagnosticTraceInfo')
make_head(_module, 'PlatformDiagnosticTraceRuntimeInfo')
