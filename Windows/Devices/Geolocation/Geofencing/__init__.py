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
import Windows.Devices.Geolocation
import Windows.Devices.Geolocation.Geofencing
import Windows.Foundation
import Windows.Foundation.Collections
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class Geofence(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Geolocation.Geofencing.IGeofence
    _classid_ = 'Windows.Devices.Geolocation.Geofencing.Geofence'
    @winrt_factorymethod
    def Create(cls: Windows.Devices.Geolocation.Geofencing.IGeofenceFactory, id: WinRT_String, geoshape: Windows.Devices.Geolocation.IGeoshape) -> Windows.Devices.Geolocation.Geofencing.Geofence: ...
    @winrt_factorymethod
    def CreateWithMonitorStates(cls: Windows.Devices.Geolocation.Geofencing.IGeofenceFactory, id: WinRT_String, geoshape: Windows.Devices.Geolocation.IGeoshape, monitoredStates: Windows.Devices.Geolocation.Geofencing.MonitoredGeofenceStates, singleUse: Boolean) -> Windows.Devices.Geolocation.Geofencing.Geofence: ...
    @winrt_factorymethod
    def CreateWithMonitorStatesAndDwellTime(cls: Windows.Devices.Geolocation.Geofencing.IGeofenceFactory, id: WinRT_String, geoshape: Windows.Devices.Geolocation.IGeoshape, monitoredStates: Windows.Devices.Geolocation.Geofencing.MonitoredGeofenceStates, singleUse: Boolean, dwellTime: Windows.Foundation.TimeSpan) -> Windows.Devices.Geolocation.Geofencing.Geofence: ...
    @winrt_factorymethod
    def CreateWithMonitorStatesDwellTimeStartTimeAndDuration(cls: Windows.Devices.Geolocation.Geofencing.IGeofenceFactory, id: WinRT_String, geoshape: Windows.Devices.Geolocation.IGeoshape, monitoredStates: Windows.Devices.Geolocation.Geofencing.MonitoredGeofenceStates, singleUse: Boolean, dwellTime: Windows.Foundation.TimeSpan, startTime: Windows.Foundation.DateTime, duration: Windows.Foundation.TimeSpan) -> Windows.Devices.Geolocation.Geofencing.Geofence: ...
    @winrt_mixinmethod
    def get_StartTime(self: Windows.Devices.Geolocation.Geofencing.IGeofence) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_Duration(self: Windows.Devices.Geolocation.Geofencing.IGeofence) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_DwellTime(self: Windows.Devices.Geolocation.Geofencing.IGeofence) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Devices.Geolocation.Geofencing.IGeofence) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_MonitoredStates(self: Windows.Devices.Geolocation.Geofencing.IGeofence) -> Windows.Devices.Geolocation.Geofencing.MonitoredGeofenceStates: ...
    @winrt_mixinmethod
    def get_Geoshape(self: Windows.Devices.Geolocation.Geofencing.IGeofence) -> Windows.Devices.Geolocation.IGeoshape: ...
    @winrt_mixinmethod
    def get_SingleUse(self: Windows.Devices.Geolocation.Geofencing.IGeofence) -> Boolean: ...
    StartTime = property(get_StartTime, None)
    Duration = property(get_Duration, None)
    DwellTime = property(get_DwellTime, None)
    Id = property(get_Id, None)
    MonitoredStates = property(get_MonitoredStates, None)
    Geoshape = property(get_Geoshape, None)
    SingleUse = property(get_SingleUse, None)
class _GeofenceMonitor_Meta_(ComPtr.__class__):
    pass
