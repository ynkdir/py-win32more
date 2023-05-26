from __future__ import annotations
from ctypes import POINTER
from Windows import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
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
CLSID_XMLGraphBuilder: Guid = Guid('{1bb05961-5fbf-11d2-a521-44df07c10000}')
class IXMLGraphBuilder(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1bb05960-5fbf-11d2-a521-44df07c10000}')
    @commethod(3)
    def BuildFromXML(self, pGraph: Windows.Win32.Media.DirectShow.IGraphBuilder_head, pxml: Windows.Win32.Data.Xml.MsXml.IXMLElement_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SaveToXML(self, pGraph: Windows.Win32.Media.DirectShow.IGraphBuilder_head, pbstrxml: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def BuildFromXMLFile(self, pGraph: Windows.Win32.Media.DirectShow.IGraphBuilder_head, wszFileName: Windows.Win32.Foundation.PWSTR, wszBaseURL: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'IXMLGraphBuilder')
