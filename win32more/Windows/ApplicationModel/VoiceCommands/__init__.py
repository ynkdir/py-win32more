from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel.AppService
import win32more.Windows.ApplicationModel.VoiceCommands
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Globalization
import win32more.Windows.Media.SpeechRecognition
import win32more.Windows.Storage
import win32more.Windows.Win32.System.WinRT
class IVoiceCommand(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.VoiceCommands.IVoiceCommand'
    _iid_ = Guid('{936f5273-ec82-42a6-a55c-d2d79ec6f920}')
    @winrt_commethod(6)
    def get_CommandName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Properties(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]]: ...
    @winrt_commethod(8)
    def get_SpeechRecognitionResult(self) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognitionResult: ...
    CommandName = property(get_CommandName, None)
    Properties = property(get_Properties, None)
    SpeechRecognitionResult = property(get_SpeechRecognitionResult, None)
class IVoiceCommandCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.VoiceCommands.IVoiceCommandCompletedEventArgs'
    _iid_ = Guid('{c85e675d-fe42-432c-9907-09df9fcf64e8}')
    @winrt_commethod(6)
    def get_Reason(self) -> win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandCompletionReason: ...
    Reason = property(get_Reason, None)
class IVoiceCommandConfirmationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.VoiceCommands.IVoiceCommandConfirmationResult'
    _iid_ = Guid('{a022593e-8221-4526-b083-840972262247}')
    @winrt_commethod(6)
    def get_Confirmed(self) -> Boolean: ...
    Confirmed = property(get_Confirmed, None)
