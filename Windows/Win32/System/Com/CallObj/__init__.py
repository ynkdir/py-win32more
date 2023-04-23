from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.Foundation
import Windows.Win32.System.Com
import Windows.Win32.System.Com.CallObj
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
def CoGetInterceptor(iidIntercepted: POINTER(Guid), punkOuter: Windows.Win32.System.Com.IUnknown_head, iid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def CoGetInterceptorFromTypeInfo(iidIntercepted: POINTER(Guid), punkOuter: Windows.Win32.System.Com.IUnknown_head, typeInfo: Windows.Win32.System.Com.ITypeInfo_head, iid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
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
    pvDestContext: c_void_p
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
class ICallFrame(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d573b4b0-894e-11d2-b8-b6-00-c0-4f-b9-61-8a')
    @commethod(3)
    def GetInfo(self, pInfo: POINTER(Windows.Win32.System.Com.CallObj.CALLFRAMEINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetIIDAndMethod(self, pIID: POINTER(Guid), piMethod: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetNames(self, pwszInterface: POINTER(Windows.Win32.Foundation.PWSTR), pwszMethod: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetStackLocation(self) -> c_void_p: ...
    @commethod(7)
    def SetStackLocation(self, pvStack: c_void_p) -> Void: ...
    @commethod(8)
    def SetReturnValue(self, hr: Windows.Win32.Foundation.HRESULT) -> Void: ...
    @commethod(9)
    def GetReturnValue(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetParamInfo(self, iparam: UInt32, pInfo: POINTER(Windows.Win32.System.Com.CallObj.CALLFRAMEPARAMINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetParam(self, iparam: UInt32, pvar: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetParam(self, iparam: UInt32, pvar: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
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
    def Marshal(self, pmshlContext: POINTER(Windows.Win32.System.Com.CallObj.CALLFRAME_MARSHALCONTEXT_head), mshlflags: Windows.Win32.System.Com.MSHLFLAGS, pBuffer: c_void_p, cbBuffer: UInt32, pcbBufferUsed: POINTER(UInt32), pdataRep: POINTER(UInt32), prpcFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def Unmarshal(self, pBuffer: c_void_p, cbBuffer: UInt32, dataRep: UInt32, pcontext: POINTER(Windows.Win32.System.Com.CallObj.CALLFRAME_MARSHALCONTEXT_head), pcbUnmarshalled: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def ReleaseMarshalData(self, pBuffer: c_void_p, cbBuffer: UInt32, ibFirstRelease: UInt32, dataRep: UInt32, pcontext: POINTER(Windows.Win32.System.Com.CallObj.CALLFRAME_MARSHALCONTEXT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def Invoke(self, pvReceiver: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
class ICallFrameEvents(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('fd5e0843-fc91-11d0-97-d7-00-c0-4f-b9-61-8a')
    @commethod(3)
    def OnCall(self, pFrame: Windows.Win32.System.Com.CallObj.ICallFrame_head) -> Windows.Win32.Foundation.HRESULT: ...
class ICallFrameWalker(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('08b23919-392d-11d2-b8-a4-00-c0-4f-b9-61-8a')
    @commethod(3)
    def OnWalkInterface(self, iid: POINTER(Guid), ppvInterface: POINTER(c_void_p), fIn: Windows.Win32.Foundation.BOOL, fOut: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class ICallIndirect(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d573b4b1-894e-11d2-b8-b6-00-c0-4f-b9-61-8a')
    @commethod(3)
    def CallIndirect(self, phrReturn: POINTER(Windows.Win32.Foundation.HRESULT), iMethod: UInt32, pvArgs: c_void_p, cbArgs: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMethodInfo(self, iMethod: UInt32, pInfo: POINTER(Windows.Win32.System.Com.CallObj.CALLFRAMEINFO_head), pwszMethod: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetStackSize(self, iMethod: UInt32, cbArgs: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetIID(self, piid: POINTER(Guid), pfDerivesFromIDispatch: POINTER(Windows.Win32.Foundation.BOOL), pcMethod: POINTER(UInt32), pwszInterface: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class ICallInterceptor(c_void_p):
    extends: Windows.Win32.System.Com.CallObj.ICallIndirect
    Guid = Guid('60c7ca75-896d-11d2-b8-b6-00-c0-4f-b9-61-8a')
    @commethod(7)
    def RegisterSink(self, psink: Windows.Win32.System.Com.CallObj.ICallFrameEvents_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetRegisteredSink(self, ppsink: POINTER(Windows.Win32.System.Com.CallObj.ICallFrameEvents_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ICallUnmarshal(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('5333b003-2e42-11d2-b8-9d-00-c0-4f-b9-61-8a')
    @commethod(3)
    def Unmarshal(self, iMethod: UInt32, pBuffer: c_void_p, cbBuffer: UInt32, fForceBufferCopy: Windows.Win32.Foundation.BOOL, dataRep: UInt32, pcontext: POINTER(Windows.Win32.System.Com.CallObj.CALLFRAME_MARSHALCONTEXT_head), pcbUnmarshalled: POINTER(UInt32), ppFrame: POINTER(Windows.Win32.System.Com.CallObj.ICallFrame_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ReleaseMarshalData(self, iMethod: UInt32, pBuffer: c_void_p, cbBuffer: UInt32, ibFirstRelease: UInt32, dataRep: UInt32, pcontext: POINTER(Windows.Win32.System.Com.CallObj.CALLFRAME_MARSHALCONTEXT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IInterfaceRelated(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d1fb5a79-7706-11d1-ad-ba-00-c0-4f-c2-ad-c0')
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
