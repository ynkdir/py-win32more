from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
import sys
from typing import Generic, TypeVar
if sys.version_info < (3, 9):
    from typing_extensions import Annotated
else:
    from typing import Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, EasyCastStructure, EasyCastUnion, ComPtr, make_ready
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.ApplicationModel.ExtendedExecution.Foreground
import win32more.Windows.Foundation
ExtendedExecutionForegroundReason = Int32
ExtendedExecutionForegroundReason_Unspecified: ExtendedExecutionForegroundReason = 0
ExtendedExecutionForegroundReason_SavingData: ExtendedExecutionForegroundReason = 1
ExtendedExecutionForegroundReason_BackgroundAudio: ExtendedExecutionForegroundReason = 2
ExtendedExecutionForegroundReason_Unconstrained: ExtendedExecutionForegroundReason = 3
ExtendedExecutionForegroundResult = Int32
ExtendedExecutionForegroundResult_Allowed: ExtendedExecutionForegroundResult = 0
ExtendedExecutionForegroundResult_Denied: ExtendedExecutionForegroundResult = 1
class ExtendedExecutionForegroundRevokedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.ExtendedExecution.Foreground.IExtendedExecutionForegroundRevokedEventArgs
    _classid_ = 'Windows.ApplicationModel.ExtendedExecution.Foreground.ExtendedExecutionForegroundRevokedEventArgs'
    @winrt_mixinmethod
    def get_Reason(self: win32more.Windows.ApplicationModel.ExtendedExecution.Foreground.IExtendedExecutionForegroundRevokedEventArgs) -> win32more.Windows.ApplicationModel.ExtendedExecution.Foreground.ExtendedExecutionForegroundRevokedReason: ...
    Reason = property(get_Reason, None)
ExtendedExecutionForegroundRevokedReason = Int32
ExtendedExecutionForegroundRevokedReason_Resumed: ExtendedExecutionForegroundRevokedReason = 0
ExtendedExecutionForegroundRevokedReason_SystemPolicy: ExtendedExecutionForegroundRevokedReason = 1
class ExtendedExecutionForegroundSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.ExtendedExecution.Foreground.IExtendedExecutionForegroundSession
    _classid_ = 'Windows.ApplicationModel.ExtendedExecution.Foreground.ExtendedExecutionForegroundSession'
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
