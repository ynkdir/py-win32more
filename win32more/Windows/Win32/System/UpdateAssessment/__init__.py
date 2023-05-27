from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.UpdateAssessment
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
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2347bbef-1a3b-45a4-902d-3e09c269b45e}')
    @commethod(3)
    def GetOSUpdateAssessment(self, result: POINTER(win32more.Windows.Win32.System.UpdateAssessment.OSUpdateAssessment_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class OSUpdateAssessment(EasyCastStructure):
    isEndOfSupport: win32more.Windows.Win32.Foundation.BOOL
    assessmentForCurrent: win32more.Windows.Win32.System.UpdateAssessment.UpdateAssessment
    assessmentForUpToDate: win32more.Windows.Win32.System.UpdateAssessment.UpdateAssessment
    securityStatus: win32more.Windows.Win32.System.UpdateAssessment.UpdateAssessmentStatus
    assessmentTime: win32more.Windows.Win32.Foundation.FILETIME
    releaseInfoTime: win32more.Windows.Win32.Foundation.FILETIME
    currentOSBuild: win32more.Windows.Win32.Foundation.PWSTR
    currentOSReleaseTime: win32more.Windows.Win32.Foundation.FILETIME
    upToDateOSBuild: win32more.Windows.Win32.Foundation.PWSTR
    upToDateOSReleaseTime: win32more.Windows.Win32.Foundation.FILETIME
class UpdateAssessment(EasyCastStructure):
    status: win32more.Windows.Win32.System.UpdateAssessment.UpdateAssessmentStatus
    impact: win32more.Windows.Win32.System.UpdateAssessment.UpdateImpactLevel
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
WaaSAssessor = Guid('{098ef871-fa9f-46af-8958-c083515d7c9c}')
make_head(_module, 'IWaaSAssessor')
make_head(_module, 'OSUpdateAssessment')
make_head(_module, 'UpdateAssessment')
