from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.UI.Shell.Common
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
PERCEIVEDFLAG_UNDEFINED: UInt32 = 0
PERCEIVEDFLAG_SOFTCODED: UInt32 = 1
PERCEIVEDFLAG_HARDCODED: UInt32 = 2
PERCEIVEDFLAG_NATIVESUPPORT: UInt32 = 4
PERCEIVEDFLAG_GDIPLUS: UInt32 = 16
PERCEIVEDFLAG_WMSDK: UInt32 = 32
PERCEIVEDFLAG_ZIPFOLDER: UInt32 = 64
class COMDLG_FILTERSPEC(EasyCastStructure):
    pszName: win32more.Windows.Win32.Foundation.PWSTR
    pszSpec: win32more.Windows.Win32.Foundation.PWSTR
DEVICE_SCALE_FACTOR = Int32
DEVICE_SCALE_FACTOR_INVALID: DEVICE_SCALE_FACTOR = 0
SCALE_100_PERCENT: DEVICE_SCALE_FACTOR = 100
SCALE_120_PERCENT: DEVICE_SCALE_FACTOR = 120
SCALE_125_PERCENT: DEVICE_SCALE_FACTOR = 125
SCALE_140_PERCENT: DEVICE_SCALE_FACTOR = 140
SCALE_150_PERCENT: DEVICE_SCALE_FACTOR = 150
SCALE_160_PERCENT: DEVICE_SCALE_FACTOR = 160
SCALE_175_PERCENT: DEVICE_SCALE_FACTOR = 175
SCALE_180_PERCENT: DEVICE_SCALE_FACTOR = 180
SCALE_200_PERCENT: DEVICE_SCALE_FACTOR = 200
SCALE_225_PERCENT: DEVICE_SCALE_FACTOR = 225
SCALE_250_PERCENT: DEVICE_SCALE_FACTOR = 250
SCALE_300_PERCENT: DEVICE_SCALE_FACTOR = 300
SCALE_350_PERCENT: DEVICE_SCALE_FACTOR = 350
SCALE_400_PERCENT: DEVICE_SCALE_FACTOR = 400
SCALE_450_PERCENT: DEVICE_SCALE_FACTOR = 450
SCALE_500_PERCENT: DEVICE_SCALE_FACTOR = 500
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
    def AddObject(self, punk: win32more.Windows.Win32.System.Com.IUnknown_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AddFromArray(self, poaSource: win32more.Windows.Win32.UI.Shell.Common.IObjectArray_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RemoveObjectAt(self, uiIndex: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Clear(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITEMIDLIST(EasyCastStructure):
    mkid: win32more.Windows.Win32.UI.Shell.Common.SHITEMID
    _pack_ = 1
PERCEIVED = Int32
PERCEIVED_TYPE_FIRST: PERCEIVED = -3
PERCEIVED_TYPE_CUSTOM: PERCEIVED = -3
PERCEIVED_TYPE_UNSPECIFIED: PERCEIVED = -2
PERCEIVED_TYPE_FOLDER: PERCEIVED = -1
PERCEIVED_TYPE_UNKNOWN: PERCEIVED = 0
PERCEIVED_TYPE_TEXT: PERCEIVED = 1
PERCEIVED_TYPE_IMAGE: PERCEIVED = 2
PERCEIVED_TYPE_AUDIO: PERCEIVED = 3
PERCEIVED_TYPE_VIDEO: PERCEIVED = 4
PERCEIVED_TYPE_COMPRESSED: PERCEIVED = 5
PERCEIVED_TYPE_DOCUMENT: PERCEIVED = 6
PERCEIVED_TYPE_SYSTEM: PERCEIVED = 7
PERCEIVED_TYPE_APPLICATION: PERCEIVED = 8
PERCEIVED_TYPE_GAMEMEDIA: PERCEIVED = 9
PERCEIVED_TYPE_CONTACTS: PERCEIVED = 10
PERCEIVED_TYPE_LAST: PERCEIVED = 10
SHCOLSTATE = Int32
SHCOLSTATE_DEFAULT: SHCOLSTATE = 0
SHCOLSTATE_TYPE_STR: SHCOLSTATE = 1
SHCOLSTATE_TYPE_INT: SHCOLSTATE = 2
SHCOLSTATE_TYPE_DATE: SHCOLSTATE = 3
SHCOLSTATE_TYPEMASK: SHCOLSTATE = 15
SHCOLSTATE_ONBYDEFAULT: SHCOLSTATE = 16
SHCOLSTATE_SLOW: SHCOLSTATE = 32
SHCOLSTATE_EXTENDED: SHCOLSTATE = 64
SHCOLSTATE_SECONDARYUI: SHCOLSTATE = 128
SHCOLSTATE_HIDDEN: SHCOLSTATE = 256
SHCOLSTATE_PREFER_VARCMP: SHCOLSTATE = 512
SHCOLSTATE_PREFER_FMTCMP: SHCOLSTATE = 1024
SHCOLSTATE_NOSORTBYFOLDERNESS: SHCOLSTATE = 2048
SHCOLSTATE_VIEWONLY: SHCOLSTATE = 65536
SHCOLSTATE_BATCHREAD: SHCOLSTATE = 131072
SHCOLSTATE_NO_GROUPBY: SHCOLSTATE = 262144
SHCOLSTATE_FIXED_WIDTH: SHCOLSTATE = 4096
SHCOLSTATE_NODPISCALE: SHCOLSTATE = 8192
SHCOLSTATE_FIXED_RATIO: SHCOLSTATE = 16384
SHCOLSTATE_DISPLAYMASK: SHCOLSTATE = 61440
class SHELLDETAILS(EasyCastStructure):
    fmt: Int32
    cxChar: Int32
    str: win32more.Windows.Win32.UI.Shell.Common.STRRET
    _pack_ = 1
class SHITEMID(EasyCastStructure):
    cb: UInt16
    abID: Byte * 1
    _pack_ = 1
class STRRET(EasyCastStructure):
    uType: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        pOleStr: win32more.Windows.Win32.Foundation.PWSTR
        uOffset: UInt32
        cStr: Byte * 260
STRRET_TYPE = Int32
STRRET_WSTR: STRRET_TYPE = 0
STRRET_OFFSET: STRRET_TYPE = 1
STRRET_CSTR: STRRET_TYPE = 2
make_head(_module, 'COMDLG_FILTERSPEC')
make_head(_module, 'IObjectArray')
make_head(_module, 'IObjectCollection')
make_head(_module, 'ITEMIDLIST')
make_head(_module, 'SHELLDETAILS')
make_head(_module, 'SHITEMID')
make_head(_module, 'STRRET')
