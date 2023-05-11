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
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Security.Authorization.AppCapabilityAccess
import Windows.System
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class AppCapability(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.Authorization.AppCapabilityAccess.IAppCapability
    _classid_ = 'Windows.Security.Authorization.AppCapabilityAccess.AppCapability'
    @winrt_mixinmethod
    def get_CapabilityName(self: Windows.Security.Authorization.AppCapabilityAccess.IAppCapability) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_User(self: Windows.Security.Authorization.AppCapabilityAccess.IAppCapability) -> Windows.System.User: ...
    @winrt_mixinmethod
    def RequestAccessAsync(self: Windows.Security.Authorization.AppCapabilityAccess.IAppCapability) -> Windows.Foundation.IAsyncOperation[Windows.Security.Authorization.AppCapabilityAccess.AppCapabilityAccessStatus]: ...
    @winrt_mixinmethod
    def CheckAccess(self: Windows.Security.Authorization.AppCapabilityAccess.IAppCapability) -> Windows.Security.Authorization.AppCapabilityAccess.AppCapabilityAccessStatus: ...
    @winrt_mixinmethod
    def add_AccessChanged(self: Windows.Security.Authorization.AppCapabilityAccess.IAppCapability, handler: Windows.Foundation.TypedEventHandler[Windows.Security.Authorization.AppCapabilityAccess.AppCapability, Windows.Security.Authorization.AppCapabilityAccess.AppCapabilityAccessChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AccessChanged(self: Windows.Security.Authorization.AppCapabilityAccess.IAppCapability, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayMessage(self: Windows.Security.Authorization.AppCapabilityAccess.IAppCapability2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayMessage(self: Windows.Security.Authorization.AppCapabilityAccess.IAppCapability2, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def RequestAccessForCapabilitiesAsync(cls: Windows.Security.Authorization.AppCapabilityAccess.IAppCapabilityStatics, capabilityNames: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Security.Authorization.AppCapabilityAccess.AppCapabilityAccessStatus]]: ...
    @winrt_classmethod
    def RequestAccessForCapabilitiesForUserAsync(cls: Windows.Security.Authorization.AppCapabilityAccess.IAppCapabilityStatics, user: Windows.System.User, capabilityNames: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Security.Authorization.AppCapabilityAccess.AppCapabilityAccessStatus]]: ...
    @winrt_classmethod
    def Create(cls: Windows.Security.Authorization.AppCapabilityAccess.IAppCapabilityStatics, capabilityName: WinRT_String) -> Windows.Security.Authorization.AppCapabilityAccess.AppCapability: ...
    @winrt_classmethod
    def CreateWithProcessIdForUser(cls: Windows.Security.Authorization.AppCapabilityAccess.IAppCapabilityStatics, user: Windows.System.User, capabilityName: WinRT_String, pid: UInt32) -> Windows.Security.Authorization.AppCapabilityAccess.AppCapability: ...
    CapabilityName = property(get_CapabilityName, None)
    User = property(get_User, None)
    DisplayMessage = property(get_DisplayMessage, put_DisplayMessage)
class AppCapabilityAccessChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.Authorization.AppCapabilityAccess.IAppCapabilityAccessChangedEventArgs
    _classid_ = 'Windows.Security.Authorization.AppCapabilityAccess.AppCapabilityAccessChangedEventArgs'
AppCapabilityAccessStatus = Int32
AppCapabilityAccessStatus_DeniedBySystem: AppCapabilityAccessStatus = 0
AppCapabilityAccessStatus_NotDeclaredByApp: AppCapabilityAccessStatus = 1
AppCapabilityAccessStatus_DeniedByUser: AppCapabilityAccessStatus = 2
AppCapabilityAccessStatus_UserPromptRequired: AppCapabilityAccessStatus = 3
AppCapabilityAccessStatus_Allowed: AppCapabilityAccessStatus = 4
class IAppCapability(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authorization.AppCapabilityAccess.IAppCapability'
    _iid_ = Guid('{4c49d915-8a2a-4295-9437-2df7c396aff4}')
    @winrt_commethod(6)
    def get_CapabilityName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_User(self) -> Windows.System.User: ...
    @winrt_commethod(8)
    def RequestAccessAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Security.Authorization.AppCapabilityAccess.AppCapabilityAccessStatus]: ...
    @winrt_commethod(9)
    def CheckAccess(self) -> Windows.Security.Authorization.AppCapabilityAccess.AppCapabilityAccessStatus: ...
    @winrt_commethod(10)
    def add_AccessChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Security.Authorization.AppCapabilityAccess.AppCapability, Windows.Security.Authorization.AppCapabilityAccess.AppCapabilityAccessChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_AccessChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    CapabilityName = property(get_CapabilityName, None)
    User = property(get_User, None)
class IAppCapability2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authorization.AppCapabilityAccess.IAppCapability2'
    _iid_ = Guid('{11c7ccb6-c74f-50a3-b960-88008767d939}')
    @winrt_commethod(6)
    def get_DisplayMessage(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_DisplayMessage(self, value: WinRT_String) -> Void: ...
    DisplayMessage = property(get_DisplayMessage, put_DisplayMessage)
class IAppCapabilityAccessChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authorization.AppCapabilityAccess.IAppCapabilityAccessChangedEventArgs'
    _iid_ = Guid('{0a578d15-bdd7-457e-8cca-6f53bd2e5944}')
class IAppCapabilityStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authorization.AppCapabilityAccess.IAppCapabilityStatics'
    _iid_ = Guid('{7c353e2a-46ee-44e5-af3d-6ad3fc49bd22}')
    @winrt_commethod(6)
    def RequestAccessForCapabilitiesAsync(self, capabilityNames: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Security.Authorization.AppCapabilityAccess.AppCapabilityAccessStatus]]: ...
    @winrt_commethod(7)
    def RequestAccessForCapabilitiesForUserAsync(self, user: Windows.System.User, capabilityNames: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Security.Authorization.AppCapabilityAccess.AppCapabilityAccessStatus]]: ...
    @winrt_commethod(8)
    def Create(self, capabilityName: WinRT_String) -> Windows.Security.Authorization.AppCapabilityAccess.AppCapability: ...
    @winrt_commethod(9)
    def CreateWithProcessIdForUser(self, user: Windows.System.User, capabilityName: WinRT_String, pid: UInt32) -> Windows.Security.Authorization.AppCapabilityAccess.AppCapability: ...
make_head(_module, 'AppCapability')
make_head(_module, 'AppCapabilityAccessChangedEventArgs')
make_head(_module, 'IAppCapability')
make_head(_module, 'IAppCapability2')
make_head(_module, 'IAppCapabilityAccessChangedEventArgs')
make_head(_module, 'IAppCapabilityStatics')
