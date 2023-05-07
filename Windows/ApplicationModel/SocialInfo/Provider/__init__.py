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
import Windows.ApplicationModel.SocialInfo.Provider
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
class ISocialDashboardItemUpdater(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.SocialInfo.Provider.ISocialDashboardItemUpdater'
    _iid_ = Guid('{3cde9dc9-4800-46cd-869b-1973ec685bde}')
    @winrt_commethod(6)
    def get_OwnerRemoteId(self: Windows.ApplicationModel.SocialInfo.Provider.ISocialDashboardItemUpdater) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Content(self: Windows.ApplicationModel.SocialInfo.Provider.ISocialDashboardItemUpdater) -> Windows.ApplicationModel.SocialInfo.SocialFeedContent: ...
    @winrt_commethod(8)
    def get_Timestamp(self: Windows.ApplicationModel.SocialInfo.Provider.ISocialDashboardItemUpdater) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(9)
    def put_Timestamp(self: Windows.ApplicationModel.SocialInfo.Provider.ISocialDashboardItemUpdater, value: Windows.Foundation.DateTime) -> Void: ...
    @winrt_commethod(10)
    def put_Thumbnail(self: Windows.ApplicationModel.SocialInfo.Provider.ISocialDashboardItemUpdater, value: Windows.ApplicationModel.SocialInfo.SocialItemThumbnail) -> Void: ...
    @winrt_commethod(11)
    def get_Thumbnail(self: Windows.ApplicationModel.SocialInfo.Provider.ISocialDashboardItemUpdater) -> Windows.ApplicationModel.SocialInfo.SocialItemThumbnail: ...
    @winrt_commethod(12)
    def CommitAsync(self: Windows.ApplicationModel.SocialInfo.Provider.ISocialDashboardItemUpdater) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(13)
    def get_TargetUri(self: Windows.ApplicationModel.SocialInfo.Provider.ISocialDashboardItemUpdater) -> Windows.Foundation.Uri: ...
    @winrt_commethod(14)
    def put_TargetUri(self: Windows.ApplicationModel.SocialInfo.Provider.ISocialDashboardItemUpdater, value: Windows.Foundation.Uri) -> Void: ...
    OwnerRemoteId = property(get_OwnerRemoteId, None)
    Content = property(get_Content, None)
    Timestamp = property(get_Timestamp, put_Timestamp)
    Thumbnail = property(get_Thumbnail, put_Thumbnail)
    TargetUri = property(get_TargetUri, put_TargetUri)
class ISocialFeedUpdater(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.SocialInfo.Provider.ISocialFeedUpdater'
    _iid_ = Guid('{7a0c0aa7-ed89-4bd5-a8d9-15f4d9861c10}')
    @winrt_commethod(6)
    def get_OwnerRemoteId(self: Windows.ApplicationModel.SocialInfo.Provider.ISocialFeedUpdater) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Kind(self: Windows.ApplicationModel.SocialInfo.Provider.ISocialFeedUpdater) -> Windows.ApplicationModel.SocialInfo.SocialFeedKind: ...
    @winrt_commethod(8)
    def get_Items(self: Windows.ApplicationModel.SocialInfo.Provider.ISocialFeedUpdater) -> Windows.Foundation.Collections.IVector[Windows.ApplicationModel.SocialInfo.SocialFeedItem]: ...
    @winrt_commethod(9)
    def CommitAsync(self: Windows.ApplicationModel.SocialInfo.Provider.ISocialFeedUpdater) -> Windows.Foundation.IAsyncAction: ...
    OwnerRemoteId = property(get_OwnerRemoteId, None)
    Kind = property(get_Kind, None)
    Items = property(get_Items, None)
class ISocialInfoProviderManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.SocialInfo.Provider.ISocialInfoProviderManagerStatics'
    _iid_ = Guid('{1b88e52b-7787-48d6-aa12-d8e8f47ab85a}')
    @winrt_commethod(6)
    def CreateSocialFeedUpdaterAsync(self: Windows.ApplicationModel.SocialInfo.Provider.ISocialInfoProviderManagerStatics, kind: Windows.ApplicationModel.SocialInfo.SocialFeedKind, mode: Windows.ApplicationModel.SocialInfo.SocialFeedUpdateMode, ownerRemoteId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.SocialInfo.Provider.SocialFeedUpdater]: ...
    @winrt_commethod(7)
    def CreateDashboardItemUpdaterAsync(self: Windows.ApplicationModel.SocialInfo.Provider.ISocialInfoProviderManagerStatics, ownerRemoteId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.SocialInfo.Provider.SocialDashboardItemUpdater]: ...
    @winrt_commethod(8)
    def UpdateBadgeCountValue(self: Windows.ApplicationModel.SocialInfo.Provider.ISocialInfoProviderManagerStatics, itemRemoteId: WinRT_String, newCount: Int32) -> Void: ...
    @winrt_commethod(9)
    def ReportNewContentAvailable(self: Windows.ApplicationModel.SocialInfo.Provider.ISocialInfoProviderManagerStatics, contactRemoteId: WinRT_String, kind: Windows.ApplicationModel.SocialInfo.SocialFeedKind) -> Void: ...
    @winrt_commethod(10)
    def ProvisionAsync(self: Windows.ApplicationModel.SocialInfo.Provider.ISocialInfoProviderManagerStatics) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(11)
    def DeprovisionAsync(self: Windows.ApplicationModel.SocialInfo.Provider.ISocialInfoProviderManagerStatics) -> Windows.Foundation.IAsyncAction: ...
class SocialDashboardItemUpdater(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.SocialInfo.Provider.ISocialDashboardItemUpdater
    _classid_ = 'Windows.ApplicationModel.SocialInfo.Provider.SocialDashboardItemUpdater'
    @winrt_mixinmethod
    def get_OwnerRemoteId(self: Windows.ApplicationModel.SocialInfo.Provider.ISocialDashboardItemUpdater) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Content(self: Windows.ApplicationModel.SocialInfo.Provider.ISocialDashboardItemUpdater) -> Windows.ApplicationModel.SocialInfo.SocialFeedContent: ...
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.ApplicationModel.SocialInfo.Provider.ISocialDashboardItemUpdater) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def put_Timestamp(self: Windows.ApplicationModel.SocialInfo.Provider.ISocialDashboardItemUpdater, value: Windows.Foundation.DateTime) -> Void: ...
    @winrt_mixinmethod
    def put_Thumbnail(self: Windows.ApplicationModel.SocialInfo.Provider.ISocialDashboardItemUpdater, value: Windows.ApplicationModel.SocialInfo.SocialItemThumbnail) -> Void: ...
    @winrt_mixinmethod
    def get_Thumbnail(self: Windows.ApplicationModel.SocialInfo.Provider.ISocialDashboardItemUpdater) -> Windows.ApplicationModel.SocialInfo.SocialItemThumbnail: ...
    @winrt_mixinmethod
    def CommitAsync(self: Windows.ApplicationModel.SocialInfo.Provider.ISocialDashboardItemUpdater) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_TargetUri(self: Windows.ApplicationModel.SocialInfo.Provider.ISocialDashboardItemUpdater) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_TargetUri(self: Windows.ApplicationModel.SocialInfo.Provider.ISocialDashboardItemUpdater, value: Windows.Foundation.Uri) -> Void: ...
    OwnerRemoteId = property(get_OwnerRemoteId, None)
    Content = property(get_Content, None)
    Timestamp = property(get_Timestamp, put_Timestamp)
    Thumbnail = property(get_Thumbnail, put_Thumbnail)
    TargetUri = property(get_TargetUri, put_TargetUri)
class SocialFeedUpdater(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.SocialInfo.Provider.ISocialFeedUpdater
    _classid_ = 'Windows.ApplicationModel.SocialInfo.Provider.SocialFeedUpdater'
    @winrt_mixinmethod
    def get_OwnerRemoteId(self: Windows.ApplicationModel.SocialInfo.Provider.ISocialFeedUpdater) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.SocialInfo.Provider.ISocialFeedUpdater) -> Windows.ApplicationModel.SocialInfo.SocialFeedKind: ...
    @winrt_mixinmethod
    def get_Items(self: Windows.ApplicationModel.SocialInfo.Provider.ISocialFeedUpdater) -> Windows.Foundation.Collections.IVector[Windows.ApplicationModel.SocialInfo.SocialFeedItem]: ...
    @winrt_mixinmethod
    def CommitAsync(self: Windows.ApplicationModel.SocialInfo.Provider.ISocialFeedUpdater) -> Windows.Foundation.IAsyncAction: ...
    OwnerRemoteId = property(get_OwnerRemoteId, None)
    Kind = property(get_Kind, None)
    Items = property(get_Items, None)
class SocialInfoProviderManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.SocialInfo.Provider.SocialInfoProviderManager'
    @winrt_classmethod
    def CreateSocialFeedUpdaterAsync(cls: Windows.ApplicationModel.SocialInfo.Provider.ISocialInfoProviderManagerStatics, kind: Windows.ApplicationModel.SocialInfo.SocialFeedKind, mode: Windows.ApplicationModel.SocialInfo.SocialFeedUpdateMode, ownerRemoteId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.SocialInfo.Provider.SocialFeedUpdater]: ...
    @winrt_classmethod
    def CreateDashboardItemUpdaterAsync(cls: Windows.ApplicationModel.SocialInfo.Provider.ISocialInfoProviderManagerStatics, ownerRemoteId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.SocialInfo.Provider.SocialDashboardItemUpdater]: ...
    @winrt_classmethod
    def UpdateBadgeCountValue(cls: Windows.ApplicationModel.SocialInfo.Provider.ISocialInfoProviderManagerStatics, itemRemoteId: WinRT_String, newCount: Int32) -> Void: ...
    @winrt_classmethod
    def ReportNewContentAvailable(cls: Windows.ApplicationModel.SocialInfo.Provider.ISocialInfoProviderManagerStatics, contactRemoteId: WinRT_String, kind: Windows.ApplicationModel.SocialInfo.SocialFeedKind) -> Void: ...
    @winrt_classmethod
    def ProvisionAsync(cls: Windows.ApplicationModel.SocialInfo.Provider.ISocialInfoProviderManagerStatics) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def DeprovisionAsync(cls: Windows.ApplicationModel.SocialInfo.Provider.ISocialInfoProviderManagerStatics) -> Windows.Foundation.IAsyncAction: ...
make_head(_module, 'ISocialDashboardItemUpdater')
make_head(_module, 'ISocialFeedUpdater')
make_head(_module, 'ISocialInfoProviderManagerStatics')
make_head(_module, 'SocialDashboardItemUpdater')
make_head(_module, 'SocialFeedUpdater')
make_head(_module, 'SocialInfoProviderManager')
