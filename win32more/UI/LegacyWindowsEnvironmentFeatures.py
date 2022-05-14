from win32more import *
import win32more.UI.LegacyWindowsEnvironmentFeatures
import win32more.Foundation
import win32more.System.Com
import win32more.System.Com.StructuredStorage
import win32more.System.Ole
import win32more.System.Registry

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.UI.LegacyWindowsEnvironmentFeatures, name, eval(f"_define_{name}()"))
    return getattr(win32more.UI.LegacyWindowsEnvironmentFeatures, name)
EVCF_HASSETTINGS = 1
EVCF_ENABLEBYDEFAULT = 2
EVCF_REMOVEFROMLIST = 4
EVCF_ENABLEBYDEFAULT_AUTO = 8
EVCF_DONTSHOWIFZERO = 16
EVCF_SETTINGSMODE = 32
EVCF_OUTOFDISKSPACE = 64
EVCF_USERCONSENTOBTAINED = 128
EVCF_SYSTEMAUTORUN = 256
EVCCBF_LASTNOTIFICATION = 1
STATEBITS_FLAT = 1
REC_S_IDIDTHEUPDATES = 266240
REC_S_NOTCOMPLETE = 266241
REC_S_NOTCOMPLETEBUTPROPAGATE = 266242
REC_E_ABORTED = -2147217408
REC_E_NOCALLBACK = -2147217407
REC_E_NORESIDUES = -2147217406
REC_E_TOODIFFERENT = -2147217405
REC_E_INEEDTODOTHEUPDATES = -2147217404
def _define_IEmptyVolumeCacheCallBack_head():
    class IEmptyVolumeCacheCallBack(win32more.System.Com.IUnknown_head):
        Guid = Guid('6e793361-73c6-11d0-8469-00aa00442901')
    return IEmptyVolumeCacheCallBack
def _define_IEmptyVolumeCacheCallBack():
    IEmptyVolumeCacheCallBack = win32more.UI.LegacyWindowsEnvironmentFeatures.IEmptyVolumeCacheCallBack_head
    IEmptyVolumeCacheCallBack.ScanProgress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,UInt32,win32more.Foundation.PWSTR, use_last_error=False)(3, 'ScanProgress', ((1, 'dwlSpaceUsed'),(1, 'dwFlags'),(1, 'pcwszStatus'),)))
    IEmptyVolumeCacheCallBack.PurgeProgress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,UInt64,UInt32,win32more.Foundation.PWSTR, use_last_error=False)(4, 'PurgeProgress', ((1, 'dwlSpaceFreed'),(1, 'dwlSpaceToFree'),(1, 'dwFlags'),(1, 'pcwszStatus'),)))
    return IEmptyVolumeCacheCallBack
def _define_IEmptyVolumeCache_head():
    class IEmptyVolumeCache(win32more.System.Com.IUnknown_head):
        Guid = Guid('8fce5227-04da-11d1-a004-00805f8abe06')
    return IEmptyVolumeCache
def _define_IEmptyVolumeCache():
    IEmptyVolumeCache = win32more.UI.LegacyWindowsEnvironmentFeatures.IEmptyVolumeCache_head
    IEmptyVolumeCache.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Registry.HKEY,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR),POINTER(UInt32), use_last_error=False)(3, 'Initialize', ((1, 'hkRegKey'),(1, 'pcwszVolume'),(1, 'ppwszDisplayName'),(1, 'ppwszDescription'),(1, 'pdwFlags'),)))
    IEmptyVolumeCache.GetSpaceUsed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64),win32more.UI.LegacyWindowsEnvironmentFeatures.IEmptyVolumeCacheCallBack_head, use_last_error=False)(4, 'GetSpaceUsed', ((1, 'pdwlSpaceUsed'),(1, 'picb'),)))
    IEmptyVolumeCache.Purge = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,win32more.UI.LegacyWindowsEnvironmentFeatures.IEmptyVolumeCacheCallBack_head, use_last_error=False)(5, 'Purge', ((1, 'dwlSpaceToFree'),(1, 'picb'),)))
    IEmptyVolumeCache.ShowProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND, use_last_error=False)(6, 'ShowProperties', ((1, 'hwnd'),)))
    IEmptyVolumeCache.Deactivate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(7, 'Deactivate', ((1, 'pdwFlags'),)))
    return IEmptyVolumeCache
