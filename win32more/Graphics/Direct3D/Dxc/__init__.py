from win32more.base import *
import win32more.Foundation
import win32more.Graphics.Direct3D.Dxc
import win32more.System.Com

import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
DXC_HASHFLAG_INCLUDES_SOURCE = 1
DxcValidatorFlags_Default = 0
DxcValidatorFlags_InPlaceEdit = 1
DxcValidatorFlags_RootSignatureOnly = 2
DxcValidatorFlags_ModuleOnly = 4
DxcValidatorFlags_ValidMask = 7
DxcVersionInfoFlags_None = 0
DxcVersionInfoFlags_Debug = 1
DxcVersionInfoFlags_Internal = 2
CLSID_DxcCompiler = '73e22d93-e6ce-47f3-b5bf-f0664f39c1b0'
CLSID_DxcLinker = 'ef6a8087-b0ea-4d56-9e45-d07e1a8b7806'
CLSID_DxcDiaDataSource = 'cd1f6b73-2ab0-484d-8edc-ebe7a43ca09f'
CLSID_DxcCompilerArgs = '3e56ae82-224d-470f-a1a1-fe3016ee9f9d'
CLSID_DxcLibrary = '6245d6af-66e0-48fd-80b4-4d271796748c'
CLSID_DxcValidator = '8ca3e215-f728-4cf3-8cdd-88af917587a1'
CLSID_DxcAssembler = 'd728db68-f903-4f80-94cd-dccf76ec7151'
CLSID_DxcContainerReflection = 'b9f54489-55b8-400c-ba3a-1675e4728b91'
CLSID_DxcOptimizer = 'ae2cd79f-cc22-453f-9b6b-b124e7a5204c'
CLSID_DxcContainerBuilder = '94134294-411f-4574-b4d0-8741e25240d2'
CLSID_DxcPdbUtils = '54621dfb-f2ce-457e-ae8c-ec355faeec7c'
DXC_CP = UInt32
DXC_CP_ACP = 0
DXC_CP_UTF16 = 1200
DXC_CP_UTF8 = 65001
def _define_DxcCreateInstanceProc():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),POINTER(c_void_p), use_last_error=False)
def _define_DxcCreateInstance2Proc():
    return CFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IMalloc_head,POINTER(Guid),POINTER(Guid),POINTER(c_void_p), use_last_error=False)
def _define_DxcShaderHash_head():
    class DxcShaderHash(Structure):
        pass
    return DxcShaderHash
def _define_DxcShaderHash():
    DxcShaderHash = win32more.Graphics.Direct3D.Dxc.DxcShaderHash_head
    DxcShaderHash._fields_ = [
        ("Flags", UInt32),
        ("HashDigest", Byte * 16),
    ]
    return DxcShaderHash
def _define_IDxcBlob_head():
    class IDxcBlob(win32more.System.Com.IUnknown_head):
        Guid = Guid('8ba5fb08-5195-40e2-ac58-0d989c3a0102')
    return IDxcBlob
def _define_IDxcBlob():
    IDxcBlob = win32more.Graphics.Direct3D.Dxc.IDxcBlob_head
    IDxcBlob.GetBufferPointer = COMMETHOD(WINFUNCTYPE(c_void_p, use_last_error=False)(3, 'GetBufferPointer', ()))
    IDxcBlob.GetBufferSize = COMMETHOD(WINFUNCTYPE(UIntPtr, use_last_error=False)(4, 'GetBufferSize', ()))
    win32more.System.Com.IUnknown
    return IDxcBlob
def _define_IDxcBlobEncoding_head():
    class IDxcBlobEncoding(win32more.Graphics.Direct3D.Dxc.IDxcBlob_head):
        Guid = Guid('7241d424-2646-4191-97c0-98e96e42fc68')
    return IDxcBlobEncoding
def _define_IDxcBlobEncoding():
    IDxcBlobEncoding = win32more.Graphics.Direct3D.Dxc.IDxcBlobEncoding_head
    IDxcBlobEncoding.GetEncoding = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL),POINTER(win32more.Graphics.Direct3D.Dxc.DXC_CP), use_last_error=False)(5, 'GetEncoding', ((1, 'pKnown'),(1, 'pCodePage'),)))
    win32more.Graphics.Direct3D.Dxc.IDxcBlob
    return IDxcBlobEncoding
def _define_IDxcBlobUtf16_head():
    class IDxcBlobUtf16(win32more.Graphics.Direct3D.Dxc.IDxcBlobEncoding_head):
        Guid = Guid('a3f84eab-0faa-497e-a39c-ee6ed60b2d84')
    return IDxcBlobUtf16
def _define_IDxcBlobUtf16():
    IDxcBlobUtf16 = win32more.Graphics.Direct3D.Dxc.IDxcBlobUtf16_head
    IDxcBlobUtf16.GetStringPointer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.PWSTR, use_last_error=False)(6, 'GetStringPointer', ()))
    IDxcBlobUtf16.GetStringLength = COMMETHOD(WINFUNCTYPE(UIntPtr, use_last_error=False)(7, 'GetStringLength', ()))
    win32more.Graphics.Direct3D.Dxc.IDxcBlobEncoding
    return IDxcBlobUtf16
def _define_IDxcBlobUtf8_head():
    class IDxcBlobUtf8(win32more.Graphics.Direct3D.Dxc.IDxcBlobEncoding_head):
        Guid = Guid('3da636c9-ba71-4024-a301-30cbf125305b')
    return IDxcBlobUtf8
