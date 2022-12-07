from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.AI.MachineLearning.WinML
import win32more.Foundation
import win32more.Graphics.Direct3D12
import win32more.System.Com
import win32more.System.WinRT.ML
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
class ILearningModelDeviceFactoryNative(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('1e9b31a1-662e-4ae0-af-67-f6-3b-b3-37-e6-34')
    @commethod(3)
    def CreateFromD3D12CommandQueue(value: win32more.Graphics.Direct3D12.ID3D12CommandQueue_head, result: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
class ILearningModelOperatorProviderNative(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('1adaa23a-eb67-41f3-aa-d8-5d-98-4e-9b-ac-d4')
    @commethod(3)
    def GetRegistry(ppOperatorRegistry: POINTER(win32more.AI.MachineLearning.WinML.IMLOperatorRegistry_head)) -> win32more.Foundation.HRESULT: ...
class ILearningModelSessionOptionsNative(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c71e953f-37b4-4564-86-58-d8-39-68-66-db-0d')
    @commethod(3)
    def SetIntraOpNumThreadsOverride(intraOpNumThreads: UInt32) -> win32more.Foundation.HRESULT: ...
class ITensorNative(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('52f547ef-5b03-49b5-82-d6-56-5f-1e-e0-dd-49')
    @commethod(3)
    def GetBuffer(value: POINTER(c_char_p_no), capacity: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetD3D12Resource(result: POINTER(win32more.Graphics.Direct3D12.ID3D12Resource_head)) -> win32more.Foundation.HRESULT: ...
class ITensorStaticsNative(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('39d055a4-66f6-4ebc-95-d9-7a-29-eb-e7-69-0a')
    @commethod(3)
    def CreateFromD3D12Resource(value: win32more.Graphics.Direct3D12.ID3D12Resource_head, shape: POINTER(Int64), shapeCount: Int32, result: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
make_head(_module, 'ILearningModelDeviceFactoryNative')
make_head(_module, 'ILearningModelOperatorProviderNative')
make_head(_module, 'ILearningModelSessionOptionsNative')
make_head(_module, 'ITensorNative')
make_head(_module, 'ITensorStaticsNative')
__all__ = [
    "ILearningModelDeviceFactoryNative",
    "ILearningModelOperatorProviderNative",
    "ILearningModelSessionOptionsNative",
    "ITensorNative",
    "ITensorStaticsNative",
]
