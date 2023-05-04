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
import Windows.ApplicationModel.ExtendedExecution
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
ExtendedExecutionReason = Int32
ExtendedExecutionReason_Unspecified: ExtendedExecutionReason = 0
ExtendedExecutionReason_LocationTracking: ExtendedExecutionReason = 1
ExtendedExecutionReason_SavingData: ExtendedExecutionReason = 2
ExtendedExecutionResult = Int32
ExtendedExecutionResult_Allowed: ExtendedExecutionResult = 0
ExtendedExecutionResult_Denied: ExtendedExecutionResult = 1
class ExtendedExecutionRevokedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.ExtendedExecution.IExtendedExecutionRevokedEventArgs
    _classid_ = 'Windows.ApplicationModel.ExtendedExecution.ExtendedExecutionRevokedEventArgs'
    @winrt_mixinmethod
    def get_Reason(self: Windows.ApplicationModel.ExtendedExecution.IExtendedExecutionRevokedEventArgs) -> Windows.ApplicationModel.ExtendedExecution.ExtendedExecutionRevokedReason: ...
    Reason = property(get_Reason, None)
ExtendedExecutionRevokedReason = Int32
ExtendedExecutionRevokedReason_Resumed: ExtendedExecutionRevokedReason = 0
ExtendedExecutionRevokedReason_SystemPolicy: ExtendedExecutionRevokedReason = 1
class ExtendedExecutionSession(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.ExtendedExecution.IExtendedExecutionSession
    _classid_ = 'Windows.ApplicationModel.ExtendedExecution.ExtendedExecutionSession'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.ExtendedExecution.ExtendedExecutionSession: ...
    @winrt_mixinmethod
    def get_Reason(self: Windows.ApplicationModel.ExtendedExecution.IExtendedExecutionSession) -> Windows.ApplicationModel.ExtendedExecution.ExtendedExecutionReason: ...
    @winrt_mixinmethod
    def put_Reason(self: Windows.ApplicationModel.ExtendedExecution.IExtendedExecutionSession, value: Windows.ApplicationModel.ExtendedExecution.ExtendedExecutionReason) -> Void: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.ApplicationModel.ExtendedExecution.IExtendedExecutionSession) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Description(self: Windows.ApplicationModel.ExtendedExecution.IExtendedExecutionSession, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_PercentProgress(self: Windows.ApplicationModel.ExtendedExecution.IExtendedExecutionSession) -> UInt32: ...
    @winrt_mixinmethod
    def put_PercentProgress(self: Windows.ApplicationModel.ExtendedExecution.IExtendedExecutionSession, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def add_Revoked(self: Windows.ApplicationModel.ExtendedExecution.IExtendedExecutionSession, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.ApplicationModel.ExtendedExecution.ExtendedExecutionRevokedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Revoked(self: Windows.ApplicationModel.ExtendedExecution.IExtendedExecutionSession, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def RequestExtensionAsync(self: Windows.ApplicationModel.ExtendedExecution.IExtendedExecutionSession) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.ExtendedExecution.ExtendedExecutionResult]: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    Reason = property(get_Reason, put_Reason)
    Description = property(get_Description, put_Description)
    PercentProgress = property(get_PercentProgress, put_PercentProgress)
class IExtendedExecutionRevokedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ExtendedExecution.IExtendedExecutionRevokedEventArgs'
    _iid_ = Guid('{bfbc9f16-63b5-4c0b-aad6-828af5373ec3}')
    @winrt_commethod(6)
    def get_Reason(self) -> Windows.ApplicationModel.ExtendedExecution.ExtendedExecutionRevokedReason: ...
    Reason = property(get_Reason, None)
class IExtendedExecutionSession(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.ExtendedExecution.IExtendedExecutionSession'
    _iid_ = Guid('{af908a2d-118b-48f1-9308-0c4fc41e200f}')
    @winrt_commethod(6)
    def get_Reason(self) -> Windows.ApplicationModel.ExtendedExecution.ExtendedExecutionReason: ...
    @winrt_commethod(7)
    def put_Reason(self, value: Windows.ApplicationModel.ExtendedExecution.ExtendedExecutionReason) -> Void: ...
    @winrt_commethod(8)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Description(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_PercentProgress(self) -> UInt32: ...
    @winrt_commethod(11)
    def put_PercentProgress(self, value: UInt32) -> Void: ...
    @winrt_commethod(12)
    def add_Revoked(self, handler: Windows.Foundation.TypedEventHandler[Windows.Win32.System.WinRT.IInspectable_head, Windows.ApplicationModel.ExtendedExecution.ExtendedExecutionRevokedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_Revoked(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def RequestExtensionAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.ExtendedExecution.ExtendedExecutionResult]: ...
    Reason = property(get_Reason, put_Reason)
    Description = property(get_Description, put_Description)
    PercentProgress = property(get_PercentProgress, put_PercentProgress)
make_head(_module, 'ExtendedExecutionRevokedEventArgs')
make_head(_module, 'ExtendedExecutionSession')
make_head(_module, 'IExtendedExecutionRevokedEventArgs')
make_head(_module, 'IExtendedExecutionSession')
