from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.System.Com
import win32more.System.Com.CallObj
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
@winfunctype('ole32.dll')
def CoGetInterceptor(iidIntercepted: POINTER(Guid), punkOuter: win32more.System.Com.IUnknown_head, iid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def CoGetInterceptorFromTypeInfo(iidIntercepted: POINTER(Guid), punkOuter: win32more.System.Com.IUnknown_head, typeInfo: win32more.System.Com.ITypeInfo_head, iid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
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
class CALLFRAME_MARSHALCONTEXT(Structure):
    fIn: win32more.Foundation.BOOLEAN
    dwDestContext: UInt32
    pvDestContext: c_void_p
    punkReserved: win32more.System.Com.IUnknown_head
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
class CALLFRAMEINFO(Structure):
    iMethod: UInt32
    fHasInValues: win32more.Foundation.BOOL
    fHasInOutValues: win32more.Foundation.BOOL
    fHasOutValues: win32more.Foundation.BOOL
    fDerivesFromIDispatch: win32more.Foundation.BOOL
    cInInterfacesMax: Int32
    cInOutInterfacesMax: Int32
    cOutInterfacesMax: Int32
    cTopLevelInInterfaces: Int32
    iid: Guid
    cMethod: UInt32
    cParams: UInt32
class CALLFRAMEPARAMINFO(Structure):
    fIn: win32more.Foundation.BOOLEAN
    fOut: win32more.Foundation.BOOLEAN
    stackOffset: UInt32
    cbParam: UInt32
class ICallFrame(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('d573b4b0-894e-11d2-b8-b6-00-c0-4f-b9-61-8a')
    @commethod(3)
    def GetInfo(pInfo: POINTER(win32more.System.Com.CallObj.CALLFRAMEINFO_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetIIDAndMethod(pIID: POINTER(Guid), piMethod: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetNames(pwszInterface: POINTER(win32more.Foundation.PWSTR), pwszMethod: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetStackLocation() -> c_void_p: ...
    @commethod(7)
    def SetStackLocation(pvStack: c_void_p) -> Void: ...
    @commethod(8)
    def SetReturnValue(hr: win32more.Foundation.HRESULT) -> Void: ...
    @commethod(9)
    def GetReturnValue() -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetParamInfo(iparam: UInt32, pInfo: POINTER(win32more.System.Com.CallObj.CALLFRAMEPARAMINFO_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def SetParam(iparam: UInt32, pvar: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetParam(iparam: UInt32, pvar: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def Copy(copyControl: win32more.System.Com.CallObj.CALLFRAME_COPY, pWalker: win32more.System.Com.CallObj.ICallFrameWalker_head, ppFrame: POINTER(win32more.System.Com.CallObj.ICallFrame_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def Free(pframeArgsDest: win32more.System.Com.CallObj.ICallFrame_head, pWalkerDestFree: win32more.System.Com.CallObj.ICallFrameWalker_head, pWalkerCopy: win32more.System.Com.CallObj.ICallFrameWalker_head, freeFlags: UInt32, pWalkerFree: win32more.System.Com.CallObj.ICallFrameWalker_head, nullFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def FreeParam(iparam: UInt32, freeFlags: UInt32, pWalkerFree: win32more.System.Com.CallObj.ICallFrameWalker_head, nullFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def WalkFrame(walkWhat: UInt32, pWalker: win32more.System.Com.CallObj.ICallFrameWalker_head) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def GetMarshalSizeMax(pmshlContext: POINTER(win32more.System.Com.CallObj.CALLFRAME_MARSHALCONTEXT_head), mshlflags: win32more.System.Com.MSHLFLAGS, pcbBufferNeeded: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def Marshal(pmshlContext: POINTER(win32more.System.Com.CallObj.CALLFRAME_MARSHALCONTEXT_head), mshlflags: win32more.System.Com.MSHLFLAGS, pBuffer: c_void_p, cbBuffer: UInt32, pcbBufferUsed: POINTER(UInt32), pdataRep: POINTER(UInt32), prpcFlags: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def Unmarshal(pBuffer: c_void_p, cbBuffer: UInt32, dataRep: UInt32, pcontext: POINTER(win32more.System.Com.CallObj.CALLFRAME_MARSHALCONTEXT_head), pcbUnmarshalled: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def ReleaseMarshalData(pBuffer: c_void_p, cbBuffer: UInt32, ibFirstRelease: UInt32, dataRep: UInt32, pcontext: POINTER(win32more.System.Com.CallObj.CALLFRAME_MARSHALCONTEXT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def Invoke(pvReceiver: c_void_p) -> win32more.Foundation.HRESULT: ...
class ICallFrameEvents(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('fd5e0843-fc91-11d0-97-d7-00-c0-4f-b9-61-8a')
    @commethod(3)
    def OnCall(pFrame: win32more.System.Com.CallObj.ICallFrame_head) -> win32more.Foundation.HRESULT: ...
class ICallFrameWalker(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('08b23919-392d-11d2-b8-a4-00-c0-4f-b9-61-8a')
    @commethod(3)
    def OnWalkInterface(iid: POINTER(Guid), ppvInterface: POINTER(c_void_p), fIn: win32more.Foundation.BOOL, fOut: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
class ICallIndirect(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('d573b4b1-894e-11d2-b8-b6-00-c0-4f-b9-61-8a')
    @commethod(3)
    def CallIndirect(phrReturn: POINTER(win32more.Foundation.HRESULT), iMethod: UInt32, pvArgs: c_void_p, cbArgs: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetMethodInfo(iMethod: UInt32, pInfo: POINTER(win32more.System.Com.CallObj.CALLFRAMEINFO_head), pwszMethod: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetStackSize(iMethod: UInt32, cbArgs: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetIID(piid: POINTER(Guid), pfDerivesFromIDispatch: POINTER(win32more.Foundation.BOOL), pcMethod: POINTER(UInt32), pwszInterface: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
class ICallInterceptor(c_void_p):
    extends: win32more.System.Com.CallObj.ICallIndirect
    Guid = Guid('60c7ca75-896d-11d2-b8-b6-00-c0-4f-b9-61-8a')
    @commethod(7)
    def RegisterSink(psink: win32more.System.Com.CallObj.ICallFrameEvents_head) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetRegisteredSink(ppsink: POINTER(win32more.System.Com.CallObj.ICallFrameEvents_head)) -> win32more.Foundation.HRESULT: ...
class ICallUnmarshal(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('5333b003-2e42-11d2-b8-9d-00-c0-4f-b9-61-8a')
    @commethod(3)
    def Unmarshal(iMethod: UInt32, pBuffer: c_void_p, cbBuffer: UInt32, fForceBufferCopy: win32more.Foundation.BOOL, dataRep: UInt32, pcontext: POINTER(win32more.System.Com.CallObj.CALLFRAME_MARSHALCONTEXT_head), pcbUnmarshalled: POINTER(UInt32), ppFrame: POINTER(win32more.System.Com.CallObj.ICallFrame_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def ReleaseMarshalData(iMethod: UInt32, pBuffer: c_void_p, cbBuffer: UInt32, ibFirstRelease: UInt32, dataRep: UInt32, pcontext: POINTER(win32more.System.Com.CallObj.CALLFRAME_MARSHALCONTEXT_head)) -> win32more.Foundation.HRESULT: ...
class IInterfaceRelated(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('d1fb5a79-7706-11d1-ad-ba-00-c0-4f-c2-ad-c0')
    @commethod(3)
    def SetIID(iid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetIID(piid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
make_head(_module, 'CALLFRAME_MARSHALCONTEXT')
make_head(_module, 'CALLFRAMEINFO')
make_head(_module, 'CALLFRAMEPARAMINFO')
make_head(_module, 'ICallFrame')
make_head(_module, 'ICallFrameEvents')
make_head(_module, 'ICallFrameWalker')
make_head(_module, 'ICallIndirect')
make_head(_module, 'ICallInterceptor')
make_head(_module, 'ICallUnmarshal')
make_head(_module, 'IInterfaceRelated')
__all__ = [
    "CALLFRAMEINFO",
    "CALLFRAMEPARAMINFO",
    "CALLFRAME_COPY",
    "CALLFRAME_COPY_INDEPENDENT",
    "CALLFRAME_COPY_NESTED",
    "CALLFRAME_FREE",
    "CALLFRAME_FREE_ALL",
    "CALLFRAME_FREE_IN",
    "CALLFRAME_FREE_INOUT",
    "CALLFRAME_FREE_NONE",
    "CALLFRAME_FREE_OUT",
    "CALLFRAME_FREE_TOP_INOUT",
    "CALLFRAME_FREE_TOP_OUT",
    "CALLFRAME_MARSHALCONTEXT",
    "CALLFRAME_NULL",
    "CALLFRAME_NULL_ALL",
    "CALLFRAME_NULL_INOUT",
    "CALLFRAME_NULL_NONE",
    "CALLFRAME_NULL_OUT",
    "CALLFRAME_WALK",
    "CALLFRAME_WALK_IN",
    "CALLFRAME_WALK_INOUT",
    "CALLFRAME_WALK_OUT",
    "CoGetInterceptor",
    "CoGetInterceptorFromTypeInfo",
    "ICallFrame",
    "ICallFrameEvents",
    "ICallFrameWalker",
    "ICallIndirect",
    "ICallInterceptor",
    "ICallUnmarshal",
    "IInterfaceRelated",
]
