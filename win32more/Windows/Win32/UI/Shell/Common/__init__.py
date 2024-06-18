from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.UI.Shell.Common
PERCEIVEDFLAG_UNDEFINED: UInt32 = 0
PERCEIVEDFLAG_SOFTCODED: UInt32 = 1
PERCEIVEDFLAG_HARDCODED: UInt32 = 2
PERCEIVEDFLAG_NATIVESUPPORT: UInt32 = 4
PERCEIVEDFLAG_GDIPLUS: UInt32 = 16
PERCEIVEDFLAG_WMSDK: UInt32 = 32
PERCEIVEDFLAG_ZIPFOLDER: UInt32 = 64
class COMDLG_FILTERSPEC(Structure):
    pszName: win32more.Windows.Win32.Foundation.PWSTR
    pszSpec: win32more.Windows.Win32.Foundation.PWSTR
DEVICE_SCALE_FACTOR = Int32
DEVICE_SCALE_FACTOR_INVALID: win32more.Windows.Win32.UI.Shell.Common.DEVICE_SCALE_FACTOR = 0
SCALE_100_PERCENT: win32more.Windows.Win32.UI.Shell.Common.DEVICE_SCALE_FACTOR = 100
SCALE_120_PERCENT: win32more.Windows.Win32.UI.Shell.Common.DEVICE_SCALE_FACTOR = 120
SCALE_125_PERCENT: win32more.Windows.Win32.UI.Shell.Common.DEVICE_SCALE_FACTOR = 125
SCALE_140_PERCENT: win32more.Windows.Win32.UI.Shell.Common.DEVICE_SCALE_FACTOR = 140
SCALE_150_PERCENT: win32more.Windows.Win32.UI.Shell.Common.DEVICE_SCALE_FACTOR = 150
SCALE_160_PERCENT: win32more.Windows.Win32.UI.Shell.Common.DEVICE_SCALE_FACTOR = 160
SCALE_175_PERCENT: win32more.Windows.Win32.UI.Shell.Common.DEVICE_SCALE_FACTOR = 175
SCALE_180_PERCENT: win32more.Windows.Win32.UI.Shell.Common.DEVICE_SCALE_FACTOR = 180
SCALE_200_PERCENT: win32more.Windows.Win32.UI.Shell.Common.DEVICE_SCALE_FACTOR = 200
SCALE_225_PERCENT: win32more.Windows.Win32.UI.Shell.Common.DEVICE_SCALE_FACTOR = 225
SCALE_250_PERCENT: win32more.Windows.Win32.UI.Shell.Common.DEVICE_SCALE_FACTOR = 250
SCALE_300_PERCENT: win32more.Windows.Win32.UI.Shell.Common.DEVICE_SCALE_FACTOR = 300
SCALE_350_PERCENT: win32more.Windows.Win32.UI.Shell.Common.DEVICE_SCALE_FACTOR = 350
SCALE_400_PERCENT: win32more.Windows.Win32.UI.Shell.Common.DEVICE_SCALE_FACTOR = 400
SCALE_450_PERCENT: win32more.Windows.Win32.UI.Shell.Common.DEVICE_SCALE_FACTOR = 450
SCALE_500_PERCENT: win32more.Windows.Win32.UI.Shell.Common.DEVICE_SCALE_FACTOR = 500
class IObjectArray(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{92ca9dcd-5622-4bba-a805-5e9f541bd8c9}')
    @commethod(3)
    def GetCount(self, pcObjects: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(self, uiIndex: UInt32, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IObjectCollection(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.Common.IObjectArray
    _iid_ = Guid('{5632b1a4-e38a-400a-928a-d4cd63230295}')
    @commethod(5)
    def AddObject(self, punk: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AddFromArray(self, poaSource: win32more.Windows.Win32.UI.Shell.Common.IObjectArray) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RemoveObjectAt(self, uiIndex: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Clear(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITEMIDLIST(Structure):
    mkid: win32more.Windows.Win32.UI.Shell.Common.SHITEMID
    _pack_ = 1
PERCEIVED = Int32
PERCEIVED_TYPE_FIRST: win32more.Windows.Win32.UI.Shell.Common.PERCEIVED = -3
PERCEIVED_TYPE_CUSTOM: win32more.Windows.Win32.UI.Shell.Common.PERCEIVED = -3
PERCEIVED_TYPE_UNSPECIFIED: win32more.Windows.Win32.UI.Shell.Common.PERCEIVED = -2
PERCEIVED_TYPE_FOLDER: win32more.Windows.Win32.UI.Shell.Common.PERCEIVED = -1
PERCEIVED_TYPE_UNKNOWN: win32more.Windows.Win32.UI.Shell.Common.PERCEIVED = 0
PERCEIVED_TYPE_TEXT: win32more.Windows.Win32.UI.Shell.Common.PERCEIVED = 1
PERCEIVED_TYPE_IMAGE: win32more.Windows.Win32.UI.Shell.Common.PERCEIVED = 2
PERCEIVED_TYPE_AUDIO: win32more.Windows.Win32.UI.Shell.Common.PERCEIVED = 3
PERCEIVED_TYPE_VIDEO: win32more.Windows.Win32.UI.Shell.Common.PERCEIVED = 4
PERCEIVED_TYPE_COMPRESSED: win32more.Windows.Win32.UI.Shell.Common.PERCEIVED = 5
PERCEIVED_TYPE_DOCUMENT: win32more.Windows.Win32.UI.Shell.Common.PERCEIVED = 6
PERCEIVED_TYPE_SYSTEM: win32more.Windows.Win32.UI.Shell.Common.PERCEIVED = 7
PERCEIVED_TYPE_APPLICATION: win32more.Windows.Win32.UI.Shell.Common.PERCEIVED = 8
PERCEIVED_TYPE_GAMEMEDIA: win32more.Windows.Win32.UI.Shell.Common.PERCEIVED = 9
PERCEIVED_TYPE_CONTACTS: win32more.Windows.Win32.UI.Shell.Common.PERCEIVED = 10
PERCEIVED_TYPE_LAST: win32more.Windows.Win32.UI.Shell.Common.PERCEIVED = 10
SHCOLSTATE = Int32
SHCOLSTATE_DEFAULT: win32more.Windows.Win32.UI.Shell.Common.SHCOLSTATE = 0
SHCOLSTATE_TYPE_STR: win32more.Windows.Win32.UI.Shell.Common.SHCOLSTATE = 1
SHCOLSTATE_TYPE_INT: win32more.Windows.Win32.UI.Shell.Common.SHCOLSTATE = 2
SHCOLSTATE_TYPE_DATE: win32more.Windows.Win32.UI.Shell.Common.SHCOLSTATE = 3
SHCOLSTATE_TYPEMASK: win32more.Windows.Win32.UI.Shell.Common.SHCOLSTATE = 15
SHCOLSTATE_ONBYDEFAULT: win32more.Windows.Win32.UI.Shell.Common.SHCOLSTATE = 16
SHCOLSTATE_SLOW: win32more.Windows.Win32.UI.Shell.Common.SHCOLSTATE = 32
SHCOLSTATE_EXTENDED: win32more.Windows.Win32.UI.Shell.Common.SHCOLSTATE = 64
SHCOLSTATE_SECONDARYUI: win32more.Windows.Win32.UI.Shell.Common.SHCOLSTATE = 128
SHCOLSTATE_HIDDEN: win32more.Windows.Win32.UI.Shell.Common.SHCOLSTATE = 256
SHCOLSTATE_PREFER_VARCMP: win32more.Windows.Win32.UI.Shell.Common.SHCOLSTATE = 512
SHCOLSTATE_PREFER_FMTCMP: win32more.Windows.Win32.UI.Shell.Common.SHCOLSTATE = 1024
SHCOLSTATE_NOSORTBYFOLDERNESS: win32more.Windows.Win32.UI.Shell.Common.SHCOLSTATE = 2048
SHCOLSTATE_VIEWONLY: win32more.Windows.Win32.UI.Shell.Common.SHCOLSTATE = 65536
SHCOLSTATE_BATCHREAD: win32more.Windows.Win32.UI.Shell.Common.SHCOLSTATE = 131072
SHCOLSTATE_NO_GROUPBY: win32more.Windows.Win32.UI.Shell.Common.SHCOLSTATE = 262144
SHCOLSTATE_FIXED_WIDTH: win32more.Windows.Win32.UI.Shell.Common.SHCOLSTATE = 4096
SHCOLSTATE_NODPISCALE: win32more.Windows.Win32.UI.Shell.Common.SHCOLSTATE = 8192
SHCOLSTATE_FIXED_RATIO: win32more.Windows.Win32.UI.Shell.Common.SHCOLSTATE = 16384
SHCOLSTATE_DISPLAYMASK: win32more.Windows.Win32.UI.Shell.Common.SHCOLSTATE = 61440
class SHELLDETAILS(Structure):
    fmt: Int32
    cxChar: Int32
    str: win32more.Windows.Win32.UI.Shell.Common.STRRET
    _pack_ = 1
class SHITEMID(Structure):
    cb: UInt16
    abID: Byte * 1
    _pack_ = 1
class STRRET(Structure):
    uType: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        pOleStr: win32more.Windows.Win32.Foundation.PWSTR
        uOffset: UInt32
        cStr: Byte * 260
STRRET_TYPE = Int32
STRRET_WSTR: win32more.Windows.Win32.UI.Shell.Common.STRRET_TYPE = 0
STRRET_OFFSET: win32more.Windows.Win32.UI.Shell.Common.STRRET_TYPE = 1
STRRET_CSTR: win32more.Windows.Win32.UI.Shell.Common.STRRET_TYPE = 2


make_ready(__name__)
