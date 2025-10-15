from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Microsoft.Graphics.Imaging
import win32more.Microsoft.Windows.AI
import win32more.Microsoft.Windows.AI.ContentSafety
import win32more.Microsoft.Windows.AI.Imaging
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Graphics
import win32more.Windows.Graphics.Imaging
class IImageDescriptionGenerator(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.Imaging.IImageDescriptionGenerator'
    _iid_ = Guid('{576b989e-9829-5682-91b0-a7110fa7d51e}')
    @winrt_commethod(6)
    def DescribeAsync(self, image: win32more.Microsoft.Graphics.Imaging.ImageBuffer, kind: win32more.Microsoft.Windows.AI.Imaging.ImageDescriptionKind, contentFilterOptions: win32more.Microsoft.Windows.AI.ContentSafety.ContentFilterOptions) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.Imaging.ImageDescriptionResult, WinRT_String]: ...
class IImageDescriptionGeneratorStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.Imaging.IImageDescriptionGeneratorStatics'
    _iid_ = Guid('{5fb50b2a-5700-55a7-b413-6073b4b7f175}')
    @winrt_commethod(6)
    def GetReadyState(self) -> win32more.Microsoft.Windows.AI.AIFeatureReadyState: ...
    @winrt_commethod(7)
    def EnsureReadyAsync(self) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.AIFeatureReadyResult, Double]: ...
    @winrt_commethod(8)
    def CreateAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Windows.AI.Imaging.ImageDescriptionGenerator]: ...
class IImageDescriptionResult(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.Imaging.IImageDescriptionResult'
    _iid_ = Guid('{a066dd0c-110b-5275-a635-52bed7519a2f}')
    @winrt_commethod(6)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Status(self) -> win32more.Microsoft.Windows.AI.Imaging.ImageDescriptionResultStatus: ...
    Description = property(get_Description, None)
    Status = property(get_Status, None)
class IImageObjectExtractor(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.Imaging.IImageObjectExtractor'
    _iid_ = Guid('{2919fdc0-d772-5fd9-a8b7-ffb56010c99c}')
    @winrt_commethod(6)
    def GetSoftwareBitmapObjectMask(self, hint: win32more.Microsoft.Windows.AI.Imaging.ImageObjectExtractorHint) -> win32more.Windows.Graphics.Imaging.SoftwareBitmap: ...
    @winrt_commethod(7)
    def GetImageBufferObjectMask(self, hint: win32more.Microsoft.Windows.AI.Imaging.ImageObjectExtractorHint) -> win32more.Microsoft.Graphics.Imaging.ImageBuffer: ...
class IImageObjectExtractorHint(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.Imaging.IImageObjectExtractorHint'
    _iid_ = Guid('{1bd8d67c-8a7a-5fe7-98a5-cbdfeb509452}')
    @winrt_commethod(6)
    def get_IncludeRects(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Graphics.RectInt32]: ...
    @winrt_commethod(7)
    def get_IncludePoints(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Graphics.PointInt32]: ...
    @winrt_commethod(8)
    def get_ExcludePoints(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Graphics.PointInt32]: ...
    ExcludePoints = property(get_ExcludePoints, None)
    IncludePoints = property(get_IncludePoints, None)
    IncludeRects = property(get_IncludeRects, None)
class IImageObjectExtractorHintFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.Imaging.IImageObjectExtractorHintFactory'
    _iid_ = Guid('{5028f206-145d-5a70-9a51-e17e60cfbad8}')
    @winrt_commethod(6)
    def CreateInstance(self, includeRects: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Graphics.RectInt32], includePoints: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Graphics.PointInt32], excludePoints: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Graphics.PointInt32]) -> win32more.Microsoft.Windows.AI.Imaging.ImageObjectExtractorHint: ...
class IImageObjectExtractorStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.Imaging.IImageObjectExtractorStatics'
    _iid_ = Guid('{38fa261e-2c33-54cb-9e10-98d50685743d}')
    @winrt_commethod(6)
    def CreateWithSoftwareBitmapAsync(self, softwareBitmap: win32more.Windows.Graphics.Imaging.SoftwareBitmap) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Windows.AI.Imaging.ImageObjectExtractor]: ...
    @winrt_commethod(7)
    def CreateWithImageBufferAsync(self, imageBuffer: win32more.Microsoft.Graphics.Imaging.ImageBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Windows.AI.Imaging.ImageObjectExtractor]: ...
    @winrt_commethod(8)
    def GetReadyState(self) -> win32more.Microsoft.Windows.AI.AIFeatureReadyState: ...
    @winrt_commethod(9)
    def EnsureReadyAsync(self) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.AIFeatureReadyResult, Double]: ...
class IImageObjectRemover(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.Imaging.IImageObjectRemover'
    _iid_ = Guid('{cfa20faf-5ae1-5b8c-b0d8-e7c64db59d26}')
    @winrt_commethod(6)
    def RemoveFromSoftwareBitmap(self, softwareBitmap: win32more.Windows.Graphics.Imaging.SoftwareBitmap, softwareBitmapMask: win32more.Windows.Graphics.Imaging.SoftwareBitmap) -> win32more.Windows.Graphics.Imaging.SoftwareBitmap: ...
    @winrt_commethod(7)
    def RemoveFromImageBuffer(self, imageBuffer: win32more.Microsoft.Graphics.Imaging.ImageBuffer, imageBufferMask: win32more.Microsoft.Graphics.Imaging.ImageBuffer) -> win32more.Microsoft.Graphics.Imaging.ImageBuffer: ...
class IImageObjectRemoverStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.Imaging.IImageObjectRemoverStatics'
    _iid_ = Guid('{cbcbd7e1-5b81-503f-8fcb-66ae1d6e5b9c}')
    @winrt_commethod(6)
    def GetReadyState(self) -> win32more.Microsoft.Windows.AI.AIFeatureReadyState: ...
    @winrt_commethod(7)
    def EnsureReadyAsync(self) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.AIFeatureReadyResult, Double]: ...
    @winrt_commethod(8)
    def CreateAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Windows.AI.Imaging.ImageObjectRemover]: ...
class IImageScaler(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.Imaging.IImageScaler'
    _iid_ = Guid('{06eec88e-91c5-5326-8128-2807faafa571}')
    @winrt_commethod(6)
    def ScaleSoftwareBitmap(self, softwareBitmap: win32more.Windows.Graphics.Imaging.SoftwareBitmap, width: Int32, height: Int32) -> win32more.Windows.Graphics.Imaging.SoftwareBitmap: ...
    @winrt_commethod(7)
    def ScaleImageBuffer(self, imageBuffer: win32more.Microsoft.Graphics.Imaging.ImageBuffer, width: Int32, height: Int32) -> win32more.Microsoft.Graphics.Imaging.ImageBuffer: ...
    @winrt_commethod(8)
    def get_MaxSupportedScaleFactor(self) -> Int32: ...
    MaxSupportedScaleFactor = property(get_MaxSupportedScaleFactor, None)
class IImageScalerStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.Imaging.IImageScalerStatics'
    _iid_ = Guid('{75380c81-9c7f-544b-9337-6e638cfb464a}')
    @winrt_commethod(6)
    def GetReadyState(self) -> win32more.Microsoft.Windows.AI.AIFeatureReadyState: ...
    @winrt_commethod(7)
    def EnsureReadyAsync(self) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.AIFeatureReadyResult, Double]: ...
    @winrt_commethod(8)
    def CreateAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Windows.AI.Imaging.ImageScaler]: ...
