from __future__ import annotations
from ctypes import POINTER
from Windows import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import Windows.Win32.Foundation
import Windows.Win32.System.Com
import Windows.Win32.System.Com.CallObj
import Windows.Win32.System.Variant
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
@winfunctype('ole32.dll')
def CoGetInterceptor(iidIntercepted: POINTER(Guid), punkOuter: Windows.Win32.System.Com.IUnknown_head, iid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def CoGetInterceptorFromTypeInfo(iidIntercepted: POINTER(Guid), punkOuter: Windows.Win32.System.Com.IUnknown_head, typeInfo: Windows.Win32.System.Com.ITypeInfo_head, iid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
class CALLFRAMEINFO(EasyCastStructure):
    iMethod: UInt32
    fHasInValues: Windows.Win32.Foundation.BOOL
    fHasInOutValues: Windows.Win32.Foundation.BOOL
    fHasOutValues: Windows.Win32.Foundation.BOOL
    fDerivesFromIDispatch: Windows.Win32.Foundation.BOOL
    cInInterfacesMax: Int32
    cInOutInterfacesMax: Int32
    cOutInterfacesMax: Int32
    cTopLevelInInterfaces: Int32
    iid: Guid
    cMethod: UInt32
    cParams: UInt32
class CALLFRAMEPARAMINFO(EasyCastStructure):
    fIn: Windows.Win32.Foundation.BOOLEAN
    fOut: Windows.Win32.Foundation.BOOLEAN
    stackOffset: UInt32
    cbParam: UInt32
CALLFRAME_COPY = Int32
CALLFRAME_COPY_NESTED: CALLFRAME_COPY = 1
CALLFRAME_COPY_INDEPENDENT: CALLFRAME_COPY = 2
CALLFRAME_FREE = Int32
CALLFRAME_FREE_NONE: CALLFRAME_FREE = 0
CALLFRAME_FREE_IN: CALLFRAME_FREE = 1
CALLFRAME_FREE_INOUT: CALLFRAME_FREE = 2
CALLFRAME_FREE_OUT: CALLFRAME_FREE = 4
CALLFRAME_FREE_TOP_INOUT: CALLFRAME_FREE = 8
CALLFRAME_FREE_TOP_OUT: CALLFRAME_FREE = 16
CALLFRAME_FREE_ALL: CALLFRAME_FREE = 31
class CALLFRAME_MARSHALCONTEXT(EasyCastStructure):
    fIn: Windows.Win32.Foundation.BOOLEAN
    dwDestContext: UInt32
    pvDestContext: VoidPtr
    punkReserved: Windows.Win32.System.Com.IUnknown_head
    guidTransferSyntax: Guid
CALLFRAME_NULL = Int32
CALLFRAME_NULL_NONE: CALLFRAME_NULL = 0
CALLFRAME_NULL_INOUT: CALLFRAME_NULL = 2
CALLFRAME_NULL_OUT: CALLFRAME_NULL = 4
CALLFRAME_NULL_ALL: CALLFRAME_NULL = 6
CALLFRAME_WALK = Int32
CALLFRAME_WALK_IN: CALLFRAME_WALK = 1
CALLFRAME_WALK_INOUT: CALLFRAME_WALK = 2
CALLFRAME_WALK_OUT: CALLFRAME_WALK = 4
class ICallFrame(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d573b4b0-894e-11d2-b8b6-00c04fb9618a}')
    @commethod(3)
    def GetInfo(self, pInfo: POINTER(Windows.Win32.System.Com.CallObj.CALLFRAMEINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetIIDAndMethod(self, pIID: POINTER(Guid), piMethod: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetNames(self, pwszInterface: POINTER(Windows.Win32.Foundation.PWSTR), pwszMethod: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetStackLocation(self) -> VoidPtr: ...
    @commethod(7)
    def SetStackLocation(self, pvStack: VoidPtr) -> Void: ...
    @commethod(8)
    def SetReturnValue(self, hr: Windows.Win32.Foundation.HRESULT) -> Void: ...
    @commethod(9)
    def GetReturnValue(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetParamInfo(self, iparam: UInt32, pInfo: POINTER(Windows.Win32.System.Com.CallObj.CALLFRAMEPARAMINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetParam(self, iparam: UInt32, pvar: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetParam(self, iparam: UInt32, pvar: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Copy(self, copyControl: Windows.Win32.System.Com.CallObj.CALLFRAME_COPY, pWalker: Windows.Win32.System.Com.CallObj.ICallFrameWalker_head, ppFrame: POINTER(Windows.Win32.System.Com.CallObj.ICallFrame_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def Free(self, pframeArgsDest: Windows.Win32.System.Com.CallObj.ICallFrame_head, pWalkerDestFree: Windows.Win32.System.Com.CallObj.ICallFrameWalker_head, pWalkerCopy: Windows.Win32.System.Com.CallObj.ICallFrameWalker_head, freeFlags: UInt32, pWalkerFree: Windows.Win32.System.Com.CallObj.ICallFrameWalker_head, nullFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def FreeParam(self, iparam: UInt32, freeFlags: UInt32, pWalkerFree: Windows.Win32.System.Com.CallObj.ICallFrameWalker_head, nullFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def WalkFrame(self, walkWhat: UInt32, pWalker: Windows.Win32.System.Com.CallObj.ICallFrameWalker_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetMarshalSizeMax(self, pmshlContext: POINTER(Windows.Win32.System.Com.CallObj.CALLFRAME_MARSHALCONTEXT_head), mshlflags: Windows.Win32.System.Com.MSHLFLAGS, pcbBufferNeeded: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def Marshal(self, pmshlContext: POINTER(Windows.Win32.System.Com.CallObj.CALLFRAME_MARSHALCONTEXT_head), mshlflags: Windows.Win32.System.Com.MSHLFLAGS, pBuffer: VoidPtr, cbBuffer: UInt32, pcbBufferUsed: POINTER(UInt32), pdataRep: POINTER(UInt32), prpcFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def Unmarshal(self, pBuffer: VoidPtr, cbBuffer: UInt32, dataRep: UInt32, pcontext: POINTER(Windows.Win32.System.Com.CallObj.CALLFRAME_MARSHALCONTEXT_head), pcbUnmarshalled: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def ReleaseMarshalData(self, pBuffer: VoidPtr, cbBuffer: UInt32, ibFirstRelease: UInt32, dataRep: UInt32, pcontext: POINTER(Windows.Win32.System.Com.CallObj.CALLFRAME_MARSHALCONTEXT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def Invoke(self, pvReceiver: VoidPtr) -> Windows.Win32.Foundation.HRESULT: ...
class ICallFrameEvents(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fd5e0843-fc91-11d0-97d7-00c04fb9618a}')
    @commethod(3)
    def OnCall(self, pFrame: Windows.Win32.System.Com.CallObj.ICallFrame_head) -> Windows.Win32.Foundation.HRESULT: ...
class ICallFrameWalker(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{08b23919-392d-11d2-b8a4-00c04fb9618a}')
    @commethod(3)
    def OnWalkInterface(self, iid: POINTER(Guid), ppvInterface: POINTER(VoidPtr), fIn: Windows.Win32.Foundation.BOOL, fOut: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class ICallIndirect(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d573b4b1-894e-11d2-b8b6-00c04fb9618a}')
    @commethod(3)
    def CallIndirect(self, phrReturn: POINTER(Windows.Win32.Foundation.HRESULT), iMethod: UInt32, pvArgs: VoidPtr, cbArgs: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMethodInfo(self, iMethod: UInt32, pInfo: POINTER(Windows.Win32.System.Com.CallObj.CALLFRAMEINFO_head), pwszMethod: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetStackSize(self, iMethod: UInt32, cbArgs: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetIID(self, piid: POINTER(Guid), pfDerivesFromIDispatch: POINTER(Windows.Win32.Foundation.BOOL), pcMethod: POINTER(UInt32), pwszInterface: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class ICallInterceptor(ComPtr):
    extends: Windows.Win32.System.Com.CallObj.ICallIndirect
    _iid_ = Guid('{60c7ca75-896d-11d2-b8b6-00c04fb9618a}')
    @commethod(7)
    def RegisterSink(self, psink: Windows.Win32.System.Com.CallObj.ICallFrameEvents_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetRegisteredSink(self, ppsink: POINTER(Windows.Win32.System.Com.CallObj.ICallFrameEvents_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ICallUnmarshal(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5333b003-2e42-11d2-b89d-00c04fb9618a}')
    @commethod(3)
    def Unmarshal(self, iMethod: UInt32, pBuffer: VoidPtr, cbBuffer: UInt32, fForceBufferCopy: Windows.Win32.Foundation.BOOL, dataRep: UInt32, pcontext: POINTER(Windows.Win32.System.Com.CallObj.CALLFRAME_MARSHALCONTEXT_head), pcbUnmarshalled: POINTER(UInt32), ppFrame: POINTER(Windows.Win32.System.Com.CallObj.ICallFrame_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ReleaseMarshalData(self, iMethod: UInt32, pBuffer: VoidPtr, cbBuffer: UInt32, ibFirstRelease: UInt32, dataRep: UInt32, pcontext: POINTER(Windows.Win32.System.Com.CallObj.CALLFRAME_MARSHALCONTEXT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IInterfaceRelated(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d1fb5a79-7706-11d1-adba-00c04fc2adc0}')
    @commethod(3)
    def SetIID(self, iid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetIID(self, piid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'CALLFRAMEINFO')
make_head(_module, 'CALLFRAMEPARAMINFO')
make_head(_module, 'CALLFRAME_MARSHALCONTEXT')
make_head(_module, 'ICallFrame')
make_head(_module, 'ICallFrameEvents')
make_head(_module, 'ICallFrameWalker')
make_head(_module, 'ICallIndirect')
make_head(_module, 'ICallInterceptor')
make_head(_module, 'ICallUnmarshal')
make_head(_module, 'IInterfaceRelated')
