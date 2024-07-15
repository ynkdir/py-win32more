from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.UI.WindowManagement
import win32more.Windows.UI.WindowManagement.Preview
import win32more.Windows.Win32.System.WinRT
class IWindowManagementPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WindowManagement.Preview.IWindowManagementPreview'
    _iid_ = Guid('{4ef55b0d-561d-513c-a67c-2c02b69cef41}')
class IWindowManagementPreviewStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WindowManagement.Preview.IWindowManagementPreviewStatics'
    _iid_ = Guid('{0f9725c6-c004-5a23-8fd2-8d092ce2704a}')
    @winrt_commethod(6)
    def SetPreferredMinSize(self, window: win32more.Windows.UI.WindowManagement.AppWindow, preferredFrameMinSize: win32more.Windows.Foundation.Size) -> Void: ...
class WindowManagementPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.WindowManagement.Preview.IWindowManagementPreview
    _classid_ = 'Windows.UI.WindowManagement.Preview.WindowManagementPreview'
    @winrt_classmethod
    def SetPreferredMinSize(cls: win32more.Windows.UI.WindowManagement.Preview.IWindowManagementPreviewStatics, window: win32more.Windows.UI.WindowManagement.AppWindow, preferredFrameMinSize: win32more.Windows.Foundation.Size) -> Void: ...


make_ready(__name__)
