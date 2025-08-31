from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Windows.AI.Actions
import win32more.Windows.AI.Actions.Hosting
import win32more.Windows.ApplicationModel.Contacts
import win32more.Windows.Foundation
import win32more.Windows.UI
class ActionEntity(ComPtr):
    extends: IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.AI.Actions.IActionEntity
    _classid_ = 'Windows.AI.Actions.ActionEntity'
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.AI.Actions.IActionEntity) -> win32more.Windows.AI.Actions.ActionEntityKind: ...
    @winrt_mixinmethod
    def get_DisplayInfo(self: win32more.Windows.AI.Actions.IActionEntity) -> win32more.Windows.AI.Actions.ActionEntityDisplayInfo: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.AI.Actions.IActionEntity2) -> WinRT_String: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    DisplayInfo = property(get_DisplayInfo, None)
    Id = property(get_Id, None)
    Kind = property(get_Kind, None)
class ActionEntityDisplayInfo(ComPtr):
    extends: IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.AI.Actions.IActionEntityDisplayInfo
    _classid_ = 'Windows.AI.Actions.ActionEntityDisplayInfo'
    @winrt_mixinmethod
    def get_Title(self: win32more.Windows.AI.Actions.IActionEntityDisplayInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    Title = property(get_Title, None)
class ActionEntityFactory(ComPtr):
    extends: IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.AI.Actions.IActionEntityFactory2
    _classid_ = 'Windows.AI.Actions.ActionEntityFactory'
    @winrt_mixinmethod
    def CreateFileEntity(self: win32more.Windows.AI.Actions.IActionEntityFactory2, path: WinRT_String) -> win32more.Windows.AI.Actions.FileActionEntity: ...
    @winrt_mixinmethod
    def CreateDocumentEntity(self: win32more.Windows.AI.Actions.IActionEntityFactory2, path: WinRT_String) -> win32more.Windows.AI.Actions.DocumentActionEntity: ...
    @winrt_mixinmethod
    def CreatePhotoEntity(self: win32more.Windows.AI.Actions.IActionEntityFactory2, path: WinRT_String) -> win32more.Windows.AI.Actions.PhotoActionEntity: ...
    @winrt_mixinmethod
    def CreateTextEntity(self: win32more.Windows.AI.Actions.IActionEntityFactory2, text: WinRT_String) -> win32more.Windows.AI.Actions.TextActionEntity: ...
    @winrt_mixinmethod
    def CreateRemoteFileEntity(self: win32more.Windows.AI.Actions.IActionEntityFactory3, sourceId: WinRT_String, fileKind: win32more.Windows.AI.Actions.RemoteFileKind, sourceUri: win32more.Windows.Foundation.Uri, fileId: WinRT_String, contentType: WinRT_String, driveId: WinRT_String, accountId: WinRT_String, extension: WinRT_String) -> win32more.Windows.AI.Actions.RemoteFileActionEntity: ...
    @winrt_mixinmethod
    def CreateTextEntityWithTextFormat(self: win32more.Windows.AI.Actions.IActionEntityFactory3, text: WinRT_String, textFormat: win32more.Windows.AI.Actions.ActionEntityTextFormat) -> win32more.Windows.AI.Actions.TextActionEntity: ...
    @winrt_mixinmethod
    def CreateStreamingTextActionEntityWriter(self: win32more.Windows.AI.Actions.IActionEntityFactory3, textFormat: win32more.Windows.AI.Actions.ActionEntityTextFormat) -> win32more.Windows.AI.Actions.StreamingTextActionEntityWriter: ...
    @winrt_mixinmethod
    def CreateTableEntity(self: win32more.Windows.AI.Actions.IActionEntityFactory4, data: PassArray[WinRT_String], columnCount: UInt32) -> win32more.Windows.AI.Actions.TableActionEntity: ...
    @winrt_mixinmethod
    def CreateContactEntity(self: win32more.Windows.AI.Actions.IActionEntityFactory4, contact: win32more.Windows.ApplicationModel.Contacts.Contact) -> win32more.Windows.AI.Actions.ContactActionEntity: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
class ActionEntityKind(Enum, Int32):
    None_ = 0
    Document = 1
    File = 2
    Photo = 3
    Text = 4
    StreamingText = 5
    RemoteFile = 6
    Table = 7
    Contact = 8
class ActionEntityTextFormat(Enum, Int32):
    Plain = 0
    Markdown = 1
class ActionFeedback(ComPtr):
    extends: IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.AI.Actions.IActionFeedback
    _classid_ = 'Windows.AI.Actions.ActionFeedback'
    @winrt_mixinmethod
    def get_FeedbackKind(self: win32more.Windows.AI.Actions.IActionFeedback) -> win32more.Windows.AI.Actions.ActionFeedbackKind: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    FeedbackKind = property(get_FeedbackKind, None)
class ActionFeedbackKind(Enum, Int32):
    Positive = 0
    Negative = 1
class ActionInvocationContext(ComPtr):
    extends: IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.AI.Actions.IActionInvocationContext
    _classid_ = 'Windows.AI.Actions.ActionInvocationContext'
    @winrt_mixinmethod
    def get_EntityFactory(self: win32more.Windows.AI.Actions.IActionInvocationContext) -> win32more.Windows.AI.Actions.ActionEntityFactory: ...
    @winrt_mixinmethod
    def SetInputEntity(self: win32more.Windows.AI.Actions.IActionInvocationContext, inputName: WinRT_String, inputValue: win32more.Windows.AI.Actions.ActionEntity) -> Void: ...
    @winrt_mixinmethod
    def GetInputEntities(self: win32more.Windows.AI.Actions.IActionInvocationContext) -> ReceiveArray[win32more.Windows.AI.Actions.NamedActionEntity]: ...
    @winrt_mixinmethod
    def SetOutputEntity(self: win32more.Windows.AI.Actions.IActionInvocationContext, outputName: WinRT_String, outputValue: win32more.Windows.AI.Actions.ActionEntity) -> Void: ...
    @winrt_mixinmethod
    def GetOutputEntities(self: win32more.Windows.AI.Actions.IActionInvocationContext) -> ReceiveArray[win32more.Windows.AI.Actions.NamedActionEntity]: ...
    @winrt_mixinmethod
    def get_Result(self: win32more.Windows.AI.Actions.IActionInvocationContext) -> win32more.Windows.AI.Actions.ActionInvocationResult: ...
    @winrt_mixinmethod
    def put_Result(self: win32more.Windows.AI.Actions.IActionInvocationContext, value: win32more.Windows.AI.Actions.ActionInvocationResult) -> Void: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.AI.Actions.IActionInvocationContext) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def put_ExtendedError(self: win32more.Windows.AI.Actions.IActionInvocationContext, value: win32more.Windows.Foundation.HResult) -> Void: ...
    @winrt_mixinmethod
    def get_InvokerWindowId(self: win32more.Windows.AI.Actions.IActionInvocationContext2) -> win32more.Windows.UI.WindowId: ...
    @winrt_mixinmethod
    def get_HelpDetails(self: win32more.Windows.AI.Actions.IActionInvocationContext2) -> win32more.Windows.AI.Actions.ActionInvocationHelpDetails: ...
    @winrt_mixinmethod
    def get_ActionId(self: win32more.Windows.AI.Actions.IActionInvocationContext2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_InvokerAppUserModelId(self: win32more.Windows.AI.Actions.IActionInvocationContext2) -> WinRT_String: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    ActionId = property(get_ActionId, None)
    EntityFactory = property(get_EntityFactory, None)
    ExtendedError = property(get_ExtendedError, put_ExtendedError)
    HelpDetails = property(get_HelpDetails, None)
    InvokerAppUserModelId = property(get_InvokerAppUserModelId, None)
    InvokerWindowId = property(get_InvokerWindowId, None)
    Result = property(get_Result, put_Result)
class ActionInvocationHelpDetails(ComPtr):
    extends: IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.AI.Actions.IActionInvocationHelpDetails
    _classid_ = 'Windows.AI.Actions.ActionInvocationHelpDetails'
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.AI.Actions.IActionInvocationHelpDetails) -> win32more.Windows.AI.Actions.ActionInvocationHelpKind: ...
    @winrt_mixinmethod
    def put_Kind(self: win32more.Windows.AI.Actions.IActionInvocationHelpDetails, value: win32more.Windows.AI.Actions.ActionInvocationHelpKind) -> Void: ...
    @winrt_mixinmethod
    def get_Title(self: win32more.Windows.AI.Actions.IActionInvocationHelpDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Title(self: win32more.Windows.AI.Actions.IActionInvocationHelpDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.AI.Actions.IActionInvocationHelpDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Description(self: win32more.Windows.AI.Actions.IActionInvocationHelpDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_HelpUri(self: win32more.Windows.AI.Actions.IActionInvocationHelpDetails) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_HelpUri(self: win32more.Windows.AI.Actions.IActionInvocationHelpDetails, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_HelpUriDescription(self: win32more.Windows.AI.Actions.IActionInvocationHelpDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_HelpUriDescription(self: win32more.Windows.AI.Actions.IActionInvocationHelpDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    Description = property(get_Description, put_Description)
    HelpUri = property(get_HelpUri, put_HelpUri)
    HelpUriDescription = property(get_HelpUriDescription, put_HelpUriDescription)
    Kind = property(get_Kind, put_Kind)
    Title = property(get_Title, put_Title)
class ActionInvocationHelpKind(Enum, Int32):
    None_ = 0
    Error = 1
    Warning = 2
class ActionInvocationResult(Enum, Int32):
    Success = 0
    UserCanceled = 1
    Unsupported = 2
    Unavailable = 3
class ActionRuntime(ComPtr):
    extends: IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.AI.Actions.IActionRuntime
    _classid_ = 'Windows.AI.Actions.ActionRuntime'
    @winrt_mixinmethod
    def get_ActionCatalog(self: win32more.Windows.AI.Actions.IActionRuntime) -> win32more.Windows.AI.Actions.Hosting.ActionCatalog: ...
    @winrt_mixinmethod
    def get_EntityFactory(self: win32more.Windows.AI.Actions.IActionRuntime) -> win32more.Windows.AI.Actions.ActionEntityFactory: ...
    @winrt_mixinmethod
    def CreateInvocationContext(self: win32more.Windows.AI.Actions.IActionRuntime, actionId: WinRT_String) -> win32more.Windows.AI.Actions.ActionInvocationContext: ...
    @winrt_mixinmethod
    def CreateActionFeedback(self: win32more.Windows.AI.Actions.IActionRuntime2, feedbackKind: win32more.Windows.AI.Actions.ActionFeedbackKind) -> win32more.Windows.AI.Actions.ActionFeedback: ...
    @winrt_mixinmethod
    def SetActionAvailability(self: win32more.Windows.AI.Actions.IActionRuntime2, actionId: WinRT_String, isAvailable: Boolean) -> Void: ...
    @winrt_mixinmethod
    def GetActionAvailability(self: win32more.Windows.AI.Actions.IActionRuntime2, actionId: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def CreateInvocationContextWithWindowId(self: win32more.Windows.AI.Actions.IActionRuntime3, actionId: WinRT_String, invokerWindowId: win32more.Windows.UI.WindowId) -> win32more.Windows.AI.Actions.ActionInvocationContext: ...
    @winrt_mixinmethod
    def GetActionEntityById(self: win32more.Windows.AI.Actions.IActionRuntime3, entityId: WinRT_String) -> win32more.Windows.AI.Actions.ActionEntity: ...
    @winrt_mixinmethod
    def get_LatestSupportedSchemaVersion(self: win32more.Windows.AI.Actions.IActionRuntime3) -> UInt32: ...
    @winrt_mixinmethod
    def GetActionInvocationContextFromToken(self: win32more.Windows.AI.Actions.IActionRuntime4, token: WinRT_String) -> win32more.Windows.AI.Actions.ActionInvocationContext: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    ActionCatalog = property(get_ActionCatalog, None)
    EntityFactory = property(get_EntityFactory, None)
    LatestSupportedSchemaVersion = property(get_LatestSupportedSchemaVersion, None)
ActionsContract: UInt32 = 327680
class ContactActionEntity(ComPtr):
    extends: win32more.Windows.AI.Actions.ActionEntity
    default_interface: win32more.Windows.AI.Actions.IContactActionEntity
    _classid_ = 'Windows.AI.Actions.ContactActionEntity'
    @winrt_mixinmethod
    def get_Contact(self: win32more.Windows.AI.Actions.IContactActionEntity) -> win32more.Windows.ApplicationModel.Contacts.Contact: ...
    Contact = property(get_Contact, None)
class DocumentActionEntity(ComPtr):
    extends: win32more.Windows.AI.Actions.ActionEntity
    default_interface: win32more.Windows.AI.Actions.IDocumentActionEntity
    _classid_ = 'Windows.AI.Actions.DocumentActionEntity'
    @winrt_mixinmethod
    def get_FullPath(self: win32more.Windows.AI.Actions.IDocumentActionEntity) -> WinRT_String: ...
    FullPath = property(get_FullPath, None)
class FileActionEntity(ComPtr):
    extends: win32more.Windows.AI.Actions.ActionEntity
    default_interface: win32more.Windows.AI.Actions.IFileActionEntity
    _classid_ = 'Windows.AI.Actions.FileActionEntity'
    @winrt_mixinmethod
    def get_FullPath(self: win32more.Windows.AI.Actions.IFileActionEntity) -> WinRT_String: ...
    FullPath = property(get_FullPath, None)
class IActionEntity(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Actions.IActionEntity'
    _iid_ = Guid('{445e700f-2122-5668-9a16-4cab2982c5f4}')
    @winrt_commethod(6)
    def get_Kind(self) -> win32more.Windows.AI.Actions.ActionEntityKind: ...
    @winrt_commethod(7)
    def get_DisplayInfo(self) -> win32more.Windows.AI.Actions.ActionEntityDisplayInfo: ...
    DisplayInfo = property(get_DisplayInfo, None)
    Kind = property(get_Kind, None)
class IActionEntity2(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Actions.IActionEntity2'
    _iid_ = Guid('{98fe136d-dd3a-58c1-af76-feb4e19dce9e}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    Id = property(get_Id, None)
class IActionEntityDisplayInfo(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Actions.IActionEntityDisplayInfo'
    _iid_ = Guid('{057a9ede-03e1-55c6-acba-c7056216735a}')
    @winrt_commethod(6)
    def get_Title(self) -> WinRT_String: ...
    Title = property(get_Title, None)
class IActionEntityFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Actions.IActionEntityFactory'
    _iid_ = Guid('{9cb752a0-5bf8-5be2-916e-b00eff80088d}')
class IActionEntityFactory2(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Actions.IActionEntityFactory2'
    _iid_ = Guid('{ea2fb6a5-ec6d-5180-9d30-bc663b84e7b8}')
    @winrt_commethod(6)
    def CreateFileEntity(self, path: WinRT_String) -> win32more.Windows.AI.Actions.FileActionEntity: ...
    @winrt_commethod(7)
    def CreateDocumentEntity(self, path: WinRT_String) -> win32more.Windows.AI.Actions.DocumentActionEntity: ...
    @winrt_commethod(8)
    def CreatePhotoEntity(self, path: WinRT_String) -> win32more.Windows.AI.Actions.PhotoActionEntity: ...
    @winrt_commethod(9)
    def CreateTextEntity(self, text: WinRT_String) -> win32more.Windows.AI.Actions.TextActionEntity: ...
class IActionEntityFactory3(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Actions.IActionEntityFactory3'
    _iid_ = Guid('{4910e689-00b5-56bb-9c65-0fcc76215283}')
    @winrt_commethod(6)
    def CreateRemoteFileEntity(self, sourceId: WinRT_String, fileKind: win32more.Windows.AI.Actions.RemoteFileKind, sourceUri: win32more.Windows.Foundation.Uri, fileId: WinRT_String, contentType: WinRT_String, driveId: WinRT_String, accountId: WinRT_String, extension: WinRT_String) -> win32more.Windows.AI.Actions.RemoteFileActionEntity: ...
    @winrt_commethod(7)
    def CreateTextEntityWithTextFormat(self, text: WinRT_String, textFormat: win32more.Windows.AI.Actions.ActionEntityTextFormat) -> win32more.Windows.AI.Actions.TextActionEntity: ...
    @winrt_commethod(8)
    def CreateStreamingTextActionEntityWriter(self, textFormat: win32more.Windows.AI.Actions.ActionEntityTextFormat) -> win32more.Windows.AI.Actions.StreamingTextActionEntityWriter: ...
class IActionEntityFactory4(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Actions.IActionEntityFactory4'
    _iid_ = Guid('{332eda05-de0e-5a58-b318-a2ad771f013d}')
    @winrt_commethod(6)
    def CreateTableEntity(self, data: PassArray[WinRT_String], columnCount: UInt32) -> win32more.Windows.AI.Actions.TableActionEntity: ...
    @winrt_commethod(7)
    def CreateContactEntity(self, contact: win32more.Windows.ApplicationModel.Contacts.Contact) -> win32more.Windows.AI.Actions.ContactActionEntity: ...
class IActionEntityFactoryFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Actions.IActionEntityFactoryFactory'
    _iid_ = Guid('{c9147d8f-88a0-5ec0-a564-47e2a1081412}')
class IActionFeedback(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Actions.IActionFeedback'
    _iid_ = Guid('{a12ee7ab-2454-56c9-bbdf-c089457fbc5e}')
    @winrt_commethod(6)
    def get_FeedbackKind(self) -> win32more.Windows.AI.Actions.ActionFeedbackKind: ...
    FeedbackKind = property(get_FeedbackKind, None)
class IActionInvocationContext(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Actions.IActionInvocationContext'
    _iid_ = Guid('{c32b622e-86e1-5eba-9661-605910104978}')
    @winrt_commethod(6)
    def get_EntityFactory(self) -> win32more.Windows.AI.Actions.ActionEntityFactory: ...
    @winrt_commethod(7)
    def SetInputEntity(self, inputName: WinRT_String, inputValue: win32more.Windows.AI.Actions.ActionEntity) -> Void: ...
    @winrt_commethod(8)
    def GetInputEntities(self) -> ReceiveArray[win32more.Windows.AI.Actions.NamedActionEntity]: ...
    @winrt_commethod(9)
    def SetOutputEntity(self, outputName: WinRT_String, outputValue: win32more.Windows.AI.Actions.ActionEntity) -> Void: ...
    @winrt_commethod(10)
    def GetOutputEntities(self) -> ReceiveArray[win32more.Windows.AI.Actions.NamedActionEntity]: ...
    @winrt_commethod(11)
    def get_Result(self) -> win32more.Windows.AI.Actions.ActionInvocationResult: ...
    @winrt_commethod(12)
    def put_Result(self, value: win32more.Windows.AI.Actions.ActionInvocationResult) -> Void: ...
    @winrt_commethod(13)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    @winrt_commethod(14)
    def put_ExtendedError(self, value: win32more.Windows.Foundation.HResult) -> Void: ...
    EntityFactory = property(get_EntityFactory, None)
    ExtendedError = property(get_ExtendedError, put_ExtendedError)
    Result = property(get_Result, put_Result)
class IActionInvocationContext2(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Actions.IActionInvocationContext2'
    _iid_ = Guid('{7c843086-9279-5bcd-8f2e-d15121e7a827}')
    @winrt_commethod(6)
    def get_InvokerWindowId(self) -> win32more.Windows.UI.WindowId: ...
    @winrt_commethod(7)
    def get_HelpDetails(self) -> win32more.Windows.AI.Actions.ActionInvocationHelpDetails: ...
    @winrt_commethod(8)
    def get_ActionId(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_InvokerAppUserModelId(self) -> WinRT_String: ...
    ActionId = property(get_ActionId, None)
    HelpDetails = property(get_HelpDetails, None)
    InvokerAppUserModelId = property(get_InvokerAppUserModelId, None)
    InvokerWindowId = property(get_InvokerWindowId, None)
class IActionInvocationHelpDetails(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Actions.IActionInvocationHelpDetails'
    _iid_ = Guid('{5430f272-078f-5722-8f7d-90cf8ddd595e}')
    @winrt_commethod(6)
    def get_Kind(self) -> win32more.Windows.AI.Actions.ActionInvocationHelpKind: ...
    @winrt_commethod(7)
    def put_Kind(self, value: win32more.Windows.AI.Actions.ActionInvocationHelpKind) -> Void: ...
    @winrt_commethod(8)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Title(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_Description(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_HelpUri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(13)
    def put_HelpUri(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(14)
    def get_HelpUriDescription(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def put_HelpUriDescription(self, value: WinRT_String) -> Void: ...
    Description = property(get_Description, put_Description)
    HelpUri = property(get_HelpUri, put_HelpUri)
    HelpUriDescription = property(get_HelpUriDescription, put_HelpUriDescription)
    Kind = property(get_Kind, put_Kind)
    Title = property(get_Title, put_Title)
class IActionRuntime(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Actions.IActionRuntime'
    _iid_ = Guid('{206efa2c-c909-508a-b4b0-9482be96db9c}')
    @winrt_commethod(6)
    def get_ActionCatalog(self) -> win32more.Windows.AI.Actions.Hosting.ActionCatalog: ...
    @winrt_commethod(7)
    def get_EntityFactory(self) -> win32more.Windows.AI.Actions.ActionEntityFactory: ...
    @winrt_commethod(8)
    def CreateInvocationContext(self, actionId: WinRT_String) -> win32more.Windows.AI.Actions.ActionInvocationContext: ...
    ActionCatalog = property(get_ActionCatalog, None)
    EntityFactory = property(get_EntityFactory, None)
class IActionRuntime2(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Actions.IActionRuntime2'
    _iid_ = Guid('{2da4d2c0-e593-5350-8143-15bb24f63411}')
    @winrt_commethod(6)
    def CreateActionFeedback(self, feedbackKind: win32more.Windows.AI.Actions.ActionFeedbackKind) -> win32more.Windows.AI.Actions.ActionFeedback: ...
    @winrt_commethod(7)
    def SetActionAvailability(self, actionId: WinRT_String, isAvailable: Boolean) -> Void: ...
    @winrt_commethod(8)
    def GetActionAvailability(self, actionId: WinRT_String) -> Boolean: ...
class IActionRuntime3(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Actions.IActionRuntime3'
    _iid_ = Guid('{f020c3c0-caec-5928-ad00-81069b80fbc1}')
    @winrt_commethod(6)
    def CreateInvocationContextWithWindowId(self, actionId: WinRT_String, invokerWindowId: win32more.Windows.UI.WindowId) -> win32more.Windows.AI.Actions.ActionInvocationContext: ...
    @winrt_commethod(7)
    def GetActionEntityById(self, entityId: WinRT_String) -> win32more.Windows.AI.Actions.ActionEntity: ...
    @winrt_commethod(8)
    def get_LatestSupportedSchemaVersion(self) -> UInt32: ...
    LatestSupportedSchemaVersion = property(get_LatestSupportedSchemaVersion, None)
class IActionRuntime4(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Actions.IActionRuntime4'
    _iid_ = Guid('{06851dcd-c743-5c7f-88a1-bbaeb02f5e28}')
    @winrt_commethod(6)
    def GetActionInvocationContextFromToken(self, token: WinRT_String) -> win32more.Windows.AI.Actions.ActionInvocationContext: ...
class IActionRuntimeFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Actions.IActionRuntimeFactory'
    _iid_ = Guid('{d3f366e9-8dc9-50a0-8040-e5c14fa609d6}')
class IContactActionEntity(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Actions.IContactActionEntity'
    _iid_ = Guid('{458c3e07-5892-5485-bd9b-8f7a540c9501}')
    @winrt_commethod(6)
    def get_Contact(self) -> win32more.Windows.ApplicationModel.Contacts.Contact: ...
    Contact = property(get_Contact, None)
class IDocumentActionEntity(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Actions.IDocumentActionEntity'
    _iid_ = Guid('{56715297-960b-59ff-af4b-ece1098b2e36}')
    @winrt_commethod(6)
    def get_FullPath(self) -> WinRT_String: ...
    FullPath = property(get_FullPath, None)
class IFileActionEntity(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Actions.IFileActionEntity'
    _iid_ = Guid('{f20ab43f-4c80-5904-bd42-3e6248babfcf}')
    @winrt_commethod(6)
    def get_FullPath(self) -> WinRT_String: ...
    FullPath = property(get_FullPath, None)
class INamedActionEntity(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Actions.INamedActionEntity'
    _iid_ = Guid('{1aaebeef-435b-5a0d-8182-05fe4dd47712}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Name(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Entity(self) -> win32more.Windows.AI.Actions.ActionEntity: ...
    @winrt_commethod(9)
    def put_Entity(self, value: win32more.Windows.AI.Actions.ActionEntity) -> Void: ...
    Entity = property(get_Entity, put_Entity)
    Name = property(get_Name, put_Name)
class IPhotoActionEntity(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Actions.IPhotoActionEntity'
    _iid_ = Guid('{425123b3-20ef-51a6-b35f-8414384765c5}')
    @winrt_commethod(6)
    def get_FullPath(self) -> WinRT_String: ...
    FullPath = property(get_FullPath, None)
class IRemoteFileActionEntity(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Actions.IRemoteFileActionEntity'
    _iid_ = Guid('{a5d8ec21-a2bd-545a-abfc-d7aa79fd0b81}')
    @winrt_commethod(6)
    def get_SourceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_FileKind(self) -> win32more.Windows.AI.Actions.RemoteFileKind: ...
    @winrt_commethod(8)
    def get_SourceUri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(9)
    def get_FileId(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_ContentType(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_DriveId(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_AccountId(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_Extension(self) -> WinRT_String: ...
    AccountId = property(get_AccountId, None)
    ContentType = property(get_ContentType, None)
    DriveId = property(get_DriveId, None)
    Extension = property(get_Extension, None)
    FileId = property(get_FileId, None)
    FileKind = property(get_FileKind, None)
    SourceId = property(get_SourceId, None)
    SourceUri = property(get_SourceUri, None)
class IStreamingTextActionEntity(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Actions.IStreamingTextActionEntity'
    _iid_ = Guid('{44cd8a16-abc9-5703-b4bf-6fe8b7a802fd}')
    @winrt_commethod(6)
    def get_IsComplete(self) -> Boolean: ...
    @winrt_commethod(7)
    def GetText(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_TextFormat(self) -> win32more.Windows.AI.Actions.ActionEntityTextFormat: ...
    @winrt_commethod(9)
    def add_TextChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.AI.Actions.StreamingTextActionEntity, win32more.Windows.AI.Actions.StreamingTextActionEntityTextChangedArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_TextChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsComplete = property(get_IsComplete, None)
    TextFormat = property(get_TextFormat, None)
    TextChanged = event()
class IStreamingTextActionEntityTextChangedArgs(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Actions.IStreamingTextActionEntityTextChangedArgs'
    _iid_ = Guid('{2c62011f-3e06-588b-a3bd-d726bd82fb13}')
    @winrt_commethod(6)
    def get_Text(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_IsComplete(self) -> Boolean: ...
    IsComplete = property(get_IsComplete, None)
    Text = property(get_Text, None)
class IStreamingTextActionEntityWriter(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Actions.IStreamingTextActionEntityWriter'
    _iid_ = Guid('{6bce2f76-a8af-5ff2-833c-108737ba0f42}')
    @winrt_commethod(6)
    def get_ReaderEntity(self) -> win32more.Windows.AI.Actions.StreamingTextActionEntity: ...
    @winrt_commethod(7)
    def get_TextFormat(self) -> win32more.Windows.AI.Actions.ActionEntityTextFormat: ...
    @winrt_commethod(8)
    def SetText(self, text: WinRT_String) -> Void: ...
    ReaderEntity = property(get_ReaderEntity, None)
    TextFormat = property(get_TextFormat, None)
class ITableActionEntity(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Actions.ITableActionEntity'
    _iid_ = Guid('{0f252cdb-ba24-5dbb-9d17-1b300773d141}')
    @winrt_commethod(6)
    def GetTextContent(self) -> ReceiveArray[WinRT_String]: ...
    @winrt_commethod(7)
    def get_RowCount(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_ColumnCount(self) -> UInt32: ...
    ColumnCount = property(get_ColumnCount, None)
    RowCount = property(get_RowCount, None)
class ITextActionEntity(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Actions.ITextActionEntity'
    _iid_ = Guid('{3c4ec25f-5adb-5f73-b8f3-080fbeadd612}')
    @winrt_commethod(6)
    def get_Text(self) -> WinRT_String: ...
    Text = property(get_Text, None)
class ITextActionEntity2(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Actions.ITextActionEntity2'
    _iid_ = Guid('{7c500889-cf08-51e7-beca-f0bbc7a7486c}')
    @winrt_commethod(6)
    def get_TextFormat(self) -> win32more.Windows.AI.Actions.ActionEntityTextFormat: ...
    TextFormat = property(get_TextFormat, None)
class NamedActionEntity(ComPtr):
    extends: IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.AI.Actions.INamedActionEntity
    _classid_ = 'Windows.AI.Actions.NamedActionEntity'
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.AI.Actions.INamedActionEntity) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Name(self: win32more.Windows.AI.Actions.INamedActionEntity, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Entity(self: win32more.Windows.AI.Actions.INamedActionEntity) -> win32more.Windows.AI.Actions.ActionEntity: ...
    @winrt_mixinmethod
    def put_Entity(self: win32more.Windows.AI.Actions.INamedActionEntity, value: win32more.Windows.AI.Actions.ActionEntity) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    Entity = property(get_Entity, put_Entity)
    Name = property(get_Name, put_Name)
class PhotoActionEntity(ComPtr):
    extends: win32more.Windows.AI.Actions.ActionEntity
    default_interface: win32more.Windows.AI.Actions.IPhotoActionEntity
    _classid_ = 'Windows.AI.Actions.PhotoActionEntity'
    @winrt_mixinmethod
    def get_FullPath(self: win32more.Windows.AI.Actions.IPhotoActionEntity) -> WinRT_String: ...
    FullPath = property(get_FullPath, None)
class RemoteFileActionEntity(ComPtr):
    extends: win32more.Windows.AI.Actions.ActionEntity
    default_interface: win32more.Windows.AI.Actions.IRemoteFileActionEntity
    _classid_ = 'Windows.AI.Actions.RemoteFileActionEntity'
    @winrt_mixinmethod
    def get_SourceId(self: win32more.Windows.AI.Actions.IRemoteFileActionEntity) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FileKind(self: win32more.Windows.AI.Actions.IRemoteFileActionEntity) -> win32more.Windows.AI.Actions.RemoteFileKind: ...
    @winrt_mixinmethod
    def get_SourceUri(self: win32more.Windows.AI.Actions.IRemoteFileActionEntity) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_FileId(self: win32more.Windows.AI.Actions.IRemoteFileActionEntity) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ContentType(self: win32more.Windows.AI.Actions.IRemoteFileActionEntity) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DriveId(self: win32more.Windows.AI.Actions.IRemoteFileActionEntity) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AccountId(self: win32more.Windows.AI.Actions.IRemoteFileActionEntity) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Extension(self: win32more.Windows.AI.Actions.IRemoteFileActionEntity) -> WinRT_String: ...
    AccountId = property(get_AccountId, None)
    ContentType = property(get_ContentType, None)
    DriveId = property(get_DriveId, None)
    Extension = property(get_Extension, None)
    FileId = property(get_FileId, None)
    FileKind = property(get_FileKind, None)
    SourceId = property(get_SourceId, None)
    SourceUri = property(get_SourceUri, None)
class RemoteFileKind(Enum, Int32):
    Document = 0
    Photo = 1
    File = 2
class StreamingTextActionEntity(ComPtr):
    extends: win32more.Windows.AI.Actions.ActionEntity
    default_interface: win32more.Windows.AI.Actions.IStreamingTextActionEntity
    _classid_ = 'Windows.AI.Actions.StreamingTextActionEntity'
    @winrt_mixinmethod
    def get_IsComplete(self: win32more.Windows.AI.Actions.IStreamingTextActionEntity) -> Boolean: ...
    @winrt_mixinmethod
    def GetText(self: win32more.Windows.AI.Actions.IStreamingTextActionEntity) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TextFormat(self: win32more.Windows.AI.Actions.IStreamingTextActionEntity) -> win32more.Windows.AI.Actions.ActionEntityTextFormat: ...
    @winrt_mixinmethod
    def add_TextChanged(self: win32more.Windows.AI.Actions.IStreamingTextActionEntity, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.AI.Actions.StreamingTextActionEntity, win32more.Windows.AI.Actions.StreamingTextActionEntityTextChangedArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TextChanged(self: win32more.Windows.AI.Actions.IStreamingTextActionEntity, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsComplete = property(get_IsComplete, None)
    TextFormat = property(get_TextFormat, None)
    TextChanged = event()
class StreamingTextActionEntityTextChangedArgs(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.AI.Actions.IStreamingTextActionEntityTextChangedArgs
    _classid_ = 'Windows.AI.Actions.StreamingTextActionEntityTextChangedArgs'
    @winrt_mixinmethod
    def get_Text(self: win32more.Windows.AI.Actions.IStreamingTextActionEntityTextChangedArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsComplete(self: win32more.Windows.AI.Actions.IStreamingTextActionEntityTextChangedArgs) -> Boolean: ...
    IsComplete = property(get_IsComplete, None)
    Text = property(get_Text, None)
class StreamingTextActionEntityWriter(ComPtr):
    extends: IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.AI.Actions.IStreamingTextActionEntityWriter
    _classid_ = 'Windows.AI.Actions.StreamingTextActionEntityWriter'
    @winrt_mixinmethod
    def get_ReaderEntity(self: win32more.Windows.AI.Actions.IStreamingTextActionEntityWriter) -> win32more.Windows.AI.Actions.StreamingTextActionEntity: ...
    @winrt_mixinmethod
    def get_TextFormat(self: win32more.Windows.AI.Actions.IStreamingTextActionEntityWriter) -> win32more.Windows.AI.Actions.ActionEntityTextFormat: ...
    @winrt_mixinmethod
    def SetText(self: win32more.Windows.AI.Actions.IStreamingTextActionEntityWriter, text: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    ReaderEntity = property(get_ReaderEntity, None)
    TextFormat = property(get_TextFormat, None)
class TableActionEntity(ComPtr):
    extends: win32more.Windows.AI.Actions.ActionEntity
    default_interface: win32more.Windows.AI.Actions.ITableActionEntity
    _classid_ = 'Windows.AI.Actions.TableActionEntity'
    @winrt_mixinmethod
    def GetTextContent(self: win32more.Windows.AI.Actions.ITableActionEntity) -> ReceiveArray[WinRT_String]: ...
    @winrt_mixinmethod
    def get_RowCount(self: win32more.Windows.AI.Actions.ITableActionEntity) -> UInt32: ...
    @winrt_mixinmethod
    def get_ColumnCount(self: win32more.Windows.AI.Actions.ITableActionEntity) -> UInt32: ...
    ColumnCount = property(get_ColumnCount, None)
    RowCount = property(get_RowCount, None)
class TextActionEntity(ComPtr):
    extends: win32more.Windows.AI.Actions.ActionEntity
    default_interface: win32more.Windows.AI.Actions.ITextActionEntity
    _classid_ = 'Windows.AI.Actions.TextActionEntity'
    @winrt_mixinmethod
    def get_Text(self: win32more.Windows.AI.Actions.ITextActionEntity) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TextFormat(self: win32more.Windows.AI.Actions.ITextActionEntity2) -> win32more.Windows.AI.Actions.ActionEntityTextFormat: ...
    Text = property(get_Text, None)
    TextFormat = property(get_TextFormat, None)


make_ready(__name__)
