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
import Windows.Management.Core
import Windows.Storage
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class ApplicationDataManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Management.Core.IApplicationDataManager
    _classid_ = 'Windows.Management.Core.ApplicationDataManager'
    @winrt_classmethod
    def CreateForPackageFamily(cls: Windows.Management.Core.IApplicationDataManagerStatics, packageFamilyName: WinRT_String) -> Windows.Storage.ApplicationData: ...
class IApplicationDataManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Core.IApplicationDataManager'
    _iid_ = Guid('{74d10432-2e99-4000-9a3a-64307e858129}')
class IApplicationDataManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Core.IApplicationDataManagerStatics'
    _iid_ = Guid('{1e1862e3-698e-49a1-9752-dee94925b9b3}')
    @winrt_commethod(6)
    def CreateForPackageFamily(self, packageFamilyName: WinRT_String) -> Windows.Storage.ApplicationData: ...
make_head(_module, 'ApplicationDataManager')
make_head(_module, 'IApplicationDataManager')
make_head(_module, 'IApplicationDataManagerStatics')
