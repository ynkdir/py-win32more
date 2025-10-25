from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Windows.ApplicationModel.UserActivities
import win32more.Windows.ApplicationModel.UserActivities.Core
import win32more.Windows.Foundation
class CoreUserActivityManager(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.Core.CoreUserActivityManager'
    @winrt_classmethod
    def CreateUserActivitySessionInBackground(cls: win32more.Windows.ApplicationModel.UserActivities.Core.ICoreUserActivityManagerStatics, activity: win32more.Windows.ApplicationModel.UserActivities.UserActivity) -> win32more.Windows.ApplicationModel.UserActivities.UserActivitySession: ...
    @winrt_classmethod
    def DeleteUserActivitySessionsInTimeRangeAsync(cls: win32more.Windows.ApplicationModel.UserActivities.Core.ICoreUserActivityManagerStatics, channel: win32more.Windows.ApplicationModel.UserActivities.UserActivityChannel, startTime: win32more.Windows.Foundation.DateTime, endTime: win32more.Windows.Foundation.DateTime) -> win32more.Windows.Foundation.IAsyncAction: ...
class ICoreUserActivityManagerStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.Core.ICoreUserActivityManagerStatics'
    _iid_ = Guid('{ca3adb02-a4be-4d4d-bfa8-6795f4264efb}')
    @winrt_commethod(6)
    def CreateUserActivitySessionInBackground(self, activity: win32more.Windows.ApplicationModel.UserActivities.UserActivity) -> win32more.Windows.ApplicationModel.UserActivities.UserActivitySession: ...
    @winrt_commethod(7)
    def DeleteUserActivitySessionsInTimeRangeAsync(self, channel: win32more.Windows.ApplicationModel.UserActivities.UserActivityChannel, startTime: win32more.Windows.Foundation.DateTime, endTime: win32more.Windows.Foundation.DateTime) -> win32more.Windows.Foundation.IAsyncAction: ...


make_ready(__name__)
