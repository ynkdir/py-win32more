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
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Microsoft.UI.Dispatching
import win32more.Windows.Foundation
class DispatcherExitDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Dispatching.IDispatcherExitDeferral
    _classid_ = 'Microsoft.UI.Dispatching.DispatcherExitDeferral'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Microsoft.UI.Dispatching.DispatcherExitDeferral.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Dispatching.DispatcherExitDeferral: ...
    @winrt_mixinmethod
    def Complete(self: win32more.Microsoft.UI.Dispatching.IDispatcherExitDeferral) -> Void: ...
class DispatcherQueue(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Dispatching.IDispatcherQueue
    _classid_ = 'Microsoft.UI.Dispatching.DispatcherQueue'
    @winrt_mixinmethod
    def EnqueueEventLoopExit(self: win32more.Microsoft.UI.Dispatching.IDispatcherQueue3) -> Void: ...
    @winrt_mixinmethod
    def TryEnqueue(self: win32more.Microsoft.UI.Dispatching.IDispatcherQueue, callback: win32more.Microsoft.UI.Dispatching.DispatcherQueueHandler) -> Boolean: ...
    @winrt_mixinmethod
    def TryEnqueueWithPriority(self: win32more.Microsoft.UI.Dispatching.IDispatcherQueue, priority: win32more.Microsoft.UI.Dispatching.DispatcherQueuePriority, callback: win32more.Microsoft.UI.Dispatching.DispatcherQueueHandler) -> Boolean: ...
    @winrt_mixinmethod
    def CreateTimer(self: win32more.Microsoft.UI.Dispatching.IDispatcherQueue) -> win32more.Microsoft.UI.Dispatching.DispatcherQueueTimer: ...
    @winrt_mixinmethod
    def remove_ShutdownStarting(self: win32more.Microsoft.UI.Dispatching.IDispatcherQueue, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ShutdownCompleted(self: win32more.Microsoft.UI.Dispatching.IDispatcherQueue, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Dispatching.DispatcherQueue, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ShutdownCompleted(self: win32more.Microsoft.UI.Dispatching.IDispatcherQueue, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_HasThreadAccess(self: win32more.Microsoft.UI.Dispatching.IDispatcherQueue2) -> Boolean: ...
    @winrt_mixinmethod
    def add_ShutdownStarting(self: win32more.Microsoft.UI.Dispatching.IDispatcherQueue, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Dispatching.DispatcherQueue, win32more.Microsoft.UI.Dispatching.DispatcherQueueShutdownStartingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def EnsureSystemDispatcherQueue(self: win32more.Microsoft.UI.Dispatching.IDispatcherQueue3) -> Void: ...
    @winrt_mixinmethod
    def RunEventLoop(self: win32more.Microsoft.UI.Dispatching.IDispatcherQueue3) -> Void: ...
    @winrt_mixinmethod
    def RunEventLoopWithOptions(self: win32more.Microsoft.UI.Dispatching.IDispatcherQueue3, options: win32more.Microsoft.UI.Dispatching.DispatcherRunOptions, deferral: win32more.Microsoft.UI.Dispatching.DispatcherExitDeferral) -> Void: ...
    @winrt_mixinmethod
    def add_FrameworkShutdownStarting(self: win32more.Microsoft.UI.Dispatching.IDispatcherQueue3, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Dispatching.DispatcherQueue, win32more.Microsoft.UI.Dispatching.DispatcherQueueShutdownStartingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FrameworkShutdownStarting(self: win32more.Microsoft.UI.Dispatching.IDispatcherQueue3, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_FrameworkShutdownCompleted(self: win32more.Microsoft.UI.Dispatching.IDispatcherQueue3, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Dispatching.DispatcherQueue, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FrameworkShutdownCompleted(self: win32more.Microsoft.UI.Dispatching.IDispatcherQueue3, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetForCurrentThread(cls: win32more.Microsoft.UI.Dispatching.IDispatcherQueueStatics) -> win32more.Microsoft.UI.Dispatching.DispatcherQueue: ...
    HasThreadAccess = property(get_HasThreadAccess, None)
class DispatcherQueueController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Dispatching.IDispatcherQueueController
    _classid_ = 'Microsoft.UI.Dispatching.DispatcherQueueController'
    @winrt_mixinmethod
    def get_DispatcherQueue(self: win32more.Microsoft.UI.Dispatching.IDispatcherQueueController) -> win32more.Microsoft.UI.Dispatching.DispatcherQueue: ...
    @winrt_mixinmethod
    def ShutdownQueueAsync(self: win32more.Microsoft.UI.Dispatching.IDispatcherQueueController) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ShutdownQueue(self: win32more.Microsoft.UI.Dispatching.IDispatcherQueueController2) -> Void: ...
    @winrt_classmethod
    def CreateOnDedicatedThread(cls: win32more.Microsoft.UI.Dispatching.IDispatcherQueueControllerStatics) -> win32more.Microsoft.UI.Dispatching.DispatcherQueueController: ...
    @winrt_classmethod
    def CreateOnCurrentThread(cls: win32more.Microsoft.UI.Dispatching.IDispatcherQueueControllerStatics) -> win32more.Microsoft.UI.Dispatching.DispatcherQueueController: ...
    DispatcherQueue = property(get_DispatcherQueue, None)
class DispatcherQueueHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2e0872a9-4e29-5f14-b688-fb96d5f9d5f8}')
    def Invoke(self) -> Void: ...
DispatcherQueuePriority = Int32
DispatcherQueuePriority_Low: DispatcherQueuePriority = -10
DispatcherQueuePriority_Normal: DispatcherQueuePriority = 0
DispatcherQueuePriority_High: DispatcherQueuePriority = 10
class DispatcherQueueShutdownStartingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Dispatching.IDispatcherQueueShutdownStartingEventArgs
    _classid_ = 'Microsoft.UI.Dispatching.DispatcherQueueShutdownStartingEventArgs'
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Microsoft.UI.Dispatching.IDispatcherQueueShutdownStartingEventArgs) -> win32more.Windows.Foundation.Deferral: ...
class DispatcherQueueTimer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Dispatching.IDispatcherQueueTimer
    _classid_ = 'Microsoft.UI.Dispatching.DispatcherQueueTimer'
    @winrt_mixinmethod
    def put_Interval(self: win32more.Microsoft.UI.Dispatching.IDispatcherQueueTimer, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def put_IsRepeating(self: win32more.Microsoft.UI.Dispatching.IDispatcherQueueTimer, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsRunning(self: win32more.Microsoft.UI.Dispatching.IDispatcherQueueTimer) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsRepeating(self: win32more.Microsoft.UI.Dispatching.IDispatcherQueueTimer) -> Boolean: ...
    @winrt_mixinmethod
    def get_Interval(self: win32more.Microsoft.UI.Dispatching.IDispatcherQueueTimer) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def Start(self: win32more.Microsoft.UI.Dispatching.IDispatcherQueueTimer) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Microsoft.UI.Dispatching.IDispatcherQueueTimer) -> Void: ...
    @winrt_mixinmethod
    def add_Tick(self: win32more.Microsoft.UI.Dispatching.IDispatcherQueueTimer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Dispatching.DispatcherQueueTimer, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Tick(self: win32more.Microsoft.UI.Dispatching.IDispatcherQueueTimer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Interval = property(get_Interval, put_Interval)
    IsRepeating = property(get_IsRepeating, put_IsRepeating)
    IsRunning = property(get_IsRunning, None)
DispatcherRunOptions = UInt32
DispatcherRunOptions_None: DispatcherRunOptions = 0
DispatcherRunOptions_ContinueOnQuit: DispatcherRunOptions = 1
DispatcherRunOptions_QuitOnlyLocalLoop: DispatcherRunOptions = 2
class IDispatcherExitDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Dispatching.IDispatcherExitDeferral'
    _iid_ = Guid('{910b5aac-3310-563e-8418-f3005579729e}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IDispatcherQueue(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Dispatching.IDispatcherQueue'
    _iid_ = Guid('{f6ebf8fa-be1c-5bf6-a467-73da28738ae8}')
    @winrt_commethod(6)
    def CreateTimer(self) -> win32more.Microsoft.UI.Dispatching.DispatcherQueueTimer: ...
    @winrt_commethod(7)
    def TryEnqueue(self, callback: win32more.Microsoft.UI.Dispatching.DispatcherQueueHandler) -> Boolean: ...
    @winrt_commethod(8)
    def TryEnqueueWithPriority(self, priority: win32more.Microsoft.UI.Dispatching.DispatcherQueuePriority, callback: win32more.Microsoft.UI.Dispatching.DispatcherQueueHandler) -> Boolean: ...
    @winrt_commethod(9)
    def add_ShutdownStarting(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Dispatching.DispatcherQueue, win32more.Microsoft.UI.Dispatching.DispatcherQueueShutdownStartingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_ShutdownStarting(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_ShutdownCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Dispatching.DispatcherQueue, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_ShutdownCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class IDispatcherQueue2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Dispatching.IDispatcherQueue2'
    _iid_ = Guid('{0cf48751-f1ac-59b8-ba52-6ce7a1444d6f}')
    @winrt_commethod(6)
    def get_HasThreadAccess(self) -> Boolean: ...
    HasThreadAccess = property(get_HasThreadAccess, None)
class IDispatcherQueue3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Dispatching.IDispatcherQueue3'
    _iid_ = Guid('{14a7a175-5c27-5a35-b079-21960cf764a8}')
    @winrt_commethod(6)
    def EnqueueEventLoopExit(self) -> Void: ...
    @winrt_commethod(7)
    def EnsureSystemDispatcherQueue(self) -> Void: ...
    @winrt_commethod(8)
    def RunEventLoop(self) -> Void: ...
    @winrt_commethod(9)
    def RunEventLoopWithOptions(self, options: win32more.Microsoft.UI.Dispatching.DispatcherRunOptions, deferral: win32more.Microsoft.UI.Dispatching.DispatcherExitDeferral) -> Void: ...
    @winrt_commethod(10)
    def add_FrameworkShutdownStarting(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Dispatching.DispatcherQueue, win32more.Microsoft.UI.Dispatching.DispatcherQueueShutdownStartingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_FrameworkShutdownStarting(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_FrameworkShutdownCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Dispatching.DispatcherQueue, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_FrameworkShutdownCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class IDispatcherQueueController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Dispatching.IDispatcherQueueController'
    _iid_ = Guid('{bce8178d-2183-584c-9e5b-f9366f6ae484}')
    @winrt_commethod(6)
    def get_DispatcherQueue(self) -> win32more.Microsoft.UI.Dispatching.DispatcherQueue: ...
    @winrt_commethod(7)
    def ShutdownQueueAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    DispatcherQueue = property(get_DispatcherQueue, None)
class IDispatcherQueueController2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Dispatching.IDispatcherQueueController2'
    _iid_ = Guid('{4c68ee2a-1cb1-5591-a3a2-9b590b8f8b9a}')
    @winrt_commethod(6)
    def ShutdownQueue(self) -> Void: ...
class IDispatcherQueueControllerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Dispatching.IDispatcherQueueControllerStatics'
    _iid_ = Guid('{f18d6145-722b-593d-bcf2-a61e713f0037}')
    @winrt_commethod(6)
    def CreateOnDedicatedThread(self) -> win32more.Microsoft.UI.Dispatching.DispatcherQueueController: ...
    @winrt_commethod(7)
    def CreateOnCurrentThread(self) -> win32more.Microsoft.UI.Dispatching.DispatcherQueueController: ...
class IDispatcherQueueShutdownStartingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Dispatching.IDispatcherQueueShutdownStartingEventArgs'
    _iid_ = Guid('{32519be5-072b-5660-a70e-8835c9b8157d}')
    @winrt_commethod(6)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
class IDispatcherQueueStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Dispatching.IDispatcherQueueStatics'
    _iid_ = Guid('{cd3382ea-a455-5124-b63a-ca40d34ca23c}')
    @winrt_commethod(6)
    def GetForCurrentThread(self) -> win32more.Microsoft.UI.Dispatching.DispatcherQueue: ...
class IDispatcherQueueTimer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Dispatching.IDispatcherQueueTimer'
    _iid_ = Guid('{ad4d63fd-88fe-541f-ac11-bf2dc1ed2ce5}')
    @winrt_commethod(6)
    def get_Interval(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def put_Interval(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(8)
    def get_IsRunning(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsRepeating(self) -> Boolean: ...
    @winrt_commethod(10)
    def put_IsRepeating(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def Start(self) -> Void: ...
    @winrt_commethod(12)
    def Stop(self) -> Void: ...
    @winrt_commethod(13)
    def add_Tick(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Dispatching.DispatcherQueueTimer, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_Tick(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Interval = property(get_Interval, put_Interval)
    IsRunning = property(get_IsRunning, None)
    IsRepeating = property(get_IsRepeating, put_IsRepeating)
make_ready(__name__)
