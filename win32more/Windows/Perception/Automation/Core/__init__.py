from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Perception.Automation.Core
import win32more.Windows.Win32.System.WinRT
class CorePerceptionAutomation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Automation.Core.CorePerceptionAutomation'
    @winrt_classmethod
    def SetActivationFactoryProvider(cls: win32more.Windows.Perception.Automation.Core.ICorePerceptionAutomationStatics, provider: win32more.Windows.Foundation.IGetActivationFactory) -> Void: ...
class ICorePerceptionAutomationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Automation.Core.ICorePerceptionAutomationStatics'
    _iid_ = Guid('{0bb04541-4ce2-4923-9a76-8187ecc59112}')
    @winrt_commethod(6)
    def SetActivationFactoryProvider(self, provider: win32more.Windows.Foundation.IGetActivationFactory) -> Void: ...
PerceptionAutomationCoreContract: UInt32 = 65536


make_ready(__name__)
