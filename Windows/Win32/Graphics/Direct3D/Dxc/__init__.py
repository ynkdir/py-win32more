from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.Graphics.Direct3D.Dxc
import Windows.Win32.System.Com
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
DXC_HASHFLAG_INCLUDES_SOURCE: UInt32 = 1
DXC_ARG_DEBUG: String = '-Zi'
DXC_ARG_SKIP_VALIDATION: String = '-Vd'
DXC_ARG_SKIP_OPTIMIZATIONS: String = '-Od'
DXC_ARG_PACK_MATRIX_ROW_MAJOR: String = '-Zpr'
DXC_ARG_PACK_MATRIX_COLUMN_MAJOR: String = '-Zpc'
DXC_ARG_AVOID_FLOW_CONTROL: String = '-Gfa'
DXC_ARG_PREFER_FLOW_CONTROL: String = '-Gfp'
DXC_ARG_ENABLE_STRICTNESS: String = '-Ges'
DXC_ARG_ENABLE_BACKWARDS_COMPATIBILITY: String = '-Gec'
DXC_ARG_IEEE_STRICTNESS: String = '-Gis'
DXC_ARG_OPTIMIZATION_LEVEL0: String = '-O0'
DXC_ARG_OPTIMIZATION_LEVEL1: String = '-O1'
DXC_ARG_OPTIMIZATION_LEVEL2: String = '-O2'
DXC_ARG_OPTIMIZATION_LEVEL3: String = '-O3'
DXC_ARG_WARNINGS_ARE_ERRORS: String = '-WX'
DXC_ARG_RESOURCES_MAY_ALIAS: String = '-res_may_alias'
DXC_ARG_ALL_RESOURCES_BOUND: String = '-all_resources_bound'
DXC_ARG_DEBUG_NAME_FOR_SOURCE: String = '-Zss'
DXC_ARG_DEBUG_NAME_FOR_BINARY: String = '-Zsb'
DXC_EXTRA_OUTPUT_NAME_STDOUT: String = '*stdout*'
DXC_EXTRA_OUTPUT_NAME_STDERR: String = '*stderr*'
DxcValidatorFlags_Default: UInt32 = 0
DxcValidatorFlags_InPlaceEdit: UInt32 = 1
DxcValidatorFlags_RootSignatureOnly: UInt32 = 2
DxcValidatorFlags_ModuleOnly: UInt32 = 4
DxcValidatorFlags_ValidMask: UInt32 = 7
DxcVersionInfoFlags_None: UInt32 = 0
DxcVersionInfoFlags_Debug: UInt32 = 1
DxcVersionInfoFlags_Internal: UInt32 = 2
CLSID_DxcCompiler: Guid = Guid('{73e22d93-e6ce-47f3-b5bf-f0664f39c1b0}')
CLSID_DxcLinker: Guid = Guid('{ef6a8087-b0ea-4d56-9e45-d07e1a8b7806}')
CLSID_DxcDiaDataSource: Guid = Guid('{cd1f6b73-2ab0-484d-8edc-ebe7a43ca09f}')
CLSID_DxcCompilerArgs: Guid = Guid('{3e56ae82-224d-470f-a1a1-fe3016ee9f9d}')
CLSID_DxcLibrary: Guid = Guid('{6245d6af-66e0-48fd-80b4-4d271796748c}')
CLSID_DxcValidator: Guid = Guid('{8ca3e215-f728-4cf3-8cdd-88af917587a1}')
CLSID_DxcAssembler: Guid = Guid('{d728db68-f903-4f80-94cd-dccf76ec7151}')
CLSID_DxcContainerReflection: Guid = Guid('{b9f54489-55b8-400c-ba3a-1675e4728b91}')
CLSID_DxcOptimizer: Guid = Guid('{ae2cd79f-cc22-453f-9b6b-b124e7a5204c}')
CLSID_DxcContainerBuilder: Guid = Guid('{94134294-411f-4574-b4d0-8741e25240d2}')
CLSID_DxcPdbUtils: Guid = Guid('{54621dfb-f2ce-457e-ae8c-ec355faeec7c}')
@winfunctype('dxcompiler.dll')
def DxcCreateInstance(rclsid: POINTER(Guid), riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('dxcompiler.dll')
def DxcCreateInstance2(pMalloc: Windows.Win32.System.Com.IMalloc_head, rclsid: POINTER(Guid), riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
DXC_CP = UInt32
DXC_CP_ACP: DXC_CP = 0
DXC_CP_UTF16: DXC_CP = 1200
DXC_CP_UTF8: DXC_CP = 65001
DXC_OUT_KIND = Int32
DXC_OUT_NONE: DXC_OUT_KIND = 0
DXC_OUT_OBJECT: DXC_OUT_KIND = 1
DXC_OUT_ERRORS: DXC_OUT_KIND = 2
DXC_OUT_PDB: DXC_OUT_KIND = 3
DXC_OUT_SHADER_HASH: DXC_OUT_KIND = 4
DXC_OUT_DISASSEMBLY: DXC_OUT_KIND = 5
DXC_OUT_HLSL: DXC_OUT_KIND = 6
DXC_OUT_TEXT: DXC_OUT_KIND = 7
DXC_OUT_REFLECTION: DXC_OUT_KIND = 8
DXC_OUT_ROOT_SIGNATURE: DXC_OUT_KIND = 9
DXC_OUT_EXTRA_OUTPUTS: DXC_OUT_KIND = 10
DXC_OUT_FORCE_DWORD: DXC_OUT_KIND = -1
class DxcArgPair(EasyCastStructure):
    pName: Windows.Win32.Foundation.PWSTR
    pValue: Windows.Win32.Foundation.PWSTR
class DxcBuffer(EasyCastStructure):
    Ptr: c_void_p
    Size: UIntPtr
    Encoding: UInt32
@winfunctype_pointer
def DxcCreateInstance2Proc(pMalloc: Windows.Win32.System.Com.IMalloc_head, rclsid: POINTER(Guid), riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def DxcCreateInstanceProc(rclsid: POINTER(Guid), riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class DxcDefine(EasyCastStructure):
    Name: Windows.Win32.Foundation.PWSTR
    Value: Windows.Win32.Foundation.PWSTR
class DxcShaderHash(EasyCastStructure):
    Flags: UInt32
    HashDigest: Byte * 16
class IDxcAssembler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{091f7a26-1c1f-4948-904b-e6e3a8a771d5}')
    @commethod(3)
    def AssembleToContainer(self, pShader: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head, ppResult: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcOperationResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDxcBlob(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8ba5fb08-5195-40e2-ac58-0d989c3a0102}')
    @commethod(3)
    def GetBufferPointer(self) -> c_void_p: ...
    @commethod(4)
    def GetBufferSize(self) -> UIntPtr: ...
class IDxcBlobEncoding(ComPtr):
    extends: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob
    _iid_ = Guid('{7241d424-2646-4191-97c0-98e96e42fc68}')
    @commethod(5)
    def GetEncoding(self, pKnown: POINTER(Windows.Win32.Foundation.BOOL), pCodePage: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.DXC_CP)) -> Windows.Win32.Foundation.HRESULT: ...
class IDxcBlobUtf16(ComPtr):
    extends: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlobEncoding
    _iid_ = Guid('{a3f84eab-0faa-497e-a39c-ee6ed60b2d84}')
    @commethod(6)
    def GetStringPointer(self) -> Windows.Win32.Foundation.PWSTR: ...
    @commethod(7)
    def GetStringLength(self) -> UIntPtr: ...
class IDxcBlobUtf8(ComPtr):
    extends: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlobEncoding
    _iid_ = Guid('{3da636c9-ba71-4024-a301-30cbf125305b}')
    @commethod(6)
    def GetStringPointer(self) -> Windows.Win32.Foundation.PSTR: ...
    @commethod(7)
    def GetStringLength(self) -> UIntPtr: ...
class IDxcCompiler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8c210bf3-011f-4422-8d70-6f9acb8db617}')
    @commethod(3)
    def Compile(self, pSource: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head, pSourceName: Windows.Win32.Foundation.PWSTR, pEntryPoint: Windows.Win32.Foundation.PWSTR, pTargetProfile: Windows.Win32.Foundation.PWSTR, pArguments: POINTER(Windows.Win32.Foundation.PWSTR), argCount: UInt32, pDefines: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.DxcDefine_head), defineCount: UInt32, pIncludeHandler: Windows.Win32.Graphics.Direct3D.Dxc.IDxcIncludeHandler_head, ppResult: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcOperationResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Preprocess(self, pSource: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head, pSourceName: Windows.Win32.Foundation.PWSTR, pArguments: POINTER(Windows.Win32.Foundation.PWSTR), argCount: UInt32, pDefines: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.DxcDefine_head), defineCount: UInt32, pIncludeHandler: Windows.Win32.Graphics.Direct3D.Dxc.IDxcIncludeHandler_head, ppResult: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcOperationResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Disassemble(self, pSource: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head, ppDisassembly: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlobEncoding_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDxcCompiler2(ComPtr):
    extends: Windows.Win32.Graphics.Direct3D.Dxc.IDxcCompiler
    _iid_ = Guid('{a005a9d9-b8bb-4594-b5c9-0e633bec4d37}')
    @commethod(6)
    def CompileWithDebug(self, pSource: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head, pSourceName: Windows.Win32.Foundation.PWSTR, pEntryPoint: Windows.Win32.Foundation.PWSTR, pTargetProfile: Windows.Win32.Foundation.PWSTR, pArguments: POINTER(Windows.Win32.Foundation.PWSTR), argCount: UInt32, pDefines: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.DxcDefine_head), defineCount: UInt32, pIncludeHandler: Windows.Win32.Graphics.Direct3D.Dxc.IDxcIncludeHandler_head, ppResult: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcOperationResult_head), ppDebugBlobName: POINTER(Windows.Win32.Foundation.PWSTR), ppDebugBlob: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDxcCompiler3(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{228b4687-5a6a-4730-900c-9702b2203f54}')
    @commethod(3)
    def Compile(self, pSource: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.DxcBuffer_head), pArguments: POINTER(Windows.Win32.Foundation.PWSTR), argCount: UInt32, pIncludeHandler: Windows.Win32.Graphics.Direct3D.Dxc.IDxcIncludeHandler_head, riid: POINTER(Guid), ppResult: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Disassemble(self, pObject: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.DxcBuffer_head), riid: POINTER(Guid), ppResult: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IDxcCompilerArgs(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{73effe2a-70dc-45f8-9690-eff64c02429d}')
    @commethod(3)
    def GetArguments(self) -> POINTER(Windows.Win32.Foundation.PWSTR): ...
    @commethod(4)
    def GetCount(self) -> UInt32: ...
    @commethod(5)
    def AddArguments(self, pArguments: POINTER(Windows.Win32.Foundation.PWSTR), argCount: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AddArgumentsUTF8(self, pArguments: POINTER(Windows.Win32.Foundation.PSTR), argCount: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def AddDefines(self, pDefines: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.DxcDefine_head), defineCount: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IDxcContainerBuilder(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{334b1f50-2292-4b35-99a1-25588d8c17fe}')
    @commethod(3)
    def Load(self, pDxilContainerHeader: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddPart(self, fourCC: UInt32, pSource: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RemovePart(self, fourCC: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SerializeContainer(self, ppResult: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcOperationResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDxcContainerReflection(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d2c21b26-8350-4bdc-976a-331ce6f4c54c}')
    @commethod(3)
    def Load(self, pContainer: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPartCount(self, pResult: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPartKind(self, idx: UInt32, pResult: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPartContent(self, idx: UInt32, ppResult: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def FindFirstPartKind(self, kind: UInt32, pResult: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetPartReflection(self, idx: UInt32, iid: POINTER(Guid), ppvObject: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IDxcExtraOutputs(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{319b37a2-a5c2-494a-a5de-4801b2faf989}')
    @commethod(3)
    def GetOutputCount(self) -> UInt32: ...
    @commethod(4)
    def GetOutput(self, uIndex: UInt32, iid: POINTER(Guid), ppvObject: POINTER(c_void_p), ppOutputType: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlobUtf16_head), ppOutputName: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlobUtf16_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDxcIncludeHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7f61fc7d-950d-467f-b3e3-3c02fb49187c}')
    @commethod(3)
    def LoadSource(self, pFilename: Windows.Win32.Foundation.PWSTR, ppIncludeSource: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDxcLibrary(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e5204dc7-d18c-4c3c-bdfb-851673980fe7}')
    @commethod(3)
    def SetMalloc(self, pMalloc: Windows.Win32.System.Com.IMalloc_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateBlobFromBlob(self, pBlob: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head, offset: UInt32, length: UInt32, ppResult: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateBlobFromFile(self, pFileName: Windows.Win32.Foundation.PWSTR, codePage: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.DXC_CP), pBlobEncoding: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlobEncoding_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateBlobWithEncodingFromPinned(self, pText: c_void_p, size: UInt32, codePage: Windows.Win32.Graphics.Direct3D.Dxc.DXC_CP, pBlobEncoding: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlobEncoding_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateBlobWithEncodingOnHeapCopy(self, pText: c_void_p, size: UInt32, codePage: Windows.Win32.Graphics.Direct3D.Dxc.DXC_CP, pBlobEncoding: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlobEncoding_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CreateBlobWithEncodingOnMalloc(self, pText: c_void_p, pIMalloc: Windows.Win32.System.Com.IMalloc_head, size: UInt32, codePage: Windows.Win32.Graphics.Direct3D.Dxc.DXC_CP, pBlobEncoding: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlobEncoding_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CreateIncludeHandler(self, ppResult: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcIncludeHandler_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CreateStreamFromBlobReadOnly(self, pBlob: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head, ppStream: POINTER(Windows.Win32.System.Com.IStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetBlobAsUtf8(self, pBlob: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head, pBlobEncoding: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlobEncoding_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetBlobAsUtf16(self, pBlob: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head, pBlobEncoding: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlobEncoding_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDxcLinker(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f1b5be2a-62dd-4327-a1c2-42ac1e1e78e6}')
    @commethod(3)
    def RegisterLibrary(self, pLibName: Windows.Win32.Foundation.PWSTR, pLib: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Link(self, pEntryName: Windows.Win32.Foundation.PWSTR, pTargetProfile: Windows.Win32.Foundation.PWSTR, pLibNames: POINTER(Windows.Win32.Foundation.PWSTR), libCount: UInt32, pArguments: POINTER(Windows.Win32.Foundation.PWSTR), argCount: UInt32, ppResult: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcOperationResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDxcOperationResult(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{cedb484a-d4e9-445a-b991-ca21ca157dc2}')
    @commethod(3)
    def GetStatus(self, pStatus: POINTER(Windows.Win32.Foundation.HRESULT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetResult(self, ppResult: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetErrorBuffer(self, ppErrors: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlobEncoding_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDxcOptimizer(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{25740e2e-9cba-401b-9119-4fb42f39f270}')
    @commethod(3)
    def GetAvailablePassCount(self, pCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAvailablePass(self, index: UInt32, ppResult: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcOptimizerPass_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RunOptimizer(self, pBlob: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head, ppOptions: POINTER(Windows.Win32.Foundation.PWSTR), optionCount: UInt32, pOutputModule: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head), ppOutputText: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlobEncoding_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDxcOptimizerPass(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ae2cd79f-cc22-453f-9b6b-b124e7a5204c}')
    @commethod(3)
    def GetOptionName(self, ppResult: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDescription(self, ppResult: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetOptionArgCount(self, pCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetOptionArgName(self, argIndex: UInt32, ppResult: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetOptionArgDescription(self, argIndex: UInt32, ppResult: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IDxcPdbUtils(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e6c9647e-9d6a-4c3b-b94c-524b5a6c343d}')
    @commethod(3)
    def Load(self, pPdbOrDxil: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSourceCount(self, pCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSource(self, uIndex: UInt32, ppResult: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlobEncoding_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSourceName(self, uIndex: UInt32, pResult: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetFlagCount(self, pCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetFlag(self, uIndex: UInt32, pResult: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetArgCount(self, pCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetArg(self, uIndex: UInt32, pResult: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetArgPairCount(self, pCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetArgPair(self, uIndex: UInt32, pName: POINTER(Windows.Win32.Foundation.BSTR), pValue: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetDefineCount(self, pCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetDefine(self, uIndex: UInt32, pResult: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetTargetProfile(self, pResult: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetEntryPoint(self, pResult: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetMainFileName(self, pResult: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetHash(self, ppResult: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetName(self, pResult: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def IsFullPDB(self) -> Windows.Win32.Foundation.BOOL: ...
    @commethod(21)
    def GetFullPDB(self, ppFullPDB: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetVersionInfo(self, ppVersionInfo: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcVersionInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetCompiler(self, pCompiler: Windows.Win32.Graphics.Direct3D.Dxc.IDxcCompiler3_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def CompileForFullPDB(self, ppResult: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def OverrideArgs(self, pArgPairs: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.DxcArgPair_head), uNumArgPairs: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def OverrideRootSignature(self, pRootSignature: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IDxcResult(ComPtr):
    extends: Windows.Win32.Graphics.Direct3D.Dxc.IDxcOperationResult
    _iid_ = Guid('{58346cda-dde7-4497-9461-6f87af5e0659}')
    @commethod(6)
    def HasOutput(self, dxcOutKind: Windows.Win32.Graphics.Direct3D.Dxc.DXC_OUT_KIND) -> Windows.Win32.Foundation.BOOL: ...
    @commethod(7)
    def GetOutput(self, dxcOutKind: Windows.Win32.Graphics.Direct3D.Dxc.DXC_OUT_KIND, iid: POINTER(Guid), ppvObject: POINTER(c_void_p), ppOutputName: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlobUtf16_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetNumOutputs(self) -> UInt32: ...
    @commethod(9)
    def GetOutputByIndex(self, Index: UInt32) -> Windows.Win32.Graphics.Direct3D.Dxc.DXC_OUT_KIND: ...
    @commethod(10)
    def PrimaryOutput(self) -> Windows.Win32.Graphics.Direct3D.Dxc.DXC_OUT_KIND: ...
class IDxcUtils(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4605c4cb-2019-492a-ada4-65f20bb7d67f}')
    @commethod(3)
    def CreateBlobFromBlob(self, pBlob: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head, offset: UInt32, length: UInt32, ppResult: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateBlobFromPinned(self, pData: c_void_p, size: UInt32, codePage: Windows.Win32.Graphics.Direct3D.Dxc.DXC_CP, pBlobEncoding: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlobEncoding_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MoveToBlob(self, pData: c_void_p, pIMalloc: Windows.Win32.System.Com.IMalloc_head, size: UInt32, codePage: Windows.Win32.Graphics.Direct3D.Dxc.DXC_CP, pBlobEncoding: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlobEncoding_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateBlob(self, pData: c_void_p, size: UInt32, codePage: Windows.Win32.Graphics.Direct3D.Dxc.DXC_CP, pBlobEncoding: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlobEncoding_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def LoadFile(self, pFileName: Windows.Win32.Foundation.PWSTR, pCodePage: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.DXC_CP), pBlobEncoding: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlobEncoding_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CreateReadOnlyStreamFromBlob(self, pBlob: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head, ppStream: POINTER(Windows.Win32.System.Com.IStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CreateDefaultIncludeHandler(self, ppResult: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcIncludeHandler_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetBlobAsUtf8(self, pBlob: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head, pBlobEncoding: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlobUtf8_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetBlobAsUtf16(self, pBlob: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head, pBlobEncoding: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlobUtf16_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetDxilContainerPart(self, pShader: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.DxcBuffer_head), DxcPart: UInt32, ppPartData: POINTER(c_void_p), pPartSizeInBytes: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def CreateReflection(self, pData: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.DxcBuffer_head), iid: POINTER(Guid), ppvReflection: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def BuildArguments(self, pSourceName: Windows.Win32.Foundation.PWSTR, pEntryPoint: Windows.Win32.Foundation.PWSTR, pTargetProfile: Windows.Win32.Foundation.PWSTR, pArguments: POINTER(Windows.Win32.Foundation.PWSTR), argCount: UInt32, pDefines: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.DxcDefine_head), defineCount: UInt32, ppArgs: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcCompilerArgs_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetPDBContents(self, pPDBBlob: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head, ppHash: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head), ppContainer: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDxcValidator(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a6e82bd2-1fd7-4826-9811-2857e797f49a}')
    @commethod(3)
    def Validate(self, pShader: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head, Flags: UInt32, ppResult: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcOperationResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDxcValidator2(ComPtr):
    extends: Windows.Win32.Graphics.Direct3D.Dxc.IDxcValidator
    _iid_ = Guid('{458e1fd1-b1b2-4750-a6e1-9c10f03bed92}')
    @commethod(4)
    def ValidateWithDebug(self, pShader: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head, Flags: UInt32, pOptDebugBitcode: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.DxcBuffer_head), ppResult: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcOperationResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDxcVersionInfo(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b04f5b50-2059-4f12-a8ff-a1e0cde1cc7e}')
    @commethod(3)
    def GetVersion(self, pMajor: POINTER(UInt32), pMinor: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFlags(self, pFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IDxcVersionInfo2(ComPtr):
    extends: Windows.Win32.Graphics.Direct3D.Dxc.IDxcVersionInfo
    _iid_ = Guid('{fb6904c4-42f0-4b62-9c46-983af7da7c83}')
    @commethod(5)
    def GetCommitInfo(self, pCommitCount: POINTER(UInt32), pCommitHash: POINTER(POINTER(SByte))) -> Windows.Win32.Foundation.HRESULT: ...
class IDxcVersionInfo3(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5e13e843-9d25-473c-9ad2-03b2d0b44b1e}')
    @commethod(3)
    def GetCustomVersionString(self, pVersionString: POINTER(POINTER(SByte))) -> Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'DxcArgPair')
make_head(_module, 'DxcBuffer')
make_head(_module, 'DxcCreateInstance2Proc')
make_head(_module, 'DxcCreateInstanceProc')
make_head(_module, 'DxcDefine')
make_head(_module, 'DxcShaderHash')
make_head(_module, 'IDxcAssembler')
make_head(_module, 'IDxcBlob')
make_head(_module, 'IDxcBlobEncoding')
make_head(_module, 'IDxcBlobUtf16')
make_head(_module, 'IDxcBlobUtf8')
make_head(_module, 'IDxcCompiler')
make_head(_module, 'IDxcCompiler2')
make_head(_module, 'IDxcCompiler3')
make_head(_module, 'IDxcCompilerArgs')
make_head(_module, 'IDxcContainerBuilder')
make_head(_module, 'IDxcContainerReflection')
make_head(_module, 'IDxcExtraOutputs')
make_head(_module, 'IDxcIncludeHandler')
make_head(_module, 'IDxcLibrary')
make_head(_module, 'IDxcLinker')
make_head(_module, 'IDxcOperationResult')
make_head(_module, 'IDxcOptimizer')
make_head(_module, 'IDxcOptimizerPass')
make_head(_module, 'IDxcPdbUtils')
make_head(_module, 'IDxcResult')
make_head(_module, 'IDxcUtils')
make_head(_module, 'IDxcValidator')
make_head(_module, 'IDxcValidator2')
make_head(_module, 'IDxcVersionInfo')
make_head(_module, 'IDxcVersionInfo2')
make_head(_module, 'IDxcVersionInfo3')
