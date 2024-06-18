from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Com.StructuredStorage
import win32more.Windows.Win32.System.Ole
import win32more.Windows.Win32.System.Registry
import win32more.Windows.Win32.UI.LegacyWindowsEnvironmentFeatures
EVCCBF_LASTNOTIFICATION: UInt32 = 1
STATEBITS_FLAT: UInt32 = 1
REC_S_IDIDTHEUPDATES: win32more.Windows.Win32.Foundation.HRESULT = 266240
REC_S_NOTCOMPLETE: win32more.Windows.Win32.Foundation.HRESULT = 266241
REC_S_NOTCOMPLETEBUTPROPAGATE: win32more.Windows.Win32.Foundation.HRESULT = 266242
REC_E_ABORTED: win32more.Windows.Win32.Foundation.HRESULT = -2147217408
REC_E_NOCALLBACK: win32more.Windows.Win32.Foundation.HRESULT = -2147217407
REC_E_NORESIDUES: win32more.Windows.Win32.Foundation.HRESULT = -2147217406
REC_E_TOODIFFERENT: win32more.Windows.Win32.Foundation.HRESULT = -2147217405
REC_E_INEEDTODOTHEUPDATES: win32more.Windows.Win32.Foundation.HRESULT = -2147217404
EMPTY_VOLUME_CACHE_FLAGS = UInt32
EVCF_HASSETTINGS: win32more.Windows.Win32.UI.LegacyWindowsEnvironmentFeatures.EMPTY_VOLUME_CACHE_FLAGS = 1
EVCF_ENABLEBYDEFAULT: win32more.Windows.Win32.UI.LegacyWindowsEnvironmentFeatures.EMPTY_VOLUME_CACHE_FLAGS = 2
EVCF_REMOVEFROMLIST: win32more.Windows.Win32.UI.LegacyWindowsEnvironmentFeatures.EMPTY_VOLUME_CACHE_FLAGS = 4
EVCF_ENABLEBYDEFAULT_AUTO: win32more.Windows.Win32.UI.LegacyWindowsEnvironmentFeatures.EMPTY_VOLUME_CACHE_FLAGS = 8
EVCF_DONTSHOWIFZERO: win32more.Windows.Win32.UI.LegacyWindowsEnvironmentFeatures.EMPTY_VOLUME_CACHE_FLAGS = 16
EVCF_SETTINGSMODE: win32more.Windows.Win32.UI.LegacyWindowsEnvironmentFeatures.EMPTY_VOLUME_CACHE_FLAGS = 32
EVCF_OUTOFDISKSPACE: win32more.Windows.Win32.UI.LegacyWindowsEnvironmentFeatures.EMPTY_VOLUME_CACHE_FLAGS = 64
EVCF_USERCONSENTOBTAINED: win32more.Windows.Win32.UI.LegacyWindowsEnvironmentFeatures.EMPTY_VOLUME_CACHE_FLAGS = 128
EVCF_SYSTEMAUTORUN: win32more.Windows.Win32.UI.LegacyWindowsEnvironmentFeatures.EMPTY_VOLUME_CACHE_FLAGS = 256
class IADesktopP2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b22754e2-4574-11d1-9888-006097deacf9}')
    @commethod(3)
    def ReReadWallpaper(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetADObjectFlags(self, pdwFlags: POINTER(UInt32), dwMask: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def UpdateAllDesktopSubscriptions(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def MakeDynamicChanges(self, pOleObj: win32more.Windows.Win32.System.Ole.IOleObject) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveDesktopP(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{52502ee0-ec80-11d0-89ab-00c04fc2972d}')
    @commethod(3)
    def SetSafeMode(self, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EnsureUpdateHTML(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetScheme(self, pwszSchemeName: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetScheme(self, pwszSchemeName: win32more.Windows.Win32.Foundation.PWSTR, pdwcchBuffer: POINTER(UInt32), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBriefcaseInitiator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{99180164-da16-101a-935c-444553540000}')
    @commethod(3)
    def IsMonikerInBriefcase(self, pmk: win32more.Windows.Win32.System.Com.IMoniker) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEmptyVolumeCache(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8fce5227-04da-11d1-a004-00805f8abe06}')
    @commethod(3)
    def Initialize(self, hkRegKey: win32more.Windows.Win32.System.Registry.HKEY, pcwszVolume: win32more.Windows.Win32.Foundation.PWSTR, ppwszDisplayName: POINTER(win32more.Windows.Win32.Foundation.PWSTR), ppwszDescription: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pdwFlags: POINTER(win32more.Windows.Win32.UI.LegacyWindowsEnvironmentFeatures.EMPTY_VOLUME_CACHE_FLAGS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSpaceUsed(self, pdwlSpaceUsed: POINTER(UInt64), picb: win32more.Windows.Win32.UI.LegacyWindowsEnvironmentFeatures.IEmptyVolumeCacheCallBack) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Purge(self, dwlSpaceToFree: UInt64, picb: win32more.Windows.Win32.UI.LegacyWindowsEnvironmentFeatures.IEmptyVolumeCacheCallBack) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ShowProperties(self, hwnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Deactivate(self, pdwFlags: POINTER(win32more.Windows.Win32.UI.LegacyWindowsEnvironmentFeatures.EMPTY_VOLUME_CACHE_FLAGS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEmptyVolumeCache2(ComPtr):
    extends: win32more.Windows.Win32.UI.LegacyWindowsEnvironmentFeatures.IEmptyVolumeCache
    _iid_ = Guid('{02b7e3ba-4db3-11d2-b2d9-00c04f8eec8c}')
    @commethod(8)
    def InitializeEx(self, hkRegKey: win32more.Windows.Win32.System.Registry.HKEY, pcwszVolume: win32more.Windows.Win32.Foundation.PWSTR, pcwszKeyName: win32more.Windows.Win32.Foundation.PWSTR, ppwszDisplayName: POINTER(win32more.Windows.Win32.Foundation.PWSTR), ppwszDescription: POINTER(win32more.Windows.Win32.Foundation.PWSTR), ppwszBtnText: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pdwFlags: POINTER(win32more.Windows.Win32.UI.LegacyWindowsEnvironmentFeatures.EMPTY_VOLUME_CACHE_FLAGS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEmptyVolumeCacheCallBack(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6e793361-73c6-11d0-8469-00aa00442901}')
    @commethod(3)
    def ScanProgress(self, dwlSpaceUsed: UInt64, dwFlags: UInt32, pcwszStatus: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def PurgeProgress(self, dwlSpaceFreed: UInt64, dwlSpaceToFree: UInt64, dwFlags: UInt32, pcwszStatus: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IReconcilableObject(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{99180162-da16-101a-935c-444553540000}')
    @commethod(3)
    def Reconcile(self, pInitiator: win32more.Windows.Win32.UI.LegacyWindowsEnvironmentFeatures.IReconcileInitiator, dwFlags: UInt32, hwndOwner: win32more.Windows.Win32.Foundation.HWND, hwndProgressFeedback: win32more.Windows.Win32.Foundation.HWND, ulcInput: UInt32, rgpmkOtherInput: POINTER(win32more.Windows.Win32.System.Com.IMoniker), plOutIndex: POINTER(Int32), pstgNewResidues: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage, pvReserved: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetProgressFeedbackMaxEstimate(self, pulProgressMax: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IReconcileInitiator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{99180161-da16-101a-935c-444553540000}')
    @commethod(3)
    def SetAbortCallback(self, punkForAbort: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetProgressFeedback(self, ulProgress: UInt32, ulProgressMax: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
RECONCILEF = Int32
RECONCILEF_MAYBOTHERUSER: win32more.Windows.Win32.UI.LegacyWindowsEnvironmentFeatures.RECONCILEF = 1
RECONCILEF_FEEDBACKWINDOWVALID: win32more.Windows.Win32.UI.LegacyWindowsEnvironmentFeatures.RECONCILEF = 2
RECONCILEF_NORESIDUESOK: win32more.Windows.Win32.UI.LegacyWindowsEnvironmentFeatures.RECONCILEF = 4
RECONCILEF_OMITSELFRESIDUE: win32more.Windows.Win32.UI.LegacyWindowsEnvironmentFeatures.RECONCILEF = 8
RECONCILEF_RESUMERECONCILIATION: win32more.Windows.Win32.UI.LegacyWindowsEnvironmentFeatures.RECONCILEF = 16
RECONCILEF_YOUMAYDOTHEUPDATES: win32more.Windows.Win32.UI.LegacyWindowsEnvironmentFeatures.RECONCILEF = 32
RECONCILEF_ONLYYOUWERECHANGED: win32more.Windows.Win32.UI.LegacyWindowsEnvironmentFeatures.RECONCILEF = 64
ALL_RECONCILE_FLAGS: win32more.Windows.Win32.UI.LegacyWindowsEnvironmentFeatures.RECONCILEF = 127


make_ready(__name__)
