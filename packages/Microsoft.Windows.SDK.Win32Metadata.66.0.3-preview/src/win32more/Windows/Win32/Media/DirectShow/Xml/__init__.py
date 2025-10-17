from __future__ import annotations
from win32more.win32.prelude import *
import win32more.Windows.Win32.Data.Xml.MsXml
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Media.DirectShow
import win32more.Windows.Win32.Media.DirectShow.Xml
import win32more.Windows.Win32.System.Com
CLSID_XMLGraphBuilder: Guid = Guid('{1bb05961-5fbf-11d2-a521-44df07c10000}')
class IXMLGraphBuilder(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1bb05960-5fbf-11d2-a521-44df07c10000}')
    @commethod(3)
    def BuildFromXML(self, pGraph: win32more.Windows.Win32.Media.DirectShow.IGraphBuilder, pxml: win32more.Windows.Win32.Data.Xml.MsXml.IXMLElement) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SaveToXML(self, pGraph: win32more.Windows.Win32.Media.DirectShow.IGraphBuilder, pbstrxml: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def BuildFromXMLFile(self, pGraph: win32more.Windows.Win32.Media.DirectShow.IGraphBuilder, wszFileName: win32more.Windows.Win32.Foundation.PWSTR, wszBaseURL: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...


make_ready(__name__)
