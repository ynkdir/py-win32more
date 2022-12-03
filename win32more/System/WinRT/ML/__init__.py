from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.AI.MachineLearning.WinML
import win32more.Foundation
import win32more.Graphics.Direct3D12
import win32more.System.Com
import win32more.System.WinRT.ML
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
def _define_ILearningModelDeviceFactoryNative_head():
    class ILearningModelDeviceFactoryNative(win32more.System.Com.IUnknown_head):
        Guid = Guid('1e9b31a1-662e-4ae0-af-67-f6-3b-b3-37-e6-34')
    return ILearningModelDeviceFactoryNative
def _define_ILearningModelDeviceFactoryNative():
    ILearningModelDeviceFactoryNative = win32more.System.WinRT.ML.ILearningModelDeviceFactoryNative_head
    ILearningModelDeviceFactoryNative.CreateFromD3D12CommandQueue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D12.ID3D12CommandQueue_head,POINTER(win32more.System.Com.IUnknown_head))(3, 'CreateFromD3D12CommandQueue', ((1, 'value'),(1, 'result'),)))
    win32more.System.Com.IUnknown
    return ILearningModelDeviceFactoryNative
def _define_ILearningModelOperatorProviderNative_head():
    class ILearningModelOperatorProviderNative(win32more.System.Com.IUnknown_head):
        Guid = Guid('1adaa23a-eb67-41f3-aa-d8-5d-98-4e-9b-ac-d4')
    return ILearningModelOperatorProviderNative
def _define_ILearningModelOperatorProviderNative():
    ILearningModelOperatorProviderNative = win32more.System.WinRT.ML.ILearningModelOperatorProviderNative_head
    ILearningModelOperatorProviderNative.GetRegistry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.AI.MachineLearning.WinML.IMLOperatorRegistry_head))(3, 'GetRegistry', ((1, 'ppOperatorRegistry'),)))
    win32more.System.Com.IUnknown
    return ILearningModelOperatorProviderNative
def _define_ILearningModelSessionOptionsNative_head():
    class ILearningModelSessionOptionsNative(win32more.System.Com.IUnknown_head):
        Guid = Guid('c71e953f-37b4-4564-86-58-d8-39-68-66-db-0d')
    return ILearningModelSessionOptionsNative
def _define_ILearningModelSessionOptionsNative():
    ILearningModelSessionOptionsNative = win32more.System.WinRT.ML.ILearningModelSessionOptionsNative_head
    ILearningModelSessionOptionsNative.SetIntraOpNumThreadsOverride = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(3, 'SetIntraOpNumThreadsOverride', ((1, 'intraOpNumThreads'),)))
    win32more.System.Com.IUnknown
    return ILearningModelSessionOptionsNative
def _define_ITensorNative_head():
    class ITensorNative(win32more.System.Com.IUnknown_head):
        Guid = Guid('52f547ef-5b03-49b5-82-d6-56-5f-1e-e0-dd-49')
    return ITensorNative
def _define_ITensorNative():
    ITensorNative = win32more.System.WinRT.ML.ITensorNative_head
    ITensorNative.GetBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(c_char_p_no),POINTER(UInt32))(3, 'GetBuffer', ((1, 'value'),(1, 'capacity'),)))
    ITensorNative.GetD3D12Resource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D12.ID3D12Resource_head))(4, 'GetD3D12Resource', ((1, 'result'),)))
    win32more.System.Com.IUnknown
    return ITensorNative
def _define_ITensorStaticsNative_head():
    class ITensorStaticsNative(win32more.System.Com.IUnknown_head):
        Guid = Guid('39d055a4-66f6-4ebc-95-d9-7a-29-eb-e7-69-0a')
    return ITensorStaticsNative
def _define_ITensorStaticsNative():
    ITensorStaticsNative = win32more.System.WinRT.ML.ITensorStaticsNative_head
    ITensorStaticsNative.CreateFromD3D12Resource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D12.ID3D12Resource_head,POINTER(Int64),Int32,POINTER(win32more.System.Com.IUnknown_head))(3, 'CreateFromD3D12Resource', ((1, 'value'),(1, 'shape'),(1, 'shapeCount'),(1, 'result'),)))
    win32more.System.Com.IUnknown
    return ITensorStaticsNative
__all__ = [
    "ILearningModelDeviceFactoryNative",
    "ILearningModelOperatorProviderNative",
    "ILearningModelSessionOptionsNative",
    "ITensorNative",
    "ITensorStaticsNative",
]
