from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
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
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Media.Playlists
import win32more.Windows.Storage
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
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
PlaylistFormat = Int32
PlaylistFormat_WindowsMedia: PlaylistFormat = 0
PlaylistFormat_Zune: PlaylistFormat = 1
PlaylistFormat_M3u: PlaylistFormat = 2
PlaylistsContract: UInt32 = 65536
make_head(_module, 'IPlaylist')
make_head(_module, 'IPlaylistStatics')
make_head(_module, 'Playlist')
