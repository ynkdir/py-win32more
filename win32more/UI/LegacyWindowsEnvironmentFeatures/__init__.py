from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.System.Com
import win32more.System.Com.StructuredStorage
import win32more.System.Ole
import win32more.System.Registry
import win32more.UI.LegacyWindowsEnvironmentFeatures
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
EVCCBF_LASTNOTIFICATION: UInt32 = 1
STATEBITS_FLAT: UInt32 = 1
REC_S_IDIDTHEUPDATES: win32more.Foundation.HRESULT = 266240
REC_S_NOTCOMPLETE: win32more.Foundation.HRESULT = 266241
REC_S_NOTCOMPLETEBUTPROPAGATE: win32more.Foundation.HRESULT = 266242
REC_E_ABORTED: win32more.Foundation.HRESULT = -2147217408
REC_E_NOCALLBACK: win32more.Foundation.HRESULT = -2147217407
REC_E_NORESIDUES: win32more.Foundation.HRESULT = -2147217406
REC_E_TOODIFFERENT: win32more.Foundation.HRESULT = -2147217405
REC_E_INEEDTODOTHEUPDATES: win32more.Foundation.HRESULT = -2147217404
EMPTY_VOLUME_CACHE_FLAGS = UInt32
EVCF_HASSETTINGS: EMPTY_VOLUME_CACHE_FLAGS = 1
EVCF_ENABLEBYDEFAULT: EMPTY_VOLUME_CACHE_FLAGS = 2
EVCF_REMOVEFROMLIST: EMPTY_VOLUME_CACHE_FLAGS = 4
EVCF_ENABLEBYDEFAULT_AUTO: EMPTY_VOLUME_CACHE_FLAGS = 8
EVCF_DONTSHOWIFZERO: EMPTY_VOLUME_CACHE_FLAGS = 16
EVCF_SETTINGSMODE: EMPTY_VOLUME_CACHE_FLAGS = 32
EVCF_OUTOFDISKSPACE: EMPTY_VOLUME_CACHE_FLAGS = 64
EVCF_USERCONSENTOBTAINED: EMPTY_VOLUME_CACHE_FLAGS = 128
EVCF_SYSTEMAUTORUN: EMPTY_VOLUME_CACHE_FLAGS = 256
class IActiveDesktopP(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('52502ee0-ec80-11d0-89-ab-00-c0-4f-c2-97-2d')
    @commethod(3)
    def SetSafeMode(dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def EnsureUpdateHTML() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetScheme(pwszSchemeName: win32more.Foundation.PWSTR, dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetScheme(pwszSchemeName: win32more.Foundation.PWSTR, pdwcchBuffer: POINTER(UInt32), dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
class IADesktopP2(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('b22754e2-4574-11d1-98-88-00-60-97-de-ac-f9')
    @commethod(3)
    def ReReadWallpaper() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetADObjectFlags(pdwFlags: POINTER(UInt32), dwMask: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def UpdateAllDesktopSubscriptions() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def MakeDynamicChanges(pOleObj: win32more.System.Ole.IOleObject_head) -> win32more.Foundation.HRESULT: ...
class IBriefcaseInitiator(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('99180164-da16-101a-93-5c-44-45-53-54-00-00')
    @commethod(3)
    def IsMonikerInBriefcase(pmk: win32more.System.Com.IMoniker_head) -> win32more.Foundation.HRESULT: ...
class IEmptyVolumeCache(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('8fce5227-04da-11d1-a0-04-00-80-5f-8a-be-06')
    @commethod(3)
    def Initialize(hkRegKey: win32more.System.Registry.HKEY, pcwszVolume: win32more.Foundation.PWSTR, ppwszDisplayName: POINTER(win32more.Foundation.PWSTR), ppwszDescription: POINTER(win32more.Foundation.PWSTR), pdwFlags: POINTER(win32more.UI.LegacyWindowsEnvironmentFeatures.EMPTY_VOLUME_CACHE_FLAGS)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetSpaceUsed(pdwlSpaceUsed: POINTER(UInt64), picb: win32more.UI.LegacyWindowsEnvironmentFeatures.IEmptyVolumeCacheCallBack_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Purge(dwlSpaceToFree: UInt64, picb: win32more.UI.LegacyWindowsEnvironmentFeatures.IEmptyVolumeCacheCallBack_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def ShowProperties(hwnd: win32more.Foundation.HWND) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def Deactivate(pdwFlags: POINTER(win32more.UI.LegacyWindowsEnvironmentFeatures.EMPTY_VOLUME_CACHE_FLAGS)) -> win32more.Foundation.HRESULT: ...
class IEmptyVolumeCache2(c_void_p):
    extends: win32more.UI.LegacyWindowsEnvironmentFeatures.IEmptyVolumeCache
    Guid = Guid('02b7e3ba-4db3-11d2-b2-d9-00-c0-4f-8e-ec-8c')
    @commethod(8)
    def InitializeEx(hkRegKey: win32more.System.Registry.HKEY, pcwszVolume: win32more.Foundation.PWSTR, pcwszKeyName: win32more.Foundation.PWSTR, ppwszDisplayName: POINTER(win32more.Foundation.PWSTR), ppwszDescription: POINTER(win32more.Foundation.PWSTR), ppwszBtnText: POINTER(win32more.Foundation.PWSTR), pdwFlags: POINTER(win32more.UI.LegacyWindowsEnvironmentFeatures.EMPTY_VOLUME_CACHE_FLAGS)) -> win32more.Foundation.HRESULT: ...
class IEmptyVolumeCacheCallBack(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('6e793361-73c6-11d0-84-69-00-aa-00-44-29-01')
    @commethod(3)
    def ScanProgress(dwlSpaceUsed: UInt64, dwFlags: UInt32, pcwszStatus: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def PurgeProgress(dwlSpaceFreed: UInt64, dwlSpaceToFree: UInt64, dwFlags: UInt32, pcwszStatus: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
class IReconcilableObject(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('99180162-da16-101a-93-5c-44-45-53-54-00-00')
    @commethod(3)
    def Reconcile(pInitiator: win32more.UI.LegacyWindowsEnvironmentFeatures.IReconcileInitiator_head, dwFlags: UInt32, hwndOwner: win32more.Foundation.HWND, hwndProgressFeedback: win32more.Foundation.HWND, ulcInput: UInt32, rgpmkOtherInput: POINTER(win32more.System.Com.IMoniker_head), plOutIndex: POINTER(Int32), pstgNewResidues: win32more.System.Com.StructuredStorage.IStorage_head, pvReserved: c_void_p) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetProgressFeedbackMaxEstimate(pulProgressMax: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IReconcileInitiator(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('99180161-da16-101a-93-5c-44-45-53-54-00-00')
    @commethod(3)
    def SetAbortCallback(punkForAbort: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetProgressFeedback(ulProgress: UInt32, ulProgressMax: UInt32) -> win32more.Foundation.HRESULT: ...
RECONCILEF = Int32
RECONCILEF_MAYBOTHERUSER: RECONCILEF = 1
RECONCILEF_FEEDBACKWINDOWVALID: RECONCILEF = 2
RECONCILEF_NORESIDUESOK: RECONCILEF = 4
RECONCILEF_OMITSELFRESIDUE: RECONCILEF = 8
RECONCILEF_RESUMERECONCILIATION: RECONCILEF = 16
RECONCILEF_YOUMAYDOTHEUPDATES: RECONCILEF = 32
RECONCILEF_ONLYYOUWERECHANGED: RECONCILEF = 64
ALL_RECONCILE_FLAGS: RECONCILEF = 127
make_head(_module, 'IActiveDesktopP')
make_head(_module, 'IADesktopP2')
make_head(_module, 'IBriefcaseInitiator')
make_head(_module, 'IEmptyVolumeCache')
make_head(_module, 'IEmptyVolumeCache2')
make_head(_module, 'IEmptyVolumeCacheCallBack')
make_head(_module, 'IReconcilableObject')
make_head(_module, 'IReconcileInitiator')
__all__ = [
    "ALL_RECONCILE_FLAGS",
    "EMPTY_VOLUME_CACHE_FLAGS",
    "EVCCBF_LASTNOTIFICATION",
    "EVCF_DONTSHOWIFZERO",
    "EVCF_ENABLEBYDEFAULT",
    "EVCF_ENABLEBYDEFAULT_AUTO",
    "EVCF_HASSETTINGS",
    "EVCF_OUTOFDISKSPACE",
    "EVCF_REMOVEFROMLIST",
    "EVCF_SETTINGSMODE",
    "EVCF_SYSTEMAUTORUN",
    "EVCF_USERCONSENTOBTAINED",
    "IADesktopP2",
    "IActiveDesktopP",
    "IBriefcaseInitiator",
    "IEmptyVolumeCache",
    "IEmptyVolumeCache2",
    "IEmptyVolumeCacheCallBack",
    "IReconcilableObject",
    "IReconcileInitiator",
    "RECONCILEF",
    "RECONCILEF_FEEDBACKWINDOWVALID",
    "RECONCILEF_MAYBOTHERUSER",
    "RECONCILEF_NORESIDUESOK",
    "RECONCILEF_OMITSELFRESIDUE",
    "RECONCILEF_ONLYYOUWERECHANGED",
    "RECONCILEF_RESUMERECONCILIATION",
    "RECONCILEF_YOUMAYDOTHEUPDATES",
    "REC_E_ABORTED",
    "REC_E_INEEDTODOTHEUPDATES",
    "REC_E_NOCALLBACK",
    "REC_E_NORESIDUES",
    "REC_E_TOODIFFERENT",
    "REC_S_IDIDTHEUPDATES",
    "REC_S_NOTCOMPLETE",
    "REC_S_NOTCOMPLETEBUTPROPAGATE",
    "STATEBITS_FLAT",
]
_arch_optional = [
]
