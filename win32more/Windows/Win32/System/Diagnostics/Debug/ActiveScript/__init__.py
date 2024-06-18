from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Diagnostics.Debug
import win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript
import win32more.Windows.Win32.System.Variant
APPLICATION_NODE_EVENT_FILTER = Int32
FILTER_EXCLUDE_NOTHING: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.APPLICATION_NODE_EVENT_FILTER = 0
FILTER_EXCLUDE_ANONYMOUS_CODE: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.APPLICATION_NODE_EVENT_FILTER = 1
FILTER_EXCLUDE_EVAL_CODE: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.APPLICATION_NODE_EVENT_FILTER = 2
CATID_ActiveScriptAuthor: Guid = Guid('{0aee2a92-bcbb-11d0-8c72-00c04fc2b085}')
APPBREAKFLAG_DEBUGGER_BLOCK: UInt32 = 1
APPBREAKFLAG_DEBUGGER_HALT: UInt32 = 2
APPBREAKFLAG_STEP: UInt32 = 65536
APPBREAKFLAG_NESTED: UInt32 = 131072
APPBREAKFLAG_STEPTYPE_SOURCE: UInt32 = 0
APPBREAKFLAG_STEPTYPE_BYTECODE: UInt32 = 1048576
APPBREAKFLAG_STEPTYPE_MACHINE: UInt32 = 2097152
APPBREAKFLAG_STEPTYPE_MASK: UInt32 = 15728640
APPBREAKFLAG_IN_BREAKPOINT: UInt32 = 2147483648
SOURCETEXT_ATTR_KEYWORD: UInt32 = 1
SOURCETEXT_ATTR_COMMENT: UInt32 = 2
SOURCETEXT_ATTR_NONSOURCE: UInt32 = 4
SOURCETEXT_ATTR_OPERATOR: UInt32 = 8
SOURCETEXT_ATTR_NUMBER: UInt32 = 16
SOURCETEXT_ATTR_STRING: UInt32 = 32
SOURCETEXT_ATTR_FUNCTION_START: UInt32 = 64
TEXT_DOC_ATTR_READONLY: UInt32 = 1
TEXT_DOC_ATTR_TYPE_PRIMARY: UInt32 = 2
TEXT_DOC_ATTR_TYPE_WORKER: UInt32 = 4
TEXT_DOC_ATTR_TYPE_SCRIPT: UInt32 = 8
DEBUG_TEXT_ISEXPRESSION: UInt32 = 1
DEBUG_TEXT_RETURNVALUE: UInt32 = 2
DEBUG_TEXT_NOSIDEEFFECTS: UInt32 = 4
DEBUG_TEXT_ALLOWBREAKPOINTS: UInt32 = 8
DEBUG_TEXT_ALLOWERRORREPORT: UInt32 = 16
DEBUG_TEXT_EVALUATETOCODECONTEXT: UInt32 = 32
DEBUG_TEXT_ISNONUSERCODE: UInt32 = 64
THREAD_STATE_RUNNING: UInt32 = 1
THREAD_STATE_SUSPENDED: UInt32 = 2
THREAD_BLOCKED: UInt32 = 4
THREAD_OUT_OF_CONTEXT: UInt32 = 8
CATID_ActiveScript: Guid = Guid('{f0b7a1a1-9847-11cf-8f20-00805f2cd064}')
CATID_ActiveScriptParse: Guid = Guid('{f0b7a1a2-9847-11cf-8f20-00805f2cd064}')
CATID_ActiveScriptEncode: Guid = Guid('{f0b7a1a3-9847-11cf-8f20-00805f2cd064}')
OID_VBSSIP: Guid = Guid('{1629f04e-2799-4db5-8fe5-ace10f17ebab}')
OID_JSSIP: Guid = Guid('{06c9e010-38ce-11d4-a2a3-00104bd35090}')
OID_WSFSIP: Guid = Guid('{1a610570-38ce-11d4-a2a3-00104bd35090}')
SCRIPTITEM_ISVISIBLE: UInt32 = 2
SCRIPTITEM_ISSOURCE: UInt32 = 4
SCRIPTITEM_GLOBALMEMBERS: UInt32 = 8
SCRIPTITEM_ISPERSISTENT: UInt32 = 64
SCRIPTITEM_CODEONLY: UInt32 = 512
SCRIPTITEM_NOCODE: UInt32 = 1024
SCRIPTTYPELIB_ISCONTROL: UInt32 = 16
SCRIPTTYPELIB_ISPERSISTENT: UInt32 = 64
SCRIPTTEXT_DELAYEXECUTION: UInt32 = 1
SCRIPTTEXT_ISVISIBLE: UInt32 = 2
SCRIPTTEXT_ISEXPRESSION: UInt32 = 32
SCRIPTTEXT_ISPERSISTENT: UInt32 = 64
SCRIPTTEXT_HOSTMANAGESSOURCE: UInt32 = 128
SCRIPTTEXT_ISXDOMAIN: UInt32 = 256
SCRIPTTEXT_ISNONUSERCODE: UInt32 = 512
SCRIPTPROC_ISEXPRESSION: UInt32 = 32
SCRIPTPROC_HOSTMANAGESSOURCE: UInt32 = 128
SCRIPTPROC_IMPLICIT_THIS: UInt32 = 256
SCRIPTPROC_IMPLICIT_PARENTS: UInt32 = 512
SCRIPTPROC_ISXDOMAIN: UInt32 = 1024
SCRIPTINFO_IUNKNOWN: UInt32 = 1
SCRIPTINFO_ITYPEINFO: UInt32 = 2
SCRIPTINTERRUPT_DEBUG: UInt32 = 1
SCRIPTINTERRUPT_RAISEEXCEPTION: UInt32 = 2
SCRIPTSTAT_STATEMENT_COUNT: UInt32 = 1
SCRIPTSTAT_INSTRUCTION_COUNT: UInt32 = 2
SCRIPTSTAT_INTSTRUCTION_TIME: UInt32 = 3
SCRIPTSTAT_TOTAL_TIME: UInt32 = 4
SCRIPT_ENCODE_SECTION: UInt32 = 1
SCRIPT_ENCODE_DEFAULT_LANGUAGE: UInt32 = 1
SCRIPT_ENCODE_NO_ASP_LANGUAGE: UInt32 = 2
SCRIPTPROP_NAME: UInt32 = 0
SCRIPTPROP_MAJORVERSION: UInt32 = 1
SCRIPTPROP_MINORVERSION: UInt32 = 2
SCRIPTPROP_BUILDNUMBER: UInt32 = 3
SCRIPTPROP_DELAYEDEVENTSINKING: UInt32 = 4096
SCRIPTPROP_CATCHEXCEPTION: UInt32 = 4097
SCRIPTPROP_CONVERSIONLCID: UInt32 = 4098
SCRIPTPROP_HOSTSTACKREQUIRED: UInt32 = 4099
SCRIPTPROP_SCRIPTSAREFULLYTRUSTED: UInt32 = 4100
SCRIPTPROP_DEBUGGER: UInt32 = 4352
SCRIPTPROP_JITDEBUG: UInt32 = 4353
SCRIPTPROP_GCCONTROLSOFTCLOSE: UInt32 = 8192
SCRIPTPROP_INTEGERMODE: UInt32 = 12288
SCRIPTPROP_STRINGCOMPAREINSTANCE: UInt32 = 12289
SCRIPTPROP_INVOKEVERSIONING: UInt32 = 16384
SCRIPTPROP_HACK_FIBERSUPPORT: UInt32 = 1879048192
SCRIPTPROP_HACK_TRIDENTEVENTSINK: UInt32 = 1879048193
SCRIPTPROP_ABBREVIATE_GLOBALNAME_RESOLUTION: UInt32 = 1879048194
SCRIPTPROP_HOSTKEEPALIVE: UInt32 = 1879048196
SCRIPT_E_RECORDED: Int32 = -2040119292
SCRIPT_E_REPORTED: Int32 = -2147352319
SCRIPT_E_PROPAGATE: Int32 = -2147352318
FACILITY_JsDEBUG: UInt32 = 3527
E_JsDEBUG_MISMATCHED_RUNTIME: win32more.Windows.Win32.Foundation.HRESULT = -1916338175
E_JsDEBUG_UNKNOWN_THREAD: win32more.Windows.Win32.Foundation.HRESULT = -1916338174
E_JsDEBUG_OUTSIDE_OF_VM: win32more.Windows.Win32.Foundation.HRESULT = -1916338172
E_JsDEBUG_INVALID_MEMORY_ADDRESS: win32more.Windows.Win32.Foundation.HRESULT = -1916338171
E_JsDEBUG_SOURCE_LOCATION_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -1916338170
E_JsDEBUG_RUNTIME_NOT_IN_DEBUG_MODE: win32more.Windows.Win32.Foundation.HRESULT = -1916338169
ACTIVPROF_E_PROFILER_PRESENT: win32more.Windows.Win32.Foundation.HRESULT = -2147220992
ACTIVPROF_E_PROFILER_ABSENT: win32more.Windows.Win32.Foundation.HRESULT = -2147220991
ACTIVPROF_E_UNABLE_TO_APPLY_ACTION: win32more.Windows.Win32.Foundation.HRESULT = -2147220990
PROFILER_HEAP_OBJECT_NAME_ID_UNAVAILABLE: UInt32 = 4294967295
fasaPreferInternalHandler: UInt32 = 1
fasaSupportInternalHandler: UInt32 = 2
fasaCaseSensitive: UInt32 = 4
SCRIPT_CMPL_NOLIST: UInt32 = 0
SCRIPT_CMPL_MEMBERLIST: UInt32 = 1
SCRIPT_CMPL_ENUMLIST: UInt32 = 2
SCRIPT_CMPL_PARAMTIP: UInt32 = 4
SCRIPT_CMPL_GLOBALLIST: UInt32 = 8
SCRIPT_CMPL_ENUM_TRIGGER: UInt32 = 1
SCRIPT_CMPL_MEMBER_TRIGGER: UInt32 = 2
SCRIPT_CMPL_PARAM_TRIGGER: UInt32 = 3
SCRIPT_CMPL_COMMIT: UInt32 = 4
GETATTRTYPE_NORMAL: UInt32 = 0
GETATTRTYPE_DEPSCAN: UInt32 = 1
GETATTRFLAG_THIS: UInt32 = 256
GETATTRFLAG_HUMANTEXT: UInt32 = 32768
SOURCETEXT_ATTR_HUMANTEXT: UInt32 = 32768
SOURCETEXT_ATTR_IDENTIFIER: UInt32 = 256
SOURCETEXT_ATTR_MEMBERLOOKUP: UInt32 = 512
SOURCETEXT_ATTR_THIS: UInt32 = 1024
class AsyncIDebugApplicationNodeEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a2e3aa3b-aa8d-4ebf-84cd-648b737b8c13}')
    @commethod(3)
    def Begin_onAddChild(self, prddpChild: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugApplicationNode) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Finish_onAddChild(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Begin_onRemoveChild(self, prddpChild: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugApplicationNode) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Finish_onRemoveChild(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Begin_onDetach(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Finish_onDetach(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Begin_onAttach(self, prddpParent: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugApplicationNode) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Finish_onAttach(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
BREAKPOINT_STATE = Int32
BREAKPOINT_DELETED: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.BREAKPOINT_STATE = 0
BREAKPOINT_DISABLED: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.BREAKPOINT_STATE = 1
BREAKPOINT_ENABLED: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.BREAKPOINT_STATE = 2
BREAKREASON = Int32
BREAKREASON_STEP: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.BREAKREASON = 0
BREAKREASON_BREAKPOINT: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.BREAKREASON = 1
BREAKREASON_DEBUGGER_BLOCK: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.BREAKREASON = 2
BREAKREASON_HOST_INITIATED: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.BREAKREASON = 3
BREAKREASON_LANGUAGE_INITIATED: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.BREAKREASON = 4
BREAKREASON_DEBUGGER_HALT: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.BREAKREASON = 5
BREAKREASON_ERROR: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.BREAKREASON = 6
BREAKREASON_JIT: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.BREAKREASON = 7
BREAKREASON_MUTATION_BREAKPOINT: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.BREAKREASON = 8
BREAKRESUMEACTION = Int32
BREAKRESUMEACTION_ABORT: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.BREAKRESUMEACTION = 0
BREAKRESUMEACTION_CONTINUE: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.BREAKRESUMEACTION = 1
BREAKRESUMEACTION_STEP_INTO: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.BREAKRESUMEACTION = 2
BREAKRESUMEACTION_STEP_OVER: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.BREAKRESUMEACTION = 3
BREAKRESUMEACTION_STEP_OUT: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.BREAKRESUMEACTION = 4
BREAKRESUMEACTION_IGNORE: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.BREAKRESUMEACTION = 5
BREAKRESUMEACTION_STEP_DOCUMENT: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.BREAKRESUMEACTION = 6
CDebugDocumentHelper = Guid('{83b8bca6-687c-11d0-a405-00aa0060275c}')
DEBUG_EVENT_INFO_TYPE = Int32
DEIT_GENERAL: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.DEBUG_EVENT_INFO_TYPE = 0
DEIT_ASMJS_IN_DEBUGGING: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.DEBUG_EVENT_INFO_TYPE = 1
DEIT_ASMJS_SUCCEEDED: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.DEBUG_EVENT_INFO_TYPE = 2
DEIT_ASMJS_FAILED: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.DEBUG_EVENT_INFO_TYPE = 3
DEBUG_STACKFRAME_TYPE = Int32
DST_SCRIPT_FRAME: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.DEBUG_STACKFRAME_TYPE = 0
DST_INTERNAL_FRAME: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.DEBUG_STACKFRAME_TYPE = 1
DST_INVOCATION_FRAME: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.DEBUG_STACKFRAME_TYPE = 2
DOCUMENTNAMETYPE = Int32
DOCUMENTNAMETYPE_APPNODE: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.DOCUMENTNAMETYPE = 0
DOCUMENTNAMETYPE_TITLE: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.DOCUMENTNAMETYPE = 1
DOCUMENTNAMETYPE_FILE_TAIL: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.DOCUMENTNAMETYPE = 2
DOCUMENTNAMETYPE_URL: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.DOCUMENTNAMETYPE = 3
DOCUMENTNAMETYPE_UNIQUE_TITLE: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.DOCUMENTNAMETYPE = 4
DOCUMENTNAMETYPE_SOURCE_MAP_URL: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.DOCUMENTNAMETYPE = 5
DebugHelper = Guid('{0bfcc060-8c1d-11d0-accd-00aa0060275c}')
class DebugStackFrameDescriptor(Structure):
    pdsf: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugStackFrame
    dwMin: UInt32
    dwLim: UInt32
    fFinal: win32more.Windows.Win32.Foundation.BOOL
    punkFinal: win32more.Windows.Win32.System.Com.IUnknown
class DebugStackFrameDescriptor64(Structure):
    pdsf: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugStackFrame
    dwMin: UInt64
    dwLim: UInt64
    fFinal: win32more.Windows.Win32.Foundation.BOOL
    punkFinal: win32more.Windows.Win32.System.Com.IUnknown
DefaultDebugSessionProvider = Guid('{834128a2-51f4-11d0-8f20-00805f2cd064}')
ERRORRESUMEACTION = Int32
ERRORRESUMEACTION_ReexecuteErrorStatement: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.ERRORRESUMEACTION = 0
ERRORRESUMEACTION_AbortCallAndReturnErrorToCaller: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.ERRORRESUMEACTION = 1
ERRORRESUMEACTION_SkipErrorStatement: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.ERRORRESUMEACTION = 2
class IActiveScript(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bb1a2ae1-a4f9-11cf-8f20-00805f2cd064}')
    @commethod(3)
    def SetScriptSite(self, pass_: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IActiveScriptSite) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetScriptSite(self, riid: POINTER(Guid), ppvObject: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetScriptState(self, ss: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPTSTATE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetScriptState(self, pssState: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPTSTATE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Close(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def AddNamedItem(self, pstrName: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AddTypeLib(self, rguidTypeLib: POINTER(Guid), dwMajor: UInt32, dwMinor: UInt32, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetScriptDispatch(self, pstrItemName: win32more.Windows.Win32.Foundation.PWSTR, ppdisp: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetCurrentScriptThreadID(self, pstidThread: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetScriptThreadID(self, dwWin32ThreadId: UInt32, pstidThread: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetScriptThreadState(self, stidThread: UInt32, pstsState: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPTTHREADSTATE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def InterruptScriptThread(self, stidThread: UInt32, pexcepinfo: POINTER(win32more.Windows.Win32.System.Com.EXCEPINFO), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Clone(self, ppscript: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IActiveScript)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveScriptAuthor(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9c109da0-7006-11d1-b36c-00a0c911e8b2}')
    @commethod(3)
    def AddNamedItem(self, pszName: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, pdisp: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddScriptlet(self, pszDefaultName: win32more.Windows.Win32.Foundation.PWSTR, pszCode: win32more.Windows.Win32.Foundation.PWSTR, pszItemName: win32more.Windows.Win32.Foundation.PWSTR, pszSubItemName: win32more.Windows.Win32.Foundation.PWSTR, pszEventName: win32more.Windows.Win32.Foundation.PWSTR, pszDelimiter: win32more.Windows.Win32.Foundation.PWSTR, dwCookie: UInt32, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ParseScriptText(self, pszCode: win32more.Windows.Win32.Foundation.PWSTR, pszItemName: win32more.Windows.Win32.Foundation.PWSTR, pszDelimiter: win32more.Windows.Win32.Foundation.PWSTR, dwCookie: UInt32, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetScriptTextAttributes(self, pszCode: win32more.Windows.Win32.Foundation.PWSTR, cch: UInt32, pszDelimiter: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, pattr: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetScriptletTextAttributes(self, pszCode: win32more.Windows.Win32.Foundation.PWSTR, cch: UInt32, pszDelimiter: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, pattr: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetRoot(self, ppsp: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IScriptNode)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetLanguageFlags(self, pgrfasa: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetEventHandler(self, pdisp: win32more.Windows.Win32.System.Com.IDispatch, pszItem: win32more.Windows.Win32.Foundation.PWSTR, pszSubItem: win32more.Windows.Win32.Foundation.PWSTR, pszEvent: win32more.Windows.Win32.Foundation.PWSTR, ppse: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IScriptEntry)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RemoveNamedItem(self, pszName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def AddTypeLib(self, rguidTypeLib: POINTER(Guid), dwMajor: UInt32, dwMinor: UInt32, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def RemoveTypeLib(self, rguidTypeLib: POINTER(Guid), dwMajor: UInt32, dwMinor: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetChars(self, fRequestedList: UInt32, pbstrChars: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetInfoFromContext(self, pszCode: win32more.Windows.Win32.Foundation.PWSTR, cchCode: UInt32, ichCurrentPosition: UInt32, dwListTypesRequested: UInt32, pdwListTypesProvided: POINTER(UInt32), pichListAnchorPosition: POINTER(UInt32), pichFuncAnchorPosition: POINTER(UInt32), pmemid: POINTER(Int32), piCurrentParameter: POINTER(Int32), ppunk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def IsCommitChar(self, ch: Char, pfcommit: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveScriptAuthorProcedure(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7e2d4b70-bd9a-11d0-9336-00a0c90dcaa9}')
    @commethod(3)
    def ParseProcedureText(self, pszCode: win32more.Windows.Win32.Foundation.PWSTR, pszFormalParams: win32more.Windows.Win32.Foundation.PWSTR, pszProcedureName: win32more.Windows.Win32.Foundation.PWSTR, pszItemName: win32more.Windows.Win32.Foundation.PWSTR, pszDelimiter: win32more.Windows.Win32.Foundation.PWSTR, dwCookie: UInt32, dwFlags: UInt32, pdispFor: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveScriptDebug32(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c10-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def GetScriptTextAttributes(self, pstrCode: win32more.Windows.Win32.Foundation.PWSTR, uNumCodeChars: UInt32, pstrDelimiter: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, pattr: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetScriptletTextAttributes(self, pstrCode: win32more.Windows.Win32.Foundation.PWSTR, uNumCodeChars: UInt32, pstrDelimiter: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, pattr: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumCodeContextsOfPosition(self, dwSourceContext: UInt32, uCharacterOffset: UInt32, uNumChars: UInt32, ppescc: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IEnumDebugCodeContexts)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveScriptDebug64(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bc437e23-f5b8-47f4-bb79-7d1ce5483b86}')
    @commethod(3)
    def GetScriptTextAttributes(self, pstrCode: win32more.Windows.Win32.Foundation.PWSTR, uNumCodeChars: UInt32, pstrDelimiter: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, pattr: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetScriptletTextAttributes(self, pstrCode: win32more.Windows.Win32.Foundation.PWSTR, uNumCodeChars: UInt32, pstrDelimiter: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, pattr: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumCodeContextsOfPosition(self, dwSourceContext: UInt64, uCharacterOffset: UInt32, uNumChars: UInt32, ppescc: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IEnumDebugCodeContexts)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveScriptEncode(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bb1a2ae3-a4f9-11cf-8f20-00805f2cd064}')
    @commethod(3)
    def EncodeSection(self, pchIn: win32more.Windows.Win32.Foundation.PWSTR, cchIn: UInt32, pchOut: win32more.Windows.Win32.Foundation.PWSTR, cchOut: UInt32, pcchRet: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DecodeScript(self, pchIn: win32more.Windows.Win32.Foundation.PWSTR, cchIn: UInt32, pchOut: win32more.Windows.Win32.Foundation.PWSTR, cchOut: UInt32, pcchRet: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetEncodeProgId(self, pbstrOut: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveScriptError(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{eae1ba61-a4ed-11cf-8f20-00805f2cd064}')
    @commethod(3)
    def GetExceptionInfo(self, pexcepinfo: POINTER(win32more.Windows.Win32.System.Com.EXCEPINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSourcePosition(self, pdwSourceContext: POINTER(UInt32), pulLineNumber: POINTER(UInt32), plCharacterPosition: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSourceLineText(self, pbstrSourceLine: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveScriptError64(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IActiveScriptError
    _iid_ = Guid('{b21fb2a1-5b8f-4963-8c21-21450f84ed7f}')
    @commethod(6)
    def GetSourcePosition64(self, pdwSourceContext: POINTER(UInt64), pulLineNumber: POINTER(UInt32), plCharacterPosition: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveScriptErrorDebug(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IActiveScriptError
    _iid_ = Guid('{51973c12-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(6)
    def GetDocumentContext(self, ppssc: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugDocumentContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetStackFrame(self, ppdsf: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugStackFrame)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveScriptErrorDebug110(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{516e42b6-89a8-4530-937b-5f0708431442}')
    @commethod(3)
    def GetExceptionThrownKind(self, pExceptionKind: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPT_ERROR_DEBUG_EXCEPTION_THROWN_KIND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveScriptGarbageCollector(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6aa2c4a0-2b53-11d4-a2a0-00104bd35090}')
    @commethod(3)
    def CollectGarbage(self, scriptgctype: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPTGCTYPE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveScriptHostEncode(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bee9b76e-cfe3-11d1-b747-00c04fc2b085}')
    @commethod(3)
    def EncodeScriptHostFile(self, bstrInFile: win32more.Windows.Win32.Foundation.BSTR, pbstrOutFile: POINTER(win32more.Windows.Win32.Foundation.BSTR), cFlags: UInt32, bstrDefaultLang: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveScriptParse32(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bb1a2ae2-a4f9-11cf-8f20-00805f2cd064}')
    @commethod(3)
    def InitNew(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddScriptlet(self, pstrDefaultName: win32more.Windows.Win32.Foundation.PWSTR, pstrCode: win32more.Windows.Win32.Foundation.PWSTR, pstrItemName: win32more.Windows.Win32.Foundation.PWSTR, pstrSubItemName: win32more.Windows.Win32.Foundation.PWSTR, pstrEventName: win32more.Windows.Win32.Foundation.PWSTR, pstrDelimiter: win32more.Windows.Win32.Foundation.PWSTR, dwSourceContextCookie: UInt32, ulStartingLineNumber: UInt32, dwFlags: UInt32, pbstrName: POINTER(win32more.Windows.Win32.Foundation.BSTR), pexcepinfo: POINTER(win32more.Windows.Win32.System.Com.EXCEPINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ParseScriptText(self, pstrCode: win32more.Windows.Win32.Foundation.PWSTR, pstrItemName: win32more.Windows.Win32.Foundation.PWSTR, punkContext: win32more.Windows.Win32.System.Com.IUnknown, pstrDelimiter: win32more.Windows.Win32.Foundation.PWSTR, dwSourceContextCookie: UInt32, ulStartingLineNumber: UInt32, dwFlags: UInt32, pvarResult: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pexcepinfo: POINTER(win32more.Windows.Win32.System.Com.EXCEPINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveScriptParse64(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c7ef7658-e1ee-480e-97ea-d52cb4d76d17}')
    @commethod(3)
    def InitNew(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddScriptlet(self, pstrDefaultName: win32more.Windows.Win32.Foundation.PWSTR, pstrCode: win32more.Windows.Win32.Foundation.PWSTR, pstrItemName: win32more.Windows.Win32.Foundation.PWSTR, pstrSubItemName: win32more.Windows.Win32.Foundation.PWSTR, pstrEventName: win32more.Windows.Win32.Foundation.PWSTR, pstrDelimiter: win32more.Windows.Win32.Foundation.PWSTR, dwSourceContextCookie: UInt64, ulStartingLineNumber: UInt32, dwFlags: UInt32, pbstrName: POINTER(win32more.Windows.Win32.Foundation.BSTR), pexcepinfo: POINTER(win32more.Windows.Win32.System.Com.EXCEPINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ParseScriptText(self, pstrCode: win32more.Windows.Win32.Foundation.PWSTR, pstrItemName: win32more.Windows.Win32.Foundation.PWSTR, punkContext: win32more.Windows.Win32.System.Com.IUnknown, pstrDelimiter: win32more.Windows.Win32.Foundation.PWSTR, dwSourceContextCookie: UInt64, ulStartingLineNumber: UInt32, dwFlags: UInt32, pvarResult: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pexcepinfo: POINTER(win32more.Windows.Win32.System.Com.EXCEPINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveScriptParseProcedure2_32(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IActiveScriptParseProcedure32
    _iid_ = Guid('{71ee5b20-fb04-11d1-b3a8-00a0c911e8b2}')
class IActiveScriptParseProcedure2_64(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IActiveScriptParseProcedure64
    _iid_ = Guid('{fe7c4271-210c-448d-9f54-76dab7047b28}')
class IActiveScriptParseProcedure32(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{aa5b6a80-b834-11d0-932f-00a0c90dcaa9}')
    @commethod(3)
    def ParseProcedureText(self, pstrCode: win32more.Windows.Win32.Foundation.PWSTR, pstrFormalParams: win32more.Windows.Win32.Foundation.PWSTR, pstrProcedureName: win32more.Windows.Win32.Foundation.PWSTR, pstrItemName: win32more.Windows.Win32.Foundation.PWSTR, punkContext: win32more.Windows.Win32.System.Com.IUnknown, pstrDelimiter: win32more.Windows.Win32.Foundation.PWSTR, dwSourceContextCookie: UInt32, ulStartingLineNumber: UInt32, dwFlags: UInt32, ppdisp: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveScriptParseProcedure64(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c64713b6-e029-4cc5-9200-438b72890b6a}')
    @commethod(3)
    def ParseProcedureText(self, pstrCode: win32more.Windows.Win32.Foundation.PWSTR, pstrFormalParams: win32more.Windows.Win32.Foundation.PWSTR, pstrProcedureName: win32more.Windows.Win32.Foundation.PWSTR, pstrItemName: win32more.Windows.Win32.Foundation.PWSTR, punkContext: win32more.Windows.Win32.System.Com.IUnknown, pstrDelimiter: win32more.Windows.Win32.Foundation.PWSTR, dwSourceContextCookie: UInt64, ulStartingLineNumber: UInt32, dwFlags: UInt32, ppdisp: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveScriptParseProcedureOld32(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1cff0050-6fdd-11d0-9328-00a0c90dcaa9}')
    @commethod(3)
    def ParseProcedureText(self, pstrCode: win32more.Windows.Win32.Foundation.PWSTR, pstrFormalParams: win32more.Windows.Win32.Foundation.PWSTR, pstrItemName: win32more.Windows.Win32.Foundation.PWSTR, punkContext: win32more.Windows.Win32.System.Com.IUnknown, pstrDelimiter: win32more.Windows.Win32.Foundation.PWSTR, dwSourceContextCookie: UInt32, ulStartingLineNumber: UInt32, dwFlags: UInt32, ppdisp: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveScriptParseProcedureOld64(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{21f57128-08c9-4638-ba12-22d15d88dc5c}')
    @commethod(3)
    def ParseProcedureText(self, pstrCode: win32more.Windows.Win32.Foundation.PWSTR, pstrFormalParams: win32more.Windows.Win32.Foundation.PWSTR, pstrItemName: win32more.Windows.Win32.Foundation.PWSTR, punkContext: win32more.Windows.Win32.System.Com.IUnknown, pstrDelimiter: win32more.Windows.Win32.Foundation.PWSTR, dwSourceContextCookie: UInt64, ulStartingLineNumber: UInt32, dwFlags: UInt32, ppdisp: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveScriptProfilerCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{740eca23-7d9d-42e5-ba9d-f8b24b1c7a9b}')
    @commethod(3)
    def Initialize(self, dwContext: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Shutdown(self, hrReason: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ScriptCompiled(self, scriptId: Int32, type: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_SCRIPT_TYPE, pIDebugDocumentContext: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def FunctionCompiled(self, functionId: Int32, scriptId: Int32, pwszFunctionName: win32more.Windows.Win32.Foundation.PWSTR, pwszFunctionNameHint: win32more.Windows.Win32.Foundation.PWSTR, pIDebugDocumentContext: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnFunctionEnter(self, scriptId: Int32, functionId: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnFunctionExit(self, scriptId: Int32, functionId: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveScriptProfilerCallback2(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IActiveScriptProfilerCallback
    _iid_ = Guid('{31b7f8ad-a637-409c-b22f-040995b6103d}')
    @commethod(9)
    def OnFunctionEnterByName(self, pwszFunctionName: win32more.Windows.Win32.Foundation.PWSTR, type: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_SCRIPT_TYPE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def OnFunctionExitByName(self, pwszFunctionName: win32more.Windows.Win32.Foundation.PWSTR, type: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_SCRIPT_TYPE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveScriptProfilerCallback3(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IActiveScriptProfilerCallback2
    _iid_ = Guid('{6ac5ad25-2037-4687-91df-b59979d93d73}')
    @commethod(11)
    def SetWebWorkerId(self, webWorkerId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveScriptProfilerControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{784b5ff0-69b0-47d1-a7dc-2518f4230e90}')
    @commethod(3)
    def StartProfiling(self, clsidProfilerObject: POINTER(Guid), dwEventMask: UInt32, dwContext: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetProfilerEventMask(self, dwEventMask: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def StopProfiling(self, hrShutdownReason: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveScriptProfilerControl2(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IActiveScriptProfilerControl
    _iid_ = Guid('{47810165-498f-40be-94f1-653557e9e7da}')
    @commethod(6)
    def CompleteProfilerStart(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def PrepareProfilerStop(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveScriptProfilerControl3(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IActiveScriptProfilerControl2
    _iid_ = Guid('{0b403015-f381-4023-a5d0-6fed076de716}')
    @commethod(8)
    def EnumHeap(self, ppEnum: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IActiveScriptProfilerHeapEnum)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveScriptProfilerControl4(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IActiveScriptProfilerControl3
    _iid_ = Guid('{160f94fd-9dbc-40d4-9eac-2b71db3132f4}')
    @commethod(9)
    def SummarizeHeap(self, heapSummary: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_SUMMARY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveScriptProfilerControl5(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IActiveScriptProfilerControl4
    _iid_ = Guid('{1c01a2d1-8f0f-46a5-9720-0d7ed2c62f0a}')
    @commethod(10)
    def EnumHeap2(self, enumFlags: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_ENUM_FLAGS, ppEnum: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IActiveScriptProfilerHeapEnum)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveScriptProfilerHeapEnum(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{32e4694e-0d37-419b-b93d-fa20ded6e8ea}')
    @commethod(3)
    def Next(self, celt: UInt32, heapObjects: POINTER(POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_OBJECT)), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetOptionalInfo(self, heapObject: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_OBJECT), celt: UInt32, optionalInfo: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_OBJECT_OPTIONAL_INFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def FreeObjectAndOptionalInfo(self, celt: UInt32, heapObjects: POINTER(POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_OBJECT))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetNameIdMap(self, pNameList: POINTER(POINTER(POINTER(win32more.Windows.Win32.Foundation.PWSTR))), pcelt: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveScriptProperty(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4954e0d0-fbc7-11d1-8410-006008c3fbfc}')
    @commethod(3)
    def GetProperty(self, dwProperty: UInt32, pvarIndex: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetProperty(self, dwProperty: UInt32, pvarIndex: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveScriptSIPInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{764651d0-38de-11d4-a2a3-00104bd35090}')
    @commethod(3)
    def GetSIPOID(self, poid_sip: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveScriptSite(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{db01a1e3-a42b-11cf-8f20-00805f2cd064}')
    @commethod(3)
    def GetLCID(self, plcid: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetItemInfo(self, pstrName: win32more.Windows.Win32.Foundation.PWSTR, dwReturnMask: UInt32, ppiunkItem: POINTER(win32more.Windows.Win32.System.Com.IUnknown), ppti: POINTER(win32more.Windows.Win32.System.Com.ITypeInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDocVersionString(self, pbstrVersion: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnScriptTerminate(self, pvarResult: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pexcepinfo: POINTER(win32more.Windows.Win32.System.Com.EXCEPINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnStateChange(self, ssScriptState: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPTSTATE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnScriptError(self, pscripterror: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IActiveScriptError) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OnEnterScript(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def OnLeaveScript(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveScriptSiteDebug32(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c11-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def GetDocumentContextFromPosition(self, dwSourceContext: UInt32, uCharacterOffset: UInt32, uNumChars: UInt32, ppsc: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugDocumentContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetApplication(self, ppda: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugApplication32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetRootApplicationNode(self, ppdanRoot: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugApplicationNode)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnScriptErrorDebug(self, pErrorDebug: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IActiveScriptErrorDebug, pfEnterDebugger: POINTER(win32more.Windows.Win32.Foundation.BOOL), pfCallOnScriptErrorWhenContinuing: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveScriptSiteDebug64(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d6b96b0a-7463-402c-92ac-89984226942f}')
    @commethod(3)
    def GetDocumentContextFromPosition(self, dwSourceContext: UInt64, uCharacterOffset: UInt32, uNumChars: UInt32, ppsc: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugDocumentContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetApplication(self, ppda: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugApplication64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetRootApplicationNode(self, ppdanRoot: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugApplicationNode)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnScriptErrorDebug(self, pErrorDebug: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IActiveScriptErrorDebug, pfEnterDebugger: POINTER(win32more.Windows.Win32.Foundation.BOOL), pfCallOnScriptErrorWhenContinuing: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveScriptSiteDebugEx(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bb722ccb-6ad2-41c6-b780-af9c03ee69f5}')
    @commethod(3)
    def OnCanNotJITScriptErrorDebug(self, pErrorDebug: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IActiveScriptErrorDebug, pfCallOnScriptErrorWhenContinuing: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveScriptSiteInterruptPoll(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{539698a0-cdca-11cf-a5eb-00aa0047a063}')
    @commethod(3)
    def QueryContinue(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveScriptSiteTraceInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4b7272ae-1955-4bfe-98b0-780621888569}')
    @commethod(3)
    def SendScriptTraceInfo(self, stiEventType: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPTTRACEINFO, guidContextID: Guid, dwScriptContextCookie: UInt32, lScriptStatementStart: Int32, lScriptStatementEnd: Int32, dwReserved: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveScriptSiteUIControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{aedae97e-d7ee-4796-b960-7f092ae844ab}')
    @commethod(3)
    def GetUIBehavior(self, UicItem: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPTUICITEM, pUicHandling: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPTUICHANDLING)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveScriptSiteWindow(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d10f6761-83e9-11cf-8f20-00805f2cd064}')
    @commethod(3)
    def GetWindow(self, phwnd: POINTER(win32more.Windows.Win32.Foundation.HWND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EnableModeless(self, fEnable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveScriptStats(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b8da6310-e19b-11d0-933c-00a0c90dcaa9}')
    @commethod(3)
    def GetStat(self, stid: UInt32, pluHi: POINTER(UInt32), pluLo: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetStatEx(self, guid: POINTER(Guid), pluHi: POINTER(UInt32), pluLo: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ResetStats(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveScriptStringCompare(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{58562769-ed52-42f7-8403-4963514e1f11}')
    @commethod(3)
    def StrComp(self, bszStr1: win32more.Windows.Win32.Foundation.BSTR, bszStr2: win32more.Windows.Win32.Foundation.BSTR, iRet: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveScriptTraceInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c35456e7-bebf-4a1b-86a9-24d56be8b369}')
    @commethod(3)
    def StartScriptTracing(self, pSiteTraceInfo: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IActiveScriptSiteTraceInfo, guidContextID: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def StopScriptTracing(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveScriptWinRTErrorDebug(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IActiveScriptError
    _iid_ = Guid('{73a3f82a-0fe9-4b33-ba3b-fe095f697e0a}')
    @commethod(6)
    def GetRestrictedErrorString(self, errorString: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetRestrictedErrorReference(self, referenceString: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetCapabilitySid(self, capabilitySid: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IApplicationDebugger(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c2a-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def QueryAlive(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateInstanceAtDebugger(self, rclsid: POINTER(Guid), pUnkOuter: win32more.Windows.Win32.System.Com.IUnknown, dwClsContext: UInt32, riid: POINTER(Guid), ppvObject: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def onDebugOutput(self, pstr: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def onHandleBreakPoint(self, prpt: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IRemoteDebugApplicationThread, br: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.BREAKREASON, pError: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IActiveScriptErrorDebug) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def onClose(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def onDebuggerEvent(self, riid: POINTER(Guid), punk: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IApplicationDebuggerUI(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c2b-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def BringDocumentToTop(self, pddt: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugDocumentText) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def BringDocumentContextToTop(self, pddc: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugDocumentContext) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBindEventHandler(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{63cdbcb0-c1b1-11d0-9336-00a0c90dcaa9}')
    @commethod(3)
    def BindHandler(self, pstrEvent: win32more.Windows.Win32.Foundation.PWSTR, pdisp: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDebugApplication11032(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IRemoteDebugApplication110
    _iid_ = Guid('{bdb3b5de-89f2-4e11-84a5-97445f941c7d}')
    @commethod(6)
    def SynchronousCallInMainThread(self, pptc: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugThreadCall32, dwParam1: UIntPtr, dwParam2: UIntPtr, dwParam3: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def AsynchronousCallInMainThread(self, pptc: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugThreadCall32, dwParam1: UIntPtr, dwParam2: UIntPtr, dwParam3: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CallableWaitForHandles(self, handleCount: UInt32, pHandles: POINTER(win32more.Windows.Win32.Foundation.HANDLE), pIndex: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDebugApplication11064(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IRemoteDebugApplication110
    _iid_ = Guid('{2039d958-4eeb-496a-87bb-2e5201eadeef}')
    @commethod(6)
    def SynchronousCallInMainThread(self, pptc: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugThreadCall64, dwParam1: UIntPtr, dwParam2: UIntPtr, dwParam3: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def AsynchronousCallInMainThread(self, pptc: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugThreadCall64, dwParam1: UIntPtr, dwParam2: UIntPtr, dwParam3: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CallableWaitForHandles(self, handleCount: UInt32, pHandles: POINTER(win32more.Windows.Win32.Foundation.HANDLE), pIndex: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDebugApplication32(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IRemoteDebugApplication
    _iid_ = Guid('{51973c32-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(14)
    def SetName(self, pstrName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def StepOutComplete(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def DebugOutput(self, pstr: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def StartDebugSession(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def HandleBreakPoint(self, br: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.BREAKREASON, pbra: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.BREAKRESUMEACTION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def Close(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetBreakFlags(self, pabf: POINTER(UInt32), pprdatSteppingThread: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IRemoteDebugApplicationThread)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetCurrentThread(self, pat: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugApplicationThread)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def CreateAsyncDebugOperation(self, psdo: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugSyncOperation, ppado: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugAsyncOperation)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def AddStackFrameSniffer(self, pdsfs: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugStackFrameSniffer, pdwCookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def RemoveStackFrameSniffer(self, dwCookie: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def QueryCurrentThreadIsDebuggerThread(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def SynchronousCallInDebuggerThread(self, pptc: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugThreadCall32, dwParam1: UInt32, dwParam2: UInt32, dwParam3: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def CreateApplicationNode(self, ppdanNew: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugApplicationNode)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def FireDebuggerEvent(self, riid: POINTER(Guid), punk: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def HandleRuntimeError(self, pErrorDebug: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IActiveScriptErrorDebug, pScriptSite: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IActiveScriptSite, pbra: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.BREAKRESUMEACTION), perra: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.ERRORRESUMEACTION), pfCallOnScriptError: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def FCanJitDebug(self) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(31)
    def FIsAutoJitDebugEnabled(self) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(32)
    def AddGlobalExpressionContextProvider(self, pdsfs: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IProvideExpressionContexts, pdwCookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def RemoveGlobalExpressionContextProvider(self, dwCookie: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDebugApplication64(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IRemoteDebugApplication
    _iid_ = Guid('{4dedc754-04c7-4f10-9e60-16a390fe6e62}')
    @commethod(14)
    def SetName(self, pstrName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def StepOutComplete(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def DebugOutput(self, pstr: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def StartDebugSession(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def HandleBreakPoint(self, br: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.BREAKREASON, pbra: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.BREAKRESUMEACTION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def Close(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetBreakFlags(self, pabf: POINTER(UInt32), pprdatSteppingThread: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IRemoteDebugApplicationThread)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetCurrentThread(self, pat: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugApplicationThread)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def CreateAsyncDebugOperation(self, psdo: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugSyncOperation, ppado: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugAsyncOperation)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def AddStackFrameSniffer(self, pdsfs: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugStackFrameSniffer, pdwCookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def RemoveStackFrameSniffer(self, dwCookie: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def QueryCurrentThreadIsDebuggerThread(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def SynchronousCallInDebuggerThread(self, pptc: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugThreadCall64, dwParam1: UInt64, dwParam2: UInt64, dwParam3: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def CreateApplicationNode(self, ppdanNew: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugApplicationNode)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def FireDebuggerEvent(self, riid: POINTER(Guid), punk: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def HandleRuntimeError(self, pErrorDebug: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IActiveScriptErrorDebug, pScriptSite: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IActiveScriptSite, pbra: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.BREAKRESUMEACTION), perra: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.ERRORRESUMEACTION), pfCallOnScriptError: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def FCanJitDebug(self) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(31)
    def FIsAutoJitDebugEnabled(self) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(32)
    def AddGlobalExpressionContextProvider(self, pdsfs: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IProvideExpressionContexts, pdwCookie: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def RemoveGlobalExpressionContextProvider(self, dwCookie: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDebugApplicationNode(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugDocumentProvider
    _iid_ = Guid('{51973c34-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(6)
    def EnumChildren(self, pperddp: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IEnumDebugApplicationNodes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetParent(self, pprddp: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugApplicationNode)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetDocumentProvider(self, pddp: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugDocumentProvider) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Close(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Attach(self, pdanParent: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugApplicationNode) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Detach(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDebugApplicationNode100(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{90a7734e-841b-4f77-9384-a2891e76e7e2}')
    @commethod(3)
    def SetFilterForEventSink(self, dwCookie: UInt32, filter: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.APPLICATION_NODE_EVENT_FILTER) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetExcludedDocuments(self, filter: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.APPLICATION_NODE_EVENT_FILTER, pDocuments: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.TEXT_DOCUMENT_ARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def QueryIsChildNode(self, pSearchKey: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugDocument) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDebugApplicationNodeEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c35-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def onAddChild(self, prddpChild: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugApplicationNode) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def onRemoveChild(self, prddpChild: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugApplicationNode) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def onDetach(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def onAttach(self, prddpParent: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugApplicationNode) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDebugApplicationThread(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IRemoteDebugApplicationThread
    _iid_ = Guid('{51973c38-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(12)
    def SynchronousCallIntoThread32(self, pstcb: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugThreadCall32, dwParam1: UInt32, dwParam2: UInt32, dwParam3: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def QueryIsCurrentThread(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def QueryIsDebuggerThread(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetDescription(self, pstrDescription: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetStateString(self, pstrState: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDebugApplicationThread11032(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2194ac5c-6561-404a-a2e9-f57d72de3702}')
    @commethod(3)
    def GetActiveThreadRequestCount(self, puiThreadRequests: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def IsSuspendedForBreakPoint(self, pfIsSuspended: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def IsThreadCallable(self, pfIsCallable: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AsynchronousCallIntoThread(self, pptc: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugThreadCall32, dwParam1: UIntPtr, dwParam2: UIntPtr, dwParam3: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDebugApplicationThread11064(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{420aa4cc-efd8-4dac-983b-47127826917d}')
    @commethod(3)
    def GetActiveThreadRequestCount(self, puiThreadRequests: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def IsSuspendedForBreakPoint(self, pfIsSuspended: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def IsThreadCallable(self, pfIsCallable: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AsynchronousCallIntoThread(self, pptc: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugThreadCall64, dwParam1: UIntPtr, dwParam2: UIntPtr, dwParam3: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDebugApplicationThread64(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugApplicationThread
    _iid_ = Guid('{9dac5886-dbad-456d-9dee-5dec39ab3dda}')
    @commethod(17)
    def SynchronousCallIntoThread64(self, pstcb: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugThreadCall64, dwParam1: UInt64, dwParam2: UInt64, dwParam3: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDebugApplicationThreadEvents110(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{84e5e468-d5da-48a8-83f4-40366429007b}')
    @commethod(3)
    def OnSuspendForBreakPoint(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnResumeFromBreakPoint(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnThreadRequestComplete(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnBeginThreadRequest(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDebugAsyncOperation(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c1b-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def GetSyncDebugOperation(self, ppsdo: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugSyncOperation)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Start(self, padocb: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugAsyncOperationCallBack) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Abort(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def QueryIsComplete(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetResult(self, phrResult: POINTER(win32more.Windows.Win32.Foundation.HRESULT), ppunkResult: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDebugAsyncOperationCallBack(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c1c-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def onComplete(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDebugCodeContext(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c13-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def GetDocumentContext(self, ppsc: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugDocumentContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetBreakPoint(self, bps: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.BREAKPOINT_STATE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDebugCookie(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c39-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def SetDebugCookie(self, dwDebugAppCookie: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDebugDocument(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugDocumentInfo
    _iid_ = Guid('{51973c21-cb0c-11d0-b5c9-00a0244a0e7a}')
class IDebugDocumentContext(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c28-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def GetDocument(self, ppsd: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugDocument)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EnumCodeContexts(self, ppescc: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IEnumDebugCodeContexts)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDebugDocumentHelper32(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c26-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def Init(self, pda: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugApplication32, pszShortName: win32more.Windows.Win32.Foundation.PWSTR, pszLongName: win32more.Windows.Win32.Foundation.PWSTR, docAttr: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Attach(self, pddhParent: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugDocumentHelper32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Detach(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AddUnicodeText(self, pszText: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def AddDBCSText(self, pszText: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetDebugDocumentHost(self, pddh: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugDocumentHost) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AddDeferredText(self, cChars: UInt32, dwTextStartCookie: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def DefineScriptBlock(self, ulCharOffset: UInt32, cChars: UInt32, pas: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IActiveScript, fScriptlet: win32more.Windows.Win32.Foundation.BOOL, pdwSourceContext: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetDefaultTextAttr(self, staTextAttr: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetTextAttributes(self, ulCharOffset: UInt32, cChars: UInt32, pstaTextAttr: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetLongName(self, pszLongName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetShortName(self, pszShortName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetDocumentAttr(self, pszAttributes: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetDebugApplicationNode(self, ppdan: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugApplicationNode)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetScriptBlockInfo(self, dwSourceContext: UInt32, ppasd: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IActiveScript), piCharPos: POINTER(UInt32), pcChars: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def CreateDebugDocumentContext(self, iCharPos: UInt32, cChars: UInt32, ppddc: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugDocumentContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def BringDocumentToTop(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def BringDocumentContextToTop(self, pddc: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugDocumentContext) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDebugDocumentHelper64(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c4c7363c-20fd-47f9-bd82-4855e0150871}')
    @commethod(3)
    def Init(self, pda: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugApplication64, pszShortName: win32more.Windows.Win32.Foundation.PWSTR, pszLongName: win32more.Windows.Win32.Foundation.PWSTR, docAttr: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Attach(self, pddhParent: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugDocumentHelper64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Detach(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AddUnicodeText(self, pszText: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def AddDBCSText(self, pszText: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetDebugDocumentHost(self, pddh: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugDocumentHost) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AddDeferredText(self, cChars: UInt32, dwTextStartCookie: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def DefineScriptBlock(self, ulCharOffset: UInt32, cChars: UInt32, pas: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IActiveScript, fScriptlet: win32more.Windows.Win32.Foundation.BOOL, pdwSourceContext: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetDefaultTextAttr(self, staTextAttr: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetTextAttributes(self, ulCharOffset: UInt32, cChars: UInt32, pstaTextAttr: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetLongName(self, pszLongName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetShortName(self, pszShortName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetDocumentAttr(self, pszAttributes: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetDebugApplicationNode(self, ppdan: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugApplicationNode)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetScriptBlockInfo(self, dwSourceContext: UInt64, ppasd: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IActiveScript), piCharPos: POINTER(UInt32), pcChars: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def CreateDebugDocumentContext(self, iCharPos: UInt32, cChars: UInt32, ppddc: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugDocumentContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def BringDocumentToTop(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def BringDocumentContextToTop(self, pddc: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugDocumentContext) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDebugDocumentHost(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c27-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def GetDeferredText(self, dwTextStartCookie: UInt32, pcharText: win32more.Windows.Win32.Foundation.PWSTR, pstaTextAttr: POINTER(UInt16), pcNumChars: POINTER(UInt32), cMaxChars: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetScriptTextAttributes(self, pstrCode: win32more.Windows.Win32.Foundation.PWSTR, uNumCodeChars: UInt32, pstrDelimiter: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, pattr: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnCreateDocumentContext(self, ppunkOuter: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPathName(self, pbstrLongName: POINTER(win32more.Windows.Win32.Foundation.BSTR), pfIsOriginalFile: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetFileName(self, pbstrShortName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def NotifyChanged(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDebugDocumentInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c1f-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def GetName(self, dnt: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.DOCUMENTNAMETYPE, pbstrName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDocumentClassId(self, pclsidDocument: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDebugDocumentProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugDocumentInfo
    _iid_ = Guid('{51973c20-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(5)
    def GetDocument(self, ppssd: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugDocument)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDebugDocumentText(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugDocument
    _iid_ = Guid('{51973c22-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(5)
    def GetDocumentAttributes(self, ptextdocattr: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSize(self, pcNumLines: POINTER(UInt32), pcNumChars: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetPositionOfLine(self, cLineNumber: UInt32, pcCharacterPosition: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetLineOfPosition(self, cCharacterPosition: UInt32, pcLineNumber: POINTER(UInt32), pcCharacterOffsetInLine: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetText(self, cCharacterPosition: UInt32, pcharText: win32more.Windows.Win32.Foundation.PWSTR, pstaTextAttr: POINTER(UInt16), pcNumChars: POINTER(UInt32), cMaxChars: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetPositionOfContext(self, psc: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugDocumentContext, pcCharacterPosition: POINTER(UInt32), cNumChars: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetContextOfPosition(self, cCharacterPosition: UInt32, cNumChars: UInt32, ppsc: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugDocumentContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDebugDocumentTextAuthor(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugDocumentText
    _iid_ = Guid('{51973c24-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(12)
    def InsertText(self, cCharacterPosition: UInt32, cNumToInsert: UInt32, pcharText: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def RemoveText(self, cCharacterPosition: UInt32, cNumToRemove: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def ReplaceText(self, cCharacterPosition: UInt32, cNumToReplace: UInt32, pcharText: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDebugDocumentTextEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c23-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def onDestroy(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def onInsertText(self, cCharacterPosition: UInt32, cNumToInsert: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def onRemoveText(self, cCharacterPosition: UInt32, cNumToRemove: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def onReplaceText(self, cCharacterPosition: UInt32, cNumToReplace: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def onUpdateTextAttributes(self, cCharacterPosition: UInt32, cNumToUpdate: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def onUpdateDocumentAttributes(self, textdocattr: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDebugDocumentTextExternalAuthor(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c25-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def GetPathName(self, pbstrLongName: POINTER(win32more.Windows.Win32.Foundation.BSTR), pfIsOriginalFile: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFileName(self, pbstrShortName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def NotifyChanged(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDebugExpression(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c14-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def Start(self, pdecb: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugExpressionCallBack) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Abort(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def QueryIsComplete(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetResultAsString(self, phrResult: POINTER(win32more.Windows.Win32.Foundation.HRESULT), pbstrResult: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetResultAsDebugProperty(self, phrResult: POINTER(win32more.Windows.Win32.Foundation.HRESULT), ppdp: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IDebugProperty)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDebugExpressionCallBack(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c16-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def onComplete(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDebugExpressionContext(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c15-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def ParseLanguageText(self, pstrCode: win32more.Windows.Win32.Foundation.PWSTR, nRadix: UInt32, pstrDelimiter: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, ppe: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugExpression)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLanguageInfo(self, pbstrLanguageName: POINTER(win32more.Windows.Win32.Foundation.BSTR), pLanguageID: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDebugFormatter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c05-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def GetStringForVariant(self, pvar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), nRadix: UInt32, pbstrValue: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetVariantForString(self, pwstrValue: win32more.Windows.Win32.Foundation.PWSTR, pvar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetStringForVarType(self, vt: win32more.Windows.Win32.System.Variant.VARENUM, ptdescArrayType: POINTER(win32more.Windows.Win32.System.Com.TYPEDESC), pbstr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDebugHelper(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c3f-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def CreatePropertyBrowser(self, pvar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), bstrName: win32more.Windows.Win32.Foundation.PWSTR, pdat: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugApplicationThread, ppdob: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IDebugProperty)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreatePropertyBrowserEx(self, pvar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), bstrName: win32more.Windows.Win32.Foundation.PWSTR, pdat: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugApplicationThread, pdf: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugFormatter, ppdob: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IDebugProperty)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateSimpleConnectionPoint(self, pdisp: win32more.Windows.Win32.System.Com.IDispatch, ppscp: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.ISimpleConnectionPoint)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDebugSessionProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c29-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def StartDebugSession(self, pda: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IRemoteDebugApplication) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDebugStackFrame(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c17-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def GetCodeContext(self, ppcc: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugCodeContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDescriptionString(self, fLong: win32more.Windows.Win32.Foundation.BOOL, pbstrDescription: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetLanguageString(self, fLong: win32more.Windows.Win32.Foundation.BOOL, pbstrLanguage: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetThread(self, ppat: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugApplicationThread)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDebugProperty(self, ppDebugProp: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.IDebugProperty)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDebugStackFrame110(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugStackFrame
    _iid_ = Guid('{4b509611-b6ea-4b24-adcb-d0ccfd1a7e33}')
    @commethod(8)
    def GetStackFrameType(self, pStackFrameKind: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.DEBUG_STACKFRAME_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetScriptInvocationContext(self, ppInvocationContext: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IScriptInvocationContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDebugStackFrameSniffer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c18-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def EnumStackFrames(self, ppedsf: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IEnumDebugStackFrames)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDebugStackFrameSnifferEx32(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugStackFrameSniffer
    _iid_ = Guid('{51973c19-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(4)
    def EnumStackFramesEx32(self, dwSpMin: UInt32, ppedsf: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IEnumDebugStackFrames)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDebugStackFrameSnifferEx64(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugStackFrameSniffer
    _iid_ = Guid('{8cd12af4-49c1-4d52-8d8a-c146f47581aa}')
    @commethod(4)
    def EnumStackFramesEx64(self, dwSpMin: UInt64, ppedsf: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IEnumDebugStackFrames64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDebugSyncOperation(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c1a-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def GetTargetThread(self, ppatTarget: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugApplicationThread)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Execute(self, ppunkResult: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def InProgressAbort(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDebugThreadCall32(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c36-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def ThreadCallHandler(self, dwParam1: UInt32, dwParam2: UInt32, dwParam3: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDebugThreadCall64(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{cb3fa335-e979-42fd-9fcf-a7546a0f3905}')
    @commethod(3)
    def ThreadCallHandler(self, dwParam1: UInt64, dwParam2: UInt64, dwParam3: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumDebugApplicationNodes(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c3a-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def Next(self, celt: UInt32, pprddp: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugApplicationNode), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, pperddp: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IEnumDebugApplicationNodes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumDebugCodeContexts(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c1d-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def Next(self, celt: UInt32, pscc: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugCodeContext), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppescc: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IEnumDebugCodeContexts)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumDebugExpressionContexts(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c40-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def Next(self, celt: UInt32, ppdec: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugExpressionContext), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppedec: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IEnumDebugExpressionContexts)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumDebugStackFrames(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c1e-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def Next(self, celt: UInt32, prgdsfd: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.DebugStackFrameDescriptor), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppedsf: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IEnumDebugStackFrames)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumDebugStackFrames64(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IEnumDebugStackFrames
    _iid_ = Guid('{0dc38853-c1b0-4176-a984-b298361027af}')
    @commethod(7)
    def Next64(self, celt: UInt32, prgdsfd: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.DebugStackFrameDescriptor64), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumJsStackFrames(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5e7da34b-fb51-4791-abe7-cb5bdf419755}')
    @commethod(3)
    def Next(self, cFrameCount: UInt32, pFrames: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.JS_NATIVE_FRAME), pcFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumRemoteDebugApplicationThreads(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c3c-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def Next(self, celt: UInt32, pprdat: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IRemoteDebugApplicationThread), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, pperdat: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IEnumRemoteDebugApplicationThreads)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumRemoteDebugApplications(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c3b-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def Next(self, celt: UInt32, ppda: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IRemoteDebugApplication), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppessd: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IEnumRemoteDebugApplications)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IJsDebug(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{be0e89da-2ac5-4c04-ac5e-59956aae3613}')
    @commethod(3)
    def OpenVirtualProcess(self, processId: UInt32, runtimeJsBaseAddress: UInt64, pDataTarget: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IJsDebugDataTarget, ppProcess: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IJsDebugProcess)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IJsDebugBreakPoint(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{df6773e3-ed8d-488b-8a3e-5812577d1542}')
    @commethod(3)
    def IsEnabled(self, pIsEnabled: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Enable(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Disable(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Delete(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDocumentPosition(self, pDocumentId: POINTER(UInt64), pCharacterOffset: POINTER(UInt32), pStatementCharCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IJsDebugDataTarget(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{53b28977-53a1-48e5-9000-5d0dfa893931}')
    @commethod(3)
    def ReadMemory(self, address: UInt64, flags: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.JsDebugReadMemoryFlags, pBuffer: POINTER(Byte), size: UInt32, pBytesRead: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def WriteMemory(self, address: UInt64, pMemory: POINTER(Byte), size: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AllocateVirtualMemory(self, address: UInt64, size: UInt32, allocationType: UInt32, pageProtection: UInt32, pAllocatedAddress: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def FreeVirtualMemory(self, address: UInt64, size: UInt32, freeType: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetTlsValue(self, threadId: UInt32, tlsIndex: UInt32, pValue: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ReadBSTR(self, address: UInt64, pString: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ReadNullTerminatedString(self, address: UInt64, characterSize: UInt16, maxCharacters: UInt32, pString: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CreateStackFrameEnumerator(self, threadId: UInt32, ppEnumerator: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IEnumJsStackFrames)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetThreadContext(self, threadId: UInt32, contextFlags: UInt32, contextSize: UInt32, pContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IJsDebugFrame(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c9196637-ab9d-44b2-bad2-13b95b3f390e}')
    @commethod(3)
    def GetStackRange(self, pStart: POINTER(UInt64), pEnd: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetName(self, pName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDocumentPositionWithId(self, pDocumentId: POINTER(UInt64), pCharacterOffset: POINTER(UInt32), pStatementCharCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetDocumentPositionWithName(self, pDocumentName: POINTER(win32more.Windows.Win32.Foundation.BSTR), pLine: POINTER(UInt32), pColumn: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDebugProperty(self, ppDebugProperty: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IJsDebugProperty)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetReturnAddress(self, pReturnAddress: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Evaluate(self, pExpressionText: win32more.Windows.Win32.Foundation.PWSTR, ppDebugProperty: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IJsDebugProperty), pError: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IJsDebugProcess(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3d587168-6a2d-4041-bd3b-0de674502862}')
    @commethod(3)
    def CreateStackWalker(self, threadId: UInt32, ppStackWalker: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IJsDebugStackWalker)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateBreakPoint(self, documentId: UInt64, characterOffset: UInt32, characterCount: UInt32, isEnabled: win32more.Windows.Win32.Foundation.BOOL, ppDebugBreakPoint: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IJsDebugBreakPoint)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def PerformAsyncBreak(self, threadId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetExternalStepAddress(self, pCodeAddress: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IJsDebugProperty(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f8ffcf2b-3aa4-4320-85c3-52a312ba9633}')
    @commethod(3)
    def GetPropertyInfo(self, nRadix: UInt32, pPropertyInfo: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.JsDebugPropertyInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMembers(self, members: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.JS_PROPERTY_MEMBERS, ppEnum: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IJsEnumDebugProperty)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IJsDebugStackWalker(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{db24b094-73c4-456c-a4ec-e90ea00bdfe3}')
    @commethod(3)
    def GetNext(self, ppFrame: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IJsDebugFrame)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IJsEnumDebugProperty(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4092432f-2f0f-4fe1-b638-5b74a52cdcbe}')
    @commethod(3)
    def Next(self, count: UInt32, ppDebugProperty: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IJsDebugProperty), pActualCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCount(self, pCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMachineDebugManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c2c-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def AddApplication(self, pda: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IRemoteDebugApplication, pdwAppCookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RemoveApplication(self, dwAppCookie: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumApplications(self, ppeda: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IEnumRemoteDebugApplications)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMachineDebugManagerCookie(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c2d-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def AddApplication(self, pda: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IRemoteDebugApplication, dwDebugAppCookie: UInt32, pdwAppCookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RemoveApplication(self, dwDebugAppCookie: UInt32, dwAppCookie: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumApplications(self, ppeda: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IEnumRemoteDebugApplications)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMachineDebugManagerEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c2e-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def onAddApplication(self, pda: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IRemoteDebugApplication, dwAppCookie: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def onRemoveApplication(self, pda: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IRemoteDebugApplication, dwAppCookie: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IProcessDebugManager32(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c2f-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def CreateApplication(self, ppda: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugApplication32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDefaultApplication(self, ppda: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugApplication32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddApplication(self, pda: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugApplication32, pdwAppCookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveApplication(self, dwAppCookie: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateDebugDocumentHelper(self, punkOuter: win32more.Windows.Win32.System.Com.IUnknown, pddh: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugDocumentHelper32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IProcessDebugManager64(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{56b9fc1c-63a9-4cc1-ac21-087d69a17fab}')
    @commethod(3)
    def CreateApplication(self, ppda: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugApplication64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDefaultApplication(self, ppda: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugApplication64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddApplication(self, pda: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugApplication64, pdwAppCookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveApplication(self, dwAppCookie: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateDebugDocumentHelper(self, punkOuter: win32more.Windows.Win32.System.Com.IUnknown, pddh: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugDocumentHelper64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IProvideExpressionContexts(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c41-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def EnumExpressionContexts(self, ppedec: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IEnumDebugExpressionContexts)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRemoteDebugApplication(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c30-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def ResumeFromBreakPoint(self, prptFocus: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IRemoteDebugApplicationThread, bra: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.BREAKRESUMEACTION, era: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.ERRORRESUMEACTION) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CauseBreak(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ConnectDebugger(self, pad: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IApplicationDebugger) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def DisconnectDebugger(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDebugger(self, pad: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IApplicationDebugger)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CreateInstanceAtApplication(self, rclsid: POINTER(Guid), pUnkOuter: win32more.Windows.Win32.System.Com.IUnknown, dwClsContext: UInt32, riid: POINTER(Guid), ppvObject: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def QueryAlive(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def EnumThreads(self, pperdat: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IEnumRemoteDebugApplicationThreads)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetName(self, pbstrName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetRootNode(self, ppdanRoot: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugApplicationNode)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def EnumGlobalExpressionContexts(self, ppedec: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IEnumDebugExpressionContexts)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRemoteDebugApplication110(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d5fe005b-2836-485e-b1f9-89d91aa24fd4}')
    @commethod(3)
    def SetDebuggerOptions(self, mask: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPT_DEBUGGER_OPTIONS, value: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPT_DEBUGGER_OPTIONS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCurrentDebuggerOptions(self, pCurrentOptions: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPT_DEBUGGER_OPTIONS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetMainThread(self, ppThread: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IRemoteDebugApplicationThread)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRemoteDebugApplicationEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c33-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def OnConnectDebugger(self, pad: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IApplicationDebugger) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnDisconnectDebugger(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnSetName(self, pstrName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnDebugOutput(self, pstr: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnClose(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnEnterBreakPoint(self, prdat: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IRemoteDebugApplicationThread) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OnLeaveBreakPoint(self, prdat: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IRemoteDebugApplicationThread) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def OnCreateThread(self, prdat: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IRemoteDebugApplicationThread) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def OnDestroyThread(self, prdat: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IRemoteDebugApplicationThread) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def OnBreakFlagChange(self, abf: UInt32, prdatSteppingThread: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IRemoteDebugApplicationThread) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRemoteDebugApplicationThread(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c37-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def GetSystemThreadId(self, dwThreadId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetApplication(self, pprda: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IRemoteDebugApplication)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumStackFrames(self, ppedsf: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IEnumDebugStackFrames)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetDescription(self, pbstrDescription: POINTER(win32more.Windows.Win32.Foundation.BSTR), pbstrState: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetNextStatement(self, pStackFrame: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugStackFrame, pCodeContext: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugCodeContext) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetState(self, pState: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Suspend(self, pdwCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Resume(self, pdwCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetSuspendCount(self, pdwCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRemoteDebugCriticalErrorEvent110(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2f69c611-6b14-47e8-9260-4bb7c52f504b}')
    @commethod(3)
    def GetErrorInfo(self, pbstrSource: POINTER(win32more.Windows.Win32.Foundation.BSTR), pMessageId: POINTER(Int32), pbstrMessage: POINTER(win32more.Windows.Win32.Foundation.BSTR), ppLocation: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugDocumentContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRemoteDebugInfoEvent110(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9ff56bb6-eb89-4c0f-8823-cc2a4c0b7f26}')
    @commethod(3)
    def GetEventInfo(self, pMessageType: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.DEBUG_EVENT_INFO_TYPE), pbstrMessage: POINTER(win32more.Windows.Win32.Foundation.BSTR), pbstrUrl: POINTER(win32more.Windows.Win32.Foundation.BSTR), ppLocation: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugDocumentContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IScriptEntry(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IScriptNode
    _iid_ = Guid('{0aee2a95-bcbb-11d0-8c72-00c04fc2b085}')
    @commethod(13)
    def GetText(self, pbstr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetText(self, psz: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetBody(self, pbstr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetBody(self, psz: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetName(self, pbstr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetName(self, psz: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetItemName(self, pbstr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SetItemName(self, psz: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetSignature(self, ppti: POINTER(win32more.Windows.Win32.System.Com.ITypeInfo), piMethod: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SetSignature(self, pti: win32more.Windows.Win32.System.Com.ITypeInfo, iMethod: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetRange(self, pichMin: POINTER(UInt32), pcch: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IScriptInvocationContext(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5d7741b7-af7e-4a2a-85e5-c77f4d0659fb}')
    @commethod(3)
    def GetContextType(self, pInvocationContextType: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPT_INVOCATION_CONTEXT_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetContextDescription(self, pDescription: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetContextObject(self, ppContextObject: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IScriptNode(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0aee2a94-bcbb-11d0-8c72-00c04fc2b085}')
    @commethod(3)
    def Alive(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Delete(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetParent(self, ppsnParent: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IScriptNode)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetIndexInParent(self, pisn: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCookie(self, pdwCookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetNumberOfChildren(self, pcsn: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetChild(self, isn: UInt32, ppsn: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IScriptNode)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetLanguage(self, pbstr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def CreateChildEntry(self, isn: UInt32, dwCookie: UInt32, pszDelimiter: win32more.Windows.Win32.Foundation.PWSTR, ppse: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IScriptEntry)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def CreateChildHandler(self, pszDefaultName: win32more.Windows.Win32.Foundation.PWSTR, prgpszNames: POINTER(win32more.Windows.Win32.Foundation.PWSTR), cpszNames: UInt32, pszEvent: win32more.Windows.Win32.Foundation.PWSTR, pszDelimiter: win32more.Windows.Win32.Foundation.PWSTR, ptiSignature: win32more.Windows.Win32.System.Com.ITypeInfo, iMethodSignature: UInt32, isn: UInt32, dwCookie: UInt32, ppse: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IScriptEntry)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IScriptScriptlet(ComPtr):
    extends: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IScriptEntry
    _iid_ = Guid('{0aee2a96-bcbb-11d0-8c72-00c04fc2b085}')
    @commethod(24)
    def GetSubItemName(self, pbstr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def SetSubItemName(self, psz: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetEventName(self, pbstr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def SetEventName(self, psz: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetSimpleEventName(self, pbstr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def SetSimpleEventName(self, psz: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISimpleConnectionPoint(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51973c3e-cb0c-11d0-b5c9-00a0244a0e7a}')
    @commethod(3)
    def GetEventCount(self, pulCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DescribeEvents(self, iEvent: UInt32, cEvents: UInt32, prgid: POINTER(Int32), prgbstr: POINTER(win32more.Windows.Win32.Foundation.BSTR), pcEventsFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Advise(self, pdisp: win32more.Windows.Win32.System.Com.IDispatch, pdwCookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Unadvise(self, dwCookie: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITridentEventSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1dc9ca50-06ef-11d2-8415-006008c3fbfc}')
    @commethod(3)
    def FireEvent(self, pstrEvent: win32more.Windows.Win32.Foundation.PWSTR, pdp: POINTER(win32more.Windows.Win32.System.Com.DISPPARAMS), pvarRes: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pei: POINTER(win32more.Windows.Win32.System.Com.EXCEPINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWebAppDiagnosticsObjectInitialization(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{16ff3a42-a5f5-432b-b625-8e8e16f57e15}')
    @commethod(3)
    def Initialize(self, hPassedHandle: win32more.Windows.Win32.Foundation.HANDLE_PTR, pDebugApplication: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWebAppDiagnosticsSetup(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{379bfbe1-c6c9-432a-93e1-6d17656c538c}')
    @commethod(3)
    def DiagnosticsSupported(self, pRetVal: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateObjectWithSiteAtWebApp(self, rclsid: POINTER(Guid), dwClsContext: UInt32, riid: POINTER(Guid), hPassToObject: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class JS_NATIVE_FRAME(Structure):
    InstructionOffset: UInt64
    ReturnOffset: UInt64
    FrameOffset: UInt64
    StackOffset: UInt64
JS_PROPERTY_ATTRIBUTES = Int32
JS_PROPERTY_ATTRIBUTE_NONE: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.JS_PROPERTY_ATTRIBUTES = 0
JS_PROPERTY_HAS_CHILDREN: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.JS_PROPERTY_ATTRIBUTES = 1
JS_PROPERTY_FAKE: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.JS_PROPERTY_ATTRIBUTES = 2
JS_PROPERTY_METHOD: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.JS_PROPERTY_ATTRIBUTES = 4
JS_PROPERTY_READONLY: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.JS_PROPERTY_ATTRIBUTES = 8
JS_PROPERTY_NATIVE_WINRT_POINTER: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.JS_PROPERTY_ATTRIBUTES = 16
JS_PROPERTY_FRAME_INTRYBLOCK: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.JS_PROPERTY_ATTRIBUTES = 32
JS_PROPERTY_FRAME_INCATCHBLOCK: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.JS_PROPERTY_ATTRIBUTES = 64
JS_PROPERTY_FRAME_INFINALLYBLOCK: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.JS_PROPERTY_ATTRIBUTES = 128
JS_PROPERTY_MEMBERS = Int32
JS_PROPERTY_MEMBERS_ALL: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.JS_PROPERTY_MEMBERS = 0
JS_PROPERTY_MEMBERS_ARGUMENTS: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.JS_PROPERTY_MEMBERS = 1
class JsDebugPropertyInfo(Structure):
    name: win32more.Windows.Win32.Foundation.BSTR
    type: win32more.Windows.Win32.Foundation.BSTR
    value: win32more.Windows.Win32.Foundation.BSTR
    fullName: win32more.Windows.Win32.Foundation.BSTR
    attr: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.JS_PROPERTY_ATTRIBUTES
class JsDebugReadMemoryFlags(Enum, Int32):
    None_ = 0
    JsDebugAllowPartialRead = 1
MachineDebugManager_DEBUG = Guid('{49769cec-3a55-4bb0-b697-88fede77e8ea}')
MachineDebugManager_RETAIL = Guid('{0c0a3666-30c9-11d0-8f20-00805f2cd064}')
PROFILER_EVENT_MASK = Int32
PROFILER_EVENT_MASK_TRACE_SCRIPT_FUNCTION_CALL: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_EVENT_MASK = 1
PROFILER_EVENT_MASK_TRACE_NATIVE_FUNCTION_CALL: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_EVENT_MASK = 2
PROFILER_EVENT_MASK_TRACE_DOM_FUNCTION_CALL: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_EVENT_MASK = 4
PROFILER_EVENT_MASK_TRACE_ALL: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_EVENT_MASK = 3
PROFILER_EVENT_MASK_TRACE_ALL_WITH_DOM: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_EVENT_MASK = 7
PROFILER_HEAP_ENUM_FLAGS = Int32
PROFILER_HEAP_ENUM_FLAGS_NONE: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_ENUM_FLAGS = 0
PROFILER_HEAP_ENUM_FLAGS_STORE_RELATIONSHIP_FLAGS: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_ENUM_FLAGS = 1
PROFILER_HEAP_ENUM_FLAGS_SUBSTRINGS: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_ENUM_FLAGS = 2
PROFILER_HEAP_ENUM_FLAGS_RELATIONSHIP_SUBSTRINGS: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_ENUM_FLAGS = 3
class PROFILER_HEAP_OBJECT(Structure):
    size: UInt32
    Anonymous: _Anonymous_e__Union
    typeNameId: UInt32
    flags: UInt32
    unused: UInt16
    optionalInfoCount: UInt16
    class _Anonymous_e__Union(Union):
        objectId: UIntPtr
        externalObjectAddress: VoidPtr
PROFILER_HEAP_OBJECT_FLAGS = Int32
PROFILER_HEAP_OBJECT_FLAGS_NEW_OBJECT: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_OBJECT_FLAGS = 1
PROFILER_HEAP_OBJECT_FLAGS_IS_ROOT: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_OBJECT_FLAGS = 2
PROFILER_HEAP_OBJECT_FLAGS_SITE_CLOSED: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_OBJECT_FLAGS = 4
PROFILER_HEAP_OBJECT_FLAGS_EXTERNAL: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_OBJECT_FLAGS = 8
PROFILER_HEAP_OBJECT_FLAGS_EXTERNAL_UNKNOWN: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_OBJECT_FLAGS = 16
PROFILER_HEAP_OBJECT_FLAGS_EXTERNAL_DISPATCH: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_OBJECT_FLAGS = 32
PROFILER_HEAP_OBJECT_FLAGS_SIZE_APPROXIMATE: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_OBJECT_FLAGS = 64
PROFILER_HEAP_OBJECT_FLAGS_SIZE_UNAVAILABLE: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_OBJECT_FLAGS = 128
PROFILER_HEAP_OBJECT_FLAGS_NEW_STATE_UNAVAILABLE: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_OBJECT_FLAGS = 256
PROFILER_HEAP_OBJECT_FLAGS_WINRT_INSTANCE: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_OBJECT_FLAGS = 512
PROFILER_HEAP_OBJECT_FLAGS_WINRT_RUNTIMECLASS: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_OBJECT_FLAGS = 1024
PROFILER_HEAP_OBJECT_FLAGS_WINRT_DELEGATE: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_OBJECT_FLAGS = 2048
PROFILER_HEAP_OBJECT_FLAGS_WINRT_NAMESPACE: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_OBJECT_FLAGS = 4096
class PROFILER_HEAP_OBJECT_OPTIONAL_INFO(Structure):
    infoType: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_OBJECT_OPTIONAL_INFO_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        prototype: UIntPtr
        functionName: win32more.Windows.Win32.Foundation.PWSTR
        elementAttributesSize: UInt32
        elementTextChildrenSize: UInt32
        scopeList: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_OBJECT_SCOPE_LIST)
        internalProperty: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_OBJECT_RELATIONSHIP)
        namePropertyList: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_OBJECT_RELATIONSHIP_LIST)
        indexPropertyList: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_OBJECT_RELATIONSHIP_LIST)
        relationshipList: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_OBJECT_RELATIONSHIP_LIST)
        eventList: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_OBJECT_RELATIONSHIP_LIST)
        weakMapCollectionList: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_OBJECT_RELATIONSHIP_LIST)
        mapCollectionList: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_OBJECT_RELATIONSHIP_LIST)
        setCollectionList: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_OBJECT_RELATIONSHIP_LIST)
PROFILER_HEAP_OBJECT_OPTIONAL_INFO_TYPE = Int32
PROFILER_HEAP_OBJECT_OPTIONAL_INFO_PROTOTYPE: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_OBJECT_OPTIONAL_INFO_TYPE = 1
PROFILER_HEAP_OBJECT_OPTIONAL_INFO_FUNCTION_NAME: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_OBJECT_OPTIONAL_INFO_TYPE = 2
PROFILER_HEAP_OBJECT_OPTIONAL_INFO_SCOPE_LIST: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_OBJECT_OPTIONAL_INFO_TYPE = 3
PROFILER_HEAP_OBJECT_OPTIONAL_INFO_INTERNAL_PROPERTY: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_OBJECT_OPTIONAL_INFO_TYPE = 4
PROFILER_HEAP_OBJECT_OPTIONAL_INFO_NAME_PROPERTIES: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_OBJECT_OPTIONAL_INFO_TYPE = 5
PROFILER_HEAP_OBJECT_OPTIONAL_INFO_INDEX_PROPERTIES: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_OBJECT_OPTIONAL_INFO_TYPE = 6
PROFILER_HEAP_OBJECT_OPTIONAL_INFO_ELEMENT_ATTRIBUTES_SIZE: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_OBJECT_OPTIONAL_INFO_TYPE = 7
PROFILER_HEAP_OBJECT_OPTIONAL_INFO_ELEMENT_TEXT_CHILDREN_SIZE: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_OBJECT_OPTIONAL_INFO_TYPE = 8
PROFILER_HEAP_OBJECT_OPTIONAL_INFO_RELATIONSHIPS: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_OBJECT_OPTIONAL_INFO_TYPE = 9
PROFILER_HEAP_OBJECT_OPTIONAL_INFO_WINRTEVENTS: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_OBJECT_OPTIONAL_INFO_TYPE = 10
PROFILER_HEAP_OBJECT_OPTIONAL_INFO_WEAKMAP_COLLECTION_LIST: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_OBJECT_OPTIONAL_INFO_TYPE = 11
PROFILER_HEAP_OBJECT_OPTIONAL_INFO_MAP_COLLECTION_LIST: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_OBJECT_OPTIONAL_INFO_TYPE = 12
PROFILER_HEAP_OBJECT_OPTIONAL_INFO_SET_COLLECTION_LIST: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_OBJECT_OPTIONAL_INFO_TYPE = 13
PROFILER_HEAP_OBJECT_OPTIONAL_INFO_MAX_VALUE: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_OBJECT_OPTIONAL_INFO_TYPE = 13
class PROFILER_HEAP_OBJECT_RELATIONSHIP(Structure):
    relationshipId: UInt32
    relationshipInfo: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_RELATIONSHIP_INFO
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        numberValue: Double
        stringValue: win32more.Windows.Win32.Foundation.PWSTR
        bstrValue: win32more.Windows.Win32.Foundation.BSTR
        objectId: UIntPtr
        externalObjectAddress: VoidPtr
        subString: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_PROPERTY_TYPE_SUBSTRING_INFO)
PROFILER_HEAP_OBJECT_RELATIONSHIP_FLAGS = Int32
PROFILER_HEAP_OBJECT_RELATIONSHIP_FLAGS_NONE: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_OBJECT_RELATIONSHIP_FLAGS = 0
PROFILER_HEAP_OBJECT_RELATIONSHIP_FLAGS_IS_GET_ACCESSOR: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_OBJECT_RELATIONSHIP_FLAGS = 65536
PROFILER_HEAP_OBJECT_RELATIONSHIP_FLAGS_IS_SET_ACCESSOR: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_OBJECT_RELATIONSHIP_FLAGS = 131072
PROFILER_HEAP_OBJECT_RELATIONSHIP_FLAGS_LET_VARIABLE: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_OBJECT_RELATIONSHIP_FLAGS = 262144
PROFILER_HEAP_OBJECT_RELATIONSHIP_FLAGS_CONST_VARIABLE: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_OBJECT_RELATIONSHIP_FLAGS = 524288
class PROFILER_HEAP_OBJECT_RELATIONSHIP_LIST(Structure):
    count: UInt32
    elements: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_OBJECT_RELATIONSHIP * 1
class PROFILER_HEAP_OBJECT_SCOPE_LIST(Structure):
    count: UInt32
    scopes: UIntPtr * 1
class PROFILER_HEAP_SUMMARY(Structure):
    version: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_SUMMARY_VERSION
    totalHeapSize: UInt32
PROFILER_HEAP_SUMMARY_VERSION = Int32
PROFILER_HEAP_SUMMARY_VERSION_1: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_HEAP_SUMMARY_VERSION = 1
class PROFILER_PROPERTY_TYPE_SUBSTRING_INFO(Structure):
    length: UInt32
    value: win32more.Windows.Win32.Foundation.PWSTR
PROFILER_RELATIONSHIP_INFO = Int32
PROFILER_PROPERTY_TYPE_NUMBER: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_RELATIONSHIP_INFO = 1
PROFILER_PROPERTY_TYPE_STRING: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_RELATIONSHIP_INFO = 2
PROFILER_PROPERTY_TYPE_HEAP_OBJECT: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_RELATIONSHIP_INFO = 3
PROFILER_PROPERTY_TYPE_EXTERNAL_OBJECT: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_RELATIONSHIP_INFO = 4
PROFILER_PROPERTY_TYPE_BSTR: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_RELATIONSHIP_INFO = 5
PROFILER_PROPERTY_TYPE_SUBSTRING: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_RELATIONSHIP_INFO = 6
PROFILER_SCRIPT_TYPE = Int32
PROFILER_SCRIPT_TYPE_USER: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_SCRIPT_TYPE = 0
PROFILER_SCRIPT_TYPE_DYNAMIC: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_SCRIPT_TYPE = 1
PROFILER_SCRIPT_TYPE_NATIVE: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_SCRIPT_TYPE = 2
PROFILER_SCRIPT_TYPE_DOM: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_SCRIPT_TYPE = 3
ProcessDebugManager = Guid('{78a51822-51f4-11d0-8f20-00805f2cd064}')
SCRIPTGCTYPE = Int32
SCRIPTGCTYPE_NORMAL: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPTGCTYPE = 0
SCRIPTGCTYPE_EXHAUSTIVE: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPTGCTYPE = 1
SCRIPTLANGUAGEVERSION = Int32
SCRIPTLANGUAGEVERSION_DEFAULT: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPTLANGUAGEVERSION = 0
SCRIPTLANGUAGEVERSION_5_7: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPTLANGUAGEVERSION = 1
SCRIPTLANGUAGEVERSION_5_8: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPTLANGUAGEVERSION = 2
SCRIPTLANGUAGEVERSION_MAX: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPTLANGUAGEVERSION = 255
SCRIPTSTATE = Int32
SCRIPTSTATE_UNINITIALIZED: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPTSTATE = 0
SCRIPTSTATE_INITIALIZED: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPTSTATE = 5
SCRIPTSTATE_STARTED: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPTSTATE = 1
SCRIPTSTATE_CONNECTED: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPTSTATE = 2
SCRIPTSTATE_DISCONNECTED: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPTSTATE = 3
SCRIPTSTATE_CLOSED: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPTSTATE = 4
SCRIPTTHREADSTATE = Int32
SCRIPTTHREADSTATE_NOTINSCRIPT: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPTTHREADSTATE = 0
SCRIPTTHREADSTATE_RUNNING: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPTTHREADSTATE = 1
SCRIPTTRACEINFO = Int32
SCRIPTTRACEINFO_SCRIPTSTART: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPTTRACEINFO = 0
SCRIPTTRACEINFO_SCRIPTEND: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPTTRACEINFO = 1
SCRIPTTRACEINFO_COMCALLSTART: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPTTRACEINFO = 2
SCRIPTTRACEINFO_COMCALLEND: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPTTRACEINFO = 3
SCRIPTTRACEINFO_CREATEOBJSTART: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPTTRACEINFO = 4
SCRIPTTRACEINFO_CREATEOBJEND: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPTTRACEINFO = 5
SCRIPTTRACEINFO_GETOBJSTART: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPTTRACEINFO = 6
SCRIPTTRACEINFO_GETOBJEND: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPTTRACEINFO = 7
SCRIPTUICHANDLING = Int32
SCRIPTUICHANDLING_ALLOW: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPTUICHANDLING = 0
SCRIPTUICHANDLING_NOUIERROR: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPTUICHANDLING = 1
SCRIPTUICHANDLING_NOUIDEFAULT: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPTUICHANDLING = 2
SCRIPTUICITEM = Int32
SCRIPTUICITEM_INPUTBOX: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPTUICITEM = 1
SCRIPTUICITEM_MSGBOX: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPTUICITEM = 2
SCRIPT_DEBUGGER_OPTIONS = Int32
SDO_NONE: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPT_DEBUGGER_OPTIONS = 0
SDO_ENABLE_FIRST_CHANCE_EXCEPTIONS: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPT_DEBUGGER_OPTIONS = 1
SDO_ENABLE_WEB_WORKER_SUPPORT: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPT_DEBUGGER_OPTIONS = 2
SDO_ENABLE_NONUSER_CODE_SUPPORT: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPT_DEBUGGER_OPTIONS = 4
SDO_ENABLE_LIBRARY_STACK_FRAME: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPT_DEBUGGER_OPTIONS = 8
SCRIPT_ERROR_DEBUG_EXCEPTION_THROWN_KIND = Int32
ETK_FIRST_CHANCE: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPT_ERROR_DEBUG_EXCEPTION_THROWN_KIND = 0
ETK_USER_UNHANDLED: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPT_ERROR_DEBUG_EXCEPTION_THROWN_KIND = 1
ETK_UNHANDLED: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPT_ERROR_DEBUG_EXCEPTION_THROWN_KIND = 2
SCRIPT_INVOCATION_CONTEXT_TYPE = Int32
SICT_Event: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPT_INVOCATION_CONTEXT_TYPE = 0
SICT_SetTimeout: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPT_INVOCATION_CONTEXT_TYPE = 1
SICT_SetInterval: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPT_INVOCATION_CONTEXT_TYPE = 2
SICT_SetImmediate: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPT_INVOCATION_CONTEXT_TYPE = 3
SICT_RequestAnimationFrame: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPT_INVOCATION_CONTEXT_TYPE = 4
SICT_ToString: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPT_INVOCATION_CONTEXT_TYPE = 5
SICT_MutationObserverCheckpoint: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPT_INVOCATION_CONTEXT_TYPE = 6
SICT_WWAExecUnsafeLocalFunction: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPT_INVOCATION_CONTEXT_TYPE = 7
SICT_WWAExecAtPriority: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.SCRIPT_INVOCATION_CONTEXT_TYPE = 8
class TEXT_DOCUMENT_ARRAY(Structure):
    dwCount: UInt32
    Members: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugDocumentText)


make_ready(__name__)
