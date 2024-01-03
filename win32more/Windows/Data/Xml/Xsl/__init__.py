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
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 1:
            return win32more.Windows.Data.Xml.Xsl.XsltProcessor.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Data.Xml.Xsl.IXsltProcessorFactory, document: win32more.Windows.Data.Xml.Dom.XmlDocument) -> win32more.Windows.Data.Xml.Xsl.XsltProcessor: ...
    @winrt_mixinmethod
    def TransformToString(self: win32more.Windows.Data.Xml.Xsl.IXsltProcessor, inputNode: win32more.Windows.Data.Xml.Dom.IXmlNode) -> WinRT_String: ...
    @winrt_mixinmethod
    def TransformToDocument(self: win32more.Windows.Data.Xml.Xsl.IXsltProcessor2, inputNode: win32more.Windows.Data.Xml.Dom.IXmlNode) -> win32more.Windows.Data.Xml.Dom.XmlDocument: ...


make_ready(__name__)
