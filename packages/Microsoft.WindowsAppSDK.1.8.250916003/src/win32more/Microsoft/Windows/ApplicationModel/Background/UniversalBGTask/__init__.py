from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Microsoft.Windows.ApplicationModel.Background.UniversalBGTask
import win32more.Windows.ApplicationModel.Background
class ITask(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.ApplicationModel.Background.UniversalBGTask.ITask'
    _iid_ = Guid('{89cf5f73-8195-590b-8158-bc7d2816ce16}')
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
    def Run(self: win32more.Windows.ApplicationModel.Background.IBackgroundTask, taskInstance: win32more.Windows.ApplicationModel.Background.IBackgroundTaskInstance) -> Void: ...
UniversalBackgroundTaskContract: UInt32 = 65536


make_ready(__name__)
