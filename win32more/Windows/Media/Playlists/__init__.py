from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Media.Playlists
import win32more.Windows.Storage
import win32more.Windows.Win32.System.WinRT
class IPlaylist(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Playlists.IPlaylist'
    _iid_ = Guid('{803736f5-cf44-4d97-83b3-7a089e9ab663}')
    @winrt_commethod(6)
    def get_Files(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Storage.StorageFile]: ...
    @winrt_commethod(7)
    def SaveAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def SaveAsAsync(self, saveLocation: win32more.Windows.Storage.IStorageFolder, desiredName: WinRT_String, option: win32more.Windows.Storage.NameCollisionOption) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_commethod(9)
    def SaveAsWithFormatAsync(self, saveLocation: win32more.Windows.Storage.IStorageFolder, desiredName: WinRT_String, option: win32more.Windows.Storage.NameCollisionOption, playlistFormat: win32more.Windows.Media.Playlists.PlaylistFormat) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    Files = property(get_Files, None)
class IPlaylistStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Playlists.IPlaylistStatics'
    _iid_ = Guid('{c5c331cd-81f9-4ff3-95b9-70b6ff046b68}')
    @winrt_commethod(6)
    def LoadAsync(self, file: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Playlists.Playlist]: ...
class Playlist(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Playlists.IPlaylist
    _classid_ = 'Windows.Media.Playlists.Playlist'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.Playlists.Playlist.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Playlists.Playlist: ...
    @winrt_mixinmethod
    def get_Files(self: win32more.Windows.Media.Playlists.IPlaylist) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Storage.StorageFile]: ...
    @winrt_mixinmethod
    def SaveAsync(self: win32more.Windows.Media.Playlists.IPlaylist) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SaveAsAsync(self: win32more.Windows.Media.Playlists.IPlaylist, saveLocation: win32more.Windows.Storage.IStorageFolder, desiredName: WinRT_String, option: win32more.Windows.Storage.NameCollisionOption) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_mixinmethod
    def SaveAsWithFormatAsync(self: win32more.Windows.Media.Playlists.IPlaylist, saveLocation: win32more.Windows.Storage.IStorageFolder, desiredName: WinRT_String, option: win32more.Windows.Storage.NameCollisionOption, playlistFormat: win32more.Windows.Media.Playlists.PlaylistFormat) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_classmethod
    def LoadAsync(cls: win32more.Windows.Media.Playlists.IPlaylistStatics, file: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Playlists.Playlist]: ...
    Files = property(get_Files, None)
class PlaylistFormat(Enum, Int32):
    WindowsMedia = 0
    Zune = 1
    M3u = 2
PlaylistsContract: UInt32 = 65536


make_ready(__name__)
