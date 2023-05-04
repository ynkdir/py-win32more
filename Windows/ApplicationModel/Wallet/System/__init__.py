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
import Windows.ApplicationModel.Wallet
import Windows.ApplicationModel.Wallet.System
import Windows.Foundation
import Windows.Foundation.Collections
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
class IWalletItemSystemStore(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Wallet.System.IWalletItemSystemStore'
    _iid_ = Guid('{522e2bff-96a2-4a17-8d19-fe1d9f837561}')
    @winrt_commethod(6)
    def GetItemsAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Wallet.WalletItem]]: ...
    @winrt_commethod(7)
    def DeleteAsync(self, item: Windows.ApplicationModel.Wallet.WalletItem) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def ImportItemAsync(self, stream: Windows.Storage.Streams.IRandomAccessStreamReference) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Wallet.WalletItem]: ...
    @winrt_commethod(9)
    def GetAppStatusForItem(self, item: Windows.ApplicationModel.Wallet.WalletItem) -> Windows.ApplicationModel.Wallet.System.WalletItemAppAssociation: ...
    @winrt_commethod(10)
    def LaunchAppForItemAsync(self, item: Windows.ApplicationModel.Wallet.WalletItem) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
class IWalletItemSystemStore2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Wallet.System.IWalletItemSystemStore2'
    _iid_ = Guid('{f98d3a4e-be00-4fdd-9734-6c113c1ac1cb}')
    @winrt_commethod(6)
    def add_ItemsChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Wallet.System.WalletItemSystemStore, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ItemsChanged(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IWalletManagerSystemStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Wallet.System.IWalletManagerSystemStatics'
    _iid_ = Guid('{bee8eb89-2634-4b9a-8b23-ee8903c91fe0}')
    @winrt_commethod(6)
    def RequestStoreAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Wallet.System.WalletItemSystemStore]: ...
WalletItemAppAssociation = Int32
WalletItemAppAssociation_None: WalletItemAppAssociation = 0
WalletItemAppAssociation_AppInstalled: WalletItemAppAssociation = 1
WalletItemAppAssociation_AppNotInstalled: WalletItemAppAssociation = 2
class WalletItemSystemStore(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Wallet.System.IWalletItemSystemStore
    _classid_ = 'Windows.ApplicationModel.Wallet.System.WalletItemSystemStore'
    @winrt_mixinmethod
    def GetItemsAsync(self: Windows.ApplicationModel.Wallet.System.IWalletItemSystemStore) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Wallet.WalletItem]]: ...
    @winrt_mixinmethod
    def DeleteAsync(self: Windows.ApplicationModel.Wallet.System.IWalletItemSystemStore, item: Windows.ApplicationModel.Wallet.WalletItem) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ImportItemAsync(self: Windows.ApplicationModel.Wallet.System.IWalletItemSystemStore, stream: Windows.Storage.Streams.IRandomAccessStreamReference) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Wallet.WalletItem]: ...
    @winrt_mixinmethod
    def GetAppStatusForItem(self: Windows.ApplicationModel.Wallet.System.IWalletItemSystemStore, item: Windows.ApplicationModel.Wallet.WalletItem) -> Windows.ApplicationModel.Wallet.System.WalletItemAppAssociation: ...
    @winrt_mixinmethod
    def LaunchAppForItemAsync(self: Windows.ApplicationModel.Wallet.System.IWalletItemSystemStore, item: Windows.ApplicationModel.Wallet.WalletItem) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def add_ItemsChanged(self: Windows.ApplicationModel.Wallet.System.IWalletItemSystemStore2, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Wallet.System.WalletItemSystemStore, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ItemsChanged(self: Windows.ApplicationModel.Wallet.System.IWalletItemSystemStore2, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
class WalletManagerSystem(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Wallet.System.WalletManagerSystem'
    @winrt_classmethod
    def RequestStoreAsync(cls: Windows.ApplicationModel.Wallet.System.IWalletManagerSystemStatics) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Wallet.System.WalletItemSystemStore]: ...
make_head(_module, 'IWalletItemSystemStore')
make_head(_module, 'IWalletItemSystemStore2')
make_head(_module, 'IWalletManagerSystemStatics')
make_head(_module, 'WalletItemSystemStore')
make_head(_module, 'WalletManagerSystem')
