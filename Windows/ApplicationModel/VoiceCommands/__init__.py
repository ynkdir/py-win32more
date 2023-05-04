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
import Windows.ApplicationModel.AppService
import Windows.ApplicationModel.VoiceCommands
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Globalization
import Windows.Media.SpeechRecognition
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
class IVoiceCommand(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{936f5273-ec82-42a6-a55c-d2d79ec6f920}')
    @winrt_commethod(6)
    def get_CommandName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Properties(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Foundation.Collections.IVectorView[WinRT_String]]: ...
    @winrt_commethod(8)
    def get_SpeechRecognitionResult(self) -> Windows.Media.SpeechRecognition.SpeechRecognitionResult: ...
    CommandName = property(get_CommandName, None)
    Properties = property(get_Properties, None)
    SpeechRecognitionResult = property(get_SpeechRecognitionResult, None)
class IVoiceCommandCompletedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{c85e675d-fe42-432c-9907-09df9fcf64e8}')
    @winrt_commethod(6)
    def get_Reason(self) -> Windows.ApplicationModel.VoiceCommands.VoiceCommandCompletionReason: ...
    Reason = property(get_Reason, None)
class IVoiceCommandConfirmationResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{a022593e-8221-4526-b083-840972262247}')
    @winrt_commethod(6)
    def get_Confirmed(self) -> Boolean: ...
    Confirmed = property(get_Confirmed, None)
class IVoiceCommandContentTile(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    def get_Image(self) -> Windows.Storage.IStorageFile: ...
    @winrt_commethod(15)
    def put_Image(self, value: Windows.Storage.IStorageFile) -> Void: ...
    @winrt_commethod(16)
    def get_AppContext(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(17)
    def put_AppContext(self, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(18)
    def get_AppLaunchArgument(self) -> WinRT_String: ...
    @winrt_commethod(19)
    def put_AppLaunchArgument(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(20)
    def get_ContentTileType(self) -> Windows.ApplicationModel.VoiceCommands.VoiceCommandContentTileType: ...
    @winrt_commethod(21)
    def put_ContentTileType(self, value: Windows.ApplicationModel.VoiceCommands.VoiceCommandContentTileType) -> Void: ...
    Title = property(get_Title, put_Title)
    TextLine1 = property(get_TextLine1, put_TextLine1)
    TextLine2 = property(get_TextLine2, put_TextLine2)
    TextLine3 = property(get_TextLine3, put_TextLine3)
    Image = property(get_Image, put_Image)
    AppContext = property(get_AppContext, put_AppContext)
    AppLaunchArgument = property(get_AppLaunchArgument, put_AppLaunchArgument)
    ContentTileType = property(get_ContentTileType, put_ContentTileType)
class IVoiceCommandDefinition(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{7972aad0-0974-4979-984b-cb8959cd61ae}')
    @winrt_commethod(6)
    def get_Language(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def SetPhraseListAsync(self, phraseListName: WinRT_String, phraseList: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncAction: ...
    Language = property(get_Language, None)
    Name = property(get_Name, None)
class IVoiceCommandDefinitionManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{8fe7a69e-067e-4f16-a18c-5b17e9499940}')
    @winrt_commethod(6)
    def InstallCommandDefinitionsFromStorageFileAsync(self, file: Windows.Storage.StorageFile) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def get_InstalledCommandDefinitions(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.ApplicationModel.VoiceCommands.VoiceCommandDefinition]: ...
    InstalledCommandDefinitions = property(get_InstalledCommandDefinitions, None)
class IVoiceCommandDisambiguationResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{ecc68cfe-c9ac-45df-a8ea-feea08ef9c5e}')
    @winrt_commethod(6)
    def get_SelectedItem(self) -> Windows.ApplicationModel.VoiceCommands.VoiceCommandContentTile: ...
    SelectedItem = property(get_SelectedItem, None)
class IVoiceCommandResponse(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{0284b30e-8a3b-4cc4-a6a1-cad5be2716b5}')
    @winrt_commethod(6)
    def get_Message(self) -> Windows.ApplicationModel.VoiceCommands.VoiceCommandUserMessage: ...
    @winrt_commethod(7)
    def put_Message(self, value: Windows.ApplicationModel.VoiceCommands.VoiceCommandUserMessage) -> Void: ...
    @winrt_commethod(8)
    def get_RepeatMessage(self) -> Windows.ApplicationModel.VoiceCommands.VoiceCommandUserMessage: ...
    @winrt_commethod(9)
    def put_RepeatMessage(self, value: Windows.ApplicationModel.VoiceCommands.VoiceCommandUserMessage) -> Void: ...
    @winrt_commethod(10)
    def get_AppLaunchArgument(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_AppLaunchArgument(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_VoiceCommandContentTiles(self) -> Windows.Foundation.Collections.IVector[Windows.ApplicationModel.VoiceCommands.VoiceCommandContentTile]: ...
    Message = property(get_Message, put_Message)
    RepeatMessage = property(get_RepeatMessage, put_RepeatMessage)
    AppLaunchArgument = property(get_AppLaunchArgument, put_AppLaunchArgument)
    VoiceCommandContentTiles = property(get_VoiceCommandContentTiles, None)
class IVoiceCommandResponseStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{2932f813-0d3b-49f2-96dd-625019bd3b5d}')
    @winrt_commethod(6)
    def get_MaxSupportedVoiceCommandContentTiles(self) -> UInt32: ...
    @winrt_commethod(7)
    def CreateResponse(self, userMessage: Windows.ApplicationModel.VoiceCommands.VoiceCommandUserMessage) -> Windows.ApplicationModel.VoiceCommands.VoiceCommandResponse: ...
    @winrt_commethod(8)
    def CreateResponseWithTiles(self, message: Windows.ApplicationModel.VoiceCommands.VoiceCommandUserMessage, contentTiles: Windows.Foundation.Collections.IIterable[Windows.ApplicationModel.VoiceCommands.VoiceCommandContentTile]) -> Windows.ApplicationModel.VoiceCommands.VoiceCommandResponse: ...
    @winrt_commethod(9)
    def CreateResponseForPrompt(self, message: Windows.ApplicationModel.VoiceCommands.VoiceCommandUserMessage, repeatMessage: Windows.ApplicationModel.VoiceCommands.VoiceCommandUserMessage) -> Windows.ApplicationModel.VoiceCommands.VoiceCommandResponse: ...
    @winrt_commethod(10)
    def CreateResponseForPromptWithTiles(self, message: Windows.ApplicationModel.VoiceCommands.VoiceCommandUserMessage, repeatMessage: Windows.ApplicationModel.VoiceCommands.VoiceCommandUserMessage, contentTiles: Windows.Foundation.Collections.IIterable[Windows.ApplicationModel.VoiceCommands.VoiceCommandContentTile]) -> Windows.ApplicationModel.VoiceCommands.VoiceCommandResponse: ...
    MaxSupportedVoiceCommandContentTiles = property(get_MaxSupportedVoiceCommandContentTiles, None)
class IVoiceCommandServiceConnection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{d894bb9f-21da-44a4-98a2-fb131920a9cc}')
    @winrt_commethod(6)
    def GetVoiceCommandAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.VoiceCommands.VoiceCommand]: ...
    @winrt_commethod(7)
    def RequestConfirmationAsync(self, response: Windows.ApplicationModel.VoiceCommands.VoiceCommandResponse) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.VoiceCommands.VoiceCommandConfirmationResult]: ...
    @winrt_commethod(8)
    def RequestDisambiguationAsync(self, response: Windows.ApplicationModel.VoiceCommands.VoiceCommandResponse) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.VoiceCommands.VoiceCommandDisambiguationResult]: ...
    @winrt_commethod(9)
    def ReportProgressAsync(self, response: Windows.ApplicationModel.VoiceCommands.VoiceCommandResponse) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def ReportSuccessAsync(self, response: Windows.ApplicationModel.VoiceCommands.VoiceCommandResponse) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(11)
    def ReportFailureAsync(self, response: Windows.ApplicationModel.VoiceCommands.VoiceCommandResponse) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(12)
    def RequestAppLaunchAsync(self, response: Windows.ApplicationModel.VoiceCommands.VoiceCommandResponse) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(13)
    def get_Language(self) -> Windows.Globalization.Language: ...
    @winrt_commethod(14)
    def add_VoiceCommandCompleted(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.VoiceCommands.VoiceCommandServiceConnection, Windows.ApplicationModel.VoiceCommands.VoiceCommandCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_VoiceCommandCompleted(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Language = property(get_Language, None)
class IVoiceCommandServiceConnectionStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{370ebffb-2d34-42df-8770-074d0f334697}')
    @winrt_commethod(6)
    def FromAppServiceTriggerDetails(self, triggerDetails: Windows.ApplicationModel.AppService.AppServiceTriggerDetails) -> Windows.ApplicationModel.VoiceCommands.VoiceCommandServiceConnection: ...
class IVoiceCommandUserMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.VoiceCommands.VoiceCommand'
    @winrt_mixinmethod
    def get_CommandName(self: Windows.ApplicationModel.VoiceCommands.IVoiceCommand) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.ApplicationModel.VoiceCommands.IVoiceCommand) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Foundation.Collections.IVectorView[WinRT_String]]: ...
    @winrt_mixinmethod
    def get_SpeechRecognitionResult(self: Windows.ApplicationModel.VoiceCommands.IVoiceCommand) -> Windows.Media.SpeechRecognition.SpeechRecognitionResult: ...
    CommandName = property(get_CommandName, None)
    Properties = property(get_Properties, None)
    SpeechRecognitionResult = property(get_SpeechRecognitionResult, None)
class VoiceCommandCompletedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.VoiceCommands.VoiceCommandCompletedEventArgs'
    @winrt_mixinmethod
    def get_Reason(self: Windows.ApplicationModel.VoiceCommands.IVoiceCommandCompletedEventArgs) -> Windows.ApplicationModel.VoiceCommands.VoiceCommandCompletionReason: ...
    Reason = property(get_Reason, None)
VoiceCommandCompletionReason = Int32
VoiceCommandCompletionReason_Unknown: VoiceCommandCompletionReason = 0
VoiceCommandCompletionReason_CommunicationFailed: VoiceCommandCompletionReason = 1
VoiceCommandCompletionReason_ResourceLimitsExceeded: VoiceCommandCompletionReason = 2
VoiceCommandCompletionReason_Canceled: VoiceCommandCompletionReason = 3
VoiceCommandCompletionReason_TimeoutExceeded: VoiceCommandCompletionReason = 4
VoiceCommandCompletionReason_AppLaunched: VoiceCommandCompletionReason = 5
VoiceCommandCompletionReason_Completed: VoiceCommandCompletionReason = 6
class VoiceCommandConfirmationResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.VoiceCommands.VoiceCommandConfirmationResult'
    @winrt_mixinmethod
    def get_Confirmed(self: Windows.ApplicationModel.VoiceCommands.IVoiceCommandConfirmationResult) -> Boolean: ...
    Confirmed = property(get_Confirmed, None)
class VoiceCommandContentTile(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.VoiceCommands.VoiceCommandContentTile'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.VoiceCommands.VoiceCommandContentTile: ...
    @winrt_mixinmethod
    def get_Title(self: Windows.ApplicationModel.VoiceCommands.IVoiceCommandContentTile) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Title(self: Windows.ApplicationModel.VoiceCommands.IVoiceCommandContentTile, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_TextLine1(self: Windows.ApplicationModel.VoiceCommands.IVoiceCommandContentTile) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TextLine1(self: Windows.ApplicationModel.VoiceCommands.IVoiceCommandContentTile, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_TextLine2(self: Windows.ApplicationModel.VoiceCommands.IVoiceCommandContentTile) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TextLine2(self: Windows.ApplicationModel.VoiceCommands.IVoiceCommandContentTile, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_TextLine3(self: Windows.ApplicationModel.VoiceCommands.IVoiceCommandContentTile) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TextLine3(self: Windows.ApplicationModel.VoiceCommands.IVoiceCommandContentTile, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Image(self: Windows.ApplicationModel.VoiceCommands.IVoiceCommandContentTile) -> Windows.Storage.IStorageFile: ...
    @winrt_mixinmethod
    def put_Image(self: Windows.ApplicationModel.VoiceCommands.IVoiceCommandContentTile, value: Windows.Storage.IStorageFile) -> Void: ...
    @winrt_mixinmethod
    def get_AppContext(self: Windows.ApplicationModel.VoiceCommands.IVoiceCommandContentTile) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def put_AppContext(self: Windows.ApplicationModel.VoiceCommands.IVoiceCommandContentTile, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_mixinmethod
    def get_AppLaunchArgument(self: Windows.ApplicationModel.VoiceCommands.IVoiceCommandContentTile) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_AppLaunchArgument(self: Windows.ApplicationModel.VoiceCommands.IVoiceCommandContentTile, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ContentTileType(self: Windows.ApplicationModel.VoiceCommands.IVoiceCommandContentTile) -> Windows.ApplicationModel.VoiceCommands.VoiceCommandContentTileType: ...
    @winrt_mixinmethod
    def put_ContentTileType(self: Windows.ApplicationModel.VoiceCommands.IVoiceCommandContentTile, value: Windows.ApplicationModel.VoiceCommands.VoiceCommandContentTileType) -> Void: ...
    Title = property(get_Title, put_Title)
    TextLine1 = property(get_TextLine1, put_TextLine1)
    TextLine2 = property(get_TextLine2, put_TextLine2)
    TextLine3 = property(get_TextLine3, put_TextLine3)
    Image = property(get_Image, put_Image)
    AppContext = property(get_AppContext, put_AppContext)
    AppLaunchArgument = property(get_AppLaunchArgument, put_AppLaunchArgument)
    ContentTileType = property(get_ContentTileType, put_ContentTileType)
VoiceCommandContentTileType = Int32
VoiceCommandContentTileType_TitleOnly: VoiceCommandContentTileType = 0
VoiceCommandContentTileType_TitleWithText: VoiceCommandContentTileType = 1
VoiceCommandContentTileType_TitleWith68x68Icon: VoiceCommandContentTileType = 2
VoiceCommandContentTileType_TitleWith68x68IconAndText: VoiceCommandContentTileType = 3
VoiceCommandContentTileType_TitleWith68x92Icon: VoiceCommandContentTileType = 4
VoiceCommandContentTileType_TitleWith68x92IconAndText: VoiceCommandContentTileType = 5
VoiceCommandContentTileType_TitleWith280x140Icon: VoiceCommandContentTileType = 6
VoiceCommandContentTileType_TitleWith280x140IconAndText: VoiceCommandContentTileType = 7
class VoiceCommandDefinition(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.VoiceCommands.VoiceCommandDefinition'
    @winrt_mixinmethod
    def get_Language(self: Windows.ApplicationModel.VoiceCommands.IVoiceCommandDefinition) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.ApplicationModel.VoiceCommands.IVoiceCommandDefinition) -> WinRT_String: ...
    @winrt_mixinmethod
    def SetPhraseListAsync(self: Windows.ApplicationModel.VoiceCommands.IVoiceCommandDefinition, phraseListName: WinRT_String, phraseList: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncAction: ...
    Language = property(get_Language, None)
    Name = property(get_Name, None)
class VoiceCommandDefinitionManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.VoiceCommands.VoiceCommandDefinitionManager'
    @winrt_classmethod
    def InstallCommandDefinitionsFromStorageFileAsync(cls: Windows.ApplicationModel.VoiceCommands.IVoiceCommandDefinitionManagerStatics, file: Windows.Storage.StorageFile) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def get_InstalledCommandDefinitions(cls: Windows.ApplicationModel.VoiceCommands.IVoiceCommandDefinitionManagerStatics) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.ApplicationModel.VoiceCommands.VoiceCommandDefinition]: ...
    InstalledCommandDefinitions = property(get_InstalledCommandDefinitions, None)
class VoiceCommandDisambiguationResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.VoiceCommands.VoiceCommandDisambiguationResult'
    @winrt_mixinmethod
    def get_SelectedItem(self: Windows.ApplicationModel.VoiceCommands.IVoiceCommandDisambiguationResult) -> Windows.ApplicationModel.VoiceCommands.VoiceCommandContentTile: ...
    SelectedItem = property(get_SelectedItem, None)
class VoiceCommandResponse(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.VoiceCommands.VoiceCommandResponse'
    @winrt_mixinmethod
    def get_Message(self: Windows.ApplicationModel.VoiceCommands.IVoiceCommandResponse) -> Windows.ApplicationModel.VoiceCommands.VoiceCommandUserMessage: ...
    @winrt_mixinmethod
    def put_Message(self: Windows.ApplicationModel.VoiceCommands.IVoiceCommandResponse, value: Windows.ApplicationModel.VoiceCommands.VoiceCommandUserMessage) -> Void: ...
    @winrt_mixinmethod
    def get_RepeatMessage(self: Windows.ApplicationModel.VoiceCommands.IVoiceCommandResponse) -> Windows.ApplicationModel.VoiceCommands.VoiceCommandUserMessage: ...
    @winrt_mixinmethod
    def put_RepeatMessage(self: Windows.ApplicationModel.VoiceCommands.IVoiceCommandResponse, value: Windows.ApplicationModel.VoiceCommands.VoiceCommandUserMessage) -> Void: ...
    @winrt_mixinmethod
    def get_AppLaunchArgument(self: Windows.ApplicationModel.VoiceCommands.IVoiceCommandResponse) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_AppLaunchArgument(self: Windows.ApplicationModel.VoiceCommands.IVoiceCommandResponse, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_VoiceCommandContentTiles(self: Windows.ApplicationModel.VoiceCommands.IVoiceCommandResponse) -> Windows.Foundation.Collections.IVector[Windows.ApplicationModel.VoiceCommands.VoiceCommandContentTile]: ...
    @winrt_classmethod
    def get_MaxSupportedVoiceCommandContentTiles(cls: Windows.ApplicationModel.VoiceCommands.IVoiceCommandResponseStatics) -> UInt32: ...
    @winrt_classmethod
    def CreateResponse(cls: Windows.ApplicationModel.VoiceCommands.IVoiceCommandResponseStatics, userMessage: Windows.ApplicationModel.VoiceCommands.VoiceCommandUserMessage) -> Windows.ApplicationModel.VoiceCommands.VoiceCommandResponse: ...
    @winrt_classmethod
    def CreateResponseWithTiles(cls: Windows.ApplicationModel.VoiceCommands.IVoiceCommandResponseStatics, message: Windows.ApplicationModel.VoiceCommands.VoiceCommandUserMessage, contentTiles: Windows.Foundation.Collections.IIterable[Windows.ApplicationModel.VoiceCommands.VoiceCommandContentTile]) -> Windows.ApplicationModel.VoiceCommands.VoiceCommandResponse: ...
    @winrt_classmethod
    def CreateResponseForPrompt(cls: Windows.ApplicationModel.VoiceCommands.IVoiceCommandResponseStatics, message: Windows.ApplicationModel.VoiceCommands.VoiceCommandUserMessage, repeatMessage: Windows.ApplicationModel.VoiceCommands.VoiceCommandUserMessage) -> Windows.ApplicationModel.VoiceCommands.VoiceCommandResponse: ...
    @winrt_classmethod
    def CreateResponseForPromptWithTiles(cls: Windows.ApplicationModel.VoiceCommands.IVoiceCommandResponseStatics, message: Windows.ApplicationModel.VoiceCommands.VoiceCommandUserMessage, repeatMessage: Windows.ApplicationModel.VoiceCommands.VoiceCommandUserMessage, contentTiles: Windows.Foundation.Collections.IIterable[Windows.ApplicationModel.VoiceCommands.VoiceCommandContentTile]) -> Windows.ApplicationModel.VoiceCommands.VoiceCommandResponse: ...
    Message = property(get_Message, put_Message)
    RepeatMessage = property(get_RepeatMessage, put_RepeatMessage)
    AppLaunchArgument = property(get_AppLaunchArgument, put_AppLaunchArgument)
    VoiceCommandContentTiles = property(get_VoiceCommandContentTiles, None)
    MaxSupportedVoiceCommandContentTiles = property(get_MaxSupportedVoiceCommandContentTiles, None)
class VoiceCommandServiceConnection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.VoiceCommands.VoiceCommandServiceConnection'
    @winrt_mixinmethod
    def GetVoiceCommandAsync(self: Windows.ApplicationModel.VoiceCommands.IVoiceCommandServiceConnection) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.VoiceCommands.VoiceCommand]: ...
    @winrt_mixinmethod
    def RequestConfirmationAsync(self: Windows.ApplicationModel.VoiceCommands.IVoiceCommandServiceConnection, response: Windows.ApplicationModel.VoiceCommands.VoiceCommandResponse) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.VoiceCommands.VoiceCommandConfirmationResult]: ...
    @winrt_mixinmethod
    def RequestDisambiguationAsync(self: Windows.ApplicationModel.VoiceCommands.IVoiceCommandServiceConnection, response: Windows.ApplicationModel.VoiceCommands.VoiceCommandResponse) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.VoiceCommands.VoiceCommandDisambiguationResult]: ...
    @winrt_mixinmethod
    def ReportProgressAsync(self: Windows.ApplicationModel.VoiceCommands.IVoiceCommandServiceConnection, response: Windows.ApplicationModel.VoiceCommands.VoiceCommandResponse) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportSuccessAsync(self: Windows.ApplicationModel.VoiceCommands.IVoiceCommandServiceConnection, response: Windows.ApplicationModel.VoiceCommands.VoiceCommandResponse) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailureAsync(self: Windows.ApplicationModel.VoiceCommands.IVoiceCommandServiceConnection, response: Windows.ApplicationModel.VoiceCommands.VoiceCommandResponse) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def RequestAppLaunchAsync(self: Windows.ApplicationModel.VoiceCommands.IVoiceCommandServiceConnection, response: Windows.ApplicationModel.VoiceCommands.VoiceCommandResponse) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_Language(self: Windows.ApplicationModel.VoiceCommands.IVoiceCommandServiceConnection) -> Windows.Globalization.Language: ...
    @winrt_mixinmethod
    def add_VoiceCommandCompleted(self: Windows.ApplicationModel.VoiceCommands.IVoiceCommandServiceConnection, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.VoiceCommands.VoiceCommandServiceConnection, Windows.ApplicationModel.VoiceCommands.VoiceCommandCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_VoiceCommandCompleted(self: Windows.ApplicationModel.VoiceCommands.IVoiceCommandServiceConnection, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def FromAppServiceTriggerDetails(cls: Windows.ApplicationModel.VoiceCommands.IVoiceCommandServiceConnectionStatics, triggerDetails: Windows.ApplicationModel.AppService.AppServiceTriggerDetails) -> Windows.ApplicationModel.VoiceCommands.VoiceCommandServiceConnection: ...
    Language = property(get_Language, None)
class VoiceCommandUserMessage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.VoiceCommands.VoiceCommandUserMessage'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.VoiceCommands.VoiceCommandUserMessage: ...
    @winrt_mixinmethod
    def get_DisplayMessage(self: Windows.ApplicationModel.VoiceCommands.IVoiceCommandUserMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayMessage(self: Windows.ApplicationModel.VoiceCommands.IVoiceCommandUserMessage, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_SpokenMessage(self: Windows.ApplicationModel.VoiceCommands.IVoiceCommandUserMessage) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_SpokenMessage(self: Windows.ApplicationModel.VoiceCommands.IVoiceCommandUserMessage, value: WinRT_String) -> Void: ...
    DisplayMessage = property(get_DisplayMessage, put_DisplayMessage)
    SpokenMessage = property(get_SpokenMessage, put_SpokenMessage)
make_head(_module, 'IVoiceCommand')
make_head(_module, 'IVoiceCommandCompletedEventArgs')
make_head(_module, 'IVoiceCommandConfirmationResult')
make_head(_module, 'IVoiceCommandContentTile')
make_head(_module, 'IVoiceCommandDefinition')
make_head(_module, 'IVoiceCommandDefinitionManagerStatics')
make_head(_module, 'IVoiceCommandDisambiguationResult')
make_head(_module, 'IVoiceCommandResponse')
make_head(_module, 'IVoiceCommandResponseStatics')
make_head(_module, 'IVoiceCommandServiceConnection')
make_head(_module, 'IVoiceCommandServiceConnectionStatics')
make_head(_module, 'IVoiceCommandUserMessage')
make_head(_module, 'VoiceCommand')
make_head(_module, 'VoiceCommandCompletedEventArgs')
make_head(_module, 'VoiceCommandConfirmationResult')
make_head(_module, 'VoiceCommandContentTile')
make_head(_module, 'VoiceCommandDefinition')
make_head(_module, 'VoiceCommandDefinitionManager')
make_head(_module, 'VoiceCommandDisambiguationResult')
make_head(_module, 'VoiceCommandResponse')
make_head(_module, 'VoiceCommandServiceConnection')
make_head(_module, 'VoiceCommandUserMessage')
