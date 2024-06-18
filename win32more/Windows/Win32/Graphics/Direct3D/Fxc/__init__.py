from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Direct3D
import win32more.Windows.Win32.Graphics.Direct3D.Fxc
import win32more.Windows.Win32.Graphics.Direct3D10
import win32more.Windows.Win32.Graphics.Direct3D11
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
def D3DReadFileToBlob(pFileName: win32more.Windows.Win32.Foundation.PWSTR, ppContents: POINTER(win32more.Windows.Win32.Graphics.Direct3D.ID3DBlob)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DWriteBlobToFile(pBlob: win32more.Windows.Win32.Graphics.Direct3D.ID3DBlob, pFileName: win32more.Windows.Win32.Foundation.PWSTR, bOverwrite: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DCompile(pSrcData: VoidPtr, SrcDataSize: UIntPtr, pSourceName: win32more.Windows.Win32.Foundation.PSTR, pDefines: POINTER(win32more.Windows.Win32.Graphics.Direct3D.D3D_SHADER_MACRO), pInclude: win32more.Windows.Win32.Graphics.Direct3D.ID3DInclude, pEntrypoint: win32more.Windows.Win32.Foundation.PSTR, pTarget: win32more.Windows.Win32.Foundation.PSTR, Flags1: UInt32, Flags2: UInt32, ppCode: POINTER(win32more.Windows.Win32.Graphics.Direct3D.ID3DBlob), ppErrorMsgs: POINTER(win32more.Windows.Win32.Graphics.Direct3D.ID3DBlob)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DCompile2(pSrcData: VoidPtr, SrcDataSize: UIntPtr, pSourceName: win32more.Windows.Win32.Foundation.PSTR, pDefines: POINTER(win32more.Windows.Win32.Graphics.Direct3D.D3D_SHADER_MACRO), pInclude: win32more.Windows.Win32.Graphics.Direct3D.ID3DInclude, pEntrypoint: win32more.Windows.Win32.Foundation.PSTR, pTarget: win32more.Windows.Win32.Foundation.PSTR, Flags1: UInt32, Flags2: UInt32, SecondaryDataFlags: UInt32, pSecondaryData: VoidPtr, SecondaryDataSize: UIntPtr, ppCode: POINTER(win32more.Windows.Win32.Graphics.Direct3D.ID3DBlob), ppErrorMsgs: POINTER(win32more.Windows.Win32.Graphics.Direct3D.ID3DBlob)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DCompileFromFile(pFileName: win32more.Windows.Win32.Foundation.PWSTR, pDefines: POINTER(win32more.Windows.Win32.Graphics.Direct3D.D3D_SHADER_MACRO), pInclude: win32more.Windows.Win32.Graphics.Direct3D.ID3DInclude, pEntrypoint: win32more.Windows.Win32.Foundation.PSTR, pTarget: win32more.Windows.Win32.Foundation.PSTR, Flags1: UInt32, Flags2: UInt32, ppCode: POINTER(win32more.Windows.Win32.Graphics.Direct3D.ID3DBlob), ppErrorMsgs: POINTER(win32more.Windows.Win32.Graphics.Direct3D.ID3DBlob)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DPreprocess(pSrcData: VoidPtr, SrcDataSize: UIntPtr, pSourceName: win32more.Windows.Win32.Foundation.PSTR, pDefines: POINTER(win32more.Windows.Win32.Graphics.Direct3D.D3D_SHADER_MACRO), pInclude: win32more.Windows.Win32.Graphics.Direct3D.ID3DInclude, ppCodeText: POINTER(win32more.Windows.Win32.Graphics.Direct3D.ID3DBlob), ppErrorMsgs: POINTER(win32more.Windows.Win32.Graphics.Direct3D.ID3DBlob)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DGetDebugInfo(pSrcData: VoidPtr, SrcDataSize: UIntPtr, ppDebugInfo: POINTER(win32more.Windows.Win32.Graphics.Direct3D.ID3DBlob)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DReflect(pSrcData: VoidPtr, SrcDataSize: UIntPtr, pInterface: POINTER(Guid), ppReflector: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DReflectLibrary(pSrcData: VoidPtr, SrcDataSize: UIntPtr, riid: POINTER(Guid), ppReflector: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DDisassemble(pSrcData: VoidPtr, SrcDataSize: UIntPtr, Flags: UInt32, szComments: win32more.Windows.Win32.Foundation.PSTR, ppDisassembly: POINTER(win32more.Windows.Win32.Graphics.Direct3D.ID3DBlob)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DDisassembleRegion(pSrcData: VoidPtr, SrcDataSize: UIntPtr, Flags: UInt32, szComments: win32more.Windows.Win32.Foundation.PSTR, StartByteOffset: UIntPtr, NumInsts: UIntPtr, pFinishByteOffset: POINTER(UIntPtr), ppDisassembly: POINTER(win32more.Windows.Win32.Graphics.Direct3D.ID3DBlob)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DCreateLinker(ppLinker: POINTER(win32more.Windows.Win32.Graphics.Direct3D11.ID3D11Linker)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DLoadModule(pSrcData: VoidPtr, cbSrcDataSize: UIntPtr, ppModule: POINTER(win32more.Windows.Win32.Graphics.Direct3D11.ID3D11Module)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DCreateFunctionLinkingGraph(uFlags: UInt32, ppFunctionLinkingGraph: POINTER(win32more.Windows.Win32.Graphics.Direct3D11.ID3D11FunctionLinkingGraph)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DGetTraceInstructionOffsets(pSrcData: VoidPtr, SrcDataSize: UIntPtr, Flags: UInt32, StartInstIndex: UIntPtr, NumInsts: UIntPtr, pOffsets: POINTER(UIntPtr), pTotalInsts: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DGetInputSignatureBlob(pSrcData: VoidPtr, SrcDataSize: UIntPtr, ppSignatureBlob: POINTER(win32more.Windows.Win32.Graphics.Direct3D.ID3DBlob)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DGetOutputSignatureBlob(pSrcData: VoidPtr, SrcDataSize: UIntPtr, ppSignatureBlob: POINTER(win32more.Windows.Win32.Graphics.Direct3D.ID3DBlob)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DGetInputAndOutputSignatureBlob(pSrcData: VoidPtr, SrcDataSize: UIntPtr, ppSignatureBlob: POINTER(win32more.Windows.Win32.Graphics.Direct3D.ID3DBlob)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DStripShader(pShaderBytecode: VoidPtr, BytecodeLength: UIntPtr, uStripFlags: UInt32, ppStrippedBlob: POINTER(win32more.Windows.Win32.Graphics.Direct3D.ID3DBlob)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DGetBlobPart(pSrcData: VoidPtr, SrcDataSize: UIntPtr, Part: win32more.Windows.Win32.Graphics.Direct3D.Fxc.D3D_BLOB_PART, Flags: UInt32, ppPart: POINTER(win32more.Windows.Win32.Graphics.Direct3D.ID3DBlob)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DSetBlobPart(pSrcData: VoidPtr, SrcDataSize: UIntPtr, Part: win32more.Windows.Win32.Graphics.Direct3D.Fxc.D3D_BLOB_PART, Flags: UInt32, pPart: VoidPtr, PartSize: UIntPtr, ppNewShader: POINTER(win32more.Windows.Win32.Graphics.Direct3D.ID3DBlob)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DCreateBlob(Size: UIntPtr, ppBlob: POINTER(win32more.Windows.Win32.Graphics.Direct3D.ID3DBlob)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DCompressShaders(uNumShaders: UInt32, pShaderData: POINTER(win32more.Windows.Win32.Graphics.Direct3D.Fxc.D3D_SHADER_DATA), uFlags: UInt32, ppCompressedData: POINTER(win32more.Windows.Win32.Graphics.Direct3D.ID3DBlob)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DDecompressShaders(pSrcData: VoidPtr, SrcDataSize: UIntPtr, uNumShaders: UInt32, uStartIndex: UInt32, pIndices: POINTER(UInt32), uFlags: UInt32, ppShaders: POINTER(win32more.Windows.Win32.Graphics.Direct3D.ID3DBlob), pTotalShaders: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('D3DCOMPILER_47.dll')
def D3DDisassemble10Effect(pEffect: win32more.Windows.Win32.Graphics.Direct3D10.ID3D10Effect, Flags: UInt32, ppDisassembly: POINTER(win32more.Windows.Win32.Graphics.Direct3D.ID3DBlob)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
D3DCOMPILER_STRIP_FLAGS = Int32
D3DCOMPILER_STRIP_REFLECTION_DATA: win32more.Windows.Win32.Graphics.Direct3D.Fxc.D3DCOMPILER_STRIP_FLAGS = 1
D3DCOMPILER_STRIP_DEBUG_INFO: win32more.Windows.Win32.Graphics.Direct3D.Fxc.D3DCOMPILER_STRIP_FLAGS = 2
D3DCOMPILER_STRIP_TEST_BLOBS: win32more.Windows.Win32.Graphics.Direct3D.Fxc.D3DCOMPILER_STRIP_FLAGS = 4
D3DCOMPILER_STRIP_PRIVATE_DATA: win32more.Windows.Win32.Graphics.Direct3D.Fxc.D3DCOMPILER_STRIP_FLAGS = 8
D3DCOMPILER_STRIP_ROOT_SIGNATURE: win32more.Windows.Win32.Graphics.Direct3D.Fxc.D3DCOMPILER_STRIP_FLAGS = 16
D3D_BLOB_PART = Int32
D3D_BLOB_INPUT_SIGNATURE_BLOB: win32more.Windows.Win32.Graphics.Direct3D.Fxc.D3D_BLOB_PART = 0
D3D_BLOB_OUTPUT_SIGNATURE_BLOB: win32more.Windows.Win32.Graphics.Direct3D.Fxc.D3D_BLOB_PART = 1
D3D_BLOB_INPUT_AND_OUTPUT_SIGNATURE_BLOB: win32more.Windows.Win32.Graphics.Direct3D.Fxc.D3D_BLOB_PART = 2
D3D_BLOB_PATCH_CONSTANT_SIGNATURE_BLOB: win32more.Windows.Win32.Graphics.Direct3D.Fxc.D3D_BLOB_PART = 3
D3D_BLOB_ALL_SIGNATURE_BLOB: win32more.Windows.Win32.Graphics.Direct3D.Fxc.D3D_BLOB_PART = 4
D3D_BLOB_DEBUG_INFO: win32more.Windows.Win32.Graphics.Direct3D.Fxc.D3D_BLOB_PART = 5
D3D_BLOB_LEGACY_SHADER: win32more.Windows.Win32.Graphics.Direct3D.Fxc.D3D_BLOB_PART = 6
D3D_BLOB_XNA_PREPASS_SHADER: win32more.Windows.Win32.Graphics.Direct3D.Fxc.D3D_BLOB_PART = 7
D3D_BLOB_XNA_SHADER: win32more.Windows.Win32.Graphics.Direct3D.Fxc.D3D_BLOB_PART = 8
D3D_BLOB_PDB: win32more.Windows.Win32.Graphics.Direct3D.Fxc.D3D_BLOB_PART = 9
D3D_BLOB_PRIVATE_DATA: win32more.Windows.Win32.Graphics.Direct3D.Fxc.D3D_BLOB_PART = 10
D3D_BLOB_ROOT_SIGNATURE: win32more.Windows.Win32.Graphics.Direct3D.Fxc.D3D_BLOB_PART = 11
D3D_BLOB_DEBUG_NAME: win32more.Windows.Win32.Graphics.Direct3D.Fxc.D3D_BLOB_PART = 12
D3D_BLOB_TEST_ALTERNATE_SHADER: win32more.Windows.Win32.Graphics.Direct3D.Fxc.D3D_BLOB_PART = 32768
D3D_BLOB_TEST_COMPILE_DETAILS: win32more.Windows.Win32.Graphics.Direct3D.Fxc.D3D_BLOB_PART = 32769
D3D_BLOB_TEST_COMPILE_PERF: win32more.Windows.Win32.Graphics.Direct3D.Fxc.D3D_BLOB_PART = 32770
D3D_BLOB_TEST_COMPILE_REPORT: win32more.Windows.Win32.Graphics.Direct3D.Fxc.D3D_BLOB_PART = 32771
class D3D_SHADER_DATA(Structure):
    pBytecode: VoidPtr
    BytecodeLength: UIntPtr
@winfunctype_pointer
def pD3DCompile(pSrcData: VoidPtr, SrcDataSize: UIntPtr, pFileName: win32more.Windows.Win32.Foundation.PSTR, pDefines: POINTER(win32more.Windows.Win32.Graphics.Direct3D.D3D_SHADER_MACRO), pInclude: win32more.Windows.Win32.Graphics.Direct3D.ID3DInclude, pEntrypoint: win32more.Windows.Win32.Foundation.PSTR, pTarget: win32more.Windows.Win32.Foundation.PSTR, Flags1: UInt32, Flags2: UInt32, ppCode: POINTER(win32more.Windows.Win32.Graphics.Direct3D.ID3DBlob), ppErrorMsgs: POINTER(win32more.Windows.Win32.Graphics.Direct3D.ID3DBlob)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def pD3DDisassemble(pSrcData: VoidPtr, SrcDataSize: UIntPtr, Flags: UInt32, szComments: win32more.Windows.Win32.Foundation.PSTR, ppDisassembly: POINTER(win32more.Windows.Win32.Graphics.Direct3D.ID3DBlob)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def pD3DPreprocess(pSrcData: VoidPtr, SrcDataSize: UIntPtr, pFileName: win32more.Windows.Win32.Foundation.PSTR, pDefines: POINTER(win32more.Windows.Win32.Graphics.Direct3D.D3D_SHADER_MACRO), pInclude: win32more.Windows.Win32.Graphics.Direct3D.ID3DInclude, ppCodeText: POINTER(win32more.Windows.Win32.Graphics.Direct3D.ID3DBlob), ppErrorMsgs: POINTER(win32more.Windows.Win32.Graphics.Direct3D.ID3DBlob)) -> win32more.Windows.Win32.Foundation.HRESULT: ...


make_ready(__name__)
