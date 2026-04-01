from __future__ import annotations
from win32more._prelude import *
import win32more.Windows.Foundation
import win32more.Windows.UI
import win32more.Windows.UI.Shell.CompanionWindows
class CompanionWindowCoordinator(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.UI.Shell.CompanionWindows.ICompanionWindowCoordinator
    _classid_ = 'Windows.UI.Shell.CompanionWindows.CompanionWindowCoordinator'
    @winrt_mixinmethod
    def RequestWindowFromAppAsync(self: win32more.Windows.UI.Shell.CompanionWindows.ICompanionWindowCoordinator, appId: hstr) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.Shell.CompanionWindows.CompanionWindowRequestResult]: ...
    @winrt_mixinmethod
    def DetachCompanionWindow(self: win32more.Windows.UI.Shell.CompanionWindows.ICompanionWindowCoordinator) -> Void: ...
    @winrt_mixinmethod
    def get_CompanionWindowId(self: win32more.Windows.UI.Shell.CompanionWindows.ICompanionWindowCoordinator) -> win32more.Windows.UI.WindowId: ...
    @winrt_mixinmethod
    def add_Changed(self: win32more.Windows.UI.Shell.CompanionWindows.ICompanionWindowCoordinator, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Shell.CompanionWindows.CompanionWindowCoordinator, IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Changed(self: win32more.Windows.UI.Shell.CompanionWindows.ICompanionWindowCoordinator, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetForWindow(cls: win32more.Windows.UI.Shell.CompanionWindows.ICompanionWindowCoordinatorStatics, windowId: win32more.Windows.UI.WindowId) -> win32more.Windows.UI.Shell.CompanionWindows.CompanionWindowCoordinator: ...
    CompanionWindowId = property(get_CompanionWindowId, None)
    Changed = event(add_Changed, remove_Changed)
class CompanionWindowRequest(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.UI.Shell.CompanionWindows.ICompanionWindowRequest
    _classid_ = 'Windows.UI.Shell.CompanionWindows.CompanionWindowRequest'
    @winrt_mixinmethod
    def Accept(self: win32more.Windows.UI.Shell.CompanionWindows.ICompanionWindowRequest, windowId: win32more.Windows.UI.WindowId) -> win32more.Windows.UI.Shell.CompanionWindows.CompanionWindowCoordinator: ...
    @winrt_mixinmethod
    def Reject(self: win32more.Windows.UI.Shell.CompanionWindows.ICompanionWindowRequest) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.UI.Shell.CompanionWindows.ICompanionWindowRequest) -> win32more.Windows.Foundation.Deferral: ...
    @winrt_mixinmethod
    def get_RequestingWindowId(self: win32more.Windows.UI.Shell.CompanionWindows.ICompanionWindowRequest) -> win32more.Windows.UI.WindowId: ...
    @winrt_classmethod
    def GetFromLaunchUri(cls: win32more.Windows.UI.Shell.CompanionWindows.ICompanionWindowRequestStatics, launchUri: win32more.Windows.Foundation.Uri) -> win32more.Windows.UI.Shell.CompanionWindows.CompanionWindowRequest: ...
    RequestingWindowId = property(get_RequestingWindowId, None)
class CompanionWindowRequestResult(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.UI.Shell.CompanionWindows.ICompanionWindowRequestResult
    _classid_ = 'Windows.UI.Shell.CompanionWindows.CompanionWindowRequestResult'
    @winrt_mixinmethod
    def get_Succeeded(self: win32more.Windows.UI.Shell.CompanionWindows.ICompanionWindowRequestResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.UI.Shell.CompanionWindows.ICompanionWindowRequestResult) -> win32more.Windows.UI.Shell.CompanionWindows.CompanionWindowRequestResultStatus: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.UI.Shell.CompanionWindows.ICompanionWindowRequestResult) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_CompanionWindowId(self: win32more.Windows.UI.Shell.CompanionWindows.ICompanionWindowRequestResult) -> win32more.Windows.UI.WindowId: ...
    CompanionWindowId = property(get_CompanionWindowId, None)
    ExtendedError = property(get_ExtendedError, None)
    Status = property(get_Status, None)
    Succeeded = property(get_Succeeded, None)
class CompanionWindowRequestResultStatus(Enum, Int32):
    _name_ = 'Windows.UI.Shell.CompanionWindows.CompanionWindowRequestResultStatus'
    Success = 0
    UnknownFailure = 1
    RegistrationNotFound = 2
    ActivationTimedOut = 3
    RejectedByCompanionApp = 4
CompanionWindowsContract: UInt32 = 65536
class ICompanionWindowCoordinator(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.Shell.CompanionWindows.ICompanionWindowCoordinator'
    _iid_ = Guid('{05620e87-b0f7-59ba-b3a5-d614bdc1ebe3}')
    @winrt_commethod(6)
    def RequestWindowFromAppAsync(self, appId: hstr) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.Shell.CompanionWindows.CompanionWindowRequestResult]: ...
    @winrt_commethod(7)
    def DetachCompanionWindow(self) -> Void: ...
    @winrt_commethod(8)
    def get_CompanionWindowId(self) -> win32more.Windows.UI.WindowId: ...
    @winrt_commethod(9)
    def add_Changed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Shell.CompanionWindows.CompanionWindowCoordinator, IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_Changed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    CompanionWindowId = property(get_CompanionWindowId, None)
    Changed = event(add_Changed, remove_Changed)
class ICompanionWindowCoordinatorStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.Shell.CompanionWindows.ICompanionWindowCoordinatorStatics'
    _iid_ = Guid('{964022fa-380e-518c-bfc8-0f3b84fafea3}')
    @winrt_commethod(6)
    def GetForWindow(self, windowId: win32more.Windows.UI.WindowId) -> win32more.Windows.UI.Shell.CompanionWindows.CompanionWindowCoordinator: ...
class ICompanionWindowRequest(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.Shell.CompanionWindows.ICompanionWindowRequest'
    _iid_ = Guid('{d92c351a-2d66-59a8-b345-78489562c4d8}')
    @winrt_commethod(6)
    def Accept(self, windowId: win32more.Windows.UI.WindowId) -> win32more.Windows.UI.Shell.CompanionWindows.CompanionWindowCoordinator: ...
    @winrt_commethod(7)
    def Reject(self) -> Void: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    @winrt_commethod(9)
    def get_RequestingWindowId(self) -> win32more.Windows.UI.WindowId: ...
    RequestingWindowId = property(get_RequestingWindowId, None)
class ICompanionWindowRequestResult(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.Shell.CompanionWindows.ICompanionWindowRequestResult'
    _iid_ = Guid('{d728d2ef-e6d4-5cc0-9ff4-20c17a2ce72d}')
    @winrt_commethod(6)
    def get_Succeeded(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_Status(self) -> win32more.Windows.UI.Shell.CompanionWindows.CompanionWindowRequestResultStatus: ...
    @winrt_commethod(8)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    @winrt_commethod(9)
    def get_CompanionWindowId(self) -> win32more.Windows.UI.WindowId: ...
    CompanionWindowId = property(get_CompanionWindowId, None)
    ExtendedError = property(get_ExtendedError, None)
    Status = property(get_Status, None)
    Succeeded = property(get_Succeeded, None)
class ICompanionWindowRequestStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.Shell.CompanionWindows.ICompanionWindowRequestStatics'
    _iid_ = Guid('{585e4544-d474-506a-96c2-3597a44882da}')
    @winrt_commethod(6)
    def GetFromLaunchUri(self, launchUri: win32more.Windows.Foundation.Uri) -> win32more.Windows.UI.Shell.CompanionWindows.CompanionWindowRequest: ...


make_ready(__name__)
