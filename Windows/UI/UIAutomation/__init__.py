from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, WinRT_String, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
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
class AutomationConnection(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.UIAutomation.AutomationConnection'
    @winrt_mixinmethod
    def get_IsRemoteSystem(self: Windows.UI.UIAutomation.IAutomationConnection) -> Boolean: ...
    @winrt_mixinmethod
    def get_AppUserModelId(self: Windows.UI.UIAutomation.IAutomationConnection) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ExecutableFileName(self: Windows.UI.UIAutomation.IAutomationConnection) -> WinRT_String: ...
    IsRemoteSystem = property(get_IsRemoteSystem, None)
    AppUserModelId = property(get_AppUserModelId, None)
    ExecutableFileName = property(get_ExecutableFileName, None)
class AutomationConnectionBoundObject(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.UIAutomation.AutomationConnectionBoundObject'
    @winrt_mixinmethod
    def get_Connection(self: Windows.UI.UIAutomation.IAutomationConnectionBoundObject) -> Windows.UI.UIAutomation.AutomationConnection: ...
    Connection = property(get_Connection, None)
class AutomationElement(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.UIAutomation.AutomationElement'
    @winrt_mixinmethod
    def get_IsRemoteSystem(self: Windows.UI.UIAutomation.IAutomationElement) -> Boolean: ...
    @winrt_mixinmethod
    def get_AppUserModelId(self: Windows.UI.UIAutomation.IAutomationElement) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ExecutableFileName(self: Windows.UI.UIAutomation.IAutomationElement) -> WinRT_String: ...
    IsRemoteSystem = property(get_IsRemoteSystem, None)
    AppUserModelId = property(get_AppUserModelId, None)
    ExecutableFileName = property(get_ExecutableFileName, None)
class AutomationTextRange(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.UIAutomation.AutomationTextRange'
class IAutomationConnection(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('aad262ed-0ef4-5d43-97-be-a8-34-e2-7b-65-b9')
    @winrt_commethod(6)
    def get_IsRemoteSystem(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_AppUserModelId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_ExecutableFileName(self) -> WinRT_String: ...
    IsRemoteSystem = property(get_IsRemoteSystem, None)
    AppUserModelId = property(get_AppUserModelId, None)
    ExecutableFileName = property(get_ExecutableFileName, None)
class IAutomationConnectionBoundObject(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5e8558fb-ca52-5b65-98-30-dd-29-05-81-60-93')
    @winrt_commethod(6)
    def get_Connection(self) -> Windows.UI.UIAutomation.AutomationConnection: ...
    Connection = property(get_Connection, None)
class IAutomationElement(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a1898370-2c07-56fd-99-3f-61-a7-2a-08-05-8c')
    @winrt_commethod(6)
    def get_IsRemoteSystem(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_AppUserModelId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_ExecutableFileName(self) -> WinRT_String: ...
    IsRemoteSystem = property(get_IsRemoteSystem, None)
    AppUserModelId = property(get_AppUserModelId, None)
    ExecutableFileName = property(get_ExecutableFileName, None)
class IAutomationTextRange(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7e101b65-40d3-5994-85-a9-0a-0c-b9-a4-ec-98')
UIAutomationContract: UInt32 = 131072
make_head(_module, 'AutomationConnection')
make_head(_module, 'AutomationConnectionBoundObject')
make_head(_module, 'AutomationElement')
make_head(_module, 'AutomationTextRange')
make_head(_module, 'IAutomationConnection')
make_head(_module, 'IAutomationConnectionBoundObject')
make_head(_module, 'IAutomationElement')
make_head(_module, 'IAutomationTextRange')
