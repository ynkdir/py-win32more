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
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.UI.Input.Inking
import win32more.Windows.UI.Input.Inking.Analysis
class IInkAnalysisInkBullet(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.Analysis.IInkAnalysisInkBullet'
    _iid_ = Guid('{ee049368-6110-4136-95f9-ee809fc20030}')
    @winrt_commethod(6)
    def get_RecognizedText(self) -> WinRT_String: ...
    RecognizedText = property(get_RecognizedText, None)
class IInkAnalysisInkDrawing(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.Analysis.IInkAnalysisInkDrawing'
    _iid_ = Guid('{6a85ed1f-1fe4-4e15-898c-8e112377e021}')
    @winrt_commethod(6)
    def get_DrawingKind(self) -> win32more.Windows.UI.Input.Inking.Analysis.InkAnalysisDrawingKind: ...
    @winrt_commethod(7)
    def get_Center(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(8)
    def get_Points(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Point]: ...
    DrawingKind = property(get_DrawingKind, None)
    Center = property(get_Center, None)
    Points = property(get_Points, None)
class IInkAnalysisInkWord(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.Analysis.IInkAnalysisInkWord'
    _iid_ = Guid('{4bd228ad-83af-4034-8f3b-f8687dfff436}')
    @winrt_commethod(6)
    def get_RecognizedText(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_TextAlternates(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    RecognizedText = property(get_RecognizedText, None)
    TextAlternates = property(get_TextAlternates, None)
class IInkAnalysisLine(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.Analysis.IInkAnalysisLine'
    _iid_ = Guid('{a06d048d-2b8d-4754-ad5a-d0871193a956}')
    @winrt_commethod(6)
    def get_RecognizedText(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_IndentLevel(self) -> Int32: ...
    RecognizedText = property(get_RecognizedText, None)
    IndentLevel = property(get_IndentLevel, None)
class IInkAnalysisListItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.Analysis.IInkAnalysisListItem'
    _iid_ = Guid('{b4e3c23f-c4c3-4c3a-a1a6-9d85547ee586}')
    @winrt_commethod(6)
    def get_RecognizedText(self) -> WinRT_String: ...
    RecognizedText = property(get_RecognizedText, None)
class IInkAnalysisNode(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.Analysis.IInkAnalysisNode'
    _iid_ = Guid('{30831f05-5f64-4a2c-ba37-4f4887879574}')
    @winrt_commethod(6)
    def get_Id(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_Kind(self) -> win32more.Windows.UI.Input.Inking.Analysis.InkAnalysisNodeKind: ...
    @winrt_commethod(8)
    def get_BoundingRect(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(9)
    def get_RotatedBoundingRect(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Point]: ...
    @winrt_commethod(10)
    def get_Children(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode]: ...
    @winrt_commethod(11)
    def get_Parent(self) -> win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode: ...
    @winrt_commethod(12)
    def GetStrokeIds(self) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    Id = property(get_Id, None)
    Kind = property(get_Kind, None)
    BoundingRect = property(get_BoundingRect, None)
    RotatedBoundingRect = property(get_RotatedBoundingRect, None)
    Children = property(get_Children, None)
    Parent = property(get_Parent, None)
class IInkAnalysisParagraph(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.Analysis.IInkAnalysisParagraph'
    _iid_ = Guid('{d9ad045c-0cd1-4dd4-a68b-eb1f12b3d727}')
    @winrt_commethod(6)
    def get_RecognizedText(self) -> WinRT_String: ...
    RecognizedText = property(get_RecognizedText, None)
class IInkAnalysisResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.Analysis.IInkAnalysisResult'
    _iid_ = Guid('{8948ba79-a243-4aa3-a294-1f98bd0ff580}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.UI.Input.Inking.Analysis.InkAnalysisStatus: ...
    Status = property(get_Status, None)
class IInkAnalysisRoot(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.Analysis.IInkAnalysisRoot'
    _iid_ = Guid('{3fb6a3c4-2fde-4061-8502-a90f32545b84}')
    @winrt_commethod(6)
    def get_RecognizedText(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def FindNodes(self, nodeKind: win32more.Windows.UI.Input.Inking.Analysis.InkAnalysisNodeKind) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode]: ...
    RecognizedText = property(get_RecognizedText, None)
class IInkAnalysisWritingRegion(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.Analysis.IInkAnalysisWritingRegion'
    _iid_ = Guid('{dd6d6231-bd16-4663-b5ae-941d3043ef5b}')
    @winrt_commethod(6)
    def get_RecognizedText(self) -> WinRT_String: ...
    RecognizedText = property(get_RecognizedText, None)
class IInkAnalyzer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.Analysis.IInkAnalyzer'
    _iid_ = Guid('{f12b8f95-0866-4dc5-8c77-f88614dfe38c}')
    @winrt_commethod(6)
    def get_AnalysisRoot(self) -> win32more.Windows.UI.Input.Inking.Analysis.InkAnalysisRoot: ...
    @winrt_commethod(7)
    def get_IsAnalyzing(self) -> Boolean: ...
    @winrt_commethod(8)
    def AddDataForStroke(self, stroke: win32more.Windows.UI.Input.Inking.InkStroke) -> Void: ...
    @winrt_commethod(9)
    def AddDataForStrokes(self, strokes: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Input.Inking.InkStroke]) -> Void: ...
    @winrt_commethod(10)
    def ClearDataForAllStrokes(self) -> Void: ...
    @winrt_commethod(11)
    def RemoveDataForStroke(self, strokeId: UInt32) -> Void: ...
    @winrt_commethod(12)
    def RemoveDataForStrokes(self, strokeIds: win32more.Windows.Foundation.Collections.IIterable[UInt32]) -> Void: ...
    @winrt_commethod(13)
    def ReplaceDataForStroke(self, stroke: win32more.Windows.UI.Input.Inking.InkStroke) -> Void: ...
    @winrt_commethod(14)
    def SetStrokeDataKind(self, strokeId: UInt32, strokeKind: win32more.Windows.UI.Input.Inking.Analysis.InkAnalysisStrokeKind) -> Void: ...
    @winrt_commethod(15)
    def AnalyzeAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.Input.Inking.Analysis.InkAnalysisResult]: ...
    AnalysisRoot = property(get_AnalysisRoot, None)
    IsAnalyzing = property(get_IsAnalyzing, None)
class IInkAnalyzerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.Analysis.IInkAnalyzerFactory'
    _iid_ = Guid('{29138686-1963-49d8-9589-e14384c769e3}')
    @winrt_commethod(6)
    def CreateAnalyzer(self) -> win32more.Windows.UI.Input.Inking.Analysis.InkAnalyzer: ...
InkAnalysisDrawingKind = Int32
InkAnalysisDrawingKind_Drawing: InkAnalysisDrawingKind = 0
InkAnalysisDrawingKind_Circle: InkAnalysisDrawingKind = 1
InkAnalysisDrawingKind_Ellipse: InkAnalysisDrawingKind = 2
InkAnalysisDrawingKind_Triangle: InkAnalysisDrawingKind = 3
InkAnalysisDrawingKind_IsoscelesTriangle: InkAnalysisDrawingKind = 4
InkAnalysisDrawingKind_EquilateralTriangle: InkAnalysisDrawingKind = 5
InkAnalysisDrawingKind_RightTriangle: InkAnalysisDrawingKind = 6
InkAnalysisDrawingKind_Quadrilateral: InkAnalysisDrawingKind = 7
InkAnalysisDrawingKind_Rectangle: InkAnalysisDrawingKind = 8
InkAnalysisDrawingKind_Square: InkAnalysisDrawingKind = 9
InkAnalysisDrawingKind_Diamond: InkAnalysisDrawingKind = 10
InkAnalysisDrawingKind_Trapezoid: InkAnalysisDrawingKind = 11
InkAnalysisDrawingKind_Parallelogram: InkAnalysisDrawingKind = 12
InkAnalysisDrawingKind_Pentagon: InkAnalysisDrawingKind = 13
InkAnalysisDrawingKind_Hexagon: InkAnalysisDrawingKind = 14
class InkAnalysisInkBullet(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisInkBullet
    _classid_ = 'Windows.UI.Input.Inking.Analysis.InkAnalysisInkBullet'
    @winrt_mixinmethod
    def get_RecognizedText(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisInkBullet) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> UInt32: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.UI.Input.Inking.Analysis.InkAnalysisNodeKind: ...
    @winrt_mixinmethod
    def get_BoundingRect(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_RotatedBoundingRect(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Point]: ...
    @winrt_mixinmethod
    def get_Children(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode]: ...
    @winrt_mixinmethod
    def get_Parent(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode: ...
    @winrt_mixinmethod
    def GetStrokeIds(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    RecognizedText = property(get_RecognizedText, None)
    Id = property(get_Id, None)
    Kind = property(get_Kind, None)
    BoundingRect = property(get_BoundingRect, None)
    RotatedBoundingRect = property(get_RotatedBoundingRect, None)
    Children = property(get_Children, None)
    Parent = property(get_Parent, None)
class InkAnalysisInkDrawing(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisInkDrawing
    _classid_ = 'Windows.UI.Input.Inking.Analysis.InkAnalysisInkDrawing'
    @winrt_mixinmethod
    def get_DrawingKind(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisInkDrawing) -> win32more.Windows.UI.Input.Inking.Analysis.InkAnalysisDrawingKind: ...
    @winrt_mixinmethod
    def get_Center(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisInkDrawing) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Points(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisInkDrawing) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Point]: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> UInt32: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.UI.Input.Inking.Analysis.InkAnalysisNodeKind: ...
    @winrt_mixinmethod
    def get_BoundingRect(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_RotatedBoundingRect(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Point]: ...
    @winrt_mixinmethod
    def get_Children(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode]: ...
    @winrt_mixinmethod
    def get_Parent(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode: ...
    @winrt_mixinmethod
    def GetStrokeIds(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    DrawingKind = property(get_DrawingKind, None)
    Center = property(get_Center, None)
    Points = property(get_Points, None)
    Id = property(get_Id, None)
    Kind = property(get_Kind, None)
    BoundingRect = property(get_BoundingRect, None)
    RotatedBoundingRect = property(get_RotatedBoundingRect, None)
    Children = property(get_Children, None)
    Parent = property(get_Parent, None)
class InkAnalysisInkWord(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisInkWord
    _classid_ = 'Windows.UI.Input.Inking.Analysis.InkAnalysisInkWord'
    @winrt_mixinmethod
    def get_RecognizedText(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisInkWord) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TextAlternates(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisInkWord) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> UInt32: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.UI.Input.Inking.Analysis.InkAnalysisNodeKind: ...
    @winrt_mixinmethod
    def get_BoundingRect(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_RotatedBoundingRect(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Point]: ...
    @winrt_mixinmethod
    def get_Children(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode]: ...
    @winrt_mixinmethod
    def get_Parent(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode: ...
    @winrt_mixinmethod
    def GetStrokeIds(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    RecognizedText = property(get_RecognizedText, None)
    TextAlternates = property(get_TextAlternates, None)
    Id = property(get_Id, None)
    Kind = property(get_Kind, None)
    BoundingRect = property(get_BoundingRect, None)
    RotatedBoundingRect = property(get_RotatedBoundingRect, None)
    Children = property(get_Children, None)
    Parent = property(get_Parent, None)
class InkAnalysisLine(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisLine
    _classid_ = 'Windows.UI.Input.Inking.Analysis.InkAnalysisLine'
    @winrt_mixinmethod
    def get_RecognizedText(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisLine) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IndentLevel(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisLine) -> Int32: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> UInt32: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.UI.Input.Inking.Analysis.InkAnalysisNodeKind: ...
    @winrt_mixinmethod
    def get_BoundingRect(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_RotatedBoundingRect(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Point]: ...
    @winrt_mixinmethod
    def get_Children(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode]: ...
    @winrt_mixinmethod
    def get_Parent(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode: ...
    @winrt_mixinmethod
    def GetStrokeIds(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    RecognizedText = property(get_RecognizedText, None)
    IndentLevel = property(get_IndentLevel, None)
    Id = property(get_Id, None)
    Kind = property(get_Kind, None)
    BoundingRect = property(get_BoundingRect, None)
    RotatedBoundingRect = property(get_RotatedBoundingRect, None)
    Children = property(get_Children, None)
    Parent = property(get_Parent, None)
class InkAnalysisListItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisListItem
    _classid_ = 'Windows.UI.Input.Inking.Analysis.InkAnalysisListItem'
    @winrt_mixinmethod
    def get_RecognizedText(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisListItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> UInt32: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.UI.Input.Inking.Analysis.InkAnalysisNodeKind: ...
    @winrt_mixinmethod
    def get_BoundingRect(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_RotatedBoundingRect(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Point]: ...
    @winrt_mixinmethod
    def get_Children(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode]: ...
    @winrt_mixinmethod
    def get_Parent(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode: ...
    @winrt_mixinmethod
    def GetStrokeIds(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    RecognizedText = property(get_RecognizedText, None)
    Id = property(get_Id, None)
    Kind = property(get_Kind, None)
    BoundingRect = property(get_BoundingRect, None)
    RotatedBoundingRect = property(get_RotatedBoundingRect, None)
    Children = property(get_Children, None)
    Parent = property(get_Parent, None)
class InkAnalysisNode(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode
    _classid_ = 'Windows.UI.Input.Inking.Analysis.InkAnalysisNode'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> UInt32: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.UI.Input.Inking.Analysis.InkAnalysisNodeKind: ...
    @winrt_mixinmethod
    def get_BoundingRect(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_RotatedBoundingRect(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Point]: ...
    @winrt_mixinmethod
    def get_Children(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode]: ...
    @winrt_mixinmethod
    def get_Parent(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode: ...
    @winrt_mixinmethod
    def GetStrokeIds(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    Id = property(get_Id, None)
    Kind = property(get_Kind, None)
    BoundingRect = property(get_BoundingRect, None)
    RotatedBoundingRect = property(get_RotatedBoundingRect, None)
    Children = property(get_Children, None)
    Parent = property(get_Parent, None)
InkAnalysisNodeKind = Int32
InkAnalysisNodeKind_UnclassifiedInk: InkAnalysisNodeKind = 0
InkAnalysisNodeKind_Root: InkAnalysisNodeKind = 1
InkAnalysisNodeKind_WritingRegion: InkAnalysisNodeKind = 2
InkAnalysisNodeKind_Paragraph: InkAnalysisNodeKind = 3
InkAnalysisNodeKind_Line: InkAnalysisNodeKind = 4
InkAnalysisNodeKind_InkWord: InkAnalysisNodeKind = 5
InkAnalysisNodeKind_InkBullet: InkAnalysisNodeKind = 6
InkAnalysisNodeKind_InkDrawing: InkAnalysisNodeKind = 7
InkAnalysisNodeKind_ListItem: InkAnalysisNodeKind = 8
class InkAnalysisParagraph(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisParagraph
    _classid_ = 'Windows.UI.Input.Inking.Analysis.InkAnalysisParagraph'
    @winrt_mixinmethod
    def get_RecognizedText(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisParagraph) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> UInt32: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.UI.Input.Inking.Analysis.InkAnalysisNodeKind: ...
    @winrt_mixinmethod
    def get_BoundingRect(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_RotatedBoundingRect(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Point]: ...
    @winrt_mixinmethod
    def get_Children(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode]: ...
    @winrt_mixinmethod
    def get_Parent(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode: ...
    @winrt_mixinmethod
    def GetStrokeIds(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    RecognizedText = property(get_RecognizedText, None)
    Id = property(get_Id, None)
    Kind = property(get_Kind, None)
    BoundingRect = property(get_BoundingRect, None)
    RotatedBoundingRect = property(get_RotatedBoundingRect, None)
    Children = property(get_Children, None)
    Parent = property(get_Parent, None)
class InkAnalysisResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisResult
    _classid_ = 'Windows.UI.Input.Inking.Analysis.InkAnalysisResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisResult) -> win32more.Windows.UI.Input.Inking.Analysis.InkAnalysisStatus: ...
    Status = property(get_Status, None)
class InkAnalysisRoot(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisRoot
    _classid_ = 'Windows.UI.Input.Inking.Analysis.InkAnalysisRoot'
    @winrt_mixinmethod
    def get_RecognizedText(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisRoot) -> WinRT_String: ...
    @winrt_mixinmethod
    def FindNodes(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisRoot, nodeKind: win32more.Windows.UI.Input.Inking.Analysis.InkAnalysisNodeKind) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode]: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> UInt32: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.UI.Input.Inking.Analysis.InkAnalysisNodeKind: ...
    @winrt_mixinmethod
    def get_BoundingRect(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_RotatedBoundingRect(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Point]: ...
    @winrt_mixinmethod
    def get_Children(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode]: ...
    @winrt_mixinmethod
    def get_Parent(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode: ...
    @winrt_mixinmethod
    def GetStrokeIds(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    RecognizedText = property(get_RecognizedText, None)
    Id = property(get_Id, None)
    Kind = property(get_Kind, None)
    BoundingRect = property(get_BoundingRect, None)
    RotatedBoundingRect = property(get_RotatedBoundingRect, None)
    Children = property(get_Children, None)
    Parent = property(get_Parent, None)
InkAnalysisStatus = Int32
InkAnalysisStatus_Updated: InkAnalysisStatus = 0
InkAnalysisStatus_Unchanged: InkAnalysisStatus = 1
InkAnalysisStrokeKind = Int32
InkAnalysisStrokeKind_Auto: InkAnalysisStrokeKind = 0
InkAnalysisStrokeKind_Writing: InkAnalysisStrokeKind = 1
InkAnalysisStrokeKind_Drawing: InkAnalysisStrokeKind = 2
class InkAnalysisWritingRegion(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisWritingRegion
    _classid_ = 'Windows.UI.Input.Inking.Analysis.InkAnalysisWritingRegion'
    @winrt_mixinmethod
    def get_RecognizedText(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisWritingRegion) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> UInt32: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.UI.Input.Inking.Analysis.InkAnalysisNodeKind: ...
    @winrt_mixinmethod
    def get_BoundingRect(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_RotatedBoundingRect(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Point]: ...
    @winrt_mixinmethod
    def get_Children(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode]: ...
    @winrt_mixinmethod
    def get_Parent(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode: ...
    @winrt_mixinmethod
    def GetStrokeIds(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    RecognizedText = property(get_RecognizedText, None)
    Id = property(get_Id, None)
    Kind = property(get_Kind, None)
    BoundingRect = property(get_BoundingRect, None)
    RotatedBoundingRect = property(get_RotatedBoundingRect, None)
    Children = property(get_Children, None)
    Parent = property(get_Parent, None)
class InkAnalyzer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalyzer
    _classid_ = 'Windows.UI.Input.Inking.Analysis.InkAnalyzer'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 0:
            return win32more.Windows.UI.Input.Inking.Analysis.InkAnalyzer.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Input.Inking.Analysis.InkAnalyzer: ...
    @winrt_mixinmethod
    def get_AnalysisRoot(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalyzer) -> win32more.Windows.UI.Input.Inking.Analysis.InkAnalysisRoot: ...
    @winrt_mixinmethod
    def get_IsAnalyzing(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalyzer) -> Boolean: ...
    @winrt_mixinmethod
    def AddDataForStroke(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalyzer, stroke: win32more.Windows.UI.Input.Inking.InkStroke) -> Void: ...
    @winrt_mixinmethod
    def AddDataForStrokes(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalyzer, strokes: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Input.Inking.InkStroke]) -> Void: ...
    @winrt_mixinmethod
    def ClearDataForAllStrokes(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalyzer) -> Void: ...
    @winrt_mixinmethod
    def RemoveDataForStroke(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalyzer, strokeId: UInt32) -> Void: ...
    @winrt_mixinmethod
    def RemoveDataForStrokes(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalyzer, strokeIds: win32more.Windows.Foundation.Collections.IIterable[UInt32]) -> Void: ...
    @winrt_mixinmethod
    def ReplaceDataForStroke(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalyzer, stroke: win32more.Windows.UI.Input.Inking.InkStroke) -> Void: ...
    @winrt_mixinmethod
    def SetStrokeDataKind(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalyzer, strokeId: UInt32, strokeKind: win32more.Windows.UI.Input.Inking.Analysis.InkAnalysisStrokeKind) -> Void: ...
    @winrt_mixinmethod
    def AnalyzeAsync(self: win32more.Windows.UI.Input.Inking.Analysis.IInkAnalyzer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.Input.Inking.Analysis.InkAnalysisResult]: ...
    AnalysisRoot = property(get_AnalysisRoot, None)
    IsAnalyzing = property(get_IsAnalyzing, None)


make_ready(__name__)
