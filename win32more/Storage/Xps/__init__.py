from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Graphics.Gdi
import win32more.Security
import win32more.Security.Cryptography
import win32more.Storage.Packaging.Opc
import win32more.Storage.Xps
import win32more.System.Com
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
def ABORTPROC(param0: win32more.Graphics.Gdi.HDC, param1: Int32) -> win32more.Foundation.BOOL: ...
XPS_E_SIGREQUESTID_DUP: win32more.Foundation.HRESULT = -2142108795
XPS_E_PACKAGE_NOT_OPENED: win32more.Foundation.HRESULT = -2142108794
XPS_E_PACKAGE_ALREADY_OPENED: win32more.Foundation.HRESULT = -2142108793
XPS_E_SIGNATUREID_DUP: win32more.Foundation.HRESULT = -2142108792
XPS_E_MARKUP_COMPATIBILITY_ELEMENTS: win32more.Foundation.HRESULT = -2142108791
XPS_E_OBJECT_DETACHED: win32more.Foundation.HRESULT = -2142108790
XPS_E_INVALID_SIGNATUREBLOCK_MARKUP: win32more.Foundation.HRESULT = -2142108789
XPS_E_INVALID_NUMBER_OF_POINTS_IN_CURVE_SEGMENTS: win32more.Foundation.HRESULT = -2142108160
XPS_E_ABSOLUTE_REFERENCE: win32more.Foundation.HRESULT = -2142108159
XPS_E_INVALID_NUMBER_OF_COLOR_CHANNELS: win32more.Foundation.HRESULT = -2142108158
XPS_E_INVALID_LANGUAGE: win32more.Foundation.HRESULT = -2142109696
XPS_E_INVALID_NAME: win32more.Foundation.HRESULT = -2142109695
XPS_E_INVALID_RESOURCE_KEY: win32more.Foundation.HRESULT = -2142109694
XPS_E_INVALID_PAGE_SIZE: win32more.Foundation.HRESULT = -2142109693
XPS_E_INVALID_BLEED_BOX: win32more.Foundation.HRESULT = -2142109692
XPS_E_INVALID_THUMBNAIL_IMAGE_TYPE: win32more.Foundation.HRESULT = -2142109691
XPS_E_INVALID_LOOKUP_TYPE: win32more.Foundation.HRESULT = -2142109690
XPS_E_INVALID_FLOAT: win32more.Foundation.HRESULT = -2142109689
XPS_E_UNEXPECTED_CONTENT_TYPE: win32more.Foundation.HRESULT = -2142109688
XPS_E_INVALID_FONT_URI: win32more.Foundation.HRESULT = -2142109686
XPS_E_INVALID_CONTENT_BOX: win32more.Foundation.HRESULT = -2142109685
XPS_E_INVALID_MARKUP: win32more.Foundation.HRESULT = -2142109684
XPS_E_INVALID_XML_ENCODING: win32more.Foundation.HRESULT = -2142109683
XPS_E_INVALID_CONTENT_TYPE: win32more.Foundation.HRESULT = -2142109682
XPS_E_INVALID_OBFUSCATED_FONT_URI: win32more.Foundation.HRESULT = -2142109681
XPS_E_UNEXPECTED_RELATIONSHIP_TYPE: win32more.Foundation.HRESULT = -2142109680
XPS_E_UNEXPECTED_RESTRICTED_FONT_RELATIONSHIP: win32more.Foundation.HRESULT = -2142109679
XPS_E_MISSING_NAME: win32more.Foundation.HRESULT = -2142109440
XPS_E_MISSING_LOOKUP: win32more.Foundation.HRESULT = -2142109439
XPS_E_MISSING_GLYPHS: win32more.Foundation.HRESULT = -2142109438
XPS_E_MISSING_SEGMENT_DATA: win32more.Foundation.HRESULT = -2142109437
XPS_E_MISSING_COLORPROFILE: win32more.Foundation.HRESULT = -2142109436
XPS_E_MISSING_RELATIONSHIP_TARGET: win32more.Foundation.HRESULT = -2142109435
XPS_E_MISSING_RESOURCE_RELATIONSHIP: win32more.Foundation.HRESULT = -2142109434
XPS_E_MISSING_FONTURI: win32more.Foundation.HRESULT = -2142109433
XPS_E_MISSING_DOCUMENTSEQUENCE_RELATIONSHIP: win32more.Foundation.HRESULT = -2142109432
XPS_E_MISSING_DOCUMENT: win32more.Foundation.HRESULT = -2142109431
XPS_E_MISSING_REFERRED_DOCUMENT: win32more.Foundation.HRESULT = -2142109430
XPS_E_MISSING_REFERRED_PAGE: win32more.Foundation.HRESULT = -2142109429
XPS_E_MISSING_PAGE_IN_DOCUMENT: win32more.Foundation.HRESULT = -2142109428
XPS_E_MISSING_PAGE_IN_PAGEREFERENCE: win32more.Foundation.HRESULT = -2142109427
XPS_E_MISSING_IMAGE_IN_IMAGEBRUSH: win32more.Foundation.HRESULT = -2142109426
XPS_E_MISSING_RESOURCE_KEY: win32more.Foundation.HRESULT = -2142109425
XPS_E_MISSING_PART_REFERENCE: win32more.Foundation.HRESULT = -2142109424
XPS_E_MISSING_RESTRICTED_FONT_RELATIONSHIP: win32more.Foundation.HRESULT = -2142109423
XPS_E_MISSING_DISCARDCONTROL: win32more.Foundation.HRESULT = -2142109422
XPS_E_MISSING_PART_STREAM: win32more.Foundation.HRESULT = -2142109421
XPS_E_UNAVAILABLE_PACKAGE: win32more.Foundation.HRESULT = -2142109420
XPS_E_DUPLICATE_RESOURCE_KEYS: win32more.Foundation.HRESULT = -2142109184
XPS_E_MULTIPLE_RESOURCES: win32more.Foundation.HRESULT = -2142109183
XPS_E_MULTIPLE_DOCUMENTSEQUENCE_RELATIONSHIPS: win32more.Foundation.HRESULT = -2142109182
XPS_E_MULTIPLE_THUMBNAILS_ON_PAGE: win32more.Foundation.HRESULT = -2142109181
XPS_E_MULTIPLE_THUMBNAILS_ON_PACKAGE: win32more.Foundation.HRESULT = -2142109180
XPS_E_MULTIPLE_PRINTTICKETS_ON_PAGE: win32more.Foundation.HRESULT = -2142109179
XPS_E_MULTIPLE_PRINTTICKETS_ON_DOCUMENT: win32more.Foundation.HRESULT = -2142109178
XPS_E_MULTIPLE_PRINTTICKETS_ON_DOCUMENTSEQUENCE: win32more.Foundation.HRESULT = -2142109177
XPS_E_MULTIPLE_REFERENCES_TO_PART: win32more.Foundation.HRESULT = -2142109176
XPS_E_DUPLICATE_NAMES: win32more.Foundation.HRESULT = -2142109175
XPS_E_STRING_TOO_LONG: win32more.Foundation.HRESULT = -2142108928
XPS_E_TOO_MANY_INDICES: win32more.Foundation.HRESULT = -2142108927
XPS_E_MAPPING_OUT_OF_ORDER: win32more.Foundation.HRESULT = -2142108926
XPS_E_MAPPING_OUTSIDE_STRING: win32more.Foundation.HRESULT = -2142108925
XPS_E_MAPPING_OUTSIDE_INDICES: win32more.Foundation.HRESULT = -2142108924
XPS_E_CARET_OUTSIDE_STRING: win32more.Foundation.HRESULT = -2142108923
XPS_E_CARET_OUT_OF_ORDER: win32more.Foundation.HRESULT = -2142108922
XPS_E_ODD_BIDILEVEL: win32more.Foundation.HRESULT = -2142108921
XPS_E_ONE_TO_ONE_MAPPING_EXPECTED: win32more.Foundation.HRESULT = -2142108920
XPS_E_RESTRICTED_FONT_NOT_OBFUSCATED: win32more.Foundation.HRESULT = -2142108919
XPS_E_NEGATIVE_FLOAT: win32more.Foundation.HRESULT = -2142108918
XPS_E_XKEY_ATTR_PRESENT_OUTSIDE_RES_DICT: win32more.Foundation.HRESULT = -2142108672
XPS_E_DICTIONARY_ITEM_NAMED: win32more.Foundation.HRESULT = -2142108671
XPS_E_NESTED_REMOTE_DICTIONARY: win32more.Foundation.HRESULT = -2142108670
XPS_E_INDEX_OUT_OF_RANGE: win32more.Foundation.HRESULT = -2142108416
XPS_E_VISUAL_CIRCULAR_REF: win32more.Foundation.HRESULT = -2142108415
XPS_E_NO_CUSTOM_OBJECTS: win32more.Foundation.HRESULT = -2142108414
XPS_E_ALREADY_OWNED: win32more.Foundation.HRESULT = -2142108413
XPS_E_RESOURCE_NOT_OWNED: win32more.Foundation.HRESULT = -2142108412
XPS_E_UNEXPECTED_COLORPROFILE: win32more.Foundation.HRESULT = -2142108411
XPS_E_COLOR_COMPONENT_OUT_OF_RANGE: win32more.Foundation.HRESULT = -2142108410
XPS_E_BOTH_PATHFIGURE_AND_ABBR_SYNTAX_PRESENT: win32more.Foundation.HRESULT = -2142108409
XPS_E_BOTH_RESOURCE_AND_SOURCEATTR_PRESENT: win32more.Foundation.HRESULT = -2142108408
XPS_E_BLEED_BOX_PAGE_DIMENSIONS_NOT_IN_SYNC: win32more.Foundation.HRESULT = -2142108407
XPS_E_RELATIONSHIP_EXTERNAL: win32more.Foundation.HRESULT = -2142108406
XPS_E_NOT_ENOUGH_GRADIENT_STOPS: win32more.Foundation.HRESULT = -2142108405
XPS_E_PACKAGE_WRITER_NOT_CLOSED: win32more.Foundation.HRESULT = -2142108404
@winfunctype('winspool.drv')
def DeviceCapabilitiesA(pDevice: win32more.Foundation.PSTR, pPort: win32more.Foundation.PSTR, fwCapability: win32more.Storage.Xps.DEVICE_CAPABILITIES, pOutput: win32more.Foundation.PSTR, pDevMode: POINTER(win32more.Graphics.Gdi.DEVMODEA_head)) -> Int32: ...
@winfunctype('winspool.drv')
def DeviceCapabilitiesW(pDevice: win32more.Foundation.PWSTR, pPort: win32more.Foundation.PWSTR, fwCapability: win32more.Storage.Xps.DEVICE_CAPABILITIES, pOutput: win32more.Foundation.PWSTR, pDevMode: POINTER(win32more.Graphics.Gdi.DEVMODEW_head)) -> Int32: ...
@winfunctype('GDI32.dll')
def Escape(hdc: win32more.Graphics.Gdi.HDC, iEscape: Int32, cjIn: Int32, pvIn: win32more.Foundation.PSTR, pvOut: c_void_p) -> Int32: ...
@winfunctype('GDI32.dll')
def ExtEscape(hdc: win32more.Graphics.Gdi.HDC, iEscape: Int32, cjInput: Int32, lpInData: win32more.Foundation.PSTR, cjOutput: Int32, lpOutData: win32more.Foundation.PSTR) -> Int32: ...
@winfunctype('GDI32.dll')
def StartDocA(hdc: win32more.Graphics.Gdi.HDC, lpdi: POINTER(win32more.Storage.Xps.DOCINFOA_head)) -> Int32: ...
@winfunctype('GDI32.dll')
def StartDocW(hdc: win32more.Graphics.Gdi.HDC, lpdi: POINTER(win32more.Storage.Xps.DOCINFOW_head)) -> Int32: ...
@winfunctype('GDI32.dll')
def EndDoc(hdc: win32more.Graphics.Gdi.HDC) -> Int32: ...
@winfunctype('GDI32.dll')
def StartPage(hdc: win32more.Graphics.Gdi.HDC) -> Int32: ...
@winfunctype('GDI32.dll')
def EndPage(hdc: win32more.Graphics.Gdi.HDC) -> Int32: ...
@winfunctype('GDI32.dll')
def AbortDoc(hdc: win32more.Graphics.Gdi.HDC) -> Int32: ...
@winfunctype('GDI32.dll')
def SetAbortProc(hdc: win32more.Graphics.Gdi.HDC, proc: win32more.Storage.Xps.ABORTPROC) -> Int32: ...
@winfunctype('USER32.dll')
def PrintWindow(hwnd: win32more.Foundation.HWND, hdcBlt: win32more.Graphics.Gdi.HDC, nFlags: win32more.Storage.Xps.PRINT_WINDOW_FLAGS) -> win32more.Foundation.BOOL: ...
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
    lpszDocName: win32more.Foundation.PSTR
    lpszOutput: win32more.Foundation.PSTR
    lpszDatatype: win32more.Foundation.PSTR
    fwType: UInt32
