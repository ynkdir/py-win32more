from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Microsoft.Windows.PushNotifications
import win32more.Windows.ApplicationModel.Background
import win32more.Windows.Foundation
import win32more.Windows.Win32.System.WinRT
class IPushNotificationChannel(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.PushNotifications.IPushNotificationChannel'
    _iid_ = Guid('{da28bbcb-7695-5d38-af82-f30b72fef1f6}')
    @winrt_commethod(6)
    def get_Uri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def get_ExpirationTime(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(8)
    def Close(self) -> Void: ...
    ExpirationTime = property(get_ExpirationTime, None)
    Uri = property(get_Uri, None)
class IPushNotificationCreateChannelResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.PushNotifications.IPushNotificationCreateChannelResult'
    _iid_ = Guid('{4df3717f-5d33-56e9-b381-1b350c95722e}')
    @winrt_commethod(6)
    def get_Channel(self) -> win32more.Microsoft.Windows.PushNotifications.PushNotificationChannel: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    @winrt_commethod(8)
    def get_Status(self) -> win32more.Microsoft.Windows.PushNotifications.PushNotificationChannelStatus: ...
    Channel = property(get_Channel, None)
    ExtendedError = property(get_ExtendedError, None)
    Status = property(get_Status, None)
class IPushNotificationManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.PushNotifications.IPushNotificationManager'
    _iid_ = Guid('{902f4aba-ff63-5dfe-a88f-15cc6bed55ff}')
    @winrt_commethod(6)
    def Register(self) -> Void: ...
    @winrt_commethod(7)
    def Unregister(self) -> Void: ...
    @winrt_commethod(8)
    def UnregisterAll(self) -> Void: ...
    @winrt_commethod(9)
    def CreateChannelAsync(self, remoteId: Guid) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.PushNotifications.PushNotificationCreateChannelResult, win32more.Microsoft.Windows.PushNotifications.PushNotificationCreateChannelStatus]: ...
    @winrt_commethod(10)
    def add_PushReceived(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Windows.PushNotifications.PushNotificationManager, win32more.Microsoft.Windows.PushNotifications.PushNotificationReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_PushReceived(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    PushReceived = event()
class IPushNotificationManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.PushNotifications.IPushNotificationManagerStatics'
    _iid_ = Guid('{71329470-1b55-58dc-a00c-68c26f2d8bd9}')
    @winrt_commethod(6)
    def IsSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_Default(self) -> win32more.Microsoft.Windows.PushNotifications.PushNotificationManager: ...
    Default = property(get_Default, None)
class IPushNotificationReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.PushNotifications.IPushNotificationReceivedEventArgs'
    _iid_ = Guid('{fbd4ec53-bb83-5495-8777-d3cf13e4299c}')
    @winrt_commethod(6)
    def get_Payload(self) -> ReceiveArray[Byte]: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.ApplicationModel.Background.BackgroundTaskDeferral: ...
    @winrt_commethod(8)
    def add_Canceled(self, handler: win32more.Windows.ApplicationModel.Background.BackgroundTaskCanceledEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_Canceled(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Payload = property(get_Payload, None)
    Canceled = event()
class PushNotificationChannel(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.PushNotifications.IPushNotificationChannel
    _classid_ = 'Microsoft.Windows.PushNotifications.PushNotificationChannel'
    @winrt_mixinmethod
    def get_Uri(self: win32more.Microsoft.Windows.PushNotifications.IPushNotificationChannel) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_ExpirationTime(self: win32more.Microsoft.Windows.PushNotifications.IPushNotificationChannel) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def Close(self: win32more.Microsoft.Windows.PushNotifications.IPushNotificationChannel) -> Void: ...
    ExpirationTime = property(get_ExpirationTime, None)
    Uri = property(get_Uri, None)
class PushNotificationChannelStatus(Enum, Int32):
    InProgress = 0
    InProgressRetry = 1
    CompletedSuccess = 2
    CompletedFailure = 3
class PushNotificationCreateChannelResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.PushNotifications.IPushNotificationCreateChannelResult
    _classid_ = 'Microsoft.Windows.PushNotifications.PushNotificationCreateChannelResult'
    @winrt_mixinmethod
    def get_Channel(self: win32more.Microsoft.Windows.PushNotifications.IPushNotificationCreateChannelResult) -> win32more.Microsoft.Windows.PushNotifications.PushNotificationChannel: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Microsoft.Windows.PushNotifications.IPushNotificationCreateChannelResult) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Microsoft.Windows.PushNotifications.IPushNotificationCreateChannelResult) -> win32more.Microsoft.Windows.PushNotifications.PushNotificationChannelStatus: ...
    Channel = property(get_Channel, None)
    ExtendedError = property(get_ExtendedError, None)
    Status = property(get_Status, None)
class PushNotificationCreateChannelStatus(Structure):
    status: win32more.Microsoft.Windows.PushNotifications.PushNotificationChannelStatus
    extendedError: win32more.Windows.Foundation.HResult
    retryCount: UInt32
class _PushNotificationManager_Meta_(ComPtr.__class__):
    pass
class PushNotificationManager(ComPtr, metaclass=_PushNotificationManager_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.PushNotifications.IPushNotificationManager
    _classid_ = 'Microsoft.Windows.PushNotifications.PushNotificationManager'
    @winrt_mixinmethod
    def Register(self: win32more.Microsoft.Windows.PushNotifications.IPushNotificationManager) -> Void: ...
    @winrt_mixinmethod
    def Unregister(self: win32more.Microsoft.Windows.PushNotifications.IPushNotificationManager) -> Void: ...
    @winrt_mixinmethod
    def UnregisterAll(self: win32more.Microsoft.Windows.PushNotifications.IPushNotificationManager) -> Void: ...
    @winrt_mixinmethod
    def CreateChannelAsync(self: win32more.Microsoft.Windows.PushNotifications.IPushNotificationManager, remoteId: Guid) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.PushNotifications.PushNotificationCreateChannelResult, win32more.Microsoft.Windows.PushNotifications.PushNotificationCreateChannelStatus]: ...
    @winrt_mixinmethod
    def add_PushReceived(self: win32more.Microsoft.Windows.PushNotifications.IPushNotificationManager, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Windows.PushNotifications.PushNotificationManager, win32more.Microsoft.Windows.PushNotifications.PushNotificationReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PushReceived(self: win32more.Microsoft.Windows.PushNotifications.IPushNotificationManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def IsSupported(cls: win32more.Microsoft.Windows.PushNotifications.IPushNotificationManagerStatics) -> Boolean: ...
    @winrt_classmethod
    def get_Default(cls: win32more.Microsoft.Windows.PushNotifications.IPushNotificationManagerStatics) -> win32more.Microsoft.Windows.PushNotifications.PushNotificationManager: ...
    _PushNotificationManager_Meta_.Default = property(get_Default, None)
    PushReceived = event()
class PushNotificationReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.PushNotifications.IPushNotificationReceivedEventArgs
    _classid_ = 'Microsoft.Windows.PushNotifications.PushNotificationReceivedEventArgs'
    @winrt_mixinmethod
    def get_Payload(self: win32more.Microsoft.Windows.PushNotifications.IPushNotificationReceivedEventArgs) -> ReceiveArray[Byte]: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Microsoft.Windows.PushNotifications.IPushNotificationReceivedEventArgs) -> win32more.Windows.ApplicationModel.Background.BackgroundTaskDeferral: ...
    @winrt_mixinmethod
    def add_Canceled(self: win32more.Microsoft.Windows.PushNotifications.IPushNotificationReceivedEventArgs, handler: win32more.Windows.ApplicationModel.Background.BackgroundTaskCanceledEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Canceled(self: win32more.Microsoft.Windows.PushNotifications.IPushNotificationReceivedEventArgs, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Payload = property(get_Payload, None)
    Canceled = event()
PushNotificationsContract: UInt32 = 65536


make_ready(__name__)
