from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.UpdateAssessment
class IWaaSAssessor(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2347bbef-1a3b-45a4-902d-3e09c269b45e}')
    @commethod(3)
    def GetOSUpdateAssessment(self, result: POINTER(win32more.Windows.Win32.System.UpdateAssessment.OSUpdateAssessment)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class OSUpdateAssessment(Structure):
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
class UpdateAssessment(Structure):
    status: win32more.Windows.Win32.System.UpdateAssessment.UpdateAssessmentStatus
    impact: win32more.Windows.Win32.System.UpdateAssessment.UpdateImpactLevel
    daysOutOfDate: UInt32
UpdateAssessmentStatus = Int32
UpdateAssessmentStatus_Latest: win32more.Windows.Win32.System.UpdateAssessment.UpdateAssessmentStatus = 0
UpdateAssessmentStatus_NotLatestSoftRestriction: win32more.Windows.Win32.System.UpdateAssessment.UpdateAssessmentStatus = 1
UpdateAssessmentStatus_NotLatestHardRestriction: win32more.Windows.Win32.System.UpdateAssessment.UpdateAssessmentStatus = 2
UpdateAssessmentStatus_NotLatestEndOfSupport: win32more.Windows.Win32.System.UpdateAssessment.UpdateAssessmentStatus = 3
UpdateAssessmentStatus_NotLatestServicingTrain: win32more.Windows.Win32.System.UpdateAssessment.UpdateAssessmentStatus = 4
UpdateAssessmentStatus_NotLatestDeferredFeature: win32more.Windows.Win32.System.UpdateAssessment.UpdateAssessmentStatus = 5
UpdateAssessmentStatus_NotLatestDeferredQuality: win32more.Windows.Win32.System.UpdateAssessment.UpdateAssessmentStatus = 6
UpdateAssessmentStatus_NotLatestPausedFeature: win32more.Windows.Win32.System.UpdateAssessment.UpdateAssessmentStatus = 7
UpdateAssessmentStatus_NotLatestPausedQuality: win32more.Windows.Win32.System.UpdateAssessment.UpdateAssessmentStatus = 8
UpdateAssessmentStatus_NotLatestManaged: win32more.Windows.Win32.System.UpdateAssessment.UpdateAssessmentStatus = 9
UpdateAssessmentStatus_NotLatestUnknown: win32more.Windows.Win32.System.UpdateAssessment.UpdateAssessmentStatus = 10
UpdateAssessmentStatus_NotLatestTargetedVersion: win32more.Windows.Win32.System.UpdateAssessment.UpdateAssessmentStatus = 11
UpdateImpactLevel = Int32
UpdateImpactLevel_None: win32more.Windows.Win32.System.UpdateAssessment.UpdateImpactLevel = 0
UpdateImpactLevel_Low: win32more.Windows.Win32.System.UpdateAssessment.UpdateImpactLevel = 1
UpdateImpactLevel_Medium: win32more.Windows.Win32.System.UpdateAssessment.UpdateImpactLevel = 2
UpdateImpactLevel_High: win32more.Windows.Win32.System.UpdateAssessment.UpdateImpactLevel = 3
WaaSAssessor = Guid('{098ef871-fa9f-46af-8958-c083515d7c9c}')


make_ready(__name__)
