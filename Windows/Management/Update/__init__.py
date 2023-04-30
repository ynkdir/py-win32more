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
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Management.Update
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IPreviewBuildsManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('fa07dd61-7e4f-59f7-7c-9f-de-f9-05-1c-5f-62')
    @winrt_commethod(6)
    def get_ArePreviewBuildsAllowed(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_ArePreviewBuildsAllowed(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def GetCurrentState(self) -> Windows.Management.Update.PreviewBuildsState: ...
    @winrt_commethod(9)
    def SyncAsync(self) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    ArePreviewBuildsAllowed = property(get_ArePreviewBuildsAllowed, put_ArePreviewBuildsAllowed)
class IPreviewBuildsManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('3e422887-b112-5a70-7d-a1-97-d7-8d-32-aa-29')
    @winrt_commethod(6)
    def GetDefault(self) -> Windows.Management.Update.PreviewBuildsManager: ...
    @winrt_commethod(7)
    def IsSupported(self) -> Boolean: ...
class IPreviewBuildsState(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('a2f2903e-b223-5f63-75-46-3e-8e-ac-07-0a-2e')
    @winrt_commethod(6)
    def get_Properties(self) -> Windows.Foundation.Collections.ValueSet: ...
    Properties = property(get_Properties, None)
class PreviewBuildsManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Update.PreviewBuildsManager'
    @winrt_mixinmethod
    def get_ArePreviewBuildsAllowed(self: Windows.Management.Update.IPreviewBuildsManager) -> Boolean: ...
    @winrt_mixinmethod
    def put_ArePreviewBuildsAllowed(self: Windows.Management.Update.IPreviewBuildsManager, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def GetCurrentState(self: Windows.Management.Update.IPreviewBuildsManager) -> Windows.Management.Update.PreviewBuildsState: ...
    @winrt_mixinmethod
    def SyncAsync(self: Windows.Management.Update.IPreviewBuildsManager) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.Management.Update.IPreviewBuildsManagerStatics) -> Windows.Management.Update.PreviewBuildsManager: ...
    @winrt_classmethod
    def IsSupported(cls: Windows.Management.Update.IPreviewBuildsManagerStatics) -> Boolean: ...
    ArePreviewBuildsAllowed = property(get_ArePreviewBuildsAllowed, put_ArePreviewBuildsAllowed)
class PreviewBuildsState(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Update.PreviewBuildsState'
    @winrt_mixinmethod
    def get_Properties(self: Windows.Management.Update.IPreviewBuildsState) -> Windows.Foundation.Collections.ValueSet: ...
    Properties = property(get_Properties, None)
make_head(_module, 'IPreviewBuildsManager')
make_head(_module, 'IPreviewBuildsManagerStatics')
make_head(_module, 'IPreviewBuildsState')
make_head(_module, 'PreviewBuildsManager')
make_head(_module, 'PreviewBuildsState')