def _define_IDxcBlobUtf8():
    IDxcBlobUtf8 = win32more.Graphics.Direct3D.Dxc.IDxcBlobUtf8_head
    IDxcBlobUtf8.GetStringPointer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.PSTR, use_last_error=False)(6, 'GetStringPointer', ()))
    IDxcBlobUtf8.GetStringLength = COMMETHOD(WINFUNCTYPE(UIntPtr, use_last_error=False)(7, 'GetStringLength', ()))
    win32more.Graphics.Direct3D.Dxc.IDxcBlobEncoding
    return IDxcBlobUtf8
def _define_IDxcIncludeHandler_head():
    class IDxcIncludeHandler(win32more.System.Com.IUnknown_head):
        Guid = Guid('7f61fc7d-950d-467f-b3e3-3c02fb49187c')
    return IDxcIncludeHandler
def _define_IDxcIncludeHandler():
    IDxcIncludeHandler = win32more.Graphics.Direct3D.Dxc.IDxcIncludeHandler_head
    IDxcIncludeHandler.LoadSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Graphics.Direct3D.Dxc.IDxcBlob_head), use_last_error=False)(3, 'LoadSource', ((1, 'pFilename'),(1, 'ppIncludeSource'),)))
    win32more.System.Com.IUnknown
    return IDxcIncludeHandler
def _define_DxcBuffer_head():
    class DxcBuffer(Structure):
        pass
    return DxcBuffer
def _define_DxcBuffer():
    DxcBuffer = win32more.Graphics.Direct3D.Dxc.DxcBuffer_head
    DxcBuffer._fields_ = [
        ("Ptr", c_void_p),
        ("Size", UIntPtr),
        ("Encoding", UInt32),
    ]
    return DxcBuffer
def _define_DxcDefine_head():
    class DxcDefine(Structure):
        pass
    return DxcDefine
def _define_DxcDefine():
    DxcDefine = win32more.Graphics.Direct3D.Dxc.DxcDefine_head
    DxcDefine._fields_ = [
        ("Name", win32more.Foundation.PWSTR),
        ("Value", win32more.Foundation.PWSTR),
    ]
    return DxcDefine
def _define_IDxcCompilerArgs_head():
    class IDxcCompilerArgs(win32more.System.Com.IUnknown_head):
        Guid = Guid('73effe2a-70dc-45f8-9690-eff64c02429d')
    return IDxcCompilerArgs
def _define_IDxcCompilerArgs():
    IDxcCompilerArgs = win32more.Graphics.Direct3D.Dxc.IDxcCompilerArgs_head
    IDxcCompilerArgs.GetArguments = COMMETHOD(WINFUNCTYPE(POINTER(win32more.Foundation.PWSTR), use_last_error=False)(3, 'GetArguments', ()))
    IDxcCompilerArgs.GetCount = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(4, 'GetCount', ()))
    IDxcCompilerArgs.AddArguments = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR),UInt32, use_last_error=False)(5, 'AddArguments', ((1, 'pArguments'),(1, 'argCount'),)))
    IDxcCompilerArgs.AddArgumentsUTF8 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PSTR),UInt32, use_last_error=False)(6, 'AddArgumentsUTF8', ((1, 'pArguments'),(1, 'argCount'),)))
    IDxcCompilerArgs.AddDefines = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D.Dxc.DxcDefine),UInt32, use_last_error=False)(7, 'AddDefines', ((1, 'pDefines'),(1, 'defineCount'),)))
    win32more.System.Com.IUnknown
    return IDxcCompilerArgs
def _define_IDxcLibrary_head():
    class IDxcLibrary(win32more.System.Com.IUnknown_head):
        Guid = Guid('e5204dc7-d18c-4c3c-bdfb-851673980fe7')
    return IDxcLibrary
def _define_IDxcLibrary():
    IDxcLibrary = win32more.Graphics.Direct3D.Dxc.IDxcLibrary_head
    IDxcLibrary.SetMalloc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IMalloc_head, use_last_error=False)(3, 'SetMalloc', ((1, 'pMalloc'),)))
    IDxcLibrary.CreateBlobFromBlob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D.Dxc.IDxcBlob_head,UInt32,UInt32,POINTER(win32more.Graphics.Direct3D.Dxc.IDxcBlob_head), use_last_error=False)(4, 'CreateBlobFromBlob', ((1, 'pBlob'),(1, 'offset'),(1, 'length'),(1, 'ppResult'),)))
    IDxcLibrary.CreateBlobFromFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Graphics.Direct3D.Dxc.DXC_CP),POINTER(win32more.Graphics.Direct3D.Dxc.IDxcBlobEncoding_head), use_last_error=False)(5, 'CreateBlobFromFile', ((1, 'pFileName'),(1, 'codePage'),(1, 'pBlobEncoding'),)))
    IDxcLibrary.CreateBlobWithEncodingFromPinned = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,win32more.Graphics.Direct3D.Dxc.DXC_CP,POINTER(win32more.Graphics.Direct3D.Dxc.IDxcBlobEncoding_head), use_last_error=False)(6, 'CreateBlobWithEncodingFromPinned', ((1, 'pText'),(1, 'size'),(1, 'codePage'),(1, 'pBlobEncoding'),)))
    IDxcLibrary.CreateBlobWithEncodingOnHeapCopy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,win32more.Graphics.Direct3D.Dxc.DXC_CP,POINTER(win32more.Graphics.Direct3D.Dxc.IDxcBlobEncoding_head), use_last_error=False)(7, 'CreateBlobWithEncodingOnHeapCopy', ((1, 'pText'),(1, 'size'),(1, 'codePage'),(1, 'pBlobEncoding'),)))
    IDxcLibrary.CreateBlobWithEncodingOnMalloc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.System.Com.IMalloc_head,UInt32,win32more.Graphics.Direct3D.Dxc.DXC_CP,POINTER(win32more.Graphics.Direct3D.Dxc.IDxcBlobEncoding_head), use_last_error=False)(8, 'CreateBlobWithEncodingOnMalloc', ((1, 'pText'),(1, 'pIMalloc'),(1, 'size'),(1, 'codePage'),(1, 'pBlobEncoding'),)))
    IDxcLibrary.CreateIncludeHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D.Dxc.IDxcIncludeHandler_head), use_last_error=False)(9, 'CreateIncludeHandler', ((1, 'ppResult'),)))
    IDxcLibrary.CreateStreamFromBlobReadOnly = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D.Dxc.IDxcBlob_head,POINTER(win32more.System.Com.IStream_head), use_last_error=False)(10, 'CreateStreamFromBlobReadOnly', ((1, 'pBlob'),(1, 'ppStream'),)))
    IDxcLibrary.GetBlobAsUtf8 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D.Dxc.IDxcBlob_head,POINTER(win32more.Graphics.Direct3D.Dxc.IDxcBlobEncoding_head), use_last_error=False)(11, 'GetBlobAsUtf8', ((1, 'pBlob'),(1, 'pBlobEncoding'),)))
    IDxcLibrary.GetBlobAsUtf16 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D.Dxc.IDxcBlob_head,POINTER(win32more.Graphics.Direct3D.Dxc.IDxcBlobEncoding_head), use_last_error=False)(12, 'GetBlobAsUtf16', ((1, 'pBlob'),(1, 'pBlobEncoding'),)))
    win32more.System.Com.IUnknown
    return IDxcLibrary
