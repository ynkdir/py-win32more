from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.UI
import win32more.Windows.UI.Notifications.Preview
import win32more.Windows.Win32.System.WinRT
class IToastOcclusionManagerPreviewStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.Preview.IToastOcclusionManagerPreviewStatics'
    _iid_ = Guid('{507e5c83-50f9-5412-8953-b65c18cfab12}')
    @winrt_commethod(6)
    def SetToastWindowMargin(self, appWindowId: win32more.Windows.UI.WindowId, margin: Double) -> Void: ...
class ToastOcclusionManagerPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.Preview.ToastOcclusionManagerPreview'
    @winrt_classmethod
    def SetToastWindowMargin(cls: win32more.Windows.UI.Notifications.Preview.IToastOcclusionManagerPreviewStatics, appWindowId: win32more.Windows.UI.WindowId, margin: Double) -> Void: ...


make_ready(__name__)
