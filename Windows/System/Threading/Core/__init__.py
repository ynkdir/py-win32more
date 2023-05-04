from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.Foundation
import Windows.System.Threading
import Windows.System.Threading.Core
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IPreallocatedWorkItem(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{b6daa9fc-bc5b-401a-a8b2-6e754d14daa6}')
    @winrt_commethod(6)
    def RunAsync(self) -> Windows.Foundation.IAsyncAction: ...
class IPreallocatedWorkItemFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{e3d32b45-dfea-469b-82c5-f6e3cefdeafb}')
    @winrt_commethod(6)
    def CreateWorkItem(self, handler: Windows.System.Threading.WorkItemHandler) -> Windows.System.Threading.Core.PreallocatedWorkItem: ...
    @winrt_commethod(7)
    def CreateWorkItemWithPriority(self, handler: Windows.System.Threading.WorkItemHandler, priority: Windows.System.Threading.WorkItemPriority) -> Windows.System.Threading.Core.PreallocatedWorkItem: ...
    @winrt_commethod(8)
    def CreateWorkItemWithPriorityAndOptions(self, handler: Windows.System.Threading.WorkItemHandler, priority: Windows.System.Threading.WorkItemPriority, options: Windows.System.Threading.WorkItemOptions) -> Windows.System.Threading.Core.PreallocatedWorkItem: ...
class ISignalNotifier(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{14285e06-63a7-4713-b6d9-62f64b56fb8b}')
    @winrt_commethod(6)
    def Enable(self) -> Void: ...
    @winrt_commethod(7)
    def Terminate(self) -> Void: ...
class ISignalNotifierStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{1c4e4566-8400-46d3-a115-7d0c0dfc9f62}')
    @winrt_commethod(6)
    def AttachToEvent(self, name: WinRT_String, handler: Windows.System.Threading.Core.SignalHandler) -> Windows.System.Threading.Core.SignalNotifier: ...
    @winrt_commethod(7)
    def AttachToEventWithTimeout(self, name: WinRT_String, handler: Windows.System.Threading.Core.SignalHandler, timeout: Windows.Foundation.TimeSpan) -> Windows.System.Threading.Core.SignalNotifier: ...
    @winrt_commethod(8)
    def AttachToSemaphore(self, name: WinRT_String, handler: Windows.System.Threading.Core.SignalHandler) -> Windows.System.Threading.Core.SignalNotifier: ...
    @winrt_commethod(9)
    def AttachToSemaphoreWithTimeout(self, name: WinRT_String, handler: Windows.System.Threading.Core.SignalHandler, timeout: Windows.Foundation.TimeSpan) -> Windows.System.Threading.Core.SignalNotifier: ...
class PreallocatedWorkItem(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.System.Threading.Core.IPreallocatedWorkItem
    _classid_ = 'Windows.System.Threading.Core.PreallocatedWorkItem'
    @winrt_factorymethod
    def CreateWorkItem(cls: Windows.System.Threading.Core.IPreallocatedWorkItemFactory, handler: Windows.System.Threading.WorkItemHandler) -> Windows.System.Threading.Core.PreallocatedWorkItem: ...
    @winrt_factorymethod
    def CreateWorkItemWithPriority(cls: Windows.System.Threading.Core.IPreallocatedWorkItemFactory, handler: Windows.System.Threading.WorkItemHandler, priority: Windows.System.Threading.WorkItemPriority) -> Windows.System.Threading.Core.PreallocatedWorkItem: ...
    @winrt_factorymethod
    def CreateWorkItemWithPriorityAndOptions(cls: Windows.System.Threading.Core.IPreallocatedWorkItemFactory, handler: Windows.System.Threading.WorkItemHandler, priority: Windows.System.Threading.WorkItemPriority, options: Windows.System.Threading.WorkItemOptions) -> Windows.System.Threading.Core.PreallocatedWorkItem: ...
    @winrt_mixinmethod
    def RunAsync(self: Windows.System.Threading.Core.IPreallocatedWorkItem) -> Windows.Foundation.IAsyncAction: ...
class SignalHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{923c402e-4721-440e-9dda-55b6f2e07710}')
    _classid_ = 'Windows.System.Threading.Core.SignalHandler'
    @winrt_commethod(3)
    def Invoke(self, signalNotifier: Windows.System.Threading.Core.SignalNotifier, timedOut: Boolean) -> Void: ...
class SignalNotifier(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.System.Threading.Core.ISignalNotifier
    _classid_ = 'Windows.System.Threading.Core.SignalNotifier'
    @winrt_mixinmethod
    def Enable(self: Windows.System.Threading.Core.ISignalNotifier) -> Void: ...
    @winrt_mixinmethod
    def Terminate(self: Windows.System.Threading.Core.ISignalNotifier) -> Void: ...
    @winrt_classmethod
    def AttachToEvent(cls: Windows.System.Threading.Core.ISignalNotifierStatics, name: WinRT_String, handler: Windows.System.Threading.Core.SignalHandler) -> Windows.System.Threading.Core.SignalNotifier: ...
    @winrt_classmethod
    def AttachToEventWithTimeout(cls: Windows.System.Threading.Core.ISignalNotifierStatics, name: WinRT_String, handler: Windows.System.Threading.Core.SignalHandler, timeout: Windows.Foundation.TimeSpan) -> Windows.System.Threading.Core.SignalNotifier: ...
    @winrt_classmethod
    def AttachToSemaphore(cls: Windows.System.Threading.Core.ISignalNotifierStatics, name: WinRT_String, handler: Windows.System.Threading.Core.SignalHandler) -> Windows.System.Threading.Core.SignalNotifier: ...
    @winrt_classmethod
    def AttachToSemaphoreWithTimeout(cls: Windows.System.Threading.Core.ISignalNotifierStatics, name: WinRT_String, handler: Windows.System.Threading.Core.SignalHandler, timeout: Windows.Foundation.TimeSpan) -> Windows.System.Threading.Core.SignalNotifier: ...
make_head(_module, 'IPreallocatedWorkItem')
make_head(_module, 'IPreallocatedWorkItemFactory')
make_head(_module, 'ISignalNotifier')
make_head(_module, 'ISignalNotifierStatics')
make_head(_module, 'PreallocatedWorkItem')
make_head(_module, 'SignalHandler')
make_head(_module, 'SignalNotifier')
