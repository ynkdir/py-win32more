from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.Com
import win32more.UI.Shell.Common
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
PERCEIVEDFLAG_UNDEFINED = 0
PERCEIVEDFLAG_SOFTCODED = 1
PERCEIVEDFLAG_HARDCODED = 2
PERCEIVEDFLAG_NATIVESUPPORT = 4
PERCEIVEDFLAG_GDIPLUS = 16
PERCEIVEDFLAG_WMSDK = 32
PERCEIVEDFLAG_ZIPFOLDER = 64
def _define_COMDLG_FILTERSPEC_head():
    class COMDLG_FILTERSPEC(Structure):
        pass
    return COMDLG_FILTERSPEC
def _define_COMDLG_FILTERSPEC():
    COMDLG_FILTERSPEC = win32more.UI.Shell.Common.COMDLG_FILTERSPEC_head
    COMDLG_FILTERSPEC._fields_ = [
        ('pszName', win32more.Foundation.PWSTR),
        ('pszSpec', win32more.Foundation.PWSTR),
    ]
    return COMDLG_FILTERSPEC
DEVICE_SCALE_FACTOR = Int32
DEVICE_SCALE_FACTOR_INVALID = 0
SCALE_100_PERCENT = 100
SCALE_120_PERCENT = 120
SCALE_125_PERCENT = 125
SCALE_140_PERCENT = 140
SCALE_150_PERCENT = 150
SCALE_160_PERCENT = 160
SCALE_175_PERCENT = 175
SCALE_180_PERCENT = 180
SCALE_200_PERCENT = 200
SCALE_225_PERCENT = 225
SCALE_250_PERCENT = 250
SCALE_300_PERCENT = 300
SCALE_350_PERCENT = 350
SCALE_400_PERCENT = 400
SCALE_450_PERCENT = 450
SCALE_500_PERCENT = 500
def _define_IObjectArray_head():
    class IObjectArray(win32more.System.Com.IUnknown_head):
        Guid = Guid('92ca9dcd-5622-4bba-a8-05-5e-9f-54-1b-d8-c9')
    return IObjectArray
def _define_IObjectArray():
    IObjectArray = win32more.UI.Shell.Common.IObjectArray_head
    IObjectArray.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetCount', ((1, 'pcObjects'),)))
    IObjectArray.GetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(c_void_p))(4, 'GetAt', ((1, 'uiIndex'),(1, 'riid'),(1, 'ppv'),)))
    win32more.System.Com.IUnknown
    return IObjectArray
def _define_IObjectCollection_head():
    class IObjectCollection(win32more.UI.Shell.Common.IObjectArray_head):
        Guid = Guid('5632b1a4-e38a-400a-92-8a-d4-cd-63-23-02-95')
    return IObjectCollection
def _define_IObjectCollection():
    IObjectCollection = win32more.UI.Shell.Common.IObjectCollection_head
    IObjectCollection.AddObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head)(5, 'AddObject', ((1, 'punk'),)))
    IObjectCollection.AddFromArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Shell.Common.IObjectArray_head)(6, 'AddFromArray', ((1, 'poaSource'),)))
    IObjectCollection.RemoveObjectAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(7, 'RemoveObjectAt', ((1, 'uiIndex'),)))
    IObjectCollection.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(8, 'Clear', ()))
    win32more.UI.Shell.Common.IObjectArray
    return IObjectCollection
def _define_ITEMIDLIST_head():
    class ITEMIDLIST(Structure):
        pass
    return ITEMIDLIST
def _define_ITEMIDLIST():
    ITEMIDLIST = win32more.UI.Shell.Common.ITEMIDLIST_head
    ITEMIDLIST._pack_ = 1
    ITEMIDLIST._fields_ = [
        ('mkid', win32more.UI.Shell.Common.SHITEMID),
    ]
    return ITEMIDLIST
PERCEIVED = Int32
PERCEIVED_TYPE_FIRST = -3
PERCEIVED_TYPE_CUSTOM = -3
PERCEIVED_TYPE_UNSPECIFIED = -2
PERCEIVED_TYPE_FOLDER = -1
PERCEIVED_TYPE_UNKNOWN = 0
PERCEIVED_TYPE_TEXT = 1
PERCEIVED_TYPE_IMAGE = 2
PERCEIVED_TYPE_AUDIO = 3
PERCEIVED_TYPE_VIDEO = 4
PERCEIVED_TYPE_COMPRESSED = 5
PERCEIVED_TYPE_DOCUMENT = 6
PERCEIVED_TYPE_SYSTEM = 7
PERCEIVED_TYPE_APPLICATION = 8
PERCEIVED_TYPE_GAMEMEDIA = 9
PERCEIVED_TYPE_CONTACTS = 10
PERCEIVED_TYPE_LAST = 10
SHCOLSTATE = Int32
SHCOLSTATE_DEFAULT = 0
SHCOLSTATE_TYPE_STR = 1
SHCOLSTATE_TYPE_INT = 2
SHCOLSTATE_TYPE_DATE = 3
SHCOLSTATE_TYPEMASK = 15
SHCOLSTATE_ONBYDEFAULT = 16
SHCOLSTATE_SLOW = 32
SHCOLSTATE_EXTENDED = 64
SHCOLSTATE_SECONDARYUI = 128
SHCOLSTATE_HIDDEN = 256
SHCOLSTATE_PREFER_VARCMP = 512
SHCOLSTATE_PREFER_FMTCMP = 1024
SHCOLSTATE_NOSORTBYFOLDERNESS = 2048
SHCOLSTATE_VIEWONLY = 65536
SHCOLSTATE_BATCHREAD = 131072
SHCOLSTATE_NO_GROUPBY = 262144
SHCOLSTATE_FIXED_WIDTH = 4096
SHCOLSTATE_NODPISCALE = 8192
SHCOLSTATE_FIXED_RATIO = 16384
SHCOLSTATE_DISPLAYMASK = 61440
def _define_SHELLDETAILS_head():
    class SHELLDETAILS(Structure):
        pass
    return SHELLDETAILS
