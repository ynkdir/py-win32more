from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Data.Xml.XmlLite
import win32more.Foundation
import win32more.System.Com
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
def _define__IID_IXmlReader():
    return Guid('7279fc81-709d-4095-b6-3d-69-fe-4b-0d-90-30')
def _define__IID_IXmlWriter():
    return Guid('7279fc88-709d-4095-b6-3d-69-fe-4b-0d-90-30')
def _define__IID_IXmlResolver():
    return Guid('7279fc82-709d-4095-b6-3d-69-fe-4b-0d-90-30')
def _define_CreateXmlReader():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p),win32more.System.Com.IMalloc_head)(('CreateXmlReader', windll['XmlLite.dll']), ((1, 'riid'),(1, 'ppvObject'),(1, 'pMalloc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateXmlReaderInputWithEncodingCodePage():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.System.Com.IMalloc_head,UInt32,win32more.Foundation.BOOL,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.IUnknown_head))(('CreateXmlReaderInputWithEncodingCodePage', windll['XmlLite.dll']), ((1, 'pInputStream'),(1, 'pMalloc'),(1, 'nEncodingCodePage'),(1, 'fEncodingHint'),(1, 'pwszBaseUri'),(1, 'ppInput'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateXmlReaderInputWithEncodingName():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.System.Com.IMalloc_head,win32more.Foundation.PWSTR,win32more.Foundation.BOOL,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.IUnknown_head))(('CreateXmlReaderInputWithEncodingName', windll['XmlLite.dll']), ((1, 'pInputStream'),(1, 'pMalloc'),(1, 'pwszEncodingName'),(1, 'fEncodingHint'),(1, 'pwszBaseUri'),(1, 'ppInput'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateXmlWriter():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p),win32more.System.Com.IMalloc_head)(('CreateXmlWriter', windll['XmlLite.dll']), ((1, 'riid'),(1, 'ppvObject'),(1, 'pMalloc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateXmlWriterOutputWithEncodingCodePage():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.System.Com.IMalloc_head,UInt32,POINTER(win32more.System.Com.IUnknown_head))(('CreateXmlWriterOutputWithEncodingCodePage', windll['XmlLite.dll']), ((1, 'pOutputStream'),(1, 'pMalloc'),(1, 'nEncodingCodePage'),(1, 'ppOutput'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateXmlWriterOutputWithEncodingName():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.System.Com.IMalloc_head,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.IUnknown_head))(('CreateXmlWriterOutputWithEncodingName', windll['XmlLite.dll']), ((1, 'pOutputStream'),(1, 'pMalloc'),(1, 'pwszEncodingName'),(1, 'ppOutput'),))
    except (FileNotFoundError, AttributeError):
        return None
DtdProcessing = Int32
DtdProcessing_Prohibit = 0
DtdProcessing_Parse = 1
_DtdProcessing_Last = 1
def _define_IXmlReader_head():
    class IXmlReader(win32more.System.Com.IUnknown_head):
        Guid = Guid('7279fc81-709d-4095-b6-3d-69-fe-4b-0d-90-30')
    return IXmlReader
def _define_IXmlReader():
    IXmlReader = win32more.Data.Xml.XmlLite.IXmlReader_head
    IXmlReader.SetInput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head)(3, 'SetInput', ((1, 'pInput'),)))
    IXmlReader.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(IntPtr))(4, 'GetProperty', ((1, 'nProperty'),(1, 'ppValue'),)))
    IXmlReader.SetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,IntPtr)(5, 'SetProperty', ((1, 'nProperty'),(1, 'pValue'),)))
    IXmlReader.Read = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Data.Xml.XmlLite.XmlNodeType))(6, 'Read', ((1, 'pNodeType'),)))
    IXmlReader.GetNodeType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Data.Xml.XmlLite.XmlNodeType))(7, 'GetNodeType', ((1, 'pNodeType'),)))
    IXmlReader.MoveToFirstAttribute = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(8, 'MoveToFirstAttribute', ()))
    IXmlReader.MoveToNextAttribute = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(9, 'MoveToNextAttribute', ()))
    IXmlReader.MoveToAttributeByName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(10, 'MoveToAttributeByName', ((1, 'pwszLocalName'),(1, 'pwszNamespaceUri'),)))
    IXmlReader.MoveToElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(11, 'MoveToElement', ()))
    IXmlReader.GetQualifiedName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR),POINTER(UInt32))(12, 'GetQualifiedName', ((1, 'ppwszQualifiedName'),(1, 'pcwchQualifiedName'),)))
    IXmlReader.GetNamespaceUri = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR),POINTER(UInt32))(13, 'GetNamespaceUri', ((1, 'ppwszNamespaceUri'),(1, 'pcwchNamespaceUri'),)))
    IXmlReader.GetLocalName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR),POINTER(UInt32))(14, 'GetLocalName', ((1, 'ppwszLocalName'),(1, 'pcwchLocalName'),)))
    IXmlReader.GetPrefix = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR),POINTER(UInt32))(15, 'GetPrefix', ((1, 'ppwszPrefix'),(1, 'pcwchPrefix'),)))
    IXmlReader.GetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR),POINTER(UInt32))(16, 'GetValue', ((1, 'ppwszValue'),(1, 'pcwchValue'),)))
    IXmlReader.ReadValueChunk = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32))(17, 'ReadValueChunk', ((1, 'pwchBuffer'),(1, 'cwchChunkSize'),(1, 'pcwchRead'),)))
    IXmlReader.GetBaseUri = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR),POINTER(UInt32))(18, 'GetBaseUri', ((1, 'ppwszBaseUri'),(1, 'pcwchBaseUri'),)))
    IXmlReader.IsDefault = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,)(19, 'IsDefault', ()))
    IXmlReader.IsEmptyElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,)(20, 'IsEmptyElement', ()))
    IXmlReader.GetLineNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(21, 'GetLineNumber', ((1, 'pnLineNumber'),)))
    IXmlReader.GetLinePosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(22, 'GetLinePosition', ((1, 'pnLinePosition'),)))
    IXmlReader.GetAttributeCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(23, 'GetAttributeCount', ((1, 'pnAttributeCount'),)))
    IXmlReader.GetDepth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(24, 'GetDepth', ((1, 'pnDepth'),)))
    IXmlReader.IsEOF = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,)(25, 'IsEOF', ()))
    win32more.System.Com.IUnknown
    return IXmlReader
