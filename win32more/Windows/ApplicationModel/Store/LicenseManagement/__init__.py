from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel.Store.LicenseManagement
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Storage.Streams
import win32more.Windows.Win32.System.WinRT
class ILicenseManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.LicenseManagement.ILicenseManagerStatics'
    _iid_ = Guid('{b5ac3ae0-da47-4f20-9a23-09182c9476ff}')
    @winrt_commethod(6)
    def AddLicenseAsync(self, license: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def GetSatisfactionInfosAsync(self, contentIds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], keyIds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Store.LicenseManagement.LicenseSatisfactionResult]: ...
class ILicenseManagerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.LicenseManagement.ILicenseManagerStatics2'
    _iid_ = Guid('{ab2ec47b-1f79-4480-b87e-2c499e601ba3}')
    @winrt_commethod(6)
    def RefreshLicensesAsync(self, refreshOption: win32more.Windows.ApplicationModel.Store.LicenseManagement.LicenseRefreshOption) -> win32more.Windows.Foundation.IAsyncAction: ...
class ILicenseSatisfactionInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.LicenseManagement.ILicenseSatisfactionInfo'
    _iid_ = Guid('{3ccbb08f-db31-48d5-8384-fa17c81474e2}')
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
    IsSatisfied = property(get_IsSatisfied, None)
    SatisfiedByDevice = property(get_SatisfiedByDevice, None)
    SatisfiedByInstallMedia = property(get_SatisfiedByInstallMedia, None)
    SatisfiedByOpenLicense = property(get_SatisfiedByOpenLicense, None)
    SatisfiedByPass = property(get_SatisfiedByPass, None)
    SatisfiedBySignedInUser = property(get_SatisfiedBySignedInUser, None)
    SatisfiedByTrial = property(get_SatisfiedByTrial, None)
class ILicenseSatisfactionResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.LicenseManagement.ILicenseSatisfactionResult'
    _iid_ = Guid('{3c674f73-3c87-4ee1-8201-f428359bd3af}')
    @winrt_commethod(6)
    def get_LicenseSatisfactionInfos(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.ApplicationModel.Store.LicenseManagement.LicenseSatisfactionInfo]: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
    LicenseSatisfactionInfos = property(get_LicenseSatisfactionInfos, None)
class LicenseManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Store.LicenseManagement.LicenseManager'
    @winrt_classmethod
    def RefreshLicensesAsync(cls: win32more.Windows.ApplicationModel.Store.LicenseManagement.ILicenseManagerStatics2, refreshOption: win32more.Windows.ApplicationModel.Store.LicenseManagement.LicenseRefreshOption) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def AddLicenseAsync(cls: win32more.Windows.ApplicationModel.Store.LicenseManagement.ILicenseManagerStatics, license: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def GetSatisfactionInfosAsync(cls: win32more.Windows.ApplicationModel.Store.LicenseManagement.ILicenseManagerStatics, contentIds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String], keyIds: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Store.LicenseManagement.LicenseSatisfactionResult]: ...
class LicenseRefreshOption(Enum, Int32):
    RunningLicenses = 0
    AllLicenses = 1
class LicenseSatisfactionInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Store.LicenseManagement.ILicenseSatisfactionInfo
    _classid_ = 'Windows.ApplicationModel.Store.LicenseManagement.LicenseSatisfactionInfo'
    @winrt_mixinmethod
    def get_SatisfiedByDevice(self: win32more.Windows.ApplicationModel.Store.LicenseManagement.ILicenseSatisfactionInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_SatisfiedByOpenLicense(self: win32more.Windows.ApplicationModel.Store.LicenseManagement.ILicenseSatisfactionInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_SatisfiedByTrial(self: win32more.Windows.ApplicationModel.Store.LicenseManagement.ILicenseSatisfactionInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_SatisfiedByPass(self: win32more.Windows.ApplicationModel.Store.LicenseManagement.ILicenseSatisfactionInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_SatisfiedByInstallMedia(self: win32more.Windows.ApplicationModel.Store.LicenseManagement.ILicenseSatisfactionInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_SatisfiedBySignedInUser(self: win32more.Windows.ApplicationModel.Store.LicenseManagement.ILicenseSatisfactionInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsSatisfied(self: win32more.Windows.ApplicationModel.Store.LicenseManagement.ILicenseSatisfactionInfo) -> Boolean: ...
    IsSatisfied = property(get_IsSatisfied, None)
    SatisfiedByDevice = property(get_SatisfiedByDevice, None)
    SatisfiedByInstallMedia = property(get_SatisfiedByInstallMedia, None)
    SatisfiedByOpenLicense = property(get_SatisfiedByOpenLicense, None)
    SatisfiedByPass = property(get_SatisfiedByPass, None)
    SatisfiedBySignedInUser = property(get_SatisfiedBySignedInUser, None)
    SatisfiedByTrial = property(get_SatisfiedByTrial, None)
class LicenseSatisfactionResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Store.LicenseManagement.ILicenseSatisfactionResult
    _classid_ = 'Windows.ApplicationModel.Store.LicenseManagement.LicenseSatisfactionResult'
    @winrt_mixinmethod
    def get_LicenseSatisfactionInfos(self: win32more.Windows.ApplicationModel.Store.LicenseManagement.ILicenseSatisfactionResult) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.ApplicationModel.Store.LicenseManagement.LicenseSatisfactionInfo]: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.ApplicationModel.Store.LicenseManagement.ILicenseSatisfactionResult) -> win32more.Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
    LicenseSatisfactionInfos = property(get_LicenseSatisfactionInfos, None)


make_ready(__name__)
