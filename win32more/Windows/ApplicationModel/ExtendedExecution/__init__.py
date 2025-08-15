from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Windows.ApplicationModel.ExtendedExecution
import win32more.Windows.Foundation
class ExtendedExecutionReason(Enum, Int32):
    Unspecified = 0
    LocationTracking = 1
    SavingData = 2
class ExtendedExecutionResult(Enum, Int32):
    Allowed = 0
    Denied = 1
class ExtendedExecutionRevokedEventArgs(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.ApplicationModel.ExtendedExecution.IExtendedExecutionRevokedEventArgs
    _classid_ = 'Windows.ApplicationModel.ExtendedExecution.ExtendedExecutionRevokedEventArgs'
    @winrt_mixinmethod
    def get_Reason(self: win32more.Windows.ApplicationModel.ExtendedExecution.IExtendedExecutionRevokedEventArgs) -> win32more.Windows.ApplicationModel.ExtendedExecution.ExtendedExecutionRevokedReason: ...
    Reason = property(get_Reason, None)
class ExtendedExecutionRevokedReason(Enum, Int32):
    Resumed = 0
    SystemPolicy = 1
class ExtendedExecutionSession(ComPtr):
    extends: IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.ApplicationModel.ExtendedExecution.IExtendedExecutionSession
    _classid_ = 'Windows.ApplicationModel.ExtendedExecution.ExtendedExecutionSession'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.ExtendedExecution.ExtendedExecutionSession.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.ExtendedExecution.ExtendedExecutionSession: ...
    @winrt_mixinmethod
    def get_Reason(self: win32more.Windows.ApplicationModel.ExtendedExecution.IExtendedExecutionSession) -> win32more.Windows.ApplicationModel.ExtendedExecution.ExtendedExecutionReason: ...
    @winrt_mixinmethod
    def put_Reason(self: win32more.Windows.ApplicationModel.ExtendedExecution.IExtendedExecutionSession, value: win32more.Windows.ApplicationModel.ExtendedExecution.ExtendedExecutionReason) -> Void: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.ApplicationModel.ExtendedExecution.IExtendedExecutionSession) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Description(self: win32more.Windows.ApplicationModel.ExtendedExecution.IExtendedExecutionSession, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_PercentProgress(self: win32more.Windows.ApplicationModel.ExtendedExecution.IExtendedExecutionSession) -> UInt32: ...
    @winrt_mixinmethod
    def put_PercentProgress(self: win32more.Windows.ApplicationModel.ExtendedExecution.IExtendedExecutionSession, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def add_Revoked(self: win32more.Windows.ApplicationModel.ExtendedExecution.IExtendedExecutionSession, handler: win32more.Windows.Foundation.TypedEventHandler[IInspectable, win32more.Windows.ApplicationModel.ExtendedExecution.ExtendedExecutionRevokedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Revoked(self: win32more.Windows.ApplicationModel.ExtendedExecution.IExtendedExecutionSession, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def RequestExtensionAsync(self: win32more.Windows.ApplicationModel.ExtendedExecution.IExtendedExecutionSession) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.ExtendedExecution.ExtendedExecutionResult]: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    Description = property(get_Description, put_Description)
    PercentProgress = property(get_PercentProgress, put_PercentProgress)
    Reason = property(get_Reason, put_Reason)
    Revoked = event()
class IExtendedExecutionRevokedEventArgs(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.ApplicationModel.ExtendedExecution.IExtendedExecutionRevokedEventArgs'
    _iid_ = Guid('{bfbc9f16-63b5-4c0b-aad6-828af5373ec3}')
    @winrt_commethod(6)
    def get_Reason(self) -> win32more.Windows.ApplicationModel.ExtendedExecution.ExtendedExecutionRevokedReason: ...
    Reason = property(get_Reason, None)
class IExtendedExecutionSession(ComPtr):
    extends: IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Windows.ApplicationModel.ExtendedExecution.IExtendedExecutionSession'
    _iid_ = Guid('{af908a2d-118b-48f1-9308-0c4fc41e200f}')
    @winrt_commethod(6)
    def get_Reason(self) -> win32more.Windows.ApplicationModel.ExtendedExecution.ExtendedExecutionReason: ...
    @winrt_commethod(7)
    def put_Reason(self, value: win32more.Windows.ApplicationModel.ExtendedExecution.ExtendedExecutionReason) -> Void: ...
    @winrt_commethod(8)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Description(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_PercentProgress(self) -> UInt32: ...
    @winrt_commethod(11)
    def put_PercentProgress(self, value: UInt32) -> Void: ...
    @winrt_commethod(12)
    def add_Revoked(self, handler: win32more.Windows.Foundation.TypedEventHandler[IInspectable, win32more.Windows.ApplicationModel.ExtendedExecution.ExtendedExecutionRevokedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_Revoked(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def RequestExtensionAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.ExtendedExecution.ExtendedExecutionResult]: ...
    Description = property(get_Description, put_Description)
    PercentProgress = property(get_PercentProgress, put_PercentProgress)
    Reason = property(get_Reason, put_Reason)
    Revoked = event()


make_ready(__name__)
