from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.Media.Render
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
AudioRenderCategory = Int32
AudioRenderCategory_Other: AudioRenderCategory = 0
AudioRenderCategory_ForegroundOnlyMedia: AudioRenderCategory = 1
AudioRenderCategory_BackgroundCapableMedia: AudioRenderCategory = 2
AudioRenderCategory_Communications: AudioRenderCategory = 3
AudioRenderCategory_Alerts: AudioRenderCategory = 4
AudioRenderCategory_SoundEffects: AudioRenderCategory = 5
AudioRenderCategory_GameEffects: AudioRenderCategory = 6
AudioRenderCategory_GameMedia: AudioRenderCategory = 7
AudioRenderCategory_GameChat: AudioRenderCategory = 8
AudioRenderCategory_Speech: AudioRenderCategory = 9
AudioRenderCategory_Movie: AudioRenderCategory = 10
AudioRenderCategory_Media: AudioRenderCategory = 11
