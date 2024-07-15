from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.System.Threading
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
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
    Delay = property(get_Delay, None)
    Period = property(get_Period, None)
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
    Delay = property(get_Delay, None)
    Period = property(get_Period, None)
class TimerDestroyedHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{34ed19fa-8384-4eb9-8209-fb5094eeec35}')
    @winrt_commethod(3)
    def Invoke(self, timer: win32more.Windows.System.Threading.ThreadPoolTimer) -> Void: ...
class TimerElapsedHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{faaea667-fbeb-49cb-adb2-71184c556e43}')
    @winrt_commethod(3)
    def Invoke(self, timer: win32more.Windows.System.Threading.ThreadPoolTimer) -> Void: ...
class WorkItemHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1d1a8b8b-fa66-414f-9cbd-b65fc99d17fa}')
    @winrt_commethod(3)
    def Invoke(self, operation: win32more.Windows.Foundation.IAsyncAction) -> Void: ...
class WorkItemOptions(Enum, UInt32):
    None_ = 0
    TimeSliced = 1
class WorkItemPriority(Enum, Int32):
    Low = -1
    Normal = 0
    High = 1


make_ready(__name__)
