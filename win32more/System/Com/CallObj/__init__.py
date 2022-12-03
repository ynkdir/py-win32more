from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.Com
import win32more.System.Com.CallObj
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
def _define_CoGetInterceptor():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IUnknown_head,POINTER(Guid),POINTER(c_void_p))(('CoGetInterceptor', windll['ole32.dll']), ((1, 'iidIntercepted'),(1, 'punkOuter'),(1, 'iid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoGetInterceptorFromTypeInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IUnknown_head,win32more.System.Com.ITypeInfo_head,POINTER(Guid),POINTER(c_void_p))(('CoGetInterceptorFromTypeInfo', windll['ole32.dll']), ((1, 'iidIntercepted'),(1, 'punkOuter'),(1, 'typeInfo'),(1, 'iid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
CALLFRAME_COPY = Int32
CALLFRAME_COPY_NESTED = 1
CALLFRAME_COPY_INDEPENDENT = 2
CALLFRAME_FREE = Int32
CALLFRAME_FREE_NONE = 0
CALLFRAME_FREE_IN = 1
CALLFRAME_FREE_INOUT = 2
CALLFRAME_FREE_OUT = 4
CALLFRAME_FREE_TOP_INOUT = 8
CALLFRAME_FREE_TOP_OUT = 16
CALLFRAME_FREE_ALL = 31
def _define_CALLFRAME_MARSHALCONTEXT_head():
    class CALLFRAME_MARSHALCONTEXT(Structure):
        pass
    return CALLFRAME_MARSHALCONTEXT
def _define_CALLFRAME_MARSHALCONTEXT():
    CALLFRAME_MARSHALCONTEXT = win32more.System.Com.CallObj.CALLFRAME_MARSHALCONTEXT_head
    CALLFRAME_MARSHALCONTEXT._fields_ = [
        ('fIn', win32more.Foundation.BOOLEAN),
        ('dwDestContext', UInt32),
        ('pvDestContext', c_void_p),
        ('punkReserved', win32more.System.Com.IUnknown_head),
        ('guidTransferSyntax', Guid),
    ]
    return CALLFRAME_MARSHALCONTEXT
CALLFRAME_NULL = Int32
CALLFRAME_NULL_NONE = 0
CALLFRAME_NULL_INOUT = 2
CALLFRAME_NULL_OUT = 4
CALLFRAME_NULL_ALL = 6
CALLFRAME_WALK = Int32
CALLFRAME_WALK_IN = 1
CALLFRAME_WALK_INOUT = 2
CALLFRAME_WALK_OUT = 4
def _define_CALLFRAMEINFO_head():
    class CALLFRAMEINFO(Structure):
        pass
    return CALLFRAMEINFO
def _define_CALLFRAMEINFO():
    CALLFRAMEINFO = win32more.System.Com.CallObj.CALLFRAMEINFO_head
    CALLFRAMEINFO._fields_ = [
        ('iMethod', UInt32),
        ('fHasInValues', win32more.Foundation.BOOL),
        ('fHasInOutValues', win32more.Foundation.BOOL),
        ('fHasOutValues', win32more.Foundation.BOOL),
        ('fDerivesFromIDispatch', win32more.Foundation.BOOL),
        ('cInInterfacesMax', Int32),
        ('cInOutInterfacesMax', Int32),
        ('cOutInterfacesMax', Int32),
        ('cTopLevelInInterfaces', Int32),
        ('iid', Guid),
        ('cMethod', UInt32),
        ('cParams', UInt32),
    ]
    return CALLFRAMEINFO
def _define_CALLFRAMEPARAMINFO_head():
    class CALLFRAMEPARAMINFO(Structure):
        pass
    return CALLFRAMEPARAMINFO
def _define_CALLFRAMEPARAMINFO():
    CALLFRAMEPARAMINFO = win32more.System.Com.CallObj.CALLFRAMEPARAMINFO_head
    CALLFRAMEPARAMINFO._fields_ = [
        ('fIn', win32more.Foundation.BOOLEAN),
        ('fOut', win32more.Foundation.BOOLEAN),
        ('stackOffset', UInt32),
        ('cbParam', UInt32),
    ]
    return CALLFRAMEPARAMINFO
def _define_ICallFrame_head():
    class ICallFrame(win32more.System.Com.IUnknown_head):
        Guid = Guid('d573b4b0-894e-11d2-b8-b6-00-c0-4f-b9-61-8a')
    return ICallFrame
def _define_ICallFrame():
    ICallFrame = win32more.System.Com.CallObj.ICallFrame_head
    ICallFrame.GetInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.CallObj.CALLFRAMEINFO_head))(3, 'GetInfo', ((1, 'pInfo'),)))
    ICallFrame.GetIIDAndMethod = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(UInt32))(4, 'GetIIDAndMethod', ((1, 'pIID'),(1, 'piMethod'),)))
    ICallFrame.GetNames = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR))(5, 'GetNames', ((1, 'pwszInterface'),(1, 'pwszMethod'),)))
    ICallFrame.GetStackLocation = COMMETHOD(WINFUNCTYPE(c_void_p,)(6, 'GetStackLocation', ()))
    ICallFrame.SetStackLocation = COMMETHOD(WINFUNCTYPE(Void,c_void_p)(7, 'SetStackLocation', ((1, 'pvStack'),)))
    ICallFrame.SetReturnValue = COMMETHOD(WINFUNCTYPE(Void,win32more.Foundation.HRESULT)(8, 'SetReturnValue', ((1, 'hr'),)))
    ICallFrame.GetReturnValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(9, 'GetReturnValue', ()))
    ICallFrame.GetParamInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.CallObj.CALLFRAMEPARAMINFO_head))(10, 'GetParamInfo', ((1, 'iparam'),(1, 'pInfo'),)))
    ICallFrame.SetParam = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.VARIANT_head))(11, 'SetParam', ((1, 'iparam'),(1, 'pvar'),)))
    ICallFrame.GetParam = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.VARIANT_head))(12, 'GetParam', ((1, 'iparam'),(1, 'pvar'),)))
    ICallFrame.Copy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.CallObj.CALLFRAME_COPY,win32more.System.Com.CallObj.ICallFrameWalker_head,POINTER(win32more.System.Com.CallObj.ICallFrame_head))(13, 'Copy', ((1, 'copyControl'),(1, 'pWalker'),(1, 'ppFrame'),)))
    ICallFrame.Free = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.CallObj.ICallFrame_head,win32more.System.Com.CallObj.ICallFrameWalker_head,win32more.System.Com.CallObj.ICallFrameWalker_head,UInt32,win32more.System.Com.CallObj.ICallFrameWalker_head,UInt32)(14, 'Free', ((1, 'pframeArgsDest'),(1, 'pWalkerDestFree'),(1, 'pWalkerCopy'),(1, 'freeFlags'),(1, 'pWalkerFree'),(1, 'nullFlags'),)))
    ICallFrame.FreeParam = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,win32more.System.Com.CallObj.ICallFrameWalker_head,UInt32)(15, 'FreeParam', ((1, 'iparam'),(1, 'freeFlags'),(1, 'pWalkerFree'),(1, 'nullFlags'),)))
    ICallFrame.WalkFrame = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.System.Com.CallObj.ICallFrameWalker_head)(16, 'WalkFrame', ((1, 'walkWhat'),(1, 'pWalker'),)))
    ICallFrame.GetMarshalSizeMax = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.CallObj.CALLFRAME_MARSHALCONTEXT_head),win32more.System.Com.MSHLFLAGS,POINTER(UInt32))(17, 'GetMarshalSizeMax', ((1, 'pmshlContext'),(1, 'mshlflags'),(1, 'pcbBufferNeeded'),)))
    ICallFrame.Marshal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.CallObj.CALLFRAME_MARSHALCONTEXT_head),win32more.System.Com.MSHLFLAGS,c_void_p,UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32))(18, 'Marshal', ((1, 'pmshlContext'),(1, 'mshlflags'),(1, 'pBuffer'),(1, 'cbBuffer'),(1, 'pcbBufferUsed'),(1, 'pdataRep'),(1, 'prpcFlags'),)))
    ICallFrame.Unmarshal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,UInt32,POINTER(win32more.System.Com.CallObj.CALLFRAME_MARSHALCONTEXT_head),POINTER(UInt32))(19, 'Unmarshal', ((1, 'pBuffer'),(1, 'cbBuffer'),(1, 'dataRep'),(1, 'pcontext'),(1, 'pcbUnmarshalled'),)))
    ICallFrame.ReleaseMarshalData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,UInt32,UInt32,POINTER(win32more.System.Com.CallObj.CALLFRAME_MARSHALCONTEXT_head))(20, 'ReleaseMarshalData', ((1, 'pBuffer'),(1, 'cbBuffer'),(1, 'ibFirstRelease'),(1, 'dataRep'),(1, 'pcontext'),)))
    ICallFrame.Invoke = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p)(21, 'Invoke', ((1, 'pvReceiver'),)))
    win32more.System.Com.IUnknown
    return ICallFrame
