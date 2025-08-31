from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Microsoft.Windows.ApplicationModel.Background.UniversalBGTask
import win32more.Windows.ApplicationModel.Background
class ITask(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.ApplicationModel.Background.UniversalBGTask.ITask'
    _iid_ = Guid('{d47c97e5-a23f-5b32-8a2e-b93c8cae4299}')
    @winrt_commethod(6)
    def Run(self, taskInstance: win32more.Windows.ApplicationModel.Background.IBackgroundTaskInstance) -> Void: ...
class Task(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.ApplicationModel.Background.UniversalBGTask.ITask
    _classid_ = 'Microsoft.Windows.ApplicationModel.Background.UniversalBGTask.Task'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.Windows.ApplicationModel.Background.UniversalBGTask.Task.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.Windows.ApplicationModel.Background.UniversalBGTask.Task: ...
    @winrt_mixinmethod
    def Run(self: win32more.Microsoft.Windows.ApplicationModel.Background.UniversalBGTask.ITask, taskInstance: win32more.Windows.ApplicationModel.Background.IBackgroundTaskInstance) -> Void: ...
UniversalBackgroundTaskContract: UInt32 = 65536


make_ready(__name__)
