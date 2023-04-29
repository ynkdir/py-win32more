from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.System.Com
import Windows.Win32.System.UpdateAssessment
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IWaaSAssessor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('2347bbef-1a3b-45a4-90-2d-3e-09-c2-69-b4-5e')
    @commethod(3)
    def GetOSUpdateAssessment(self, result: POINTER(Windows.Win32.System.UpdateAssessment.OSUpdateAssessment_head)) -> Windows.Win32.Foundation.HRESULT: ...
class OSUpdateAssessment(EasyCastStructure):
    isEndOfSupport: Windows.Win32.Foundation.BOOL
    assessmentForCurrent: Windows.Win32.System.UpdateAssessment.UpdateAssessment
    assessmentForUpToDate: Windows.Win32.System.UpdateAssessment.UpdateAssessment
    securityStatus: Windows.Win32.System.UpdateAssessment.UpdateAssessmentStatus
    assessmentTime: Windows.Win32.Foundation.FILETIME
    releaseInfoTime: Windows.Win32.Foundation.FILETIME
    currentOSBuild: Windows.Win32.Foundation.PWSTR
    currentOSReleaseTime: Windows.Win32.Foundation.FILETIME
    upToDateOSBuild: Windows.Win32.Foundation.PWSTR
    upToDateOSReleaseTime: Windows.Win32.Foundation.FILETIME
class UpdateAssessment(EasyCastStructure):
    status: Windows.Win32.System.UpdateAssessment.UpdateAssessmentStatus
    impact: Windows.Win32.System.UpdateAssessment.UpdateImpactLevel
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
