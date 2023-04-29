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
import Windows.Media
import Windows.Media.Core.Preview
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class ISoundLevelBrokerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6a633961-dbed-464c-a0-9a-33-41-2f-5c-aa-3f')
    @winrt_commethod(6)
    def get_SoundLevel(self) -> Windows.Media.SoundLevel: ...
    @winrt_commethod(7)
    def add_SoundLevelChanged(self, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_SoundLevelChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    SoundLevel = property(get_SoundLevel, None)
class SoundLevelBroker(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Core.Preview.SoundLevelBroker'
    @winrt_classmethod
    def get_SoundLevel(cls: Windows.Media.Core.Preview.ISoundLevelBrokerStatics) -> Windows.Media.SoundLevel: ...
    @winrt_classmethod
    def add_SoundLevelChanged(cls: Windows.Media.Core.Preview.ISoundLevelBrokerStatics, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_SoundLevelChanged(cls: Windows.Media.Core.Preview.ISoundLevelBrokerStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    SoundLevel = property(get_SoundLevel, None)
make_head(_module, 'ISoundLevelBrokerStatics')
make_head(_module, 'SoundLevelBroker')