class IRecognizedLine(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.Imaging.IRecognizedLine'
    _iid_ = Guid('{612a6be6-f6bb-53c9-84ce-f0a5e565faa7}')
    @winrt_commethod(6)
    def get_Text(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_BoundingBox(self) -> win32more.Microsoft.Windows.AI.Imaging.RecognizedTextBoundingBox: ...
    @winrt_commethod(8)
    def get_Words(self) -> ReceiveArray[win32more.Microsoft.Windows.AI.Imaging.RecognizedWord]: ...
    @winrt_commethod(9)
    def get_Style(self) -> win32more.Microsoft.Windows.AI.Imaging.RecognizedLineStyle: ...
    @winrt_commethod(10)
    def get_LineStyleConfidence(self) -> Single: ...
    BoundingBox = property(get_BoundingBox, None)
    LineStyleConfidence = property(get_LineStyleConfidence, None)
    Style = property(get_Style, None)
    Text = property(get_Text, None)
    Words = property(get_Words, None)
class IRecognizedText(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.Imaging.IRecognizedText'
    _iid_ = Guid('{ae4766d3-2924-57a6-b3d3-b866f59b9972}')
    @winrt_commethod(6)
    def get_Lines(self) -> ReceiveArray[win32more.Microsoft.Windows.AI.Imaging.RecognizedLine]: ...
    @winrt_commethod(7)
    def get_TextAngle(self) -> Single: ...
    Lines = property(get_Lines, None)
    TextAngle = property(get_TextAngle, None)
class IRecognizedWord(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.Imaging.IRecognizedWord'
    _iid_ = Guid('{6b53daab-3410-5088-826a-0788a1ee3b52}')
    @winrt_commethod(6)
    def get_Text(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_BoundingBox(self) -> win32more.Microsoft.Windows.AI.Imaging.RecognizedTextBoundingBox: ...
    @winrt_commethod(8)
    def get_MatchConfidence(self) -> Single: ...
    BoundingBox = property(get_BoundingBox, None)
    MatchConfidence = property(get_MatchConfidence, None)
    Text = property(get_Text, None)
class ITextRecognizer(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.Imaging.ITextRecognizer'
    _iid_ = Guid('{be7bf6c0-30f6-570d-bd92-3ffe5665d933}')
    @winrt_commethod(6)
    def RecognizeTextFromImageAsync(self, imageBuffer: win32more.Microsoft.Graphics.Imaging.ImageBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Windows.AI.Imaging.RecognizedText]: ...
    @winrt_commethod(7)
    def RecognizeTextFromImage(self, imageBuffer: win32more.Microsoft.Graphics.Imaging.ImageBuffer) -> win32more.Microsoft.Windows.AI.Imaging.RecognizedText: ...
class ITextRecognizerStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.Imaging.ITextRecognizerStatics'
    _iid_ = Guid('{3788c2fd-e496-53ab-85a7-e54a135824e9}')
    @winrt_commethod(6)
    def GetReadyState(self) -> win32more.Microsoft.Windows.AI.AIFeatureReadyState: ...
    @winrt_commethod(7)
    def EnsureReadyAsync(self) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.AIFeatureReadyResult, Double]: ...
    @winrt_commethod(8)
    def CreateAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Windows.AI.Imaging.TextRecognizer]: ...
ImageDescriptionContract: UInt32 = 65536
class ImageDescriptionGenerator(ComPtr):
    extends: IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Microsoft.Windows.AI.Imaging.IImageDescriptionGenerator
    _classid_ = 'Microsoft.Windows.AI.Imaging.ImageDescriptionGenerator'
    @winrt_mixinmethod
    def DescribeAsync(self: win32more.Microsoft.Windows.AI.Imaging.IImageDescriptionGenerator, image: win32more.Microsoft.Graphics.Imaging.ImageBuffer, kind: win32more.Microsoft.Windows.AI.Imaging.ImageDescriptionKind, contentFilterOptions: win32more.Microsoft.Windows.AI.ContentSafety.ContentFilterOptions) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.Imaging.ImageDescriptionResult, WinRT_String]: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def GetReadyState(cls: win32more.Microsoft.Windows.AI.Imaging.IImageDescriptionGeneratorStatics) -> win32more.Microsoft.Windows.AI.AIFeatureReadyState: ...
    @winrt_classmethod
    def EnsureReadyAsync(cls: win32more.Microsoft.Windows.AI.Imaging.IImageDescriptionGeneratorStatics) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.AIFeatureReadyResult, Double]: ...
    @winrt_classmethod
    def CreateAsync(cls: win32more.Microsoft.Windows.AI.Imaging.IImageDescriptionGeneratorStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Windows.AI.Imaging.ImageDescriptionGenerator]: ...
class ImageDescriptionKind(Enum, Int32):
    BriefDescription = 0
    DetailedDescription = 1
    DiagramDescription = 2
    AccessibleDescription = 3
class ImageDescriptionResult(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.AI.Imaging.IImageDescriptionResult
    _classid_ = 'Microsoft.Windows.AI.Imaging.ImageDescriptionResult'
    @winrt_mixinmethod
    def get_Description(self: win32more.Microsoft.Windows.AI.Imaging.IImageDescriptionResult) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Microsoft.Windows.AI.Imaging.IImageDescriptionResult) -> win32more.Microsoft.Windows.AI.Imaging.ImageDescriptionResultStatus: ...
    Description = property(get_Description, None)
    Status = property(get_Status, None)
class ImageDescriptionResultStatus(Enum, Int32):
    Complete = 0
    InProgress = 1
    BlockedByPolicy = 2
    ImageBlockedByContentModeration = 3
    TextInImageBlockedByContentModeration = 4
    DescriptionTextBlockedByContentModeration = 5
    ImageHasTooMuchText = 6
    InternalError = 7
class ImageObjectExtractor(ComPtr):
    extends: IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Microsoft.Windows.AI.Imaging.IImageObjectExtractor
    _classid_ = 'Microsoft.Windows.AI.Imaging.ImageObjectExtractor'
    @winrt_mixinmethod
    def GetSoftwareBitmapObjectMask(self: win32more.Microsoft.Windows.AI.Imaging.IImageObjectExtractor, hint: win32more.Microsoft.Windows.AI.Imaging.ImageObjectExtractorHint) -> win32more.Windows.Graphics.Imaging.SoftwareBitmap: ...
    @winrt_mixinmethod
    def GetImageBufferObjectMask(self: win32more.Microsoft.Windows.AI.Imaging.IImageObjectExtractor, hint: win32more.Microsoft.Windows.AI.Imaging.ImageObjectExtractorHint) -> win32more.Microsoft.Graphics.Imaging.ImageBuffer: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def CreateWithSoftwareBitmapAsync(cls: win32more.Microsoft.Windows.AI.Imaging.IImageObjectExtractorStatics, softwareBitmap: win32more.Windows.Graphics.Imaging.SoftwareBitmap) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Windows.AI.Imaging.ImageObjectExtractor]: ...
    @winrt_classmethod
    def CreateWithImageBufferAsync(cls: win32more.Microsoft.Windows.AI.Imaging.IImageObjectExtractorStatics, imageBuffer: win32more.Microsoft.Graphics.Imaging.ImageBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Windows.AI.Imaging.ImageObjectExtractor]: ...
    @winrt_classmethod
    def GetReadyState(cls: win32more.Microsoft.Windows.AI.Imaging.IImageObjectExtractorStatics) -> win32more.Microsoft.Windows.AI.AIFeatureReadyState: ...
    @winrt_classmethod
    def EnsureReadyAsync(cls: win32more.Microsoft.Windows.AI.Imaging.IImageObjectExtractorStatics) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.AIFeatureReadyResult, Double]: ...
