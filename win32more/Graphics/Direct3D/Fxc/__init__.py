from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Graphics.Direct3D
import win32more.Graphics.Direct3D.Fxc
import win32more.Graphics.Direct3D10
import win32more.Graphics.Direct3D11
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        if name in _arch_optional:
            return None
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
D3DCOMPILER_DLL_W: String = 'd3dcompiler_47.dll'
D3DCOMPILER_DLL_A: String = 'd3dcompiler_47.dll'
D3D_COMPILER_VERSION: UInt32 = 47
D3DCOMPILE_DEBUG: UInt32 = 1
D3DCOMPILE_SKIP_VALIDATION: UInt32 = 2
D3DCOMPILE_SKIP_OPTIMIZATION: UInt32 = 4
D3DCOMPILE_PACK_MATRIX_ROW_MAJOR: UInt32 = 8
D3DCOMPILE_PACK_MATRIX_COLUMN_MAJOR: UInt32 = 16
D3DCOMPILE_PARTIAL_PRECISION: UInt32 = 32
D3DCOMPILE_FORCE_VS_SOFTWARE_NO_OPT: UInt32 = 64
D3DCOMPILE_FORCE_PS_SOFTWARE_NO_OPT: UInt32 = 128
D3DCOMPILE_NO_PRESHADER: UInt32 = 256
D3DCOMPILE_AVOID_FLOW_CONTROL: UInt32 = 512
D3DCOMPILE_PREFER_FLOW_CONTROL: UInt32 = 1024
D3DCOMPILE_ENABLE_STRICTNESS: UInt32 = 2048
D3DCOMPILE_ENABLE_BACKWARDS_COMPATIBILITY: UInt32 = 4096
D3DCOMPILE_IEEE_STRICTNESS: UInt32 = 8192
D3DCOMPILE_OPTIMIZATION_LEVEL0: UInt32 = 16384
D3DCOMPILE_OPTIMIZATION_LEVEL1: UInt32 = 0
D3DCOMPILE_OPTIMIZATION_LEVEL3: UInt32 = 32768
D3DCOMPILE_RESERVED16: UInt32 = 65536
D3DCOMPILE_RESERVED17: UInt32 = 131072
D3DCOMPILE_WARNINGS_ARE_ERRORS: UInt32 = 262144
D3DCOMPILE_RESOURCES_MAY_ALIAS: UInt32 = 524288
D3DCOMPILE_ENABLE_UNBOUNDED_DESCRIPTOR_TABLES: UInt32 = 1048576
D3DCOMPILE_ALL_RESOURCES_BOUND: UInt32 = 2097152
D3DCOMPILE_DEBUG_NAME_FOR_SOURCE: UInt32 = 4194304
D3DCOMPILE_DEBUG_NAME_FOR_BINARY: UInt32 = 8388608
D3DCOMPILE_EFFECT_CHILD_EFFECT: UInt32 = 1
D3DCOMPILE_EFFECT_ALLOW_SLOW_OPS: UInt32 = 2
D3DCOMPILE_FLAGS2_FORCE_ROOT_SIGNATURE_LATEST: UInt32 = 0
D3DCOMPILE_FLAGS2_FORCE_ROOT_SIGNATURE_1_0: UInt32 = 16
D3DCOMPILE_FLAGS2_FORCE_ROOT_SIGNATURE_1_1: UInt32 = 32
D3DCOMPILE_SECDATA_MERGE_UAV_SLOTS: UInt32 = 1
D3DCOMPILE_SECDATA_PRESERVE_TEMPLATE_SLOTS: UInt32 = 2
D3DCOMPILE_SECDATA_REQUIRE_TEMPLATE_MATCH: UInt32 = 4
D3D_DISASM_ENABLE_COLOR_CODE: UInt32 = 1
D3D_DISASM_ENABLE_DEFAULT_VALUE_PRINTS: UInt32 = 2
D3D_DISASM_ENABLE_INSTRUCTION_NUMBERING: UInt32 = 4
D3D_DISASM_ENABLE_INSTRUCTION_CYCLE: UInt32 = 8
D3D_DISASM_DISABLE_DEBUG_INFO: UInt32 = 16
D3D_DISASM_ENABLE_INSTRUCTION_OFFSET: UInt32 = 32
D3D_DISASM_INSTRUCTION_ONLY: UInt32 = 64
D3D_DISASM_PRINT_HEX_LITERALS: UInt32 = 128
D3D_GET_INST_OFFSETS_INCLUDE_NON_EXECUTABLE: UInt32 = 1
D3D_COMPRESS_SHADER_KEEP_ALL_PARTS: UInt32 = 1
@winfunctype('D3DCOMPILER_47.dll')
def D3DReadFileToBlob(pFileName: win32more.Foundation.PWSTR, ppContents: POINTER(win32more.Graphics.Direct3D.ID3DBlob_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DWriteBlobToFile(pBlob: win32more.Graphics.Direct3D.ID3DBlob_head, pFileName: win32more.Foundation.PWSTR, bOverwrite: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DCompile(pSrcData: c_void_p, SrcDataSize: UIntPtr, pSourceName: win32more.Foundation.PSTR, pDefines: POINTER(win32more.Graphics.Direct3D.D3D_SHADER_MACRO_head), pInclude: win32more.Graphics.Direct3D.ID3DInclude_head, pEntrypoint: win32more.Foundation.PSTR, pTarget: win32more.Foundation.PSTR, Flags1: UInt32, Flags2: UInt32, ppCode: POINTER(win32more.Graphics.Direct3D.ID3DBlob_head), ppErrorMsgs: POINTER(win32more.Graphics.Direct3D.ID3DBlob_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DCompile2(pSrcData: c_void_p, SrcDataSize: UIntPtr, pSourceName: win32more.Foundation.PSTR, pDefines: POINTER(win32more.Graphics.Direct3D.D3D_SHADER_MACRO_head), pInclude: win32more.Graphics.Direct3D.ID3DInclude_head, pEntrypoint: win32more.Foundation.PSTR, pTarget: win32more.Foundation.PSTR, Flags1: UInt32, Flags2: UInt32, SecondaryDataFlags: UInt32, pSecondaryData: c_void_p, SecondaryDataSize: UIntPtr, ppCode: POINTER(win32more.Graphics.Direct3D.ID3DBlob_head), ppErrorMsgs: POINTER(win32more.Graphics.Direct3D.ID3DBlob_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DCompileFromFile(pFileName: win32more.Foundation.PWSTR, pDefines: POINTER(win32more.Graphics.Direct3D.D3D_SHADER_MACRO_head), pInclude: win32more.Graphics.Direct3D.ID3DInclude_head, pEntrypoint: win32more.Foundation.PSTR, pTarget: win32more.Foundation.PSTR, Flags1: UInt32, Flags2: UInt32, ppCode: POINTER(win32more.Graphics.Direct3D.ID3DBlob_head), ppErrorMsgs: POINTER(win32more.Graphics.Direct3D.ID3DBlob_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DPreprocess(pSrcData: c_void_p, SrcDataSize: UIntPtr, pSourceName: win32more.Foundation.PSTR, pDefines: POINTER(win32more.Graphics.Direct3D.D3D_SHADER_MACRO_head), pInclude: win32more.Graphics.Direct3D.ID3DInclude_head, ppCodeText: POINTER(win32more.Graphics.Direct3D.ID3DBlob_head), ppErrorMsgs: POINTER(win32more.Graphics.Direct3D.ID3DBlob_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DGetDebugInfo(pSrcData: c_void_p, SrcDataSize: UIntPtr, ppDebugInfo: POINTER(win32more.Graphics.Direct3D.ID3DBlob_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DReflect(pSrcData: c_void_p, SrcDataSize: UIntPtr, pInterface: POINTER(Guid), ppReflector: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DReflectLibrary(pSrcData: c_void_p, SrcDataSize: UIntPtr, riid: POINTER(Guid), ppReflector: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DDisassemble(pSrcData: c_void_p, SrcDataSize: UIntPtr, Flags: UInt32, szComments: win32more.Foundation.PSTR, ppDisassembly: POINTER(win32more.Graphics.Direct3D.ID3DBlob_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DDisassembleRegion(pSrcData: c_void_p, SrcDataSize: UIntPtr, Flags: UInt32, szComments: win32more.Foundation.PSTR, StartByteOffset: UIntPtr, NumInsts: UIntPtr, pFinishByteOffset: POINTER(UIntPtr), ppDisassembly: POINTER(win32more.Graphics.Direct3D.ID3DBlob_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DCreateLinker(ppLinker: POINTER(win32more.Graphics.Direct3D11.ID3D11Linker_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DLoadModule(pSrcData: c_void_p, cbSrcDataSize: UIntPtr, ppModule: POINTER(win32more.Graphics.Direct3D11.ID3D11Module_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DCreateFunctionLinkingGraph(uFlags: UInt32, ppFunctionLinkingGraph: POINTER(win32more.Graphics.Direct3D11.ID3D11FunctionLinkingGraph_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DGetTraceInstructionOffsets(pSrcData: c_void_p, SrcDataSize: UIntPtr, Flags: UInt32, StartInstIndex: UIntPtr, NumInsts: UIntPtr, pOffsets: POINTER(UIntPtr), pTotalInsts: POINTER(UIntPtr)) -> win32more.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DGetInputSignatureBlob(pSrcData: c_void_p, SrcDataSize: UIntPtr, ppSignatureBlob: POINTER(win32more.Graphics.Direct3D.ID3DBlob_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DGetOutputSignatureBlob(pSrcData: c_void_p, SrcDataSize: UIntPtr, ppSignatureBlob: POINTER(win32more.Graphics.Direct3D.ID3DBlob_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DGetInputAndOutputSignatureBlob(pSrcData: c_void_p, SrcDataSize: UIntPtr, ppSignatureBlob: POINTER(win32more.Graphics.Direct3D.ID3DBlob_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DStripShader(pShaderBytecode: c_void_p, BytecodeLength: UIntPtr, uStripFlags: UInt32, ppStrippedBlob: POINTER(win32more.Graphics.Direct3D.ID3DBlob_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DGetBlobPart(pSrcData: c_void_p, SrcDataSize: UIntPtr, Part: win32more.Graphics.Direct3D.Fxc.D3D_BLOB_PART, Flags: UInt32, ppPart: POINTER(win32more.Graphics.Direct3D.ID3DBlob_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DSetBlobPart(pSrcData: c_void_p, SrcDataSize: UIntPtr, Part: win32more.Graphics.Direct3D.Fxc.D3D_BLOB_PART, Flags: UInt32, pPart: c_void_p, PartSize: UIntPtr, ppNewShader: POINTER(win32more.Graphics.Direct3D.ID3DBlob_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DCreateBlob(Size: UIntPtr, ppBlob: POINTER(win32more.Graphics.Direct3D.ID3DBlob_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DCompressShaders(uNumShaders: UInt32, pShaderData: POINTER(win32more.Graphics.Direct3D.Fxc.D3D_SHADER_DATA_head), uFlags: UInt32, ppCompressedData: POINTER(win32more.Graphics.Direct3D.ID3DBlob_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DDecompressShaders(pSrcData: c_void_p, SrcDataSize: UIntPtr, uNumShaders: UInt32, uStartIndex: UInt32, pIndices: POINTER(UInt32), uFlags: UInt32, ppShaders: POINTER(win32more.Graphics.Direct3D.ID3DBlob_head), pTotalShaders: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DDisassemble10Effect(pEffect: win32more.Graphics.Direct3D10.ID3D10Effect_head, Flags: UInt32, ppDisassembly: POINTER(win32more.Graphics.Direct3D.ID3DBlob_head)) -> win32more.Foundation.HRESULT: ...
D3DCOMPILER_STRIP_FLAGS = Int32
D3DCOMPILER_STRIP_REFLECTION_DATA: D3DCOMPILER_STRIP_FLAGS = 1
D3DCOMPILER_STRIP_DEBUG_INFO: D3DCOMPILER_STRIP_FLAGS = 2
D3DCOMPILER_STRIP_TEST_BLOBS: D3DCOMPILER_STRIP_FLAGS = 4
D3DCOMPILER_STRIP_PRIVATE_DATA: D3DCOMPILER_STRIP_FLAGS = 8
D3DCOMPILER_STRIP_ROOT_SIGNATURE: D3DCOMPILER_STRIP_FLAGS = 16
D3DCOMPILER_STRIP_FORCE_DWORD: D3DCOMPILER_STRIP_FLAGS = 2147483647
D3D_BLOB_PART = Int32
D3D_BLOB_INPUT_SIGNATURE_BLOB: D3D_BLOB_PART = 0
D3D_BLOB_OUTPUT_SIGNATURE_BLOB: D3D_BLOB_PART = 1
D3D_BLOB_INPUT_AND_OUTPUT_SIGNATURE_BLOB: D3D_BLOB_PART = 2
D3D_BLOB_PATCH_CONSTANT_SIGNATURE_BLOB: D3D_BLOB_PART = 3
D3D_BLOB_ALL_SIGNATURE_BLOB: D3D_BLOB_PART = 4
D3D_BLOB_DEBUG_INFO: D3D_BLOB_PART = 5
D3D_BLOB_LEGACY_SHADER: D3D_BLOB_PART = 6
D3D_BLOB_XNA_PREPASS_SHADER: D3D_BLOB_PART = 7
D3D_BLOB_XNA_SHADER: D3D_BLOB_PART = 8
D3D_BLOB_PDB: D3D_BLOB_PART = 9
D3D_BLOB_PRIVATE_DATA: D3D_BLOB_PART = 10
D3D_BLOB_ROOT_SIGNATURE: D3D_BLOB_PART = 11
D3D_BLOB_DEBUG_NAME: D3D_BLOB_PART = 12
D3D_BLOB_TEST_ALTERNATE_SHADER: D3D_BLOB_PART = 32768
D3D_BLOB_TEST_COMPILE_DETAILS: D3D_BLOB_PART = 32769
D3D_BLOB_TEST_COMPILE_PERF: D3D_BLOB_PART = 32770
D3D_BLOB_TEST_COMPILE_REPORT: D3D_BLOB_PART = 32771
class D3D_SHADER_DATA(Structure):
    pBytecode: c_void_p
    BytecodeLength: UIntPtr
@winfunctype_pointer
def pD3DCompile(pSrcData: c_void_p, SrcDataSize: UIntPtr, pFileName: win32more.Foundation.PSTR, pDefines: POINTER(win32more.Graphics.Direct3D.D3D_SHADER_MACRO_head), pInclude: win32more.Graphics.Direct3D.ID3DInclude_head, pEntrypoint: win32more.Foundation.PSTR, pTarget: win32more.Foundation.PSTR, Flags1: UInt32, Flags2: UInt32, ppCode: POINTER(win32more.Graphics.Direct3D.ID3DBlob_head), ppErrorMsgs: POINTER(win32more.Graphics.Direct3D.ID3DBlob_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def pD3DDisassemble(pSrcData: c_void_p, SrcDataSize: UIntPtr, Flags: UInt32, szComments: win32more.Foundation.PSTR, ppDisassembly: POINTER(win32more.Graphics.Direct3D.ID3DBlob_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def pD3DPreprocess(pSrcData: c_void_p, SrcDataSize: UIntPtr, pFileName: win32more.Foundation.PSTR, pDefines: POINTER(win32more.Graphics.Direct3D.D3D_SHADER_MACRO_head), pInclude: win32more.Graphics.Direct3D.ID3DInclude_head, ppCodeText: POINTER(win32more.Graphics.Direct3D.ID3DBlob_head), ppErrorMsgs: POINTER(win32more.Graphics.Direct3D.ID3DBlob_head)) -> win32more.Foundation.HRESULT: ...
make_head(_module, 'D3D_SHADER_DATA')
make_head(_module, 'pD3DCompile')
make_head(_module, 'pD3DDisassemble')
make_head(_module, 'pD3DPreprocess')
__all__ = [
    "D3DCOMPILER_DLL_A",
    "D3DCOMPILER_DLL_W",
    "D3DCOMPILER_STRIP_DEBUG_INFO",
    "D3DCOMPILER_STRIP_FLAGS",
    "D3DCOMPILER_STRIP_FORCE_DWORD",
    "D3DCOMPILER_STRIP_PRIVATE_DATA",
    "D3DCOMPILER_STRIP_REFLECTION_DATA",
    "D3DCOMPILER_STRIP_ROOT_SIGNATURE",
    "D3DCOMPILER_STRIP_TEST_BLOBS",
    "D3DCOMPILE_ALL_RESOURCES_BOUND",
    "D3DCOMPILE_AVOID_FLOW_CONTROL",
    "D3DCOMPILE_DEBUG",
    "D3DCOMPILE_DEBUG_NAME_FOR_BINARY",
    "D3DCOMPILE_DEBUG_NAME_FOR_SOURCE",
    "D3DCOMPILE_EFFECT_ALLOW_SLOW_OPS",
    "D3DCOMPILE_EFFECT_CHILD_EFFECT",
    "D3DCOMPILE_ENABLE_BACKWARDS_COMPATIBILITY",
    "D3DCOMPILE_ENABLE_STRICTNESS",
    "D3DCOMPILE_ENABLE_UNBOUNDED_DESCRIPTOR_TABLES",
    "D3DCOMPILE_FLAGS2_FORCE_ROOT_SIGNATURE_1_0",
    "D3DCOMPILE_FLAGS2_FORCE_ROOT_SIGNATURE_1_1",
    "D3DCOMPILE_FLAGS2_FORCE_ROOT_SIGNATURE_LATEST",
    "D3DCOMPILE_FORCE_PS_SOFTWARE_NO_OPT",
    "D3DCOMPILE_FORCE_VS_SOFTWARE_NO_OPT",
    "D3DCOMPILE_IEEE_STRICTNESS",
    "D3DCOMPILE_NO_PRESHADER",
    "D3DCOMPILE_OPTIMIZATION_LEVEL0",
    "D3DCOMPILE_OPTIMIZATION_LEVEL1",
    "D3DCOMPILE_OPTIMIZATION_LEVEL3",
    "D3DCOMPILE_PACK_MATRIX_COLUMN_MAJOR",
    "D3DCOMPILE_PACK_MATRIX_ROW_MAJOR",
    "D3DCOMPILE_PARTIAL_PRECISION",
    "D3DCOMPILE_PREFER_FLOW_CONTROL",
    "D3DCOMPILE_RESERVED16",
    "D3DCOMPILE_RESERVED17",
    "D3DCOMPILE_RESOURCES_MAY_ALIAS",
    "D3DCOMPILE_SECDATA_MERGE_UAV_SLOTS",
    "D3DCOMPILE_SECDATA_PRESERVE_TEMPLATE_SLOTS",
    "D3DCOMPILE_SECDATA_REQUIRE_TEMPLATE_MATCH",
    "D3DCOMPILE_SKIP_OPTIMIZATION",
    "D3DCOMPILE_SKIP_VALIDATION",
    "D3DCOMPILE_WARNINGS_ARE_ERRORS",
    "D3DCompile",
    "D3DCompile2",
    "D3DCompileFromFile",
    "D3DCompressShaders",
    "D3DCreateBlob",
    "D3DCreateFunctionLinkingGraph",
    "D3DCreateLinker",
    "D3DDecompressShaders",
    "D3DDisassemble",
    "D3DDisassemble10Effect",
    "D3DDisassembleRegion",
    "D3DGetBlobPart",
    "D3DGetDebugInfo",
    "D3DGetInputAndOutputSignatureBlob",
    "D3DGetInputSignatureBlob",
    "D3DGetOutputSignatureBlob",
    "D3DGetTraceInstructionOffsets",
    "D3DLoadModule",
    "D3DPreprocess",
    "D3DReadFileToBlob",
    "D3DReflect",
    "D3DReflectLibrary",
    "D3DSetBlobPart",
    "D3DStripShader",
    "D3DWriteBlobToFile",
    "D3D_BLOB_ALL_SIGNATURE_BLOB",
    "D3D_BLOB_DEBUG_INFO",
    "D3D_BLOB_DEBUG_NAME",
    "D3D_BLOB_INPUT_AND_OUTPUT_SIGNATURE_BLOB",
    "D3D_BLOB_INPUT_SIGNATURE_BLOB",
    "D3D_BLOB_LEGACY_SHADER",
    "D3D_BLOB_OUTPUT_SIGNATURE_BLOB",
    "D3D_BLOB_PART",
    "D3D_BLOB_PATCH_CONSTANT_SIGNATURE_BLOB",
    "D3D_BLOB_PDB",
    "D3D_BLOB_PRIVATE_DATA",
    "D3D_BLOB_ROOT_SIGNATURE",
    "D3D_BLOB_TEST_ALTERNATE_SHADER",
    "D3D_BLOB_TEST_COMPILE_DETAILS",
    "D3D_BLOB_TEST_COMPILE_PERF",
    "D3D_BLOB_TEST_COMPILE_REPORT",
    "D3D_BLOB_XNA_PREPASS_SHADER",
    "D3D_BLOB_XNA_SHADER",
    "D3D_COMPILER_VERSION",
    "D3D_COMPRESS_SHADER_KEEP_ALL_PARTS",
    "D3D_DISASM_DISABLE_DEBUG_INFO",
    "D3D_DISASM_ENABLE_COLOR_CODE",
    "D3D_DISASM_ENABLE_DEFAULT_VALUE_PRINTS",
    "D3D_DISASM_ENABLE_INSTRUCTION_CYCLE",
    "D3D_DISASM_ENABLE_INSTRUCTION_NUMBERING",
    "D3D_DISASM_ENABLE_INSTRUCTION_OFFSET",
    "D3D_DISASM_INSTRUCTION_ONLY",
    "D3D_DISASM_PRINT_HEX_LITERALS",
    "D3D_GET_INST_OFFSETS_INCLUDE_NON_EXECUTABLE",
    "D3D_SHADER_DATA",
    "pD3DCompile",
    "pD3DDisassemble",
    "pD3DPreprocess",
]
_arch_optional = [
]
