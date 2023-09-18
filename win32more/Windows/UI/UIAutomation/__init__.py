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
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.UI.UIAutomation
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class AutomationConnection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.UIAutomation.IAutomationConnection
    _classid_ = 'Windows.UI.UIAutomation.AutomationConnection'
    @winrt_mixinmethod
    def get_IsRemoteSystem(self: win32more.Windows.UI.UIAutomation.IAutomationConnection) -> Boolean: ...
    @winrt_mixinmethod
    def get_AppUserModelId(self: win32more.Windows.UI.UIAutomation.IAutomationConnection) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ExecutableFileName(self: win32more.Windows.UI.UIAutomation.IAutomationConnection) -> WinRT_String: ...
    IsRemoteSystem = property(get_IsRemoteSystem, None)
    AppUserModelId = property(get_AppUserModelId, None)
    ExecutableFileName = property(get_ExecutableFileName, None)
class AutomationConnectionBoundObject(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.UIAutomation.IAutomationConnectionBoundObject
    _classid_ = 'Windows.UI.UIAutomation.AutomationConnectionBoundObject'
    @winrt_mixinmethod
    def get_Connection(self: win32more.Windows.UI.UIAutomation.IAutomationConnectionBoundObject) -> win32more.Windows.UI.UIAutomation.AutomationConnection: ...
    Connection = property(get_Connection, None)
class AutomationElement(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.UIAutomation.IAutomationElement
    _classid_ = 'Windows.UI.UIAutomation.AutomationElement'
    @winrt_mixinmethod
    def get_IsRemoteSystem(self: win32more.Windows.UI.UIAutomation.IAutomationElement) -> Boolean: ...
    @winrt_mixinmethod
    def get_AppUserModelId(self: win32more.Windows.UI.UIAutomation.IAutomationElement) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ExecutableFileName(self: win32more.Windows.UI.UIAutomation.IAutomationElement) -> WinRT_String: ...
    IsRemoteSystem = property(get_IsRemoteSystem, None)
    AppUserModelId = property(get_AppUserModelId, None)
    ExecutableFileName = property(get_ExecutableFileName, None)
class AutomationTextRange(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.UIAutomation.IAutomationTextRange
    _classid_ = 'Windows.UI.UIAutomation.AutomationTextRange'
class IAutomationConnection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.UIAutomation.IAutomationConnection'
    _iid_ = Guid('{aad262ed-0ef4-5d43-97be-a834e27b65b9}')
    @winrt_commethod(6)
    def get_IsRemoteSystem(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_AppUserModelId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_ExecutableFileName(self) -> WinRT_String: ...
    IsRemoteSystem = property(get_IsRemoteSystem, None)
    AppUserModelId = property(get_AppUserModelId, None)
    ExecutableFileName = property(get_ExecutableFileName, None)
class IAutomationConnectionBoundObject(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.UIAutomation.IAutomationConnectionBoundObject'
    _iid_ = Guid('{5e8558fb-ca52-5b65-9830-dd2905816093}')
    @winrt_commethod(6)
    def get_Connection(self) -> win32more.Windows.UI.UIAutomation.AutomationConnection: ...
    Connection = property(get_Connection, None)
class IAutomationElement(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.UIAutomation.IAutomationElement'
    _iid_ = Guid('{a1898370-2c07-56fd-993f-61a72a08058c}')
    @winrt_commethod(6)
    def get_IsRemoteSystem(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_AppUserModelId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_ExecutableFileName(self) -> WinRT_String: ...
    IsRemoteSystem = property(get_IsRemoteSystem, None)
    AppUserModelId = property(get_AppUserModelId, None)
    ExecutableFileName = property(get_ExecutableFileName, None)
class IAutomationTextRange(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.UIAutomation.IAutomationTextRange'
    _iid_ = Guid('{7e101b65-40d3-5994-85a9-0a0cb9a4ec98}')
UIAutomationContract: UInt32 = 131072
make_head(_module, 'AutomationConnection')
make_head(_module, 'AutomationConnectionBoundObject')
make_head(_module, 'AutomationElement')
make_head(_module, 'AutomationTextRange')
make_head(_module, 'IAutomationConnection')
make_head(_module, 'IAutomationConnectionBoundObject')
make_head(_module, 'IAutomationElement')
make_head(_module, 'IAutomationTextRange')
