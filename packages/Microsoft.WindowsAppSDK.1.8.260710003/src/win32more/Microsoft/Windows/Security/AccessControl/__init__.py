from __future__ import annotations
from win32more._prelude import *
import win32more.Microsoft.Windows.Security.AccessControl
AccessControlContract: UInt32 = 65536
class AppContainerNameAndAccess(Structure):
    _name_ = 'Microsoft.Windows.Security.AccessControl.AppContainerNameAndAccess'
    appContainerName: hstr
    accessMask: UInt32
class ISecurityDescriptorHelpersStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Security.AccessControl.ISecurityDescriptorHelpersStatics'
    _iid_ = Guid('{14fa9e8d-59f0-5017-852f-3ae24fd5ebb1}')
    @winrt_commethod(6)
    def GetSddlForAppContainerNames(self, accessRequests: PassArray[win32more.Microsoft.Windows.Security.AccessControl.AppContainerNameAndAccess], principalStringSid: hstr, principalAccessMask: UInt32) -> hstr: ...
    @winrt_commethod(7)
    def GetSecurityDescriptorBytesFromAppContainerNames(self, accessRequests: PassArray[win32more.Microsoft.Windows.Security.AccessControl.AppContainerNameAndAccess], principalStringSid: hstr, principalAccessMask: UInt32) -> ReceiveArray[Byte]: ...
class SecurityDescriptorHelpers(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Security.AccessControl.SecurityDescriptorHelpers'
    @winrt_classmethod
    def GetSddlForAppContainerNames(cls: win32more.Microsoft.Windows.Security.AccessControl.ISecurityDescriptorHelpersStatics, accessRequests: PassArray[win32more.Microsoft.Windows.Security.AccessControl.AppContainerNameAndAccess], principalStringSid: hstr, principalAccessMask: UInt32) -> hstr: ...
    @winrt_classmethod
    def GetSecurityDescriptorBytesFromAppContainerNames(cls: win32more.Microsoft.Windows.Security.AccessControl.ISecurityDescriptorHelpersStatics, accessRequests: PassArray[win32more.Microsoft.Windows.Security.AccessControl.AppContainerNameAndAccess], principalStringSid: hstr, principalAccessMask: UInt32) -> ReceiveArray[Byte]: ...


make_ready(__name__)
