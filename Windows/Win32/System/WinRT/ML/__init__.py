from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.AI.MachineLearning.WinML
import Windows.Win32.Foundation
import Windows.Win32.Graphics.Direct3D12
import Windows.Win32.System.Com
import Windows.Win32.System.WinRT.ML
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class ILearningModelDeviceFactoryNative(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1e9b31a1-662e-4ae0-af-67-f6-3b-b3-37-e6-34')
    @commethod(3)
    def CreateFromD3D12CommandQueue(self, value: Windows.Win32.Graphics.Direct3D12.ID3D12CommandQueue_head, result: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ILearningModelOperatorProviderNative(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1adaa23a-eb67-41f3-aa-d8-5d-98-4e-9b-ac-d4')
    @commethod(3)
    def GetRegistry(self, ppOperatorRegistry: POINTER(Windows.Win32.AI.MachineLearning.WinML.IMLOperatorRegistry_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ILearningModelSessionOptionsNative(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c71e953f-37b4-4564-86-58-d8-39-68-66-db-0d')
    @commethod(3)
    def SetIntraOpNumThreadsOverride(self, intraOpNumThreads: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ILearningModelSessionOptionsNative1(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('5da37a26-0526-414b-91-e4-2a-0f-a3-dd-ba-40')
    @commethod(3)
    def SetIntraOpThreadSpinning(self, allowSpinning: Byte) -> Windows.Win32.Foundation.HRESULT: ...
class ITensorNative(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('52f547ef-5b03-49b5-82-d6-56-5f-1e-e0-dd-49')
    @commethod(3)
    def GetBuffer(self, value: POINTER(POINTER(Byte)), capacity: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetD3D12Resource(self, result: POINTER(Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ITensorStaticsNative(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('39d055a4-66f6-4ebc-95-d9-7a-29-eb-e7-69-0a')
    @commethod(3)
    def CreateFromD3D12Resource(self, value: Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head, shape: POINTER(Int64), shapeCount: Int32, result: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'ILearningModelDeviceFactoryNative')
make_head(_module, 'ILearningModelOperatorProviderNative')
make_head(_module, 'ILearningModelSessionOptionsNative')
make_head(_module, 'ILearningModelSessionOptionsNative1')
make_head(_module, 'ITensorNative')
make_head(_module, 'ITensorStaticsNative')
