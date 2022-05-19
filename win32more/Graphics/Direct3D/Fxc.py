from win32more import *
import win32more.Foundation
import win32more.Graphics.Direct3D
import win32more.Graphics.Direct3D.Fxc
import win32more.Graphics.Direct3D10
import win32more.Graphics.Direct3D11

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
D3D_COMPILER_VERSION = 47
D3DCOMPILE_DEBUG = 1
D3DCOMPILE_SKIP_VALIDATION = 2
D3DCOMPILE_SKIP_OPTIMIZATION = 4
D3DCOMPILE_PACK_MATRIX_ROW_MAJOR = 8
D3DCOMPILE_PACK_MATRIX_COLUMN_MAJOR = 16
D3DCOMPILE_PARTIAL_PRECISION = 32
D3DCOMPILE_FORCE_VS_SOFTWARE_NO_OPT = 64
D3DCOMPILE_FORCE_PS_SOFTWARE_NO_OPT = 128
D3DCOMPILE_NO_PRESHADER = 256
D3DCOMPILE_AVOID_FLOW_CONTROL = 512
D3DCOMPILE_PREFER_FLOW_CONTROL = 1024
D3DCOMPILE_ENABLE_STRICTNESS = 2048
D3DCOMPILE_ENABLE_BACKWARDS_COMPATIBILITY = 4096
D3DCOMPILE_IEEE_STRICTNESS = 8192
D3DCOMPILE_OPTIMIZATION_LEVEL0 = 16384
D3DCOMPILE_OPTIMIZATION_LEVEL1 = 0
D3DCOMPILE_OPTIMIZATION_LEVEL3 = 32768
D3DCOMPILE_RESERVED16 = 65536
D3DCOMPILE_RESERVED17 = 131072
D3DCOMPILE_WARNINGS_ARE_ERRORS = 262144
D3DCOMPILE_RESOURCES_MAY_ALIAS = 524288
D3DCOMPILE_ENABLE_UNBOUNDED_DESCRIPTOR_TABLES = 1048576
D3DCOMPILE_ALL_RESOURCES_BOUND = 2097152
D3DCOMPILE_DEBUG_NAME_FOR_SOURCE = 4194304
D3DCOMPILE_DEBUG_NAME_FOR_BINARY = 8388608
D3DCOMPILE_EFFECT_CHILD_EFFECT = 1
D3DCOMPILE_EFFECT_ALLOW_SLOW_OPS = 2
D3DCOMPILE_FLAGS2_FORCE_ROOT_SIGNATURE_LATEST = 0
D3DCOMPILE_FLAGS2_FORCE_ROOT_SIGNATURE_1_0 = 16
D3DCOMPILE_FLAGS2_FORCE_ROOT_SIGNATURE_1_1 = 32
D3DCOMPILE_SECDATA_MERGE_UAV_SLOTS = 1
D3DCOMPILE_SECDATA_PRESERVE_TEMPLATE_SLOTS = 2
D3DCOMPILE_SECDATA_REQUIRE_TEMPLATE_MATCH = 4
D3D_DISASM_ENABLE_COLOR_CODE = 1
D3D_DISASM_ENABLE_DEFAULT_VALUE_PRINTS = 2
D3D_DISASM_ENABLE_INSTRUCTION_NUMBERING = 4
D3D_DISASM_ENABLE_INSTRUCTION_CYCLE = 8
D3D_DISASM_DISABLE_DEBUG_INFO = 16
D3D_DISASM_ENABLE_INSTRUCTION_OFFSET = 32
D3D_DISASM_INSTRUCTION_ONLY = 64
D3D_DISASM_PRINT_HEX_LITERALS = 128
D3D_GET_INST_OFFSETS_INCLUDE_NON_EXECUTABLE = 1
D3D_COMPRESS_SHADER_KEEP_ALL_PARTS = 1
def _define_pD3DCompile():
    return CFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UIntPtr,win32more.Foundation.PSTR,POINTER(win32more.Graphics.Direct3D.D3D_SHADER_MACRO_head),win32more.Graphics.Direct3D.ID3DInclude_head,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32,UInt32,POINTER(win32more.Graphics.Direct3D.ID3DBlob_head),POINTER(win32more.Graphics.Direct3D.ID3DBlob_head), use_last_error=False)
