from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Data.Xml.Dom
import win32more.Windows.Data.Xml.Xsl
import win32more.Windows.Win32.System.WinRT
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
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Data.Xml.Xsl.XsltProcessor.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Data.Xml.Xsl.IXsltProcessorFactory, document: win32more.Windows.Data.Xml.Dom.XmlDocument) -> win32more.Windows.Data.Xml.Xsl.XsltProcessor: ...
    @winrt_mixinmethod
    def TransformToString(self: win32more.Windows.Data.Xml.Xsl.IXsltProcessor, inputNode: win32more.Windows.Data.Xml.Dom.IXmlNode) -> WinRT_String: ...
    @winrt_mixinmethod
    def TransformToDocument(self: win32more.Windows.Data.Xml.Xsl.IXsltProcessor2, inputNode: win32more.Windows.Data.Xml.Dom.IXmlNode) -> win32more.Windows.Data.Xml.Dom.XmlDocument: ...


make_ready(__name__)