def _define_IDxcOperationResult_head():
    class IDxcOperationResult(win32more.System.Com.IUnknown_head):
        Guid = Guid('cedb484a-d4e9-445a-b991-ca21ca157dc2')
    return IDxcOperationResult
def _define_IDxcOperationResult():
    IDxcOperationResult = win32more.Graphics.Direct3D.Dxc.IDxcOperationResult_head
    IDxcOperationResult.GetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HRESULT), use_last_error=False)(3, 'GetStatus', ((1, 'pStatus'),)))
    IDxcOperationResult.GetResult = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D.Dxc.IDxcBlob_head), use_last_error=False)(4, 'GetResult', ((1, 'ppResult'),)))
    IDxcOperationResult.GetErrorBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D.Dxc.IDxcBlobEncoding_head), use_last_error=False)(5, 'GetErrorBuffer', ((1, 'ppErrors'),)))
    win32more.System.Com.IUnknown
    return IDxcOperationResult
def _define_IDxcCompiler_head():
    class IDxcCompiler(win32more.System.Com.IUnknown_head):
        Guid = Guid('8c210bf3-011f-4422-8d70-6f9acb8db617')
    return IDxcCompiler
def _define_IDxcCompiler():
    IDxcCompiler = win32more.Graphics.Direct3D.Dxc.IDxcCompiler_head
    IDxcCompiler.Compile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D.Dxc.IDxcBlob_head,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR),UInt32,POINTER(win32more.Graphics.Direct3D.Dxc.DxcDefine),UInt32,win32more.Graphics.Direct3D.Dxc.IDxcIncludeHandler_head,POINTER(win32more.Graphics.Direct3D.Dxc.IDxcOperationResult_head), use_last_error=False)(3, 'Compile', ((1, 'pSource'),(1, 'pSourceName'),(1, 'pEntryPoint'),(1, 'pTargetProfile'),(1, 'pArguments'),(1, 'argCount'),(1, 'pDefines'),(1, 'defineCount'),(1, 'pIncludeHandler'),(1, 'ppResult'),)))
    IDxcCompiler.Preprocess = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D.Dxc.IDxcBlob_head,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR),UInt32,POINTER(win32more.Graphics.Direct3D.Dxc.DxcDefine),UInt32,win32more.Graphics.Direct3D.Dxc.IDxcIncludeHandler_head,POINTER(win32more.Graphics.Direct3D.Dxc.IDxcOperationResult_head), use_last_error=False)(4, 'Preprocess', ((1, 'pSource'),(1, 'pSourceName'),(1, 'pArguments'),(1, 'argCount'),(1, 'pDefines'),(1, 'defineCount'),(1, 'pIncludeHandler'),(1, 'ppResult'),)))
    IDxcCompiler.Disassemble = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D.Dxc.IDxcBlob_head,POINTER(win32more.Graphics.Direct3D.Dxc.IDxcBlobEncoding_head), use_last_error=False)(5, 'Disassemble', ((1, 'pSource'),(1, 'ppDisassembly'),)))
    win32more.System.Com.IUnknown
    return IDxcCompiler
def _define_IDxcCompiler2_head():
    class IDxcCompiler2(win32more.Graphics.Direct3D.Dxc.IDxcCompiler_head):
        Guid = Guid('a005a9d9-b8bb-4594-b5c9-0e633bec4d37')
    return IDxcCompiler2
def _define_IDxcCompiler2():
    IDxcCompiler2 = win32more.Graphics.Direct3D.Dxc.IDxcCompiler2_head
    IDxcCompiler2.CompileWithDebug = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D.Dxc.IDxcBlob_head,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR),UInt32,POINTER(win32more.Graphics.Direct3D.Dxc.DxcDefine),UInt32,win32more.Graphics.Direct3D.Dxc.IDxcIncludeHandler_head,POINTER(win32more.Graphics.Direct3D.Dxc.IDxcOperationResult_head),POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Graphics.Direct3D.Dxc.IDxcBlob_head), use_last_error=False)(6, 'CompileWithDebug', ((1, 'pSource'),(1, 'pSourceName'),(1, 'pEntryPoint'),(1, 'pTargetProfile'),(1, 'pArguments'),(1, 'argCount'),(1, 'pDefines'),(1, 'defineCount'),(1, 'pIncludeHandler'),(1, 'ppResult'),(1, 'ppDebugBlobName'),(1, 'ppDebugBlob'),)))
    win32more.Graphics.Direct3D.Dxc.IDxcCompiler
    return IDxcCompiler2