def _define_IXmlResolver_head():
    class IXmlResolver(win32more.System.Com.IUnknown_head):
        Guid = Guid('7279fc82-709d-4095-b6-3d-69-fe-4b-0d-90-30')
    return IXmlResolver
def _define_IXmlResolver():
    IXmlResolver = win32more.Data.Xml.XmlLite.IXmlResolver_head
    IXmlResolver.ResolveUri = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.IUnknown_head))(3, 'ResolveUri', ((1, 'pwszBaseUri'),(1, 'pwszPublicIdentifier'),(1, 'pwszSystemIdentifier'),(1, 'ppResolvedInput'),)))
    win32more.System.Com.IUnknown
    return IXmlResolver
def _define_IXmlWriter_head():
    class IXmlWriter(win32more.System.Com.IUnknown_head):
        Guid = Guid('7279fc88-709d-4095-b6-3d-69-fe-4b-0d-90-30')
    return IXmlWriter
def _define_IXmlWriter():
    IXmlWriter = win32more.Data.Xml.XmlLite.IXmlWriter_head
    IXmlWriter.SetOutput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head)(3, 'SetOutput', ((1, 'pOutput'),)))
    IXmlWriter.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(IntPtr))(4, 'GetProperty', ((1, 'nProperty'),(1, 'ppValue'),)))
    IXmlWriter.SetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,IntPtr)(5, 'SetProperty', ((1, 'nProperty'),(1, 'pValue'),)))
    IXmlWriter.WriteAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Data.Xml.XmlLite.IXmlReader_head,win32more.Foundation.BOOL)(6, 'WriteAttributes', ((1, 'pReader'),(1, 'fWriteDefaultAttributes'),)))
    IXmlWriter.WriteAttributeString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(7, 'WriteAttributeString', ((1, 'pwszPrefix'),(1, 'pwszLocalName'),(1, 'pwszNamespaceUri'),(1, 'pwszValue'),)))
    IXmlWriter.WriteCData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(8, 'WriteCData', ((1, 'pwszText'),)))
    IXmlWriter.WriteCharEntity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Char)(9, 'WriteCharEntity', ((1, 'wch'),)))
    IXmlWriter.WriteChars = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32)(10, 'WriteChars', ((1, 'pwch'),(1, 'cwch'),)))
    IXmlWriter.WriteComment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(11, 'WriteComment', ((1, 'pwszComment'),)))
    IXmlWriter.WriteDocType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(12, 'WriteDocType', ((1, 'pwszName'),(1, 'pwszPublicId'),(1, 'pwszSystemId'),(1, 'pwszSubset'),)))
    IXmlWriter.WriteElementString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(13, 'WriteElementString', ((1, 'pwszPrefix'),(1, 'pwszLocalName'),(1, 'pwszNamespaceUri'),(1, 'pwszValue'),)))
    IXmlWriter.WriteEndDocument = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(14, 'WriteEndDocument', ()))
    IXmlWriter.WriteEndElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(15, 'WriteEndElement', ()))
    IXmlWriter.WriteEntityRef = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(16, 'WriteEntityRef', ((1, 'pwszName'),)))
    IXmlWriter.WriteFullEndElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(17, 'WriteFullEndElement', ()))
    IXmlWriter.WriteName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(18, 'WriteName', ((1, 'pwszName'),)))
    IXmlWriter.WriteNmToken = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(19, 'WriteNmToken', ((1, 'pwszNmToken'),)))
    IXmlWriter.WriteNode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Data.Xml.XmlLite.IXmlReader_head,win32more.Foundation.BOOL)(20, 'WriteNode', ((1, 'pReader'),(1, 'fWriteDefaultAttributes'),)))
    IXmlWriter.WriteNodeShallow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Data.Xml.XmlLite.IXmlReader_head,win32more.Foundation.BOOL)(21, 'WriteNodeShallow', ((1, 'pReader'),(1, 'fWriteDefaultAttributes'),)))
    IXmlWriter.WriteProcessingInstruction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(22, 'WriteProcessingInstruction', ((1, 'pwszName'),(1, 'pwszText'),)))
    IXmlWriter.WriteQualifiedName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(23, 'WriteQualifiedName', ((1, 'pwszLocalName'),(1, 'pwszNamespaceUri'),)))
    IXmlWriter.WriteRaw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(24, 'WriteRaw', ((1, 'pwszData'),)))
    IXmlWriter.WriteRawChars = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32)(25, 'WriteRawChars', ((1, 'pwch'),(1, 'cwch'),)))
    IXmlWriter.WriteStartDocument = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Data.Xml.XmlLite.XmlStandalone)(26, 'WriteStartDocument', ((1, 'standalone'),)))
    IXmlWriter.WriteStartElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(27, 'WriteStartElement', ((1, 'pwszPrefix'),(1, 'pwszLocalName'),(1, 'pwszNamespaceUri'),)))
    IXmlWriter.WriteString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(28, 'WriteString', ((1, 'pwszText'),)))
    IXmlWriter.WriteSurrogateCharEntity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Char,Char)(29, 'WriteSurrogateCharEntity', ((1, 'wchLow'),(1, 'wchHigh'),)))
    IXmlWriter.WriteWhitespace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(30, 'WriteWhitespace', ((1, 'pwszWhitespace'),)))
    IXmlWriter.Flush = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(31, 'Flush', ()))
    win32more.System.Com.IUnknown
    return IXmlWriter