class IVoiceCommandContentTile(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.VoiceCommands.IVoiceCommandContentTile'
    _iid_ = Guid('{3eefe9f0-b8c7-4c76-a0de-1607895ee327}')
    @winrt_commethod(6)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Title(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_TextLine1(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_TextLine1(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_TextLine2(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_TextLine2(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_TextLine3(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def put_TextLine3(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(14)
    def get_Image(self) -> win32more.Windows.Storage.IStorageFile: ...
    @winrt_commethod(15)
    def put_Image(self, value: win32more.Windows.Storage.IStorageFile) -> Void: ...
    @winrt_commethod(16)
    def get_AppContext(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(17)
    def put_AppContext(self, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(18)
    def get_AppLaunchArgument(self) -> WinRT_String: ...
    @winrt_commethod(19)
    def put_AppLaunchArgument(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(20)
    def get_ContentTileType(self) -> win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandContentTileType: ...
    @winrt_commethod(21)
    def put_ContentTileType(self, value: win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandContentTileType) -> Void: ...
    AppContext = property(get_AppContext, put_AppContext)
    AppLaunchArgument = property(get_AppLaunchArgument, put_AppLaunchArgument)
    ContentTileType = property(get_ContentTileType, put_ContentTileType)
    Image = property(get_Image, put_Image)
    TextLine1 = property(get_TextLine1, put_TextLine1)
    TextLine2 = property(get_TextLine2, put_TextLine2)
    TextLine3 = property(get_TextLine3, put_TextLine3)
    Title = property(get_Title, put_Title)
class IVoiceCommandDefinition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.VoiceCommands.IVoiceCommandDefinition'
    _iid_ = Guid('{7972aad0-0974-4979-984b-cb8959cd61ae}')
    @winrt_commethod(6)
    def get_Language(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def SetPhraseListAsync(self, phraseListName: WinRT_String, phraseList: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncAction: ...
    Language = property(get_Language, None)
    Name = property(get_Name, None)
class IVoiceCommandDefinitionManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.VoiceCommands.IVoiceCommandDefinitionManagerStatics'
    _iid_ = Guid('{8fe7a69e-067e-4f16-a18c-5b17e9499940}')
    @winrt_commethod(6)
    def InstallCommandDefinitionsFromStorageFileAsync(self, file: win32more.Windows.Storage.StorageFile) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def get_InstalledCommandDefinitions(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandDefinition]: ...
    InstalledCommandDefinitions = property(get_InstalledCommandDefinitions, None)
class IVoiceCommandDisambiguationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.VoiceCommands.IVoiceCommandDisambiguationResult'
    _iid_ = Guid('{ecc68cfe-c9ac-45df-a8ea-feea08ef9c5e}')
    @winrt_commethod(6)
    def get_SelectedItem(self) -> win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandContentTile: ...
    SelectedItem = property(get_SelectedItem, None)
class IVoiceCommandResponse(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.VoiceCommands.IVoiceCommandResponse'
    _iid_ = Guid('{0284b30e-8a3b-4cc4-a6a1-cad5be2716b5}')
    @winrt_commethod(6)
    def get_Message(self) -> win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandUserMessage: ...
    @winrt_commethod(7)
    def put_Message(self, value: win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandUserMessage) -> Void: ...
    @winrt_commethod(8)
    def get_RepeatMessage(self) -> win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandUserMessage: ...
    @winrt_commethod(9)
    def put_RepeatMessage(self, value: win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandUserMessage) -> Void: ...
    @winrt_commethod(10)
    def get_AppLaunchArgument(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_AppLaunchArgument(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_VoiceCommandContentTiles(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandContentTile]: ...
    AppLaunchArgument = property(get_AppLaunchArgument, put_AppLaunchArgument)
    Message = property(get_Message, put_Message)
    RepeatMessage = property(get_RepeatMessage, put_RepeatMessage)
    VoiceCommandContentTiles = property(get_VoiceCommandContentTiles, None)
class IVoiceCommandResponseStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.VoiceCommands.IVoiceCommandResponseStatics'
    _iid_ = Guid('{2932f813-0d3b-49f2-96dd-625019bd3b5d}')
    @winrt_commethod(6)
    def get_MaxSupportedVoiceCommandContentTiles(self) -> UInt32: ...
    @winrt_commethod(7)
    def CreateResponse(self, userMessage: win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandUserMessage) -> win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandResponse: ...
    @winrt_commethod(8)
    def CreateResponseWithTiles(self, message: win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandUserMessage, contentTiles: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandContentTile]) -> win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandResponse: ...
    @winrt_commethod(9)
    def CreateResponseForPrompt(self, message: win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandUserMessage, repeatMessage: win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandUserMessage) -> win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandResponse: ...
    @winrt_commethod(10)
    def CreateResponseForPromptWithTiles(self, message: win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandUserMessage, repeatMessage: win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandUserMessage, contentTiles: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandContentTile]) -> win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandResponse: ...
    MaxSupportedVoiceCommandContentTiles = property(get_MaxSupportedVoiceCommandContentTiles, None)
class IVoiceCommandServiceConnection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.VoiceCommands.IVoiceCommandServiceConnection'
    _iid_ = Guid('{d894bb9f-21da-44a4-98a2-fb131920a9cc}')
    @winrt_commethod(6)
    def GetVoiceCommandAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommand]: ...
    @winrt_commethod(7)
    def RequestConfirmationAsync(self, response: win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandResponse) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandConfirmationResult]: ...
    @winrt_commethod(8)
    def RequestDisambiguationAsync(self, response: win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandResponse) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandDisambiguationResult]: ...
    @winrt_commethod(9)
    def ReportProgressAsync(self, response: win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandResponse) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def ReportSuccessAsync(self, response: win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandResponse) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(11)
    def ReportFailureAsync(self, response: win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandResponse) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(12)
    def RequestAppLaunchAsync(self, response: win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandResponse) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(13)
    def get_Language(self) -> win32more.Windows.Globalization.Language: ...
    @winrt_commethod(14)
    def add_VoiceCommandCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandServiceConnection, win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_VoiceCommandCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Language = property(get_Language, None)
    VoiceCommandCompleted = event()
class IVoiceCommandServiceConnectionStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.VoiceCommands.IVoiceCommandServiceConnectionStatics'
    _iid_ = Guid('{370ebffb-2d34-42df-8770-074d0f334697}')
    @winrt_commethod(6)
    def FromAppServiceTriggerDetails(self, triggerDetails: win32more.Windows.ApplicationModel.AppService.AppServiceTriggerDetails) -> win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandServiceConnection: ...
class IVoiceCommandUserMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.VoiceCommands.IVoiceCommandUserMessage'
    _iid_ = Guid('{674eb3c0-44f6-4f07-b979-4c723fc08597}')
    @winrt_commethod(6)
    def get_DisplayMessage(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_DisplayMessage(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_SpokenMessage(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_SpokenMessage(self, value: WinRT_String) -> Void: ...
    DisplayMessage = property(get_DisplayMessage, put_DisplayMessage)
    SpokenMessage = property(get_SpokenMessage, put_SpokenMessage)
class VoiceCommand(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommand
    _classid_ = 'Windows.ApplicationModel.VoiceCommands.VoiceCommand'
    @winrt_mixinmethod
    def get_CommandName(self: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommand) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommand) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]]: ...
    @winrt_mixinmethod
    def get_SpeechRecognitionResult(self: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommand) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognitionResult: ...
    CommandName = property(get_CommandName, None)
    Properties = property(get_Properties, None)
    SpeechRecognitionResult = property(get_SpeechRecognitionResult, None)
class VoiceCommandCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandCompletedEventArgs
    _classid_ = 'Windows.ApplicationModel.VoiceCommands.VoiceCommandCompletedEventArgs'
    @winrt_mixinmethod
    def get_Reason(self: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandCompletedEventArgs) -> win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandCompletionReason: ...
    Reason = property(get_Reason, None)
class VoiceCommandCompletionReason(Enum, Int32):
    Unknown = 0
    CommunicationFailed = 1
    ResourceLimitsExceeded = 2
    Canceled = 3
    TimeoutExceeded = 4
    AppLaunched = 5
    Completed = 6
class VoiceCommandConfirmationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandConfirmationResult
    _classid_ = 'Windows.ApplicationModel.VoiceCommands.VoiceCommandConfirmationResult'
    @winrt_mixinmethod
    def get_Confirmed(self: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandConfirmationResult) -> Boolean: ...
    Confirmed = property(get_Confirmed, None)
class VoiceCommandContentTile(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandContentTile
    _classid_ = 'Windows.ApplicationModel.VoiceCommands.VoiceCommandContentTile'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandContentTile.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandContentTile: ...
    @winrt_mixinmethod
    def get_Title(self: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandContentTile) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Title(self: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandContentTile, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_TextLine1(self: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandContentTile) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TextLine1(self: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandContentTile, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_TextLine2(self: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandContentTile) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TextLine2(self: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandContentTile, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_TextLine3(self: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandContentTile) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TextLine3(self: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandContentTile, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Image(self: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandContentTile) -> win32more.Windows.Storage.IStorageFile: ...
    @winrt_mixinmethod
    def put_Image(self: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandContentTile, value: win32more.Windows.Storage.IStorageFile) -> Void: ...
    @winrt_mixinmethod
    def get_AppContext(self: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandContentTile) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def put_AppContext(self: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandContentTile, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def get_AppLaunchArgument(self: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandContentTile) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_AppLaunchArgument(self: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandContentTile, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ContentTileType(self: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandContentTile) -> win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandContentTileType: ...
    @winrt_mixinmethod
    def put_ContentTileType(self: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandContentTile, value: win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandContentTileType) -> Void: ...
    AppContext = property(get_AppContext, put_AppContext)
    AppLaunchArgument = property(get_AppLaunchArgument, put_AppLaunchArgument)
    ContentTileType = property(get_ContentTileType, put_ContentTileType)
    Image = property(get_Image, put_Image)
    TextLine1 = property(get_TextLine1, put_TextLine1)
    TextLine2 = property(get_TextLine2, put_TextLine2)
    TextLine3 = property(get_TextLine3, put_TextLine3)
    Title = property(get_Title, put_Title)
class VoiceCommandContentTileType(Enum, Int32):
    TitleOnly = 0
    TitleWithText = 1
    TitleWith68x68Icon = 2
    TitleWith68x68IconAndText = 3
    TitleWith68x92Icon = 4
    TitleWith68x92IconAndText = 5
    TitleWith280x140Icon = 6
    TitleWith280x140IconAndText = 7
class VoiceCommandDefinition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandDefinition
    _classid_ = 'Windows.ApplicationModel.VoiceCommands.VoiceCommandDefinition'
    @winrt_mixinmethod
    def get_Language(self: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandDefinition) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandDefinition) -> WinRT_String: ...
    @winrt_mixinmethod
    def SetPhraseListAsync(self: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandDefinition, phraseListName: WinRT_String, phraseList: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncAction: ...
    Language = property(get_Language, None)
    Name = property(get_Name, None)
class _VoiceCommandDefinitionManager_Meta_(ComPtr.__class__):
    pass
class VoiceCommandDefinitionManager(ComPtr, metaclass=_VoiceCommandDefinitionManager_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.VoiceCommands.VoiceCommandDefinitionManager'
    @winrt_classmethod
    def InstallCommandDefinitionsFromStorageFileAsync(cls: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandDefinitionManagerStatics, file: win32more.Windows.Storage.StorageFile) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def get_InstalledCommandDefinitions(cls: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandDefinitionManagerStatics) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandDefinition]: ...
    _VoiceCommandDefinitionManager_Meta_.InstalledCommandDefinitions = property(get_InstalledCommandDefinitions, None)
class VoiceCommandDisambiguationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandDisambiguationResult
    _classid_ = 'Windows.ApplicationModel.VoiceCommands.VoiceCommandDisambiguationResult'
    @winrt_mixinmethod
    def get_SelectedItem(self: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandDisambiguationResult) -> win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandContentTile: ...
    SelectedItem = property(get_SelectedItem, None)
class _VoiceCommandResponse_Meta_(ComPtr.__class__):
    pass
class VoiceCommandResponse(ComPtr, metaclass=_VoiceCommandResponse_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandResponse
    _classid_ = 'Windows.ApplicationModel.VoiceCommands.VoiceCommandResponse'
    @winrt_mixinmethod
    def get_Message(self: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandResponse) -> win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandUserMessage: ...
    @winrt_mixinmethod
    def put_Message(self: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandResponse, value: win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandUserMessage) -> Void: ...
    @winrt_mixinmethod
    def get_RepeatMessage(self: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandResponse) -> win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandUserMessage: ...
    @winrt_mixinmethod
    def put_RepeatMessage(self: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandResponse, value: win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandUserMessage) -> Void: ...
    @winrt_mixinmethod
    def get_AppLaunchArgument(self: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandResponse) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_AppLaunchArgument(self: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandResponse, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_VoiceCommandContentTiles(self: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandResponse) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandContentTile]: ...
    @winrt_classmethod
    def get_MaxSupportedVoiceCommandContentTiles(cls: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandResponseStatics) -> UInt32: ...
    @winrt_classmethod
    def CreateResponse(cls: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandResponseStatics, userMessage: win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandUserMessage) -> win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandResponse: ...
    @winrt_classmethod
    def CreateResponseWithTiles(cls: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandResponseStatics, message: win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandUserMessage, contentTiles: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandContentTile]) -> win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandResponse: ...
    @winrt_classmethod
    def CreateResponseForPrompt(cls: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandResponseStatics, message: win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandUserMessage, repeatMessage: win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandUserMessage) -> win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandResponse: ...
    @winrt_classmethod
    def CreateResponseForPromptWithTiles(cls: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandResponseStatics, message: win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandUserMessage, repeatMessage: win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandUserMessage, contentTiles: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandContentTile]) -> win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandResponse: ...
    AppLaunchArgument = property(get_AppLaunchArgument, put_AppLaunchArgument)
    Message = property(get_Message, put_Message)
    RepeatMessage = property(get_RepeatMessage, put_RepeatMessage)
    VoiceCommandContentTiles = property(get_VoiceCommandContentTiles, None)
    _VoiceCommandResponse_Meta_.MaxSupportedVoiceCommandContentTiles = property(get_MaxSupportedVoiceCommandContentTiles, None)
class VoiceCommandServiceConnection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandServiceConnection
    _classid_ = 'Windows.ApplicationModel.VoiceCommands.VoiceCommandServiceConnection'
    @winrt_mixinmethod
    def GetVoiceCommandAsync(self: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandServiceConnection) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommand]: ...
    @winrt_mixinmethod
    def RequestConfirmationAsync(self: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandServiceConnection, response: win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandResponse) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandConfirmationResult]: ...
    @winrt_mixinmethod
    def RequestDisambiguationAsync(self: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandServiceConnection, response: win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandResponse) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandDisambiguationResult]: ...
    @winrt_mixinmethod
    def ReportProgressAsync(self: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandServiceConnection, response: win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandResponse) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportSuccessAsync(self: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandServiceConnection, response: win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandResponse) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailureAsync(self: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandServiceConnection, response: win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandResponse) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def RequestAppLaunchAsync(self: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandServiceConnection, response: win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandResponse) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_Language(self: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandServiceConnection) -> win32more.Windows.Globalization.Language: ...
    @winrt_mixinmethod
    def add_VoiceCommandCompleted(self: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandServiceConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandServiceConnection, win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_VoiceCommandCompleted(self: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandServiceConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def FromAppServiceTriggerDetails(cls: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandServiceConnectionStatics, triggerDetails: win32more.Windows.ApplicationModel.AppService.AppServiceTriggerDetails) -> win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandServiceConnection: ...
    Language = property(get_Language, None)
    VoiceCommandCompleted = event()
class VoiceCommandUserMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandUserMessage
    _classid_ = 'Windows.ApplicationModel.VoiceCommands.VoiceCommandUserMessage'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandUserMessage.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.VoiceCommands.VoiceCommandUserMessage: ...
    @winrt_mixinmethod
    def get_DisplayMessage(self: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandUserMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayMessage(self: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandUserMessage, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_SpokenMessage(self: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandUserMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_SpokenMessage(self: win32more.Windows.ApplicationModel.VoiceCommands.IVoiceCommandUserMessage, value: WinRT_String) -> Void: ...
    DisplayMessage = property(get_DisplayMessage, put_DisplayMessage)
    SpokenMessage = property(get_SpokenMessage, put_SpokenMessage)


make_ready(__name__)