def _define_IEmptyVolumeCache2_head():
    class IEmptyVolumeCache2(win32more.UI.LegacyWindowsEnvironmentFeatures.IEmptyVolumeCache_head):
        Guid = Guid('02b7e3ba-4db3-11d2-b2d9-00c04f8eec8c')
    return IEmptyVolumeCache2
def _define_IEmptyVolumeCache2():
    IEmptyVolumeCache2 = win32more.UI.LegacyWindowsEnvironmentFeatures.IEmptyVolumeCache2_head
    IEmptyVolumeCache2.InitializeEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Registry.HKEY,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR),POINTER(UInt32), use_last_error=False)(8, 'InitializeEx', ((1, 'hkRegKey'),(1, 'pcwszVolume'),(1, 'pcwszKeyName'),(1, 'ppwszDisplayName'),(1, 'ppwszDescription'),(1, 'ppwszBtnText'),(1, 'pdwFlags'),)))
    return IEmptyVolumeCache2
def _define_IReconcileInitiator_head():
    class IReconcileInitiator(win32more.System.Com.IUnknown_head):
        Guid = Guid('99180161-da16-101a-935c-444553540000')
    return IReconcileInitiator
def _define_IReconcileInitiator():
    IReconcileInitiator = win32more.UI.LegacyWindowsEnvironmentFeatures.IReconcileInitiator_head
    IReconcileInitiator.SetAbortCallback = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(3, 'SetAbortCallback', ((1, 'punkForAbort'),)))
    IReconcileInitiator.SetProgressFeedback = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(4, 'SetProgressFeedback', ((1, 'ulProgress'),(1, 'ulProgressMax'),)))
    return IReconcileInitiator
_reconcilef = Int32
RECONCILEF_MAYBOTHERUSER = 1
RECONCILEF_FEEDBACKWINDOWVALID = 2
RECONCILEF_NORESIDUESOK = 4
RECONCILEF_OMITSELFRESIDUE = 8
RECONCILEF_RESUMERECONCILIATION = 16
RECONCILEF_YOUMAYDOTHEUPDATES = 32
RECONCILEF_ONLYYOUWERECHANGED = 64
ALL_RECONCILE_FLAGS = 127
def _define_IReconcilableObject_head():
    class IReconcilableObject(win32more.System.Com.IUnknown_head):
        Guid = Guid('99180162-da16-101a-935c-444553540000')
    return IReconcilableObject
def _define_IReconcilableObject():
    IReconcilableObject = win32more.UI.LegacyWindowsEnvironmentFeatures.IReconcilableObject_head
    IReconcilableObject.Reconcile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.LegacyWindowsEnvironmentFeatures.IReconcileInitiator_head,UInt32,win32more.Foundation.HWND,win32more.Foundation.HWND,UInt32,POINTER(win32more.System.Com.IMoniker_head),POINTER(Int32),win32more.System.Com.StructuredStorage.IStorage_head,c_void_p, use_last_error=False)(3, 'Reconcile', ((1, 'pInitiator'),(1, 'dwFlags'),(1, 'hwndOwner'),(1, 'hwndProgressFeedback'),(1, 'ulcInput'),(1, 'rgpmkOtherInput'),(1, 'plOutIndex'),(1, 'pstgNewResidues'),(1, 'pvReserved'),)))
    IReconcilableObject.GetProgressFeedbackMaxEstimate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(4, 'GetProgressFeedbackMaxEstimate', ((1, 'pulProgressMax'),)))
    return IReconcilableObject
def _define_IBriefcaseInitiator_head():
    class IBriefcaseInitiator(win32more.System.Com.IUnknown_head):
        Guid = Guid('99180164-da16-101a-935c-444553540000')
    return IBriefcaseInitiator
