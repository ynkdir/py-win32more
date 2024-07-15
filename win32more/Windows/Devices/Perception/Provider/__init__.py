from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Devices.Perception
import win32more.Windows.Devices.Perception.Provider
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Foundation.Numerics
import win32more.Windows.Graphics.Imaging
import win32more.Windows.Media
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
class IKnownPerceptionFrameKindStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.Provider.IKnownPerceptionFrameKindStatics'
    _iid_ = Guid('{3ae651d6-9669-4106-9fae-4835c1b96104}')
    @winrt_commethod(6)
    def get_Color(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Depth(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Infrared(self) -> WinRT_String: ...
    Color = property(get_Color, None)
    Depth = property(get_Depth, None)
    Infrared = property(get_Infrared, None)
class IPerceptionControlGroup(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.Provider.IPerceptionControlGroup'
    _iid_ = Guid('{172c4882-2fd9-4c4e-ba34-fdf20a73dde5}')
    @winrt_commethod(6)
    def get_FrameProviderIds(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    FrameProviderIds = property(get_FrameProviderIds, None)
class IPerceptionControlGroupFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.Provider.IPerceptionControlGroupFactory'
    _iid_ = Guid('{2f1af2e0-baf1-453b-bed4-cd9d4619154c}')
    @winrt_commethod(6)
    def Create(self, ids: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Devices.Perception.Provider.PerceptionControlGroup: ...
class IPerceptionCorrelation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.Provider.IPerceptionCorrelation'
    _iid_ = Guid('{b4131a82-dff5-4047-8a19-3b4d805f7176}')
    @winrt_commethod(6)
    def get_TargetId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Position(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(8)
    def get_Orientation(self) -> win32more.Windows.Foundation.Numerics.Quaternion: ...
    Orientation = property(get_Orientation, None)
    Position = property(get_Position, None)
    TargetId = property(get_TargetId, None)
class IPerceptionCorrelationFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.Provider.IPerceptionCorrelationFactory'
    _iid_ = Guid('{d4a6c425-2884-4a8f-8134-2835d7286cbf}')
    @winrt_commethod(6)
    def Create(self, targetId: WinRT_String, position: win32more.Windows.Foundation.Numerics.Vector3, orientation: win32more.Windows.Foundation.Numerics.Quaternion) -> win32more.Windows.Devices.Perception.Provider.PerceptionCorrelation: ...
class IPerceptionCorrelationGroup(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.Provider.IPerceptionCorrelationGroup'
    _iid_ = Guid('{752a0906-36a7-47bb-9b79-56cc6b746770}')
    @winrt_commethod(6)
    def get_RelativeLocations(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Perception.Provider.PerceptionCorrelation]: ...
    RelativeLocations = property(get_RelativeLocations, None)
class IPerceptionCorrelationGroupFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.Provider.IPerceptionCorrelationGroupFactory'
    _iid_ = Guid('{7dfe2088-63df-48ed-83b1-4ab829132995}')
    @winrt_commethod(6)
    def Create(self, relativeLocations: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Devices.Perception.Provider.PerceptionCorrelation]) -> win32more.Windows.Devices.Perception.Provider.PerceptionCorrelationGroup: ...
class IPerceptionFaceAuthenticationGroup(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.Provider.IPerceptionFaceAuthenticationGroup'
    _iid_ = Guid('{e8019814-4a91-41b0-83a6-881a1775353e}')
    @winrt_commethod(6)
    def get_FrameProviderIds(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    FrameProviderIds = property(get_FrameProviderIds, None)
class IPerceptionFaceAuthenticationGroupFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.Provider.IPerceptionFaceAuthenticationGroupFactory'
    _iid_ = Guid('{e68a05d4-b60c-40f4-bcb9-f24d46467320}')
    @winrt_commethod(6)
    def Create(self, ids: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], startHandler: win32more.Windows.Devices.Perception.Provider.PerceptionStartFaceAuthenticationHandler, stopHandler: win32more.Windows.Devices.Perception.Provider.PerceptionStopFaceAuthenticationHandler) -> win32more.Windows.Devices.Perception.Provider.PerceptionFaceAuthenticationGroup: ...
class IPerceptionFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.Provider.IPerceptionFrame'
    _iid_ = Guid('{7cfe7825-54bb-4d9d-bec5-8ef66151d2ac}')
    @winrt_commethod(6)
    def get_RelativeTime(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def put_RelativeTime(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(8)
    def get_Properties(self) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    @winrt_commethod(9)
    def get_FrameData(self) -> win32more.Windows.Foundation.IMemoryBuffer: ...
    FrameData = property(get_FrameData, None)
    Properties = property(get_Properties, None)
    RelativeTime = property(get_RelativeTime, put_RelativeTime)
class IPerceptionFrameProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Windows.Devices.Perception.Provider.IPerceptionFrameProvider'
    _iid_ = Guid('{794f7ab9-b37d-3b33-a10d-30626419ce65}')
    @winrt_commethod(6)
    def get_FrameProviderInfo(self) -> win32more.Windows.Devices.Perception.Provider.PerceptionFrameProviderInfo: ...
    @winrt_commethod(7)
    def get_Available(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_Properties(self) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    @winrt_commethod(9)
    def Start(self) -> Void: ...
    @winrt_commethod(10)
    def Stop(self) -> Void: ...
    @winrt_commethod(11)
    def SetProperty(self, value: win32more.Windows.Devices.Perception.Provider.PerceptionPropertyChangeRequest) -> Void: ...
    Available = property(get_Available, None)
    FrameProviderInfo = property(get_FrameProviderInfo, None)
    Properties = property(get_Properties, None)
class IPerceptionFrameProviderInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.Provider.IPerceptionFrameProviderInfo'
    _iid_ = Guid('{cca959e8-797e-4e83-9b87-036a74142fc4}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Id(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_DisplayName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_DeviceKind(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_DeviceKind(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_FrameKind(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def put_FrameKind(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(14)
    def get_Hidden(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_Hidden(self, value: Boolean) -> Void: ...
    DeviceKind = property(get_DeviceKind, put_DeviceKind)
    DisplayName = property(get_DisplayName, put_DisplayName)
    FrameKind = property(get_FrameKind, put_FrameKind)
    Hidden = property(get_Hidden, put_Hidden)
    Id = property(get_Id, put_Id)
class IPerceptionFrameProviderManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Windows.Devices.Perception.Provider.IPerceptionFrameProviderManager'
    _iid_ = Guid('{a959ce07-ead3-33df-8ec1-b924abe019c4}')
    @winrt_commethod(6)
    def GetFrameProvider(self, frameProviderInfo: win32more.Windows.Devices.Perception.Provider.PerceptionFrameProviderInfo) -> win32more.Windows.Devices.Perception.Provider.IPerceptionFrameProvider: ...
class IPerceptionFrameProviderManagerServiceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.Provider.IPerceptionFrameProviderManagerServiceStatics'
    _iid_ = Guid('{ae8386e6-cad9-4359-8f96-8eae51810526}')
    @winrt_commethod(6)
    def RegisterFrameProviderInfo(self, manager: win32more.Windows.Devices.Perception.Provider.IPerceptionFrameProviderManager, frameProviderInfo: win32more.Windows.Devices.Perception.Provider.PerceptionFrameProviderInfo) -> Void: ...
    @winrt_commethod(7)
    def UnregisterFrameProviderInfo(self, manager: win32more.Windows.Devices.Perception.Provider.IPerceptionFrameProviderManager, frameProviderInfo: win32more.Windows.Devices.Perception.Provider.PerceptionFrameProviderInfo) -> Void: ...
    @winrt_commethod(8)
    def RegisterFaceAuthenticationGroup(self, manager: win32more.Windows.Devices.Perception.Provider.IPerceptionFrameProviderManager, faceAuthenticationGroup: win32more.Windows.Devices.Perception.Provider.PerceptionFaceAuthenticationGroup) -> Void: ...
    @winrt_commethod(9)
    def UnregisterFaceAuthenticationGroup(self, manager: win32more.Windows.Devices.Perception.Provider.IPerceptionFrameProviderManager, faceAuthenticationGroup: win32more.Windows.Devices.Perception.Provider.PerceptionFaceAuthenticationGroup) -> Void: ...
    @winrt_commethod(10)
    def RegisterControlGroup(self, manager: win32more.Windows.Devices.Perception.Provider.IPerceptionFrameProviderManager, controlGroup: win32more.Windows.Devices.Perception.Provider.PerceptionControlGroup) -> Void: ...
    @winrt_commethod(11)
    def UnregisterControlGroup(self, manager: win32more.Windows.Devices.Perception.Provider.IPerceptionFrameProviderManager, controlGroup: win32more.Windows.Devices.Perception.Provider.PerceptionControlGroup) -> Void: ...
    @winrt_commethod(12)
    def RegisterCorrelationGroup(self, manager: win32more.Windows.Devices.Perception.Provider.IPerceptionFrameProviderManager, correlationGroup: win32more.Windows.Devices.Perception.Provider.PerceptionCorrelationGroup) -> Void: ...
    @winrt_commethod(13)
    def UnregisterCorrelationGroup(self, manager: win32more.Windows.Devices.Perception.Provider.IPerceptionFrameProviderManager, correlationGroup: win32more.Windows.Devices.Perception.Provider.PerceptionCorrelationGroup) -> Void: ...
    @winrt_commethod(14)
    def UpdateAvailabilityForProvider(self, provider: win32more.Windows.Devices.Perception.Provider.IPerceptionFrameProvider, available: Boolean) -> Void: ...
    @winrt_commethod(15)
    def PublishFrameForProvider(self, provider: win32more.Windows.Devices.Perception.Provider.IPerceptionFrameProvider, frame: win32more.Windows.Devices.Perception.Provider.PerceptionFrame) -> Void: ...
class IPerceptionPropertyChangeRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.Provider.IPerceptionPropertyChangeRequest'
    _iid_ = Guid('{3c5aeb51-350b-4df8-9414-59e09815510b}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Value(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(8)
    def get_Status(self) -> win32more.Windows.Devices.Perception.PerceptionFrameSourcePropertyChangeStatus: ...
    @winrt_commethod(9)
    def put_Status(self, value: win32more.Windows.Devices.Perception.PerceptionFrameSourcePropertyChangeStatus) -> Void: ...
    @winrt_commethod(10)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Name = property(get_Name, None)
    Status = property(get_Status, put_Status)
    Value = property(get_Value, None)
class IPerceptionVideoFrameAllocator(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Windows.Devices.Perception.Provider.IPerceptionVideoFrameAllocator'
    _iid_ = Guid('{4c38a7da-fdd8-4ed4-a039-2a6f9b235038}')
    @winrt_commethod(6)
    def AllocateFrame(self) -> win32more.Windows.Devices.Perception.Provider.PerceptionFrame: ...
    @winrt_commethod(7)
    def CopyFromVideoFrame(self, frame: win32more.Windows.Media.VideoFrame) -> win32more.Windows.Devices.Perception.Provider.PerceptionFrame: ...
class IPerceptionVideoFrameAllocatorFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.Provider.IPerceptionVideoFrameAllocatorFactory'
    _iid_ = Guid('{1a58b0e1-e91a-481e-b876-a89e2bbc6b33}')
    @winrt_commethod(6)
    def Create(self, maxOutstandingFrameCountForWrite: UInt32, format: win32more.Windows.Graphics.Imaging.BitmapPixelFormat, resolution: win32more.Windows.Foundation.Size, alpha: win32more.Windows.Graphics.Imaging.BitmapAlphaMode) -> win32more.Windows.Devices.Perception.Provider.PerceptionVideoFrameAllocator: ...
class _KnownPerceptionFrameKind_Meta_(ComPtr.__class__):
    pass
class KnownPerceptionFrameKind(ComPtr, metaclass=_KnownPerceptionFrameKind_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.Provider.KnownPerceptionFrameKind'
    @winrt_classmethod
    def get_Color(cls: win32more.Windows.Devices.Perception.Provider.IKnownPerceptionFrameKindStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Depth(cls: win32more.Windows.Devices.Perception.Provider.IKnownPerceptionFrameKindStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Infrared(cls: win32more.Windows.Devices.Perception.Provider.IKnownPerceptionFrameKindStatics) -> WinRT_String: ...
    _KnownPerceptionFrameKind_Meta_.Color = property(get_Color, None)
    _KnownPerceptionFrameKind_Meta_.Depth = property(get_Depth, None)
    _KnownPerceptionFrameKind_Meta_.Infrared = property(get_Infrared, None)
class PerceptionControlGroup(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Perception.Provider.IPerceptionControlGroup
    _classid_ = 'Windows.Devices.Perception.Provider.PerceptionControlGroup'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Devices.Perception.Provider.PerceptionControlGroup.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Devices.Perception.Provider.IPerceptionControlGroupFactory, ids: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Devices.Perception.Provider.PerceptionControlGroup: ...
    @winrt_mixinmethod
    def get_FrameProviderIds(self: win32more.Windows.Devices.Perception.Provider.IPerceptionControlGroup) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    FrameProviderIds = property(get_FrameProviderIds, None)
class PerceptionCorrelation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Perception.Provider.IPerceptionCorrelation
    _classid_ = 'Windows.Devices.Perception.Provider.PerceptionCorrelation'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Devices.Perception.Provider.PerceptionCorrelation.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Devices.Perception.Provider.IPerceptionCorrelationFactory, targetId: WinRT_String, position: win32more.Windows.Foundation.Numerics.Vector3, orientation: win32more.Windows.Foundation.Numerics.Quaternion) -> win32more.Windows.Devices.Perception.Provider.PerceptionCorrelation: ...
    @winrt_mixinmethod
    def get_TargetId(self: win32more.Windows.Devices.Perception.Provider.IPerceptionCorrelation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.Devices.Perception.Provider.IPerceptionCorrelation) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_Orientation(self: win32more.Windows.Devices.Perception.Provider.IPerceptionCorrelation) -> win32more.Windows.Foundation.Numerics.Quaternion: ...
    Orientation = property(get_Orientation, None)
    Position = property(get_Position, None)
    TargetId = property(get_TargetId, None)
class PerceptionCorrelationGroup(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Perception.Provider.IPerceptionCorrelationGroup
    _classid_ = 'Windows.Devices.Perception.Provider.PerceptionCorrelationGroup'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Devices.Perception.Provider.PerceptionCorrelationGroup.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Devices.Perception.Provider.IPerceptionCorrelationGroupFactory, relativeLocations: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Devices.Perception.Provider.PerceptionCorrelation]) -> win32more.Windows.Devices.Perception.Provider.PerceptionCorrelationGroup: ...
    @winrt_mixinmethod
    def get_RelativeLocations(self: win32more.Windows.Devices.Perception.Provider.IPerceptionCorrelationGroup) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Perception.Provider.PerceptionCorrelation]: ...
    RelativeLocations = property(get_RelativeLocations, None)
class PerceptionFaceAuthenticationGroup(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Perception.Provider.IPerceptionFaceAuthenticationGroup
    _classid_ = 'Windows.Devices.Perception.Provider.PerceptionFaceAuthenticationGroup'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Devices.Perception.Provider.PerceptionFaceAuthenticationGroup.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Devices.Perception.Provider.IPerceptionFaceAuthenticationGroupFactory, ids: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], startHandler: win32more.Windows.Devices.Perception.Provider.PerceptionStartFaceAuthenticationHandler, stopHandler: win32more.Windows.Devices.Perception.Provider.PerceptionStopFaceAuthenticationHandler) -> win32more.Windows.Devices.Perception.Provider.PerceptionFaceAuthenticationGroup: ...
    @winrt_mixinmethod
    def get_FrameProviderIds(self: win32more.Windows.Devices.Perception.Provider.IPerceptionFaceAuthenticationGroup) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    FrameProviderIds = property(get_FrameProviderIds, None)
class PerceptionFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Perception.Provider.IPerceptionFrame
    _classid_ = 'Windows.Devices.Perception.Provider.PerceptionFrame'
    @winrt_mixinmethod
    def get_RelativeTime(self: win32more.Windows.Devices.Perception.Provider.IPerceptionFrame) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_RelativeTime(self: win32more.Windows.Devices.Perception.Provider.IPerceptionFrame, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Devices.Perception.Provider.IPerceptionFrame) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_FrameData(self: win32more.Windows.Devices.Perception.Provider.IPerceptionFrame) -> win32more.Windows.Foundation.IMemoryBuffer: ...
    FrameData = property(get_FrameData, None)
    Properties = property(get_Properties, None)
    RelativeTime = property(get_RelativeTime, put_RelativeTime)
class PerceptionFrameProviderInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Perception.Provider.IPerceptionFrameProviderInfo
    _classid_ = 'Windows.Devices.Perception.Provider.PerceptionFrameProviderInfo'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Devices.Perception.Provider.PerceptionFrameProviderInfo.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.Perception.Provider.PerceptionFrameProviderInfo: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Devices.Perception.Provider.IPerceptionFrameProviderInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Id(self: win32more.Windows.Devices.Perception.Provider.IPerceptionFrameProviderInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.Devices.Perception.Provider.IPerceptionFrameProviderInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayName(self: win32more.Windows.Devices.Perception.Provider.IPerceptionFrameProviderInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DeviceKind(self: win32more.Windows.Devices.Perception.Provider.IPerceptionFrameProviderInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DeviceKind(self: win32more.Windows.Devices.Perception.Provider.IPerceptionFrameProviderInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_FrameKind(self: win32more.Windows.Devices.Perception.Provider.IPerceptionFrameProviderInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_FrameKind(self: win32more.Windows.Devices.Perception.Provider.IPerceptionFrameProviderInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Hidden(self: win32more.Windows.Devices.Perception.Provider.IPerceptionFrameProviderInfo) -> Boolean: ...
    @winrt_mixinmethod
    def put_Hidden(self: win32more.Windows.Devices.Perception.Provider.IPerceptionFrameProviderInfo, value: Boolean) -> Void: ...
    DeviceKind = property(get_DeviceKind, put_DeviceKind)
    DisplayName = property(get_DisplayName, put_DisplayName)
    FrameKind = property(get_FrameKind, put_FrameKind)
    Hidden = property(get_Hidden, put_Hidden)
    Id = property(get_Id, put_Id)
class PerceptionFrameProviderManagerService(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Perception.Provider.PerceptionFrameProviderManagerService'
    @winrt_classmethod
    def RegisterFrameProviderInfo(cls: win32more.Windows.Devices.Perception.Provider.IPerceptionFrameProviderManagerServiceStatics, manager: win32more.Windows.Devices.Perception.Provider.IPerceptionFrameProviderManager, frameProviderInfo: win32more.Windows.Devices.Perception.Provider.PerceptionFrameProviderInfo) -> Void: ...
    @winrt_classmethod
    def UnregisterFrameProviderInfo(cls: win32more.Windows.Devices.Perception.Provider.IPerceptionFrameProviderManagerServiceStatics, manager: win32more.Windows.Devices.Perception.Provider.IPerceptionFrameProviderManager, frameProviderInfo: win32more.Windows.Devices.Perception.Provider.PerceptionFrameProviderInfo) -> Void: ...
    @winrt_classmethod
    def RegisterFaceAuthenticationGroup(cls: win32more.Windows.Devices.Perception.Provider.IPerceptionFrameProviderManagerServiceStatics, manager: win32more.Windows.Devices.Perception.Provider.IPerceptionFrameProviderManager, faceAuthenticationGroup: win32more.Windows.Devices.Perception.Provider.PerceptionFaceAuthenticationGroup) -> Void: ...
    @winrt_classmethod
    def UnregisterFaceAuthenticationGroup(cls: win32more.Windows.Devices.Perception.Provider.IPerceptionFrameProviderManagerServiceStatics, manager: win32more.Windows.Devices.Perception.Provider.IPerceptionFrameProviderManager, faceAuthenticationGroup: win32more.Windows.Devices.Perception.Provider.PerceptionFaceAuthenticationGroup) -> Void: ...
    @winrt_classmethod
    def RegisterControlGroup(cls: win32more.Windows.Devices.Perception.Provider.IPerceptionFrameProviderManagerServiceStatics, manager: win32more.Windows.Devices.Perception.Provider.IPerceptionFrameProviderManager, controlGroup: win32more.Windows.Devices.Perception.Provider.PerceptionControlGroup) -> Void: ...
    @winrt_classmethod
    def UnregisterControlGroup(cls: win32more.Windows.Devices.Perception.Provider.IPerceptionFrameProviderManagerServiceStatics, manager: win32more.Windows.Devices.Perception.Provider.IPerceptionFrameProviderManager, controlGroup: win32more.Windows.Devices.Perception.Provider.PerceptionControlGroup) -> Void: ...
    @winrt_classmethod
    def RegisterCorrelationGroup(cls: win32more.Windows.Devices.Perception.Provider.IPerceptionFrameProviderManagerServiceStatics, manager: win32more.Windows.Devices.Perception.Provider.IPerceptionFrameProviderManager, correlationGroup: win32more.Windows.Devices.Perception.Provider.PerceptionCorrelationGroup) -> Void: ...
    @winrt_classmethod
    def UnregisterCorrelationGroup(cls: win32more.Windows.Devices.Perception.Provider.IPerceptionFrameProviderManagerServiceStatics, manager: win32more.Windows.Devices.Perception.Provider.IPerceptionFrameProviderManager, correlationGroup: win32more.Windows.Devices.Perception.Provider.PerceptionCorrelationGroup) -> Void: ...
    @winrt_classmethod
    def UpdateAvailabilityForProvider(cls: win32more.Windows.Devices.Perception.Provider.IPerceptionFrameProviderManagerServiceStatics, provider: win32more.Windows.Devices.Perception.Provider.IPerceptionFrameProvider, available: Boolean) -> Void: ...
    @winrt_classmethod
    def PublishFrameForProvider(cls: win32more.Windows.Devices.Perception.Provider.IPerceptionFrameProviderManagerServiceStatics, provider: win32more.Windows.Devices.Perception.Provider.IPerceptionFrameProvider, frame: win32more.Windows.Devices.Perception.Provider.PerceptionFrame) -> Void: ...
class PerceptionPropertyChangeRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Perception.Provider.IPerceptionPropertyChangeRequest
    _classid_ = 'Windows.Devices.Perception.Provider.PerceptionPropertyChangeRequest'
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Devices.Perception.Provider.IPerceptionPropertyChangeRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.Devices.Perception.Provider.IPerceptionPropertyChangeRequest) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Devices.Perception.Provider.IPerceptionPropertyChangeRequest) -> win32more.Windows.Devices.Perception.PerceptionFrameSourcePropertyChangeStatus: ...
    @winrt_mixinmethod
    def put_Status(self: win32more.Windows.Devices.Perception.Provider.IPerceptionPropertyChangeRequest, value: win32more.Windows.Devices.Perception.PerceptionFrameSourcePropertyChangeStatus) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Devices.Perception.Provider.IPerceptionPropertyChangeRequest) -> win32more.Windows.Foundation.Deferral: ...
    Name = property(get_Name, None)
    Status = property(get_Status, put_Status)
    Value = property(get_Value, None)
class PerceptionStartFaceAuthenticationHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{74816d2a-2090-4670-8c48-ef39e7ff7c26}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Devices.Perception.Provider.PerceptionFaceAuthenticationGroup) -> Boolean: ...
class PerceptionStopFaceAuthenticationHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{387ee6aa-89cd-481e-aade-dd92f70b2ad7}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Devices.Perception.Provider.PerceptionFaceAuthenticationGroup) -> Void: ...
class PerceptionVideoFrameAllocator(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Devices.Perception.Provider.IPerceptionVideoFrameAllocator
    _classid_ = 'Windows.Devices.Perception.Provider.PerceptionVideoFrameAllocator'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 4:
            super().__init__(move=win32more.Windows.Devices.Perception.Provider.PerceptionVideoFrameAllocator.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Devices.Perception.Provider.IPerceptionVideoFrameAllocatorFactory, maxOutstandingFrameCountForWrite: UInt32, format: win32more.Windows.Graphics.Imaging.BitmapPixelFormat, resolution: win32more.Windows.Foundation.Size, alpha: win32more.Windows.Graphics.Imaging.BitmapAlphaMode) -> win32more.Windows.Devices.Perception.Provider.PerceptionVideoFrameAllocator: ...
    @winrt_mixinmethod
    def AllocateFrame(self: win32more.Windows.Devices.Perception.Provider.IPerceptionVideoFrameAllocator) -> win32more.Windows.Devices.Perception.Provider.PerceptionFrame: ...
    @winrt_mixinmethod
    def CopyFromVideoFrame(self: win32more.Windows.Devices.Perception.Provider.IPerceptionVideoFrameAllocator, frame: win32more.Windows.Media.VideoFrame) -> win32more.Windows.Devices.Perception.Provider.PerceptionFrame: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...


make_ready(__name__)
