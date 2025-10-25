from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Windows.ApplicationModel.Wallet
import win32more.Windows.ApplicationModel.Wallet.System
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Storage.Streams
class IWalletItemSystemStore(ComPtr):
    extends: IInspectable
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
    extends: IInspectable
    _classid_ = 'Windows.ApplicationModel.Wallet.System.IWalletItemSystemStore2'
    _iid_ = Guid('{f98d3a4e-be00-4fdd-9734-6c113c1ac1cb}')
    @winrt_commethod(6)
    def add_ItemsChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Wallet.System.WalletItemSystemStore, IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ItemsChanged(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    ItemsChanged = event()
class IWalletManagerSystemStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.ApplicationModel.Wallet.System.IWalletManagerSystemStatics'
    _iid_ = Guid('{bee8eb89-2634-4b9a-8b23-ee8903c91fe0}')
    @winrt_commethod(6)
    def RequestStoreAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Wallet.System.WalletItemSystemStore]: ...
class WalletItemAppAssociation(Enum, Int32):
    None_ = 0
    AppInstalled = 1
    AppNotInstalled = 2
class WalletItemSystemStore(ComPtr):
    extends: IInspectable
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
    def add_ItemsChanged(self: win32more.Windows.ApplicationModel.Wallet.System.IWalletItemSystemStore2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Wallet.System.WalletItemSystemStore, IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ItemsChanged(self: win32more.Windows.ApplicationModel.Wallet.System.IWalletItemSystemStore2, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    ItemsChanged = event()
class WalletManagerSystem(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.ApplicationModel.Wallet.System.WalletManagerSystem'
    @winrt_classmethod
    def RequestStoreAsync(cls: win32more.Windows.ApplicationModel.Wallet.System.IWalletManagerSystemStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Wallet.System.WalletItemSystemStore]: ...


make_ready(__name__)
