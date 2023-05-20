from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import Windows.Win32.System.WinRT
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Security.Authentication.Identity
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class EnterpriseKeyCredentialRegistrationInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.Authentication.Identity.IEnterpriseKeyCredentialRegistrationInfo
    _classid_ = 'Windows.Security.Authentication.Identity.EnterpriseKeyCredentialRegistrationInfo'
    @winrt_mixinmethod
    def get_TenantId(self: Windows.Security.Authentication.Identity.IEnterpriseKeyCredentialRegistrationInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TenantName(self: Windows.Security.Authentication.Identity.IEnterpriseKeyCredentialRegistrationInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Subject(self: Windows.Security.Authentication.Identity.IEnterpriseKeyCredentialRegistrationInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_KeyId(self: Windows.Security.Authentication.Identity.IEnterpriseKeyCredentialRegistrationInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_KeyName(self: Windows.Security.Authentication.Identity.IEnterpriseKeyCredentialRegistrationInfo) -> WinRT_String: ...
    TenantId = property(get_TenantId, None)
    TenantName = property(get_TenantName, None)
    Subject = property(get_Subject, None)
    KeyId = property(get_KeyId, None)
    KeyName = property(get_KeyName, None)
class _EnterpriseKeyCredentialRegistrationManager_Meta_(ComPtr.__class__):
    pass
class EnterpriseKeyCredentialRegistrationManager(ComPtr, metaclass=_EnterpriseKeyCredentialRegistrationManager_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.Authentication.Identity.IEnterpriseKeyCredentialRegistrationManager
    _classid_ = 'Windows.Security.Authentication.Identity.EnterpriseKeyCredentialRegistrationManager'
    @winrt_mixinmethod
    def GetRegistrationsAsync(self: Windows.Security.Authentication.Identity.IEnterpriseKeyCredentialRegistrationManager) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Security.Authentication.Identity.EnterpriseKeyCredentialRegistrationInfo]]: ...
    @winrt_classmethod
    def get_Current(cls: Windows.Security.Authentication.Identity.IEnterpriseKeyCredentialRegistrationManagerStatics) -> Windows.Security.Authentication.Identity.EnterpriseKeyCredentialRegistrationManager: ...
    _EnterpriseKeyCredentialRegistrationManager_Meta_.Current = property(get_Current.__wrapped__, None)
class IEnterpriseKeyCredentialRegistrationInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Identity.IEnterpriseKeyCredentialRegistrationInfo'
    _iid_ = Guid('{38321acc-672b-4823-b603-6b3c753daf97}')
    @winrt_commethod(6)
    def get_TenantId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_TenantName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Subject(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_KeyId(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_KeyName(self) -> WinRT_String: ...
    TenantId = property(get_TenantId, None)
    TenantName = property(get_TenantName, None)
    Subject = property(get_Subject, None)
    KeyId = property(get_KeyId, None)
    KeyName = property(get_KeyName, None)
class IEnterpriseKeyCredentialRegistrationManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Identity.IEnterpriseKeyCredentialRegistrationManager'
    _iid_ = Guid('{83f3be3f-a25f-4cba-bb8e-bdc32d03c297}')
    @winrt_commethod(6)
    def GetRegistrationsAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Security.Authentication.Identity.EnterpriseKeyCredentialRegistrationInfo]]: ...
class IEnterpriseKeyCredentialRegistrationManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Identity.IEnterpriseKeyCredentialRegistrationManagerStatics'
    _iid_ = Guid('{77b85e9e-acf4-4bc0-bac2-40bb46efbb3f}')
    @winrt_commethod(6)
    def get_Current(self) -> Windows.Security.Authentication.Identity.EnterpriseKeyCredentialRegistrationManager: ...
    Current = property(get_Current, None)
make_head(_module, 'EnterpriseKeyCredentialRegistrationInfo')
make_head(_module, 'EnterpriseKeyCredentialRegistrationManager')
make_head(_module, 'IEnterpriseKeyCredentialRegistrationInfo')
make_head(_module, 'IEnterpriseKeyCredentialRegistrationManager')
make_head(_module, 'IEnterpriseKeyCredentialRegistrationManagerStatics')
