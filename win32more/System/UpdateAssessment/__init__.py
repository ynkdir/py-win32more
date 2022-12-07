from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.System.Com
import win32more.System.UpdateAssessment
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
class IWaaSAssessor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('2347bbef-1a3b-45a4-90-2d-3e-09-c2-69-b4-5e')
    @commethod(3)
    def GetOSUpdateAssessment(result: POINTER(win32more.System.UpdateAssessment.OSUpdateAssessment_head)) -> win32more.Foundation.HRESULT: ...
class OSUpdateAssessment(Structure):
    isEndOfSupport: win32more.Foundation.BOOL
    assessmentForCurrent: win32more.System.UpdateAssessment.UpdateAssessment
    assessmentForUpToDate: win32more.System.UpdateAssessment.UpdateAssessment
    securityStatus: win32more.System.UpdateAssessment.UpdateAssessmentStatus
    assessmentTime: win32more.Foundation.FILETIME
    releaseInfoTime: win32more.Foundation.FILETIME
    currentOSBuild: win32more.Foundation.PWSTR
    currentOSReleaseTime: win32more.Foundation.FILETIME
    upToDateOSBuild: win32more.Foundation.PWSTR
    upToDateOSReleaseTime: win32more.Foundation.FILETIME
class UpdateAssessment(Structure):
    status: win32more.System.UpdateAssessment.UpdateAssessmentStatus
    impact: win32more.System.UpdateAssessment.UpdateImpactLevel
    daysOutOfDate: UInt32
UpdateAssessmentStatus = Int32
UpdateAssessmentStatus_Latest: UpdateAssessmentStatus = 0
UpdateAssessmentStatus_NotLatestSoftRestriction: UpdateAssessmentStatus = 1
UpdateAssessmentStatus_NotLatestHardRestriction: UpdateAssessmentStatus = 2
UpdateAssessmentStatus_NotLatestEndOfSupport: UpdateAssessmentStatus = 3
UpdateAssessmentStatus_NotLatestServicingTrain: UpdateAssessmentStatus = 4
UpdateAssessmentStatus_NotLatestDeferredFeature: UpdateAssessmentStatus = 5
UpdateAssessmentStatus_NotLatestDeferredQuality: UpdateAssessmentStatus = 6
UpdateAssessmentStatus_NotLatestPausedFeature: UpdateAssessmentStatus = 7
UpdateAssessmentStatus_NotLatestPausedQuality: UpdateAssessmentStatus = 8
UpdateAssessmentStatus_NotLatestManaged: UpdateAssessmentStatus = 9
UpdateAssessmentStatus_NotLatestUnknown: UpdateAssessmentStatus = 10
UpdateAssessmentStatus_NotLatestTargetedVersion: UpdateAssessmentStatus = 11
UpdateImpactLevel = Int32
UpdateImpactLevel_None: UpdateImpactLevel = 0
UpdateImpactLevel_Low: UpdateImpactLevel = 1
UpdateImpactLevel_Medium: UpdateImpactLevel = 2
UpdateImpactLevel_High: UpdateImpactLevel = 3
WaaSAssessor = Guid('098ef871-fa9f-46af-89-58-c0-83-51-5d-7c-9c')
make_head(_module, 'IWaaSAssessor')
make_head(_module, 'OSUpdateAssessment')
make_head(_module, 'UpdateAssessment')
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
