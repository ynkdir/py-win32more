from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
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
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, EasyCastStructure, EasyCastUnion, ComPtr, make_ready
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, winrt_overload, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Management.Workplace
class IMdmAllowPolicyStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Workplace.IMdmAllowPolicyStatics'
    _iid_ = Guid('{c39709e7-741c-41f2-a4b6-314c31502586}')
    @winrt_commethod(6)
    def IsBrowserAllowed(self) -> Boolean: ...
    @winrt_commethod(7)
    def IsCameraAllowed(self) -> Boolean: ...
    @winrt_commethod(8)
    def IsMicrosoftAccountAllowed(self) -> Boolean: ...
    @winrt_commethod(9)
    def IsStoreAllowed(self) -> Boolean: ...
class IMdmPolicyStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Workplace.IMdmPolicyStatics2'
    _iid_ = Guid('{c99c7526-03d4-49f9-a993-43efccd265c4}')
    @winrt_commethod(6)
    def GetMessagingSyncPolicy(self) -> win32more.Windows.Management.Workplace.MessagingSyncPolicy: ...
class IWorkplaceSettingsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Workplace.IWorkplaceSettingsStatics'
    _iid_ = Guid('{e4676ffd-2d92-4c08-bad4-f6590b54a6d3}')
    @winrt_commethod(6)
    def get_IsMicrosoftAccountOptional(self) -> Boolean: ...
    IsMicrosoftAccountOptional = property(get_IsMicrosoftAccountOptional, None)
class MdmPolicy(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Workplace.MdmPolicy'
    @winrt_classmethod
    def GetMessagingSyncPolicy(cls: win32more.Windows.Management.Workplace.IMdmPolicyStatics2) -> win32more.Windows.Management.Workplace.MessagingSyncPolicy: ...
    @winrt_classmethod
    def IsBrowserAllowed(cls: win32more.Windows.Management.Workplace.IMdmAllowPolicyStatics) -> Boolean: ...
    @winrt_classmethod
    def IsCameraAllowed(cls: win32more.Windows.Management.Workplace.IMdmAllowPolicyStatics) -> Boolean: ...
    @winrt_classmethod
    def IsMicrosoftAccountAllowed(cls: win32more.Windows.Management.Workplace.IMdmAllowPolicyStatics) -> Boolean: ...
    @winrt_classmethod
    def IsStoreAllowed(cls: win32more.Windows.Management.Workplace.IMdmAllowPolicyStatics) -> Boolean: ...
MessagingSyncPolicy = Int32
MessagingSyncPolicy_Disallowed: MessagingSyncPolicy = 0
MessagingSyncPolicy_Allowed: MessagingSyncPolicy = 1
MessagingSyncPolicy_Required: MessagingSyncPolicy = 2
class _WorkplaceSettings_Meta_(ComPtr.__class__):
    pass
class WorkplaceSettings(ComPtr, metaclass=_WorkplaceSettings_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Workplace.WorkplaceSettings'
    @winrt_classmethod
    def get_IsMicrosoftAccountOptional(cls: win32more.Windows.Management.Workplace.IWorkplaceSettingsStatics) -> Boolean: ...
    _WorkplaceSettings_Meta_.IsMicrosoftAccountOptional = property(get_IsMicrosoftAccountOptional.__wrapped__, None)
WorkplaceSettingsContract: UInt32 = 65536
make_ready(__name__)
