from __future__ import annotations
from win32more._prelude import *
import win32more.Windows.Foundation
import win32more.Windows.UI.Shell.Tasks
class _AppTaskContent_Meta_(ComPtr.__class__):
    pass
class AppTaskContent(ComPtr, metaclass=_AppTaskContent_Meta_):
    extends: IInspectable
    default_interface: win32more.Windows.UI.Shell.Tasks.IAppTaskContent
    _classid_ = 'Windows.UI.Shell.Tasks.AppTaskContent'
    @winrt_mixinmethod
    def AddButton(self: win32more.Windows.UI.Shell.Tasks.IAppTaskContent, text: hstr, actionUri: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def SetTextInput(self: win32more.Windows.UI.Shell.Tasks.IAppTaskContent, placeholderText: hstr, actionUriTemplate: hstr) -> Void: ...
    @winrt_mixinmethod
    def SetQuestion(self: win32more.Windows.UI.Shell.Tasks.IAppTaskContent, question: hstr) -> Void: ...
    @winrt_classmethod
    def CreateSequenceOfSteps(cls: win32more.Windows.UI.Shell.Tasks.IAppTaskContentStatics, completedSteps: PassArray[hstr], executingStep: hstr) -> win32more.Windows.UI.Shell.Tasks.AppTaskContent: ...
    @winrt_classmethod
    def CreatePreviewThumbnail(cls: win32more.Windows.UI.Shell.Tasks.IAppTaskContentStatics, imageUri: win32more.Windows.Foundation.Uri, executingStep: hstr) -> win32more.Windows.UI.Shell.Tasks.AppTaskContent: ...
    @winrt_classmethod
    def CreateTextSummaryResult(cls: win32more.Windows.UI.Shell.Tasks.IAppTaskContentStatics, text: hstr) -> win32more.Windows.UI.Shell.Tasks.AppTaskContent: ...
    @winrt_classmethod
    def CreateGeneratedAssetsResult(cls: win32more.Windows.UI.Shell.Tasks.IAppTaskContentStatics, assets: PassArray[win32more.Windows.UI.Shell.Tasks.AppTaskResultAsset]) -> win32more.Windows.UI.Shell.Tasks.AppTaskContent: ...
    @winrt_classmethod
    def get_MaxButtons(cls: win32more.Windows.UI.Shell.Tasks.IAppTaskContentStatics) -> UInt32: ...
    _AppTaskContent_Meta_.MaxButtons = property(get_MaxButtons, None)
AppTaskContract: UInt32 = 131072
class AppTaskInfo(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.UI.Shell.Tasks.IAppTaskInfo
    _classid_ = 'Windows.UI.Shell.Tasks.AppTaskInfo'
    @winrt_mixinmethod
    def Remove(self: win32more.Windows.UI.Shell.Tasks.IAppTaskInfo) -> Void: ...
    @winrt_mixinmethod
    def Update(self: win32more.Windows.UI.Shell.Tasks.IAppTaskInfo, state: win32more.Windows.UI.Shell.Tasks.AppTaskState, content: win32more.Windows.UI.Shell.Tasks.AppTaskContent) -> Void: ...
    @winrt_mixinmethod
    def UpdateState(self: win32more.Windows.UI.Shell.Tasks.IAppTaskInfo, state: win32more.Windows.UI.Shell.Tasks.AppTaskState) -> Void: ...
    @winrt_mixinmethod
    def UpdateTitles(self: win32more.Windows.UI.Shell.Tasks.IAppTaskInfo, title: hstr, subtitle: hstr) -> Void: ...
    @winrt_mixinmethod
    def GetCompletedSteps(self: win32more.Windows.UI.Shell.Tasks.IAppTaskInfo) -> ReceiveArray[hstr]: ...
    @winrt_mixinmethod
    def GetExecutingStep(self: win32more.Windows.UI.Shell.Tasks.IAppTaskInfo) -> hstr: ...
    @winrt_mixinmethod
    def get_Title(self: win32more.Windows.UI.Shell.Tasks.IAppTaskInfo) -> hstr: ...
    @winrt_mixinmethod
    def get_Subtitle(self: win32more.Windows.UI.Shell.Tasks.IAppTaskInfo) -> hstr: ...
    @winrt_mixinmethod
    def get_DeepLink(self: win32more.Windows.UI.Shell.Tasks.IAppTaskInfo) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_IconUri(self: win32more.Windows.UI.Shell.Tasks.IAppTaskInfo) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.UI.Shell.Tasks.IAppTaskInfo) -> win32more.Windows.UI.Shell.Tasks.AppTaskState: ...
    @winrt_mixinmethod
    def get_StartTime(self: win32more.Windows.UI.Shell.Tasks.IAppTaskInfo) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_EndTime(self: win32more.Windows.UI.Shell.Tasks.IAppTaskInfo) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.UI.Shell.Tasks.IAppTaskInfo2) -> hstr: ...
    @winrt_mixinmethod
    def get_HiddenByUser(self: win32more.Windows.UI.Shell.Tasks.IAppTaskInfo2) -> Boolean: ...
    @winrt_mixinmethod
    def UpdateDeepLink(self: win32more.Windows.UI.Shell.Tasks.IAppTaskInfo2, deepLink: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_classmethod
    def IsSupported(cls: win32more.Windows.UI.Shell.Tasks.IAppTaskInfoStatics) -> Boolean: ...
    @winrt_classmethod
    def FindAll(cls: win32more.Windows.UI.Shell.Tasks.IAppTaskInfoStatics) -> ReceiveArray[win32more.Windows.UI.Shell.Tasks.AppTaskInfo]: ...
    @winrt_classmethod
    def Create(cls: win32more.Windows.UI.Shell.Tasks.IAppTaskInfoStatics, title: hstr, subtitle: hstr, deepLink: win32more.Windows.Foundation.Uri, iconUri: win32more.Windows.Foundation.Uri, content: win32more.Windows.UI.Shell.Tasks.AppTaskContent) -> win32more.Windows.UI.Shell.Tasks.AppTaskInfo: ...
    DeepLink = property(get_DeepLink, None)
    EndTime = property(get_EndTime, None)
    HiddenByUser = property(get_HiddenByUser, None)
    IconUri = property(get_IconUri, None)
    Id = property(get_Id, None)
    StartTime = property(get_StartTime, None)
    State = property(get_State, None)
    Subtitle = property(get_Subtitle, None)
    Title = property(get_Title, None)
class AppTaskResultAsset(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.UI.Shell.Tasks.IAppTaskResultAsset
    _classid_ = 'Windows.UI.Shell.Tasks.AppTaskResultAsset'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 4:
            super().__init__(move=win32more.Windows.UI.Shell.Tasks.AppTaskResultAsset.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Shell.Tasks.IAppTaskResultAssetFactory, name: hstr, context: hstr, iconUri: win32more.Windows.Foundation.Uri, assetUri: win32more.Windows.Foundation.Uri) -> win32more.Windows.UI.Shell.Tasks.AppTaskResultAsset: ...
class AppTaskState(Enum, Int32):
    _name_ = 'Windows.UI.Shell.Tasks.AppTaskState'
    Running = 0
    Completed = 1
    NeedsAttention = 2
    Paused = 3
    Error = 4
class IAppTaskContent(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.Shell.Tasks.IAppTaskContent'
    _iid_ = Guid('{2411bf59-1b2d-5b63-8181-03d6c2248a68}')
    @winrt_commethod(6)
    def AddButton(self, text: hstr, actionUri: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(7)
    def SetTextInput(self, placeholderText: hstr, actionUriTemplate: hstr) -> Void: ...
    @winrt_commethod(8)
    def SetQuestion(self, question: hstr) -> Void: ...
class IAppTaskContentStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.Shell.Tasks.IAppTaskContentStatics'
    _iid_ = Guid('{aabd19f6-7afc-5b1b-94f6-5dc9dc9af9e7}')
    @winrt_commethod(6)
    def CreateSequenceOfSteps(self, completedSteps: PassArray[hstr], executingStep: hstr) -> win32more.Windows.UI.Shell.Tasks.AppTaskContent: ...
    @winrt_commethod(7)
    def CreatePreviewThumbnail(self, imageUri: win32more.Windows.Foundation.Uri, executingStep: hstr) -> win32more.Windows.UI.Shell.Tasks.AppTaskContent: ...
    @winrt_commethod(8)
    def CreateTextSummaryResult(self, text: hstr) -> win32more.Windows.UI.Shell.Tasks.AppTaskContent: ...
    @winrt_commethod(9)
    def CreateGeneratedAssetsResult(self, assets: PassArray[win32more.Windows.UI.Shell.Tasks.AppTaskResultAsset]) -> win32more.Windows.UI.Shell.Tasks.AppTaskContent: ...
    @winrt_commethod(10)
    def get_MaxButtons(self) -> UInt32: ...
    MaxButtons = property(get_MaxButtons, None)
class IAppTaskInfo(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.Shell.Tasks.IAppTaskInfo'
    _iid_ = Guid('{6720eed6-435b-5db9-be66-9343b70654f7}')
    @winrt_commethod(6)
    def Remove(self) -> Void: ...
    @winrt_commethod(7)
    def Update(self, state: win32more.Windows.UI.Shell.Tasks.AppTaskState, content: win32more.Windows.UI.Shell.Tasks.AppTaskContent) -> Void: ...
    @winrt_commethod(8)
    def UpdateState(self, state: win32more.Windows.UI.Shell.Tasks.AppTaskState) -> Void: ...
    @winrt_commethod(9)
    def UpdateTitles(self, title: hstr, subtitle: hstr) -> Void: ...
    @winrt_commethod(10)
    def GetCompletedSteps(self) -> ReceiveArray[hstr]: ...
    @winrt_commethod(11)
    def GetExecutingStep(self) -> hstr: ...
    @winrt_commethod(12)
    def get_Title(self) -> hstr: ...
    @winrt_commethod(13)
    def get_Subtitle(self) -> hstr: ...
    @winrt_commethod(14)
    def get_DeepLink(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(15)
    def get_IconUri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(16)
    def get_State(self) -> win32more.Windows.UI.Shell.Tasks.AppTaskState: ...
    @winrt_commethod(17)
    def get_StartTime(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(18)
    def get_EndTime(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    DeepLink = property(get_DeepLink, None)
    EndTime = property(get_EndTime, None)
    IconUri = property(get_IconUri, None)
    StartTime = property(get_StartTime, None)
    State = property(get_State, None)
    Subtitle = property(get_Subtitle, None)
    Title = property(get_Title, None)
class IAppTaskInfo2(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.Shell.Tasks.IAppTaskInfo2'
    _iid_ = Guid('{ad724d71-f137-51c0-8111-3552436bf447}')
    @winrt_commethod(6)
    def get_Id(self) -> hstr: ...
    @winrt_commethod(7)
    def get_HiddenByUser(self) -> Boolean: ...
    @winrt_commethod(8)
    def UpdateDeepLink(self, deepLink: win32more.Windows.Foundation.Uri) -> Void: ...
    HiddenByUser = property(get_HiddenByUser, None)
    Id = property(get_Id, None)
class IAppTaskInfoStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.Shell.Tasks.IAppTaskInfoStatics'
    _iid_ = Guid('{a0b0434f-c640-5800-88c9-d7691ac2f48f}')
    @winrt_commethod(6)
    def IsSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def FindAll(self) -> ReceiveArray[win32more.Windows.UI.Shell.Tasks.AppTaskInfo]: ...
    @winrt_commethod(8)
    def Create(self, title: hstr, subtitle: hstr, deepLink: win32more.Windows.Foundation.Uri, iconUri: win32more.Windows.Foundation.Uri, content: win32more.Windows.UI.Shell.Tasks.AppTaskContent) -> win32more.Windows.UI.Shell.Tasks.AppTaskInfo: ...
class IAppTaskResultAsset(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.Shell.Tasks.IAppTaskResultAsset'
    _iid_ = Guid('{75d0c2b3-8a31-5f8f-bda4-bdca96e95532}')
class IAppTaskResultAssetFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.Shell.Tasks.IAppTaskResultAssetFactory'
    _iid_ = Guid('{0334d9df-0e06-5999-ba41-85d72e980085}')
    @winrt_commethod(6)
    def CreateInstance(self, name: hstr, context: hstr, iconUri: win32more.Windows.Foundation.Uri, assetUri: win32more.Windows.Foundation.Uri) -> win32more.Windows.UI.Shell.Tasks.AppTaskResultAsset: ...


make_ready(__name__)
