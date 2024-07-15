from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Media.Capture
import win32more.Windows.Media.Capture.Core
import win32more.Windows.Win32.System.WinRT
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
    CaptureTimeOffset = property(get_CaptureTimeOffset, None)
    CapturedFrameControlValues = property(get_CapturedFrameControlValues, None)
    Frame = property(get_Frame, None)
    UsedFrameControllerIndex = property(get_UsedFrameControllerIndex, None)
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
    def add_Stopped(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.Core.VariablePhotoSequenceCapture, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_Stopped(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    PhotoCaptured = event()
    Stopped = event()
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
    CaptureTimeOffset = property(get_CaptureTimeOffset, None)
    CapturedFrameControlValues = property(get_CapturedFrameControlValues, None)
    Frame = property(get_Frame, None)
    UsedFrameControllerIndex = property(get_UsedFrameControllerIndex, None)
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
    def add_Stopped(self: win32more.Windows.Media.Capture.Core.IVariablePhotoSequenceCapture, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Capture.Core.VariablePhotoSequenceCapture, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Stopped(self: win32more.Windows.Media.Capture.Core.IVariablePhotoSequenceCapture, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def UpdateSettingsAsync(self: win32more.Windows.Media.Capture.Core.IVariablePhotoSequenceCapture2) -> win32more.Windows.Foundation.IAsyncAction: ...
    PhotoCaptured = event()
    Stopped = event()


make_ready(__name__)
