from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Data.Xml.XmlLite
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Com
@winfunctype('XmlLite.dll')
def CreateXmlReader(riid: POINTER(Guid), ppvObject: POINTER(VoidPtr), pMalloc: win32more.Windows.Win32.System.Com.IMalloc) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('XmlLite.dll')
def CreateXmlReaderInputWithEncodingCodePage(pInputStream: win32more.Windows.Win32.System.Com.IUnknown, pMalloc: win32more.Windows.Win32.System.Com.IMalloc, nEncodingCodePage: UInt32, fEncodingHint: win32more.Windows.Win32.Foundation.BOOL, pwszBaseUri: win32more.Windows.Win32.Foundation.PWSTR, ppInput: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('XmlLite.dll')
def CreateXmlReaderInputWithEncodingName(pInputStream: win32more.Windows.Win32.System.Com.IUnknown, pMalloc: win32more.Windows.Win32.System.Com.IMalloc, pwszEncodingName: win32more.Windows.Win32.Foundation.PWSTR, fEncodingHint: win32more.Windows.Win32.Foundation.BOOL, pwszBaseUri: win32more.Windows.Win32.Foundation.PWSTR, ppInput: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('XmlLite.dll')
def CreateXmlWriter(riid: POINTER(Guid), ppvObject: POINTER(VoidPtr), pMalloc: win32more.Windows.Win32.System.Com.IMalloc) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('XmlLite.dll')
def CreateXmlWriterOutputWithEncodingCodePage(pOutputStream: win32more.Windows.Win32.System.Com.IUnknown, pMalloc: win32more.Windows.Win32.System.Com.IMalloc, nEncodingCodePage: UInt32, ppOutput: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('XmlLite.dll')
def CreateXmlWriterOutputWithEncodingName(pOutputStream: win32more.Windows.Win32.System.Com.IUnknown, pMalloc: win32more.Windows.Win32.System.Com.IMalloc, pwszEncodingName: win32more.Windows.Win32.Foundation.PWSTR, ppOutput: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
DtdProcessing = Int32
DtdProcessing_Prohibit: win32more.Windows.Win32.Data.Xml.XmlLite.DtdProcessing = 0
DtdProcessing_Parse: win32more.Windows.Win32.Data.Xml.XmlLite.DtdProcessing = 1
_DtdProcessing_Last: win32more.Windows.Win32.Data.Xml.XmlLite.DtdProcessing = 1
class IXmlReader(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7279fc81-709d-4095-b63d-69fe4b0d9030}')
    @commethod(3)
    def SetInput(self, pInput: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetProperty(self, nProperty: UInt32, ppValue: POINTER(IntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetProperty(self, nProperty: UInt32, pValue: IntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Read(self, pNodeType: POINTER(win32more.Windows.Win32.Data.Xml.XmlLite.XmlNodeType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetNodeType(self, pNodeType: POINTER(win32more.Windows.Win32.Data.Xml.XmlLite.XmlNodeType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def MoveToFirstAttribute(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def MoveToNextAttribute(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def MoveToAttributeByName(self, pwszLocalName: win32more.Windows.Win32.Foundation.PWSTR, pwszNamespaceUri: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def MoveToElement(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetQualifiedName(self, ppwszQualifiedName: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pcwchQualifiedName: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetNamespaceUri(self, ppwszNamespaceUri: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pcwchNamespaceUri: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetLocalName(self, ppwszLocalName: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pcwchLocalName: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetPrefix(self, ppwszPrefix: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pcwchPrefix: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetValue(self, ppwszValue: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pcwchValue: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def ReadValueChunk(self, pwchBuffer: win32more.Windows.Win32.Foundation.PWSTR, cwchChunkSize: UInt32, pcwchRead: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetBaseUri(self, ppwszBaseUri: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pcwchBaseUri: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def IsDefault(self) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(20)
    def IsEmptyElement(self) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(21)
    def GetLineNumber(self, pnLineNumber: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetLinePosition(self, pnLinePosition: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetAttributeCount(self, pnAttributeCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetDepth(self, pnDepth: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def IsEOF(self) -> win32more.Windows.Win32.Foundation.BOOL: ...
class IXmlResolver(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7279fc82-709d-4095-b63d-69fe4b0d9030}')
    @commethod(3)
    def ResolveUri(self, pwszBaseUri: win32more.Windows.Win32.Foundation.PWSTR, pwszPublicIdentifier: win32more.Windows.Win32.Foundation.PWSTR, pwszSystemIdentifier: win32more.Windows.Win32.Foundation.PWSTR, ppResolvedInput: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IXmlWriter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7279fc88-709d-4095-b63d-69fe4b0d9030}')
    @commethod(3)
    def SetOutput(self, pOutput: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetProperty(self, nProperty: UInt32, ppValue: POINTER(IntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetProperty(self, nProperty: UInt32, pValue: IntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def WriteAttributes(self, pReader: win32more.Windows.Win32.Data.Xml.XmlLite.IXmlReader, fWriteDefaultAttributes: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def WriteAttributeString(self, pwszPrefix: win32more.Windows.Win32.Foundation.PWSTR, pwszLocalName: win32more.Windows.Win32.Foundation.PWSTR, pwszNamespaceUri: win32more.Windows.Win32.Foundation.PWSTR, pwszValue: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def WriteCData(self, pwszText: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def WriteCharEntity(self, wch: Char) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def WriteChars(self, pwch: win32more.Windows.Win32.Foundation.PWSTR, cwch: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def WriteComment(self, pwszComment: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def WriteDocType(self, pwszName: win32more.Windows.Win32.Foundation.PWSTR, pwszPublicId: win32more.Windows.Win32.Foundation.PWSTR, pwszSystemId: win32more.Windows.Win32.Foundation.PWSTR, pwszSubset: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def WriteElementString(self, pwszPrefix: win32more.Windows.Win32.Foundation.PWSTR, pwszLocalName: win32more.Windows.Win32.Foundation.PWSTR, pwszNamespaceUri: win32more.Windows.Win32.Foundation.PWSTR, pwszValue: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def WriteEndDocument(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def WriteEndElement(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def WriteEntityRef(self, pwszName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def WriteFullEndElement(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def WriteName(self, pwszName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def WriteNmToken(self, pwszNmToken: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def WriteNode(self, pReader: win32more.Windows.Win32.Data.Xml.XmlLite.IXmlReader, fWriteDefaultAttributes: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def WriteNodeShallow(self, pReader: win32more.Windows.Win32.Data.Xml.XmlLite.IXmlReader, fWriteDefaultAttributes: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def WriteProcessingInstruction(self, pwszName: win32more.Windows.Win32.Foundation.PWSTR, pwszText: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def WriteQualifiedName(self, pwszLocalName: win32more.Windows.Win32.Foundation.PWSTR, pwszNamespaceUri: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def WriteRaw(self, pwszData: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def WriteRawChars(self, pwch: win32more.Windows.Win32.Foundation.PWSTR, cwch: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def WriteStartDocument(self, standalone: win32more.Windows.Win32.Data.Xml.XmlLite.XmlStandalone) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def WriteStartElement(self, pwszPrefix: win32more.Windows.Win32.Foundation.PWSTR, pwszLocalName: win32more.Windows.Win32.Foundation.PWSTR, pwszNamespaceUri: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def WriteString(self, pwszText: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def WriteSurrogateCharEntity(self, wchLow: Char, wchHigh: Char) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def WriteWhitespace(self, pwszWhitespace: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def Flush(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IXmlWriterLite(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{862494c6-1310-4aad-b3cd-2dbeebf670d3}')
    @commethod(3)
    def SetOutput(self, pOutput: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetProperty(self, nProperty: UInt32, ppValue: POINTER(IntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetProperty(self, nProperty: UInt32, pValue: IntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def WriteAttributes(self, pReader: win32more.Windows.Win32.Data.Xml.XmlLite.IXmlReader, fWriteDefaultAttributes: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def WriteAttributeString(self, pwszQName: win32more.Windows.Win32.Foundation.PWSTR, cwszQName: UInt32, pwszValue: win32more.Windows.Win32.Foundation.PWSTR, cwszValue: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def WriteCData(self, pwszText: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def WriteCharEntity(self, wch: Char) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def WriteChars(self, pwch: win32more.Windows.Win32.Foundation.PWSTR, cwch: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def WriteComment(self, pwszComment: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def WriteDocType(self, pwszName: win32more.Windows.Win32.Foundation.PWSTR, pwszPublicId: win32more.Windows.Win32.Foundation.PWSTR, pwszSystemId: win32more.Windows.Win32.Foundation.PWSTR, pwszSubset: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def WriteElementString(self, pwszQName: win32more.Windows.Win32.Foundation.PWSTR, cwszQName: UInt32, pwszValue: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def WriteEndDocument(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def WriteEndElement(self, pwszQName: win32more.Windows.Win32.Foundation.PWSTR, cwszQName: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def WriteEntityRef(self, pwszName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def WriteFullEndElement(self, pwszQName: win32more.Windows.Win32.Foundation.PWSTR, cwszQName: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def WriteName(self, pwszName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def WriteNmToken(self, pwszNmToken: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def WriteNode(self, pReader: win32more.Windows.Win32.Data.Xml.XmlLite.IXmlReader, fWriteDefaultAttributes: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def WriteNodeShallow(self, pReader: win32more.Windows.Win32.Data.Xml.XmlLite.IXmlReader, fWriteDefaultAttributes: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def WriteProcessingInstruction(self, pwszName: win32more.Windows.Win32.Foundation.PWSTR, pwszText: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def WriteRaw(self, pwszData: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def WriteRawChars(self, pwch: win32more.Windows.Win32.Foundation.PWSTR, cwch: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def WriteStartDocument(self, standalone: win32more.Windows.Win32.Data.Xml.XmlLite.XmlStandalone) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def WriteStartElement(self, pwszQName: win32more.Windows.Win32.Foundation.PWSTR, cwszQName: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def WriteString(self, pwszText: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def WriteSurrogateCharEntity(self, wchLow: Char, wchHigh: Char) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def WriteWhitespace(self, pwszWhitespace: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def Flush(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
XmlConformanceLevel = Int32
XmlConformanceLevel_Auto: win32more.Windows.Win32.Data.Xml.XmlLite.XmlConformanceLevel = 0
XmlConformanceLevel_Fragment: win32more.Windows.Win32.Data.Xml.XmlLite.XmlConformanceLevel = 1
XmlConformanceLevel_Document: win32more.Windows.Win32.Data.Xml.XmlLite.XmlConformanceLevel = 2
_XmlConformanceLevel_Last: win32more.Windows.Win32.Data.Xml.XmlLite.XmlConformanceLevel = 2
XmlError = Int32
MX_E_MX: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894464
MX_E_INPUTEND: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894463
MX_E_ENCODING: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894462
MX_E_ENCODINGSWITCH: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894461
MX_E_ENCODINGSIGNATURE: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894460
WC_E_WC: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894432
WC_E_WHITESPACE: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894431
WC_E_SEMICOLON: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894430
WC_E_GREATERTHAN: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894429
WC_E_QUOTE: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894428
WC_E_EQUAL: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894427
WC_E_LESSTHAN: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894426
WC_E_HEXDIGIT: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894425
WC_E_DIGIT: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894424
WC_E_LEFTBRACKET: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894423
WC_E_LEFTPAREN: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894422
WC_E_XMLCHARACTER: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894421
WC_E_NAMECHARACTER: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894420
WC_E_SYNTAX: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894419
WC_E_CDSECT: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894418
WC_E_COMMENT: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894417
WC_E_CONDSECT: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894416
WC_E_DECLATTLIST: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894415
WC_E_DECLDOCTYPE: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894414
WC_E_DECLELEMENT: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894413
WC_E_DECLENTITY: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894412
WC_E_DECLNOTATION: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894411
WC_E_NDATA: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894410
WC_E_PUBLIC: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894409
WC_E_SYSTEM: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894408
WC_E_NAME: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894407
WC_E_ROOTELEMENT: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894406
WC_E_ELEMENTMATCH: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894405
WC_E_UNIQUEATTRIBUTE: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894404
WC_E_TEXTXMLDECL: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894403
WC_E_LEADINGXML: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894402
WC_E_TEXTDECL: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894401
WC_E_XMLDECL: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894400
WC_E_ENCNAME: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894399
WC_E_PUBLICID: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894398
WC_E_PESINTERNALSUBSET: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894397
WC_E_PESBETWEENDECLS: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894396
WC_E_NORECURSION: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894395
WC_E_ENTITYCONTENT: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894394
WC_E_UNDECLAREDENTITY: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894393
WC_E_PARSEDENTITY: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894392
WC_E_NOEXTERNALENTITYREF: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894391
WC_E_PI: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894390
WC_E_SYSTEMID: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894389
WC_E_QUESTIONMARK: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894388
WC_E_CDSECTEND: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894387
WC_E_MOREDATA: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894386
WC_E_DTDPROHIBITED: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894385
WC_E_INVALIDXMLSPACE: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894384
NC_E_NC: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894368
NC_E_QNAMECHARACTER: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894367
NC_E_QNAMECOLON: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894366
NC_E_NAMECOLON: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894365
NC_E_DECLAREDPREFIX: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894364
NC_E_UNDECLAREDPREFIX: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894363
NC_E_EMPTYURI: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894362
NC_E_XMLPREFIXRESERVED: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894361
NC_E_XMLNSPREFIXRESERVED: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894360
NC_E_XMLURIRESERVED: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894359
NC_E_XMLNSURIRESERVED: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894358
SC_E_SC: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894336
SC_E_MAXELEMENTDEPTH: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894335
SC_E_MAXENTITYEXPANSION: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894334
WR_E_WR: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894208
WR_E_NONWHITESPACE: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894207
WR_E_NSPREFIXDECLARED: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894206
WR_E_NSPREFIXWITHEMPTYNSURI: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894205
WR_E_DUPLICATEATTRIBUTE: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894204
WR_E_XMLNSPREFIXDECLARATION: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894203
WR_E_XMLPREFIXDECLARATION: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894202
WR_E_XMLURIDECLARATION: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894201
WR_E_XMLNSURIDECLARATION: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894200
WR_E_NAMESPACEUNDECLARED: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894199
WR_E_INVALIDXMLSPACE: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894198
WR_E_INVALIDACTION: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894197
WR_E_INVALIDSURROGATEPAIR: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072894196
XML_E_INVALID_DECIMAL: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072898019
XML_E_INVALID_HEXIDECIMAL: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072898018
XML_E_INVALID_UNICODE: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072898017
XML_E_INVALIDENCODING: win32more.Windows.Win32.Data.Xml.XmlLite.XmlError = -1072897938
XmlNodeType = Int32
XmlNodeType_None: win32more.Windows.Win32.Data.Xml.XmlLite.XmlNodeType = 0
XmlNodeType_Element: win32more.Windows.Win32.Data.Xml.XmlLite.XmlNodeType = 1
XmlNodeType_Attribute: win32more.Windows.Win32.Data.Xml.XmlLite.XmlNodeType = 2
XmlNodeType_Text: win32more.Windows.Win32.Data.Xml.XmlLite.XmlNodeType = 3
XmlNodeType_CDATA: win32more.Windows.Win32.Data.Xml.XmlLite.XmlNodeType = 4
XmlNodeType_ProcessingInstruction: win32more.Windows.Win32.Data.Xml.XmlLite.XmlNodeType = 7
XmlNodeType_Comment: win32more.Windows.Win32.Data.Xml.XmlLite.XmlNodeType = 8
XmlNodeType_DocumentType: win32more.Windows.Win32.Data.Xml.XmlLite.XmlNodeType = 10
XmlNodeType_Whitespace: win32more.Windows.Win32.Data.Xml.XmlLite.XmlNodeType = 13
XmlNodeType_EndElement: win32more.Windows.Win32.Data.Xml.XmlLite.XmlNodeType = 15
XmlNodeType_XmlDeclaration: win32more.Windows.Win32.Data.Xml.XmlLite.XmlNodeType = 17
_XmlNodeType_Last: win32more.Windows.Win32.Data.Xml.XmlLite.XmlNodeType = 17
XmlReadState = Int32
XmlReadState_Initial: win32more.Windows.Win32.Data.Xml.XmlLite.XmlReadState = 0
XmlReadState_Interactive: win32more.Windows.Win32.Data.Xml.XmlLite.XmlReadState = 1
XmlReadState_Error: win32more.Windows.Win32.Data.Xml.XmlLite.XmlReadState = 2
XmlReadState_EndOfFile: win32more.Windows.Win32.Data.Xml.XmlLite.XmlReadState = 3
XmlReadState_Closed: win32more.Windows.Win32.Data.Xml.XmlLite.XmlReadState = 4
XmlReaderProperty = Int32
XmlReaderProperty_MultiLanguage: win32more.Windows.Win32.Data.Xml.XmlLite.XmlReaderProperty = 0
XmlReaderProperty_ConformanceLevel: win32more.Windows.Win32.Data.Xml.XmlLite.XmlReaderProperty = 1
XmlReaderProperty_RandomAccess: win32more.Windows.Win32.Data.Xml.XmlLite.XmlReaderProperty = 2
XmlReaderProperty_XmlResolver: win32more.Windows.Win32.Data.Xml.XmlLite.XmlReaderProperty = 3
XmlReaderProperty_DtdProcessing: win32more.Windows.Win32.Data.Xml.XmlLite.XmlReaderProperty = 4
XmlReaderProperty_ReadState: win32more.Windows.Win32.Data.Xml.XmlLite.XmlReaderProperty = 5
XmlReaderProperty_MaxElementDepth: win32more.Windows.Win32.Data.Xml.XmlLite.XmlReaderProperty = 6
XmlReaderProperty_MaxEntityExpansion: win32more.Windows.Win32.Data.Xml.XmlLite.XmlReaderProperty = 7
_XmlReaderProperty_Last: win32more.Windows.Win32.Data.Xml.XmlLite.XmlReaderProperty = 7
XmlStandalone = Int32
XmlStandalone_Omit: win32more.Windows.Win32.Data.Xml.XmlLite.XmlStandalone = 0
XmlStandalone_Yes: win32more.Windows.Win32.Data.Xml.XmlLite.XmlStandalone = 1
XmlStandalone_No: win32more.Windows.Win32.Data.Xml.XmlLite.XmlStandalone = 2
_XmlStandalone_Last: win32more.Windows.Win32.Data.Xml.XmlLite.XmlStandalone = 2
XmlWriterProperty = Int32
XmlWriterProperty_MultiLanguage: win32more.Windows.Win32.Data.Xml.XmlLite.XmlWriterProperty = 0
XmlWriterProperty_Indent: win32more.Windows.Win32.Data.Xml.XmlLite.XmlWriterProperty = 1
XmlWriterProperty_ByteOrderMark: win32more.Windows.Win32.Data.Xml.XmlLite.XmlWriterProperty = 2
XmlWriterProperty_OmitXmlDeclaration: win32more.Windows.Win32.Data.Xml.XmlLite.XmlWriterProperty = 3
XmlWriterProperty_ConformanceLevel: win32more.Windows.Win32.Data.Xml.XmlLite.XmlWriterProperty = 4
XmlWriterProperty_CompactEmptyElement: win32more.Windows.Win32.Data.Xml.XmlLite.XmlWriterProperty = 5
_XmlWriterProperty_Last: win32more.Windows.Win32.Data.Xml.XmlLite.XmlWriterProperty = 5


make_ready(__name__)
