from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
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
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, EasyCastStructure, EasyCastUnion, ComPtr, make_ready
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Data.Xml.Dom
import win32more.Windows.Data.Xml.Xsl
class IXsltProcessor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Xml.Xsl.IXsltProcessor'
    _iid_ = Guid('{7b64703f-550c-48c6-a90f-93a5b964518f}')
    @winrt_commethod(6)
    def TransformToString(self, inputNode: win32more.Windows.Data.Xml.Dom.IXmlNode) -> WinRT_String: ...
class IXsltProcessor2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Xml.Xsl.IXsltProcessor2'
    _iid_ = Guid('{8da45c56-97a5-44cb-a8be-27d86280c70a}')
    @winrt_commethod(6)
    def TransformToDocument(self, inputNode: win32more.Windows.Data.Xml.Dom.IXmlNode) -> win32more.Windows.Data.Xml.Dom.XmlDocument: ...
class IXsltProcessorFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Xml.Xsl.IXsltProcessorFactory'
    _iid_ = Guid('{274146c0-9a51-4663-bf30-0ef742146f20}')
    @winrt_commethod(6)
    def CreateInstance(self, document: win32more.Windows.Data.Xml.Dom.XmlDocument) -> win32more.Windows.Data.Xml.Xsl.XsltProcessor: ...
class XsltProcessor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Data.Xml.Xsl.IXsltProcessor
    _classid_ = 'Windows.Data.Xml.Xsl.XsltProcessor'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs.get('allocate', False):
            return super().__init__(**kwargs)
        elif len(args) == 1:
            instance = win32more.Windows.Data.Xml.Xsl.XsltProcessor.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Data.Xml.Xsl.IXsltProcessorFactory, document: win32more.Windows.Data.Xml.Dom.XmlDocument) -> win32more.Windows.Data.Xml.Xsl.XsltProcessor: ...
    @winrt_mixinmethod
    def TransformToString(self: win32more.Windows.Data.Xml.Xsl.IXsltProcessor, inputNode: win32more.Windows.Data.Xml.Dom.IXmlNode) -> WinRT_String: ...
    @winrt_mixinmethod
    def TransformToDocument(self: win32more.Windows.Data.Xml.Xsl.IXsltProcessor2, inputNode: win32more.Windows.Data.Xml.Dom.IXmlNode) -> win32more.Windows.Data.Xml.Dom.XmlDocument: ...
make_ready(__name__)
