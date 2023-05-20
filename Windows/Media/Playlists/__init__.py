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
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Media.Playlists
import Windows.Storage
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Playlists.IPlaylist'
    _iid_ = Guid('{803736f5-cf44-4d97-83b3-7a089e9ab663}')
    @winrt_commethod(6)
    def get_Files(self) -> Windows.Foundation.Collections.IVector[Windows.Storage.StorageFile]: ...
    @winrt_commethod(7)
    def SaveAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def SaveAsAsync(self, saveLocation: Windows.Storage.IStorageFolder, desiredName: WinRT_String, option: Windows.Storage.NameCollisionOption) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    @winrt_commethod(9)
    def SaveAsWithFormatAsync(self, saveLocation: Windows.Storage.IStorageFolder, desiredName: WinRT_String, option: Windows.Storage.NameCollisionOption, playlistFormat: Windows.Media.Playlists.PlaylistFormat) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    Files = property(get_Files, None)
class IPlaylistStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Playlists.IPlaylistStatics'
    _iid_ = Guid('{c5c331cd-81f9-4ff3-95b9-70b6ff046b68}')
    @winrt_commethod(6)
    def LoadAsync(self, file: Windows.Storage.IStorageFile) -> Windows.Foundation.IAsyncOperation[Windows.Media.Playlists.Playlist]: ...
class Playlist(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.Playlists.IPlaylist
    _classid_ = 'Windows.Media.Playlists.Playlist'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Media.Playlists.Playlist: ...
    @winrt_mixinmethod
    def get_Files(self: Windows.Media.Playlists.IPlaylist) -> Windows.Foundation.Collections.IVector[Windows.Storage.StorageFile]: ...
    @winrt_mixinmethod
    def SaveAsync(self: Windows.Media.Playlists.IPlaylist) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SaveAsAsync(self: Windows.Media.Playlists.IPlaylist, saveLocation: Windows.Storage.IStorageFolder, desiredName: WinRT_String, option: Windows.Storage.NameCollisionOption) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    @winrt_mixinmethod
    def SaveAsWithFormatAsync(self: Windows.Media.Playlists.IPlaylist, saveLocation: Windows.Storage.IStorageFolder, desiredName: WinRT_String, option: Windows.Storage.NameCollisionOption, playlistFormat: Windows.Media.Playlists.PlaylistFormat) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    @winrt_classmethod
    def LoadAsync(cls: Windows.Media.Playlists.IPlaylistStatics, file: Windows.Storage.IStorageFile) -> Windows.Foundation.IAsyncOperation[Windows.Media.Playlists.Playlist]: ...
    Files = property(get_Files, None)
PlaylistFormat = Int32
PlaylistFormat_WindowsMedia: PlaylistFormat = 0
PlaylistFormat_Zune: PlaylistFormat = 1
PlaylistFormat_M3u: PlaylistFormat = 2
PlaylistsContract: UInt32 = 65536
make_head(_module, 'IPlaylist')
make_head(_module, 'IPlaylistStatics')
make_head(_module, 'Playlist')