ImageObjectExtractorContract: UInt32 = 65536
class ImageObjectExtractorHint(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.AI.Imaging.IImageObjectExtractorHint
    _classid_ = 'Microsoft.Windows.AI.Imaging.ImageObjectExtractorHint'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 3:
            super().__init__(move=win32more.Microsoft.Windows.AI.Imaging.ImageObjectExtractorHint.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.Windows.AI.Imaging.IImageObjectExtractorHintFactory, includeRects: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Graphics.RectInt32], includePoints: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Graphics.PointInt32], excludePoints: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Graphics.PointInt32]) -> win32more.Microsoft.Windows.AI.Imaging.ImageObjectExtractorHint: ...
    @winrt_mixinmethod
    def get_IncludeRects(self: win32more.Microsoft.Windows.AI.Imaging.IImageObjectExtractorHint) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Graphics.RectInt32]: ...
    @winrt_mixinmethod
    def get_IncludePoints(self: win32more.Microsoft.Windows.AI.Imaging.IImageObjectExtractorHint) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Graphics.PointInt32]: ...
    @winrt_mixinmethod
    def get_ExcludePoints(self: win32more.Microsoft.Windows.AI.Imaging.IImageObjectExtractorHint) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Graphics.PointInt32]: ...
    ExcludePoints = property(get_ExcludePoints, None)
    IncludePoints = property(get_IncludePoints, None)
    IncludeRects = property(get_IncludeRects, None)
