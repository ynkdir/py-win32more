from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Devices.Geolocation
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Foundation.Numerics
import win32more.Windows.Services.Maps
import win32more.Windows.Services.Maps.LocalSearch
import win32more.Windows.Storage.Streams
import win32more.Windows.UI
import win32more.Windows.UI.Xaml
import win32more.Windows.UI.Xaml.Controls
import win32more.Windows.UI.Xaml.Controls.Maps
import win32more.Windows.Win32.System.WinRT
class CustomMapTileDataSource(ComPtr):
    extends: win32more.Windows.UI.Xaml.Controls.Maps.MapTileDataSource
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.ICustomMapTileDataSource
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.CustomMapTileDataSource'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.CustomMapTileDataSource.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Controls.Maps.ICustomMapTileDataSourceFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Maps.CustomMapTileDataSource: ...
    @winrt_mixinmethod
    def add_BitmapRequested(self: win32more.Windows.UI.Xaml.Controls.Maps.ICustomMapTileDataSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.CustomMapTileDataSource, win32more.Windows.UI.Xaml.Controls.Maps.MapTileBitmapRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_BitmapRequested(self: win32more.Windows.UI.Xaml.Controls.Maps.ICustomMapTileDataSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    BitmapRequested = event()
class HttpMapTileDataSource(ComPtr):
    extends: win32more.Windows.UI.Xaml.Controls.Maps.MapTileDataSource
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IHttpMapTileDataSource
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.HttpMapTileDataSource'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.HttpMapTileDataSource.CreateInstance(*args, None, None))
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.HttpMapTileDataSource.CreateInstanceWithUriFormatString(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Controls.Maps.IHttpMapTileDataSourceFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Maps.HttpMapTileDataSource: ...
    @winrt_factorymethod
    def CreateInstanceWithUriFormatString(cls: win32more.Windows.UI.Xaml.Controls.Maps.IHttpMapTileDataSourceFactory, uriFormatString: WinRT_String, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Maps.HttpMapTileDataSource: ...
    @winrt_mixinmethod
    def get_UriFormatString(self: win32more.Windows.UI.Xaml.Controls.Maps.IHttpMapTileDataSource) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_UriFormatString(self: win32more.Windows.UI.Xaml.Controls.Maps.IHttpMapTileDataSource, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_AdditionalRequestHeaders(self: win32more.Windows.UI.Xaml.Controls.Maps.IHttpMapTileDataSource) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def get_AllowCaching(self: win32more.Windows.UI.Xaml.Controls.Maps.IHttpMapTileDataSource) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowCaching(self: win32more.Windows.UI.Xaml.Controls.Maps.IHttpMapTileDataSource, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def add_UriRequested(self: win32more.Windows.UI.Xaml.Controls.Maps.IHttpMapTileDataSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.HttpMapTileDataSource, win32more.Windows.UI.Xaml.Controls.Maps.MapTileUriRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UriRequested(self: win32more.Windows.UI.Xaml.Controls.Maps.IHttpMapTileDataSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    AdditionalRequestHeaders = property(get_AdditionalRequestHeaders, None)
    AllowCaching = property(get_AllowCaching, put_AllowCaching)
    UriFormatString = property(get_UriFormatString, put_UriFormatString)
    UriRequested = event()
class ICustomMapTileDataSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.ICustomMapTileDataSource'
    _iid_ = Guid('{65da384a-2db1-4be1-b155-3d0c9ecf4799}')
    @winrt_commethod(6)
    def add_BitmapRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.CustomMapTileDataSource, win32more.Windows.UI.Xaml.Controls.Maps.MapTileBitmapRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_BitmapRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    BitmapRequested = event()
class ICustomMapTileDataSourceFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.ICustomMapTileDataSourceFactory'
    _iid_ = Guid('{c8477947-c955-4f22-9444-a1d8d744af11}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Maps.CustomMapTileDataSource: ...
class IHttpMapTileDataSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IHttpMapTileDataSource'
    _iid_ = Guid('{9d03cb5c-fd79-4795-87be-7e54ca0b37d0}')
    @winrt_commethod(6)
    def get_UriFormatString(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_UriFormatString(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_AdditionalRequestHeaders(self) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_commethod(9)
    def get_AllowCaching(self) -> Boolean: ...
    @winrt_commethod(10)
    def put_AllowCaching(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def add_UriRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.HttpMapTileDataSource, win32more.Windows.UI.Xaml.Controls.Maps.MapTileUriRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_UriRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    AdditionalRequestHeaders = property(get_AdditionalRequestHeaders, None)
    AllowCaching = property(get_AllowCaching, put_AllowCaching)
    UriFormatString = property(get_UriFormatString, put_UriFormatString)
    UriRequested = event()
class IHttpMapTileDataSourceFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IHttpMapTileDataSourceFactory'
    _iid_ = Guid('{53b4b107-84dc-4291-89f8-6d0bb612a055}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Maps.HttpMapTileDataSource: ...
    @winrt_commethod(7)
    def CreateInstanceWithUriFormatString(self, uriFormatString: WinRT_String, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Maps.HttpMapTileDataSource: ...
class ILocalMapTileDataSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.ILocalMapTileDataSource'
    _iid_ = Guid('{616257b5-9108-4f12-8bf4-bb3c8f6274e5}')
    @winrt_commethod(6)
    def get_UriFormatString(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_UriFormatString(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def add_UriRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.LocalMapTileDataSource, win32more.Windows.UI.Xaml.Controls.Maps.MapTileUriRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_UriRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    UriFormatString = property(get_UriFormatString, put_UriFormatString)
    UriRequested = event()
class ILocalMapTileDataSourceFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.ILocalMapTileDataSourceFactory'
    _iid_ = Guid('{c5cfe9fc-72ac-4839-8a0d-011f24693c79}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Maps.LocalMapTileDataSource: ...
    @winrt_commethod(7)
    def CreateInstanceWithUriFormatString(self, uriFormatString: WinRT_String, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Maps.LocalMapTileDataSource: ...
class IMapActualCameraChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapActualCameraChangedEventArgs'
    _iid_ = Guid('{daa080da-b7f4-422c-a618-bbaa7c1d814c}')
    @winrt_commethod(6)
    def get_Camera(self) -> win32more.Windows.UI.Xaml.Controls.Maps.MapCamera: ...
    Camera = property(get_Camera, None)
class IMapActualCameraChangedEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapActualCameraChangedEventArgs2'
    _iid_ = Guid('{7ba4c7e5-10dc-455a-9d04-1d72fb6d9b93}')
    @winrt_commethod(6)
    def get_ChangeReason(self) -> win32more.Windows.UI.Xaml.Controls.Maps.MapCameraChangeReason: ...
    ChangeReason = property(get_ChangeReason, None)
class IMapActualCameraChangingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapActualCameraChangingEventArgs'
    _iid_ = Guid('{6b0dbed6-93f7-4682-8de5-a47a1cc7a945}')
    @winrt_commethod(6)
    def get_Camera(self) -> win32more.Windows.UI.Xaml.Controls.Maps.MapCamera: ...
    Camera = property(get_Camera, None)
class IMapActualCameraChangingEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapActualCameraChangingEventArgs2'
    _iid_ = Guid('{f2867897-40ac-4e8a-a927-510f3846a47e}')
    @winrt_commethod(6)
    def get_ChangeReason(self) -> win32more.Windows.UI.Xaml.Controls.Maps.MapCameraChangeReason: ...
    ChangeReason = property(get_ChangeReason, None)
class IMapBillboard(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapBillboard'
    _iid_ = Guid('{1694259d-0ae2-4f42-a02e-292ca835d39d}')
    @winrt_commethod(6)
    def get_Location(self) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(7)
    def put_Location(self, value: win32more.Windows.Devices.Geolocation.Geopoint) -> Void: ...
    @winrt_commethod(8)
    def get_NormalizedAnchorPoint(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(9)
    def put_NormalizedAnchorPoint(self, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(10)
    def get_Image(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(11)
    def put_Image(self, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_commethod(12)
    def get_CollisionBehaviorDesired(self) -> win32more.Windows.UI.Xaml.Controls.Maps.MapElementCollisionBehavior: ...
    @winrt_commethod(13)
    def put_CollisionBehaviorDesired(self, value: win32more.Windows.UI.Xaml.Controls.Maps.MapElementCollisionBehavior) -> Void: ...
    @winrt_commethod(14)
    def get_ReferenceCamera(self) -> win32more.Windows.UI.Xaml.Controls.Maps.MapCamera: ...
    CollisionBehaviorDesired = property(get_CollisionBehaviorDesired, put_CollisionBehaviorDesired)
    Image = property(get_Image, put_Image)
    Location = property(get_Location, put_Location)
    NormalizedAnchorPoint = property(get_NormalizedAnchorPoint, put_NormalizedAnchorPoint)
    ReferenceCamera = property(get_ReferenceCamera, None)
class IMapBillboardFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapBillboardFactory'
    _iid_ = Guid('{be45a4c5-8f09-4b86-ae28-783740eb8b31}')
    @winrt_commethod(6)
    def CreateInstanceFromCamera(self, camera: win32more.Windows.UI.Xaml.Controls.Maps.MapCamera) -> win32more.Windows.UI.Xaml.Controls.Maps.MapBillboard: ...
class IMapBillboardStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapBillboardStatics'
    _iid_ = Guid('{fdf839fe-e1f7-4fb0-8887-7da68c647333}')
    @winrt_commethod(6)
    def get_LocationProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_NormalizedAnchorPointProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_CollisionBehaviorDesiredProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    CollisionBehaviorDesiredProperty = property(get_CollisionBehaviorDesiredProperty, None)
    LocationProperty = property(get_LocationProperty, None)
    NormalizedAnchorPointProperty = property(get_NormalizedAnchorPointProperty, None)
class IMapCamera(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapCamera'
    _iid_ = Guid('{53a6b623-c0f8-4d8b-ad1e-a59598ea840b}')
    @winrt_commethod(6)
    def get_Location(self) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(7)
    def put_Location(self, value: win32more.Windows.Devices.Geolocation.Geopoint) -> Void: ...
    @winrt_commethod(8)
    def get_Heading(self) -> Double: ...
    @winrt_commethod(9)
    def put_Heading(self, value: Double) -> Void: ...
    @winrt_commethod(10)
    def get_Pitch(self) -> Double: ...
    @winrt_commethod(11)
    def put_Pitch(self, value: Double) -> Void: ...
    @winrt_commethod(12)
    def get_Roll(self) -> Double: ...
    @winrt_commethod(13)
    def put_Roll(self, value: Double) -> Void: ...
    @winrt_commethod(14)
    def get_FieldOfView(self) -> Double: ...
    @winrt_commethod(15)
    def put_FieldOfView(self, value: Double) -> Void: ...
    FieldOfView = property(get_FieldOfView, put_FieldOfView)
    Heading = property(get_Heading, put_Heading)
    Location = property(get_Location, put_Location)
    Pitch = property(get_Pitch, put_Pitch)
    Roll = property(get_Roll, put_Roll)
class IMapCameraFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapCameraFactory'
    _iid_ = Guid('{ea3b0f16-83af-4ace-8e71-10ad9f1e9e7f}')
    @winrt_commethod(6)
    def CreateInstanceWithLocation(self, location: win32more.Windows.Devices.Geolocation.Geopoint) -> win32more.Windows.UI.Xaml.Controls.Maps.MapCamera: ...
    @winrt_commethod(7)
    def CreateInstanceWithLocationAndHeading(self, location: win32more.Windows.Devices.Geolocation.Geopoint, headingInDegrees: Double) -> win32more.Windows.UI.Xaml.Controls.Maps.MapCamera: ...
    @winrt_commethod(8)
    def CreateInstanceWithLocationHeadingAndPitch(self, location: win32more.Windows.Devices.Geolocation.Geopoint, headingInDegrees: Double, pitchInDegrees: Double) -> win32more.Windows.UI.Xaml.Controls.Maps.MapCamera: ...
    @winrt_commethod(9)
    def CreateInstanceWithLocationHeadingPitchRollAndFieldOfView(self, location: win32more.Windows.Devices.Geolocation.Geopoint, headingInDegrees: Double, pitchInDegrees: Double, rollInDegrees: Double, fieldOfViewInDegrees: Double) -> win32more.Windows.UI.Xaml.Controls.Maps.MapCamera: ...
class IMapContextRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapContextRequestedEventArgs'
    _iid_ = Guid('{fdd1b423-c961-4df2-bb57-82ee0f0bb591}')
    @winrt_commethod(6)
    def get_Position(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def get_Location(self) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(8)
    def get_MapElements(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Xaml.Controls.Maps.MapElement]: ...
    Location = property(get_Location, None)
    MapElements = property(get_MapElements, None)
    Position = property(get_Position, None)
class IMapControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControl'
    _iid_ = Guid('{42d0b851-5256-4747-9e6c-0d11e966141e}')
    @winrt_commethod(6)
    def get_Center(self) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(7)
    def put_Center(self, value: win32more.Windows.Devices.Geolocation.Geopoint) -> Void: ...
    @winrt_commethod(8)
    def get_Children(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.DependencyObject]: ...
    @winrt_commethod(9)
    def get_ColorScheme(self) -> win32more.Windows.UI.Xaml.Controls.Maps.MapColorScheme: ...
    @winrt_commethod(10)
    def put_ColorScheme(self, value: win32more.Windows.UI.Xaml.Controls.Maps.MapColorScheme) -> Void: ...
    @winrt_commethod(11)
    def get_DesiredPitch(self) -> Double: ...
    @winrt_commethod(12)
    def put_DesiredPitch(self, value: Double) -> Void: ...
    @winrt_commethod(13)
    def get_Heading(self) -> Double: ...
    @winrt_commethod(14)
    def put_Heading(self, value: Double) -> Void: ...
    @winrt_commethod(15)
    def get_LandmarksVisible(self) -> Boolean: ...
    @winrt_commethod(16)
    def put_LandmarksVisible(self, value: Boolean) -> Void: ...
    @winrt_commethod(17)
    def get_LoadingStatus(self) -> win32more.Windows.UI.Xaml.Controls.Maps.MapLoadingStatus: ...
    @winrt_commethod(18)
    def get_MapServiceToken(self) -> WinRT_String: ...
    @winrt_commethod(19)
    def put_MapServiceToken(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(20)
    def get_MaxZoomLevel(self) -> Double: ...
    @winrt_commethod(21)
    def get_MinZoomLevel(self) -> Double: ...
    @winrt_commethod(22)
    def get_PedestrianFeaturesVisible(self) -> Boolean: ...
    @winrt_commethod(23)
    def put_PedestrianFeaturesVisible(self, value: Boolean) -> Void: ...
    @winrt_commethod(24)
    def get_Pitch(self) -> Double: ...
    @winrt_commethod(25)
    def get_Style(self) -> win32more.Windows.UI.Xaml.Controls.Maps.MapStyle: ...
    @winrt_commethod(26)
    def put_Style(self, value: win32more.Windows.UI.Xaml.Controls.Maps.MapStyle) -> Void: ...
    @winrt_commethod(27)
    def get_TrafficFlowVisible(self) -> Boolean: ...
    @winrt_commethod(28)
    def put_TrafficFlowVisible(self, value: Boolean) -> Void: ...
    @winrt_commethod(29)
    def get_TransformOrigin(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(30)
    def put_TransformOrigin(self, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(31)
    def get_WatermarkMode(self) -> win32more.Windows.UI.Xaml.Controls.Maps.MapWatermarkMode: ...
    @winrt_commethod(32)
    def put_WatermarkMode(self, value: win32more.Windows.UI.Xaml.Controls.Maps.MapWatermarkMode) -> Void: ...
    @winrt_commethod(33)
    def get_ZoomLevel(self) -> Double: ...
    @winrt_commethod(34)
    def put_ZoomLevel(self, value: Double) -> Void: ...
    @winrt_commethod(35)
    def get_MapElements(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Controls.Maps.MapElement]: ...
    @winrt_commethod(36)
    def get_Routes(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Controls.Maps.MapRouteView]: ...
    @winrt_commethod(37)
    def get_TileSources(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Controls.Maps.MapTileSource]: ...
    @winrt_commethod(38)
    def add_CenterChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(39)
    def remove_CenterChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(40)
    def add_HeadingChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(41)
    def remove_HeadingChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(42)
    def add_LoadingStatusChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(43)
    def remove_LoadingStatusChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(44)
    def add_MapDoubleTapped(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.UI.Xaml.Controls.Maps.MapInputEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(45)
    def remove_MapDoubleTapped(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(46)
    def add_MapHolding(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.UI.Xaml.Controls.Maps.MapInputEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(47)
    def remove_MapHolding(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(48)
    def add_MapTapped(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.UI.Xaml.Controls.Maps.MapInputEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(49)
    def remove_MapTapped(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(50)
    def add_PitchChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(51)
    def remove_PitchChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(52)
    def add_TransformOriginChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(53)
    def remove_TransformOriginChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(54)
    def add_ZoomLevelChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(55)
    def remove_ZoomLevelChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(56)
    def FindMapElementsAtOffset(self, offset: win32more.Windows.Foundation.Point) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Xaml.Controls.Maps.MapElement]: ...
    @winrt_commethod(57)
    def GetLocationFromOffset(self, offset: win32more.Windows.Foundation.Point, location: POINTER(win32more.Windows.Devices.Geolocation.Geopoint)) -> Void: ...
    @winrt_commethod(58)
    def GetOffsetFromLocation(self, location: win32more.Windows.Devices.Geolocation.Geopoint, offset: POINTER(win32more.Windows.Foundation.Point)) -> Void: ...
    @winrt_commethod(59)
    def IsLocationInView(self, location: win32more.Windows.Devices.Geolocation.Geopoint, isInView: POINTER(Boolean)) -> Void: ...
    @winrt_commethod(60)
    def TrySetViewBoundsAsync(self, bounds: win32more.Windows.Devices.Geolocation.GeoboundingBox, margin: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Xaml.Thickness], animation: win32more.Windows.UI.Xaml.Controls.Maps.MapAnimationKind) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(61)
    def TrySetViewWithCenterAsync(self, center: win32more.Windows.Devices.Geolocation.Geopoint) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(62)
    def TrySetViewWithCenterAndZoomAsync(self, center: win32more.Windows.Devices.Geolocation.Geopoint, zoomLevel: win32more.Windows.Foundation.IReference[Double]) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(63)
    def TrySetViewWithCenterZoomHeadingAndPitchAsync(self, center: win32more.Windows.Devices.Geolocation.Geopoint, zoomLevel: win32more.Windows.Foundation.IReference[Double], heading: win32more.Windows.Foundation.IReference[Double], desiredPitch: win32more.Windows.Foundation.IReference[Double]) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(64)
    def TrySetViewWithCenterZoomHeadingPitchAndAnimationAsync(self, center: win32more.Windows.Devices.Geolocation.Geopoint, zoomLevel: win32more.Windows.Foundation.IReference[Double], heading: win32more.Windows.Foundation.IReference[Double], desiredPitch: win32more.Windows.Foundation.IReference[Double], animation: win32more.Windows.UI.Xaml.Controls.Maps.MapAnimationKind) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    Center = property(get_Center, put_Center)
    Children = property(get_Children, None)
    ColorScheme = property(get_ColorScheme, put_ColorScheme)
    DesiredPitch = property(get_DesiredPitch, put_DesiredPitch)
    Heading = property(get_Heading, put_Heading)
    LandmarksVisible = property(get_LandmarksVisible, put_LandmarksVisible)
    LoadingStatus = property(get_LoadingStatus, None)
    MapElements = property(get_MapElements, None)
    MapServiceToken = property(get_MapServiceToken, put_MapServiceToken)
    MaxZoomLevel = property(get_MaxZoomLevel, None)
    MinZoomLevel = property(get_MinZoomLevel, None)
    PedestrianFeaturesVisible = property(get_PedestrianFeaturesVisible, put_PedestrianFeaturesVisible)
    Pitch = property(get_Pitch, None)
    Routes = property(get_Routes, None)
    Style = property(get_Style, put_Style)
    TileSources = property(get_TileSources, None)
    TrafficFlowVisible = property(get_TrafficFlowVisible, put_TrafficFlowVisible)
    TransformOrigin = property(get_TransformOrigin, put_TransformOrigin)
    WatermarkMode = property(get_WatermarkMode, put_WatermarkMode)
    ZoomLevel = property(get_ZoomLevel, put_ZoomLevel)
    CenterChanged = event()
    HeadingChanged = event()
    LoadingStatusChanged = event()
    MapDoubleTapped = event()
    MapHolding = event()
    MapTapped = event()
    PitchChanged = event()
    TransformOriginChanged = event()
    ZoomLevelChanged = event()
class IMapControl2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControl2'
    _iid_ = Guid('{e1fd644d-96ec-4065-b0f0-75281da3654d}')
    @winrt_commethod(6)
    def get_BusinessLandmarksVisible(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_BusinessLandmarksVisible(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_TransitFeaturesVisible(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_TransitFeaturesVisible(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_PanInteractionMode(self) -> win32more.Windows.UI.Xaml.Controls.Maps.MapPanInteractionMode: ...
    @winrt_commethod(11)
    def put_PanInteractionMode(self, value: win32more.Windows.UI.Xaml.Controls.Maps.MapPanInteractionMode) -> Void: ...
    @winrt_commethod(12)
    def get_RotateInteractionMode(self) -> win32more.Windows.UI.Xaml.Controls.Maps.MapInteractionMode: ...
    @winrt_commethod(13)
    def put_RotateInteractionMode(self, value: win32more.Windows.UI.Xaml.Controls.Maps.MapInteractionMode) -> Void: ...
    @winrt_commethod(14)
    def get_TiltInteractionMode(self) -> win32more.Windows.UI.Xaml.Controls.Maps.MapInteractionMode: ...
    @winrt_commethod(15)
    def put_TiltInteractionMode(self, value: win32more.Windows.UI.Xaml.Controls.Maps.MapInteractionMode) -> Void: ...
    @winrt_commethod(16)
    def get_ZoomInteractionMode(self) -> win32more.Windows.UI.Xaml.Controls.Maps.MapInteractionMode: ...
    @winrt_commethod(17)
    def put_ZoomInteractionMode(self, value: win32more.Windows.UI.Xaml.Controls.Maps.MapInteractionMode) -> Void: ...
    @winrt_commethod(18)
    def get_Is3DSupported(self) -> Boolean: ...
    @winrt_commethod(19)
    def get_IsStreetsideSupported(self) -> Boolean: ...
    @winrt_commethod(20)
    def get_Scene(self) -> win32more.Windows.UI.Xaml.Controls.Maps.MapScene: ...
    @winrt_commethod(21)
    def put_Scene(self, value: win32more.Windows.UI.Xaml.Controls.Maps.MapScene) -> Void: ...
    @winrt_commethod(22)
    def get_ActualCamera(self) -> win32more.Windows.UI.Xaml.Controls.Maps.MapCamera: ...
    @winrt_commethod(23)
    def get_TargetCamera(self) -> win32more.Windows.UI.Xaml.Controls.Maps.MapCamera: ...
    @winrt_commethod(24)
    def get_CustomExperience(self) -> win32more.Windows.UI.Xaml.Controls.Maps.MapCustomExperience: ...
    @winrt_commethod(25)
    def put_CustomExperience(self, value: win32more.Windows.UI.Xaml.Controls.Maps.MapCustomExperience) -> Void: ...
    @winrt_commethod(26)
    def add_MapElementClick(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.UI.Xaml.Controls.Maps.MapElementClickEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(27)
    def remove_MapElementClick(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(28)
    def add_MapElementPointerEntered(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.UI.Xaml.Controls.Maps.MapElementPointerEnteredEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(29)
    def remove_MapElementPointerEntered(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(30)
    def add_MapElementPointerExited(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.UI.Xaml.Controls.Maps.MapElementPointerExitedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(31)
    def remove_MapElementPointerExited(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(32)
    def add_ActualCameraChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.UI.Xaml.Controls.Maps.MapActualCameraChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(33)
    def remove_ActualCameraChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(34)
    def add_ActualCameraChanging(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.UI.Xaml.Controls.Maps.MapActualCameraChangingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(35)
    def remove_ActualCameraChanging(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(36)
    def add_TargetCameraChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.UI.Xaml.Controls.Maps.MapTargetCameraChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(37)
    def remove_TargetCameraChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(38)
    def add_CustomExperienceChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.UI.Xaml.Controls.Maps.MapCustomExperienceChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(39)
    def remove_CustomExperienceChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(40)
    def StartContinuousRotate(self, rateInDegreesPerSecond: Double) -> Void: ...
    @winrt_commethod(41)
    def StopContinuousRotate(self) -> Void: ...
    @winrt_commethod(42)
    def StartContinuousTilt(self, rateInDegreesPerSecond: Double) -> Void: ...
    @winrt_commethod(43)
    def StopContinuousTilt(self) -> Void: ...
    @winrt_commethod(44)
    def StartContinuousZoom(self, rateOfChangePerSecond: Double) -> Void: ...
    @winrt_commethod(45)
    def StopContinuousZoom(self) -> Void: ...
    @winrt_commethod(46)
    def TryRotateAsync(self, degrees: Double) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(47)
    def TryRotateToAsync(self, angleInDegrees: Double) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(48)
    def TryTiltAsync(self, degrees: Double) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(49)
    def TryTiltToAsync(self, angleInDegrees: Double) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(50)
    def TryZoomInAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(51)
    def TryZoomOutAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(52)
    def TryZoomToAsync(self, zoomLevel: Double) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(53)
    def TrySetSceneAsync(self, scene: win32more.Windows.UI.Xaml.Controls.Maps.MapScene) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(54)
    def TrySetSceneWithAnimationAsync(self, scene: win32more.Windows.UI.Xaml.Controls.Maps.MapScene, animationKind: win32more.Windows.UI.Xaml.Controls.Maps.MapAnimationKind) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    ActualCamera = property(get_ActualCamera, None)
    BusinessLandmarksVisible = property(get_BusinessLandmarksVisible, put_BusinessLandmarksVisible)
    CustomExperience = property(get_CustomExperience, put_CustomExperience)
    Is3DSupported = property(get_Is3DSupported, None)
    IsStreetsideSupported = property(get_IsStreetsideSupported, None)
    PanInteractionMode = property(get_PanInteractionMode, put_PanInteractionMode)
    RotateInteractionMode = property(get_RotateInteractionMode, put_RotateInteractionMode)
    Scene = property(get_Scene, put_Scene)
    TargetCamera = property(get_TargetCamera, None)
    TiltInteractionMode = property(get_TiltInteractionMode, put_TiltInteractionMode)
    TransitFeaturesVisible = property(get_TransitFeaturesVisible, put_TransitFeaturesVisible)
    ZoomInteractionMode = property(get_ZoomInteractionMode, put_ZoomInteractionMode)
    MapElementClick = event()
    MapElementPointerEntered = event()
    MapElementPointerExited = event()
    ActualCameraChanged = event()
    ActualCameraChanging = event()
    TargetCameraChanged = event()
    CustomExperienceChanged = event()
class IMapControl3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControl3'
    _iid_ = Guid('{586328f8-8cdd-40ae-9338-af2a7be845e5}')
    @winrt_commethod(6)
    def add_MapRightTapped(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.UI.Xaml.Controls.Maps.MapRightTappedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_MapRightTapped(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    MapRightTapped = event()
class IMapControl4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControl4'
    _iid_ = Guid('{068f132a-1817-466d-b7ce-419b3f8e248b}')
    @winrt_commethod(6)
    def get_BusinessLandmarksEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_BusinessLandmarksEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_TransitFeaturesEnabled(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_TransitFeaturesEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def GetVisibleRegion(self, region: win32more.Windows.UI.Xaml.Controls.Maps.MapVisibleRegionKind) -> win32more.Windows.Devices.Geolocation.Geopath: ...
    BusinessLandmarksEnabled = property(get_BusinessLandmarksEnabled, put_BusinessLandmarksEnabled)
    TransitFeaturesEnabled = property(get_TransitFeaturesEnabled, put_TransitFeaturesEnabled)
class IMapControl5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControl5'
    _iid_ = Guid('{dd9b0ffd-7823-46a2-82c9-65ddac4f365f}')
    @winrt_commethod(6)
    def get_MapProjection(self) -> win32more.Windows.UI.Xaml.Controls.Maps.MapProjection: ...
    @winrt_commethod(7)
    def put_MapProjection(self, value: win32more.Windows.UI.Xaml.Controls.Maps.MapProjection) -> Void: ...
    @winrt_commethod(8)
    def get_StyleSheet(self) -> win32more.Windows.UI.Xaml.Controls.Maps.MapStyleSheet: ...
    @winrt_commethod(9)
    def put_StyleSheet(self, value: win32more.Windows.UI.Xaml.Controls.Maps.MapStyleSheet) -> Void: ...
    @winrt_commethod(10)
    def get_ViewPadding(self) -> win32more.Windows.UI.Xaml.Thickness: ...
    @winrt_commethod(11)
    def put_ViewPadding(self, value: win32more.Windows.UI.Xaml.Thickness) -> Void: ...
    @winrt_commethod(12)
    def add_MapContextRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.UI.Xaml.Controls.Maps.MapContextRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_MapContextRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def FindMapElementsAtOffsetWithRadius(self, offset: win32more.Windows.Foundation.Point, radius: Double) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Xaml.Controls.Maps.MapElement]: ...
    @winrt_commethod(15)
    def GetLocationFromOffsetWithReferenceSystem(self, offset: win32more.Windows.Foundation.Point, desiredReferenceSystem: win32more.Windows.Devices.Geolocation.AltitudeReferenceSystem, location: POINTER(win32more.Windows.Devices.Geolocation.Geopoint)) -> Void: ...
    @winrt_commethod(16)
    def StartContinuousPan(self, horizontalPixelsPerSecond: Double, verticalPixelsPerSecond: Double) -> Void: ...
    @winrt_commethod(17)
    def StopContinuousPan(self) -> Void: ...
    @winrt_commethod(18)
    def TryPanAsync(self, horizontalPixels: Double, verticalPixels: Double) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(19)
    def TryPanToAsync(self, location: win32more.Windows.Devices.Geolocation.Geopoint) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    MapProjection = property(get_MapProjection, put_MapProjection)
    StyleSheet = property(get_StyleSheet, put_StyleSheet)
    ViewPadding = property(get_ViewPadding, put_ViewPadding)
    MapContextRequested = event()
class IMapControl6(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControl6'
    _iid_ = Guid('{b0da89a2-1041-4bea-b88a-12ac9a82e0e2}')
    @winrt_commethod(6)
    def get_Layers(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Controls.Maps.MapLayer]: ...
    @winrt_commethod(7)
    def put_Layers(self, value: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Controls.Maps.MapLayer]) -> Void: ...
    @winrt_commethod(8)
    def TryGetLocationFromOffset(self, offset: win32more.Windows.Foundation.Point, location: POINTER(win32more.Windows.Devices.Geolocation.Geopoint)) -> Boolean: ...
    @winrt_commethod(9)
    def TryGetLocationFromOffsetWithReferenceSystem(self, offset: win32more.Windows.Foundation.Point, desiredReferenceSystem: win32more.Windows.Devices.Geolocation.AltitudeReferenceSystem, location: POINTER(win32more.Windows.Devices.Geolocation.Geopoint)) -> Boolean: ...
    Layers = property(get_Layers, put_Layers)
class IMapControl7(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControl7'
    _iid_ = Guid('{0d86e453-0c1f-4f7e-ae66-4ad0b4987857}')
    @winrt_commethod(6)
    def get_Region(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Region(self, value: WinRT_String) -> Void: ...
    Region = property(get_Region, put_Region)
class IMapControl8(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControl8'
    _iid_ = Guid('{009e9c46-724d-53ca-9421-7a48fc731523}')
    @winrt_commethod(6)
    def get_CanTiltDown(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_CanTiltUp(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_CanZoomIn(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_CanZoomOut(self) -> Boolean: ...
    CanTiltDown = property(get_CanTiltDown, None)
    CanTiltUp = property(get_CanTiltUp, None)
    CanZoomIn = property(get_CanZoomIn, None)
    CanZoomOut = property(get_CanZoomOut, None)
class IMapControlBusinessLandmarkClickEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControlBusinessLandmarkClickEventArgs'
    _iid_ = Guid('{5e464922-4a1a-4797-beb7-5cf7754cb867}')
    @winrt_commethod(6)
    def get_LocalLocations(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Maps.LocalSearch.LocalLocation]: ...
    LocalLocations = property(get_LocalLocations, None)
class IMapControlBusinessLandmarkPointerEnteredEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControlBusinessLandmarkPointerEnteredEventArgs'
    _iid_ = Guid('{5e4081a6-ea98-4f95-8caf-5b42696ff504}')
    @winrt_commethod(6)
    def get_LocalLocations(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Maps.LocalSearch.LocalLocation]: ...
    LocalLocations = property(get_LocalLocations, None)
class IMapControlBusinessLandmarkPointerExitedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControlBusinessLandmarkPointerExitedEventArgs'
    _iid_ = Guid('{2bb52caf-f24a-46d0-b463-65f719731057}')
    @winrt_commethod(6)
    def get_LocalLocations(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Maps.LocalSearch.LocalLocation]: ...
    LocalLocations = property(get_LocalLocations, None)
class IMapControlBusinessLandmarkRightTappedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControlBusinessLandmarkRightTappedEventArgs'
    _iid_ = Guid('{59ab8ae7-f184-4ab1-b0b0-35c8bf0654b2}')
    @winrt_commethod(6)
    def get_LocalLocations(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Maps.LocalSearch.LocalLocation]: ...
    LocalLocations = property(get_LocalLocations, None)
class IMapControlDataHelper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControlDataHelper'
    _iid_ = Guid('{8bb0f09c-14ab-486c-9de5-5a5def0205a2}')
    @winrt_commethod(6)
    def add_BusinessLandmarkClick(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.UI.Xaml.Controls.Maps.MapControlBusinessLandmarkClickEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_BusinessLandmarkClick(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_TransitFeatureClick(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.UI.Xaml.Controls.Maps.MapControlTransitFeatureClickEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_TransitFeatureClick(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_BusinessLandmarkRightTapped(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.UI.Xaml.Controls.Maps.MapControlBusinessLandmarkRightTappedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_BusinessLandmarkRightTapped(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_TransitFeatureRightTapped(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.UI.Xaml.Controls.Maps.MapControlTransitFeatureRightTappedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_TransitFeatureRightTapped(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    BusinessLandmarkClick = event()
    TransitFeatureClick = event()
    BusinessLandmarkRightTapped = event()
    TransitFeatureRightTapped = event()
class IMapControlDataHelper2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControlDataHelper2'
    _iid_ = Guid('{59ce429e-562f-4c21-a674-0f11decf0fb3}')
    @winrt_commethod(6)
    def add_BusinessLandmarkPointerEntered(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.UI.Xaml.Controls.Maps.MapControlBusinessLandmarkPointerEnteredEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_BusinessLandmarkPointerEntered(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_TransitFeaturePointerEntered(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.UI.Xaml.Controls.Maps.MapControlTransitFeaturePointerEnteredEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_TransitFeaturePointerEntered(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_BusinessLandmarkPointerExited(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.UI.Xaml.Controls.Maps.MapControlBusinessLandmarkPointerExitedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_BusinessLandmarkPointerExited(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_TransitFeaturePointerExited(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.UI.Xaml.Controls.Maps.MapControlTransitFeaturePointerExitedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_TransitFeaturePointerExited(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    BusinessLandmarkPointerEntered = event()
    TransitFeaturePointerEntered = event()
    BusinessLandmarkPointerExited = event()
    TransitFeaturePointerExited = event()
class IMapControlDataHelperFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControlDataHelperFactory'
    _iid_ = Guid('{3b70aa8e-02ef-469c-bbaf-dc2158d4289b}')
    @winrt_commethod(6)
    def CreateInstance(self, map: win32more.Windows.UI.Xaml.Controls.Maps.MapControl) -> win32more.Windows.UI.Xaml.Controls.Maps.MapControlDataHelper: ...
class IMapControlDataHelperStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControlDataHelperStatics'
    _iid_ = Guid('{7a6632d6-e944-4110-83cf-314d0722e2e5}')
    @winrt_commethod(6)
    def CreateMapControl(self, rasterRenderMode: Boolean) -> win32more.Windows.UI.Xaml.Controls.Maps.MapControl: ...
class IMapControlStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControlStatics'
    _iid_ = Guid('{c2c61795-2147-4f0a-942a-5493a85de807}')
    @winrt_commethod(6)
    def get_CenterProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_ChildrenProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_ColorSchemeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_DesiredPitchProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_HeadingProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_LandmarksVisibleProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(12)
    def get_LoadingStatusProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def get_MapServiceTokenProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(14)
    def get_PedestrianFeaturesVisibleProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(15)
    def get_PitchProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(16)
    def get_StyleProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(17)
    def get_TrafficFlowVisibleProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(18)
    def get_TransformOriginProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(19)
    def get_WatermarkModeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(20)
    def get_ZoomLevelProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(21)
    def get_MapElementsProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(22)
    def get_RoutesProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(23)
    def get_TileSourcesProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(24)
    def get_LocationProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(25)
    def GetLocation(self, element: win32more.Windows.UI.Xaml.DependencyObject) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(26)
    def SetLocation(self, element: win32more.Windows.UI.Xaml.DependencyObject, value: win32more.Windows.Devices.Geolocation.Geopoint) -> Void: ...
    @winrt_commethod(27)
    def get_NormalizedAnchorPointProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(28)
    def GetNormalizedAnchorPoint(self, element: win32more.Windows.UI.Xaml.DependencyObject) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(29)
    def SetNormalizedAnchorPoint(self, element: win32more.Windows.UI.Xaml.DependencyObject, value: win32more.Windows.Foundation.Point) -> Void: ...
    CenterProperty = property(get_CenterProperty, None)
    ChildrenProperty = property(get_ChildrenProperty, None)
    ColorSchemeProperty = property(get_ColorSchemeProperty, None)
    DesiredPitchProperty = property(get_DesiredPitchProperty, None)
    HeadingProperty = property(get_HeadingProperty, None)
    LandmarksVisibleProperty = property(get_LandmarksVisibleProperty, None)
    LoadingStatusProperty = property(get_LoadingStatusProperty, None)
    LocationProperty = property(get_LocationProperty, None)
    MapElementsProperty = property(get_MapElementsProperty, None)
    MapServiceTokenProperty = property(get_MapServiceTokenProperty, None)
    NormalizedAnchorPointProperty = property(get_NormalizedAnchorPointProperty, None)
    PedestrianFeaturesVisibleProperty = property(get_PedestrianFeaturesVisibleProperty, None)
    PitchProperty = property(get_PitchProperty, None)
    RoutesProperty = property(get_RoutesProperty, None)
    StyleProperty = property(get_StyleProperty, None)
    TileSourcesProperty = property(get_TileSourcesProperty, None)
    TrafficFlowVisibleProperty = property(get_TrafficFlowVisibleProperty, None)
    TransformOriginProperty = property(get_TransformOriginProperty, None)
    WatermarkModeProperty = property(get_WatermarkModeProperty, None)
    ZoomLevelProperty = property(get_ZoomLevelProperty, None)
class IMapControlStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControlStatics2'
    _iid_ = Guid('{04852b93-b446-4d31-9752-1ec69a5996ae}')
    @winrt_commethod(6)
    def get_BusinessLandmarksVisibleProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_TransitFeaturesVisibleProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_PanInteractionModeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_RotateInteractionModeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_TiltInteractionModeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_ZoomInteractionModeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(12)
    def get_Is3DSupportedProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def get_IsStreetsideSupportedProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(14)
    def get_SceneProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    BusinessLandmarksVisibleProperty = property(get_BusinessLandmarksVisibleProperty, None)
    Is3DSupportedProperty = property(get_Is3DSupportedProperty, None)
    IsStreetsideSupportedProperty = property(get_IsStreetsideSupportedProperty, None)
    PanInteractionModeProperty = property(get_PanInteractionModeProperty, None)
    RotateInteractionModeProperty = property(get_RotateInteractionModeProperty, None)
    SceneProperty = property(get_SceneProperty, None)
    TiltInteractionModeProperty = property(get_TiltInteractionModeProperty, None)
    TransitFeaturesVisibleProperty = property(get_TransitFeaturesVisibleProperty, None)
    ZoomInteractionModeProperty = property(get_ZoomInteractionModeProperty, None)
class IMapControlStatics4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControlStatics4'
    _iid_ = Guid('{fe785d97-5d13-4fa1-bf1d-84061768c183}')
    @winrt_commethod(6)
    def get_BusinessLandmarksEnabledProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_TransitFeaturesEnabledProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    BusinessLandmarksEnabledProperty = property(get_BusinessLandmarksEnabledProperty, None)
    TransitFeaturesEnabledProperty = property(get_TransitFeaturesEnabledProperty, None)
class IMapControlStatics5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControlStatics5'
    _iid_ = Guid('{09626f00-b7dd-4189-a7f7-830c412deea3}')
    @winrt_commethod(6)
    def get_MapProjectionProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_StyleSheetProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_ViewPaddingProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    MapProjectionProperty = property(get_MapProjectionProperty, None)
    StyleSheetProperty = property(get_StyleSheetProperty, None)
    ViewPaddingProperty = property(get_ViewPaddingProperty, None)
class IMapControlStatics6(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControlStatics6'
    _iid_ = Guid('{3ccfdd7f-24d1-40a2-8351-b3063a8c95a4}')
    @winrt_commethod(6)
    def get_LayersProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    LayersProperty = property(get_LayersProperty, None)
class IMapControlStatics7(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControlStatics7'
    _iid_ = Guid('{55f1ac4d-72c2-46b2-b7ae-790260be641b}')
    @winrt_commethod(6)
    def get_RegionProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    RegionProperty = property(get_RegionProperty, None)
class IMapControlStatics8(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControlStatics8'
    _iid_ = Guid('{adb7a7b0-0605-592c-bf9d-d10bdc2be47b}')
    @winrt_commethod(6)
    def get_CanTiltDownProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_CanTiltUpProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_CanZoomInProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_CanZoomOutProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    CanTiltDownProperty = property(get_CanTiltDownProperty, None)
    CanTiltUpProperty = property(get_CanTiltUpProperty, None)
    CanZoomInProperty = property(get_CanZoomInProperty, None)
    CanZoomOutProperty = property(get_CanZoomOutProperty, None)
class IMapControlTransitFeatureClickEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControlTransitFeatureClickEventArgs'
    _iid_ = Guid('{76179969-b765-4622-b08a-3072745a4541}')
    @winrt_commethod(6)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Location(self) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(8)
    def get_TransitProperties(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    DisplayName = property(get_DisplayName, None)
    Location = property(get_Location, None)
    TransitProperties = property(get_TransitProperties, None)
class IMapControlTransitFeaturePointerEnteredEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControlTransitFeaturePointerEnteredEventArgs'
    _iid_ = Guid('{73911a4e-ec4f-479e-94a1-36e081d0d897}')
    @winrt_commethod(6)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Location(self) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(8)
    def get_TransitProperties(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    DisplayName = property(get_DisplayName, None)
    Location = property(get_Location, None)
    TransitProperties = property(get_TransitProperties, None)
class IMapControlTransitFeaturePointerExitedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControlTransitFeaturePointerExitedEventArgs'
    _iid_ = Guid('{6a11258d-448d-44e7-bc69-d13d497154e9}')
    @winrt_commethod(6)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Location(self) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(8)
    def get_TransitProperties(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    DisplayName = property(get_DisplayName, None)
    Location = property(get_Location, None)
    TransitProperties = property(get_TransitProperties, None)
class IMapControlTransitFeatureRightTappedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControlTransitFeatureRightTappedEventArgs'
    _iid_ = Guid('{aea1cc49-a729-4eae-a59a-3ec9a125a028}')
    @winrt_commethod(6)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Location(self) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(8)
    def get_TransitProperties(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    DisplayName = property(get_DisplayName, None)
    Location = property(get_Location, None)
    TransitProperties = property(get_TransitProperties, None)
class IMapCustomExperience(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapCustomExperience'
    _iid_ = Guid('{64592866-14a3-4e5f-8883-8e9c500eeede}')
class IMapCustomExperienceChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapCustomExperienceChangedEventArgs'
    _iid_ = Guid('{b9e6fb9b-8fc1-4042-ac34-a61b38bb7514}')
class IMapCustomExperienceFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapCustomExperienceFactory'
    _iid_ = Guid('{7a403fb5-a1b1-4e7f-921e-3e6b8d8ebed6}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Maps.MapCustomExperience: ...
class IMapElement(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapElement'
    _iid_ = Guid('{d61fc4df-b245-47f2-9ac2-43c058b1c903}')
    @winrt_commethod(6)
    def get_ZIndex(self) -> Int32: ...
    @winrt_commethod(7)
    def put_ZIndex(self, value: Int32) -> Void: ...
    @winrt_commethod(8)
    def get_Visible(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_Visible(self, value: Boolean) -> Void: ...
    Visible = property(get_Visible, put_Visible)
    ZIndex = property(get_ZIndex, put_ZIndex)
class IMapElement2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapElement2'
    _iid_ = Guid('{6619f261-fba6-4964-a7ff-f1af63ab9cb0}')
    @winrt_commethod(6)
    def get_MapTabIndex(self) -> Int32: ...
    @winrt_commethod(7)
    def put_MapTabIndex(self, value: Int32) -> Void: ...
    MapTabIndex = property(get_MapTabIndex, put_MapTabIndex)
class IMapElement3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapElement3'
    _iid_ = Guid('{13efbc59-45ed-48b4-93ad-e3f78f8cf218}')
    @winrt_commethod(6)
    def get_MapStyleSheetEntry(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_MapStyleSheetEntry(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_MapStyleSheetEntryState(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_MapStyleSheetEntryState(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_Tag(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(11)
    def put_Tag(self, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    MapStyleSheetEntry = property(get_MapStyleSheetEntry, put_MapStyleSheetEntry)
    MapStyleSheetEntryState = property(get_MapStyleSheetEntryState, put_MapStyleSheetEntryState)
    Tag = property(get_Tag, put_Tag)
class IMapElement3D(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapElement3D'
    _iid_ = Guid('{827af8d5-3843-48e2-bd00-0f0644fbe6a5}')
    @winrt_commethod(6)
    def get_Location(self) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(7)
    def put_Location(self, value: win32more.Windows.Devices.Geolocation.Geopoint) -> Void: ...
    @winrt_commethod(8)
    def get_Model(self) -> win32more.Windows.UI.Xaml.Controls.Maps.MapModel3D: ...
    @winrt_commethod(9)
    def put_Model(self, value: win32more.Windows.UI.Xaml.Controls.Maps.MapModel3D) -> Void: ...
    @winrt_commethod(10)
    def get_Heading(self) -> Double: ...
    @winrt_commethod(11)
    def put_Heading(self, value: Double) -> Void: ...
    @winrt_commethod(12)
    def get_Pitch(self) -> Double: ...
    @winrt_commethod(13)
    def put_Pitch(self, value: Double) -> Void: ...
    @winrt_commethod(14)
    def get_Roll(self) -> Double: ...
    @winrt_commethod(15)
    def put_Roll(self, value: Double) -> Void: ...
    @winrt_commethod(16)
    def get_Scale(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(17)
    def put_Scale(self, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    Heading = property(get_Heading, put_Heading)
    Location = property(get_Location, put_Location)
    Model = property(get_Model, put_Model)
    Pitch = property(get_Pitch, put_Pitch)
    Roll = property(get_Roll, put_Roll)
    Scale = property(get_Scale, put_Scale)
class IMapElement3DStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapElement3DStatics'
    _iid_ = Guid('{6128011a-450f-442a-b9d9-aa815c71907a}')
    @winrt_commethod(6)
    def get_LocationProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_HeadingProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_PitchProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_RollProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_ScaleProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    HeadingProperty = property(get_HeadingProperty, None)
    LocationProperty = property(get_LocationProperty, None)
    PitchProperty = property(get_PitchProperty, None)
    RollProperty = property(get_RollProperty, None)
    ScaleProperty = property(get_ScaleProperty, None)
class IMapElement4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapElement4'
    _iid_ = Guid('{645883b6-1fc1-4ceb-93bd-dc2c960072e9}')
    @winrt_commethod(6)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsEnabled(self, value: Boolean) -> Void: ...
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
class IMapElementClickEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapElementClickEventArgs'
    _iid_ = Guid('{40168a11-d080-4519-99a1-3149fb8999d0}')
    @winrt_commethod(6)
    def get_Position(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def get_Location(self) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(8)
    def get_MapElements(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Controls.Maps.MapElement]: ...
    Location = property(get_Location, None)
    MapElements = property(get_MapElements, None)
    Position = property(get_Position, None)
class IMapElementFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapElementFactory'
    _iid_ = Guid('{4a30d007-0bd6-47a5-860b-7e7cf5f0c573}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Maps.MapElement: ...
class IMapElementPointerEnteredEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapElementPointerEnteredEventArgs'
    _iid_ = Guid('{ab85dd4e-91d7-4b31-8f0a-d390c7d3a2ef}')
    @winrt_commethod(6)
    def get_Position(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def get_Location(self) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(8)
    def get_MapElement(self) -> win32more.Windows.UI.Xaml.Controls.Maps.MapElement: ...
    Location = property(get_Location, None)
    MapElement = property(get_MapElement, None)
    Position = property(get_Position, None)
class IMapElementPointerExitedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapElementPointerExitedEventArgs'
    _iid_ = Guid('{c1a45af9-60c9-4679-9119-20abc75d931f}')
    @winrt_commethod(6)
    def get_Position(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def get_Location(self) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(8)
    def get_MapElement(self) -> win32more.Windows.UI.Xaml.Controls.Maps.MapElement: ...
    Location = property(get_Location, None)
    MapElement = property(get_MapElement, None)
    Position = property(get_Position, None)
class IMapElementStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapElementStatics'
    _iid_ = Guid('{e8c71cf2-bfef-4b49-8e99-41b5e3789fd2}')
    @winrt_commethod(6)
    def get_ZIndexProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_VisibleProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    VisibleProperty = property(get_VisibleProperty, None)
    ZIndexProperty = property(get_ZIndexProperty, None)
class IMapElementStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapElementStatics2'
    _iid_ = Guid('{9bf72f30-80fe-4f30-bcc1-fa894050f676}')
    @winrt_commethod(6)
    def get_MapTabIndexProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    MapTabIndexProperty = property(get_MapTabIndexProperty, None)
class IMapElementStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapElementStatics3'
    _iid_ = Guid('{e11ee92f-9742-49aa-aad8-2e466bff3796}')
    @winrt_commethod(6)
    def get_MapStyleSheetEntryProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_MapStyleSheetEntryStateProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_TagProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    MapStyleSheetEntryProperty = property(get_MapStyleSheetEntryProperty, None)
    MapStyleSheetEntryStateProperty = property(get_MapStyleSheetEntryStateProperty, None)
    TagProperty = property(get_TagProperty, None)
class IMapElementStatics4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapElementStatics4'
    _iid_ = Guid('{a4296f0b-dff8-467c-9315-6f6db93ee2ba}')
    @winrt_commethod(6)
    def get_IsEnabledProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    IsEnabledProperty = property(get_IsEnabledProperty, None)
class IMapElementsLayer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapElementsLayer'
    _iid_ = Guid('{de79689a-01ef-46f4-ac60-7c200b552610}')
    @winrt_commethod(6)
    def get_MapElements(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Controls.Maps.MapElement]: ...
    @winrt_commethod(7)
    def put_MapElements(self, value: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Controls.Maps.MapElement]) -> Void: ...
    @winrt_commethod(8)
    def add_MapElementClick(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapElementsLayer, win32more.Windows.UI.Xaml.Controls.Maps.MapElementsLayerClickEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_MapElementClick(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_MapElementPointerEntered(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapElementsLayer, win32more.Windows.UI.Xaml.Controls.Maps.MapElementsLayerPointerEnteredEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_MapElementPointerEntered(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_MapElementPointerExited(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapElementsLayer, win32more.Windows.UI.Xaml.Controls.Maps.MapElementsLayerPointerExitedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_MapElementPointerExited(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_MapContextRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapElementsLayer, win32more.Windows.UI.Xaml.Controls.Maps.MapElementsLayerContextRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_MapContextRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    MapElements = property(get_MapElements, put_MapElements)
    MapElementClick = event()
    MapElementPointerEntered = event()
    MapElementPointerExited = event()
    MapContextRequested = event()
class IMapElementsLayerClickEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapElementsLayerClickEventArgs'
    _iid_ = Guid('{2ca7cf66-af1b-4c05-8c85-f74ae3d4677f}')
    @winrt_commethod(6)
    def get_Position(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def get_Location(self) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(8)
    def get_MapElements(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Controls.Maps.MapElement]: ...
    Location = property(get_Location, None)
    MapElements = property(get_MapElements, None)
    Position = property(get_Position, None)
class IMapElementsLayerContextRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapElementsLayerContextRequestedEventArgs'
    _iid_ = Guid('{da45d0b3-7a0e-4758-808b-3a637627eb0d}')
    @winrt_commethod(6)
    def get_Position(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def get_Location(self) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(8)
    def get_MapElements(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Xaml.Controls.Maps.MapElement]: ...
    Location = property(get_Location, None)
    MapElements = property(get_MapElements, None)
    Position = property(get_Position, None)
class IMapElementsLayerPointerEnteredEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapElementsLayerPointerEnteredEventArgs'
    _iid_ = Guid('{757fc032-4694-4404-8c89-348b6b76c5e6}')
    @winrt_commethod(6)
    def get_Position(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def get_Location(self) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(8)
    def get_MapElement(self) -> win32more.Windows.UI.Xaml.Controls.Maps.MapElement: ...
    Location = property(get_Location, None)
    MapElement = property(get_MapElement, None)
    Position = property(get_Position, None)
class IMapElementsLayerPointerExitedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapElementsLayerPointerExitedEventArgs'
    _iid_ = Guid('{92f3c6ad-03ed-4c39-af20-2a07ee1ccea6}')
    @winrt_commethod(6)
    def get_Position(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def get_Location(self) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(8)
    def get_MapElement(self) -> win32more.Windows.UI.Xaml.Controls.Maps.MapElement: ...
    Location = property(get_Location, None)
    MapElement = property(get_MapElement, None)
    Position = property(get_Position, None)
class IMapElementsLayerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapElementsLayerStatics'
    _iid_ = Guid('{34005727-f509-4d28-9180-911c03411d74}')
    @winrt_commethod(6)
    def get_MapElementsProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    MapElementsProperty = property(get_MapElementsProperty, None)
class IMapIcon(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapIcon'
    _iid_ = Guid('{d2096872-23d9-4a2b-8be0-69f3a85482ab}')
    @winrt_commethod(6)
    def get_Location(self) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(7)
    def put_Location(self, value: win32more.Windows.Devices.Geolocation.Geopoint) -> Void: ...
    @winrt_commethod(8)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Title(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_NormalizedAnchorPoint(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(11)
    def put_NormalizedAnchorPoint(self, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(12)
    def get_Image(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(13)
    def put_Image(self, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    Image = property(get_Image, put_Image)
    Location = property(get_Location, put_Location)
    NormalizedAnchorPoint = property(get_NormalizedAnchorPoint, put_NormalizedAnchorPoint)
    Title = property(get_Title, put_Title)
class IMapIcon2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapIcon2'
    _iid_ = Guid('{611254b9-d8aa-4bbd-a316-badf06911d63}')
    @winrt_commethod(6)
    def get_CollisionBehaviorDesired(self) -> win32more.Windows.UI.Xaml.Controls.Maps.MapElementCollisionBehavior: ...
    @winrt_commethod(7)
    def put_CollisionBehaviorDesired(self, value: win32more.Windows.UI.Xaml.Controls.Maps.MapElementCollisionBehavior) -> Void: ...
    CollisionBehaviorDesired = property(get_CollisionBehaviorDesired, put_CollisionBehaviorDesired)
class IMapIconStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapIconStatics'
    _iid_ = Guid('{dcbc9e56-1190-4b5d-9e56-e5b6724aa328}')
    @winrt_commethod(6)
    def get_LocationProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_TitleProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_NormalizedAnchorPointProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    LocationProperty = property(get_LocationProperty, None)
    NormalizedAnchorPointProperty = property(get_NormalizedAnchorPointProperty, None)
    TitleProperty = property(get_TitleProperty, None)
class IMapIconStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapIconStatics2'
    _iid_ = Guid('{ff4c306a-cf76-46ab-a12f-b603b986c696}')
    @winrt_commethod(6)
    def get_CollisionBehaviorDesiredProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    CollisionBehaviorDesiredProperty = property(get_CollisionBehaviorDesiredProperty, None)
class IMapInputEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapInputEventArgs'
    _iid_ = Guid('{9fc503a0-a8a2-4394-92e9-2247764f2f49}')
    @winrt_commethod(6)
    def get_Position(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def get_Location(self) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    Location = property(get_Location, None)
    Position = property(get_Position, None)
class IMapItemsControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapItemsControl'
    _iid_ = Guid('{94c2c4d3-b335-42c5-b660-e6a07ec3bddc}')
    @winrt_commethod(6)
    def get_ItemsSource(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(7)
    def put_ItemsSource(self, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(8)
    def get_Items(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.DependencyObject]: ...
    @winrt_commethod(9)
    def get_ItemTemplate(self) -> win32more.Windows.UI.Xaml.DataTemplate: ...
    @winrt_commethod(10)
    def put_ItemTemplate(self, value: win32more.Windows.UI.Xaml.DataTemplate) -> Void: ...
    ItemTemplate = property(get_ItemTemplate, put_ItemTemplate)
    Items = property(get_Items, None)
    ItemsSource = property(get_ItemsSource, put_ItemsSource)
class IMapItemsControlStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapItemsControlStatics'
    _iid_ = Guid('{33a859c7-789b-425c-8a0a-32385896cb4a}')
    @winrt_commethod(6)
    def get_ItemsSourceProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_ItemsProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_ItemTemplateProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    ItemTemplateProperty = property(get_ItemTemplateProperty, None)
    ItemsProperty = property(get_ItemsProperty, None)
    ItemsSourceProperty = property(get_ItemsSourceProperty, None)
class IMapLayer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapLayer'
    _iid_ = Guid('{6d0ff9c1-a14d-4f97-8f57-46715b57683a}')
    @winrt_commethod(6)
    def get_MapTabIndex(self) -> Int32: ...
    @winrt_commethod(7)
    def put_MapTabIndex(self, value: Int32) -> Void: ...
    @winrt_commethod(8)
    def get_Visible(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_Visible(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_ZIndex(self) -> Int32: ...
    @winrt_commethod(11)
    def put_ZIndex(self, value: Int32) -> Void: ...
    MapTabIndex = property(get_MapTabIndex, put_MapTabIndex)
    Visible = property(get_Visible, put_Visible)
    ZIndex = property(get_ZIndex, put_ZIndex)
class IMapLayerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapLayerFactory'
    _iid_ = Guid('{e02a2207-dee3-47c8-9825-bd029c5752f7}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Maps.MapLayer: ...
class IMapLayerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapLayerStatics'
    _iid_ = Guid('{9ca4a26b-5db9-4f0c-bdd5-b1bffdcce946}')
    @winrt_commethod(6)
    def get_MapTabIndexProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_VisibleProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_ZIndexProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    MapTabIndexProperty = property(get_MapTabIndexProperty, None)
    VisibleProperty = property(get_VisibleProperty, None)
    ZIndexProperty = property(get_ZIndexProperty, None)
class IMapModel3D(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapModel3D'
    _iid_ = Guid('{f8c541a1-ca27-4968-a2bf-9c20f06a0468}')
class IMapModel3DFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapModel3DFactory'
    _iid_ = Guid('{df7f0bcc-580a-498b-939b-0119a9dadb9e}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Maps.MapModel3D: ...
class IMapModel3DStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapModel3DStatics'
    _iid_ = Guid('{4834a480-8e56-4b0f-872d-7ead103187cd}')
    @winrt_commethod(6)
    def CreateFrom3MFAsync(self, source: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.Xaml.Controls.Maps.MapModel3D]: ...
    @winrt_commethod(7)
    def CreateFrom3MFWithShadingOptionAsync(self, source: win32more.Windows.Storage.Streams.IRandomAccessStreamReference, shadingOption: win32more.Windows.UI.Xaml.Controls.Maps.MapModel3DShadingOption) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.Xaml.Controls.Maps.MapModel3D]: ...
class IMapPolygon(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapPolygon'
    _iid_ = Guid('{abda2285-4926-4c3a-a5f9-19df7f69db3d}')
    @winrt_commethod(6)
    def get_Path(self) -> win32more.Windows.Devices.Geolocation.Geopath: ...
    @winrt_commethod(7)
    def put_Path(self, value: win32more.Windows.Devices.Geolocation.Geopath) -> Void: ...
    @winrt_commethod(8)
    def get_StrokeColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(9)
    def put_StrokeColor(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(10)
    def get_StrokeThickness(self) -> Double: ...
    @winrt_commethod(11)
    def put_StrokeThickness(self, value: Double) -> Void: ...
    @winrt_commethod(12)
    def get_StrokeDashed(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_StrokeDashed(self, value: Boolean) -> Void: ...
    @winrt_commethod(14)
    def get_FillColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(15)
    def put_FillColor(self, value: win32more.Windows.UI.Color) -> Void: ...
    FillColor = property(get_FillColor, put_FillColor)
    Path = property(get_Path, put_Path)
    StrokeColor = property(get_StrokeColor, put_StrokeColor)
    StrokeDashed = property(get_StrokeDashed, put_StrokeDashed)
    StrokeThickness = property(get_StrokeThickness, put_StrokeThickness)
class IMapPolygon2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapPolygon2'
    _iid_ = Guid('{96c8a11e-636b-4018-9c2e-acc9122a01b2}')
    @winrt_commethod(6)
    def get_Paths(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Devices.Geolocation.Geopath]: ...
    Paths = property(get_Paths, None)
class IMapPolygonStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapPolygonStatics'
    _iid_ = Guid('{37f573be-097b-424c-87cc-2ee042fda6d2}')
    @winrt_commethod(6)
    def get_PathProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_StrokeThicknessProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_StrokeDashedProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    PathProperty = property(get_PathProperty, None)
    StrokeDashedProperty = property(get_StrokeDashedProperty, None)
    StrokeThicknessProperty = property(get_StrokeThicknessProperty, None)
class IMapPolyline(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapPolyline'
    _iid_ = Guid('{fbad24a2-24df-4a86-8ffa-0f8f4d9ec17d}')
    @winrt_commethod(6)
    def get_Path(self) -> win32more.Windows.Devices.Geolocation.Geopath: ...
    @winrt_commethod(7)
    def put_Path(self, value: win32more.Windows.Devices.Geolocation.Geopath) -> Void: ...
    @winrt_commethod(8)
    def get_StrokeColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(9)
    def put_StrokeColor(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(10)
    def get_StrokeThickness(self) -> Double: ...
    @winrt_commethod(11)
    def put_StrokeThickness(self, value: Double) -> Void: ...
    @winrt_commethod(12)
    def get_StrokeDashed(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_StrokeDashed(self, value: Boolean) -> Void: ...
    Path = property(get_Path, put_Path)
    StrokeColor = property(get_StrokeColor, put_StrokeColor)
    StrokeDashed = property(get_StrokeDashed, put_StrokeDashed)
    StrokeThickness = property(get_StrokeThickness, put_StrokeThickness)
class IMapPolylineStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapPolylineStatics'
    _iid_ = Guid('{61fde44b-1ddf-4303-b809-ec87f58ad065}')
    @winrt_commethod(6)
    def get_PathProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_StrokeDashedProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    PathProperty = property(get_PathProperty, None)
    StrokeDashedProperty = property(get_StrokeDashedProperty, None)
class IMapRightTappedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapRightTappedEventArgs'
    _iid_ = Guid('{20943171-6fe8-40a6-ad0e-297379b575a7}')
    @winrt_commethod(6)
    def get_Position(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def get_Location(self) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    Location = property(get_Location, None)
    Position = property(get_Position, None)
class IMapRouteView(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapRouteView'
    _iid_ = Guid('{740eaec5-bacc-41e1-a67e-dd6513832049}')
    @winrt_commethod(6)
    def get_RouteColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(7)
    def put_RouteColor(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(8)
    def get_OutlineColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(9)
    def put_OutlineColor(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(10)
    def get_Route(self) -> win32more.Windows.Services.Maps.MapRoute: ...
    OutlineColor = property(get_OutlineColor, put_OutlineColor)
    Route = property(get_Route, None)
    RouteColor = property(get_RouteColor, put_RouteColor)
class IMapRouteViewFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapRouteViewFactory'
    _iid_ = Guid('{f083addf-0066-4628-82fe-ea78c23cec1e}')
    @winrt_commethod(6)
    def CreateInstanceWithMapRoute(self, route: win32more.Windows.Services.Maps.MapRoute, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Maps.MapRouteView: ...
class IMapScene(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapScene'
    _iid_ = Guid('{8bba10a9-50e7-482c-9789-c688b178ac24}')
    @winrt_commethod(6)
    def get_TargetCamera(self) -> win32more.Windows.UI.Xaml.Controls.Maps.MapCamera: ...
    @winrt_commethod(7)
    def add_TargetCameraChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapScene, win32more.Windows.UI.Xaml.Controls.Maps.MapTargetCameraChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_TargetCameraChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    TargetCamera = property(get_TargetCamera, None)
    TargetCameraChanged = event()
class IMapSceneStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapSceneStatics'
    _iid_ = Guid('{03e4ad6c-86ec-44d9-9597-fb75b7deba0a}')
    @winrt_commethod(6)
    def CreateFromBoundingBox(self, bounds: win32more.Windows.Devices.Geolocation.GeoboundingBox) -> win32more.Windows.UI.Xaml.Controls.Maps.MapScene: ...
    @winrt_commethod(7)
    def CreateFromBoundingBoxWithHeadingAndPitch(self, bounds: win32more.Windows.Devices.Geolocation.GeoboundingBox, headingInDegrees: Double, pitchInDegrees: Double) -> win32more.Windows.UI.Xaml.Controls.Maps.MapScene: ...
    @winrt_commethod(8)
    def CreateFromCamera(self, camera: win32more.Windows.UI.Xaml.Controls.Maps.MapCamera) -> win32more.Windows.UI.Xaml.Controls.Maps.MapScene: ...
    @winrt_commethod(9)
    def CreateFromLocation(self, location: win32more.Windows.Devices.Geolocation.Geopoint) -> win32more.Windows.UI.Xaml.Controls.Maps.MapScene: ...
    @winrt_commethod(10)
    def CreateFromLocationWithHeadingAndPitch(self, location: win32more.Windows.Devices.Geolocation.Geopoint, headingInDegrees: Double, pitchInDegrees: Double) -> win32more.Windows.UI.Xaml.Controls.Maps.MapScene: ...
    @winrt_commethod(11)
    def CreateFromLocationAndRadius(self, location: win32more.Windows.Devices.Geolocation.Geopoint, radiusInMeters: Double) -> win32more.Windows.UI.Xaml.Controls.Maps.MapScene: ...
    @winrt_commethod(12)
    def CreateFromLocationAndRadiusWithHeadingAndPitch(self, location: win32more.Windows.Devices.Geolocation.Geopoint, radiusInMeters: Double, headingInDegrees: Double, pitchInDegrees: Double) -> win32more.Windows.UI.Xaml.Controls.Maps.MapScene: ...
    @winrt_commethod(13)
    def CreateFromLocations(self, locations: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Devices.Geolocation.Geopoint]) -> win32more.Windows.UI.Xaml.Controls.Maps.MapScene: ...
    @winrt_commethod(14)
    def CreateFromLocationsWithHeadingAndPitch(self, locations: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Devices.Geolocation.Geopoint], headingInDegrees: Double, pitchInDegrees: Double) -> win32more.Windows.UI.Xaml.Controls.Maps.MapScene: ...
class IMapStyleSheet(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapStyleSheet'
    _iid_ = Guid('{ae54b2bf-8991-42ed-8d58-20473deede1d}')
class IMapStyleSheetEntriesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics'
    _iid_ = Guid('{c9636345-ef1a-41a4-a757-bd4f43e1e4d1}')
    @winrt_commethod(6)
    def get_Area(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Airport(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Cemetery(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Continent(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Education(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_IndigenousPeoplesReserve(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_Island(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_Medical(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def get_Military(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def get_Nautical(self) -> WinRT_String: ...
    @winrt_commethod(16)
    def get_Neighborhood(self) -> WinRT_String: ...
    @winrt_commethod(17)
    def get_Runway(self) -> WinRT_String: ...
    @winrt_commethod(18)
    def get_Sand(self) -> WinRT_String: ...
    @winrt_commethod(19)
    def get_ShoppingCenter(self) -> WinRT_String: ...
    @winrt_commethod(20)
    def get_Stadium(self) -> WinRT_String: ...
    @winrt_commethod(21)
    def get_Vegetation(self) -> WinRT_String: ...
    @winrt_commethod(22)
    def get_Forest(self) -> WinRT_String: ...
    @winrt_commethod(23)
    def get_GolfCourse(self) -> WinRT_String: ...
    @winrt_commethod(24)
    def get_Park(self) -> WinRT_String: ...
    @winrt_commethod(25)
    def get_PlayingField(self) -> WinRT_String: ...
    @winrt_commethod(26)
    def get_Reserve(self) -> WinRT_String: ...
    @winrt_commethod(27)
    def get_Point(self) -> WinRT_String: ...
    @winrt_commethod(28)
    def get_NaturalPoint(self) -> WinRT_String: ...
    @winrt_commethod(29)
    def get_Peak(self) -> WinRT_String: ...
    @winrt_commethod(30)
    def get_VolcanicPeak(self) -> WinRT_String: ...
    @winrt_commethod(31)
    def get_WaterPoint(self) -> WinRT_String: ...
    @winrt_commethod(32)
    def get_PointOfInterest(self) -> WinRT_String: ...
    @winrt_commethod(33)
    def get_Business(self) -> WinRT_String: ...
    @winrt_commethod(34)
    def get_FoodPoint(self) -> WinRT_String: ...
    @winrt_commethod(35)
    def get_PopulatedPlace(self) -> WinRT_String: ...
    @winrt_commethod(36)
    def get_Capital(self) -> WinRT_String: ...
    @winrt_commethod(37)
    def get_AdminDistrictCapital(self) -> WinRT_String: ...
    @winrt_commethod(38)
    def get_CountryRegionCapital(self) -> WinRT_String: ...
    @winrt_commethod(39)
    def get_RoadShield(self) -> WinRT_String: ...
    @winrt_commethod(40)
    def get_RoadExit(self) -> WinRT_String: ...
    @winrt_commethod(41)
    def get_Transit(self) -> WinRT_String: ...
    @winrt_commethod(42)
    def get_Political(self) -> WinRT_String: ...
    @winrt_commethod(43)
    def get_CountryRegion(self) -> WinRT_String: ...
    @winrt_commethod(44)
    def get_AdminDistrict(self) -> WinRT_String: ...
    @winrt_commethod(45)
    def get_District(self) -> WinRT_String: ...
    @winrt_commethod(46)
    def get_Structure(self) -> WinRT_String: ...
    @winrt_commethod(47)
    def get_Building(self) -> WinRT_String: ...
    @winrt_commethod(48)
    def get_EducationBuilding(self) -> WinRT_String: ...
    @winrt_commethod(49)
    def get_MedicalBuilding(self) -> WinRT_String: ...
    @winrt_commethod(50)
    def get_TransitBuilding(self) -> WinRT_String: ...
    @winrt_commethod(51)
    def get_Transportation(self) -> WinRT_String: ...
    @winrt_commethod(52)
    def get_Road(self) -> WinRT_String: ...
    @winrt_commethod(53)
    def get_ControlledAccessHighway(self) -> WinRT_String: ...
    @winrt_commethod(54)
    def get_HighSpeedRamp(self) -> WinRT_String: ...
    @winrt_commethod(55)
    def get_Highway(self) -> WinRT_String: ...
    @winrt_commethod(56)
    def get_MajorRoad(self) -> WinRT_String: ...
    @winrt_commethod(57)
    def get_ArterialRoad(self) -> WinRT_String: ...
    @winrt_commethod(58)
    def get_Street(self) -> WinRT_String: ...
    @winrt_commethod(59)
    def get_Ramp(self) -> WinRT_String: ...
    @winrt_commethod(60)
    def get_UnpavedStreet(self) -> WinRT_String: ...
    @winrt_commethod(61)
    def get_TollRoad(self) -> WinRT_String: ...
    @winrt_commethod(62)
    def get_Railway(self) -> WinRT_String: ...
    @winrt_commethod(63)
    def get_Trail(self) -> WinRT_String: ...
    @winrt_commethod(64)
    def get_WaterRoute(self) -> WinRT_String: ...
    @winrt_commethod(65)
    def get_Water(self) -> WinRT_String: ...
    @winrt_commethod(66)
    def get_River(self) -> WinRT_String: ...
    @winrt_commethod(67)
    def get_RouteLine(self) -> WinRT_String: ...
    @winrt_commethod(68)
    def get_WalkingRoute(self) -> WinRT_String: ...
    @winrt_commethod(69)
    def get_DrivingRoute(self) -> WinRT_String: ...
    AdminDistrict = property(get_AdminDistrict, None)
    AdminDistrictCapital = property(get_AdminDistrictCapital, None)
    Airport = property(get_Airport, None)
    Area = property(get_Area, None)
    ArterialRoad = property(get_ArterialRoad, None)
    Building = property(get_Building, None)
    Business = property(get_Business, None)
    Capital = property(get_Capital, None)
    Cemetery = property(get_Cemetery, None)
    Continent = property(get_Continent, None)
    ControlledAccessHighway = property(get_ControlledAccessHighway, None)
    CountryRegion = property(get_CountryRegion, None)
    CountryRegionCapital = property(get_CountryRegionCapital, None)
    District = property(get_District, None)
    DrivingRoute = property(get_DrivingRoute, None)
    Education = property(get_Education, None)
    EducationBuilding = property(get_EducationBuilding, None)
    FoodPoint = property(get_FoodPoint, None)
    Forest = property(get_Forest, None)
    GolfCourse = property(get_GolfCourse, None)
    HighSpeedRamp = property(get_HighSpeedRamp, None)
    Highway = property(get_Highway, None)
    IndigenousPeoplesReserve = property(get_IndigenousPeoplesReserve, None)
    Island = property(get_Island, None)
    MajorRoad = property(get_MajorRoad, None)
    Medical = property(get_Medical, None)
    MedicalBuilding = property(get_MedicalBuilding, None)
    Military = property(get_Military, None)
    NaturalPoint = property(get_NaturalPoint, None)
    Nautical = property(get_Nautical, None)
    Neighborhood = property(get_Neighborhood, None)
    Park = property(get_Park, None)
    Peak = property(get_Peak, None)
    PlayingField = property(get_PlayingField, None)
    Point = property(get_Point, None)
    PointOfInterest = property(get_PointOfInterest, None)
    Political = property(get_Political, None)
    PopulatedPlace = property(get_PopulatedPlace, None)
    Railway = property(get_Railway, None)
    Ramp = property(get_Ramp, None)
    Reserve = property(get_Reserve, None)
    River = property(get_River, None)
    Road = property(get_Road, None)
    RoadExit = property(get_RoadExit, None)
    RoadShield = property(get_RoadShield, None)
    RouteLine = property(get_RouteLine, None)
    Runway = property(get_Runway, None)
    Sand = property(get_Sand, None)
    ShoppingCenter = property(get_ShoppingCenter, None)
    Stadium = property(get_Stadium, None)
    Street = property(get_Street, None)
    Structure = property(get_Structure, None)
    TollRoad = property(get_TollRoad, None)
    Trail = property(get_Trail, None)
    Transit = property(get_Transit, None)
    TransitBuilding = property(get_TransitBuilding, None)
    Transportation = property(get_Transportation, None)
    UnpavedStreet = property(get_UnpavedStreet, None)
    Vegetation = property(get_Vegetation, None)
    VolcanicPeak = property(get_VolcanicPeak, None)
    WalkingRoute = property(get_WalkingRoute, None)
    Water = property(get_Water, None)
    WaterPoint = property(get_WaterPoint, None)
    WaterRoute = property(get_WaterRoute, None)
class IMapStyleSheetEntryStatesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntryStatesStatics'
    _iid_ = Guid('{23ac5532-866d-4bfa-b481-39bea1de3506}')
    @winrt_commethod(6)
    def get_Disabled(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Hover(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Selected(self) -> WinRT_String: ...
    Disabled = property(get_Disabled, None)
    Hover = property(get_Hover, None)
    Selected = property(get_Selected, None)
class IMapStyleSheetStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapStyleSheetStatics'
    _iid_ = Guid('{abbd00ad-0a1c-4335-82f4-61d936aa197d}')
    @winrt_commethod(6)
    def Aerial(self) -> win32more.Windows.UI.Xaml.Controls.Maps.MapStyleSheet: ...
    @winrt_commethod(7)
    def AerialWithOverlay(self) -> win32more.Windows.UI.Xaml.Controls.Maps.MapStyleSheet: ...
    @winrt_commethod(8)
    def RoadLight(self) -> win32more.Windows.UI.Xaml.Controls.Maps.MapStyleSheet: ...
    @winrt_commethod(9)
    def RoadDark(self) -> win32more.Windows.UI.Xaml.Controls.Maps.MapStyleSheet: ...
    @winrt_commethod(10)
    def RoadHighContrastLight(self) -> win32more.Windows.UI.Xaml.Controls.Maps.MapStyleSheet: ...
    @winrt_commethod(11)
    def RoadHighContrastDark(self) -> win32more.Windows.UI.Xaml.Controls.Maps.MapStyleSheet: ...
    @winrt_commethod(12)
    def Combine(self, styleSheets: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Xaml.Controls.Maps.MapStyleSheet]) -> win32more.Windows.UI.Xaml.Controls.Maps.MapStyleSheet: ...
    @winrt_commethod(13)
    def ParseFromJson(self, styleAsJson: WinRT_String) -> win32more.Windows.UI.Xaml.Controls.Maps.MapStyleSheet: ...
    @winrt_commethod(14)
    def TryParseFromJson(self, styleAsJson: WinRT_String, styleSheet: POINTER(win32more.Windows.UI.Xaml.Controls.Maps.MapStyleSheet)) -> Boolean: ...
class IMapTargetCameraChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapTargetCameraChangedEventArgs'
    _iid_ = Guid('{dbf00472-e953-4fa8-97d0-ea86359057cf}')
    @winrt_commethod(6)
    def get_Camera(self) -> win32more.Windows.UI.Xaml.Controls.Maps.MapCamera: ...
    Camera = property(get_Camera, None)
class IMapTargetCameraChangedEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapTargetCameraChangedEventArgs2'
    _iid_ = Guid('{97c0b332-f2b6-460b-8d91-ac020a2383dd}')
    @winrt_commethod(6)
    def get_ChangeReason(self) -> win32more.Windows.UI.Xaml.Controls.Maps.MapCameraChangeReason: ...
    ChangeReason = property(get_ChangeReason, None)
class IMapTileBitmapRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapTileBitmapRequest'
    _iid_ = Guid('{46733fbc-d89d-472b-b5f6-d7066b0584f4}')
    @winrt_commethod(6)
    def get_PixelData(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(7)
    def put_PixelData(self, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> win32more.Windows.UI.Xaml.Controls.Maps.MapTileBitmapRequestDeferral: ...
    PixelData = property(get_PixelData, put_PixelData)
class IMapTileBitmapRequestDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapTileBitmapRequestDeferral'
    _iid_ = Guid('{fe370542-a4ac-4efa-9665-0490b0cafdd2}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IMapTileBitmapRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapTileBitmapRequestedEventArgs'
    _iid_ = Guid('{337f691d-9b02-4aa2-8b1e-cc4d91719bf3}')
    @winrt_commethod(6)
    def get_X(self) -> Int32: ...
    @winrt_commethod(7)
    def get_Y(self) -> Int32: ...
    @winrt_commethod(8)
    def get_ZoomLevel(self) -> Int32: ...
    @winrt_commethod(9)
    def get_Request(self) -> win32more.Windows.UI.Xaml.Controls.Maps.MapTileBitmapRequest: ...
    Request = property(get_Request, None)
    X = property(get_X, None)
    Y = property(get_Y, None)
    ZoomLevel = property(get_ZoomLevel, None)
class IMapTileBitmapRequestedEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapTileBitmapRequestedEventArgs2'
    _iid_ = Guid('{0261d114-246a-5296-bc85-590f53aa39c8}')
    @winrt_commethod(6)
    def get_FrameIndex(self) -> Int32: ...
    FrameIndex = property(get_FrameIndex, None)
class IMapTileDataSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapTileDataSource'
    _iid_ = Guid('{c03d9f5e-be1f-4c69-9969-79467a513c38}')
class IMapTileDataSourceFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapTileDataSourceFactory'
    _iid_ = Guid('{a3920fbd-e446-4648-a74d-fd2c5d557c06}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Maps.MapTileDataSource: ...
class IMapTileSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapTileSource'
    _iid_ = Guid('{88a76e4e-2fdf-4567-9255-1100519c8d62}')
    @winrt_commethod(6)
    def get_DataSource(self) -> win32more.Windows.UI.Xaml.Controls.Maps.MapTileDataSource: ...
    @winrt_commethod(7)
    def put_DataSource(self, value: win32more.Windows.UI.Xaml.Controls.Maps.MapTileDataSource) -> Void: ...
    @winrt_commethod(8)
    def get_Layer(self) -> win32more.Windows.UI.Xaml.Controls.Maps.MapTileLayer: ...
    @winrt_commethod(9)
    def put_Layer(self, value: win32more.Windows.UI.Xaml.Controls.Maps.MapTileLayer) -> Void: ...
    @winrt_commethod(10)
    def get_ZoomLevelRange(self) -> win32more.Windows.UI.Xaml.Controls.Maps.MapZoomLevelRange: ...
    @winrt_commethod(11)
    def put_ZoomLevelRange(self, value: win32more.Windows.UI.Xaml.Controls.Maps.MapZoomLevelRange) -> Void: ...
    @winrt_commethod(12)
    def get_Bounds(self) -> win32more.Windows.Devices.Geolocation.GeoboundingBox: ...
    @winrt_commethod(13)
    def put_Bounds(self, value: win32more.Windows.Devices.Geolocation.GeoboundingBox) -> Void: ...
    @winrt_commethod(14)
    def get_AllowOverstretch(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_AllowOverstretch(self, value: Boolean) -> Void: ...
    @winrt_commethod(16)
    def get_IsFadingEnabled(self) -> Boolean: ...
    @winrt_commethod(17)
    def put_IsFadingEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(18)
    def get_IsTransparencyEnabled(self) -> Boolean: ...
    @winrt_commethod(19)
    def put_IsTransparencyEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(20)
    def get_IsRetryEnabled(self) -> Boolean: ...
    @winrt_commethod(21)
    def put_IsRetryEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(22)
    def get_ZIndex(self) -> Int32: ...
    @winrt_commethod(23)
    def put_ZIndex(self, value: Int32) -> Void: ...
    @winrt_commethod(24)
    def get_TilePixelSize(self) -> Int32: ...
    @winrt_commethod(25)
    def put_TilePixelSize(self, value: Int32) -> Void: ...
    @winrt_commethod(26)
    def get_Visible(self) -> Boolean: ...
    @winrt_commethod(27)
    def put_Visible(self, value: Boolean) -> Void: ...
    AllowOverstretch = property(get_AllowOverstretch, put_AllowOverstretch)
    Bounds = property(get_Bounds, put_Bounds)
    DataSource = property(get_DataSource, put_DataSource)
    IsFadingEnabled = property(get_IsFadingEnabled, put_IsFadingEnabled)
    IsRetryEnabled = property(get_IsRetryEnabled, put_IsRetryEnabled)
    IsTransparencyEnabled = property(get_IsTransparencyEnabled, put_IsTransparencyEnabled)
    Layer = property(get_Layer, put_Layer)
    TilePixelSize = property(get_TilePixelSize, put_TilePixelSize)
    Visible = property(get_Visible, put_Visible)
    ZIndex = property(get_ZIndex, put_ZIndex)
    ZoomLevelRange = property(get_ZoomLevelRange, put_ZoomLevelRange)
class IMapTileSource2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapTileSource2'
    _iid_ = Guid('{8e65ebbd-4095-5c15-99f1-1260b4e8b0a9}')
    @winrt_commethod(6)
    def get_AnimationState(self) -> win32more.Windows.UI.Xaml.Controls.Maps.MapTileAnimationState: ...
    @winrt_commethod(7)
    def get_AutoPlay(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_AutoPlay(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_FrameCount(self) -> Int32: ...
    @winrt_commethod(10)
    def put_FrameCount(self, value: Int32) -> Void: ...
    @winrt_commethod(11)
    def get_FrameDuration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(12)
    def put_FrameDuration(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(13)
    def Pause(self) -> Void: ...
    @winrt_commethod(14)
    def Play(self) -> Void: ...
    @winrt_commethod(15)
    def Stop(self) -> Void: ...
    AnimationState = property(get_AnimationState, None)
    AutoPlay = property(get_AutoPlay, put_AutoPlay)
    FrameCount = property(get_FrameCount, put_FrameCount)
    FrameDuration = property(get_FrameDuration, put_FrameDuration)
class IMapTileSourceFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapTileSourceFactory'
    _iid_ = Guid('{cd7f811f-77fa-482b-9d34-71d31d465c48}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Maps.MapTileSource: ...
    @winrt_commethod(7)
    def CreateInstanceWithDataSource(self, dataSource: win32more.Windows.UI.Xaml.Controls.Maps.MapTileDataSource, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Maps.MapTileSource: ...
    @winrt_commethod(8)
    def CreateInstanceWithDataSourceAndZoomRange(self, dataSource: win32more.Windows.UI.Xaml.Controls.Maps.MapTileDataSource, zoomLevelRange: win32more.Windows.UI.Xaml.Controls.Maps.MapZoomLevelRange, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Maps.MapTileSource: ...
    @winrt_commethod(9)
    def CreateInstanceWithDataSourceZoomRangeAndBounds(self, dataSource: win32more.Windows.UI.Xaml.Controls.Maps.MapTileDataSource, zoomLevelRange: win32more.Windows.UI.Xaml.Controls.Maps.MapZoomLevelRange, bounds: win32more.Windows.Devices.Geolocation.GeoboundingBox, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Maps.MapTileSource: ...
    @winrt_commethod(10)
    def CreateInstanceWithDataSourceZoomRangeBoundsAndTileSize(self, dataSource: win32more.Windows.UI.Xaml.Controls.Maps.MapTileDataSource, zoomLevelRange: win32more.Windows.UI.Xaml.Controls.Maps.MapZoomLevelRange, bounds: win32more.Windows.Devices.Geolocation.GeoboundingBox, tileSizeInPixels: Int32, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Maps.MapTileSource: ...
class IMapTileSourceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapTileSourceStatics'
    _iid_ = Guid('{93fcc93c-7035-4603-99b1-e659921b6093}')
    @winrt_commethod(6)
    def get_DataSourceProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_LayerProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_ZoomLevelRangeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_BoundsProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_AllowOverstretchProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_IsFadingEnabledProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(12)
    def get_IsTransparencyEnabledProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def get_IsRetryEnabledProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(14)
    def get_ZIndexProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(15)
    def get_TilePixelSizeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(16)
    def get_VisibleProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    AllowOverstretchProperty = property(get_AllowOverstretchProperty, None)
    BoundsProperty = property(get_BoundsProperty, None)
    DataSourceProperty = property(get_DataSourceProperty, None)
    IsFadingEnabledProperty = property(get_IsFadingEnabledProperty, None)
    IsRetryEnabledProperty = property(get_IsRetryEnabledProperty, None)
    IsTransparencyEnabledProperty = property(get_IsTransparencyEnabledProperty, None)
    LayerProperty = property(get_LayerProperty, None)
    TilePixelSizeProperty = property(get_TilePixelSizeProperty, None)
    VisibleProperty = property(get_VisibleProperty, None)
    ZIndexProperty = property(get_ZIndexProperty, None)
    ZoomLevelRangeProperty = property(get_ZoomLevelRangeProperty, None)
class IMapTileSourceStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapTileSourceStatics2'
    _iid_ = Guid('{75cdd47e-669c-50fd-ad85-5ea5174cf59b}')
    @winrt_commethod(6)
    def get_AnimationStateProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_AutoPlayProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_FrameCountProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_FrameDurationProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    AnimationStateProperty = property(get_AnimationStateProperty, None)
    AutoPlayProperty = property(get_AutoPlayProperty, None)
    FrameCountProperty = property(get_FrameCountProperty, None)
    FrameDurationProperty = property(get_FrameDurationProperty, None)
class IMapTileUriRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapTileUriRequest'
    _iid_ = Guid('{17402335-3127-45b8-87a7-99f87d4e2745}')
    @winrt_commethod(6)
    def get_Uri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def put_Uri(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> win32more.Windows.UI.Xaml.Controls.Maps.MapTileUriRequestDeferral: ...
    Uri = property(get_Uri, put_Uri)
class IMapTileUriRequestDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapTileUriRequestDeferral'
    _iid_ = Guid('{c117ade0-bf3e-4c51-8faa-4b593cf68eb2}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IMapTileUriRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapTileUriRequestedEventArgs'
    _iid_ = Guid('{d2147b43-1bbf-4b98-8dd3-b7834e407e0d}')
    @winrt_commethod(6)
    def get_X(self) -> Int32: ...
    @winrt_commethod(7)
    def get_Y(self) -> Int32: ...
    @winrt_commethod(8)
    def get_ZoomLevel(self) -> Int32: ...
    @winrt_commethod(9)
    def get_Request(self) -> win32more.Windows.UI.Xaml.Controls.Maps.MapTileUriRequest: ...
    Request = property(get_Request, None)
    X = property(get_X, None)
    Y = property(get_Y, None)
    ZoomLevel = property(get_ZoomLevel, None)
class IMapTileUriRequestedEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapTileUriRequestedEventArgs2'
    _iid_ = Guid('{2302185d-33b5-5a55-92f5-74a86a22efa6}')
    @winrt_commethod(6)
    def get_FrameIndex(self) -> Int32: ...
    FrameIndex = property(get_FrameIndex, None)
class IStreetsideExperience(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IStreetsideExperience'
    _iid_ = Guid('{a558aec9-e30c-46c8-8116-484691675558}')
    @winrt_commethod(6)
    def get_AddressTextVisible(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_AddressTextVisible(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_CursorVisible(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_CursorVisible(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_OverviewMapVisible(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_OverviewMapVisible(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_StreetLabelsVisible(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_StreetLabelsVisible(self, value: Boolean) -> Void: ...
    @winrt_commethod(14)
    def get_ExitButtonVisible(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_ExitButtonVisible(self, value: Boolean) -> Void: ...
    @winrt_commethod(16)
    def get_ZoomButtonsVisible(self) -> Boolean: ...
    @winrt_commethod(17)
    def put_ZoomButtonsVisible(self, value: Boolean) -> Void: ...
    AddressTextVisible = property(get_AddressTextVisible, put_AddressTextVisible)
    CursorVisible = property(get_CursorVisible, put_CursorVisible)
    ExitButtonVisible = property(get_ExitButtonVisible, put_ExitButtonVisible)
    OverviewMapVisible = property(get_OverviewMapVisible, put_OverviewMapVisible)
    StreetLabelsVisible = property(get_StreetLabelsVisible, put_StreetLabelsVisible)
    ZoomButtonsVisible = property(get_ZoomButtonsVisible, put_ZoomButtonsVisible)
class IStreetsideExperienceFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IStreetsideExperienceFactory'
    _iid_ = Guid('{7a5bcf3c-649e-4342-9995-68a6cf5961a7}')
    @winrt_commethod(6)
    def CreateInstanceWithPanorama(self, panorama: win32more.Windows.UI.Xaml.Controls.Maps.StreetsidePanorama) -> win32more.Windows.UI.Xaml.Controls.Maps.StreetsideExperience: ...
    @winrt_commethod(7)
    def CreateInstanceWithPanoramaHeadingPitchAndFieldOfView(self, panorama: win32more.Windows.UI.Xaml.Controls.Maps.StreetsidePanorama, headingInDegrees: Double, pitchInDegrees: Double, fieldOfViewInDegrees: Double) -> win32more.Windows.UI.Xaml.Controls.Maps.StreetsideExperience: ...
class IStreetsidePanorama(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IStreetsidePanorama'
    _iid_ = Guid('{6fe00fd8-ad60-4664-b539-b1069f16c5af}')
    @winrt_commethod(6)
    def get_Location(self) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    Location = property(get_Location, None)
class IStreetsidePanoramaStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IStreetsidePanoramaStatics'
    _iid_ = Guid('{d3b47f69-54b3-4ec5-b2a0-4f8204576507}')
    @winrt_commethod(6)
    def FindNearbyWithLocationAsync(self, location: win32more.Windows.Devices.Geolocation.Geopoint) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.Xaml.Controls.Maps.StreetsidePanorama]: ...
    @winrt_commethod(7)
    def FindNearbyWithLocationAndRadiusAsync(self, location: win32more.Windows.Devices.Geolocation.Geopoint, radiusInMeters: Double) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.Xaml.Controls.Maps.StreetsidePanorama]: ...
class LocalMapTileDataSource(ComPtr):
    extends: win32more.Windows.UI.Xaml.Controls.Maps.MapTileDataSource
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.ILocalMapTileDataSource
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.LocalMapTileDataSource'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.LocalMapTileDataSource.CreateInstance(*args, None, None))
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.LocalMapTileDataSource.CreateInstanceWithUriFormatString(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Controls.Maps.ILocalMapTileDataSourceFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Maps.LocalMapTileDataSource: ...
    @winrt_factorymethod
    def CreateInstanceWithUriFormatString(cls: win32more.Windows.UI.Xaml.Controls.Maps.ILocalMapTileDataSourceFactory, uriFormatString: WinRT_String, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Maps.LocalMapTileDataSource: ...
    @winrt_mixinmethod
    def get_UriFormatString(self: win32more.Windows.UI.Xaml.Controls.Maps.ILocalMapTileDataSource) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_UriFormatString(self: win32more.Windows.UI.Xaml.Controls.Maps.ILocalMapTileDataSource, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def add_UriRequested(self: win32more.Windows.UI.Xaml.Controls.Maps.ILocalMapTileDataSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.LocalMapTileDataSource, win32more.Windows.UI.Xaml.Controls.Maps.MapTileUriRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UriRequested(self: win32more.Windows.UI.Xaml.Controls.Maps.ILocalMapTileDataSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    UriFormatString = property(get_UriFormatString, put_UriFormatString)
    UriRequested = event()
class MapActualCameraChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IMapActualCameraChangedEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapActualCameraChangedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapActualCameraChangedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Controls.Maps.MapActualCameraChangedEventArgs: ...
    @winrt_mixinmethod
    def get_Camera(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapActualCameraChangedEventArgs) -> win32more.Windows.UI.Xaml.Controls.Maps.MapCamera: ...
    @winrt_mixinmethod
    def get_ChangeReason(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapActualCameraChangedEventArgs2) -> win32more.Windows.UI.Xaml.Controls.Maps.MapCameraChangeReason: ...
    Camera = property(get_Camera, None)
    ChangeReason = property(get_ChangeReason, None)
class MapActualCameraChangingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IMapActualCameraChangingEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapActualCameraChangingEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapActualCameraChangingEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Controls.Maps.MapActualCameraChangingEventArgs: ...
    @winrt_mixinmethod
    def get_Camera(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapActualCameraChangingEventArgs) -> win32more.Windows.UI.Xaml.Controls.Maps.MapCamera: ...
    @winrt_mixinmethod
    def get_ChangeReason(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapActualCameraChangingEventArgs2) -> win32more.Windows.UI.Xaml.Controls.Maps.MapCameraChangeReason: ...
    Camera = property(get_Camera, None)
    ChangeReason = property(get_ChangeReason, None)
class MapAnimationKind(Enum, Int32):
    Default = 0
    None_ = 1
    Linear = 2
    Bow = 3
class _MapBillboard_Meta_(ComPtr.__class__):
    pass
class MapBillboard(ComPtr, metaclass=_MapBillboard_Meta_):
    extends: win32more.Windows.UI.Xaml.Controls.Maps.MapElement
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IMapBillboard
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapBillboard'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapBillboard.CreateInstanceFromCamera(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceFromCamera(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapBillboardFactory, camera: win32more.Windows.UI.Xaml.Controls.Maps.MapCamera) -> win32more.Windows.UI.Xaml.Controls.Maps.MapBillboard: ...
    @winrt_mixinmethod
    def get_Location(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapBillboard) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def put_Location(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapBillboard, value: win32more.Windows.Devices.Geolocation.Geopoint) -> Void: ...
    @winrt_mixinmethod
    def get_NormalizedAnchorPoint(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapBillboard) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_NormalizedAnchorPoint(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapBillboard, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_Image(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapBillboard) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def put_Image(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapBillboard, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_mixinmethod
    def get_CollisionBehaviorDesired(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapBillboard) -> win32more.Windows.UI.Xaml.Controls.Maps.MapElementCollisionBehavior: ...
    @winrt_mixinmethod
    def put_CollisionBehaviorDesired(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapBillboard, value: win32more.Windows.UI.Xaml.Controls.Maps.MapElementCollisionBehavior) -> Void: ...
    @winrt_mixinmethod
    def get_ReferenceCamera(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapBillboard) -> win32more.Windows.UI.Xaml.Controls.Maps.MapCamera: ...
    @winrt_classmethod
    def get_LocationProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapBillboardStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_NormalizedAnchorPointProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapBillboardStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CollisionBehaviorDesiredProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapBillboardStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    CollisionBehaviorDesired = property(get_CollisionBehaviorDesired, put_CollisionBehaviorDesired)
    Image = property(get_Image, put_Image)
    Location = property(get_Location, put_Location)
    NormalizedAnchorPoint = property(get_NormalizedAnchorPoint, put_NormalizedAnchorPoint)
    ReferenceCamera = property(get_ReferenceCamera, None)
    _MapBillboard_Meta_.CollisionBehaviorDesiredProperty = property(get_CollisionBehaviorDesiredProperty, None)
    _MapBillboard_Meta_.LocationProperty = property(get_LocationProperty, None)
    _MapBillboard_Meta_.NormalizedAnchorPointProperty = property(get_NormalizedAnchorPointProperty, None)
class MapCamera(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IMapCamera
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapCamera'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapCamera.CreateInstanceWithLocation(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapCamera.CreateInstanceWithLocationAndHeading(*args))
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapCamera.CreateInstanceWithLocationHeadingAndPitch(*args))
        elif len(args) == 5:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapCamera.CreateInstanceWithLocationHeadingPitchRollAndFieldOfView(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithLocation(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapCameraFactory, location: win32more.Windows.Devices.Geolocation.Geopoint) -> win32more.Windows.UI.Xaml.Controls.Maps.MapCamera: ...
    @winrt_factorymethod
    def CreateInstanceWithLocationAndHeading(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapCameraFactory, location: win32more.Windows.Devices.Geolocation.Geopoint, headingInDegrees: Double) -> win32more.Windows.UI.Xaml.Controls.Maps.MapCamera: ...
    @winrt_factorymethod
    def CreateInstanceWithLocationHeadingAndPitch(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapCameraFactory, location: win32more.Windows.Devices.Geolocation.Geopoint, headingInDegrees: Double, pitchInDegrees: Double) -> win32more.Windows.UI.Xaml.Controls.Maps.MapCamera: ...
    @winrt_factorymethod
    def CreateInstanceWithLocationHeadingPitchRollAndFieldOfView(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapCameraFactory, location: win32more.Windows.Devices.Geolocation.Geopoint, headingInDegrees: Double, pitchInDegrees: Double, rollInDegrees: Double, fieldOfViewInDegrees: Double) -> win32more.Windows.UI.Xaml.Controls.Maps.MapCamera: ...
    @winrt_mixinmethod
    def get_Location(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapCamera) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def put_Location(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapCamera, value: win32more.Windows.Devices.Geolocation.Geopoint) -> Void: ...
    @winrt_mixinmethod
    def get_Heading(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapCamera) -> Double: ...
    @winrt_mixinmethod
    def put_Heading(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapCamera, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Pitch(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapCamera) -> Double: ...
    @winrt_mixinmethod
    def put_Pitch(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapCamera, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Roll(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapCamera) -> Double: ...
    @winrt_mixinmethod
    def put_Roll(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapCamera, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_FieldOfView(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapCamera) -> Double: ...
    @winrt_mixinmethod
    def put_FieldOfView(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapCamera, value: Double) -> Void: ...
    FieldOfView = property(get_FieldOfView, put_FieldOfView)
    Heading = property(get_Heading, put_Heading)
    Location = property(get_Location, put_Location)
    Pitch = property(get_Pitch, put_Pitch)
    Roll = property(get_Roll, put_Roll)
class MapCameraChangeReason(Enum, Int32):
    System = 0
    UserInteraction = 1
    Programmatic = 2
class MapColorScheme(Enum, Int32):
    Light = 0
    Dark = 1
class MapContextRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IMapContextRequestedEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapContextRequestedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapContextRequestedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Controls.Maps.MapContextRequestedEventArgs: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapContextRequestedEventArgs) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Location(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapContextRequestedEventArgs) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def get_MapElements(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapContextRequestedEventArgs) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Xaml.Controls.Maps.MapElement]: ...
    Location = property(get_Location, None)
    MapElements = property(get_MapElements, None)
    Position = property(get_Position, None)
class _MapControl_Meta_(ComPtr.__class__):
    pass
class MapControl(ComPtr, metaclass=_MapControl_Meta_):
    extends: win32more.Windows.UI.Xaml.Controls.Control
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapControl'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapControl.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Controls.Maps.MapControl: ...
    @winrt_mixinmethod
    def get_Center(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def put_Center(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl, value: win32more.Windows.Devices.Geolocation.Geopoint) -> Void: ...
    @winrt_mixinmethod
    def get_Children(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.DependencyObject]: ...
    @winrt_mixinmethod
    def get_ColorScheme(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl) -> win32more.Windows.UI.Xaml.Controls.Maps.MapColorScheme: ...
    @winrt_mixinmethod
    def put_ColorScheme(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl, value: win32more.Windows.UI.Xaml.Controls.Maps.MapColorScheme) -> Void: ...
    @winrt_mixinmethod
    def get_DesiredPitch(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl) -> Double: ...
    @winrt_mixinmethod
    def put_DesiredPitch(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Heading(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl) -> Double: ...
    @winrt_mixinmethod
    def put_Heading(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_LandmarksVisible(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_LandmarksVisible(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_LoadingStatus(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl) -> win32more.Windows.UI.Xaml.Controls.Maps.MapLoadingStatus: ...
    @winrt_mixinmethod
    def get_MapServiceToken(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_MapServiceToken(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_MaxZoomLevel(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl) -> Double: ...
    @winrt_mixinmethod
    def get_MinZoomLevel(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl) -> Double: ...
    @winrt_mixinmethod
    def get_PedestrianFeaturesVisible(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_PedestrianFeaturesVisible(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Pitch(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl) -> Double: ...
    @winrt_mixinmethod
    def get_Style(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl) -> win32more.Windows.UI.Xaml.Controls.Maps.MapStyle: ...
    @winrt_mixinmethod
    def put_Style(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl, value: win32more.Windows.UI.Xaml.Controls.Maps.MapStyle) -> Void: ...
    @winrt_mixinmethod
    def get_TrafficFlowVisible(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_TrafficFlowVisible(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_TransformOrigin(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_TransformOrigin(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_WatermarkMode(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl) -> win32more.Windows.UI.Xaml.Controls.Maps.MapWatermarkMode: ...
    @winrt_mixinmethod
    def put_WatermarkMode(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl, value: win32more.Windows.UI.Xaml.Controls.Maps.MapWatermarkMode) -> Void: ...
    @winrt_mixinmethod
    def get_ZoomLevel(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl) -> Double: ...
    @winrt_mixinmethod
    def put_ZoomLevel(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_MapElements(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Controls.Maps.MapElement]: ...
    @winrt_mixinmethod
    def get_Routes(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Controls.Maps.MapRouteView]: ...
    @winrt_mixinmethod
    def get_TileSources(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Controls.Maps.MapTileSource]: ...
    @winrt_mixinmethod
    def add_CenterChanged(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CenterChanged(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_HeadingChanged(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HeadingChanged(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_LoadingStatusChanged(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_LoadingStatusChanged(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_MapDoubleTapped(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.UI.Xaml.Controls.Maps.MapInputEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MapDoubleTapped(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_MapHolding(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.UI.Xaml.Controls.Maps.MapInputEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MapHolding(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_MapTapped(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.UI.Xaml.Controls.Maps.MapInputEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MapTapped(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PitchChanged(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PitchChanged(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_TransformOriginChanged(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TransformOriginChanged(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ZoomLevelChanged(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ZoomLevelChanged(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def FindMapElementsAtOffset(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl, offset: win32more.Windows.Foundation.Point) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Xaml.Controls.Maps.MapElement]: ...
    @winrt_mixinmethod
    def GetLocationFromOffset(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl, offset: win32more.Windows.Foundation.Point, location: POINTER(win32more.Windows.Devices.Geolocation.Geopoint)) -> Void: ...
    @winrt_mixinmethod
    def GetOffsetFromLocation(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl, location: win32more.Windows.Devices.Geolocation.Geopoint, offset: POINTER(win32more.Windows.Foundation.Point)) -> Void: ...
    @winrt_mixinmethod
    def IsLocationInView(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl, location: win32more.Windows.Devices.Geolocation.Geopoint, isInView: POINTER(Boolean)) -> Void: ...
    @winrt_mixinmethod
    def TrySetViewBoundsAsync(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl, bounds: win32more.Windows.Devices.Geolocation.GeoboundingBox, margin: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Xaml.Thickness], animation: win32more.Windows.UI.Xaml.Controls.Maps.MapAnimationKind) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TrySetViewWithCenterAsync(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl, center: win32more.Windows.Devices.Geolocation.Geopoint) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TrySetViewWithCenterAndZoomAsync(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl, center: win32more.Windows.Devices.Geolocation.Geopoint, zoomLevel: win32more.Windows.Foundation.IReference[Double]) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TrySetViewWithCenterZoomHeadingAndPitchAsync(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl, center: win32more.Windows.Devices.Geolocation.Geopoint, zoomLevel: win32more.Windows.Foundation.IReference[Double], heading: win32more.Windows.Foundation.IReference[Double], desiredPitch: win32more.Windows.Foundation.IReference[Double]) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TrySetViewWithCenterZoomHeadingPitchAndAnimationAsync(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl, center: win32more.Windows.Devices.Geolocation.Geopoint, zoomLevel: win32more.Windows.Foundation.IReference[Double], heading: win32more.Windows.Foundation.IReference[Double], desiredPitch: win32more.Windows.Foundation.IReference[Double], animation: win32more.Windows.UI.Xaml.Controls.Maps.MapAnimationKind) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def get_BusinessLandmarksVisible(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2) -> Boolean: ...
    @winrt_mixinmethod
    def put_BusinessLandmarksVisible(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_TransitFeaturesVisible(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2) -> Boolean: ...
    @winrt_mixinmethod
    def put_TransitFeaturesVisible(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_PanInteractionMode(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2) -> win32more.Windows.UI.Xaml.Controls.Maps.MapPanInteractionMode: ...
    @winrt_mixinmethod
    def put_PanInteractionMode(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2, value: win32more.Windows.UI.Xaml.Controls.Maps.MapPanInteractionMode) -> Void: ...
    @winrt_mixinmethod
    def get_RotateInteractionMode(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2) -> win32more.Windows.UI.Xaml.Controls.Maps.MapInteractionMode: ...
    @winrt_mixinmethod
    def put_RotateInteractionMode(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2, value: win32more.Windows.UI.Xaml.Controls.Maps.MapInteractionMode) -> Void: ...
    @winrt_mixinmethod
    def get_TiltInteractionMode(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2) -> win32more.Windows.UI.Xaml.Controls.Maps.MapInteractionMode: ...
    @winrt_mixinmethod
    def put_TiltInteractionMode(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2, value: win32more.Windows.UI.Xaml.Controls.Maps.MapInteractionMode) -> Void: ...
    @winrt_mixinmethod
    def get_ZoomInteractionMode(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2) -> win32more.Windows.UI.Xaml.Controls.Maps.MapInteractionMode: ...
    @winrt_mixinmethod
    def put_ZoomInteractionMode(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2, value: win32more.Windows.UI.Xaml.Controls.Maps.MapInteractionMode) -> Void: ...
    @winrt_mixinmethod
    def get_Is3DSupported(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsStreetsideSupported(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2) -> Boolean: ...
    @winrt_mixinmethod
    def get_Scene(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2) -> win32more.Windows.UI.Xaml.Controls.Maps.MapScene: ...
    @winrt_mixinmethod
    def put_Scene(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2, value: win32more.Windows.UI.Xaml.Controls.Maps.MapScene) -> Void: ...
    @winrt_mixinmethod
    def get_ActualCamera(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2) -> win32more.Windows.UI.Xaml.Controls.Maps.MapCamera: ...
    @winrt_mixinmethod
    def get_TargetCamera(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2) -> win32more.Windows.UI.Xaml.Controls.Maps.MapCamera: ...
    @winrt_mixinmethod
    def get_CustomExperience(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2) -> win32more.Windows.UI.Xaml.Controls.Maps.MapCustomExperience: ...
    @winrt_mixinmethod
    def put_CustomExperience(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2, value: win32more.Windows.UI.Xaml.Controls.Maps.MapCustomExperience) -> Void: ...
    @winrt_mixinmethod
    def add_MapElementClick(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.UI.Xaml.Controls.Maps.MapElementClickEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MapElementClick(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_MapElementPointerEntered(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.UI.Xaml.Controls.Maps.MapElementPointerEnteredEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MapElementPointerEntered(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_MapElementPointerExited(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.UI.Xaml.Controls.Maps.MapElementPointerExitedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MapElementPointerExited(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ActualCameraChanged(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.UI.Xaml.Controls.Maps.MapActualCameraChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ActualCameraChanged(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ActualCameraChanging(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.UI.Xaml.Controls.Maps.MapActualCameraChangingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ActualCameraChanging(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_TargetCameraChanged(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.UI.Xaml.Controls.Maps.MapTargetCameraChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TargetCameraChanged(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_CustomExperienceChanged(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.UI.Xaml.Controls.Maps.MapCustomExperienceChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CustomExperienceChanged(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def StartContinuousRotate(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2, rateInDegreesPerSecond: Double) -> Void: ...
    @winrt_mixinmethod
    def StopContinuousRotate(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2) -> Void: ...
    @winrt_mixinmethod
    def StartContinuousTilt(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2, rateInDegreesPerSecond: Double) -> Void: ...
    @winrt_mixinmethod
    def StopContinuousTilt(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2) -> Void: ...
    @winrt_mixinmethod
    def StartContinuousZoom(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2, rateOfChangePerSecond: Double) -> Void: ...
    @winrt_mixinmethod
    def StopContinuousZoom(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2) -> Void: ...
    @winrt_mixinmethod
    def TryRotateAsync(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2, degrees: Double) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryRotateToAsync(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2, angleInDegrees: Double) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryTiltAsync(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2, degrees: Double) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryTiltToAsync(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2, angleInDegrees: Double) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryZoomInAsync(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryZoomOutAsync(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryZoomToAsync(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2, zoomLevel: Double) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TrySetSceneAsync(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2, scene: win32more.Windows.UI.Xaml.Controls.Maps.MapScene) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TrySetSceneWithAnimationAsync(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl2, scene: win32more.Windows.UI.Xaml.Controls.Maps.MapScene, animationKind: win32more.Windows.UI.Xaml.Controls.Maps.MapAnimationKind) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def add_MapRightTapped(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl3, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.UI.Xaml.Controls.Maps.MapRightTappedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MapRightTapped(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl3, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_BusinessLandmarksEnabled(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl4) -> Boolean: ...
    @winrt_mixinmethod
    def put_BusinessLandmarksEnabled(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl4, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_TransitFeaturesEnabled(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl4) -> Boolean: ...
    @winrt_mixinmethod
    def put_TransitFeaturesEnabled(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl4, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def GetVisibleRegion(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl4, region: win32more.Windows.UI.Xaml.Controls.Maps.MapVisibleRegionKind) -> win32more.Windows.Devices.Geolocation.Geopath: ...
    @winrt_mixinmethod
    def get_MapProjection(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl5) -> win32more.Windows.UI.Xaml.Controls.Maps.MapProjection: ...
    @winrt_mixinmethod
    def put_MapProjection(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl5, value: win32more.Windows.UI.Xaml.Controls.Maps.MapProjection) -> Void: ...
    @winrt_mixinmethod
    def get_StyleSheet(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl5) -> win32more.Windows.UI.Xaml.Controls.Maps.MapStyleSheet: ...
    @winrt_mixinmethod
    def put_StyleSheet(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl5, value: win32more.Windows.UI.Xaml.Controls.Maps.MapStyleSheet) -> Void: ...
    @winrt_mixinmethod
    def get_ViewPadding(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl5) -> win32more.Windows.UI.Xaml.Thickness: ...
    @winrt_mixinmethod
    def put_ViewPadding(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl5, value: win32more.Windows.UI.Xaml.Thickness) -> Void: ...
    @winrt_mixinmethod
    def add_MapContextRequested(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl5, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.UI.Xaml.Controls.Maps.MapContextRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MapContextRequested(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl5, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def FindMapElementsAtOffsetWithRadius(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl5, offset: win32more.Windows.Foundation.Point, radius: Double) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Xaml.Controls.Maps.MapElement]: ...
    @winrt_mixinmethod
    def GetLocationFromOffsetWithReferenceSystem(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl5, offset: win32more.Windows.Foundation.Point, desiredReferenceSystem: win32more.Windows.Devices.Geolocation.AltitudeReferenceSystem, location: POINTER(win32more.Windows.Devices.Geolocation.Geopoint)) -> Void: ...
    @winrt_mixinmethod
    def StartContinuousPan(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl5, horizontalPixelsPerSecond: Double, verticalPixelsPerSecond: Double) -> Void: ...
    @winrt_mixinmethod
    def StopContinuousPan(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl5) -> Void: ...
    @winrt_mixinmethod
    def TryPanAsync(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl5, horizontalPixels: Double, verticalPixels: Double) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryPanToAsync(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl5, location: win32more.Windows.Devices.Geolocation.Geopoint) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def get_Layers(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl6) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Controls.Maps.MapLayer]: ...
    @winrt_mixinmethod
    def put_Layers(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl6, value: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Controls.Maps.MapLayer]) -> Void: ...
    @winrt_mixinmethod
    def TryGetLocationFromOffset(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl6, offset: win32more.Windows.Foundation.Point, location: POINTER(win32more.Windows.Devices.Geolocation.Geopoint)) -> Boolean: ...
    @winrt_mixinmethod
    def TryGetLocationFromOffsetWithReferenceSystem(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl6, offset: win32more.Windows.Foundation.Point, desiredReferenceSystem: win32more.Windows.Devices.Geolocation.AltitudeReferenceSystem, location: POINTER(win32more.Windows.Devices.Geolocation.Geopoint)) -> Boolean: ...
    @winrt_mixinmethod
    def get_Region(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl7) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Region(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl7, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_CanTiltDown(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl8) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanTiltUp(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl8) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanZoomIn(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl8) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanZoomOut(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControl8) -> Boolean: ...
    @winrt_classmethod
    def get_CanTiltDownProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlStatics8) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CanTiltUpProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlStatics8) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CanZoomInProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlStatics8) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CanZoomOutProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlStatics8) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RegionProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlStatics7) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_LayersProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlStatics6) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_MapProjectionProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlStatics5) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StyleSheetProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlStatics5) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ViewPaddingProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlStatics5) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_BusinessLandmarksEnabledProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlStatics4) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TransitFeaturesEnabledProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlStatics4) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_BusinessLandmarksVisibleProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlStatics2) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TransitFeaturesVisibleProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlStatics2) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_PanInteractionModeProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlStatics2) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RotateInteractionModeProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlStatics2) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TiltInteractionModeProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlStatics2) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ZoomInteractionModeProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlStatics2) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_Is3DSupportedProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlStatics2) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsStreetsideSupportedProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlStatics2) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SceneProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlStatics2) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CenterProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ChildrenProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ColorSchemeProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_DesiredPitchProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_HeadingProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_LandmarksVisibleProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_LoadingStatusProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_MapServiceTokenProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_PedestrianFeaturesVisibleProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_PitchProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StyleProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TrafficFlowVisibleProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TransformOriginProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_WatermarkModeProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ZoomLevelProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_MapElementsProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RoutesProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TileSourcesProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_LocationProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetLocation(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlStatics, element: win32more.Windows.UI.Xaml.DependencyObject) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_classmethod
    def SetLocation(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlStatics, element: win32more.Windows.UI.Xaml.DependencyObject, value: win32more.Windows.Devices.Geolocation.Geopoint) -> Void: ...
    @winrt_classmethod
    def get_NormalizedAnchorPointProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetNormalizedAnchorPoint(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlStatics, element: win32more.Windows.UI.Xaml.DependencyObject) -> win32more.Windows.Foundation.Point: ...
    @winrt_classmethod
    def SetNormalizedAnchorPoint(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlStatics, element: win32more.Windows.UI.Xaml.DependencyObject, value: win32more.Windows.Foundation.Point) -> Void: ...
    ActualCamera = property(get_ActualCamera, None)
    BusinessLandmarksEnabled = property(get_BusinessLandmarksEnabled, put_BusinessLandmarksEnabled)
    BusinessLandmarksVisible = property(get_BusinessLandmarksVisible, put_BusinessLandmarksVisible)
    CanTiltDown = property(get_CanTiltDown, None)
    CanTiltUp = property(get_CanTiltUp, None)
    CanZoomIn = property(get_CanZoomIn, None)
    CanZoomOut = property(get_CanZoomOut, None)
    Center = property(get_Center, put_Center)
    Children = property(get_Children, None)
    ColorScheme = property(get_ColorScheme, put_ColorScheme)
    CustomExperience = property(get_CustomExperience, put_CustomExperience)
    DesiredPitch = property(get_DesiredPitch, put_DesiredPitch)
    Heading = property(get_Heading, put_Heading)
    Is3DSupported = property(get_Is3DSupported, None)
    IsStreetsideSupported = property(get_IsStreetsideSupported, None)
    LandmarksVisible = property(get_LandmarksVisible, put_LandmarksVisible)
    Layers = property(get_Layers, put_Layers)
    LoadingStatus = property(get_LoadingStatus, None)
    MapElements = property(get_MapElements, None)
    MapProjection = property(get_MapProjection, put_MapProjection)
    MapServiceToken = property(get_MapServiceToken, put_MapServiceToken)
    MaxZoomLevel = property(get_MaxZoomLevel, None)
    MinZoomLevel = property(get_MinZoomLevel, None)
    PanInteractionMode = property(get_PanInteractionMode, put_PanInteractionMode)
    PedestrianFeaturesVisible = property(get_PedestrianFeaturesVisible, put_PedestrianFeaturesVisible)
    Pitch = property(get_Pitch, None)
    Region = property(get_Region, put_Region)
    RotateInteractionMode = property(get_RotateInteractionMode, put_RotateInteractionMode)
    Routes = property(get_Routes, None)
    Scene = property(get_Scene, put_Scene)
    Style = property(get_Style, put_Style)
    StyleSheet = property(get_StyleSheet, put_StyleSheet)
    TargetCamera = property(get_TargetCamera, None)
    TileSources = property(get_TileSources, None)
    TiltInteractionMode = property(get_TiltInteractionMode, put_TiltInteractionMode)
    TrafficFlowVisible = property(get_TrafficFlowVisible, put_TrafficFlowVisible)
    TransformOrigin = property(get_TransformOrigin, put_TransformOrigin)
    TransitFeaturesEnabled = property(get_TransitFeaturesEnabled, put_TransitFeaturesEnabled)
    TransitFeaturesVisible = property(get_TransitFeaturesVisible, put_TransitFeaturesVisible)
    ViewPadding = property(get_ViewPadding, put_ViewPadding)
    WatermarkMode = property(get_WatermarkMode, put_WatermarkMode)
    ZoomInteractionMode = property(get_ZoomInteractionMode, put_ZoomInteractionMode)
    ZoomLevel = property(get_ZoomLevel, put_ZoomLevel)
    _MapControl_Meta_.BusinessLandmarksEnabledProperty = property(get_BusinessLandmarksEnabledProperty, None)
    _MapControl_Meta_.BusinessLandmarksVisibleProperty = property(get_BusinessLandmarksVisibleProperty, None)
    _MapControl_Meta_.CanTiltDownProperty = property(get_CanTiltDownProperty, None)
    _MapControl_Meta_.CanTiltUpProperty = property(get_CanTiltUpProperty, None)
    _MapControl_Meta_.CanZoomInProperty = property(get_CanZoomInProperty, None)
    _MapControl_Meta_.CanZoomOutProperty = property(get_CanZoomOutProperty, None)
    _MapControl_Meta_.CenterProperty = property(get_CenterProperty, None)
    _MapControl_Meta_.ChildrenProperty = property(get_ChildrenProperty, None)
    _MapControl_Meta_.ColorSchemeProperty = property(get_ColorSchemeProperty, None)
    _MapControl_Meta_.DesiredPitchProperty = property(get_DesiredPitchProperty, None)
    _MapControl_Meta_.HeadingProperty = property(get_HeadingProperty, None)
    _MapControl_Meta_.Is3DSupportedProperty = property(get_Is3DSupportedProperty, None)
    _MapControl_Meta_.IsStreetsideSupportedProperty = property(get_IsStreetsideSupportedProperty, None)
    _MapControl_Meta_.LandmarksVisibleProperty = property(get_LandmarksVisibleProperty, None)
    _MapControl_Meta_.LayersProperty = property(get_LayersProperty, None)
    _MapControl_Meta_.LoadingStatusProperty = property(get_LoadingStatusProperty, None)
    _MapControl_Meta_.LocationProperty = property(get_LocationProperty, None)
    _MapControl_Meta_.MapElementsProperty = property(get_MapElementsProperty, None)
    _MapControl_Meta_.MapProjectionProperty = property(get_MapProjectionProperty, None)
    _MapControl_Meta_.MapServiceTokenProperty = property(get_MapServiceTokenProperty, None)
    _MapControl_Meta_.NormalizedAnchorPointProperty = property(get_NormalizedAnchorPointProperty, None)
    _MapControl_Meta_.PanInteractionModeProperty = property(get_PanInteractionModeProperty, None)
    _MapControl_Meta_.PedestrianFeaturesVisibleProperty = property(get_PedestrianFeaturesVisibleProperty, None)
    _MapControl_Meta_.PitchProperty = property(get_PitchProperty, None)
    _MapControl_Meta_.RegionProperty = property(get_RegionProperty, None)
    _MapControl_Meta_.RotateInteractionModeProperty = property(get_RotateInteractionModeProperty, None)
    _MapControl_Meta_.RoutesProperty = property(get_RoutesProperty, None)
    _MapControl_Meta_.SceneProperty = property(get_SceneProperty, None)
    _MapControl_Meta_.StyleProperty = property(get_StyleProperty, None)
    _MapControl_Meta_.StyleSheetProperty = property(get_StyleSheetProperty, None)
    _MapControl_Meta_.TileSourcesProperty = property(get_TileSourcesProperty, None)
    _MapControl_Meta_.TiltInteractionModeProperty = property(get_TiltInteractionModeProperty, None)
    _MapControl_Meta_.TrafficFlowVisibleProperty = property(get_TrafficFlowVisibleProperty, None)
    _MapControl_Meta_.TransformOriginProperty = property(get_TransformOriginProperty, None)
    _MapControl_Meta_.TransitFeaturesEnabledProperty = property(get_TransitFeaturesEnabledProperty, None)
    _MapControl_Meta_.TransitFeaturesVisibleProperty = property(get_TransitFeaturesVisibleProperty, None)
    _MapControl_Meta_.ViewPaddingProperty = property(get_ViewPaddingProperty, None)
    _MapControl_Meta_.WatermarkModeProperty = property(get_WatermarkModeProperty, None)
    _MapControl_Meta_.ZoomInteractionModeProperty = property(get_ZoomInteractionModeProperty, None)
    _MapControl_Meta_.ZoomLevelProperty = property(get_ZoomLevelProperty, None)
    CenterChanged = event()
    HeadingChanged = event()
    LoadingStatusChanged = event()
    MapDoubleTapped = event()
    MapHolding = event()
    MapTapped = event()
    PitchChanged = event()
    TransformOriginChanged = event()
    ZoomLevelChanged = event()
    MapElementClick = event()
    MapElementPointerEntered = event()
    MapElementPointerExited = event()
    ActualCameraChanged = event()
    ActualCameraChanging = event()
    TargetCameraChanged = event()
    CustomExperienceChanged = event()
    MapRightTapped = event()
    MapContextRequested = event()
class MapControlBusinessLandmarkClickEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlBusinessLandmarkClickEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapControlBusinessLandmarkClickEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapControlBusinessLandmarkClickEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Controls.Maps.MapControlBusinessLandmarkClickEventArgs: ...
    @winrt_mixinmethod
    def get_LocalLocations(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlBusinessLandmarkClickEventArgs) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Maps.LocalSearch.LocalLocation]: ...
    LocalLocations = property(get_LocalLocations, None)
class MapControlBusinessLandmarkPointerEnteredEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlBusinessLandmarkPointerEnteredEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapControlBusinessLandmarkPointerEnteredEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapControlBusinessLandmarkPointerEnteredEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Controls.Maps.MapControlBusinessLandmarkPointerEnteredEventArgs: ...
    @winrt_mixinmethod
    def get_LocalLocations(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlBusinessLandmarkPointerEnteredEventArgs) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Maps.LocalSearch.LocalLocation]: ...
    LocalLocations = property(get_LocalLocations, None)
class MapControlBusinessLandmarkPointerExitedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlBusinessLandmarkPointerExitedEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapControlBusinessLandmarkPointerExitedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapControlBusinessLandmarkPointerExitedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Controls.Maps.MapControlBusinessLandmarkPointerExitedEventArgs: ...
    @winrt_mixinmethod
    def get_LocalLocations(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlBusinessLandmarkPointerExitedEventArgs) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Maps.LocalSearch.LocalLocation]: ...
    LocalLocations = property(get_LocalLocations, None)
class MapControlBusinessLandmarkRightTappedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlBusinessLandmarkRightTappedEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapControlBusinessLandmarkRightTappedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapControlBusinessLandmarkRightTappedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Controls.Maps.MapControlBusinessLandmarkRightTappedEventArgs: ...
    @winrt_mixinmethod
    def get_LocalLocations(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlBusinessLandmarkRightTappedEventArgs) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Maps.LocalSearch.LocalLocation]: ...
    LocalLocations = property(get_LocalLocations, None)
class MapControlDataHelper(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlDataHelper
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapControlDataHelper'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapControlDataHelper.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlDataHelperFactory, map: win32more.Windows.UI.Xaml.Controls.Maps.MapControl) -> win32more.Windows.UI.Xaml.Controls.Maps.MapControlDataHelper: ...
    @winrt_mixinmethod
    def add_BusinessLandmarkClick(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlDataHelper, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.UI.Xaml.Controls.Maps.MapControlBusinessLandmarkClickEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_BusinessLandmarkClick(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlDataHelper, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_TransitFeatureClick(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlDataHelper, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.UI.Xaml.Controls.Maps.MapControlTransitFeatureClickEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TransitFeatureClick(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlDataHelper, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_BusinessLandmarkRightTapped(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlDataHelper, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.UI.Xaml.Controls.Maps.MapControlBusinessLandmarkRightTappedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_BusinessLandmarkRightTapped(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlDataHelper, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_TransitFeatureRightTapped(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlDataHelper, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.UI.Xaml.Controls.Maps.MapControlTransitFeatureRightTappedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TransitFeatureRightTapped(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlDataHelper, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_BusinessLandmarkPointerEntered(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlDataHelper2, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.UI.Xaml.Controls.Maps.MapControlBusinessLandmarkPointerEnteredEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_BusinessLandmarkPointerEntered(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlDataHelper2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_TransitFeaturePointerEntered(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlDataHelper2, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.UI.Xaml.Controls.Maps.MapControlTransitFeaturePointerEnteredEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TransitFeaturePointerEntered(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlDataHelper2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_BusinessLandmarkPointerExited(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlDataHelper2, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.UI.Xaml.Controls.Maps.MapControlBusinessLandmarkPointerExitedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_BusinessLandmarkPointerExited(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlDataHelper2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_TransitFeaturePointerExited(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlDataHelper2, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapControl, win32more.Windows.UI.Xaml.Controls.Maps.MapControlTransitFeaturePointerExitedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TransitFeaturePointerExited(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlDataHelper2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def CreateMapControl(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlDataHelperStatics, rasterRenderMode: Boolean) -> win32more.Windows.UI.Xaml.Controls.Maps.MapControl: ...
    BusinessLandmarkClick = event()
    TransitFeatureClick = event()
    BusinessLandmarkRightTapped = event()
    TransitFeatureRightTapped = event()
    BusinessLandmarkPointerEntered = event()
    TransitFeaturePointerEntered = event()
    BusinessLandmarkPointerExited = event()
    TransitFeaturePointerExited = event()
class MapControlTransitFeatureClickEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlTransitFeatureClickEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapControlTransitFeatureClickEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapControlTransitFeatureClickEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Controls.Maps.MapControlTransitFeatureClickEventArgs: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlTransitFeatureClickEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Location(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlTransitFeatureClickEventArgs) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def get_TransitProperties(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlTransitFeatureClickEventArgs) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    DisplayName = property(get_DisplayName, None)
    Location = property(get_Location, None)
    TransitProperties = property(get_TransitProperties, None)
class MapControlTransitFeaturePointerEnteredEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlTransitFeaturePointerEnteredEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapControlTransitFeaturePointerEnteredEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapControlTransitFeaturePointerEnteredEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Controls.Maps.MapControlTransitFeaturePointerEnteredEventArgs: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlTransitFeaturePointerEnteredEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Location(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlTransitFeaturePointerEnteredEventArgs) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def get_TransitProperties(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlTransitFeaturePointerEnteredEventArgs) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    DisplayName = property(get_DisplayName, None)
    Location = property(get_Location, None)
    TransitProperties = property(get_TransitProperties, None)
class MapControlTransitFeaturePointerExitedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlTransitFeaturePointerExitedEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapControlTransitFeaturePointerExitedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapControlTransitFeaturePointerExitedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Controls.Maps.MapControlTransitFeaturePointerExitedEventArgs: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlTransitFeaturePointerExitedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Location(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlTransitFeaturePointerExitedEventArgs) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def get_TransitProperties(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlTransitFeaturePointerExitedEventArgs) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    DisplayName = property(get_DisplayName, None)
    Location = property(get_Location, None)
    TransitProperties = property(get_TransitProperties, None)
class MapControlTransitFeatureRightTappedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlTransitFeatureRightTappedEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapControlTransitFeatureRightTappedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapControlTransitFeatureRightTappedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Controls.Maps.MapControlTransitFeatureRightTappedEventArgs: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlTransitFeatureRightTappedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Location(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlTransitFeatureRightTappedEventArgs) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def get_TransitProperties(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapControlTransitFeatureRightTappedEventArgs) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    DisplayName = property(get_DisplayName, None)
    Location = property(get_Location, None)
    TransitProperties = property(get_TransitProperties, None)
class MapCustomExperience(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IMapCustomExperience
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapCustomExperience'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapCustomExperience.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapCustomExperienceFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Maps.MapCustomExperience: ...
class MapCustomExperienceChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IMapCustomExperienceChangedEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapCustomExperienceChangedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapCustomExperienceChangedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Controls.Maps.MapCustomExperienceChangedEventArgs: ...
class _MapElement_Meta_(ComPtr.__class__):
    pass
class MapElement(ComPtr, metaclass=_MapElement_Meta_):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IMapElement
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapElement'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapElement.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Maps.MapElement: ...
    @winrt_mixinmethod
    def get_ZIndex(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElement) -> Int32: ...
    @winrt_mixinmethod
    def put_ZIndex(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElement, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_Visible(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElement) -> Boolean: ...
    @winrt_mixinmethod
    def put_Visible(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElement, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_MapTabIndex(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElement2) -> Int32: ...
    @winrt_mixinmethod
    def put_MapTabIndex(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElement2, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_MapStyleSheetEntry(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElement3) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_MapStyleSheetEntry(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElement3, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_MapStyleSheetEntryState(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElement3) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_MapStyleSheetEntryState(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElement3, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Tag(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElement3) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def put_Tag(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElement3, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def get_IsEnabled(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElement4) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsEnabled(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElement4, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_IsEnabledProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementStatics4) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_MapStyleSheetEntryProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementStatics3) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_MapStyleSheetEntryStateProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementStatics3) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TagProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementStatics3) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_MapTabIndexProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementStatics2) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ZIndexProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_VisibleProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    MapStyleSheetEntry = property(get_MapStyleSheetEntry, put_MapStyleSheetEntry)
    MapStyleSheetEntryState = property(get_MapStyleSheetEntryState, put_MapStyleSheetEntryState)
    MapTabIndex = property(get_MapTabIndex, put_MapTabIndex)
    Tag = property(get_Tag, put_Tag)
    Visible = property(get_Visible, put_Visible)
    ZIndex = property(get_ZIndex, put_ZIndex)
    _MapElement_Meta_.IsEnabledProperty = property(get_IsEnabledProperty, None)
    _MapElement_Meta_.MapStyleSheetEntryProperty = property(get_MapStyleSheetEntryProperty, None)
    _MapElement_Meta_.MapStyleSheetEntryStateProperty = property(get_MapStyleSheetEntryStateProperty, None)
    _MapElement_Meta_.MapTabIndexProperty = property(get_MapTabIndexProperty, None)
    _MapElement_Meta_.TagProperty = property(get_TagProperty, None)
    _MapElement_Meta_.VisibleProperty = property(get_VisibleProperty, None)
    _MapElement_Meta_.ZIndexProperty = property(get_ZIndexProperty, None)
class _MapElement3D_Meta_(ComPtr.__class__):
    pass
class MapElement3D(ComPtr, metaclass=_MapElement3D_Meta_):
    extends: win32more.Windows.UI.Xaml.Controls.Maps.MapElement
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IMapElement3D
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapElement3D'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapElement3D.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Controls.Maps.MapElement3D: ...
    @winrt_mixinmethod
    def get_Location(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElement3D) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def put_Location(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElement3D, value: win32more.Windows.Devices.Geolocation.Geopoint) -> Void: ...
    @winrt_mixinmethod
    def get_Model(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElement3D) -> win32more.Windows.UI.Xaml.Controls.Maps.MapModel3D: ...
    @winrt_mixinmethod
    def put_Model(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElement3D, value: win32more.Windows.UI.Xaml.Controls.Maps.MapModel3D) -> Void: ...
    @winrt_mixinmethod
    def get_Heading(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElement3D) -> Double: ...
    @winrt_mixinmethod
    def put_Heading(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElement3D, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Pitch(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElement3D) -> Double: ...
    @winrt_mixinmethod
    def put_Pitch(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElement3D, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Roll(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElement3D) -> Double: ...
    @winrt_mixinmethod
    def put_Roll(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElement3D, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Scale(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElement3D) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_Scale(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElement3D, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_classmethod
    def get_LocationProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapElement3DStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_HeadingProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapElement3DStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_PitchProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapElement3DStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RollProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapElement3DStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ScaleProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapElement3DStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    Heading = property(get_Heading, put_Heading)
    Location = property(get_Location, put_Location)
    Model = property(get_Model, put_Model)
    Pitch = property(get_Pitch, put_Pitch)
    Roll = property(get_Roll, put_Roll)
    Scale = property(get_Scale, put_Scale)
    _MapElement3D_Meta_.HeadingProperty = property(get_HeadingProperty, None)
    _MapElement3D_Meta_.LocationProperty = property(get_LocationProperty, None)
    _MapElement3D_Meta_.PitchProperty = property(get_PitchProperty, None)
    _MapElement3D_Meta_.RollProperty = property(get_RollProperty, None)
    _MapElement3D_Meta_.ScaleProperty = property(get_ScaleProperty, None)
class MapElementClickEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementClickEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapElementClickEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapElementClickEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Controls.Maps.MapElementClickEventArgs: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementClickEventArgs) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Location(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementClickEventArgs) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def get_MapElements(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementClickEventArgs) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Controls.Maps.MapElement]: ...
    Location = property(get_Location, None)
    MapElements = property(get_MapElements, None)
    Position = property(get_Position, None)
class MapElementCollisionBehavior(Enum, Int32):
    Hide = 0
    RemainVisible = 1
class MapElementPointerEnteredEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementPointerEnteredEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapElementPointerEnteredEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapElementPointerEnteredEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Controls.Maps.MapElementPointerEnteredEventArgs: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementPointerEnteredEventArgs) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Location(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementPointerEnteredEventArgs) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def get_MapElement(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementPointerEnteredEventArgs) -> win32more.Windows.UI.Xaml.Controls.Maps.MapElement: ...
    Location = property(get_Location, None)
    MapElement = property(get_MapElement, None)
    Position = property(get_Position, None)
class MapElementPointerExitedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementPointerExitedEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapElementPointerExitedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapElementPointerExitedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Controls.Maps.MapElementPointerExitedEventArgs: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementPointerExitedEventArgs) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Location(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementPointerExitedEventArgs) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def get_MapElement(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementPointerExitedEventArgs) -> win32more.Windows.UI.Xaml.Controls.Maps.MapElement: ...
    Location = property(get_Location, None)
    MapElement = property(get_MapElement, None)
    Position = property(get_Position, None)
class _MapElementsLayer_Meta_(ComPtr.__class__):
    pass
class MapElementsLayer(ComPtr, metaclass=_MapElementsLayer_Meta_):
    extends: win32more.Windows.UI.Xaml.Controls.Maps.MapLayer
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementsLayer
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapElementsLayer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapElementsLayer.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Controls.Maps.MapElementsLayer: ...
    @winrt_mixinmethod
    def get_MapElements(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementsLayer) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Controls.Maps.MapElement]: ...
    @winrt_mixinmethod
    def put_MapElements(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementsLayer, value: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Controls.Maps.MapElement]) -> Void: ...
    @winrt_mixinmethod
    def add_MapElementClick(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementsLayer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapElementsLayer, win32more.Windows.UI.Xaml.Controls.Maps.MapElementsLayerClickEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MapElementClick(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementsLayer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_MapElementPointerEntered(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementsLayer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapElementsLayer, win32more.Windows.UI.Xaml.Controls.Maps.MapElementsLayerPointerEnteredEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MapElementPointerEntered(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementsLayer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_MapElementPointerExited(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementsLayer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapElementsLayer, win32more.Windows.UI.Xaml.Controls.Maps.MapElementsLayerPointerExitedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MapElementPointerExited(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementsLayer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_MapContextRequested(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementsLayer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapElementsLayer, win32more.Windows.UI.Xaml.Controls.Maps.MapElementsLayerContextRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MapContextRequested(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementsLayer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_MapElementsProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementsLayerStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    MapElements = property(get_MapElements, put_MapElements)
    _MapElementsLayer_Meta_.MapElementsProperty = property(get_MapElementsProperty, None)
    MapElementClick = event()
    MapElementPointerEntered = event()
    MapElementPointerExited = event()
    MapContextRequested = event()
class MapElementsLayerClickEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementsLayerClickEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapElementsLayerClickEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapElementsLayerClickEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Controls.Maps.MapElementsLayerClickEventArgs: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementsLayerClickEventArgs) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Location(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementsLayerClickEventArgs) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def get_MapElements(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementsLayerClickEventArgs) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Controls.Maps.MapElement]: ...
    Location = property(get_Location, None)
    MapElements = property(get_MapElements, None)
    Position = property(get_Position, None)
class MapElementsLayerContextRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementsLayerContextRequestedEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapElementsLayerContextRequestedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapElementsLayerContextRequestedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Controls.Maps.MapElementsLayerContextRequestedEventArgs: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementsLayerContextRequestedEventArgs) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Location(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementsLayerContextRequestedEventArgs) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def get_MapElements(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementsLayerContextRequestedEventArgs) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Xaml.Controls.Maps.MapElement]: ...
    Location = property(get_Location, None)
    MapElements = property(get_MapElements, None)
    Position = property(get_Position, None)
class MapElementsLayerPointerEnteredEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementsLayerPointerEnteredEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapElementsLayerPointerEnteredEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapElementsLayerPointerEnteredEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Controls.Maps.MapElementsLayerPointerEnteredEventArgs: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementsLayerPointerEnteredEventArgs) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Location(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementsLayerPointerEnteredEventArgs) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def get_MapElement(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementsLayerPointerEnteredEventArgs) -> win32more.Windows.UI.Xaml.Controls.Maps.MapElement: ...
    Location = property(get_Location, None)
    MapElement = property(get_MapElement, None)
    Position = property(get_Position, None)
class MapElementsLayerPointerExitedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementsLayerPointerExitedEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapElementsLayerPointerExitedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapElementsLayerPointerExitedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Controls.Maps.MapElementsLayerPointerExitedEventArgs: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementsLayerPointerExitedEventArgs) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Location(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementsLayerPointerExitedEventArgs) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def get_MapElement(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapElementsLayerPointerExitedEventArgs) -> win32more.Windows.UI.Xaml.Controls.Maps.MapElement: ...
    Location = property(get_Location, None)
    MapElement = property(get_MapElement, None)
    Position = property(get_Position, None)
class _MapIcon_Meta_(ComPtr.__class__):
    pass
class MapIcon(ComPtr, metaclass=_MapIcon_Meta_):
    extends: win32more.Windows.UI.Xaml.Controls.Maps.MapElement
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IMapIcon
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapIcon'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapIcon.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Controls.Maps.MapIcon: ...
    @winrt_mixinmethod
    def get_Location(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapIcon) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def put_Location(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapIcon, value: win32more.Windows.Devices.Geolocation.Geopoint) -> Void: ...
    @winrt_mixinmethod
    def get_Title(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapIcon) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Title(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapIcon, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_NormalizedAnchorPoint(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapIcon) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_NormalizedAnchorPoint(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapIcon, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_Image(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapIcon) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def put_Image(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapIcon, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_mixinmethod
    def get_CollisionBehaviorDesired(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapIcon2) -> win32more.Windows.UI.Xaml.Controls.Maps.MapElementCollisionBehavior: ...
    @winrt_mixinmethod
    def put_CollisionBehaviorDesired(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapIcon2, value: win32more.Windows.UI.Xaml.Controls.Maps.MapElementCollisionBehavior) -> Void: ...
    @winrt_classmethod
    def get_CollisionBehaviorDesiredProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapIconStatics2) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_LocationProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapIconStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TitleProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapIconStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_NormalizedAnchorPointProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapIconStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    CollisionBehaviorDesired = property(get_CollisionBehaviorDesired, put_CollisionBehaviorDesired)
    Image = property(get_Image, put_Image)
    Location = property(get_Location, put_Location)
    NormalizedAnchorPoint = property(get_NormalizedAnchorPoint, put_NormalizedAnchorPoint)
    Title = property(get_Title, put_Title)
    _MapIcon_Meta_.CollisionBehaviorDesiredProperty = property(get_CollisionBehaviorDesiredProperty, None)
    _MapIcon_Meta_.LocationProperty = property(get_LocationProperty, None)
    _MapIcon_Meta_.NormalizedAnchorPointProperty = property(get_NormalizedAnchorPointProperty, None)
    _MapIcon_Meta_.TitleProperty = property(get_TitleProperty, None)
class MapInputEventArgs(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IMapInputEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapInputEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapInputEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Controls.Maps.MapInputEventArgs: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapInputEventArgs) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Location(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapInputEventArgs) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    Location = property(get_Location, None)
    Position = property(get_Position, None)
class MapInteractionMode(Enum, Int32):
    Auto = 0
    Disabled = 1
    GestureOnly = 2
    PointerAndKeyboard = 2
    ControlOnly = 3
    GestureAndControl = 4
    PointerKeyboardAndControl = 4
    PointerOnly = 5
class _MapItemsControl_Meta_(ComPtr.__class__):
    pass
class MapItemsControl(ComPtr, metaclass=_MapItemsControl_Meta_):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IMapItemsControl
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapItemsControl'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapItemsControl.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Controls.Maps.MapItemsControl: ...
    @winrt_mixinmethod
    def get_ItemsSource(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapItemsControl) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def put_ItemsSource(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapItemsControl, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def get_Items(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapItemsControl) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.DependencyObject]: ...
    @winrt_mixinmethod
    def get_ItemTemplate(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapItemsControl) -> win32more.Windows.UI.Xaml.DataTemplate: ...
    @winrt_mixinmethod
    def put_ItemTemplate(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapItemsControl, value: win32more.Windows.UI.Xaml.DataTemplate) -> Void: ...
    @winrt_classmethod
    def get_ItemsSourceProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapItemsControlStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ItemsProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapItemsControlStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ItemTemplateProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapItemsControlStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    ItemTemplate = property(get_ItemTemplate, put_ItemTemplate)
    Items = property(get_Items, None)
    ItemsSource = property(get_ItemsSource, put_ItemsSource)
    _MapItemsControl_Meta_.ItemTemplateProperty = property(get_ItemTemplateProperty, None)
    _MapItemsControl_Meta_.ItemsProperty = property(get_ItemsProperty, None)
    _MapItemsControl_Meta_.ItemsSourceProperty = property(get_ItemsSourceProperty, None)
class _MapLayer_Meta_(ComPtr.__class__):
    pass
class MapLayer(ComPtr, metaclass=_MapLayer_Meta_):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IMapLayer
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapLayer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapLayer.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapLayerFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Maps.MapLayer: ...
    @winrt_mixinmethod
    def get_MapTabIndex(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapLayer) -> Int32: ...
    @winrt_mixinmethod
    def put_MapTabIndex(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapLayer, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_Visible(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapLayer) -> Boolean: ...
    @winrt_mixinmethod
    def put_Visible(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapLayer, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ZIndex(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapLayer) -> Int32: ...
    @winrt_mixinmethod
    def put_ZIndex(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapLayer, value: Int32) -> Void: ...
    @winrt_classmethod
    def get_MapTabIndexProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapLayerStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_VisibleProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapLayerStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ZIndexProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapLayerStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    MapTabIndex = property(get_MapTabIndex, put_MapTabIndex)
    Visible = property(get_Visible, put_Visible)
    ZIndex = property(get_ZIndex, put_ZIndex)
    _MapLayer_Meta_.MapTabIndexProperty = property(get_MapTabIndexProperty, None)
    _MapLayer_Meta_.VisibleProperty = property(get_VisibleProperty, None)
    _MapLayer_Meta_.ZIndexProperty = property(get_ZIndexProperty, None)
class MapLoadingStatus(Enum, Int32):
    Loading = 0
    Loaded = 1
    DataUnavailable = 2
    DownloadedMapsManagerUnavailable = 3
class MapModel3D(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IMapModel3D
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapModel3D'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapModel3D.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapModel3DFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Maps.MapModel3D: ...
    @winrt_classmethod
    def CreateFrom3MFAsync(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapModel3DStatics, source: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.Xaml.Controls.Maps.MapModel3D]: ...
    @winrt_classmethod
    def CreateFrom3MFWithShadingOptionAsync(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapModel3DStatics, source: win32more.Windows.Storage.Streams.IRandomAccessStreamReference, shadingOption: win32more.Windows.UI.Xaml.Controls.Maps.MapModel3DShadingOption) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.Xaml.Controls.Maps.MapModel3D]: ...
class MapModel3DShadingOption(Enum, Int32):
    Default = 0
    Flat = 1
    Smooth = 2
class MapPanInteractionMode(Enum, Int32):
    Auto = 0
    Disabled = 1
class _MapPolygon_Meta_(ComPtr.__class__):
    pass
class MapPolygon(ComPtr, metaclass=_MapPolygon_Meta_):
    extends: win32more.Windows.UI.Xaml.Controls.Maps.MapElement
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IMapPolygon
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapPolygon'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapPolygon.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Controls.Maps.MapPolygon: ...
    @winrt_mixinmethod
    def get_Path(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapPolygon) -> win32more.Windows.Devices.Geolocation.Geopath: ...
    @winrt_mixinmethod
    def put_Path(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapPolygon, value: win32more.Windows.Devices.Geolocation.Geopath) -> Void: ...
    @winrt_mixinmethod
    def get_StrokeColor(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapPolygon) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_StrokeColor(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapPolygon, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_StrokeThickness(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapPolygon) -> Double: ...
    @winrt_mixinmethod
    def put_StrokeThickness(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapPolygon, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_StrokeDashed(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapPolygon) -> Boolean: ...
    @winrt_mixinmethod
    def put_StrokeDashed(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapPolygon, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_FillColor(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapPolygon) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_FillColor(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapPolygon, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_Paths(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapPolygon2) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Devices.Geolocation.Geopath]: ...
    @winrt_classmethod
    def get_PathProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapPolygonStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StrokeThicknessProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapPolygonStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StrokeDashedProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapPolygonStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    FillColor = property(get_FillColor, put_FillColor)
    Path = property(get_Path, put_Path)
    Paths = property(get_Paths, None)
    StrokeColor = property(get_StrokeColor, put_StrokeColor)
    StrokeDashed = property(get_StrokeDashed, put_StrokeDashed)
    StrokeThickness = property(get_StrokeThickness, put_StrokeThickness)
    _MapPolygon_Meta_.PathProperty = property(get_PathProperty, None)
    _MapPolygon_Meta_.StrokeDashedProperty = property(get_StrokeDashedProperty, None)
    _MapPolygon_Meta_.StrokeThicknessProperty = property(get_StrokeThicknessProperty, None)
class _MapPolyline_Meta_(ComPtr.__class__):
    pass
class MapPolyline(ComPtr, metaclass=_MapPolyline_Meta_):
    extends: win32more.Windows.UI.Xaml.Controls.Maps.MapElement
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IMapPolyline
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapPolyline'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapPolyline.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Controls.Maps.MapPolyline: ...
    @winrt_mixinmethod
    def get_Path(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapPolyline) -> win32more.Windows.Devices.Geolocation.Geopath: ...
    @winrt_mixinmethod
    def put_Path(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapPolyline, value: win32more.Windows.Devices.Geolocation.Geopath) -> Void: ...
    @winrt_mixinmethod
    def get_StrokeColor(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapPolyline) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_StrokeColor(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapPolyline, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_StrokeThickness(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapPolyline) -> Double: ...
    @winrt_mixinmethod
    def put_StrokeThickness(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapPolyline, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_StrokeDashed(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapPolyline) -> Boolean: ...
    @winrt_mixinmethod
    def put_StrokeDashed(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapPolyline, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_PathProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapPolylineStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StrokeDashedProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapPolylineStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    Path = property(get_Path, put_Path)
    StrokeColor = property(get_StrokeColor, put_StrokeColor)
    StrokeDashed = property(get_StrokeDashed, put_StrokeDashed)
    StrokeThickness = property(get_StrokeThickness, put_StrokeThickness)
    _MapPolyline_Meta_.PathProperty = property(get_PathProperty, None)
    _MapPolyline_Meta_.StrokeDashedProperty = property(get_StrokeDashedProperty, None)
class MapProjection(Enum, Int32):
    WebMercator = 0
    Globe = 1
class MapRightTappedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IMapRightTappedEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapRightTappedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapRightTappedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Controls.Maps.MapRightTappedEventArgs: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapRightTappedEventArgs) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Location(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapRightTappedEventArgs) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    Location = property(get_Location, None)
    Position = property(get_Position, None)
class MapRouteView(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IMapRouteView
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapRouteView'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapRouteView.CreateInstanceWithMapRoute(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithMapRoute(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapRouteViewFactory, route: win32more.Windows.Services.Maps.MapRoute, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Maps.MapRouteView: ...
    @winrt_mixinmethod
    def get_RouteColor(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapRouteView) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_RouteColor(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapRouteView, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_OutlineColor(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapRouteView) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_OutlineColor(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapRouteView, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_Route(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapRouteView) -> win32more.Windows.Services.Maps.MapRoute: ...
    OutlineColor = property(get_OutlineColor, put_OutlineColor)
    Route = property(get_Route, None)
    RouteColor = property(get_RouteColor, put_RouteColor)
class MapScene(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IMapScene
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapScene'
    @winrt_mixinmethod
    def get_TargetCamera(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapScene) -> win32more.Windows.UI.Xaml.Controls.Maps.MapCamera: ...
    @winrt_mixinmethod
    def add_TargetCameraChanged(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapScene, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Controls.Maps.MapScene, win32more.Windows.UI.Xaml.Controls.Maps.MapTargetCameraChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TargetCameraChanged(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapScene, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def CreateFromBoundingBox(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapSceneStatics, bounds: win32more.Windows.Devices.Geolocation.GeoboundingBox) -> win32more.Windows.UI.Xaml.Controls.Maps.MapScene: ...
    @winrt_classmethod
    def CreateFromBoundingBoxWithHeadingAndPitch(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapSceneStatics, bounds: win32more.Windows.Devices.Geolocation.GeoboundingBox, headingInDegrees: Double, pitchInDegrees: Double) -> win32more.Windows.UI.Xaml.Controls.Maps.MapScene: ...
    @winrt_classmethod
    def CreateFromCamera(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapSceneStatics, camera: win32more.Windows.UI.Xaml.Controls.Maps.MapCamera) -> win32more.Windows.UI.Xaml.Controls.Maps.MapScene: ...
    @winrt_classmethod
    def CreateFromLocation(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapSceneStatics, location: win32more.Windows.Devices.Geolocation.Geopoint) -> win32more.Windows.UI.Xaml.Controls.Maps.MapScene: ...
    @winrt_classmethod
    def CreateFromLocationWithHeadingAndPitch(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapSceneStatics, location: win32more.Windows.Devices.Geolocation.Geopoint, headingInDegrees: Double, pitchInDegrees: Double) -> win32more.Windows.UI.Xaml.Controls.Maps.MapScene: ...
    @winrt_classmethod
    def CreateFromLocationAndRadius(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapSceneStatics, location: win32more.Windows.Devices.Geolocation.Geopoint, radiusInMeters: Double) -> win32more.Windows.UI.Xaml.Controls.Maps.MapScene: ...
    @winrt_classmethod
    def CreateFromLocationAndRadiusWithHeadingAndPitch(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapSceneStatics, location: win32more.Windows.Devices.Geolocation.Geopoint, radiusInMeters: Double, headingInDegrees: Double, pitchInDegrees: Double) -> win32more.Windows.UI.Xaml.Controls.Maps.MapScene: ...
    @winrt_classmethod
    def CreateFromLocations(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapSceneStatics, locations: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Devices.Geolocation.Geopoint]) -> win32more.Windows.UI.Xaml.Controls.Maps.MapScene: ...
    @winrt_classmethod
    def CreateFromLocationsWithHeadingAndPitch(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapSceneStatics, locations: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Devices.Geolocation.Geopoint], headingInDegrees: Double, pitchInDegrees: Double) -> win32more.Windows.UI.Xaml.Controls.Maps.MapScene: ...
    TargetCamera = property(get_TargetCamera, None)
    TargetCameraChanged = event()
class MapStyle(Enum, Int32):
    None_ = 0
    Road = 1
    Aerial = 2
    AerialWithRoads = 3
    Terrain = 4
    Aerial3D = 5
    Aerial3DWithRoads = 6
    Custom = 7
class MapStyleSheet(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheet
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapStyleSheet'
    @winrt_classmethod
    def Aerial(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetStatics) -> win32more.Windows.UI.Xaml.Controls.Maps.MapStyleSheet: ...
    @winrt_classmethod
    def AerialWithOverlay(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetStatics) -> win32more.Windows.UI.Xaml.Controls.Maps.MapStyleSheet: ...
    @winrt_classmethod
    def RoadLight(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetStatics) -> win32more.Windows.UI.Xaml.Controls.Maps.MapStyleSheet: ...
    @winrt_classmethod
    def RoadDark(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetStatics) -> win32more.Windows.UI.Xaml.Controls.Maps.MapStyleSheet: ...
    @winrt_classmethod
    def RoadHighContrastLight(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetStatics) -> win32more.Windows.UI.Xaml.Controls.Maps.MapStyleSheet: ...
    @winrt_classmethod
    def RoadHighContrastDark(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetStatics) -> win32more.Windows.UI.Xaml.Controls.Maps.MapStyleSheet: ...
    @winrt_classmethod
    def Combine(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetStatics, styleSheets: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Xaml.Controls.Maps.MapStyleSheet]) -> win32more.Windows.UI.Xaml.Controls.Maps.MapStyleSheet: ...
    @winrt_classmethod
    def ParseFromJson(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetStatics, styleAsJson: WinRT_String) -> win32more.Windows.UI.Xaml.Controls.Maps.MapStyleSheet: ...
    @winrt_classmethod
    def TryParseFromJson(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetStatics, styleAsJson: WinRT_String, styleSheet: POINTER(win32more.Windows.UI.Xaml.Controls.Maps.MapStyleSheet)) -> Boolean: ...
class _MapStyleSheetEntries_Meta_(ComPtr.__class__):
    pass
class MapStyleSheetEntries(ComPtr, metaclass=_MapStyleSheetEntries_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapStyleSheetEntries'
    @winrt_classmethod
    def get_Area(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Airport(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Cemetery(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Continent(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Education(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_IndigenousPeoplesReserve(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Island(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Medical(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Military(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Nautical(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Neighborhood(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Runway(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Sand(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_ShoppingCenter(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Stadium(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Vegetation(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Forest(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_GolfCourse(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Park(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_PlayingField(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Reserve(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Point(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_NaturalPoint(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Peak(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VolcanicPeak(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_WaterPoint(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_PointOfInterest(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Business(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_FoodPoint(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_PopulatedPlace(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Capital(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AdminDistrictCapital(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_CountryRegionCapital(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_RoadShield(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_RoadExit(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Transit(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Political(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_CountryRegion(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AdminDistrict(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_District(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Structure(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Building(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_EducationBuilding(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_MedicalBuilding(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_TransitBuilding(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Transportation(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Road(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_ControlledAccessHighway(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_HighSpeedRamp(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Highway(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_MajorRoad(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_ArterialRoad(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Street(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Ramp(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_UnpavedStreet(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_TollRoad(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Railway(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Trail(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_WaterRoute(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Water(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_River(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_RouteLine(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_WalkingRoute(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_DrivingRoute(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    _MapStyleSheetEntries_Meta_.AdminDistrict = property(get_AdminDistrict, None)
    _MapStyleSheetEntries_Meta_.AdminDistrictCapital = property(get_AdminDistrictCapital, None)
    _MapStyleSheetEntries_Meta_.Airport = property(get_Airport, None)
    _MapStyleSheetEntries_Meta_.Area = property(get_Area, None)
    _MapStyleSheetEntries_Meta_.ArterialRoad = property(get_ArterialRoad, None)
    _MapStyleSheetEntries_Meta_.Building = property(get_Building, None)
    _MapStyleSheetEntries_Meta_.Business = property(get_Business, None)
    _MapStyleSheetEntries_Meta_.Capital = property(get_Capital, None)
    _MapStyleSheetEntries_Meta_.Cemetery = property(get_Cemetery, None)
    _MapStyleSheetEntries_Meta_.Continent = property(get_Continent, None)
    _MapStyleSheetEntries_Meta_.ControlledAccessHighway = property(get_ControlledAccessHighway, None)
    _MapStyleSheetEntries_Meta_.CountryRegion = property(get_CountryRegion, None)
    _MapStyleSheetEntries_Meta_.CountryRegionCapital = property(get_CountryRegionCapital, None)
    _MapStyleSheetEntries_Meta_.District = property(get_District, None)
    _MapStyleSheetEntries_Meta_.DrivingRoute = property(get_DrivingRoute, None)
    _MapStyleSheetEntries_Meta_.Education = property(get_Education, None)
    _MapStyleSheetEntries_Meta_.EducationBuilding = property(get_EducationBuilding, None)
    _MapStyleSheetEntries_Meta_.FoodPoint = property(get_FoodPoint, None)
    _MapStyleSheetEntries_Meta_.Forest = property(get_Forest, None)
    _MapStyleSheetEntries_Meta_.GolfCourse = property(get_GolfCourse, None)
    _MapStyleSheetEntries_Meta_.HighSpeedRamp = property(get_HighSpeedRamp, None)
    _MapStyleSheetEntries_Meta_.Highway = property(get_Highway, None)
    _MapStyleSheetEntries_Meta_.IndigenousPeoplesReserve = property(get_IndigenousPeoplesReserve, None)
    _MapStyleSheetEntries_Meta_.Island = property(get_Island, None)
    _MapStyleSheetEntries_Meta_.MajorRoad = property(get_MajorRoad, None)
    _MapStyleSheetEntries_Meta_.Medical = property(get_Medical, None)
    _MapStyleSheetEntries_Meta_.MedicalBuilding = property(get_MedicalBuilding, None)
    _MapStyleSheetEntries_Meta_.Military = property(get_Military, None)
    _MapStyleSheetEntries_Meta_.NaturalPoint = property(get_NaturalPoint, None)
    _MapStyleSheetEntries_Meta_.Nautical = property(get_Nautical, None)
    _MapStyleSheetEntries_Meta_.Neighborhood = property(get_Neighborhood, None)
    _MapStyleSheetEntries_Meta_.Park = property(get_Park, None)
    _MapStyleSheetEntries_Meta_.Peak = property(get_Peak, None)
    _MapStyleSheetEntries_Meta_.PlayingField = property(get_PlayingField, None)
    _MapStyleSheetEntries_Meta_.Point = property(get_Point, None)
    _MapStyleSheetEntries_Meta_.PointOfInterest = property(get_PointOfInterest, None)
    _MapStyleSheetEntries_Meta_.Political = property(get_Political, None)
    _MapStyleSheetEntries_Meta_.PopulatedPlace = property(get_PopulatedPlace, None)
    _MapStyleSheetEntries_Meta_.Railway = property(get_Railway, None)
    _MapStyleSheetEntries_Meta_.Ramp = property(get_Ramp, None)
    _MapStyleSheetEntries_Meta_.Reserve = property(get_Reserve, None)
    _MapStyleSheetEntries_Meta_.River = property(get_River, None)
    _MapStyleSheetEntries_Meta_.Road = property(get_Road, None)
    _MapStyleSheetEntries_Meta_.RoadExit = property(get_RoadExit, None)
    _MapStyleSheetEntries_Meta_.RoadShield = property(get_RoadShield, None)
    _MapStyleSheetEntries_Meta_.RouteLine = property(get_RouteLine, None)
    _MapStyleSheetEntries_Meta_.Runway = property(get_Runway, None)
    _MapStyleSheetEntries_Meta_.Sand = property(get_Sand, None)
    _MapStyleSheetEntries_Meta_.ShoppingCenter = property(get_ShoppingCenter, None)
    _MapStyleSheetEntries_Meta_.Stadium = property(get_Stadium, None)
    _MapStyleSheetEntries_Meta_.Street = property(get_Street, None)
    _MapStyleSheetEntries_Meta_.Structure = property(get_Structure, None)
    _MapStyleSheetEntries_Meta_.TollRoad = property(get_TollRoad, None)
    _MapStyleSheetEntries_Meta_.Trail = property(get_Trail, None)
    _MapStyleSheetEntries_Meta_.Transit = property(get_Transit, None)
    _MapStyleSheetEntries_Meta_.TransitBuilding = property(get_TransitBuilding, None)
    _MapStyleSheetEntries_Meta_.Transportation = property(get_Transportation, None)
    _MapStyleSheetEntries_Meta_.UnpavedStreet = property(get_UnpavedStreet, None)
    _MapStyleSheetEntries_Meta_.Vegetation = property(get_Vegetation, None)
    _MapStyleSheetEntries_Meta_.VolcanicPeak = property(get_VolcanicPeak, None)
    _MapStyleSheetEntries_Meta_.WalkingRoute = property(get_WalkingRoute, None)
    _MapStyleSheetEntries_Meta_.Water = property(get_Water, None)
    _MapStyleSheetEntries_Meta_.WaterPoint = property(get_WaterPoint, None)
    _MapStyleSheetEntries_Meta_.WaterRoute = property(get_WaterRoute, None)
class _MapStyleSheetEntryStates_Meta_(ComPtr.__class__):
    pass
class MapStyleSheetEntryStates(ComPtr, metaclass=_MapStyleSheetEntryStates_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapStyleSheetEntryStates'
    @winrt_classmethod
    def get_Disabled(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntryStatesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Hover(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntryStatesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Selected(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntryStatesStatics) -> WinRT_String: ...
    _MapStyleSheetEntryStates_Meta_.Disabled = property(get_Disabled, None)
    _MapStyleSheetEntryStates_Meta_.Hover = property(get_Hover, None)
    _MapStyleSheetEntryStates_Meta_.Selected = property(get_Selected, None)
class MapTargetCameraChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IMapTargetCameraChangedEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapTargetCameraChangedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapTargetCameraChangedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Controls.Maps.MapTargetCameraChangedEventArgs: ...
    @winrt_mixinmethod
    def get_Camera(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTargetCameraChangedEventArgs) -> win32more.Windows.UI.Xaml.Controls.Maps.MapCamera: ...
    @winrt_mixinmethod
    def get_ChangeReason(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTargetCameraChangedEventArgs2) -> win32more.Windows.UI.Xaml.Controls.Maps.MapCameraChangeReason: ...
    Camera = property(get_Camera, None)
    ChangeReason = property(get_ChangeReason, None)
class MapTileAnimationState(Enum, Int32):
    Stopped = 0
    Paused = 1
    Playing = 2
class MapTileBitmapRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileBitmapRequest
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapTileBitmapRequest'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapTileBitmapRequest.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Controls.Maps.MapTileBitmapRequest: ...
    @winrt_mixinmethod
    def get_PixelData(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileBitmapRequest) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def put_PixelData(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileBitmapRequest, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileBitmapRequest) -> win32more.Windows.UI.Xaml.Controls.Maps.MapTileBitmapRequestDeferral: ...
    PixelData = property(get_PixelData, put_PixelData)
class MapTileBitmapRequestDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileBitmapRequestDeferral
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapTileBitmapRequestDeferral'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapTileBitmapRequestDeferral.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Controls.Maps.MapTileBitmapRequestDeferral: ...
    @winrt_mixinmethod
    def Complete(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileBitmapRequestDeferral) -> Void: ...
class MapTileBitmapRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileBitmapRequestedEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapTileBitmapRequestedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapTileBitmapRequestedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Controls.Maps.MapTileBitmapRequestedEventArgs: ...
    @winrt_mixinmethod
    def get_X(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileBitmapRequestedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_Y(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileBitmapRequestedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ZoomLevel(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileBitmapRequestedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileBitmapRequestedEventArgs) -> win32more.Windows.UI.Xaml.Controls.Maps.MapTileBitmapRequest: ...
    @winrt_mixinmethod
    def get_FrameIndex(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileBitmapRequestedEventArgs2) -> Int32: ...
    FrameIndex = property(get_FrameIndex, None)
    Request = property(get_Request, None)
    X = property(get_X, None)
    Y = property(get_Y, None)
    ZoomLevel = property(get_ZoomLevel, None)
class MapTileDataSource(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileDataSource
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapTileDataSource'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapTileDataSource.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileDataSourceFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Maps.MapTileDataSource: ...
class MapTileLayer(Enum, Int32):
    LabelOverlay = 0
    RoadOverlay = 1
    AreaOverlay = 2
    BackgroundOverlay = 3
    BackgroundReplacement = 4
class _MapTileSource_Meta_(ComPtr.__class__):
    pass
class MapTileSource(ComPtr, metaclass=_MapTileSource_Meta_):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSource
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapTileSource'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapTileSource.CreateInstance(*args, None, None))
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapTileSource.CreateInstanceWithDataSource(*args, None, None))
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapTileSource.CreateInstanceWithDataSourceAndZoomRange(*args, None, None))
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapTileSource.CreateInstanceWithDataSourceZoomRangeAndBounds(*args, None, None))
        elif len(args) == 4:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapTileSource.CreateInstanceWithDataSourceZoomRangeBoundsAndTileSize(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSourceFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Maps.MapTileSource: ...
    @winrt_factorymethod
    def CreateInstanceWithDataSource(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSourceFactory, dataSource: win32more.Windows.UI.Xaml.Controls.Maps.MapTileDataSource, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Maps.MapTileSource: ...
    @winrt_factorymethod
    def CreateInstanceWithDataSourceAndZoomRange(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSourceFactory, dataSource: win32more.Windows.UI.Xaml.Controls.Maps.MapTileDataSource, zoomLevelRange: win32more.Windows.UI.Xaml.Controls.Maps.MapZoomLevelRange, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Maps.MapTileSource: ...
    @winrt_factorymethod
    def CreateInstanceWithDataSourceZoomRangeAndBounds(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSourceFactory, dataSource: win32more.Windows.UI.Xaml.Controls.Maps.MapTileDataSource, zoomLevelRange: win32more.Windows.UI.Xaml.Controls.Maps.MapZoomLevelRange, bounds: win32more.Windows.Devices.Geolocation.GeoboundingBox, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Maps.MapTileSource: ...
    @winrt_factorymethod
    def CreateInstanceWithDataSourceZoomRangeBoundsAndTileSize(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSourceFactory, dataSource: win32more.Windows.UI.Xaml.Controls.Maps.MapTileDataSource, zoomLevelRange: win32more.Windows.UI.Xaml.Controls.Maps.MapZoomLevelRange, bounds: win32more.Windows.Devices.Geolocation.GeoboundingBox, tileSizeInPixels: Int32, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Controls.Maps.MapTileSource: ...
    @winrt_mixinmethod
    def get_DataSource(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSource) -> win32more.Windows.UI.Xaml.Controls.Maps.MapTileDataSource: ...
    @winrt_mixinmethod
    def put_DataSource(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSource, value: win32more.Windows.UI.Xaml.Controls.Maps.MapTileDataSource) -> Void: ...
    @winrt_mixinmethod
    def get_Layer(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSource) -> win32more.Windows.UI.Xaml.Controls.Maps.MapTileLayer: ...
    @winrt_mixinmethod
    def put_Layer(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSource, value: win32more.Windows.UI.Xaml.Controls.Maps.MapTileLayer) -> Void: ...
    @winrt_mixinmethod
    def get_ZoomLevelRange(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSource) -> win32more.Windows.UI.Xaml.Controls.Maps.MapZoomLevelRange: ...
    @winrt_mixinmethod
    def put_ZoomLevelRange(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSource, value: win32more.Windows.UI.Xaml.Controls.Maps.MapZoomLevelRange) -> Void: ...
    @winrt_mixinmethod
    def get_Bounds(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSource) -> win32more.Windows.Devices.Geolocation.GeoboundingBox: ...
    @winrt_mixinmethod
    def put_Bounds(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSource, value: win32more.Windows.Devices.Geolocation.GeoboundingBox) -> Void: ...
    @winrt_mixinmethod
    def get_AllowOverstretch(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSource) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowOverstretch(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSource, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsFadingEnabled(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSource) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsFadingEnabled(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSource, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsTransparencyEnabled(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSource) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsTransparencyEnabled(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSource, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsRetryEnabled(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSource) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsRetryEnabled(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSource, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ZIndex(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSource) -> Int32: ...
    @winrt_mixinmethod
    def put_ZIndex(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSource, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_TilePixelSize(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSource) -> Int32: ...
    @winrt_mixinmethod
    def put_TilePixelSize(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSource, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_Visible(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSource) -> Boolean: ...
    @winrt_mixinmethod
    def put_Visible(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSource, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AnimationState(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSource2) -> win32more.Windows.UI.Xaml.Controls.Maps.MapTileAnimationState: ...
    @winrt_mixinmethod
    def get_AutoPlay(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSource2) -> Boolean: ...
    @winrt_mixinmethod
    def put_AutoPlay(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSource2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_FrameCount(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSource2) -> Int32: ...
    @winrt_mixinmethod
    def put_FrameCount(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSource2, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_FrameDuration(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSource2) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_FrameDuration(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSource2, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def Pause(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSource2) -> Void: ...
    @winrt_mixinmethod
    def Play(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSource2) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSource2) -> Void: ...
    @winrt_classmethod
    def get_AnimationStateProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSourceStatics2) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_AutoPlayProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSourceStatics2) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FrameCountProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSourceStatics2) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FrameDurationProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSourceStatics2) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_DataSourceProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSourceStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_LayerProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSourceStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ZoomLevelRangeProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSourceStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_BoundsProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSourceStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_AllowOverstretchProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSourceStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsFadingEnabledProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSourceStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsTransparencyEnabledProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSourceStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsRetryEnabledProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSourceStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ZIndexProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSourceStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TilePixelSizeProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSourceStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_VisibleProperty(cls: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileSourceStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    AllowOverstretch = property(get_AllowOverstretch, put_AllowOverstretch)
    AnimationState = property(get_AnimationState, None)
    AutoPlay = property(get_AutoPlay, put_AutoPlay)
    Bounds = property(get_Bounds, put_Bounds)
    DataSource = property(get_DataSource, put_DataSource)
    FrameCount = property(get_FrameCount, put_FrameCount)
    FrameDuration = property(get_FrameDuration, put_FrameDuration)
    IsFadingEnabled = property(get_IsFadingEnabled, put_IsFadingEnabled)
    IsRetryEnabled = property(get_IsRetryEnabled, put_IsRetryEnabled)
    IsTransparencyEnabled = property(get_IsTransparencyEnabled, put_IsTransparencyEnabled)
    Layer = property(get_Layer, put_Layer)
    TilePixelSize = property(get_TilePixelSize, put_TilePixelSize)
    Visible = property(get_Visible, put_Visible)
    ZIndex = property(get_ZIndex, put_ZIndex)
    ZoomLevelRange = property(get_ZoomLevelRange, put_ZoomLevelRange)
    _MapTileSource_Meta_.AllowOverstretchProperty = property(get_AllowOverstretchProperty, None)
    _MapTileSource_Meta_.AnimationStateProperty = property(get_AnimationStateProperty, None)
    _MapTileSource_Meta_.AutoPlayProperty = property(get_AutoPlayProperty, None)
    _MapTileSource_Meta_.BoundsProperty = property(get_BoundsProperty, None)
    _MapTileSource_Meta_.DataSourceProperty = property(get_DataSourceProperty, None)
    _MapTileSource_Meta_.FrameCountProperty = property(get_FrameCountProperty, None)
    _MapTileSource_Meta_.FrameDurationProperty = property(get_FrameDurationProperty, None)
    _MapTileSource_Meta_.IsFadingEnabledProperty = property(get_IsFadingEnabledProperty, None)
    _MapTileSource_Meta_.IsRetryEnabledProperty = property(get_IsRetryEnabledProperty, None)
    _MapTileSource_Meta_.IsTransparencyEnabledProperty = property(get_IsTransparencyEnabledProperty, None)
    _MapTileSource_Meta_.LayerProperty = property(get_LayerProperty, None)
    _MapTileSource_Meta_.TilePixelSizeProperty = property(get_TilePixelSizeProperty, None)
    _MapTileSource_Meta_.VisibleProperty = property(get_VisibleProperty, None)
    _MapTileSource_Meta_.ZIndexProperty = property(get_ZIndexProperty, None)
    _MapTileSource_Meta_.ZoomLevelRangeProperty = property(get_ZoomLevelRangeProperty, None)
class MapTileUriRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileUriRequest
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapTileUriRequest'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapTileUriRequest.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Controls.Maps.MapTileUriRequest: ...
    @winrt_mixinmethod
    def get_Uri(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileUriRequest) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_Uri(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileUriRequest, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileUriRequest) -> win32more.Windows.UI.Xaml.Controls.Maps.MapTileUriRequestDeferral: ...
    Uri = property(get_Uri, put_Uri)
class MapTileUriRequestDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileUriRequestDeferral
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapTileUriRequestDeferral'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapTileUriRequestDeferral.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Controls.Maps.MapTileUriRequestDeferral: ...
    @winrt_mixinmethod
    def Complete(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileUriRequestDeferral) -> Void: ...
class MapTileUriRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileUriRequestedEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapTileUriRequestedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.MapTileUriRequestedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Controls.Maps.MapTileUriRequestedEventArgs: ...
    @winrt_mixinmethod
    def get_X(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileUriRequestedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_Y(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileUriRequestedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ZoomLevel(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileUriRequestedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileUriRequestedEventArgs) -> win32more.Windows.UI.Xaml.Controls.Maps.MapTileUriRequest: ...
    @winrt_mixinmethod
    def get_FrameIndex(self: win32more.Windows.UI.Xaml.Controls.Maps.IMapTileUriRequestedEventArgs2) -> Int32: ...
    FrameIndex = property(get_FrameIndex, None)
    Request = property(get_Request, None)
    X = property(get_X, None)
    Y = property(get_Y, None)
    ZoomLevel = property(get_ZoomLevel, None)
class MapVisibleRegionKind(Enum, Int32):
    Near = 0
    Full = 1
class MapWatermarkMode(Enum, Int32):
    Automatic = 0
    On = 1
class MapZoomLevelRange(Structure):
    Min: Double
    Max: Double
class StreetsideExperience(ComPtr):
    extends: win32more.Windows.UI.Xaml.Controls.Maps.MapCustomExperience
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IStreetsideExperience
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.StreetsideExperience'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.StreetsideExperience.CreateInstanceWithPanorama(*args))
        elif len(args) == 4:
            super().__init__(move=win32more.Windows.UI.Xaml.Controls.Maps.StreetsideExperience.CreateInstanceWithPanoramaHeadingPitchAndFieldOfView(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithPanorama(cls: win32more.Windows.UI.Xaml.Controls.Maps.IStreetsideExperienceFactory, panorama: win32more.Windows.UI.Xaml.Controls.Maps.StreetsidePanorama) -> win32more.Windows.UI.Xaml.Controls.Maps.StreetsideExperience: ...
    @winrt_factorymethod
    def CreateInstanceWithPanoramaHeadingPitchAndFieldOfView(cls: win32more.Windows.UI.Xaml.Controls.Maps.IStreetsideExperienceFactory, panorama: win32more.Windows.UI.Xaml.Controls.Maps.StreetsidePanorama, headingInDegrees: Double, pitchInDegrees: Double, fieldOfViewInDegrees: Double) -> win32more.Windows.UI.Xaml.Controls.Maps.StreetsideExperience: ...
    @winrt_mixinmethod
    def get_AddressTextVisible(self: win32more.Windows.UI.Xaml.Controls.Maps.IStreetsideExperience) -> Boolean: ...
    @winrt_mixinmethod
    def put_AddressTextVisible(self: win32more.Windows.UI.Xaml.Controls.Maps.IStreetsideExperience, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CursorVisible(self: win32more.Windows.UI.Xaml.Controls.Maps.IStreetsideExperience) -> Boolean: ...
    @winrt_mixinmethod
    def put_CursorVisible(self: win32more.Windows.UI.Xaml.Controls.Maps.IStreetsideExperience, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_OverviewMapVisible(self: win32more.Windows.UI.Xaml.Controls.Maps.IStreetsideExperience) -> Boolean: ...
    @winrt_mixinmethod
    def put_OverviewMapVisible(self: win32more.Windows.UI.Xaml.Controls.Maps.IStreetsideExperience, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_StreetLabelsVisible(self: win32more.Windows.UI.Xaml.Controls.Maps.IStreetsideExperience) -> Boolean: ...
    @winrt_mixinmethod
    def put_StreetLabelsVisible(self: win32more.Windows.UI.Xaml.Controls.Maps.IStreetsideExperience, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ExitButtonVisible(self: win32more.Windows.UI.Xaml.Controls.Maps.IStreetsideExperience) -> Boolean: ...
    @winrt_mixinmethod
    def put_ExitButtonVisible(self: win32more.Windows.UI.Xaml.Controls.Maps.IStreetsideExperience, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ZoomButtonsVisible(self: win32more.Windows.UI.Xaml.Controls.Maps.IStreetsideExperience) -> Boolean: ...
    @winrt_mixinmethod
    def put_ZoomButtonsVisible(self: win32more.Windows.UI.Xaml.Controls.Maps.IStreetsideExperience, value: Boolean) -> Void: ...
    AddressTextVisible = property(get_AddressTextVisible, put_AddressTextVisible)
    CursorVisible = property(get_CursorVisible, put_CursorVisible)
    ExitButtonVisible = property(get_ExitButtonVisible, put_ExitButtonVisible)
    OverviewMapVisible = property(get_OverviewMapVisible, put_OverviewMapVisible)
    StreetLabelsVisible = property(get_StreetLabelsVisible, put_StreetLabelsVisible)
    ZoomButtonsVisible = property(get_ZoomButtonsVisible, put_ZoomButtonsVisible)
class StreetsidePanorama(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Controls.Maps.IStreetsidePanorama
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.StreetsidePanorama'
    @winrt_mixinmethod
    def get_Location(self: win32more.Windows.UI.Xaml.Controls.Maps.IStreetsidePanorama) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_classmethod
    def FindNearbyWithLocationAsync(cls: win32more.Windows.UI.Xaml.Controls.Maps.IStreetsidePanoramaStatics, location: win32more.Windows.Devices.Geolocation.Geopoint) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.Xaml.Controls.Maps.StreetsidePanorama]: ...
    @winrt_classmethod
    def FindNearbyWithLocationAndRadiusAsync(cls: win32more.Windows.UI.Xaml.Controls.Maps.IStreetsidePanoramaStatics, location: win32more.Windows.Devices.Geolocation.Geopoint, radiusInMeters: Double) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.Xaml.Controls.Maps.StreetsidePanorama]: ...
    Location = property(get_Location, None)


make_ready(__name__)
