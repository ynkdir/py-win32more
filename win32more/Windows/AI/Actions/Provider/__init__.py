from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, FlexibleArray, Guid, Int16, Int32, Int64, IntPtr, NativeBitfieldAttribute, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.AI.Actions
import win32more.Windows.AI.Actions.Provider
import win32more.Windows.Foundation
import win32more.Windows.Win32.System.WinRT
class IActionFeedbackHandler(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.Actions.Provider.IActionFeedbackHandler'
    _iid_ = Guid('{a3fc3c51-a8c6-52c8-ad77-37bf3e2b565c}')
    @winrt_commethod(6)
    def ProcessFeedbackAsync(self, context: win32more.Windows.AI.Actions.ActionInvocationContext, feedback: win32more.Windows.AI.Actions.ActionFeedback) -> win32more.Windows.Foundation.IAsyncAction: ...
class IActionProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.Actions.Provider.IActionProvider'
    _iid_ = Guid('{62906c47-3d07-55f1-aefa-1522505afbbe}')
    @winrt_commethod(6)
    def InvokeAsync(self, context: win32more.Windows.AI.Actions.ActionInvocationContext) -> win32more.Windows.Foundation.IAsyncAction: ...


make_ready(__name__)