def _define_ICallFrameEvents_head():
    class ICallFrameEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('fd5e0843-fc91-11d0-97-d7-00-c0-4f-b9-61-8a')
    return ICallFrameEvents
def _define_ICallFrameEvents():
    ICallFrameEvents = win32more.System.Com.CallObj.ICallFrameEvents_head
    ICallFrameEvents.OnCall = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.CallObj.ICallFrame_head)(3, 'OnCall', ((1, 'pFrame'),)))
    win32more.System.Com.IUnknown
    return ICallFrameEvents
def _define_ICallFrameWalker_head():
    class ICallFrameWalker(win32more.System.Com.IUnknown_head):
        Guid = Guid('08b23919-392d-11d2-b8-a4-00-c0-4f-b9-61-8a')
    return ICallFrameWalker
def _define_ICallFrameWalker():
    ICallFrameWalker = win32more.System.Com.CallObj.ICallFrameWalker_head
    ICallFrameWalker.OnWalkInterface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p),win32more.Foundation.BOOL,win32more.Foundation.BOOL)(3, 'OnWalkInterface', ((1, 'iid'),(1, 'ppvInterface'),(1, 'fIn'),(1, 'fOut'),)))
    win32more.System.Com.IUnknown
    return ICallFrameWalker
def _define_ICallIndirect_head():
    class ICallIndirect(win32more.System.Com.IUnknown_head):
        Guid = Guid('d573b4b1-894e-11d2-b8-b6-00-c0-4f-b9-61-8a')
    return ICallIndirect
