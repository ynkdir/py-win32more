from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Globalization
import win32more.Windows.Graphics.Imaging
import win32more.Windows.Media.Ocr
import win32more.Windows.Win32.System.WinRT
class IOcrEngine(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Ocr.IOcrEngine'
    _iid_ = Guid('{5a14bc41-5b76-3140-b680-8825562683ac}')
    @winrt_commethod(6)
    def RecognizeAsync(self, bitmap: win32more.Windows.Graphics.Imaging.SoftwareBitmap) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Ocr.OcrResult]: ...
    @winrt_commethod(7)
    def get_RecognizerLanguage(self) -> win32more.Windows.Globalization.Language: ...
    RecognizerLanguage = property(get_RecognizerLanguage, None)
class IOcrEngineStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Ocr.IOcrEngineStatics'
    _iid_ = Guid('{5bffa85a-3384-3540-9940-699120d428a8}')
    @winrt_commethod(6)
    def get_MaxImageDimension(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_AvailableRecognizerLanguages(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Globalization.Language]: ...
    @winrt_commethod(8)
    def IsLanguageSupported(self, language: win32more.Windows.Globalization.Language) -> Boolean: ...
    @winrt_commethod(9)
    def TryCreateFromLanguage(self, language: win32more.Windows.Globalization.Language) -> win32more.Windows.Media.Ocr.OcrEngine: ...
    @winrt_commethod(10)
    def TryCreateFromUserProfileLanguages(self) -> win32more.Windows.Media.Ocr.OcrEngine: ...
    AvailableRecognizerLanguages = property(get_AvailableRecognizerLanguages, None)
    MaxImageDimension = property(get_MaxImageDimension, None)
class IOcrLine(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Ocr.IOcrLine'
    _iid_ = Guid('{0043a16f-e31f-3a24-899c-d444bd088124}')
    @winrt_commethod(6)
    def get_Words(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Ocr.OcrWord]: ...
    @winrt_commethod(7)
    def get_Text(self) -> WinRT_String: ...
    Text = property(get_Text, None)
    Words = property(get_Words, None)
class IOcrResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Ocr.IOcrResult'
    _iid_ = Guid('{9bd235b2-175b-3d6a-92e2-388c206e2f63}')
    @winrt_commethod(6)
    def get_Lines(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Ocr.OcrLine]: ...
    @winrt_commethod(7)
    def get_TextAngle(self) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(8)
    def get_Text(self) -> WinRT_String: ...
    Lines = property(get_Lines, None)
    Text = property(get_Text, None)
    TextAngle = property(get_TextAngle, None)
class IOcrWord(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Ocr.IOcrWord'
    _iid_ = Guid('{3c2a477a-5cd9-3525-ba2a-23d1e0a68a1d}')
    @winrt_commethod(6)
    def get_BoundingRect(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(7)
    def get_Text(self) -> WinRT_String: ...
    BoundingRect = property(get_BoundingRect, None)
    Text = property(get_Text, None)
class _OcrEngine_Meta_(ComPtr.__class__):
    pass
class OcrEngine(ComPtr, metaclass=_OcrEngine_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Ocr.IOcrEngine
    _classid_ = 'Windows.Media.Ocr.OcrEngine'
    @winrt_mixinmethod
    def RecognizeAsync(self: win32more.Windows.Media.Ocr.IOcrEngine, bitmap: win32more.Windows.Graphics.Imaging.SoftwareBitmap) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Ocr.OcrResult]: ...
    @winrt_mixinmethod
    def get_RecognizerLanguage(self: win32more.Windows.Media.Ocr.IOcrEngine) -> win32more.Windows.Globalization.Language: ...
    @winrt_classmethod
    def get_MaxImageDimension(cls: win32more.Windows.Media.Ocr.IOcrEngineStatics) -> UInt32: ...
    @winrt_classmethod
    def get_AvailableRecognizerLanguages(cls: win32more.Windows.Media.Ocr.IOcrEngineStatics) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Globalization.Language]: ...
    @winrt_classmethod
    def IsLanguageSupported(cls: win32more.Windows.Media.Ocr.IOcrEngineStatics, language: win32more.Windows.Globalization.Language) -> Boolean: ...
    @winrt_classmethod
    def TryCreateFromLanguage(cls: win32more.Windows.Media.Ocr.IOcrEngineStatics, language: win32more.Windows.Globalization.Language) -> win32more.Windows.Media.Ocr.OcrEngine: ...
    @winrt_classmethod
    def TryCreateFromUserProfileLanguages(cls: win32more.Windows.Media.Ocr.IOcrEngineStatics) -> win32more.Windows.Media.Ocr.OcrEngine: ...
    RecognizerLanguage = property(get_RecognizerLanguage, None)
    _OcrEngine_Meta_.AvailableRecognizerLanguages = property(get_AvailableRecognizerLanguages, None)
    _OcrEngine_Meta_.MaxImageDimension = property(get_MaxImageDimension, None)
class OcrLine(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Ocr.IOcrLine
    _classid_ = 'Windows.Media.Ocr.OcrLine'
    @winrt_mixinmethod
    def get_Words(self: win32more.Windows.Media.Ocr.IOcrLine) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Ocr.OcrWord]: ...
    @winrt_mixinmethod
    def get_Text(self: win32more.Windows.Media.Ocr.IOcrLine) -> WinRT_String: ...
    Text = property(get_Text, None)
    Words = property(get_Words, None)
class OcrResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Ocr.IOcrResult
    _classid_ = 'Windows.Media.Ocr.OcrResult'
    @winrt_mixinmethod
    def get_Lines(self: win32more.Windows.Media.Ocr.IOcrResult) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Ocr.OcrLine]: ...
    @winrt_mixinmethod
    def get_TextAngle(self: win32more.Windows.Media.Ocr.IOcrResult) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_Text(self: win32more.Windows.Media.Ocr.IOcrResult) -> WinRT_String: ...
    Lines = property(get_Lines, None)
    Text = property(get_Text, None)
    TextAngle = property(get_TextAngle, None)
class OcrWord(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Ocr.IOcrWord
    _classid_ = 'Windows.Media.Ocr.OcrWord'
    @winrt_mixinmethod
    def get_BoundingRect(self: win32more.Windows.Media.Ocr.IOcrWord) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_Text(self: win32more.Windows.Media.Ocr.IOcrWord) -> WinRT_String: ...
    BoundingRect = property(get_BoundingRect, None)
    Text = property(get_Text, None)


make_ready(__name__)
