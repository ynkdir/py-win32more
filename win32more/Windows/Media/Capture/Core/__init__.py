from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
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
import win32more.Windows.Media.Capture
import win32more.Windows.Media.Capture.Core
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IVariablePhotoCapturedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.Core.IVariablePhotoCapturedEventArgs'
    _iid_ = Guid('{d1eb4c5c-1b53-4e4a-8b5c-db7887ac949b}')
    @winrt_commethod(6)
    def get_Frame(self) -> win32more.Windows.Media.Capture.CapturedFrame: ...
    @winrt_commethod(7)
    def get_CaptureTimeOffset(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(8)
    def get_UsedFrameControllerIndex(self) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(9)
    def get_CapturedFrameControlValues(self) -> win32more.Windows.Media.Capture.CapturedFrameControlValues: ...
    Frame = property(get_Frame, None)
    CaptureTimeOffset = property(get_CaptureTimeOffset, None)
    UsedFrameControllerIndex = property(get_UsedFrameControllerIndex, None)
    CapturedFrameControlValues = property(get_CapturedFrameControlValues, None)
class IVariablePhotoSequenceCapture(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.Core.IVariablePhotoSequenceCapture'
    _iid_ = Guid('{d0112d1d-031e-4041-a6d6-bd742476a8ee}')
    @winrt_commethod(6)
    def StartAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def StopAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def FinishAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def add_PhotoCaptured(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.Core.VariablePhotoSequenceCapture, win32more.Windows.Media.Capture.Core.VariablePhotoCapturedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_PhotoCaptured(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_Stopped(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.Core.VariablePhotoSequenceCapture, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_Stopped(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class IVariablePhotoSequenceCapture2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Capture.Core.IVariablePhotoSequenceCapture2'
    _iid_ = Guid('{fe2c62bc-50b0-43e3-917c-e3b92798942f}')
    @winrt_commethod(6)
    def UpdateSettingsAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
class VariablePhotoCapturedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.Core.IVariablePhotoCapturedEventArgs
    _classid_ = 'Windows.Media.Capture.Core.VariablePhotoCapturedEventArgs'
    @winrt_mixinmethod
    def get_Frame(self: win32more.Windows.Media.Capture.Core.IVariablePhotoCapturedEventArgs) -> win32more.Windows.Media.Capture.CapturedFrame: ...
    @winrt_mixinmethod
    def get_CaptureTimeOffset(self: win32more.Windows.Media.Capture.Core.IVariablePhotoCapturedEventArgs) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_UsedFrameControllerIndex(self: win32more.Windows.Media.Capture.Core.IVariablePhotoCapturedEventArgs) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def get_CapturedFrameControlValues(self: win32more.Windows.Media.Capture.Core.IVariablePhotoCapturedEventArgs) -> win32more.Windows.Media.Capture.CapturedFrameControlValues: ...
    Frame = property(get_Frame, None)
    CaptureTimeOffset = property(get_CaptureTimeOffset, None)
    UsedFrameControllerIndex = property(get_UsedFrameControllerIndex, None)
    CapturedFrameControlValues = property(get_CapturedFrameControlValues, None)
class VariablePhotoSequenceCapture(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Capture.Core.IVariablePhotoSequenceCapture
    _classid_ = 'Windows.Media.Capture.Core.VariablePhotoSequenceCapture'
    @winrt_mixinmethod
    def StartAsync(self: win32more.Windows.Media.Capture.Core.IVariablePhotoSequenceCapture) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def StopAsync(self: win32more.Windows.Media.Capture.Core.IVariablePhotoSequenceCapture) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def FinishAsync(self: win32more.Windows.Media.Capture.Core.IVariablePhotoSequenceCapture) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def add_PhotoCaptured(self: win32more.Windows.Media.Capture.Core.IVariablePhotoSequenceCapture, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.Core.VariablePhotoSequenceCapture, win32more.Windows.Media.Capture.Core.VariablePhotoCapturedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PhotoCaptured(self: win32more.Windows.Media.Capture.Core.IVariablePhotoSequenceCapture, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Stopped(self: win32more.Windows.Media.Capture.Core.IVariablePhotoSequenceCapture, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.Core.VariablePhotoSequenceCapture, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Stopped(self: win32more.Windows.Media.Capture.Core.IVariablePhotoSequenceCapture, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def UpdateSettingsAsync(self: win32more.Windows.Media.Capture.Core.IVariablePhotoSequenceCapture2) -> win32more.Windows.Foundation.IAsyncAction: ...
make_head(_module, 'IVariablePhotoCapturedEventArgs')
make_head(_module, 'IVariablePhotoSequenceCapture')
make_head(_module, 'IVariablePhotoSequenceCapture2')
make_head(_module, 'VariablePhotoCapturedEventArgs')
make_head(_module, 'VariablePhotoSequenceCapture')
