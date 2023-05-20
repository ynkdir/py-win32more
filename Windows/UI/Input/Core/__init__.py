from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import Windows.Win32.System.WinRT
import Windows.ApplicationModel.Core
import Windows.System
import Windows.UI.Core
import Windows.UI.Input
import Windows.UI.Input.Core
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IRadialControllerIndependentInputSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Core.IRadialControllerIndependentInputSource'
    _iid_ = Guid('{3d577ef6-4cee-11e6-b535-001bdc06ab3b}')
    @winrt_commethod(6)
    def get_Controller(self) -> Windows.UI.Input.RadialController: ...
    @winrt_commethod(7)
    def get_Dispatcher(self) -> Windows.UI.Core.CoreDispatcher: ...
    Controller = property(get_Controller, None)
    Dispatcher = property(get_Dispatcher, None)
class IRadialControllerIndependentInputSource2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Core.IRadialControllerIndependentInputSource2'
    _iid_ = Guid('{7073aad8-35f3-4eeb-8751-be4d0a66faf4}')
    @winrt_commethod(6)
    def get_DispatcherQueue(self) -> Windows.System.DispatcherQueue: ...
    DispatcherQueue = property(get_DispatcherQueue, None)
class IRadialControllerIndependentInputSourceStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Core.IRadialControllerIndependentInputSourceStatics'
    _iid_ = Guid('{3d577ef5-4cee-11e6-b535-001bdc06ab3b}')
    @winrt_commethod(6)
    def CreateForView(self, view: Windows.ApplicationModel.Core.CoreApplicationView) -> Windows.UI.Input.Core.RadialControllerIndependentInputSource: ...
class RadialControllerIndependentInputSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Input.Core.IRadialControllerIndependentInputSource
    _classid_ = 'Windows.UI.Input.Core.RadialControllerIndependentInputSource'
    @winrt_mixinmethod
    def get_Controller(self: Windows.UI.Input.Core.IRadialControllerIndependentInputSource) -> Windows.UI.Input.RadialController: ...
    @winrt_mixinmethod
    def get_Dispatcher(self: Windows.UI.Input.Core.IRadialControllerIndependentInputSource) -> Windows.UI.Core.CoreDispatcher: ...
    @winrt_mixinmethod
    def get_DispatcherQueue(self: Windows.UI.Input.Core.IRadialControllerIndependentInputSource2) -> Windows.System.DispatcherQueue: ...
    @winrt_classmethod
    def CreateForView(cls: Windows.UI.Input.Core.IRadialControllerIndependentInputSourceStatics, view: Windows.ApplicationModel.Core.CoreApplicationView) -> Windows.UI.Input.Core.RadialControllerIndependentInputSource: ...
    Controller = property(get_Controller, None)
    Dispatcher = property(get_Dispatcher, None)
    DispatcherQueue = property(get_DispatcherQueue, None)
make_head(_module, 'IRadialControllerIndependentInputSource')
make_head(_module, 'IRadialControllerIndependentInputSource2')
make_head(_module, 'IRadialControllerIndependentInputSourceStatics')
make_head(_module, 'RadialControllerIndependentInputSource')
