from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Microsoft.Graphics.Canvas
import win32more.Microsoft.Graphics.Canvas.UI.Composition
import win32more.Microsoft.UI.Composition
import win32more.Windows.Foundation
import win32more.Windows.Win32.System.WinRT
class CanvasComposition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Graphics.Canvas.UI.Composition.CanvasComposition'
    @winrt_classmethod
    def CreateCompositionGraphicsDevice(cls: win32more.Microsoft.Graphics.Canvas.UI.Composition.ICanvasCompositionStatics, compositor: win32more.Microsoft.UI.Composition.Compositor, canvasDevice: win32more.Microsoft.Graphics.Canvas.CanvasDevice) -> win32more.Microsoft.UI.Composition.CompositionGraphicsDevice: ...
    @winrt_classmethod
    def GetCanvasDevice(cls: win32more.Microsoft.Graphics.Canvas.UI.Composition.ICanvasCompositionStatics, graphicsDevice: win32more.Microsoft.UI.Composition.CompositionGraphicsDevice) -> win32more.Microsoft.Graphics.Canvas.CanvasDevice: ...
    @winrt_classmethod
    def SetCanvasDevice(cls: win32more.Microsoft.Graphics.Canvas.UI.Composition.ICanvasCompositionStatics, graphicsDevice: win32more.Microsoft.UI.Composition.CompositionGraphicsDevice, canvasDevice: win32more.Microsoft.Graphics.Canvas.CanvasDevice) -> Void: ...
    @winrt_classmethod
    def CreateDrawingSession(cls: win32more.Microsoft.Graphics.Canvas.UI.Composition.ICanvasCompositionStatics, drawingSurface: win32more.Microsoft.UI.Composition.CompositionDrawingSurface) -> win32more.Microsoft.Graphics.Canvas.CanvasDrawingSession: ...
    @winrt_classmethod
    def CreateDrawingSessionWithUpdateRect(cls: win32more.Microsoft.Graphics.Canvas.UI.Composition.ICanvasCompositionStatics, drawingSurface: win32more.Microsoft.UI.Composition.CompositionDrawingSurface, updateRect: win32more.Windows.Foundation.Rect) -> win32more.Microsoft.Graphics.Canvas.CanvasDrawingSession: ...
    @winrt_classmethod
    def CreateDrawingSessionWithUpdateRectAndDpi(cls: win32more.Microsoft.Graphics.Canvas.UI.Composition.ICanvasCompositionStatics, drawingSurface: win32more.Microsoft.UI.Composition.CompositionDrawingSurface, updateRectInPixels: win32more.Windows.Foundation.Rect, dpi: Single) -> win32more.Microsoft.Graphics.Canvas.CanvasDrawingSession: ...
    @winrt_classmethod
    def Resize(cls: win32more.Microsoft.Graphics.Canvas.UI.Composition.ICanvasCompositionStatics, drawingSurface: win32more.Microsoft.UI.Composition.CompositionDrawingSurface, sizeInPixels: win32more.Windows.Foundation.Size) -> Void: ...
class ICanvasCompositionStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Graphics.Canvas.UI.Composition.ICanvasCompositionStatics'
    _iid_ = Guid('{162deb43-1cf5-46f8-a0af-356b23158f92}')
    @winrt_commethod(6)
    def CreateCompositionGraphicsDevice(self, compositor: win32more.Microsoft.UI.Composition.Compositor, canvasDevice: win32more.Microsoft.Graphics.Canvas.CanvasDevice) -> win32more.Microsoft.UI.Composition.CompositionGraphicsDevice: ...
    @winrt_commethod(7)
    def GetCanvasDevice(self, graphicsDevice: win32more.Microsoft.UI.Composition.CompositionGraphicsDevice) -> win32more.Microsoft.Graphics.Canvas.CanvasDevice: ...
    @winrt_commethod(8)
    def SetCanvasDevice(self, graphicsDevice: win32more.Microsoft.UI.Composition.CompositionGraphicsDevice, canvasDevice: win32more.Microsoft.Graphics.Canvas.CanvasDevice) -> Void: ...
    @winrt_commethod(9)
    def CreateDrawingSession(self, drawingSurface: win32more.Microsoft.UI.Composition.CompositionDrawingSurface) -> win32more.Microsoft.Graphics.Canvas.CanvasDrawingSession: ...
    @winrt_commethod(10)
    def CreateDrawingSessionWithUpdateRect(self, drawingSurface: win32more.Microsoft.UI.Composition.CompositionDrawingSurface, updateRect: win32more.Windows.Foundation.Rect) -> win32more.Microsoft.Graphics.Canvas.CanvasDrawingSession: ...
    @winrt_commethod(11)
    def CreateDrawingSessionWithUpdateRectAndDpi(self, drawingSurface: win32more.Microsoft.UI.Composition.CompositionDrawingSurface, updateRectInPixels: win32more.Windows.Foundation.Rect, dpi: Single) -> win32more.Microsoft.Graphics.Canvas.CanvasDrawingSession: ...
    @winrt_commethod(12)
    def Resize(self, drawingSurface: win32more.Microsoft.UI.Composition.CompositionDrawingSurface, sizeInPixels: win32more.Windows.Foundation.Size) -> Void: ...


make_ready(__name__)