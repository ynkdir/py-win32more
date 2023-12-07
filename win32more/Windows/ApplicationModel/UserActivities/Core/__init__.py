from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
import sys
from typing import Generic, TypeVar
if sys.version_info < (3, 9):
    from typing_extensions import Annotated
else:
    from typing import Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, EasyCastStructure, EasyCastUnion, ComPtr, make_ready
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, winrt_overload, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.ApplicationModel.UserActivities
import win32more.Windows.ApplicationModel.UserActivities.Core
import win32more.Windows.Foundation
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
