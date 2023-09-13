from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Phone.PersonalInformation
import win32more.Windows.Phone.PersonalInformation.Provisioning
import win32more.Windows.Storage.Streams
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class ContactPartnerProvisioningManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.PersonalInformation.Provisioning.ContactPartnerProvisioningManager'
    @winrt_classmethod
    def AssociateNetworkAccountAsync(cls: win32more.Windows.Phone.PersonalInformation.Provisioning.IContactPartnerProvisioningManagerStatics, store: win32more.Windows.Phone.PersonalInformation.ContactStore, networkName: WinRT_String, networkAccountId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def ImportVcardToSystemAsync(cls: win32more.Windows.Phone.PersonalInformation.Provisioning.IContactPartnerProvisioningManagerStatics, stream: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def AssociateSocialNetworkAccountAsync(cls: win32more.Windows.Phone.PersonalInformation.Provisioning.IContactPartnerProvisioningManagerStatics2, store: win32more.Windows.Phone.PersonalInformation.ContactStore, networkName: WinRT_String, networkAccountId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
class IContactPartnerProvisioningManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.PersonalInformation.Provisioning.IContactPartnerProvisioningManagerStatics'
    _iid_ = Guid('{c0d79a21-01af-4fd3-98cd-b3d656de15f4}')
    @winrt_commethod(6)
    def AssociateNetworkAccountAsync(self, store: win32more.Windows.Phone.PersonalInformation.ContactStore, networkName: WinRT_String, networkAccountId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def ImportVcardToSystemAsync(self, stream: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Windows.Foundation.IAsyncAction: ...
class IContactPartnerProvisioningManagerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.PersonalInformation.Provisioning.IContactPartnerProvisioningManagerStatics2'
    _iid_ = Guid('{c26155f7-55ed-475d-9334-c5d484c30f1a}')
    @winrt_commethod(6)
    def AssociateSocialNetworkAccountAsync(self, store: win32more.Windows.Phone.PersonalInformation.ContactStore, networkName: WinRT_String, networkAccountId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
class IMessagePartnerProvisioningManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.PersonalInformation.Provisioning.IMessagePartnerProvisioningManagerStatics'
    _iid_ = Guid('{8a1b0850-73c5-457c-bc59-ed7d615c05a4}')
    @winrt_commethod(6)
    def ImportSmsToSystemAsync(self, incoming: Boolean, read: Boolean, body: WinRT_String, sender: WinRT_String, recipients: win32more.Windows.Foundation.Collections.IVectorView[WinRT_String], deliveryTime: win32more.Windows.Foundation.DateTime) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def ImportMmsToSystemAsync(self, incoming: Boolean, read: Boolean, subject: WinRT_String, sender: WinRT_String, recipients: win32more.Windows.Foundation.Collections.IVectorView[WinRT_String], deliveryTime: win32more.Windows.Foundation.DateTime, attachments: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable_head]]) -> win32more.Windows.Foundation.IAsyncAction: ...
class MessagePartnerProvisioningManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.PersonalInformation.Provisioning.MessagePartnerProvisioningManager'
    @winrt_classmethod
    def ImportSmsToSystemAsync(cls: win32more.Windows.Phone.PersonalInformation.Provisioning.IMessagePartnerProvisioningManagerStatics, incoming: Boolean, read: Boolean, body: WinRT_String, sender: WinRT_String, recipients: win32more.Windows.Foundation.Collections.IVectorView[WinRT_String], deliveryTime: win32more.Windows.Foundation.DateTime) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def ImportMmsToSystemAsync(cls: win32more.Windows.Phone.PersonalInformation.Provisioning.IMessagePartnerProvisioningManagerStatics, incoming: Boolean, read: Boolean, subject: WinRT_String, sender: WinRT_String, recipients: win32more.Windows.Foundation.Collections.IVectorView[WinRT_String], deliveryTime: win32more.Windows.Foundation.DateTime, attachments: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable_head]]) -> win32more.Windows.Foundation.IAsyncAction: ...
make_head(_module, 'ContactPartnerProvisioningManager')
make_head(_module, 'IContactPartnerProvisioningManagerStatics')
make_head(_module, 'IContactPartnerProvisioningManagerStatics2')
make_head(_module, 'IMessagePartnerProvisioningManagerStatics')
make_head(_module, 'MessagePartnerProvisioningManager')
