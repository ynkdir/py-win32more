from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel.Preview.InkWorkspace
import win32more.Windows.Foundation
import win32more.Windows.Graphics.Imaging
import win32more.Windows.Win32.System.WinRT
class IInkWorkspaceHostedAppManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Preview.InkWorkspace.IInkWorkspaceHostedAppManager'
    _iid_ = Guid('{fe0a7990-5e59-4bb7-8a63-7d218cd96300}')
    @winrt_commethod(6)
    def SetThumbnailAsync(self, bitmap: win32more.Windows.Graphics.Imaging.SoftwareBitmap) -> win32more.Windows.Foundation.IAsyncAction: ...
class IInkWorkspaceHostedAppManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Preview.InkWorkspace.IInkWorkspaceHostedAppManagerStatics'
    _iid_ = Guid('{cbfd8cc5-a162-4bc4-84ee-e8716d5233c5}')
    @winrt_commethod(6)
    def GetForCurrentApp(self) -> win32more.Windows.ApplicationModel.Preview.InkWorkspace.InkWorkspaceHostedAppManager: ...
class InkWorkspaceHostedAppManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Preview.InkWorkspace.IInkWorkspaceHostedAppManager
    _classid_ = 'Windows.ApplicationModel.Preview.InkWorkspace.InkWorkspaceHostedAppManager'
    @winrt_mixinmethod
    def SetThumbnailAsync(self: win32more.Windows.ApplicationModel.Preview.InkWorkspace.IInkWorkspaceHostedAppManager, bitmap: win32more.Windows.Graphics.Imaging.SoftwareBitmap) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def GetForCurrentApp(cls: win32more.Windows.ApplicationModel.Preview.InkWorkspace.IInkWorkspaceHostedAppManagerStatics) -> win32more.Windows.ApplicationModel.Preview.InkWorkspace.InkWorkspaceHostedAppManager: ...
PreviewInkWorkspaceContract: UInt32 = 65536


make_ready(__name__)