def _define_IBriefcaseInitiator():
    IBriefcaseInitiator = win32more.UI.LegacyWindowsEnvironmentFeatures.IBriefcaseInitiator_head
    IBriefcaseInitiator.IsMonikerInBriefcase = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IMoniker_head, use_last_error=False)(3, 'IsMonikerInBriefcase', ((1, 'pmk'),)))
    return IBriefcaseInitiator
def _define_IActiveDesktopP_head():
    class IActiveDesktopP(win32more.System.Com.IUnknown_head):
        Guid = Guid('52502ee0-ec80-11d0-89ab-00c04fc2972d')
    return IActiveDesktopP
def _define_IActiveDesktopP():
    IActiveDesktopP = win32more.UI.LegacyWindowsEnvironmentFeatures.IActiveDesktopP_head
    IActiveDesktopP.SetSafeMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(3, 'SetSafeMode', ((1, 'dwFlags'),)))
    IActiveDesktopP.EnsureUpdateHTML = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'EnsureUpdateHTML', ()))
    IActiveDesktopP.SetScheme = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(5, 'SetScheme', ((1, 'pwszSchemeName'),(1, 'dwFlags'),)))
    IActiveDesktopP.GetScheme = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),POINTER(UInt32),UInt32, use_last_error=False)(6, 'GetScheme', ((1, 'pwszSchemeName'),(1, 'pdwcchBuffer'),(1, 'dwFlags'),)))
    return IActiveDesktopP
def _define_IADesktopP2_head():
    class IADesktopP2(win32more.System.Com.IUnknown_head):
        Guid = Guid('b22754e2-4574-11d1-9888-006097deacf9')
    return IADesktopP2
def _define_IADesktopP2():
    IADesktopP2 = win32more.UI.LegacyWindowsEnvironmentFeatures.IADesktopP2_head
    IADesktopP2.ReReadWallpaper = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'ReReadWallpaper', ()))
    IADesktopP2.GetADObjectFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),UInt32, use_last_error=False)(4, 'GetADObjectFlags', ((1, 'pdwFlags'),(1, 'dwMask'),)))
    IADesktopP2.UpdateAllDesktopSubscriptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'UpdateAllDesktopSubscriptions', ()))
    IADesktopP2.MakeDynamicChanges = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Ole.IOleObject_head, use_last_error=False)(6, 'MakeDynamicChanges', ((1, 'pOleObj'),)))
    return IADesktopP2
__all__ = [
    "EVCF_HASSETTINGS",
    "EVCF_ENABLEBYDEFAULT",
    "EVCF_REMOVEFROMLIST",
    "EVCF_ENABLEBYDEFAULT_AUTO",
    "EVCF_DONTSHOWIFZERO",
    "EVCF_SETTINGSMODE",
    "EVCF_OUTOFDISKSPACE",
    "EVCF_USERCONSENTOBTAINED",
    "EVCF_SYSTEMAUTORUN",
    "EVCCBF_LASTNOTIFICATION",
    "STATEBITS_FLAT",
    "REC_S_IDIDTHEUPDATES",
    "REC_S_NOTCOMPLETE",
    "REC_S_NOTCOMPLETEBUTPROPAGATE",
    "REC_E_ABORTED",
    "REC_E_NOCALLBACK",
    "REC_E_NORESIDUES",
    "REC_E_TOODIFFERENT",
    "REC_E_INEEDTODOTHEUPDATES",
    "IEmptyVolumeCacheCallBack",
    "IEmptyVolumeCache",
    "IEmptyVolumeCache2",
    "IReconcileInitiator",
    "_reconcilef",
    "RECONCILEF_MAYBOTHERUSER",
    "RECONCILEF_FEEDBACKWINDOWVALID",
    "RECONCILEF_NORESIDUESOK",
    "RECONCILEF_OMITSELFRESIDUE",
    "RECONCILEF_RESUMERECONCILIATION",
    "RECONCILEF_YOUMAYDOTHEUPDATES",
    "RECONCILEF_ONLYYOUWERECHANGED",
    "ALL_RECONCILE_FLAGS",
    "IReconcilableObject",
    "IBriefcaseInitiator",
    "IActiveDesktopP",
    "IADesktopP2",
]
