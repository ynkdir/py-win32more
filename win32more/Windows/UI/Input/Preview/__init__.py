from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.UI.Input
import win32more.Windows.UI.Input.Preview
import win32more.Windows.UI.WindowManagement
import win32more.Windows.Win32.System.WinRT
class IInputActivationListenerPreviewStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Preview.IInputActivationListenerPreviewStatics'
    _iid_ = Guid('{f0551ce5-0de6-5be0-a589-f737201a4582}')
    @winrt_commethod(6)
    def CreateForApplicationWindow(self, window: win32more.Windows.UI.WindowManagement.AppWindow) -> win32more.Windows.UI.Input.InputActivationListener: ...
class InputActivationListenerPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Preview.InputActivationListenerPreview'
    @winrt_classmethod
    def CreateForApplicationWindow(cls: win32more.Windows.UI.Input.Preview.IInputActivationListenerPreviewStatics, window: win32more.Windows.UI.WindowManagement.AppWindow) -> win32more.Windows.UI.Input.InputActivationListener: ...


make_ready(__name__)
