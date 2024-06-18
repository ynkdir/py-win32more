from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.AI.MachineLearning.WinML
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Direct3D12
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT.ML
class ILearningModelDeviceFactoryNative(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1e9b31a1-662e-4ae0-af67-f63bb337e634}')
    @commethod(3)
    def CreateFromD3D12CommandQueue(self, value: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12CommandQueue, result: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ILearningModelOperatorProviderNative(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1adaa23a-eb67-41f3-aad8-5d984e9bacd4}')
    @commethod(3)
    def GetRegistry(self, ppOperatorRegistry: POINTER(win32more.Windows.Win32.AI.MachineLearning.WinML.IMLOperatorRegistry)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ILearningModelSessionOptionsNative(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c71e953f-37b4-4564-8658-d8396866db0d}')
    @commethod(3)
    def SetIntraOpNumThreadsOverride(self, intraOpNumThreads: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ILearningModelSessionOptionsNative1(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5da37a26-0526-414b-91e4-2a0fa3ddba40}')
    @commethod(3)
    def SetIntraOpThreadSpinning(self, allowSpinning: Byte) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITensorNative(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{52f547ef-5b03-49b5-82d6-565f1ee0dd49}')
    @commethod(3)
    def GetBuffer(self, value: POINTER(POINTER(Byte)), capacity: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetD3D12Resource(self, result: POINTER(win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Resource)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITensorStaticsNative(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{39d055a4-66f6-4ebc-95d9-7a29ebe7690a}')
    @commethod(3)
    def CreateFromD3D12Resource(self, value: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Resource, shape: POINTER(Int64), shapeCount: Int32, result: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...


make_ready(__name__)
