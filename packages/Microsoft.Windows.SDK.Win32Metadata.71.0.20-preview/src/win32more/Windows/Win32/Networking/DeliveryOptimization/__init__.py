from __future__ import annotations
from win32more._prelude import *
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Networking.DeliveryOptimization
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Variant
DecryptionInfo_KeyData: String = 'KeyData'
DecryptionInfo_EncryptionBufferSize: String = 'EncryptionBufferSize'
DecryptionInfo_AlgorithmName: String = 'AlgorithmName'
DecryptionInfo_ChainingMode: String = 'ChainingMode'
IntegrityCheckInfo_PiecesHashFileUrl: String = 'PiecesHashFileUrl'
IntegrityCheckInfo_PiecesHashFileDigest: String = 'PiecesHashFileDigest'
IntegrityCheckInfo_PiecesHashFileDigestAlgorithm: String = 'PiecesHashFileDigestAlgorithm'
IntegrityCheckInfo_HashOfHashes: String = 'HashOfHashes'
DODownloadCostPolicy = Int32
DODownloadCostPolicy_Always: win32more.Windows.Win32.Networking.DeliveryOptimization.DODownloadCostPolicy = 0
DODownloadCostPolicy_Unrestricted: win32more.Windows.Win32.Networking.DeliveryOptimization.DODownloadCostPolicy = 1
DODownloadCostPolicy_Standard: win32more.Windows.Win32.Networking.DeliveryOptimization.DODownloadCostPolicy = 2
DODownloadCostPolicy_NoRoaming: win32more.Windows.Win32.Networking.DeliveryOptimization.DODownloadCostPolicy = 3
DODownloadCostPolicy_NoSurcharge: win32more.Windows.Win32.Networking.DeliveryOptimization.DODownloadCostPolicy = 4
DODownloadCostPolicy_NoCellular: win32more.Windows.Win32.Networking.DeliveryOptimization.DODownloadCostPolicy = 5
DODownloadProperty = Int32
DODownloadProperty_Id: win32more.Windows.Win32.Networking.DeliveryOptimization.DODownloadProperty = 0
DODownloadProperty_Uri: win32more.Windows.Win32.Networking.DeliveryOptimization.DODownloadProperty = 1
DODownloadProperty_ContentId: win32more.Windows.Win32.Networking.DeliveryOptimization.DODownloadProperty = 2
DODownloadProperty_DisplayName: win32more.Windows.Win32.Networking.DeliveryOptimization.DODownloadProperty = 3
DODownloadProperty_LocalPath: win32more.Windows.Win32.Networking.DeliveryOptimization.DODownloadProperty = 4
DODownloadProperty_HttpCustomHeaders: win32more.Windows.Win32.Networking.DeliveryOptimization.DODownloadProperty = 5
DODownloadProperty_CostPolicy: win32more.Windows.Win32.Networking.DeliveryOptimization.DODownloadProperty = 6
DODownloadProperty_SecurityFlags: win32more.Windows.Win32.Networking.DeliveryOptimization.DODownloadProperty = 7
DODownloadProperty_CallbackFreqPercent: win32more.Windows.Win32.Networking.DeliveryOptimization.DODownloadProperty = 8
DODownloadProperty_CallbackFreqSeconds: win32more.Windows.Win32.Networking.DeliveryOptimization.DODownloadProperty = 9
DODownloadProperty_NoProgressTimeoutSeconds: win32more.Windows.Win32.Networking.DeliveryOptimization.DODownloadProperty = 10
DODownloadProperty_ForegroundPriority: win32more.Windows.Win32.Networking.DeliveryOptimization.DODownloadProperty = 11
DODownloadProperty_BlockingMode: win32more.Windows.Win32.Networking.DeliveryOptimization.DODownloadProperty = 12
DODownloadProperty_CallbackInterface: win32more.Windows.Win32.Networking.DeliveryOptimization.DODownloadProperty = 13
DODownloadProperty_StreamInterface: win32more.Windows.Win32.Networking.DeliveryOptimization.DODownloadProperty = 14
DODownloadProperty_SecurityContext: win32more.Windows.Win32.Networking.DeliveryOptimization.DODownloadProperty = 15
DODownloadProperty_NetworkToken: win32more.Windows.Win32.Networking.DeliveryOptimization.DODownloadProperty = 16
DODownloadProperty_CorrelationVector: win32more.Windows.Win32.Networking.DeliveryOptimization.DODownloadProperty = 17
DODownloadProperty_DecryptionInfo: win32more.Windows.Win32.Networking.DeliveryOptimization.DODownloadProperty = 18
DODownloadProperty_IntegrityCheckInfo: win32more.Windows.Win32.Networking.DeliveryOptimization.DODownloadProperty = 19
DODownloadProperty_IntegrityCheckMandatory: win32more.Windows.Win32.Networking.DeliveryOptimization.DODownloadProperty = 20
DODownloadProperty_TotalSizeBytes: win32more.Windows.Win32.Networking.DeliveryOptimization.DODownloadProperty = 21
DODownloadProperty_DisallowOnCellular: win32more.Windows.Win32.Networking.DeliveryOptimization.DODownloadProperty = 22
DODownloadProperty_HttpCustomAuthHeaders: win32more.Windows.Win32.Networking.DeliveryOptimization.DODownloadProperty = 23
DODownloadProperty_HttpAllowSecureToNonSecureRedirect: win32more.Windows.Win32.Networking.DeliveryOptimization.DODownloadProperty = 24
DODownloadProperty_NonVolatile: win32more.Windows.Win32.Networking.DeliveryOptimization.DODownloadProperty = 25
DODownloadProperty_HttpRedirectionTarget: win32more.Windows.Win32.Networking.DeliveryOptimization.DODownloadProperty = 26
DODownloadProperty_HttpResponseHeaders: win32more.Windows.Win32.Networking.DeliveryOptimization.DODownloadProperty = 27
DODownloadProperty_HttpServerIPAddress: win32more.Windows.Win32.Networking.DeliveryOptimization.DODownloadProperty = 28
DODownloadProperty_HttpStatusCode: win32more.Windows.Win32.Networking.DeliveryOptimization.DODownloadProperty = 29
DODownloadState = Int32
DODownloadState_Created: win32more.Windows.Win32.Networking.DeliveryOptimization.DODownloadState = 0
DODownloadState_Transferring: win32more.Windows.Win32.Networking.DeliveryOptimization.DODownloadState = 1
DODownloadState_Transferred: win32more.Windows.Win32.Networking.DeliveryOptimization.DODownloadState = 2
DODownloadState_Finalized: win32more.Windows.Win32.Networking.DeliveryOptimization.DODownloadState = 3
DODownloadState_Aborted: win32more.Windows.Win32.Networking.DeliveryOptimization.DODownloadState = 4
DODownloadState_Paused: win32more.Windows.Win32.Networking.DeliveryOptimization.DODownloadState = 5
class DO_DOWNLOAD_ENUM_CATEGORY(Structure):
    Property: win32more.Windows.Win32.Networking.DeliveryOptimization.DODownloadProperty
    Value: win32more.Windows.Win32.Foundation.PWSTR
