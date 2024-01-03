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
import win32more.Windows.Media.Render
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


make_ready(__name__)