def _define_IDxcLinker_head():
    class IDxcLinker(win32more.System.Com.IUnknown_head):
        Guid = Guid('f1b5be2a-62dd-4327-a1c2-42ac1e1e78e6')
    return IDxcLinker
def _define_IDxcLinker():
    IDxcLinker = win32more.Graphics.Direct3D.Dxc.IDxcLinker_head
    IDxcLinker.RegisterLibrary = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Graphics.Direct3D.Dxc.IDxcBlob_head, use_last_error=False)(3, 'RegisterLibrary', ((1, 'pLibName'),(1, 'pLib'),)))
    IDxcLinker.Link = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR),UInt32,POINTER(win32more.Foundation.PWSTR),UInt32,POINTER(win32more.Graphics.Direct3D.Dxc.IDxcOperationResult_head), use_last_error=False)(4, 'Link', ((1, 'pEntryName'),(1, 'pTargetProfile'),(1, 'pLibNames'),(1, 'libCount'),(1, 'pArguments'),(1, 'argCount'),(1, 'ppResult'),)))
    win32more.System.Com.IUnknown
    return IDxcLinker
def _define_IDxcUtils_head():
    class IDxcUtils(win32more.System.Com.IUnknown_head):
        Guid = Guid('4605c4cb-2019-492a-ada4-65f20bb7d67f')
    return IDxcUtils
def _define_IDxcUtils():
    IDxcUtils = win32more.Graphics.Direct3D.Dxc.IDxcUtils_head
    IDxcUtils.CreateBlobFromBlob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D.Dxc.IDxcBlob_head,UInt32,UInt32,POINTER(win32more.Graphics.Direct3D.Dxc.IDxcBlob_head), use_last_error=False)(3, 'CreateBlobFromBlob', ((1, 'pBlob'),(1, 'offset'),(1, 'length'),(1, 'ppResult'),)))
    IDxcUtils.CreateBlobFromPinned = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,win32more.Graphics.Direct3D.Dxc.DXC_CP,POINTER(win32more.Graphics.Direct3D.Dxc.IDxcBlobEncoding_head), use_last_error=False)(4, 'CreateBlobFromPinned', ((1, 'pData'),(1, 'size'),(1, 'codePage'),(1, 'pBlobEncoding'),)))
    IDxcUtils.MoveToBlob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.System.Com.IMalloc_head,UInt32,win32more.Graphics.Direct3D.Dxc.DXC_CP,POINTER(win32more.Graphics.Direct3D.Dxc.IDxcBlobEncoding_head), use_last_error=False)(5, 'MoveToBlob', ((1, 'pData'),(1, 'pIMalloc'),(1, 'size'),(1, 'codePage'),(1, 'pBlobEncoding'),)))
    IDxcUtils.CreateBlob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,win32more.Graphics.Direct3D.Dxc.DXC_CP,POINTER(win32more.Graphics.Direct3D.Dxc.IDxcBlobEncoding_head), use_last_error=False)(6, 'CreateBlob', ((1, 'pData'),(1, 'size'),(1, 'codePage'),(1, 'pBlobEncoding'),)))
    IDxcUtils.LoadFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Graphics.Direct3D.Dxc.DXC_CP),POINTER(win32more.Graphics.Direct3D.Dxc.IDxcBlobEncoding_head), use_last_error=False)(7, 'LoadFile', ((1, 'pFileName'),(1, 'pCodePage'),(1, 'pBlobEncoding'),)))
    IDxcUtils.CreateReadOnlyStreamFromBlob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D.Dxc.IDxcBlob_head,POINTER(win32more.System.Com.IStream_head), use_last_error=False)(8, 'CreateReadOnlyStreamFromBlob', ((1, 'pBlob'),(1, 'ppStream'),)))
    IDxcUtils.CreateDefaultIncludeHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D.Dxc.IDxcIncludeHandler_head), use_last_error=False)(9, 'CreateDefaultIncludeHandler', ((1, 'ppResult'),)))
    IDxcUtils.GetBlobAsUtf8 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D.Dxc.IDxcBlob_head,POINTER(win32more.Graphics.Direct3D.Dxc.IDxcBlobUtf8_head), use_last_error=False)(10, 'GetBlobAsUtf8', ((1, 'pBlob'),(1, 'pBlobEncoding'),)))
    IDxcUtils.GetBlobAsUtf16 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D.Dxc.IDxcBlob_head,POINTER(win32more.Graphics.Direct3D.Dxc.IDxcBlobUtf16_head), use_last_error=False)(11, 'GetBlobAsUtf16', ((1, 'pBlob'),(1, 'pBlobEncoding'),)))
    IDxcUtils.GetDxilContainerPart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D.Dxc.DxcBuffer_head),UInt32,POINTER(c_void_p),POINTER(UInt32), use_last_error=False)(12, 'GetDxilContainerPart', ((1, 'pShader'),(1, 'DxcPart'),(1, 'ppPartData'),(1, 'pPartSizeInBytes'),)))
    IDxcUtils.CreateReflection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D.Dxc.DxcBuffer_head),POINTER(Guid),POINTER(c_void_p), use_last_error=False)(13, 'CreateReflection', ((1, 'pData'),(1, 'iid'),(1, 'ppvReflection'),)))
    IDxcUtils.BuildArguments = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR),UInt32,POINTER(win32more.Graphics.Direct3D.Dxc.DxcDefine),UInt32,POINTER(win32more.Graphics.Direct3D.Dxc.IDxcCompilerArgs_head), use_last_error=False)(14, 'BuildArguments', ((1, 'pSourceName'),(1, 'pEntryPoint'),(1, 'pTargetProfile'),(1, 'pArguments'),(1, 'argCount'),(1, 'pDefines'),(1, 'defineCount'),(1, 'ppArgs'),)))
    IDxcUtils.GetPDBContents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D.Dxc.IDxcBlob_head,POINTER(win32more.Graphics.Direct3D.Dxc.IDxcBlob_head),POINTER(win32more.Graphics.Direct3D.Dxc.IDxcBlob_head), use_last_error=False)(15, 'GetPDBContents', ((1, 'pPDBBlob'),(1, 'ppHash'),(1, 'ppContainer'),)))
    win32more.System.Com.IUnknown
    return IDxcUtils