def _define_pD3DPreprocess():
    return CFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UIntPtr,win32more.Foundation.PSTR,POINTER(win32more.Graphics.Direct3D.D3D_SHADER_MACRO_head),win32more.Graphics.Direct3D.ID3DInclude_head,POINTER(win32more.Graphics.Direct3D.ID3DBlob_head),POINTER(win32more.Graphics.Direct3D.ID3DBlob_head), use_last_error=False)
def _define_pD3DDisassemble():
    return CFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UIntPtr,UInt32,win32more.Foundation.PSTR,POINTER(win32more.Graphics.Direct3D.ID3DBlob_head), use_last_error=False)
D3DCOMPILER_STRIP_FLAGS = Int32
D3DCOMPILER_STRIP_REFLECTION_DATA = 1
D3DCOMPILER_STRIP_DEBUG_INFO = 2
D3DCOMPILER_STRIP_TEST_BLOBS = 4
D3DCOMPILER_STRIP_PRIVATE_DATA = 8
D3DCOMPILER_STRIP_ROOT_SIGNATURE = 16
D3DCOMPILER_STRIP_FORCE_DWORD = 2147483647
D3D_BLOB_PART = Int32
D3D_BLOB_INPUT_SIGNATURE_BLOB = 0
D3D_BLOB_OUTPUT_SIGNATURE_BLOB = 1
D3D_BLOB_INPUT_AND_OUTPUT_SIGNATURE_BLOB = 2
D3D_BLOB_PATCH_CONSTANT_SIGNATURE_BLOB = 3
D3D_BLOB_ALL_SIGNATURE_BLOB = 4
D3D_BLOB_DEBUG_INFO = 5
D3D_BLOB_LEGACY_SHADER = 6
D3D_BLOB_XNA_PREPASS_SHADER = 7
D3D_BLOB_XNA_SHADER = 8
D3D_BLOB_PDB = 9
D3D_BLOB_PRIVATE_DATA = 10
D3D_BLOB_ROOT_SIGNATURE = 11
D3D_BLOB_DEBUG_NAME = 12
D3D_BLOB_TEST_ALTERNATE_SHADER = 32768
D3D_BLOB_TEST_COMPILE_DETAILS = 32769
D3D_BLOB_TEST_COMPILE_PERF = 32770
D3D_BLOB_TEST_COMPILE_REPORT = 32771
def _define_D3D_SHADER_DATA_head():
    class D3D_SHADER_DATA(Structure):
        pass
    return D3D_SHADER_DATA
def _define_D3D_SHADER_DATA():
    D3D_SHADER_DATA = win32more.Graphics.Direct3D.Fxc.D3D_SHADER_DATA_head
    D3D_SHADER_DATA._fields_ = [
        ("pBytecode", c_void_p),
        ("BytecodeLength", UIntPtr),
    ]
    return D3D_SHADER_DATA
