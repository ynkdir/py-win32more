from __future__ import annotations
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
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, winrt_overload, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Security.Authentication.Identity
class EnterpriseKeyCredentialRegistrationInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Authentication.Identity.IEnterpriseKeyCredentialRegistrationInfo
    _classid_ = 'Windows.Security.Authentication.Identity.EnterpriseKeyCredentialRegistrationInfo'
    @winrt_mixinmethod
    def get_TenantId(self: win32more.Windows.Security.Authentication.Identity.IEnterpriseKeyCredentialRegistrationInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TenantName(self: win32more.Windows.Security.Authentication.Identity.IEnterpriseKeyCredentialRegistrationInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Subject(self: win32more.Windows.Security.Authentication.Identity.IEnterpriseKeyCredentialRegistrationInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_KeyId(self: win32more.Windows.Security.Authentication.Identity.IEnterpriseKeyCredentialRegistrationInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_KeyName(self: win32more.Windows.Security.Authentication.Identity.IEnterpriseKeyCredentialRegistrationInfo) -> WinRT_String: ...
    TenantId = property(get_TenantId, None)
    TenantName = property(get_TenantName, None)
    Subject = property(get_Subject, None)
    KeyId = property(get_KeyId, None)
    KeyName = property(get_KeyName, None)
class _EnterpriseKeyCredentialRegistrationManager_Meta_(ComPtr.__class__):
    pass
class EnterpriseKeyCredentialRegistrationManager(ComPtr, metaclass=_EnterpriseKeyCredentialRegistrationManager_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Authentication.Identity.IEnterpriseKeyCredentialRegistrationManager
    _classid_ = 'Windows.Security.Authentication.Identity.EnterpriseKeyCredentialRegistrationManager'
    @winrt_mixinmethod
    def GetRegistrationsAsync(self: win32more.Windows.Security.Authentication.Identity.IEnterpriseKeyCredentialRegistrationManager) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Authentication.Identity.EnterpriseKeyCredentialRegistrationInfo]]: ...
    @winrt_classmethod
    def get_Current(cls: win32more.Windows.Security.Authentication.Identity.IEnterpriseKeyCredentialRegistrationManagerStatics) -> win32more.Windows.Security.Authentication.Identity.EnterpriseKeyCredentialRegistrationManager: ...
    _EnterpriseKeyCredentialRegistrationManager_Meta_.Current = property(get_Current.__wrapped__, None)
class IEnterpriseKeyCredentialRegistrationInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Identity.IEnterpriseKeyCredentialRegistrationManager'
    _iid_ = Guid('{83f3be3f-a25f-4cba-bb8e-bdc32d03c297}')
    @winrt_commethod(6)
    def GetRegistrationsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Security.Authentication.Identity.EnterpriseKeyCredentialRegistrationInfo]]: ...
class IEnterpriseKeyCredentialRegistrationManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Authentication.Identity.IEnterpriseKeyCredentialRegistrationManagerStatics'
    _iid_ = Guid('{77b85e9e-acf4-4bc0-bac2-40bb46efbb3f}')
    @winrt_commethod(6)
    def get_Current(self) -> win32more.Windows.Security.Authentication.Identity.EnterpriseKeyCredentialRegistrationManager: ...
    Current = property(get_Current, None)


make_ready(__name__)
