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
import win32more.Windows.Phone.ApplicationModel
class _ApplicationProfile_Meta_(ComPtr.__class__):
    pass
class ApplicationProfile(ComPtr, metaclass=_ApplicationProfile_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.ApplicationModel.ApplicationProfile'
    @winrt_classmethod
    def get_Modes(cls: win32more.Windows.Phone.ApplicationModel.IApplicationProfileStatics) -> win32more.Windows.Phone.ApplicationModel.ApplicationProfileModes: ...
    _ApplicationProfile_Meta_.Modes = property(get_Modes.__wrapped__, None)
ApplicationProfileModes = UInt32
ApplicationProfileModes_Default: ApplicationProfileModes = 0
ApplicationProfileModes_Alternate: ApplicationProfileModes = 1
class IApplicationProfileStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.ApplicationModel.IApplicationProfileStatics'
    _iid_ = Guid('{d5008ab4-7e7a-11e1-a7f2-b0a14824019b}')
    @winrt_commethod(6)
    def get_Modes(self) -> win32more.Windows.Phone.ApplicationModel.ApplicationProfileModes: ...
    Modes = property(get_Modes, None)


make_ready(__name__)
