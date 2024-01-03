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
import win32more.Windows.Phone.Speech.Recognition
SpeechRecognitionUIStatus = Int32
SpeechRecognitionUIStatus_Succeeded: SpeechRecognitionUIStatus = 0
SpeechRecognitionUIStatus_Busy: SpeechRecognitionUIStatus = 1
SpeechRecognitionUIStatus_Cancelled: SpeechRecognitionUIStatus = 2
SpeechRecognitionUIStatus_Preempted: SpeechRecognitionUIStatus = 3
SpeechRecognitionUIStatus_PrivacyPolicyDeclined: SpeechRecognitionUIStatus = 4


make_ready(__name__)
