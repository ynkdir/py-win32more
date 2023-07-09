from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation
import win32more.Windows.System.Threading
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IThreadPoolStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Threading.IThreadPoolStatics'
    _iid_ = Guid('{b6bf67dd-84bd-44f8-ac1c-93ebcb9dba91}')
    @winrt_commethod(6)
    def RunAsync(self, handler: win32more.Windows.System.Threading.WorkItemHandler) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def RunWithPriorityAsync(self, handler: win32more.Windows.System.Threading.WorkItemHandler, priority: win32more.Windows.System.Threading.WorkItemPriority) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def RunWithPriorityAndOptionsAsync(self, handler: win32more.Windows.System.Threading.WorkItemHandler, priority: win32more.Windows.System.Threading.WorkItemPriority, options: win32more.Windows.System.Threading.WorkItemOptions) -> win32more.Windows.Foundation.IAsyncAction: ...
class IThreadPoolTimer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Threading.IThreadPoolTimer'
    _iid_ = Guid('{594ebe78-55ea-4a88-a50d-3402ae1f9cf2}')
    @winrt_commethod(6)
    def get_Period(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def get_Delay(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(8)
    def Cancel(self) -> Void: ...
    Period = property(get_Period, None)
    Delay = property(get_Delay, None)
class IThreadPoolTimerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Threading.IThreadPoolTimerStatics'
    _iid_ = Guid('{1a8a9d02-e482-461b-b8c7-8efad1cce590}')
    @winrt_commethod(6)
    def CreatePeriodicTimer(self, handler: win32more.Windows.System.Threading.TimerElapsedHandler, period: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.System.Threading.ThreadPoolTimer: ...
    @winrt_commethod(7)
    def CreateTimer(self, handler: win32more.Windows.System.Threading.TimerElapsedHandler, delay: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.System.Threading.ThreadPoolTimer: ...
    @winrt_commethod(8)
    def CreatePeriodicTimerWithCompletion(self, handler: win32more.Windows.System.Threading.TimerElapsedHandler, period: win32more.Windows.Foundation.TimeSpan, destroyed: win32more.Windows.System.Threading.TimerDestroyedHandler) -> win32more.Windows.System.Threading.ThreadPoolTimer: ...
    @winrt_commethod(9)
    def CreateTimerWithCompletion(self, handler: win32more.Windows.System.Threading.TimerElapsedHandler, delay: win32more.Windows.Foundation.TimeSpan, destroyed: win32more.Windows.System.Threading.TimerDestroyedHandler) -> win32more.Windows.System.Threading.ThreadPoolTimer: ...
class ThreadPool(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Threading.ThreadPool'
    @winrt_classmethod
    def RunAsync(cls: win32more.Windows.System.Threading.IThreadPoolStatics, handler: win32more.Windows.System.Threading.WorkItemHandler) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def RunWithPriorityAsync(cls: win32more.Windows.System.Threading.IThreadPoolStatics, handler: win32more.Windows.System.Threading.WorkItemHandler, priority: win32more.Windows.System.Threading.WorkItemPriority) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def RunWithPriorityAndOptionsAsync(cls: win32more.Windows.System.Threading.IThreadPoolStatics, handler: win32more.Windows.System.Threading.WorkItemHandler, priority: win32more.Windows.System.Threading.WorkItemPriority, options: win32more.Windows.System.Threading.WorkItemOptions) -> win32more.Windows.Foundation.IAsyncAction: ...
class ThreadPoolTimer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.Threading.IThreadPoolTimer
    _classid_ = 'Windows.System.Threading.ThreadPoolTimer'
    @winrt_mixinmethod
    def get_Period(self: win32more.Windows.System.Threading.IThreadPoolTimer) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Delay(self: win32more.Windows.System.Threading.IThreadPoolTimer) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def Cancel(self: win32more.Windows.System.Threading.IThreadPoolTimer) -> Void: ...
    @winrt_classmethod
    def CreatePeriodicTimer(cls: win32more.Windows.System.Threading.IThreadPoolTimerStatics, handler: win32more.Windows.System.Threading.TimerElapsedHandler, period: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.System.Threading.ThreadPoolTimer: ...
    @winrt_classmethod
    def CreateTimer(cls: win32more.Windows.System.Threading.IThreadPoolTimerStatics, handler: win32more.Windows.System.Threading.TimerElapsedHandler, delay: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.System.Threading.ThreadPoolTimer: ...
    @winrt_classmethod
    def CreatePeriodicTimerWithCompletion(cls: win32more.Windows.System.Threading.IThreadPoolTimerStatics, handler: win32more.Windows.System.Threading.TimerElapsedHandler, period: win32more.Windows.Foundation.TimeSpan, destroyed: win32more.Windows.System.Threading.TimerDestroyedHandler) -> win32more.Windows.System.Threading.ThreadPoolTimer: ...
    @winrt_classmethod
    def CreateTimerWithCompletion(cls: win32more.Windows.System.Threading.IThreadPoolTimerStatics, handler: win32more.Windows.System.Threading.TimerElapsedHandler, delay: win32more.Windows.Foundation.TimeSpan, destroyed: win32more.Windows.System.Threading.TimerDestroyedHandler) -> win32more.Windows.System.Threading.ThreadPoolTimer: ...
    Period = property(get_Period, None)
    Delay = property(get_Delay, None)
class TimerDestroyedHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{34ed19fa-8384-4eb9-8209-fb5094eeec35}')
    def Invoke(self, timer: win32more.Windows.System.Threading.ThreadPoolTimer) -> Void: ...
class TimerElapsedHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{faaea667-fbeb-49cb-adb2-71184c556e43}')
    def Invoke(self, timer: win32more.Windows.System.Threading.ThreadPoolTimer) -> Void: ...
class WorkItemHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1d1a8b8b-fa66-414f-9cbd-b65fc99d17fa}')
    def Invoke(self, operation: win32more.Windows.Foundation.IAsyncAction) -> Void: ...
WorkItemOptions = UInt32
WorkItemOptions_None: WorkItemOptions = 0
WorkItemOptions_TimeSliced: WorkItemOptions = 1
WorkItemPriority = Int32
WorkItemPriority_Low: WorkItemPriority = -1
WorkItemPriority_Normal: WorkItemPriority = 0
WorkItemPriority_High: WorkItemPriority = 1
make_head(_module, 'IThreadPoolStatics')
make_head(_module, 'IThreadPoolTimer')
make_head(_module, 'IThreadPoolTimerStatics')
make_head(_module, 'ThreadPool')
make_head(_module, 'ThreadPoolTimer')
