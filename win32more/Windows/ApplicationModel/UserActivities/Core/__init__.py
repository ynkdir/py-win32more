from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel.UserActivities
import win32more.Windows.ApplicationModel.UserActivities.Core
import win32more.Windows.Foundation
import win32more.Windows.Win32.System.WinRT
class CoreUserActivityManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.Core.CoreUserActivityManager'
    @winrt_classmethod
    def CreateUserActivitySessionInBackground(cls: win32more.Windows.ApplicationModel.UserActivities.Core.ICoreUserActivityManagerStatics, activity: win32more.Windows.ApplicationModel.UserActivities.UserActivity) -> win32more.Windows.ApplicationModel.UserActivities.UserActivitySession: ...
    @winrt_classmethod
    def DeleteUserActivitySessionsInTimeRangeAsync(cls: win32more.Windows.ApplicationModel.UserActivities.Core.ICoreUserActivityManagerStatics, channel: win32more.Windows.ApplicationModel.UserActivities.UserActivityChannel, startTime: win32more.Windows.Foundation.DateTime, endTime: win32more.Windows.Foundation.DateTime) -> win32more.Windows.Foundation.IAsyncAction: ...
class ICoreUserActivityManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.Core.ICoreUserActivityManagerStatics'
    _iid_ = Guid('{ca3adb02-a4be-4d4d-bfa8-6795f4264efb}')
    @winrt_commethod(6)
    def CreateUserActivitySessionInBackground(self, activity: win32more.Windows.ApplicationModel.UserActivities.UserActivity) -> win32more.Windows.ApplicationModel.UserActivities.UserActivitySession: ...
    @winrt_commethod(7)
    def DeleteUserActivitySessionsInTimeRangeAsync(self, channel: win32more.Windows.ApplicationModel.UserActivities.UserActivityChannel, startTime: win32more.Windows.Foundation.DateTime, endTime: win32more.Windows.Foundation.DateTime) -> win32more.Windows.Foundation.IAsyncAction: ...


make_ready(__name__)