DXC_OUT_KIND = Int32
DXC_OUT_NONE = 0
DXC_OUT_OBJECT = 1
DXC_OUT_ERRORS = 2
DXC_OUT_PDB = 3
DXC_OUT_SHADER_HASH = 4
DXC_OUT_DISASSEMBLY = 5
DXC_OUT_HLSL = 6
DXC_OUT_TEXT = 7
DXC_OUT_REFLECTION = 8
DXC_OUT_ROOT_SIGNATURE = 9
DXC_OUT_EXTRA_OUTPUTS = 10
DXC_OUT_FORCE_DWORD = -1
def _define_IDxcResult_head():
    class IDxcResult(win32more.Graphics.Direct3D.Dxc.IDxcOperationResult_head):
        Guid = Guid('58346cda-dde7-4497-9461-6f87af5e0659')
    return IDxcResult
def _define_IDxcResult():
    IDxcResult = win32more.Graphics.Direct3D.Dxc.IDxcResult_head
    IDxcResult.HasOutput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Direct3D.Dxc.DXC_OUT_KIND, use_last_error=False)(6, 'HasOutput', ((1, 'dxcOutKind'),)))
    IDxcResult.GetOutput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D.Dxc.DXC_OUT_KIND,POINTER(Guid),POINTER(c_void_p),POINTER(win32more.Graphics.Direct3D.Dxc.IDxcBlobUtf16_head), use_last_error=False)(7, 'GetOutput', ((1, 'dxcOutKind'),(1, 'iid'),(1, 'ppvObject'),(1, 'ppOutputName'),)))
    IDxcResult.GetNumOutputs = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(8, 'GetNumOutputs', ()))
    IDxcResult.GetOutputByIndex = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D.Dxc.DXC_OUT_KIND,UInt32, use_last_error=False)(9, 'GetOutputByIndex', ((1, 'Index'),)))
    IDxcResult.PrimaryOutput = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D.Dxc.DXC_OUT_KIND, use_last_error=False)(10, 'PrimaryOutput', ()))
    win32more.Graphics.Direct3D.Dxc.IDxcOperationResult
    return IDxcResult
def _define_IDxcExtraOutputs_head():
    class IDxcExtraOutputs(win32more.System.Com.IUnknown_head):
        Guid = Guid('319b37a2-a5c2-494a-a5de-4801b2faf989')
    return IDxcExtraOutputs
def _define_IDxcExtraOutputs():
    IDxcExtraOutputs = win32more.Graphics.Direct3D.Dxc.IDxcExtraOutputs_head
    IDxcExtraOutputs.GetOutputCount = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(3, 'GetOutputCount', ()))
    IDxcExtraOutputs.GetOutput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(c_void_p),POINTER(win32more.Graphics.Direct3D.Dxc.IDxcBlobUtf16_head),POINTER(win32more.Graphics.Direct3D.Dxc.IDxcBlobUtf16_head), use_last_error=False)(4, 'GetOutput', ((1, 'uIndex'),(1, 'iid'),(1, 'ppvObject'),(1, 'ppOutputType'),(1, 'ppOutputName'),)))
    win32more.System.Com.IUnknown
    return IDxcExtraOutputs
def _define_IDxcCompiler3_head():
    class IDxcCompiler3(win32more.System.Com.IUnknown_head):
        Guid = Guid('228b4687-5a6a-4730-900c-9702b2203f54')
    return IDxcCompiler3
def _define_IDxcCompiler3():
    IDxcCompiler3 = win32more.Graphics.Direct3D.Dxc.IDxcCompiler3_head
    IDxcCompiler3.Compile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D.Dxc.DxcBuffer_head),POINTER(win32more.Foundation.PWSTR),UInt32,win32more.Graphics.Direct3D.Dxc.IDxcIncludeHandler_head,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(3, 'Compile', ((1, 'pSource'),(1, 'pArguments'),(1, 'argCount'),(1, 'pIncludeHandler'),(1, 'riid'),(1, 'ppResult'),)))
    IDxcCompiler3.Disassemble = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D.Dxc.DxcBuffer_head),POINTER(Guid),POINTER(c_void_p), use_last_error=False)(4, 'Disassemble', ((1, 'pObject'),(1, 'riid'),(1, 'ppResult'),)))
    win32more.System.Com.IUnknown
    return IDxcCompiler3
def _define_IDxcValidator_head():
    class IDxcValidator(win32more.System.Com.IUnknown_head):
        Guid = Guid('a6e82bd2-1fd7-4826-9811-2857e797f49a')
    return IDxcValidator
