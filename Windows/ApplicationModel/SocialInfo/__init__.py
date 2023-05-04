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
import Windows.ApplicationModel.SocialInfo
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Graphics.Imaging
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
class ISocialFeedChildItem(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.SocialInfo.ISocialFeedChildItem'
    _iid_ = Guid('{0b6a985a-d59d-40be-980c-488a2ab30a83}')
    @winrt_commethod(6)
    def get_Author(self) -> Windows.ApplicationModel.SocialInfo.SocialUserInfo: ...
    @winrt_commethod(7)
    def get_PrimaryContent(self) -> Windows.ApplicationModel.SocialInfo.SocialFeedContent: ...
    @winrt_commethod(8)
    def get_SecondaryContent(self) -> Windows.ApplicationModel.SocialInfo.SocialFeedContent: ...
    @winrt_commethod(9)
    def get_Timestamp(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(10)
    def put_Timestamp(self, value: Windows.Foundation.DateTime) -> Void: ...
    @winrt_commethod(11)
    def get_TargetUri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(12)
    def put_TargetUri(self, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(13)
    def get_Thumbnails(self) -> Windows.Foundation.Collections.IVector[Windows.ApplicationModel.SocialInfo.SocialItemThumbnail]: ...
    @winrt_commethod(14)
    def get_SharedItem(self) -> Windows.ApplicationModel.SocialInfo.SocialFeedSharedItem: ...
    @winrt_commethod(15)
    def put_SharedItem(self, value: Windows.ApplicationModel.SocialInfo.SocialFeedSharedItem) -> Void: ...
    Author = property(get_Author, None)
    PrimaryContent = property(get_PrimaryContent, None)
    SecondaryContent = property(get_SecondaryContent, None)
    Timestamp = property(get_Timestamp, put_Timestamp)
    TargetUri = property(get_TargetUri, put_TargetUri)
    Thumbnails = property(get_Thumbnails, None)
    SharedItem = property(get_SharedItem, put_SharedItem)
class ISocialFeedContent(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.SocialInfo.ISocialFeedContent'
    _iid_ = Guid('{a234e429-3e39-494d-a37c-f462a2494514}')
    @winrt_commethod(6)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Title(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Message(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Message(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_TargetUri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(11)
    def put_TargetUri(self, value: Windows.Foundation.Uri) -> Void: ...
    Title = property(get_Title, put_Title)
    Message = property(get_Message, put_Message)
    TargetUri = property(get_TargetUri, put_TargetUri)
class ISocialFeedItem(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.SocialInfo.ISocialFeedItem'
    _iid_ = Guid('{4f1392ab-1f72-4d33-b695-de3e1db60317}')
    @winrt_commethod(6)
    def get_Author(self) -> Windows.ApplicationModel.SocialInfo.SocialUserInfo: ...
    @winrt_commethod(7)
    def get_PrimaryContent(self) -> Windows.ApplicationModel.SocialInfo.SocialFeedContent: ...
    @winrt_commethod(8)
    def get_SecondaryContent(self) -> Windows.ApplicationModel.SocialInfo.SocialFeedContent: ...
    @winrt_commethod(9)
    def get_Timestamp(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(10)
    def put_Timestamp(self, value: Windows.Foundation.DateTime) -> Void: ...
    @winrt_commethod(11)
    def get_TargetUri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(12)
    def put_TargetUri(self, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(13)
    def get_Thumbnails(self) -> Windows.Foundation.Collections.IVector[Windows.ApplicationModel.SocialInfo.SocialItemThumbnail]: ...
    @winrt_commethod(14)
    def get_SharedItem(self) -> Windows.ApplicationModel.SocialInfo.SocialFeedSharedItem: ...
    @winrt_commethod(15)
    def put_SharedItem(self, value: Windows.ApplicationModel.SocialInfo.SocialFeedSharedItem) -> Void: ...
    @winrt_commethod(16)
    def get_BadgeStyle(self) -> Windows.ApplicationModel.SocialInfo.SocialItemBadgeStyle: ...
    @winrt_commethod(17)
    def put_BadgeStyle(self, value: Windows.ApplicationModel.SocialInfo.SocialItemBadgeStyle) -> Void: ...
    @winrt_commethod(18)
    def get_BadgeCountValue(self) -> Int32: ...
    @winrt_commethod(19)
    def put_BadgeCountValue(self, value: Int32) -> Void: ...
    @winrt_commethod(20)
    def get_RemoteId(self) -> WinRT_String: ...
    @winrt_commethod(21)
    def put_RemoteId(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(22)
    def get_ChildItem(self) -> Windows.ApplicationModel.SocialInfo.SocialFeedChildItem: ...
    @winrt_commethod(23)
    def put_ChildItem(self, value: Windows.ApplicationModel.SocialInfo.SocialFeedChildItem) -> Void: ...
    @winrt_commethod(24)
    def get_Style(self) -> Windows.ApplicationModel.SocialInfo.SocialFeedItemStyle: ...
    @winrt_commethod(25)
    def put_Style(self, value: Windows.ApplicationModel.SocialInfo.SocialFeedItemStyle) -> Void: ...
    Author = property(get_Author, None)
    PrimaryContent = property(get_PrimaryContent, None)
    SecondaryContent = property(get_SecondaryContent, None)
    Timestamp = property(get_Timestamp, put_Timestamp)
    TargetUri = property(get_TargetUri, put_TargetUri)
    Thumbnails = property(get_Thumbnails, None)
    SharedItem = property(get_SharedItem, put_SharedItem)
    BadgeStyle = property(get_BadgeStyle, put_BadgeStyle)
    BadgeCountValue = property(get_BadgeCountValue, put_BadgeCountValue)
    RemoteId = property(get_RemoteId, put_RemoteId)
    ChildItem = property(get_ChildItem, put_ChildItem)
    Style = property(get_Style, put_Style)
class ISocialFeedSharedItem(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.SocialInfo.ISocialFeedSharedItem'
    _iid_ = Guid('{7bfb9e40-a6aa-45a7-9ff6-54c42105dd1f}')
    @winrt_commethod(6)
    def get_OriginalSource(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def put_OriginalSource(self, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(8)
    def get_Content(self) -> Windows.ApplicationModel.SocialInfo.SocialFeedContent: ...
    @winrt_commethod(9)
    def get_Timestamp(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(10)
    def put_Timestamp(self, value: Windows.Foundation.DateTime) -> Void: ...
    @winrt_commethod(11)
    def get_TargetUri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(12)
    def put_TargetUri(self, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(13)
    def put_Thumbnail(self, value: Windows.ApplicationModel.SocialInfo.SocialItemThumbnail) -> Void: ...
    @winrt_commethod(14)
    def get_Thumbnail(self) -> Windows.ApplicationModel.SocialInfo.SocialItemThumbnail: ...
    OriginalSource = property(get_OriginalSource, put_OriginalSource)
    Content = property(get_Content, None)
    Timestamp = property(get_Timestamp, put_Timestamp)
    TargetUri = property(get_TargetUri, put_TargetUri)
    Thumbnail = property(get_Thumbnail, put_Thumbnail)
class ISocialItemThumbnail(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.SocialInfo.ISocialItemThumbnail'
    _iid_ = Guid('{5cbf831a-3f08-497f-917f-57e09d84b141}')
    @winrt_commethod(6)
    def get_TargetUri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def put_TargetUri(self, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(8)
    def get_ImageUri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(9)
    def put_ImageUri(self, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(10)
    def get_BitmapSize(self) -> Windows.Graphics.Imaging.BitmapSize: ...
    @winrt_commethod(11)
    def put_BitmapSize(self, value: Windows.Graphics.Imaging.BitmapSize) -> Void: ...
    @winrt_commethod(12)
    def SetImageAsync(self, image: Windows.Storage.Streams.IInputStream) -> Windows.Foundation.IAsyncAction: ...
    TargetUri = property(get_TargetUri, put_TargetUri)
    ImageUri = property(get_ImageUri, put_ImageUri)
    BitmapSize = property(get_BitmapSize, put_BitmapSize)
class ISocialUserInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.SocialInfo.ISocialUserInfo'
    _iid_ = Guid('{9e5e1bd1-90d0-4e1d-9554-844d46607f61}')
    @winrt_commethod(6)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_DisplayName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_UserName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_UserName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_RemoteId(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_RemoteId(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_TargetUri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(13)
    def put_TargetUri(self, value: Windows.Foundation.Uri) -> Void: ...
    DisplayName = property(get_DisplayName, put_DisplayName)
    UserName = property(get_UserName, put_UserName)
    RemoteId = property(get_RemoteId, put_RemoteId)
    TargetUri = property(get_TargetUri, put_TargetUri)
class SocialFeedChildItem(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.SocialInfo.ISocialFeedChildItem
    _classid_ = 'Windows.ApplicationModel.SocialInfo.SocialFeedChildItem'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.SocialInfo.SocialFeedChildItem: ...
    @winrt_mixinmethod
    def get_Author(self: Windows.ApplicationModel.SocialInfo.ISocialFeedChildItem) -> Windows.ApplicationModel.SocialInfo.SocialUserInfo: ...
    @winrt_mixinmethod
    def get_PrimaryContent(self: Windows.ApplicationModel.SocialInfo.ISocialFeedChildItem) -> Windows.ApplicationModel.SocialInfo.SocialFeedContent: ...
    @winrt_mixinmethod
    def get_SecondaryContent(self: Windows.ApplicationModel.SocialInfo.ISocialFeedChildItem) -> Windows.ApplicationModel.SocialInfo.SocialFeedContent: ...
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.ApplicationModel.SocialInfo.ISocialFeedChildItem) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def put_Timestamp(self: Windows.ApplicationModel.SocialInfo.ISocialFeedChildItem, value: Windows.Foundation.DateTime) -> Void: ...
    @winrt_mixinmethod
    def get_TargetUri(self: Windows.ApplicationModel.SocialInfo.ISocialFeedChildItem) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_TargetUri(self: Windows.ApplicationModel.SocialInfo.ISocialFeedChildItem, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_Thumbnails(self: Windows.ApplicationModel.SocialInfo.ISocialFeedChildItem) -> Windows.Foundation.Collections.IVector[Windows.ApplicationModel.SocialInfo.SocialItemThumbnail]: ...
    @winrt_mixinmethod
    def get_SharedItem(self: Windows.ApplicationModel.SocialInfo.ISocialFeedChildItem) -> Windows.ApplicationModel.SocialInfo.SocialFeedSharedItem: ...
    @winrt_mixinmethod
    def put_SharedItem(self: Windows.ApplicationModel.SocialInfo.ISocialFeedChildItem, value: Windows.ApplicationModel.SocialInfo.SocialFeedSharedItem) -> Void: ...
    Author = property(get_Author, None)
    PrimaryContent = property(get_PrimaryContent, None)
    SecondaryContent = property(get_SecondaryContent, None)
    Timestamp = property(get_Timestamp, put_Timestamp)
    TargetUri = property(get_TargetUri, put_TargetUri)
    Thumbnails = property(get_Thumbnails, None)
    SharedItem = property(get_SharedItem, put_SharedItem)
class SocialFeedContent(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.SocialInfo.ISocialFeedContent
    _classid_ = 'Windows.ApplicationModel.SocialInfo.SocialFeedContent'
    @winrt_mixinmethod
    def get_Title(self: Windows.ApplicationModel.SocialInfo.ISocialFeedContent) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Title(self: Windows.ApplicationModel.SocialInfo.ISocialFeedContent, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Message(self: Windows.ApplicationModel.SocialInfo.ISocialFeedContent) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Message(self: Windows.ApplicationModel.SocialInfo.ISocialFeedContent, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_TargetUri(self: Windows.ApplicationModel.SocialInfo.ISocialFeedContent) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_TargetUri(self: Windows.ApplicationModel.SocialInfo.ISocialFeedContent, value: Windows.Foundation.Uri) -> Void: ...
    Title = property(get_Title, put_Title)
    Message = property(get_Message, put_Message)
    TargetUri = property(get_TargetUri, put_TargetUri)
class SocialFeedItem(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.SocialInfo.ISocialFeedItem
    _classid_ = 'Windows.ApplicationModel.SocialInfo.SocialFeedItem'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.SocialInfo.SocialFeedItem: ...
    @winrt_mixinmethod
    def get_Author(self: Windows.ApplicationModel.SocialInfo.ISocialFeedItem) -> Windows.ApplicationModel.SocialInfo.SocialUserInfo: ...
    @winrt_mixinmethod
    def get_PrimaryContent(self: Windows.ApplicationModel.SocialInfo.ISocialFeedItem) -> Windows.ApplicationModel.SocialInfo.SocialFeedContent: ...
    @winrt_mixinmethod
    def get_SecondaryContent(self: Windows.ApplicationModel.SocialInfo.ISocialFeedItem) -> Windows.ApplicationModel.SocialInfo.SocialFeedContent: ...
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.ApplicationModel.SocialInfo.ISocialFeedItem) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def put_Timestamp(self: Windows.ApplicationModel.SocialInfo.ISocialFeedItem, value: Windows.Foundation.DateTime) -> Void: ...
    @winrt_mixinmethod
    def get_TargetUri(self: Windows.ApplicationModel.SocialInfo.ISocialFeedItem) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_TargetUri(self: Windows.ApplicationModel.SocialInfo.ISocialFeedItem, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_Thumbnails(self: Windows.ApplicationModel.SocialInfo.ISocialFeedItem) -> Windows.Foundation.Collections.IVector[Windows.ApplicationModel.SocialInfo.SocialItemThumbnail]: ...
    @winrt_mixinmethod
    def get_SharedItem(self: Windows.ApplicationModel.SocialInfo.ISocialFeedItem) -> Windows.ApplicationModel.SocialInfo.SocialFeedSharedItem: ...
    @winrt_mixinmethod
    def put_SharedItem(self: Windows.ApplicationModel.SocialInfo.ISocialFeedItem, value: Windows.ApplicationModel.SocialInfo.SocialFeedSharedItem) -> Void: ...
    @winrt_mixinmethod
    def get_BadgeStyle(self: Windows.ApplicationModel.SocialInfo.ISocialFeedItem) -> Windows.ApplicationModel.SocialInfo.SocialItemBadgeStyle: ...
    @winrt_mixinmethod
    def put_BadgeStyle(self: Windows.ApplicationModel.SocialInfo.ISocialFeedItem, value: Windows.ApplicationModel.SocialInfo.SocialItemBadgeStyle) -> Void: ...
    @winrt_mixinmethod
    def get_BadgeCountValue(self: Windows.ApplicationModel.SocialInfo.ISocialFeedItem) -> Int32: ...
    @winrt_mixinmethod
    def put_BadgeCountValue(self: Windows.ApplicationModel.SocialInfo.ISocialFeedItem, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_RemoteId(self: Windows.ApplicationModel.SocialInfo.ISocialFeedItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_RemoteId(self: Windows.ApplicationModel.SocialInfo.ISocialFeedItem, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ChildItem(self: Windows.ApplicationModel.SocialInfo.ISocialFeedItem) -> Windows.ApplicationModel.SocialInfo.SocialFeedChildItem: ...
    @winrt_mixinmethod
    def put_ChildItem(self: Windows.ApplicationModel.SocialInfo.ISocialFeedItem, value: Windows.ApplicationModel.SocialInfo.SocialFeedChildItem) -> Void: ...
    @winrt_mixinmethod
    def get_Style(self: Windows.ApplicationModel.SocialInfo.ISocialFeedItem) -> Windows.ApplicationModel.SocialInfo.SocialFeedItemStyle: ...
    @winrt_mixinmethod
    def put_Style(self: Windows.ApplicationModel.SocialInfo.ISocialFeedItem, value: Windows.ApplicationModel.SocialInfo.SocialFeedItemStyle) -> Void: ...
    Author = property(get_Author, None)
    PrimaryContent = property(get_PrimaryContent, None)
    SecondaryContent = property(get_SecondaryContent, None)
    Timestamp = property(get_Timestamp, put_Timestamp)
    TargetUri = property(get_TargetUri, put_TargetUri)
    Thumbnails = property(get_Thumbnails, None)
    SharedItem = property(get_SharedItem, put_SharedItem)
    BadgeStyle = property(get_BadgeStyle, put_BadgeStyle)
    BadgeCountValue = property(get_BadgeCountValue, put_BadgeCountValue)
    RemoteId = property(get_RemoteId, put_RemoteId)
    ChildItem = property(get_ChildItem, put_ChildItem)
    Style = property(get_Style, put_Style)
SocialFeedItemStyle = Int32
SocialFeedItemStyle_Default: SocialFeedItemStyle = 0
SocialFeedItemStyle_Photo: SocialFeedItemStyle = 1
SocialFeedKind = Int32
SocialFeedKind_HomeFeed: SocialFeedKind = 0
SocialFeedKind_ContactFeed: SocialFeedKind = 1
SocialFeedKind_Dashboard: SocialFeedKind = 2
class SocialFeedSharedItem(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.SocialInfo.ISocialFeedSharedItem
    _classid_ = 'Windows.ApplicationModel.SocialInfo.SocialFeedSharedItem'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.SocialInfo.SocialFeedSharedItem: ...
    @winrt_mixinmethod
    def get_OriginalSource(self: Windows.ApplicationModel.SocialInfo.ISocialFeedSharedItem) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_OriginalSource(self: Windows.ApplicationModel.SocialInfo.ISocialFeedSharedItem, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_Content(self: Windows.ApplicationModel.SocialInfo.ISocialFeedSharedItem) -> Windows.ApplicationModel.SocialInfo.SocialFeedContent: ...
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.ApplicationModel.SocialInfo.ISocialFeedSharedItem) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def put_Timestamp(self: Windows.ApplicationModel.SocialInfo.ISocialFeedSharedItem, value: Windows.Foundation.DateTime) -> Void: ...
    @winrt_mixinmethod
    def get_TargetUri(self: Windows.ApplicationModel.SocialInfo.ISocialFeedSharedItem) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_TargetUri(self: Windows.ApplicationModel.SocialInfo.ISocialFeedSharedItem, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def put_Thumbnail(self: Windows.ApplicationModel.SocialInfo.ISocialFeedSharedItem, value: Windows.ApplicationModel.SocialInfo.SocialItemThumbnail) -> Void: ...
    @winrt_mixinmethod
    def get_Thumbnail(self: Windows.ApplicationModel.SocialInfo.ISocialFeedSharedItem) -> Windows.ApplicationModel.SocialInfo.SocialItemThumbnail: ...
    OriginalSource = property(get_OriginalSource, put_OriginalSource)
    Content = property(get_Content, None)
    Timestamp = property(get_Timestamp, put_Timestamp)
    TargetUri = property(get_TargetUri, put_TargetUri)
    Thumbnail = property(get_Thumbnail, put_Thumbnail)
SocialFeedUpdateMode = Int32
SocialFeedUpdateMode_Append: SocialFeedUpdateMode = 0
SocialFeedUpdateMode_Replace: SocialFeedUpdateMode = 1
SocialInfoContract: UInt32 = 131072
SocialItemBadgeStyle = Int32
SocialItemBadgeStyle_Hidden: SocialItemBadgeStyle = 0
SocialItemBadgeStyle_Visible: SocialItemBadgeStyle = 1
SocialItemBadgeStyle_VisibleWithCount: SocialItemBadgeStyle = 2
class SocialItemThumbnail(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.SocialInfo.ISocialItemThumbnail
    _classid_ = 'Windows.ApplicationModel.SocialInfo.SocialItemThumbnail'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.SocialInfo.SocialItemThumbnail: ...
    @winrt_mixinmethod
    def get_TargetUri(self: Windows.ApplicationModel.SocialInfo.ISocialItemThumbnail) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_TargetUri(self: Windows.ApplicationModel.SocialInfo.ISocialItemThumbnail, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_ImageUri(self: Windows.ApplicationModel.SocialInfo.ISocialItemThumbnail) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_ImageUri(self: Windows.ApplicationModel.SocialInfo.ISocialItemThumbnail, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_BitmapSize(self: Windows.ApplicationModel.SocialInfo.ISocialItemThumbnail) -> Windows.Graphics.Imaging.BitmapSize: ...
    @winrt_mixinmethod
    def put_BitmapSize(self: Windows.ApplicationModel.SocialInfo.ISocialItemThumbnail, value: Windows.Graphics.Imaging.BitmapSize) -> Void: ...
    @winrt_mixinmethod
    def SetImageAsync(self: Windows.ApplicationModel.SocialInfo.ISocialItemThumbnail, image: Windows.Storage.Streams.IInputStream) -> Windows.Foundation.IAsyncAction: ...
    TargetUri = property(get_TargetUri, put_TargetUri)
    ImageUri = property(get_ImageUri, put_ImageUri)
    BitmapSize = property(get_BitmapSize, put_BitmapSize)
class SocialUserInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.SocialInfo.ISocialUserInfo
    _classid_ = 'Windows.ApplicationModel.SocialInfo.SocialUserInfo'
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.ApplicationModel.SocialInfo.ISocialUserInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayName(self: Windows.ApplicationModel.SocialInfo.ISocialUserInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_UserName(self: Windows.ApplicationModel.SocialInfo.ISocialUserInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_UserName(self: Windows.ApplicationModel.SocialInfo.ISocialUserInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_RemoteId(self: Windows.ApplicationModel.SocialInfo.ISocialUserInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_RemoteId(self: Windows.ApplicationModel.SocialInfo.ISocialUserInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_TargetUri(self: Windows.ApplicationModel.SocialInfo.ISocialUserInfo) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_TargetUri(self: Windows.ApplicationModel.SocialInfo.ISocialUserInfo, value: Windows.Foundation.Uri) -> Void: ...
    DisplayName = property(get_DisplayName, put_DisplayName)
    UserName = property(get_UserName, put_UserName)
    RemoteId = property(get_RemoteId, put_RemoteId)
    TargetUri = property(get_TargetUri, put_TargetUri)
make_head(_module, 'ISocialFeedChildItem')
make_head(_module, 'ISocialFeedContent')
make_head(_module, 'ISocialFeedItem')
make_head(_module, 'ISocialFeedSharedItem')
make_head(_module, 'ISocialItemThumbnail')
make_head(_module, 'ISocialUserInfo')
make_head(_module, 'SocialFeedChildItem')
make_head(_module, 'SocialFeedContent')
make_head(_module, 'SocialFeedItem')
make_head(_module, 'SocialFeedSharedItem')
make_head(_module, 'SocialItemThumbnail')
make_head(_module, 'SocialUserInfo')
