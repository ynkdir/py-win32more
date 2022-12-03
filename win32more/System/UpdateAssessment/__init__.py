from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.Com
import win32more.System.UpdateAssessment
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
def _define_IWaaSAssessor_head():
    class IWaaSAssessor(win32more.System.Com.IUnknown_head):
        Guid = Guid('2347bbef-1a3b-45a4-90-2d-3e-09-c2-69-b4-5e')
    return IWaaSAssessor
def _define_IWaaSAssessor():
    IWaaSAssessor = win32more.System.UpdateAssessment.IWaaSAssessor_head
    IWaaSAssessor.GetOSUpdateAssessment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAssessment.OSUpdateAssessment_head))(3, 'GetOSUpdateAssessment', ((1, 'result'),)))
    win32more.System.Com.IUnknown
    return IWaaSAssessor
def _define_OSUpdateAssessment_head():
    class OSUpdateAssessment(Structure):
        pass
    return OSUpdateAssessment
def _define_OSUpdateAssessment():
    OSUpdateAssessment = win32more.System.UpdateAssessment.OSUpdateAssessment_head
    OSUpdateAssessment._fields_ = [
        ('isEndOfSupport', win32more.Foundation.BOOL),
        ('assessmentForCurrent', win32more.System.UpdateAssessment.UpdateAssessment),
        ('assessmentForUpToDate', win32more.System.UpdateAssessment.UpdateAssessment),
        ('securityStatus', win32more.System.UpdateAssessment.UpdateAssessmentStatus),
        ('assessmentTime', win32more.Foundation.FILETIME),
        ('releaseInfoTime', win32more.Foundation.FILETIME),
        ('currentOSBuild', win32more.Foundation.PWSTR),
        ('currentOSReleaseTime', win32more.Foundation.FILETIME),
        ('upToDateOSBuild', win32more.Foundation.PWSTR),
        ('upToDateOSReleaseTime', win32more.Foundation.FILETIME),
    ]
    return OSUpdateAssessment
def _define_UpdateAssessment_head():
    class UpdateAssessment(Structure):
        pass
    return UpdateAssessment
def _define_UpdateAssessment():
    UpdateAssessment = win32more.System.UpdateAssessment.UpdateAssessment_head
    UpdateAssessment._fields_ = [
        ('status', win32more.System.UpdateAssessment.UpdateAssessmentStatus),
        ('impact', win32more.System.UpdateAssessment.UpdateImpactLevel),
        ('daysOutOfDate', UInt32),
    ]
    return UpdateAssessment
UpdateAssessmentStatus = Int32
UpdateAssessmentStatus_Latest = 0
UpdateAssessmentStatus_NotLatestSoftRestriction = 1
UpdateAssessmentStatus_NotLatestHardRestriction = 2
UpdateAssessmentStatus_NotLatestEndOfSupport = 3
UpdateAssessmentStatus_NotLatestServicingTrain = 4
UpdateAssessmentStatus_NotLatestDeferredFeature = 5
UpdateAssessmentStatus_NotLatestDeferredQuality = 6
UpdateAssessmentStatus_NotLatestPausedFeature = 7
UpdateAssessmentStatus_NotLatestPausedQuality = 8
UpdateAssessmentStatus_NotLatestManaged = 9
UpdateAssessmentStatus_NotLatestUnknown = 10
UpdateAssessmentStatus_NotLatestTargetedVersion = 11
UpdateImpactLevel = Int32
UpdateImpactLevel_None = 0
UpdateImpactLevel_Low = 1
UpdateImpactLevel_Medium = 2
UpdateImpactLevel_High = 3
WaaSAssessor = Guid('098ef871-fa9f-46af-89-58-c0-83-51-5d-7c-9c')
__all__ = [
    "IWaaSAssessor",
    "OSUpdateAssessment",
    "UpdateAssessment",
    "UpdateAssessmentStatus",
    "UpdateAssessmentStatus_Latest",
    "UpdateAssessmentStatus_NotLatestDeferredFeature",
    "UpdateAssessmentStatus_NotLatestDeferredQuality",
    "UpdateAssessmentStatus_NotLatestEndOfSupport",
    "UpdateAssessmentStatus_NotLatestHardRestriction",
    "UpdateAssessmentStatus_NotLatestManaged",
    "UpdateAssessmentStatus_NotLatestPausedFeature",
    "UpdateAssessmentStatus_NotLatestPausedQuality",
    "UpdateAssessmentStatus_NotLatestServicingTrain",
    "UpdateAssessmentStatus_NotLatestSoftRestriction",
    "UpdateAssessmentStatus_NotLatestTargetedVersion",
    "UpdateAssessmentStatus_NotLatestUnknown",
    "UpdateImpactLevel",
    "UpdateImpactLevel_High",
    "UpdateImpactLevel_Low",
    "UpdateImpactLevel_Medium",
    "UpdateImpactLevel_None",
    "WaaSAssessor",
]