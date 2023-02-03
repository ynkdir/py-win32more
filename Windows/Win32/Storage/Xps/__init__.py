from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.Graphics.Gdi
import Windows.Win32.Security
import Windows.Win32.Security.Cryptography
import Windows.Win32.Storage.Packaging.Opc
import Windows.Win32.Storage.Xps
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
@winfunctype_pointer
def ABORTPROC(param0: Windows.Win32.Graphics.Gdi.HDC, param1: Int32) -> Windows.Win32.Foundation.BOOL: ...
XPS_E_SIGREQUESTID_DUP: Windows.Win32.Foundation.HRESULT = -2142108795
XPS_E_PACKAGE_NOT_OPENED: Windows.Win32.Foundation.HRESULT = -2142108794
XPS_E_PACKAGE_ALREADY_OPENED: Windows.Win32.Foundation.HRESULT = -2142108793
XPS_E_SIGNATUREID_DUP: Windows.Win32.Foundation.HRESULT = -2142108792
XPS_E_MARKUP_COMPATIBILITY_ELEMENTS: Windows.Win32.Foundation.HRESULT = -2142108791
XPS_E_OBJECT_DETACHED: Windows.Win32.Foundation.HRESULT = -2142108790
XPS_E_INVALID_SIGNATUREBLOCK_MARKUP: Windows.Win32.Foundation.HRESULT = -2142108789
XPS_E_INVALID_NUMBER_OF_POINTS_IN_CURVE_SEGMENTS: Windows.Win32.Foundation.HRESULT = -2142108160
XPS_E_ABSOLUTE_REFERENCE: Windows.Win32.Foundation.HRESULT = -2142108159
XPS_E_INVALID_NUMBER_OF_COLOR_CHANNELS: Windows.Win32.Foundation.HRESULT = -2142108158
XPS_E_INVALID_LANGUAGE: Windows.Win32.Foundation.HRESULT = -2142109696
XPS_E_INVALID_NAME: Windows.Win32.Foundation.HRESULT = -2142109695
XPS_E_INVALID_RESOURCE_KEY: Windows.Win32.Foundation.HRESULT = -2142109694
XPS_E_INVALID_PAGE_SIZE: Windows.Win32.Foundation.HRESULT = -2142109693
XPS_E_INVALID_BLEED_BOX: Windows.Win32.Foundation.HRESULT = -2142109692
XPS_E_INVALID_THUMBNAIL_IMAGE_TYPE: Windows.Win32.Foundation.HRESULT = -2142109691
XPS_E_INVALID_LOOKUP_TYPE: Windows.Win32.Foundation.HRESULT = -2142109690
XPS_E_INVALID_FLOAT: Windows.Win32.Foundation.HRESULT = -2142109689
XPS_E_UNEXPECTED_CONTENT_TYPE: Windows.Win32.Foundation.HRESULT = -2142109688
XPS_E_INVALID_FONT_URI: Windows.Win32.Foundation.HRESULT = -2142109686
XPS_E_INVALID_CONTENT_BOX: Windows.Win32.Foundation.HRESULT = -2142109685
XPS_E_INVALID_MARKUP: Windows.Win32.Foundation.HRESULT = -2142109684
XPS_E_INVALID_XML_ENCODING: Windows.Win32.Foundation.HRESULT = -2142109683
XPS_E_INVALID_CONTENT_TYPE: Windows.Win32.Foundation.HRESULT = -2142109682
XPS_E_INVALID_OBFUSCATED_FONT_URI: Windows.Win32.Foundation.HRESULT = -2142109681
XPS_E_UNEXPECTED_RELATIONSHIP_TYPE: Windows.Win32.Foundation.HRESULT = -2142109680
XPS_E_UNEXPECTED_RESTRICTED_FONT_RELATIONSHIP: Windows.Win32.Foundation.HRESULT = -2142109679
XPS_E_MISSING_NAME: Windows.Win32.Foundation.HRESULT = -2142109440
XPS_E_MISSING_LOOKUP: Windows.Win32.Foundation.HRESULT = -2142109439
XPS_E_MISSING_GLYPHS: Windows.Win32.Foundation.HRESULT = -2142109438
XPS_E_MISSING_SEGMENT_DATA: Windows.Win32.Foundation.HRESULT = -2142109437
XPS_E_MISSING_COLORPROFILE: Windows.Win32.Foundation.HRESULT = -2142109436
XPS_E_MISSING_RELATIONSHIP_TARGET: Windows.Win32.Foundation.HRESULT = -2142109435
XPS_E_MISSING_RESOURCE_RELATIONSHIP: Windows.Win32.Foundation.HRESULT = -2142109434
XPS_E_MISSING_FONTURI: Windows.Win32.Foundation.HRESULT = -2142109433
XPS_E_MISSING_DOCUMENTSEQUENCE_RELATIONSHIP: Windows.Win32.Foundation.HRESULT = -2142109432
XPS_E_MISSING_DOCUMENT: Windows.Win32.Foundation.HRESULT = -2142109431
XPS_E_MISSING_REFERRED_DOCUMENT: Windows.Win32.Foundation.HRESULT = -2142109430
XPS_E_MISSING_REFERRED_PAGE: Windows.Win32.Foundation.HRESULT = -2142109429
XPS_E_MISSING_PAGE_IN_DOCUMENT: Windows.Win32.Foundation.HRESULT = -2142109428
XPS_E_MISSING_PAGE_IN_PAGEREFERENCE: Windows.Win32.Foundation.HRESULT = -2142109427
XPS_E_MISSING_IMAGE_IN_IMAGEBRUSH: Windows.Win32.Foundation.HRESULT = -2142109426
XPS_E_MISSING_RESOURCE_KEY: Windows.Win32.Foundation.HRESULT = -2142109425
XPS_E_MISSING_PART_REFERENCE: Windows.Win32.Foundation.HRESULT = -2142109424
XPS_E_MISSING_RESTRICTED_FONT_RELATIONSHIP: Windows.Win32.Foundation.HRESULT = -2142109423
XPS_E_MISSING_DISCARDCONTROL: Windows.Win32.Foundation.HRESULT = -2142109422
XPS_E_MISSING_PART_STREAM: Windows.Win32.Foundation.HRESULT = -2142109421
XPS_E_UNAVAILABLE_PACKAGE: Windows.Win32.Foundation.HRESULT = -2142109420
XPS_E_DUPLICATE_RESOURCE_KEYS: Windows.Win32.Foundation.HRESULT = -2142109184
XPS_E_MULTIPLE_RESOURCES: Windows.Win32.Foundation.HRESULT = -2142109183
XPS_E_MULTIPLE_DOCUMENTSEQUENCE_RELATIONSHIPS: Windows.Win32.Foundation.HRESULT = -2142109182
XPS_E_MULTIPLE_THUMBNAILS_ON_PAGE: Windows.Win32.Foundation.HRESULT = -2142109181
XPS_E_MULTIPLE_THUMBNAILS_ON_PACKAGE: Windows.Win32.Foundation.HRESULT = -2142109180
XPS_E_MULTIPLE_PRINTTICKETS_ON_PAGE: Windows.Win32.Foundation.HRESULT = -2142109179
XPS_E_MULTIPLE_PRINTTICKETS_ON_DOCUMENT: Windows.Win32.Foundation.HRESULT = -2142109178
XPS_E_MULTIPLE_PRINTTICKETS_ON_DOCUMENTSEQUENCE: Windows.Win32.Foundation.HRESULT = -2142109177
XPS_E_MULTIPLE_REFERENCES_TO_PART: Windows.Win32.Foundation.HRESULT = -2142109176
XPS_E_DUPLICATE_NAMES: Windows.Win32.Foundation.HRESULT = -2142109175
XPS_E_STRING_TOO_LONG: Windows.Win32.Foundation.HRESULT = -2142108928
XPS_E_TOO_MANY_INDICES: Windows.Win32.Foundation.HRESULT = -2142108927
XPS_E_MAPPING_OUT_OF_ORDER: Windows.Win32.Foundation.HRESULT = -2142108926
XPS_E_MAPPING_OUTSIDE_STRING: Windows.Win32.Foundation.HRESULT = -2142108925
XPS_E_MAPPING_OUTSIDE_INDICES: Windows.Win32.Foundation.HRESULT = -2142108924
XPS_E_CARET_OUTSIDE_STRING: Windows.Win32.Foundation.HRESULT = -2142108923
XPS_E_CARET_OUT_OF_ORDER: Windows.Win32.Foundation.HRESULT = -2142108922
XPS_E_ODD_BIDILEVEL: Windows.Win32.Foundation.HRESULT = -2142108921
XPS_E_ONE_TO_ONE_MAPPING_EXPECTED: Windows.Win32.Foundation.HRESULT = -2142108920
XPS_E_RESTRICTED_FONT_NOT_OBFUSCATED: Windows.Win32.Foundation.HRESULT = -2142108919
XPS_E_NEGATIVE_FLOAT: Windows.Win32.Foundation.HRESULT = -2142108918
XPS_E_XKEY_ATTR_PRESENT_OUTSIDE_RES_DICT: Windows.Win32.Foundation.HRESULT = -2142108672
XPS_E_DICTIONARY_ITEM_NAMED: Windows.Win32.Foundation.HRESULT = -2142108671
XPS_E_NESTED_REMOTE_DICTIONARY: Windows.Win32.Foundation.HRESULT = -2142108670
XPS_E_INDEX_OUT_OF_RANGE: Windows.Win32.Foundation.HRESULT = -2142108416
XPS_E_VISUAL_CIRCULAR_REF: Windows.Win32.Foundation.HRESULT = -2142108415
XPS_E_NO_CUSTOM_OBJECTS: Windows.Win32.Foundation.HRESULT = -2142108414
XPS_E_ALREADY_OWNED: Windows.Win32.Foundation.HRESULT = -2142108413
XPS_E_RESOURCE_NOT_OWNED: Windows.Win32.Foundation.HRESULT = -2142108412
XPS_E_UNEXPECTED_COLORPROFILE: Windows.Win32.Foundation.HRESULT = -2142108411
XPS_E_COLOR_COMPONENT_OUT_OF_RANGE: Windows.Win32.Foundation.HRESULT = -2142108410
XPS_E_BOTH_PATHFIGURE_AND_ABBR_SYNTAX_PRESENT: Windows.Win32.Foundation.HRESULT = -2142108409
XPS_E_BOTH_RESOURCE_AND_SOURCEATTR_PRESENT: Windows.Win32.Foundation.HRESULT = -2142108408
XPS_E_BLEED_BOX_PAGE_DIMENSIONS_NOT_IN_SYNC: Windows.Win32.Foundation.HRESULT = -2142108407
XPS_E_RELATIONSHIP_EXTERNAL: Windows.Win32.Foundation.HRESULT = -2142108406
XPS_E_NOT_ENOUGH_GRADIENT_STOPS: Windows.Win32.Foundation.HRESULT = -2142108405
XPS_E_PACKAGE_WRITER_NOT_CLOSED: Windows.Win32.Foundation.HRESULT = -2142108404
@winfunctype('winspool.drv')
def DeviceCapabilitiesA(pDevice: Windows.Win32.Foundation.PSTR, pPort: Windows.Win32.Foundation.PSTR, fwCapability: Windows.Win32.Storage.Xps.DEVICE_CAPABILITIES, pOutput: Windows.Win32.Foundation.PSTR, pDevMode: POINTER(Windows.Win32.Graphics.Gdi.DEVMODEA_head)) -> Int32: ...
@winfunctype('winspool.drv')
def DeviceCapabilitiesW(pDevice: Windows.Win32.Foundation.PWSTR, pPort: Windows.Win32.Foundation.PWSTR, fwCapability: Windows.Win32.Storage.Xps.DEVICE_CAPABILITIES, pOutput: Windows.Win32.Foundation.PWSTR, pDevMode: POINTER(Windows.Win32.Graphics.Gdi.DEVMODEW_head)) -> Int32: ...
@winfunctype('GDI32.dll')
def Escape(hdc: Windows.Win32.Graphics.Gdi.HDC, iEscape: Int32, cjIn: Int32, pvIn: Windows.Win32.Foundation.PSTR, pvOut: c_void_p) -> Int32: ...
@winfunctype('GDI32.dll')
def ExtEscape(hdc: Windows.Win32.Graphics.Gdi.HDC, iEscape: Int32, cjInput: Int32, lpInData: Windows.Win32.Foundation.PSTR, cjOutput: Int32, lpOutData: Windows.Win32.Foundation.PSTR) -> Int32: ...
@winfunctype('GDI32.dll')
def StartDocA(hdc: Windows.Win32.Graphics.Gdi.HDC, lpdi: POINTER(Windows.Win32.Storage.Xps.DOCINFOA_head)) -> Int32: ...
@winfunctype('GDI32.dll')
def StartDocW(hdc: Windows.Win32.Graphics.Gdi.HDC, lpdi: POINTER(Windows.Win32.Storage.Xps.DOCINFOW_head)) -> Int32: ...
@winfunctype('GDI32.dll')
def EndDoc(hdc: Windows.Win32.Graphics.Gdi.HDC) -> Int32: ...
@winfunctype('GDI32.dll')
def StartPage(hdc: Windows.Win32.Graphics.Gdi.HDC) -> Int32: ...
@winfunctype('GDI32.dll')
def EndPage(hdc: Windows.Win32.Graphics.Gdi.HDC) -> Int32: ...
@winfunctype('GDI32.dll')
def AbortDoc(hdc: Windows.Win32.Graphics.Gdi.HDC) -> Int32: ...
@winfunctype('GDI32.dll')
def SetAbortProc(hdc: Windows.Win32.Graphics.Gdi.HDC, proc: Windows.Win32.Storage.Xps.ABORTPROC) -> Int32: ...
@winfunctype('USER32.dll')
def PrintWindow(hwnd: Windows.Win32.Foundation.HWND, hdcBlt: Windows.Win32.Graphics.Gdi.HDC, nFlags: Windows.Win32.Storage.Xps.PRINT_WINDOW_FLAGS) -> Windows.Win32.Foundation.BOOL: ...
DEVICE_CAPABILITIES = UInt16
DC_BINNAMES: DEVICE_CAPABILITIES = 12
DC_BINS: DEVICE_CAPABILITIES = 6
DC_COLLATE: DEVICE_CAPABILITIES = 22
DC_COLORDEVICE: DEVICE_CAPABILITIES = 32
DC_COPIES: DEVICE_CAPABILITIES = 18
DC_DRIVER: DEVICE_CAPABILITIES = 11
DC_DUPLEX: DEVICE_CAPABILITIES = 7
DC_ENUMRESOLUTIONS: DEVICE_CAPABILITIES = 13
DC_EXTRA: DEVICE_CAPABILITIES = 9
DC_FIELDS: DEVICE_CAPABILITIES = 1
DC_FILEDEPENDENCIES: DEVICE_CAPABILITIES = 14
DC_MAXEXTENT: DEVICE_CAPABILITIES = 5
DC_MEDIAREADY: DEVICE_CAPABILITIES = 29
DC_MEDIATYPENAMES: DEVICE_CAPABILITIES = 34
DC_MEDIATYPES: DEVICE_CAPABILITIES = 35
DC_MINEXTENT: DEVICE_CAPABILITIES = 4
DC_ORIENTATION: DEVICE_CAPABILITIES = 17
DC_NUP: DEVICE_CAPABILITIES = 33
DC_PAPERNAMES: DEVICE_CAPABILITIES = 16
DC_PAPERS: DEVICE_CAPABILITIES = 2
DC_PAPERSIZE: DEVICE_CAPABILITIES = 3
DC_PERSONALITY: DEVICE_CAPABILITIES = 25
DC_PRINTERMEM: DEVICE_CAPABILITIES = 28
DC_PRINTRATE: DEVICE_CAPABILITIES = 26
DC_PRINTRATEPPM: DEVICE_CAPABILITIES = 31
DC_PRINTRATEUNIT: DEVICE_CAPABILITIES = 27
DC_SIZE: DEVICE_CAPABILITIES = 8
DC_STAPLE: DEVICE_CAPABILITIES = 30
DC_TRUETYPE: DEVICE_CAPABILITIES = 15
DC_VERSION: DEVICE_CAPABILITIES = 10
class DOCINFOA(Structure):
    cbSize: Int32
    lpszDocName: Windows.Win32.Foundation.PSTR
    lpszOutput: Windows.Win32.Foundation.PSTR
    lpszDatatype: Windows.Win32.Foundation.PSTR
    fwType: UInt32
