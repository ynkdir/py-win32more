from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, WinRT_String, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.System.WinRT
import Windows.Foundation
import Windows.Media.Capture
import Windows.Media.Capture.Core
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IVariablePhotoCapturedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d1eb4c5c-1b53-4e4a-8b-5c-db-78-87-ac-94-9b')
    @winrt_commethod(6)
    def get_Frame(self) -> Windows.Media.Capture.CapturedFrame: ...
    @winrt_commethod(7)
    def get_CaptureTimeOffset(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(8)
    def get_UsedFrameControllerIndex(self) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(9)
    def get_CapturedFrameControlValues(self) -> Windows.Media.Capture.CapturedFrameControlValues: ...
    Frame = property(get_Frame, None)
    CaptureTimeOffset = property(get_CaptureTimeOffset, None)
    UsedFrameControllerIndex = property(get_UsedFrameControllerIndex, None)
    CapturedFrameControlValues = property(get_CapturedFrameControlValues, None)
class IVariablePhotoSequenceCapture(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d0112d1d-031e-4041-a6-d6-bd-74-24-76-a8-ee')
    @winrt_commethod(6)
    def StartAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def StopAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def FinishAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def add_PhotoCaptured(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Capture.Core.VariablePhotoSequenceCapture, Windows.Media.Capture.Core.VariablePhotoCapturedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_PhotoCaptured(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_Stopped(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Capture.Core.VariablePhotoSequenceCapture, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_Stopped(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IVariablePhotoSequenceCapture2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('fe2c62bc-50b0-43e3-91-7c-e3-b9-27-98-94-2f')
    @winrt_commethod(6)
    def UpdateSettingsAsync(self) -> Windows.Foundation.IAsyncAction: ...
class VariablePhotoCapturedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.Core.VariablePhotoCapturedEventArgs'
    @winrt_mixinmethod
    def get_Frame(self: Windows.Media.Capture.Core.IVariablePhotoCapturedEventArgs) -> Windows.Media.Capture.CapturedFrame: ...
    @winrt_mixinmethod
    def get_CaptureTimeOffset(self: Windows.Media.Capture.Core.IVariablePhotoCapturedEventArgs) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_UsedFrameControllerIndex(self: Windows.Media.Capture.Core.IVariablePhotoCapturedEventArgs) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def get_CapturedFrameControlValues(self: Windows.Media.Capture.Core.IVariablePhotoCapturedEventArgs) -> Windows.Media.Capture.CapturedFrameControlValues: ...
    Frame = property(get_Frame, None)
    CaptureTimeOffset = property(get_CaptureTimeOffset, None)
    UsedFrameControllerIndex = property(get_UsedFrameControllerIndex, None)
    CapturedFrameControlValues = property(get_CapturedFrameControlValues, None)
class VariablePhotoSequenceCapture(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Media.Capture.Core.VariablePhotoSequenceCapture'
    @winrt_mixinmethod
    def StartAsync(self: Windows.Media.Capture.Core.IVariablePhotoSequenceCapture) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def StopAsync(self: Windows.Media.Capture.Core.IVariablePhotoSequenceCapture) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def FinishAsync(self: Windows.Media.Capture.Core.IVariablePhotoSequenceCapture) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def add_PhotoCaptured(self: Windows.Media.Capture.Core.IVariablePhotoSequenceCapture, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Capture.Core.VariablePhotoSequenceCapture, Windows.Media.Capture.Core.VariablePhotoCapturedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PhotoCaptured(self: Windows.Media.Capture.Core.IVariablePhotoSequenceCapture, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Stopped(self: Windows.Media.Capture.Core.IVariablePhotoSequenceCapture, handler: Windows.Foundation.TypedEventHandler[Windows.Media.Capture.Core.VariablePhotoSequenceCapture, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Stopped(self: Windows.Media.Capture.Core.IVariablePhotoSequenceCapture, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def UpdateSettingsAsync(self: Windows.Media.Capture.Core.IVariablePhotoSequenceCapture2) -> Windows.Foundation.IAsyncAction: ...
make_head(_module, 'IVariablePhotoCapturedEventArgs')
make_head(_module, 'IVariablePhotoSequenceCapture')
make_head(_module, 'IVariablePhotoSequenceCapture2')
make_head(_module, 'VariablePhotoCapturedEventArgs')
make_head(_module, 'VariablePhotoSequenceCapture')
