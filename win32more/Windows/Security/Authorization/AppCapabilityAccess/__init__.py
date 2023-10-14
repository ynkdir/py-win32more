from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
import sys
from typing import Generic, TypeVar
if sys.version_info < (3, 9):
    from typing_extensions import Annotated
else:
    from typing import Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, EasyCastStructure, EasyCastUnion, ComPtr, make_ready
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Security.Authorization.AppCapabilityAccess
import win32more.Windows.System
class AppCapability(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Authorization.AppCapabilityAccess.IAppCapability
    _classid_ = 'Windows.Security.Authorization.AppCapabilityAccess.AppCapability'
    @winrt_mixinmethod
    def get_CapabilityName(self: win32more.Windows.Security.Authorization.AppCapabilityAccess.IAppCapability) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.Security.Authorization.AppCapabilityAccess.IAppCapability) -> win32more.Windows.System.User: ...
    @winrt_mixinmethod
    def RequestAccessAsync(self: win32more.Windows.Security.Authorization.AppCapabilityAccess.IAppCapability) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authorization.AppCapabilityAccess.AppCapabilityAccessStatus]: ...
    @winrt_mixinmethod
    def CheckAccess(self: win32more.Windows.Security.Authorization.AppCapabilityAccess.IAppCapability) -> win32more.Windows.Security.Authorization.AppCapabilityAccess.AppCapabilityAccessStatus: ...
    @winrt_mixinmethod
    def add_AccessChanged(self: win32more.Windows.Security.Authorization.AppCapabilityAccess.IAppCapability, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Security.Authorization.AppCapabilityAccess.AppCapability, win32more.Windows.Security.Authorization.AppCapabilityAccess.AppCapabilityAccessChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AccessChanged(self: win32more.Windows.Security.Authorization.AppCapabilityAccess.IAppCapability, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayMessage(self: win32more.Windows.Security.Authorization.AppCapabilityAccess.IAppCapability2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayMessage(self: win32more.Windows.Security.Authorization.AppCapabilityAccess.IAppCapability2, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def RequestAccessForCapabilitiesAsync(cls: win32more.Windows.Security.Authorization.AppCapabilityAccess.IAppCapabilityStatics, capabilityNames: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Security.Authorization.AppCapabilityAccess.AppCapabilityAccessStatus]]: ...
    @winrt_classmethod
    def RequestAccessForCapabilitiesForUserAsync(cls: win32more.Windows.Security.Authorization.AppCapabilityAccess.IAppCapabilityStatics, user: win32more.Windows.System.User, capabilityNames: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Security.Authorization.AppCapabilityAccess.AppCapabilityAccessStatus]]: ...
    @winrt_classmethod
    def Create(cls: win32more.Windows.Security.Authorization.AppCapabilityAccess.IAppCapabilityStatics, capabilityName: WinRT_String) -> win32more.Windows.Security.Authorization.AppCapabilityAccess.AppCapability: ...
    @winrt_classmethod
    def CreateWithProcessIdForUser(cls: win32more.Windows.Security.Authorization.AppCapabilityAccess.IAppCapabilityStatics, user: win32more.Windows.System.User, capabilityName: WinRT_String, pid: UInt32) -> win32more.Windows.Security.Authorization.AppCapabilityAccess.AppCapability: ...
    CapabilityName = property(get_CapabilityName, None)
    User = property(get_User, None)
    DisplayMessage = property(get_DisplayMessage, put_DisplayMessage)
class AppCapabilityAccessChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Authorization.AppCapabilityAccess.IAppCapabilityAccessChangedEventArgs
    _classid_ = 'Windows.Security.Authorization.AppCapabilityAccess.AppCapabilityAccessChangedEventArgs'
AppCapabilityAccessStatus = Int32
AppCapabilityAccessStatus_DeniedBySystem: AppCapabilityAccessStatus = 0
AppCapabilityAccessStatus_NotDeclaredByApp: AppCapabilityAccessStatus = 1
AppCapabilityAccessStatus_DeniedByUser: AppCapabilityAccessStatus = 2
AppCapabilityAccessStatus_UserPromptRequired: AppCapabilityAccessStatus = 3
AppCapabilityAccessStatus_Allowed: AppCapabilityAccessStatus = 4
class IAppCapability(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authorization.AppCapabilityAccess.IAppCapability'
    _iid_ = Guid('{4c49d915-8a2a-4295-9437-2df7c396aff4}')
    @winrt_commethod(6)
    def get_CapabilityName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_User(self) -> win32more.Windows.System.User: ...
    @winrt_commethod(8)
    def RequestAccessAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.Authorization.AppCapabilityAccess.AppCapabilityAccessStatus]: ...
    @winrt_commethod(9)
    def CheckAccess(self) -> win32more.Windows.Security.Authorization.AppCapabilityAccess.AppCapabilityAccessStatus: ...
    @winrt_commethod(10)
    def add_AccessChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Security.Authorization.AppCapabilityAccess.AppCapability, win32more.Windows.Security.Authorization.AppCapabilityAccess.AppCapabilityAccessChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_AccessChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    CapabilityName = property(get_CapabilityName, None)
    User = property(get_User, None)
class IAppCapability2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authorization.AppCapabilityAccess.IAppCapability2'
    _iid_ = Guid('{11c7ccb6-c74f-50a3-b960-88008767d939}')
    @winrt_commethod(6)
    def get_DisplayMessage(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_DisplayMessage(self, value: WinRT_String) -> Void: ...
    DisplayMessage = property(get_DisplayMessage, put_DisplayMessage)
class IAppCapabilityAccessChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authorization.AppCapabilityAccess.IAppCapabilityAccessChangedEventArgs'
    _iid_ = Guid('{0a578d15-bdd7-457e-8cca-6f53bd2e5944}')
class IAppCapabilityStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authorization.AppCapabilityAccess.IAppCapabilityStatics'
    _iid_ = Guid('{7c353e2a-46ee-44e5-af3d-6ad3fc49bd22}')
    @winrt_commethod(6)
    def RequestAccessForCapabilitiesAsync(self, capabilityNames: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Security.Authorization.AppCapabilityAccess.AppCapabilityAccessStatus]]: ...
    @winrt_commethod(7)
    def RequestAccessForCapabilitiesForUserAsync(self, user: win32more.Windows.System.User, capabilityNames: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Security.Authorization.AppCapabilityAccess.AppCapabilityAccessStatus]]: ...
    @winrt_commethod(8)
    def Create(self, capabilityName: WinRT_String) -> win32more.Windows.Security.Authorization.AppCapabilityAccess.AppCapability: ...
    @winrt_commethod(9)
    def CreateWithProcessIdForUser(self, user: win32more.Windows.System.User, capabilityName: WinRT_String, pid: UInt32) -> win32more.Windows.Security.Authorization.AppCapabilityAccess.AppCapability: ...
make_ready(__name__)
