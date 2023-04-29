from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.ApplicationModel.Store.LicenseManagement
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Storage.Streams
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class ILicenseManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('b5ac3ae0-da47-4f20-9a-23-09-18-2c-94-76-ff')
    @winrt_commethod(6)
    def AddLicenseAsync(self, license: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def GetSatisfactionInfosAsync(self, contentIds: Windows.Foundation.Collections.IIterable[WinRT_String], keyIds: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Store.LicenseManagement.LicenseSatisfactionResult]: ...
class ILicenseManagerStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('ab2ec47b-1f79-4480-b8-7e-2c-49-9e-60-1b-a3')
    @winrt_commethod(6)
    def RefreshLicensesAsync(self, refreshOption: Windows.ApplicationModel.Store.LicenseManagement.LicenseRefreshOption) -> Windows.Foundation.IAsyncAction: ...
class ILicenseSatisfactionInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('3ccbb08f-db31-48d5-83-84-fa-17-c8-14-74-e2')
    @winrt_commethod(6)
    def get_SatisfiedByDevice(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_SatisfiedByOpenLicense(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_SatisfiedByTrial(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_SatisfiedByPass(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_SatisfiedByInstallMedia(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_SatisfiedBySignedInUser(self) -> Boolean: ...
    @winrt_commethod(12)
    def get_IsSatisfied(self) -> Boolean: ...
    SatisfiedByDevice = property(get_SatisfiedByDevice, None)
    SatisfiedByOpenLicense = property(get_SatisfiedByOpenLicense, None)
    SatisfiedByTrial = property(get_SatisfiedByTrial, None)
    SatisfiedByPass = property(get_SatisfiedByPass, None)
    SatisfiedByInstallMedia = property(get_SatisfiedByInstallMedia, None)
    SatisfiedBySignedInUser = property(get_SatisfiedBySignedInUser, None)
    IsSatisfied = property(get_IsSatisfied, None)
class ILicenseSatisfactionResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('3c674f73-3c87-4ee1-82-01-f4-28-35-9b-d3-af')
    @winrt_commethod(6)
    def get_LicenseSatisfactionInfos(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.ApplicationModel.Store.LicenseManagement.LicenseSatisfactionInfo]: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    LicenseSatisfactionInfos = property(get_LicenseSatisfactionInfos, None)
    ExtendedError = property(get_ExtendedError, None)
class LicenseManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Store.LicenseManagement.LicenseManager'
    @winrt_classmethod
    def RefreshLicensesAsync(cls: Windows.ApplicationModel.Store.LicenseManagement.ILicenseManagerStatics2, refreshOption: Windows.ApplicationModel.Store.LicenseManagement.LicenseRefreshOption) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def AddLicenseAsync(cls: Windows.ApplicationModel.Store.LicenseManagement.ILicenseManagerStatics, license: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def GetSatisfactionInfosAsync(cls: Windows.ApplicationModel.Store.LicenseManagement.ILicenseManagerStatics, contentIds: Windows.Foundation.Collections.IIterable[WinRT_String], keyIds: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Store.LicenseManagement.LicenseSatisfactionResult]: ...
LicenseRefreshOption = Int32
LicenseRefreshOption_RunningLicenses: LicenseRefreshOption = 0
LicenseRefreshOption_AllLicenses: LicenseRefreshOption = 1
class LicenseSatisfactionInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Store.LicenseManagement.LicenseSatisfactionInfo'
    @winrt_mixinmethod
    def get_SatisfiedByDevice(self: Windows.ApplicationModel.Store.LicenseManagement.ILicenseSatisfactionInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_SatisfiedByOpenLicense(self: Windows.ApplicationModel.Store.LicenseManagement.ILicenseSatisfactionInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_SatisfiedByTrial(self: Windows.ApplicationModel.Store.LicenseManagement.ILicenseSatisfactionInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_SatisfiedByPass(self: Windows.ApplicationModel.Store.LicenseManagement.ILicenseSatisfactionInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_SatisfiedByInstallMedia(self: Windows.ApplicationModel.Store.LicenseManagement.ILicenseSatisfactionInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_SatisfiedBySignedInUser(self: Windows.ApplicationModel.Store.LicenseManagement.ILicenseSatisfactionInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsSatisfied(self: Windows.ApplicationModel.Store.LicenseManagement.ILicenseSatisfactionInfo) -> Boolean: ...
    SatisfiedByDevice = property(get_SatisfiedByDevice, None)
    SatisfiedByOpenLicense = property(get_SatisfiedByOpenLicense, None)
    SatisfiedByTrial = property(get_SatisfiedByTrial, None)
    SatisfiedByPass = property(get_SatisfiedByPass, None)
    SatisfiedByInstallMedia = property(get_SatisfiedByInstallMedia, None)
    SatisfiedBySignedInUser = property(get_SatisfiedBySignedInUser, None)
    IsSatisfied = property(get_IsSatisfied, None)
class LicenseSatisfactionResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Store.LicenseManagement.LicenseSatisfactionResult'
    @winrt_mixinmethod
    def get_LicenseSatisfactionInfos(self: Windows.ApplicationModel.Store.LicenseManagement.ILicenseSatisfactionResult) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.ApplicationModel.Store.LicenseManagement.LicenseSatisfactionInfo]: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.ApplicationModel.Store.LicenseManagement.ILicenseSatisfactionResult) -> Windows.Foundation.HResult: ...
    LicenseSatisfactionInfos = property(get_LicenseSatisfactionInfos, None)
    ExtendedError = property(get_ExtendedError, None)
make_head(_module, 'ILicenseManagerStatics')
make_head(_module, 'ILicenseManagerStatics2')
make_head(_module, 'ILicenseSatisfactionInfo')
make_head(_module, 'ILicenseSatisfactionResult')
make_head(_module, 'LicenseManager')
make_head(_module, 'LicenseSatisfactionInfo')
make_head(_module, 'LicenseSatisfactionResult')
