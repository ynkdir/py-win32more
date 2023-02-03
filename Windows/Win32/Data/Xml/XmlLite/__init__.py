from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Data.Xml.XmlLite
import Windows.Win32.Foundation
import Windows.Win32.System.Com
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        if name in _arch_optional:
            return None
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
_IID_IXmlReader: Guid = Guid('7279fc81-709d-4095-b6-3d-69-fe-4b-0d-90-30')
_IID_IXmlWriter: Guid = Guid('7279fc88-709d-4095-b6-3d-69-fe-4b-0d-90-30')
_IID_IXmlResolver: Guid = Guid('7279fc82-709d-4095-b6-3d-69-fe-4b-0d-90-30')
@winfunctype('XmlLite.dll')
def CreateXmlReader(riid: POINTER(Guid), ppvObject: POINTER(c_void_p), pMalloc: Windows.Win32.System.Com.IMalloc_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('XmlLite.dll')
def CreateXmlReaderInputWithEncodingCodePage(pInputStream: Windows.Win32.System.Com.IUnknown_head, pMalloc: Windows.Win32.System.Com.IMalloc_head, nEncodingCodePage: UInt32, fEncodingHint: Windows.Win32.Foundation.BOOL, pwszBaseUri: Windows.Win32.Foundation.PWSTR, ppInput: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('XmlLite.dll')
def CreateXmlReaderInputWithEncodingName(pInputStream: Windows.Win32.System.Com.IUnknown_head, pMalloc: Windows.Win32.System.Com.IMalloc_head, pwszEncodingName: Windows.Win32.Foundation.PWSTR, fEncodingHint: Windows.Win32.Foundation.BOOL, pwszBaseUri: Windows.Win32.Foundation.PWSTR, ppInput: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('XmlLite.dll')
def CreateXmlWriter(riid: POINTER(Guid), ppvObject: POINTER(c_void_p), pMalloc: Windows.Win32.System.Com.IMalloc_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('XmlLite.dll')
def CreateXmlWriterOutputWithEncodingCodePage(pOutputStream: Windows.Win32.System.Com.IUnknown_head, pMalloc: Windows.Win32.System.Com.IMalloc_head, nEncodingCodePage: UInt32, ppOutput: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('XmlLite.dll')
def CreateXmlWriterOutputWithEncodingName(pOutputStream: Windows.Win32.System.Com.IUnknown_head, pMalloc: Windows.Win32.System.Com.IMalloc_head, pwszEncodingName: Windows.Win32.Foundation.PWSTR, ppOutput: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
DtdProcessing = Int32
DtdProcessing_Prohibit: DtdProcessing = 0
DtdProcessing_Parse: DtdProcessing = 1
_DtdProcessing_Last: DtdProcessing = 1
class IXmlReader(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('7279fc81-709d-4095-b6-3d-69-fe-4b-0d-90-30')
    @commethod(3)
    def SetInput(pInput: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetProperty(nProperty: UInt32, ppValue: POINTER(IntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetProperty(nProperty: UInt32, pValue: IntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Read(pNodeType: POINTER(Windows.Win32.Data.Xml.XmlLite.XmlNodeType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetNodeType(pNodeType: POINTER(Windows.Win32.Data.Xml.XmlLite.XmlNodeType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def MoveToFirstAttribute() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def MoveToNextAttribute() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def MoveToAttributeByName(pwszLocalName: Windows.Win32.Foundation.PWSTR, pwszNamespaceUri: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def MoveToElement() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetQualifiedName(ppwszQualifiedName: POINTER(Windows.Win32.Foundation.PWSTR), pcwchQualifiedName: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetNamespaceUri(ppwszNamespaceUri: POINTER(Windows.Win32.Foundation.PWSTR), pcwchNamespaceUri: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetLocalName(ppwszLocalName: POINTER(Windows.Win32.Foundation.PWSTR), pcwchLocalName: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetPrefix(ppwszPrefix: POINTER(Windows.Win32.Foundation.PWSTR), pcwchPrefix: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetValue(ppwszValue: POINTER(Windows.Win32.Foundation.PWSTR), pcwchValue: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def ReadValueChunk(pwchBuffer: Windows.Win32.Foundation.PWSTR, cwchChunkSize: UInt32, pcwchRead: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetBaseUri(ppwszBaseUri: POINTER(Windows.Win32.Foundation.PWSTR), pcwchBaseUri: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def IsDefault() -> Windows.Win32.Foundation.BOOL: ...
    @commethod(20)
    def IsEmptyElement() -> Windows.Win32.Foundation.BOOL: ...
    @commethod(21)
    def GetLineNumber(pnLineNumber: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetLinePosition(pnLinePosition: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetAttributeCount(pnAttributeCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetDepth(pnDepth: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def IsEOF() -> Windows.Win32.Foundation.BOOL: ...
class IXmlResolver(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('7279fc82-709d-4095-b6-3d-69-fe-4b-0d-90-30')
    @commethod(3)
    def ResolveUri(pwszBaseUri: Windows.Win32.Foundation.PWSTR, pwszPublicIdentifier: Windows.Win32.Foundation.PWSTR, pwszSystemIdentifier: Windows.Win32.Foundation.PWSTR, ppResolvedInput: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IXmlWriter(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('7279fc88-709d-4095-b6-3d-69-fe-4b-0d-90-30')
    @commethod(3)
    def SetOutput(pOutput: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetProperty(nProperty: UInt32, ppValue: POINTER(IntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetProperty(nProperty: UInt32, pValue: IntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def WriteAttributes(pReader: Windows.Win32.Data.Xml.XmlLite.IXmlReader_head, fWriteDefaultAttributes: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def WriteAttributeString(pwszPrefix: Windows.Win32.Foundation.PWSTR, pwszLocalName: Windows.Win32.Foundation.PWSTR, pwszNamespaceUri: Windows.Win32.Foundation.PWSTR, pwszValue: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def WriteCData(pwszText: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def WriteCharEntity(wch: Char) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def WriteChars(pwch: Windows.Win32.Foundation.PWSTR, cwch: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def WriteComment(pwszComment: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def WriteDocType(pwszName: Windows.Win32.Foundation.PWSTR, pwszPublicId: Windows.Win32.Foundation.PWSTR, pwszSystemId: Windows.Win32.Foundation.PWSTR, pwszSubset: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def WriteElementString(pwszPrefix: Windows.Win32.Foundation.PWSTR, pwszLocalName: Windows.Win32.Foundation.PWSTR, pwszNamespaceUri: Windows.Win32.Foundation.PWSTR, pwszValue: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def WriteEndDocument() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def WriteEndElement() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def WriteEntityRef(pwszName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def WriteFullEndElement() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def WriteName(pwszName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def WriteNmToken(pwszNmToken: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def WriteNode(pReader: Windows.Win32.Data.Xml.XmlLite.IXmlReader_head, fWriteDefaultAttributes: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def WriteNodeShallow(pReader: Windows.Win32.Data.Xml.XmlLite.IXmlReader_head, fWriteDefaultAttributes: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def WriteProcessingInstruction(pwszName: Windows.Win32.Foundation.PWSTR, pwszText: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def WriteQualifiedName(pwszLocalName: Windows.Win32.Foundation.PWSTR, pwszNamespaceUri: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def WriteRaw(pwszData: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def WriteRawChars(pwch: Windows.Win32.Foundation.PWSTR, cwch: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def WriteStartDocument(standalone: Windows.Win32.Data.Xml.XmlLite.XmlStandalone) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def WriteStartElement(pwszPrefix: Windows.Win32.Foundation.PWSTR, pwszLocalName: Windows.Win32.Foundation.PWSTR, pwszNamespaceUri: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def WriteString(pwszText: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def WriteSurrogateCharEntity(wchLow: Char, wchHigh: Char) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def WriteWhitespace(pwszWhitespace: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def Flush() -> Windows.Win32.Foundation.HRESULT: ...
class IXmlWriterLite(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('862494c6-1310-4aad-b3-cd-2d-be-eb-f6-70-d3')
    @commethod(3)
    def SetOutput(pOutput: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetProperty(nProperty: UInt32, ppValue: POINTER(IntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetProperty(nProperty: UInt32, pValue: IntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def WriteAttributes(pReader: Windows.Win32.Data.Xml.XmlLite.IXmlReader_head, fWriteDefaultAttributes: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def WriteAttributeString(pwszQName: Windows.Win32.Foundation.PWSTR, cwszQName: UInt32, pwszValue: Windows.Win32.Foundation.PWSTR, cwszValue: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def WriteCData(pwszText: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def WriteCharEntity(wch: Char) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def WriteChars(pwch: Windows.Win32.Foundation.PWSTR, cwch: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def WriteComment(pwszComment: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def WriteDocType(pwszName: Windows.Win32.Foundation.PWSTR, pwszPublicId: Windows.Win32.Foundation.PWSTR, pwszSystemId: Windows.Win32.Foundation.PWSTR, pwszSubset: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def WriteElementString(pwszQName: Windows.Win32.Foundation.PWSTR, cwszQName: UInt32, pwszValue: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def WriteEndDocument() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def WriteEndElement(pwszQName: Windows.Win32.Foundation.PWSTR, cwszQName: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def WriteEntityRef(pwszName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def WriteFullEndElement(pwszQName: Windows.Win32.Foundation.PWSTR, cwszQName: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def WriteName(pwszName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def WriteNmToken(pwszNmToken: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def WriteNode(pReader: Windows.Win32.Data.Xml.XmlLite.IXmlReader_head, fWriteDefaultAttributes: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def WriteNodeShallow(pReader: Windows.Win32.Data.Xml.XmlLite.IXmlReader_head, fWriteDefaultAttributes: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def WriteProcessingInstruction(pwszName: Windows.Win32.Foundation.PWSTR, pwszText: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def WriteRaw(pwszData: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def WriteRawChars(pwch: Windows.Win32.Foundation.PWSTR, cwch: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def WriteStartDocument(standalone: Windows.Win32.Data.Xml.XmlLite.XmlStandalone) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def WriteStartElement(pwszQName: Windows.Win32.Foundation.PWSTR, cwszQName: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def WriteString(pwszText: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def WriteSurrogateCharEntity(wchLow: Char, wchHigh: Char) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def WriteWhitespace(pwszWhitespace: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def Flush() -> Windows.Win32.Foundation.HRESULT: ...
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
make_head(_module, 'IXmlReader')
make_head(_module, 'IXmlResolver')
make_head(_module, 'IXmlWriter')
make_head(_module, 'IXmlWriterLite')
__all__ = [
    "CreateXmlReader",
    "CreateXmlReaderInputWithEncodingCodePage",
    "CreateXmlReaderInputWithEncodingName",
    "CreateXmlWriter",
    "CreateXmlWriterOutputWithEncodingCodePage",
    "CreateXmlWriterOutputWithEncodingName",
    "DtdProcessing",
    "DtdProcessing_Parse",
    "DtdProcessing_Prohibit",
    "IXmlReader",
    "IXmlResolver",
    "IXmlWriter",
    "IXmlWriterLite",
    "MX_E_ENCODING",
    "MX_E_ENCODINGSIGNATURE",
    "MX_E_ENCODINGSWITCH",
    "MX_E_INPUTEND",
    "MX_E_MX",
    "NC_E_DECLAREDPREFIX",
    "NC_E_EMPTYURI",
    "NC_E_NAMECOLON",
    "NC_E_NC",
    "NC_E_QNAMECHARACTER",
    "NC_E_QNAMECOLON",
    "NC_E_UNDECLAREDPREFIX",
    "NC_E_XMLNSPREFIXRESERVED",
    "NC_E_XMLNSURIRESERVED",
    "NC_E_XMLPREFIXRESERVED",
    "NC_E_XMLURIRESERVED",
    "SC_E_MAXELEMENTDEPTH",
    "SC_E_MAXENTITYEXPANSION",
    "SC_E_SC",
    "WC_E_CDSECT",
    "WC_E_CDSECTEND",
    "WC_E_COMMENT",
    "WC_E_CONDSECT",
    "WC_E_DECLATTLIST",
    "WC_E_DECLDOCTYPE",
    "WC_E_DECLELEMENT",
    "WC_E_DECLENTITY",
    "WC_E_DECLNOTATION",
    "WC_E_DIGIT",
    "WC_E_DTDPROHIBITED",
    "WC_E_ELEMENTMATCH",
    "WC_E_ENCNAME",
    "WC_E_ENTITYCONTENT",
    "WC_E_EQUAL",
    "WC_E_GREATERTHAN",
    "WC_E_HEXDIGIT",
    "WC_E_INVALIDXMLSPACE",
    "WC_E_LEADINGXML",
    "WC_E_LEFTBRACKET",
    "WC_E_LEFTPAREN",
    "WC_E_LESSTHAN",
    "WC_E_MOREDATA",
    "WC_E_NAME",
    "WC_E_NAMECHARACTER",
    "WC_E_NDATA",
    "WC_E_NOEXTERNALENTITYREF",
    "WC_E_NORECURSION",
    "WC_E_PARSEDENTITY",
    "WC_E_PESBETWEENDECLS",
    "WC_E_PESINTERNALSUBSET",
    "WC_E_PI",
    "WC_E_PUBLIC",
    "WC_E_PUBLICID",
    "WC_E_QUESTIONMARK",
    "WC_E_QUOTE",
    "WC_E_ROOTELEMENT",
    "WC_E_SEMICOLON",
    "WC_E_SYNTAX",
    "WC_E_SYSTEM",
    "WC_E_SYSTEMID",
    "WC_E_TEXTDECL",
    "WC_E_TEXTXMLDECL",
    "WC_E_UNDECLAREDENTITY",
    "WC_E_UNIQUEATTRIBUTE",
    "WC_E_WC",
    "WC_E_WHITESPACE",
    "WC_E_XMLCHARACTER",
    "WC_E_XMLDECL",
    "WR_E_DUPLICATEATTRIBUTE",
    "WR_E_INVALIDACTION",
    "WR_E_INVALIDSURROGATEPAIR",
    "WR_E_INVALIDXMLSPACE",
    "WR_E_NAMESPACEUNDECLARED",
    "WR_E_NONWHITESPACE",
    "WR_E_NSPREFIXDECLARED",
    "WR_E_NSPREFIXWITHEMPTYNSURI",
    "WR_E_WR",
    "WR_E_XMLNSPREFIXDECLARATION",
    "WR_E_XMLNSURIDECLARATION",
    "WR_E_XMLPREFIXDECLARATION",
    "WR_E_XMLURIDECLARATION",
    "XML_E_INVALIDENCODING",
    "XML_E_INVALID_DECIMAL",
    "XML_E_INVALID_HEXIDECIMAL",
    "XML_E_INVALID_UNICODE",
    "XmlConformanceLevel",
    "XmlConformanceLevel_Auto",
    "XmlConformanceLevel_Document",
    "XmlConformanceLevel_Fragment",
    "XmlError",
    "XmlNodeType",
    "XmlNodeType_Attribute",
    "XmlNodeType_CDATA",
    "XmlNodeType_Comment",
    "XmlNodeType_DocumentType",
    "XmlNodeType_Element",
    "XmlNodeType_EndElement",
    "XmlNodeType_None",
    "XmlNodeType_ProcessingInstruction",
    "XmlNodeType_Text",
    "XmlNodeType_Whitespace",
    "XmlNodeType_XmlDeclaration",
    "XmlReadState",
    "XmlReadState_Closed",
    "XmlReadState_EndOfFile",
    "XmlReadState_Error",
    "XmlReadState_Initial",
    "XmlReadState_Interactive",
    "XmlReaderProperty",
    "XmlReaderProperty_ConformanceLevel",
    "XmlReaderProperty_DtdProcessing",
    "XmlReaderProperty_MaxElementDepth",
    "XmlReaderProperty_MaxEntityExpansion",
    "XmlReaderProperty_MultiLanguage",
    "XmlReaderProperty_RandomAccess",
    "XmlReaderProperty_ReadState",
    "XmlReaderProperty_XmlResolver",
    "XmlStandalone",
    "XmlStandalone_No",
    "XmlStandalone_Omit",
    "XmlStandalone_Yes",
    "XmlWriterProperty",
    "XmlWriterProperty_ByteOrderMark",
    "XmlWriterProperty_CompactEmptyElement",
    "XmlWriterProperty_ConformanceLevel",
    "XmlWriterProperty_Indent",
    "XmlWriterProperty_MultiLanguage",
    "XmlWriterProperty_OmitXmlDeclaration",
    "_DtdProcessing_Last",
    "_IID_IXmlReader",
    "_IID_IXmlResolver",
    "_IID_IXmlWriter",
    "_XmlConformanceLevel_Last",
    "_XmlNodeType_Last",
    "_XmlReaderProperty_Last",
    "_XmlStandalone_Last",
    "_XmlWriterProperty_Last",
]
_arch_optional = [
]
