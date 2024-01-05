from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import Annotated, Generic, K, MulticastDelegate, SZArray, T, TProgress, TResult, TSender, V, WinRT_String, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Phone.Speech.Recognition
SpeechRecognitionUIStatus = Int32
SpeechRecognitionUIStatus_Succeeded: SpeechRecognitionUIStatus = 0
SpeechRecognitionUIStatus_Busy: SpeechRecognitionUIStatus = 1
SpeechRecognitionUIStatus_Cancelled: SpeechRecognitionUIStatus = 2
SpeechRecognitionUIStatus_Preempted: SpeechRecognitionUIStatus = 3
SpeechRecognitionUIStatus_PrivacyPolicyDeclined: SpeechRecognitionUIStatus = 4


make_ready(__name__)