def _define_IXmlWriterLite_head():
    class IXmlWriterLite(win32more.System.Com.IUnknown_head):
        Guid = Guid('862494c6-1310-4aad-b3-cd-2d-be-eb-f6-70-d3')
    return IXmlWriterLite
def _define_IXmlWriterLite():
    IXmlWriterLite = win32more.Data.Xml.XmlLite.IXmlWriterLite_head
    IXmlWriterLite.SetOutput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head)(3, 'SetOutput', ((1, 'pOutput'),)))
    IXmlWriterLite.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(IntPtr))(4, 'GetProperty', ((1, 'nProperty'),(1, 'ppValue'),)))
    IXmlWriterLite.SetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,IntPtr)(5, 'SetProperty', ((1, 'nProperty'),(1, 'pValue'),)))
    IXmlWriterLite.WriteAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Data.Xml.XmlLite.IXmlReader_head,win32more.Foundation.BOOL)(6, 'WriteAttributes', ((1, 'pReader'),(1, 'fWriteDefaultAttributes'),)))
    IXmlWriterLite.WriteAttributeString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,UInt32)(7, 'WriteAttributeString', ((1, 'pwszQName'),(1, 'cwszQName'),(1, 'pwszValue'),(1, 'cwszValue'),)))
    IXmlWriterLite.WriteCData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(8, 'WriteCData', ((1, 'pwszText'),)))
    IXmlWriterLite.WriteCharEntity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Char)(9, 'WriteCharEntity', ((1, 'wch'),)))
    IXmlWriterLite.WriteChars = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32)(10, 'WriteChars', ((1, 'pwch'),(1, 'cwch'),)))
    IXmlWriterLite.WriteComment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(11, 'WriteComment', ((1, 'pwszComment'),)))
    IXmlWriterLite.WriteDocType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(12, 'WriteDocType', ((1, 'pwszName'),(1, 'pwszPublicId'),(1, 'pwszSystemId'),(1, 'pwszSubset'),)))
    IXmlWriterLite.WriteElementString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR)(13, 'WriteElementString', ((1, 'pwszQName'),(1, 'cwszQName'),(1, 'pwszValue'),)))
    IXmlWriterLite.WriteEndDocument = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(14, 'WriteEndDocument', ()))
    IXmlWriterLite.WriteEndElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32)(15, 'WriteEndElement', ((1, 'pwszQName'),(1, 'cwszQName'),)))
    IXmlWriterLite.WriteEntityRef = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(16, 'WriteEntityRef', ((1, 'pwszName'),)))
    IXmlWriterLite.WriteFullEndElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32)(17, 'WriteFullEndElement', ((1, 'pwszQName'),(1, 'cwszQName'),)))
    IXmlWriterLite.WriteName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(18, 'WriteName', ((1, 'pwszName'),)))
    IXmlWriterLite.WriteNmToken = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(19, 'WriteNmToken', ((1, 'pwszNmToken'),)))
    IXmlWriterLite.WriteNode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Data.Xml.XmlLite.IXmlReader_head,win32more.Foundation.BOOL)(20, 'WriteNode', ((1, 'pReader'),(1, 'fWriteDefaultAttributes'),)))
    IXmlWriterLite.WriteNodeShallow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Data.Xml.XmlLite.IXmlReader_head,win32more.Foundation.BOOL)(21, 'WriteNodeShallow', ((1, 'pReader'),(1, 'fWriteDefaultAttributes'),)))
    IXmlWriterLite.WriteProcessingInstruction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(22, 'WriteProcessingInstruction', ((1, 'pwszName'),(1, 'pwszText'),)))
    IXmlWriterLite.WriteRaw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(23, 'WriteRaw', ((1, 'pwszData'),)))
    IXmlWriterLite.WriteRawChars = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32)(24, 'WriteRawChars', ((1, 'pwch'),(1, 'cwch'),)))
    IXmlWriterLite.WriteStartDocument = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Data.Xml.XmlLite.XmlStandalone)(25, 'WriteStartDocument', ((1, 'standalone'),)))
    IXmlWriterLite.WriteStartElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32)(26, 'WriteStartElement', ((1, 'pwszQName'),(1, 'cwszQName'),)))
    IXmlWriterLite.WriteString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(27, 'WriteString', ((1, 'pwszText'),)))
    IXmlWriterLite.WriteSurrogateCharEntity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Char,Char)(28, 'WriteSurrogateCharEntity', ((1, 'wchLow'),(1, 'wchHigh'),)))
    IXmlWriterLite.WriteWhitespace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(29, 'WriteWhitespace', ((1, 'pwszWhitespace'),)))
    IXmlWriterLite.Flush = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(30, 'Flush', ()))
    win32more.System.Com.IUnknown
    return IXmlWriterLite
