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
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import Windows.Win32.System.WinRT
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Foundation.Numerics
import Windows.UI.Composition
import Windows.UI.Core
import Windows.UI.Input.Inking
import Windows.UI.Input.Inking.Core
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class CoreIncrementalInkStroke(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Input.Inking.Core.ICoreIncrementalInkStroke
    _classid_ = 'Windows.UI.Input.Inking.Core.CoreIncrementalInkStroke'
    @winrt_factorymethod
    def Create(cls: Windows.UI.Input.Inking.Core.ICoreIncrementalInkStrokeFactory, drawingAttributes: Windows.UI.Input.Inking.InkDrawingAttributes, pointTransform: Windows.Foundation.Numerics.Matrix3x2) -> Windows.UI.Input.Inking.Core.CoreIncrementalInkStroke: ...
    @winrt_mixinmethod
    def AppendInkPoints(self: Windows.UI.Input.Inking.Core.ICoreIncrementalInkStroke, inkPoints: Windows.Foundation.Collections.IIterable[Windows.UI.Input.Inking.InkPoint]) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def CreateInkStroke(self: Windows.UI.Input.Inking.Core.ICoreIncrementalInkStroke) -> Windows.UI.Input.Inking.InkStroke: ...
    @winrt_mixinmethod
    def get_DrawingAttributes(self: Windows.UI.Input.Inking.Core.ICoreIncrementalInkStroke) -> Windows.UI.Input.Inking.InkDrawingAttributes: ...
    @winrt_mixinmethod
    def get_PointTransform(self: Windows.UI.Input.Inking.Core.ICoreIncrementalInkStroke) -> Windows.Foundation.Numerics.Matrix3x2: ...
    @winrt_mixinmethod
    def get_BoundingRect(self: Windows.UI.Input.Inking.Core.ICoreIncrementalInkStroke) -> Windows.Foundation.Rect: ...
    DrawingAttributes = property(get_DrawingAttributes, None)
    PointTransform = property(get_PointTransform, None)
    BoundingRect = property(get_BoundingRect, None)
class CoreInkIndependentInputSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Input.Inking.Core.ICoreInkIndependentInputSource
    _classid_ = 'Windows.UI.Input.Inking.Core.CoreInkIndependentInputSource'
    @winrt_mixinmethod
    def add_PointerEntering(self: Windows.UI.Input.Inking.Core.ICoreInkIndependentInputSource, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.Core.CoreInkIndependentInputSource, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerEntering(self: Windows.UI.Input.Inking.Core.ICoreInkIndependentInputSource, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerHovering(self: Windows.UI.Input.Inking.Core.ICoreInkIndependentInputSource, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.Core.CoreInkIndependentInputSource, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerHovering(self: Windows.UI.Input.Inking.Core.ICoreInkIndependentInputSource, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerExiting(self: Windows.UI.Input.Inking.Core.ICoreInkIndependentInputSource, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.Core.CoreInkIndependentInputSource, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerExiting(self: Windows.UI.Input.Inking.Core.ICoreInkIndependentInputSource, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerPressing(self: Windows.UI.Input.Inking.Core.ICoreInkIndependentInputSource, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.Core.CoreInkIndependentInputSource, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerPressing(self: Windows.UI.Input.Inking.Core.ICoreInkIndependentInputSource, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerMoving(self: Windows.UI.Input.Inking.Core.ICoreInkIndependentInputSource, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.Core.CoreInkIndependentInputSource, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerMoving(self: Windows.UI.Input.Inking.Core.ICoreInkIndependentInputSource, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerReleasing(self: Windows.UI.Input.Inking.Core.ICoreInkIndependentInputSource, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.Core.CoreInkIndependentInputSource, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerReleasing(self: Windows.UI.Input.Inking.Core.ICoreInkIndependentInputSource, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerLost(self: Windows.UI.Input.Inking.Core.ICoreInkIndependentInputSource, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.Core.CoreInkIndependentInputSource, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerLost(self: Windows.UI.Input.Inking.Core.ICoreInkIndependentInputSource, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_InkPresenter(self: Windows.UI.Input.Inking.Core.ICoreInkIndependentInputSource) -> Windows.UI.Input.Inking.InkPresenter: ...
    @winrt_mixinmethod
    def get_PointerCursor(self: Windows.UI.Input.Inking.Core.ICoreInkIndependentInputSource2) -> Windows.UI.Core.CoreCursor: ...
    @winrt_mixinmethod
    def put_PointerCursor(self: Windows.UI.Input.Inking.Core.ICoreInkIndependentInputSource2, value: Windows.UI.Core.CoreCursor) -> Void: ...
    @winrt_classmethod
    def Create(cls: Windows.UI.Input.Inking.Core.ICoreInkIndependentInputSourceStatics, inkPresenter: Windows.UI.Input.Inking.InkPresenter) -> Windows.UI.Input.Inking.Core.CoreInkIndependentInputSource: ...
    InkPresenter = property(get_InkPresenter, None)
    PointerCursor = property(get_PointerCursor, put_PointerCursor)
class CoreInkPresenterHost(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Input.Inking.Core.ICoreInkPresenterHost
    _classid_ = 'Windows.UI.Input.Inking.Core.CoreInkPresenterHost'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Input.Inking.Core.CoreInkPresenterHost: ...
    @winrt_mixinmethod
    def get_InkPresenter(self: Windows.UI.Input.Inking.Core.ICoreInkPresenterHost) -> Windows.UI.Input.Inking.InkPresenter: ...
    @winrt_mixinmethod
    def get_RootVisual(self: Windows.UI.Input.Inking.Core.ICoreInkPresenterHost) -> Windows.UI.Composition.ContainerVisual: ...
    @winrt_mixinmethod
    def put_RootVisual(self: Windows.UI.Input.Inking.Core.ICoreInkPresenterHost, value: Windows.UI.Composition.ContainerVisual) -> Void: ...
    InkPresenter = property(get_InkPresenter, None)
    RootVisual = property(get_RootVisual, put_RootVisual)
CoreWetStrokeDisposition = Int32
CoreWetStrokeDisposition_Inking: CoreWetStrokeDisposition = 0
CoreWetStrokeDisposition_Completed: CoreWetStrokeDisposition = 1
CoreWetStrokeDisposition_Canceled: CoreWetStrokeDisposition = 2
class CoreWetStrokeUpdateEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Input.Inking.Core.ICoreWetStrokeUpdateEventArgs
    _classid_ = 'Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateEventArgs'
    @winrt_mixinmethod
    def get_NewInkPoints(self: Windows.UI.Input.Inking.Core.ICoreWetStrokeUpdateEventArgs) -> Windows.Foundation.Collections.IVector[Windows.UI.Input.Inking.InkPoint]: ...
    @winrt_mixinmethod
    def get_PointerId(self: Windows.UI.Input.Inking.Core.ICoreWetStrokeUpdateEventArgs) -> UInt32: ...
    @winrt_mixinmethod
    def get_Disposition(self: Windows.UI.Input.Inking.Core.ICoreWetStrokeUpdateEventArgs) -> Windows.UI.Input.Inking.Core.CoreWetStrokeDisposition: ...
    @winrt_mixinmethod
    def put_Disposition(self: Windows.UI.Input.Inking.Core.ICoreWetStrokeUpdateEventArgs, value: Windows.UI.Input.Inking.Core.CoreWetStrokeDisposition) -> Void: ...
    NewInkPoints = property(get_NewInkPoints, None)
    PointerId = property(get_PointerId, None)
    Disposition = property(get_Disposition, put_Disposition)
class CoreWetStrokeUpdateSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Input.Inking.Core.ICoreWetStrokeUpdateSource
    _classid_ = 'Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateSource'
    @winrt_mixinmethod
    def add_WetStrokeStarting(self: Windows.UI.Input.Inking.Core.ICoreWetStrokeUpdateSource, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateSource, Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_WetStrokeStarting(self: Windows.UI.Input.Inking.Core.ICoreWetStrokeUpdateSource, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_WetStrokeContinuing(self: Windows.UI.Input.Inking.Core.ICoreWetStrokeUpdateSource, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateSource, Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_WetStrokeContinuing(self: Windows.UI.Input.Inking.Core.ICoreWetStrokeUpdateSource, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_WetStrokeStopping(self: Windows.UI.Input.Inking.Core.ICoreWetStrokeUpdateSource, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateSource, Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_WetStrokeStopping(self: Windows.UI.Input.Inking.Core.ICoreWetStrokeUpdateSource, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_WetStrokeCompleted(self: Windows.UI.Input.Inking.Core.ICoreWetStrokeUpdateSource, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateSource, Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_WetStrokeCompleted(self: Windows.UI.Input.Inking.Core.ICoreWetStrokeUpdateSource, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_WetStrokeCanceled(self: Windows.UI.Input.Inking.Core.ICoreWetStrokeUpdateSource, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateSource, Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_WetStrokeCanceled(self: Windows.UI.Input.Inking.Core.ICoreWetStrokeUpdateSource, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_InkPresenter(self: Windows.UI.Input.Inking.Core.ICoreWetStrokeUpdateSource) -> Windows.UI.Input.Inking.InkPresenter: ...
    @winrt_classmethod
    def Create(cls: Windows.UI.Input.Inking.Core.ICoreWetStrokeUpdateSourceStatics, inkPresenter: Windows.UI.Input.Inking.InkPresenter) -> Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateSource: ...
    InkPresenter = property(get_InkPresenter, None)
class ICoreIncrementalInkStroke(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.Core.ICoreIncrementalInkStroke'
    _iid_ = Guid('{fda015d3-9d66-4f7d-a57f-cc70b9cfaa76}')
    @winrt_commethod(6)
    def AppendInkPoints(self, inkPoints: Windows.Foundation.Collections.IIterable[Windows.UI.Input.Inking.InkPoint]) -> Windows.Foundation.Rect: ...
    @winrt_commethod(7)
    def CreateInkStroke(self) -> Windows.UI.Input.Inking.InkStroke: ...
    @winrt_commethod(8)
    def get_DrawingAttributes(self) -> Windows.UI.Input.Inking.InkDrawingAttributes: ...
    @winrt_commethod(9)
    def get_PointTransform(self) -> Windows.Foundation.Numerics.Matrix3x2: ...
    @winrt_commethod(10)
    def get_BoundingRect(self) -> Windows.Foundation.Rect: ...
    DrawingAttributes = property(get_DrawingAttributes, None)
    PointTransform = property(get_PointTransform, None)
    BoundingRect = property(get_BoundingRect, None)
class ICoreIncrementalInkStrokeFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.Core.ICoreIncrementalInkStrokeFactory'
    _iid_ = Guid('{d7c59f46-8da8-4f70-9751-e53bb6df4596}')
    @winrt_commethod(6)
    def Create(self, drawingAttributes: Windows.UI.Input.Inking.InkDrawingAttributes, pointTransform: Windows.Foundation.Numerics.Matrix3x2) -> Windows.UI.Input.Inking.Core.CoreIncrementalInkStroke: ...
class ICoreInkIndependentInputSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.Core.ICoreInkIndependentInputSource'
    _iid_ = Guid('{39b38da9-7639-4499-a5b5-191d00e35b16}')
    @winrt_commethod(6)
    def add_PointerEntering(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.Core.CoreInkIndependentInputSource, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_PointerEntering(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_PointerHovering(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.Core.CoreInkIndependentInputSource, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_PointerHovering(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_PointerExiting(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.Core.CoreInkIndependentInputSource, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_PointerExiting(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_PointerPressing(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.Core.CoreInkIndependentInputSource, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_PointerPressing(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_PointerMoving(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.Core.CoreInkIndependentInputSource, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_PointerMoving(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def add_PointerReleasing(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.Core.CoreInkIndependentInputSource, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_PointerReleasing(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(18)
    def add_PointerLost(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.Core.CoreInkIndependentInputSource, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(19)
    def remove_PointerLost(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(20)
    def get_InkPresenter(self) -> Windows.UI.Input.Inking.InkPresenter: ...
    InkPresenter = property(get_InkPresenter, None)
class ICoreInkIndependentInputSource2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.Core.ICoreInkIndependentInputSource2'
    _iid_ = Guid('{2846b012-0b59-5bb9-a3c5-becb7cf03a33}')
    @winrt_commethod(6)
    def get_PointerCursor(self) -> Windows.UI.Core.CoreCursor: ...
    @winrt_commethod(7)
    def put_PointerCursor(self, value: Windows.UI.Core.CoreCursor) -> Void: ...
    PointerCursor = property(get_PointerCursor, put_PointerCursor)
class ICoreInkIndependentInputSourceStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.Core.ICoreInkIndependentInputSourceStatics'
    _iid_ = Guid('{73e6011b-80c0-4dfb-9b66-10ba7f3f9c84}')
    @winrt_commethod(6)
    def Create(self, inkPresenter: Windows.UI.Input.Inking.InkPresenter) -> Windows.UI.Input.Inking.Core.CoreInkIndependentInputSource: ...
class ICoreInkPresenterHost(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.Core.ICoreInkPresenterHost'
    _iid_ = Guid('{396e89e6-7d55-4617-9e58-68c70c9169b9}')
    @winrt_commethod(6)
    def get_InkPresenter(self) -> Windows.UI.Input.Inking.InkPresenter: ...
    @winrt_commethod(7)
    def get_RootVisual(self) -> Windows.UI.Composition.ContainerVisual: ...
    @winrt_commethod(8)
    def put_RootVisual(self, value: Windows.UI.Composition.ContainerVisual) -> Void: ...
    InkPresenter = property(get_InkPresenter, None)
    RootVisual = property(get_RootVisual, put_RootVisual)
class ICoreWetStrokeUpdateEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.Core.ICoreWetStrokeUpdateEventArgs'
    _iid_ = Guid('{fb07d14c-3380-457a-a987-991357896c1b}')
    @winrt_commethod(6)
    def get_NewInkPoints(self) -> Windows.Foundation.Collections.IVector[Windows.UI.Input.Inking.InkPoint]: ...
    @winrt_commethod(7)
    def get_PointerId(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_Disposition(self) -> Windows.UI.Input.Inking.Core.CoreWetStrokeDisposition: ...
    @winrt_commethod(9)
    def put_Disposition(self, value: Windows.UI.Input.Inking.Core.CoreWetStrokeDisposition) -> Void: ...
    NewInkPoints = property(get_NewInkPoints, None)
    PointerId = property(get_PointerId, None)
    Disposition = property(get_Disposition, put_Disposition)
class ICoreWetStrokeUpdateSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.Core.ICoreWetStrokeUpdateSource'
    _iid_ = Guid('{1f718e22-ee52-4e00-8209-4c3e5b21a3cc}')
    @winrt_commethod(6)
    def add_WetStrokeStarting(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateSource, Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_WetStrokeStarting(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_WetStrokeContinuing(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateSource, Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_WetStrokeContinuing(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_WetStrokeStopping(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateSource, Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_WetStrokeStopping(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_WetStrokeCompleted(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateSource, Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_WetStrokeCompleted(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_WetStrokeCanceled(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateSource, Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_WetStrokeCanceled(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def get_InkPresenter(self) -> Windows.UI.Input.Inking.InkPresenter: ...
    InkPresenter = property(get_InkPresenter, None)
class ICoreWetStrokeUpdateSourceStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.Core.ICoreWetStrokeUpdateSourceStatics'
    _iid_ = Guid('{3dad9cba-1d3d-46ae-ab9d-8647486c6f90}')
    @winrt_commethod(6)
    def Create(self, inkPresenter: Windows.UI.Input.Inking.InkPresenter) -> Windows.UI.Input.Inking.Core.CoreWetStrokeUpdateSource: ...
make_head(_module, 'CoreIncrementalInkStroke')
make_head(_module, 'CoreInkIndependentInputSource')
make_head(_module, 'CoreInkPresenterHost')
make_head(_module, 'CoreWetStrokeUpdateEventArgs')
make_head(_module, 'CoreWetStrokeUpdateSource')
make_head(_module, 'ICoreIncrementalInkStroke')
make_head(_module, 'ICoreIncrementalInkStrokeFactory')
make_head(_module, 'ICoreInkIndependentInputSource')
make_head(_module, 'ICoreInkIndependentInputSource2')
make_head(_module, 'ICoreInkIndependentInputSourceStatics')
make_head(_module, 'ICoreInkPresenterHost')
make_head(_module, 'ICoreWetStrokeUpdateEventArgs')
make_head(_module, 'ICoreWetStrokeUpdateSource')
make_head(_module, 'ICoreWetStrokeUpdateSourceStatics')