def _define_IDxcValidator():
    IDxcValidator = win32more.Graphics.Direct3D.Dxc.IDxcValidator_head
    IDxcValidator.Validate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D.Dxc.IDxcBlob_head,UInt32,POINTER(win32more.Graphics.Direct3D.Dxc.IDxcOperationResult_head), use_last_error=False)(3, 'Validate', ((1, 'pShader'),(1, 'Flags'),(1, 'ppResult'),)))
    win32more.System.Com.IUnknown
    return IDxcValidator
def _define_IDxcValidator2_head():
    class IDxcValidator2(win32more.Graphics.Direct3D.Dxc.IDxcValidator_head):
        Guid = Guid('458e1fd1-b1b2-4750-a6e1-9c10f03bed92')
    return IDxcValidator2
def _define_IDxcValidator2():
    IDxcValidator2 = win32more.Graphics.Direct3D.Dxc.IDxcValidator2_head
    IDxcValidator2.ValidateWithDebug = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D.Dxc.IDxcBlob_head,UInt32,POINTER(win32more.Graphics.Direct3D.Dxc.DxcBuffer_head),POINTER(win32more.Graphics.Direct3D.Dxc.IDxcOperationResult_head), use_last_error=False)(4, 'ValidateWithDebug', ((1, 'pShader'),(1, 'Flags'),(1, 'pOptDebugBitcode'),(1, 'ppResult'),)))
    win32more.Graphics.Direct3D.Dxc.IDxcValidator
    return IDxcValidator2
def _define_IDxcContainerBuilder_head():
    class IDxcContainerBuilder(win32more.System.Com.IUnknown_head):
        Guid = Guid('334b1f50-2292-4b35-99a1-25588d8c17fe')
    return IDxcContainerBuilder
def _define_IDxcContainerBuilder():
    IDxcContainerBuilder = win32more.Graphics.Direct3D.Dxc.IDxcContainerBuilder_head
    IDxcContainerBuilder.Load = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D.Dxc.IDxcBlob_head, use_last_error=False)(3, 'Load', ((1, 'pDxilContainerHeader'),)))
    IDxcContainerBuilder.AddPart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Graphics.Direct3D.Dxc.IDxcBlob_head, use_last_error=False)(4, 'AddPart', ((1, 'fourCC'),(1, 'pSource'),)))
    IDxcContainerBuilder.RemovePart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(5, 'RemovePart', ((1, 'fourCC'),)))
    IDxcContainerBuilder.SerializeContainer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D.Dxc.IDxcOperationResult_head), use_last_error=False)(6, 'SerializeContainer', ((1, 'ppResult'),)))
    win32more.System.Com.IUnknown
    return IDxcContainerBuilder
def _define_IDxcAssembler_head():
    class IDxcAssembler(win32more.System.Com.IUnknown_head):
        Guid = Guid('091f7a26-1c1f-4948-904b-e6e3a8a771d5')
    return IDxcAssembler
def _define_IDxcAssembler():
    IDxcAssembler = win32more.Graphics.Direct3D.Dxc.IDxcAssembler_head
    IDxcAssembler.AssembleToContainer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D.Dxc.IDxcBlob_head,POINTER(win32more.Graphics.Direct3D.Dxc.IDxcOperationResult_head), use_last_error=False)(3, 'AssembleToContainer', ((1, 'pShader'),(1, 'ppResult'),)))
    win32more.System.Com.IUnknown
    return IDxcAssembler
def _define_IDxcContainerReflection_head():
    class IDxcContainerReflection(win32more.System.Com.IUnknown_head):
        Guid = Guid('d2c21b26-8350-4bdc-976a-331ce6f4c54c')
    return IDxcContainerReflection
def _define_IDxcContainerReflection():
    IDxcContainerReflection = win32more.Graphics.Direct3D.Dxc.IDxcContainerReflection_head
    IDxcContainerReflection.Load = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D.Dxc.IDxcBlob_head, use_last_error=False)(3, 'Load', ((1, 'pContainer'),)))
    IDxcContainerReflection.GetPartCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(4, 'GetPartCount', ((1, 'pResult'),)))
    IDxcContainerReflection.GetPartKind = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(5, 'GetPartKind', ((1, 'idx'),(1, 'pResult'),)))
    IDxcContainerReflection.GetPartContent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Direct3D.Dxc.IDxcBlob_head), use_last_error=False)(6, 'GetPartContent', ((1, 'idx'),(1, 'ppResult'),)))
    IDxcContainerReflection.FindFirstPartKind = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(7, 'FindFirstPartKind', ((1, 'kind'),(1, 'pResult'),)))
    IDxcContainerReflection.GetPartReflection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(8, 'GetPartReflection', ((1, 'idx'),(1, 'iid'),(1, 'ppvObject'),)))
    win32more.System.Com.IUnknown
    return IDxcContainerReflection
def _define_IDxcOptimizerPass_head():
    class IDxcOptimizerPass(win32more.System.Com.IUnknown_head):
        Guid = Guid('ae2cd79f-cc22-453f-9b6b-b124e7a5204c')
    return IDxcOptimizerPass
def _define_IDxcOptimizerPass():
    IDxcOptimizerPass = win32more.Graphics.Direct3D.Dxc.IDxcOptimizerPass_head
    IDxcOptimizerPass.GetOptionName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(3, 'GetOptionName', ((1, 'ppResult'),)))
    IDxcOptimizerPass.GetDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(4, 'GetDescription', ((1, 'ppResult'),)))
    IDxcOptimizerPass.GetOptionArgCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(5, 'GetOptionArgCount', ((1, 'pCount'),)))
    IDxcOptimizerPass.GetOptionArgName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(6, 'GetOptionArgName', ((1, 'argIndex'),(1, 'ppResult'),)))
    IDxcOptimizerPass.GetOptionArgDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(7, 'GetOptionArgDescription', ((1, 'argIndex'),(1, 'ppResult'),)))
    win32more.System.Com.IUnknown
    return IDxcOptimizerPass
