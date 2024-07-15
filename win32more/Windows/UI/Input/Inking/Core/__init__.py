from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Foundation.Numerics
import win32more.Windows.UI.Composition
import win32more.Windows.UI.Core
import win32more.Windows.UI.Input.Inking
import win32more.Windows.UI.Input.Inking.Core
import win32more.Windows.Win32.System.WinRT
class CoreIncrementalInkStroke(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Inking.Core.ICoreIncrementalInkStroke
    _classid_ = 'Windows.UI.Input.Inking.Core.CoreIncrementalInkStroke'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.UI.Input.Inking.Core.CoreIncrementalInkStroke.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.UI.Input.Inking.Core.ICoreIncrementalInkStrokeFactory, drawingAttributes: win32more.Windows.UI.Input.Inking.InkDrawingAttributes, pointTransform: win32more.Windows.Foundation.Numerics.Matrix3x2) -> win32more.Windows.UI.Input.Inking.Core.CoreIncrementalInkStroke: ...
    @winrt_mixinmethod
    def AppendInkPoints(self: win32more.Windows.UI.Input.Inking.Core.ICoreIncrementalInkStroke, inkPoints: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Input.Inking.InkPoint]) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def CreateInkStroke(self: win32more.Windows.UI.Input.Inking.Core.ICoreIncrementalInkStroke) -> win32more.Windows.UI.Input.Inking.InkStroke: ...
    @winrt_mixinmethod
    def get_DrawingAttributes(self: win32more.Windows.UI.Input.Inking.Core.ICoreIncrementalInkStroke) -> win32more.Windows.UI.Input.Inking.InkDrawingAttributes: ...
    @winrt_mixinmethod
    def get_PointTransform(self: win32more.Windows.UI.Input.Inking.Core.ICoreIncrementalInkStroke) -> win32more.Windows.Foundation.Numerics.Matrix3x2: ...
    @winrt_mixinmethod
    def get_BoundingRect(self: win32more.Windows.UI.Input.Inking.Core.ICoreIncrementalInkStroke) -> win32more.Windows.Foundation.Rect: ...
    BoundingRect = property(get_BoundingRect, None)
    DrawingAttributes = property(get_DrawingAttributes, None)
    PointTransform = property(get_PointTransform, None)
class CoreInkIndependentInputSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Inking.Core.ICoreInkIndependentInputSource
    _classid_ = 'Windows.UI.Input.Inking.Core.CoreInkIndependentInputSource'
    @winrt_mixinmethod
    def add_PointerEntering(self: win32more.Windows.UI.Input.Inking.Core.ICoreInkIndependentInputSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.Core.CoreInkIndependentInputSource, win32more.Windows.UI.Core.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerEntering(self: win32more.Windows.UI.Input.Inking.Core.ICoreInkIndependentInputSource, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerHovering(self: win32more.Windows.UI.Input.Inking.Core.ICoreInkIndependentInputSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.Core.CoreInkIndependentInputSource, win32more.Windows.UI.Core.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerHovering(self: win32more.Windows.UI.Input.Inking.Core.ICoreInkIndependentInputSource, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerExiting(self: win32more.Windows.UI.Input.Inking.Core.ICoreInkIndependentInputSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.Core.CoreInkIndependentInputSource, win32more.Windows.UI.Core.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerExiting(self: win32more.Windows.UI.Input.Inking.Core.ICoreInkIndependentInputSource, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerPressing(self: win32more.Windows.UI.Input.Inking.Core.ICoreInkIndependentInputSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.Core.CoreInkIndependentInputSource, win32more.Windows.UI.Core.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerPressing(self: win32more.Windows.UI.Input.Inking.Core.ICoreInkIndependentInputSource, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerMoving(self: win32more.Windows.UI.Input.Inking.Core.ICoreInkIndependentInputSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.Core.CoreInkIndependentInputSource, win32more.Windows.UI.Core.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerMoving(self: win32more.Windows.UI.Input.Inking.Core.ICoreInkIndependentInputSource, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerReleasing(self: win32more.Windows.UI.Input.Inking.Core.ICoreInkIndependentInputSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.Core.CoreInkIndependentInputSource, win32more.Windows.UI.Core.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerReleasing(self: win32more.Windows.UI.Input.Inking.Core.ICoreInkIndependentInputSource, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerLost(self: win32more.Windows.UI.Input.Inking.Core.ICoreInkIndependentInputSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.Core.CoreInkIndependentInputSource, win32more.Windows.UI.Core.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerLost(self: win32more.Windows.UI.Input.Inking.Core.ICoreInkIndependentInputSource, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_InkPresenter(self: win32more.Windows.UI.Input.Inking.Core.ICoreInkIndependentInputSource) -> win32more.Windows.UI.Input.Inking.InkPresenter: ...
    @winrt_mixinmethod
    def get_PointerCursor(self: win32more.Windows.UI.Input.Inking.Core.ICoreInkIndependentInputSource2) -> win32more.Windows.UI.Core.CoreCursor: ...
    @winrt_mixinmethod
    def put_PointerCursor(self: win32more.Windows.UI.Input.Inking.Core.ICoreInkIndependentInputSource2, value: win32more.Windows.UI.Core.CoreCursor) -> Void: ...
    @winrt_classmethod
    def Create(cls: win32more.Windows.UI.Input.Inking.Core.ICoreInkIndependentInputSourceStatics, inkPresenter: win32more.Windows.UI.Input.Inking.InkPresenter) -> win32more.Windows.UI.Input.Inking.Core.CoreInkIndependentInputSource: ...
    InkPresenter = property(get_InkPresenter, None)
    PointerCursor = property(get_PointerCursor, put_PointerCursor)
    PointerEntering = event()
    PointerHovering = event()
    PointerExiting = event()
    PointerPressing = event()
    PointerMoving = event()
    PointerReleasing = event()
    PointerLost = event()
class CoreInkPresenterHost(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Inking.Core.ICoreInkPresenterHost
    _classid_ = 'Windows.UI.Input.Inking.Core.CoreInkPresenterHost'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Input.Inking.Core.CoreInkPresenterHost.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Input.Inking.Core.CoreInkPresenterHost: ...
    @winrt_mixinmethod
    def get_InkPresenter(self: win32more.Windows.UI.Input.Inking.Core.ICoreInkPresenterHost) -> win32more.Windows.UI.Input.Inking.InkPresenter: ...
    @winrt_mixinmethod
    def get_RootVisual(self: win32more.Windows.UI.Input.Inking.Core.ICoreInkPresenterHost) -> win32more.Windows.UI.Composition.ContainerVisual: ...
    @winrt_mixinmethod
    def put_RootVisual(self: win32more.Windows.UI.Input.Inking.Core.ICoreInkPresenterHost, value: win32more.Windows.UI.Composition.ContainerVisual) -> Void: ...
    InkPresenter = property(get_InkPresenter, None)
    RootVisual = property(get_RootVisual, put_RootVisual)
class CoreWetStrokeDisposition(Enum, Int32):
    Inking = 0
    Completed = 1
    Canceled = 2
class CoreWetStrokeUpdateEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Inking.Core.ICoreWetStrokeUpdateEventArgs
    _classid_ = 'Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateEventArgs'
    @winrt_mixinmethod
    def get_NewInkPoints(self: win32more.Windows.UI.Input.Inking.Core.ICoreWetStrokeUpdateEventArgs) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Input.Inking.InkPoint]: ...
    @winrt_mixinmethod
    def get_PointerId(self: win32more.Windows.UI.Input.Inking.Core.ICoreWetStrokeUpdateEventArgs) -> UInt32: ...
    @winrt_mixinmethod
    def get_Disposition(self: win32more.Windows.UI.Input.Inking.Core.ICoreWetStrokeUpdateEventArgs) -> win32more.Windows.UI.Input.Inking.Core.CoreWetStrokeDisposition: ...
    @winrt_mixinmethod
    def put_Disposition(self: win32more.Windows.UI.Input.Inking.Core.ICoreWetStrokeUpdateEventArgs, value: win32more.Windows.UI.Input.Inking.Core.CoreWetStrokeDisposition) -> Void: ...
    Disposition = property(get_Disposition, put_Disposition)
    NewInkPoints = property(get_NewInkPoints, None)
    PointerId = property(get_PointerId, None)
class CoreWetStrokeUpdateSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Inking.Core.ICoreWetStrokeUpdateSource
    _classid_ = 'Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateSource'
    @winrt_mixinmethod
    def add_WetStrokeStarting(self: win32more.Windows.UI.Input.Inking.Core.ICoreWetStrokeUpdateSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateSource, win32more.Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_WetStrokeStarting(self: win32more.Windows.UI.Input.Inking.Core.ICoreWetStrokeUpdateSource, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_WetStrokeContinuing(self: win32more.Windows.UI.Input.Inking.Core.ICoreWetStrokeUpdateSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateSource, win32more.Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_WetStrokeContinuing(self: win32more.Windows.UI.Input.Inking.Core.ICoreWetStrokeUpdateSource, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_WetStrokeStopping(self: win32more.Windows.UI.Input.Inking.Core.ICoreWetStrokeUpdateSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateSource, win32more.Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_WetStrokeStopping(self: win32more.Windows.UI.Input.Inking.Core.ICoreWetStrokeUpdateSource, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_WetStrokeCompleted(self: win32more.Windows.UI.Input.Inking.Core.ICoreWetStrokeUpdateSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateSource, win32more.Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_WetStrokeCompleted(self: win32more.Windows.UI.Input.Inking.Core.ICoreWetStrokeUpdateSource, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_WetStrokeCanceled(self: win32more.Windows.UI.Input.Inking.Core.ICoreWetStrokeUpdateSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateSource, win32more.Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_WetStrokeCanceled(self: win32more.Windows.UI.Input.Inking.Core.ICoreWetStrokeUpdateSource, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_InkPresenter(self: win32more.Windows.UI.Input.Inking.Core.ICoreWetStrokeUpdateSource) -> win32more.Windows.UI.Input.Inking.InkPresenter: ...
    @winrt_classmethod
    def Create(cls: win32more.Windows.UI.Input.Inking.Core.ICoreWetStrokeUpdateSourceStatics, inkPresenter: win32more.Windows.UI.Input.Inking.InkPresenter) -> win32more.Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateSource: ...
    InkPresenter = property(get_InkPresenter, None)
    WetStrokeStarting = event()
    WetStrokeContinuing = event()
    WetStrokeStopping = event()
    WetStrokeCompleted = event()
    WetStrokeCanceled = event()
class ICoreIncrementalInkStroke(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.Core.ICoreIncrementalInkStroke'
    _iid_ = Guid('{fda015d3-9d66-4f7d-a57f-cc70b9cfaa76}')
    @winrt_commethod(6)
    def AppendInkPoints(self, inkPoints: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Input.Inking.InkPoint]) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(7)
    def CreateInkStroke(self) -> win32more.Windows.UI.Input.Inking.InkStroke: ...
    @winrt_commethod(8)
    def get_DrawingAttributes(self) -> win32more.Windows.UI.Input.Inking.InkDrawingAttributes: ...
    @winrt_commethod(9)
    def get_PointTransform(self) -> win32more.Windows.Foundation.Numerics.Matrix3x2: ...
    @winrt_commethod(10)
    def get_BoundingRect(self) -> win32more.Windows.Foundation.Rect: ...
    BoundingRect = property(get_BoundingRect, None)
    DrawingAttributes = property(get_DrawingAttributes, None)
    PointTransform = property(get_PointTransform, None)
class ICoreIncrementalInkStrokeFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.Core.ICoreIncrementalInkStrokeFactory'
    _iid_ = Guid('{d7c59f46-8da8-4f70-9751-e53bb6df4596}')
    @winrt_commethod(6)
    def Create(self, drawingAttributes: win32more.Windows.UI.Input.Inking.InkDrawingAttributes, pointTransform: win32more.Windows.Foundation.Numerics.Matrix3x2) -> win32more.Windows.UI.Input.Inking.Core.CoreIncrementalInkStroke: ...
class ICoreInkIndependentInputSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.Core.ICoreInkIndependentInputSource'
    _iid_ = Guid('{39b38da9-7639-4499-a5b5-191d00e35b16}')
    @winrt_commethod(6)
    def add_PointerEntering(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.Core.CoreInkIndependentInputSource, win32more.Windows.UI.Core.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_PointerEntering(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_PointerHovering(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.Core.CoreInkIndependentInputSource, win32more.Windows.UI.Core.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_PointerHovering(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_PointerExiting(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.Core.CoreInkIndependentInputSource, win32more.Windows.UI.Core.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_PointerExiting(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_PointerPressing(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.Core.CoreInkIndependentInputSource, win32more.Windows.UI.Core.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_PointerPressing(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_PointerMoving(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.Core.CoreInkIndependentInputSource, win32more.Windows.UI.Core.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_PointerMoving(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def add_PointerReleasing(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.Core.CoreInkIndependentInputSource, win32more.Windows.UI.Core.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_PointerReleasing(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(18)
    def add_PointerLost(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.Core.CoreInkIndependentInputSource, win32more.Windows.UI.Core.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(19)
    def remove_PointerLost(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(20)
    def get_InkPresenter(self) -> win32more.Windows.UI.Input.Inking.InkPresenter: ...
    InkPresenter = property(get_InkPresenter, None)
    PointerEntering = event()
    PointerHovering = event()
    PointerExiting = event()
    PointerPressing = event()
    PointerMoving = event()
    PointerReleasing = event()
    PointerLost = event()
class ICoreInkIndependentInputSource2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.Core.ICoreInkIndependentInputSource2'
    _iid_ = Guid('{2846b012-0b59-5bb9-a3c5-becb7cf03a33}')
    @winrt_commethod(6)
    def get_PointerCursor(self) -> win32more.Windows.UI.Core.CoreCursor: ...
    @winrt_commethod(7)
    def put_PointerCursor(self, value: win32more.Windows.UI.Core.CoreCursor) -> Void: ...
    PointerCursor = property(get_PointerCursor, put_PointerCursor)
class ICoreInkIndependentInputSourceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.Core.ICoreInkIndependentInputSourceStatics'
    _iid_ = Guid('{73e6011b-80c0-4dfb-9b66-10ba7f3f9c84}')
    @winrt_commethod(6)
    def Create(self, inkPresenter: win32more.Windows.UI.Input.Inking.InkPresenter) -> win32more.Windows.UI.Input.Inking.Core.CoreInkIndependentInputSource: ...
class ICoreInkPresenterHost(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.Core.ICoreInkPresenterHost'
    _iid_ = Guid('{396e89e6-7d55-4617-9e58-68c70c9169b9}')
    @winrt_commethod(6)
    def get_InkPresenter(self) -> win32more.Windows.UI.Input.Inking.InkPresenter: ...
    @winrt_commethod(7)
    def get_RootVisual(self) -> win32more.Windows.UI.Composition.ContainerVisual: ...
    @winrt_commethod(8)
    def put_RootVisual(self, value: win32more.Windows.UI.Composition.ContainerVisual) -> Void: ...
    InkPresenter = property(get_InkPresenter, None)
    RootVisual = property(get_RootVisual, put_RootVisual)
class ICoreWetStrokeUpdateEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.Core.ICoreWetStrokeUpdateEventArgs'
    _iid_ = Guid('{fb07d14c-3380-457a-a987-991357896c1b}')
    @winrt_commethod(6)
    def get_NewInkPoints(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Input.Inking.InkPoint]: ...
    @winrt_commethod(7)
    def get_PointerId(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_Disposition(self) -> win32more.Windows.UI.Input.Inking.Core.CoreWetStrokeDisposition: ...
    @winrt_commethod(9)
    def put_Disposition(self, value: win32more.Windows.UI.Input.Inking.Core.CoreWetStrokeDisposition) -> Void: ...
    Disposition = property(get_Disposition, put_Disposition)
    NewInkPoints = property(get_NewInkPoints, None)
    PointerId = property(get_PointerId, None)
class ICoreWetStrokeUpdateSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.Core.ICoreWetStrokeUpdateSource'
    _iid_ = Guid('{1f718e22-ee52-4e00-8209-4c3e5b21a3cc}')
    @winrt_commethod(6)
    def add_WetStrokeStarting(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateSource, win32more.Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_WetStrokeStarting(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_WetStrokeContinuing(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateSource, win32more.Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_WetStrokeContinuing(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_WetStrokeStopping(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateSource, win32more.Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_WetStrokeStopping(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_WetStrokeCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateSource, win32more.Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_WetStrokeCompleted(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_WetStrokeCanceled(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateSource, win32more.Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_WetStrokeCanceled(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def get_InkPresenter(self) -> win32more.Windows.UI.Input.Inking.InkPresenter: ...
    InkPresenter = property(get_InkPresenter, None)
    WetStrokeStarting = event()
    WetStrokeContinuing = event()
    WetStrokeStopping = event()
    WetStrokeCompleted = event()
    WetStrokeCanceled = event()
class ICoreWetStrokeUpdateSourceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.Core.ICoreWetStrokeUpdateSourceStatics'
    _iid_ = Guid('{3dad9cba-1d3d-46ae-ab9d-8647486c6f90}')
    @winrt_commethod(6)
    def Create(self, inkPresenter: win32more.Windows.UI.Input.Inking.InkPresenter) -> win32more.Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateSource: ...


make_ready(__name__)
