from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, winfunctype, winfunctype_pointer, make_ready
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
DtdProcessing_Prohibit: DtdProcessing = 0
DtdProcessing_Parse: DtdProcessing = 1
_DtdProcessing_Last: DtdProcessing = 1
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
XmlConformanceLevel_Auto: XmlConformanceLevel = 0
XmlConformanceLevel_Fragment: XmlConformanceLevel = 1
XmlConformanceLevel_Document: XmlConformanceLevel = 2
_XmlConformanceLevel_Last: XmlConformanceLevel = 2
XmlError = Int32
MX_E_MX: XmlError = -1072894464
MX_E_INPUTEND: XmlError = -1072894463
MX_E_ENCODING: XmlError = -1072894462
MX_E_ENCODINGSWITCH: XmlError = -1072894461
MX_E_ENCODINGSIGNATURE: XmlError = -1072894460
WC_E_WC: XmlError = -1072894432
WC_E_WHITESPACE: XmlError = -1072894431
WC_E_SEMICOLON: XmlError = -1072894430
WC_E_GREATERTHAN: XmlError = -1072894429
WC_E_QUOTE: XmlError = -1072894428
WC_E_EQUAL: XmlError = -1072894427
WC_E_LESSTHAN: XmlError = -1072894426
WC_E_HEXDIGIT: XmlError = -1072894425
WC_E_DIGIT: XmlError = -1072894424
WC_E_LEFTBRACKET: XmlError = -1072894423
WC_E_LEFTPAREN: XmlError = -1072894422
WC_E_XMLCHARACTER: XmlError = -1072894421
WC_E_NAMECHARACTER: XmlError = -1072894420
WC_E_SYNTAX: XmlError = -1072894419
WC_E_CDSECT: XmlError = -1072894418
WC_E_COMMENT: XmlError = -1072894417
WC_E_CONDSECT: XmlError = -1072894416
WC_E_DECLATTLIST: XmlError = -1072894415
WC_E_DECLDOCTYPE: XmlError = -1072894414
WC_E_DECLELEMENT: XmlError = -1072894413
WC_E_DECLENTITY: XmlError = -1072894412
WC_E_DECLNOTATION: XmlError = -1072894411
WC_E_NDATA: XmlError = -1072894410
WC_E_PUBLIC: XmlError = -1072894409
WC_E_SYSTEM: XmlError = -1072894408
WC_E_NAME: XmlError = -1072894407
WC_E_ROOTELEMENT: XmlError = -1072894406
WC_E_ELEMENTMATCH: XmlError = -1072894405
WC_E_UNIQUEATTRIBUTE: XmlError = -1072894404
WC_E_TEXTXMLDECL: XmlError = -1072894403
WC_E_LEADINGXML: XmlError = -1072894402
WC_E_TEXTDECL: XmlError = -1072894401
WC_E_XMLDECL: XmlError = -1072894400
WC_E_ENCNAME: XmlError = -1072894399
WC_E_PUBLICID: XmlError = -1072894398
WC_E_PESINTERNALSUBSET: XmlError = -1072894397
WC_E_PESBETWEENDECLS: XmlError = -1072894396
WC_E_NORECURSION: XmlError = -1072894395
WC_E_ENTITYCONTENT: XmlError = -1072894394
WC_E_UNDECLAREDENTITY: XmlError = -1072894393
WC_E_PARSEDENTITY: XmlError = -1072894392
WC_E_NOEXTERNALENTITYREF: XmlError = -1072894391
WC_E_PI: XmlError = -1072894390
WC_E_SYSTEMID: XmlError = -1072894389
WC_E_QUESTIONMARK: XmlError = -1072894388
WC_E_CDSECTEND: XmlError = -1072894387
WC_E_MOREDATA: XmlError = -1072894386
WC_E_DTDPROHIBITED: XmlError = -1072894385
WC_E_INVALIDXMLSPACE: XmlError = -1072894384
NC_E_NC: XmlError = -1072894368
NC_E_QNAMECHARACTER: XmlError = -1072894367
NC_E_QNAMECOLON: XmlError = -1072894366
NC_E_NAMECOLON: XmlError = -1072894365
NC_E_DECLAREDPREFIX: XmlError = -1072894364
NC_E_UNDECLAREDPREFIX: XmlError = -1072894363
NC_E_EMPTYURI: XmlError = -1072894362
NC_E_XMLPREFIXRESERVED: XmlError = -1072894361
NC_E_XMLNSPREFIXRESERVED: XmlError = -1072894360
NC_E_XMLURIRESERVED: XmlError = -1072894359
NC_E_XMLNSURIRESERVED: XmlError = -1072894358
SC_E_SC: XmlError = -1072894336
SC_E_MAXELEMENTDEPTH: XmlError = -1072894335
SC_E_MAXENTITYEXPANSION: XmlError = -1072894334
WR_E_WR: XmlError = -1072894208
WR_E_NONWHITESPACE: XmlError = -1072894207
WR_E_NSPREFIXDECLARED: XmlError = -1072894206
WR_E_NSPREFIXWITHEMPTYNSURI: XmlError = -1072894205
WR_E_DUPLICATEATTRIBUTE: XmlError = -1072894204
WR_E_XMLNSPREFIXDECLARATION: XmlError = -1072894203
WR_E_XMLPREFIXDECLARATION: XmlError = -1072894202
WR_E_XMLURIDECLARATION: XmlError = -1072894201
WR_E_XMLNSURIDECLARATION: XmlError = -1072894200
WR_E_NAMESPACEUNDECLARED: XmlError = -1072894199
WR_E_INVALIDXMLSPACE: XmlError = -1072894198
WR_E_INVALIDACTION: XmlError = -1072894197
WR_E_INVALIDSURROGATEPAIR: XmlError = -1072894196
XML_E_INVALID_DECIMAL: XmlError = -1072898019
XML_E_INVALID_HEXIDECIMAL: XmlError = -1072898018
XML_E_INVALID_UNICODE: XmlError = -1072898017
XML_E_INVALIDENCODING: XmlError = -1072897938
XmlNodeType = Int32
XmlNodeType_None: XmlNodeType = 0
XmlNodeType_Element: XmlNodeType = 1
XmlNodeType_Attribute: XmlNodeType = 2
XmlNodeType_Text: XmlNodeType = 3
XmlNodeType_CDATA: XmlNodeType = 4
XmlNodeType_ProcessingInstruction: XmlNodeType = 7
XmlNodeType_Comment: XmlNodeType = 8
XmlNodeType_DocumentType: XmlNodeType = 10
XmlNodeType_Whitespace: XmlNodeType = 13
XmlNodeType_EndElement: XmlNodeType = 15
XmlNodeType_XmlDeclaration: XmlNodeType = 17
_XmlNodeType_Last: XmlNodeType = 17
XmlReadState = Int32
XmlReadState_Initial: XmlReadState = 0
XmlReadState_Interactive: XmlReadState = 1
XmlReadState_Error: XmlReadState = 2
XmlReadState_EndOfFile: XmlReadState = 3
XmlReadState_Closed: XmlReadState = 4
XmlReaderProperty = Int32
XmlReaderProperty_MultiLanguage: XmlReaderProperty = 0
XmlReaderProperty_ConformanceLevel: XmlReaderProperty = 1
XmlReaderProperty_RandomAccess: XmlReaderProperty = 2
XmlReaderProperty_XmlResolver: XmlReaderProperty = 3
XmlReaderProperty_DtdProcessing: XmlReaderProperty = 4
XmlReaderProperty_ReadState: XmlReaderProperty = 5
XmlReaderProperty_MaxElementDepth: XmlReaderProperty = 6
XmlReaderProperty_MaxEntityExpansion: XmlReaderProperty = 7
_XmlReaderProperty_Last: XmlReaderProperty = 7
XmlStandalone = Int32
XmlStandalone_Omit: XmlStandalone = 0
XmlStandalone_Yes: XmlStandalone = 1
XmlStandalone_No: XmlStandalone = 2
_XmlStandalone_Last: XmlStandalone = 2
XmlWriterProperty = Int32
XmlWriterProperty_MultiLanguage: XmlWriterProperty = 0
XmlWriterProperty_Indent: XmlWriterProperty = 1
XmlWriterProperty_ByteOrderMark: XmlWriterProperty = 2
XmlWriterProperty_OmitXmlDeclaration: XmlWriterProperty = 3
XmlWriterProperty_ConformanceLevel: XmlWriterProperty = 4
XmlWriterProperty_CompactEmptyElement: XmlWriterProperty = 5
_XmlWriterProperty_Last: XmlWriterProperty = 5
make_ready(__name__)
