from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.System.Power.Thermal
class IPowerThermalChannelConfiguration(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.System.Power.Thermal.IPowerThermalChannelConfiguration'
    _iid_ = Guid('{ad8383fa-172d-5d82-b29d-81d93710fb45}')
    @winrt_commethod(6)
    def get_Id(self) -> win32more.Windows.System.Power.Thermal.PowerThermalChannelId: ...
    @winrt_commethod(7)
    def get_ConfigurationString(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def GetConfigurationNumericParameters(self) -> ReceiveArray[Int32]: ...
    ConfigurationString = property(get_ConfigurationString, None)
    Id = property(get_Id, None)
class IPowerThermalChannelDataConsumer(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.System.Power.Thermal.IPowerThermalChannelDataConsumer'
    _iid_ = Guid('{47cca211-7348-5026-898c-b1873123760d}')
    @winrt_commethod(6)
    def GetChannelIds(self) -> ReceiveArray[win32more.Windows.System.Power.Thermal.PowerThermalChannelId]: ...
    @winrt_commethod(7)
    def GetChannelConfigurations(self) -> win32more.Windows.Foundation.Collections.IMapView[win32more.Windows.System.Power.Thermal.PowerThermalChannelId, win32more.Windows.System.Power.Thermal.PowerThermalChannelConfiguration]: ...
    @winrt_commethod(8)
    def Start(self) -> Void: ...
    @winrt_commethod(9)
    def Stop(self) -> Void: ...
    @winrt_commethod(10)
    def add_ChannelDataReceived(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.Power.Thermal.PowerThermalChannelDataConsumer, win32more.Windows.System.Power.Thermal.PowerThermalChannelDataReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_ChannelDataReceived(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def get_BackEndStatus(self) -> win32more.Windows.System.Power.Thermal.PowerThermalBackEndStatus: ...
    @winrt_commethod(13)
    def add_BackEndStatusChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.Power.Thermal.PowerThermalChannelDataConsumer, IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_BackEndStatusChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    BackEndStatus = property(get_BackEndStatus, None)
    BackEndStatusChanged = event(add_BackEndStatusChanged, remove_BackEndStatusChanged)
    ChannelDataReceived = event(add_ChannelDataReceived, remove_ChannelDataReceived)
class IPowerThermalChannelDataConsumerFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.System.Power.Thermal.IPowerThermalChannelDataConsumerFactory'
    _iid_ = Guid('{b42d9ab1-32f0-54bb-899a-9ae0529da381}')
    @winrt_commethod(6)
    def CreateInstance(self, channelIds: PassArray[win32more.Windows.System.Power.Thermal.PowerThermalChannelId]) -> win32more.Windows.System.Power.Thermal.PowerThermalChannelDataConsumer: ...
class IPowerThermalChannelDataProducer(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.System.Power.Thermal.IPowerThermalChannelDataProducer'
    _iid_ = Guid('{a935f244-1a7d-55d5-9c69-8adc1cd1d993}')
    @winrt_commethod(6)
    def GetChannelIds(self) -> ReceiveArray[win32more.Windows.System.Power.Thermal.PowerThermalChannelId]: ...
    @winrt_commethod(7)
    def GetChannelConfigurations(self) -> win32more.Windows.Foundation.Collections.IMapView[win32more.Windows.System.Power.Thermal.PowerThermalChannelId, win32more.Windows.System.Power.Thermal.PowerThermalChannelConfiguration]: ...
    @winrt_commethod(8)
    def DisableChannel(self, channelId: win32more.Windows.System.Power.Thermal.PowerThermalChannelId) -> Void: ...
    @winrt_commethod(9)
    def Start(self) -> Void: ...
    @winrt_commethod(10)
    def Stop(self) -> Void: ...
    @winrt_commethod(11)
    def PublishInputChannelData(self, data: PassArray[win32more.Windows.System.Power.Thermal.PowerThermalChannelData]) -> Void: ...
    @winrt_commethod(12)
    def get_BackEndStatus(self) -> win32more.Windows.System.Power.Thermal.PowerThermalBackEndStatus: ...
    @winrt_commethod(13)
    def add_BackEndStatusChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.Power.Thermal.PowerThermalChannelDataProducer, IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_BackEndStatusChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    BackEndStatus = property(get_BackEndStatus, None)
    BackEndStatusChanged = event(add_BackEndStatusChanged, remove_BackEndStatusChanged)
class IPowerThermalChannelDataProducerFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.System.Power.Thermal.IPowerThermalChannelDataProducerFactory'
    _iid_ = Guid('{d2d380cd-e09d-5472-ad62-70061e630067}')
    @winrt_commethod(6)
    def CreateInstance(self, channelIds: PassArray[win32more.Windows.System.Power.Thermal.PowerThermalChannelId]) -> win32more.Windows.System.Power.Thermal.PowerThermalChannelDataProducer: ...
class IPowerThermalChannelDataReceivedEventArgs(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.System.Power.Thermal.IPowerThermalChannelDataReceivedEventArgs'
    _iid_ = Guid('{d6b643e0-6ab6-5683-a8fc-5ed65ee20dc5}')
    @winrt_commethod(6)
    def GetData(self) -> ReceiveArray[win32more.Windows.System.Power.Thermal.PowerThermalChannelData]: ...
class IPowerThermalChannelDiagnostics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.System.Power.Thermal.IPowerThermalChannelDiagnostics'
    _iid_ = Guid('{628fd5c4-49b7-508f-ad9f-2309b1168aad}')
class IPowerThermalChannelDiagnosticsStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.System.Power.Thermal.IPowerThermalChannelDiagnosticsStatics'
    _iid_ = Guid('{a86ec393-b684-5633-a6ca-dfa1c7eecf87}')
    @winrt_commethod(6)
    def get_Current(self) -> win32more.Windows.System.Power.Thermal.PowerThermalChannelDiagnostics: ...
    @winrt_commethod(7)
    def GetDataForChannels(self, channelIds: PassArray[win32more.Windows.System.Power.Thermal.PowerThermalChannelId]) -> ReceiveArray[win32more.Windows.System.Power.Thermal.PowerThermalChannelData]: ...
    Current = property(get_Current, None)
class IPowerThermalChannelFinderStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.System.Power.Thermal.IPowerThermalChannelFinderStatics'
    _iid_ = Guid('{df8d288b-f056-55ce-b370-f3e1c4e32063}')
    @winrt_commethod(6)
    def FindChannels(self, channelInterfaceType: Guid) -> ReceiveArray[win32more.Windows.System.Power.Thermal.PowerThermalChannelId]: ...
PowerThermalApiContract: UInt32 = 65536
class PowerThermalBackEndStatus(Enum, Int32):
    Stopped = 0
    Started = 1
class PowerThermalChannelConfiguration(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.System.Power.Thermal.IPowerThermalChannelConfiguration
    _classid_ = 'Windows.System.Power.Thermal.PowerThermalChannelConfiguration'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.System.Power.Thermal.IPowerThermalChannelConfiguration) -> win32more.Windows.System.Power.Thermal.PowerThermalChannelId: ...
    @winrt_mixinmethod
    def get_ConfigurationString(self: win32more.Windows.System.Power.Thermal.IPowerThermalChannelConfiguration) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetConfigurationNumericParameters(self: win32more.Windows.System.Power.Thermal.IPowerThermalChannelConfiguration) -> ReceiveArray[Int32]: ...
    ConfigurationString = property(get_ConfigurationString, None)
    Id = property(get_Id, None)
class PowerThermalChannelData(Structure):
    Id: win32more.Windows.System.Power.Thermal.PowerThermalChannelId
    Value: Int32
class PowerThermalChannelDataConsumer(ComPtr):
    extends: IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.System.Power.Thermal.IPowerThermalChannelDataConsumer
    _classid_ = 'Windows.System.Power.Thermal.PowerThermalChannelDataConsumer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.System.Power.Thermal.PowerThermalChannelDataConsumer.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.System.Power.Thermal.IPowerThermalChannelDataConsumerFactory, channelIds: PassArray[win32more.Windows.System.Power.Thermal.PowerThermalChannelId]) -> win32more.Windows.System.Power.Thermal.PowerThermalChannelDataConsumer: ...
    @winrt_mixinmethod
    def GetChannelIds(self: win32more.Windows.System.Power.Thermal.IPowerThermalChannelDataConsumer) -> ReceiveArray[win32more.Windows.System.Power.Thermal.PowerThermalChannelId]: ...
    @winrt_mixinmethod
    def GetChannelConfigurations(self: win32more.Windows.System.Power.Thermal.IPowerThermalChannelDataConsumer) -> win32more.Windows.Foundation.Collections.IMapView[win32more.Windows.System.Power.Thermal.PowerThermalChannelId, win32more.Windows.System.Power.Thermal.PowerThermalChannelConfiguration]: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.System.Power.Thermal.IPowerThermalChannelDataConsumer) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.System.Power.Thermal.IPowerThermalChannelDataConsumer) -> Void: ...
    @winrt_mixinmethod
    def add_ChannelDataReceived(self: win32more.Windows.System.Power.Thermal.IPowerThermalChannelDataConsumer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.Power.Thermal.PowerThermalChannelDataConsumer, win32more.Windows.System.Power.Thermal.PowerThermalChannelDataReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ChannelDataReceived(self: win32more.Windows.System.Power.Thermal.IPowerThermalChannelDataConsumer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_BackEndStatus(self: win32more.Windows.System.Power.Thermal.IPowerThermalChannelDataConsumer) -> win32more.Windows.System.Power.Thermal.PowerThermalBackEndStatus: ...
    @winrt_mixinmethod
    def add_BackEndStatusChanged(self: win32more.Windows.System.Power.Thermal.IPowerThermalChannelDataConsumer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.Power.Thermal.PowerThermalChannelDataConsumer, IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_BackEndStatusChanged(self: win32more.Windows.System.Power.Thermal.IPowerThermalChannelDataConsumer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    BackEndStatus = property(get_BackEndStatus, None)
    BackEndStatusChanged = event(add_BackEndStatusChanged, remove_BackEndStatusChanged)
    ChannelDataReceived = event(add_ChannelDataReceived, remove_ChannelDataReceived)
class PowerThermalChannelDataProducer(ComPtr):
    extends: IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.System.Power.Thermal.IPowerThermalChannelDataProducer
    _classid_ = 'Windows.System.Power.Thermal.PowerThermalChannelDataProducer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.System.Power.Thermal.PowerThermalChannelDataProducer.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.System.Power.Thermal.IPowerThermalChannelDataProducerFactory, channelIds: PassArray[win32more.Windows.System.Power.Thermal.PowerThermalChannelId]) -> win32more.Windows.System.Power.Thermal.PowerThermalChannelDataProducer: ...
    @winrt_mixinmethod
    def GetChannelIds(self: win32more.Windows.System.Power.Thermal.IPowerThermalChannelDataProducer) -> ReceiveArray[win32more.Windows.System.Power.Thermal.PowerThermalChannelId]: ...
    @winrt_mixinmethod
    def GetChannelConfigurations(self: win32more.Windows.System.Power.Thermal.IPowerThermalChannelDataProducer) -> win32more.Windows.Foundation.Collections.IMapView[win32more.Windows.System.Power.Thermal.PowerThermalChannelId, win32more.Windows.System.Power.Thermal.PowerThermalChannelConfiguration]: ...
    @winrt_mixinmethod
    def DisableChannel(self: win32more.Windows.System.Power.Thermal.IPowerThermalChannelDataProducer, channelId: win32more.Windows.System.Power.Thermal.PowerThermalChannelId) -> Void: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.System.Power.Thermal.IPowerThermalChannelDataProducer) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.System.Power.Thermal.IPowerThermalChannelDataProducer) -> Void: ...
    @winrt_mixinmethod
    def PublishInputChannelData(self: win32more.Windows.System.Power.Thermal.IPowerThermalChannelDataProducer, data: PassArray[win32more.Windows.System.Power.Thermal.PowerThermalChannelData]) -> Void: ...
    @winrt_mixinmethod
    def get_BackEndStatus(self: win32more.Windows.System.Power.Thermal.IPowerThermalChannelDataProducer) -> win32more.Windows.System.Power.Thermal.PowerThermalBackEndStatus: ...
    @winrt_mixinmethod
    def add_BackEndStatusChanged(self: win32more.Windows.System.Power.Thermal.IPowerThermalChannelDataProducer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.Power.Thermal.PowerThermalChannelDataProducer, IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_BackEndStatusChanged(self: win32more.Windows.System.Power.Thermal.IPowerThermalChannelDataProducer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    BackEndStatus = property(get_BackEndStatus, None)
    BackEndStatusChanged = event(add_BackEndStatusChanged, remove_BackEndStatusChanged)
class PowerThermalChannelDataReceivedEventArgs(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.System.Power.Thermal.IPowerThermalChannelDataReceivedEventArgs
    _classid_ = 'Windows.System.Power.Thermal.PowerThermalChannelDataReceivedEventArgs'
    @winrt_mixinmethod
    def GetData(self: win32more.Windows.System.Power.Thermal.IPowerThermalChannelDataReceivedEventArgs) -> ReceiveArray[win32more.Windows.System.Power.Thermal.PowerThermalChannelData]: ...
class _PowerThermalChannelDiagnostics_Meta_(ComPtr.__class__):
    pass
class PowerThermalChannelDiagnostics(ComPtr, metaclass=_PowerThermalChannelDiagnostics_Meta_):
    extends: IInspectable
    default_interface: win32more.Windows.System.Power.Thermal.IPowerThermalChannelDiagnostics
    _classid_ = 'Windows.System.Power.Thermal.PowerThermalChannelDiagnostics'
    @winrt_classmethod
    def get_Current(cls: win32more.Windows.System.Power.Thermal.IPowerThermalChannelDiagnosticsStatics) -> win32more.Windows.System.Power.Thermal.PowerThermalChannelDiagnostics: ...
    @winrt_classmethod
    def GetDataForChannels(cls: win32more.Windows.System.Power.Thermal.IPowerThermalChannelDiagnosticsStatics, channelIds: PassArray[win32more.Windows.System.Power.Thermal.PowerThermalChannelId]) -> ReceiveArray[win32more.Windows.System.Power.Thermal.PowerThermalChannelData]: ...
    _PowerThermalChannelDiagnostics_Meta_.Current = property(get_Current, None)
class PowerThermalChannelFinder(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.System.Power.Thermal.PowerThermalChannelFinder'
    @winrt_classmethod
    def FindChannels(cls: win32more.Windows.System.Power.Thermal.IPowerThermalChannelFinderStatics, channelInterfaceType: Guid) -> ReceiveArray[win32more.Windows.System.Power.Thermal.PowerThermalChannelId]: ...
class PowerThermalChannelId(Structure):
    InterfaceType: Guid
    InstanceId: UInt16


make_ready(__name__)
