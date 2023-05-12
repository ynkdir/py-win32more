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
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import Windows.Win32.System.WinRT
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Phone.PersonalInformation
import Windows.Phone.PersonalInformation.Provisioning
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
class ContactPartnerProvisioningManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.PersonalInformation.Provisioning.ContactPartnerProvisioningManager'
    @winrt_classmethod
    def AssociateNetworkAccountAsync(cls: Windows.Phone.PersonalInformation.Provisioning.IContactPartnerProvisioningManagerStatics, store: Windows.Phone.PersonalInformation.ContactStore, networkName: WinRT_String, networkAccountId: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def ImportVcardToSystemAsync(cls: Windows.Phone.PersonalInformation.Provisioning.IContactPartnerProvisioningManagerStatics, stream: Windows.Storage.Streams.IInputStream) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def AssociateSocialNetworkAccountAsync(cls: Windows.Phone.PersonalInformation.Provisioning.IContactPartnerProvisioningManagerStatics2, store: Windows.Phone.PersonalInformation.ContactStore, networkName: WinRT_String, networkAccountId: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
class IContactPartnerProvisioningManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.PersonalInformation.Provisioning.IContactPartnerProvisioningManagerStatics'
    _iid_ = Guid('{c0d79a21-01af-4fd3-98cd-b3d656de15f4}')
    @winrt_commethod(6)
    def AssociateNetworkAccountAsync(self, store: Windows.Phone.PersonalInformation.ContactStore, networkName: WinRT_String, networkAccountId: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def ImportVcardToSystemAsync(self, stream: Windows.Storage.Streams.IInputStream) -> Windows.Foundation.IAsyncAction: ...
class IContactPartnerProvisioningManagerStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.PersonalInformation.Provisioning.IContactPartnerProvisioningManagerStatics2'
    _iid_ = Guid('{c26155f7-55ed-475d-9334-c5d484c30f1a}')
    @winrt_commethod(6)
    def AssociateSocialNetworkAccountAsync(self, store: Windows.Phone.PersonalInformation.ContactStore, networkName: WinRT_String, networkAccountId: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
class IMessagePartnerProvisioningManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.PersonalInformation.Provisioning.IMessagePartnerProvisioningManagerStatics'
    _iid_ = Guid('{8a1b0850-73c5-457c-bc59-ed7d615c05a4}')
    @winrt_commethod(6)
    def ImportSmsToSystemAsync(self, incoming: Boolean, read: Boolean, body: WinRT_String, sender: WinRT_String, recipients: Windows.Foundation.Collections.IVectorView[WinRT_String], deliveryTime: Windows.Foundation.DateTime) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def ImportMmsToSystemAsync(self, incoming: Boolean, read: Boolean, subject: WinRT_String, sender: WinRT_String, recipients: Windows.Foundation.Collections.IVectorView[WinRT_String], deliveryTime: Windows.Foundation.DateTime, attachments: Windows.Foundation.Collections.IVectorView[Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]]) -> Windows.Foundation.IAsyncAction: ...
class MessagePartnerProvisioningManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.PersonalInformation.Provisioning.MessagePartnerProvisioningManager'
    @winrt_classmethod
    def ImportSmsToSystemAsync(cls: Windows.Phone.PersonalInformation.Provisioning.IMessagePartnerProvisioningManagerStatics, incoming: Boolean, read: Boolean, body: WinRT_String, sender: WinRT_String, recipients: Windows.Foundation.Collections.IVectorView[WinRT_String], deliveryTime: Windows.Foundation.DateTime) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def ImportMmsToSystemAsync(cls: Windows.Phone.PersonalInformation.Provisioning.IMessagePartnerProvisioningManagerStatics, incoming: Boolean, read: Boolean, subject: WinRT_String, sender: WinRT_String, recipients: Windows.Foundation.Collections.IVectorView[WinRT_String], deliveryTime: Windows.Foundation.DateTime, attachments: Windows.Foundation.Collections.IVectorView[Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]]) -> Windows.Foundation.IAsyncAction: ...
make_head(_module, 'ContactPartnerProvisioningManager')
make_head(_module, 'IContactPartnerProvisioningManagerStatics')
make_head(_module, 'IContactPartnerProvisioningManagerStatics2')
make_head(_module, 'IMessagePartnerProvisioningManagerStatics')
make_head(_module, 'MessagePartnerProvisioningManager')
