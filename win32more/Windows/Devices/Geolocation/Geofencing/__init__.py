from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Devices.Geolocation
import win32more.Windows.Devices.Geolocation.Geofencing
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Win32.System.WinRT
class Geofence(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Geolocation.Geofencing.IGeofence
    _classid_ = 'Windows.Devices.Geolocation.Geofencing.Geofence'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Devices.Geolocation.Geofencing.Geofence.Create(*args))
        elif len(args) == 4:
            super().__init__(move=win32more.Windows.Devices.Geolocation.Geofencing.Geofence.CreateWithMonitorStates(*args))
        elif len(args) == 5:
            super().__init__(move=win32more.Windows.Devices.Geolocation.Geofencing.Geofence.CreateWithMonitorStatesAndDwellTime(*args))
        elif len(args) == 7:
            super().__init__(move=win32more.Windows.Devices.Geolocation.Geofencing.Geofence.CreateWithMonitorStatesDwellTimeStartTimeAndDuration(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Devices.Geolocation.Geofencing.IGeofenceFactory, id: WinRT_String, geoshape: win32more.Windows.Devices.Geolocation.IGeoshape) -> win32more.Windows.Devices.Geolocation.Geofencing.Geofence: ...
    @winrt_factorymethod
    def CreateWithMonitorStates(cls: win32more.Windows.Devices.Geolocation.Geofencing.IGeofenceFactory, id: WinRT_String, geoshape: win32more.Windows.Devices.Geolocation.IGeoshape, monitoredStates: win32more.Windows.Devices.Geolocation.Geofencing.MonitoredGeofenceStates, singleUse: Boolean) -> win32more.Windows.Devices.Geolocation.Geofencing.Geofence: ...
    @winrt_factorymethod
    def CreateWithMonitorStatesAndDwellTime(cls: win32more.Windows.Devices.Geolocation.Geofencing.IGeofenceFactory, id: WinRT_String, geoshape: win32more.Windows.Devices.Geolocation.IGeoshape, monitoredStates: win32more.Windows.Devices.Geolocation.Geofencing.MonitoredGeofenceStates, singleUse: Boolean, dwellTime: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.Devices.Geolocation.Geofencing.Geofence: ...
    @winrt_factorymethod
    def CreateWithMonitorStatesDwellTimeStartTimeAndDuration(cls: win32more.Windows.Devices.Geolocation.Geofencing.IGeofenceFactory, id: WinRT_String, geoshape: win32more.Windows.Devices.Geolocation.IGeoshape, monitoredStates: win32more.Windows.Devices.Geolocation.Geofencing.MonitoredGeofenceStates, singleUse: Boolean, dwellTime: win32more.Windows.Foundation.TimeSpan, startTime: win32more.Windows.Foundation.DateTime, duration: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.Devices.Geolocation.Geofencing.Geofence: ...
    @winrt_mixinmethod
    def get_StartTime(self: win32more.Windows.Devices.Geolocation.Geofencing.IGeofence) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_Duration(self: win32more.Windows.Devices.Geolocation.Geofencing.IGeofence) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_DwellTime(self: win32more.Windows.Devices.Geolocation.Geofencing.IGeofence) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Devices.Geolocation.Geofencing.IGeofence) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_MonitoredStates(self: win32more.Windows.Devices.Geolocation.Geofencing.IGeofence) -> win32more.Windows.Devices.Geolocation.Geofencing.MonitoredGeofenceStates: ...
    @winrt_mixinmethod
    def get_Geoshape(self: win32more.Windows.Devices.Geolocation.Geofencing.IGeofence) -> win32more.Windows.Devices.Geolocation.IGeoshape: ...
    @winrt_mixinmethod
    def get_SingleUse(self: win32more.Windows.Devices.Geolocation.Geofencing.IGeofence) -> Boolean: ...
    Duration = property(get_Duration, None)
    DwellTime = property(get_DwellTime, None)
    Geoshape = property(get_Geoshape, None)
    Id = property(get_Id, None)
    MonitoredStates = property(get_MonitoredStates, None)
    SingleUse = property(get_SingleUse, None)
    StartTime = property(get_StartTime, None)
class _GeofenceMonitor_Meta_(ComPtr.__class__):
    pass
class GeofenceMonitor(ComPtr, metaclass=_GeofenceMonitor_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Geolocation.Geofencing.IGeofenceMonitor
    _classid_ = 'Windows.Devices.Geolocation.Geofencing.GeofenceMonitor'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Devices.Geolocation.Geofencing.IGeofenceMonitor) -> win32more.Windows.Devices.Geolocation.Geofencing.GeofenceMonitorStatus: ...
    @winrt_mixinmethod
    def get_Geofences(self: win32more.Windows.Devices.Geolocation.Geofencing.IGeofenceMonitor) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Devices.Geolocation.Geofencing.Geofence]: ...
    @winrt_mixinmethod
    def get_LastKnownGeoposition(self: win32more.Windows.Devices.Geolocation.Geofencing.IGeofenceMonitor) -> win32more.Windows.Devices.Geolocation.Geoposition: ...
    @winrt_mixinmethod
    def add_GeofenceStateChanged(self: win32more.Windows.Devices.Geolocation.Geofencing.IGeofenceMonitor, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Geolocation.Geofencing.GeofenceMonitor, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_GeofenceStateChanged(self: win32more.Windows.Devices.Geolocation.Geofencing.IGeofenceMonitor, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def ReadReports(self: win32more.Windows.Devices.Geolocation.Geofencing.IGeofenceMonitor) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Geolocation.Geofencing.GeofenceStateChangeReport]: ...
    @winrt_mixinmethod
    def add_StatusChanged(self: win32more.Windows.Devices.Geolocation.Geofencing.IGeofenceMonitor, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Geolocation.Geofencing.GeofenceMonitor, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StatusChanged(self: win32more.Windows.Devices.Geolocation.Geofencing.IGeofenceMonitor, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_Current(cls: win32more.Windows.Devices.Geolocation.Geofencing.IGeofenceMonitorStatics) -> win32more.Windows.Devices.Geolocation.Geofencing.GeofenceMonitor: ...
    Geofences = property(get_Geofences, None)
    LastKnownGeoposition = property(get_LastKnownGeoposition, None)
    Status = property(get_Status, None)
    _GeofenceMonitor_Meta_.Current = property(get_Current, None)
    GeofenceStateChanged = event()
    StatusChanged = event()
class GeofenceMonitorStatus(Enum, Int32):
    Ready = 0
    Initializing = 1
    NoData = 2
    Disabled = 3
    NotInitialized = 4
    NotAvailable = 5
class GeofenceRemovalReason(Enum, Int32):
    Used = 0
    Expired = 1
class GeofenceState(Enum, UInt32):
    None_ = 0
    Entered = 1
    Exited = 2
    Removed = 4
class GeofenceStateChangeReport(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Geolocation.Geofencing.IGeofenceStateChangeReport
    _classid_ = 'Windows.Devices.Geolocation.Geofencing.GeofenceStateChangeReport'
    @winrt_mixinmethod
    def get_NewState(self: win32more.Windows.Devices.Geolocation.Geofencing.IGeofenceStateChangeReport) -> win32more.Windows.Devices.Geolocation.Geofencing.GeofenceState: ...
    @winrt_mixinmethod
    def get_Geofence(self: win32more.Windows.Devices.Geolocation.Geofencing.IGeofenceStateChangeReport) -> win32more.Windows.Devices.Geolocation.Geofencing.Geofence: ...
    @winrt_mixinmethod
    def get_Geoposition(self: win32more.Windows.Devices.Geolocation.Geofencing.IGeofenceStateChangeReport) -> win32more.Windows.Devices.Geolocation.Geoposition: ...
    @winrt_mixinmethod
    def get_RemovalReason(self: win32more.Windows.Devices.Geolocation.Geofencing.IGeofenceStateChangeReport) -> win32more.Windows.Devices.Geolocation.Geofencing.GeofenceRemovalReason: ...
    Geofence = property(get_Geofence, None)
    Geoposition = property(get_Geoposition, None)
    NewState = property(get_NewState, None)
    RemovalReason = property(get_RemovalReason, None)
class IGeofence(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.Geofencing.IGeofence'
    _iid_ = Guid('{9c090823-edb8-47e0-8245-5bf61d321f2d}')
    @winrt_commethod(6)
    def get_StartTime(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_Duration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(8)
    def get_DwellTime(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_MonitoredStates(self) -> win32more.Windows.Devices.Geolocation.Geofencing.MonitoredGeofenceStates: ...
    @winrt_commethod(11)
    def get_Geoshape(self) -> win32more.Windows.Devices.Geolocation.IGeoshape: ...
    @winrt_commethod(12)
    def get_SingleUse(self) -> Boolean: ...
    Duration = property(get_Duration, None)
    DwellTime = property(get_DwellTime, None)
    Geoshape = property(get_Geoshape, None)
    Id = property(get_Id, None)
    MonitoredStates = property(get_MonitoredStates, None)
    SingleUse = property(get_SingleUse, None)
    StartTime = property(get_StartTime, None)
class IGeofenceFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.Geofencing.IGeofenceFactory'
    _iid_ = Guid('{841f624b-325f-4b90-bca7-2b8022a93796}')
    @winrt_commethod(6)
    def Create(self, id: WinRT_String, geoshape: win32more.Windows.Devices.Geolocation.IGeoshape) -> win32more.Windows.Devices.Geolocation.Geofencing.Geofence: ...
    @winrt_commethod(7)
    def CreateWithMonitorStates(self, id: WinRT_String, geoshape: win32more.Windows.Devices.Geolocation.IGeoshape, monitoredStates: win32more.Windows.Devices.Geolocation.Geofencing.MonitoredGeofenceStates, singleUse: Boolean) -> win32more.Windows.Devices.Geolocation.Geofencing.Geofence: ...
    @winrt_commethod(8)
    def CreateWithMonitorStatesAndDwellTime(self, id: WinRT_String, geoshape: win32more.Windows.Devices.Geolocation.IGeoshape, monitoredStates: win32more.Windows.Devices.Geolocation.Geofencing.MonitoredGeofenceStates, singleUse: Boolean, dwellTime: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.Devices.Geolocation.Geofencing.Geofence: ...
    @winrt_commethod(9)
    def CreateWithMonitorStatesDwellTimeStartTimeAndDuration(self, id: WinRT_String, geoshape: win32more.Windows.Devices.Geolocation.IGeoshape, monitoredStates: win32more.Windows.Devices.Geolocation.Geofencing.MonitoredGeofenceStates, singleUse: Boolean, dwellTime: win32more.Windows.Foundation.TimeSpan, startTime: win32more.Windows.Foundation.DateTime, duration: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.Devices.Geolocation.Geofencing.Geofence: ...
class IGeofenceMonitor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.Geofencing.IGeofenceMonitor'
    _iid_ = Guid('{4c0f5f78-1c1f-4621-bbbd-833b92247226}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Devices.Geolocation.Geofencing.GeofenceMonitorStatus: ...
    @winrt_commethod(7)
    def get_Geofences(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Devices.Geolocation.Geofencing.Geofence]: ...
    @winrt_commethod(8)
    def get_LastKnownGeoposition(self) -> win32more.Windows.Devices.Geolocation.Geoposition: ...
    @winrt_commethod(9)
    def add_GeofenceStateChanged(self, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Geolocation.Geofencing.GeofenceMonitor, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_GeofenceStateChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def ReadReports(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Geolocation.Geofencing.GeofenceStateChangeReport]: ...
    @winrt_commethod(12)
    def add_StatusChanged(self, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Geolocation.Geofencing.GeofenceMonitor, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_StatusChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Geofences = property(get_Geofences, None)
    LastKnownGeoposition = property(get_LastKnownGeoposition, None)
    Status = property(get_Status, None)
    GeofenceStateChanged = event()
    StatusChanged = event()
class IGeofenceMonitorStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.Geofencing.IGeofenceMonitorStatics'
    _iid_ = Guid('{2dd32fcf-7e75-4899-ace3-2bd0a65cce06}')
    @winrt_commethod(6)
    def get_Current(self) -> win32more.Windows.Devices.Geolocation.Geofencing.GeofenceMonitor: ...
    Current = property(get_Current, None)
class IGeofenceStateChangeReport(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.Geofencing.IGeofenceStateChangeReport'
    _iid_ = Guid('{9a243c18-2464-4c89-be05-b3ffff5babc5}')
    @winrt_commethod(6)
    def get_NewState(self) -> win32more.Windows.Devices.Geolocation.Geofencing.GeofenceState: ...
    @winrt_commethod(7)
    def get_Geofence(self) -> win32more.Windows.Devices.Geolocation.Geofencing.Geofence: ...
    @winrt_commethod(8)
    def get_Geoposition(self) -> win32more.Windows.Devices.Geolocation.Geoposition: ...
    @winrt_commethod(9)
    def get_RemovalReason(self) -> win32more.Windows.Devices.Geolocation.Geofencing.GeofenceRemovalReason: ...
    Geofence = property(get_Geofence, None)
    Geoposition = property(get_Geoposition, None)
    NewState = property(get_NewState, None)
    RemovalReason = property(get_RemovalReason, None)
class MonitoredGeofenceStates(Enum, UInt32):
    None_ = 0
    Entered = 1
    Exited = 2
    Removed = 4


make_ready(__name__)
