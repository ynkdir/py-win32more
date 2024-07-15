from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel.ExtendedExecution.Foreground
import win32more.Windows.Foundation
import win32more.Windows.Win32.System.WinRT
class ExtendedExecutionForegroundReason(Enum, Int32):
    Unspecified = 0
    SavingData = 1
    BackgroundAudio = 2
    Unconstrained = 3
class ExtendedExecutionForegroundResult(Enum, Int32):
    Allowed = 0
    Denied = 1
class ExtendedExecutionForegroundRevokedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.ExtendedExecution.Foreground.IExtendedExecutionForegroundRevokedEventArgs
    _classid_ = 'Windows.ApplicationModel.ExtendedExecution.Foreground.ExtendedExecutionForegroundRevokedEventArgs'
    @winrt_mixinmethod
    def get_Reason(self: win32more.Windows.ApplicationModel.ExtendedExecution.Foreground.IExtendedExecutionForegroundRevokedEventArgs) -> win32more.Windows.ApplicationModel.ExtendedExecution.Foreground.ExtendedExecutionForegroundRevokedReason: ...
    Reason = property(get_Reason, None)
class ExtendedExecutionForegroundRevokedReason(Enum, Int32):
    Resumed = 0
    SystemPolicy = 1
class ExtendedExecutionForegroundSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.ApplicationModel.ExtendedExecution.Foreground.IExtendedExecutionForegroundSession
    _classid_ = 'Windows.ApplicationModel.ExtendedExecution.Foreground.ExtendedExecutionForegroundSession'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.ExtendedExecution.Foreground.ExtendedExecutionForegroundSession.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.ExtendedExecution.Foreground.ExtendedExecutionForegroundSession: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.ApplicationModel.ExtendedExecution.Foreground.IExtendedExecutionForegroundSession) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Description(self: win32more.Windows.ApplicationModel.ExtendedExecution.Foreground.IExtendedExecutionForegroundSession, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def add_Revoked(self: win32more.Windows.ApplicationModel.ExtendedExecution.Foreground.IExtendedExecutionForegroundSession, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Win32.System.WinRT.IInspectable, win32more.Windows.ApplicationModel.ExtendedExecution.Foreground.ExtendedExecutionForegroundRevokedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Revoked(self: win32more.Windows.ApplicationModel.ExtendedExecution.Foreground.IExtendedExecutionForegroundSession, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def RequestExtensionAsync(self: win32more.Windows.ApplicationModel.ExtendedExecution.Foreground.IExtendedExecutionForegroundSession) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.ExtendedExecution.Foreground.ExtendedExecutionForegroundResult]: ...
    @winrt_mixinmethod
    def get_Reason(self: win32more.Windows.ApplicationModel.ExtendedExecution.Foreground.IExtendedExecutionForegroundSession) -> win32more.Windows.ApplicationModel.ExtendedExecution.Foreground.ExtendedExecutionForegroundReason: ...
    @winrt_mixinmethod
    def put_Reason(self: win32more.Windows.ApplicationModel.ExtendedExecution.Foreground.IExtendedExecutionForegroundSession, value: win32more.Windows.ApplicationModel.ExtendedExecution.Foreground.ExtendedExecutionForegroundReason) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    Description = property(get_Description, put_Description)
    Reason = property(get_Reason, put_Reason)
    Revoked = event()
class IExtendedExecutionForegroundRevokedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ExtendedExecution.Foreground.IExtendedExecutionForegroundRevokedEventArgs'
    _iid_ = Guid('{b07cd940-9557-aea4-2c99-bdd56d9be461}')
    @winrt_commethod(6)
    def get_Reason(self) -> win32more.Windows.ApplicationModel.ExtendedExecution.Foreground.ExtendedExecutionForegroundRevokedReason: ...
    Reason = property(get_Reason, None)
class IExtendedExecutionForegroundSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Windows.ApplicationModel.ExtendedExecution.Foreground.IExtendedExecutionForegroundSession'
    _iid_ = Guid('{fbf440e1-9d10-4201-b01e-c83275296f2e}')
    @winrt_commethod(6)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Description(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def add_Revoked(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Win32.System.WinRT.IInspectable, win32more.Windows.ApplicationModel.ExtendedExecution.Foreground.ExtendedExecutionForegroundRevokedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_Revoked(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def RequestExtensionAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.ExtendedExecution.Foreground.ExtendedExecutionForegroundResult]: ...
    @winrt_commethod(11)
    def get_Reason(self) -> win32more.Windows.ApplicationModel.ExtendedExecution.Foreground.ExtendedExecutionForegroundReason: ...
    @winrt_commethod(12)
    def put_Reason(self, value: win32more.Windows.ApplicationModel.ExtendedExecution.Foreground.ExtendedExecutionForegroundReason) -> Void: ...
    Description = property(get_Description, put_Description)
    Reason = property(get_Reason, put_Reason)
    Revoked = event()


make_ready(__name__)