class DOCINFOW(Structure):
    cbSize: Int32
    lpszDocName: Windows.Win32.Foundation.PWSTR
    lpszOutput: Windows.Win32.Foundation.PWSTR
    lpszDatatype: Windows.Win32.Foundation.PWSTR
    fwType: UInt32
class DRAWPATRECT(Structure):
    ptPosition: Windows.Win32.Foundation.POINT
    ptSize: Windows.Win32.Foundation.POINT
    wStyle: UInt16
    wPattern: UInt16
HPTPROVIDER = IntPtr
class IXpsDocumentPackageTarget(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('3b0b6d38-53ad-41da-b2-12-d3-76-37-a6-71-4e')
    @commethod(3)
    def GetXpsOMPackageWriter(documentSequencePartName: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, discardControlPartName: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, packageWriter: POINTER(Windows.Win32.Storage.Xps.IXpsOMPackageWriter_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetXpsOMFactory(xpsFactory: POINTER(Windows.Win32.Storage.Xps.IXpsOMObjectFactory_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetXpsType(documentType: POINTER(Windows.Win32.Storage.Xps.XPS_DOCUMENT_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsDocumentPackageTarget3D(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('60ba71b8-3101-4984-91-99-f4-ea-77-5f-f0-1d')
    @commethod(3)
    def GetXpsOMPackageWriter3D(documentSequencePartName: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, discardControlPartName: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, modelPartName: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, modelData: Windows.Win32.System.Com.IStream_head, packageWriter: POINTER(Windows.Win32.Storage.Xps.IXpsOMPackageWriter3D_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetXpsOMFactory(xpsFactory: POINTER(Windows.Win32.Storage.Xps.IXpsOMObjectFactory_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMBrush(c_void_p):
    extends: Windows.Win32.Storage.Xps.IXpsOMShareable
    Guid = Guid('56a3f80c-ea4c-4187-a5-7b-a2-a4-73-b2-b4-2b')
    @commethod(5)
    def GetOpacity(opacity: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetOpacity(opacity: Single) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMCanvas(c_void_p):
    extends: Windows.Win32.Storage.Xps.IXpsOMVisual
    Guid = Guid('221d1452-331e-47c6-87-e9-6c-ce-fb-9b-5b-a3')
    @commethod(30)
    def GetVisuals(visuals: POINTER(Windows.Win32.Storage.Xps.IXpsOMVisualCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def GetUseAliasedEdgeMode(useAliasedEdgeMode: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def SetUseAliasedEdgeMode(useAliasedEdgeMode: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def GetAccessibilityShortDescription(shortDescription: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def SetAccessibilityShortDescription(shortDescription: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def GetAccessibilityLongDescription(longDescription: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def SetAccessibilityLongDescription(longDescription: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def GetDictionary(resourceDictionary: POINTER(Windows.Win32.Storage.Xps.IXpsOMDictionary_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def GetDictionaryLocal(resourceDictionary: POINTER(Windows.Win32.Storage.Xps.IXpsOMDictionary_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def SetDictionaryLocal(resourceDictionary: Windows.Win32.Storage.Xps.IXpsOMDictionary_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def GetDictionaryResource(remoteDictionaryResource: POINTER(Windows.Win32.Storage.Xps.IXpsOMRemoteDictionaryResource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def SetDictionaryResource(remoteDictionaryResource: Windows.Win32.Storage.Xps.IXpsOMRemoteDictionaryResource_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def Clone(canvas: POINTER(Windows.Win32.Storage.Xps.IXpsOMCanvas_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMColorProfileResource(c_void_p):
    extends: Windows.Win32.Storage.Xps.IXpsOMResource
    Guid = Guid('67bd7d69-1eef-4bb1-b5-e7-6f-4f-87-be-8a-be')
    @commethod(5)
    def GetStream(stream: POINTER(Windows.Win32.System.Com.IStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetContent(sourceStream: Windows.Win32.System.Com.IStream_head, partName: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMColorProfileResourceCollection(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('12759630-5fba-4283-8f-7d-cc-a8-49-80-9e-db')
    @commethod(3)
    def GetCount(count: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(index: UInt32, object: POINTER(Windows.Win32.Storage.Xps.IXpsOMColorProfileResource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def InsertAt(index: UInt32, object: Windows.Win32.Storage.Xps.IXpsOMColorProfileResource_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveAt(index: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetAt(index: UInt32, object: Windows.Win32.Storage.Xps.IXpsOMColorProfileResource_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Append(object: Windows.Win32.Storage.Xps.IXpsOMColorProfileResource_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetByPartName(partName: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, part: POINTER(Windows.Win32.Storage.Xps.IXpsOMColorProfileResource_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMCoreProperties(c_void_p):
    extends: Windows.Win32.Storage.Xps.IXpsOMPart
    Guid = Guid('3340fe8f-4027-4aa1-8f-5f-d3-5a-e4-5f-e5-97')
    @commethod(5)
    def GetOwner(package: POINTER(Windows.Win32.Storage.Xps.IXpsOMPackage_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCategory(category: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetCategory(category: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetContentStatus(contentStatus: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetContentStatus(contentStatus: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetContentType(contentType: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetContentType(contentType: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetCreated(created: POINTER(Windows.Win32.Foundation.SYSTEMTIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetCreated(created: POINTER(Windows.Win32.Foundation.SYSTEMTIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetCreator(creator: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetCreator(creator: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetDescription(description: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetDescription(description: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetIdentifier(identifier: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetIdentifier(identifier: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetKeywords(keywords: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def SetKeywords(keywords: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetLanguage(language: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetLanguage(language: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetLastModifiedBy(lastModifiedBy: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def SetLastModifiedBy(lastModifiedBy: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetLastPrinted(lastPrinted: POINTER(Windows.Win32.Foundation.SYSTEMTIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def SetLastPrinted(lastPrinted: POINTER(Windows.Win32.Foundation.SYSTEMTIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetModified(modified: POINTER(Windows.Win32.Foundation.SYSTEMTIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def SetModified(modified: POINTER(Windows.Win32.Foundation.SYSTEMTIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def GetRevision(revision: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def SetRevision(revision: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def GetSubject(subject: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def SetSubject(subject: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetTitle(title: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def SetTitle(title: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def GetVersion(version: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def SetVersion(version: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def Clone(coreProperties: POINTER(Windows.Win32.Storage.Xps.IXpsOMCoreProperties_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMDashCollection(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('081613f4-74eb-48f2-83-b3-37-a9-ce-2d-7d-c6')
    @commethod(3)
    def GetCount(count: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(index: UInt32, dash: POINTER(Windows.Win32.Storage.Xps.XPS_DASH_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def InsertAt(index: UInt32, dash: POINTER(Windows.Win32.Storage.Xps.XPS_DASH_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveAt(index: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetAt(index: UInt32, dash: POINTER(Windows.Win32.Storage.Xps.XPS_DASH_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Append(dash: POINTER(Windows.Win32.Storage.Xps.XPS_DASH_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMDictionary(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('897c86b8-8eaf-4ae3-bd-de-56-41-9f-cf-42-36')
    @commethod(3)
    def GetOwner(owner: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCount(count: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetAt(index: UInt32, key: POINTER(Windows.Win32.Foundation.PWSTR), entry: POINTER(Windows.Win32.Storage.Xps.IXpsOMShareable_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetByKey(key: Windows.Win32.Foundation.PWSTR, beforeEntry: Windows.Win32.Storage.Xps.IXpsOMShareable_head, entry: POINTER(Windows.Win32.Storage.Xps.IXpsOMShareable_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetIndex(entry: Windows.Win32.Storage.Xps.IXpsOMShareable_head, index: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Append(key: Windows.Win32.Foundation.PWSTR, entry: Windows.Win32.Storage.Xps.IXpsOMShareable_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def InsertAt(index: UInt32, key: Windows.Win32.Foundation.PWSTR, entry: Windows.Win32.Storage.Xps.IXpsOMShareable_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def RemoveAt(index: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetAt(index: UInt32, key: Windows.Win32.Foundation.PWSTR, entry: Windows.Win32.Storage.Xps.IXpsOMShareable_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Clone(dictionary: POINTER(Windows.Win32.Storage.Xps.IXpsOMDictionary_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMDocument(c_void_p):
    extends: Windows.Win32.Storage.Xps.IXpsOMPart
    Guid = Guid('2c2c94cb-ac5f-4254-8e-e9-23-94-83-09-d9-f0')
    @commethod(5)
    def GetOwner(documentSequence: POINTER(Windows.Win32.Storage.Xps.IXpsOMDocumentSequence_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPageReferences(pageReferences: POINTER(Windows.Win32.Storage.Xps.IXpsOMPageReferenceCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetPrintTicketResource(printTicketResource: POINTER(Windows.Win32.Storage.Xps.IXpsOMPrintTicketResource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetPrintTicketResource(printTicketResource: Windows.Win32.Storage.Xps.IXpsOMPrintTicketResource_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetDocumentStructureResource(documentStructureResource: POINTER(Windows.Win32.Storage.Xps.IXpsOMDocumentStructureResource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetDocumentStructureResource(documentStructureResource: Windows.Win32.Storage.Xps.IXpsOMDocumentStructureResource_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetSignatureBlockResources(signatureBlockResources: POINTER(Windows.Win32.Storage.Xps.IXpsOMSignatureBlockResourceCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Clone(document: POINTER(Windows.Win32.Storage.Xps.IXpsOMDocument_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMDocumentCollection(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d1c87f0d-e947-4754-8a-25-97-14-78-f7-e8-3e')
    @commethod(3)
    def GetCount(count: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(index: UInt32, document: POINTER(Windows.Win32.Storage.Xps.IXpsOMDocument_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def InsertAt(index: UInt32, document: Windows.Win32.Storage.Xps.IXpsOMDocument_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveAt(index: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetAt(index: UInt32, document: Windows.Win32.Storage.Xps.IXpsOMDocument_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Append(document: Windows.Win32.Storage.Xps.IXpsOMDocument_head) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMDocumentSequence(c_void_p):
    extends: Windows.Win32.Storage.Xps.IXpsOMPart
    Guid = Guid('56492eb4-d8d5-425e-82-56-4c-2b-64-ad-02-64')
    @commethod(5)
    def GetOwner(package: POINTER(Windows.Win32.Storage.Xps.IXpsOMPackage_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetDocuments(documents: POINTER(Windows.Win32.Storage.Xps.IXpsOMDocumentCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetPrintTicketResource(printTicketResource: POINTER(Windows.Win32.Storage.Xps.IXpsOMPrintTicketResource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetPrintTicketResource(printTicketResource: Windows.Win32.Storage.Xps.IXpsOMPrintTicketResource_head) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMDocumentStructureResource(c_void_p):
    extends: Windows.Win32.Storage.Xps.IXpsOMResource
    Guid = Guid('85febc8a-6b63-48a9-af-07-70-64-e4-ec-ff-30')
    @commethod(5)
    def GetOwner(owner: POINTER(Windows.Win32.Storage.Xps.IXpsOMDocument_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetStream(stream: POINTER(Windows.Win32.System.Com.IStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetContent(sourceStream: Windows.Win32.System.Com.IStream_head, partName: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMFontResource(c_void_p):
    extends: Windows.Win32.Storage.Xps.IXpsOMResource
    Guid = Guid('a8c45708-47d9-4af4-8d-20-33-b4-8c-9b-84-85')
    @commethod(5)
    def GetStream(readerStream: POINTER(Windows.Win32.System.Com.IStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetContent(sourceStream: Windows.Win32.System.Com.IStream_head, embeddingOption: Windows.Win32.Storage.Xps.XPS_FONT_EMBEDDING, partName: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetEmbeddingOption(embeddingOption: POINTER(Windows.Win32.Storage.Xps.XPS_FONT_EMBEDDING)) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMFontResourceCollection(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('70b4a6bb-88d4-4fa8-aa-f9-6d-9c-59-6f-db-ad')
    @commethod(3)
    def GetCount(count: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(index: UInt32, value: POINTER(Windows.Win32.Storage.Xps.IXpsOMFontResource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetAt(index: UInt32, value: Windows.Win32.Storage.Xps.IXpsOMFontResource_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def InsertAt(index: UInt32, value: Windows.Win32.Storage.Xps.IXpsOMFontResource_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Append(value: Windows.Win32.Storage.Xps.IXpsOMFontResource_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RemoveAt(index: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetByPartName(partName: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, part: POINTER(Windows.Win32.Storage.Xps.IXpsOMFontResource_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMGeometry(c_void_p):
    extends: Windows.Win32.Storage.Xps.IXpsOMShareable
    Guid = Guid('64fcf3d7-4d58-44ba-ad-73-a1-3a-f6-49-20-72')
    @commethod(5)
    def GetFigures(figures: POINTER(Windows.Win32.Storage.Xps.IXpsOMGeometryFigureCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetFillRule(fillRule: POINTER(Windows.Win32.Storage.Xps.XPS_FILL_RULE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetFillRule(fillRule: Windows.Win32.Storage.Xps.XPS_FILL_RULE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetTransform(transform: POINTER(Windows.Win32.Storage.Xps.IXpsOMMatrixTransform_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetTransformLocal(transform: POINTER(Windows.Win32.Storage.Xps.IXpsOMMatrixTransform_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetTransformLocal(transform: Windows.Win32.Storage.Xps.IXpsOMMatrixTransform_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetTransformLookup(lookup: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetTransformLookup(lookup: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Clone(geometry: POINTER(Windows.Win32.Storage.Xps.IXpsOMGeometry_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMGeometryFigure(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d410dc83-908c-443e-89-47-b1-79-5d-3c-16-5a')
    @commethod(3)
    def GetOwner(owner: POINTER(Windows.Win32.Storage.Xps.IXpsOMGeometry_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSegmentData(dataCount: POINTER(UInt32), segmentData: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSegmentTypes(segmentCount: POINTER(UInt32), segmentTypes: POINTER(Windows.Win32.Storage.Xps.XPS_SEGMENT_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSegmentStrokes(segmentCount: POINTER(UInt32), segmentStrokes: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetSegments(segmentCount: UInt32, segmentDataCount: UInt32, segmentTypes: POINTER(Windows.Win32.Storage.Xps.XPS_SEGMENT_TYPE), segmentData: POINTER(Single), segmentStrokes: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetStartPoint(startPoint: POINTER(Windows.Win32.Storage.Xps.XPS_POINT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetStartPoint(startPoint: POINTER(Windows.Win32.Storage.Xps.XPS_POINT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetIsClosed(isClosed: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetIsClosed(isClosed: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetIsFilled(isFilled: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetIsFilled(isFilled: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetSegmentCount(segmentCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetSegmentDataCount(segmentDataCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetSegmentStrokePattern(segmentStrokePattern: POINTER(Windows.Win32.Storage.Xps.XPS_SEGMENT_STROKE_PATTERN)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def Clone(geometryFigure: POINTER(Windows.Win32.Storage.Xps.IXpsOMGeometryFigure_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMGeometryFigureCollection(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('fd48c3f3-a58e-4b5a-88-26-1d-e5-4a-be-72-b2')
    @commethod(3)
    def GetCount(count: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(index: UInt32, geometryFigure: POINTER(Windows.Win32.Storage.Xps.IXpsOMGeometryFigure_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def InsertAt(index: UInt32, geometryFigure: Windows.Win32.Storage.Xps.IXpsOMGeometryFigure_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveAt(index: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetAt(index: UInt32, geometryFigure: Windows.Win32.Storage.Xps.IXpsOMGeometryFigure_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Append(geometryFigure: Windows.Win32.Storage.Xps.IXpsOMGeometryFigure_head) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMGlyphs(c_void_p):
    extends: Windows.Win32.Storage.Xps.IXpsOMVisual
    Guid = Guid('819b3199-0a5a-4b64-be-c7-a9-e1-7e-78-0d-e2')
    @commethod(30)
    def GetUnicodeString(unicodeString: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def GetGlyphIndexCount(indexCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def GetGlyphIndices(indexCount: POINTER(UInt32), glyphIndices: POINTER(Windows.Win32.Storage.Xps.XPS_GLYPH_INDEX_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def GetGlyphMappingCount(glyphMappingCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetGlyphMappings(glyphMappingCount: POINTER(UInt32), glyphMappings: POINTER(Windows.Win32.Storage.Xps.XPS_GLYPH_MAPPING_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def GetProhibitedCaretStopCount(prohibitedCaretStopCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def GetProhibitedCaretStops(prohibitedCaretStopCount: POINTER(UInt32), prohibitedCaretStops: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def GetBidiLevel(bidiLevel: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def GetIsSideways(isSideways: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def GetDeviceFontName(deviceFontName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def GetStyleSimulations(styleSimulations: POINTER(Windows.Win32.Storage.Xps.XPS_STYLE_SIMULATION)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def SetStyleSimulations(styleSimulations: Windows.Win32.Storage.Xps.XPS_STYLE_SIMULATION) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def GetOrigin(origin: POINTER(Windows.Win32.Storage.Xps.XPS_POINT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def SetOrigin(origin: POINTER(Windows.Win32.Storage.Xps.XPS_POINT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def GetFontRenderingEmSize(fontRenderingEmSize: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def SetFontRenderingEmSize(fontRenderingEmSize: Single) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def GetFontResource(fontResource: POINTER(Windows.Win32.Storage.Xps.IXpsOMFontResource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def SetFontResource(fontResource: Windows.Win32.Storage.Xps.IXpsOMFontResource_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def GetFontFaceIndex(fontFaceIndex: POINTER(Int16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def SetFontFaceIndex(fontFaceIndex: Int16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def GetFillBrush(fillBrush: POINTER(Windows.Win32.Storage.Xps.IXpsOMBrush_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def GetFillBrushLocal(fillBrush: POINTER(Windows.Win32.Storage.Xps.IXpsOMBrush_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def SetFillBrushLocal(fillBrush: Windows.Win32.Storage.Xps.IXpsOMBrush_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def GetFillBrushLookup(key: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def SetFillBrushLookup(key: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def GetGlyphsEditor(editor: POINTER(Windows.Win32.Storage.Xps.IXpsOMGlyphsEditor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def Clone(glyphs: POINTER(Windows.Win32.Storage.Xps.IXpsOMGlyphs_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMGlyphsEditor(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a5ab8616-5b16-4b9f-96-29-89-b3-23-ed-79-09')
    @commethod(3)
    def ApplyEdits() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetUnicodeString(unicodeString: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetUnicodeString(unicodeString: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetGlyphIndexCount(indexCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetGlyphIndices(indexCount: POINTER(UInt32), glyphIndices: POINTER(Windows.Win32.Storage.Xps.XPS_GLYPH_INDEX_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetGlyphIndices(indexCount: UInt32, glyphIndices: POINTER(Windows.Win32.Storage.Xps.XPS_GLYPH_INDEX_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetGlyphMappingCount(glyphMappingCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetGlyphMappings(glyphMappingCount: POINTER(UInt32), glyphMappings: POINTER(Windows.Win32.Storage.Xps.XPS_GLYPH_MAPPING_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetGlyphMappings(glyphMappingCount: UInt32, glyphMappings: POINTER(Windows.Win32.Storage.Xps.XPS_GLYPH_MAPPING_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetProhibitedCaretStopCount(prohibitedCaretStopCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetProhibitedCaretStops(count: POINTER(UInt32), prohibitedCaretStops: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetProhibitedCaretStops(count: UInt32, prohibitedCaretStops: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetBidiLevel(bidiLevel: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetBidiLevel(bidiLevel: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetIsSideways(isSideways: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetIsSideways(isSideways: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetDeviceFontName(deviceFontName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SetDeviceFontName(deviceFontName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMGradientBrush(c_void_p):
    extends: Windows.Win32.Storage.Xps.IXpsOMBrush
    Guid = Guid('edb59622-61a2-42c3-ba-ce-ac-f2-28-6c-06-bf')
    @commethod(7)
    def GetGradientStops(gradientStops: POINTER(Windows.Win32.Storage.Xps.IXpsOMGradientStopCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetTransform(transform: POINTER(Windows.Win32.Storage.Xps.IXpsOMMatrixTransform_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetTransformLocal(transform: POINTER(Windows.Win32.Storage.Xps.IXpsOMMatrixTransform_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetTransformLocal(transform: Windows.Win32.Storage.Xps.IXpsOMMatrixTransform_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetTransformLookup(key: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetTransformLookup(key: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetSpreadMethod(spreadMethod: POINTER(Windows.Win32.Storage.Xps.XPS_SPREAD_METHOD)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetSpreadMethod(spreadMethod: Windows.Win32.Storage.Xps.XPS_SPREAD_METHOD) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetColorInterpolationMode(colorInterpolationMode: POINTER(Windows.Win32.Storage.Xps.XPS_COLOR_INTERPOLATION)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetColorInterpolationMode(colorInterpolationMode: Windows.Win32.Storage.Xps.XPS_COLOR_INTERPOLATION) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMGradientStop(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('5cf4f5cc-3969-49b5-a7-0a-55-50-b6-18-fe-49')
    @commethod(3)
    def GetOwner(owner: POINTER(Windows.Win32.Storage.Xps.IXpsOMGradientBrush_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetOffset(offset: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetOffset(offset: Single) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetColor(color: POINTER(Windows.Win32.Storage.Xps.XPS_COLOR_head), colorProfile: POINTER(Windows.Win32.Storage.Xps.IXpsOMColorProfileResource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetColor(color: POINTER(Windows.Win32.Storage.Xps.XPS_COLOR_head), colorProfile: Windows.Win32.Storage.Xps.IXpsOMColorProfileResource_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Clone(gradientStop: POINTER(Windows.Win32.Storage.Xps.IXpsOMGradientStop_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMGradientStopCollection(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c9174c3a-3cd3-4319-bd-a4-11-a3-93-92-ce-ef')
    @commethod(3)
    def GetCount(count: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(index: UInt32, stop: POINTER(Windows.Win32.Storage.Xps.IXpsOMGradientStop_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def InsertAt(index: UInt32, stop: Windows.Win32.Storage.Xps.IXpsOMGradientStop_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveAt(index: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetAt(index: UInt32, stop: Windows.Win32.Storage.Xps.IXpsOMGradientStop_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Append(stop: Windows.Win32.Storage.Xps.IXpsOMGradientStop_head) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMImageBrush(c_void_p):
    extends: Windows.Win32.Storage.Xps.IXpsOMTileBrush
    Guid = Guid('3df0b466-d382-49ef-85-50-dd-94-c8-02-42-e4')
    @commethod(18)
    def GetImageResource(imageResource: POINTER(Windows.Win32.Storage.Xps.IXpsOMImageResource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetImageResource(imageResource: Windows.Win32.Storage.Xps.IXpsOMImageResource_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetColorProfileResource(colorProfileResource: POINTER(Windows.Win32.Storage.Xps.IXpsOMColorProfileResource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def SetColorProfileResource(colorProfileResource: Windows.Win32.Storage.Xps.IXpsOMColorProfileResource_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def Clone(imageBrush: POINTER(Windows.Win32.Storage.Xps.IXpsOMImageBrush_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMImageResource(c_void_p):
    extends: Windows.Win32.Storage.Xps.IXpsOMResource
    Guid = Guid('3db8417d-ae50-485e-9a-44-d7-75-8f-78-a2-3f')
    @commethod(5)
    def GetStream(readerStream: POINTER(Windows.Win32.System.Com.IStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetContent(sourceStream: Windows.Win32.System.Com.IStream_head, imageType: Windows.Win32.Storage.Xps.XPS_IMAGE_TYPE, partName: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetImageType(imageType: POINTER(Windows.Win32.Storage.Xps.XPS_IMAGE_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMImageResourceCollection(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('7a4a1a71-9cde-4b71-b3-3f-62-de-84-3e-ab-fe')
    @commethod(3)
    def GetCount(count: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(index: UInt32, object: POINTER(Windows.Win32.Storage.Xps.IXpsOMImageResource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def InsertAt(index: UInt32, object: Windows.Win32.Storage.Xps.IXpsOMImageResource_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveAt(index: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetAt(index: UInt32, object: Windows.Win32.Storage.Xps.IXpsOMImageResource_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Append(object: Windows.Win32.Storage.Xps.IXpsOMImageResource_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetByPartName(partName: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, part: POINTER(Windows.Win32.Storage.Xps.IXpsOMImageResource_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMLinearGradientBrush(c_void_p):
    extends: Windows.Win32.Storage.Xps.IXpsOMGradientBrush
    Guid = Guid('005e279f-c30d-40ff-93-ec-19-50-d3-c5-28-db')
    @commethod(17)
    def GetStartPoint(startPoint: POINTER(Windows.Win32.Storage.Xps.XPS_POINT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetStartPoint(startPoint: POINTER(Windows.Win32.Storage.Xps.XPS_POINT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetEndPoint(endPoint: POINTER(Windows.Win32.Storage.Xps.XPS_POINT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SetEndPoint(endPoint: POINTER(Windows.Win32.Storage.Xps.XPS_POINT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def Clone(linearGradientBrush: POINTER(Windows.Win32.Storage.Xps.IXpsOMLinearGradientBrush_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMMatrixTransform(c_void_p):
    extends: Windows.Win32.Storage.Xps.IXpsOMShareable
    Guid = Guid('b77330ff-bb37-4501-a9-3e-f1-b1-e5-0b-fc-46')
    @commethod(5)
    def GetMatrix(matrix: POINTER(Windows.Win32.Storage.Xps.XPS_MATRIX_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetMatrix(matrix: POINTER(Windows.Win32.Storage.Xps.XPS_MATRIX_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Clone(matrixTransform: POINTER(Windows.Win32.Storage.Xps.IXpsOMMatrixTransform_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMNameCollection(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('4bddf8ec-c915-421b-a1-66-d1-73-d2-56-53-d2')
    @commethod(3)
    def GetCount(count: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(index: UInt32, name: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMObjectFactory(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f9b2a685-a50d-4fc2-b7-64-b5-6e-09-3e-a0-ca')
    @commethod(3)
    def CreatePackage(package: POINTER(Windows.Win32.Storage.Xps.IXpsOMPackage_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreatePackageFromFile(filename: Windows.Win32.Foundation.PWSTR, reuseObjects: Windows.Win32.Foundation.BOOL, package: POINTER(Windows.Win32.Storage.Xps.IXpsOMPackage_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreatePackageFromStream(stream: Windows.Win32.System.Com.IStream_head, reuseObjects: Windows.Win32.Foundation.BOOL, package: POINTER(Windows.Win32.Storage.Xps.IXpsOMPackage_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateStoryFragmentsResource(acquiredStream: Windows.Win32.System.Com.IStream_head, partUri: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, storyFragmentsResource: POINTER(Windows.Win32.Storage.Xps.IXpsOMStoryFragmentsResource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateDocumentStructureResource(acquiredStream: Windows.Win32.System.Com.IStream_head, partUri: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, documentStructureResource: POINTER(Windows.Win32.Storage.Xps.IXpsOMDocumentStructureResource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CreateSignatureBlockResource(acquiredStream: Windows.Win32.System.Com.IStream_head, partUri: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, signatureBlockResource: POINTER(Windows.Win32.Storage.Xps.IXpsOMSignatureBlockResource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CreateRemoteDictionaryResource(dictionary: Windows.Win32.Storage.Xps.IXpsOMDictionary_head, partUri: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, remoteDictionaryResource: POINTER(Windows.Win32.Storage.Xps.IXpsOMRemoteDictionaryResource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CreateRemoteDictionaryResourceFromStream(dictionaryMarkupStream: Windows.Win32.System.Com.IStream_head, dictionaryPartUri: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, resources: Windows.Win32.Storage.Xps.IXpsOMPartResources_head, dictionaryResource: POINTER(Windows.Win32.Storage.Xps.IXpsOMRemoteDictionaryResource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def CreatePartResources(partResources: POINTER(Windows.Win32.Storage.Xps.IXpsOMPartResources_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def CreateDocumentSequence(partUri: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, documentSequence: POINTER(Windows.Win32.Storage.Xps.IXpsOMDocumentSequence_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def CreateDocument(partUri: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, document: POINTER(Windows.Win32.Storage.Xps.IXpsOMDocument_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def CreatePageReference(advisoryPageDimensions: POINTER(Windows.Win32.Storage.Xps.XPS_SIZE_head), pageReference: POINTER(Windows.Win32.Storage.Xps.IXpsOMPageReference_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def CreatePage(pageDimensions: POINTER(Windows.Win32.Storage.Xps.XPS_SIZE_head), language: Windows.Win32.Foundation.PWSTR, partUri: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, page: POINTER(Windows.Win32.Storage.Xps.IXpsOMPage_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def CreatePageFromStream(pageMarkupStream: Windows.Win32.System.Com.IStream_head, partUri: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, resources: Windows.Win32.Storage.Xps.IXpsOMPartResources_head, reuseObjects: Windows.Win32.Foundation.BOOL, page: POINTER(Windows.Win32.Storage.Xps.IXpsOMPage_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def CreateCanvas(canvas: POINTER(Windows.Win32.Storage.Xps.IXpsOMCanvas_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def CreateGlyphs(fontResource: Windows.Win32.Storage.Xps.IXpsOMFontResource_head, glyphs: POINTER(Windows.Win32.Storage.Xps.IXpsOMGlyphs_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def CreatePath(path: POINTER(Windows.Win32.Storage.Xps.IXpsOMPath_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def CreateGeometry(geometry: POINTER(Windows.Win32.Storage.Xps.IXpsOMGeometry_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def CreateGeometryFigure(startPoint: POINTER(Windows.Win32.Storage.Xps.XPS_POINT_head), figure: POINTER(Windows.Win32.Storage.Xps.IXpsOMGeometryFigure_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def CreateMatrixTransform(matrix: POINTER(Windows.Win32.Storage.Xps.XPS_MATRIX_head), transform: POINTER(Windows.Win32.Storage.Xps.IXpsOMMatrixTransform_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def CreateSolidColorBrush(color: POINTER(Windows.Win32.Storage.Xps.XPS_COLOR_head), colorProfile: Windows.Win32.Storage.Xps.IXpsOMColorProfileResource_head, solidColorBrush: POINTER(Windows.Win32.Storage.Xps.IXpsOMSolidColorBrush_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def CreateColorProfileResource(acquiredStream: Windows.Win32.System.Com.IStream_head, partUri: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, colorProfileResource: POINTER(Windows.Win32.Storage.Xps.IXpsOMColorProfileResource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def CreateImageBrush(image: Windows.Win32.Storage.Xps.IXpsOMImageResource_head, viewBox: POINTER(Windows.Win32.Storage.Xps.XPS_RECT_head), viewPort: POINTER(Windows.Win32.Storage.Xps.XPS_RECT_head), imageBrush: POINTER(Windows.Win32.Storage.Xps.IXpsOMImageBrush_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def CreateVisualBrush(viewBox: POINTER(Windows.Win32.Storage.Xps.XPS_RECT_head), viewPort: POINTER(Windows.Win32.Storage.Xps.XPS_RECT_head), visualBrush: POINTER(Windows.Win32.Storage.Xps.IXpsOMVisualBrush_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def CreateImageResource(acquiredStream: Windows.Win32.System.Com.IStream_head, contentType: Windows.Win32.Storage.Xps.XPS_IMAGE_TYPE, partUri: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, imageResource: POINTER(Windows.Win32.Storage.Xps.IXpsOMImageResource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def CreatePrintTicketResource(acquiredStream: Windows.Win32.System.Com.IStream_head, partUri: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, printTicketResource: POINTER(Windows.Win32.Storage.Xps.IXpsOMPrintTicketResource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def CreateFontResource(acquiredStream: Windows.Win32.System.Com.IStream_head, fontEmbedding: Windows.Win32.Storage.Xps.XPS_FONT_EMBEDDING, partUri: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, isObfSourceStream: Windows.Win32.Foundation.BOOL, fontResource: POINTER(Windows.Win32.Storage.Xps.IXpsOMFontResource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def CreateGradientStop(color: POINTER(Windows.Win32.Storage.Xps.XPS_COLOR_head), colorProfile: Windows.Win32.Storage.Xps.IXpsOMColorProfileResource_head, offset: Single, gradientStop: POINTER(Windows.Win32.Storage.Xps.IXpsOMGradientStop_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def CreateLinearGradientBrush(gradStop1: Windows.Win32.Storage.Xps.IXpsOMGradientStop_head, gradStop2: Windows.Win32.Storage.Xps.IXpsOMGradientStop_head, startPoint: POINTER(Windows.Win32.Storage.Xps.XPS_POINT_head), endPoint: POINTER(Windows.Win32.Storage.Xps.XPS_POINT_head), linearGradientBrush: POINTER(Windows.Win32.Storage.Xps.IXpsOMLinearGradientBrush_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def CreateRadialGradientBrush(gradStop1: Windows.Win32.Storage.Xps.IXpsOMGradientStop_head, gradStop2: Windows.Win32.Storage.Xps.IXpsOMGradientStop_head, centerPoint: POINTER(Windows.Win32.Storage.Xps.XPS_POINT_head), gradientOrigin: POINTER(Windows.Win32.Storage.Xps.XPS_POINT_head), radiiSizes: POINTER(Windows.Win32.Storage.Xps.XPS_SIZE_head), radialGradientBrush: POINTER(Windows.Win32.Storage.Xps.IXpsOMRadialGradientBrush_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def CreateCoreProperties(partUri: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, coreProperties: POINTER(Windows.Win32.Storage.Xps.IXpsOMCoreProperties_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def CreateDictionary(dictionary: POINTER(Windows.Win32.Storage.Xps.IXpsOMDictionary_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def CreatePartUriCollection(partUriCollection: POINTER(Windows.Win32.Storage.Xps.IXpsOMPartUriCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def CreatePackageWriterOnFile(fileName: Windows.Win32.Foundation.PWSTR, securityAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head), flagsAndAttributes: UInt32, optimizeMarkupSize: Windows.Win32.Foundation.BOOL, interleaving: Windows.Win32.Storage.Xps.XPS_INTERLEAVING, documentSequencePartName: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, coreProperties: Windows.Win32.Storage.Xps.IXpsOMCoreProperties_head, packageThumbnail: Windows.Win32.Storage.Xps.IXpsOMImageResource_head, documentSequencePrintTicket: Windows.Win32.Storage.Xps.IXpsOMPrintTicketResource_head, discardControlPartName: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, packageWriter: POINTER(Windows.Win32.Storage.Xps.IXpsOMPackageWriter_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def CreatePackageWriterOnStream(outputStream: Windows.Win32.System.Com.ISequentialStream_head, optimizeMarkupSize: Windows.Win32.Foundation.BOOL, interleaving: Windows.Win32.Storage.Xps.XPS_INTERLEAVING, documentSequencePartName: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, coreProperties: Windows.Win32.Storage.Xps.IXpsOMCoreProperties_head, packageThumbnail: Windows.Win32.Storage.Xps.IXpsOMImageResource_head, documentSequencePrintTicket: Windows.Win32.Storage.Xps.IXpsOMPrintTicketResource_head, discardControlPartName: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, packageWriter: POINTER(Windows.Win32.Storage.Xps.IXpsOMPackageWriter_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def CreatePartUri(uri: Windows.Win32.Foundation.PWSTR, partUri: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def CreateReadOnlyStreamOnFile(filename: Windows.Win32.Foundation.PWSTR, stream: POINTER(Windows.Win32.System.Com.IStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMObjectFactory1(c_void_p):
    extends: Windows.Win32.Storage.Xps.IXpsOMObjectFactory
    Guid = Guid('0a91b617-d612-4181-bf-7c-be-58-24-e9-cc-8f')
    @commethod(40)
    def GetDocumentTypeFromFile(filename: Windows.Win32.Foundation.PWSTR, documentType: POINTER(Windows.Win32.Storage.Xps.XPS_DOCUMENT_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def GetDocumentTypeFromStream(xpsDocumentStream: Windows.Win32.System.Com.IStream_head, documentType: POINTER(Windows.Win32.Storage.Xps.XPS_DOCUMENT_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def ConvertHDPhotoToJpegXR(imageResource: Windows.Win32.Storage.Xps.IXpsOMImageResource_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def ConvertJpegXRToHDPhoto(imageResource: Windows.Win32.Storage.Xps.IXpsOMImageResource_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def CreatePackageWriterOnFile1(fileName: Windows.Win32.Foundation.PWSTR, securityAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head), flagsAndAttributes: UInt32, optimizeMarkupSize: Windows.Win32.Foundation.BOOL, interleaving: Windows.Win32.Storage.Xps.XPS_INTERLEAVING, documentSequencePartName: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, coreProperties: Windows.Win32.Storage.Xps.IXpsOMCoreProperties_head, packageThumbnail: Windows.Win32.Storage.Xps.IXpsOMImageResource_head, documentSequencePrintTicket: Windows.Win32.Storage.Xps.IXpsOMPrintTicketResource_head, discardControlPartName: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, documentType: Windows.Win32.Storage.Xps.XPS_DOCUMENT_TYPE, packageWriter: POINTER(Windows.Win32.Storage.Xps.IXpsOMPackageWriter_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def CreatePackageWriterOnStream1(outputStream: Windows.Win32.System.Com.ISequentialStream_head, optimizeMarkupSize: Windows.Win32.Foundation.BOOL, interleaving: Windows.Win32.Storage.Xps.XPS_INTERLEAVING, documentSequencePartName: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, coreProperties: Windows.Win32.Storage.Xps.IXpsOMCoreProperties_head, packageThumbnail: Windows.Win32.Storage.Xps.IXpsOMImageResource_head, documentSequencePrintTicket: Windows.Win32.Storage.Xps.IXpsOMPrintTicketResource_head, discardControlPartName: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, documentType: Windows.Win32.Storage.Xps.XPS_DOCUMENT_TYPE, packageWriter: POINTER(Windows.Win32.Storage.Xps.IXpsOMPackageWriter_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def CreatePackage1(package: POINTER(Windows.Win32.Storage.Xps.IXpsOMPackage1_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def CreatePackageFromStream1(stream: Windows.Win32.System.Com.IStream_head, reuseObjects: Windows.Win32.Foundation.BOOL, package: POINTER(Windows.Win32.Storage.Xps.IXpsOMPackage1_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def CreatePackageFromFile1(filename: Windows.Win32.Foundation.PWSTR, reuseObjects: Windows.Win32.Foundation.BOOL, package: POINTER(Windows.Win32.Storage.Xps.IXpsOMPackage1_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def CreatePage1(pageDimensions: POINTER(Windows.Win32.Storage.Xps.XPS_SIZE_head), language: Windows.Win32.Foundation.PWSTR, partUri: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, page: POINTER(Windows.Win32.Storage.Xps.IXpsOMPage1_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def CreatePageFromStream1(pageMarkupStream: Windows.Win32.System.Com.IStream_head, partUri: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, resources: Windows.Win32.Storage.Xps.IXpsOMPartResources_head, reuseObjects: Windows.Win32.Foundation.BOOL, page: POINTER(Windows.Win32.Storage.Xps.IXpsOMPage1_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def CreateRemoteDictionaryResourceFromStream1(dictionaryMarkupStream: Windows.Win32.System.Com.IStream_head, partUri: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, resources: Windows.Win32.Storage.Xps.IXpsOMPartResources_head, dictionaryResource: POINTER(Windows.Win32.Storage.Xps.IXpsOMRemoteDictionaryResource_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMPackage(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('18c3df65-81e1-4674-91-dc-fc-45-2f-5a-41-6f')
    @commethod(3)
    def GetDocumentSequence(documentSequence: POINTER(Windows.Win32.Storage.Xps.IXpsOMDocumentSequence_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetDocumentSequence(documentSequence: Windows.Win32.Storage.Xps.IXpsOMDocumentSequence_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCoreProperties(coreProperties: POINTER(Windows.Win32.Storage.Xps.IXpsOMCoreProperties_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetCoreProperties(coreProperties: Windows.Win32.Storage.Xps.IXpsOMCoreProperties_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDiscardControlPartName(discardControlPartUri: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetDiscardControlPartName(discardControlPartUri: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetThumbnailResource(imageResource: POINTER(Windows.Win32.Storage.Xps.IXpsOMImageResource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetThumbnailResource(imageResource: Windows.Win32.Storage.Xps.IXpsOMImageResource_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def WriteToFile(fileName: Windows.Win32.Foundation.PWSTR, securityAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head), flagsAndAttributes: UInt32, optimizeMarkupSize: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def WriteToStream(stream: Windows.Win32.System.Com.ISequentialStream_head, optimizeMarkupSize: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMPackage1(c_void_p):
    extends: Windows.Win32.Storage.Xps.IXpsOMPackage
    Guid = Guid('95a9435e-12bb-461b-8e-7f-c6-ad-b0-4c-d9-6a')
    @commethod(13)
    def GetDocumentType(documentType: POINTER(Windows.Win32.Storage.Xps.XPS_DOCUMENT_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def WriteToFile1(fileName: Windows.Win32.Foundation.PWSTR, securityAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head), flagsAndAttributes: UInt32, optimizeMarkupSize: Windows.Win32.Foundation.BOOL, documentType: Windows.Win32.Storage.Xps.XPS_DOCUMENT_TYPE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def WriteToStream1(outputStream: Windows.Win32.System.Com.ISequentialStream_head, optimizeMarkupSize: Windows.Win32.Foundation.BOOL, documentType: Windows.Win32.Storage.Xps.XPS_DOCUMENT_TYPE) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMPackageTarget(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('219a9db0-4959-47d0-80-34-b1-ce-84-f4-1a-4d')
    @commethod(3)
    def CreateXpsOMPackageWriter(documentSequencePartName: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, documentSequencePrintTicket: Windows.Win32.Storage.Xps.IXpsOMPrintTicketResource_head, discardControlPartName: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, packageWriter: POINTER(Windows.Win32.Storage.Xps.IXpsOMPackageWriter_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMPackageWriter(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('4e2aa182-a443-42c6-b4-1b-4f-8e-9d-e7-3f-f9')
    @commethod(3)
    def StartNewDocument(documentPartName: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, documentPrintTicket: Windows.Win32.Storage.Xps.IXpsOMPrintTicketResource_head, documentStructure: Windows.Win32.Storage.Xps.IXpsOMDocumentStructureResource_head, signatureBlockResources: Windows.Win32.Storage.Xps.IXpsOMSignatureBlockResourceCollection_head, restrictedFonts: Windows.Win32.Storage.Xps.IXpsOMPartUriCollection_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddPage(page: Windows.Win32.Storage.Xps.IXpsOMPage_head, advisoryPageDimensions: POINTER(Windows.Win32.Storage.Xps.XPS_SIZE_head), discardableResourceParts: Windows.Win32.Storage.Xps.IXpsOMPartUriCollection_head, storyFragments: Windows.Win32.Storage.Xps.IXpsOMStoryFragmentsResource_head, pagePrintTicket: Windows.Win32.Storage.Xps.IXpsOMPrintTicketResource_head, pageThumbnail: Windows.Win32.Storage.Xps.IXpsOMImageResource_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddResource(resource: Windows.Win32.Storage.Xps.IXpsOMResource_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Close() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def IsClosed(isClosed: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMPackageWriter3D(c_void_p):
    extends: Windows.Win32.Storage.Xps.IXpsOMPackageWriter
    Guid = Guid('e8a45033-640e-43fa-9b-df-fd-de-aa-31-c6-a0')
    @commethod(8)
    def AddModelTexture(texturePartName: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, textureData: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetModelPrintTicket(printTicketPartName: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, printTicketData: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMPage(c_void_p):
    extends: Windows.Win32.Storage.Xps.IXpsOMPart
    Guid = Guid('d3e18888-f120-4fee-8c-68-35-29-6e-ae-91-d4')
    @commethod(5)
    def GetOwner(pageReference: POINTER(Windows.Win32.Storage.Xps.IXpsOMPageReference_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetVisuals(visuals: POINTER(Windows.Win32.Storage.Xps.IXpsOMVisualCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetPageDimensions(pageDimensions: POINTER(Windows.Win32.Storage.Xps.XPS_SIZE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetPageDimensions(pageDimensions: POINTER(Windows.Win32.Storage.Xps.XPS_SIZE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetContentBox(contentBox: POINTER(Windows.Win32.Storage.Xps.XPS_RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetContentBox(contentBox: POINTER(Windows.Win32.Storage.Xps.XPS_RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetBleedBox(bleedBox: POINTER(Windows.Win32.Storage.Xps.XPS_RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetBleedBox(bleedBox: POINTER(Windows.Win32.Storage.Xps.XPS_RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetLanguage(language: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetLanguage(language: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetName(name: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetName(name: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetIsHyperlinkTarget(isHyperlinkTarget: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetIsHyperlinkTarget(isHyperlinkTarget: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetDictionary(resourceDictionary: POINTER(Windows.Win32.Storage.Xps.IXpsOMDictionary_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetDictionaryLocal(resourceDictionary: POINTER(Windows.Win32.Storage.Xps.IXpsOMDictionary_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def SetDictionaryLocal(resourceDictionary: Windows.Win32.Storage.Xps.IXpsOMDictionary_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetDictionaryResource(remoteDictionaryResource: POINTER(Windows.Win32.Storage.Xps.IXpsOMRemoteDictionaryResource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetDictionaryResource(remoteDictionaryResource: Windows.Win32.Storage.Xps.IXpsOMRemoteDictionaryResource_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def Write(stream: Windows.Win32.System.Com.ISequentialStream_head, optimizeMarkupSize: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GenerateUnusedLookupKey(type: Windows.Win32.Storage.Xps.XPS_OBJECT_TYPE, key: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def Clone(page: POINTER(Windows.Win32.Storage.Xps.IXpsOMPage_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMPage1(c_void_p):
    extends: Windows.Win32.Storage.Xps.IXpsOMPage
    Guid = Guid('305b60ef-6892-4dda-9c-bb-3a-a6-59-74-50-8a')
    @commethod(27)
    def GetDocumentType(documentType: POINTER(Windows.Win32.Storage.Xps.XPS_DOCUMENT_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def Write1(stream: Windows.Win32.System.Com.ISequentialStream_head, optimizeMarkupSize: Windows.Win32.Foundation.BOOL, documentType: Windows.Win32.Storage.Xps.XPS_DOCUMENT_TYPE) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMPageReference(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('ed360180-6f92-4998-89-0d-2f-20-85-31-a0-a0')
    @commethod(3)
    def GetOwner(document: POINTER(Windows.Win32.Storage.Xps.IXpsOMDocument_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPage(page: POINTER(Windows.Win32.Storage.Xps.IXpsOMPage_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetPage(page: Windows.Win32.Storage.Xps.IXpsOMPage_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def DiscardPage() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def IsPageLoaded(isPageLoaded: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetAdvisoryPageDimensions(pageDimensions: POINTER(Windows.Win32.Storage.Xps.XPS_SIZE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetAdvisoryPageDimensions(pageDimensions: POINTER(Windows.Win32.Storage.Xps.XPS_SIZE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetStoryFragmentsResource(storyFragmentsResource: POINTER(Windows.Win32.Storage.Xps.IXpsOMStoryFragmentsResource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetStoryFragmentsResource(storyFragmentsResource: Windows.Win32.Storage.Xps.IXpsOMStoryFragmentsResource_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetPrintTicketResource(printTicketResource: POINTER(Windows.Win32.Storage.Xps.IXpsOMPrintTicketResource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetPrintTicketResource(printTicketResource: Windows.Win32.Storage.Xps.IXpsOMPrintTicketResource_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetThumbnailResource(imageResource: POINTER(Windows.Win32.Storage.Xps.IXpsOMImageResource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetThumbnailResource(imageResource: Windows.Win32.Storage.Xps.IXpsOMImageResource_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def CollectLinkTargets(linkTargets: POINTER(Windows.Win32.Storage.Xps.IXpsOMNameCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def CollectPartResources(partResources: POINTER(Windows.Win32.Storage.Xps.IXpsOMPartResources_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def HasRestrictedFonts(restrictedFonts: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def Clone(pageReference: POINTER(Windows.Win32.Storage.Xps.IXpsOMPageReference_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMPageReferenceCollection(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('ca16ba4d-e7b9-45c5-95-8b-f9-80-22-47-37-45')
    @commethod(3)
    def GetCount(count: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(index: UInt32, pageReference: POINTER(Windows.Win32.Storage.Xps.IXpsOMPageReference_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def InsertAt(index: UInt32, pageReference: Windows.Win32.Storage.Xps.IXpsOMPageReference_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveAt(index: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetAt(index: UInt32, pageReference: Windows.Win32.Storage.Xps.IXpsOMPageReference_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Append(pageReference: Windows.Win32.Storage.Xps.IXpsOMPageReference_head) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMPart(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('74eb2f0b-a91e-4486-af-ac-0f-ab-ec-a3-df-c6')
    @commethod(3)
    def GetPartName(partUri: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetPartName(partUri: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMPartResources(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f4cf7729-4864-4275-99-b3-a8-71-71-63-ec-af')
    @commethod(3)
    def GetFontResources(fontResources: POINTER(Windows.Win32.Storage.Xps.IXpsOMFontResourceCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetImageResources(imageResources: POINTER(Windows.Win32.Storage.Xps.IXpsOMImageResourceCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetColorProfileResources(colorProfileResources: POINTER(Windows.Win32.Storage.Xps.IXpsOMColorProfileResourceCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetRemoteDictionaryResources(dictionaryResources: POINTER(Windows.Win32.Storage.Xps.IXpsOMRemoteDictionaryResourceCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMPartUriCollection(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('57c650d4-067c-4893-8c-33-f6-2a-06-33-73-0f')
    @commethod(3)
    def GetCount(count: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(index: UInt32, partUri: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def InsertAt(index: UInt32, partUri: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveAt(index: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetAt(index: UInt32, partUri: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Append(partUri: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMPath(c_void_p):
    extends: Windows.Win32.Storage.Xps.IXpsOMVisual
    Guid = Guid('37d38bb6-3ee9-4110-93-12-14-b1-94-16-33-37')
    @commethod(30)
    def GetGeometry(geometry: POINTER(Windows.Win32.Storage.Xps.IXpsOMGeometry_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def GetGeometryLocal(geometry: POINTER(Windows.Win32.Storage.Xps.IXpsOMGeometry_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def SetGeometryLocal(geometry: Windows.Win32.Storage.Xps.IXpsOMGeometry_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def GetGeometryLookup(lookup: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def SetGeometryLookup(lookup: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def GetAccessibilityShortDescription(shortDescription: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def SetAccessibilityShortDescription(shortDescription: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def GetAccessibilityLongDescription(longDescription: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def SetAccessibilityLongDescription(longDescription: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def GetSnapsToPixels(snapsToPixels: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def SetSnapsToPixels(snapsToPixels: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def GetStrokeBrush(brush: POINTER(Windows.Win32.Storage.Xps.IXpsOMBrush_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def GetStrokeBrushLocal(brush: POINTER(Windows.Win32.Storage.Xps.IXpsOMBrush_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def SetStrokeBrushLocal(brush: Windows.Win32.Storage.Xps.IXpsOMBrush_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def GetStrokeBrushLookup(lookup: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def SetStrokeBrushLookup(lookup: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def GetStrokeDashes(strokeDashes: POINTER(Windows.Win32.Storage.Xps.IXpsOMDashCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def GetStrokeDashCap(strokeDashCap: POINTER(Windows.Win32.Storage.Xps.XPS_DASH_CAP)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def SetStrokeDashCap(strokeDashCap: Windows.Win32.Storage.Xps.XPS_DASH_CAP) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def GetStrokeDashOffset(strokeDashOffset: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def SetStrokeDashOffset(strokeDashOffset: Single) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def GetStrokeStartLineCap(strokeStartLineCap: POINTER(Windows.Win32.Storage.Xps.XPS_LINE_CAP)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def SetStrokeStartLineCap(strokeStartLineCap: Windows.Win32.Storage.Xps.XPS_LINE_CAP) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def GetStrokeEndLineCap(strokeEndLineCap: POINTER(Windows.Win32.Storage.Xps.XPS_LINE_CAP)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def SetStrokeEndLineCap(strokeEndLineCap: Windows.Win32.Storage.Xps.XPS_LINE_CAP) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def GetStrokeLineJoin(strokeLineJoin: POINTER(Windows.Win32.Storage.Xps.XPS_LINE_JOIN)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def SetStrokeLineJoin(strokeLineJoin: Windows.Win32.Storage.Xps.XPS_LINE_JOIN) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def GetStrokeMiterLimit(strokeMiterLimit: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(58)
    def SetStrokeMiterLimit(strokeMiterLimit: Single) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def GetStrokeThickness(strokeThickness: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(60)
    def SetStrokeThickness(strokeThickness: Single) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(61)
    def GetFillBrush(brush: POINTER(Windows.Win32.Storage.Xps.IXpsOMBrush_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(62)
    def GetFillBrushLocal(brush: POINTER(Windows.Win32.Storage.Xps.IXpsOMBrush_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(63)
    def SetFillBrushLocal(brush: Windows.Win32.Storage.Xps.IXpsOMBrush_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(64)
    def GetFillBrushLookup(lookup: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(65)
    def SetFillBrushLookup(lookup: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(66)
    def Clone(path: POINTER(Windows.Win32.Storage.Xps.IXpsOMPath_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMPrintTicketResource(c_void_p):
    extends: Windows.Win32.Storage.Xps.IXpsOMResource
    Guid = Guid('e7ff32d2-34aa-499b-bb-e9-9c-d4-ee-6c-59-f7')
    @commethod(5)
    def GetStream(stream: POINTER(Windows.Win32.System.Com.IStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetContent(sourceStream: Windows.Win32.System.Com.IStream_head, partName: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMRadialGradientBrush(c_void_p):
    extends: Windows.Win32.Storage.Xps.IXpsOMGradientBrush
    Guid = Guid('75f207e5-08bf-413c-96-b1-b8-2b-40-64-17-6b')
    @commethod(17)
    def GetCenter(center: POINTER(Windows.Win32.Storage.Xps.XPS_POINT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetCenter(center: POINTER(Windows.Win32.Storage.Xps.XPS_POINT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetRadiiSizes(radiiSizes: POINTER(Windows.Win32.Storage.Xps.XPS_SIZE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SetRadiiSizes(radiiSizes: POINTER(Windows.Win32.Storage.Xps.XPS_SIZE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetGradientOrigin(origin: POINTER(Windows.Win32.Storage.Xps.XPS_POINT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SetGradientOrigin(origin: POINTER(Windows.Win32.Storage.Xps.XPS_POINT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def Clone(radialGradientBrush: POINTER(Windows.Win32.Storage.Xps.IXpsOMRadialGradientBrush_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMRemoteDictionaryResource(c_void_p):
    extends: Windows.Win32.Storage.Xps.IXpsOMResource
    Guid = Guid('c9bd7cd4-e16a-4bf8-8c-84-c9-50-af-7a-30-61')
    @commethod(5)
    def GetDictionary(dictionary: POINTER(Windows.Win32.Storage.Xps.IXpsOMDictionary_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetDictionary(dictionary: Windows.Win32.Storage.Xps.IXpsOMDictionary_head) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMRemoteDictionaryResource1(c_void_p):
    extends: Windows.Win32.Storage.Xps.IXpsOMRemoteDictionaryResource
    Guid = Guid('bf8fc1d4-9d46-4141-ba-5f-94-bb-92-50-d0-41')
    @commethod(7)
    def GetDocumentType(documentType: POINTER(Windows.Win32.Storage.Xps.XPS_DOCUMENT_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Write1(stream: Windows.Win32.System.Com.ISequentialStream_head, documentType: Windows.Win32.Storage.Xps.XPS_DOCUMENT_TYPE) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMRemoteDictionaryResourceCollection(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('5c38db61-7fec-464a-87-bd-41-e3-be-f0-18-be')
    @commethod(3)
    def GetCount(count: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(index: UInt32, object: POINTER(Windows.Win32.Storage.Xps.IXpsOMRemoteDictionaryResource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def InsertAt(index: UInt32, object: Windows.Win32.Storage.Xps.IXpsOMRemoteDictionaryResource_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveAt(index: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetAt(index: UInt32, object: Windows.Win32.Storage.Xps.IXpsOMRemoteDictionaryResource_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Append(object: Windows.Win32.Storage.Xps.IXpsOMRemoteDictionaryResource_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetByPartName(partName: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, remoteDictionaryResource: POINTER(Windows.Win32.Storage.Xps.IXpsOMRemoteDictionaryResource_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMResource(c_void_p):
    extends: Windows.Win32.Storage.Xps.IXpsOMPart
    Guid = Guid('da2ac0a2-73a2-4975-ad-14-74-09-7c-3f-f3-a5')
class IXpsOMShareable(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('7137398f-2fc1-454d-8c-6a-2c-31-15-a1-6e-ce')
    @commethod(3)
    def GetOwner(owner: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetType(type: POINTER(Windows.Win32.Storage.Xps.XPS_OBJECT_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMSignatureBlockResource(c_void_p):
    extends: Windows.Win32.Storage.Xps.IXpsOMResource
    Guid = Guid('4776ad35-2e04-4357-87-43-eb-f6-c1-71-a9-05')
    @commethod(5)
    def GetOwner(owner: POINTER(Windows.Win32.Storage.Xps.IXpsOMDocument_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetStream(stream: POINTER(Windows.Win32.System.Com.IStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetContent(sourceStream: Windows.Win32.System.Com.IStream_head, partName: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMSignatureBlockResourceCollection(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('ab8f5d8e-351b-4d33-aa-ed-fa-56-f0-02-29-31')
    @commethod(3)
    def GetCount(count: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(index: UInt32, signatureBlockResource: POINTER(Windows.Win32.Storage.Xps.IXpsOMSignatureBlockResource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def InsertAt(index: UInt32, signatureBlockResource: Windows.Win32.Storage.Xps.IXpsOMSignatureBlockResource_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveAt(index: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetAt(index: UInt32, signatureBlockResource: Windows.Win32.Storage.Xps.IXpsOMSignatureBlockResource_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Append(signatureBlockResource: Windows.Win32.Storage.Xps.IXpsOMSignatureBlockResource_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetByPartName(partName: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, signatureBlockResource: POINTER(Windows.Win32.Storage.Xps.IXpsOMSignatureBlockResource_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMSolidColorBrush(c_void_p):
    extends: Windows.Win32.Storage.Xps.IXpsOMBrush
    Guid = Guid('a06f9f05-3be9-4763-98-a8-09-4f-c6-72-e4-88')
    @commethod(7)
    def GetColor(color: POINTER(Windows.Win32.Storage.Xps.XPS_COLOR_head), colorProfile: POINTER(Windows.Win32.Storage.Xps.IXpsOMColorProfileResource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetColor(color: POINTER(Windows.Win32.Storage.Xps.XPS_COLOR_head), colorProfile: Windows.Win32.Storage.Xps.IXpsOMColorProfileResource_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Clone(solidColorBrush: POINTER(Windows.Win32.Storage.Xps.IXpsOMSolidColorBrush_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMStoryFragmentsResource(c_void_p):
    extends: Windows.Win32.Storage.Xps.IXpsOMResource
    Guid = Guid('c2b3ca09-0473-4282-87-ae-17-80-86-32-23-f0')
    @commethod(5)
    def GetOwner(owner: POINTER(Windows.Win32.Storage.Xps.IXpsOMPageReference_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetStream(stream: POINTER(Windows.Win32.System.Com.IStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetContent(sourceStream: Windows.Win32.System.Com.IStream_head, partName: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMThumbnailGenerator(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('15b873d5-1971-41e8-83-a3-65-78-40-30-64-c7')
    @commethod(3)
    def GenerateThumbnail(page: Windows.Win32.Storage.Xps.IXpsOMPage_head, thumbnailType: Windows.Win32.Storage.Xps.XPS_IMAGE_TYPE, thumbnailSize: Windows.Win32.Storage.Xps.XPS_THUMBNAIL_SIZE, imageResourcePartName: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, imageResource: POINTER(Windows.Win32.Storage.Xps.IXpsOMImageResource_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMTileBrush(c_void_p):
    extends: Windows.Win32.Storage.Xps.IXpsOMBrush
    Guid = Guid('0fc2328d-d722-4a54-b2-ec-be-90-21-8a-78-9e')
    @commethod(7)
    def GetTransform(transform: POINTER(Windows.Win32.Storage.Xps.IXpsOMMatrixTransform_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetTransformLocal(transform: POINTER(Windows.Win32.Storage.Xps.IXpsOMMatrixTransform_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetTransformLocal(transform: Windows.Win32.Storage.Xps.IXpsOMMatrixTransform_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetTransformLookup(key: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetTransformLookup(key: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetViewbox(viewbox: POINTER(Windows.Win32.Storage.Xps.XPS_RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetViewbox(viewbox: POINTER(Windows.Win32.Storage.Xps.XPS_RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetViewport(viewport: POINTER(Windows.Win32.Storage.Xps.XPS_RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetViewport(viewport: POINTER(Windows.Win32.Storage.Xps.XPS_RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetTileMode(tileMode: POINTER(Windows.Win32.Storage.Xps.XPS_TILE_MODE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetTileMode(tileMode: Windows.Win32.Storage.Xps.XPS_TILE_MODE) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMVisual(c_void_p):
    extends: Windows.Win32.Storage.Xps.IXpsOMShareable
    Guid = Guid('bc3e7333-fb0b-4af3-a8-19-0b-4e-aa-d0-d2-fd')
    @commethod(5)
    def GetTransform(matrixTransform: POINTER(Windows.Win32.Storage.Xps.IXpsOMMatrixTransform_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetTransformLocal(matrixTransform: POINTER(Windows.Win32.Storage.Xps.IXpsOMMatrixTransform_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetTransformLocal(matrixTransform: Windows.Win32.Storage.Xps.IXpsOMMatrixTransform_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetTransformLookup(key: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetTransformLookup(key: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetClipGeometry(clipGeometry: POINTER(Windows.Win32.Storage.Xps.IXpsOMGeometry_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetClipGeometryLocal(clipGeometry: POINTER(Windows.Win32.Storage.Xps.IXpsOMGeometry_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetClipGeometryLocal(clipGeometry: Windows.Win32.Storage.Xps.IXpsOMGeometry_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetClipGeometryLookup(key: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetClipGeometryLookup(key: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetOpacity(opacity: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetOpacity(opacity: Single) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetOpacityMaskBrush(opacityMaskBrush: POINTER(Windows.Win32.Storage.Xps.IXpsOMBrush_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetOpacityMaskBrushLocal(opacityMaskBrush: POINTER(Windows.Win32.Storage.Xps.IXpsOMBrush_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetOpacityMaskBrushLocal(opacityMaskBrush: Windows.Win32.Storage.Xps.IXpsOMBrush_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetOpacityMaskBrushLookup(key: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def SetOpacityMaskBrushLookup(key: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetName(name: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetName(name: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetIsHyperlinkTarget(isHyperlink: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def SetIsHyperlinkTarget(isHyperlink: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetHyperlinkNavigateUri(hyperlinkUri: POINTER(Windows.Win32.System.Com.IUri_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def SetHyperlinkNavigateUri(hyperlinkUri: Windows.Win32.System.Com.IUri_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetLanguage(language: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def SetLanguage(language: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMVisualBrush(c_void_p):
    extends: Windows.Win32.Storage.Xps.IXpsOMTileBrush
    Guid = Guid('97e294af-5b37-46b4-80-57-87-4d-2f-64-11-9b')
    @commethod(18)
    def GetVisual(visual: POINTER(Windows.Win32.Storage.Xps.IXpsOMVisual_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetVisualLocal(visual: POINTER(Windows.Win32.Storage.Xps.IXpsOMVisual_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SetVisualLocal(visual: Windows.Win32.Storage.Xps.IXpsOMVisual_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetVisualLookup(lookup: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SetVisualLookup(lookup: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def Clone(visualBrush: POINTER(Windows.Win32.Storage.Xps.IXpsOMVisualBrush_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsOMVisualCollection(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('94d8abde-ab91-46a8-82-b7-f5-b0-5e-f0-1a-96')
    @commethod(3)
    def GetCount(count: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(index: UInt32, object: POINTER(Windows.Win32.Storage.Xps.IXpsOMVisual_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def InsertAt(index: UInt32, object: Windows.Win32.Storage.Xps.IXpsOMVisual_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveAt(index: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetAt(index: UInt32, object: Windows.Win32.Storage.Xps.IXpsOMVisual_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Append(object: Windows.Win32.Storage.Xps.IXpsOMVisual_head) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsSignature(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('6ae4c93e-1ade-42fb-89-8b-3a-56-58-28-48-57')
    @commethod(3)
    def GetSignatureId(sigId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSignatureValue(signatureHashValue: POINTER(c_char_p_no), count: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCertificateEnumerator(certificateEnumerator: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcCertificateEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSigningTime(sigDateTimeString: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetSigningTimeFormat(timeFormat: POINTER(Windows.Win32.Storage.Packaging.Opc.OPC_SIGNATURE_TIME_FORMAT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetSignaturePartName(signaturePartName: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Verify(x509Certificate: POINTER(Windows.Win32.Security.Cryptography.CERT_CONTEXT_head), sigStatus: POINTER(Windows.Win32.Storage.Xps.XPS_SIGNATURE_STATUS)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetPolicy(policy: POINTER(Windows.Win32.Storage.Xps.XPS_SIGN_POLICY)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetCustomObjectEnumerator(customObjectEnumerator: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcSignatureCustomObjectEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetCustomReferenceEnumerator(customReferenceEnumerator: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcSignatureReferenceEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetSignatureXml(signatureXml: POINTER(c_char_p_no), count: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetSignatureXml(signatureXml: c_char_p_no, count: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsSignatureBlock(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('151fac09-0b97-4ac6-a3-23-5e-42-97-d4-32-2b')
    @commethod(3)
    def GetRequests(requests: POINTER(Windows.Win32.Storage.Xps.IXpsSignatureRequestCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPartName(partName: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDocumentIndex(fixedDocumentIndex: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetDocumentName(fixedDocumentName: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateRequest(requestId: Windows.Win32.Foundation.PWSTR, signatureRequest: POINTER(Windows.Win32.Storage.Xps.IXpsSignatureRequest_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsSignatureBlockCollection(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('23397050-fe99-467a-8d-ce-92-37-f0-74-ff-e4')
    @commethod(3)
    def GetCount(count: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(index: UInt32, signatureBlock: POINTER(Windows.Win32.Storage.Xps.IXpsSignatureBlock_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RemoveAt(index: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsSignatureCollection(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a2d1d95d-add2-4dff-ab-27-6b-9c-64-5f-f3-22')
    @commethod(3)
    def GetCount(count: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(index: UInt32, signature: POINTER(Windows.Win32.Storage.Xps.IXpsSignature_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RemoveAt(index: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsSignatureManager(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d3e8d338-fdc4-4afc-80-b5-d5-32-a1-78-2e-e1')
    @commethod(3)
    def LoadPackageFile(fileName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def LoadPackageStream(stream: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Sign(signOptions: Windows.Win32.Storage.Xps.IXpsSigningOptions_head, x509Certificate: POINTER(Windows.Win32.Security.Cryptography.CERT_CONTEXT_head), signature: POINTER(Windows.Win32.Storage.Xps.IXpsSignature_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSignatureOriginPartName(signatureOriginPartName: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetSignatureOriginPartName(signatureOriginPartName: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetSignatures(signatures: POINTER(Windows.Win32.Storage.Xps.IXpsSignatureCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AddSignatureBlock(partName: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head, fixedDocumentIndex: UInt32, signatureBlock: POINTER(Windows.Win32.Storage.Xps.IXpsSignatureBlock_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetSignatureBlocks(signatureBlocks: POINTER(Windows.Win32.Storage.Xps.IXpsSignatureBlockCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def CreateSigningOptions(signingOptions: POINTER(Windows.Win32.Storage.Xps.IXpsSigningOptions_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SavePackageToFile(fileName: Windows.Win32.Foundation.PWSTR, securityAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head), flagsAndAttributes: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SavePackageToStream(stream: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsSignatureRequest(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('ac58950b-7208-4b2d-b2-c4-95-10-83-d3-b8-eb')
    @commethod(3)
    def GetIntent(intent: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetIntent(intent: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetRequestedSigner(signerName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetRequestedSigner(signerName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetRequestSignByDate(dateString: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetRequestSignByDate(dateString: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetSigningLocale(place: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetSigningLocale(place: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetSpotLocation(pageIndex: POINTER(Int32), pagePartName: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head), x: POINTER(Single), y: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetSpotLocation(pageIndex: Int32, x: Single, y: Single) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetRequestId(requestId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetSignature(signature: POINTER(Windows.Win32.Storage.Xps.IXpsSignature_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsSignatureRequestCollection(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f0253e68-9f19-412e-9b-4f-54-d3-b0-ac-6c-d9')
    @commethod(3)
    def GetCount(count: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(index: UInt32, signatureRequest: POINTER(Windows.Win32.Storage.Xps.IXpsSignatureRequest_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RemoveAt(index: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsSigningOptions(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('7718eae4-3215-49be-af-5b-59-4f-ef-7f-cf-a6')
    @commethod(3)
    def GetSignatureId(signatureId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetSignatureId(signatureId: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSignatureMethod(signatureMethod: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetSignatureMethod(signatureMethod: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDigestMethod(digestMethod: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetDigestMethod(digestMethod: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetSignaturePartName(signaturePartName: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetSignaturePartName(signaturePartName: Windows.Win32.Storage.Packaging.Opc.IOpcPartUri_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetPolicy(policy: POINTER(Windows.Win32.Storage.Xps.XPS_SIGN_POLICY)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetPolicy(policy: Windows.Win32.Storage.Xps.XPS_SIGN_POLICY) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetSigningTimeFormat(timeFormat: POINTER(Windows.Win32.Storage.Packaging.Opc.OPC_SIGNATURE_TIME_FORMAT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetSigningTimeFormat(timeFormat: Windows.Win32.Storage.Packaging.Opc.OPC_SIGNATURE_TIME_FORMAT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetCustomObjects(customObjectSet: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcSignatureCustomObjectSet_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetCustomReferences(customReferenceSet: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcSignatureReferenceSet_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetCertificateSet(certificateSet: POINTER(Windows.Win32.Storage.Packaging.Opc.IOpcCertificateSet_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetFlags(flags: POINTER(Windows.Win32.Storage.Xps.XPS_SIGN_FLAGS)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetFlags(flags: Windows.Win32.Storage.Xps.XPS_SIGN_FLAGS) -> Windows.Win32.Foundation.HRESULT: ...
PRINT_WINDOW_FLAGS = UInt32
PW_CLIENTONLY: PRINT_WINDOW_FLAGS = 1
class PSFEATURE_CUSTPAPER(Structure):
    lOrientation: Int32
    lWidth: Int32
    lHeight: Int32
    lWidthOffset: Int32
    lHeightOffset: Int32
class PSFEATURE_OUTPUT(Structure):
    bPageIndependent: Windows.Win32.Foundation.BOOL
    bSetPageDevice: Windows.Win32.Foundation.BOOL
class PSINJECTDATA(Structure):
    DataBytes: UInt32
    InjectionPoint: Windows.Win32.Storage.Xps.PSINJECT_POINT
    PageNumber: UInt16
PSINJECT_POINT = UInt16
PSINJECT_BEGINSTREAM: PSINJECT_POINT = 1
PSINJECT_PSADOBE: PSINJECT_POINT = 2
PSINJECT_PAGESATEND: PSINJECT_POINT = 3
PSINJECT_PAGES: PSINJECT_POINT = 4
PSINJECT_DOCNEEDEDRES: PSINJECT_POINT = 5
PSINJECT_DOCSUPPLIEDRES: PSINJECT_POINT = 6
PSINJECT_PAGEORDER: PSINJECT_POINT = 7
PSINJECT_ORIENTATION: PSINJECT_POINT = 8
PSINJECT_BOUNDINGBOX: PSINJECT_POINT = 9
PSINJECT_DOCUMENTPROCESSCOLORS: PSINJECT_POINT = 10
PSINJECT_COMMENTS: PSINJECT_POINT = 11
PSINJECT_BEGINDEFAULTS: PSINJECT_POINT = 12
PSINJECT_ENDDEFAULTS: PSINJECT_POINT = 13
PSINJECT_BEGINPROLOG: PSINJECT_POINT = 14
PSINJECT_ENDPROLOG: PSINJECT_POINT = 15
PSINJECT_BEGINSETUP: PSINJECT_POINT = 16
PSINJECT_ENDSETUP: PSINJECT_POINT = 17
PSINJECT_TRAILER: PSINJECT_POINT = 18
PSINJECT_EOF: PSINJECT_POINT = 19
PSINJECT_ENDSTREAM: PSINJECT_POINT = 20
PSINJECT_DOCUMENTPROCESSCOLORSATEND: PSINJECT_POINT = 21
PSINJECT_PAGENUMBER: PSINJECT_POINT = 100
PSINJECT_BEGINPAGESETUP: PSINJECT_POINT = 101
PSINJECT_ENDPAGESETUP: PSINJECT_POINT = 102
PSINJECT_PAGETRAILER: PSINJECT_POINT = 103
PSINJECT_PLATECOLOR: PSINJECT_POINT = 104
PSINJECT_SHOWPAGE: PSINJECT_POINT = 105
PSINJECT_PAGEBBOX: PSINJECT_POINT = 106
PSINJECT_ENDPAGECOMMENTS: PSINJECT_POINT = 107
PSINJECT_VMSAVE: PSINJECT_POINT = 200
PSINJECT_VMRESTORE: PSINJECT_POINT = 201
class XPS_COLOR(Structure):
    colorType: Windows.Win32.Storage.Xps.XPS_COLOR_TYPE
    value: XPS_COLOR_VALUE
    class XPS_COLOR_VALUE(Union):
        sRGB: _sRGB_e__Struct
        scRGB: _scRGB_e__Struct
        context: _context_e__Struct
        class _sRGB_e__Struct(Structure):
            alpha: Byte
            red: Byte
            green: Byte
            blue: Byte
        class _scRGB_e__Struct(Structure):
            alpha: Single
            red: Single
            green: Single
            blue: Single
        class _context_e__Struct(Structure):
            channelCount: Byte
            channels: Single * 9
XPS_COLOR_INTERPOLATION = Int32
XPS_COLOR_INTERPOLATION_SCRGBLINEAR: XPS_COLOR_INTERPOLATION = 1
XPS_COLOR_INTERPOLATION_SRGBLINEAR: XPS_COLOR_INTERPOLATION = 2
XPS_COLOR_TYPE = Int32
XPS_COLOR_TYPE_SRGB: XPS_COLOR_TYPE = 1
XPS_COLOR_TYPE_SCRGB: XPS_COLOR_TYPE = 2
XPS_COLOR_TYPE_CONTEXT: XPS_COLOR_TYPE = 3
class XPS_DASH(Structure):
    length: Single
    gap: Single
XPS_DASH_CAP = Int32
XPS_DASH_CAP_FLAT: XPS_DASH_CAP = 1
XPS_DASH_CAP_ROUND: XPS_DASH_CAP = 2
XPS_DASH_CAP_SQUARE: XPS_DASH_CAP = 3
XPS_DASH_CAP_TRIANGLE: XPS_DASH_CAP = 4
XPS_DOCUMENT_TYPE = Int32
XPS_DOCUMENT_TYPE_UNSPECIFIED: XPS_DOCUMENT_TYPE = 1
XPS_DOCUMENT_TYPE_XPS: XPS_DOCUMENT_TYPE = 2
XPS_DOCUMENT_TYPE_OPENXPS: XPS_DOCUMENT_TYPE = 3
XPS_FILL_RULE = Int32
XPS_FILL_RULE_EVENODD: XPS_FILL_RULE = 1
XPS_FILL_RULE_NONZERO: XPS_FILL_RULE = 2
XPS_FONT_EMBEDDING = Int32
XPS_FONT_EMBEDDING_NORMAL: XPS_FONT_EMBEDDING = 1
XPS_FONT_EMBEDDING_OBFUSCATED: XPS_FONT_EMBEDDING = 2
XPS_FONT_EMBEDDING_RESTRICTED: XPS_FONT_EMBEDDING = 3
XPS_FONT_EMBEDDING_RESTRICTED_UNOBFUSCATED: XPS_FONT_EMBEDDING = 4
class XPS_GLYPH_INDEX(Structure):
    index: Int32
    advanceWidth: Single
    horizontalOffset: Single
    verticalOffset: Single
class XPS_GLYPH_MAPPING(Structure):
    unicodeStringStart: UInt32
    unicodeStringLength: UInt16
    glyphIndicesStart: UInt32
    glyphIndicesLength: UInt16
XPS_IMAGE_TYPE = Int32
XPS_IMAGE_TYPE_JPEG: XPS_IMAGE_TYPE = 1
XPS_IMAGE_TYPE_PNG: XPS_IMAGE_TYPE = 2
XPS_IMAGE_TYPE_TIFF: XPS_IMAGE_TYPE = 3
XPS_IMAGE_TYPE_WDP: XPS_IMAGE_TYPE = 4
XPS_IMAGE_TYPE_JXR: XPS_IMAGE_TYPE = 5
XPS_INTERLEAVING = Int32
XPS_INTERLEAVING_OFF: XPS_INTERLEAVING = 1
XPS_INTERLEAVING_ON: XPS_INTERLEAVING = 2
XPS_LINE_CAP = Int32
XPS_LINE_CAP_FLAT: XPS_LINE_CAP = 1
XPS_LINE_CAP_ROUND: XPS_LINE_CAP = 2
XPS_LINE_CAP_SQUARE: XPS_LINE_CAP = 3
XPS_LINE_CAP_TRIANGLE: XPS_LINE_CAP = 4
XPS_LINE_JOIN = Int32
XPS_LINE_JOIN_MITER: XPS_LINE_JOIN = 1
XPS_LINE_JOIN_BEVEL: XPS_LINE_JOIN = 2
XPS_LINE_JOIN_ROUND: XPS_LINE_JOIN = 3
class XPS_MATRIX(Structure):
    m11: Single
    m12: Single
    m21: Single
    m22: Single
    m31: Single
    m32: Single
XPS_OBJECT_TYPE = Int32
XPS_OBJECT_TYPE_CANVAS: XPS_OBJECT_TYPE = 1
XPS_OBJECT_TYPE_GLYPHS: XPS_OBJECT_TYPE = 2
XPS_OBJECT_TYPE_PATH: XPS_OBJECT_TYPE = 3
XPS_OBJECT_TYPE_MATRIX_TRANSFORM: XPS_OBJECT_TYPE = 4
XPS_OBJECT_TYPE_GEOMETRY: XPS_OBJECT_TYPE = 5
XPS_OBJECT_TYPE_SOLID_COLOR_BRUSH: XPS_OBJECT_TYPE = 6
XPS_OBJECT_TYPE_IMAGE_BRUSH: XPS_OBJECT_TYPE = 7
XPS_OBJECT_TYPE_LINEAR_GRADIENT_BRUSH: XPS_OBJECT_TYPE = 8
XPS_OBJECT_TYPE_RADIAL_GRADIENT_BRUSH: XPS_OBJECT_TYPE = 9
XPS_OBJECT_TYPE_VISUAL_BRUSH: XPS_OBJECT_TYPE = 10
class XPS_POINT(Structure):
    x: Single
    y: Single
class XPS_RECT(Structure):
    x: Single
    y: Single
    width: Single
    height: Single
XPS_SEGMENT_STROKE_PATTERN = Int32
XPS_SEGMENT_STROKE_PATTERN_ALL: XPS_SEGMENT_STROKE_PATTERN = 1
XPS_SEGMENT_STROKE_PATTERN_NONE: XPS_SEGMENT_STROKE_PATTERN = 2
XPS_SEGMENT_STROKE_PATTERN_MIXED: XPS_SEGMENT_STROKE_PATTERN = 3
XPS_SEGMENT_TYPE = Int32
XPS_SEGMENT_TYPE_ARC_LARGE_CLOCKWISE: XPS_SEGMENT_TYPE = 1
XPS_SEGMENT_TYPE_ARC_LARGE_COUNTERCLOCKWISE: XPS_SEGMENT_TYPE = 2
XPS_SEGMENT_TYPE_ARC_SMALL_CLOCKWISE: XPS_SEGMENT_TYPE = 3
XPS_SEGMENT_TYPE_ARC_SMALL_COUNTERCLOCKWISE: XPS_SEGMENT_TYPE = 4
XPS_SEGMENT_TYPE_BEZIER: XPS_SEGMENT_TYPE = 5
XPS_SEGMENT_TYPE_LINE: XPS_SEGMENT_TYPE = 6
XPS_SEGMENT_TYPE_QUADRATIC_BEZIER: XPS_SEGMENT_TYPE = 7
XPS_SIGNATURE_STATUS = Int32
XPS_SIGNATURE_STATUS_INCOMPLIANT: XPS_SIGNATURE_STATUS = 1
XPS_SIGNATURE_STATUS_INCOMPLETE: XPS_SIGNATURE_STATUS = 2
XPS_SIGNATURE_STATUS_BROKEN: XPS_SIGNATURE_STATUS = 3
XPS_SIGNATURE_STATUS_QUESTIONABLE: XPS_SIGNATURE_STATUS = 4
XPS_SIGNATURE_STATUS_VALID: XPS_SIGNATURE_STATUS = 5
XPS_SIGN_FLAGS = Int32
XPS_SIGN_FLAGS_NONE: XPS_SIGN_FLAGS = 0
XPS_SIGN_FLAGS_IGNORE_MARKUP_COMPATIBILITY: XPS_SIGN_FLAGS = 1
XPS_SIGN_POLICY = Int32
XPS_SIGN_POLICY_NONE: XPS_SIGN_POLICY = 0
XPS_SIGN_POLICY_CORE_PROPERTIES: XPS_SIGN_POLICY = 1
XPS_SIGN_POLICY_SIGNATURE_RELATIONSHIPS: XPS_SIGN_POLICY = 2
XPS_SIGN_POLICY_PRINT_TICKET: XPS_SIGN_POLICY = 4
XPS_SIGN_POLICY_DISCARD_CONTROL: XPS_SIGN_POLICY = 8
XPS_SIGN_POLICY_ALL: XPS_SIGN_POLICY = 15
class XPS_SIZE(Structure):
    width: Single
    height: Single
XPS_SPREAD_METHOD = Int32
XPS_SPREAD_METHOD_PAD: XPS_SPREAD_METHOD = 1
XPS_SPREAD_METHOD_REFLECT: XPS_SPREAD_METHOD = 2
XPS_SPREAD_METHOD_REPEAT: XPS_SPREAD_METHOD = 3
XPS_STYLE_SIMULATION = Int32
XPS_STYLE_SIMULATION_NONE: XPS_STYLE_SIMULATION = 1
XPS_STYLE_SIMULATION_ITALIC: XPS_STYLE_SIMULATION = 2
XPS_STYLE_SIMULATION_BOLD: XPS_STYLE_SIMULATION = 3
XPS_STYLE_SIMULATION_BOLDITALIC: XPS_STYLE_SIMULATION = 4
XPS_THUMBNAIL_SIZE = Int32
XPS_THUMBNAIL_SIZE_VERYSMALL: XPS_THUMBNAIL_SIZE = 1
XPS_THUMBNAIL_SIZE_SMALL: XPS_THUMBNAIL_SIZE = 2
XPS_THUMBNAIL_SIZE_MEDIUM: XPS_THUMBNAIL_SIZE = 3
XPS_THUMBNAIL_SIZE_LARGE: XPS_THUMBNAIL_SIZE = 4
XPS_TILE_MODE = Int32
XPS_TILE_MODE_NONE: XPS_TILE_MODE = 1
XPS_TILE_MODE_TILE: XPS_TILE_MODE = 2
XPS_TILE_MODE_FLIPX: XPS_TILE_MODE = 3
XPS_TILE_MODE_FLIPY: XPS_TILE_MODE = 4
XPS_TILE_MODE_FLIPXY: XPS_TILE_MODE = 5
XpsOMObjectFactory = Guid('e974d26d-3d9b-4d47-88-cc-38-72-f2-dc-35-85')
XpsOMThumbnailGenerator = Guid('7e4a23e2-b969-4761-be-35-1a-8c-ed-58-e3-23')
XpsSignatureManager = Guid('b0c43320-2315-44a2-b7-0a-09-43-a1-40-a8-ee')
make_head(_module, 'ABORTPROC')
make_head(_module, 'DOCINFOA')
make_head(_module, 'DOCINFOW')
make_head(_module, 'DRAWPATRECT')
make_head(_module, 'IXpsDocumentPackageTarget')
make_head(_module, 'IXpsDocumentPackageTarget3D')
make_head(_module, 'IXpsOMBrush')
make_head(_module, 'IXpsOMCanvas')
make_head(_module, 'IXpsOMColorProfileResource')
make_head(_module, 'IXpsOMColorProfileResourceCollection')
make_head(_module, 'IXpsOMCoreProperties')
make_head(_module, 'IXpsOMDashCollection')
make_head(_module, 'IXpsOMDictionary')
make_head(_module, 'IXpsOMDocument')
make_head(_module, 'IXpsOMDocumentCollection')
make_head(_module, 'IXpsOMDocumentSequence')
make_head(_module, 'IXpsOMDocumentStructureResource')
make_head(_module, 'IXpsOMFontResource')
make_head(_module, 'IXpsOMFontResourceCollection')
make_head(_module, 'IXpsOMGeometry')
make_head(_module, 'IXpsOMGeometryFigure')
make_head(_module, 'IXpsOMGeometryFigureCollection')
make_head(_module, 'IXpsOMGlyphs')
make_head(_module, 'IXpsOMGlyphsEditor')
make_head(_module, 'IXpsOMGradientBrush')
make_head(_module, 'IXpsOMGradientStop')
make_head(_module, 'IXpsOMGradientStopCollection')
make_head(_module, 'IXpsOMImageBrush')
make_head(_module, 'IXpsOMImageResource')
make_head(_module, 'IXpsOMImageResourceCollection')
make_head(_module, 'IXpsOMLinearGradientBrush')
make_head(_module, 'IXpsOMMatrixTransform')
make_head(_module, 'IXpsOMNameCollection')
make_head(_module, 'IXpsOMObjectFactory')
make_head(_module, 'IXpsOMObjectFactory1')
make_head(_module, 'IXpsOMPackage')
make_head(_module, 'IXpsOMPackage1')
make_head(_module, 'IXpsOMPackageTarget')
make_head(_module, 'IXpsOMPackageWriter')
make_head(_module, 'IXpsOMPackageWriter3D')
make_head(_module, 'IXpsOMPage')
make_head(_module, 'IXpsOMPage1')
make_head(_module, 'IXpsOMPageReference')
make_head(_module, 'IXpsOMPageReferenceCollection')
make_head(_module, 'IXpsOMPart')
make_head(_module, 'IXpsOMPartResources')
make_head(_module, 'IXpsOMPartUriCollection')
make_head(_module, 'IXpsOMPath')
make_head(_module, 'IXpsOMPrintTicketResource')
make_head(_module, 'IXpsOMRadialGradientBrush')
make_head(_module, 'IXpsOMRemoteDictionaryResource')
make_head(_module, 'IXpsOMRemoteDictionaryResource1')
make_head(_module, 'IXpsOMRemoteDictionaryResourceCollection')
make_head(_module, 'IXpsOMResource')
make_head(_module, 'IXpsOMShareable')
make_head(_module, 'IXpsOMSignatureBlockResource')
make_head(_module, 'IXpsOMSignatureBlockResourceCollection')
make_head(_module, 'IXpsOMSolidColorBrush')
make_head(_module, 'IXpsOMStoryFragmentsResource')
make_head(_module, 'IXpsOMThumbnailGenerator')
make_head(_module, 'IXpsOMTileBrush')
make_head(_module, 'IXpsOMVisual')
make_head(_module, 'IXpsOMVisualBrush')
make_head(_module, 'IXpsOMVisualCollection')
make_head(_module, 'IXpsSignature')
make_head(_module, 'IXpsSignatureBlock')
make_head(_module, 'IXpsSignatureBlockCollection')
make_head(_module, 'IXpsSignatureCollection')
make_head(_module, 'IXpsSignatureManager')
make_head(_module, 'IXpsSignatureRequest')
make_head(_module, 'IXpsSignatureRequestCollection')
make_head(_module, 'IXpsSigningOptions')
make_head(_module, 'PSFEATURE_CUSTPAPER')
make_head(_module, 'PSFEATURE_OUTPUT')
make_head(_module, 'PSINJECTDATA')
make_head(_module, 'XPS_COLOR')
make_head(_module, 'XPS_DASH')
make_head(_module, 'XPS_GLYPH_INDEX')
make_head(_module, 'XPS_GLYPH_MAPPING')
make_head(_module, 'XPS_MATRIX')
make_head(_module, 'XPS_POINT')
make_head(_module, 'XPS_RECT')
make_head(_module, 'XPS_SIZE')
__all__ = [
    "ABORTPROC",
    "AbortDoc",
    "DC_BINNAMES",
    "DC_BINS",
    "DC_COLLATE",
    "DC_COLORDEVICE",
    "DC_COPIES",
    "DC_DRIVER",
    "DC_DUPLEX",
    "DC_ENUMRESOLUTIONS",
    "DC_EXTRA",
    "DC_FIELDS",
    "DC_FILEDEPENDENCIES",
    "DC_MAXEXTENT",
    "DC_MEDIAREADY",
    "DC_MEDIATYPENAMES",
    "DC_MEDIATYPES",
    "DC_MINEXTENT",
    "DC_NUP",
    "DC_ORIENTATION",
    "DC_PAPERNAMES",
    "DC_PAPERS",
    "DC_PAPERSIZE",
    "DC_PERSONALITY",
    "DC_PRINTERMEM",
    "DC_PRINTRATE",
    "DC_PRINTRATEPPM",
    "DC_PRINTRATEUNIT",
    "DC_SIZE",
    "DC_STAPLE",
    "DC_TRUETYPE",
    "DC_VERSION",
    "DEVICE_CAPABILITIES",
    "DOCINFOA",
    "DOCINFOW",
    "DRAWPATRECT",
    "DeviceCapabilitiesA",
    "DeviceCapabilitiesW",
    "EndDoc",
    "EndPage",
    "Escape",
    "ExtEscape",
    "HPTPROVIDER",
    "IXpsDocumentPackageTarget",
    "IXpsDocumentPackageTarget3D",
    "IXpsOMBrush",
    "IXpsOMCanvas",
    "IXpsOMColorProfileResource",
    "IXpsOMColorProfileResourceCollection",
    "IXpsOMCoreProperties",
    "IXpsOMDashCollection",
    "IXpsOMDictionary",
    "IXpsOMDocument",
    "IXpsOMDocumentCollection",
    "IXpsOMDocumentSequence",
    "IXpsOMDocumentStructureResource",
    "IXpsOMFontResource",
    "IXpsOMFontResourceCollection",
    "IXpsOMGeometry",
    "IXpsOMGeometryFigure",
    "IXpsOMGeometryFigureCollection",
    "IXpsOMGlyphs",
    "IXpsOMGlyphsEditor",
    "IXpsOMGradientBrush",
    "IXpsOMGradientStop",
    "IXpsOMGradientStopCollection",
    "IXpsOMImageBrush",
    "IXpsOMImageResource",
    "IXpsOMImageResourceCollection",
    "IXpsOMLinearGradientBrush",
    "IXpsOMMatrixTransform",
    "IXpsOMNameCollection",
    "IXpsOMObjectFactory",
    "IXpsOMObjectFactory1",
    "IXpsOMPackage",
    "IXpsOMPackage1",
    "IXpsOMPackageTarget",
    "IXpsOMPackageWriter",
    "IXpsOMPackageWriter3D",
    "IXpsOMPage",
    "IXpsOMPage1",
    "IXpsOMPageReference",
    "IXpsOMPageReferenceCollection",
    "IXpsOMPart",
    "IXpsOMPartResources",
    "IXpsOMPartUriCollection",
    "IXpsOMPath",
    "IXpsOMPrintTicketResource",
    "IXpsOMRadialGradientBrush",
    "IXpsOMRemoteDictionaryResource",
    "IXpsOMRemoteDictionaryResource1",
    "IXpsOMRemoteDictionaryResourceCollection",
    "IXpsOMResource",
    "IXpsOMShareable",
    "IXpsOMSignatureBlockResource",
    "IXpsOMSignatureBlockResourceCollection",
    "IXpsOMSolidColorBrush",
    "IXpsOMStoryFragmentsResource",
    "IXpsOMThumbnailGenerator",
    "IXpsOMTileBrush",
    "IXpsOMVisual",
    "IXpsOMVisualBrush",
    "IXpsOMVisualCollection",
    "IXpsSignature",
    "IXpsSignatureBlock",
    "IXpsSignatureBlockCollection",
    "IXpsSignatureCollection",
    "IXpsSignatureManager",
    "IXpsSignatureRequest",
    "IXpsSignatureRequestCollection",
    "IXpsSigningOptions",
    "PRINT_WINDOW_FLAGS",
    "PSFEATURE_CUSTPAPER",
    "PSFEATURE_OUTPUT",
    "PSINJECTDATA",
    "PSINJECT_BEGINDEFAULTS",
    "PSINJECT_BEGINPAGESETUP",
    "PSINJECT_BEGINPROLOG",
    "PSINJECT_BEGINSETUP",
    "PSINJECT_BEGINSTREAM",
    "PSINJECT_BOUNDINGBOX",
    "PSINJECT_COMMENTS",
    "PSINJECT_DOCNEEDEDRES",
    "PSINJECT_DOCSUPPLIEDRES",
    "PSINJECT_DOCUMENTPROCESSCOLORS",
    "PSINJECT_DOCUMENTPROCESSCOLORSATEND",
    "PSINJECT_ENDDEFAULTS",
    "PSINJECT_ENDPAGECOMMENTS",
    "PSINJECT_ENDPAGESETUP",
    "PSINJECT_ENDPROLOG",
    "PSINJECT_ENDSETUP",
    "PSINJECT_ENDSTREAM",
    "PSINJECT_EOF",
    "PSINJECT_ORIENTATION",
    "PSINJECT_PAGEBBOX",
    "PSINJECT_PAGENUMBER",
    "PSINJECT_PAGEORDER",
    "PSINJECT_PAGES",
    "PSINJECT_PAGESATEND",
    "PSINJECT_PAGETRAILER",
    "PSINJECT_PLATECOLOR",
    "PSINJECT_POINT",
    "PSINJECT_PSADOBE",
    "PSINJECT_SHOWPAGE",
    "PSINJECT_TRAILER",
    "PSINJECT_VMRESTORE",
    "PSINJECT_VMSAVE",
    "PW_CLIENTONLY",
    "PrintWindow",
    "SetAbortProc",
    "StartDocA",
    "StartDocW",
    "StartPage",
    "XPS_COLOR",
    "XPS_COLOR_INTERPOLATION",
    "XPS_COLOR_INTERPOLATION_SCRGBLINEAR",
    "XPS_COLOR_INTERPOLATION_SRGBLINEAR",
    "XPS_COLOR_TYPE",
    "XPS_COLOR_TYPE_CONTEXT",
    "XPS_COLOR_TYPE_SCRGB",
    "XPS_COLOR_TYPE_SRGB",
    "XPS_DASH",
    "XPS_DASH_CAP",
    "XPS_DASH_CAP_FLAT",
    "XPS_DASH_CAP_ROUND",
    "XPS_DASH_CAP_SQUARE",
    "XPS_DASH_CAP_TRIANGLE",
    "XPS_DOCUMENT_TYPE",
    "XPS_DOCUMENT_TYPE_OPENXPS",
    "XPS_DOCUMENT_TYPE_UNSPECIFIED",
    "XPS_DOCUMENT_TYPE_XPS",
    "XPS_E_ABSOLUTE_REFERENCE",
    "XPS_E_ALREADY_OWNED",
    "XPS_E_BLEED_BOX_PAGE_DIMENSIONS_NOT_IN_SYNC",
    "XPS_E_BOTH_PATHFIGURE_AND_ABBR_SYNTAX_PRESENT",
    "XPS_E_BOTH_RESOURCE_AND_SOURCEATTR_PRESENT",
    "XPS_E_CARET_OUTSIDE_STRING",
    "XPS_E_CARET_OUT_OF_ORDER",
    "XPS_E_COLOR_COMPONENT_OUT_OF_RANGE",
    "XPS_E_DICTIONARY_ITEM_NAMED",
    "XPS_E_DUPLICATE_NAMES",
    "XPS_E_DUPLICATE_RESOURCE_KEYS",
    "XPS_E_INDEX_OUT_OF_RANGE",
    "XPS_E_INVALID_BLEED_BOX",
    "XPS_E_INVALID_CONTENT_BOX",
    "XPS_E_INVALID_CONTENT_TYPE",
    "XPS_E_INVALID_FLOAT",
    "XPS_E_INVALID_FONT_URI",
    "XPS_E_INVALID_LANGUAGE",
    "XPS_E_INVALID_LOOKUP_TYPE",
    "XPS_E_INVALID_MARKUP",
    "XPS_E_INVALID_NAME",
    "XPS_E_INVALID_NUMBER_OF_COLOR_CHANNELS",
    "XPS_E_INVALID_NUMBER_OF_POINTS_IN_CURVE_SEGMENTS",
    "XPS_E_INVALID_OBFUSCATED_FONT_URI",
    "XPS_E_INVALID_PAGE_SIZE",
    "XPS_E_INVALID_RESOURCE_KEY",
    "XPS_E_INVALID_SIGNATUREBLOCK_MARKUP",
    "XPS_E_INVALID_THUMBNAIL_IMAGE_TYPE",
    "XPS_E_INVALID_XML_ENCODING",
    "XPS_E_MAPPING_OUTSIDE_INDICES",
    "XPS_E_MAPPING_OUTSIDE_STRING",
    "XPS_E_MAPPING_OUT_OF_ORDER",
    "XPS_E_MARKUP_COMPATIBILITY_ELEMENTS",
    "XPS_E_MISSING_COLORPROFILE",
    "XPS_E_MISSING_DISCARDCONTROL",
    "XPS_E_MISSING_DOCUMENT",
    "XPS_E_MISSING_DOCUMENTSEQUENCE_RELATIONSHIP",
    "XPS_E_MISSING_FONTURI",
    "XPS_E_MISSING_GLYPHS",
    "XPS_E_MISSING_IMAGE_IN_IMAGEBRUSH",
    "XPS_E_MISSING_LOOKUP",
    "XPS_E_MISSING_NAME",
    "XPS_E_MISSING_PAGE_IN_DOCUMENT",
    "XPS_E_MISSING_PAGE_IN_PAGEREFERENCE",
    "XPS_E_MISSING_PART_REFERENCE",
    "XPS_E_MISSING_PART_STREAM",
    "XPS_E_MISSING_REFERRED_DOCUMENT",
    "XPS_E_MISSING_REFERRED_PAGE",
    "XPS_E_MISSING_RELATIONSHIP_TARGET",
    "XPS_E_MISSING_RESOURCE_KEY",
    "XPS_E_MISSING_RESOURCE_RELATIONSHIP",
    "XPS_E_MISSING_RESTRICTED_FONT_RELATIONSHIP",
    "XPS_E_MISSING_SEGMENT_DATA",
    "XPS_E_MULTIPLE_DOCUMENTSEQUENCE_RELATIONSHIPS",
    "XPS_E_MULTIPLE_PRINTTICKETS_ON_DOCUMENT",
    "XPS_E_MULTIPLE_PRINTTICKETS_ON_DOCUMENTSEQUENCE",
    "XPS_E_MULTIPLE_PRINTTICKETS_ON_PAGE",
    "XPS_E_MULTIPLE_REFERENCES_TO_PART",
    "XPS_E_MULTIPLE_RESOURCES",
    "XPS_E_MULTIPLE_THUMBNAILS_ON_PACKAGE",
    "XPS_E_MULTIPLE_THUMBNAILS_ON_PAGE",
    "XPS_E_NEGATIVE_FLOAT",
    "XPS_E_NESTED_REMOTE_DICTIONARY",
    "XPS_E_NOT_ENOUGH_GRADIENT_STOPS",
    "XPS_E_NO_CUSTOM_OBJECTS",
    "XPS_E_OBJECT_DETACHED",
    "XPS_E_ODD_BIDILEVEL",
    "XPS_E_ONE_TO_ONE_MAPPING_EXPECTED",
    "XPS_E_PACKAGE_ALREADY_OPENED",
    "XPS_E_PACKAGE_NOT_OPENED",
    "XPS_E_PACKAGE_WRITER_NOT_CLOSED",
    "XPS_E_RELATIONSHIP_EXTERNAL",
    "XPS_E_RESOURCE_NOT_OWNED",
    "XPS_E_RESTRICTED_FONT_NOT_OBFUSCATED",
    "XPS_E_SIGNATUREID_DUP",
    "XPS_E_SIGREQUESTID_DUP",
    "XPS_E_STRING_TOO_LONG",
    "XPS_E_TOO_MANY_INDICES",
    "XPS_E_UNAVAILABLE_PACKAGE",
    "XPS_E_UNEXPECTED_COLORPROFILE",
    "XPS_E_UNEXPECTED_CONTENT_TYPE",
    "XPS_E_UNEXPECTED_RELATIONSHIP_TYPE",
    "XPS_E_UNEXPECTED_RESTRICTED_FONT_RELATIONSHIP",
    "XPS_E_VISUAL_CIRCULAR_REF",
    "XPS_E_XKEY_ATTR_PRESENT_OUTSIDE_RES_DICT",
    "XPS_FILL_RULE",
    "XPS_FILL_RULE_EVENODD",
    "XPS_FILL_RULE_NONZERO",
    "XPS_FONT_EMBEDDING",
    "XPS_FONT_EMBEDDING_NORMAL",
    "XPS_FONT_EMBEDDING_OBFUSCATED",
    "XPS_FONT_EMBEDDING_RESTRICTED",
    "XPS_FONT_EMBEDDING_RESTRICTED_UNOBFUSCATED",
    "XPS_GLYPH_INDEX",
    "XPS_GLYPH_MAPPING",
    "XPS_IMAGE_TYPE",
    "XPS_IMAGE_TYPE_JPEG",
    "XPS_IMAGE_TYPE_JXR",
    "XPS_IMAGE_TYPE_PNG",
    "XPS_IMAGE_TYPE_TIFF",
    "XPS_IMAGE_TYPE_WDP",
    "XPS_INTERLEAVING",
    "XPS_INTERLEAVING_OFF",
    "XPS_INTERLEAVING_ON",
    "XPS_LINE_CAP",
    "XPS_LINE_CAP_FLAT",
    "XPS_LINE_CAP_ROUND",
    "XPS_LINE_CAP_SQUARE",
    "XPS_LINE_CAP_TRIANGLE",
    "XPS_LINE_JOIN",
    "XPS_LINE_JOIN_BEVEL",
    "XPS_LINE_JOIN_MITER",
    "XPS_LINE_JOIN_ROUND",
    "XPS_MATRIX",
    "XPS_OBJECT_TYPE",
    "XPS_OBJECT_TYPE_CANVAS",
    "XPS_OBJECT_TYPE_GEOMETRY",
    "XPS_OBJECT_TYPE_GLYPHS",
    "XPS_OBJECT_TYPE_IMAGE_BRUSH",
    "XPS_OBJECT_TYPE_LINEAR_GRADIENT_BRUSH",
    "XPS_OBJECT_TYPE_MATRIX_TRANSFORM",
    "XPS_OBJECT_TYPE_PATH",
    "XPS_OBJECT_TYPE_RADIAL_GRADIENT_BRUSH",
    "XPS_OBJECT_TYPE_SOLID_COLOR_BRUSH",
    "XPS_OBJECT_TYPE_VISUAL_BRUSH",
    "XPS_POINT",
    "XPS_RECT",
    "XPS_SEGMENT_STROKE_PATTERN",
    "XPS_SEGMENT_STROKE_PATTERN_ALL",
    "XPS_SEGMENT_STROKE_PATTERN_MIXED",
    "XPS_SEGMENT_STROKE_PATTERN_NONE",
    "XPS_SEGMENT_TYPE",
    "XPS_SEGMENT_TYPE_ARC_LARGE_CLOCKWISE",
    "XPS_SEGMENT_TYPE_ARC_LARGE_COUNTERCLOCKWISE",
    "XPS_SEGMENT_TYPE_ARC_SMALL_CLOCKWISE",
    "XPS_SEGMENT_TYPE_ARC_SMALL_COUNTERCLOCKWISE",
    "XPS_SEGMENT_TYPE_BEZIER",
    "XPS_SEGMENT_TYPE_LINE",
    "XPS_SEGMENT_TYPE_QUADRATIC_BEZIER",
    "XPS_SIGNATURE_STATUS",
    "XPS_SIGNATURE_STATUS_BROKEN",
    "XPS_SIGNATURE_STATUS_INCOMPLETE",
    "XPS_SIGNATURE_STATUS_INCOMPLIANT",
    "XPS_SIGNATURE_STATUS_QUESTIONABLE",
    "XPS_SIGNATURE_STATUS_VALID",
    "XPS_SIGN_FLAGS",
    "XPS_SIGN_FLAGS_IGNORE_MARKUP_COMPATIBILITY",
    "XPS_SIGN_FLAGS_NONE",
    "XPS_SIGN_POLICY",
    "XPS_SIGN_POLICY_ALL",
    "XPS_SIGN_POLICY_CORE_PROPERTIES",
    "XPS_SIGN_POLICY_DISCARD_CONTROL",
    "XPS_SIGN_POLICY_NONE",
    "XPS_SIGN_POLICY_PRINT_TICKET",
    "XPS_SIGN_POLICY_SIGNATURE_RELATIONSHIPS",
    "XPS_SIZE",
    "XPS_SPREAD_METHOD",
    "XPS_SPREAD_METHOD_PAD",
    "XPS_SPREAD_METHOD_REFLECT",
    "XPS_SPREAD_METHOD_REPEAT",
    "XPS_STYLE_SIMULATION",
    "XPS_STYLE_SIMULATION_BOLD",
    "XPS_STYLE_SIMULATION_BOLDITALIC",
    "XPS_STYLE_SIMULATION_ITALIC",
    "XPS_STYLE_SIMULATION_NONE",
    "XPS_THUMBNAIL_SIZE",
    "XPS_THUMBNAIL_SIZE_LARGE",
    "XPS_THUMBNAIL_SIZE_MEDIUM",
    "XPS_THUMBNAIL_SIZE_SMALL",
    "XPS_THUMBNAIL_SIZE_VERYSMALL",
    "XPS_TILE_MODE",
    "XPS_TILE_MODE_FLIPX",
    "XPS_TILE_MODE_FLIPXY",
    "XPS_TILE_MODE_FLIPY",
    "XPS_TILE_MODE_NONE",
    "XPS_TILE_MODE_TILE",
    "XpsOMObjectFactory",
    "XpsOMThumbnailGenerator",
    "XpsSignatureManager",
]
_arch_optional = [
]
