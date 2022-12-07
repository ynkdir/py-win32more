from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Data.Xml.MsXml
import win32more.Foundation
import win32more.Media.DirectShow
import win32more.Media.DirectShow.Xml
import win32more.System.Com
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
CLSID_XMLGraphBuilder: Guid = Guid('1bb05961-5fbf-11d2-a5-21-44-df-07-c1-00-00')
class IXMLGraphBuilder(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('1bb05960-5fbf-11d2-a5-21-44-df-07-c1-00-00')
    @commethod(3)
    def BuildFromXML(pGraph: win32more.Media.DirectShow.IGraphBuilder_head, pxml: win32more.Data.Xml.MsXml.IXMLElement_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SaveToXML(pGraph: win32more.Media.DirectShow.IGraphBuilder_head, pbstrxml: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def BuildFromXMLFile(pGraph: win32more.Media.DirectShow.IGraphBuilder_head, wszFileName: win32more.Foundation.PWSTR, wszBaseURL: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
make_head(_module, 'IXMLGraphBuilder')
__all__ = [
    "CLSID_XMLGraphBuilder",
    "IXMLGraphBuilder",
]
