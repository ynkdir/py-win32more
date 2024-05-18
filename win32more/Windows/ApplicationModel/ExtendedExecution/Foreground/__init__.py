from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import FillArray, Generic, K, MulticastDelegate, PassArray, ReceiveArray, T, TProgress, TResult, TSender, V, WinRT_String, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel.ExtendedExecution.Foreground
import win32more.Windows.Foundation
import win32more.Windows.Win32.System.WinRT
class ExtendedExecutionForegroundReason(Int32):  # enum
    Unspecified = 0
    SavingData = 1
    BackgroundAudio = 2
    Unconstrained = 3
class ExtendedExecutionForegroundResult(Int32):  # enum
    Allowed = 0
    Denied = 1
class ExtendedExecutionForegroundRevokedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.ExtendedExecution.Foreground.IExtendedExecutionForegroundRevokedEventArgs
    _classid_ = 'Windows.ApplicationModel.ExtendedExecution.Foreground.ExtendedExecutionForegroundRevokedEventArgs'
    @winrt_mixinmethod
    def get_Reason(self: win32more.Windows.ApplicationModel.ExtendedExecution.Foreground.IExtendedExecutionForegroundRevokedEventArgs) -> win32more.Windows.ApplicationModel.ExtendedExecution.Foreground.ExtendedExecutionForegroundRevokedReason: ...
    Reason = property(get_Reason, None)
class ExtendedExecutionForegroundRevokedReason(Int32):  # enum
    Resumed = 0
    SystemPolicy = 1
class ExtendedExecutionForegroundSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.ExtendedExecution.Foreground.IExtendedExecutionForegroundSession
    _classid_ = 'Windows.ApplicationModel.ExtendedExecution.Foreground.ExtendedExecutionForegroundSession'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 0:
            return win32more.Windows.ApplicationModel.ExtendedExecution.Foreground.ExtendedExecutionForegroundSession.CreateInstance(*args)
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
class IExtendedExecutionForegroundRevokedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ExtendedExecution.Foreground.IExtendedExecutionForegroundRevokedEventArgs'
    _iid_ = Guid('{b07cd940-9557-aea4-2c99-bdd56d9be461}')
    @winrt_commethod(6)
    def get_Reason(self) -> win32more.Windows.ApplicationModel.ExtendedExecution.Foreground.ExtendedExecutionForegroundRevokedReason: ...
    Reason = property(get_Reason, None)
class IExtendedExecutionForegroundSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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


make_ready(__name__)
