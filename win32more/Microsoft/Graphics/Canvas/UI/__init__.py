from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Microsoft.Graphics.Canvas.UI
import win32more.Windows.Foundation
import win32more.Windows.Win32.System.WinRT
class CanvasCreateResourcesEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Graphics.Canvas.UI.ICanvasCreateResourcesEventArgs
    _classid_ = 'Microsoft.Graphics.Canvas.UI.CanvasCreateResourcesEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.Graphics.Canvas.UI.CanvasCreateResourcesEventArgs.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Microsoft.Graphics.Canvas.UI.ICanvasCreateResourcesEventArgsFactory, createResourcesReason: win32more.Microsoft.Graphics.Canvas.UI.CanvasCreateResourcesReason) -> win32more.Microsoft.Graphics.Canvas.UI.CanvasCreateResourcesEventArgs: ...
    @winrt_mixinmethod
    def get_Reason(self: win32more.Microsoft.Graphics.Canvas.UI.ICanvasCreateResourcesEventArgs) -> win32more.Microsoft.Graphics.Canvas.UI.CanvasCreateResourcesReason: ...
    @winrt_mixinmethod
    def TrackAsyncAction(self: win32more.Microsoft.Graphics.Canvas.UI.ICanvasCreateResourcesEventArgs, action: win32more.Windows.Foundation.IAsyncAction) -> Void: ...
    @winrt_mixinmethod
    def GetTrackedAction(self: win32more.Microsoft.Graphics.Canvas.UI.ICanvasCreateResourcesEventArgs) -> win32more.Windows.Foundation.IAsyncAction: ...
    Reason = property(get_Reason, None)
class CanvasCreateResourcesReason(Enum, Int32):
    FirstTime = 0
    NewDevice = 1
    DpiChanged = 2
class CanvasTimingInformation(Structure):
    UpdateCount: Int64
    TotalTime: win32more.Windows.Foundation.TimeSpan
    ElapsedTime: win32more.Windows.Foundation.TimeSpan
    IsRunningSlowly: Boolean
class ICanvasCreateResourcesEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Graphics.Canvas.UI.ICanvasCreateResourcesEventArgs'
    _iid_ = Guid('{edc52108-f6ba-4a09-9fa3-10c97a24e49a}')
    @winrt_commethod(6)
    def get_Reason(self) -> win32more.Microsoft.Graphics.Canvas.UI.CanvasCreateResourcesReason: ...
    @winrt_commethod(7)
    def TrackAsyncAction(self, action: win32more.Windows.Foundation.IAsyncAction) -> Void: ...
    @winrt_commethod(8)
    def GetTrackedAction(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    Reason = property(get_Reason, None)
class ICanvasCreateResourcesEventArgsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Graphics.Canvas.UI.ICanvasCreateResourcesEventArgsFactory'
    _iid_ = Guid('{3a21c766-0781-4389-bbc3-86b1f5022af1}')
    @winrt_commethod(6)
    def Create(self, createResourcesReason: win32more.Microsoft.Graphics.Canvas.UI.CanvasCreateResourcesReason) -> win32more.Microsoft.Graphics.Canvas.UI.CanvasCreateResourcesEventArgs: ...


make_ready(__name__)
