from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.ApplicationModel.Wallet
import win32more.Windows.ApplicationModel.Wallet.System
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
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
class IWalletItemSystemStore(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Wallet.System.IWalletItemSystemStore'
    _iid_ = Guid('{522e2bff-96a2-4a17-8d19-fe1d9f837561}')
    @winrt_commethod(6)
    def GetItemsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Wallet.WalletItem]]: ...
    @winrt_commethod(7)
    def DeleteAsync(self, item: win32more.Windows.ApplicationModel.Wallet.WalletItem) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def ImportItemAsync(self, stream: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Wallet.WalletItem]: ...
    @winrt_commethod(9)
    def GetAppStatusForItem(self, item: win32more.Windows.ApplicationModel.Wallet.WalletItem) -> win32more.Windows.ApplicationModel.Wallet.System.WalletItemAppAssociation: ...
    @winrt_commethod(10)
    def LaunchAppForItemAsync(self, item: win32more.Windows.ApplicationModel.Wallet.WalletItem) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
class IWalletItemSystemStore2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Wallet.System.IWalletItemSystemStore2'
    _iid_ = Guid('{f98d3a4e-be00-4fdd-9734-6c113c1ac1cb}')
    @winrt_commethod(6)
    def add_ItemsChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Wallet.System.WalletItemSystemStore, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ItemsChanged(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class IWalletManagerSystemStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Wallet.System.IWalletManagerSystemStatics'
    _iid_ = Guid('{bee8eb89-2634-4b9a-8b23-ee8903c91fe0}')
    @winrt_commethod(6)
    def RequestStoreAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Wallet.System.WalletItemSystemStore]: ...
WalletItemAppAssociation = Int32
WalletItemAppAssociation_None: WalletItemAppAssociation = 0
WalletItemAppAssociation_AppInstalled: WalletItemAppAssociation = 1
WalletItemAppAssociation_AppNotInstalled: WalletItemAppAssociation = 2
class WalletItemSystemStore(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Wallet.System.IWalletItemSystemStore
    _classid_ = 'Windows.ApplicationModel.Wallet.System.WalletItemSystemStore'
    @winrt_mixinmethod
    def GetItemsAsync(self: win32more.Windows.ApplicationModel.Wallet.System.IWalletItemSystemStore) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Wallet.WalletItem]]: ...
    @winrt_mixinmethod
    def DeleteAsync(self: win32more.Windows.ApplicationModel.Wallet.System.IWalletItemSystemStore, item: win32more.Windows.ApplicationModel.Wallet.WalletItem) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ImportItemAsync(self: win32more.Windows.ApplicationModel.Wallet.System.IWalletItemSystemStore, stream: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Wallet.WalletItem]: ...
    @winrt_mixinmethod
    def GetAppStatusForItem(self: win32more.Windows.ApplicationModel.Wallet.System.IWalletItemSystemStore, item: win32more.Windows.ApplicationModel.Wallet.WalletItem) -> win32more.Windows.ApplicationModel.Wallet.System.WalletItemAppAssociation: ...
    @winrt_mixinmethod
    def LaunchAppForItemAsync(self: win32more.Windows.ApplicationModel.Wallet.System.IWalletItemSystemStore, item: win32more.Windows.ApplicationModel.Wallet.WalletItem) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def add_ItemsChanged(self: win32more.Windows.ApplicationModel.Wallet.System.IWalletItemSystemStore2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Wallet.System.WalletItemSystemStore, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ItemsChanged(self: win32more.Windows.ApplicationModel.Wallet.System.IWalletItemSystemStore2, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class WalletManagerSystem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Wallet.System.WalletManagerSystem'
    @winrt_classmethod
    def RequestStoreAsync(cls: Windows.ApplicationModel.Wallet.System.IWalletManagerSystemStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Wallet.System.WalletItemSystemStore]: ...
make_head(_module, 'IWalletItemSystemStore')
make_head(_module, 'IWalletItemSystemStore2')
make_head(_module, 'IWalletManagerSystemStatics')
make_head(_module, 'WalletItemSystemStore')
make_head(_module, 'WalletManagerSystem')
