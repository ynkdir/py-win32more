from __future__ import annotations
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
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, winrt_overload, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation
import win32more.Windows.Perception.Automation.Core
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
