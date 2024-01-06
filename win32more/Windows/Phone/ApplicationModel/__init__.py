from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import Annotated, Generic, K, MulticastDelegate, SZArray, T, TProgress, TResult, TSender, V, WinRT_String, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Phone.ApplicationModel
import win32more.Windows.Win32.System.WinRT
class _ApplicationProfile_Meta_(ComPtr.__class__):
    pass
class ApplicationProfile(ComPtr, metaclass=_ApplicationProfile_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.ApplicationModel.ApplicationProfile'
    @winrt_classmethod
    def get_Modes(cls: win32more.Windows.Phone.ApplicationModel.IApplicationProfileStatics) -> win32more.Windows.Phone.ApplicationModel.ApplicationProfileModes: ...
    _ApplicationProfile_Meta_.Modes = property(get_Modes.__wrapped__, None)
class ApplicationProfileModes(UInt32):  # enum
    Default = 0
    Alternate = 1
class IApplicationProfileStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.ApplicationModel.IApplicationProfileStatics'
    _iid_ = Guid('{d5008ab4-7e7a-11e1-a7f2-b0a14824019b}')
    @winrt_commethod(6)
    def get_Modes(self) -> win32more.Windows.Phone.ApplicationModel.ApplicationProfileModes: ...
    Modes = property(get_Modes, None)


make_ready(__name__)
