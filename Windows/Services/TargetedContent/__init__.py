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
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Services.TargetedContent
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
class ITargetedContentAction(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('d75b691e-6cd6-4ca0-9d-8f-47-28-b0-b7-e6-b6')
    @winrt_commethod(6)
    def InvokeAsync(self) -> Windows.Foundation.IAsyncAction: ...
class ITargetedContentAvailabilityChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('e0f59d26-5927-4450-96-5c-1c-eb-7b-ec-de-65')
    @winrt_commethod(6)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
class ITargetedContentChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('99d488c9-587e-4586-8e-f7-b5-4c-a9-45-3a-16')
    @winrt_commethod(6)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    @winrt_commethod(7)
    def get_HasPreviousContentExpired(self) -> Boolean: ...
    HasPreviousContentExpired = property(get_HasPreviousContentExpired, None)
class ITargetedContentCollection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('2d4b66c5-f163-44ba-9f-6e-e1-a4-c2-bb-55-9d')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def ReportInteraction(self, interaction: Windows.Services.TargetedContent.TargetedContentInteraction) -> Void: ...
    @winrt_commethod(8)
    def ReportCustomInteraction(self, customInteractionName: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_Path(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Properties(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Services.TargetedContent.TargetedContentValue]: ...
    @winrt_commethod(11)
    def get_Collections(self) -> Windows.Foundation.Collections.IVectorView[Windows.Services.TargetedContent.TargetedContentCollection]: ...
    @winrt_commethod(12)
    def get_Items(self) -> Windows.Foundation.Collections.IVectorView[Windows.Services.TargetedContent.TargetedContentItem]: ...
    Id = property(get_Id, None)
    Path = property(get_Path, None)
    Properties = property(get_Properties, None)
    Collections = property(get_Collections, None)
    Items = property(get_Items, None)
class ITargetedContentContainer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('bc2494c9-8837-47c2-85-0f-d7-9d-64-59-59-26')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Timestamp(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(8)
    def get_Availability(self) -> Windows.Services.TargetedContent.TargetedContentAvailability: ...
    @winrt_commethod(9)
    def get_Content(self) -> Windows.Services.TargetedContent.TargetedContentCollection: ...
    @winrt_commethod(10)
    def SelectSingleObject(self, path: WinRT_String) -> Windows.Services.TargetedContent.TargetedContentObject: ...
    Id = property(get_Id, None)
    Timestamp = property(get_Timestamp, None)
    Availability = property(get_Availability, None)
    Content = property(get_Content, None)
class ITargetedContentContainerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('5b47e7fb-2140-4c1f-a7-36-c5-95-83-f2-27-d8')
    @winrt_commethod(6)
    def GetAsync(self, contentId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Services.TargetedContent.TargetedContentContainer]: ...
class ITargetedContentImage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('a7a585d9-779f-4b1e-bb-b1-8e-af-53-fb-ea-b2')
    @winrt_commethod(6)
    def get_Height(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_Width(self) -> UInt32: ...
    Height = property(get_Height, None)
    Width = property(get_Width, None)
class ITargetedContentItem(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('38168dc4-276c-4c32-96-ba-56-5c-6e-40-6e-74')
    @winrt_commethod(6)
    def get_Path(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def ReportInteraction(self, interaction: Windows.Services.TargetedContent.TargetedContentInteraction) -> Void: ...
    @winrt_commethod(8)
    def ReportCustomInteraction(self, customInteractionName: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_State(self) -> Windows.Services.TargetedContent.TargetedContentItemState: ...
    @winrt_commethod(10)
    def get_Properties(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Services.TargetedContent.TargetedContentValue]: ...
    @winrt_commethod(11)
    def get_Collections(self) -> Windows.Foundation.Collections.IVectorView[Windows.Services.TargetedContent.TargetedContentCollection]: ...
    Path = property(get_Path, None)
    State = property(get_State, None)
    Properties = property(get_Properties, None)
    Collections = property(get_Collections, None)
class ITargetedContentItemState(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('73935454-4c65-4b47-a4-41-47-2d-e5-3c-79-b6')
    @winrt_commethod(6)
    def get_ShouldDisplay(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_AppInstallationState(self) -> Windows.Services.TargetedContent.TargetedContentAppInstallationState: ...
    ShouldDisplay = property(get_ShouldDisplay, None)
    AppInstallationState = property(get_AppInstallationState, None)
class ITargetedContentObject(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('041d7969-2212-42d1-9d-fa-88-a8-e3-03-3a-a3')
    @winrt_commethod(6)
    def get_ObjectKind(self) -> Windows.Services.TargetedContent.TargetedContentObjectKind: ...
    @winrt_commethod(7)
    def get_Collection(self) -> Windows.Services.TargetedContent.TargetedContentCollection: ...
    @winrt_commethod(8)
    def get_Item(self) -> Windows.Services.TargetedContent.TargetedContentItem: ...
    @winrt_commethod(9)
    def get_Value(self) -> Windows.Services.TargetedContent.TargetedContentValue: ...
    ObjectKind = property(get_ObjectKind, None)
    Collection = property(get_Collection, None)
    Item = property(get_Item, None)
    Value = property(get_Value, None)
class ITargetedContentStateChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('9a1cef3d-8073-4416-8d-f2-54-68-35-a6-41-4f')
    @winrt_commethod(6)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
class ITargetedContentSubscription(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('882c2c49-c652-4c7a-ac-ad-1f-7f-a2-98-6c-73')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetContentContainerAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Services.TargetedContent.TargetedContentContainer]: ...
    @winrt_commethod(8)
    def add_ContentChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Services.TargetedContent.TargetedContentSubscription, Windows.Services.TargetedContent.TargetedContentChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_ContentChanged(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_AvailabilityChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Services.TargetedContent.TargetedContentSubscription, Windows.Services.TargetedContent.TargetedContentAvailabilityChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_AvailabilityChanged(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_StateChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Services.TargetedContent.TargetedContentSubscription, Windows.Services.TargetedContent.TargetedContentStateChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_StateChanged(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Id = property(get_Id, None)
class ITargetedContentSubscriptionOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('61ee6ad0-2c83-421b-84-67-41-3e-af-1a-eb-97')
    @winrt_commethod(6)
    def get_SubscriptionId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_AllowPartialContentAvailability(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_AllowPartialContentAvailability(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_CloudQueryParameters(self) -> Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_commethod(10)
    def get_LocalFilters(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(11)
    def Update(self) -> Void: ...
    SubscriptionId = property(get_SubscriptionId, None)
    AllowPartialContentAvailability = property(get_AllowPartialContentAvailability, put_AllowPartialContentAvailability)
    CloudQueryParameters = property(get_CloudQueryParameters, None)
    LocalFilters = property(get_LocalFilters, None)
class ITargetedContentSubscriptionStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('faddfe80-360d-4916-b5-3c-7e-a2-70-90-d0-2a')
    @winrt_commethod(6)
    def GetAsync(self, subscriptionId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Services.TargetedContent.TargetedContentSubscription]: ...
    @winrt_commethod(7)
    def GetOptions(self, subscriptionId: WinRT_String) -> Windows.Services.TargetedContent.TargetedContentSubscriptionOptions: ...
class ITargetedContentValue(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('aafde4b3-4215-4bf8-86-7f-43-f0-48-65-f9-bf')
    @winrt_commethod(6)
    def get_ValueKind(self) -> Windows.Services.TargetedContent.TargetedContentValueKind: ...
    @winrt_commethod(7)
    def get_Path(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_String(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Uri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(10)
    def get_Number(self) -> Double: ...
    @winrt_commethod(11)
    def get_Boolean(self) -> Boolean: ...
    @winrt_commethod(12)
    def get_File(self) -> Windows.Services.TargetedContent.TargetedContentFile: ...
    @winrt_commethod(13)
    def get_ImageFile(self) -> Windows.Services.TargetedContent.TargetedContentImage: ...
    @winrt_commethod(14)
    def get_Action(self) -> Windows.Services.TargetedContent.TargetedContentAction: ...
    @winrt_commethod(15)
    def get_Strings(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(16)
    def get_Uris(self) -> Windows.Foundation.Collections.IVectorView[Windows.Foundation.Uri]: ...
    @winrt_commethod(17)
    def get_Numbers(self) -> Windows.Foundation.Collections.IVectorView[Double]: ...
    @winrt_commethod(18)
    def get_Booleans(self) -> Windows.Foundation.Collections.IVectorView[Boolean]: ...
    @winrt_commethod(19)
    def get_Files(self) -> Windows.Foundation.Collections.IVectorView[Windows.Services.TargetedContent.TargetedContentFile]: ...
    @winrt_commethod(20)
    def get_ImageFiles(self) -> Windows.Foundation.Collections.IVectorView[Windows.Services.TargetedContent.TargetedContentImage]: ...
    @winrt_commethod(21)
    def get_Actions(self) -> Windows.Foundation.Collections.IVectorView[Windows.Services.TargetedContent.TargetedContentAction]: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.TargetedContent.TargetedContentAction'
    @winrt_mixinmethod
    def InvokeAsync(self: Windows.Services.TargetedContent.ITargetedContentAction) -> Windows.Foundation.IAsyncAction: ...
TargetedContentAppInstallationState = Int32
TargetedContentAppInstallationState_NotApplicable: TargetedContentAppInstallationState = 0
TargetedContentAppInstallationState_NotInstalled: TargetedContentAppInstallationState = 1
TargetedContentAppInstallationState_Installed: TargetedContentAppInstallationState = 2
TargetedContentAvailability = Int32
TargetedContentAvailability_None: TargetedContentAvailability = 0
TargetedContentAvailability_Partial: TargetedContentAvailability = 1
TargetedContentAvailability_All: TargetedContentAvailability = 2
class TargetedContentAvailabilityChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.TargetedContent.TargetedContentAvailabilityChangedEventArgs'
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Services.TargetedContent.ITargetedContentAvailabilityChangedEventArgs) -> Windows.Foundation.Deferral: ...
class TargetedContentChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.TargetedContent.TargetedContentChangedEventArgs'
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Services.TargetedContent.ITargetedContentChangedEventArgs) -> Windows.Foundation.Deferral: ...
    @winrt_mixinmethod
    def get_HasPreviousContentExpired(self: Windows.Services.TargetedContent.ITargetedContentChangedEventArgs) -> Boolean: ...
    HasPreviousContentExpired = property(get_HasPreviousContentExpired, None)
class TargetedContentCollection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.TargetedContent.TargetedContentCollection'
    @winrt_mixinmethod
    def get_Id(self: Windows.Services.TargetedContent.ITargetedContentCollection) -> WinRT_String: ...
    @winrt_mixinmethod
    def ReportInteraction(self: Windows.Services.TargetedContent.ITargetedContentCollection, interaction: Windows.Services.TargetedContent.TargetedContentInteraction) -> Void: ...
    @winrt_mixinmethod
    def ReportCustomInteraction(self: Windows.Services.TargetedContent.ITargetedContentCollection, customInteractionName: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Path(self: Windows.Services.TargetedContent.ITargetedContentCollection) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Services.TargetedContent.ITargetedContentCollection) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Services.TargetedContent.TargetedContentValue]: ...
    @winrt_mixinmethod
    def get_Collections(self: Windows.Services.TargetedContent.ITargetedContentCollection) -> Windows.Foundation.Collections.IVectorView[Windows.Services.TargetedContent.TargetedContentCollection]: ...
    @winrt_mixinmethod
    def get_Items(self: Windows.Services.TargetedContent.ITargetedContentCollection) -> Windows.Foundation.Collections.IVectorView[Windows.Services.TargetedContent.TargetedContentItem]: ...
    Id = property(get_Id, None)
    Path = property(get_Path, None)
    Properties = property(get_Properties, None)
    Collections = property(get_Collections, None)
    Items = property(get_Items, None)
class TargetedContentContainer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.TargetedContent.TargetedContentContainer'
    @winrt_mixinmethod
    def get_Id(self: Windows.Services.TargetedContent.ITargetedContentContainer) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Services.TargetedContent.ITargetedContentContainer) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_Availability(self: Windows.Services.TargetedContent.ITargetedContentContainer) -> Windows.Services.TargetedContent.TargetedContentAvailability: ...
    @winrt_mixinmethod
    def get_Content(self: Windows.Services.TargetedContent.ITargetedContentContainer) -> Windows.Services.TargetedContent.TargetedContentCollection: ...
    @winrt_mixinmethod
    def SelectSingleObject(self: Windows.Services.TargetedContent.ITargetedContentContainer, path: WinRT_String) -> Windows.Services.TargetedContent.TargetedContentObject: ...
    @winrt_classmethod
    def GetAsync(cls: Windows.Services.TargetedContent.ITargetedContentContainerStatics, contentId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Services.TargetedContent.TargetedContentContainer]: ...
    Id = property(get_Id, None)
    Timestamp = property(get_Timestamp, None)
    Availability = property(get_Availability, None)
    Content = property(get_Content, None)
TargetedContentContract: UInt32 = 65536
class TargetedContentFile(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.TargetedContent.TargetedContentFile'
    @winrt_mixinmethod
    def OpenReadAsync(self: Windows.Storage.Streams.IRandomAccessStreamReference) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IRandomAccessStreamWithContentType]: ...
class TargetedContentImage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.TargetedContent.TargetedContentImage'
    @winrt_mixinmethod
    def get_Height(self: Windows.Services.TargetedContent.ITargetedContentImage) -> UInt32: ...
    @winrt_mixinmethod
    def get_Width(self: Windows.Services.TargetedContent.ITargetedContentImage) -> UInt32: ...
    @winrt_mixinmethod
    def OpenReadAsync(self: Windows.Storage.Streams.IRandomAccessStreamReference) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IRandomAccessStreamWithContentType]: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.TargetedContent.TargetedContentItem'
    @winrt_mixinmethod
    def get_Path(self: Windows.Services.TargetedContent.ITargetedContentItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def ReportInteraction(self: Windows.Services.TargetedContent.ITargetedContentItem, interaction: Windows.Services.TargetedContent.TargetedContentInteraction) -> Void: ...
    @winrt_mixinmethod
    def ReportCustomInteraction(self: Windows.Services.TargetedContent.ITargetedContentItem, customInteractionName: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_State(self: Windows.Services.TargetedContent.ITargetedContentItem) -> Windows.Services.TargetedContent.TargetedContentItemState: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Services.TargetedContent.ITargetedContentItem) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Services.TargetedContent.TargetedContentValue]: ...
    @winrt_mixinmethod
    def get_Collections(self: Windows.Services.TargetedContent.ITargetedContentItem) -> Windows.Foundation.Collections.IVectorView[Windows.Services.TargetedContent.TargetedContentCollection]: ...
    Path = property(get_Path, None)
    State = property(get_State, None)
    Properties = property(get_Properties, None)
    Collections = property(get_Collections, None)
class TargetedContentItemState(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.TargetedContent.TargetedContentItemState'
    @winrt_mixinmethod
    def get_ShouldDisplay(self: Windows.Services.TargetedContent.ITargetedContentItemState) -> Boolean: ...
    @winrt_mixinmethod
    def get_AppInstallationState(self: Windows.Services.TargetedContent.ITargetedContentItemState) -> Windows.Services.TargetedContent.TargetedContentAppInstallationState: ...
    ShouldDisplay = property(get_ShouldDisplay, None)
    AppInstallationState = property(get_AppInstallationState, None)
class TargetedContentObject(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.TargetedContent.TargetedContentObject'
    @winrt_mixinmethod
    def get_ObjectKind(self: Windows.Services.TargetedContent.ITargetedContentObject) -> Windows.Services.TargetedContent.TargetedContentObjectKind: ...
    @winrt_mixinmethod
    def get_Collection(self: Windows.Services.TargetedContent.ITargetedContentObject) -> Windows.Services.TargetedContent.TargetedContentCollection: ...
    @winrt_mixinmethod
    def get_Item(self: Windows.Services.TargetedContent.ITargetedContentObject) -> Windows.Services.TargetedContent.TargetedContentItem: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Services.TargetedContent.ITargetedContentObject) -> Windows.Services.TargetedContent.TargetedContentValue: ...
    ObjectKind = property(get_ObjectKind, None)
    Collection = property(get_Collection, None)
    Item = property(get_Item, None)
    Value = property(get_Value, None)
TargetedContentObjectKind = Int32
TargetedContentObjectKind_Collection: TargetedContentObjectKind = 0
TargetedContentObjectKind_Item: TargetedContentObjectKind = 1
TargetedContentObjectKind_Value: TargetedContentObjectKind = 2
class TargetedContentStateChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.TargetedContent.TargetedContentStateChangedEventArgs'
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Services.TargetedContent.ITargetedContentStateChangedEventArgs) -> Windows.Foundation.Deferral: ...
class TargetedContentSubscription(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.TargetedContent.TargetedContentSubscription'
    @winrt_mixinmethod
    def get_Id(self: Windows.Services.TargetedContent.ITargetedContentSubscription) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetContentContainerAsync(self: Windows.Services.TargetedContent.ITargetedContentSubscription) -> Windows.Foundation.IAsyncOperation[Windows.Services.TargetedContent.TargetedContentContainer]: ...
    @winrt_mixinmethod
    def add_ContentChanged(self: Windows.Services.TargetedContent.ITargetedContentSubscription, handler: Windows.Foundation.TypedEventHandler[Windows.Services.TargetedContent.TargetedContentSubscription, Windows.Services.TargetedContent.TargetedContentChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ContentChanged(self: Windows.Services.TargetedContent.ITargetedContentSubscription, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_AvailabilityChanged(self: Windows.Services.TargetedContent.ITargetedContentSubscription, handler: Windows.Foundation.TypedEventHandler[Windows.Services.TargetedContent.TargetedContentSubscription, Windows.Services.TargetedContent.TargetedContentAvailabilityChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AvailabilityChanged(self: Windows.Services.TargetedContent.ITargetedContentSubscription, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_StateChanged(self: Windows.Services.TargetedContent.ITargetedContentSubscription, handler: Windows.Foundation.TypedEventHandler[Windows.Services.TargetedContent.TargetedContentSubscription, Windows.Services.TargetedContent.TargetedContentStateChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StateChanged(self: Windows.Services.TargetedContent.ITargetedContentSubscription, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetAsync(cls: Windows.Services.TargetedContent.ITargetedContentSubscriptionStatics, subscriptionId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Services.TargetedContent.TargetedContentSubscription]: ...
    @winrt_classmethod
    def GetOptions(cls: Windows.Services.TargetedContent.ITargetedContentSubscriptionStatics, subscriptionId: WinRT_String) -> Windows.Services.TargetedContent.TargetedContentSubscriptionOptions: ...
    Id = property(get_Id, None)
class TargetedContentSubscriptionOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.TargetedContent.TargetedContentSubscriptionOptions'
    @winrt_mixinmethod
    def get_SubscriptionId(self: Windows.Services.TargetedContent.ITargetedContentSubscriptionOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AllowPartialContentAvailability(self: Windows.Services.TargetedContent.ITargetedContentSubscriptionOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowPartialContentAvailability(self: Windows.Services.TargetedContent.ITargetedContentSubscriptionOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CloudQueryParameters(self: Windows.Services.TargetedContent.ITargetedContentSubscriptionOptions) -> Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def get_LocalFilters(self: Windows.Services.TargetedContent.ITargetedContentSubscriptionOptions) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def Update(self: Windows.Services.TargetedContent.ITargetedContentSubscriptionOptions) -> Void: ...
    SubscriptionId = property(get_SubscriptionId, None)
    AllowPartialContentAvailability = property(get_AllowPartialContentAvailability, put_AllowPartialContentAvailability)
    CloudQueryParameters = property(get_CloudQueryParameters, None)
    LocalFilters = property(get_LocalFilters, None)
class TargetedContentValue(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.TargetedContent.TargetedContentValue'
    @winrt_mixinmethod
    def get_ValueKind(self: Windows.Services.TargetedContent.ITargetedContentValue) -> Windows.Services.TargetedContent.TargetedContentValueKind: ...
    @winrt_mixinmethod
    def get_Path(self: Windows.Services.TargetedContent.ITargetedContentValue) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_String(self: Windows.Services.TargetedContent.ITargetedContentValue) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Uri(self: Windows.Services.TargetedContent.ITargetedContentValue) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_Number(self: Windows.Services.TargetedContent.ITargetedContentValue) -> Double: ...
    @winrt_mixinmethod
    def get_Boolean(self: Windows.Services.TargetedContent.ITargetedContentValue) -> Boolean: ...
    @winrt_mixinmethod
    def get_File(self: Windows.Services.TargetedContent.ITargetedContentValue) -> Windows.Services.TargetedContent.TargetedContentFile: ...
    @winrt_mixinmethod
    def get_ImageFile(self: Windows.Services.TargetedContent.ITargetedContentValue) -> Windows.Services.TargetedContent.TargetedContentImage: ...
    @winrt_mixinmethod
    def get_Action(self: Windows.Services.TargetedContent.ITargetedContentValue) -> Windows.Services.TargetedContent.TargetedContentAction: ...
    @winrt_mixinmethod
    def get_Strings(self: Windows.Services.TargetedContent.ITargetedContentValue) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Uris(self: Windows.Services.TargetedContent.ITargetedContentValue) -> Windows.Foundation.Collections.IVectorView[Windows.Foundation.Uri]: ...
    @winrt_mixinmethod
    def get_Numbers(self: Windows.Services.TargetedContent.ITargetedContentValue) -> Windows.Foundation.Collections.IVectorView[Double]: ...
    @winrt_mixinmethod
    def get_Booleans(self: Windows.Services.TargetedContent.ITargetedContentValue) -> Windows.Foundation.Collections.IVectorView[Boolean]: ...
    @winrt_mixinmethod
    def get_Files(self: Windows.Services.TargetedContent.ITargetedContentValue) -> Windows.Foundation.Collections.IVectorView[Windows.Services.TargetedContent.TargetedContentFile]: ...
    @winrt_mixinmethod
    def get_ImageFiles(self: Windows.Services.TargetedContent.ITargetedContentValue) -> Windows.Foundation.Collections.IVectorView[Windows.Services.TargetedContent.TargetedContentImage]: ...
    @winrt_mixinmethod
    def get_Actions(self: Windows.Services.TargetedContent.ITargetedContentValue) -> Windows.Foundation.Collections.IVectorView[Windows.Services.TargetedContent.TargetedContentAction]: ...
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
