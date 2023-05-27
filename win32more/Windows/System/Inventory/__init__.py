from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.System.Inventory
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IInstalledDesktopApp(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Inventory.IInstalledDesktopApp'
    _iid_ = Guid('{75eab8ed-c0bc-5364-4c28-166e0545167a}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Publisher(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_DisplayVersion(self) -> WinRT_String: ...
    Id = property(get_Id, None)
    DisplayName = property(get_DisplayName, None)
    Publisher = property(get_Publisher, None)
    DisplayVersion = property(get_DisplayVersion, None)
class IInstalledDesktopAppStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Inventory.IInstalledDesktopAppStatics'
    _iid_ = Guid('{264cf74e-21cd-5f9b-6056-7866ad72489a}')
    @winrt_commethod(6)
    def GetInventoryAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.System.Inventory.InstalledDesktopApp]]: ...
class InstalledDesktopApp(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.Inventory.IInstalledDesktopApp
    _classid_ = 'Windows.System.Inventory.InstalledDesktopApp'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.System.Inventory.IInstalledDesktopApp) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.System.Inventory.IInstalledDesktopApp) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Publisher(self: win32more.Windows.System.Inventory.IInstalledDesktopApp) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayVersion(self: win32more.Windows.System.Inventory.IInstalledDesktopApp) -> WinRT_String: ...
    @winrt_mixinmethod
    def ToString(self: win32more.Windows.Foundation.IStringable) -> WinRT_String: ...
    @winrt_classmethod
    def GetInventoryAsync(cls: win32more.Windows.System.Inventory.IInstalledDesktopAppStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.System.Inventory.InstalledDesktopApp]]: ...
    Id = property(get_Id, None)
    DisplayName = property(get_DisplayName, None)
    Publisher = property(get_Publisher, None)
    DisplayVersion = property(get_DisplayVersion, None)
make_head(_module, 'IInstalledDesktopApp')
make_head(_module, 'IInstalledDesktopAppStatics')
make_head(_module, 'InstalledDesktopApp')