class ImageObjectRemover(ComPtr):
    extends: IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Microsoft.Windows.AI.Imaging.IImageObjectRemover
    _classid_ = 'Microsoft.Windows.AI.Imaging.ImageObjectRemover'
    @winrt_mixinmethod
    def RemoveFromSoftwareBitmap(self: win32more.Microsoft.Windows.AI.Imaging.IImageObjectRemover, softwareBitmap: win32more.Windows.Graphics.Imaging.SoftwareBitmap, softwareBitmapMask: win32more.Windows.Graphics.Imaging.SoftwareBitmap) -> win32more.Windows.Graphics.Imaging.SoftwareBitmap: ...
    @winrt_mixinmethod
    def RemoveFromImageBuffer(self: win32more.Microsoft.Windows.AI.Imaging.IImageObjectRemover, imageBuffer: win32more.Microsoft.Graphics.Imaging.ImageBuffer, imageBufferMask: win32more.Microsoft.Graphics.Imaging.ImageBuffer) -> win32more.Microsoft.Graphics.Imaging.ImageBuffer: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def GetReadyState(cls: win32more.Microsoft.Windows.AI.Imaging.IImageObjectRemoverStatics) -> win32more.Microsoft.Windows.AI.AIFeatureReadyState: ...
    @winrt_classmethod
    def EnsureReadyAsync(cls: win32more.Microsoft.Windows.AI.Imaging.IImageObjectRemoverStatics) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.AIFeatureReadyResult, Double]: ...
    @winrt_classmethod
    def CreateAsync(cls: win32more.Microsoft.Windows.AI.Imaging.IImageObjectRemoverStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Windows.AI.Imaging.ImageObjectRemover]: ...
ImageObjectRemoverContract: UInt32 = 65536
class ImageScaler(ComPtr):
    extends: IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Microsoft.Windows.AI.Imaging.IImageScaler
    _classid_ = 'Microsoft.Windows.AI.Imaging.ImageScaler'
    @winrt_mixinmethod
    def ScaleSoftwareBitmap(self: win32more.Microsoft.Windows.AI.Imaging.IImageScaler, softwareBitmap: win32more.Windows.Graphics.Imaging.SoftwareBitmap, width: Int32, height: Int32) -> win32more.Windows.Graphics.Imaging.SoftwareBitmap: ...
    @winrt_mixinmethod
    def ScaleImageBuffer(self: win32more.Microsoft.Windows.AI.Imaging.IImageScaler, imageBuffer: win32more.Microsoft.Graphics.Imaging.ImageBuffer, width: Int32, height: Int32) -> win32more.Microsoft.Graphics.Imaging.ImageBuffer: ...
    @winrt_mixinmethod
    def get_MaxSupportedScaleFactor(self: win32more.Microsoft.Windows.AI.Imaging.IImageScaler) -> Int32: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def GetReadyState(cls: win32more.Microsoft.Windows.AI.Imaging.IImageScalerStatics) -> win32more.Microsoft.Windows.AI.AIFeatureReadyState: ...
    @winrt_classmethod
    def EnsureReadyAsync(cls: win32more.Microsoft.Windows.AI.Imaging.IImageScalerStatics) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.AIFeatureReadyResult, Double]: ...
    @winrt_classmethod
    def CreateAsync(cls: win32more.Microsoft.Windows.AI.Imaging.IImageScalerStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Windows.AI.Imaging.ImageScaler]: ...
    MaxSupportedScaleFactor = property(get_MaxSupportedScaleFactor, None)
