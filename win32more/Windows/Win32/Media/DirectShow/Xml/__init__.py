from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Data.Xml.MsXml
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Media.DirectShow
import win32more.Windows.Win32.Media.DirectShow.Xml
import win32more.Windows.Win32.System.Com
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
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1bb05960-5fbf-11d2-a521-44df07c10000}')
    @commethod(3)
    def BuildFromXML(self, pGraph: win32more.Windows.Win32.Media.DirectShow.IGraphBuilder_head, pxml: win32more.Windows.Win32.Data.Xml.MsXml.IXMLElement_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SaveToXML(self, pGraph: win32more.Windows.Win32.Media.DirectShow.IGraphBuilder_head, pbstrxml: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def BuildFromXMLFile(self, pGraph: win32more.Windows.Win32.Media.DirectShow.IGraphBuilder_head, wszFileName: win32more.Windows.Win32.Foundation.PWSTR, wszBaseURL: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'IXMLGraphBuilder')