def _define_D3DReadFileToBlob():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Graphics.Direct3D.ID3DBlob_head), use_last_error=False)(("D3DReadFileToBlob", windll["D3DCOMPILER_47"]), ((1, 'pFileName'),(1, 'ppContents'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3DWriteBlobToFile():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D.ID3DBlob_head,win32more.Foundation.PWSTR,win32more.Foundation.BOOL, use_last_error=False)(("D3DWriteBlobToFile", windll["D3DCOMPILER_47"]), ((1, 'pBlob'),(1, 'pFileName'),(1, 'bOverwrite'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3DCompile():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UIntPtr,win32more.Foundation.PSTR,POINTER(win32more.Graphics.Direct3D.D3D_SHADER_MACRO_head),win32more.Graphics.Direct3D.ID3DInclude_head,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32,UInt32,POINTER(win32more.Graphics.Direct3D.ID3DBlob_head),POINTER(win32more.Graphics.Direct3D.ID3DBlob_head), use_last_error=False)(("D3DCompile", windll["D3DCOMPILER_47"]), ((1, 'pSrcData'),(1, 'SrcDataSize'),(1, 'pSourceName'),(1, 'pDefines'),(1, 'pInclude'),(1, 'pEntrypoint'),(1, 'pTarget'),(1, 'Flags1'),(1, 'Flags2'),(1, 'ppCode'),(1, 'ppErrorMsgs'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3DCompile2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UIntPtr,win32more.Foundation.PSTR,POINTER(win32more.Graphics.Direct3D.D3D_SHADER_MACRO_head),win32more.Graphics.Direct3D.ID3DInclude_head,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32,UInt32,UInt32,c_void_p,UIntPtr,POINTER(win32more.Graphics.Direct3D.ID3DBlob_head),POINTER(win32more.Graphics.Direct3D.ID3DBlob_head), use_last_error=False)(("D3DCompile2", windll["D3DCOMPILER_47"]), ((1, 'pSrcData'),(1, 'SrcDataSize'),(1, 'pSourceName'),(1, 'pDefines'),(1, 'pInclude'),(1, 'pEntrypoint'),(1, 'pTarget'),(1, 'Flags1'),(1, 'Flags2'),(1, 'SecondaryDataFlags'),(1, 'pSecondaryData'),(1, 'SecondaryDataSize'),(1, 'ppCode'),(1, 'ppErrorMsgs'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3DCompileFromFile():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Graphics.Direct3D.D3D_SHADER_MACRO_head),win32more.Graphics.Direct3D.ID3DInclude_head,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32,UInt32,POINTER(win32more.Graphics.Direct3D.ID3DBlob_head),POINTER(win32more.Graphics.Direct3D.ID3DBlob_head), use_last_error=False)(("D3DCompileFromFile", windll["D3DCOMPILER_47"]), ((1, 'pFileName'),(1, 'pDefines'),(1, 'pInclude'),(1, 'pEntrypoint'),(1, 'pTarget'),(1, 'Flags1'),(1, 'Flags2'),(1, 'ppCode'),(1, 'ppErrorMsgs'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3DPreprocess():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UIntPtr,win32more.Foundation.PSTR,POINTER(win32more.Graphics.Direct3D.D3D_SHADER_MACRO_head),win32more.Graphics.Direct3D.ID3DInclude_head,POINTER(win32more.Graphics.Direct3D.ID3DBlob_head),POINTER(win32more.Graphics.Direct3D.ID3DBlob_head), use_last_error=False)(("D3DPreprocess", windll["D3DCOMPILER_47"]), ((1, 'pSrcData'),(1, 'SrcDataSize'),(1, 'pSourceName'),(1, 'pDefines'),(1, 'pInclude'),(1, 'ppCodeText'),(1, 'ppErrorMsgs'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3DGetDebugInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UIntPtr,POINTER(win32more.Graphics.Direct3D.ID3DBlob_head), use_last_error=False)(("D3DGetDebugInfo", windll["D3DCOMPILER_47"]), ((1, 'pSrcData'),(1, 'SrcDataSize'),(1, 'ppDebugInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3DReflect():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UIntPtr,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("D3DReflect", windll["D3DCOMPILER_47"]), ((1, 'pSrcData'),(1, 'SrcDataSize'),(1, 'pInterface'),(1, 'ppReflector'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3DReflectLibrary():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UIntPtr,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("D3DReflectLibrary", windll["D3DCOMPILER_47"]), ((1, 'pSrcData'),(1, 'SrcDataSize'),(1, 'riid'),(1, 'ppReflector'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3DDisassemble():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UIntPtr,UInt32,win32more.Foundation.PSTR,POINTER(win32more.Graphics.Direct3D.ID3DBlob_head), use_last_error=False)(("D3DDisassemble", windll["D3DCOMPILER_47"]), ((1, 'pSrcData'),(1, 'SrcDataSize'),(1, 'Flags'),(1, 'szComments'),(1, 'ppDisassembly'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3DDisassembleRegion():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UIntPtr,UInt32,win32more.Foundation.PSTR,UIntPtr,UIntPtr,POINTER(UIntPtr),POINTER(win32more.Graphics.Direct3D.ID3DBlob_head), use_last_error=False)(("D3DDisassembleRegion", windll["D3DCOMPILER_47"]), ((1, 'pSrcData'),(1, 'SrcDataSize'),(1, 'Flags'),(1, 'szComments'),(1, 'StartByteOffset'),(1, 'NumInsts'),(1, 'pFinishByteOffset'),(1, 'ppDisassembly'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3DCreateLinker():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D11.ID3D11Linker_head), use_last_error=False)(("D3DCreateLinker", windll["D3DCOMPILER_47"]), ((1, 'ppLinker'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3DLoadModule():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UIntPtr,POINTER(win32more.Graphics.Direct3D11.ID3D11Module_head), use_last_error=False)(("D3DLoadModule", windll["D3DCOMPILER_47"]), ((1, 'pSrcData'),(1, 'cbSrcDataSize'),(1, 'ppModule'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3DCreateFunctionLinkingGraph():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Direct3D11.ID3D11FunctionLinkingGraph_head), use_last_error=False)(("D3DCreateFunctionLinkingGraph", windll["D3DCOMPILER_47"]), ((1, 'uFlags'),(1, 'ppFunctionLinkingGraph'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3DGetTraceInstructionOffsets():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UIntPtr,UInt32,UIntPtr,UIntPtr,POINTER(UIntPtr),POINTER(UIntPtr), use_last_error=False)(("D3DGetTraceInstructionOffsets", windll["D3DCOMPILER_47"]), ((1, 'pSrcData'),(1, 'SrcDataSize'),(1, 'Flags'),(1, 'StartInstIndex'),(1, 'NumInsts'),(1, 'pOffsets'),(1, 'pTotalInsts'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3DGetInputSignatureBlob():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UIntPtr,POINTER(win32more.Graphics.Direct3D.ID3DBlob_head), use_last_error=False)(("D3DGetInputSignatureBlob", windll["D3DCOMPILER_47"]), ((1, 'pSrcData'),(1, 'SrcDataSize'),(1, 'ppSignatureBlob'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3DGetOutputSignatureBlob():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UIntPtr,POINTER(win32more.Graphics.Direct3D.ID3DBlob_head), use_last_error=False)(("D3DGetOutputSignatureBlob", windll["D3DCOMPILER_47"]), ((1, 'pSrcData'),(1, 'SrcDataSize'),(1, 'ppSignatureBlob'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3DGetInputAndOutputSignatureBlob():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UIntPtr,POINTER(win32more.Graphics.Direct3D.ID3DBlob_head), use_last_error=False)(("D3DGetInputAndOutputSignatureBlob", windll["D3DCOMPILER_47"]), ((1, 'pSrcData'),(1, 'SrcDataSize'),(1, 'ppSignatureBlob'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3DStripShader():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UIntPtr,UInt32,POINTER(win32more.Graphics.Direct3D.ID3DBlob_head), use_last_error=False)(("D3DStripShader", windll["D3DCOMPILER_47"]), ((1, 'pShaderBytecode'),(1, 'BytecodeLength'),(1, 'uStripFlags'),(1, 'ppStrippedBlob'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3DGetBlobPart():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UIntPtr,win32more.Graphics.Direct3D.Fxc.D3D_BLOB_PART,UInt32,POINTER(win32more.Graphics.Direct3D.ID3DBlob_head), use_last_error=False)(("D3DGetBlobPart", windll["D3DCOMPILER_47"]), ((1, 'pSrcData'),(1, 'SrcDataSize'),(1, 'Part'),(1, 'Flags'),(1, 'ppPart'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3DSetBlobPart():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UIntPtr,win32more.Graphics.Direct3D.Fxc.D3D_BLOB_PART,UInt32,c_void_p,UIntPtr,POINTER(win32more.Graphics.Direct3D.ID3DBlob_head), use_last_error=False)(("D3DSetBlobPart", windll["D3DCOMPILER_47"]), ((1, 'pSrcData'),(1, 'SrcDataSize'),(1, 'Part'),(1, 'Flags'),(1, 'pPart'),(1, 'PartSize'),(1, 'ppNewShader'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3DCreateBlob():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UIntPtr,POINTER(win32more.Graphics.Direct3D.ID3DBlob_head), use_last_error=False)(("D3DCreateBlob", windll["D3DCOMPILER_47"]), ((1, 'Size'),(1, 'ppBlob'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3DCompressShaders():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Direct3D.Fxc.D3D_SHADER_DATA),UInt32,POINTER(win32more.Graphics.Direct3D.ID3DBlob_head), use_last_error=False)(("D3DCompressShaders", windll["D3DCOMPILER_47"]), ((1, 'uNumShaders'),(1, 'pShaderData'),(1, 'uFlags'),(1, 'ppCompressedData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3DDecompressShaders():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UIntPtr,UInt32,UInt32,POINTER(UInt32),UInt32,POINTER(win32more.Graphics.Direct3D.ID3DBlob_head),POINTER(UInt32), use_last_error=False)(("D3DDecompressShaders", windll["D3DCOMPILER_47"]), ((1, 'pSrcData'),(1, 'SrcDataSize'),(1, 'uNumShaders'),(1, 'uStartIndex'),(1, 'pIndices'),(1, 'uFlags'),(1, 'ppShaders'),(1, 'pTotalShaders'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3DDisassemble10Effect():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D10.ID3D10Effect_head,UInt32,POINTER(win32more.Graphics.Direct3D.ID3DBlob_head), use_last_error=False)(("D3DDisassemble10Effect", windll["D3DCOMPILER_47"]), ((1, 'pEffect'),(1, 'Flags'),(1, 'ppDisassembly'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "D3D_COMPILER_VERSION",
    "D3DCOMPILE_DEBUG",
    "D3DCOMPILE_SKIP_VALIDATION",
    "D3DCOMPILE_SKIP_OPTIMIZATION",
    "D3DCOMPILE_PACK_MATRIX_ROW_MAJOR",
    "D3DCOMPILE_PACK_MATRIX_COLUMN_MAJOR",
    "D3DCOMPILE_PARTIAL_PRECISION",
    "D3DCOMPILE_FORCE_VS_SOFTWARE_NO_OPT",
    "D3DCOMPILE_FORCE_PS_SOFTWARE_NO_OPT",
    "D3DCOMPILE_NO_PRESHADER",
    "D3DCOMPILE_AVOID_FLOW_CONTROL",
    "D3DCOMPILE_PREFER_FLOW_CONTROL",
    "D3DCOMPILE_ENABLE_STRICTNESS",
    "D3DCOMPILE_ENABLE_BACKWARDS_COMPATIBILITY",
    "D3DCOMPILE_IEEE_STRICTNESS",
    "D3DCOMPILE_OPTIMIZATION_LEVEL0",
    "D3DCOMPILE_OPTIMIZATION_LEVEL1",
    "D3DCOMPILE_OPTIMIZATION_LEVEL3",
    "D3DCOMPILE_RESERVED16",
    "D3DCOMPILE_RESERVED17",
    "D3DCOMPILE_WARNINGS_ARE_ERRORS",
    "D3DCOMPILE_RESOURCES_MAY_ALIAS",
    "D3DCOMPILE_ENABLE_UNBOUNDED_DESCRIPTOR_TABLES",
    "D3DCOMPILE_ALL_RESOURCES_BOUND",
    "D3DCOMPILE_DEBUG_NAME_FOR_SOURCE",
    "D3DCOMPILE_DEBUG_NAME_FOR_BINARY",
    "D3DCOMPILE_EFFECT_CHILD_EFFECT",
    "D3DCOMPILE_EFFECT_ALLOW_SLOW_OPS",
    "D3DCOMPILE_FLAGS2_FORCE_ROOT_SIGNATURE_LATEST",
    "D3DCOMPILE_FLAGS2_FORCE_ROOT_SIGNATURE_1_0",
    "D3DCOMPILE_FLAGS2_FORCE_ROOT_SIGNATURE_1_1",
    "D3DCOMPILE_SECDATA_MERGE_UAV_SLOTS",
    "D3DCOMPILE_SECDATA_PRESERVE_TEMPLATE_SLOTS",
    "D3DCOMPILE_SECDATA_REQUIRE_TEMPLATE_MATCH",
    "D3D_DISASM_ENABLE_COLOR_CODE",
    "D3D_DISASM_ENABLE_DEFAULT_VALUE_PRINTS",
    "D3D_DISASM_ENABLE_INSTRUCTION_NUMBERING",
    "D3D_DISASM_ENABLE_INSTRUCTION_CYCLE",
    "D3D_DISASM_DISABLE_DEBUG_INFO",
    "D3D_DISASM_ENABLE_INSTRUCTION_OFFSET",
    "D3D_DISASM_INSTRUCTION_ONLY",
    "D3D_DISASM_PRINT_HEX_LITERALS",
    "D3D_GET_INST_OFFSETS_INCLUDE_NON_EXECUTABLE",
    "D3D_COMPRESS_SHADER_KEEP_ALL_PARTS",
    "pD3DCompile",
    "pD3DPreprocess",
    "pD3DDisassemble",
    "D3DCOMPILER_STRIP_FLAGS",
    "D3DCOMPILER_STRIP_REFLECTION_DATA",
    "D3DCOMPILER_STRIP_DEBUG_INFO",
    "D3DCOMPILER_STRIP_TEST_BLOBS",
    "D3DCOMPILER_STRIP_PRIVATE_DATA",
    "D3DCOMPILER_STRIP_ROOT_SIGNATURE",
    "D3DCOMPILER_STRIP_FORCE_DWORD",
    "D3D_BLOB_PART",
    "D3D_BLOB_INPUT_SIGNATURE_BLOB",
    "D3D_BLOB_OUTPUT_SIGNATURE_BLOB",
    "D3D_BLOB_INPUT_AND_OUTPUT_SIGNATURE_BLOB",
    "D3D_BLOB_PATCH_CONSTANT_SIGNATURE_BLOB",
    "D3D_BLOB_ALL_SIGNATURE_BLOB",
    "D3D_BLOB_DEBUG_INFO",
    "D3D_BLOB_LEGACY_SHADER",
    "D3D_BLOB_XNA_PREPASS_SHADER",
    "D3D_BLOB_XNA_SHADER",
    "D3D_BLOB_PDB",
    "D3D_BLOB_PRIVATE_DATA",
    "D3D_BLOB_ROOT_SIGNATURE",
    "D3D_BLOB_DEBUG_NAME",
    "D3D_BLOB_TEST_ALTERNATE_SHADER",
    "D3D_BLOB_TEST_COMPILE_DETAILS",
    "D3D_BLOB_TEST_COMPILE_PERF",
    "D3D_BLOB_TEST_COMPILE_REPORT",
    "D3D_SHADER_DATA",
    "D3DReadFileToBlob",
    "D3DWriteBlobToFile",
    "D3DCompile",
    "D3DCompile2",
    "D3DCompileFromFile",
    "D3DPreprocess",
    "D3DGetDebugInfo",
    "D3DReflect",
    "D3DReflectLibrary",
    "D3DDisassemble",
    "D3DDisassembleRegion",
    "D3DCreateLinker",
    "D3DLoadModule",
    "D3DCreateFunctionLinkingGraph",
    "D3DGetTraceInstructionOffsets",
    "D3DGetInputSignatureBlob",
    "D3DGetOutputSignatureBlob",
    "D3DGetInputAndOutputSignatureBlob",
    "D3DStripShader",
    "D3DGetBlobPart",
    "D3DSetBlobPart",
    "D3DCreateBlob",
    "D3DCompressShaders",
    "D3DDecompressShaders",
    "D3DDisassemble10Effect",
]
