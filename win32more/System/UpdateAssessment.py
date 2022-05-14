from win32more import *
import win32more.System.UpdateAssessment
import win32more.Foundation
import win32more.System.Com

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.System.UpdateAssessment, name, eval(f"_define_{name}()"))
    return getattr(win32more.System.UpdateAssessment, name)
WaaSAssessor = Guid('098ef871-fa9f-46af-8958-c083515d7c9c')
UpdateImpactLevel = Int32
UpdateImpactLevel_None = 0
UpdateImpactLevel_Low = 1
UpdateImpactLevel_Medium = 2
UpdateImpactLevel_High = 3
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
def _define_UpdateAssessment_head():
    class UpdateAssessment(Structure):
        pass
    return UpdateAssessment
def _define_UpdateAssessment():
    UpdateAssessment = win32more.System.UpdateAssessment.UpdateAssessment_head
    UpdateAssessment._fields_ = [
        ("status", win32more.System.UpdateAssessment.UpdateAssessmentStatus),
        ("impact", win32more.System.UpdateAssessment.UpdateImpactLevel),
        ("daysOutOfDate", UInt32),
    ]
    return UpdateAssessment
def _define_OSUpdateAssessment_head():
    class OSUpdateAssessment(Structure):
        pass
    return OSUpdateAssessment
def _define_OSUpdateAssessment():
    OSUpdateAssessment = win32more.System.UpdateAssessment.OSUpdateAssessment_head
    OSUpdateAssessment._fields_ = [
        ("isEndOfSupport", win32more.Foundation.BOOL),
        ("assessmentForCurrent", win32more.System.UpdateAssessment.UpdateAssessment),
        ("assessmentForUpToDate", win32more.System.UpdateAssessment.UpdateAssessment),
        ("securityStatus", win32more.System.UpdateAssessment.UpdateAssessmentStatus),
        ("assessmentTime", win32more.Foundation.FILETIME),
        ("releaseInfoTime", win32more.Foundation.FILETIME),
        ("currentOSBuild", win32more.Foundation.PWSTR),
        ("currentOSReleaseTime", win32more.Foundation.FILETIME),
        ("upToDateOSBuild", win32more.Foundation.PWSTR),
        ("upToDateOSReleaseTime", win32more.Foundation.FILETIME),
    ]
    return OSUpdateAssessment
def _define_IWaaSAssessor_head():
    class IWaaSAssessor(win32more.System.Com.IUnknown_head):
        Guid = Guid('2347bbef-1a3b-45a4-902d-3e09c269b45e')
    return IWaaSAssessor
def _define_IWaaSAssessor():
    IWaaSAssessor = win32more.System.UpdateAssessment.IWaaSAssessor_head
    IWaaSAssessor.GetOSUpdateAssessment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UpdateAssessment.OSUpdateAssessment_head), use_last_error=False)(3, 'GetOSUpdateAssessment', ((1, 'result'),)))
    return IWaaSAssessor
__all__ = [
    "WaaSAssessor",
    "UpdateImpactLevel",
    "UpdateImpactLevel_None",
    "UpdateImpactLevel_Low",
    "UpdateImpactLevel_Medium",
    "UpdateImpactLevel_High",
    "UpdateAssessmentStatus",
    "UpdateAssessmentStatus_Latest",
    "UpdateAssessmentStatus_NotLatestSoftRestriction",
    "UpdateAssessmentStatus_NotLatestHardRestriction",
    "UpdateAssessmentStatus_NotLatestEndOfSupport",
    "UpdateAssessmentStatus_NotLatestServicingTrain",
    "UpdateAssessmentStatus_NotLatestDeferredFeature",
    "UpdateAssessmentStatus_NotLatestDeferredQuality",
    "UpdateAssessmentStatus_NotLatestPausedFeature",
    "UpdateAssessmentStatus_NotLatestPausedQuality",
    "UpdateAssessmentStatus_NotLatestManaged",
    "UpdateAssessmentStatus_NotLatestUnknown",
    "UpdateAssessmentStatus_NotLatestTargetedVersion",
    "UpdateAssessment",
    "OSUpdateAssessment",
    "IWaaSAssessor",
]
