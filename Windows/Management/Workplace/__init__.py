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
import Windows.Management.Workplace
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IMdmAllowPolicyStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c39709e7-741c-41f2-a4-b6-31-4c-31-50-25-86')
    @winrt_commethod(6)
    def IsBrowserAllowed(self) -> Boolean: ...
    @winrt_commethod(7)
    def IsCameraAllowed(self) -> Boolean: ...
    @winrt_commethod(8)
    def IsMicrosoftAccountAllowed(self) -> Boolean: ...
    @winrt_commethod(9)
    def IsStoreAllowed(self) -> Boolean: ...
class IMdmPolicyStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c99c7526-03d4-49f9-a9-93-43-ef-cc-d2-65-c4')
    @winrt_commethod(6)
    def GetMessagingSyncPolicy(self) -> Windows.Management.Workplace.MessagingSyncPolicy: ...
class MdmPolicy(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Management.Workplace.MdmPolicy'
    @winrt_classmethod
    def GetMessagingSyncPolicy(cls: Windows.Management.Workplace.IMdmPolicyStatics2) -> Windows.Management.Workplace.MessagingSyncPolicy: ...
    @winrt_classmethod
    def IsBrowserAllowed(cls: Windows.Management.Workplace.IMdmAllowPolicyStatics) -> Boolean: ...
    @winrt_classmethod
    def IsCameraAllowed(cls: Windows.Management.Workplace.IMdmAllowPolicyStatics) -> Boolean: ...
    @winrt_classmethod
    def IsMicrosoftAccountAllowed(cls: Windows.Management.Workplace.IMdmAllowPolicyStatics) -> Boolean: ...
    @winrt_classmethod
    def IsStoreAllowed(cls: Windows.Management.Workplace.IMdmAllowPolicyStatics) -> Boolean: ...
MessagingSyncPolicy = Int32
MessagingSyncPolicy_Disallowed: MessagingSyncPolicy = 0
MessagingSyncPolicy_Allowed: MessagingSyncPolicy = 1
MessagingSyncPolicy_Required: MessagingSyncPolicy = 2
make_head(_module, 'IMdmAllowPolicyStatics')
make_head(_module, 'IMdmPolicyStatics2')
make_head(_module, 'MdmPolicy')