def _define_IDxcOptimizer_head():
    class IDxcOptimizer(win32more.System.Com.IUnknown_head):
        Guid = Guid('25740e2e-9cba-401b-9119-4fb42f39f270')
    return IDxcOptimizer
def _define_IDxcOptimizer():
    IDxcOptimizer = win32more.Graphics.Direct3D.Dxc.IDxcOptimizer_head
    IDxcOptimizer.GetAvailablePassCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetAvailablePassCount', ((1, 'pCount'),)))
    IDxcOptimizer.GetAvailablePass = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Direct3D.Dxc.IDxcOptimizerPass_head), use_last_error=False)(4, 'GetAvailablePass', ((1, 'index'),(1, 'ppResult'),)))
    IDxcOptimizer.RunOptimizer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D.Dxc.IDxcBlob_head,POINTER(win32more.Foundation.PWSTR),UInt32,POINTER(win32more.Graphics.Direct3D.Dxc.IDxcBlob_head),POINTER(win32more.Graphics.Direct3D.Dxc.IDxcBlobEncoding_head), use_last_error=False)(5, 'RunOptimizer', ((1, 'pBlob'),(1, 'ppOptions'),(1, 'optionCount'),(1, 'pOutputModule'),(1, 'ppOutputText'),)))
    win32more.System.Com.IUnknown
    return IDxcOptimizer
def _define_IDxcVersionInfo_head():
    class IDxcVersionInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('b04f5b50-2059-4f12-a8ff-a1e0cde1cc7e')
    return IDxcVersionInfo
def _define_IDxcVersionInfo():
    IDxcVersionInfo = win32more.Graphics.Direct3D.Dxc.IDxcVersionInfo_head
    IDxcVersionInfo.GetVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(3, 'GetVersion', ((1, 'pMajor'),(1, 'pMinor'),)))
    IDxcVersionInfo.GetFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(4, 'GetFlags', ((1, 'pFlags'),)))
    win32more.System.Com.IUnknown
    return IDxcVersionInfo
def _define_IDxcVersionInfo2_head():
    class IDxcVersionInfo2(win32more.Graphics.Direct3D.Dxc.IDxcVersionInfo_head):
        Guid = Guid('fb6904c4-42f0-4b62-9c46-983af7da7c83')
    return IDxcVersionInfo2
def _define_IDxcVersionInfo2():
    IDxcVersionInfo2 = win32more.Graphics.Direct3D.Dxc.IDxcVersionInfo2_head
    IDxcVersionInfo2.GetCommitInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(POINTER(SByte)), use_last_error=False)(5, 'GetCommitInfo', ((1, 'pCommitCount'),(1, 'pCommitHash'),)))
    win32more.Graphics.Direct3D.Dxc.IDxcVersionInfo
    return IDxcVersionInfo2
def _define_IDxcVersionInfo3_head():
    class IDxcVersionInfo3(win32more.System.Com.IUnknown_head):
        Guid = Guid('5e13e843-9d25-473c-9ad2-03b2d0b44b1e')
    return IDxcVersionInfo3
def _define_IDxcVersionInfo3():
    IDxcVersionInfo3 = win32more.Graphics.Direct3D.Dxc.IDxcVersionInfo3_head
    IDxcVersionInfo3.GetCustomVersionString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(SByte)), use_last_error=False)(3, 'GetCustomVersionString', ((1, 'pVersionString'),)))
    win32more.System.Com.IUnknown
    return IDxcVersionInfo3
def _define_DxcArgPair_head():
    class DxcArgPair(Structure):
        pass
    return DxcArgPair
def _define_DxcArgPair():
    DxcArgPair = win32more.Graphics.Direct3D.Dxc.DxcArgPair_head
    DxcArgPair._fields_ = [
        ("pName", win32more.Foundation.PWSTR),
        ("pValue", win32more.Foundation.PWSTR),
    ]
    return DxcArgPair
def _define_IDxcPdbUtils_head():
    class IDxcPdbUtils(win32more.System.Com.IUnknown_head):
        Guid = Guid('e6c9647e-9d6a-4c3b-b94c-524b5a6c343d')
    return IDxcPdbUtils
