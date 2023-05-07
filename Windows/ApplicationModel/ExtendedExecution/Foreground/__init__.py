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
import Windows.ApplicationModel.ExtendedExecution.Foreground
import Windows.Foundation
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
ExtendedExecutionForegroundReason = Int32
ExtendedExecutionForegroundReason_Unspecified: ExtendedExecutionForegroundReason = 0
ExtendedExecutionForegroundReason_SavingData: ExtendedExecutionForegroundReason = 1
ExtendedExecutionForegroundReason_BackgroundAudio: ExtendedExecutionForegroundReason = 2
ExtendedExecutionForegroundReason_Unconstrained: ExtendedExecutionForegroundReason = 3
ExtendedExecutionForegroundResult = Int32
ExtendedExecutionForegroundResult_Allowed: ExtendedExecutionForegroundResult = 0
ExtendedExecutionForegroundResult_Denied: ExtendedExecutionForegroundResult = 1
class ExtendedExecutionForegroundRevokedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.ExtendedExecution.Foreground.IExtendedExecutionForegroundRevokedEventArgs
    _classid_ = 'Windows.ApplicationModel.ExtendedExecution.Foreground.ExtendedExecutionForegroundRevokedEventArgs'
    @winrt_mixinmethod
    def get_Reason(self: Windows.ApplicationModel.ExtendedExecution.Foreground.IExtendedExecutionForegroundRevokedEventArgs) -> Windows.ApplicationModel.ExtendedExecution.Foreground.ExtendedExecutionForegroundRevokedReason: ...
    Reason = property(get_Reason, None)
ExtendedExecutionForegroundRevokedReason = Int32
ExtendedExecutionForegroundRevokedReason_Resumed: ExtendedExecutionForegroundRevokedReason = 0
ExtendedExecutionForegroundRevokedReason_SystemPolicy: ExtendedExecutionForegroundRevokedReason = 1
class ExtendedExecutionForegroundSession(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.ExtendedExecution.Foreground.IExtendedExecutionForegroundSession
    _classid_ = 'Windows.ApplicationModel.ExtendedExecution.Foreground.ExtendedExecutionForegroundSession'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.ExtendedExecution.Foreground.ExtendedExecutionForegroundSession: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.ApplicationModel.ExtendedExecution.Foreground.IExtendedExecutionForegroundSession) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Description(self: Windows.ApplicationModel.ExtendedExecution.Foreground.IExtendedExecutionForegroundSession, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def add_Revoked(self: Windows.ApplicationModel.ExtendedExecution.Foreground.IExtendedExecutionForegroundSession, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.ApplicationModel.ExtendedExecution.Foreground.ExtendedExecutionForegroundRevokedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Revoked(self: Windows.ApplicationModel.ExtendedExecution.Foreground.IExtendedExecutionForegroundSession, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def RequestExtensionAsync(self: Windows.ApplicationModel.ExtendedExecution.Foreground.IExtendedExecutionForegroundSession) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.ExtendedExecution.Foreground.ExtendedExecutionForegroundResult]: ...
    @winrt_mixinmethod
    def get_Reason(self: Windows.ApplicationModel.ExtendedExecution.Foreground.IExtendedExecutionForegroundSession) -> Windows.ApplicationModel.ExtendedExecution.Foreground.ExtendedExecutionForegroundReason: ...
    @winrt_mixinmethod
    def put_Reason(self: Windows.ApplicationModel.ExtendedExecution.Foreground.IExtendedExecutionForegroundSession, value: Windows.ApplicationModel.ExtendedExecution.Foreground.ExtendedExecutionForegroundReason) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    Description = property(get_Description, put_Description)
    Reason = property(get_Reason, put_Reason)
class IExtendedExecutionForegroundRevokedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ExtendedExecution.Foreground.IExtendedExecutionForegroundRevokedEventArgs'
    _iid_ = Guid('{b07cd940-9557-aea4-2c99-bdd56d9be461}')
    @winrt_commethod(6)
    def get_Reason(self: Windows.ApplicationModel.ExtendedExecution.Foreground.IExtendedExecutionForegroundRevokedEventArgs) -> Windows.ApplicationModel.ExtendedExecution.Foreground.ExtendedExecutionForegroundRevokedReason: ...
    Reason = property(get_Reason, None)
class IExtendedExecutionForegroundSession(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ExtendedExecution.Foreground.IExtendedExecutionForegroundSession'
    _iid_ = Guid('{fbf440e1-9d10-4201-b01e-c83275296f2e}')
    @winrt_commethod(6)
    def get_Description(self: Windows.ApplicationModel.ExtendedExecution.Foreground.IExtendedExecutionForegroundSession) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Description(self: Windows.ApplicationModel.ExtendedExecution.Foreground.IExtendedExecutionForegroundSession, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def add_Revoked(self: Windows.ApplicationModel.ExtendedExecution.Foreground.IExtendedExecutionForegroundSession, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.ApplicationModel.ExtendedExecution.Foreground.ExtendedExecutionForegroundRevokedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_Revoked(self: Windows.ApplicationModel.ExtendedExecution.Foreground.IExtendedExecutionForegroundSession, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def RequestExtensionAsync(self: Windows.ApplicationModel.ExtendedExecution.Foreground.IExtendedExecutionForegroundSession) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.ExtendedExecution.Foreground.ExtendedExecutionForegroundResult]: ...
    @winrt_commethod(11)
    def get_Reason(self: Windows.ApplicationModel.ExtendedExecution.Foreground.IExtendedExecutionForegroundSession) -> Windows.ApplicationModel.ExtendedExecution.Foreground.ExtendedExecutionForegroundReason: ...
    @winrt_commethod(12)
    def put_Reason(self: Windows.ApplicationModel.ExtendedExecution.Foreground.IExtendedExecutionForegroundSession, value: Windows.ApplicationModel.ExtendedExecution.Foreground.ExtendedExecutionForegroundReason) -> Void: ...
    Description = property(get_Description, put_Description)
    Reason = property(get_Reason, put_Reason)
make_head(_module, 'ExtendedExecutionForegroundRevokedEventArgs')
make_head(_module, 'ExtendedExecutionForegroundSession')
make_head(_module, 'IExtendedExecutionForegroundRevokedEventArgs')
make_head(_module, 'IExtendedExecutionForegroundSession')