class DOCINFOW(Structure):
    cbSize: Int32
    lpszDocName: win32more.Foundation.PWSTR
    lpszOutput: win32more.Foundation.PWSTR
    lpszDatatype: win32more.Foundation.PWSTR
    fwType: UInt32
class DRAWPATRECT(Structure):
    ptPosition: win32more.Foundation.POINT
    ptSize: win32more.Foundation.POINT
    wStyle: UInt16
    wPattern: UInt16
HPTPROVIDER = IntPtr
class IXpsDocumentPackageTarget(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('3b0b6d38-53ad-41da-b2-12-d3-76-37-a6-71-4e')
    @commethod(3)
    def GetXpsOMPackageWriter(documentSequencePartName: win32more.Storage.Packaging.Opc.IOpcPartUri_head, discardControlPartName: win32more.Storage.Packaging.Opc.IOpcPartUri_head, packageWriter: POINTER(win32more.Storage.Xps.IXpsOMPackageWriter_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetXpsOMFactory(xpsFactory: POINTER(win32more.Storage.Xps.IXpsOMObjectFactory_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetXpsType(documentType: POINTER(win32more.Storage.Xps.XPS_DOCUMENT_TYPE)) -> win32more.Foundation.HRESULT: ...
class IXpsDocumentPackageTarget3D(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('60ba71b8-3101-4984-91-99-f4-ea-77-5f-f0-1d')
    @commethod(3)
    def GetXpsOMPackageWriter3D(documentSequencePartName: win32more.Storage.Packaging.Opc.IOpcPartUri_head, discardControlPartName: win32more.Storage.Packaging.Opc.IOpcPartUri_head, modelPartName: win32more.Storage.Packaging.Opc.IOpcPartUri_head, modelData: win32more.System.Com.IStream_head, packageWriter: POINTER(win32more.Storage.Xps.IXpsOMPackageWriter3D_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetXpsOMFactory(xpsFactory: POINTER(win32more.Storage.Xps.IXpsOMObjectFactory_head)) -> win32more.Foundation.HRESULT: ...
class IXpsOMBrush(c_void_p):
    extends: win32more.Storage.Xps.IXpsOMShareable
    Guid = Guid('56a3f80c-ea4c-4187-a5-7b-a2-a4-73-b2-b4-2b')
    @commethod(5)
    def GetOpacity(opacity: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetOpacity(opacity: Single) -> win32more.Foundation.HRESULT: ...
class IXpsOMCanvas(c_void_p):
    extends: win32more.Storage.Xps.IXpsOMVisual
    Guid = Guid('221d1452-331e-47c6-87-e9-6c-ce-fb-9b-5b-a3')
    @commethod(30)
    def GetVisuals(visuals: POINTER(win32more.Storage.Xps.IXpsOMVisualCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def GetUseAliasedEdgeMode(useAliasedEdgeMode: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def SetUseAliasedEdgeMode(useAliasedEdgeMode: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def GetAccessibilityShortDescription(shortDescription: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def SetAccessibilityShortDescription(shortDescription: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def GetAccessibilityLongDescription(longDescription: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def SetAccessibilityLongDescription(longDescription: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def GetDictionary(resourceDictionary: POINTER(win32more.Storage.Xps.IXpsOMDictionary_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def GetDictionaryLocal(resourceDictionary: POINTER(win32more.Storage.Xps.IXpsOMDictionary_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def SetDictionaryLocal(resourceDictionary: win32more.Storage.Xps.IXpsOMDictionary_head) -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def GetDictionaryResource(remoteDictionaryResource: POINTER(win32more.Storage.Xps.IXpsOMRemoteDictionaryResource_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(41)
    def SetDictionaryResource(remoteDictionaryResource: win32more.Storage.Xps.IXpsOMRemoteDictionaryResource_head) -> win32more.Foundation.HRESULT: ...
    @commethod(42)
    def Clone(canvas: POINTER(win32more.Storage.Xps.IXpsOMCanvas_head)) -> win32more.Foundation.HRESULT: ...
class IXpsOMColorProfileResource(c_void_p):
    extends: win32more.Storage.Xps.IXpsOMResource
    Guid = Guid('67bd7d69-1eef-4bb1-b5-e7-6f-4f-87-be-8a-be')
    @commethod(5)
    def GetStream(stream: POINTER(win32more.System.Com.IStream_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetContent(sourceStream: win32more.System.Com.IStream_head, partName: win32more.Storage.Packaging.Opc.IOpcPartUri_head) -> win32more.Foundation.HRESULT: ...
class IXpsOMColorProfileResourceCollection(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('12759630-5fba-4283-8f-7d-cc-a8-49-80-9e-db')
    @commethod(3)
    def GetCount(count: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(index: UInt32, object: POINTER(win32more.Storage.Xps.IXpsOMColorProfileResource_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def InsertAt(index: UInt32, object: win32more.Storage.Xps.IXpsOMColorProfileResource_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveAt(index: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetAt(index: UInt32, object: win32more.Storage.Xps.IXpsOMColorProfileResource_head) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Append(object: win32more.Storage.Xps.IXpsOMColorProfileResource_head) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetByPartName(partName: win32more.Storage.Packaging.Opc.IOpcPartUri_head, part: POINTER(win32more.Storage.Xps.IXpsOMColorProfileResource_head)) -> win32more.Foundation.HRESULT: ...
class IXpsOMCoreProperties(c_void_p):
    extends: win32more.Storage.Xps.IXpsOMPart
    Guid = Guid('3340fe8f-4027-4aa1-8f-5f-d3-5a-e4-5f-e5-97')
    @commethod(5)
    def GetOwner(package: POINTER(win32more.Storage.Xps.IXpsOMPackage_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetCategory(category: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetCategory(category: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetContentStatus(contentStatus: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetContentStatus(contentStatus: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetContentType(contentType: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def SetContentType(contentType: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetCreated(created: POINTER(win32more.Foundation.SYSTEMTIME_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def SetCreated(created: POINTER(win32more.Foundation.SYSTEMTIME_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetCreator(creator: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def SetCreator(creator: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def GetDescription(description: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def SetDescription(description: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def GetIdentifier(identifier: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def SetIdentifier(identifier: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def GetKeywords(keywords: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def SetKeywords(keywords: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def GetLanguage(language: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def SetLanguage(language: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def GetLastModifiedBy(lastModifiedBy: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def SetLastModifiedBy(lastModifiedBy: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def GetLastPrinted(lastPrinted: POINTER(win32more.Foundation.SYSTEMTIME_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def SetLastPrinted(lastPrinted: POINTER(win32more.Foundation.SYSTEMTIME_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def GetModified(modified: POINTER(win32more.Foundation.SYSTEMTIME_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def SetModified(modified: POINTER(win32more.Foundation.SYSTEMTIME_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def GetRevision(revision: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def SetRevision(revision: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def GetSubject(subject: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def SetSubject(subject: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def GetTitle(title: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def SetTitle(title: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def GetVersion(version: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def SetVersion(version: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def Clone(coreProperties: POINTER(win32more.Storage.Xps.IXpsOMCoreProperties_head)) -> win32more.Foundation.HRESULT: ...
class IXpsOMDashCollection(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('081613f4-74eb-48f2-83-b3-37-a9-ce-2d-7d-c6')
    @commethod(3)
    def GetCount(count: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(index: UInt32, dash: POINTER(win32more.Storage.Xps.XPS_DASH_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def InsertAt(index: UInt32, dash: POINTER(win32more.Storage.Xps.XPS_DASH_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveAt(index: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetAt(index: UInt32, dash: POINTER(win32more.Storage.Xps.XPS_DASH_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Append(dash: POINTER(win32more.Storage.Xps.XPS_DASH_head)) -> win32more.Foundation.HRESULT: ...
class IXpsOMDictionary(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('897c86b8-8eaf-4ae3-bd-de-56-41-9f-cf-42-36')
    @commethod(3)
    def GetOwner(owner: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetCount(count: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetAt(index: UInt32, key: POINTER(win32more.Foundation.PWSTR), entry: POINTER(win32more.Storage.Xps.IXpsOMShareable_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetByKey(key: win32more.Foundation.PWSTR, beforeEntry: win32more.Storage.Xps.IXpsOMShareable_head, entry: POINTER(win32more.Storage.Xps.IXpsOMShareable_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetIndex(entry: win32more.Storage.Xps.IXpsOMShareable_head, index: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Append(key: win32more.Foundation.PWSTR, entry: win32more.Storage.Xps.IXpsOMShareable_head) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def InsertAt(index: UInt32, key: win32more.Foundation.PWSTR, entry: win32more.Storage.Xps.IXpsOMShareable_head) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def RemoveAt(index: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def SetAt(index: UInt32, key: win32more.Foundation.PWSTR, entry: win32more.Storage.Xps.IXpsOMShareable_head) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def Clone(dictionary: POINTER(win32more.Storage.Xps.IXpsOMDictionary_head)) -> win32more.Foundation.HRESULT: ...
class IXpsOMDocument(c_void_p):
    extends: win32more.Storage.Xps.IXpsOMPart
    Guid = Guid('2c2c94cb-ac5f-4254-8e-e9-23-94-83-09-d9-f0')
    @commethod(5)
    def GetOwner(documentSequence: POINTER(win32more.Storage.Xps.IXpsOMDocumentSequence_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetPageReferences(pageReferences: POINTER(win32more.Storage.Xps.IXpsOMPageReferenceCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetPrintTicketResource(printTicketResource: POINTER(win32more.Storage.Xps.IXpsOMPrintTicketResource_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetPrintTicketResource(printTicketResource: win32more.Storage.Xps.IXpsOMPrintTicketResource_head) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetDocumentStructureResource(documentStructureResource: POINTER(win32more.Storage.Xps.IXpsOMDocumentStructureResource_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetDocumentStructureResource(documentStructureResource: win32more.Storage.Xps.IXpsOMDocumentStructureResource_head) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetSignatureBlockResources(signatureBlockResources: POINTER(win32more.Storage.Xps.IXpsOMSignatureBlockResourceCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def Clone(document: POINTER(win32more.Storage.Xps.IXpsOMDocument_head)) -> win32more.Foundation.HRESULT: ...
class IXpsOMDocumentCollection(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('d1c87f0d-e947-4754-8a-25-97-14-78-f7-e8-3e')
    @commethod(3)
    def GetCount(count: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(index: UInt32, document: POINTER(win32more.Storage.Xps.IXpsOMDocument_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def InsertAt(index: UInt32, document: win32more.Storage.Xps.IXpsOMDocument_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveAt(index: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetAt(index: UInt32, document: win32more.Storage.Xps.IXpsOMDocument_head) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Append(document: win32more.Storage.Xps.IXpsOMDocument_head) -> win32more.Foundation.HRESULT: ...
class IXpsOMDocumentSequence(c_void_p):
    extends: win32more.Storage.Xps.IXpsOMPart
    Guid = Guid('56492eb4-d8d5-425e-82-56-4c-2b-64-ad-02-64')
    @commethod(5)
    def GetOwner(package: POINTER(win32more.Storage.Xps.IXpsOMPackage_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetDocuments(documents: POINTER(win32more.Storage.Xps.IXpsOMDocumentCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetPrintTicketResource(printTicketResource: POINTER(win32more.Storage.Xps.IXpsOMPrintTicketResource_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetPrintTicketResource(printTicketResource: win32more.Storage.Xps.IXpsOMPrintTicketResource_head) -> win32more.Foundation.HRESULT: ...
class IXpsOMDocumentStructureResource(c_void_p):
    extends: win32more.Storage.Xps.IXpsOMResource
    Guid = Guid('85febc8a-6b63-48a9-af-07-70-64-e4-ec-ff-30')
    @commethod(5)
    def GetOwner(owner: POINTER(win32more.Storage.Xps.IXpsOMDocument_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetStream(stream: POINTER(win32more.System.Com.IStream_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetContent(sourceStream: win32more.System.Com.IStream_head, partName: win32more.Storage.Packaging.Opc.IOpcPartUri_head) -> win32more.Foundation.HRESULT: ...
class IXpsOMFontResource(c_void_p):
    extends: win32more.Storage.Xps.IXpsOMResource
    Guid = Guid('a8c45708-47d9-4af4-8d-20-33-b4-8c-9b-84-85')
    @commethod(5)
    def GetStream(readerStream: POINTER(win32more.System.Com.IStream_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetContent(sourceStream: win32more.System.Com.IStream_head, embeddingOption: win32more.Storage.Xps.XPS_FONT_EMBEDDING, partName: win32more.Storage.Packaging.Opc.IOpcPartUri_head) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetEmbeddingOption(embeddingOption: POINTER(win32more.Storage.Xps.XPS_FONT_EMBEDDING)) -> win32more.Foundation.HRESULT: ...
class IXpsOMFontResourceCollection(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('70b4a6bb-88d4-4fa8-aa-f9-6d-9c-59-6f-db-ad')
    @commethod(3)
    def GetCount(count: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(index: UInt32, value: POINTER(win32more.Storage.Xps.IXpsOMFontResource_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetAt(index: UInt32, value: win32more.Storage.Xps.IXpsOMFontResource_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def InsertAt(index: UInt32, value: win32more.Storage.Xps.IXpsOMFontResource_head) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def Append(value: win32more.Storage.Xps.IXpsOMFontResource_head) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def RemoveAt(index: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetByPartName(partName: win32more.Storage.Packaging.Opc.IOpcPartUri_head, part: POINTER(win32more.Storage.Xps.IXpsOMFontResource_head)) -> win32more.Foundation.HRESULT: ...
class IXpsOMGeometry(c_void_p):
    extends: win32more.Storage.Xps.IXpsOMShareable
    Guid = Guid('64fcf3d7-4d58-44ba-ad-73-a1-3a-f6-49-20-72')
    @commethod(5)
    def GetFigures(figures: POINTER(win32more.Storage.Xps.IXpsOMGeometryFigureCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetFillRule(fillRule: POINTER(win32more.Storage.Xps.XPS_FILL_RULE)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetFillRule(fillRule: win32more.Storage.Xps.XPS_FILL_RULE) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetTransform(transform: POINTER(win32more.Storage.Xps.IXpsOMMatrixTransform_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetTransformLocal(transform: POINTER(win32more.Storage.Xps.IXpsOMMatrixTransform_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetTransformLocal(transform: win32more.Storage.Xps.IXpsOMMatrixTransform_head) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetTransformLookup(lookup: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def SetTransformLookup(lookup: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def Clone(geometry: POINTER(win32more.Storage.Xps.IXpsOMGeometry_head)) -> win32more.Foundation.HRESULT: ...
class IXpsOMGeometryFigure(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('d410dc83-908c-443e-89-47-b1-79-5d-3c-16-5a')
    @commethod(3)
    def GetOwner(owner: POINTER(win32more.Storage.Xps.IXpsOMGeometry_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetSegmentData(dataCount: POINTER(UInt32), segmentData: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetSegmentTypes(segmentCount: POINTER(UInt32), segmentTypes: POINTER(win32more.Storage.Xps.XPS_SEGMENT_TYPE)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetSegmentStrokes(segmentCount: POINTER(UInt32), segmentStrokes: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetSegments(segmentCount: UInt32, segmentDataCount: UInt32, segmentTypes: POINTER(win32more.Storage.Xps.XPS_SEGMENT_TYPE), segmentData: POINTER(Single), segmentStrokes: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetStartPoint(startPoint: POINTER(win32more.Storage.Xps.XPS_POINT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetStartPoint(startPoint: POINTER(win32more.Storage.Xps.XPS_POINT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetIsClosed(isClosed: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def SetIsClosed(isClosed: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetIsFilled(isFilled: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def SetIsFilled(isFilled: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetSegmentCount(segmentCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetSegmentDataCount(segmentDataCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def GetSegmentStrokePattern(segmentStrokePattern: POINTER(win32more.Storage.Xps.XPS_SEGMENT_STROKE_PATTERN)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def Clone(geometryFigure: POINTER(win32more.Storage.Xps.IXpsOMGeometryFigure_head)) -> win32more.Foundation.HRESULT: ...
class IXpsOMGeometryFigureCollection(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('fd48c3f3-a58e-4b5a-88-26-1d-e5-4a-be-72-b2')
    @commethod(3)
    def GetCount(count: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(index: UInt32, geometryFigure: POINTER(win32more.Storage.Xps.IXpsOMGeometryFigure_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def InsertAt(index: UInt32, geometryFigure: win32more.Storage.Xps.IXpsOMGeometryFigure_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveAt(index: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetAt(index: UInt32, geometryFigure: win32more.Storage.Xps.IXpsOMGeometryFigure_head) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Append(geometryFigure: win32more.Storage.Xps.IXpsOMGeometryFigure_head) -> win32more.Foundation.HRESULT: ...
class IXpsOMGlyphs(c_void_p):
    extends: win32more.Storage.Xps.IXpsOMVisual
    Guid = Guid('819b3199-0a5a-4b64-be-c7-a9-e1-7e-78-0d-e2')
    @commethod(30)
    def GetUnicodeString(unicodeString: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def GetGlyphIndexCount(indexCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def GetGlyphIndices(indexCount: POINTER(UInt32), glyphIndices: POINTER(win32more.Storage.Xps.XPS_GLYPH_INDEX_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def GetGlyphMappingCount(glyphMappingCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def GetGlyphMappings(glyphMappingCount: POINTER(UInt32), glyphMappings: POINTER(win32more.Storage.Xps.XPS_GLYPH_MAPPING_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def GetProhibitedCaretStopCount(prohibitedCaretStopCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def GetProhibitedCaretStops(prohibitedCaretStopCount: POINTER(UInt32), prohibitedCaretStops: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def GetBidiLevel(bidiLevel: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def GetIsSideways(isSideways: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def GetDeviceFontName(deviceFontName: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def GetStyleSimulations(styleSimulations: POINTER(win32more.Storage.Xps.XPS_STYLE_SIMULATION)) -> win32more.Foundation.HRESULT: ...
    @commethod(41)
    def SetStyleSimulations(styleSimulations: win32more.Storage.Xps.XPS_STYLE_SIMULATION) -> win32more.Foundation.HRESULT: ...
    @commethod(42)
    def GetOrigin(origin: POINTER(win32more.Storage.Xps.XPS_POINT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(43)
    def SetOrigin(origin: POINTER(win32more.Storage.Xps.XPS_POINT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(44)
    def GetFontRenderingEmSize(fontRenderingEmSize: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(45)
    def SetFontRenderingEmSize(fontRenderingEmSize: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(46)
    def GetFontResource(fontResource: POINTER(win32more.Storage.Xps.IXpsOMFontResource_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(47)
    def SetFontResource(fontResource: win32more.Storage.Xps.IXpsOMFontResource_head) -> win32more.Foundation.HRESULT: ...
    @commethod(48)
    def GetFontFaceIndex(fontFaceIndex: POINTER(Int16)) -> win32more.Foundation.HRESULT: ...
    @commethod(49)
    def SetFontFaceIndex(fontFaceIndex: Int16) -> win32more.Foundation.HRESULT: ...
    @commethod(50)
    def GetFillBrush(fillBrush: POINTER(win32more.Storage.Xps.IXpsOMBrush_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(51)
    def GetFillBrushLocal(fillBrush: POINTER(win32more.Storage.Xps.IXpsOMBrush_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(52)
    def SetFillBrushLocal(fillBrush: win32more.Storage.Xps.IXpsOMBrush_head) -> win32more.Foundation.HRESULT: ...
    @commethod(53)
    def GetFillBrushLookup(key: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(54)
    def SetFillBrushLookup(key: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(55)
    def GetGlyphsEditor(editor: POINTER(win32more.Storage.Xps.IXpsOMGlyphsEditor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(56)
    def Clone(glyphs: POINTER(win32more.Storage.Xps.IXpsOMGlyphs_head)) -> win32more.Foundation.HRESULT: ...
class IXpsOMGlyphsEditor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('a5ab8616-5b16-4b9f-96-29-89-b3-23-ed-79-09')
    @commethod(3)
    def ApplyEdits() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetUnicodeString(unicodeString: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetUnicodeString(unicodeString: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetGlyphIndexCount(indexCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetGlyphIndices(indexCount: POINTER(UInt32), glyphIndices: POINTER(win32more.Storage.Xps.XPS_GLYPH_INDEX_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetGlyphIndices(indexCount: UInt32, glyphIndices: POINTER(win32more.Storage.Xps.XPS_GLYPH_INDEX_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetGlyphMappingCount(glyphMappingCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetGlyphMappings(glyphMappingCount: POINTER(UInt32), glyphMappings: POINTER(win32more.Storage.Xps.XPS_GLYPH_MAPPING_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def SetGlyphMappings(glyphMappingCount: UInt32, glyphMappings: POINTER(win32more.Storage.Xps.XPS_GLYPH_MAPPING_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetProhibitedCaretStopCount(prohibitedCaretStopCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetProhibitedCaretStops(count: POINTER(UInt32), prohibitedCaretStops: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def SetProhibitedCaretStops(count: UInt32, prohibitedCaretStops: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetBidiLevel(bidiLevel: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def SetBidiLevel(bidiLevel: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def GetIsSideways(isSideways: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def SetIsSideways(isSideways: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def GetDeviceFontName(deviceFontName: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def SetDeviceFontName(deviceFontName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
class IXpsOMGradientBrush(c_void_p):
    extends: win32more.Storage.Xps.IXpsOMBrush
    Guid = Guid('edb59622-61a2-42c3-ba-ce-ac-f2-28-6c-06-bf')
    @commethod(7)
    def GetGradientStops(gradientStops: POINTER(win32more.Storage.Xps.IXpsOMGradientStopCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetTransform(transform: POINTER(win32more.Storage.Xps.IXpsOMMatrixTransform_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetTransformLocal(transform: POINTER(win32more.Storage.Xps.IXpsOMMatrixTransform_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetTransformLocal(transform: win32more.Storage.Xps.IXpsOMMatrixTransform_head) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetTransformLookup(key: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def SetTransformLookup(key: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetSpreadMethod(spreadMethod: POINTER(win32more.Storage.Xps.XPS_SPREAD_METHOD)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def SetSpreadMethod(spreadMethod: win32more.Storage.Xps.XPS_SPREAD_METHOD) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetColorInterpolationMode(colorInterpolationMode: POINTER(win32more.Storage.Xps.XPS_COLOR_INTERPOLATION)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def SetColorInterpolationMode(colorInterpolationMode: win32more.Storage.Xps.XPS_COLOR_INTERPOLATION) -> win32more.Foundation.HRESULT: ...
class IXpsOMGradientStop(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('5cf4f5cc-3969-49b5-a7-0a-55-50-b6-18-fe-49')
    @commethod(3)
    def GetOwner(owner: POINTER(win32more.Storage.Xps.IXpsOMGradientBrush_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetOffset(offset: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetOffset(offset: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetColor(color: POINTER(win32more.Storage.Xps.XPS_COLOR_head), colorProfile: POINTER(win32more.Storage.Xps.IXpsOMColorProfileResource_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetColor(color: POINTER(win32more.Storage.Xps.XPS_COLOR_head), colorProfile: win32more.Storage.Xps.IXpsOMColorProfileResource_head) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Clone(gradientStop: POINTER(win32more.Storage.Xps.IXpsOMGradientStop_head)) -> win32more.Foundation.HRESULT: ...
class IXpsOMGradientStopCollection(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c9174c3a-3cd3-4319-bd-a4-11-a3-93-92-ce-ef')
    @commethod(3)
    def GetCount(count: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(index: UInt32, stop: POINTER(win32more.Storage.Xps.IXpsOMGradientStop_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def InsertAt(index: UInt32, stop: win32more.Storage.Xps.IXpsOMGradientStop_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveAt(index: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetAt(index: UInt32, stop: win32more.Storage.Xps.IXpsOMGradientStop_head) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Append(stop: win32more.Storage.Xps.IXpsOMGradientStop_head) -> win32more.Foundation.HRESULT: ...
class IXpsOMImageBrush(c_void_p):
    extends: win32more.Storage.Xps.IXpsOMTileBrush
    Guid = Guid('3df0b466-d382-49ef-85-50-dd-94-c8-02-42-e4')
    @commethod(18)
    def GetImageResource(imageResource: POINTER(win32more.Storage.Xps.IXpsOMImageResource_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def SetImageResource(imageResource: win32more.Storage.Xps.IXpsOMImageResource_head) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def GetColorProfileResource(colorProfileResource: POINTER(win32more.Storage.Xps.IXpsOMColorProfileResource_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def SetColorProfileResource(colorProfileResource: win32more.Storage.Xps.IXpsOMColorProfileResource_head) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def Clone(imageBrush: POINTER(win32more.Storage.Xps.IXpsOMImageBrush_head)) -> win32more.Foundation.HRESULT: ...
class IXpsOMImageResource(c_void_p):
    extends: win32more.Storage.Xps.IXpsOMResource
    Guid = Guid('3db8417d-ae50-485e-9a-44-d7-75-8f-78-a2-3f')
    @commethod(5)
    def GetStream(readerStream: POINTER(win32more.System.Com.IStream_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetContent(sourceStream: win32more.System.Com.IStream_head, imageType: win32more.Storage.Xps.XPS_IMAGE_TYPE, partName: win32more.Storage.Packaging.Opc.IOpcPartUri_head) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetImageType(imageType: POINTER(win32more.Storage.Xps.XPS_IMAGE_TYPE)) -> win32more.Foundation.HRESULT: ...
class IXpsOMImageResourceCollection(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('7a4a1a71-9cde-4b71-b3-3f-62-de-84-3e-ab-fe')
    @commethod(3)
    def GetCount(count: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(index: UInt32, object: POINTER(win32more.Storage.Xps.IXpsOMImageResource_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def InsertAt(index: UInt32, object: win32more.Storage.Xps.IXpsOMImageResource_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveAt(index: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetAt(index: UInt32, object: win32more.Storage.Xps.IXpsOMImageResource_head) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Append(object: win32more.Storage.Xps.IXpsOMImageResource_head) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetByPartName(partName: win32more.Storage.Packaging.Opc.IOpcPartUri_head, part: POINTER(win32more.Storage.Xps.IXpsOMImageResource_head)) -> win32more.Foundation.HRESULT: ...
class IXpsOMLinearGradientBrush(c_void_p):
    extends: win32more.Storage.Xps.IXpsOMGradientBrush
    Guid = Guid('005e279f-c30d-40ff-93-ec-19-50-d3-c5-28-db')
    @commethod(17)
    def GetStartPoint(startPoint: POINTER(win32more.Storage.Xps.XPS_POINT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def SetStartPoint(startPoint: POINTER(win32more.Storage.Xps.XPS_POINT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def GetEndPoint(endPoint: POINTER(win32more.Storage.Xps.XPS_POINT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def SetEndPoint(endPoint: POINTER(win32more.Storage.Xps.XPS_POINT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def Clone(linearGradientBrush: POINTER(win32more.Storage.Xps.IXpsOMLinearGradientBrush_head)) -> win32more.Foundation.HRESULT: ...
class IXpsOMMatrixTransform(c_void_p):
    extends: win32more.Storage.Xps.IXpsOMShareable
    Guid = Guid('b77330ff-bb37-4501-a9-3e-f1-b1-e5-0b-fc-46')
    @commethod(5)
    def GetMatrix(matrix: POINTER(win32more.Storage.Xps.XPS_MATRIX_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetMatrix(matrix: POINTER(win32more.Storage.Xps.XPS_MATRIX_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def Clone(matrixTransform: POINTER(win32more.Storage.Xps.IXpsOMMatrixTransform_head)) -> win32more.Foundation.HRESULT: ...
class IXpsOMNameCollection(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('4bddf8ec-c915-421b-a1-66-d1-73-d2-56-53-d2')
    @commethod(3)
    def GetCount(count: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(index: UInt32, name: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
class IXpsOMObjectFactory(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('f9b2a685-a50d-4fc2-b7-64-b5-6e-09-3e-a0-ca')
    @commethod(3)
    def CreatePackage(package: POINTER(win32more.Storage.Xps.IXpsOMPackage_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def CreatePackageFromFile(filename: win32more.Foundation.PWSTR, reuseObjects: win32more.Foundation.BOOL, package: POINTER(win32more.Storage.Xps.IXpsOMPackage_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def CreatePackageFromStream(stream: win32more.System.Com.IStream_head, reuseObjects: win32more.Foundation.BOOL, package: POINTER(win32more.Storage.Xps.IXpsOMPackage_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def CreateStoryFragmentsResource(acquiredStream: win32more.System.Com.IStream_head, partUri: win32more.Storage.Packaging.Opc.IOpcPartUri_head, storyFragmentsResource: POINTER(win32more.Storage.Xps.IXpsOMStoryFragmentsResource_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def CreateDocumentStructureResource(acquiredStream: win32more.System.Com.IStream_head, partUri: win32more.Storage.Packaging.Opc.IOpcPartUri_head, documentStructureResource: POINTER(win32more.Storage.Xps.IXpsOMDocumentStructureResource_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def CreateSignatureBlockResource(acquiredStream: win32more.System.Com.IStream_head, partUri: win32more.Storage.Packaging.Opc.IOpcPartUri_head, signatureBlockResource: POINTER(win32more.Storage.Xps.IXpsOMSignatureBlockResource_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def CreateRemoteDictionaryResource(dictionary: win32more.Storage.Xps.IXpsOMDictionary_head, partUri: win32more.Storage.Packaging.Opc.IOpcPartUri_head, remoteDictionaryResource: POINTER(win32more.Storage.Xps.IXpsOMRemoteDictionaryResource_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def CreateRemoteDictionaryResourceFromStream(dictionaryMarkupStream: win32more.System.Com.IStream_head, dictionaryPartUri: win32more.Storage.Packaging.Opc.IOpcPartUri_head, resources: win32more.Storage.Xps.IXpsOMPartResources_head, dictionaryResource: POINTER(win32more.Storage.Xps.IXpsOMRemoteDictionaryResource_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def CreatePartResources(partResources: POINTER(win32more.Storage.Xps.IXpsOMPartResources_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def CreateDocumentSequence(partUri: win32more.Storage.Packaging.Opc.IOpcPartUri_head, documentSequence: POINTER(win32more.Storage.Xps.IXpsOMDocumentSequence_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def CreateDocument(partUri: win32more.Storage.Packaging.Opc.IOpcPartUri_head, document: POINTER(win32more.Storage.Xps.IXpsOMDocument_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def CreatePageReference(advisoryPageDimensions: POINTER(win32more.Storage.Xps.XPS_SIZE_head), pageReference: POINTER(win32more.Storage.Xps.IXpsOMPageReference_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def CreatePage(pageDimensions: POINTER(win32more.Storage.Xps.XPS_SIZE_head), language: win32more.Foundation.PWSTR, partUri: win32more.Storage.Packaging.Opc.IOpcPartUri_head, page: POINTER(win32more.Storage.Xps.IXpsOMPage_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def CreatePageFromStream(pageMarkupStream: win32more.System.Com.IStream_head, partUri: win32more.Storage.Packaging.Opc.IOpcPartUri_head, resources: win32more.Storage.Xps.IXpsOMPartResources_head, reuseObjects: win32more.Foundation.BOOL, page: POINTER(win32more.Storage.Xps.IXpsOMPage_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def CreateCanvas(canvas: POINTER(win32more.Storage.Xps.IXpsOMCanvas_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def CreateGlyphs(fontResource: win32more.Storage.Xps.IXpsOMFontResource_head, glyphs: POINTER(win32more.Storage.Xps.IXpsOMGlyphs_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def CreatePath(path: POINTER(win32more.Storage.Xps.IXpsOMPath_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def CreateGeometry(geometry: POINTER(win32more.Storage.Xps.IXpsOMGeometry_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def CreateGeometryFigure(startPoint: POINTER(win32more.Storage.Xps.XPS_POINT_head), figure: POINTER(win32more.Storage.Xps.IXpsOMGeometryFigure_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def CreateMatrixTransform(matrix: POINTER(win32more.Storage.Xps.XPS_MATRIX_head), transform: POINTER(win32more.Storage.Xps.IXpsOMMatrixTransform_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def CreateSolidColorBrush(color: POINTER(win32more.Storage.Xps.XPS_COLOR_head), colorProfile: win32more.Storage.Xps.IXpsOMColorProfileResource_head, solidColorBrush: POINTER(win32more.Storage.Xps.IXpsOMSolidColorBrush_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def CreateColorProfileResource(acquiredStream: win32more.System.Com.IStream_head, partUri: win32more.Storage.Packaging.Opc.IOpcPartUri_head, colorProfileResource: POINTER(win32more.Storage.Xps.IXpsOMColorProfileResource_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def CreateImageBrush(image: win32more.Storage.Xps.IXpsOMImageResource_head, viewBox: POINTER(win32more.Storage.Xps.XPS_RECT_head), viewPort: POINTER(win32more.Storage.Xps.XPS_RECT_head), imageBrush: POINTER(win32more.Storage.Xps.IXpsOMImageBrush_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def CreateVisualBrush(viewBox: POINTER(win32more.Storage.Xps.XPS_RECT_head), viewPort: POINTER(win32more.Storage.Xps.XPS_RECT_head), visualBrush: POINTER(win32more.Storage.Xps.IXpsOMVisualBrush_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def CreateImageResource(acquiredStream: win32more.System.Com.IStream_head, contentType: win32more.Storage.Xps.XPS_IMAGE_TYPE, partUri: win32more.Storage.Packaging.Opc.IOpcPartUri_head, imageResource: POINTER(win32more.Storage.Xps.IXpsOMImageResource_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def CreatePrintTicketResource(acquiredStream: win32more.System.Com.IStream_head, partUri: win32more.Storage.Packaging.Opc.IOpcPartUri_head, printTicketResource: POINTER(win32more.Storage.Xps.IXpsOMPrintTicketResource_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def CreateFontResource(acquiredStream: win32more.System.Com.IStream_head, fontEmbedding: win32more.Storage.Xps.XPS_FONT_EMBEDDING, partUri: win32more.Storage.Packaging.Opc.IOpcPartUri_head, isObfSourceStream: win32more.Foundation.BOOL, fontResource: POINTER(win32more.Storage.Xps.IXpsOMFontResource_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def CreateGradientStop(color: POINTER(win32more.Storage.Xps.XPS_COLOR_head), colorProfile: win32more.Storage.Xps.IXpsOMColorProfileResource_head, offset: Single, gradientStop: POINTER(win32more.Storage.Xps.IXpsOMGradientStop_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def CreateLinearGradientBrush(gradStop1: win32more.Storage.Xps.IXpsOMGradientStop_head, gradStop2: win32more.Storage.Xps.IXpsOMGradientStop_head, startPoint: POINTER(win32more.Storage.Xps.XPS_POINT_head), endPoint: POINTER(win32more.Storage.Xps.XPS_POINT_head), linearGradientBrush: POINTER(win32more.Storage.Xps.IXpsOMLinearGradientBrush_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def CreateRadialGradientBrush(gradStop1: win32more.Storage.Xps.IXpsOMGradientStop_head, gradStop2: win32more.Storage.Xps.IXpsOMGradientStop_head, centerPoint: POINTER(win32more.Storage.Xps.XPS_POINT_head), gradientOrigin: POINTER(win32more.Storage.Xps.XPS_POINT_head), radiiSizes: POINTER(win32more.Storage.Xps.XPS_SIZE_head), radialGradientBrush: POINTER(win32more.Storage.Xps.IXpsOMRadialGradientBrush_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def CreateCoreProperties(partUri: win32more.Storage.Packaging.Opc.IOpcPartUri_head, coreProperties: POINTER(win32more.Storage.Xps.IXpsOMCoreProperties_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def CreateDictionary(dictionary: POINTER(win32more.Storage.Xps.IXpsOMDictionary_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def CreatePartUriCollection(partUriCollection: POINTER(win32more.Storage.Xps.IXpsOMPartUriCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def CreatePackageWriterOnFile(fileName: win32more.Foundation.PWSTR, securityAttributes: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), flagsAndAttributes: UInt32, optimizeMarkupSize: win32more.Foundation.BOOL, interleaving: win32more.Storage.Xps.XPS_INTERLEAVING, documentSequencePartName: win32more.Storage.Packaging.Opc.IOpcPartUri_head, coreProperties: win32more.Storage.Xps.IXpsOMCoreProperties_head, packageThumbnail: win32more.Storage.Xps.IXpsOMImageResource_head, documentSequencePrintTicket: win32more.Storage.Xps.IXpsOMPrintTicketResource_head, discardControlPartName: win32more.Storage.Packaging.Opc.IOpcPartUri_head, packageWriter: POINTER(win32more.Storage.Xps.IXpsOMPackageWriter_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def CreatePackageWriterOnStream(outputStream: win32more.System.Com.ISequentialStream_head, optimizeMarkupSize: win32more.Foundation.BOOL, interleaving: win32more.Storage.Xps.XPS_INTERLEAVING, documentSequencePartName: win32more.Storage.Packaging.Opc.IOpcPartUri_head, coreProperties: win32more.Storage.Xps.IXpsOMCoreProperties_head, packageThumbnail: win32more.Storage.Xps.IXpsOMImageResource_head, documentSequencePrintTicket: win32more.Storage.Xps.IXpsOMPrintTicketResource_head, discardControlPartName: win32more.Storage.Packaging.Opc.IOpcPartUri_head, packageWriter: POINTER(win32more.Storage.Xps.IXpsOMPackageWriter_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def CreatePartUri(uri: win32more.Foundation.PWSTR, partUri: POINTER(win32more.Storage.Packaging.Opc.IOpcPartUri_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def CreateReadOnlyStreamOnFile(filename: win32more.Foundation.PWSTR, stream: POINTER(win32more.System.Com.IStream_head)) -> win32more.Foundation.HRESULT: ...
class IXpsOMObjectFactory1(c_void_p):
    extends: win32more.Storage.Xps.IXpsOMObjectFactory
    Guid = Guid('0a91b617-d612-4181-bf-7c-be-58-24-e9-cc-8f')
    @commethod(40)
    def GetDocumentTypeFromFile(filename: win32more.Foundation.PWSTR, documentType: POINTER(win32more.Storage.Xps.XPS_DOCUMENT_TYPE)) -> win32more.Foundation.HRESULT: ...
    @commethod(41)
    def GetDocumentTypeFromStream(xpsDocumentStream: win32more.System.Com.IStream_head, documentType: POINTER(win32more.Storage.Xps.XPS_DOCUMENT_TYPE)) -> win32more.Foundation.HRESULT: ...
    @commethod(42)
    def ConvertHDPhotoToJpegXR(imageResource: win32more.Storage.Xps.IXpsOMImageResource_head) -> win32more.Foundation.HRESULT: ...
    @commethod(43)
    def ConvertJpegXRToHDPhoto(imageResource: win32more.Storage.Xps.IXpsOMImageResource_head) -> win32more.Foundation.HRESULT: ...
    @commethod(44)
    def CreatePackageWriterOnFile1(fileName: win32more.Foundation.PWSTR, securityAttributes: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), flagsAndAttributes: UInt32, optimizeMarkupSize: win32more.Foundation.BOOL, interleaving: win32more.Storage.Xps.XPS_INTERLEAVING, documentSequencePartName: win32more.Storage.Packaging.Opc.IOpcPartUri_head, coreProperties: win32more.Storage.Xps.IXpsOMCoreProperties_head, packageThumbnail: win32more.Storage.Xps.IXpsOMImageResource_head, documentSequencePrintTicket: win32more.Storage.Xps.IXpsOMPrintTicketResource_head, discardControlPartName: win32more.Storage.Packaging.Opc.IOpcPartUri_head, documentType: win32more.Storage.Xps.XPS_DOCUMENT_TYPE, packageWriter: POINTER(win32more.Storage.Xps.IXpsOMPackageWriter_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(45)
    def CreatePackageWriterOnStream1(outputStream: win32more.System.Com.ISequentialStream_head, optimizeMarkupSize: win32more.Foundation.BOOL, interleaving: win32more.Storage.Xps.XPS_INTERLEAVING, documentSequencePartName: win32more.Storage.Packaging.Opc.IOpcPartUri_head, coreProperties: win32more.Storage.Xps.IXpsOMCoreProperties_head, packageThumbnail: win32more.Storage.Xps.IXpsOMImageResource_head, documentSequencePrintTicket: win32more.Storage.Xps.IXpsOMPrintTicketResource_head, discardControlPartName: win32more.Storage.Packaging.Opc.IOpcPartUri_head, documentType: win32more.Storage.Xps.XPS_DOCUMENT_TYPE, packageWriter: POINTER(win32more.Storage.Xps.IXpsOMPackageWriter_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(46)
    def CreatePackage1(package: POINTER(win32more.Storage.Xps.IXpsOMPackage1_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(47)
    def CreatePackageFromStream1(stream: win32more.System.Com.IStream_head, reuseObjects: win32more.Foundation.BOOL, package: POINTER(win32more.Storage.Xps.IXpsOMPackage1_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(48)
    def CreatePackageFromFile1(filename: win32more.Foundation.PWSTR, reuseObjects: win32more.Foundation.BOOL, package: POINTER(win32more.Storage.Xps.IXpsOMPackage1_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(49)
    def CreatePage1(pageDimensions: POINTER(win32more.Storage.Xps.XPS_SIZE_head), language: win32more.Foundation.PWSTR, partUri: win32more.Storage.Packaging.Opc.IOpcPartUri_head, page: POINTER(win32more.Storage.Xps.IXpsOMPage1_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(50)
    def CreatePageFromStream1(pageMarkupStream: win32more.System.Com.IStream_head, partUri: win32more.Storage.Packaging.Opc.IOpcPartUri_head, resources: win32more.Storage.Xps.IXpsOMPartResources_head, reuseObjects: win32more.Foundation.BOOL, page: POINTER(win32more.Storage.Xps.IXpsOMPage1_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(51)
    def CreateRemoteDictionaryResourceFromStream1(dictionaryMarkupStream: win32more.System.Com.IStream_head, partUri: win32more.Storage.Packaging.Opc.IOpcPartUri_head, resources: win32more.Storage.Xps.IXpsOMPartResources_head, dictionaryResource: POINTER(win32more.Storage.Xps.IXpsOMRemoteDictionaryResource_head)) -> win32more.Foundation.HRESULT: ...
class IXpsOMPackage(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('18c3df65-81e1-4674-91-dc-fc-45-2f-5a-41-6f')
    @commethod(3)
    def GetDocumentSequence(documentSequence: POINTER(win32more.Storage.Xps.IXpsOMDocumentSequence_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetDocumentSequence(documentSequence: win32more.Storage.Xps.IXpsOMDocumentSequence_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetCoreProperties(coreProperties: POINTER(win32more.Storage.Xps.IXpsOMCoreProperties_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetCoreProperties(coreProperties: win32more.Storage.Xps.IXpsOMCoreProperties_head) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetDiscardControlPartName(discardControlPartUri: POINTER(win32more.Storage.Packaging.Opc.IOpcPartUri_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetDiscardControlPartName(discardControlPartUri: win32more.Storage.Packaging.Opc.IOpcPartUri_head) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetThumbnailResource(imageResource: POINTER(win32more.Storage.Xps.IXpsOMImageResource_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetThumbnailResource(imageResource: win32more.Storage.Xps.IXpsOMImageResource_head) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def WriteToFile(fileName: win32more.Foundation.PWSTR, securityAttributes: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), flagsAndAttributes: UInt32, optimizeMarkupSize: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def WriteToStream(stream: win32more.System.Com.ISequentialStream_head, optimizeMarkupSize: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
class IXpsOMPackage1(c_void_p):
    extends: win32more.Storage.Xps.IXpsOMPackage
    Guid = Guid('95a9435e-12bb-461b-8e-7f-c6-ad-b0-4c-d9-6a')
    @commethod(13)
    def GetDocumentType(documentType: POINTER(win32more.Storage.Xps.XPS_DOCUMENT_TYPE)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def WriteToFile1(fileName: win32more.Foundation.PWSTR, securityAttributes: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), flagsAndAttributes: UInt32, optimizeMarkupSize: win32more.Foundation.BOOL, documentType: win32more.Storage.Xps.XPS_DOCUMENT_TYPE) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def WriteToStream1(outputStream: win32more.System.Com.ISequentialStream_head, optimizeMarkupSize: win32more.Foundation.BOOL, documentType: win32more.Storage.Xps.XPS_DOCUMENT_TYPE) -> win32more.Foundation.HRESULT: ...
class IXpsOMPackageTarget(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('219a9db0-4959-47d0-80-34-b1-ce-84-f4-1a-4d')
    @commethod(3)
    def CreateXpsOMPackageWriter(documentSequencePartName: win32more.Storage.Packaging.Opc.IOpcPartUri_head, documentSequencePrintTicket: win32more.Storage.Xps.IXpsOMPrintTicketResource_head, discardControlPartName: win32more.Storage.Packaging.Opc.IOpcPartUri_head, packageWriter: POINTER(win32more.Storage.Xps.IXpsOMPackageWriter_head)) -> win32more.Foundation.HRESULT: ...
class IXpsOMPackageWriter(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('4e2aa182-a443-42c6-b4-1b-4f-8e-9d-e7-3f-f9')
    @commethod(3)
    def StartNewDocument(documentPartName: win32more.Storage.Packaging.Opc.IOpcPartUri_head, documentPrintTicket: win32more.Storage.Xps.IXpsOMPrintTicketResource_head, documentStructure: win32more.Storage.Xps.IXpsOMDocumentStructureResource_head, signatureBlockResources: win32more.Storage.Xps.IXpsOMSignatureBlockResourceCollection_head, restrictedFonts: win32more.Storage.Xps.IXpsOMPartUriCollection_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def AddPage(page: win32more.Storage.Xps.IXpsOMPage_head, advisoryPageDimensions: POINTER(win32more.Storage.Xps.XPS_SIZE_head), discardableResourceParts: win32more.Storage.Xps.IXpsOMPartUriCollection_head, storyFragments: win32more.Storage.Xps.IXpsOMStoryFragmentsResource_head, pagePrintTicket: win32more.Storage.Xps.IXpsOMPrintTicketResource_head, pageThumbnail: win32more.Storage.Xps.IXpsOMImageResource_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def AddResource(resource: win32more.Storage.Xps.IXpsOMResource_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Close() -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def IsClosed(isClosed: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
class IXpsOMPackageWriter3D(c_void_p):
    extends: win32more.Storage.Xps.IXpsOMPackageWriter
    Guid = Guid('e8a45033-640e-43fa-9b-df-fd-de-aa-31-c6-a0')
    @commethod(8)
    def AddModelTexture(texturePartName: win32more.Storage.Packaging.Opc.IOpcPartUri_head, textureData: win32more.System.Com.IStream_head) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetModelPrintTicket(printTicketPartName: win32more.Storage.Packaging.Opc.IOpcPartUri_head, printTicketData: win32more.System.Com.IStream_head) -> win32more.Foundation.HRESULT: ...
class IXpsOMPage(c_void_p):
    extends: win32more.Storage.Xps.IXpsOMPart
    Guid = Guid('d3e18888-f120-4fee-8c-68-35-29-6e-ae-91-d4')
    @commethod(5)
    def GetOwner(pageReference: POINTER(win32more.Storage.Xps.IXpsOMPageReference_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetVisuals(visuals: POINTER(win32more.Storage.Xps.IXpsOMVisualCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetPageDimensions(pageDimensions: POINTER(win32more.Storage.Xps.XPS_SIZE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetPageDimensions(pageDimensions: POINTER(win32more.Storage.Xps.XPS_SIZE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetContentBox(contentBox: POINTER(win32more.Storage.Xps.XPS_RECT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetContentBox(contentBox: POINTER(win32more.Storage.Xps.XPS_RECT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetBleedBox(bleedBox: POINTER(win32more.Storage.Xps.XPS_RECT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def SetBleedBox(bleedBox: POINTER(win32more.Storage.Xps.XPS_RECT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetLanguage(language: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def SetLanguage(language: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetName(name: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def SetName(name: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def GetIsHyperlinkTarget(isHyperlinkTarget: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def SetIsHyperlinkTarget(isHyperlinkTarget: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def GetDictionary(resourceDictionary: POINTER(win32more.Storage.Xps.IXpsOMDictionary_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def GetDictionaryLocal(resourceDictionary: POINTER(win32more.Storage.Xps.IXpsOMDictionary_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def SetDictionaryLocal(resourceDictionary: win32more.Storage.Xps.IXpsOMDictionary_head) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def GetDictionaryResource(remoteDictionaryResource: POINTER(win32more.Storage.Xps.IXpsOMRemoteDictionaryResource_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def SetDictionaryResource(remoteDictionaryResource: win32more.Storage.Xps.IXpsOMRemoteDictionaryResource_head) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def Write(stream: win32more.System.Com.ISequentialStream_head, optimizeMarkupSize: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def GenerateUnusedLookupKey(type: win32more.Storage.Xps.XPS_OBJECT_TYPE, key: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def Clone(page: POINTER(win32more.Storage.Xps.IXpsOMPage_head)) -> win32more.Foundation.HRESULT: ...
class IXpsOMPage1(c_void_p):
    extends: win32more.Storage.Xps.IXpsOMPage
    Guid = Guid('305b60ef-6892-4dda-9c-bb-3a-a6-59-74-50-8a')
    @commethod(27)
    def GetDocumentType(documentType: POINTER(win32more.Storage.Xps.XPS_DOCUMENT_TYPE)) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def Write1(stream: win32more.System.Com.ISequentialStream_head, optimizeMarkupSize: win32more.Foundation.BOOL, documentType: win32more.Storage.Xps.XPS_DOCUMENT_TYPE) -> win32more.Foundation.HRESULT: ...
class IXpsOMPageReference(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ed360180-6f92-4998-89-0d-2f-20-85-31-a0-a0')
    @commethod(3)
    def GetOwner(document: POINTER(win32more.Storage.Xps.IXpsOMDocument_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetPage(page: POINTER(win32more.Storage.Xps.IXpsOMPage_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetPage(page: win32more.Storage.Xps.IXpsOMPage_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def DiscardPage() -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def IsPageLoaded(isPageLoaded: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetAdvisoryPageDimensions(pageDimensions: POINTER(win32more.Storage.Xps.XPS_SIZE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetAdvisoryPageDimensions(pageDimensions: POINTER(win32more.Storage.Xps.XPS_SIZE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetStoryFragmentsResource(storyFragmentsResource: POINTER(win32more.Storage.Xps.IXpsOMStoryFragmentsResource_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def SetStoryFragmentsResource(storyFragmentsResource: win32more.Storage.Xps.IXpsOMStoryFragmentsResource_head) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetPrintTicketResource(printTicketResource: POINTER(win32more.Storage.Xps.IXpsOMPrintTicketResource_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def SetPrintTicketResource(printTicketResource: win32more.Storage.Xps.IXpsOMPrintTicketResource_head) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetThumbnailResource(imageResource: POINTER(win32more.Storage.Xps.IXpsOMImageResource_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def SetThumbnailResource(imageResource: win32more.Storage.Xps.IXpsOMImageResource_head) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def CollectLinkTargets(linkTargets: POINTER(win32more.Storage.Xps.IXpsOMNameCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def CollectPartResources(partResources: POINTER(win32more.Storage.Xps.IXpsOMPartResources_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def HasRestrictedFonts(restrictedFonts: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def Clone(pageReference: POINTER(win32more.Storage.Xps.IXpsOMPageReference_head)) -> win32more.Foundation.HRESULT: ...
class IXpsOMPageReferenceCollection(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ca16ba4d-e7b9-45c5-95-8b-f9-80-22-47-37-45')
    @commethod(3)
    def GetCount(count: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(index: UInt32, pageReference: POINTER(win32more.Storage.Xps.IXpsOMPageReference_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def InsertAt(index: UInt32, pageReference: win32more.Storage.Xps.IXpsOMPageReference_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveAt(index: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetAt(index: UInt32, pageReference: win32more.Storage.Xps.IXpsOMPageReference_head) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Append(pageReference: win32more.Storage.Xps.IXpsOMPageReference_head) -> win32more.Foundation.HRESULT: ...
class IXpsOMPart(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('74eb2f0b-a91e-4486-af-ac-0f-ab-ec-a3-df-c6')
    @commethod(3)
    def GetPartName(partUri: POINTER(win32more.Storage.Packaging.Opc.IOpcPartUri_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetPartName(partUri: win32more.Storage.Packaging.Opc.IOpcPartUri_head) -> win32more.Foundation.HRESULT: ...
class IXpsOMPartResources(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('f4cf7729-4864-4275-99-b3-a8-71-71-63-ec-af')
    @commethod(3)
    def GetFontResources(fontResources: POINTER(win32more.Storage.Xps.IXpsOMFontResourceCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetImageResources(imageResources: POINTER(win32more.Storage.Xps.IXpsOMImageResourceCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetColorProfileResources(colorProfileResources: POINTER(win32more.Storage.Xps.IXpsOMColorProfileResourceCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetRemoteDictionaryResources(dictionaryResources: POINTER(win32more.Storage.Xps.IXpsOMRemoteDictionaryResourceCollection_head)) -> win32more.Foundation.HRESULT: ...
class IXpsOMPartUriCollection(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('57c650d4-067c-4893-8c-33-f6-2a-06-33-73-0f')
    @commethod(3)
    def GetCount(count: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(index: UInt32, partUri: POINTER(win32more.Storage.Packaging.Opc.IOpcPartUri_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def InsertAt(index: UInt32, partUri: win32more.Storage.Packaging.Opc.IOpcPartUri_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveAt(index: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetAt(index: UInt32, partUri: win32more.Storage.Packaging.Opc.IOpcPartUri_head) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Append(partUri: win32more.Storage.Packaging.Opc.IOpcPartUri_head) -> win32more.Foundation.HRESULT: ...
class IXpsOMPath(c_void_p):
    extends: win32more.Storage.Xps.IXpsOMVisual
    Guid = Guid('37d38bb6-3ee9-4110-93-12-14-b1-94-16-33-37')
    @commethod(30)
    def GetGeometry(geometry: POINTER(win32more.Storage.Xps.IXpsOMGeometry_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def GetGeometryLocal(geometry: POINTER(win32more.Storage.Xps.IXpsOMGeometry_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def SetGeometryLocal(geometry: win32more.Storage.Xps.IXpsOMGeometry_head) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def GetGeometryLookup(lookup: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def SetGeometryLookup(lookup: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def GetAccessibilityShortDescription(shortDescription: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def SetAccessibilityShortDescription(shortDescription: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def GetAccessibilityLongDescription(longDescription: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def SetAccessibilityLongDescription(longDescription: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def GetSnapsToPixels(snapsToPixels: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def SetSnapsToPixels(snapsToPixels: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(41)
    def GetStrokeBrush(brush: POINTER(win32more.Storage.Xps.IXpsOMBrush_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(42)
    def GetStrokeBrushLocal(brush: POINTER(win32more.Storage.Xps.IXpsOMBrush_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(43)
    def SetStrokeBrushLocal(brush: win32more.Storage.Xps.IXpsOMBrush_head) -> win32more.Foundation.HRESULT: ...
    @commethod(44)
    def GetStrokeBrushLookup(lookup: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(45)
    def SetStrokeBrushLookup(lookup: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(46)
    def GetStrokeDashes(strokeDashes: POINTER(win32more.Storage.Xps.IXpsOMDashCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(47)
    def GetStrokeDashCap(strokeDashCap: POINTER(win32more.Storage.Xps.XPS_DASH_CAP)) -> win32more.Foundation.HRESULT: ...
    @commethod(48)
    def SetStrokeDashCap(strokeDashCap: win32more.Storage.Xps.XPS_DASH_CAP) -> win32more.Foundation.HRESULT: ...
    @commethod(49)
    def GetStrokeDashOffset(strokeDashOffset: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(50)
    def SetStrokeDashOffset(strokeDashOffset: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(51)
    def GetStrokeStartLineCap(strokeStartLineCap: POINTER(win32more.Storage.Xps.XPS_LINE_CAP)) -> win32more.Foundation.HRESULT: ...
    @commethod(52)
    def SetStrokeStartLineCap(strokeStartLineCap: win32more.Storage.Xps.XPS_LINE_CAP) -> win32more.Foundation.HRESULT: ...
    @commethod(53)
    def GetStrokeEndLineCap(strokeEndLineCap: POINTER(win32more.Storage.Xps.XPS_LINE_CAP)) -> win32more.Foundation.HRESULT: ...
    @commethod(54)
    def SetStrokeEndLineCap(strokeEndLineCap: win32more.Storage.Xps.XPS_LINE_CAP) -> win32more.Foundation.HRESULT: ...
    @commethod(55)
    def GetStrokeLineJoin(strokeLineJoin: POINTER(win32more.Storage.Xps.XPS_LINE_JOIN)) -> win32more.Foundation.HRESULT: ...
    @commethod(56)
    def SetStrokeLineJoin(strokeLineJoin: win32more.Storage.Xps.XPS_LINE_JOIN) -> win32more.Foundation.HRESULT: ...
    @commethod(57)
    def GetStrokeMiterLimit(strokeMiterLimit: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(58)
    def SetStrokeMiterLimit(strokeMiterLimit: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(59)
    def GetStrokeThickness(strokeThickness: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(60)
    def SetStrokeThickness(strokeThickness: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(61)
    def GetFillBrush(brush: POINTER(win32more.Storage.Xps.IXpsOMBrush_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(62)
    def GetFillBrushLocal(brush: POINTER(win32more.Storage.Xps.IXpsOMBrush_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(63)
    def SetFillBrushLocal(brush: win32more.Storage.Xps.IXpsOMBrush_head) -> win32more.Foundation.HRESULT: ...
    @commethod(64)
    def GetFillBrushLookup(lookup: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(65)
    def SetFillBrushLookup(lookup: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(66)
    def Clone(path: POINTER(win32more.Storage.Xps.IXpsOMPath_head)) -> win32more.Foundation.HRESULT: ...
class IXpsOMPrintTicketResource(c_void_p):
    extends: win32more.Storage.Xps.IXpsOMResource
    Guid = Guid('e7ff32d2-34aa-499b-bb-e9-9c-d4-ee-6c-59-f7')
    @commethod(5)
    def GetStream(stream: POINTER(win32more.System.Com.IStream_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetContent(sourceStream: win32more.System.Com.IStream_head, partName: win32more.Storage.Packaging.Opc.IOpcPartUri_head) -> win32more.Foundation.HRESULT: ...
class IXpsOMRadialGradientBrush(c_void_p):
    extends: win32more.Storage.Xps.IXpsOMGradientBrush
    Guid = Guid('75f207e5-08bf-413c-96-b1-b8-2b-40-64-17-6b')
    @commethod(17)
    def GetCenter(center: POINTER(win32more.Storage.Xps.XPS_POINT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def SetCenter(center: POINTER(win32more.Storage.Xps.XPS_POINT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def GetRadiiSizes(radiiSizes: POINTER(win32more.Storage.Xps.XPS_SIZE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def SetRadiiSizes(radiiSizes: POINTER(win32more.Storage.Xps.XPS_SIZE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def GetGradientOrigin(origin: POINTER(win32more.Storage.Xps.XPS_POINT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def SetGradientOrigin(origin: POINTER(win32more.Storage.Xps.XPS_POINT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def Clone(radialGradientBrush: POINTER(win32more.Storage.Xps.IXpsOMRadialGradientBrush_head)) -> win32more.Foundation.HRESULT: ...
class IXpsOMRemoteDictionaryResource(c_void_p):
    extends: win32more.Storage.Xps.IXpsOMResource
    Guid = Guid('c9bd7cd4-e16a-4bf8-8c-84-c9-50-af-7a-30-61')
    @commethod(5)
    def GetDictionary(dictionary: POINTER(win32more.Storage.Xps.IXpsOMDictionary_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetDictionary(dictionary: win32more.Storage.Xps.IXpsOMDictionary_head) -> win32more.Foundation.HRESULT: ...
class IXpsOMRemoteDictionaryResource1(c_void_p):
    extends: win32more.Storage.Xps.IXpsOMRemoteDictionaryResource
    Guid = Guid('bf8fc1d4-9d46-4141-ba-5f-94-bb-92-50-d0-41')
    @commethod(7)
    def GetDocumentType(documentType: POINTER(win32more.Storage.Xps.XPS_DOCUMENT_TYPE)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Write1(stream: win32more.System.Com.ISequentialStream_head, documentType: win32more.Storage.Xps.XPS_DOCUMENT_TYPE) -> win32more.Foundation.HRESULT: ...
class IXpsOMRemoteDictionaryResourceCollection(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('5c38db61-7fec-464a-87-bd-41-e3-be-f0-18-be')
    @commethod(3)
    def GetCount(count: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(index: UInt32, object: POINTER(win32more.Storage.Xps.IXpsOMRemoteDictionaryResource_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def InsertAt(index: UInt32, object: win32more.Storage.Xps.IXpsOMRemoteDictionaryResource_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveAt(index: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetAt(index: UInt32, object: win32more.Storage.Xps.IXpsOMRemoteDictionaryResource_head) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Append(object: win32more.Storage.Xps.IXpsOMRemoteDictionaryResource_head) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetByPartName(partName: win32more.Storage.Packaging.Opc.IOpcPartUri_head, remoteDictionaryResource: POINTER(win32more.Storage.Xps.IXpsOMRemoteDictionaryResource_head)) -> win32more.Foundation.HRESULT: ...
class IXpsOMResource(c_void_p):
    extends: win32more.Storage.Xps.IXpsOMPart
    Guid = Guid('da2ac0a2-73a2-4975-ad-14-74-09-7c-3f-f3-a5')
class IXpsOMShareable(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('7137398f-2fc1-454d-8c-6a-2c-31-15-a1-6e-ce')
    @commethod(3)
    def GetOwner(owner: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetType(type: POINTER(win32more.Storage.Xps.XPS_OBJECT_TYPE)) -> win32more.Foundation.HRESULT: ...
class IXpsOMSignatureBlockResource(c_void_p):
    extends: win32more.Storage.Xps.IXpsOMResource
    Guid = Guid('4776ad35-2e04-4357-87-43-eb-f6-c1-71-a9-05')
    @commethod(5)
    def GetOwner(owner: POINTER(win32more.Storage.Xps.IXpsOMDocument_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetStream(stream: POINTER(win32more.System.Com.IStream_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetContent(sourceStream: win32more.System.Com.IStream_head, partName: win32more.Storage.Packaging.Opc.IOpcPartUri_head) -> win32more.Foundation.HRESULT: ...
class IXpsOMSignatureBlockResourceCollection(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ab8f5d8e-351b-4d33-aa-ed-fa-56-f0-02-29-31')
    @commethod(3)
    def GetCount(count: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(index: UInt32, signatureBlockResource: POINTER(win32more.Storage.Xps.IXpsOMSignatureBlockResource_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def InsertAt(index: UInt32, signatureBlockResource: win32more.Storage.Xps.IXpsOMSignatureBlockResource_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveAt(index: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetAt(index: UInt32, signatureBlockResource: win32more.Storage.Xps.IXpsOMSignatureBlockResource_head) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Append(signatureBlockResource: win32more.Storage.Xps.IXpsOMSignatureBlockResource_head) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetByPartName(partName: win32more.Storage.Packaging.Opc.IOpcPartUri_head, signatureBlockResource: POINTER(win32more.Storage.Xps.IXpsOMSignatureBlockResource_head)) -> win32more.Foundation.HRESULT: ...
class IXpsOMSolidColorBrush(c_void_p):
    extends: win32more.Storage.Xps.IXpsOMBrush
    Guid = Guid('a06f9f05-3be9-4763-98-a8-09-4f-c6-72-e4-88')
    @commethod(7)
    def GetColor(color: POINTER(win32more.Storage.Xps.XPS_COLOR_head), colorProfile: POINTER(win32more.Storage.Xps.IXpsOMColorProfileResource_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetColor(color: POINTER(win32more.Storage.Xps.XPS_COLOR_head), colorProfile: win32more.Storage.Xps.IXpsOMColorProfileResource_head) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def Clone(solidColorBrush: POINTER(win32more.Storage.Xps.IXpsOMSolidColorBrush_head)) -> win32more.Foundation.HRESULT: ...
class IXpsOMStoryFragmentsResource(c_void_p):
    extends: win32more.Storage.Xps.IXpsOMResource
    Guid = Guid('c2b3ca09-0473-4282-87-ae-17-80-86-32-23-f0')
    @commethod(5)
    def GetOwner(owner: POINTER(win32more.Storage.Xps.IXpsOMPageReference_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetStream(stream: POINTER(win32more.System.Com.IStream_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetContent(sourceStream: win32more.System.Com.IStream_head, partName: win32more.Storage.Packaging.Opc.IOpcPartUri_head) -> win32more.Foundation.HRESULT: ...
class IXpsOMThumbnailGenerator(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('15b873d5-1971-41e8-83-a3-65-78-40-30-64-c7')
    @commethod(3)
    def GenerateThumbnail(page: win32more.Storage.Xps.IXpsOMPage_head, thumbnailType: win32more.Storage.Xps.XPS_IMAGE_TYPE, thumbnailSize: win32more.Storage.Xps.XPS_THUMBNAIL_SIZE, imageResourcePartName: win32more.Storage.Packaging.Opc.IOpcPartUri_head, imageResource: POINTER(win32more.Storage.Xps.IXpsOMImageResource_head)) -> win32more.Foundation.HRESULT: ...
class IXpsOMTileBrush(c_void_p):
    extends: win32more.Storage.Xps.IXpsOMBrush
    Guid = Guid('0fc2328d-d722-4a54-b2-ec-be-90-21-8a-78-9e')
    @commethod(7)
    def GetTransform(transform: POINTER(win32more.Storage.Xps.IXpsOMMatrixTransform_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetTransformLocal(transform: POINTER(win32more.Storage.Xps.IXpsOMMatrixTransform_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetTransformLocal(transform: win32more.Storage.Xps.IXpsOMMatrixTransform_head) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetTransformLookup(key: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def SetTransformLookup(key: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetViewbox(viewbox: POINTER(win32more.Storage.Xps.XPS_RECT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def SetViewbox(viewbox: POINTER(win32more.Storage.Xps.XPS_RECT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetViewport(viewport: POINTER(win32more.Storage.Xps.XPS_RECT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def SetViewport(viewport: POINTER(win32more.Storage.Xps.XPS_RECT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def GetTileMode(tileMode: POINTER(win32more.Storage.Xps.XPS_TILE_MODE)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def SetTileMode(tileMode: win32more.Storage.Xps.XPS_TILE_MODE) -> win32more.Foundation.HRESULT: ...
class IXpsOMVisual(c_void_p):
    extends: win32more.Storage.Xps.IXpsOMShareable
    Guid = Guid('bc3e7333-fb0b-4af3-a8-19-0b-4e-aa-d0-d2-fd')
    @commethod(5)
    def GetTransform(matrixTransform: POINTER(win32more.Storage.Xps.IXpsOMMatrixTransform_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetTransformLocal(matrixTransform: POINTER(win32more.Storage.Xps.IXpsOMMatrixTransform_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetTransformLocal(matrixTransform: win32more.Storage.Xps.IXpsOMMatrixTransform_head) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetTransformLookup(key: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetTransformLookup(key: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetClipGeometry(clipGeometry: POINTER(win32more.Storage.Xps.IXpsOMGeometry_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetClipGeometryLocal(clipGeometry: POINTER(win32more.Storage.Xps.IXpsOMGeometry_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def SetClipGeometryLocal(clipGeometry: win32more.Storage.Xps.IXpsOMGeometry_head) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetClipGeometryLookup(key: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def SetClipGeometryLookup(key: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetOpacity(opacity: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def SetOpacity(opacity: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def GetOpacityMaskBrush(opacityMaskBrush: POINTER(win32more.Storage.Xps.IXpsOMBrush_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def GetOpacityMaskBrushLocal(opacityMaskBrush: POINTER(win32more.Storage.Xps.IXpsOMBrush_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def SetOpacityMaskBrushLocal(opacityMaskBrush: win32more.Storage.Xps.IXpsOMBrush_head) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def GetOpacityMaskBrushLookup(key: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def SetOpacityMaskBrushLookup(key: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def GetName(name: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def SetName(name: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def GetIsHyperlinkTarget(isHyperlink: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def SetIsHyperlinkTarget(isHyperlink: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def GetHyperlinkNavigateUri(hyperlinkUri: POINTER(win32more.System.Com.IUri_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def SetHyperlinkNavigateUri(hyperlinkUri: win32more.System.Com.IUri_head) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def GetLanguage(language: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def SetLanguage(language: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
class IXpsOMVisualBrush(c_void_p):
    extends: win32more.Storage.Xps.IXpsOMTileBrush
    Guid = Guid('97e294af-5b37-46b4-80-57-87-4d-2f-64-11-9b')
    @commethod(18)
    def GetVisual(visual: POINTER(win32more.Storage.Xps.IXpsOMVisual_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def GetVisualLocal(visual: POINTER(win32more.Storage.Xps.IXpsOMVisual_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def SetVisualLocal(visual: win32more.Storage.Xps.IXpsOMVisual_head) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def GetVisualLookup(lookup: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def SetVisualLookup(lookup: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def Clone(visualBrush: POINTER(win32more.Storage.Xps.IXpsOMVisualBrush_head)) -> win32more.Foundation.HRESULT: ...
class IXpsOMVisualCollection(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('94d8abde-ab91-46a8-82-b7-f5-b0-5e-f0-1a-96')
    @commethod(3)
    def GetCount(count: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(index: UInt32, object: POINTER(win32more.Storage.Xps.IXpsOMVisual_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def InsertAt(index: UInt32, object: win32more.Storage.Xps.IXpsOMVisual_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveAt(index: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetAt(index: UInt32, object: win32more.Storage.Xps.IXpsOMVisual_head) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Append(object: win32more.Storage.Xps.IXpsOMVisual_head) -> win32more.Foundation.HRESULT: ...
class IXpsSignature(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('6ae4c93e-1ade-42fb-89-8b-3a-56-58-28-48-57')
    @commethod(3)
    def GetSignatureId(sigId: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetSignatureValue(signatureHashValue: POINTER(c_char_p_no), count: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetCertificateEnumerator(certificateEnumerator: POINTER(win32more.Storage.Packaging.Opc.IOpcCertificateEnumerator_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetSigningTime(sigDateTimeString: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetSigningTimeFormat(timeFormat: POINTER(win32more.Storage.Packaging.Opc.OPC_SIGNATURE_TIME_FORMAT)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetSignaturePartName(signaturePartName: POINTER(win32more.Storage.Packaging.Opc.IOpcPartUri_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def Verify(x509Certificate: POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head), sigStatus: POINTER(win32more.Storage.Xps.XPS_SIGNATURE_STATUS)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetPolicy(policy: POINTER(win32more.Storage.Xps.XPS_SIGN_POLICY)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetCustomObjectEnumerator(customObjectEnumerator: POINTER(win32more.Storage.Packaging.Opc.IOpcSignatureCustomObjectEnumerator_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetCustomReferenceEnumerator(customReferenceEnumerator: POINTER(win32more.Storage.Packaging.Opc.IOpcSignatureReferenceEnumerator_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetSignatureXml(signatureXml: POINTER(c_char_p_no), count: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def SetSignatureXml(signatureXml: c_char_p_no, count: UInt32) -> win32more.Foundation.HRESULT: ...
class IXpsSignatureBlock(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('151fac09-0b97-4ac6-a3-23-5e-42-97-d4-32-2b')
    @commethod(3)
    def GetRequests(requests: POINTER(win32more.Storage.Xps.IXpsSignatureRequestCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetPartName(partName: POINTER(win32more.Storage.Packaging.Opc.IOpcPartUri_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetDocumentIndex(fixedDocumentIndex: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetDocumentName(fixedDocumentName: POINTER(win32more.Storage.Packaging.Opc.IOpcPartUri_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def CreateRequest(requestId: win32more.Foundation.PWSTR, signatureRequest: POINTER(win32more.Storage.Xps.IXpsSignatureRequest_head)) -> win32more.Foundation.HRESULT: ...
class IXpsSignatureBlockCollection(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('23397050-fe99-467a-8d-ce-92-37-f0-74-ff-e4')
    @commethod(3)
    def GetCount(count: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(index: UInt32, signatureBlock: POINTER(win32more.Storage.Xps.IXpsSignatureBlock_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def RemoveAt(index: UInt32) -> win32more.Foundation.HRESULT: ...
class IXpsSignatureCollection(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('a2d1d95d-add2-4dff-ab-27-6b-9c-64-5f-f3-22')
    @commethod(3)
    def GetCount(count: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(index: UInt32, signature: POINTER(win32more.Storage.Xps.IXpsSignature_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def RemoveAt(index: UInt32) -> win32more.Foundation.HRESULT: ...
class IXpsSignatureManager(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('d3e8d338-fdc4-4afc-80-b5-d5-32-a1-78-2e-e1')
    @commethod(3)
    def LoadPackageFile(fileName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def LoadPackageStream(stream: win32more.System.Com.IStream_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Sign(signOptions: win32more.Storage.Xps.IXpsSigningOptions_head, x509Certificate: POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head), signature: POINTER(win32more.Storage.Xps.IXpsSignature_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetSignatureOriginPartName(signatureOriginPartName: POINTER(win32more.Storage.Packaging.Opc.IOpcPartUri_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetSignatureOriginPartName(signatureOriginPartName: win32more.Storage.Packaging.Opc.IOpcPartUri_head) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetSignatures(signatures: POINTER(win32more.Storage.Xps.IXpsSignatureCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def AddSignatureBlock(partName: win32more.Storage.Packaging.Opc.IOpcPartUri_head, fixedDocumentIndex: UInt32, signatureBlock: POINTER(win32more.Storage.Xps.IXpsSignatureBlock_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetSignatureBlocks(signatureBlocks: POINTER(win32more.Storage.Xps.IXpsSignatureBlockCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def CreateSigningOptions(signingOptions: POINTER(win32more.Storage.Xps.IXpsSigningOptions_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def SavePackageToFile(fileName: win32more.Foundation.PWSTR, securityAttributes: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), flagsAndAttributes: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def SavePackageToStream(stream: win32more.System.Com.IStream_head) -> win32more.Foundation.HRESULT: ...
class IXpsSignatureRequest(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ac58950b-7208-4b2d-b2-c4-95-10-83-d3-b8-eb')
    @commethod(3)
    def GetIntent(intent: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetIntent(intent: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetRequestedSigner(signerName: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetRequestedSigner(signerName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetRequestSignByDate(dateString: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetRequestSignByDate(dateString: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetSigningLocale(place: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetSigningLocale(place: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetSpotLocation(pageIndex: POINTER(Int32), pagePartName: POINTER(win32more.Storage.Packaging.Opc.IOpcPartUri_head), x: POINTER(Single), y: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def SetSpotLocation(pageIndex: Int32, x: Single, y: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetRequestId(requestId: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetSignature(signature: POINTER(win32more.Storage.Xps.IXpsSignature_head)) -> win32more.Foundation.HRESULT: ...
class IXpsSignatureRequestCollection(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('f0253e68-9f19-412e-9b-4f-54-d3-b0-ac-6c-d9')
    @commethod(3)
    def GetCount(count: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(index: UInt32, signatureRequest: POINTER(win32more.Storage.Xps.IXpsSignatureRequest_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def RemoveAt(index: UInt32) -> win32more.Foundation.HRESULT: ...
class IXpsSigningOptions(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('7718eae4-3215-49be-af-5b-59-4f-ef-7f-cf-a6')
    @commethod(3)
    def GetSignatureId(signatureId: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetSignatureId(signatureId: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetSignatureMethod(signatureMethod: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetSignatureMethod(signatureMethod: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetDigestMethod(digestMethod: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetDigestMethod(digestMethod: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetSignaturePartName(signaturePartName: POINTER(win32more.Storage.Packaging.Opc.IOpcPartUri_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetSignaturePartName(signaturePartName: win32more.Storage.Packaging.Opc.IOpcPartUri_head) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetPolicy(policy: POINTER(win32more.Storage.Xps.XPS_SIGN_POLICY)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def SetPolicy(policy: win32more.Storage.Xps.XPS_SIGN_POLICY) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetSigningTimeFormat(timeFormat: POINTER(win32more.Storage.Packaging.Opc.OPC_SIGNATURE_TIME_FORMAT)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def SetSigningTimeFormat(timeFormat: win32more.Storage.Packaging.Opc.OPC_SIGNATURE_TIME_FORMAT) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetCustomObjects(customObjectSet: POINTER(win32more.Storage.Packaging.Opc.IOpcSignatureCustomObjectSet_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def GetCustomReferences(customReferenceSet: POINTER(win32more.Storage.Packaging.Opc.IOpcSignatureReferenceSet_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def GetCertificateSet(certificateSet: POINTER(win32more.Storage.Packaging.Opc.IOpcCertificateSet_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def GetFlags(flags: POINTER(win32more.Storage.Xps.XPS_SIGN_FLAGS)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def SetFlags(flags: win32more.Storage.Xps.XPS_SIGN_FLAGS) -> win32more.Foundation.HRESULT: ...
PRINT_WINDOW_FLAGS = UInt32
PW_CLIENTONLY: PRINT_WINDOW_FLAGS = 1
class PSFEATURE_CUSTPAPER(Structure):
    lOrientation: Int32
    lWidth: Int32
    lHeight: Int32
    lWidthOffset: Int32
    lHeightOffset: Int32
class PSFEATURE_OUTPUT(Structure):
    bPageIndependent: win32more.Foundation.BOOL
    bSetPageDevice: win32more.Foundation.BOOL
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
class PSINJECTDATA(Structure):
    DataBytes: UInt32
    InjectionPoint: win32more.Storage.Xps.PSINJECT_POINT
    PageNumber: UInt16
class XPS_COLOR(Structure):
    colorType: win32more.Storage.Xps.XPS_COLOR_TYPE
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
XPS_SIGNATURE_STATUS = Int32
XPS_SIGNATURE_STATUS_INCOMPLIANT: XPS_SIGNATURE_STATUS = 1
XPS_SIGNATURE_STATUS_INCOMPLETE: XPS_SIGNATURE_STATUS = 2
XPS_SIGNATURE_STATUS_BROKEN: XPS_SIGNATURE_STATUS = 3
XPS_SIGNATURE_STATUS_QUESTIONABLE: XPS_SIGNATURE_STATUS = 4
XPS_SIGNATURE_STATUS_VALID: XPS_SIGNATURE_STATUS = 5
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