def _define_IDxcPdbUtils():
    IDxcPdbUtils = win32more.Graphics.Direct3D.Dxc.IDxcPdbUtils_head
    IDxcPdbUtils.Load = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D.Dxc.IDxcBlob_head, use_last_error=False)(3, 'Load', ((1, 'pPdbOrDxil'),)))
    IDxcPdbUtils.GetSourceCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(4, 'GetSourceCount', ((1, 'pCount'),)))
    IDxcPdbUtils.GetSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Direct3D.Dxc.IDxcBlobEncoding_head), use_last_error=False)(5, 'GetSource', ((1, 'uIndex'),(1, 'ppResult'),)))
    IDxcPdbUtils.GetSourceName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(6, 'GetSourceName', ((1, 'uIndex'),(1, 'pResult'),)))
    IDxcPdbUtils.GetFlagCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(7, 'GetFlagCount', ((1, 'pCount'),)))
    IDxcPdbUtils.GetFlag = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'GetFlag', ((1, 'uIndex'),(1, 'pResult'),)))
    IDxcPdbUtils.GetArgCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(9, 'GetArgCount', ((1, 'pCount'),)))
    IDxcPdbUtils.GetArg = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'GetArg', ((1, 'uIndex'),(1, 'pResult'),)))
    IDxcPdbUtils.GetArgPairCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(11, 'GetArgPairCount', ((1, 'pCount'),)))
    IDxcPdbUtils.GetArgPair = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.BSTR),POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'GetArgPair', ((1, 'uIndex'),(1, 'pName'),(1, 'pValue'),)))
    IDxcPdbUtils.GetDefineCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(13, 'GetDefineCount', ((1, 'pCount'),)))
    IDxcPdbUtils.GetDefine = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(14, 'GetDefine', ((1, 'uIndex'),(1, 'pResult'),)))
    IDxcPdbUtils.GetTargetProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(15, 'GetTargetProfile', ((1, 'pResult'),)))
    IDxcPdbUtils.GetEntryPoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(16, 'GetEntryPoint', ((1, 'pResult'),)))
    IDxcPdbUtils.GetMainFileName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(17, 'GetMainFileName', ((1, 'pResult'),)))
    IDxcPdbUtils.GetHash = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D.Dxc.IDxcBlob_head), use_last_error=False)(18, 'GetHash', ((1, 'ppResult'),)))
    IDxcPdbUtils.GetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(19, 'GetName', ((1, 'pResult'),)))
    IDxcPdbUtils.IsFullPDB = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL, use_last_error=False)(20, 'IsFullPDB', ()))
    IDxcPdbUtils.GetFullPDB = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D.Dxc.IDxcBlob_head), use_last_error=False)(21, 'GetFullPDB', ((1, 'ppFullPDB'),)))
    IDxcPdbUtils.GetVersionInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D.Dxc.IDxcVersionInfo_head), use_last_error=False)(22, 'GetVersionInfo', ((1, 'ppVersionInfo'),)))
    IDxcPdbUtils.SetCompiler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D.Dxc.IDxcCompiler3_head, use_last_error=False)(23, 'SetCompiler', ((1, 'pCompiler'),)))
    IDxcPdbUtils.CompileForFullPDB = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D.Dxc.IDxcResult_head), use_last_error=False)(24, 'CompileForFullPDB', ((1, 'ppResult'),)))
    IDxcPdbUtils.OverrideArgs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D.Dxc.DxcArgPair_head),UInt32, use_last_error=False)(25, 'OverrideArgs', ((1, 'pArgPairs'),(1, 'uNumArgPairs'),)))
    IDxcPdbUtils.OverrideRootSignature = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(26, 'OverrideRootSignature', ((1, 'pRootSignature'),)))
    win32more.System.Com.IUnknown
    return IDxcPdbUtils
def _define_DxcCreateInstance():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("DxcCreateInstance", windll["dxcompiler"]), ((1, 'rclsid'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DxcCreateInstance2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IMalloc_head,POINTER(Guid),POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("DxcCreateInstance2", windll["dxcompiler"]), ((1, 'pMalloc'),(1, 'rclsid'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "DXC_HASHFLAG_INCLUDES_SOURCE",
    "DxcValidatorFlags_Default",
    "DxcValidatorFlags_InPlaceEdit",
    "DxcValidatorFlags_RootSignatureOnly",
    "DxcValidatorFlags_ModuleOnly",
    "DxcValidatorFlags_ValidMask",
    "DxcVersionInfoFlags_None",
    "DxcVersionInfoFlags_Debug",
    "DxcVersionInfoFlags_Internal",
    "CLSID_DxcCompiler",
    "CLSID_DxcLinker",
    "CLSID_DxcDiaDataSource",
    "CLSID_DxcCompilerArgs",
    "CLSID_DxcLibrary",
    "CLSID_DxcValidator",
    "CLSID_DxcAssembler",
    "CLSID_DxcContainerReflection",
    "CLSID_DxcOptimizer",
    "CLSID_DxcContainerBuilder",
    "CLSID_DxcPdbUtils",
    "DXC_CP",
    "DXC_CP_ACP",
    "DXC_CP_UTF16",
    "DXC_CP_UTF8",
    "DxcCreateInstanceProc",
    "DxcCreateInstance2Proc",
    "DxcShaderHash",
    "IDxcBlob",
    "IDxcBlobEncoding",
    "IDxcBlobUtf16",
    "IDxcBlobUtf8",
    "IDxcIncludeHandler",
    "DxcBuffer",
    "DxcDefine",
    "IDxcCompilerArgs",
    "IDxcLibrary",
    "IDxcOperationResult",
    "IDxcCompiler",
    "IDxcCompiler2",
    "IDxcLinker",
    "IDxcUtils",
    "DXC_OUT_KIND",
    "DXC_OUT_NONE",
    "DXC_OUT_OBJECT",
    "DXC_OUT_ERRORS",
    "DXC_OUT_PDB",
    "DXC_OUT_SHADER_HASH",
    "DXC_OUT_DISASSEMBLY",
    "DXC_OUT_HLSL",
    "DXC_OUT_TEXT",
    "DXC_OUT_REFLECTION",
    "DXC_OUT_ROOT_SIGNATURE",
    "DXC_OUT_EXTRA_OUTPUTS",
    "DXC_OUT_FORCE_DWORD",
    "IDxcResult",
    "IDxcExtraOutputs",
    "IDxcCompiler3",
    "IDxcValidator",
    "IDxcValidator2",
    "IDxcContainerBuilder",
    "IDxcAssembler",
    "IDxcContainerReflection",
    "IDxcOptimizerPass",
    "IDxcOptimizer",
    "IDxcVersionInfo",
    "IDxcVersionInfo2",
    "IDxcVersionInfo3",
    "DxcArgPair",
    "IDxcPdbUtils",
    "DxcCreateInstance",
    "DxcCreateInstance2",
]
