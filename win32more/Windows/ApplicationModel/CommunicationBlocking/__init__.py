from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel.CommunicationBlocking
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Win32.System.WinRT
class _CommunicationBlockingAccessManager_Meta_(ComPtr.__class__):
    pass
class CommunicationBlockingAccessManager(ComPtr, metaclass=_CommunicationBlockingAccessManager_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.CommunicationBlocking.CommunicationBlockingAccessManager'
    @winrt_classmethod
    def get_IsBlockingActive(cls: win32more.Windows.ApplicationModel.CommunicationBlocking.ICommunicationBlockingAccessManagerStatics) -> Boolean: ...
    @winrt_classmethod
    def IsBlockedNumberAsync(cls: win32more.Windows.ApplicationModel.CommunicationBlocking.ICommunicationBlockingAccessManagerStatics, number: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def ShowBlockNumbersUI(cls: win32more.Windows.ApplicationModel.CommunicationBlocking.ICommunicationBlockingAccessManagerStatics, phoneNumbers: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> Boolean: ...
    @winrt_classmethod
    def ShowUnblockNumbersUI(cls: win32more.Windows.ApplicationModel.CommunicationBlocking.ICommunicationBlockingAccessManagerStatics, phoneNumbers: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> Boolean: ...
    @winrt_classmethod
    def ShowBlockedCallsUI(cls: win32more.Windows.ApplicationModel.CommunicationBlocking.ICommunicationBlockingAccessManagerStatics) -> Void: ...
    @winrt_classmethod
    def ShowBlockedMessagesUI(cls: win32more.Windows.ApplicationModel.CommunicationBlocking.ICommunicationBlockingAccessManagerStatics) -> Void: ...
    _CommunicationBlockingAccessManager_Meta_.IsBlockingActive = property(get_IsBlockingActive, None)
class _CommunicationBlockingAppManager_Meta_(ComPtr.__class__):
    pass
class CommunicationBlockingAppManager(ComPtr, metaclass=_CommunicationBlockingAppManager_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.CommunicationBlocking.CommunicationBlockingAppManager'
    @winrt_classmethod
    def RequestSetAsActiveBlockingAppAsync(cls: win32more.Windows.ApplicationModel.CommunicationBlocking.ICommunicationBlockingAppManagerStatics2) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def get_IsCurrentAppActiveBlockingApp(cls: win32more.Windows.ApplicationModel.CommunicationBlocking.ICommunicationBlockingAppManagerStatics) -> Boolean: ...
    @winrt_classmethod
    def ShowCommunicationBlockingSettingsUI(cls: win32more.Windows.ApplicationModel.CommunicationBlocking.ICommunicationBlockingAppManagerStatics) -> Void: ...
    _CommunicationBlockingAppManager_Meta_.IsCurrentAppActiveBlockingApp = property(get_IsCurrentAppActiveBlockingApp, None)
CommunicationBlockingContract: UInt32 = 131072
class ICommunicationBlockingAccessManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.CommunicationBlocking.ICommunicationBlockingAccessManagerStatics'
    _iid_ = Guid('{1c969998-9d2a-5db7-edd5-0ce407fc2595}')
    @winrt_commethod(6)
    def get_IsBlockingActive(self) -> Boolean: ...
    @winrt_commethod(7)
    def IsBlockedNumberAsync(self, number: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(8)
    def ShowBlockNumbersUI(self, phoneNumbers: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> Boolean: ...
    @winrt_commethod(9)
    def ShowUnblockNumbersUI(self, phoneNumbers: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> Boolean: ...
    @winrt_commethod(10)
    def ShowBlockedCallsUI(self) -> Void: ...
    @winrt_commethod(11)
    def ShowBlockedMessagesUI(self) -> Void: ...
    IsBlockingActive = property(get_IsBlockingActive, None)
class ICommunicationBlockingAppManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.CommunicationBlocking.ICommunicationBlockingAppManagerStatics'
    _iid_ = Guid('{77db58ec-14a6-4baa-942a-6a673d999bf2}')
    @winrt_commethod(6)
    def get_IsCurrentAppActiveBlockingApp(self) -> Boolean: ...
    @winrt_commethod(7)
    def ShowCommunicationBlockingSettingsUI(self) -> Void: ...
    IsCurrentAppActiveBlockingApp = property(get_IsCurrentAppActiveBlockingApp, None)
class ICommunicationBlockingAppManagerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.CommunicationBlocking.ICommunicationBlockingAppManagerStatics2'
    _iid_ = Guid('{14a68edd-ed88-457a-a364-a3634d6f166d}')
    @winrt_commethod(6)
    def RequestSetAsActiveBlockingAppAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...


make_ready(__name__)
