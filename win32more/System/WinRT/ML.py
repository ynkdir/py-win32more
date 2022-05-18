from win32more import *
import win32more.AI.MachineLearning.WinML
import win32more.Foundation
import win32more.Graphics.Direct3D12
import win32more.System.Com

def __getattr__(name):
    module = globals()
    try:
        f = module[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    module[name] = f()
    return module[name]
def __dir__():
    return __all__
def _define_ILearningModelOperatorProviderNative_head():
    class ILearningModelOperatorProviderNative(win32more.System.Com.IUnknown_head):
        Guid = Guid('1adaa23a-eb67-41f3-aad8-5d984e9bacd4')
    return ILearningModelOperatorProviderNative
def _define_ILearningModelOperatorProviderNative():
    ILearningModelOperatorProviderNative = win32more.System.WinRT.ML.ILearningModelOperatorProviderNative_head
    ILearningModelOperatorProviderNative.GetRegistry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.AI.MachineLearning.WinML.IMLOperatorRegistry_head), use_last_error=False)(3, 'GetRegistry', ((1, 'ppOperatorRegistry'),)))
    return ILearningModelOperatorProviderNative
def _define_ITensorNative_head():
    class ITensorNative(win32more.System.Com.IUnknown_head):
        Guid = Guid('52f547ef-5b03-49b5-82d6-565f1ee0dd49')
    return ITensorNative
def _define_ITensorNative():
    ITensorNative = win32more.System.WinRT.ML.ITensorNative_head
    ITensorNative.GetBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(c_char_p_no),POINTER(UInt32), use_last_error=False)(3, 'GetBuffer', ((1, 'value'),(1, 'capacity'),)))
    ITensorNative.GetD3D12Resource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D12.ID3D12Resource_head), use_last_error=False)(4, 'GetD3D12Resource', ((1, 'result'),)))
    return ITensorNative
def _define_ITensorStaticsNative_head():
    class ITensorStaticsNative(win32more.System.Com.IUnknown_head):
        Guid = Guid('39d055a4-66f6-4ebc-95d9-7a29ebe7690a')
    return ITensorStaticsNative
def _define_ITensorStaticsNative():
    ITensorStaticsNative = win32more.System.WinRT.ML.ITensorStaticsNative_head
    ITensorStaticsNative.CreateFromD3D12Resource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D12.ID3D12Resource_head,POINTER(Int64),Int32,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(3, 'CreateFromD3D12Resource', ((1, 'value'),(1, 'shape'),(1, 'shapeCount'),(1, 'result'),)))
    return ITensorStaticsNative
def _define_ILearningModelDeviceFactoryNative_head():
    class ILearningModelDeviceFactoryNative(win32more.System.Com.IUnknown_head):
        Guid = Guid('1e9b31a1-662e-4ae0-af67-f63bb337e634')
    return ILearningModelDeviceFactoryNative
def _define_ILearningModelDeviceFactoryNative():
    ILearningModelDeviceFactoryNative = win32more.System.WinRT.ML.ILearningModelDeviceFactoryNative_head
    ILearningModelDeviceFactoryNative.CreateFromD3D12CommandQueue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D12.ID3D12CommandQueue_head,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(3, 'CreateFromD3D12CommandQueue', ((1, 'value'),(1, 'result'),)))
    return ILearningModelDeviceFactoryNative
def _define_ILearningModelSessionOptionsNative_head():
    class ILearningModelSessionOptionsNative(win32more.System.Com.IUnknown_head):
        Guid = Guid('c71e953f-37b4-4564-8658-d8396866db0d')
    return ILearningModelSessionOptionsNative
def _define_ILearningModelSessionOptionsNative():
    ILearningModelSessionOptionsNative = win32more.System.WinRT.ML.ILearningModelSessionOptionsNative_head
    ILearningModelSessionOptionsNative.SetIntraOpNumThreadsOverride = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(3, 'SetIntraOpNumThreadsOverride', ((1, 'intraOpNumThreads'),)))
    return ILearningModelSessionOptionsNative
__all__ = [
    "ILearningModelOperatorProviderNative",
    "ITensorNative",
    "ITensorStaticsNative",
    "ILearningModelDeviceFactoryNative",
    "ILearningModelSessionOptionsNative",
]
