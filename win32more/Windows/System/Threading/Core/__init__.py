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
import win32more.Windows.Foundation
import win32more.Windows.System.Threading
import win32more.Windows.System.Threading.Core
class IPreallocatedWorkItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Threading.Core.IPreallocatedWorkItem'
    _iid_ = Guid('{b6daa9fc-bc5b-401a-a8b2-6e754d14daa6}')
    @winrt_commethod(6)
    def RunAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
class IPreallocatedWorkItemFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Threading.Core.IPreallocatedWorkItemFactory'
    _iid_ = Guid('{e3d32b45-dfea-469b-82c5-f6e3cefdeafb}')
    @winrt_commethod(6)
    def CreateWorkItem(self, handler: win32more.Windows.System.Threading.WorkItemHandler) -> win32more.Windows.System.Threading.Core.PreallocatedWorkItem: ...
    @winrt_commethod(7)
    def CreateWorkItemWithPriority(self, handler: win32more.Windows.System.Threading.WorkItemHandler, priority: win32more.Windows.System.Threading.WorkItemPriority) -> win32more.Windows.System.Threading.Core.PreallocatedWorkItem: ...
    @winrt_commethod(8)
    def CreateWorkItemWithPriorityAndOptions(self, handler: win32more.Windows.System.Threading.WorkItemHandler, priority: win32more.Windows.System.Threading.WorkItemPriority, options: win32more.Windows.System.Threading.WorkItemOptions) -> win32more.Windows.System.Threading.Core.PreallocatedWorkItem: ...
class ISignalNotifier(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Threading.Core.ISignalNotifier'
    _iid_ = Guid('{14285e06-63a7-4713-b6d9-62f64b56fb8b}')
    @winrt_commethod(6)
    def Enable(self) -> Void: ...
    @winrt_commethod(7)
    def Terminate(self) -> Void: ...
class ISignalNotifierStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Threading.Core.ISignalNotifierStatics'
    _iid_ = Guid('{1c4e4566-8400-46d3-a115-7d0c0dfc9f62}')
    @winrt_commethod(6)
    def AttachToEvent(self, name: WinRT_String, handler: win32more.Windows.System.Threading.Core.SignalHandler) -> win32more.Windows.System.Threading.Core.SignalNotifier: ...
    @winrt_commethod(7)
    def AttachToEventWithTimeout(self, name: WinRT_String, handler: win32more.Windows.System.Threading.Core.SignalHandler, timeout: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.System.Threading.Core.SignalNotifier: ...
    @winrt_commethod(8)
    def AttachToSemaphore(self, name: WinRT_String, handler: win32more.Windows.System.Threading.Core.SignalHandler) -> win32more.Windows.System.Threading.Core.SignalNotifier: ...
    @winrt_commethod(9)
    def AttachToSemaphoreWithTimeout(self, name: WinRT_String, handler: win32more.Windows.System.Threading.Core.SignalHandler, timeout: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.System.Threading.Core.SignalNotifier: ...
class PreallocatedWorkItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.Threading.Core.IPreallocatedWorkItem
    _classid_ = 'Windows.System.Threading.Core.PreallocatedWorkItem'
    @winrt_factorymethod
    def CreateWorkItem(cls: win32more.Windows.System.Threading.Core.IPreallocatedWorkItemFactory, handler: win32more.Windows.System.Threading.WorkItemHandler) -> win32more.Windows.System.Threading.Core.PreallocatedWorkItem: ...
    @winrt_factorymethod
    def CreateWorkItemWithPriority(cls: win32more.Windows.System.Threading.Core.IPreallocatedWorkItemFactory, handler: win32more.Windows.System.Threading.WorkItemHandler, priority: win32more.Windows.System.Threading.WorkItemPriority) -> win32more.Windows.System.Threading.Core.PreallocatedWorkItem: ...
    @winrt_factorymethod
    def CreateWorkItemWithPriorityAndOptions(cls: win32more.Windows.System.Threading.Core.IPreallocatedWorkItemFactory, handler: win32more.Windows.System.Threading.WorkItemHandler, priority: win32more.Windows.System.Threading.WorkItemPriority, options: win32more.Windows.System.Threading.WorkItemOptions) -> win32more.Windows.System.Threading.Core.PreallocatedWorkItem: ...
    @winrt_mixinmethod
    def RunAsync(self: win32more.Windows.System.Threading.Core.IPreallocatedWorkItem) -> win32more.Windows.Foundation.IAsyncAction: ...
class SignalHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{923c402e-4721-440e-9dda-55b6f2e07710}')
    def Invoke(self, signalNotifier: win32more.Windows.System.Threading.Core.SignalNotifier, timedOut: Boolean) -> Void: ...
class SignalNotifier(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.Threading.Core.ISignalNotifier
    _classid_ = 'Windows.System.Threading.Core.SignalNotifier'
    @winrt_mixinmethod
    def Enable(self: win32more.Windows.System.Threading.Core.ISignalNotifier) -> Void: ...
    @winrt_mixinmethod
    def Terminate(self: win32more.Windows.System.Threading.Core.ISignalNotifier) -> Void: ...
    @winrt_classmethod
    def AttachToEvent(cls: win32more.Windows.System.Threading.Core.ISignalNotifierStatics, name: WinRT_String, handler: win32more.Windows.System.Threading.Core.SignalHandler) -> win32more.Windows.System.Threading.Core.SignalNotifier: ...
    @winrt_classmethod
    def AttachToEventWithTimeout(cls: win32more.Windows.System.Threading.Core.ISignalNotifierStatics, name: WinRT_String, handler: win32more.Windows.System.Threading.Core.SignalHandler, timeout: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.System.Threading.Core.SignalNotifier: ...
    @winrt_classmethod
    def AttachToSemaphore(cls: win32more.Windows.System.Threading.Core.ISignalNotifierStatics, name: WinRT_String, handler: win32more.Windows.System.Threading.Core.SignalHandler) -> win32more.Windows.System.Threading.Core.SignalNotifier: ...
    @winrt_classmethod
    def AttachToSemaphoreWithTimeout(cls: win32more.Windows.System.Threading.Core.ISignalNotifierStatics, name: WinRT_String, handler: win32more.Windows.System.Threading.Core.SignalHandler, timeout: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.System.Threading.Core.SignalNotifier: ...
make_ready(__name__)