class GeofenceMonitor(ComPtr, metaclass=_GeofenceMonitor_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Geolocation.Geofencing.IGeofenceMonitor
    _classid_ = 'Windows.Devices.Geolocation.Geofencing.GeofenceMonitor'
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.Geolocation.Geofencing.IGeofenceMonitor) -> Windows.Devices.Geolocation.Geofencing.GeofenceMonitorStatus: ...
    @winrt_mixinmethod
    def get_Geofences(self: Windows.Devices.Geolocation.Geofencing.IGeofenceMonitor) -> Windows.Foundation.Collections.IVector[Windows.Devices.Geolocation.Geofencing.Geofence]: ...
    @winrt_mixinmethod
    def get_LastKnownGeoposition(self: Windows.Devices.Geolocation.Geofencing.IGeofenceMonitor) -> Windows.Devices.Geolocation.Geoposition: ...
    @winrt_mixinmethod
    def add_GeofenceStateChanged(self: Windows.Devices.Geolocation.Geofencing.IGeofenceMonitor, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Devices.Geolocation.Geofencing.GeofenceMonitor, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_GeofenceStateChanged(self: Windows.Devices.Geolocation.Geofencing.IGeofenceMonitor, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def ReadReports(self: Windows.Devices.Geolocation.Geofencing.IGeofenceMonitor) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Geolocation.Geofencing.GeofenceStateChangeReport]: ...
    @winrt_mixinmethod
    def add_StatusChanged(self: Windows.Devices.Geolocation.Geofencing.IGeofenceMonitor, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Devices.Geolocation.Geofencing.GeofenceMonitor, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StatusChanged(self: Windows.Devices.Geolocation.Geofencing.IGeofenceMonitor, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_Current(cls: Windows.Devices.Geolocation.Geofencing.IGeofenceMonitorStatics) -> Windows.Devices.Geolocation.Geofencing.GeofenceMonitor: ...
    Status = property(get_Status, None)
    Geofences = property(get_Geofences, None)
    LastKnownGeoposition = property(get_LastKnownGeoposition, None)
    _GeofenceMonitor_Meta_.Current = property(get_Current.__wrapped__, None)
GeofenceMonitorStatus = Int32
GeofenceMonitorStatus_Ready: GeofenceMonitorStatus = 0
GeofenceMonitorStatus_Initializing: GeofenceMonitorStatus = 1
GeofenceMonitorStatus_NoData: GeofenceMonitorStatus = 2
GeofenceMonitorStatus_Disabled: GeofenceMonitorStatus = 3
GeofenceMonitorStatus_NotInitialized: GeofenceMonitorStatus = 4
GeofenceMonitorStatus_NotAvailable: GeofenceMonitorStatus = 5
GeofenceRemovalReason = Int32
GeofenceRemovalReason_Used: GeofenceRemovalReason = 0
GeofenceRemovalReason_Expired: GeofenceRemovalReason = 1
GeofenceState = UInt32
GeofenceState_None: GeofenceState = 0
GeofenceState_Entered: GeofenceState = 1
GeofenceState_Exited: GeofenceState = 2
GeofenceState_Removed: GeofenceState = 4
class GeofenceStateChangeReport(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Geolocation.Geofencing.IGeofenceStateChangeReport
    _classid_ = 'Windows.Devices.Geolocation.Geofencing.GeofenceStateChangeReport'
    @winrt_mixinmethod
    def get_NewState(self: Windows.Devices.Geolocation.Geofencing.IGeofenceStateChangeReport) -> Windows.Devices.Geolocation.Geofencing.GeofenceState: ...
    @winrt_mixinmethod
    def get_Geofence(self: Windows.Devices.Geolocation.Geofencing.IGeofenceStateChangeReport) -> Windows.Devices.Geolocation.Geofencing.Geofence: ...
    @winrt_mixinmethod
    def get_Geoposition(self: Windows.Devices.Geolocation.Geofencing.IGeofenceStateChangeReport) -> Windows.Devices.Geolocation.Geoposition: ...
    @winrt_mixinmethod
    def get_RemovalReason(self: Windows.Devices.Geolocation.Geofencing.IGeofenceStateChangeReport) -> Windows.Devices.Geolocation.Geofencing.GeofenceRemovalReason: ...
    NewState = property(get_NewState, None)
    Geofence = property(get_Geofence, None)
    Geoposition = property(get_Geoposition, None)
    RemovalReason = property(get_RemovalReason, None)
class IGeofence(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.Geofencing.IGeofence'
    _iid_ = Guid('{9c090823-edb8-47e0-8245-5bf61d321f2d}')
    @winrt_commethod(6)
    def get_StartTime(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_Duration(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(8)
    def get_DwellTime(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_MonitoredStates(self) -> Windows.Devices.Geolocation.Geofencing.MonitoredGeofenceStates: ...
    @winrt_commethod(11)
    def get_Geoshape(self) -> Windows.Devices.Geolocation.IGeoshape: ...
    @winrt_commethod(12)
    def get_SingleUse(self) -> Boolean: ...
    StartTime = property(get_StartTime, None)
    Duration = property(get_Duration, None)
    DwellTime = property(get_DwellTime, None)
    Id = property(get_Id, None)
    MonitoredStates = property(get_MonitoredStates, None)
    Geoshape = property(get_Geoshape, None)
    SingleUse = property(get_SingleUse, None)
class IGeofenceFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.Geofencing.IGeofenceFactory'
    _iid_ = Guid('{841f624b-325f-4b90-bca7-2b8022a93796}')
    @winrt_commethod(6)
    def Create(self, id: WinRT_String, geoshape: Windows.Devices.Geolocation.IGeoshape) -> Windows.Devices.Geolocation.Geofencing.Geofence: ...
    @winrt_commethod(7)
    def CreateWithMonitorStates(self, id: WinRT_String, geoshape: Windows.Devices.Geolocation.IGeoshape, monitoredStates: Windows.Devices.Geolocation.Geofencing.MonitoredGeofenceStates, singleUse: Boolean) -> Windows.Devices.Geolocation.Geofencing.Geofence: ...
    @winrt_commethod(8)
    def CreateWithMonitorStatesAndDwellTime(self, id: WinRT_String, geoshape: Windows.Devices.Geolocation.IGeoshape, monitoredStates: Windows.Devices.Geolocation.Geofencing.MonitoredGeofenceStates, singleUse: Boolean, dwellTime: Windows.Foundation.TimeSpan) -> Windows.Devices.Geolocation.Geofencing.Geofence: ...
    @winrt_commethod(9)
    def CreateWithMonitorStatesDwellTimeStartTimeAndDuration(self, id: WinRT_String, geoshape: Windows.Devices.Geolocation.IGeoshape, monitoredStates: Windows.Devices.Geolocation.Geofencing.MonitoredGeofenceStates, singleUse: Boolean, dwellTime: Windows.Foundation.TimeSpan, startTime: Windows.Foundation.DateTime, duration: Windows.Foundation.TimeSpan) -> Windows.Devices.Geolocation.Geofencing.Geofence: ...
class IGeofenceMonitor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.Geofencing.IGeofenceMonitor'
    _iid_ = Guid('{4c0f5f78-1c1f-4621-bbbd-833b92247226}')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Devices.Geolocation.Geofencing.GeofenceMonitorStatus: ...
    @winrt_commethod(7)
    def get_Geofences(self) -> Windows.Foundation.Collections.IVector[Windows.Devices.Geolocation.Geofencing.Geofence]: ...
    @winrt_commethod(8)
    def get_LastKnownGeoposition(self) -> Windows.Devices.Geolocation.Geoposition: ...
    @winrt_commethod(9)
    def add_GeofenceStateChanged(self, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Devices.Geolocation.Geofencing.GeofenceMonitor, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_GeofenceStateChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def ReadReports(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Geolocation.Geofencing.GeofenceStateChangeReport]: ...
    @winrt_commethod(12)
    def add_StatusChanged(self, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Devices.Geolocation.Geofencing.GeofenceMonitor, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_StatusChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Status = property(get_Status, None)
    Geofences = property(get_Geofences, None)
    LastKnownGeoposition = property(get_LastKnownGeoposition, None)
class IGeofenceMonitorStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.Geofencing.IGeofenceMonitorStatics'
    _iid_ = Guid('{2dd32fcf-7e75-4899-ace3-2bd0a65cce06}')
    @winrt_commethod(6)
    def get_Current(self) -> Windows.Devices.Geolocation.Geofencing.GeofenceMonitor: ...
    Current = property(get_Current, None)
class IGeofenceStateChangeReport(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.Geofencing.IGeofenceStateChangeReport'
    _iid_ = Guid('{9a243c18-2464-4c89-be05-b3ffff5babc5}')
    @winrt_commethod(6)
    def get_NewState(self) -> Windows.Devices.Geolocation.Geofencing.GeofenceState: ...
    @winrt_commethod(7)
    def get_Geofence(self) -> Windows.Devices.Geolocation.Geofencing.Geofence: ...
    @winrt_commethod(8)
    def get_Geoposition(self) -> Windows.Devices.Geolocation.Geoposition: ...
    @winrt_commethod(9)
    def get_RemovalReason(self) -> Windows.Devices.Geolocation.Geofencing.GeofenceRemovalReason: ...
    NewState = property(get_NewState, None)
    Geofence = property(get_Geofence, None)
    Geoposition = property(get_Geoposition, None)
    RemovalReason = property(get_RemovalReason, None)
MonitoredGeofenceStates = UInt32
MonitoredGeofenceStates_None: MonitoredGeofenceStates = 0
MonitoredGeofenceStates_Entered: MonitoredGeofenceStates = 1
MonitoredGeofenceStates_Exited: MonitoredGeofenceStates = 2
MonitoredGeofenceStates_Removed: MonitoredGeofenceStates = 4
make_head(_module, 'Geofence')
make_head(_module, 'GeofenceMonitor')
make_head(_module, 'GeofenceStateChangeReport')
make_head(_module, 'IGeofence')
make_head(_module, 'IGeofenceFactory')
make_head(_module, 'IGeofenceMonitor')
make_head(_module, 'IGeofenceMonitorStatics')
make_head(_module, 'IGeofenceStateChangeReport')
