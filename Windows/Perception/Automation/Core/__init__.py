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
import Windows.Foundation
import Windows.Perception.Automation.Core
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.Automation.Core.CorePerceptionAutomation'
    @winrt_classmethod
    def SetActivationFactoryProvider(cls: Windows.Perception.Automation.Core.ICorePerceptionAutomationStatics, provider: Windows.Foundation.IGetActivationFactory) -> Void: ...
class ICorePerceptionAutomationStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('0bb04541-4ce2-4923-9a-76-81-87-ec-c5-91-12')
    @winrt_commethod(6)
    def SetActivationFactoryProvider(self, provider: Windows.Foundation.IGetActivationFactory) -> Void: ...
PerceptionAutomationCoreContract: UInt32 = 65536
make_head(_module, 'CorePerceptionAutomation')
make_head(_module, 'ICorePerceptionAutomationStatics')
