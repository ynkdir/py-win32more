from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Data.Xml.MsXml
import Windows.Win32.Foundation
import Windows.Win32.Media.DirectShow
import Windows.Win32.Media.DirectShow.Xml
import Windows.Win32.System.Com
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
CLSID_XMLGraphBuilder: Guid = Guid('1bb05961-5fbf-11d2-a5-21-44-df-07-c1-00-00')
class IXMLGraphBuilder(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1bb05960-5fbf-11d2-a5-21-44-df-07-c1-00-00')
    @commethod(3)
    def BuildFromXML(self, pGraph: Windows.Win32.Media.DirectShow.IGraphBuilder_head, pxml: Windows.Win32.Data.Xml.MsXml.IXMLElement_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SaveToXML(self, pGraph: Windows.Win32.Media.DirectShow.IGraphBuilder_head, pbstrxml: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def BuildFromXMLFile(self, pGraph: Windows.Win32.Media.DirectShow.IGraphBuilder_head, wszFileName: Windows.Win32.Foundation.PWSTR, wszBaseURL: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'IXMLGraphBuilder')
