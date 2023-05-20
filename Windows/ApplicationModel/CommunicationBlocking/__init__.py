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
import Windows.ApplicationModel.CommunicationBlocking
import Windows.Foundation
import Windows.Foundation.Collections
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class _CommunicationBlockingAccessManager_Meta_(ComPtr.__class__):
    pass
class CommunicationBlockingAccessManager(ComPtr, metaclass=_CommunicationBlockingAccessManager_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.CommunicationBlocking.CommunicationBlockingAccessManager'
    @winrt_classmethod
    def get_IsBlockingActive(cls: Windows.ApplicationModel.CommunicationBlocking.ICommunicationBlockingAccessManagerStatics) -> Boolean: ...
    @winrt_classmethod
    def IsBlockedNumberAsync(cls: Windows.ApplicationModel.CommunicationBlocking.ICommunicationBlockingAccessManagerStatics, number: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def ShowBlockNumbersUI(cls: Windows.ApplicationModel.CommunicationBlocking.ICommunicationBlockingAccessManagerStatics, phoneNumbers: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Boolean: ...
    @winrt_classmethod
    def ShowUnblockNumbersUI(cls: Windows.ApplicationModel.CommunicationBlocking.ICommunicationBlockingAccessManagerStatics, phoneNumbers: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Boolean: ...
    @winrt_classmethod
    def ShowBlockedCallsUI(cls: Windows.ApplicationModel.CommunicationBlocking.ICommunicationBlockingAccessManagerStatics) -> Void: ...
    @winrt_classmethod
    def ShowBlockedMessagesUI(cls: Windows.ApplicationModel.CommunicationBlocking.ICommunicationBlockingAccessManagerStatics) -> Void: ...
    _CommunicationBlockingAccessManager_Meta_.IsBlockingActive = property(get_IsBlockingActive.__wrapped__, None)
class _CommunicationBlockingAppManager_Meta_(ComPtr.__class__):
    pass
class CommunicationBlockingAppManager(ComPtr, metaclass=_CommunicationBlockingAppManager_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.CommunicationBlocking.CommunicationBlockingAppManager'
    @winrt_classmethod
    def RequestSetAsActiveBlockingAppAsync(cls: Windows.ApplicationModel.CommunicationBlocking.ICommunicationBlockingAppManagerStatics2) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def get_IsCurrentAppActiveBlockingApp(cls: Windows.ApplicationModel.CommunicationBlocking.ICommunicationBlockingAppManagerStatics) -> Boolean: ...
    @winrt_classmethod
    def ShowCommunicationBlockingSettingsUI(cls: Windows.ApplicationModel.CommunicationBlocking.ICommunicationBlockingAppManagerStatics) -> Void: ...
    _CommunicationBlockingAppManager_Meta_.IsCurrentAppActiveBlockingApp = property(get_IsCurrentAppActiveBlockingApp.__wrapped__, None)
CommunicationBlockingContract: UInt32 = 131072
class ICommunicationBlockingAccessManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.CommunicationBlocking.ICommunicationBlockingAccessManagerStatics'
    _iid_ = Guid('{1c969998-9d2a-5db7-edd5-0ce407fc2595}')
    @winrt_commethod(6)
    def get_IsBlockingActive(self) -> Boolean: ...
    @winrt_commethod(7)
    def IsBlockedNumberAsync(self, number: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(8)
    def ShowBlockNumbersUI(self, phoneNumbers: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Boolean: ...
    @winrt_commethod(9)
    def ShowUnblockNumbersUI(self, phoneNumbers: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Boolean: ...
    @winrt_commethod(10)
    def ShowBlockedCallsUI(self) -> Void: ...
    @winrt_commethod(11)
    def ShowBlockedMessagesUI(self) -> Void: ...
    IsBlockingActive = property(get_IsBlockingActive, None)
class ICommunicationBlockingAppManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.CommunicationBlocking.ICommunicationBlockingAppManagerStatics'
    _iid_ = Guid('{77db58ec-14a6-4baa-942a-6a673d999bf2}')
    @winrt_commethod(6)
    def get_IsCurrentAppActiveBlockingApp(self) -> Boolean: ...
    @winrt_commethod(7)
    def ShowCommunicationBlockingSettingsUI(self) -> Void: ...
    IsCurrentAppActiveBlockingApp = property(get_IsCurrentAppActiveBlockingApp, None)
class ICommunicationBlockingAppManagerStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.CommunicationBlocking.ICommunicationBlockingAppManagerStatics2'
    _iid_ = Guid('{14a68edd-ed88-457a-a364-a3634d6f166d}')
    @winrt_commethod(6)
    def RequestSetAsActiveBlockingAppAsync(self) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
make_head(_module, 'CommunicationBlockingAccessManager')
make_head(_module, 'CommunicationBlockingAppManager')
make_head(_module, 'ICommunicationBlockingAccessManagerStatics')
make_head(_module, 'ICommunicationBlockingAppManagerStatics')
make_head(_module, 'ICommunicationBlockingAppManagerStatics2')
