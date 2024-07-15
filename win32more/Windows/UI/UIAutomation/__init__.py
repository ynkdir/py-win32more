from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.UI.UIAutomation
import win32more.Windows.Win32.System.WinRT
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
    AppUserModelId = property(get_AppUserModelId, None)
    ExecutableFileName = property(get_ExecutableFileName, None)
    IsRemoteSystem = property(get_IsRemoteSystem, None)
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
    AppUserModelId = property(get_AppUserModelId, None)
    ExecutableFileName = property(get_ExecutableFileName, None)
    IsRemoteSystem = property(get_IsRemoteSystem, None)
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
    AppUserModelId = property(get_AppUserModelId, None)
    ExecutableFileName = property(get_ExecutableFileName, None)
    IsRemoteSystem = property(get_IsRemoteSystem, None)
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
    AppUserModelId = property(get_AppUserModelId, None)
    ExecutableFileName = property(get_ExecutableFileName, None)
    IsRemoteSystem = property(get_IsRemoteSystem, None)
class IAutomationTextRange(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.UIAutomation.IAutomationTextRange'
    _iid_ = Guid('{7e101b65-40d3-5994-85a9-0a0cb9a4ec98}')
UIAutomationContract: UInt32 = 131072


make_ready(__name__)
