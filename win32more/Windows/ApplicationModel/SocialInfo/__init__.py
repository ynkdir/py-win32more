from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel.SocialInfo
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Graphics.Imaging
import win32more.Windows.Storage.Streams
import win32more.Windows.Win32.System.WinRT
class ISocialFeedChildItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.SocialInfo.ISocialFeedChildItem'
    _iid_ = Guid('{0b6a985a-d59d-40be-980c-488a2ab30a83}')
    @winrt_commethod(6)
    def get_Author(self) -> win32more.Windows.ApplicationModel.SocialInfo.SocialUserInfo: ...
    @winrt_commethod(7)
    def get_PrimaryContent(self) -> win32more.Windows.ApplicationModel.SocialInfo.SocialFeedContent: ...
    @winrt_commethod(8)
    def get_SecondaryContent(self) -> win32more.Windows.ApplicationModel.SocialInfo.SocialFeedContent: ...
    @winrt_commethod(9)
    def get_Timestamp(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(10)
    def put_Timestamp(self, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    @winrt_commethod(11)
    def get_TargetUri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(12)
    def put_TargetUri(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(13)
    def get_Thumbnails(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.SocialInfo.SocialItemThumbnail]: ...
    @winrt_commethod(14)
    def get_SharedItem(self) -> win32more.Windows.ApplicationModel.SocialInfo.SocialFeedSharedItem: ...
    @winrt_commethod(15)
    def put_SharedItem(self, value: win32more.Windows.ApplicationModel.SocialInfo.SocialFeedSharedItem) -> Void: ...
    Author = property(get_Author, None)
    PrimaryContent = property(get_PrimaryContent, None)
    SecondaryContent = property(get_SecondaryContent, None)
    SharedItem = property(get_SharedItem, put_SharedItem)
    TargetUri = property(get_TargetUri, put_TargetUri)
    Thumbnails = property(get_Thumbnails, None)
    Timestamp = property(get_Timestamp, put_Timestamp)
class ISocialFeedContent(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    def get_TargetUri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(11)
    def put_TargetUri(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    Message = property(get_Message, put_Message)
    TargetUri = property(get_TargetUri, put_TargetUri)
    Title = property(get_Title, put_Title)
class ISocialFeedItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.SocialInfo.ISocialFeedItem'
    _iid_ = Guid('{4f1392ab-1f72-4d33-b695-de3e1db60317}')
    @winrt_commethod(6)
    def get_Author(self) -> win32more.Windows.ApplicationModel.SocialInfo.SocialUserInfo: ...
    @winrt_commethod(7)
    def get_PrimaryContent(self) -> win32more.Windows.ApplicationModel.SocialInfo.SocialFeedContent: ...
    @winrt_commethod(8)
    def get_SecondaryContent(self) -> win32more.Windows.ApplicationModel.SocialInfo.SocialFeedContent: ...
    @winrt_commethod(9)
    def get_Timestamp(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(10)
    def put_Timestamp(self, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    @winrt_commethod(11)
    def get_TargetUri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(12)
    def put_TargetUri(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(13)
    def get_Thumbnails(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.SocialInfo.SocialItemThumbnail]: ...
    @winrt_commethod(14)
    def get_SharedItem(self) -> win32more.Windows.ApplicationModel.SocialInfo.SocialFeedSharedItem: ...
    @winrt_commethod(15)
    def put_SharedItem(self, value: win32more.Windows.ApplicationModel.SocialInfo.SocialFeedSharedItem) -> Void: ...
    @winrt_commethod(16)
    def get_BadgeStyle(self) -> win32more.Windows.ApplicationModel.SocialInfo.SocialItemBadgeStyle: ...
    @winrt_commethod(17)
    def put_BadgeStyle(self, value: win32more.Windows.ApplicationModel.SocialInfo.SocialItemBadgeStyle) -> Void: ...
    @winrt_commethod(18)
    def get_BadgeCountValue(self) -> Int32: ...
    @winrt_commethod(19)
    def put_BadgeCountValue(self, value: Int32) -> Void: ...
    @winrt_commethod(20)
    def get_RemoteId(self) -> WinRT_String: ...
    @winrt_commethod(21)
    def put_RemoteId(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(22)
    def get_ChildItem(self) -> win32more.Windows.ApplicationModel.SocialInfo.SocialFeedChildItem: ...
    @winrt_commethod(23)
    def put_ChildItem(self, value: win32more.Windows.ApplicationModel.SocialInfo.SocialFeedChildItem) -> Void: ...
    @winrt_commethod(24)
    def get_Style(self) -> win32more.Windows.ApplicationModel.SocialInfo.SocialFeedItemStyle: ...
    @winrt_commethod(25)
    def put_Style(self, value: win32more.Windows.ApplicationModel.SocialInfo.SocialFeedItemStyle) -> Void: ...
    Author = property(get_Author, None)
    BadgeCountValue = property(get_BadgeCountValue, put_BadgeCountValue)
    BadgeStyle = property(get_BadgeStyle, put_BadgeStyle)
    ChildItem = property(get_ChildItem, put_ChildItem)
    PrimaryContent = property(get_PrimaryContent, None)
    RemoteId = property(get_RemoteId, put_RemoteId)
    SecondaryContent = property(get_SecondaryContent, None)
    SharedItem = property(get_SharedItem, put_SharedItem)
    Style = property(get_Style, put_Style)
    TargetUri = property(get_TargetUri, put_TargetUri)
    Thumbnails = property(get_Thumbnails, None)
    Timestamp = property(get_Timestamp, put_Timestamp)
class ISocialFeedSharedItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.SocialInfo.ISocialFeedSharedItem'
    _iid_ = Guid('{7bfb9e40-a6aa-45a7-9ff6-54c42105dd1f}')
    @winrt_commethod(6)
    def get_OriginalSource(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def put_OriginalSource(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(8)
    def get_Content(self) -> win32more.Windows.ApplicationModel.SocialInfo.SocialFeedContent: ...
    @winrt_commethod(9)
    def get_Timestamp(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(10)
    def put_Timestamp(self, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    @winrt_commethod(11)
    def get_TargetUri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(12)
    def put_TargetUri(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(13)
    def put_Thumbnail(self, value: win32more.Windows.ApplicationModel.SocialInfo.SocialItemThumbnail) -> Void: ...
    @winrt_commethod(14)
    def get_Thumbnail(self) -> win32more.Windows.ApplicationModel.SocialInfo.SocialItemThumbnail: ...
    Content = property(get_Content, None)
    OriginalSource = property(get_OriginalSource, put_OriginalSource)
    TargetUri = property(get_TargetUri, put_TargetUri)
    Thumbnail = property(get_Thumbnail, put_Thumbnail)
    Timestamp = property(get_Timestamp, put_Timestamp)
class ISocialItemThumbnail(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.SocialInfo.ISocialItemThumbnail'
    _iid_ = Guid('{5cbf831a-3f08-497f-917f-57e09d84b141}')
    @winrt_commethod(6)
    def get_TargetUri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def put_TargetUri(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(8)
    def get_ImageUri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(9)
    def put_ImageUri(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(10)
    def get_BitmapSize(self) -> win32more.Windows.Graphics.Imaging.BitmapSize: ...
    @winrt_commethod(11)
    def put_BitmapSize(self, value: win32more.Windows.Graphics.Imaging.BitmapSize) -> Void: ...
    @winrt_commethod(12)
    def SetImageAsync(self, image: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Windows.Foundation.IAsyncAction: ...
    BitmapSize = property(get_BitmapSize, put_BitmapSize)
    ImageUri = property(get_ImageUri, put_ImageUri)
    TargetUri = property(get_TargetUri, put_TargetUri)
class ISocialUserInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    def get_TargetUri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(13)
    def put_TargetUri(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    DisplayName = property(get_DisplayName, put_DisplayName)
    RemoteId = property(get_RemoteId, put_RemoteId)
    TargetUri = property(get_TargetUri, put_TargetUri)
    UserName = property(get_UserName, put_UserName)
class SocialFeedChildItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedChildItem
    _classid_ = 'Windows.ApplicationModel.SocialInfo.SocialFeedChildItem'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.SocialInfo.SocialFeedChildItem.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.SocialInfo.SocialFeedChildItem: ...
    @winrt_mixinmethod
    def get_Author(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedChildItem) -> win32more.Windows.ApplicationModel.SocialInfo.SocialUserInfo: ...
    @winrt_mixinmethod
    def get_PrimaryContent(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedChildItem) -> win32more.Windows.ApplicationModel.SocialInfo.SocialFeedContent: ...
    @winrt_mixinmethod
    def get_SecondaryContent(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedChildItem) -> win32more.Windows.ApplicationModel.SocialInfo.SocialFeedContent: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedChildItem) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def put_Timestamp(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedChildItem, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    @winrt_mixinmethod
    def get_TargetUri(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedChildItem) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_TargetUri(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedChildItem, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_Thumbnails(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedChildItem) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.SocialInfo.SocialItemThumbnail]: ...
    @winrt_mixinmethod
    def get_SharedItem(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedChildItem) -> win32more.Windows.ApplicationModel.SocialInfo.SocialFeedSharedItem: ...
    @winrt_mixinmethod
    def put_SharedItem(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedChildItem, value: win32more.Windows.ApplicationModel.SocialInfo.SocialFeedSharedItem) -> Void: ...
    Author = property(get_Author, None)
    PrimaryContent = property(get_PrimaryContent, None)
    SecondaryContent = property(get_SecondaryContent, None)
    SharedItem = property(get_SharedItem, put_SharedItem)
    TargetUri = property(get_TargetUri, put_TargetUri)
    Thumbnails = property(get_Thumbnails, None)
    Timestamp = property(get_Timestamp, put_Timestamp)
class SocialFeedContent(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedContent
    _classid_ = 'Windows.ApplicationModel.SocialInfo.SocialFeedContent'
    @winrt_mixinmethod
    def get_Title(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedContent) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Title(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedContent, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Message(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedContent) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Message(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedContent, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_TargetUri(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedContent) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_TargetUri(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedContent, value: win32more.Windows.Foundation.Uri) -> Void: ...
    Message = property(get_Message, put_Message)
    TargetUri = property(get_TargetUri, put_TargetUri)
    Title = property(get_Title, put_Title)
class SocialFeedItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedItem
    _classid_ = 'Windows.ApplicationModel.SocialInfo.SocialFeedItem'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.SocialInfo.SocialFeedItem.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.SocialInfo.SocialFeedItem: ...
    @winrt_mixinmethod
    def get_Author(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedItem) -> win32more.Windows.ApplicationModel.SocialInfo.SocialUserInfo: ...
    @winrt_mixinmethod
    def get_PrimaryContent(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedItem) -> win32more.Windows.ApplicationModel.SocialInfo.SocialFeedContent: ...
    @winrt_mixinmethod
    def get_SecondaryContent(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedItem) -> win32more.Windows.ApplicationModel.SocialInfo.SocialFeedContent: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedItem) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def put_Timestamp(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedItem, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    @winrt_mixinmethod
    def get_TargetUri(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedItem) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_TargetUri(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedItem, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_Thumbnails(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedItem) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.SocialInfo.SocialItemThumbnail]: ...
    @winrt_mixinmethod
    def get_SharedItem(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedItem) -> win32more.Windows.ApplicationModel.SocialInfo.SocialFeedSharedItem: ...
    @winrt_mixinmethod
    def put_SharedItem(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedItem, value: win32more.Windows.ApplicationModel.SocialInfo.SocialFeedSharedItem) -> Void: ...
    @winrt_mixinmethod
    def get_BadgeStyle(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedItem) -> win32more.Windows.ApplicationModel.SocialInfo.SocialItemBadgeStyle: ...
    @winrt_mixinmethod
    def put_BadgeStyle(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedItem, value: win32more.Windows.ApplicationModel.SocialInfo.SocialItemBadgeStyle) -> Void: ...
    @winrt_mixinmethod
    def get_BadgeCountValue(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedItem) -> Int32: ...
    @winrt_mixinmethod
    def put_BadgeCountValue(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedItem, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_RemoteId(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_RemoteId(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedItem, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ChildItem(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedItem) -> win32more.Windows.ApplicationModel.SocialInfo.SocialFeedChildItem: ...
    @winrt_mixinmethod
    def put_ChildItem(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedItem, value: win32more.Windows.ApplicationModel.SocialInfo.SocialFeedChildItem) -> Void: ...
    @winrt_mixinmethod
    def get_Style(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedItem) -> win32more.Windows.ApplicationModel.SocialInfo.SocialFeedItemStyle: ...
    @winrt_mixinmethod
    def put_Style(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedItem, value: win32more.Windows.ApplicationModel.SocialInfo.SocialFeedItemStyle) -> Void: ...
    Author = property(get_Author, None)
    BadgeCountValue = property(get_BadgeCountValue, put_BadgeCountValue)
    BadgeStyle = property(get_BadgeStyle, put_BadgeStyle)
    ChildItem = property(get_ChildItem, put_ChildItem)
    PrimaryContent = property(get_PrimaryContent, None)
    RemoteId = property(get_RemoteId, put_RemoteId)
    SecondaryContent = property(get_SecondaryContent, None)
    SharedItem = property(get_SharedItem, put_SharedItem)
    Style = property(get_Style, put_Style)
    TargetUri = property(get_TargetUri, put_TargetUri)
    Thumbnails = property(get_Thumbnails, None)
    Timestamp = property(get_Timestamp, put_Timestamp)
class SocialFeedItemStyle(Enum, Int32):
    Default = 0
    Photo = 1
class SocialFeedKind(Enum, Int32):
    HomeFeed = 0
    ContactFeed = 1
    Dashboard = 2
class SocialFeedSharedItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedSharedItem
    _classid_ = 'Windows.ApplicationModel.SocialInfo.SocialFeedSharedItem'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.SocialInfo.SocialFeedSharedItem.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.SocialInfo.SocialFeedSharedItem: ...
    @winrt_mixinmethod
    def get_OriginalSource(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedSharedItem) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_OriginalSource(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedSharedItem, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_Content(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedSharedItem) -> win32more.Windows.ApplicationModel.SocialInfo.SocialFeedContent: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedSharedItem) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def put_Timestamp(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedSharedItem, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    @winrt_mixinmethod
    def get_TargetUri(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedSharedItem) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_TargetUri(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedSharedItem, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def put_Thumbnail(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedSharedItem, value: win32more.Windows.ApplicationModel.SocialInfo.SocialItemThumbnail) -> Void: ...
    @winrt_mixinmethod
    def get_Thumbnail(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialFeedSharedItem) -> win32more.Windows.ApplicationModel.SocialInfo.SocialItemThumbnail: ...
    Content = property(get_Content, None)
    OriginalSource = property(get_OriginalSource, put_OriginalSource)
    TargetUri = property(get_TargetUri, put_TargetUri)
    Thumbnail = property(get_Thumbnail, put_Thumbnail)
    Timestamp = property(get_Timestamp, put_Timestamp)
class SocialFeedUpdateMode(Enum, Int32):
    Append = 0
    Replace = 1
SocialInfoContract: UInt32 = 131072
class SocialItemBadgeStyle(Enum, Int32):
    Hidden = 0
    Visible = 1
    VisibleWithCount = 2
class SocialItemThumbnail(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.SocialInfo.ISocialItemThumbnail
    _classid_ = 'Windows.ApplicationModel.SocialInfo.SocialItemThumbnail'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.SocialInfo.SocialItemThumbnail.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.SocialInfo.SocialItemThumbnail: ...
    @winrt_mixinmethod
    def get_TargetUri(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialItemThumbnail) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_TargetUri(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialItemThumbnail, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_ImageUri(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialItemThumbnail) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_ImageUri(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialItemThumbnail, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_BitmapSize(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialItemThumbnail) -> win32more.Windows.Graphics.Imaging.BitmapSize: ...
    @winrt_mixinmethod
    def put_BitmapSize(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialItemThumbnail, value: win32more.Windows.Graphics.Imaging.BitmapSize) -> Void: ...
    @winrt_mixinmethod
    def SetImageAsync(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialItemThumbnail, image: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Windows.Foundation.IAsyncAction: ...
    BitmapSize = property(get_BitmapSize, put_BitmapSize)
    ImageUri = property(get_ImageUri, put_ImageUri)
    TargetUri = property(get_TargetUri, put_TargetUri)
class SocialUserInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.SocialInfo.ISocialUserInfo
    _classid_ = 'Windows.ApplicationModel.SocialInfo.SocialUserInfo'
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialUserInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayName(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialUserInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_UserName(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialUserInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_UserName(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialUserInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_RemoteId(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialUserInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_RemoteId(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialUserInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_TargetUri(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialUserInfo) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_TargetUri(self: win32more.Windows.ApplicationModel.SocialInfo.ISocialUserInfo, value: win32more.Windows.Foundation.Uri) -> Void: ...
    DisplayName = property(get_DisplayName, put_DisplayName)
    RemoteId = property(get_RemoteId, put_RemoteId)
    TargetUri = property(get_TargetUri, put_TargetUri)
    UserName = property(get_UserName, put_UserName)


make_ready(__name__)
