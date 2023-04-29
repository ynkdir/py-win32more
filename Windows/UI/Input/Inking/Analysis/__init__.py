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
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.UI.Input.Inking
import Windows.UI.Input.Inking.Analysis
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IInkAnalysisInkBullet(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('ee049368-6110-4136-95-f9-ee-80-9f-c2-00-30')
    @winrt_commethod(6)
    def get_RecognizedText(self) -> WinRT_String: ...
    RecognizedText = property(get_RecognizedText, None)
class IInkAnalysisInkDrawing(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('6a85ed1f-1fe4-4e15-89-8c-8e-11-23-77-e0-21')
    @winrt_commethod(6)
    def get_DrawingKind(self) -> Windows.UI.Input.Inking.Analysis.InkAnalysisDrawingKind: ...
    @winrt_commethod(7)
    def get_Center(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(8)
    def get_Points(self) -> Windows.Foundation.Collections.IVectorView[Windows.Foundation.Point]: ...
    DrawingKind = property(get_DrawingKind, None)
    Center = property(get_Center, None)
    Points = property(get_Points, None)
class IInkAnalysisInkWord(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('4bd228ad-83af-4034-8f-3b-f8-68-7d-ff-f4-36')
    @winrt_commethod(6)
    def get_RecognizedText(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_TextAlternates(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    RecognizedText = property(get_RecognizedText, None)
    TextAlternates = property(get_TextAlternates, None)
class IInkAnalysisLine(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('a06d048d-2b8d-4754-ad-5a-d0-87-11-93-a9-56')
    @winrt_commethod(6)
    def get_RecognizedText(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_IndentLevel(self) -> Int32: ...
    RecognizedText = property(get_RecognizedText, None)
    IndentLevel = property(get_IndentLevel, None)
class IInkAnalysisListItem(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('b4e3c23f-c4c3-4c3a-a1-a6-9d-85-54-7e-e5-86')
    @winrt_commethod(6)
    def get_RecognizedText(self) -> WinRT_String: ...
    RecognizedText = property(get_RecognizedText, None)
class IInkAnalysisNode(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('30831f05-5f64-4a2c-ba-37-4f-48-87-87-95-74')
    @winrt_commethod(6)
    def get_Id(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_Kind(self) -> Windows.UI.Input.Inking.Analysis.InkAnalysisNodeKind: ...
    @winrt_commethod(8)
    def get_BoundingRect(self) -> Windows.Foundation.Rect: ...
    @winrt_commethod(9)
    def get_RotatedBoundingRect(self) -> Windows.Foundation.Collections.IVectorView[Windows.Foundation.Point]: ...
    @winrt_commethod(10)
    def get_Children(self) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Input.Inking.Analysis.IInkAnalysisNode]: ...
    @winrt_commethod(11)
    def get_Parent(self) -> Windows.UI.Input.Inking.Analysis.IInkAnalysisNode: ...
    @winrt_commethod(12)
    def GetStrokeIds(self) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    Id = property(get_Id, None)
    Kind = property(get_Kind, None)
    BoundingRect = property(get_BoundingRect, None)
    RotatedBoundingRect = property(get_RotatedBoundingRect, None)
    Children = property(get_Children, None)
    Parent = property(get_Parent, None)
class IInkAnalysisParagraph(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('d9ad045c-0cd1-4dd4-a6-8b-eb-1f-12-b3-d7-27')
    @winrt_commethod(6)
    def get_RecognizedText(self) -> WinRT_String: ...
    RecognizedText = property(get_RecognizedText, None)
class IInkAnalysisResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('8948ba79-a243-4aa3-a2-94-1f-98-bd-0f-f5-80')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.UI.Input.Inking.Analysis.InkAnalysisStatus: ...
    Status = property(get_Status, None)
class IInkAnalysisRoot(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('3fb6a3c4-2fde-4061-85-02-a9-0f-32-54-5b-84')
    @winrt_commethod(6)
    def get_RecognizedText(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def FindNodes(self, nodeKind: Windows.UI.Input.Inking.Analysis.InkAnalysisNodeKind) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Input.Inking.Analysis.IInkAnalysisNode]: ...
    RecognizedText = property(get_RecognizedText, None)
class IInkAnalysisWritingRegion(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('dd6d6231-bd16-4663-b5-ae-94-1d-30-43-ef-5b')
    @winrt_commethod(6)
    def get_RecognizedText(self) -> WinRT_String: ...
    RecognizedText = property(get_RecognizedText, None)
class IInkAnalyzer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('f12b8f95-0866-4dc5-8c-77-f8-86-14-df-e3-8c')
    @winrt_commethod(6)
    def get_AnalysisRoot(self) -> Windows.UI.Input.Inking.Analysis.InkAnalysisRoot: ...
    @winrt_commethod(7)
    def get_IsAnalyzing(self) -> Boolean: ...
    @winrt_commethod(8)
    def AddDataForStroke(self, stroke: Windows.UI.Input.Inking.InkStroke) -> Void: ...
    @winrt_commethod(9)
    def AddDataForStrokes(self, strokes: Windows.Foundation.Collections.IIterable[Windows.UI.Input.Inking.InkStroke]) -> Void: ...
    @winrt_commethod(10)
    def ClearDataForAllStrokes(self) -> Void: ...
    @winrt_commethod(11)
    def RemoveDataForStroke(self, strokeId: UInt32) -> Void: ...
    @winrt_commethod(12)
    def RemoveDataForStrokes(self, strokeIds: Windows.Foundation.Collections.IIterable[UInt32]) -> Void: ...
    @winrt_commethod(13)
    def ReplaceDataForStroke(self, stroke: Windows.UI.Input.Inking.InkStroke) -> Void: ...
    @winrt_commethod(14)
    def SetStrokeDataKind(self, strokeId: UInt32, strokeKind: Windows.UI.Input.Inking.Analysis.InkAnalysisStrokeKind) -> Void: ...
    @winrt_commethod(15)
    def AnalyzeAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.UI.Input.Inking.Analysis.InkAnalysisResult]: ...
    AnalysisRoot = property(get_AnalysisRoot, None)
    IsAnalyzing = property(get_IsAnalyzing, None)
class IInkAnalyzerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('29138686-1963-49d8-95-89-e1-43-84-c7-69-e3')
    @winrt_commethod(6)
    def CreateAnalyzer(self) -> Windows.UI.Input.Inking.Analysis.InkAnalyzer: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.Inking.Analysis.InkAnalysisInkBullet'
    @winrt_mixinmethod
    def get_RecognizedText(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisInkBullet) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> UInt32: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.UI.Input.Inking.Analysis.InkAnalysisNodeKind: ...
    @winrt_mixinmethod
    def get_BoundingRect(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_RotatedBoundingRect(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.Foundation.Collections.IVectorView[Windows.Foundation.Point]: ...
    @winrt_mixinmethod
    def get_Children(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Input.Inking.Analysis.IInkAnalysisNode]: ...
    @winrt_mixinmethod
    def get_Parent(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.UI.Input.Inking.Analysis.IInkAnalysisNode: ...
    @winrt_mixinmethod
    def GetStrokeIds(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    RecognizedText = property(get_RecognizedText, None)
    Id = property(get_Id, None)
    Kind = property(get_Kind, None)
    BoundingRect = property(get_BoundingRect, None)
    RotatedBoundingRect = property(get_RotatedBoundingRect, None)
    Children = property(get_Children, None)
    Parent = property(get_Parent, None)
class InkAnalysisInkDrawing(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.Inking.Analysis.InkAnalysisInkDrawing'
    @winrt_mixinmethod
    def get_DrawingKind(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisInkDrawing) -> Windows.UI.Input.Inking.Analysis.InkAnalysisDrawingKind: ...
    @winrt_mixinmethod
    def get_Center(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisInkDrawing) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Points(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisInkDrawing) -> Windows.Foundation.Collections.IVectorView[Windows.Foundation.Point]: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> UInt32: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.UI.Input.Inking.Analysis.InkAnalysisNodeKind: ...
    @winrt_mixinmethod
    def get_BoundingRect(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_RotatedBoundingRect(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.Foundation.Collections.IVectorView[Windows.Foundation.Point]: ...
    @winrt_mixinmethod
    def get_Children(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Input.Inking.Analysis.IInkAnalysisNode]: ...
    @winrt_mixinmethod
    def get_Parent(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.UI.Input.Inking.Analysis.IInkAnalysisNode: ...
    @winrt_mixinmethod
    def GetStrokeIds(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.Inking.Analysis.InkAnalysisInkWord'
    @winrt_mixinmethod
    def get_RecognizedText(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisInkWord) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TextAlternates(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisInkWord) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> UInt32: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.UI.Input.Inking.Analysis.InkAnalysisNodeKind: ...
    @winrt_mixinmethod
    def get_BoundingRect(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_RotatedBoundingRect(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.Foundation.Collections.IVectorView[Windows.Foundation.Point]: ...
    @winrt_mixinmethod
    def get_Children(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Input.Inking.Analysis.IInkAnalysisNode]: ...
    @winrt_mixinmethod
    def get_Parent(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.UI.Input.Inking.Analysis.IInkAnalysisNode: ...
    @winrt_mixinmethod
    def GetStrokeIds(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    RecognizedText = property(get_RecognizedText, None)
    TextAlternates = property(get_TextAlternates, None)
    Id = property(get_Id, None)
    Kind = property(get_Kind, None)
    BoundingRect = property(get_BoundingRect, None)
    RotatedBoundingRect = property(get_RotatedBoundingRect, None)
    Children = property(get_Children, None)
    Parent = property(get_Parent, None)
class InkAnalysisLine(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.Inking.Analysis.InkAnalysisLine'
    @winrt_mixinmethod
    def get_RecognizedText(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisLine) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IndentLevel(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisLine) -> Int32: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> UInt32: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.UI.Input.Inking.Analysis.InkAnalysisNodeKind: ...
    @winrt_mixinmethod
    def get_BoundingRect(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_RotatedBoundingRect(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.Foundation.Collections.IVectorView[Windows.Foundation.Point]: ...
    @winrt_mixinmethod
    def get_Children(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Input.Inking.Analysis.IInkAnalysisNode]: ...
    @winrt_mixinmethod
    def get_Parent(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.UI.Input.Inking.Analysis.IInkAnalysisNode: ...
    @winrt_mixinmethod
    def GetStrokeIds(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    RecognizedText = property(get_RecognizedText, None)
    IndentLevel = property(get_IndentLevel, None)
    Id = property(get_Id, None)
    Kind = property(get_Kind, None)
    BoundingRect = property(get_BoundingRect, None)
    RotatedBoundingRect = property(get_RotatedBoundingRect, None)
    Children = property(get_Children, None)
    Parent = property(get_Parent, None)
class InkAnalysisListItem(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.Inking.Analysis.InkAnalysisListItem'
    @winrt_mixinmethod
    def get_RecognizedText(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisListItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> UInt32: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.UI.Input.Inking.Analysis.InkAnalysisNodeKind: ...
    @winrt_mixinmethod
    def get_BoundingRect(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_RotatedBoundingRect(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.Foundation.Collections.IVectorView[Windows.Foundation.Point]: ...
    @winrt_mixinmethod
    def get_Children(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Input.Inking.Analysis.IInkAnalysisNode]: ...
    @winrt_mixinmethod
    def get_Parent(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.UI.Input.Inking.Analysis.IInkAnalysisNode: ...
    @winrt_mixinmethod
    def GetStrokeIds(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    RecognizedText = property(get_RecognizedText, None)
    Id = property(get_Id, None)
    Kind = property(get_Kind, None)
    BoundingRect = property(get_BoundingRect, None)
    RotatedBoundingRect = property(get_RotatedBoundingRect, None)
    Children = property(get_Children, None)
    Parent = property(get_Parent, None)
class InkAnalysisNode(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.Inking.Analysis.InkAnalysisNode'
    @winrt_mixinmethod
    def get_Id(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> UInt32: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.UI.Input.Inking.Analysis.InkAnalysisNodeKind: ...
    @winrt_mixinmethod
    def get_BoundingRect(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_RotatedBoundingRect(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.Foundation.Collections.IVectorView[Windows.Foundation.Point]: ...
    @winrt_mixinmethod
    def get_Children(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Input.Inking.Analysis.IInkAnalysisNode]: ...
    @winrt_mixinmethod
    def get_Parent(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.UI.Input.Inking.Analysis.IInkAnalysisNode: ...
    @winrt_mixinmethod
    def GetStrokeIds(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.Inking.Analysis.InkAnalysisParagraph'
    @winrt_mixinmethod
    def get_RecognizedText(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisParagraph) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> UInt32: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.UI.Input.Inking.Analysis.InkAnalysisNodeKind: ...
    @winrt_mixinmethod
    def get_BoundingRect(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_RotatedBoundingRect(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.Foundation.Collections.IVectorView[Windows.Foundation.Point]: ...
    @winrt_mixinmethod
    def get_Children(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Input.Inking.Analysis.IInkAnalysisNode]: ...
    @winrt_mixinmethod
    def get_Parent(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.UI.Input.Inking.Analysis.IInkAnalysisNode: ...
    @winrt_mixinmethod
    def GetStrokeIds(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    RecognizedText = property(get_RecognizedText, None)
    Id = property(get_Id, None)
    Kind = property(get_Kind, None)
    BoundingRect = property(get_BoundingRect, None)
    RotatedBoundingRect = property(get_RotatedBoundingRect, None)
    Children = property(get_Children, None)
    Parent = property(get_Parent, None)
class InkAnalysisResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.Inking.Analysis.InkAnalysisResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisResult) -> Windows.UI.Input.Inking.Analysis.InkAnalysisStatus: ...
    Status = property(get_Status, None)
class InkAnalysisRoot(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.Inking.Analysis.InkAnalysisRoot'
    @winrt_mixinmethod
    def get_RecognizedText(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisRoot) -> WinRT_String: ...
    @winrt_mixinmethod
    def FindNodes(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisRoot, nodeKind: Windows.UI.Input.Inking.Analysis.InkAnalysisNodeKind) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Input.Inking.Analysis.IInkAnalysisNode]: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> UInt32: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.UI.Input.Inking.Analysis.InkAnalysisNodeKind: ...
    @winrt_mixinmethod
    def get_BoundingRect(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_RotatedBoundingRect(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.Foundation.Collections.IVectorView[Windows.Foundation.Point]: ...
    @winrt_mixinmethod
    def get_Children(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Input.Inking.Analysis.IInkAnalysisNode]: ...
    @winrt_mixinmethod
    def get_Parent(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.UI.Input.Inking.Analysis.IInkAnalysisNode: ...
    @winrt_mixinmethod
    def GetStrokeIds(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.Inking.Analysis.InkAnalysisWritingRegion'
    @winrt_mixinmethod
    def get_RecognizedText(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisWritingRegion) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> UInt32: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.UI.Input.Inking.Analysis.InkAnalysisNodeKind: ...
    @winrt_mixinmethod
    def get_BoundingRect(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_RotatedBoundingRect(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.Foundation.Collections.IVectorView[Windows.Foundation.Point]: ...
    @winrt_mixinmethod
    def get_Children(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Input.Inking.Analysis.IInkAnalysisNode]: ...
    @winrt_mixinmethod
    def get_Parent(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.UI.Input.Inking.Analysis.IInkAnalysisNode: ...
    @winrt_mixinmethod
    def GetStrokeIds(self: Windows.UI.Input.Inking.Analysis.IInkAnalysisNode) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    RecognizedText = property(get_RecognizedText, None)
    Id = property(get_Id, None)
    Kind = property(get_Kind, None)
    BoundingRect = property(get_BoundingRect, None)
    RotatedBoundingRect = property(get_RotatedBoundingRect, None)
    Children = property(get_Children, None)
    Parent = property(get_Parent, None)
class InkAnalyzer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.Inking.Analysis.InkAnalyzer'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Input.Inking.Analysis.InkAnalyzer: ...
    @winrt_mixinmethod
    def get_AnalysisRoot(self: Windows.UI.Input.Inking.Analysis.IInkAnalyzer) -> Windows.UI.Input.Inking.Analysis.InkAnalysisRoot: ...
    @winrt_mixinmethod
    def get_IsAnalyzing(self: Windows.UI.Input.Inking.Analysis.IInkAnalyzer) -> Boolean: ...
    @winrt_mixinmethod
    def AddDataForStroke(self: Windows.UI.Input.Inking.Analysis.IInkAnalyzer, stroke: Windows.UI.Input.Inking.InkStroke) -> Void: ...
    @winrt_mixinmethod
    def AddDataForStrokes(self: Windows.UI.Input.Inking.Analysis.IInkAnalyzer, strokes: Windows.Foundation.Collections.IIterable[Windows.UI.Input.Inking.InkStroke]) -> Void: ...
    @winrt_mixinmethod
    def ClearDataForAllStrokes(self: Windows.UI.Input.Inking.Analysis.IInkAnalyzer) -> Void: ...
    @winrt_mixinmethod
    def RemoveDataForStroke(self: Windows.UI.Input.Inking.Analysis.IInkAnalyzer, strokeId: UInt32) -> Void: ...
    @winrt_mixinmethod
    def RemoveDataForStrokes(self: Windows.UI.Input.Inking.Analysis.IInkAnalyzer, strokeIds: Windows.Foundation.Collections.IIterable[UInt32]) -> Void: ...
    @winrt_mixinmethod
    def ReplaceDataForStroke(self: Windows.UI.Input.Inking.Analysis.IInkAnalyzer, stroke: Windows.UI.Input.Inking.InkStroke) -> Void: ...
    @winrt_mixinmethod
    def SetStrokeDataKind(self: Windows.UI.Input.Inking.Analysis.IInkAnalyzer, strokeId: UInt32, strokeKind: Windows.UI.Input.Inking.Analysis.InkAnalysisStrokeKind) -> Void: ...
    @winrt_mixinmethod
    def AnalyzeAsync(self: Windows.UI.Input.Inking.Analysis.IInkAnalyzer) -> Windows.Foundation.IAsyncOperation[Windows.UI.Input.Inking.Analysis.InkAnalysisResult]: ...
    AnalysisRoot = property(get_AnalysisRoot, None)
    IsAnalyzing = property(get_IsAnalyzing, None)
make_head(_module, 'IInkAnalysisInkBullet')
make_head(_module, 'IInkAnalysisInkDrawing')
make_head(_module, 'IInkAnalysisInkWord')
make_head(_module, 'IInkAnalysisLine')
make_head(_module, 'IInkAnalysisListItem')
make_head(_module, 'IInkAnalysisNode')
make_head(_module, 'IInkAnalysisParagraph')
make_head(_module, 'IInkAnalysisResult')
make_head(_module, 'IInkAnalysisRoot')
make_head(_module, 'IInkAnalysisWritingRegion')
make_head(_module, 'IInkAnalyzer')
make_head(_module, 'IInkAnalyzerFactory')
make_head(_module, 'InkAnalysisInkBullet')
make_head(_module, 'InkAnalysisInkDrawing')
make_head(_module, 'InkAnalysisInkWord')
make_head(_module, 'InkAnalysisLine')
make_head(_module, 'InkAnalysisListItem')
make_head(_module, 'InkAnalysisNode')
make_head(_module, 'InkAnalysisParagraph')
make_head(_module, 'InkAnalysisResult')
make_head(_module, 'InkAnalysisRoot')
make_head(_module, 'InkAnalysisWritingRegion')
make_head(_module, 'InkAnalyzer')
