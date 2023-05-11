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
import Windows.UI.UIAutomation
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
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.UIAutomation.IAutomationConnection
    _classid_ = 'Windows.UI.UIAutomation.AutomationConnection'
    @winrt_mixinmethod
    def get_IsRemoteSystem(self: Windows.UI.UIAutomation.IAutomationConnection) -> Boolean: ...
    @winrt_mixinmethod
    def get_AppUserModelId(self: Windows.UI.UIAutomation.IAutomationConnection) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ExecutableFileName(self: Windows.UI.UIAutomation.IAutomationConnection) -> WinRT_String: ...
    IsRemoteSystem = property(get_IsRemoteSystem, None)
    AppUserModelId = property(get_AppUserModelId, None)
    ExecutableFileName = property(get_ExecutableFileName, None)
class AutomationConnectionBoundObject(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.UIAutomation.IAutomationConnectionBoundObject
    _classid_ = 'Windows.UI.UIAutomation.AutomationConnectionBoundObject'
    @winrt_mixinmethod
    def get_Connection(self: Windows.UI.UIAutomation.IAutomationConnectionBoundObject) -> Windows.UI.UIAutomation.AutomationConnection: ...
    Connection = property(get_Connection, None)
class AutomationElement(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.UIAutomation.IAutomationElement
    _classid_ = 'Windows.UI.UIAutomation.AutomationElement'
    @winrt_mixinmethod
    def get_IsRemoteSystem(self: Windows.UI.UIAutomation.IAutomationElement) -> Boolean: ...
    @winrt_mixinmethod
    def get_AppUserModelId(self: Windows.UI.UIAutomation.IAutomationElement) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ExecutableFileName(self: Windows.UI.UIAutomation.IAutomationElement) -> WinRT_String: ...
    IsRemoteSystem = property(get_IsRemoteSystem, None)
    AppUserModelId = property(get_AppUserModelId, None)
    ExecutableFileName = property(get_ExecutableFileName, None)
class AutomationTextRange(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.UIAutomation.IAutomationTextRange
    _classid_ = 'Windows.UI.UIAutomation.AutomationTextRange'
class IAutomationConnection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.UIAutomation.IAutomationConnectionBoundObject'
    _iid_ = Guid('{5e8558fb-ca52-5b65-9830-dd2905816093}')
    @winrt_commethod(6)
    def get_Connection(self) -> Windows.UI.UIAutomation.AutomationConnection: ...
    Connection = property(get_Connection, None)
class IAutomationElement(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    extends: Windows.Win32.System.WinRT.IInspectable
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
