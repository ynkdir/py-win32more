from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.System.Diagnostics.TraceLogging
WINEVENT_CHANNEL_CLASSIC_TRACE: Int32 = 0
WINEVENT_CHANNEL_GLOBAL_SYSTEM: Int32 = 8
WINEVENT_CHANNEL_GLOBAL_APPLICATION: Int32 = 9
WINEVENT_CHANNEL_GLOBAL_SECURITY: Int32 = 10
WINEVENT_CHANNEL_TRACELOGGING: Int32 = 11
WINEVENT_CHANNEL_PROVIDERMETADATA: Int32 = 12
WINEVENT_LEVEL_LOG_ALWAYS: Int32 = 0
WINEVENT_LEVEL_CRITICAL: Int32 = 1
WINEVENT_LEVEL_ERROR: Int32 = 2
WINEVENT_LEVEL_WARNING: Int32 = 3
WINEVENT_LEVEL_INFO: Int32 = 4
WINEVENT_LEVEL_VERBOSE: Int32 = 5
WINEVENT_LEVEL_RESERVED_6: Int32 = 6
WINEVENT_LEVEL_RESERVED_7: Int32 = 7
WINEVENT_LEVEL_RESERVED_8: Int32 = 8
WINEVENT_LEVEL_RESERVED_9: Int32 = 9
WINEVENT_LEVEL_RESERVED_10: Int32 = 10
WINEVENT_LEVEL_RESERVED_11: Int32 = 11
WINEVENT_LEVEL_RESERVED_12: Int32 = 12
WINEVENT_LEVEL_RESERVED_13: Int32 = 13
WINEVENT_LEVEL_RESERVED_14: Int32 = 14
WINEVENT_LEVEL_RESERVED_15: Int32 = 15
WINEVENT_OPCODE_INFO: Int32 = 0
WINEVENT_OPCODE_START: Int32 = 1
WINEVENT_OPCODE_STOP: Int32 = 2
WINEVENT_OPCODE_DC_START: Int32 = 3
WINEVENT_OPCODE_DC_STOP: Int32 = 4
WINEVENT_OPCODE_EXTENSION: Int32 = 5
WINEVENT_OPCODE_REPLY: Int32 = 6
WINEVENT_OPCODE_RESUME: Int32 = 7
WINEVENT_OPCODE_SUSPEND: Int32 = 8
WINEVENT_OPCODE_SEND: Int32 = 9
WINEVENT_OPCODE_RECEIVE: Int32 = 240
WINEVENT_OPCODE_RESERVED_241: Int32 = 241
WINEVENT_OPCODE_RESERVED_242: Int32 = 242
WINEVENT_OPCODE_RESERVED_243: Int32 = 243
WINEVENT_OPCODE_RESERVED_244: Int32 = 244
WINEVENT_OPCODE_RESERVED_245: Int32 = 245
WINEVENT_OPCODE_RESERVED_246: Int32 = 246
WINEVENT_OPCODE_RESERVED_247: Int32 = 247
WINEVENT_OPCODE_RESERVED_248: Int32 = 248
WINEVENT_OPCODE_RESERVED_249: Int32 = 249
WINEVENT_OPCODE_RESERVED_250: Int32 = 250
WINEVENT_OPCODE_RESERVED_251: Int32 = 251
WINEVENT_OPCODE_RESERVED_252: Int32 = 252
WINEVENT_OPCODE_RESERVED_253: Int32 = 253
WINEVENT_OPCODE_RESERVED_254: Int32 = 254
WINEVENT_OPCODE_RESERVED_255: Int32 = 255
WINEVENT_TASK_NONE: Int32 = 0
WINEVT_KEYWORD_ANY: Int32 = 0
WINEVENT_KEYWORD_RESPONSE_TIME: Int64 = 281474976710656
WINEVENT_KEYWORD_RESERVED_49: Int64 = 562949953421312
WINEVENT_KEYWORD_WDI_DIAG: Int64 = 1125899906842624
WINEVENT_KEYWORD_SQM: Int64 = 2251799813685248
WINEVENT_KEYWORD_AUDIT_FAILURE: Int64 = 4503599627370496
WINEVENT_KEYWORD_AUDIT_SUCCESS: Int64 = 9007199254740992
WINEVENT_KEYWORD_CORRELATION_HINT: Int64 = 18014398509481984
WINEVENT_KEYWORD_EVENTLOG_CLASSIC: Int64 = 36028797018963968
WINEVENT_KEYWORD_RESERVED_56: Int64 = 72057594037927936
WINEVENT_KEYWORD_RESERVED_57: Int64 = 144115188075855872
WINEVENT_KEYWORD_RESERVED_58: Int64 = 288230376151711744
WINEVENT_KEYWORD_RESERVED_59: Int64 = 576460752303423488
WINEVENT_KEYWORD_RESERVED_60: Int64 = 1152921504606846976
WINEVENT_KEYWORD_RESERVED_61: Int64 = 2305843009213693952
WINEVENT_KEYWORD_RESERVED_62: Int64 = 4611686018427387904
WINEVENT_KEYWORD_RESERVED_63: UInt64 = 9223372036854775808
MSG_category_Devices: Int32 = 1
MSG_category_Disk: Int32 = 2
MSG_category_Network: Int32 = 7
MSG_category_Printers: Int32 = 3
MSG_category_Services: Int32 = 4
MSG_category_Shell: Int32 = 5
MSG_category_SystemEvent: Int32 = 6
MSG_channel_Application: Int32 = 256
MSG_channel_ProviderMetadata: Int32 = -1879048189
MSG_channel_Security: Int32 = 257
MSG_channel_System: Int32 = 258
MSG_channel_TraceClassic: Int32 = -1879048191
MSG_channel_TraceLogging: Int32 = -1879048190
MSG_keyword_AnyKeyword: Int32 = 268435456
MSG_keyword_AuditFailure: Int32 = 268435509
MSG_keyword_AuditSuccess: Int32 = 268435510
MSG_keyword_Classic: Int32 = 268435512
MSG_keyword_CorrelationHint: Int32 = 268435511
MSG_keyword_ResponseTime: Int32 = 268435505
MSG_keyword_SQM: Int32 = 268435508
MSG_keyword_WDIDiag: Int32 = 268435507
MSG_level_Critical: Int32 = 1342177281
MSG_level_Error: Int32 = 1342177282
MSG_level_Informational: Int32 = 1342177284
MSG_level_LogAlways: Int32 = 1342177280
MSG_level_Verbose: Int32 = 1342177285
MSG_level_Warning: Int32 = 1342177283
MSG_opcode_DCStart: Int32 = 805502976
MSG_opcode_DCStop: Int32 = 805568512
MSG_opcode_Extension: Int32 = 805634048
MSG_opcode_Info: Int32 = 805306368
MSG_opcode_Receive: Int32 = 821035008
MSG_opcode_Reply: Int32 = 805699584
MSG_opcode_Resume: Int32 = 805765120
MSG_opcode_Send: Int32 = 805896192
MSG_opcode_Start: Int32 = 805371904
MSG_opcode_Stop: Int32 = 805437440
MSG_opcode_Suspend: Int32 = 805830656
MSG_task_None: Int32 = 1879048192


make_ready(__name__)
