from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
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
import win32more.Windows.Services.TargetedContent
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
class ITargetedContentAction(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.TargetedContent.ITargetedContentAction'
    _iid_ = Guid('{d75b691e-6cd6-4ca0-9d8f-4728b0b7e6b6}')
    @winrt_commethod(6)
    def InvokeAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
class ITargetedContentAvailabilityChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.TargetedContent.ITargetedContentAvailabilityChangedEventArgs'
    _iid_ = Guid('{e0f59d26-5927-4450-965c-1ceb7becde65}')
    @winrt_commethod(6)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
class ITargetedContentChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.TargetedContent.ITargetedContentChangedEventArgs'
    _iid_ = Guid('{99d488c9-587e-4586-8ef7-b54ca9453a16}')
    @winrt_commethod(6)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    @winrt_commethod(7)
    def get_HasPreviousContentExpired(self) -> Boolean: ...
    HasPreviousContentExpired = property(get_HasPreviousContentExpired, None)
class ITargetedContentCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.TargetedContent.ITargetedContentCollection'
    _iid_ = Guid('{2d4b66c5-f163-44ba-9f6e-e1a4c2bb559d}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def ReportInteraction(self, interaction: win32more.Windows.Services.TargetedContent.TargetedContentInteraction) -> Void: ...
    @winrt_commethod(8)
    def ReportCustomInteraction(self, customInteractionName: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_Path(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Properties(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Services.TargetedContent.TargetedContentValue]: ...
    @winrt_commethod(11)
    def get_Collections(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.TargetedContent.TargetedContentCollection]: ...
    @winrt_commethod(12)
    def get_Items(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.TargetedContent.TargetedContentItem]: ...
    Id = property(get_Id, None)
    Path = property(get_Path, None)
    Properties = property(get_Properties, None)
    Collections = property(get_Collections, None)
    Items = property(get_Items, None)
class ITargetedContentContainer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.TargetedContent.ITargetedContentContainer'
    _iid_ = Guid('{bc2494c9-8837-47c2-850f-d79d64595926}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Timestamp(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(8)
    def get_Availability(self) -> win32more.Windows.Services.TargetedContent.TargetedContentAvailability: ...
    @winrt_commethod(9)
    def get_Content(self) -> win32more.Windows.Services.TargetedContent.TargetedContentCollection: ...
    @winrt_commethod(10)
    def SelectSingleObject(self, path: WinRT_String) -> win32more.Windows.Services.TargetedContent.TargetedContentObject: ...
    Id = property(get_Id, None)
    Timestamp = property(get_Timestamp, None)
    Availability = property(get_Availability, None)
    Content = property(get_Content, None)
class ITargetedContentContainerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.TargetedContent.ITargetedContentContainerStatics'
    _iid_ = Guid('{5b47e7fb-2140-4c1f-a736-c59583f227d8}')
    @winrt_commethod(6)
    def GetAsync(self, contentId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.TargetedContent.TargetedContentContainer]: ...
class ITargetedContentImage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.TargetedContent.ITargetedContentImage'
    _iid_ = Guid('{a7a585d9-779f-4b1e-bbb1-8eaf53fbeab2}')
    @winrt_commethod(6)
    def get_Height(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_Width(self) -> UInt32: ...
    Height = property(get_Height, None)
    Width = property(get_Width, None)
class ITargetedContentItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.TargetedContent.ITargetedContentItem'
    _iid_ = Guid('{38168dc4-276c-4c32-96ba-565c6e406e74}')
    @winrt_commethod(6)
    def get_Path(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def ReportInteraction(self, interaction: win32more.Windows.Services.TargetedContent.TargetedContentInteraction) -> Void: ...
    @winrt_commethod(8)
    def ReportCustomInteraction(self, customInteractionName: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_State(self) -> win32more.Windows.Services.TargetedContent.TargetedContentItemState: ...
    @winrt_commethod(10)
    def get_Properties(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Services.TargetedContent.TargetedContentValue]: ...
    @winrt_commethod(11)
    def get_Collections(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.TargetedContent.TargetedContentCollection]: ...
    Path = property(get_Path, None)
    State = property(get_State, None)
    Properties = property(get_Properties, None)
    Collections = property(get_Collections, None)
class ITargetedContentItemState(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.TargetedContent.ITargetedContentItemState'
    _iid_ = Guid('{73935454-4c65-4b47-a441-472de53c79b6}')
    @winrt_commethod(6)
    def get_ShouldDisplay(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_AppInstallationState(self) -> win32more.Windows.Services.TargetedContent.TargetedContentAppInstallationState: ...
    ShouldDisplay = property(get_ShouldDisplay, None)
    AppInstallationState = property(get_AppInstallationState, None)
class ITargetedContentObject(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.TargetedContent.ITargetedContentObject'
    _iid_ = Guid('{041d7969-2212-42d1-9dfa-88a8e3033aa3}')
    @winrt_commethod(6)
    def get_ObjectKind(self) -> win32more.Windows.Services.TargetedContent.TargetedContentObjectKind: ...
    @winrt_commethod(7)
    def get_Collection(self) -> win32more.Windows.Services.TargetedContent.TargetedContentCollection: ...
    @winrt_commethod(8)
    def get_Item(self) -> win32more.Windows.Services.TargetedContent.TargetedContentItem: ...
    @winrt_commethod(9)
    def get_Value(self) -> win32more.Windows.Services.TargetedContent.TargetedContentValue: ...
    ObjectKind = property(get_ObjectKind, None)
    Collection = property(get_Collection, None)
    Item = property(get_Item, None)
    Value = property(get_Value, None)
class ITargetedContentStateChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.TargetedContent.ITargetedContentStateChangedEventArgs'
    _iid_ = Guid('{9a1cef3d-8073-4416-8df2-546835a6414f}')
    @winrt_commethod(6)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
class ITargetedContentSubscription(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.TargetedContent.ITargetedContentSubscription'
    _iid_ = Guid('{882c2c49-c652-4c7a-acad-1f7fa2986c73}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetContentContainerAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.TargetedContent.TargetedContentContainer]: ...
    @winrt_commethod(8)
    def add_ContentChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Services.TargetedContent.TargetedContentSubscription, win32more.Windows.Services.TargetedContent.TargetedContentChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_ContentChanged(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_AvailabilityChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Services.TargetedContent.TargetedContentSubscription, win32more.Windows.Services.TargetedContent.TargetedContentAvailabilityChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_AvailabilityChanged(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_StateChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Services.TargetedContent.TargetedContentSubscription, win32more.Windows.Services.TargetedContent.TargetedContentStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_StateChanged(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Id = property(get_Id, None)
class ITargetedContentSubscriptionOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.TargetedContent.ITargetedContentSubscriptionOptions'
    _iid_ = Guid('{61ee6ad0-2c83-421b-8467-413eaf1aeb97}')
    @winrt_commethod(6)
    def get_SubscriptionId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_AllowPartialContentAvailability(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_AllowPartialContentAvailability(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_CloudQueryParameters(self) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_commethod(10)
    def get_LocalFilters(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(11)
    def Update(self) -> Void: ...
    SubscriptionId = property(get_SubscriptionId, None)
    AllowPartialContentAvailability = property(get_AllowPartialContentAvailability, put_AllowPartialContentAvailability)
    CloudQueryParameters = property(get_CloudQueryParameters, None)
    LocalFilters = property(get_LocalFilters, None)
class ITargetedContentSubscriptionStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.TargetedContent.ITargetedContentSubscriptionStatics'
    _iid_ = Guid('{faddfe80-360d-4916-b53c-7ea27090d02a}')
    @winrt_commethod(6)
    def GetAsync(self, subscriptionId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.TargetedContent.TargetedContentSubscription]: ...
    @winrt_commethod(7)
    def GetOptions(self, subscriptionId: WinRT_String) -> win32more.Windows.Services.TargetedContent.TargetedContentSubscriptionOptions: ...
class ITargetedContentValue(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.TargetedContent.ITargetedContentValue'
    _iid_ = Guid('{aafde4b3-4215-4bf8-867f-43f04865f9bf}')
    @winrt_commethod(6)
    def get_ValueKind(self) -> win32more.Windows.Services.TargetedContent.TargetedContentValueKind: ...
    @winrt_commethod(7)
    def get_Path(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_String(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Uri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(10)
    def get_Number(self) -> Double: ...
    @winrt_commethod(11)
    def get_Boolean(self) -> Boolean: ...
    @winrt_commethod(12)
    def get_File(self) -> win32more.Windows.Services.TargetedContent.TargetedContentFile: ...
    @winrt_commethod(13)
    def get_ImageFile(self) -> win32more.Windows.Services.TargetedContent.TargetedContentImage: ...
    @winrt_commethod(14)
    def get_Action(self) -> win32more.Windows.Services.TargetedContent.TargetedContentAction: ...
    @winrt_commethod(15)
    def get_Strings(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(16)
    def get_Uris(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Uri]: ...
    @winrt_commethod(17)
    def get_Numbers(self) -> win32more.Windows.Foundation.Collections.IVectorView[Double]: ...
    @winrt_commethod(18)
    def get_Booleans(self) -> win32more.Windows.Foundation.Collections.IVectorView[Boolean]: ...
    @winrt_commethod(19)
    def get_Files(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.TargetedContent.TargetedContentFile]: ...
    @winrt_commethod(20)
    def get_ImageFiles(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.TargetedContent.TargetedContentImage]: ...
    @winrt_commethod(21)
    def get_Actions(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.TargetedContent.TargetedContentAction]: ...
    ValueKind = property(get_ValueKind, None)
    Path = property(get_Path, None)
    String = property(get_String, None)
    Uri = property(get_Uri, None)
    Number = property(get_Number, None)
    Boolean = property(get_Boolean, None)
    File = property(get_File, None)
    ImageFile = property(get_ImageFile, None)
    Action = property(get_Action, None)
    Strings = property(get_Strings, None)
    Uris = property(get_Uris, None)
    Numbers = property(get_Numbers, None)
    Booleans = property(get_Booleans, None)
    Files = property(get_Files, None)
    ImageFiles = property(get_ImageFiles, None)
    Actions = property(get_Actions, None)
class TargetedContentAction(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.TargetedContent.ITargetedContentAction
    _classid_ = 'Windows.Services.TargetedContent.TargetedContentAction'
    @winrt_mixinmethod
    def InvokeAsync(self: win32more.Windows.Services.TargetedContent.ITargetedContentAction) -> win32more.Windows.Foundation.IAsyncAction: ...
TargetedContentAppInstallationState = Int32
TargetedContentAppInstallationState_NotApplicable: TargetedContentAppInstallationState = 0
TargetedContentAppInstallationState_NotInstalled: TargetedContentAppInstallationState = 1
TargetedContentAppInstallationState_Installed: TargetedContentAppInstallationState = 2
TargetedContentAvailability = Int32
TargetedContentAvailability_None: TargetedContentAvailability = 0
TargetedContentAvailability_Partial: TargetedContentAvailability = 1
TargetedContentAvailability_All: TargetedContentAvailability = 2
class TargetedContentAvailabilityChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.TargetedContent.ITargetedContentAvailabilityChangedEventArgs
    _classid_ = 'Windows.Services.TargetedContent.TargetedContentAvailabilityChangedEventArgs'
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Services.TargetedContent.ITargetedContentAvailabilityChangedEventArgs) -> win32more.Windows.Foundation.Deferral: ...
class TargetedContentChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.TargetedContent.ITargetedContentChangedEventArgs
    _classid_ = 'Windows.Services.TargetedContent.TargetedContentChangedEventArgs'
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Services.TargetedContent.ITargetedContentChangedEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    @winrt_mixinmethod
    def get_HasPreviousContentExpired(self: win32more.Windows.Services.TargetedContent.ITargetedContentChangedEventArgs) -> Boolean: ...
    HasPreviousContentExpired = property(get_HasPreviousContentExpired, None)
class TargetedContentCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.TargetedContent.ITargetedContentCollection
    _classid_ = 'Windows.Services.TargetedContent.TargetedContentCollection'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Services.TargetedContent.ITargetedContentCollection) -> WinRT_String: ...
    @winrt_mixinmethod
    def ReportInteraction(self: win32more.Windows.Services.TargetedContent.ITargetedContentCollection, interaction: win32more.Windows.Services.TargetedContent.TargetedContentInteraction) -> Void: ...
    @winrt_mixinmethod
    def ReportCustomInteraction(self: win32more.Windows.Services.TargetedContent.ITargetedContentCollection, customInteractionName: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Path(self: win32more.Windows.Services.TargetedContent.ITargetedContentCollection) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Services.TargetedContent.ITargetedContentCollection) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Services.TargetedContent.TargetedContentValue]: ...
    @winrt_mixinmethod
    def get_Collections(self: win32more.Windows.Services.TargetedContent.ITargetedContentCollection) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.TargetedContent.TargetedContentCollection]: ...
    @winrt_mixinmethod
    def get_Items(self: win32more.Windows.Services.TargetedContent.ITargetedContentCollection) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.TargetedContent.TargetedContentItem]: ...
    Id = property(get_Id, None)
    Path = property(get_Path, None)
    Properties = property(get_Properties, None)
    Collections = property(get_Collections, None)
    Items = property(get_Items, None)
class TargetedContentContainer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.TargetedContent.ITargetedContentContainer
    _classid_ = 'Windows.Services.TargetedContent.TargetedContentContainer'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Services.TargetedContent.ITargetedContentContainer) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Services.TargetedContent.ITargetedContentContainer) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_Availability(self: win32more.Windows.Services.TargetedContent.ITargetedContentContainer) -> win32more.Windows.Services.TargetedContent.TargetedContentAvailability: ...
    @winrt_mixinmethod
    def get_Content(self: win32more.Windows.Services.TargetedContent.ITargetedContentContainer) -> win32more.Windows.Services.TargetedContent.TargetedContentCollection: ...
    @winrt_mixinmethod
    def SelectSingleObject(self: win32more.Windows.Services.TargetedContent.ITargetedContentContainer, path: WinRT_String) -> win32more.Windows.Services.TargetedContent.TargetedContentObject: ...
    @winrt_classmethod
    def GetAsync(cls: win32more.Windows.Services.TargetedContent.ITargetedContentContainerStatics, contentId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.TargetedContent.TargetedContentContainer]: ...
    Id = property(get_Id, None)
    Timestamp = property(get_Timestamp, None)
    Availability = property(get_Availability, None)
    Content = property(get_Content, None)
TargetedContentContract: UInt32 = 65536
class TargetedContentFile(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Streams.IRandomAccessStreamReference
    _classid_ = 'Windows.Services.TargetedContent.TargetedContentFile'
    @winrt_mixinmethod
    def OpenReadAsync(self: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStreamWithContentType]: ...
class TargetedContentImage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.TargetedContent.ITargetedContentImage
    _classid_ = 'Windows.Services.TargetedContent.TargetedContentImage'
    @winrt_mixinmethod
    def get_Height(self: win32more.Windows.Services.TargetedContent.ITargetedContentImage) -> UInt32: ...
    @winrt_mixinmethod
    def get_Width(self: win32more.Windows.Services.TargetedContent.ITargetedContentImage) -> UInt32: ...
    @winrt_mixinmethod
    def OpenReadAsync(self: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStreamWithContentType]: ...
    Height = property(get_Height, None)
    Width = property(get_Width, None)
TargetedContentInteraction = Int32
TargetedContentInteraction_Impression: TargetedContentInteraction = 0
TargetedContentInteraction_ClickThrough: TargetedContentInteraction = 1
TargetedContentInteraction_Hover: TargetedContentInteraction = 2
TargetedContentInteraction_Like: TargetedContentInteraction = 3
TargetedContentInteraction_Dislike: TargetedContentInteraction = 4
TargetedContentInteraction_Dismiss: TargetedContentInteraction = 5
TargetedContentInteraction_Ineligible: TargetedContentInteraction = 6
TargetedContentInteraction_Accept: TargetedContentInteraction = 7
TargetedContentInteraction_Decline: TargetedContentInteraction = 8
TargetedContentInteraction_Defer: TargetedContentInteraction = 9
TargetedContentInteraction_Canceled: TargetedContentInteraction = 10
TargetedContentInteraction_Conversion: TargetedContentInteraction = 11
TargetedContentInteraction_Opportunity: TargetedContentInteraction = 12
class TargetedContentItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.TargetedContent.ITargetedContentItem
    _classid_ = 'Windows.Services.TargetedContent.TargetedContentItem'
    @winrt_mixinmethod
    def get_Path(self: win32more.Windows.Services.TargetedContent.ITargetedContentItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def ReportInteraction(self: win32more.Windows.Services.TargetedContent.ITargetedContentItem, interaction: win32more.Windows.Services.TargetedContent.TargetedContentInteraction) -> Void: ...
    @winrt_mixinmethod
    def ReportCustomInteraction(self: win32more.Windows.Services.TargetedContent.ITargetedContentItem, customInteractionName: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.Services.TargetedContent.ITargetedContentItem) -> win32more.Windows.Services.TargetedContent.TargetedContentItemState: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Services.TargetedContent.ITargetedContentItem) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Services.TargetedContent.TargetedContentValue]: ...
    @winrt_mixinmethod
    def get_Collections(self: win32more.Windows.Services.TargetedContent.ITargetedContentItem) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.TargetedContent.TargetedContentCollection]: ...
    Path = property(get_Path, None)
    State = property(get_State, None)
    Properties = property(get_Properties, None)
    Collections = property(get_Collections, None)
class TargetedContentItemState(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.TargetedContent.ITargetedContentItemState
    _classid_ = 'Windows.Services.TargetedContent.TargetedContentItemState'
    @winrt_mixinmethod
    def get_ShouldDisplay(self: win32more.Windows.Services.TargetedContent.ITargetedContentItemState) -> Boolean: ...
    @winrt_mixinmethod
    def get_AppInstallationState(self: win32more.Windows.Services.TargetedContent.ITargetedContentItemState) -> win32more.Windows.Services.TargetedContent.TargetedContentAppInstallationState: ...
    ShouldDisplay = property(get_ShouldDisplay, None)
    AppInstallationState = property(get_AppInstallationState, None)
class TargetedContentObject(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.TargetedContent.ITargetedContentObject
    _classid_ = 'Windows.Services.TargetedContent.TargetedContentObject'
    @winrt_mixinmethod
    def get_ObjectKind(self: win32more.Windows.Services.TargetedContent.ITargetedContentObject) -> win32more.Windows.Services.TargetedContent.TargetedContentObjectKind: ...
    @winrt_mixinmethod
    def get_Collection(self: win32more.Windows.Services.TargetedContent.ITargetedContentObject) -> win32more.Windows.Services.TargetedContent.TargetedContentCollection: ...
    @winrt_mixinmethod
    def get_Item(self: win32more.Windows.Services.TargetedContent.ITargetedContentObject) -> win32more.Windows.Services.TargetedContent.TargetedContentItem: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.Services.TargetedContent.ITargetedContentObject) -> win32more.Windows.Services.TargetedContent.TargetedContentValue: ...
    ObjectKind = property(get_ObjectKind, None)
    Collection = property(get_Collection, None)
    Item = property(get_Item, None)
    Value = property(get_Value, None)
TargetedContentObjectKind = Int32
TargetedContentObjectKind_Collection: TargetedContentObjectKind = 0
TargetedContentObjectKind_Item: TargetedContentObjectKind = 1
TargetedContentObjectKind_Value: TargetedContentObjectKind = 2
class TargetedContentStateChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.TargetedContent.ITargetedContentStateChangedEventArgs
    _classid_ = 'Windows.Services.TargetedContent.TargetedContentStateChangedEventArgs'
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Services.TargetedContent.ITargetedContentStateChangedEventArgs) -> win32more.Windows.Foundation.Deferral: ...
class TargetedContentSubscription(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.TargetedContent.ITargetedContentSubscription
    _classid_ = 'Windows.Services.TargetedContent.TargetedContentSubscription'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Services.TargetedContent.ITargetedContentSubscription) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetContentContainerAsync(self: win32more.Windows.Services.TargetedContent.ITargetedContentSubscription) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.TargetedContent.TargetedContentContainer]: ...
    @winrt_mixinmethod
    def add_ContentChanged(self: win32more.Windows.Services.TargetedContent.ITargetedContentSubscription, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Services.TargetedContent.TargetedContentSubscription, win32more.Windows.Services.TargetedContent.TargetedContentChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ContentChanged(self: win32more.Windows.Services.TargetedContent.ITargetedContentSubscription, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_AvailabilityChanged(self: win32more.Windows.Services.TargetedContent.ITargetedContentSubscription, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Services.TargetedContent.TargetedContentSubscription, win32more.Windows.Services.TargetedContent.TargetedContentAvailabilityChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AvailabilityChanged(self: win32more.Windows.Services.TargetedContent.ITargetedContentSubscription, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_StateChanged(self: win32more.Windows.Services.TargetedContent.ITargetedContentSubscription, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Services.TargetedContent.TargetedContentSubscription, win32more.Windows.Services.TargetedContent.TargetedContentStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StateChanged(self: win32more.Windows.Services.TargetedContent.ITargetedContentSubscription, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetAsync(cls: win32more.Windows.Services.TargetedContent.ITargetedContentSubscriptionStatics, subscriptionId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.TargetedContent.TargetedContentSubscription]: ...
    @winrt_classmethod
    def GetOptions(cls: win32more.Windows.Services.TargetedContent.ITargetedContentSubscriptionStatics, subscriptionId: WinRT_String) -> win32more.Windows.Services.TargetedContent.TargetedContentSubscriptionOptions: ...
    Id = property(get_Id, None)
class TargetedContentSubscriptionOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.TargetedContent.ITargetedContentSubscriptionOptions
    _classid_ = 'Windows.Services.TargetedContent.TargetedContentSubscriptionOptions'
    @winrt_mixinmethod
    def get_SubscriptionId(self: win32more.Windows.Services.TargetedContent.ITargetedContentSubscriptionOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AllowPartialContentAvailability(self: win32more.Windows.Services.TargetedContent.ITargetedContentSubscriptionOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowPartialContentAvailability(self: win32more.Windows.Services.TargetedContent.ITargetedContentSubscriptionOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CloudQueryParameters(self: win32more.Windows.Services.TargetedContent.ITargetedContentSubscriptionOptions) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def get_LocalFilters(self: win32more.Windows.Services.TargetedContent.ITargetedContentSubscriptionOptions) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def Update(self: win32more.Windows.Services.TargetedContent.ITargetedContentSubscriptionOptions) -> Void: ...
    SubscriptionId = property(get_SubscriptionId, None)
    AllowPartialContentAvailability = property(get_AllowPartialContentAvailability, put_AllowPartialContentAvailability)
    CloudQueryParameters = property(get_CloudQueryParameters, None)
    LocalFilters = property(get_LocalFilters, None)
class TargetedContentValue(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.TargetedContent.ITargetedContentValue
    _classid_ = 'Windows.Services.TargetedContent.TargetedContentValue'
    @winrt_mixinmethod
    def get_ValueKind(self: win32more.Windows.Services.TargetedContent.ITargetedContentValue) -> win32more.Windows.Services.TargetedContent.TargetedContentValueKind: ...
    @winrt_mixinmethod
    def get_Path(self: win32more.Windows.Services.TargetedContent.ITargetedContentValue) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_String(self: win32more.Windows.Services.TargetedContent.ITargetedContentValue) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Uri(self: win32more.Windows.Services.TargetedContent.ITargetedContentValue) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_Number(self: win32more.Windows.Services.TargetedContent.ITargetedContentValue) -> Double: ...
    @winrt_mixinmethod
    def get_Boolean(self: win32more.Windows.Services.TargetedContent.ITargetedContentValue) -> Boolean: ...
    @winrt_mixinmethod
    def get_File(self: win32more.Windows.Services.TargetedContent.ITargetedContentValue) -> win32more.Windows.Services.TargetedContent.TargetedContentFile: ...
    @winrt_mixinmethod
    def get_ImageFile(self: win32more.Windows.Services.TargetedContent.ITargetedContentValue) -> win32more.Windows.Services.TargetedContent.TargetedContentImage: ...
    @winrt_mixinmethod
    def get_Action(self: win32more.Windows.Services.TargetedContent.ITargetedContentValue) -> win32more.Windows.Services.TargetedContent.TargetedContentAction: ...
    @winrt_mixinmethod
    def get_Strings(self: win32more.Windows.Services.TargetedContent.ITargetedContentValue) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Uris(self: win32more.Windows.Services.TargetedContent.ITargetedContentValue) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Uri]: ...
    @winrt_mixinmethod
    def get_Numbers(self: win32more.Windows.Services.TargetedContent.ITargetedContentValue) -> win32more.Windows.Foundation.Collections.IVectorView[Double]: ...
    @winrt_mixinmethod
    def get_Booleans(self: win32more.Windows.Services.TargetedContent.ITargetedContentValue) -> win32more.Windows.Foundation.Collections.IVectorView[Boolean]: ...
    @winrt_mixinmethod
    def get_Files(self: win32more.Windows.Services.TargetedContent.ITargetedContentValue) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.TargetedContent.TargetedContentFile]: ...
    @winrt_mixinmethod
    def get_ImageFiles(self: win32more.Windows.Services.TargetedContent.ITargetedContentValue) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.TargetedContent.TargetedContentImage]: ...
    @winrt_mixinmethod
    def get_Actions(self: win32more.Windows.Services.TargetedContent.ITargetedContentValue) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.TargetedContent.TargetedContentAction]: ...
    ValueKind = property(get_ValueKind, None)
    Path = property(get_Path, None)
    String = property(get_String, None)
    Uri = property(get_Uri, None)
    Number = property(get_Number, None)
    Boolean = property(get_Boolean, None)
    File = property(get_File, None)
    ImageFile = property(get_ImageFile, None)
    Action = property(get_Action, None)
    Strings = property(get_Strings, None)
    Uris = property(get_Uris, None)
    Numbers = property(get_Numbers, None)
    Booleans = property(get_Booleans, None)
    Files = property(get_Files, None)
    ImageFiles = property(get_ImageFiles, None)
    Actions = property(get_Actions, None)
TargetedContentValueKind = Int32
TargetedContentValueKind_String: TargetedContentValueKind = 0
TargetedContentValueKind_Uri: TargetedContentValueKind = 1
TargetedContentValueKind_Number: TargetedContentValueKind = 2
TargetedContentValueKind_Boolean: TargetedContentValueKind = 3
TargetedContentValueKind_File: TargetedContentValueKind = 4
TargetedContentValueKind_ImageFile: TargetedContentValueKind = 5
TargetedContentValueKind_Action: TargetedContentValueKind = 6
TargetedContentValueKind_Strings: TargetedContentValueKind = 7
TargetedContentValueKind_Uris: TargetedContentValueKind = 8
TargetedContentValueKind_Numbers: TargetedContentValueKind = 9
TargetedContentValueKind_Booleans: TargetedContentValueKind = 10
TargetedContentValueKind_Files: TargetedContentValueKind = 11
TargetedContentValueKind_ImageFiles: TargetedContentValueKind = 12
TargetedContentValueKind_Actions: TargetedContentValueKind = 13
make_head(_module, 'ITargetedContentAction')
make_head(_module, 'ITargetedContentAvailabilityChangedEventArgs')
make_head(_module, 'ITargetedContentChangedEventArgs')
make_head(_module, 'ITargetedContentCollection')
make_head(_module, 'ITargetedContentContainer')
make_head(_module, 'ITargetedContentContainerStatics')
make_head(_module, 'ITargetedContentImage')
make_head(_module, 'ITargetedContentItem')
make_head(_module, 'ITargetedContentItemState')
make_head(_module, 'ITargetedContentObject')
make_head(_module, 'ITargetedContentStateChangedEventArgs')
make_head(_module, 'ITargetedContentSubscription')
make_head(_module, 'ITargetedContentSubscriptionOptions')
make_head(_module, 'ITargetedContentSubscriptionStatics')
make_head(_module, 'ITargetedContentValue')
make_head(_module, 'TargetedContentAction')
make_head(_module, 'TargetedContentAvailabilityChangedEventArgs')
make_head(_module, 'TargetedContentChangedEventArgs')
make_head(_module, 'TargetedContentCollection')
make_head(_module, 'TargetedContentContainer')
make_head(_module, 'TargetedContentFile')
make_head(_module, 'TargetedContentImage')
make_head(_module, 'TargetedContentItem')
make_head(_module, 'TargetedContentItemState')
make_head(_module, 'TargetedContentObject')
make_head(_module, 'TargetedContentStateChangedEventArgs')
make_head(_module, 'TargetedContentSubscription')
make_head(_module, 'TargetedContentSubscriptionOptions')
make_head(_module, 'TargetedContentValue')
