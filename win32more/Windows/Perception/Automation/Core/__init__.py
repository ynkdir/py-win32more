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
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation
import win32more.Windows.Perception.Automation.Core
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
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
make_head(_module, 'CorePerceptionAutomation')
make_head(_module, 'ICorePerceptionAutomationStatics')