def _define_ICallIndirect():
    ICallIndirect = win32more.System.Com.CallObj.ICallIndirect_head
    ICallIndirect.CallIndirect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HRESULT),UInt32,c_void_p,POINTER(UInt32))(3, 'CallIndirect', ((1, 'phrReturn'),(1, 'iMethod'),(1, 'pvArgs'),(1, 'cbArgs'),)))
    ICallIndirect.GetMethodInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.CallObj.CALLFRAMEINFO_head),POINTER(win32more.Foundation.PWSTR))(4, 'GetMethodInfo', ((1, 'iMethod'),(1, 'pInfo'),(1, 'pwszMethod'),)))
    ICallIndirect.GetStackSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32))(5, 'GetStackSize', ((1, 'iMethod'),(1, 'cbArgs'),)))
    ICallIndirect.GetIID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Foundation.BOOL),POINTER(UInt32),POINTER(win32more.Foundation.PWSTR))(6, 'GetIID', ((1, 'piid'),(1, 'pfDerivesFromIDispatch'),(1, 'pcMethod'),(1, 'pwszInterface'),)))
    win32more.System.Com.IUnknown
    return ICallIndirect
def _define_ICallInterceptor_head():
    class ICallInterceptor(win32more.System.Com.CallObj.ICallIndirect_head):
        Guid = Guid('60c7ca75-896d-11d2-b8-b6-00-c0-4f-b9-61-8a')
    return ICallInterceptor
def _define_ICallInterceptor():
    ICallInterceptor = win32more.System.Com.CallObj.ICallInterceptor_head
    ICallInterceptor.RegisterSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.CallObj.ICallFrameEvents_head)(7, 'RegisterSink', ((1, 'psink'),)))
    ICallInterceptor.GetRegisteredSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.CallObj.ICallFrameEvents_head))(8, 'GetRegisteredSink', ((1, 'ppsink'),)))
    win32more.System.Com.CallObj.ICallIndirect
    return ICallInterceptor
def _define_ICallUnmarshal_head():
    class ICallUnmarshal(win32more.System.Com.IUnknown_head):
        Guid = Guid('5333b003-2e42-11d2-b8-9d-00-c0-4f-b9-61-8a')
    return ICallUnmarshal
def _define_ICallUnmarshal():
    ICallUnmarshal = win32more.System.Com.CallObj.ICallUnmarshal_head
    ICallUnmarshal.Unmarshal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_void_p,UInt32,win32more.Foundation.BOOL,UInt32,POINTER(win32more.System.Com.CallObj.CALLFRAME_MARSHALCONTEXT_head),POINTER(UInt32),POINTER(win32more.System.Com.CallObj.ICallFrame_head))(3, 'Unmarshal', ((1, 'iMethod'),(1, 'pBuffer'),(1, 'cbBuffer'),(1, 'fForceBufferCopy'),(1, 'dataRep'),(1, 'pcontext'),(1, 'pcbUnmarshalled'),(1, 'ppFrame'),)))
    ICallUnmarshal.ReleaseMarshalData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_void_p,UInt32,UInt32,UInt32,POINTER(win32more.System.Com.CallObj.CALLFRAME_MARSHALCONTEXT_head))(4, 'ReleaseMarshalData', ((1, 'iMethod'),(1, 'pBuffer'),(1, 'cbBuffer'),(1, 'ibFirstRelease'),(1, 'dataRep'),(1, 'pcontext'),)))
    win32more.System.Com.IUnknown
    return ICallUnmarshal
def _define_IInterfaceRelated_head():
    class IInterfaceRelated(win32more.System.Com.IUnknown_head):
        Guid = Guid('d1fb5a79-7706-11d1-ad-ba-00-c0-4f-c2-ad-c0')
    return IInterfaceRelated
def _define_IInterfaceRelated():
    IInterfaceRelated = win32more.System.Com.CallObj.IInterfaceRelated_head
    IInterfaceRelated.SetIID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(3, 'SetIID', ((1, 'iid'),)))
    IInterfaceRelated.GetIID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(4, 'GetIID', ((1, 'piid'),)))
    win32more.System.Com.IUnknown
    return IInterfaceRelated
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