XmlConformanceLevel = Int32
XmlConformanceLevel_Auto = 0
XmlConformanceLevel_Fragment = 1
XmlConformanceLevel_Document = 2
_XmlConformanceLevel_Last = 2
XmlError = Int32
MX_E_MX = -1072894464
MX_E_INPUTEND = -1072894463
MX_E_ENCODING = -1072894462
MX_E_ENCODINGSWITCH = -1072894461
MX_E_ENCODINGSIGNATURE = -1072894460
WC_E_WC = -1072894432
WC_E_WHITESPACE = -1072894431
WC_E_SEMICOLON = -1072894430
WC_E_GREATERTHAN = -1072894429
WC_E_QUOTE = -1072894428
WC_E_EQUAL = -1072894427
WC_E_LESSTHAN = -1072894426
WC_E_HEXDIGIT = -1072894425
WC_E_DIGIT = -1072894424
WC_E_LEFTBRACKET = -1072894423
WC_E_LEFTPAREN = -1072894422
WC_E_XMLCHARACTER = -1072894421
WC_E_NAMECHARACTER = -1072894420
WC_E_SYNTAX = -1072894419
WC_E_CDSECT = -1072894418
WC_E_COMMENT = -1072894417
WC_E_CONDSECT = -1072894416
WC_E_DECLATTLIST = -1072894415
WC_E_DECLDOCTYPE = -1072894414
WC_E_DECLELEMENT = -1072894413
WC_E_DECLENTITY = -1072894412
WC_E_DECLNOTATION = -1072894411
WC_E_NDATA = -1072894410
WC_E_PUBLIC = -1072894409
WC_E_SYSTEM = -1072894408
WC_E_NAME = -1072894407
WC_E_ROOTELEMENT = -1072894406
WC_E_ELEMENTMATCH = -1072894405
WC_E_UNIQUEATTRIBUTE = -1072894404
WC_E_TEXTXMLDECL = -1072894403
WC_E_LEADINGXML = -1072894402
WC_E_TEXTDECL = -1072894401
WC_E_XMLDECL = -1072894400
WC_E_ENCNAME = -1072894399
WC_E_PUBLICID = -1072894398
WC_E_PESINTERNALSUBSET = -1072894397
WC_E_PESBETWEENDECLS = -1072894396
WC_E_NORECURSION = -1072894395
WC_E_ENTITYCONTENT = -1072894394
WC_E_UNDECLAREDENTITY = -1072894393
WC_E_PARSEDENTITY = -1072894392
WC_E_NOEXTERNALENTITYREF = -1072894391
WC_E_PI = -1072894390
WC_E_SYSTEMID = -1072894389
WC_E_QUESTIONMARK = -1072894388
WC_E_CDSECTEND = -1072894387
WC_E_MOREDATA = -1072894386
WC_E_DTDPROHIBITED = -1072894385
WC_E_INVALIDXMLSPACE = -1072894384
NC_E_NC = -1072894368
NC_E_QNAMECHARACTER = -1072894367
NC_E_QNAMECOLON = -1072894366
NC_E_NAMECOLON = -1072894365
NC_E_DECLAREDPREFIX = -1072894364
NC_E_UNDECLAREDPREFIX = -1072894363
NC_E_EMPTYURI = -1072894362
NC_E_XMLPREFIXRESERVED = -1072894361
NC_E_XMLNSPREFIXRESERVED = -1072894360
NC_E_XMLURIRESERVED = -1072894359
NC_E_XMLNSURIRESERVED = -1072894358
SC_E_SC = -1072894336
SC_E_MAXELEMENTDEPTH = -1072894335
SC_E_MAXENTITYEXPANSION = -1072894334
WR_E_WR = -1072894208
WR_E_NONWHITESPACE = -1072894207
WR_E_NSPREFIXDECLARED = -1072894206
WR_E_NSPREFIXWITHEMPTYNSURI = -1072894205
WR_E_DUPLICATEATTRIBUTE = -1072894204
WR_E_XMLNSPREFIXDECLARATION = -1072894203
WR_E_XMLPREFIXDECLARATION = -1072894202
WR_E_XMLURIDECLARATION = -1072894201
WR_E_XMLNSURIDECLARATION = -1072894200
WR_E_NAMESPACEUNDECLARED = -1072894199
WR_E_INVALIDXMLSPACE = -1072894198
WR_E_INVALIDACTION = -1072894197
WR_E_INVALIDSURROGATEPAIR = -1072894196
XML_E_INVALID_DECIMAL = -1072898019
XML_E_INVALID_HEXIDECIMAL = -1072898018
XML_E_INVALID_UNICODE = -1072898017
XML_E_INVALIDENCODING = -1072897938
XmlNodeType = Int32
XmlNodeType_None = 0
XmlNodeType_Element = 1
XmlNodeType_Attribute = 2
XmlNodeType_Text = 3
XmlNodeType_CDATA = 4
XmlNodeType_ProcessingInstruction = 7
XmlNodeType_Comment = 8
XmlNodeType_DocumentType = 10
XmlNodeType_Whitespace = 13
XmlNodeType_EndElement = 15
XmlNodeType_XmlDeclaration = 17
_XmlNodeType_Last = 17
XmlReaderProperty = Int32
XmlReaderProperty_MultiLanguage = 0
XmlReaderProperty_ConformanceLevel = 1
XmlReaderProperty_RandomAccess = 2
XmlReaderProperty_XmlResolver = 3
XmlReaderProperty_DtdProcessing = 4
XmlReaderProperty_ReadState = 5
XmlReaderProperty_MaxElementDepth = 6
XmlReaderProperty_MaxEntityExpansion = 7
_XmlReaderProperty_Last = 7
XmlReadState = Int32
XmlReadState_Initial = 0
XmlReadState_Interactive = 1
XmlReadState_Error = 2
XmlReadState_EndOfFile = 3
XmlReadState_Closed = 4
XmlStandalone = Int32
XmlStandalone_Omit = 0
XmlStandalone_Yes = 1
XmlStandalone_No = 2
_XmlStandalone_Last = 2
XmlWriterProperty = Int32
XmlWriterProperty_MultiLanguage = 0
XmlWriterProperty_Indent = 1
XmlWriterProperty_ByteOrderMark = 2
XmlWriterProperty_OmitXmlDeclaration = 3
XmlWriterProperty_ConformanceLevel = 4
XmlWriterProperty_CompactEmptyElement = 5
_XmlWriterProperty_Last = 5
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