class DO_DOWNLOAD_RANGE(Structure):
    Offset: UInt64
    Length: UInt64
class DO_DOWNLOAD_RANGES_INFO(Structure):
    RangeCount: UInt32
    Ranges: FlexibleArray[win32more.Windows.Win32.Networking.DeliveryOptimization.DO_DOWNLOAD_RANGE]
class DO_DOWNLOAD_STATUS(Structure):
    BytesTotal: UInt64
    BytesTransferred: UInt64
    State: win32more.Windows.Win32.Networking.DeliveryOptimization.DODownloadState
    Error: win32more.Windows.Win32.Foundation.HRESULT
    ExtendedError: win32more.Windows.Win32.Foundation.HRESULT
DeliveryOptimization = Guid('{5b99fa76-721c-423c-adac-56d03c8a8007}')
class IDODownload(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fbbd7fc0-c147-4727-a38d-827ef071ee77}')
    @commethod(3)
    def Start(self, ranges: POINTER(win32more.Windows.Win32.Networking.DeliveryOptimization.DO_DOWNLOAD_RANGES_INFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Pause(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Abort(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Finalize(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetStatus(self, status: POINTER(win32more.Windows.Win32.Networking.DeliveryOptimization.DO_DOWNLOAD_STATUS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetProperty(self, propId: win32more.Windows.Win32.Networking.DeliveryOptimization.DODownloadProperty, propVal: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetProperty(self, propId: win32more.Windows.Win32.Networking.DeliveryOptimization.DODownloadProperty, propVal: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDODownloadStatusCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d166e8e3-a90e-4392-8e87-05e996d3747d}')
    @commethod(3)
    def OnStatusChange(self, download: win32more.Windows.Win32.Networking.DeliveryOptimization.IDODownload, status: POINTER(win32more.Windows.Win32.Networking.DeliveryOptimization.DO_DOWNLOAD_STATUS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDOManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{400e2d4a-1431-4c1a-a748-39ca472cfdb1}')
    @commethod(3)
    def CreateDownload(self, download: POINTER(win32more.Windows.Win32.Networking.DeliveryOptimization.IDODownload)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EnumDownloads(self, category: POINTER(win32more.Windows.Win32.Networking.DeliveryOptimization.DO_DOWNLOAD_ENUM_CATEGORY), ppEnum: POINTER(win32more.Windows.Win32.System.Com.IEnumUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...


make_ready(__name__)