def _define_SHELLDETAILS():
    SHELLDETAILS = win32more.UI.Shell.Common.SHELLDETAILS_head
    SHELLDETAILS._pack_ = 1
    SHELLDETAILS._fields_ = [
        ('fmt', Int32),
        ('cxChar', Int32),
        ('str', win32more.UI.Shell.Common.STRRET),
    ]
    return SHELLDETAILS
def _define_SHITEMID_head():
    class SHITEMID(Structure):
        pass
    return SHITEMID
def _define_SHITEMID():
    SHITEMID = win32more.UI.Shell.Common.SHITEMID_head
    SHITEMID._pack_ = 1
    SHITEMID._fields_ = [
        ('cb', UInt16),
        ('abID', Byte * 1),
    ]
    return SHITEMID
def _define_STRRET_head():
    class STRRET(Structure):
        pass
    return STRRET
def _define_STRRET():
    STRRET = win32more.UI.Shell.Common.STRRET_head
    class STRRET__Anonymous_e__Union(Union):
        pass
    STRRET__Anonymous_e__Union._fields_ = [
        ('pOleStr', win32more.Foundation.PWSTR),
        ('uOffset', UInt32),
        ('cStr', Byte * 260),
    ]
    STRRET._anonymous_ = [
        'Anonymous',
    ]
    STRRET._fields_ = [
        ('uType', UInt32),
        ('Anonymous', STRRET__Anonymous_e__Union),
    ]
    return STRRET
STRRET_TYPE = Int32
STRRET_WSTR = 0
STRRET_OFFSET = 1
STRRET_CSTR = 2
__all__ = [
    "COMDLG_FILTERSPEC",
    "DEVICE_SCALE_FACTOR",
    "DEVICE_SCALE_FACTOR_INVALID",
    "IObjectArray",
    "IObjectCollection",
    "ITEMIDLIST",
    "PERCEIVED",
    "PERCEIVEDFLAG_GDIPLUS",
    "PERCEIVEDFLAG_HARDCODED",
    "PERCEIVEDFLAG_NATIVESUPPORT",
    "PERCEIVEDFLAG_SOFTCODED",
    "PERCEIVEDFLAG_UNDEFINED",
    "PERCEIVEDFLAG_WMSDK",
    "PERCEIVEDFLAG_ZIPFOLDER",
    "PERCEIVED_TYPE_APPLICATION",
    "PERCEIVED_TYPE_AUDIO",
    "PERCEIVED_TYPE_COMPRESSED",
    "PERCEIVED_TYPE_CONTACTS",
    "PERCEIVED_TYPE_CUSTOM",
    "PERCEIVED_TYPE_DOCUMENT",
    "PERCEIVED_TYPE_FIRST",
    "PERCEIVED_TYPE_FOLDER",
    "PERCEIVED_TYPE_GAMEMEDIA",
    "PERCEIVED_TYPE_IMAGE",
    "PERCEIVED_TYPE_LAST",
    "PERCEIVED_TYPE_SYSTEM",
    "PERCEIVED_TYPE_TEXT",
    "PERCEIVED_TYPE_UNKNOWN",
    "PERCEIVED_TYPE_UNSPECIFIED",
    "PERCEIVED_TYPE_VIDEO",
    "SCALE_100_PERCENT",
    "SCALE_120_PERCENT",
    "SCALE_125_PERCENT",
    "SCALE_140_PERCENT",
    "SCALE_150_PERCENT",
    "SCALE_160_PERCENT",
    "SCALE_175_PERCENT",
    "SCALE_180_PERCENT",
    "SCALE_200_PERCENT",
    "SCALE_225_PERCENT",
    "SCALE_250_PERCENT",
    "SCALE_300_PERCENT",
    "SCALE_350_PERCENT",
    "SCALE_400_PERCENT",
    "SCALE_450_PERCENT",
    "SCALE_500_PERCENT",
    "SHCOLSTATE",
    "SHCOLSTATE_BATCHREAD",
    "SHCOLSTATE_DEFAULT",
    "SHCOLSTATE_DISPLAYMASK",
    "SHCOLSTATE_EXTENDED",
    "SHCOLSTATE_FIXED_RATIO",
    "SHCOLSTATE_FIXED_WIDTH",
    "SHCOLSTATE_HIDDEN",
    "SHCOLSTATE_NODPISCALE",
    "SHCOLSTATE_NOSORTBYFOLDERNESS",
    "SHCOLSTATE_NO_GROUPBY",
    "SHCOLSTATE_ONBYDEFAULT",
    "SHCOLSTATE_PREFER_FMTCMP",
    "SHCOLSTATE_PREFER_VARCMP",
    "SHCOLSTATE_SECONDARYUI",
    "SHCOLSTATE_SLOW",
    "SHCOLSTATE_TYPEMASK",
    "SHCOLSTATE_TYPE_DATE",
    "SHCOLSTATE_TYPE_INT",
    "SHCOLSTATE_TYPE_STR",
    "SHCOLSTATE_VIEWONLY",
    "SHELLDETAILS",
    "SHITEMID",
    "STRRET",
    "STRRET_CSTR",
    "STRRET_OFFSET",
    "STRRET_TYPE",
    "STRRET_WSTR",
]
