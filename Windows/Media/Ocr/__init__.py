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
import Windows.Globalization
import Windows.Graphics.Imaging
import Windows.Media.Ocr
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IOcrEngine(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('5a14bc41-5b76-3140-b6-80-88-25-56-26-83-ac')
    @winrt_commethod(6)
    def RecognizeAsync(self, bitmap: Windows.Graphics.Imaging.SoftwareBitmap) -> Windows.Foundation.IAsyncOperation[Windows.Media.Ocr.OcrResult]: ...
    @winrt_commethod(7)
    def get_RecognizerLanguage(self) -> Windows.Globalization.Language: ...
    RecognizerLanguage = property(get_RecognizerLanguage, None)
class IOcrEngineStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('5bffa85a-3384-3540-99-40-69-91-20-d4-28-a8')
    @winrt_commethod(6)
    def get_MaxImageDimension(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_AvailableRecognizerLanguages(self) -> Windows.Foundation.Collections.IVectorView[Windows.Globalization.Language]: ...
    @winrt_commethod(8)
    def IsLanguageSupported(self, language: Windows.Globalization.Language) -> Boolean: ...
    @winrt_commethod(9)
    def TryCreateFromLanguage(self, language: Windows.Globalization.Language) -> Windows.Media.Ocr.OcrEngine: ...
    @winrt_commethod(10)
    def TryCreateFromUserProfileLanguages(self) -> Windows.Media.Ocr.OcrEngine: ...
    MaxImageDimension = property(get_MaxImageDimension, None)
    AvailableRecognizerLanguages = property(get_AvailableRecognizerLanguages, None)
class IOcrLine(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('0043a16f-e31f-3a24-89-9c-d4-44-bd-08-81-24')
    @winrt_commethod(6)
    def get_Words(self) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Ocr.OcrWord]: ...
    @winrt_commethod(7)
    def get_Text(self) -> WinRT_String: ...
    Words = property(get_Words, None)
    Text = property(get_Text, None)
class IOcrResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('9bd235b2-175b-3d6a-92-e2-38-8c-20-6e-2f-63')
    @winrt_commethod(6)
    def get_Lines(self) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Ocr.OcrLine]: ...
    @winrt_commethod(7)
    def get_TextAngle(self) -> Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(8)
    def get_Text(self) -> WinRT_String: ...
    Lines = property(get_Lines, None)
    TextAngle = property(get_TextAngle, None)
    Text = property(get_Text, None)
class IOcrWord(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('3c2a477a-5cd9-3525-ba-2a-23-d1-e0-a6-8a-1d')
    @winrt_commethod(6)
    def get_BoundingRect(self) -> Windows.Foundation.Rect: ...
    @winrt_commethod(7)
    def get_Text(self) -> WinRT_String: ...
    BoundingRect = property(get_BoundingRect, None)
    Text = property(get_Text, None)
class OcrEngine(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Ocr.OcrEngine'
    @winrt_mixinmethod
    def RecognizeAsync(self: Windows.Media.Ocr.IOcrEngine, bitmap: Windows.Graphics.Imaging.SoftwareBitmap) -> Windows.Foundation.IAsyncOperation[Windows.Media.Ocr.OcrResult]: ...
    @winrt_mixinmethod
    def get_RecognizerLanguage(self: Windows.Media.Ocr.IOcrEngine) -> Windows.Globalization.Language: ...
    @winrt_classmethod
    def get_MaxImageDimension(cls: Windows.Media.Ocr.IOcrEngineStatics) -> UInt32: ...
    @winrt_classmethod
    def get_AvailableRecognizerLanguages(cls: Windows.Media.Ocr.IOcrEngineStatics) -> Windows.Foundation.Collections.IVectorView[Windows.Globalization.Language]: ...
    @winrt_classmethod
    def IsLanguageSupported(cls: Windows.Media.Ocr.IOcrEngineStatics, language: Windows.Globalization.Language) -> Boolean: ...
    @winrt_classmethod
    def TryCreateFromLanguage(cls: Windows.Media.Ocr.IOcrEngineStatics, language: Windows.Globalization.Language) -> Windows.Media.Ocr.OcrEngine: ...
    @winrt_classmethod
    def TryCreateFromUserProfileLanguages(cls: Windows.Media.Ocr.IOcrEngineStatics) -> Windows.Media.Ocr.OcrEngine: ...
    RecognizerLanguage = property(get_RecognizerLanguage, None)
    MaxImageDimension = property(get_MaxImageDimension, None)
    AvailableRecognizerLanguages = property(get_AvailableRecognizerLanguages, None)
class OcrLine(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Ocr.OcrLine'
    @winrt_mixinmethod
    def get_Words(self: Windows.Media.Ocr.IOcrLine) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Ocr.OcrWord]: ...
    @winrt_mixinmethod
    def get_Text(self: Windows.Media.Ocr.IOcrLine) -> WinRT_String: ...
    Words = property(get_Words, None)
    Text = property(get_Text, None)
class OcrResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Ocr.OcrResult'
    @winrt_mixinmethod
    def get_Lines(self: Windows.Media.Ocr.IOcrResult) -> Windows.Foundation.Collections.IVectorView[Windows.Media.Ocr.OcrLine]: ...
    @winrt_mixinmethod
    def get_TextAngle(self: Windows.Media.Ocr.IOcrResult) -> Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_Text(self: Windows.Media.Ocr.IOcrResult) -> WinRT_String: ...
    Lines = property(get_Lines, None)
    TextAngle = property(get_TextAngle, None)
    Text = property(get_Text, None)
class OcrWord(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Ocr.OcrWord'
    @winrt_mixinmethod
    def get_BoundingRect(self: Windows.Media.Ocr.IOcrWord) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_Text(self: Windows.Media.Ocr.IOcrWord) -> WinRT_String: ...
    BoundingRect = property(get_BoundingRect, None)
    Text = property(get_Text, None)
make_head(_module, 'IOcrEngine')
make_head(_module, 'IOcrEngineStatics')
make_head(_module, 'IOcrLine')
make_head(_module, 'IOcrResult')
make_head(_module, 'IOcrWord')
make_head(_module, 'OcrEngine')
make_head(_module, 'OcrLine')
make_head(_module, 'OcrResult')
make_head(_module, 'OcrWord')