ImageScalerContract: UInt32 = 65536
class RecognizedLine(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.AI.Imaging.IRecognizedLine
    _classid_ = 'Microsoft.Windows.AI.Imaging.RecognizedLine'
    @winrt_mixinmethod
    def get_Text(self: win32more.Microsoft.Windows.AI.Imaging.IRecognizedLine) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_BoundingBox(self: win32more.Microsoft.Windows.AI.Imaging.IRecognizedLine) -> win32more.Microsoft.Windows.AI.Imaging.RecognizedTextBoundingBox: ...
    @winrt_mixinmethod
    def get_Words(self: win32more.Microsoft.Windows.AI.Imaging.IRecognizedLine) -> ReceiveArray[win32more.Microsoft.Windows.AI.Imaging.RecognizedWord]: ...
    @winrt_mixinmethod
    def get_Style(self: win32more.Microsoft.Windows.AI.Imaging.IRecognizedLine) -> win32more.Microsoft.Windows.AI.Imaging.RecognizedLineStyle: ...
    @winrt_mixinmethod
    def get_LineStyleConfidence(self: win32more.Microsoft.Windows.AI.Imaging.IRecognizedLine) -> Single: ...
    BoundingBox = property(get_BoundingBox, None)
    LineStyleConfidence = property(get_LineStyleConfidence, None)
    Style = property(get_Style, None)
    Text = property(get_Text, None)
    Words = property(get_Words, None)
class RecognizedLineStyle(Enum, Int32):
    Handwritten = 0
class RecognizedText(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.AI.Imaging.IRecognizedText
    _classid_ = 'Microsoft.Windows.AI.Imaging.RecognizedText'
    @winrt_mixinmethod
    def get_Lines(self: win32more.Microsoft.Windows.AI.Imaging.IRecognizedText) -> ReceiveArray[win32more.Microsoft.Windows.AI.Imaging.RecognizedLine]: ...
    @winrt_mixinmethod
    def get_TextAngle(self: win32more.Microsoft.Windows.AI.Imaging.IRecognizedText) -> Single: ...
    Lines = property(get_Lines, None)
    TextAngle = property(get_TextAngle, None)
class RecognizedTextBoundingBox(Structure):
    BottomLeft: win32more.Windows.Foundation.Point
    BottomRight: win32more.Windows.Foundation.Point
    TopLeft: win32more.Windows.Foundation.Point
    TopRight: win32more.Windows.Foundation.Point
class RecognizedWord(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.AI.Imaging.IRecognizedWord
    _classid_ = 'Microsoft.Windows.AI.Imaging.RecognizedWord'
    @winrt_mixinmethod
    def get_Text(self: win32more.Microsoft.Windows.AI.Imaging.IRecognizedWord) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_BoundingBox(self: win32more.Microsoft.Windows.AI.Imaging.IRecognizedWord) -> win32more.Microsoft.Windows.AI.Imaging.RecognizedTextBoundingBox: ...
    @winrt_mixinmethod
    def get_MatchConfidence(self: win32more.Microsoft.Windows.AI.Imaging.IRecognizedWord) -> Single: ...
    BoundingBox = property(get_BoundingBox, None)
    MatchConfidence = property(get_MatchConfidence, None)
    Text = property(get_Text, None)
TextRecognitionContract: UInt32 = 65536
class TextRecognizer(ComPtr):
    extends: IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Microsoft.Windows.AI.Imaging.ITextRecognizer
    _classid_ = 'Microsoft.Windows.AI.Imaging.TextRecognizer'
    @winrt_mixinmethod
    def RecognizeTextFromImageAsync(self: win32more.Microsoft.Windows.AI.Imaging.ITextRecognizer, imageBuffer: win32more.Microsoft.Graphics.Imaging.ImageBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Windows.AI.Imaging.RecognizedText]: ...
    @winrt_mixinmethod
    def RecognizeTextFromImage(self: win32more.Microsoft.Windows.AI.Imaging.ITextRecognizer, imageBuffer: win32more.Microsoft.Graphics.Imaging.ImageBuffer) -> win32more.Microsoft.Windows.AI.Imaging.RecognizedText: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def GetReadyState(cls: win32more.Microsoft.Windows.AI.Imaging.ITextRecognizerStatics) -> win32more.Microsoft.Windows.AI.AIFeatureReadyState: ...
    @winrt_classmethod
    def EnsureReadyAsync(cls: win32more.Microsoft.Windows.AI.Imaging.ITextRecognizerStatics) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.AIFeatureReadyResult, Double]: ...
    @winrt_classmethod
    def CreateAsync(cls: win32more.Microsoft.Windows.AI.Imaging.ITextRecognizerStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Windows.AI.Imaging.TextRecognizer]: ...


make_ready(__name__)
