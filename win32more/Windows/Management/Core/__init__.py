from __future__ import annotations
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
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, winrt_overload, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Management.Core
import win32more.Windows.Storage
class ApplicationDataManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Management.Core.IApplicationDataManager
    _classid_ = 'Windows.Management.Core.ApplicationDataManager'
    @winrt_classmethod
    def CreateForPackageFamily(cls: win32more.Windows.Management.Core.IApplicationDataManagerStatics, packageFamilyName: WinRT_String) -> win32more.Windows.Storage.ApplicationData: ...
class IApplicationDataManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Core.IApplicationDataManager'
    _iid_ = Guid('{74d10432-2e99-4000-9a3a-64307e858129}')
class IApplicationDataManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Core.IApplicationDataManagerStatics'
    _iid_ = Guid('{1e1862e3-698e-49a1-9752-dee94925b9b3}')
    @winrt_commethod(6)
    def CreateForPackageFamily(self, packageFamilyName: WinRT_String) -> win32more.Windows.Storage.ApplicationData: ...


make_ready(__name__)
