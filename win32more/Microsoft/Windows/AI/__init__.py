from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, FlexibleArray, Guid, Int16, Int32, Int64, IntPtr, NativeBitfieldAttribute, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Microsoft.Windows.AI
import win32more.Windows.Foundation
import win32more.Windows.Win32.System.WinRT
AIFeatureReadyContract: UInt32 = 65536
class AIFeatureReadyResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.AI.IAIFeatureReadyResult
    _classid_ = 'Microsoft.Windows.AI.AIFeatureReadyResult'
    @winrt_mixinmethod
    def get_Error(self: win32more.Microsoft.Windows.AI.IAIFeatureReadyResult) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_ErrorDisplayText(self: win32more.Microsoft.Windows.AI.IAIFeatureReadyResult) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Microsoft.Windows.AI.IAIFeatureReadyResult) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Microsoft.Windows.AI.IAIFeatureReadyResult) -> win32more.Microsoft.Windows.AI.AIFeatureReadyResultState: ...
    Error = property(get_Error, None)
    ErrorDisplayText = property(get_ErrorDisplayText, None)
    ExtendedError = property(get_ExtendedError, None)
    Status = property(get_Status, None)
class AIFeatureReadyResultState(Enum, Int32):
    InProgress = 0
    Success = 1
    Failure = 2
class AIFeatureReadyState(Enum, Int32):
    Ready = 0
    NotReady = 1
    NotSupportedOnCurrentSystem = 2
    DisabledByUser = 3
class IAIFeatureReadyResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.AI.IAIFeatureReadyResult'
    _iid_ = Guid('{936a78a6-c242-5937-9814-e512d4193a6d}')
    @winrt_commethod(6)
    def get_Error(self) -> win32more.Windows.Foundation.HResult: ...
    @winrt_commethod(7)
    def get_ErrorDisplayText(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    @winrt_commethod(9)
    def get_Status(self) -> win32more.Microsoft.Windows.AI.AIFeatureReadyResultState: ...
    Error = property(get_Error, None)
    ErrorDisplayText = property(get_ErrorDisplayText, None)
    ExtendedError = property(get_ExtendedError, None)
    Status = property(get_Status, None)


make_ready(__name__)
