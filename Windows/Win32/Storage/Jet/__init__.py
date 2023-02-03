from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.Storage.Jet
import Windows.Win32.Storage.StructuredStorage
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
JET_VERSION: UInt32 = 1280
JET_wszConfigStoreReadControl: String = 'CsReadControl'
JET_bitConfigStoreReadControlInhibitRead: UInt32 = 1
JET_bitConfigStoreReadControlDisableAll: UInt32 = 2
JET_bitConfigStoreReadControlDefault: UInt32 = 0
JET_wszConfigStoreRelPathSysParamDefault: String = 'SysParamDefault'
JET_wszConfigStoreRelPathSysParamOverride: String = 'SysParamOverride'
JET_bitDefragmentBatchStart: UInt32 = 1
JET_bitDefragmentBatchStop: UInt32 = 2
JET_bitDefragmentAvailSpaceTreesOnly: UInt32 = 64
JET_bitDefragmentNoPartialMerges: UInt32 = 128
JET_bitDefragmentBTree: UInt32 = 256
JET_cbtypNull: UInt32 = 0
JET_cbtypFinalize: UInt32 = 1
JET_cbtypBeforeInsert: UInt32 = 2
JET_cbtypAfterInsert: UInt32 = 4
JET_cbtypBeforeReplace: UInt32 = 8
JET_cbtypAfterReplace: UInt32 = 16
JET_cbtypBeforeDelete: UInt32 = 32
JET_cbtypAfterDelete: UInt32 = 64
JET_cbtypUserDefinedDefaultValue: UInt32 = 128
JET_cbtypOnlineDefragCompleted: UInt32 = 256
JET_cbtypFreeCursorLS: UInt32 = 512
JET_cbtypFreeTableLS: UInt32 = 1024
JET_bitTableInfoUpdatable: UInt32 = 1
JET_bitTableInfoBookmark: UInt32 = 2
JET_bitTableInfoRollback: UInt32 = 4
JET_bitObjectSystem: UInt32 = 2147483648
JET_bitObjectTableFixedDDL: UInt32 = 1073741824
JET_bitObjectTableTemplate: UInt32 = 536870912
JET_bitObjectTableDerived: UInt32 = 268435456
JET_bitObjectTableNoFixedVarColumnsInDerivedTables: UInt32 = 67108864
cObjectInfoCols: UInt32 = 9
cColumnInfoCols: UInt32 = 14
cIndexInfoCols: UInt32 = 15
JET_MAX_COMPUTERNAME_LENGTH: UInt32 = 15
JET_bitDurableCommitCallbackLogUnavailable: UInt32 = 1
JET_cbBookmarkMost: UInt32 = 256
JET_cbNameMost: UInt32 = 64
JET_cbFullNameMost: UInt32 = 255
JET_cbColumnLVPageOverhead: UInt32 = 82
JET_cbLVDefaultValueMost: UInt32 = 255
JET_cbColumnMost: UInt32 = 255
JET_cbLVColumnMost: UInt32 = 2147483647
JET_cbKeyMost8KBytePage: UInt32 = 2000
JET_cbKeyMost4KBytePage: UInt32 = 1000
JET_cbKeyMost2KBytePage: UInt32 = 500
JET_cbKeyMostMin: UInt32 = 255
JET_cbKeyMost: UInt32 = 255
JET_cbLimitKeyMost: UInt32 = 256
JET_cbPrimaryKeyMost: UInt32 = 255
JET_cbSecondaryKeyMost: UInt32 = 255
JET_ccolKeyMost: UInt32 = 16
JET_ccolMost: UInt32 = 65248
JET_ccolFixedMost: UInt32 = 127
JET_ccolVarMost: UInt32 = 128
JET_EventLoggingDisable: UInt32 = 0
JET_EventLoggingLevelMin: UInt32 = 1
JET_EventLoggingLevelLow: UInt32 = 25
JET_EventLoggingLevelMedium: UInt32 = 50
JET_EventLoggingLevelHigh: UInt32 = 75
JET_EventLoggingLevelMax: UInt32 = 100
JET_IOPriorityNormal: UInt32 = 0
JET_IOPriorityLow: UInt32 = 1
JET_configDefault: UInt32 = 1
JET_configRemoveQuotas: UInt32 = 2
JET_configLowDiskFootprint: UInt32 = 4
JET_configMediumDiskFootprint: UInt32 = 8
JET_configLowMemory: UInt32 = 16
JET_configDynamicMediumMemory: UInt32 = 32
JET_configLowPower: UInt32 = 64
JET_configSSDProfileIO: UInt32 = 128
JET_configRunSilent: UInt32 = 256
JET_configUnthrottledMemory: UInt32 = 512
JET_configHighConcurrencyScaling: UInt32 = 1024
JET_paramSystemPath: UInt32 = 0
JET_paramTempPath: UInt32 = 1
JET_paramLogFilePath: UInt32 = 2
JET_paramBaseName: UInt32 = 3
JET_paramEventSource: UInt32 = 4
JET_paramMaxSessions: UInt32 = 5
JET_paramMaxOpenTables: UInt32 = 6
JET_paramPreferredMaxOpenTables: UInt32 = 7
JET_paramCachedClosedTables: UInt32 = 125
JET_paramMaxCursors: UInt32 = 8
JET_paramMaxVerPages: UInt32 = 9
JET_paramPreferredVerPages: UInt32 = 63
JET_paramGlobalMinVerPages: UInt32 = 81
JET_paramVersionStoreTaskQueueMax: UInt32 = 105
JET_paramMaxTemporaryTables: UInt32 = 10
JET_paramLogFileSize: UInt32 = 11
JET_paramLogBuffers: UInt32 = 12
JET_paramWaitLogFlush: UInt32 = 13
JET_paramLogCheckpointPeriod: UInt32 = 14
JET_paramLogWaitingUserMax: UInt32 = 15
JET_paramCommitDefault: UInt32 = 16
JET_paramCircularLog: UInt32 = 17
JET_paramDbExtensionSize: UInt32 = 18
JET_paramPageTempDBMin: UInt32 = 19
JET_paramPageFragment: UInt32 = 20
JET_paramEnableFileCache: UInt32 = 126
JET_paramVerPageSize: UInt32 = 128
JET_paramConfiguration: UInt32 = 129
JET_paramEnableAdvanced: UInt32 = 130
JET_paramMaxColtyp: UInt32 = 131
JET_paramBatchIOBufferMax: UInt32 = 22
JET_paramCacheSize: UInt32 = 41
JET_paramCacheSizeMin: UInt32 = 60
JET_paramCacheSizeMax: UInt32 = 23
JET_paramCheckpointDepthMax: UInt32 = 24
JET_paramLRUKCorrInterval: UInt32 = 25
JET_paramLRUKHistoryMax: UInt32 = 26
JET_paramLRUKPolicy: UInt32 = 27
JET_paramLRUKTimeout: UInt32 = 28
JET_paramLRUKTrxCorrInterval: UInt32 = 29
JET_paramOutstandingIOMax: UInt32 = 30
JET_paramStartFlushThreshold: UInt32 = 31
JET_paramStopFlushThreshold: UInt32 = 32
JET_paramEnableViewCache: UInt32 = 127
JET_paramCheckpointIOMax: UInt32 = 135
JET_paramTableClass1Name: UInt32 = 137
JET_paramTableClass2Name: UInt32 = 138
JET_paramTableClass3Name: UInt32 = 139
JET_paramTableClass4Name: UInt32 = 140
JET_paramTableClass5Name: UInt32 = 141
JET_paramTableClass6Name: UInt32 = 142
JET_paramTableClass7Name: UInt32 = 143
JET_paramTableClass8Name: UInt32 = 144
JET_paramTableClass9Name: UInt32 = 145
JET_paramTableClass10Name: UInt32 = 146
JET_paramTableClass11Name: UInt32 = 147
JET_paramTableClass12Name: UInt32 = 148
JET_paramTableClass13Name: UInt32 = 149
JET_paramTableClass14Name: UInt32 = 150
JET_paramTableClass15Name: UInt32 = 151
JET_paramIOPriority: UInt32 = 152
JET_paramRecovery: UInt32 = 34
JET_paramEnableOnlineDefrag: UInt32 = 35
JET_paramCheckFormatWhenOpenFail: UInt32 = 44
JET_paramEnableTempTableVersioning: UInt32 = 46
JET_paramIgnoreLogVersion: UInt32 = 47
JET_paramDeleteOldLogs: UInt32 = 48
JET_paramEventSourceKey: UInt32 = 49
JET_paramNoInformationEvent: UInt32 = 50
JET_paramEventLoggingLevel: UInt32 = 51
JET_paramDeleteOutOfRangeLogs: UInt32 = 52
JET_paramAccessDeniedRetryPeriod: UInt32 = 53
JET_paramEnableIndexChecking: UInt32 = 45
JET_paramEnableIndexCleanup: UInt32 = 54
JET_paramDatabasePageSize: UInt32 = 64
JET_paramDisableCallbacks: UInt32 = 65
JET_paramLogFileCreateAsynch: UInt32 = 69
JET_paramErrorToString: UInt32 = 70
JET_paramZeroDatabaseDuringBackup: UInt32 = 71
JET_paramUnicodeIndexDefault: UInt32 = 72
JET_paramRuntimeCallback: UInt32 = 73
JET_paramCleanupMismatchedLogFiles: UInt32 = 77
JET_paramRecordUpgradeDirtyLevel: UInt32 = 78
JET_paramOSSnapshotTimeout: UInt32 = 82
JET_paramExceptionAction: UInt32 = 98
JET_paramEventLogCache: UInt32 = 99
JET_paramCreatePathIfNotExist: UInt32 = 100
JET_paramPageHintCacheSize: UInt32 = 101
JET_paramOneDatabasePerSession: UInt32 = 102
JET_paramMaxInstances: UInt32 = 104
JET_paramDisablePerfmon: UInt32 = 107
JET_paramIndexTuplesLengthMin: UInt32 = 110
JET_paramIndexTuplesLengthMax: UInt32 = 111
JET_paramIndexTuplesToIndexMax: UInt32 = 112
JET_paramAlternateDatabaseRecoveryPath: UInt32 = 113
JET_paramIndexTupleIncrement: UInt32 = 132
JET_paramIndexTupleStart: UInt32 = 133
JET_paramKeyMost: UInt32 = 134
JET_paramLegacyFileNames: UInt32 = 136
JET_paramEnablePersistedCallbacks: UInt32 = 156
JET_paramWaypointLatency: UInt32 = 153
JET_paramDefragmentSequentialBTrees: UInt32 = 160
JET_paramDefragmentSequentialBTreesDensityCheckFrequency: UInt32 = 161
JET_paramIOThrottlingTimeQuanta: UInt32 = 162
JET_paramLVChunkSizeMost: UInt32 = 163
JET_paramMaxCoalesceReadSize: UInt32 = 164
JET_paramMaxCoalesceWriteSize: UInt32 = 165
JET_paramMaxCoalesceReadGapSize: UInt32 = 166
JET_paramMaxCoalesceWriteGapSize: UInt32 = 167
JET_paramEnableDBScanInRecovery: UInt32 = 169
JET_paramDbScanThrottle: UInt32 = 170
JET_paramDbScanIntervalMinSec: UInt32 = 171
JET_paramDbScanIntervalMaxSec: UInt32 = 172
JET_paramCachePriority: UInt32 = 177
JET_paramMaxTransactionSize: UInt32 = 178
JET_paramPrereadIOMax: UInt32 = 179
JET_paramEnableDBScanSerialization: UInt32 = 180
JET_paramHungIOThreshold: UInt32 = 181
JET_paramHungIOActions: UInt32 = 182
JET_paramMinDataForXpress: UInt32 = 183
JET_paramEnableShrinkDatabase: UInt32 = 184
JET_paramProcessFriendlyName: UInt32 = 186
JET_paramDurableCommitCallback: UInt32 = 187
JET_paramEnableSqm: UInt32 = 188
JET_paramConfigStoreSpec: UInt32 = 189
JET_paramUseFlushForWriteDurability: UInt32 = 214
JET_paramEnableRBS: UInt32 = 215
JET_paramRBSFilePath: UInt32 = 216
JET_paramMaxValueInvalid: UInt32 = 217
JET_sesparamCommitDefault: UInt32 = 4097
JET_sesparamTransactionLevel: UInt32 = 4099
JET_sesparamOperationContext: UInt32 = 4100
JET_sesparamCorrelationID: UInt32 = 4101
JET_sesparamMaxValueInvalid: UInt32 = 4110
JET_bitESE98FileNames: UInt32 = 1
JET_bitEightDotThreeSoftCompat: UInt32 = 2
JET_bitHungIOEvent: UInt32 = 1
JET_bitShrinkDatabaseOff: UInt32 = 0
JET_bitShrinkDatabaseOn: UInt32 = 1
JET_bitShrinkDatabaseRealtime: UInt32 = 2
JET_bitShrinkDatabaseTrim: UInt32 = 1
JET_bitReplayIgnoreMissingDB: UInt32 = 4
JET_bitRecoveryWithoutUndo: UInt32 = 8
JET_bitTruncateLogsAfterRecovery: UInt32 = 16
JET_bitReplayMissingMapEntryDB: UInt32 = 32
JET_bitLogStreamMustExist: UInt32 = 64
JET_bitReplayIgnoreLostLogs: UInt32 = 128
JET_bitKeepDbAttachedAtEndOfRecovery: UInt32 = 4096
JET_bitTermComplete: UInt32 = 1
JET_bitTermAbrupt: UInt32 = 2
JET_bitTermStopBackup: UInt32 = 4
JET_bitTermDirty: UInt32 = 8
JET_bitIdleFlushBuffers: UInt32 = 1
JET_bitIdleCompact: UInt32 = 2
JET_bitIdleStatus: UInt32 = 4
JET_bitDbReadOnly: UInt32 = 1
JET_bitDbExclusive: UInt32 = 2
JET_bitDbDeleteCorruptIndexes: UInt32 = 16
JET_bitDbDeleteUnicodeIndexes: UInt32 = 1024
JET_bitDbUpgrade: UInt32 = 512
JET_bitDbEnableBackgroundMaintenance: UInt32 = 2048
JET_bitDbPurgeCacheOnAttach: UInt32 = 4096
JET_bitForceDetach: UInt32 = 1
JET_bitDbRecoveryOff: UInt32 = 8
JET_bitDbShadowingOff: UInt32 = 128
JET_bitDbOverwriteExisting: UInt32 = 512
JET_bitBackupIncremental: UInt32 = 1
JET_bitBackupAtomic: UInt32 = 4
JET_bitBackupSnapshot: UInt32 = 16
JET_bitBackupEndNormal: UInt32 = 1
JET_bitBackupEndAbort: UInt32 = 2
JET_bitBackupTruncateDone: UInt32 = 256
JET_bitTableCreateFixedDDL: UInt32 = 1
JET_bitTableCreateTemplateTable: UInt32 = 2
JET_bitTableCreateNoFixedVarColumnsInDerivedTables: UInt32 = 4
JET_bitTableCreateImmutableStructure: UInt32 = 8
JET_bitColumnFixed: UInt32 = 1
JET_bitColumnTagged: UInt32 = 2
JET_bitColumnNotNULL: UInt32 = 4
JET_bitColumnVersion: UInt32 = 8
JET_bitColumnAutoincrement: UInt32 = 16
JET_bitColumnUpdatable: UInt32 = 32
JET_bitColumnTTKey: UInt32 = 64
JET_bitColumnTTDescending: UInt32 = 128
JET_bitColumnMultiValued: UInt32 = 1024
JET_bitColumnEscrowUpdate: UInt32 = 2048
JET_bitColumnUnversioned: UInt32 = 4096
JET_bitColumnMaybeNull: UInt32 = 8192
JET_bitColumnFinalize: UInt32 = 16384
JET_bitColumnUserDefinedDefault: UInt32 = 32768
JET_bitColumnDeleteOnZero: UInt32 = 131072
JET_bitColumnCompressed: UInt32 = 524288
JET_bitDeleteColumnIgnoreTemplateColumns: UInt32 = 1
JET_bitMoveFirst: UInt32 = 0
JET_bitNoMove: UInt32 = 2
JET_bitNewKey: UInt32 = 1
JET_bitStrLimit: UInt32 = 2
JET_bitSubStrLimit: UInt32 = 4
JET_bitNormalizedKey: UInt32 = 8
JET_bitKeyDataZeroLength: UInt32 = 16
JET_bitFullColumnStartLimit: UInt32 = 256
JET_bitFullColumnEndLimit: UInt32 = 512
JET_bitPartialColumnStartLimit: UInt32 = 1024
JET_bitPartialColumnEndLimit: UInt32 = 2048
JET_bitRangeInclusive: UInt32 = 1
JET_bitRangeUpperLimit: UInt32 = 2
JET_bitRangeInstantDuration: UInt32 = 4
JET_bitRangeRemove: UInt32 = 8
JET_bitReadLock: UInt32 = 1
JET_bitWriteLock: UInt32 = 2
JET_MoveFirst: UInt32 = 2147483648
JET_MovePrevious: Int32 = -1
JET_MoveLast: UInt32 = 2147483647
JET_bitMoveKeyNE: UInt32 = 1
JET_bitSeekEQ: UInt32 = 1
JET_bitSeekLT: UInt32 = 2
JET_bitSeekLE: UInt32 = 4
JET_bitSeekGE: UInt32 = 8
JET_bitSeekGT: UInt32 = 16
JET_bitSetIndexRange: UInt32 = 32
JET_bitCheckUniqueness: UInt32 = 64
JET_bitBookmarkPermitVirtualCurrency: UInt32 = 1
JET_bitIndexColumnMustBeNull: UInt32 = 1
JET_bitIndexColumnMustBeNonNull: UInt32 = 2
JET_bitRecordInIndex: UInt32 = 1
JET_bitRecordNotInIndex: UInt32 = 2
JET_bitIndexUnique: UInt32 = 1
JET_bitIndexPrimary: UInt32 = 2
JET_bitIndexDisallowNull: UInt32 = 4
JET_bitIndexIgnoreNull: UInt32 = 8
JET_bitIndexIgnoreAnyNull: UInt32 = 32
JET_bitIndexIgnoreFirstNull: UInt32 = 64
JET_bitIndexLazyFlush: UInt32 = 128
JET_bitIndexEmpty: UInt32 = 256
JET_bitIndexUnversioned: UInt32 = 512
JET_bitIndexSortNullsHigh: UInt32 = 1024
JET_bitIndexUnicode: UInt32 = 2048
JET_bitIndexTuples: UInt32 = 4096
JET_bitIndexTupleLimits: UInt32 = 8192
JET_bitIndexCrossProduct: UInt32 = 16384
JET_bitIndexKeyMost: UInt32 = 32768
JET_bitIndexDisallowTruncation: UInt32 = 65536
JET_bitIndexNestedTable: UInt32 = 131072
JET_bitIndexDotNetGuid: UInt32 = 262144
JET_bitIndexImmutableStructure: UInt32 = 524288
JET_bitKeyAscending: UInt32 = 0
JET_bitKeyDescending: UInt32 = 1
JET_bitTableDenyWrite: UInt32 = 1
JET_bitTableDenyRead: UInt32 = 2
JET_bitTableReadOnly: UInt32 = 4
JET_bitTableUpdatable: UInt32 = 8
JET_bitTablePermitDDL: UInt32 = 16
JET_bitTableNoCache: UInt32 = 32
JET_bitTablePreread: UInt32 = 64
JET_bitTableOpportuneRead: UInt32 = 128
JET_bitTableSequential: UInt32 = 32768
JET_bitTableClassMask: UInt32 = 2031616
JET_bitTableClassNone: UInt32 = 0
JET_bitTableClass1: UInt32 = 65536
JET_bitTableClass2: UInt32 = 131072
JET_bitTableClass3: UInt32 = 196608
JET_bitTableClass4: UInt32 = 262144
JET_bitTableClass5: UInt32 = 327680
JET_bitTableClass6: UInt32 = 393216
JET_bitTableClass7: UInt32 = 458752
JET_bitTableClass8: UInt32 = 524288
JET_bitTableClass9: UInt32 = 589824
JET_bitTableClass10: UInt32 = 655360
JET_bitTableClass11: UInt32 = 720896
JET_bitTableClass12: UInt32 = 786432
JET_bitTableClass13: UInt32 = 851968
JET_bitTableClass14: UInt32 = 917504
JET_bitTableClass15: UInt32 = 983040
JET_bitLSReset: UInt32 = 1
JET_bitLSCursor: UInt32 = 2
JET_bitLSTable: UInt32 = 4
JET_bitPrereadForward: UInt32 = 1
JET_bitPrereadBackward: UInt32 = 2
JET_bitPrereadFirstPage: UInt32 = 4
JET_bitPrereadNormalizedKey: UInt32 = 8
JET_bitTTIndexed: UInt32 = 1
JET_bitTTUnique: UInt32 = 2
JET_bitTTUpdatable: UInt32 = 4
JET_bitTTScrollable: UInt32 = 8
JET_bitTTSortNullsHigh: UInt32 = 16
JET_bitTTForceMaterialization: UInt32 = 32
JET_bitTTErrorOnDuplicateInsertion: UInt32 = 32
JET_bitTTForwardOnly: UInt32 = 64
JET_bitTTIntrinsicLVsOnly: UInt32 = 128
JET_bitTTDotNetGuid: UInt32 = 256
JET_bitSetAppendLV: UInt32 = 1
JET_bitSetOverwriteLV: UInt32 = 4
JET_bitSetSizeLV: UInt32 = 8
JET_bitSetZeroLength: UInt32 = 32
JET_bitSetSeparateLV: UInt32 = 64
JET_bitSetUniqueMultiValues: UInt32 = 128
JET_bitSetUniqueNormalizedMultiValues: UInt32 = 256
JET_bitSetRevertToDefaultValue: UInt32 = 512
JET_bitSetIntrinsicLV: UInt32 = 1024
JET_bitSetUncompressed: UInt32 = 65536
JET_bitSetCompressed: UInt32 = 131072
JET_bitSetContiguousLV: UInt32 = 262144
JET_bitSpaceHintsUtilizeParentSpace: UInt32 = 1
JET_bitCreateHintAppendSequential: UInt32 = 2
JET_bitCreateHintHotpointSequential: UInt32 = 4
JET_bitRetrieveHintReserve1: UInt32 = 8
JET_bitRetrieveHintTableScanForward: UInt32 = 16
JET_bitRetrieveHintTableScanBackward: UInt32 = 32
JET_bitRetrieveHintReserve2: UInt32 = 64
JET_bitRetrieveHintReserve3: UInt32 = 128
JET_bitDeleteHintTableSequential: UInt32 = 256
JET_prepInsert: UInt32 = 0
JET_prepReplace: UInt32 = 2
JET_prepCancel: UInt32 = 3
JET_prepReplaceNoLock: UInt32 = 4
JET_prepInsertCopy: UInt32 = 5
JET_prepInsertCopyDeleteOriginal: UInt32 = 7
JET_prepInsertCopyReplaceOriginal: UInt32 = 9
JET_sqmDisable: UInt32 = 0
JET_sqmEnable: UInt32 = 1
JET_sqmFromCEIP: UInt32 = 2
JET_bitUpdateCheckESE97Compatibility: UInt32 = 1
JET_bitEscrowNoRollback: UInt32 = 1
JET_bitRetrieveCopy: UInt32 = 1
JET_bitRetrieveFromIndex: UInt32 = 2
JET_bitRetrieveFromPrimaryBookmark: UInt32 = 4
JET_bitRetrieveTag: UInt32 = 8
JET_bitRetrieveNull: UInt32 = 16
JET_bitRetrieveIgnoreDefault: UInt32 = 32
JET_bitRetrieveTuple: UInt32 = 2048
JET_bitZeroLength: UInt32 = 1
JET_bitEnumerateCopy: UInt32 = 1
JET_bitEnumerateIgnoreDefault: UInt32 = 32
JET_bitEnumeratePresenceOnly: UInt32 = 131072
JET_bitEnumerateTaggedOnly: UInt32 = 262144
JET_bitEnumerateCompressOutput: UInt32 = 524288
JET_bitEnumerateIgnoreUserDefinedDefault: UInt32 = 1048576
JET_bitEnumerateInRecordOnly: UInt32 = 2097152
JET_bitRecordSizeInCopyBuffer: UInt32 = 1
JET_bitRecordSizeRunningTotal: UInt32 = 2
JET_bitRecordSizeLocal: UInt32 = 4
JET_bitTransactionReadOnly: UInt32 = 1
JET_bitCommitLazyFlush: UInt32 = 1
JET_bitWaitLastLevel0Commit: UInt32 = 2
JET_bitWaitAllLevel0Commit: UInt32 = 8
JET_bitForceNewLog: UInt32 = 16
JET_bitRollbackAll: UInt32 = 1
JET_bitIncrementalSnapshot: UInt32 = 1
JET_bitCopySnapshot: UInt32 = 2
JET_bitContinueAfterThaw: UInt32 = 4
JET_bitExplicitPrepare: UInt32 = 8
JET_bitAllDatabasesSnapshot: UInt32 = 1
JET_bitAbortSnapshot: UInt32 = 1
JET_DbInfoFilename: UInt32 = 0
JET_DbInfoConnect: UInt32 = 1
JET_DbInfoCountry: UInt32 = 2
JET_DbInfoLCID: UInt32 = 3
JET_DbInfoLangid: UInt32 = 3
JET_DbInfoCp: UInt32 = 4
JET_DbInfoCollate: UInt32 = 5
JET_DbInfoOptions: UInt32 = 6
JET_DbInfoTransactions: UInt32 = 7
JET_DbInfoVersion: UInt32 = 8
JET_DbInfoIsam: UInt32 = 9
JET_DbInfoFilesize: UInt32 = 10
JET_DbInfoSpaceOwned: UInt32 = 11
JET_DbInfoSpaceAvailable: UInt32 = 12
JET_DbInfoUpgrade: UInt32 = 13
JET_DbInfoMisc: UInt32 = 14
JET_DbInfoDBInUse: UInt32 = 15
JET_DbInfoPageSize: UInt32 = 17
JET_DbInfoFileType: UInt32 = 19
JET_DbInfoFilesizeOnDisk: UInt32 = 21
JET_dbstateJustCreated: UInt32 = 1
JET_dbstateDirtyShutdown: UInt32 = 2
JET_dbstateCleanShutdown: UInt32 = 3
JET_dbstateBeingConverted: UInt32 = 4
JET_dbstateForceDetach: UInt32 = 5
JET_filetypeUnknown: UInt32 = 0
JET_filetypeDatabase: UInt32 = 1
JET_filetypeLog: UInt32 = 3
JET_filetypeCheckpoint: UInt32 = 4
JET_filetypeTempDatabase: UInt32 = 5
JET_filetypeFlushMap: UInt32 = 7
JET_revertstateNone: UInt32 = 0
JET_revertstateInProgress: UInt32 = 1
JET_revertstateCopingLogs: UInt32 = 2
JET_revertstateCompleted: UInt32 = 3
JET_bitDeleteAllExistingLogs: UInt32 = 1
JET_coltypNil: UInt32 = 0
JET_coltypBit: UInt32 = 1
JET_coltypUnsignedByte: UInt32 = 2
JET_coltypShort: UInt32 = 3
JET_coltypLong: UInt32 = 4
JET_coltypCurrency: UInt32 = 5
JET_coltypIEEESingle: UInt32 = 6
JET_coltypIEEEDouble: UInt32 = 7
JET_coltypDateTime: UInt32 = 8
JET_coltypBinary: UInt32 = 9
JET_coltypText: UInt32 = 10
JET_coltypLongBinary: UInt32 = 11
JET_coltypLongText: UInt32 = 12
JET_coltypMax: UInt32 = 13
JET_coltypSLV: UInt32 = 13
JET_coltypUnsignedLong: UInt32 = 14
JET_coltypLongLong: UInt32 = 15
JET_coltypGUID: UInt32 = 16
JET_coltypUnsignedShort: UInt32 = 17
JET_coltypUnsignedLongLong: UInt32 = 18
JET_ColInfoGrbitNonDerivedColumnsOnly: UInt32 = 2147483648
JET_ColInfoGrbitMinimalInfo: UInt32 = 1073741824
JET_ColInfoGrbitSortByColumnid: UInt32 = 536870912
JET_objtypNil: UInt32 = 0
JET_objtypTable: UInt32 = 1
JET_bitCompactStats: UInt32 = 32
JET_bitCompactRepair: UInt32 = 64
JET_snpRepair: UInt32 = 2
JET_snpCompact: UInt32 = 4
JET_snpRestore: UInt32 = 8
JET_snpBackup: UInt32 = 9
JET_snpUpgrade: UInt32 = 10
JET_snpScrub: UInt32 = 11
JET_snpUpgradeRecordFormat: UInt32 = 12
JET_sntBegin: UInt32 = 5
JET_sntRequirements: UInt32 = 7
JET_sntProgress: UInt32 = 0
JET_sntComplete: UInt32 = 6
JET_sntFail: UInt32 = 3
JET_ExceptionMsgBox: UInt32 = 1
JET_ExceptionNone: UInt32 = 2
JET_ExceptionFailFast: UInt32 = 4
JET_OnlineDefragDisable: UInt32 = 0
JET_OnlineDefragAllOBSOLETE: UInt32 = 1
JET_OnlineDefragDatabases: UInt32 = 2
JET_OnlineDefragSpaceTrees: UInt32 = 4
JET_OnlineDefragAll: UInt32 = 65535
JET_bitResizeDatabaseOnlyGrow: UInt32 = 1
JET_bitResizeDatabaseOnlyShrink: UInt32 = 2
JET_bitStopServiceAll: UInt32 = 0
JET_bitStopServiceBackgroundUserTasks: UInt32 = 2
JET_bitStopServiceQuiesceCaches: UInt32 = 4
JET_bitStopServiceResume: UInt32 = 2147483648
JET_errSuccess: UInt32 = 0
JET_wrnNyi: Int32 = -1
JET_errRfsFailure: Int32 = -100
JET_errRfsNotArmed: Int32 = -101
JET_errFileClose: Int32 = -102
JET_errOutOfThreads: Int32 = -103
JET_errTooManyIO: Int32 = -105
JET_errTaskDropped: Int32 = -106
JET_errInternalError: Int32 = -107
JET_errDisabledFunctionality: Int32 = -112
JET_errUnloadableOSFunctionality: Int32 = -113
JET_errDatabaseBufferDependenciesCorrupted: Int32 = -255
JET_wrnRemainingVersions: UInt32 = 321
JET_errPreviousVersion: Int32 = -322
JET_errPageBoundary: Int32 = -323
JET_errKeyBoundary: Int32 = -324
JET_errBadPageLink: Int32 = -327
JET_errBadBookmark: Int32 = -328
JET_errNTSystemCallFailed: Int32 = -334
JET_errBadParentPageLink: Int32 = -338
JET_errSPAvailExtCacheOutOfSync: Int32 = -340
JET_errSPAvailExtCorrupted: Int32 = -341
JET_errSPAvailExtCacheOutOfMemory: Int32 = -342
JET_errSPOwnExtCorrupted: Int32 = -343
JET_errDbTimeCorrupted: Int32 = -344
JET_wrnUniqueKey: UInt32 = 345
JET_errKeyTruncated: Int32 = -346
JET_errDatabaseLeakInSpace: Int32 = -348
JET_errBadEmptyPage: Int32 = -351
wrnBTNotVisibleRejected: UInt32 = 352
wrnBTNotVisibleAccumulated: UInt32 = 353
JET_errBadLineCount: Int32 = -354
JET_errPageTagCorrupted: Int32 = -357
JET_errNodeCorrupted: Int32 = -358
JET_wrnSeparateLongValue: UInt32 = 406
JET_errKeyTooBig: Int32 = -408
JET_errCannotSeparateIntrinsicLV: Int32 = -416
JET_errSeparatedLongValue: Int32 = -421
JET_errMustBeSeparateLongValue: Int32 = -423
JET_errInvalidPreread: Int32 = -424
JET_errInvalidLoggedOperation: Int32 = -500
JET_errLogFileCorrupt: Int32 = -501
JET_errNoBackupDirectory: Int32 = -503
JET_errBackupDirectoryNotEmpty: Int32 = -504
JET_errBackupInProgress: Int32 = -505
JET_errRestoreInProgress: Int32 = -506
JET_errMissingPreviousLogFile: Int32 = -509
JET_errLogWriteFail: Int32 = -510
JET_errLogDisabledDueToRecoveryFailure: Int32 = -511
JET_errCannotLogDuringRecoveryRedo: Int32 = -512
JET_errLogGenerationMismatch: Int32 = -513
JET_errBadLogVersion: Int32 = -514
JET_errInvalidLogSequence: Int32 = -515
JET_errLoggingDisabled: Int32 = -516
JET_errLogBufferTooSmall: Int32 = -517
JET_errLogSequenceEnd: Int32 = -519
JET_errNoBackup: Int32 = -520
JET_errInvalidBackupSequence: Int32 = -521
JET_errBackupNotAllowedYet: Int32 = -523
JET_errDeleteBackupFileFail: Int32 = -524
JET_errMakeBackupDirectoryFail: Int32 = -525
JET_errInvalidBackup: Int32 = -526
JET_errRecoveredWithErrors: Int32 = -527
JET_errMissingLogFile: Int32 = -528
JET_errLogDiskFull: Int32 = -529
JET_errBadLogSignature: Int32 = -530
JET_errBadDbSignature: Int32 = -531
JET_errBadCheckpointSignature: Int32 = -532
JET_errCheckpointCorrupt: Int32 = -533
JET_errMissingPatchPage: Int32 = -534
JET_errBadPatchPage: Int32 = -535
JET_errRedoAbruptEnded: Int32 = -536
JET_errPatchFileMissing: Int32 = -538
JET_errDatabaseLogSetMismatch: Int32 = -539
JET_errDatabaseStreamingFileMismatch: Int32 = -540
JET_errLogFileSizeMismatch: Int32 = -541
JET_errCheckpointFileNotFound: Int32 = -542
JET_errRequiredLogFilesMissing: Int32 = -543
JET_errSoftRecoveryOnBackupDatabase: Int32 = -544
JET_errLogFileSizeMismatchDatabasesConsistent: Int32 = -545
JET_errLogSectorSizeMismatch: Int32 = -546
JET_errLogSectorSizeMismatchDatabasesConsistent: Int32 = -547
JET_errLogSequenceEndDatabasesConsistent: Int32 = -548
JET_errStreamingDataNotLogged: Int32 = -549
JET_errDatabaseDirtyShutdown: Int32 = -550
JET_errDatabaseInconsistent: Int32 = -550
JET_errConsistentTimeMismatch: Int32 = -551
JET_errDatabasePatchFileMismatch: Int32 = -552
JET_errEndingRestoreLogTooLow: Int32 = -553
JET_errStartingRestoreLogTooHigh: Int32 = -554
JET_errGivenLogFileHasBadSignature: Int32 = -555
JET_errGivenLogFileIsNotContiguous: Int32 = -556
JET_errMissingRestoreLogFiles: Int32 = -557
JET_wrnExistingLogFileHasBadSignature: UInt32 = 558
JET_wrnExistingLogFileIsNotContiguous: UInt32 = 559
JET_errMissingFullBackup: Int32 = -560
JET_errBadBackupDatabaseSize: Int32 = -561
JET_errDatabaseAlreadyUpgraded: Int32 = -562
JET_errDatabaseIncompleteUpgrade: Int32 = -563
JET_wrnSkipThisRecord: UInt32 = 564
JET_errMissingCurrentLogFiles: Int32 = -565
JET_errDbTimeTooOld: Int32 = -566
JET_errDbTimeTooNew: Int32 = -567
JET_errMissingFileToBackup: Int32 = -569
JET_errLogTornWriteDuringHardRestore: Int32 = -570
JET_errLogTornWriteDuringHardRecovery: Int32 = -571
JET_errLogCorruptDuringHardRestore: Int32 = -573
JET_errLogCorruptDuringHardRecovery: Int32 = -574
JET_errMustDisableLoggingForDbUpgrade: Int32 = -575
JET_errBadRestoreTargetInstance: Int32 = -577
JET_wrnTargetInstanceRunning: UInt32 = 578
JET_errRecoveredWithoutUndo: Int32 = -579
JET_errDatabasesNotFromSameSnapshot: Int32 = -580
JET_errSoftRecoveryOnSnapshot: Int32 = -581
JET_errCommittedLogFilesMissing: Int32 = -582
JET_errSectorSizeNotSupported: Int32 = -583
JET_errRecoveredWithoutUndoDatabasesConsistent: Int32 = -584
JET_wrnCommittedLogFilesLost: UInt32 = 585
JET_errCommittedLogFileCorrupt: Int32 = -586
JET_wrnCommittedLogFilesRemoved: UInt32 = 587
JET_wrnFinishWithUndo: UInt32 = 588
JET_errLogSequenceChecksumMismatch: Int32 = -590
JET_wrnDatabaseRepaired: UInt32 = 595
JET_errPageInitializedMismatch: Int32 = -596
JET_errUnicodeTranslationBufferTooSmall: Int32 = -601
JET_errUnicodeTranslationFail: Int32 = -602
JET_errUnicodeNormalizationNotSupported: Int32 = -603
JET_errUnicodeLanguageValidationFailure: Int32 = -604
JET_errExistingLogFileHasBadSignature: Int32 = -610
JET_errExistingLogFileIsNotContiguous: Int32 = -611
JET_errLogReadVerifyFailure: Int32 = -612
JET_errCheckpointDepthTooDeep: Int32 = -614
JET_errRestoreOfNonBackupDatabase: Int32 = -615
JET_errLogFileNotCopied: Int32 = -616
JET_errTransactionTooLong: Int32 = -618
JET_errEngineFormatVersionNoLongerSupportedTooLow: Int32 = -619
JET_errEngineFormatVersionNotYetImplementedTooHigh: Int32 = -620
JET_errEngineFormatVersionParamTooLowForRequestedFeature: Int32 = -621
JET_errEngineFormatVersionSpecifiedTooLowForLogVersion: Int32 = -622
JET_errEngineFormatVersionSpecifiedTooLowForDatabaseVersion: Int32 = -623
JET_errBackupAbortByServer: Int32 = -801
JET_errInvalidGrbit: Int32 = -900
JET_errTermInProgress: Int32 = -1000
JET_errFeatureNotAvailable: Int32 = -1001
JET_errInvalidName: Int32 = -1002
JET_errInvalidParameter: Int32 = -1003
JET_wrnColumnNull: UInt32 = 1004
JET_wrnBufferTruncated: UInt32 = 1006
JET_wrnDatabaseAttached: UInt32 = 1007
JET_errDatabaseFileReadOnly: Int32 = -1008
JET_wrnSortOverflow: UInt32 = 1009
JET_errInvalidDatabaseId: Int32 = -1010
JET_errOutOfMemory: Int32 = -1011
JET_errOutOfDatabaseSpace: Int32 = -1012
JET_errOutOfCursors: Int32 = -1013
JET_errOutOfBuffers: Int32 = -1014
JET_errTooManyIndexes: Int32 = -1015
JET_errTooManyKeys: Int32 = -1016
JET_errRecordDeleted: Int32 = -1017
JET_errReadVerifyFailure: Int32 = -1018
JET_errPageNotInitialized: Int32 = -1019
JET_errOutOfFileHandles: Int32 = -1020
JET_errDiskReadVerificationFailure: Int32 = -1021
JET_errDiskIO: Int32 = -1022
JET_errInvalidPath: Int32 = -1023
JET_errInvalidSystemPath: Int32 = -1024
JET_errInvalidLogDirectory: Int32 = -1025
JET_errRecordTooBig: Int32 = -1026
JET_errTooManyOpenDatabases: Int32 = -1027
JET_errInvalidDatabase: Int32 = -1028
JET_errNotInitialized: Int32 = -1029
JET_errAlreadyInitialized: Int32 = -1030
JET_errInitInProgress: Int32 = -1031
JET_errFileAccessDenied: Int32 = -1032
JET_errBufferTooSmall: Int32 = -1038
JET_wrnSeekNotEqual: UInt32 = 1039
JET_errTooManyColumns: Int32 = -1040
JET_errContainerNotEmpty: Int32 = -1043
JET_errInvalidFilename: Int32 = -1044
JET_errInvalidBookmark: Int32 = -1045
JET_errColumnInUse: Int32 = -1046
JET_errInvalidBufferSize: Int32 = -1047
JET_errColumnNotUpdatable: Int32 = -1048
JET_errIndexInUse: Int32 = -1051
JET_errLinkNotSupported: Int32 = -1052
JET_errNullKeyDisallowed: Int32 = -1053
JET_errNotInTransaction: Int32 = -1054
JET_wrnNoErrorInfo: UInt32 = 1055
JET_errMustRollback: Int32 = -1057
JET_wrnNoIdleActivity: UInt32 = 1058
JET_errTooManyActiveUsers: Int32 = -1059
JET_errInvalidCountry: Int32 = -1061
JET_errInvalidLanguageId: Int32 = -1062
JET_errInvalidCodePage: Int32 = -1063
JET_errInvalidLCMapStringFlags: Int32 = -1064
JET_errVersionStoreEntryTooBig: Int32 = -1065
JET_errVersionStoreOutOfMemoryAndCleanupTimedOut: Int32 = -1066
JET_wrnNoWriteLock: UInt32 = 1067
JET_wrnColumnSetNull: UInt32 = 1068
JET_errVersionStoreOutOfMemory: Int32 = -1069
JET_errCannotIndex: Int32 = -1071
JET_errRecordNotDeleted: Int32 = -1072
JET_errTooManyMempoolEntries: Int32 = -1073
JET_errOutOfObjectIDs: Int32 = -1074
JET_errOutOfLongValueIDs: Int32 = -1075
JET_errOutOfAutoincrementValues: Int32 = -1076
JET_errOutOfDbtimeValues: Int32 = -1077
JET_errOutOfSequentialIndexValues: Int32 = -1078
JET_errRunningInOneInstanceMode: Int32 = -1080
JET_errRunningInMultiInstanceMode: Int32 = -1081
JET_errSystemParamsAlreadySet: Int32 = -1082
JET_errSystemPathInUse: Int32 = -1083
JET_errLogFilePathInUse: Int32 = -1084
JET_errTempPathInUse: Int32 = -1085
JET_errInstanceNameInUse: Int32 = -1086
JET_errSystemParameterConflict: Int32 = -1087
JET_errInstanceUnavailable: Int32 = -1090
JET_errDatabaseUnavailable: Int32 = -1091
JET_errInstanceUnavailableDueToFatalLogDiskFull: Int32 = -1092
JET_errInvalidSesparamId: Int32 = -1093
JET_errTooManyRecords: Int32 = -1094
JET_errInvalidDbparamId: Int32 = -1095
JET_errOutOfSessions: Int32 = -1101
JET_errWriteConflict: Int32 = -1102
JET_errTransTooDeep: Int32 = -1103
JET_errInvalidSesid: Int32 = -1104
JET_errWriteConflictPrimaryIndex: Int32 = -1105
JET_errInTransaction: Int32 = -1108
JET_errRollbackRequired: Int32 = -1109
JET_errTransReadOnly: Int32 = -1110
JET_errSessionWriteConflict: Int32 = -1111
JET_errRecordTooBigForBackwardCompatibility: Int32 = -1112
JET_errCannotMaterializeForwardOnlySort: Int32 = -1113
JET_errSesidTableIdMismatch: Int32 = -1114
JET_errInvalidInstance: Int32 = -1115
JET_errDirtyShutdown: Int32 = -1116
JET_errReadPgnoVerifyFailure: Int32 = -1118
JET_errReadLostFlushVerifyFailure: Int32 = -1119
JET_errFileSystemCorruption: Int32 = -1121
JET_wrnShrinkNotPossible: UInt32 = 1122
JET_errRecoveryVerifyFailure: Int32 = -1123
JET_errFilteredMoveNotSupported: Int32 = -1124
JET_errDatabaseDuplicate: Int32 = -1201
JET_errDatabaseInUse: Int32 = -1202
JET_errDatabaseNotFound: Int32 = -1203
JET_errDatabaseInvalidName: Int32 = -1204
JET_errDatabaseInvalidPages: Int32 = -1205
JET_errDatabaseCorrupted: Int32 = -1206
JET_errDatabaseLocked: Int32 = -1207
JET_errCannotDisableVersioning: Int32 = -1208
JET_errInvalidDatabaseVersion: Int32 = -1209
JET_errDatabase200Format: Int32 = -1210
JET_errDatabase400Format: Int32 = -1211
JET_errDatabase500Format: Int32 = -1212
JET_errPageSizeMismatch: Int32 = -1213
JET_errTooManyInstances: Int32 = -1214
JET_errDatabaseSharingViolation: Int32 = -1215
JET_errAttachedDatabaseMismatch: Int32 = -1216
JET_errDatabaseInvalidPath: Int32 = -1217
JET_errDatabaseIdInUse: Int32 = -1218
JET_errForceDetachNotAllowed: Int32 = -1219
JET_errCatalogCorrupted: Int32 = -1220
JET_errPartiallyAttachedDB: Int32 = -1221
JET_errDatabaseSignInUse: Int32 = -1222
JET_errDatabaseCorruptedNoRepair: Int32 = -1224
JET_errInvalidCreateDbVersion: Int32 = -1225
JET_errDatabaseNotReady: Int32 = -1230
JET_errDatabaseAttachedForRecovery: Int32 = -1231
JET_errTransactionsNotReadyDuringRecovery: Int32 = -1232
JET_wrnTableEmpty: UInt32 = 1301
JET_errTableLocked: Int32 = -1302
JET_errTableDuplicate: Int32 = -1303
JET_errTableInUse: Int32 = -1304
JET_errObjectNotFound: Int32 = -1305
JET_errDensityInvalid: Int32 = -1307
JET_errTableNotEmpty: Int32 = -1308
JET_errInvalidTableId: Int32 = -1310
JET_errTooManyOpenTables: Int32 = -1311
JET_errIllegalOperation: Int32 = -1312
JET_errTooManyOpenTablesAndCleanupTimedOut: Int32 = -1313
JET_errObjectDuplicate: Int32 = -1314
JET_errInvalidObject: Int32 = -1316
JET_errCannotDeleteTempTable: Int32 = -1317
JET_errCannotDeleteSystemTable: Int32 = -1318
JET_errCannotDeleteTemplateTable: Int32 = -1319
JET_errExclusiveTableLockRequired: Int32 = -1322
JET_errFixedDDL: Int32 = -1323
JET_errFixedInheritedDDL: Int32 = -1324
JET_errCannotNestDDL: Int32 = -1325
JET_errDDLNotInheritable: Int32 = -1326
JET_wrnTableInUseBySystem: UInt32 = 1327
JET_errInvalidSettings: Int32 = -1328
JET_errClientRequestToStopJetService: Int32 = -1329
JET_errCannotAddFixedVarColumnToDerivedTable: Int32 = -1330
JET_errIndexCantBuild: Int32 = -1401
JET_errIndexHasPrimary: Int32 = -1402
JET_errIndexDuplicate: Int32 = -1403
JET_errIndexNotFound: Int32 = -1404
JET_errIndexMustStay: Int32 = -1405
JET_errIndexInvalidDef: Int32 = -1406
JET_errInvalidCreateIndex: Int32 = -1409
JET_errTooManyOpenIndexes: Int32 = -1410
JET_errMultiValuedIndexViolation: Int32 = -1411
JET_errIndexBuildCorrupted: Int32 = -1412
JET_errPrimaryIndexCorrupted: Int32 = -1413
JET_errSecondaryIndexCorrupted: Int32 = -1414
JET_wrnCorruptIndexDeleted: UInt32 = 1415
JET_errInvalidIndexId: Int32 = -1416
JET_wrnPrimaryIndexOutOfDate: UInt32 = 1417
JET_wrnSecondaryIndexOutOfDate: UInt32 = 1418
JET_errIndexTuplesSecondaryIndexOnly: Int32 = -1430
JET_errIndexTuplesTooManyColumns: Int32 = -1431
JET_errIndexTuplesOneColumnOnly: Int32 = -1431
JET_errIndexTuplesNonUniqueOnly: Int32 = -1432
JET_errIndexTuplesTextBinaryColumnsOnly: Int32 = -1433
JET_errIndexTuplesTextColumnsOnly: Int32 = -1433
JET_errIndexTuplesVarSegMacNotAllowed: Int32 = -1434
JET_errIndexTuplesInvalidLimits: Int32 = -1435
JET_errIndexTuplesCannotRetrieveFromIndex: Int32 = -1436
JET_errIndexTuplesKeyTooSmall: Int32 = -1437
JET_errInvalidLVChunkSize: Int32 = -1438
JET_errColumnCannotBeEncrypted: Int32 = -1439
JET_errCannotIndexOnEncryptedColumn: Int32 = -1440
JET_errColumnLong: Int32 = -1501
JET_errColumnNoChunk: Int32 = -1502
JET_errColumnDoesNotFit: Int32 = -1503
JET_errNullInvalid: Int32 = -1504
JET_errColumnIndexed: Int32 = -1505
JET_errColumnTooBig: Int32 = -1506
JET_errColumnNotFound: Int32 = -1507
JET_errColumnDuplicate: Int32 = -1508
JET_errMultiValuedColumnMustBeTagged: Int32 = -1509
JET_errColumnRedundant: Int32 = -1510
JET_errInvalidColumnType: Int32 = -1511
JET_wrnColumnMaxTruncated: UInt32 = 1512
JET_errTaggedNotNULL: Int32 = -1514
JET_errNoCurrentIndex: Int32 = -1515
JET_errKeyIsMade: Int32 = -1516
JET_errBadColumnId: Int32 = -1517
JET_errBadItagSequence: Int32 = -1518
JET_errColumnInRelationship: Int32 = -1519
JET_wrnCopyLongValue: UInt32 = 1520
JET_errCannotBeTagged: Int32 = -1521
JET_errDefaultValueTooBig: Int32 = -1524
JET_errMultiValuedDuplicate: Int32 = -1525
JET_errLVCorrupted: Int32 = -1526
JET_errMultiValuedDuplicateAfterTruncation: Int32 = -1528
JET_errDerivedColumnCorruption: Int32 = -1529
JET_errInvalidPlaceholderColumn: Int32 = -1530
JET_wrnColumnSkipped: UInt32 = 1531
JET_wrnColumnNotLocal: UInt32 = 1532
JET_wrnColumnMoreTags: UInt32 = 1533
JET_wrnColumnTruncated: UInt32 = 1534
JET_wrnColumnPresent: UInt32 = 1535
JET_wrnColumnSingleValue: UInt32 = 1536
JET_wrnColumnDefault: UInt32 = 1537
JET_errColumnCannotBeCompressed: Int32 = -1538
JET_wrnColumnNotInRecord: UInt32 = 1539
JET_errColumnNoEncryptionKey: Int32 = -1540
JET_wrnColumnReference: UInt32 = 1541
JET_errRecordNotFound: Int32 = -1601
JET_errRecordNoCopy: Int32 = -1602
JET_errNoCurrentRecord: Int32 = -1603
JET_errRecordPrimaryChanged: Int32 = -1604
JET_errKeyDuplicate: Int32 = -1605
JET_errAlreadyPrepared: Int32 = -1607
JET_errKeyNotMade: Int32 = -1608
JET_errUpdateNotPrepared: Int32 = -1609
JET_wrnDataHasChanged: UInt32 = 1610
JET_errDataHasChanged: Int32 = -1611
JET_wrnKeyChanged: UInt32 = 1618
JET_errLanguageNotSupported: Int32 = -1619
JET_errDecompressionFailed: Int32 = -1620
JET_errUpdateMustVersion: Int32 = -1621
JET_errDecryptionFailed: Int32 = -1622
JET_errEncryptionBadItag: Int32 = -1623
JET_errTooManySorts: Int32 = -1701
JET_errInvalidOnSort: Int32 = -1702
JET_errTempFileOpenError: Int32 = -1803
JET_errTooManyAttachedDatabases: Int32 = -1805
JET_errDiskFull: Int32 = -1808
JET_errPermissionDenied: Int32 = -1809
JET_errFileNotFound: Int32 = -1811
JET_errFileInvalidType: Int32 = -1812
JET_wrnFileOpenReadOnly: UInt32 = 1813
JET_errFileAlreadyExists: Int32 = -1814
JET_errAfterInitialization: Int32 = -1850
JET_errLogCorrupted: Int32 = -1852
JET_errInvalidOperation: Int32 = -1906
JET_errAccessDenied: Int32 = -1907
JET_wrnIdleFull: UInt32 = 1908
JET_errTooManySplits: Int32 = -1909
JET_errSessionSharingViolation: Int32 = -1910
JET_errEntryPointNotFound: Int32 = -1911
JET_errSessionContextAlreadySet: Int32 = -1912
JET_errSessionContextNotSetByThisThread: Int32 = -1913
JET_errSessionInUse: Int32 = -1914
JET_errRecordFormatConversionFailed: Int32 = -1915
JET_errOneDatabasePerSession: Int32 = -1916
JET_errRollbackError: Int32 = -1917
JET_errFlushMapVersionUnsupported: Int32 = -1918
JET_errFlushMapDatabaseMismatch: Int32 = -1919
JET_errFlushMapUnrecoverable: Int32 = -1920
JET_wrnDefragAlreadyRunning: UInt32 = 2000
JET_wrnDefragNotRunning: UInt32 = 2001
JET_errDatabaseAlreadyRunningMaintenance: Int32 = -2004
JET_wrnCallbackNotRegistered: UInt32 = 2100
JET_errCallbackFailed: Int32 = -2101
JET_errCallbackNotResolved: Int32 = -2102
JET_errSpaceHintsInvalid: Int32 = -2103
JET_errOSSnapshotInvalidSequence: Int32 = -2401
JET_errOSSnapshotTimeOut: Int32 = -2402
JET_errOSSnapshotNotAllowed: Int32 = -2403
JET_errOSSnapshotInvalidSnapId: Int32 = -2404
JET_errLSCallbackNotSpecified: Int32 = -3000
JET_errLSAlreadySet: Int32 = -3001
JET_errLSNotSet: Int32 = -3002
JET_errFileIOSparse: Int32 = -4000
JET_errFileIOBeyondEOF: Int32 = -4001
JET_errFileIOAbort: Int32 = -4002
JET_errFileIORetry: Int32 = -4003
JET_errFileIOFail: Int32 = -4004
JET_errFileCompressed: Int32 = -4005
JET_BASE_NAME_LENGTH: UInt32 = 3
JET_bitDumpMinimum: UInt32 = 1
JET_bitDumpMaximum: UInt32 = 2
JET_bitDumpCacheMinimum: UInt32 = 4
JET_bitDumpCacheMaximum: UInt32 = 8
JET_bitDumpCacheIncludeDirtyPages: UInt32 = 16
JET_bitDumpCacheIncludeCachedPages: UInt32 = 32
JET_bitDumpCacheIncludeCorruptedPages: UInt32 = 64
JET_bitDumpCacheNoDecommit: UInt32 = 128
@winfunctype('ESENT.dll')
def JetInit(pinstance: POINTER(Windows.Win32.Storage.StructuredStorage.JET_INSTANCE)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetInit2(pinstance: POINTER(Windows.Win32.Storage.StructuredStorage.JET_INSTANCE), grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetInit3A(pinstance: POINTER(Windows.Win32.Storage.StructuredStorage.JET_INSTANCE), prstInfo: POINTER(Windows.Win32.Storage.Jet.JET_RSTINFO_A_head), grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetInit3W(pinstance: POINTER(Windows.Win32.Storage.StructuredStorage.JET_INSTANCE), prstInfo: POINTER(Windows.Win32.Storage.Jet.JET_RSTINFO_W_head), grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetCreateInstanceA(pinstance: POINTER(Windows.Win32.Storage.StructuredStorage.JET_INSTANCE), szInstanceName: POINTER(SByte)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetCreateInstanceW(pinstance: POINTER(Windows.Win32.Storage.StructuredStorage.JET_INSTANCE), szInstanceName: POINTER(UInt16)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetCreateInstance2A(pinstance: POINTER(Windows.Win32.Storage.StructuredStorage.JET_INSTANCE), szInstanceName: POINTER(SByte), szDisplayName: POINTER(SByte), grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetCreateInstance2W(pinstance: POINTER(Windows.Win32.Storage.StructuredStorage.JET_INSTANCE), szInstanceName: POINTER(UInt16), szDisplayName: POINTER(UInt16), grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGetInstanceMiscInfo(instance: Windows.Win32.Storage.StructuredStorage.JET_INSTANCE, pvResult: c_void_p, cbMax: UInt32, InfoLevel: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetTerm(instance: Windows.Win32.Storage.StructuredStorage.JET_INSTANCE) -> Int32: ...
@winfunctype('ESENT.dll')
def JetTerm2(instance: Windows.Win32.Storage.StructuredStorage.JET_INSTANCE, grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetStopService() -> Int32: ...
@winfunctype('ESENT.dll')
def JetStopServiceInstance(instance: Windows.Win32.Storage.StructuredStorage.JET_INSTANCE) -> Int32: ...
@winfunctype('ESENT.dll')
def JetStopServiceInstance2(instance: Windows.Win32.Storage.StructuredStorage.JET_INSTANCE, grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetStopBackup() -> Int32: ...
@winfunctype('ESENT.dll')
def JetStopBackupInstance(instance: Windows.Win32.Storage.StructuredStorage.JET_INSTANCE) -> Int32: ...
@winfunctype('ESENT.dll')
def JetSetSystemParameterA(pinstance: POINTER(Windows.Win32.Storage.StructuredStorage.JET_INSTANCE), sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, paramid: UInt32, lParam: Windows.Win32.Storage.StructuredStorage.JET_API_PTR, szParam: POINTER(SByte)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetSetSystemParameterW(pinstance: POINTER(Windows.Win32.Storage.StructuredStorage.JET_INSTANCE), sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, paramid: UInt32, lParam: Windows.Win32.Storage.StructuredStorage.JET_API_PTR, szParam: POINTER(UInt16)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGetSystemParameterA(instance: Windows.Win32.Storage.StructuredStorage.JET_INSTANCE, sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, paramid: UInt32, plParam: POINTER(Windows.Win32.Storage.StructuredStorage.JET_API_PTR), szParam: POINTER(SByte), cbMax: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGetSystemParameterW(instance: Windows.Win32.Storage.StructuredStorage.JET_INSTANCE, sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, paramid: UInt32, plParam: POINTER(Windows.Win32.Storage.StructuredStorage.JET_API_PTR), szParam: POINTER(UInt16), cbMax: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetEnableMultiInstanceA(psetsysparam: POINTER(Windows.Win32.Storage.Jet.JET_SETSYSPARAM_A_head), csetsysparam: UInt32, pcsetsucceed: POINTER(UInt32)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetEnableMultiInstanceW(psetsysparam: POINTER(Windows.Win32.Storage.Jet.JET_SETSYSPARAM_W_head), csetsysparam: UInt32, pcsetsucceed: POINTER(UInt32)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGetThreadStats(pvResult: c_void_p, cbMax: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetBeginSessionA(instance: Windows.Win32.Storage.StructuredStorage.JET_INSTANCE, psesid: POINTER(Windows.Win32.Storage.StructuredStorage.JET_SESID), szUserName: POINTER(SByte), szPassword: POINTER(SByte)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetBeginSessionW(instance: Windows.Win32.Storage.StructuredStorage.JET_INSTANCE, psesid: POINTER(Windows.Win32.Storage.StructuredStorage.JET_SESID), szUserName: POINTER(UInt16), szPassword: POINTER(UInt16)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetDupSession(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, psesid: POINTER(Windows.Win32.Storage.StructuredStorage.JET_SESID)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetEndSession(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGetVersion(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, pwVersion: POINTER(UInt32)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetIdle(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetCreateDatabaseA(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, szFilename: POINTER(SByte), szConnect: POINTER(SByte), pdbid: POINTER(UInt32), grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetCreateDatabaseW(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, szFilename: POINTER(UInt16), szConnect: POINTER(UInt16), pdbid: POINTER(UInt32), grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetCreateDatabase2A(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, szFilename: POINTER(SByte), cpgDatabaseSizeMax: UInt32, pdbid: POINTER(UInt32), grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetCreateDatabase2W(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, szFilename: POINTER(UInt16), cpgDatabaseSizeMax: UInt32, pdbid: POINTER(UInt32), grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetAttachDatabaseA(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, szFilename: POINTER(SByte), grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetAttachDatabaseW(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, szFilename: POINTER(UInt16), grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetAttachDatabase2A(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, szFilename: POINTER(SByte), cpgDatabaseSizeMax: UInt32, grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetAttachDatabase2W(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, szFilename: POINTER(UInt16), cpgDatabaseSizeMax: UInt32, grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetDetachDatabaseA(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, szFilename: POINTER(SByte)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetDetachDatabaseW(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, szFilename: POINTER(UInt16)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetDetachDatabase2A(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, szFilename: POINTER(SByte), grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetDetachDatabase2W(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, szFilename: POINTER(UInt16), grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGetObjectInfoA(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, dbid: UInt32, objtyp: UInt32, szContainerName: POINTER(SByte), szObjectName: POINTER(SByte), pvResult: c_void_p, cbMax: UInt32, InfoLevel: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGetObjectInfoW(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, dbid: UInt32, objtyp: UInt32, szContainerName: POINTER(UInt16), szObjectName: POINTER(UInt16), pvResult: c_void_p, cbMax: UInt32, InfoLevel: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGetTableInfoA(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, pvResult: c_void_p, cbMax: UInt32, InfoLevel: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGetTableInfoW(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, pvResult: c_void_p, cbMax: UInt32, InfoLevel: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetCreateTableA(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, dbid: UInt32, szTableName: POINTER(SByte), lPages: UInt32, lDensity: UInt32, ptableid: POINTER(Windows.Win32.Storage.StructuredStorage.JET_TABLEID)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetCreateTableW(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, dbid: UInt32, szTableName: POINTER(UInt16), lPages: UInt32, lDensity: UInt32, ptableid: POINTER(Windows.Win32.Storage.StructuredStorage.JET_TABLEID)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetCreateTableColumnIndexA(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, dbid: UInt32, ptablecreate: POINTER(Windows.Win32.Storage.Jet.JET_TABLECREATE_A_head)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetCreateTableColumnIndexW(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, dbid: UInt32, ptablecreate: POINTER(Windows.Win32.Storage.Jet.JET_TABLECREATE_W_head)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetCreateTableColumnIndex2A(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, dbid: UInt32, ptablecreate: POINTER(Windows.Win32.Storage.Jet.JET_TABLECREATE2_A_head)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetCreateTableColumnIndex2W(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, dbid: UInt32, ptablecreate: POINTER(Windows.Win32.Storage.Jet.JET_TABLECREATE2_W_head)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetCreateTableColumnIndex3A(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, dbid: UInt32, ptablecreate: POINTER(Windows.Win32.Storage.Jet.JET_TABLECREATE3_A_head)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetCreateTableColumnIndex3W(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, dbid: UInt32, ptablecreate: POINTER(Windows.Win32.Storage.Jet.JET_TABLECREATE3_W_head)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetCreateTableColumnIndex4A(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, dbid: UInt32, ptablecreate: POINTER(Windows.Win32.Storage.Jet.JET_TABLECREATE4_A_head)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetCreateTableColumnIndex4W(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, dbid: UInt32, ptablecreate: POINTER(Windows.Win32.Storage.Jet.JET_TABLECREATE4_W_head)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetDeleteTableA(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, dbid: UInt32, szTableName: POINTER(SByte)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetDeleteTableW(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, dbid: UInt32, szTableName: POINTER(UInt16)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetRenameTableA(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, dbid: UInt32, szName: POINTER(SByte), szNameNew: POINTER(SByte)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetRenameTableW(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, dbid: UInt32, szName: POINTER(UInt16), szNameNew: POINTER(UInt16)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGetTableColumnInfoA(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, szColumnName: POINTER(SByte), pvResult: c_void_p, cbMax: UInt32, InfoLevel: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGetTableColumnInfoW(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, szColumnName: POINTER(UInt16), pvResult: c_void_p, cbMax: UInt32, InfoLevel: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGetColumnInfoA(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, dbid: UInt32, szTableName: POINTER(SByte), pColumnNameOrId: POINTER(SByte), pvResult: c_void_p, cbMax: UInt32, InfoLevel: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGetColumnInfoW(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, dbid: UInt32, szTableName: POINTER(UInt16), pwColumnNameOrId: POINTER(UInt16), pvResult: c_void_p, cbMax: UInt32, InfoLevel: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetAddColumnA(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, szColumnName: POINTER(SByte), pcolumndef: POINTER(Windows.Win32.Storage.Jet.JET_COLUMNDEF_head), pvDefault: c_void_p, cbDefault: UInt32, pcolumnid: POINTER(UInt32)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetAddColumnW(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, szColumnName: POINTER(UInt16), pcolumndef: POINTER(Windows.Win32.Storage.Jet.JET_COLUMNDEF_head), pvDefault: c_void_p, cbDefault: UInt32, pcolumnid: POINTER(UInt32)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetDeleteColumnA(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, szColumnName: POINTER(SByte)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetDeleteColumnW(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, szColumnName: POINTER(UInt16)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetDeleteColumn2A(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, szColumnName: POINTER(SByte), grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetDeleteColumn2W(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, szColumnName: POINTER(UInt16), grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetRenameColumnA(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, szName: POINTER(SByte), szNameNew: POINTER(SByte), grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetRenameColumnW(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, szName: POINTER(UInt16), szNameNew: POINTER(UInt16), grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetSetColumnDefaultValueA(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, dbid: UInt32, szTableName: POINTER(SByte), szColumnName: POINTER(SByte), pvData: c_void_p, cbData: UInt32, grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetSetColumnDefaultValueW(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, dbid: UInt32, szTableName: POINTER(UInt16), szColumnName: POINTER(UInt16), pvData: c_void_p, cbData: UInt32, grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGetTableIndexInfoA(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, szIndexName: POINTER(SByte), pvResult: c_void_p, cbResult: UInt32, InfoLevel: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGetTableIndexInfoW(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, szIndexName: POINTER(UInt16), pvResult: c_void_p, cbResult: UInt32, InfoLevel: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGetIndexInfoA(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, dbid: UInt32, szTableName: POINTER(SByte), szIndexName: POINTER(SByte), pvResult: c_void_p, cbResult: UInt32, InfoLevel: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGetIndexInfoW(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, dbid: UInt32, szTableName: POINTER(UInt16), szIndexName: POINTER(UInt16), pvResult: c_void_p, cbResult: UInt32, InfoLevel: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetCreateIndexA(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, szIndexName: POINTER(SByte), grbit: UInt32, szKey: Windows.Win32.Foundation.PSTR, cbKey: UInt32, lDensity: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetCreateIndexW(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, szIndexName: POINTER(UInt16), grbit: UInt32, szKey: Windows.Win32.Foundation.PWSTR, cbKey: UInt32, lDensity: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetCreateIndex2A(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, pindexcreate: POINTER(Windows.Win32.Storage.Jet.JET_INDEXCREATE_A_head), cIndexCreate: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetCreateIndex2W(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, pindexcreate: POINTER(Windows.Win32.Storage.Jet.JET_INDEXCREATE_W_head), cIndexCreate: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetCreateIndex3A(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, pindexcreate: POINTER(Windows.Win32.Storage.Jet.JET_INDEXCREATE2_A_head), cIndexCreate: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetCreateIndex3W(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, pindexcreate: POINTER(Windows.Win32.Storage.Jet.JET_INDEXCREATE2_W_head), cIndexCreate: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetCreateIndex4A(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, pindexcreate: POINTER(Windows.Win32.Storage.Jet.JET_INDEXCREATE3_A_head), cIndexCreate: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetCreateIndex4W(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, pindexcreate: POINTER(Windows.Win32.Storage.Jet.JET_INDEXCREATE3_W_head), cIndexCreate: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetDeleteIndexA(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, szIndexName: POINTER(SByte)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetDeleteIndexW(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, szIndexName: POINTER(UInt16)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetBeginTransaction(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID) -> Int32: ...
@winfunctype('ESENT.dll')
def JetBeginTransaction2(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetBeginTransaction3(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, trxid: Int64, grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetCommitTransaction(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetCommitTransaction2(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, grbit: UInt32, cmsecDurableCommit: UInt32, pCommitId: POINTER(Windows.Win32.Storage.Jet.JET_COMMIT_ID_head)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetRollback(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGetDatabaseInfoA(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, dbid: UInt32, pvResult: c_void_p, cbMax: UInt32, InfoLevel: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGetDatabaseInfoW(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, dbid: UInt32, pvResult: c_void_p, cbMax: UInt32, InfoLevel: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGetDatabaseFileInfoA(szDatabaseName: POINTER(SByte), pvResult: c_void_p, cbMax: UInt32, InfoLevel: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGetDatabaseFileInfoW(szDatabaseName: POINTER(UInt16), pvResult: c_void_p, cbMax: UInt32, InfoLevel: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetOpenDatabaseA(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, szFilename: POINTER(SByte), szConnect: POINTER(SByte), pdbid: POINTER(UInt32), grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetOpenDatabaseW(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, szFilename: POINTER(UInt16), szConnect: POINTER(UInt16), pdbid: POINTER(UInt32), grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetCloseDatabase(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, dbid: UInt32, grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetOpenTableA(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, dbid: UInt32, szTableName: POINTER(SByte), pvParameters: c_void_p, cbParameters: UInt32, grbit: UInt32, ptableid: POINTER(Windows.Win32.Storage.StructuredStorage.JET_TABLEID)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetOpenTableW(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, dbid: UInt32, szTableName: POINTER(UInt16), pvParameters: c_void_p, cbParameters: UInt32, grbit: UInt32, ptableid: POINTER(Windows.Win32.Storage.StructuredStorage.JET_TABLEID)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetSetTableSequential(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetResetTableSequential(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetCloseTable(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID) -> Int32: ...
@winfunctype('ESENT.dll')
def JetDelete(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID) -> Int32: ...
@winfunctype('ESENT.dll')
def JetUpdate(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, pvBookmark: c_void_p, cbBookmark: UInt32, pcbActual: POINTER(UInt32)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetUpdate2(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, pvBookmark: c_void_p, cbBookmark: UInt32, pcbActual: POINTER(UInt32), grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetEscrowUpdate(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, columnid: UInt32, pv: c_void_p, cbMax: UInt32, pvOld: c_void_p, cbOldMax: UInt32, pcbOldActual: POINTER(UInt32), grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetRetrieveColumn(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, columnid: UInt32, pvData: c_void_p, cbData: UInt32, pcbActual: POINTER(UInt32), grbit: UInt32, pretinfo: POINTER(Windows.Win32.Storage.Jet.JET_RETINFO_head)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetRetrieveColumns(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, pretrievecolumn: POINTER(Windows.Win32.Storage.Jet.JET_RETRIEVECOLUMN_head), cretrievecolumn: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetEnumerateColumns(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, cEnumColumnId: UInt32, rgEnumColumnId: POINTER(Windows.Win32.Storage.Jet.JET_ENUMCOLUMNID_head), pcEnumColumn: POINTER(UInt32), prgEnumColumn: POINTER(POINTER(Windows.Win32.Storage.Jet.JET_ENUMCOLUMN_head)), pfnRealloc: Windows.Win32.Storage.Jet.JET_PFNREALLOC, pvReallocContext: c_void_p, cbDataMost: UInt32, grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGetRecordSize(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, precsize: POINTER(Windows.Win32.Storage.Jet.JET_RECSIZE_head), grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGetRecordSize2(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, precsize: POINTER(Windows.Win32.Storage.Jet.JET_RECSIZE2_head), grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetSetColumn(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, columnid: UInt32, pvData: c_void_p, cbData: UInt32, grbit: UInt32, psetinfo: POINTER(Windows.Win32.Storage.Jet.JET_SETINFO_head)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetSetColumns(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, psetcolumn: POINTER(Windows.Win32.Storage.Jet.JET_SETCOLUMN_head), csetcolumn: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetPrepareUpdate(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, prep: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGetRecordPosition(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, precpos: POINTER(Windows.Win32.Storage.Jet.JET_RECPOS_head), cbRecpos: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGotoPosition(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, precpos: POINTER(Windows.Win32.Storage.Jet.JET_RECPOS_head)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGetCursorInfo(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, pvResult: c_void_p, cbMax: UInt32, InfoLevel: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetDupCursor(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, ptableid: POINTER(Windows.Win32.Storage.StructuredStorage.JET_TABLEID), grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGetCurrentIndexA(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, szIndexName: POINTER(SByte), cbIndexName: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGetCurrentIndexW(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, szIndexName: POINTER(UInt16), cbIndexName: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetSetCurrentIndexA(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, szIndexName: POINTER(SByte)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetSetCurrentIndexW(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, szIndexName: POINTER(UInt16)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetSetCurrentIndex2A(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, szIndexName: POINTER(SByte), grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetSetCurrentIndex2W(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, szIndexName: POINTER(UInt16), grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetSetCurrentIndex3A(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, szIndexName: POINTER(SByte), grbit: UInt32, itagSequence: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetSetCurrentIndex3W(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, szIndexName: POINTER(UInt16), grbit: UInt32, itagSequence: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetSetCurrentIndex4A(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, szIndexName: POINTER(SByte), pindexid: POINTER(Windows.Win32.Storage.Jet.JET_INDEXID_head), grbit: UInt32, itagSequence: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetSetCurrentIndex4W(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, szIndexName: POINTER(UInt16), pindexid: POINTER(Windows.Win32.Storage.Jet.JET_INDEXID_head), grbit: UInt32, itagSequence: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetMove(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, cRow: Int32, grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetSetCursorFilter(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, rgColumnFilters: POINTER(Windows.Win32.Storage.Jet.JET_INDEX_COLUMN_head), cColumnFilters: UInt32, grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGetLock(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetMakeKey(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, pvData: c_void_p, cbData: UInt32, grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetSeek(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetPrereadKeys(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, rgpvKeys: POINTER(c_void_p), rgcbKeys: POINTER(UInt32), ckeys: Int32, pckeysPreread: POINTER(Int32), grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetPrereadIndexRanges(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, rgIndexRanges: POINTER(Windows.Win32.Storage.Jet.JET_INDEX_RANGE_head), cIndexRanges: UInt32, pcRangesPreread: POINTER(UInt32), rgcolumnidPreread: POINTER(UInt32), ccolumnidPreread: UInt32, grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGetBookmark(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, pvBookmark: c_void_p, cbMax: UInt32, pcbActual: POINTER(UInt32)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGetSecondaryIndexBookmark(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, pvSecondaryKey: c_void_p, cbSecondaryKeyMax: UInt32, pcbSecondaryKeyActual: POINTER(UInt32), pvPrimaryBookmark: c_void_p, cbPrimaryBookmarkMax: UInt32, pcbPrimaryBookmarkActual: POINTER(UInt32), grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetCompactA(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, szDatabaseSrc: POINTER(SByte), szDatabaseDest: POINTER(SByte), pfnStatus: Windows.Win32.Storage.Jet.JET_PFNSTATUS, pconvert: POINTER(Windows.Win32.Storage.Jet.JET_CONVERT_A_head), grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetCompactW(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, szDatabaseSrc: POINTER(UInt16), szDatabaseDest: POINTER(UInt16), pfnStatus: Windows.Win32.Storage.Jet.JET_PFNSTATUS, pconvert: POINTER(Windows.Win32.Storage.Jet.JET_CONVERT_W_head), grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetDefragmentA(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, dbid: UInt32, szTableName: POINTER(SByte), pcPasses: POINTER(UInt32), pcSeconds: POINTER(UInt32), grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetDefragmentW(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, dbid: UInt32, szTableName: POINTER(UInt16), pcPasses: POINTER(UInt32), pcSeconds: POINTER(UInt32), grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetDefragment2A(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, dbid: UInt32, szTableName: POINTER(SByte), pcPasses: POINTER(UInt32), pcSeconds: POINTER(UInt32), callback: Windows.Win32.Storage.Jet.JET_CALLBACK, grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetDefragment2W(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, dbid: UInt32, szTableName: POINTER(UInt16), pcPasses: POINTER(UInt32), pcSeconds: POINTER(UInt32), callback: Windows.Win32.Storage.Jet.JET_CALLBACK, grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetDefragment3A(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, szDatabaseName: POINTER(SByte), szTableName: POINTER(SByte), pcPasses: POINTER(UInt32), pcSeconds: POINTER(UInt32), callback: Windows.Win32.Storage.Jet.JET_CALLBACK, pvContext: c_void_p, grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetDefragment3W(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, szDatabaseName: POINTER(UInt16), szTableName: POINTER(UInt16), pcPasses: POINTER(UInt32), pcSeconds: POINTER(UInt32), callback: Windows.Win32.Storage.Jet.JET_CALLBACK, pvContext: c_void_p, grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetSetDatabaseSizeA(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, szDatabaseName: POINTER(SByte), cpg: UInt32, pcpgReal: POINTER(UInt32)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetSetDatabaseSizeW(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, szDatabaseName: POINTER(UInt16), cpg: UInt32, pcpgReal: POINTER(UInt32)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGrowDatabase(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, dbid: UInt32, cpg: UInt32, pcpgReal: POINTER(UInt32)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetResizeDatabase(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, dbid: UInt32, cpgTarget: UInt32, pcpgActual: POINTER(UInt32), grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetSetSessionContext(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, ulContext: Windows.Win32.Storage.StructuredStorage.JET_API_PTR) -> Int32: ...
@winfunctype('ESENT.dll')
def JetResetSessionContext(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGotoBookmark(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, pvBookmark: c_void_p, cbBookmark: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGotoSecondaryIndexBookmark(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, pvSecondaryKey: c_void_p, cbSecondaryKey: UInt32, pvPrimaryBookmark: c_void_p, cbPrimaryBookmark: UInt32, grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetIntersectIndexes(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, rgindexrange: POINTER(Windows.Win32.Storage.Jet.JET_INDEXRANGE_head), cindexrange: UInt32, precordlist: POINTER(Windows.Win32.Storage.Jet.JET_RECORDLIST_head), grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetComputeStats(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID) -> Int32: ...
@winfunctype('ESENT.dll')
def JetOpenTempTable(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, prgcolumndef: POINTER(Windows.Win32.Storage.Jet.JET_COLUMNDEF_head), ccolumn: UInt32, grbit: UInt32, ptableid: POINTER(Windows.Win32.Storage.StructuredStorage.JET_TABLEID), prgcolumnid: POINTER(UInt32)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetOpenTempTable2(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, prgcolumndef: POINTER(Windows.Win32.Storage.Jet.JET_COLUMNDEF_head), ccolumn: UInt32, lcid: UInt32, grbit: UInt32, ptableid: POINTER(Windows.Win32.Storage.StructuredStorage.JET_TABLEID), prgcolumnid: POINTER(UInt32)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetOpenTempTable3(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, prgcolumndef: POINTER(Windows.Win32.Storage.Jet.JET_COLUMNDEF_head), ccolumn: UInt32, pidxunicode: POINTER(Windows.Win32.Storage.Jet.JET_UNICODEINDEX_head), grbit: UInt32, ptableid: POINTER(Windows.Win32.Storage.StructuredStorage.JET_TABLEID), prgcolumnid: POINTER(UInt32)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetOpenTemporaryTable(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, popentemporarytable: POINTER(Windows.Win32.Storage.Jet.JET_OPENTEMPORARYTABLE_head)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetOpenTemporaryTable2(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, popentemporarytable: POINTER(Windows.Win32.Storage.Jet.JET_OPENTEMPORARYTABLE2_head)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetBackupA(szBackupPath: POINTER(SByte), grbit: UInt32, pfnStatus: Windows.Win32.Storage.Jet.JET_PFNSTATUS) -> Int32: ...
@winfunctype('ESENT.dll')
def JetBackupW(szBackupPath: POINTER(UInt16), grbit: UInt32, pfnStatus: Windows.Win32.Storage.Jet.JET_PFNSTATUS) -> Int32: ...
@winfunctype('ESENT.dll')
def JetBackupInstanceA(instance: Windows.Win32.Storage.StructuredStorage.JET_INSTANCE, szBackupPath: POINTER(SByte), grbit: UInt32, pfnStatus: Windows.Win32.Storage.Jet.JET_PFNSTATUS) -> Int32: ...
@winfunctype('ESENT.dll')
def JetBackupInstanceW(instance: Windows.Win32.Storage.StructuredStorage.JET_INSTANCE, szBackupPath: POINTER(UInt16), grbit: UInt32, pfnStatus: Windows.Win32.Storage.Jet.JET_PFNSTATUS) -> Int32: ...
@winfunctype('ESENT.dll')
def JetRestoreA(szSource: POINTER(SByte), pfn: Windows.Win32.Storage.Jet.JET_PFNSTATUS) -> Int32: ...
@winfunctype('ESENT.dll')
def JetRestoreW(szSource: POINTER(UInt16), pfn: Windows.Win32.Storage.Jet.JET_PFNSTATUS) -> Int32: ...
@winfunctype('ESENT.dll')
def JetRestore2A(sz: POINTER(SByte), szDest: POINTER(SByte), pfn: Windows.Win32.Storage.Jet.JET_PFNSTATUS) -> Int32: ...
@winfunctype('ESENT.dll')
def JetRestore2W(sz: POINTER(UInt16), szDest: POINTER(UInt16), pfn: Windows.Win32.Storage.Jet.JET_PFNSTATUS) -> Int32: ...
@winfunctype('ESENT.dll')
def JetRestoreInstanceA(instance: Windows.Win32.Storage.StructuredStorage.JET_INSTANCE, sz: POINTER(SByte), szDest: POINTER(SByte), pfn: Windows.Win32.Storage.Jet.JET_PFNSTATUS) -> Int32: ...
@winfunctype('ESENT.dll')
def JetRestoreInstanceW(instance: Windows.Win32.Storage.StructuredStorage.JET_INSTANCE, sz: POINTER(UInt16), szDest: POINTER(UInt16), pfn: Windows.Win32.Storage.Jet.JET_PFNSTATUS) -> Int32: ...
@winfunctype('ESENT.dll')
def JetSetIndexRange(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableidSrc: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetIndexRecordCount(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, pcrec: POINTER(UInt32), crecMax: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetRetrieveKey(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, pvKey: c_void_p, cbMax: UInt32, pcbActual: POINTER(UInt32), grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetBeginExternalBackup(grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetBeginExternalBackupInstance(instance: Windows.Win32.Storage.StructuredStorage.JET_INSTANCE, grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGetAttachInfoA(szzDatabases: POINTER(SByte), cbMax: UInt32, pcbActual: POINTER(UInt32)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGetAttachInfoW(wszzDatabases: POINTER(UInt16), cbMax: UInt32, pcbActual: POINTER(UInt32)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGetAttachInfoInstanceA(instance: Windows.Win32.Storage.StructuredStorage.JET_INSTANCE, szzDatabases: POINTER(SByte), cbMax: UInt32, pcbActual: POINTER(UInt32)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGetAttachInfoInstanceW(instance: Windows.Win32.Storage.StructuredStorage.JET_INSTANCE, szzDatabases: POINTER(UInt16), cbMax: UInt32, pcbActual: POINTER(UInt32)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetOpenFileA(szFileName: POINTER(SByte), phfFile: POINTER(Windows.Win32.Storage.StructuredStorage.JET_HANDLE), pulFileSizeLow: POINTER(UInt32), pulFileSizeHigh: POINTER(UInt32)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetOpenFileW(szFileName: POINTER(UInt16), phfFile: POINTER(Windows.Win32.Storage.StructuredStorage.JET_HANDLE), pulFileSizeLow: POINTER(UInt32), pulFileSizeHigh: POINTER(UInt32)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetOpenFileInstanceA(instance: Windows.Win32.Storage.StructuredStorage.JET_INSTANCE, szFileName: POINTER(SByte), phfFile: POINTER(Windows.Win32.Storage.StructuredStorage.JET_HANDLE), pulFileSizeLow: POINTER(UInt32), pulFileSizeHigh: POINTER(UInt32)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetOpenFileInstanceW(instance: Windows.Win32.Storage.StructuredStorage.JET_INSTANCE, szFileName: POINTER(UInt16), phfFile: POINTER(Windows.Win32.Storage.StructuredStorage.JET_HANDLE), pulFileSizeLow: POINTER(UInt32), pulFileSizeHigh: POINTER(UInt32)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetReadFile(hfFile: Windows.Win32.Storage.StructuredStorage.JET_HANDLE, pv: c_void_p, cb: UInt32, pcbActual: POINTER(UInt32)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetReadFileInstance(instance: Windows.Win32.Storage.StructuredStorage.JET_INSTANCE, hfFile: Windows.Win32.Storage.StructuredStorage.JET_HANDLE, pv: c_void_p, cb: UInt32, pcbActual: POINTER(UInt32)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetCloseFile(hfFile: Windows.Win32.Storage.StructuredStorage.JET_HANDLE) -> Int32: ...
@winfunctype('ESENT.dll')
def JetCloseFileInstance(instance: Windows.Win32.Storage.StructuredStorage.JET_INSTANCE, hfFile: Windows.Win32.Storage.StructuredStorage.JET_HANDLE) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGetLogInfoA(szzLogs: POINTER(SByte), cbMax: UInt32, pcbActual: POINTER(UInt32)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGetLogInfoW(szzLogs: POINTER(UInt16), cbMax: UInt32, pcbActual: POINTER(UInt32)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGetLogInfoInstanceA(instance: Windows.Win32.Storage.StructuredStorage.JET_INSTANCE, szzLogs: POINTER(SByte), cbMax: UInt32, pcbActual: POINTER(UInt32)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGetLogInfoInstanceW(instance: Windows.Win32.Storage.StructuredStorage.JET_INSTANCE, wszzLogs: POINTER(UInt16), cbMax: UInt32, pcbActual: POINTER(UInt32)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGetLogInfoInstance2A(instance: Windows.Win32.Storage.StructuredStorage.JET_INSTANCE, szzLogs: POINTER(SByte), cbMax: UInt32, pcbActual: POINTER(UInt32), pLogInfo: POINTER(Windows.Win32.Storage.Jet.JET_LOGINFO_A_head)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGetLogInfoInstance2W(instance: Windows.Win32.Storage.StructuredStorage.JET_INSTANCE, wszzLogs: POINTER(UInt16), cbMax: UInt32, pcbActual: POINTER(UInt32), pLogInfo: POINTER(Windows.Win32.Storage.Jet.JET_LOGINFO_W_head)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGetTruncateLogInfoInstanceA(instance: Windows.Win32.Storage.StructuredStorage.JET_INSTANCE, szzLogs: POINTER(SByte), cbMax: UInt32, pcbActual: POINTER(UInt32)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGetTruncateLogInfoInstanceW(instance: Windows.Win32.Storage.StructuredStorage.JET_INSTANCE, wszzLogs: POINTER(UInt16), cbMax: UInt32, pcbActual: POINTER(UInt32)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetTruncateLog() -> Int32: ...
@winfunctype('ESENT.dll')
def JetTruncateLogInstance(instance: Windows.Win32.Storage.StructuredStorage.JET_INSTANCE) -> Int32: ...
@winfunctype('ESENT.dll')
def JetEndExternalBackup() -> Int32: ...
@winfunctype('ESENT.dll')
def JetEndExternalBackupInstance(instance: Windows.Win32.Storage.StructuredStorage.JET_INSTANCE) -> Int32: ...
@winfunctype('ESENT.dll')
def JetEndExternalBackupInstance2(instance: Windows.Win32.Storage.StructuredStorage.JET_INSTANCE, grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetExternalRestoreA(szCheckpointFilePath: POINTER(SByte), szLogPath: POINTER(SByte), rgrstmap: POINTER(Windows.Win32.Storage.Jet.JET_RSTMAP_A_head), crstfilemap: Int32, szBackupLogPath: POINTER(SByte), genLow: Int32, genHigh: Int32, pfn: Windows.Win32.Storage.Jet.JET_PFNSTATUS) -> Int32: ...
@winfunctype('ESENT.dll')
def JetExternalRestoreW(szCheckpointFilePath: POINTER(UInt16), szLogPath: POINTER(UInt16), rgrstmap: POINTER(Windows.Win32.Storage.Jet.JET_RSTMAP_W_head), crstfilemap: Int32, szBackupLogPath: POINTER(UInt16), genLow: Int32, genHigh: Int32, pfn: Windows.Win32.Storage.Jet.JET_PFNSTATUS) -> Int32: ...
@winfunctype('ESENT.dll')
def JetExternalRestore2A(szCheckpointFilePath: POINTER(SByte), szLogPath: POINTER(SByte), rgrstmap: POINTER(Windows.Win32.Storage.Jet.JET_RSTMAP_A_head), crstfilemap: Int32, szBackupLogPath: POINTER(SByte), pLogInfo: POINTER(Windows.Win32.Storage.Jet.JET_LOGINFO_A_head), szTargetInstanceName: POINTER(SByte), szTargetInstanceLogPath: POINTER(SByte), szTargetInstanceCheckpointPath: POINTER(SByte), pfn: Windows.Win32.Storage.Jet.JET_PFNSTATUS) -> Int32: ...
@winfunctype('ESENT.dll')
def JetExternalRestore2W(szCheckpointFilePath: POINTER(UInt16), szLogPath: POINTER(UInt16), rgrstmap: POINTER(Windows.Win32.Storage.Jet.JET_RSTMAP_W_head), crstfilemap: Int32, szBackupLogPath: POINTER(UInt16), pLogInfo: POINTER(Windows.Win32.Storage.Jet.JET_LOGINFO_W_head), szTargetInstanceName: POINTER(UInt16), szTargetInstanceLogPath: POINTER(UInt16), szTargetInstanceCheckpointPath: POINTER(UInt16), pfn: Windows.Win32.Storage.Jet.JET_PFNSTATUS) -> Int32: ...
@winfunctype('ESENT.dll')
def JetRegisterCallback(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, cbtyp: UInt32, pCallback: Windows.Win32.Storage.Jet.JET_CALLBACK, pvContext: c_void_p, phCallbackId: POINTER(Windows.Win32.Storage.StructuredStorage.JET_HANDLE)) -> Int32: ...
@winfunctype('ESENT.dll')
def JetUnregisterCallback(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, cbtyp: UInt32, hCallbackId: Windows.Win32.Storage.StructuredStorage.JET_HANDLE) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGetInstanceInfoA(pcInstanceInfo: POINTER(UInt32), paInstanceInfo: POINTER(POINTER(Windows.Win32.Storage.Jet.JET_INSTANCE_INFO_A_head))) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGetInstanceInfoW(pcInstanceInfo: POINTER(UInt32), paInstanceInfo: POINTER(POINTER(Windows.Win32.Storage.Jet.JET_INSTANCE_INFO_W_head))) -> Int32: ...
@winfunctype('ESENT.dll')
def JetFreeBuffer(pbBuf: Windows.Win32.Foundation.PSTR) -> Int32: ...
@winfunctype('ESENT.dll')
def JetSetLS(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, ls: Windows.Win32.Storage.Jet.JET_LS, grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGetLS(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, pls: POINTER(Windows.Win32.Storage.Jet.JET_LS), grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetOSSnapshotPrepare(psnapId: POINTER(Windows.Win32.Storage.Jet.JET_OSSNAPID), grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetOSSnapshotPrepareInstance(snapId: Windows.Win32.Storage.Jet.JET_OSSNAPID, instance: Windows.Win32.Storage.StructuredStorage.JET_INSTANCE, grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetOSSnapshotFreezeA(snapId: Windows.Win32.Storage.Jet.JET_OSSNAPID, pcInstanceInfo: POINTER(UInt32), paInstanceInfo: POINTER(POINTER(Windows.Win32.Storage.Jet.JET_INSTANCE_INFO_A_head)), grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetOSSnapshotFreezeW(snapId: Windows.Win32.Storage.Jet.JET_OSSNAPID, pcInstanceInfo: POINTER(UInt32), paInstanceInfo: POINTER(POINTER(Windows.Win32.Storage.Jet.JET_INSTANCE_INFO_W_head)), grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetOSSnapshotThaw(snapId: Windows.Win32.Storage.Jet.JET_OSSNAPID, grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetOSSnapshotAbort(snapId: Windows.Win32.Storage.Jet.JET_OSSNAPID, grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetOSSnapshotTruncateLog(snapId: Windows.Win32.Storage.Jet.JET_OSSNAPID, grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetOSSnapshotTruncateLogInstance(snapId: Windows.Win32.Storage.Jet.JET_OSSNAPID, instance: Windows.Win32.Storage.StructuredStorage.JET_INSTANCE, grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetOSSnapshotGetFreezeInfoA(snapId: Windows.Win32.Storage.Jet.JET_OSSNAPID, pcInstanceInfo: POINTER(UInt32), paInstanceInfo: POINTER(POINTER(Windows.Win32.Storage.Jet.JET_INSTANCE_INFO_A_head)), grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetOSSnapshotGetFreezeInfoW(snapId: Windows.Win32.Storage.Jet.JET_OSSNAPID, pcInstanceInfo: POINTER(UInt32), paInstanceInfo: POINTER(POINTER(Windows.Win32.Storage.Jet.JET_INSTANCE_INFO_W_head)), grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetOSSnapshotEnd(snapId: Windows.Win32.Storage.Jet.JET_OSSNAPID, grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetConfigureProcessForCrashDump(grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGetErrorInfoW(pvContext: c_void_p, pvResult: c_void_p, cbMax: UInt32, InfoLevel: UInt32, grbit: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetSetSessionParameter(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, sesparamid: UInt32, pvParam: c_void_p, cbParam: UInt32) -> Int32: ...
@winfunctype('ESENT.dll')
def JetGetSessionParameter(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, sesparamid: UInt32, pvParam: c_void_p, cbParamMax: UInt32, pcbParamActual: POINTER(UInt32)) -> Int32: ...
class JET_BKINFO(Structure):
    lgposMark: Windows.Win32.Storage.Jet.JET_LGPOS
    Anonymous: _Anonymous_e__Union
    genLow: UInt32
    genHigh: UInt32
    _pack_ = 1
    class _Anonymous_e__Union(Union):
        logtimeMark: Windows.Win32.Storage.Jet.JET_LOGTIME
        bklogtimeMark: Windows.Win32.Storage.Jet.JET_BKLOGTIME
class JET_BKLOGTIME(Structure):
    bSeconds: Windows.Win32.Foundation.CHAR
    bMinutes: Windows.Win32.Foundation.CHAR
    bHours: Windows.Win32.Foundation.CHAR
    bDay: Windows.Win32.Foundation.CHAR
    bMonth: Windows.Win32.Foundation.CHAR
    bYear: Windows.Win32.Foundation.CHAR
    Anonymous1: _Anonymous1_e__Union
    Anonymous2: _Anonymous2_e__Union
    class _Anonymous1_e__Union(Union):
        bFiller1: Windows.Win32.Foundation.CHAR
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            _bitfield: Byte
    class _Anonymous2_e__Union(Union):
        bFiller2: Windows.Win32.Foundation.CHAR
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            _bitfield: Byte
@winfunctype_pointer
def JET_CALLBACK(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, dbid: UInt32, tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID, cbtyp: UInt32, pvArg1: c_void_p, pvArg2: c_void_p, pvContext: c_void_p, ulUnused: Windows.Win32.Storage.StructuredStorage.JET_API_PTR) -> Int32: ...
class JET_COLUMNBASE_A(Structure):
    cbStruct: UInt32
    columnid: UInt32
    coltyp: UInt32
    wCountry: UInt16
    langid: UInt16
    cp: UInt16
    wFiller: UInt16
    cbMax: UInt32
    grbit: UInt32
    szBaseTableName: Windows.Win32.Foundation.CHAR * 256
    szBaseColumnName: Windows.Win32.Foundation.CHAR * 256
class JET_COLUMNBASE_W(Structure):
    cbStruct: UInt32
    columnid: UInt32
    coltyp: UInt32
    wCountry: UInt16
    langid: UInt16
    cp: UInt16
    wFiller: UInt16
    cbMax: UInt32
    grbit: UInt32
    szBaseTableName: Char * 256
    szBaseColumnName: Char * 256
class JET_COLUMNCREATE_A(Structure):
    cbStruct: UInt32
    szColumnName: Windows.Win32.Foundation.PSTR
    coltyp: UInt32
    cbMax: UInt32
    grbit: UInt32
    pvDefault: c_void_p
    cbDefault: UInt32
    cp: UInt32
    columnid: UInt32
    err: Int32
class JET_COLUMNCREATE_W(Structure):
    cbStruct: UInt32
    szColumnName: Windows.Win32.Foundation.PWSTR
    coltyp: UInt32
    cbMax: UInt32
    grbit: UInt32
    pvDefault: c_void_p
    cbDefault: UInt32
    cp: UInt32
    columnid: UInt32
    err: Int32
class JET_COLUMNDEF(Structure):
    cbStruct: UInt32
    columnid: UInt32
    coltyp: UInt32
    wCountry: UInt16
    langid: UInt16
    cp: UInt16
    wCollate: UInt16
    cbMax: UInt32
    grbit: UInt32
class JET_COLUMNLIST(Structure):
    cbStruct: UInt32
    tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID
    cRecord: UInt32
    columnidPresentationOrder: UInt32
    columnidcolumnname: UInt32
    columnidcolumnid: UInt32
    columnidcoltyp: UInt32
    columnidCountry: UInt32
    columnidLangid: UInt32
    columnidCp: UInt32
    columnidCollate: UInt32
    columnidcbMax: UInt32
    columnidgrbit: UInt32
    columnidDefault: UInt32
    columnidBaseTableName: UInt32
    columnidBaseColumnName: UInt32
    columnidDefinitionName: UInt32
if ARCH in 'X64,ARM64':
    class JET_COMMIT_ID(Structure):
        signLog: Windows.Win32.Storage.Jet.JET_SIGNATURE
        reserved: Int32
        commitId: Int64
if ARCH in 'X86':
    class JET_COMMIT_ID(Structure):
        signLog: Windows.Win32.Storage.Jet.JET_SIGNATURE
        reserved: Int32
        commitId: Int64
        _pack_ = 4
class JET_CONDITIONALCOLUMN_A(Structure):
    cbStruct: UInt32
    szColumnName: Windows.Win32.Foundation.PSTR
    grbit: UInt32
class JET_CONDITIONALCOLUMN_W(Structure):
    cbStruct: UInt32
    szColumnName: Windows.Win32.Foundation.PWSTR
    grbit: UInt32
class JET_CONVERT_A(Structure):
    szOldDll: Windows.Win32.Foundation.PSTR
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        fFlags: UInt32
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            _bitfield: UInt32
class JET_CONVERT_W(Structure):
    szOldDll: Windows.Win32.Foundation.PWSTR
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        fFlags: UInt32
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            _bitfield: UInt32
class JET_DBINFOMISC(Structure):
    ulVersion: UInt32
    ulUpdate: UInt32
    signDb: Windows.Win32.Storage.Jet.JET_SIGNATURE
    dbstate: UInt32
    lgposConsistent: Windows.Win32.Storage.Jet.JET_LGPOS
    logtimeConsistent: Windows.Win32.Storage.Jet.JET_LOGTIME
    logtimeAttach: Windows.Win32.Storage.Jet.JET_LOGTIME
    lgposAttach: Windows.Win32.Storage.Jet.JET_LGPOS
    logtimeDetach: Windows.Win32.Storage.Jet.JET_LOGTIME
    lgposDetach: Windows.Win32.Storage.Jet.JET_LGPOS
    signLog: Windows.Win32.Storage.Jet.JET_SIGNATURE
    bkinfoFullPrev: Windows.Win32.Storage.Jet.JET_BKINFO
    bkinfoIncPrev: Windows.Win32.Storage.Jet.JET_BKINFO
    bkinfoFullCur: Windows.Win32.Storage.Jet.JET_BKINFO
    fShadowingDisabled: UInt32
    fUpgradeDb: UInt32
    dwMajorVersion: UInt32
    dwMinorVersion: UInt32
    dwBuildNumber: UInt32
    lSPNumber: Int32
    cbPageSize: UInt32
class JET_DBINFOMISC2(Structure):
    ulVersion: UInt32
    ulUpdate: UInt32
    signDb: Windows.Win32.Storage.Jet.JET_SIGNATURE
    dbstate: UInt32
    lgposConsistent: Windows.Win32.Storage.Jet.JET_LGPOS
    logtimeConsistent: Windows.Win32.Storage.Jet.JET_LOGTIME
    logtimeAttach: Windows.Win32.Storage.Jet.JET_LOGTIME
    lgposAttach: Windows.Win32.Storage.Jet.JET_LGPOS
    logtimeDetach: Windows.Win32.Storage.Jet.JET_LOGTIME
    lgposDetach: Windows.Win32.Storage.Jet.JET_LGPOS
    signLog: Windows.Win32.Storage.Jet.JET_SIGNATURE
    bkinfoFullPrev: Windows.Win32.Storage.Jet.JET_BKINFO
    bkinfoIncPrev: Windows.Win32.Storage.Jet.JET_BKINFO
    bkinfoFullCur: Windows.Win32.Storage.Jet.JET_BKINFO
    fShadowingDisabled: UInt32
    fUpgradeDb: UInt32
    dwMajorVersion: UInt32
    dwMinorVersion: UInt32
    dwBuildNumber: UInt32
    lSPNumber: Int32
    cbPageSize: UInt32
    genMinRequired: UInt32
    genMaxRequired: UInt32
    logtimeGenMaxCreate: Windows.Win32.Storage.Jet.JET_LOGTIME
    ulRepairCount: UInt32
    logtimeRepair: Windows.Win32.Storage.Jet.JET_LOGTIME
    ulRepairCountOld: UInt32
    ulECCFixSuccess: UInt32
    logtimeECCFixSuccess: Windows.Win32.Storage.Jet.JET_LOGTIME
    ulECCFixSuccessOld: UInt32
    ulECCFixFail: UInt32
    logtimeECCFixFail: Windows.Win32.Storage.Jet.JET_LOGTIME
    ulECCFixFailOld: UInt32
    ulBadChecksum: UInt32
    logtimeBadChecksum: Windows.Win32.Storage.Jet.JET_LOGTIME
    ulBadChecksumOld: UInt32
class JET_DBINFOMISC3(Structure):
    ulVersion: UInt32
    ulUpdate: UInt32
    signDb: Windows.Win32.Storage.Jet.JET_SIGNATURE
    dbstate: UInt32
    lgposConsistent: Windows.Win32.Storage.Jet.JET_LGPOS
    logtimeConsistent: Windows.Win32.Storage.Jet.JET_LOGTIME
    logtimeAttach: Windows.Win32.Storage.Jet.JET_LOGTIME
    lgposAttach: Windows.Win32.Storage.Jet.JET_LGPOS
    logtimeDetach: Windows.Win32.Storage.Jet.JET_LOGTIME
    lgposDetach: Windows.Win32.Storage.Jet.JET_LGPOS
    signLog: Windows.Win32.Storage.Jet.JET_SIGNATURE
    bkinfoFullPrev: Windows.Win32.Storage.Jet.JET_BKINFO
    bkinfoIncPrev: Windows.Win32.Storage.Jet.JET_BKINFO
    bkinfoFullCur: Windows.Win32.Storage.Jet.JET_BKINFO
    fShadowingDisabled: UInt32
    fUpgradeDb: UInt32
    dwMajorVersion: UInt32
    dwMinorVersion: UInt32
    dwBuildNumber: UInt32
    lSPNumber: Int32
    cbPageSize: UInt32
    genMinRequired: UInt32
    genMaxRequired: UInt32
    logtimeGenMaxCreate: Windows.Win32.Storage.Jet.JET_LOGTIME
    ulRepairCount: UInt32
    logtimeRepair: Windows.Win32.Storage.Jet.JET_LOGTIME
    ulRepairCountOld: UInt32
    ulECCFixSuccess: UInt32
    logtimeECCFixSuccess: Windows.Win32.Storage.Jet.JET_LOGTIME
    ulECCFixSuccessOld: UInt32
    ulECCFixFail: UInt32
    logtimeECCFixFail: Windows.Win32.Storage.Jet.JET_LOGTIME
    ulECCFixFailOld: UInt32
    ulBadChecksum: UInt32
    logtimeBadChecksum: Windows.Win32.Storage.Jet.JET_LOGTIME
    ulBadChecksumOld: UInt32
    genCommitted: UInt32
class JET_DBINFOMISC4(Structure):
    ulVersion: UInt32
    ulUpdate: UInt32
    signDb: Windows.Win32.Storage.Jet.JET_SIGNATURE
    dbstate: UInt32
    lgposConsistent: Windows.Win32.Storage.Jet.JET_LGPOS
    logtimeConsistent: Windows.Win32.Storage.Jet.JET_LOGTIME
    logtimeAttach: Windows.Win32.Storage.Jet.JET_LOGTIME
    lgposAttach: Windows.Win32.Storage.Jet.JET_LGPOS
    logtimeDetach: Windows.Win32.Storage.Jet.JET_LOGTIME
    lgposDetach: Windows.Win32.Storage.Jet.JET_LGPOS
    signLog: Windows.Win32.Storage.Jet.JET_SIGNATURE
    bkinfoFullPrev: Windows.Win32.Storage.Jet.JET_BKINFO
    bkinfoIncPrev: Windows.Win32.Storage.Jet.JET_BKINFO
    bkinfoFullCur: Windows.Win32.Storage.Jet.JET_BKINFO
    fShadowingDisabled: UInt32
    fUpgradeDb: UInt32
    dwMajorVersion: UInt32
    dwMinorVersion: UInt32
    dwBuildNumber: UInt32
    lSPNumber: Int32
    cbPageSize: UInt32
    genMinRequired: UInt32
    genMaxRequired: UInt32
    logtimeGenMaxCreate: Windows.Win32.Storage.Jet.JET_LOGTIME
    ulRepairCount: UInt32
    logtimeRepair: Windows.Win32.Storage.Jet.JET_LOGTIME
    ulRepairCountOld: UInt32
    ulECCFixSuccess: UInt32
    logtimeECCFixSuccess: Windows.Win32.Storage.Jet.JET_LOGTIME
    ulECCFixSuccessOld: UInt32
    ulECCFixFail: UInt32
    logtimeECCFixFail: Windows.Win32.Storage.Jet.JET_LOGTIME
    ulECCFixFailOld: UInt32
    ulBadChecksum: UInt32
    logtimeBadChecksum: Windows.Win32.Storage.Jet.JET_LOGTIME
    ulBadChecksumOld: UInt32
    genCommitted: UInt32
    bkinfoCopyPrev: Windows.Win32.Storage.Jet.JET_BKINFO
    bkinfoDiffPrev: Windows.Win32.Storage.Jet.JET_BKINFO
class JET_DBINFOUPGRADE(Structure):
    cbStruct: UInt32
    cbFilesizeLow: UInt32
    cbFilesizeHigh: UInt32
    cbFreeSpaceRequiredLow: UInt32
    cbFreeSpaceRequiredHigh: UInt32
    csecToUpgrade: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        ulFlags: UInt32
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            _bitfield: UInt32
class JET_ENUMCOLUMN(Structure):
    columnid: UInt32
    err: Int32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Anonymous1: _Anonymous1_e__Struct
        Anonymous2: _Anonymous2_e__Struct
        class _Anonymous1_e__Struct(Structure):
            cEnumColumnValue: UInt32
            rgEnumColumnValue: POINTER(Windows.Win32.Storage.Jet.JET_ENUMCOLUMNVALUE_head)
        class _Anonymous2_e__Struct(Structure):
            cbData: UInt32
            pvData: c_void_p
class JET_ENUMCOLUMNID(Structure):
    columnid: UInt32
    ctagSequence: UInt32
    rgtagSequence: POINTER(UInt32)
class JET_ENUMCOLUMNVALUE(Structure):
    itagSequence: UInt32
    err: Int32
    cbData: UInt32
    pvData: c_void_p
JET_ERRCAT = Int32
JET_errcatUnknown: JET_ERRCAT = 0
JET_errcatError: JET_ERRCAT = 1
JET_errcatOperation: JET_ERRCAT = 2
JET_errcatFatal: JET_ERRCAT = 3
JET_errcatIO: JET_ERRCAT = 4
JET_errcatResource: JET_ERRCAT = 5
JET_errcatMemory: JET_ERRCAT = 6
JET_errcatQuota: JET_ERRCAT = 7
JET_errcatDisk: JET_ERRCAT = 8
JET_errcatData: JET_ERRCAT = 9
JET_errcatCorruption: JET_ERRCAT = 10
JET_errcatInconsistent: JET_ERRCAT = 11
JET_errcatFragmentation: JET_ERRCAT = 12
JET_errcatApi: JET_ERRCAT = 13
JET_errcatUsage: JET_ERRCAT = 14
JET_errcatState: JET_ERRCAT = 15
JET_errcatObsolete: JET_ERRCAT = 16
JET_errcatMax: JET_ERRCAT = 17
class JET_ERRINFOBASIC_W(Structure):
    cbStruct: UInt32
    errValue: Int32
    errcatMostSpecific: Windows.Win32.Storage.Jet.JET_ERRCAT
    rgCategoricalHierarchy: Byte * 8
    lSourceLine: UInt32
    rgszSourceFile: Char * 64
JET_INDEXCHECKING = Int32
JET_IndexCheckingOff: JET_INDEXCHECKING = 0
JET_IndexCheckingOn: JET_INDEXCHECKING = 1
JET_IndexCheckingDeferToOpenTable: JET_INDEXCHECKING = 2
JET_IndexCheckingMax: JET_INDEXCHECKING = 3
class JET_INDEXCREATE2_A(Structure):
    cbStruct: UInt32
    szIndexName: Windows.Win32.Foundation.PSTR
    szKey: Windows.Win32.Foundation.PSTR
    cbKey: UInt32
    grbit: UInt32
    ulDensity: UInt32
    Anonymous1: _Anonymous1_e__Union
    Anonymous2: _Anonymous2_e__Union
    rgconditionalcolumn: POINTER(Windows.Win32.Storage.Jet.JET_CONDITIONALCOLUMN_A_head)
    cConditionalColumn: UInt32
    err: Int32
    cbKeyMost: UInt32
    pSpacehints: POINTER(Windows.Win32.Storage.Jet.JET_SPACEHINTS_head)
    class _Anonymous1_e__Union(Union):
        lcid: UInt32
        pidxunicode: POINTER(Windows.Win32.Storage.Jet.JET_UNICODEINDEX_head)
    class _Anonymous2_e__Union(Union):
        cbVarSegMac: UInt32
        ptuplelimits: POINTER(Windows.Win32.Storage.Jet.JET_TUPLELIMITS_head)
class JET_INDEXCREATE2_W(Structure):
    cbStruct: UInt32
    szIndexName: Windows.Win32.Foundation.PWSTR
    szKey: Windows.Win32.Foundation.PWSTR
    cbKey: UInt32
    grbit: UInt32
    ulDensity: UInt32
    Anonymous1: _Anonymous1_e__Union
    Anonymous2: _Anonymous2_e__Union
    rgconditionalcolumn: POINTER(Windows.Win32.Storage.Jet.JET_CONDITIONALCOLUMN_W_head)
    cConditionalColumn: UInt32
    err: Int32
    cbKeyMost: UInt32
    pSpacehints: POINTER(Windows.Win32.Storage.Jet.JET_SPACEHINTS_head)
    class _Anonymous1_e__Union(Union):
        lcid: UInt32
        pidxunicode: POINTER(Windows.Win32.Storage.Jet.JET_UNICODEINDEX_head)
    class _Anonymous2_e__Union(Union):
        cbVarSegMac: UInt32
        ptuplelimits: POINTER(Windows.Win32.Storage.Jet.JET_TUPLELIMITS_head)
class JET_INDEXCREATE3_A(Structure):
    cbStruct: UInt32
    szIndexName: Windows.Win32.Foundation.PSTR
    szKey: Windows.Win32.Foundation.PSTR
    cbKey: UInt32
    grbit: UInt32
    ulDensity: UInt32
    pidxunicode: POINTER(Windows.Win32.Storage.Jet.JET_UNICODEINDEX2_head)
    Anonymous: _Anonymous_e__Union
    rgconditionalcolumn: POINTER(Windows.Win32.Storage.Jet.JET_CONDITIONALCOLUMN_A_head)
    cConditionalColumn: UInt32
    err: Int32
    cbKeyMost: UInt32
    pSpacehints: POINTER(Windows.Win32.Storage.Jet.JET_SPACEHINTS_head)
    class _Anonymous_e__Union(Union):
        cbVarSegMac: UInt32
        ptuplelimits: POINTER(Windows.Win32.Storage.Jet.JET_TUPLELIMITS_head)
class JET_INDEXCREATE3_W(Structure):
    cbStruct: UInt32
    szIndexName: Windows.Win32.Foundation.PWSTR
    szKey: Windows.Win32.Foundation.PWSTR
    cbKey: UInt32
    grbit: UInt32
    ulDensity: UInt32
    pidxunicode: POINTER(Windows.Win32.Storage.Jet.JET_UNICODEINDEX2_head)
    Anonymous: _Anonymous_e__Union
    rgconditionalcolumn: POINTER(Windows.Win32.Storage.Jet.JET_CONDITIONALCOLUMN_W_head)
    cConditionalColumn: UInt32
    err: Int32
    cbKeyMost: UInt32
    pSpacehints: POINTER(Windows.Win32.Storage.Jet.JET_SPACEHINTS_head)
    class _Anonymous_e__Union(Union):
        cbVarSegMac: UInt32
        ptuplelimits: POINTER(Windows.Win32.Storage.Jet.JET_TUPLELIMITS_head)
class JET_INDEXCREATE_A(Structure):
    cbStruct: UInt32
    szIndexName: Windows.Win32.Foundation.PSTR
    szKey: Windows.Win32.Foundation.PSTR
    cbKey: UInt32
    grbit: UInt32
    ulDensity: UInt32
    Anonymous1: _Anonymous1_e__Union
    Anonymous2: _Anonymous2_e__Union
    rgconditionalcolumn: POINTER(Windows.Win32.Storage.Jet.JET_CONDITIONALCOLUMN_A_head)
    cConditionalColumn: UInt32
    err: Int32
    cbKeyMost: UInt32
    class _Anonymous1_e__Union(Union):
        lcid: UInt32
        pidxunicode: POINTER(Windows.Win32.Storage.Jet.JET_UNICODEINDEX_head)
    class _Anonymous2_e__Union(Union):
        cbVarSegMac: UInt32
        ptuplelimits: POINTER(Windows.Win32.Storage.Jet.JET_TUPLELIMITS_head)
class JET_INDEXCREATE_W(Structure):
    cbStruct: UInt32
    szIndexName: Windows.Win32.Foundation.PWSTR
    szKey: Windows.Win32.Foundation.PWSTR
    cbKey: UInt32
    grbit: UInt32
    ulDensity: UInt32
    Anonymous1: _Anonymous1_e__Union
    Anonymous2: _Anonymous2_e__Union
    rgconditionalcolumn: POINTER(Windows.Win32.Storage.Jet.JET_CONDITIONALCOLUMN_W_head)
    cConditionalColumn: UInt32
    err: Int32
    cbKeyMost: UInt32
    class _Anonymous1_e__Union(Union):
        lcid: UInt32
        pidxunicode: POINTER(Windows.Win32.Storage.Jet.JET_UNICODEINDEX_head)
    class _Anonymous2_e__Union(Union):
        cbVarSegMac: UInt32
        ptuplelimits: POINTER(Windows.Win32.Storage.Jet.JET_TUPLELIMITS_head)
if ARCH in 'X64,ARM64':
    class JET_INDEXID(Structure):
        cbStruct: UInt32
        rgbIndexId: Byte * 16
if ARCH in 'X86':
    class JET_INDEXID(Structure):
        cbStruct: UInt32
        rgbIndexId: Byte * 12
class JET_INDEXLIST(Structure):
    cbStruct: UInt32
    tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID
    cRecord: UInt32
    columnidindexname: UInt32
    columnidgrbitIndex: UInt32
    columnidcKey: UInt32
    columnidcEntry: UInt32
    columnidcPage: UInt32
    columnidcColumn: UInt32
    columnidiColumn: UInt32
    columnidcolumnid: UInt32
    columnidcoltyp: UInt32
    columnidCountry: UInt32
    columnidLangid: UInt32
    columnidCp: UInt32
    columnidCollate: UInt32
    columnidgrbitColumn: UInt32
    columnidcolumnname: UInt32
    columnidLCMapFlags: UInt32
class JET_INDEXRANGE(Structure):
    cbStruct: UInt32
    tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID
    grbit: UInt32
class JET_INDEX_COLUMN(Structure):
    columnid: UInt32
    relop: Windows.Win32.Storage.Jet.JET_RELOP
    pv: c_void_p
    cb: UInt32
    grbit: UInt32
class JET_INDEX_RANGE(Structure):
    rgStartColumns: POINTER(Windows.Win32.Storage.Jet.JET_INDEX_COLUMN_head)
    cStartColumns: UInt32
    rgEndColumns: POINTER(Windows.Win32.Storage.Jet.JET_INDEX_COLUMN_head)
    cEndColumns: UInt32
class JET_INSTANCE_INFO_A(Structure):
    hInstanceId: Windows.Win32.Storage.StructuredStorage.JET_INSTANCE
    szInstanceName: Windows.Win32.Foundation.PSTR
    cDatabases: Windows.Win32.Storage.StructuredStorage.JET_API_PTR
    szDatabaseFileName: POINTER(POINTER(SByte))
    szDatabaseDisplayName: POINTER(POINTER(SByte))
    szDatabaseSLVFileName_Obsolete: POINTER(POINTER(SByte))
class JET_INSTANCE_INFO_W(Structure):
    hInstanceId: Windows.Win32.Storage.StructuredStorage.JET_INSTANCE
    szInstanceName: Windows.Win32.Foundation.PWSTR
    cDatabases: Windows.Win32.Storage.StructuredStorage.JET_API_PTR
    szDatabaseFileName: POINTER(POINTER(UInt16))
    szDatabaseDisplayName: POINTER(POINTER(UInt16))
    szDatabaseSLVFileName_Obsolete: POINTER(POINTER(UInt16))
class JET_LGPOS(Structure):
    ib: UInt16
    isec: UInt16
    lGeneration: Int32
    _pack_ = 1
class JET_LOGINFO_A(Structure):
    cbSize: UInt32
    ulGenLow: UInt32
    ulGenHigh: UInt32
    szBaseName: Windows.Win32.Foundation.CHAR * 4
class JET_LOGINFO_W(Structure):
    cbSize: UInt32
    ulGenLow: UInt32
    ulGenHigh: UInt32
    szBaseName: Char * 4
class JET_LOGTIME(Structure):
    bSeconds: Windows.Win32.Foundation.CHAR
    bMinutes: Windows.Win32.Foundation.CHAR
    bHours: Windows.Win32.Foundation.CHAR
    bDay: Windows.Win32.Foundation.CHAR
    bMonth: Windows.Win32.Foundation.CHAR
    bYear: Windows.Win32.Foundation.CHAR
    Anonymous1: _Anonymous1_e__Union
    Anonymous2: _Anonymous2_e__Union
    class _Anonymous1_e__Union(Union):
        bFiller1: Windows.Win32.Foundation.CHAR
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            _bitfield: Byte
    class _Anonymous2_e__Union(Union):
        bFiller2: Windows.Win32.Foundation.CHAR
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            _bitfield: Byte
JET_LS = UIntPtr
if ARCH in 'X64,ARM64':
    class JET_OBJECTINFO(Structure):
        cbStruct: UInt32
        objtyp: UInt32
        dtCreate: Double
        dtUpdate: Double
        grbit: UInt32
        flags: UInt32
        cRecord: UInt32
        cPage: UInt32
if ARCH in 'X86':
    class JET_OBJECTINFO(Structure):
        cbStruct: UInt32
        objtyp: UInt32
        dtCreate: Double
        dtUpdate: Double
        grbit: UInt32
        flags: UInt32
        cRecord: UInt32
        cPage: UInt32
        _pack_ = 4
class JET_OBJECTLIST(Structure):
    cbStruct: UInt32
    tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID
    cRecord: UInt32
    columnidcontainername: UInt32
    columnidobjectname: UInt32
    columnidobjtyp: UInt32
    columniddtCreate: UInt32
    columniddtUpdate: UInt32
    columnidgrbit: UInt32
    columnidflags: UInt32
    columnidcRecord: UInt32
    columnidcPage: UInt32
class JET_OPENTEMPORARYTABLE(Structure):
    cbStruct: UInt32
    prgcolumndef: POINTER(Windows.Win32.Storage.Jet.JET_COLUMNDEF_head)
    ccolumn: UInt32
    pidxunicode: POINTER(Windows.Win32.Storage.Jet.JET_UNICODEINDEX_head)
    grbit: UInt32
    prgcolumnid: POINTER(UInt32)
    cbKeyMost: UInt32
    cbVarSegMac: UInt32
    tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID
class JET_OPENTEMPORARYTABLE2(Structure):
    cbStruct: UInt32
    prgcolumndef: POINTER(Windows.Win32.Storage.Jet.JET_COLUMNDEF_head)
    ccolumn: UInt32
    pidxunicode: POINTER(Windows.Win32.Storage.Jet.JET_UNICODEINDEX2_head)
    grbit: UInt32
    prgcolumnid: POINTER(UInt32)
    cbKeyMost: UInt32
    cbVarSegMac: UInt32
    tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID
class JET_OPERATIONCONTEXT(Structure):
    ulUserID: UInt32
    nOperationID: Byte
    nOperationType: Byte
    nClientType: Byte
    fFlags: Byte
JET_OSSNAPID = UIntPtr
@winfunctype_pointer
def JET_PFNDURABLECOMMITCALLBACK(instance: Windows.Win32.Storage.StructuredStorage.JET_INSTANCE, pCommitIdSeen: POINTER(Windows.Win32.Storage.Jet.JET_COMMIT_ID_head), grbit: UInt32) -> Int32: ...
@winfunctype_pointer
def JET_PFNREALLOC(pvContext: c_void_p, pv: c_void_p, cb: UInt32) -> c_void_p: ...
@winfunctype_pointer
def JET_PFNSTATUS(sesid: Windows.Win32.Storage.StructuredStorage.JET_SESID, snp: UInt32, snt: UInt32, pv: c_void_p) -> Int32: ...
if ARCH in 'X64,ARM64':
    class JET_RBSINFOMISC(Structure):
        lRBSGeneration: Int32
        logtimeCreate: Windows.Win32.Storage.Jet.JET_LOGTIME
        logtimeCreatePrevRBS: Windows.Win32.Storage.Jet.JET_LOGTIME
        ulMajor: UInt32
        ulMinor: UInt32
        cbLogicalFileSize: UInt64
if ARCH in 'X86':
    class JET_RBSINFOMISC(Structure):
        lRBSGeneration: Int32
        logtimeCreate: Windows.Win32.Storage.Jet.JET_LOGTIME
        logtimeCreatePrevRBS: Windows.Win32.Storage.Jet.JET_LOGTIME
        ulMajor: UInt32
        ulMinor: UInt32
        cbLogicalFileSize: UInt64
        _pack_ = 4
if ARCH in 'X64,ARM64':
    class JET_RBSREVERTINFOMISC(Structure):
        lGenMinRevertStart: Int32
        lGenMaxRevertStart: Int32
        lGenMinRevertEnd: Int32
        lGenMaxRevertEnd: Int32
        logtimeRevertFrom: Windows.Win32.Storage.Jet.JET_LOGTIME
        cSecRevert: UInt64
        cPagesReverted: UInt64
if ARCH in 'X86':
    class JET_RBSREVERTINFOMISC(Structure):
        lGenMinRevertStart: Int32
        lGenMaxRevertStart: Int32
        lGenMinRevertEnd: Int32
        lGenMaxRevertEnd: Int32
        logtimeRevertFrom: Windows.Win32.Storage.Jet.JET_LOGTIME
        cSecRevert: UInt64
        cPagesReverted: UInt64
        _pack_ = 4
class JET_RECORDLIST(Structure):
    cbStruct: UInt32
    tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID
    cRecord: UInt32
    columnidBookmark: UInt32
class JET_RECPOS(Structure):
    cbStruct: UInt32
    centriesLT: UInt32
    centriesInRange: UInt32
    centriesTotal: UInt32
if ARCH in 'X64,ARM64':
    class JET_RECSIZE(Structure):
        cbData: UInt64
        cbLongValueData: UInt64
        cbOverhead: UInt64
        cbLongValueOverhead: UInt64
        cNonTaggedColumns: UInt64
        cTaggedColumns: UInt64
        cLongValues: UInt64
        cMultiValues: UInt64
if ARCH in 'X86':
    class JET_RECSIZE(Structure):
        cbData: UInt64
        cbLongValueData: UInt64
        cbOverhead: UInt64
        cbLongValueOverhead: UInt64
        cNonTaggedColumns: UInt64
        cTaggedColumns: UInt64
        cLongValues: UInt64
        cMultiValues: UInt64
        _pack_ = 4
if ARCH in 'X64,ARM64':
    class JET_RECSIZE2(Structure):
        cbData: UInt64
        cbLongValueData: UInt64
        cbOverhead: UInt64
        cbLongValueOverhead: UInt64
        cNonTaggedColumns: UInt64
        cTaggedColumns: UInt64
        cLongValues: UInt64
        cMultiValues: UInt64
        cCompressedColumns: UInt64
        cbDataCompressed: UInt64
        cbLongValueDataCompressed: UInt64
if ARCH in 'X86':
    class JET_RECSIZE2(Structure):
        cbData: UInt64
        cbLongValueData: UInt64
        cbOverhead: UInt64
        cbLongValueOverhead: UInt64
        cNonTaggedColumns: UInt64
        cTaggedColumns: UInt64
        cLongValues: UInt64
        cMultiValues: UInt64
        cCompressedColumns: UInt64
        cbDataCompressed: UInt64
        cbLongValueDataCompressed: UInt64
        _pack_ = 4
JET_RELOP = Int32
JET_relopEquals: JET_RELOP = 0
JET_relopPrefixEquals: JET_RELOP = 1
JET_relopNotEquals: JET_RELOP = 2
JET_relopLessThanOrEqual: JET_RELOP = 3
JET_relopLessThan: JET_RELOP = 4
JET_relopGreaterThanOrEqual: JET_RELOP = 5
JET_relopGreaterThan: JET_RELOP = 6
JET_relopBitmaskEqualsZero: JET_RELOP = 7
JET_relopBitmaskNotEqualsZero: JET_RELOP = 8
class JET_RETINFO(Structure):
    cbStruct: UInt32
    ibLongValue: UInt32
    itagSequence: UInt32
    columnidNextTagged: UInt32
class JET_RETRIEVECOLUMN(Structure):
    columnid: UInt32
    pvData: c_void_p
    cbData: UInt32
    cbActual: UInt32
    grbit: UInt32
    ibLongValue: UInt32
    itagSequence: UInt32
    columnidNextTagged: UInt32
    err: Int32
class JET_RSTINFO_A(Structure):
    cbStruct: UInt32
    rgrstmap: POINTER(Windows.Win32.Storage.Jet.JET_RSTMAP_A_head)
    crstmap: Int32
    lgposStop: Windows.Win32.Storage.Jet.JET_LGPOS
    logtimeStop: Windows.Win32.Storage.Jet.JET_LOGTIME
    pfnStatus: Windows.Win32.Storage.Jet.JET_PFNSTATUS
class JET_RSTINFO_W(Structure):
    cbStruct: UInt32
    rgrstmap: POINTER(Windows.Win32.Storage.Jet.JET_RSTMAP_W_head)
    crstmap: Int32
    lgposStop: Windows.Win32.Storage.Jet.JET_LGPOS
    logtimeStop: Windows.Win32.Storage.Jet.JET_LOGTIME
    pfnStatus: Windows.Win32.Storage.Jet.JET_PFNSTATUS
class JET_RSTMAP_A(Structure):
    szDatabaseName: Windows.Win32.Foundation.PSTR
    szNewDatabaseName: Windows.Win32.Foundation.PSTR
class JET_RSTMAP_W(Structure):
    szDatabaseName: Windows.Win32.Foundation.PWSTR
    szNewDatabaseName: Windows.Win32.Foundation.PWSTR
class JET_SETCOLUMN(Structure):
    columnid: UInt32
    pvData: c_void_p
    cbData: UInt32
    grbit: UInt32
    ibLongValue: UInt32
    itagSequence: UInt32
    err: Int32
class JET_SETINFO(Structure):
    cbStruct: UInt32
    ibLongValue: UInt32
    itagSequence: UInt32
class JET_SETSYSPARAM_A(Structure):
    paramid: UInt32
    lParam: Windows.Win32.Storage.StructuredStorage.JET_API_PTR
    sz: Windows.Win32.Foundation.PSTR
    err: Int32
class JET_SETSYSPARAM_W(Structure):
    paramid: UInt32
    lParam: Windows.Win32.Storage.StructuredStorage.JET_API_PTR
    sz: Windows.Win32.Foundation.PWSTR
    err: Int32
class JET_SIGNATURE(Structure):
    ulRandom: UInt32
    logtimeCreate: Windows.Win32.Storage.Jet.JET_LOGTIME
    szComputerName: Windows.Win32.Foundation.CHAR * 16
    _pack_ = 1
class JET_SNPROG(Structure):
    cbStruct: UInt32
    cunitDone: UInt32
    cunitTotal: UInt32
class JET_SPACEHINTS(Structure):
    cbStruct: UInt32
    ulInitialDensity: UInt32
    cbInitial: UInt32
    grbit: UInt32
    ulMaintDensity: UInt32
    ulGrowth: UInt32
    cbMinExtent: UInt32
    cbMaxExtent: UInt32
class JET_TABLECREATE2_A(Structure):
    cbStruct: UInt32
    szTableName: Windows.Win32.Foundation.PSTR
    szTemplateTableName: Windows.Win32.Foundation.PSTR
    ulPages: UInt32
    ulDensity: UInt32
    rgcolumncreate: POINTER(Windows.Win32.Storage.Jet.JET_COLUMNCREATE_A_head)
    cColumns: UInt32
    rgindexcreate: POINTER(Windows.Win32.Storage.Jet.JET_INDEXCREATE_A_head)
    cIndexes: UInt32
    szCallback: Windows.Win32.Foundation.PSTR
    cbtyp: UInt32
    grbit: UInt32
    tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID
    cCreated: UInt32
class JET_TABLECREATE2_W(Structure):
    cbStruct: UInt32
    szTableName: Windows.Win32.Foundation.PWSTR
    szTemplateTableName: Windows.Win32.Foundation.PWSTR
    ulPages: UInt32
    ulDensity: UInt32
    rgcolumncreate: POINTER(Windows.Win32.Storage.Jet.JET_COLUMNCREATE_W_head)
    cColumns: UInt32
    rgindexcreate: POINTER(Windows.Win32.Storage.Jet.JET_INDEXCREATE_W_head)
    cIndexes: UInt32
    szCallback: Windows.Win32.Foundation.PWSTR
    cbtyp: UInt32
    grbit: UInt32
    tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID
    cCreated: UInt32
class JET_TABLECREATE3_A(Structure):
    cbStruct: UInt32
    szTableName: Windows.Win32.Foundation.PSTR
    szTemplateTableName: Windows.Win32.Foundation.PSTR
    ulPages: UInt32
    ulDensity: UInt32
    rgcolumncreate: POINTER(Windows.Win32.Storage.Jet.JET_COLUMNCREATE_A_head)
    cColumns: UInt32
    rgindexcreate: POINTER(Windows.Win32.Storage.Jet.JET_INDEXCREATE2_A_head)
    cIndexes: UInt32
    szCallback: Windows.Win32.Foundation.PSTR
    cbtyp: UInt32
    grbit: UInt32
    pSeqSpacehints: POINTER(Windows.Win32.Storage.Jet.JET_SPACEHINTS_head)
    pLVSpacehints: POINTER(Windows.Win32.Storage.Jet.JET_SPACEHINTS_head)
    cbSeparateLV: UInt32
    tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID
    cCreated: UInt32
class JET_TABLECREATE3_W(Structure):
    cbStruct: UInt32
    szTableName: Windows.Win32.Foundation.PWSTR
    szTemplateTableName: Windows.Win32.Foundation.PWSTR
    ulPages: UInt32
    ulDensity: UInt32
    rgcolumncreate: POINTER(Windows.Win32.Storage.Jet.JET_COLUMNCREATE_W_head)
    cColumns: UInt32
    rgindexcreate: POINTER(Windows.Win32.Storage.Jet.JET_INDEXCREATE2_W_head)
    cIndexes: UInt32
    szCallback: Windows.Win32.Foundation.PWSTR
    cbtyp: UInt32
    grbit: UInt32
    pSeqSpacehints: POINTER(Windows.Win32.Storage.Jet.JET_SPACEHINTS_head)
    pLVSpacehints: POINTER(Windows.Win32.Storage.Jet.JET_SPACEHINTS_head)
    cbSeparateLV: UInt32
    tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID
    cCreated: UInt32
class JET_TABLECREATE4_A(Structure):
    cbStruct: UInt32
    szTableName: Windows.Win32.Foundation.PSTR
    szTemplateTableName: Windows.Win32.Foundation.PSTR
    ulPages: UInt32
    ulDensity: UInt32
    rgcolumncreate: POINTER(Windows.Win32.Storage.Jet.JET_COLUMNCREATE_A_head)
    cColumns: UInt32
    rgindexcreate: POINTER(Windows.Win32.Storage.Jet.JET_INDEXCREATE3_A_head)
    cIndexes: UInt32
    szCallback: Windows.Win32.Foundation.PSTR
    cbtyp: UInt32
    grbit: UInt32
    pSeqSpacehints: POINTER(Windows.Win32.Storage.Jet.JET_SPACEHINTS_head)
    pLVSpacehints: POINTER(Windows.Win32.Storage.Jet.JET_SPACEHINTS_head)
    cbSeparateLV: UInt32
    tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID
    cCreated: UInt32
class JET_TABLECREATE4_W(Structure):
    cbStruct: UInt32
    szTableName: Windows.Win32.Foundation.PWSTR
    szTemplateTableName: Windows.Win32.Foundation.PWSTR
    ulPages: UInt32
    ulDensity: UInt32
    rgcolumncreate: POINTER(Windows.Win32.Storage.Jet.JET_COLUMNCREATE_W_head)
    cColumns: UInt32
    rgindexcreate: POINTER(Windows.Win32.Storage.Jet.JET_INDEXCREATE3_W_head)
    cIndexes: UInt32
    szCallback: Windows.Win32.Foundation.PWSTR
    cbtyp: UInt32
    grbit: UInt32
    pSeqSpacehints: POINTER(Windows.Win32.Storage.Jet.JET_SPACEHINTS_head)
    pLVSpacehints: POINTER(Windows.Win32.Storage.Jet.JET_SPACEHINTS_head)
    cbSeparateLV: UInt32
    tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID
    cCreated: UInt32
class JET_TABLECREATE_A(Structure):
    cbStruct: UInt32
    szTableName: Windows.Win32.Foundation.PSTR
    szTemplateTableName: Windows.Win32.Foundation.PSTR
    ulPages: UInt32
    ulDensity: UInt32
    rgcolumncreate: POINTER(Windows.Win32.Storage.Jet.JET_COLUMNCREATE_A_head)
    cColumns: UInt32
    rgindexcreate: POINTER(Windows.Win32.Storage.Jet.JET_INDEXCREATE_A_head)
    cIndexes: UInt32
    grbit: UInt32
    tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID
    cCreated: UInt32
class JET_TABLECREATE_W(Structure):
    cbStruct: UInt32
    szTableName: Windows.Win32.Foundation.PWSTR
    szTemplateTableName: Windows.Win32.Foundation.PWSTR
    ulPages: UInt32
    ulDensity: UInt32
    rgcolumncreate: POINTER(Windows.Win32.Storage.Jet.JET_COLUMNCREATE_W_head)
    cColumns: UInt32
    rgindexcreate: POINTER(Windows.Win32.Storage.Jet.JET_INDEXCREATE_W_head)
    cIndexes: UInt32
    grbit: UInt32
    tableid: Windows.Win32.Storage.StructuredStorage.JET_TABLEID
    cCreated: UInt32
class JET_THREADSTATS(Structure):
    cbStruct: UInt32
    cPageReferenced: UInt32
    cPageRead: UInt32
    cPagePreread: UInt32
    cPageDirtied: UInt32
    cPageRedirtied: UInt32
    cLogRecord: UInt32
    cbLogRecord: UInt32
if ARCH in 'X64,ARM64':
    class JET_THREADSTATS2(Structure):
        cbStruct: UInt32
        cPageReferenced: UInt32
        cPageRead: UInt32
        cPagePreread: UInt32
        cPageDirtied: UInt32
        cPageRedirtied: UInt32
        cLogRecord: UInt32
        cbLogRecord: UInt32
        cusecPageCacheMiss: UInt64
        cPageCacheMiss: UInt32
if ARCH in 'X86':
    class JET_THREADSTATS2(Structure):
        cbStruct: UInt32
        cPageReferenced: UInt32
        cPageRead: UInt32
        cPagePreread: UInt32
        cPageDirtied: UInt32
        cPageRedirtied: UInt32
        cLogRecord: UInt32
        cbLogRecord: UInt32
        cusecPageCacheMiss: UInt64
        cPageCacheMiss: UInt32
        _pack_ = 4
class JET_TUPLELIMITS(Structure):
    chLengthMin: UInt32
    chLengthMax: UInt32
    chToIndexMax: UInt32
    cchIncrement: UInt32
    ichStart: UInt32
class JET_UNICODEINDEX(Structure):
    lcid: UInt32
    dwMapFlags: UInt32
class JET_UNICODEINDEX2(Structure):
    szLocaleName: Windows.Win32.Foundation.PWSTR
    dwMapFlags: UInt32
class JET_USERDEFINEDDEFAULT_A(Structure):
    szCallback: Windows.Win32.Foundation.PSTR
    pbUserData: c_char_p_no
    cbUserData: UInt32
    szDependantColumns: Windows.Win32.Foundation.PSTR
class JET_USERDEFINEDDEFAULT_W(Structure):
    szCallback: Windows.Win32.Foundation.PWSTR
    pbUserData: c_char_p_no
    cbUserData: UInt32
    szDependantColumns: Windows.Win32.Foundation.PWSTR
make_head(_module, 'JET_BKINFO')
make_head(_module, 'JET_BKLOGTIME')
make_head(_module, 'JET_CALLBACK')
make_head(_module, 'JET_COLUMNBASE_A')
make_head(_module, 'JET_COLUMNBASE_W')
make_head(_module, 'JET_COLUMNCREATE_A')
make_head(_module, 'JET_COLUMNCREATE_W')
make_head(_module, 'JET_COLUMNDEF')
make_head(_module, 'JET_COLUMNLIST')
if ARCH in 'X64,ARM64':
    make_head(_module, 'JET_COMMIT_ID')
if ARCH in 'X86':
    make_head(_module, 'JET_COMMIT_ID')
make_head(_module, 'JET_CONDITIONALCOLUMN_A')
make_head(_module, 'JET_CONDITIONALCOLUMN_W')
make_head(_module, 'JET_CONVERT_A')
make_head(_module, 'JET_CONVERT_W')
make_head(_module, 'JET_DBINFOMISC')
make_head(_module, 'JET_DBINFOMISC2')
make_head(_module, 'JET_DBINFOMISC3')
make_head(_module, 'JET_DBINFOMISC4')
make_head(_module, 'JET_DBINFOUPGRADE')
make_head(_module, 'JET_ENUMCOLUMN')
make_head(_module, 'JET_ENUMCOLUMNID')
make_head(_module, 'JET_ENUMCOLUMNVALUE')
make_head(_module, 'JET_ERRINFOBASIC_W')
make_head(_module, 'JET_INDEXCREATE2_A')
make_head(_module, 'JET_INDEXCREATE2_W')
make_head(_module, 'JET_INDEXCREATE3_A')
make_head(_module, 'JET_INDEXCREATE3_W')
make_head(_module, 'JET_INDEXCREATE_A')
make_head(_module, 'JET_INDEXCREATE_W')
if ARCH in 'X64,ARM64':
    make_head(_module, 'JET_INDEXID')
if ARCH in 'X86':
    make_head(_module, 'JET_INDEXID')
make_head(_module, 'JET_INDEXLIST')
make_head(_module, 'JET_INDEXRANGE')
make_head(_module, 'JET_INDEX_COLUMN')
make_head(_module, 'JET_INDEX_RANGE')
make_head(_module, 'JET_INSTANCE_INFO_A')
make_head(_module, 'JET_INSTANCE_INFO_W')
make_head(_module, 'JET_LGPOS')
make_head(_module, 'JET_LOGINFO_A')
make_head(_module, 'JET_LOGINFO_W')
make_head(_module, 'JET_LOGTIME')
if ARCH in 'X64,ARM64':
    make_head(_module, 'JET_OBJECTINFO')
if ARCH in 'X86':
    make_head(_module, 'JET_OBJECTINFO')
make_head(_module, 'JET_OBJECTLIST')
make_head(_module, 'JET_OPENTEMPORARYTABLE')
make_head(_module, 'JET_OPENTEMPORARYTABLE2')
make_head(_module, 'JET_OPERATIONCONTEXT')
make_head(_module, 'JET_PFNDURABLECOMMITCALLBACK')
make_head(_module, 'JET_PFNREALLOC')
make_head(_module, 'JET_PFNSTATUS')
if ARCH in 'X64,ARM64':
    make_head(_module, 'JET_RBSINFOMISC')
if ARCH in 'X86':
    make_head(_module, 'JET_RBSINFOMISC')
if ARCH in 'X64,ARM64':
    make_head(_module, 'JET_RBSREVERTINFOMISC')
if ARCH in 'X86':
    make_head(_module, 'JET_RBSREVERTINFOMISC')
make_head(_module, 'JET_RECORDLIST')
make_head(_module, 'JET_RECPOS')
if ARCH in 'X64,ARM64':
    make_head(_module, 'JET_RECSIZE')
if ARCH in 'X86':
    make_head(_module, 'JET_RECSIZE')
if ARCH in 'X64,ARM64':
    make_head(_module, 'JET_RECSIZE2')
if ARCH in 'X86':
    make_head(_module, 'JET_RECSIZE2')
make_head(_module, 'JET_RETINFO')
make_head(_module, 'JET_RETRIEVECOLUMN')
make_head(_module, 'JET_RSTINFO_A')
make_head(_module, 'JET_RSTINFO_W')
make_head(_module, 'JET_RSTMAP_A')
make_head(_module, 'JET_RSTMAP_W')
make_head(_module, 'JET_SETCOLUMN')
make_head(_module, 'JET_SETINFO')
make_head(_module, 'JET_SETSYSPARAM_A')
make_head(_module, 'JET_SETSYSPARAM_W')
make_head(_module, 'JET_SIGNATURE')
make_head(_module, 'JET_SNPROG')
make_head(_module, 'JET_SPACEHINTS')
make_head(_module, 'JET_TABLECREATE2_A')
make_head(_module, 'JET_TABLECREATE2_W')
make_head(_module, 'JET_TABLECREATE3_A')
make_head(_module, 'JET_TABLECREATE3_W')
make_head(_module, 'JET_TABLECREATE4_A')
make_head(_module, 'JET_TABLECREATE4_W')
make_head(_module, 'JET_TABLECREATE_A')
make_head(_module, 'JET_TABLECREATE_W')
make_head(_module, 'JET_THREADSTATS')
if ARCH in 'X64,ARM64':
    make_head(_module, 'JET_THREADSTATS2')
if ARCH in 'X86':
    make_head(_module, 'JET_THREADSTATS2')
make_head(_module, 'JET_TUPLELIMITS')
make_head(_module, 'JET_UNICODEINDEX')
make_head(_module, 'JET_UNICODEINDEX2')
make_head(_module, 'JET_USERDEFINEDDEFAULT_A')
make_head(_module, 'JET_USERDEFINEDDEFAULT_W')
__all__ = [
    "JET_BASE_NAME_LENGTH",
    "JET_BKINFO",
    "JET_BKLOGTIME",
    "JET_CALLBACK",
    "JET_COLUMNBASE_A",
    "JET_COLUMNBASE_W",
    "JET_COLUMNCREATE_A",
    "JET_COLUMNCREATE_W",
    "JET_COLUMNDEF",
    "JET_COLUMNLIST",
    "JET_COMMIT_ID",
    "JET_CONDITIONALCOLUMN_A",
    "JET_CONDITIONALCOLUMN_W",
    "JET_CONVERT_A",
    "JET_CONVERT_W",
    "JET_ColInfoGrbitMinimalInfo",
    "JET_ColInfoGrbitNonDerivedColumnsOnly",
    "JET_ColInfoGrbitSortByColumnid",
    "JET_DBINFOMISC",
    "JET_DBINFOMISC2",
    "JET_DBINFOMISC3",
    "JET_DBINFOMISC4",
    "JET_DBINFOUPGRADE",
    "JET_DbInfoCollate",
    "JET_DbInfoConnect",
    "JET_DbInfoCountry",
    "JET_DbInfoCp",
    "JET_DbInfoDBInUse",
    "JET_DbInfoFileType",
    "JET_DbInfoFilename",
    "JET_DbInfoFilesize",
    "JET_DbInfoFilesizeOnDisk",
    "JET_DbInfoIsam",
    "JET_DbInfoLCID",
    "JET_DbInfoLangid",
    "JET_DbInfoMisc",
    "JET_DbInfoOptions",
    "JET_DbInfoPageSize",
    "JET_DbInfoSpaceAvailable",
    "JET_DbInfoSpaceOwned",
    "JET_DbInfoTransactions",
    "JET_DbInfoUpgrade",
    "JET_DbInfoVersion",
    "JET_ENUMCOLUMN",
    "JET_ENUMCOLUMNID",
    "JET_ENUMCOLUMNVALUE",
    "JET_ERRCAT",
    "JET_ERRINFOBASIC_W",
    "JET_EventLoggingDisable",
    "JET_EventLoggingLevelHigh",
    "JET_EventLoggingLevelLow",
    "JET_EventLoggingLevelMax",
    "JET_EventLoggingLevelMedium",
    "JET_EventLoggingLevelMin",
    "JET_ExceptionFailFast",
    "JET_ExceptionMsgBox",
    "JET_ExceptionNone",
    "JET_INDEXCHECKING",
    "JET_INDEXCREATE2_A",
    "JET_INDEXCREATE2_W",
    "JET_INDEXCREATE3_A",
    "JET_INDEXCREATE3_W",
    "JET_INDEXCREATE_A",
    "JET_INDEXCREATE_W",
    "JET_INDEXID",
    "JET_INDEXLIST",
    "JET_INDEXRANGE",
    "JET_INDEX_COLUMN",
    "JET_INDEX_RANGE",
    "JET_INSTANCE_INFO_A",
    "JET_INSTANCE_INFO_W",
    "JET_IOPriorityLow",
    "JET_IOPriorityNormal",
    "JET_IndexCheckingDeferToOpenTable",
    "JET_IndexCheckingMax",
    "JET_IndexCheckingOff",
    "JET_IndexCheckingOn",
    "JET_LGPOS",
    "JET_LOGINFO_A",
    "JET_LOGINFO_W",
    "JET_LOGTIME",
    "JET_LS",
    "JET_MAX_COMPUTERNAME_LENGTH",
    "JET_MoveFirst",
    "JET_MoveLast",
    "JET_MovePrevious",
    "JET_OBJECTINFO",
    "JET_OBJECTLIST",
    "JET_OPENTEMPORARYTABLE",
    "JET_OPENTEMPORARYTABLE2",
    "JET_OPERATIONCONTEXT",
    "JET_OSSNAPID",
    "JET_OnlineDefragAll",
    "JET_OnlineDefragAllOBSOLETE",
    "JET_OnlineDefragDatabases",
    "JET_OnlineDefragDisable",
    "JET_OnlineDefragSpaceTrees",
    "JET_PFNDURABLECOMMITCALLBACK",
    "JET_PFNREALLOC",
    "JET_PFNSTATUS",
    "JET_RBSINFOMISC",
    "JET_RBSREVERTINFOMISC",
    "JET_RECORDLIST",
    "JET_RECPOS",
    "JET_RECSIZE",
    "JET_RECSIZE2",
    "JET_RELOP",
    "JET_RETINFO",
    "JET_RETRIEVECOLUMN",
    "JET_RSTINFO_A",
    "JET_RSTINFO_W",
    "JET_RSTMAP_A",
    "JET_RSTMAP_W",
    "JET_SETCOLUMN",
    "JET_SETINFO",
    "JET_SETSYSPARAM_A",
    "JET_SETSYSPARAM_W",
    "JET_SIGNATURE",
    "JET_SNPROG",
    "JET_SPACEHINTS",
    "JET_TABLECREATE2_A",
    "JET_TABLECREATE2_W",
    "JET_TABLECREATE3_A",
    "JET_TABLECREATE3_W",
    "JET_TABLECREATE4_A",
    "JET_TABLECREATE4_W",
    "JET_TABLECREATE_A",
    "JET_TABLECREATE_W",
    "JET_THREADSTATS",
    "JET_THREADSTATS2",
    "JET_TUPLELIMITS",
    "JET_UNICODEINDEX",
    "JET_UNICODEINDEX2",
    "JET_USERDEFINEDDEFAULT_A",
    "JET_USERDEFINEDDEFAULT_W",
    "JET_VERSION",
    "JET_bitAbortSnapshot",
    "JET_bitAllDatabasesSnapshot",
    "JET_bitBackupAtomic",
    "JET_bitBackupEndAbort",
    "JET_bitBackupEndNormal",
    "JET_bitBackupIncremental",
    "JET_bitBackupSnapshot",
    "JET_bitBackupTruncateDone",
    "JET_bitBookmarkPermitVirtualCurrency",
    "JET_bitCheckUniqueness",
    "JET_bitColumnAutoincrement",
    "JET_bitColumnCompressed",
    "JET_bitColumnDeleteOnZero",
    "JET_bitColumnEscrowUpdate",
    "JET_bitColumnFinalize",
    "JET_bitColumnFixed",
    "JET_bitColumnMaybeNull",
    "JET_bitColumnMultiValued",
    "JET_bitColumnNotNULL",
    "JET_bitColumnTTDescending",
    "JET_bitColumnTTKey",
    "JET_bitColumnTagged",
    "JET_bitColumnUnversioned",
    "JET_bitColumnUpdatable",
    "JET_bitColumnUserDefinedDefault",
    "JET_bitColumnVersion",
    "JET_bitCommitLazyFlush",
    "JET_bitCompactRepair",
    "JET_bitCompactStats",
    "JET_bitConfigStoreReadControlDefault",
    "JET_bitConfigStoreReadControlDisableAll",
    "JET_bitConfigStoreReadControlInhibitRead",
    "JET_bitContinueAfterThaw",
    "JET_bitCopySnapshot",
    "JET_bitCreateHintAppendSequential",
    "JET_bitCreateHintHotpointSequential",
    "JET_bitDbDeleteCorruptIndexes",
    "JET_bitDbDeleteUnicodeIndexes",
    "JET_bitDbEnableBackgroundMaintenance",
    "JET_bitDbExclusive",
    "JET_bitDbOverwriteExisting",
    "JET_bitDbPurgeCacheOnAttach",
    "JET_bitDbReadOnly",
    "JET_bitDbRecoveryOff",
    "JET_bitDbShadowingOff",
    "JET_bitDbUpgrade",
    "JET_bitDefragmentAvailSpaceTreesOnly",
    "JET_bitDefragmentBTree",
    "JET_bitDefragmentBatchStart",
    "JET_bitDefragmentBatchStop",
    "JET_bitDefragmentNoPartialMerges",
    "JET_bitDeleteAllExistingLogs",
    "JET_bitDeleteColumnIgnoreTemplateColumns",
    "JET_bitDeleteHintTableSequential",
    "JET_bitDumpCacheIncludeCachedPages",
    "JET_bitDumpCacheIncludeCorruptedPages",
    "JET_bitDumpCacheIncludeDirtyPages",
    "JET_bitDumpCacheMaximum",
    "JET_bitDumpCacheMinimum",
    "JET_bitDumpCacheNoDecommit",
    "JET_bitDumpMaximum",
    "JET_bitDumpMinimum",
    "JET_bitDurableCommitCallbackLogUnavailable",
    "JET_bitESE98FileNames",
    "JET_bitEightDotThreeSoftCompat",
    "JET_bitEnumerateCompressOutput",
    "JET_bitEnumerateCopy",
    "JET_bitEnumerateIgnoreDefault",
    "JET_bitEnumerateIgnoreUserDefinedDefault",
    "JET_bitEnumerateInRecordOnly",
    "JET_bitEnumeratePresenceOnly",
    "JET_bitEnumerateTaggedOnly",
    "JET_bitEscrowNoRollback",
    "JET_bitExplicitPrepare",
    "JET_bitForceDetach",
    "JET_bitForceNewLog",
    "JET_bitFullColumnEndLimit",
    "JET_bitFullColumnStartLimit",
    "JET_bitHungIOEvent",
    "JET_bitIdleCompact",
    "JET_bitIdleFlushBuffers",
    "JET_bitIdleStatus",
    "JET_bitIncrementalSnapshot",
    "JET_bitIndexColumnMustBeNonNull",
    "JET_bitIndexColumnMustBeNull",
    "JET_bitIndexCrossProduct",
    "JET_bitIndexDisallowNull",
    "JET_bitIndexDisallowTruncation",
    "JET_bitIndexDotNetGuid",
    "JET_bitIndexEmpty",
    "JET_bitIndexIgnoreAnyNull",
    "JET_bitIndexIgnoreFirstNull",
    "JET_bitIndexIgnoreNull",
    "JET_bitIndexImmutableStructure",
    "JET_bitIndexKeyMost",
    "JET_bitIndexLazyFlush",
    "JET_bitIndexNestedTable",
    "JET_bitIndexPrimary",
    "JET_bitIndexSortNullsHigh",
    "JET_bitIndexTupleLimits",
    "JET_bitIndexTuples",
    "JET_bitIndexUnicode",
    "JET_bitIndexUnique",
    "JET_bitIndexUnversioned",
    "JET_bitKeepDbAttachedAtEndOfRecovery",
    "JET_bitKeyAscending",
    "JET_bitKeyDataZeroLength",
    "JET_bitKeyDescending",
    "JET_bitLSCursor",
    "JET_bitLSReset",
    "JET_bitLSTable",
    "JET_bitLogStreamMustExist",
    "JET_bitMoveFirst",
    "JET_bitMoveKeyNE",
    "JET_bitNewKey",
    "JET_bitNoMove",
    "JET_bitNormalizedKey",
    "JET_bitObjectSystem",
    "JET_bitObjectTableDerived",
    "JET_bitObjectTableFixedDDL",
    "JET_bitObjectTableNoFixedVarColumnsInDerivedTables",
    "JET_bitObjectTableTemplate",
    "JET_bitPartialColumnEndLimit",
    "JET_bitPartialColumnStartLimit",
    "JET_bitPrereadBackward",
    "JET_bitPrereadFirstPage",
    "JET_bitPrereadForward",
    "JET_bitPrereadNormalizedKey",
    "JET_bitRangeInclusive",
    "JET_bitRangeInstantDuration",
    "JET_bitRangeRemove",
    "JET_bitRangeUpperLimit",
    "JET_bitReadLock",
    "JET_bitRecordInIndex",
    "JET_bitRecordNotInIndex",
    "JET_bitRecordSizeInCopyBuffer",
    "JET_bitRecordSizeLocal",
    "JET_bitRecordSizeRunningTotal",
    "JET_bitRecoveryWithoutUndo",
    "JET_bitReplayIgnoreLostLogs",
    "JET_bitReplayIgnoreMissingDB",
    "JET_bitReplayMissingMapEntryDB",
    "JET_bitResizeDatabaseOnlyGrow",
    "JET_bitResizeDatabaseOnlyShrink",
    "JET_bitRetrieveCopy",
    "JET_bitRetrieveFromIndex",
    "JET_bitRetrieveFromPrimaryBookmark",
    "JET_bitRetrieveHintReserve1",
    "JET_bitRetrieveHintReserve2",
    "JET_bitRetrieveHintReserve3",
    "JET_bitRetrieveHintTableScanBackward",
    "JET_bitRetrieveHintTableScanForward",
    "JET_bitRetrieveIgnoreDefault",
    "JET_bitRetrieveNull",
    "JET_bitRetrieveTag",
    "JET_bitRetrieveTuple",
    "JET_bitRollbackAll",
    "JET_bitSeekEQ",
    "JET_bitSeekGE",
    "JET_bitSeekGT",
    "JET_bitSeekLE",
    "JET_bitSeekLT",
    "JET_bitSetAppendLV",
    "JET_bitSetCompressed",
    "JET_bitSetContiguousLV",
    "JET_bitSetIndexRange",
    "JET_bitSetIntrinsicLV",
    "JET_bitSetOverwriteLV",
    "JET_bitSetRevertToDefaultValue",
    "JET_bitSetSeparateLV",
    "JET_bitSetSizeLV",
    "JET_bitSetUncompressed",
    "JET_bitSetUniqueMultiValues",
    "JET_bitSetUniqueNormalizedMultiValues",
    "JET_bitSetZeroLength",
    "JET_bitShrinkDatabaseOff",
    "JET_bitShrinkDatabaseOn",
    "JET_bitShrinkDatabaseRealtime",
    "JET_bitShrinkDatabaseTrim",
    "JET_bitSpaceHintsUtilizeParentSpace",
    "JET_bitStopServiceAll",
    "JET_bitStopServiceBackgroundUserTasks",
    "JET_bitStopServiceQuiesceCaches",
    "JET_bitStopServiceResume",
    "JET_bitStrLimit",
    "JET_bitSubStrLimit",
    "JET_bitTTDotNetGuid",
    "JET_bitTTErrorOnDuplicateInsertion",
    "JET_bitTTForceMaterialization",
    "JET_bitTTForwardOnly",
    "JET_bitTTIndexed",
    "JET_bitTTIntrinsicLVsOnly",
    "JET_bitTTScrollable",
    "JET_bitTTSortNullsHigh",
    "JET_bitTTUnique",
    "JET_bitTTUpdatable",
    "JET_bitTableClass1",
    "JET_bitTableClass10",
    "JET_bitTableClass11",
    "JET_bitTableClass12",
    "JET_bitTableClass13",
    "JET_bitTableClass14",
    "JET_bitTableClass15",
    "JET_bitTableClass2",
    "JET_bitTableClass3",
    "JET_bitTableClass4",
    "JET_bitTableClass5",
    "JET_bitTableClass6",
    "JET_bitTableClass7",
    "JET_bitTableClass8",
    "JET_bitTableClass9",
    "JET_bitTableClassMask",
    "JET_bitTableClassNone",
    "JET_bitTableCreateFixedDDL",
    "JET_bitTableCreateImmutableStructure",
    "JET_bitTableCreateNoFixedVarColumnsInDerivedTables",
    "JET_bitTableCreateTemplateTable",
    "JET_bitTableDenyRead",
    "JET_bitTableDenyWrite",
    "JET_bitTableInfoBookmark",
    "JET_bitTableInfoRollback",
    "JET_bitTableInfoUpdatable",
    "JET_bitTableNoCache",
    "JET_bitTableOpportuneRead",
    "JET_bitTablePermitDDL",
    "JET_bitTablePreread",
    "JET_bitTableReadOnly",
    "JET_bitTableSequential",
    "JET_bitTableUpdatable",
    "JET_bitTermAbrupt",
    "JET_bitTermComplete",
    "JET_bitTermDirty",
    "JET_bitTermStopBackup",
    "JET_bitTransactionReadOnly",
    "JET_bitTruncateLogsAfterRecovery",
    "JET_bitUpdateCheckESE97Compatibility",
    "JET_bitWaitAllLevel0Commit",
    "JET_bitWaitLastLevel0Commit",
    "JET_bitWriteLock",
    "JET_bitZeroLength",
    "JET_cbBookmarkMost",
    "JET_cbColumnLVPageOverhead",
    "JET_cbColumnMost",
    "JET_cbFullNameMost",
    "JET_cbKeyMost",
    "JET_cbKeyMost2KBytePage",
    "JET_cbKeyMost4KBytePage",
    "JET_cbKeyMost8KBytePage",
    "JET_cbKeyMostMin",
    "JET_cbLVColumnMost",
    "JET_cbLVDefaultValueMost",
    "JET_cbLimitKeyMost",
    "JET_cbNameMost",
    "JET_cbPrimaryKeyMost",
    "JET_cbSecondaryKeyMost",
    "JET_cbtypAfterDelete",
    "JET_cbtypAfterInsert",
    "JET_cbtypAfterReplace",
    "JET_cbtypBeforeDelete",
    "JET_cbtypBeforeInsert",
    "JET_cbtypBeforeReplace",
    "JET_cbtypFinalize",
    "JET_cbtypFreeCursorLS",
    "JET_cbtypFreeTableLS",
    "JET_cbtypNull",
    "JET_cbtypOnlineDefragCompleted",
    "JET_cbtypUserDefinedDefaultValue",
    "JET_ccolFixedMost",
    "JET_ccolKeyMost",
    "JET_ccolMost",
    "JET_ccolVarMost",
    "JET_coltypBinary",
    "JET_coltypBit",
    "JET_coltypCurrency",
    "JET_coltypDateTime",
    "JET_coltypGUID",
    "JET_coltypIEEEDouble",
    "JET_coltypIEEESingle",
    "JET_coltypLong",
    "JET_coltypLongBinary",
    "JET_coltypLongLong",
    "JET_coltypLongText",
    "JET_coltypMax",
    "JET_coltypNil",
    "JET_coltypSLV",
    "JET_coltypShort",
    "JET_coltypText",
    "JET_coltypUnsignedByte",
    "JET_coltypUnsignedLong",
    "JET_coltypUnsignedLongLong",
    "JET_coltypUnsignedShort",
    "JET_configDefault",
    "JET_configDynamicMediumMemory",
    "JET_configHighConcurrencyScaling",
    "JET_configLowDiskFootprint",
    "JET_configLowMemory",
    "JET_configLowPower",
    "JET_configMediumDiskFootprint",
    "JET_configRemoveQuotas",
    "JET_configRunSilent",
    "JET_configSSDProfileIO",
    "JET_configUnthrottledMemory",
    "JET_dbstateBeingConverted",
    "JET_dbstateCleanShutdown",
    "JET_dbstateDirtyShutdown",
    "JET_dbstateForceDetach",
    "JET_dbstateJustCreated",
    "JET_errAccessDenied",
    "JET_errAfterInitialization",
    "JET_errAlreadyInitialized",
    "JET_errAlreadyPrepared",
    "JET_errAttachedDatabaseMismatch",
    "JET_errBackupAbortByServer",
    "JET_errBackupDirectoryNotEmpty",
    "JET_errBackupInProgress",
    "JET_errBackupNotAllowedYet",
    "JET_errBadBackupDatabaseSize",
    "JET_errBadBookmark",
    "JET_errBadCheckpointSignature",
    "JET_errBadColumnId",
    "JET_errBadDbSignature",
    "JET_errBadEmptyPage",
    "JET_errBadItagSequence",
    "JET_errBadLineCount",
    "JET_errBadLogSignature",
    "JET_errBadLogVersion",
    "JET_errBadPageLink",
    "JET_errBadParentPageLink",
    "JET_errBadPatchPage",
    "JET_errBadRestoreTargetInstance",
    "JET_errBufferTooSmall",
    "JET_errCallbackFailed",
    "JET_errCallbackNotResolved",
    "JET_errCannotAddFixedVarColumnToDerivedTable",
    "JET_errCannotBeTagged",
    "JET_errCannotDeleteSystemTable",
    "JET_errCannotDeleteTempTable",
    "JET_errCannotDeleteTemplateTable",
    "JET_errCannotDisableVersioning",
    "JET_errCannotIndex",
    "JET_errCannotIndexOnEncryptedColumn",
    "JET_errCannotLogDuringRecoveryRedo",
    "JET_errCannotMaterializeForwardOnlySort",
    "JET_errCannotNestDDL",
    "JET_errCannotSeparateIntrinsicLV",
    "JET_errCatalogCorrupted",
    "JET_errCheckpointCorrupt",
    "JET_errCheckpointDepthTooDeep",
    "JET_errCheckpointFileNotFound",
    "JET_errClientRequestToStopJetService",
    "JET_errColumnCannotBeCompressed",
    "JET_errColumnCannotBeEncrypted",
    "JET_errColumnDoesNotFit",
    "JET_errColumnDuplicate",
    "JET_errColumnInRelationship",
    "JET_errColumnInUse",
    "JET_errColumnIndexed",
    "JET_errColumnLong",
    "JET_errColumnNoChunk",
    "JET_errColumnNoEncryptionKey",
    "JET_errColumnNotFound",
    "JET_errColumnNotUpdatable",
    "JET_errColumnRedundant",
    "JET_errColumnTooBig",
    "JET_errCommittedLogFileCorrupt",
    "JET_errCommittedLogFilesMissing",
    "JET_errConsistentTimeMismatch",
    "JET_errContainerNotEmpty",
    "JET_errDDLNotInheritable",
    "JET_errDataHasChanged",
    "JET_errDatabase200Format",
    "JET_errDatabase400Format",
    "JET_errDatabase500Format",
    "JET_errDatabaseAlreadyRunningMaintenance",
    "JET_errDatabaseAlreadyUpgraded",
    "JET_errDatabaseAttachedForRecovery",
    "JET_errDatabaseBufferDependenciesCorrupted",
    "JET_errDatabaseCorrupted",
    "JET_errDatabaseCorruptedNoRepair",
    "JET_errDatabaseDirtyShutdown",
    "JET_errDatabaseDuplicate",
    "JET_errDatabaseFileReadOnly",
    "JET_errDatabaseIdInUse",
    "JET_errDatabaseInUse",
    "JET_errDatabaseIncompleteUpgrade",
    "JET_errDatabaseInconsistent",
    "JET_errDatabaseInvalidName",
    "JET_errDatabaseInvalidPages",
    "JET_errDatabaseInvalidPath",
    "JET_errDatabaseLeakInSpace",
    "JET_errDatabaseLocked",
    "JET_errDatabaseLogSetMismatch",
    "JET_errDatabaseNotFound",
    "JET_errDatabaseNotReady",
    "JET_errDatabasePatchFileMismatch",
    "JET_errDatabaseSharingViolation",
    "JET_errDatabaseSignInUse",
    "JET_errDatabaseStreamingFileMismatch",
    "JET_errDatabaseUnavailable",
    "JET_errDatabasesNotFromSameSnapshot",
    "JET_errDbTimeCorrupted",
    "JET_errDbTimeTooNew",
    "JET_errDbTimeTooOld",
    "JET_errDecompressionFailed",
    "JET_errDecryptionFailed",
    "JET_errDefaultValueTooBig",
    "JET_errDeleteBackupFileFail",
    "JET_errDensityInvalid",
    "JET_errDerivedColumnCorruption",
    "JET_errDirtyShutdown",
    "JET_errDisabledFunctionality",
    "JET_errDiskFull",
    "JET_errDiskIO",
    "JET_errDiskReadVerificationFailure",
    "JET_errEncryptionBadItag",
    "JET_errEndingRestoreLogTooLow",
    "JET_errEngineFormatVersionNoLongerSupportedTooLow",
    "JET_errEngineFormatVersionNotYetImplementedTooHigh",
    "JET_errEngineFormatVersionParamTooLowForRequestedFeature",
    "JET_errEngineFormatVersionSpecifiedTooLowForDatabaseVersion",
    "JET_errEngineFormatVersionSpecifiedTooLowForLogVersion",
    "JET_errEntryPointNotFound",
    "JET_errExclusiveTableLockRequired",
    "JET_errExistingLogFileHasBadSignature",
    "JET_errExistingLogFileIsNotContiguous",
    "JET_errFeatureNotAvailable",
    "JET_errFileAccessDenied",
    "JET_errFileAlreadyExists",
    "JET_errFileClose",
    "JET_errFileCompressed",
    "JET_errFileIOAbort",
    "JET_errFileIOBeyondEOF",
    "JET_errFileIOFail",
    "JET_errFileIORetry",
    "JET_errFileIOSparse",
    "JET_errFileInvalidType",
    "JET_errFileNotFound",
    "JET_errFileSystemCorruption",
    "JET_errFilteredMoveNotSupported",
    "JET_errFixedDDL",
    "JET_errFixedInheritedDDL",
    "JET_errFlushMapDatabaseMismatch",
    "JET_errFlushMapUnrecoverable",
    "JET_errFlushMapVersionUnsupported",
    "JET_errForceDetachNotAllowed",
    "JET_errGivenLogFileHasBadSignature",
    "JET_errGivenLogFileIsNotContiguous",
    "JET_errIllegalOperation",
    "JET_errInTransaction",
    "JET_errIndexBuildCorrupted",
    "JET_errIndexCantBuild",
    "JET_errIndexDuplicate",
    "JET_errIndexHasPrimary",
    "JET_errIndexInUse",
    "JET_errIndexInvalidDef",
    "JET_errIndexMustStay",
    "JET_errIndexNotFound",
    "JET_errIndexTuplesCannotRetrieveFromIndex",
    "JET_errIndexTuplesInvalidLimits",
    "JET_errIndexTuplesKeyTooSmall",
    "JET_errIndexTuplesNonUniqueOnly",
    "JET_errIndexTuplesOneColumnOnly",
    "JET_errIndexTuplesSecondaryIndexOnly",
    "JET_errIndexTuplesTextBinaryColumnsOnly",
    "JET_errIndexTuplesTextColumnsOnly",
    "JET_errIndexTuplesTooManyColumns",
    "JET_errIndexTuplesVarSegMacNotAllowed",
    "JET_errInitInProgress",
    "JET_errInstanceNameInUse",
    "JET_errInstanceUnavailable",
    "JET_errInstanceUnavailableDueToFatalLogDiskFull",
    "JET_errInternalError",
    "JET_errInvalidBackup",
    "JET_errInvalidBackupSequence",
    "JET_errInvalidBookmark",
    "JET_errInvalidBufferSize",
    "JET_errInvalidCodePage",
    "JET_errInvalidColumnType",
    "JET_errInvalidCountry",
    "JET_errInvalidCreateDbVersion",
    "JET_errInvalidCreateIndex",
    "JET_errInvalidDatabase",
    "JET_errInvalidDatabaseId",
    "JET_errInvalidDatabaseVersion",
    "JET_errInvalidDbparamId",
    "JET_errInvalidFilename",
    "JET_errInvalidGrbit",
    "JET_errInvalidIndexId",
    "JET_errInvalidInstance",
    "JET_errInvalidLCMapStringFlags",
    "JET_errInvalidLVChunkSize",
    "JET_errInvalidLanguageId",
    "JET_errInvalidLogDirectory",
    "JET_errInvalidLogSequence",
    "JET_errInvalidLoggedOperation",
    "JET_errInvalidName",
    "JET_errInvalidObject",
    "JET_errInvalidOnSort",
    "JET_errInvalidOperation",
    "JET_errInvalidParameter",
    "JET_errInvalidPath",
    "JET_errInvalidPlaceholderColumn",
    "JET_errInvalidPreread",
    "JET_errInvalidSesid",
    "JET_errInvalidSesparamId",
    "JET_errInvalidSettings",
    "JET_errInvalidSystemPath",
    "JET_errInvalidTableId",
    "JET_errKeyBoundary",
    "JET_errKeyDuplicate",
    "JET_errKeyIsMade",
    "JET_errKeyNotMade",
    "JET_errKeyTooBig",
    "JET_errKeyTruncated",
    "JET_errLSAlreadySet",
    "JET_errLSCallbackNotSpecified",
    "JET_errLSNotSet",
    "JET_errLVCorrupted",
    "JET_errLanguageNotSupported",
    "JET_errLinkNotSupported",
    "JET_errLogBufferTooSmall",
    "JET_errLogCorruptDuringHardRecovery",
    "JET_errLogCorruptDuringHardRestore",
    "JET_errLogCorrupted",
    "JET_errLogDisabledDueToRecoveryFailure",
    "JET_errLogDiskFull",
    "JET_errLogFileCorrupt",
    "JET_errLogFileNotCopied",
    "JET_errLogFilePathInUse",
    "JET_errLogFileSizeMismatch",
    "JET_errLogFileSizeMismatchDatabasesConsistent",
    "JET_errLogGenerationMismatch",
    "JET_errLogReadVerifyFailure",
    "JET_errLogSectorSizeMismatch",
    "JET_errLogSectorSizeMismatchDatabasesConsistent",
    "JET_errLogSequenceChecksumMismatch",
    "JET_errLogSequenceEnd",
    "JET_errLogSequenceEndDatabasesConsistent",
    "JET_errLogTornWriteDuringHardRecovery",
    "JET_errLogTornWriteDuringHardRestore",
    "JET_errLogWriteFail",
    "JET_errLoggingDisabled",
    "JET_errMakeBackupDirectoryFail",
    "JET_errMissingCurrentLogFiles",
    "JET_errMissingFileToBackup",
    "JET_errMissingFullBackup",
    "JET_errMissingLogFile",
    "JET_errMissingPatchPage",
    "JET_errMissingPreviousLogFile",
    "JET_errMissingRestoreLogFiles",
    "JET_errMultiValuedColumnMustBeTagged",
    "JET_errMultiValuedDuplicate",
    "JET_errMultiValuedDuplicateAfterTruncation",
    "JET_errMultiValuedIndexViolation",
    "JET_errMustBeSeparateLongValue",
    "JET_errMustDisableLoggingForDbUpgrade",
    "JET_errMustRollback",
    "JET_errNTSystemCallFailed",
    "JET_errNoBackup",
    "JET_errNoBackupDirectory",
    "JET_errNoCurrentIndex",
    "JET_errNoCurrentRecord",
    "JET_errNodeCorrupted",
    "JET_errNotInTransaction",
    "JET_errNotInitialized",
    "JET_errNullInvalid",
    "JET_errNullKeyDisallowed",
    "JET_errOSSnapshotInvalidSequence",
    "JET_errOSSnapshotInvalidSnapId",
    "JET_errOSSnapshotNotAllowed",
    "JET_errOSSnapshotTimeOut",
    "JET_errObjectDuplicate",
    "JET_errObjectNotFound",
    "JET_errOneDatabasePerSession",
    "JET_errOutOfAutoincrementValues",
    "JET_errOutOfBuffers",
    "JET_errOutOfCursors",
    "JET_errOutOfDatabaseSpace",
    "JET_errOutOfDbtimeValues",
    "JET_errOutOfFileHandles",
    "JET_errOutOfLongValueIDs",
    "JET_errOutOfMemory",
    "JET_errOutOfObjectIDs",
    "JET_errOutOfSequentialIndexValues",
    "JET_errOutOfSessions",
    "JET_errOutOfThreads",
    "JET_errPageBoundary",
    "JET_errPageInitializedMismatch",
    "JET_errPageNotInitialized",
    "JET_errPageSizeMismatch",
    "JET_errPageTagCorrupted",
    "JET_errPartiallyAttachedDB",
    "JET_errPatchFileMissing",
    "JET_errPermissionDenied",
    "JET_errPreviousVersion",
    "JET_errPrimaryIndexCorrupted",
    "JET_errReadLostFlushVerifyFailure",
    "JET_errReadPgnoVerifyFailure",
    "JET_errReadVerifyFailure",
    "JET_errRecordDeleted",
    "JET_errRecordFormatConversionFailed",
    "JET_errRecordNoCopy",
    "JET_errRecordNotDeleted",
    "JET_errRecordNotFound",
    "JET_errRecordPrimaryChanged",
    "JET_errRecordTooBig",
    "JET_errRecordTooBigForBackwardCompatibility",
    "JET_errRecoveredWithErrors",
    "JET_errRecoveredWithoutUndo",
    "JET_errRecoveredWithoutUndoDatabasesConsistent",
    "JET_errRecoveryVerifyFailure",
    "JET_errRedoAbruptEnded",
    "JET_errRequiredLogFilesMissing",
    "JET_errRestoreInProgress",
    "JET_errRestoreOfNonBackupDatabase",
    "JET_errRfsFailure",
    "JET_errRfsNotArmed",
    "JET_errRollbackError",
    "JET_errRollbackRequired",
    "JET_errRunningInMultiInstanceMode",
    "JET_errRunningInOneInstanceMode",
    "JET_errSPAvailExtCacheOutOfMemory",
    "JET_errSPAvailExtCacheOutOfSync",
    "JET_errSPAvailExtCorrupted",
    "JET_errSPOwnExtCorrupted",
    "JET_errSecondaryIndexCorrupted",
    "JET_errSectorSizeNotSupported",
    "JET_errSeparatedLongValue",
    "JET_errSesidTableIdMismatch",
    "JET_errSessionContextAlreadySet",
    "JET_errSessionContextNotSetByThisThread",
    "JET_errSessionInUse",
    "JET_errSessionSharingViolation",
    "JET_errSessionWriteConflict",
    "JET_errSoftRecoveryOnBackupDatabase",
    "JET_errSoftRecoveryOnSnapshot",
    "JET_errSpaceHintsInvalid",
    "JET_errStartingRestoreLogTooHigh",
    "JET_errStreamingDataNotLogged",
    "JET_errSuccess",
    "JET_errSystemParameterConflict",
    "JET_errSystemParamsAlreadySet",
    "JET_errSystemPathInUse",
    "JET_errTableDuplicate",
    "JET_errTableInUse",
    "JET_errTableLocked",
    "JET_errTableNotEmpty",
    "JET_errTaggedNotNULL",
    "JET_errTaskDropped",
    "JET_errTempFileOpenError",
    "JET_errTempPathInUse",
    "JET_errTermInProgress",
    "JET_errTooManyActiveUsers",
    "JET_errTooManyAttachedDatabases",
    "JET_errTooManyColumns",
    "JET_errTooManyIO",
    "JET_errTooManyIndexes",
    "JET_errTooManyInstances",
    "JET_errTooManyKeys",
    "JET_errTooManyMempoolEntries",
    "JET_errTooManyOpenDatabases",
    "JET_errTooManyOpenIndexes",
    "JET_errTooManyOpenTables",
    "JET_errTooManyOpenTablesAndCleanupTimedOut",
    "JET_errTooManyRecords",
    "JET_errTooManySorts",
    "JET_errTooManySplits",
    "JET_errTransReadOnly",
    "JET_errTransTooDeep",
    "JET_errTransactionTooLong",
    "JET_errTransactionsNotReadyDuringRecovery",
    "JET_errUnicodeLanguageValidationFailure",
    "JET_errUnicodeNormalizationNotSupported",
    "JET_errUnicodeTranslationBufferTooSmall",
    "JET_errUnicodeTranslationFail",
    "JET_errUnloadableOSFunctionality",
    "JET_errUpdateMustVersion",
    "JET_errUpdateNotPrepared",
    "JET_errVersionStoreEntryTooBig",
    "JET_errVersionStoreOutOfMemory",
    "JET_errVersionStoreOutOfMemoryAndCleanupTimedOut",
    "JET_errWriteConflict",
    "JET_errWriteConflictPrimaryIndex",
    "JET_errcatApi",
    "JET_errcatCorruption",
    "JET_errcatData",
    "JET_errcatDisk",
    "JET_errcatError",
    "JET_errcatFatal",
    "JET_errcatFragmentation",
    "JET_errcatIO",
    "JET_errcatInconsistent",
    "JET_errcatMax",
    "JET_errcatMemory",
    "JET_errcatObsolete",
    "JET_errcatOperation",
    "JET_errcatQuota",
    "JET_errcatResource",
    "JET_errcatState",
    "JET_errcatUnknown",
    "JET_errcatUsage",
    "JET_filetypeCheckpoint",
    "JET_filetypeDatabase",
    "JET_filetypeFlushMap",
    "JET_filetypeLog",
    "JET_filetypeTempDatabase",
    "JET_filetypeUnknown",
    "JET_objtypNil",
    "JET_objtypTable",
    "JET_paramAccessDeniedRetryPeriod",
    "JET_paramAlternateDatabaseRecoveryPath",
    "JET_paramBaseName",
    "JET_paramBatchIOBufferMax",
    "JET_paramCachePriority",
    "JET_paramCacheSize",
    "JET_paramCacheSizeMax",
    "JET_paramCacheSizeMin",
    "JET_paramCachedClosedTables",
    "JET_paramCheckFormatWhenOpenFail",
    "JET_paramCheckpointDepthMax",
    "JET_paramCheckpointIOMax",
    "JET_paramCircularLog",
    "JET_paramCleanupMismatchedLogFiles",
    "JET_paramCommitDefault",
    "JET_paramConfigStoreSpec",
    "JET_paramConfiguration",
    "JET_paramCreatePathIfNotExist",
    "JET_paramDatabasePageSize",
    "JET_paramDbExtensionSize",
    "JET_paramDbScanIntervalMaxSec",
    "JET_paramDbScanIntervalMinSec",
    "JET_paramDbScanThrottle",
    "JET_paramDefragmentSequentialBTrees",
    "JET_paramDefragmentSequentialBTreesDensityCheckFrequency",
    "JET_paramDeleteOldLogs",
    "JET_paramDeleteOutOfRangeLogs",
    "JET_paramDisableCallbacks",
    "JET_paramDisablePerfmon",
    "JET_paramDurableCommitCallback",
    "JET_paramEnableAdvanced",
    "JET_paramEnableDBScanInRecovery",
    "JET_paramEnableDBScanSerialization",
    "JET_paramEnableFileCache",
    "JET_paramEnableIndexChecking",
    "JET_paramEnableIndexCleanup",
    "JET_paramEnableOnlineDefrag",
    "JET_paramEnablePersistedCallbacks",
    "JET_paramEnableRBS",
    "JET_paramEnableShrinkDatabase",
    "JET_paramEnableSqm",
    "JET_paramEnableTempTableVersioning",
    "JET_paramEnableViewCache",
    "JET_paramErrorToString",
    "JET_paramEventLogCache",
    "JET_paramEventLoggingLevel",
    "JET_paramEventSource",
    "JET_paramEventSourceKey",
    "JET_paramExceptionAction",
    "JET_paramGlobalMinVerPages",
    "JET_paramHungIOActions",
    "JET_paramHungIOThreshold",
    "JET_paramIOPriority",
    "JET_paramIOThrottlingTimeQuanta",
    "JET_paramIgnoreLogVersion",
    "JET_paramIndexTupleIncrement",
    "JET_paramIndexTupleStart",
    "JET_paramIndexTuplesLengthMax",
    "JET_paramIndexTuplesLengthMin",
    "JET_paramIndexTuplesToIndexMax",
    "JET_paramKeyMost",
    "JET_paramLRUKCorrInterval",
    "JET_paramLRUKHistoryMax",
    "JET_paramLRUKPolicy",
    "JET_paramLRUKTimeout",
    "JET_paramLRUKTrxCorrInterval",
    "JET_paramLVChunkSizeMost",
    "JET_paramLegacyFileNames",
    "JET_paramLogBuffers",
    "JET_paramLogCheckpointPeriod",
    "JET_paramLogFileCreateAsynch",
    "JET_paramLogFilePath",
    "JET_paramLogFileSize",
    "JET_paramLogWaitingUserMax",
    "JET_paramMaxCoalesceReadGapSize",
    "JET_paramMaxCoalesceReadSize",
    "JET_paramMaxCoalesceWriteGapSize",
    "JET_paramMaxCoalesceWriteSize",
    "JET_paramMaxColtyp",
    "JET_paramMaxCursors",
    "JET_paramMaxInstances",
    "JET_paramMaxOpenTables",
    "JET_paramMaxSessions",
    "JET_paramMaxTemporaryTables",
    "JET_paramMaxTransactionSize",
    "JET_paramMaxValueInvalid",
    "JET_paramMaxVerPages",
    "JET_paramMinDataForXpress",
    "JET_paramNoInformationEvent",
    "JET_paramOSSnapshotTimeout",
    "JET_paramOneDatabasePerSession",
    "JET_paramOutstandingIOMax",
    "JET_paramPageFragment",
    "JET_paramPageHintCacheSize",
    "JET_paramPageTempDBMin",
    "JET_paramPreferredMaxOpenTables",
    "JET_paramPreferredVerPages",
    "JET_paramPrereadIOMax",
    "JET_paramProcessFriendlyName",
    "JET_paramRBSFilePath",
    "JET_paramRecordUpgradeDirtyLevel",
    "JET_paramRecovery",
    "JET_paramRuntimeCallback",
    "JET_paramStartFlushThreshold",
    "JET_paramStopFlushThreshold",
    "JET_paramSystemPath",
    "JET_paramTableClass10Name",
    "JET_paramTableClass11Name",
    "JET_paramTableClass12Name",
    "JET_paramTableClass13Name",
    "JET_paramTableClass14Name",
    "JET_paramTableClass15Name",
    "JET_paramTableClass1Name",
    "JET_paramTableClass2Name",
    "JET_paramTableClass3Name",
    "JET_paramTableClass4Name",
    "JET_paramTableClass5Name",
    "JET_paramTableClass6Name",
    "JET_paramTableClass7Name",
    "JET_paramTableClass8Name",
    "JET_paramTableClass9Name",
    "JET_paramTempPath",
    "JET_paramUnicodeIndexDefault",
    "JET_paramUseFlushForWriteDurability",
    "JET_paramVerPageSize",
    "JET_paramVersionStoreTaskQueueMax",
    "JET_paramWaitLogFlush",
    "JET_paramWaypointLatency",
    "JET_paramZeroDatabaseDuringBackup",
    "JET_prepCancel",
    "JET_prepInsert",
    "JET_prepInsertCopy",
    "JET_prepInsertCopyDeleteOriginal",
    "JET_prepInsertCopyReplaceOriginal",
    "JET_prepReplace",
    "JET_prepReplaceNoLock",
    "JET_relopBitmaskEqualsZero",
    "JET_relopBitmaskNotEqualsZero",
    "JET_relopEquals",
    "JET_relopGreaterThan",
    "JET_relopGreaterThanOrEqual",
    "JET_relopLessThan",
    "JET_relopLessThanOrEqual",
    "JET_relopNotEquals",
    "JET_relopPrefixEquals",
    "JET_revertstateCompleted",
    "JET_revertstateCopingLogs",
    "JET_revertstateInProgress",
    "JET_revertstateNone",
    "JET_sesparamCommitDefault",
    "JET_sesparamCorrelationID",
    "JET_sesparamMaxValueInvalid",
    "JET_sesparamOperationContext",
    "JET_sesparamTransactionLevel",
    "JET_snpBackup",
    "JET_snpCompact",
    "JET_snpRepair",
    "JET_snpRestore",
    "JET_snpScrub",
    "JET_snpUpgrade",
    "JET_snpUpgradeRecordFormat",
    "JET_sntBegin",
    "JET_sntComplete",
    "JET_sntFail",
    "JET_sntProgress",
    "JET_sntRequirements",
    "JET_sqmDisable",
    "JET_sqmEnable",
    "JET_sqmFromCEIP",
    "JET_wrnBufferTruncated",
    "JET_wrnCallbackNotRegistered",
    "JET_wrnColumnDefault",
    "JET_wrnColumnMaxTruncated",
    "JET_wrnColumnMoreTags",
    "JET_wrnColumnNotInRecord",
    "JET_wrnColumnNotLocal",
    "JET_wrnColumnNull",
    "JET_wrnColumnPresent",
    "JET_wrnColumnReference",
    "JET_wrnColumnSetNull",
    "JET_wrnColumnSingleValue",
    "JET_wrnColumnSkipped",
    "JET_wrnColumnTruncated",
    "JET_wrnCommittedLogFilesLost",
    "JET_wrnCommittedLogFilesRemoved",
    "JET_wrnCopyLongValue",
    "JET_wrnCorruptIndexDeleted",
    "JET_wrnDataHasChanged",
    "JET_wrnDatabaseAttached",
    "JET_wrnDatabaseRepaired",
    "JET_wrnDefragAlreadyRunning",
    "JET_wrnDefragNotRunning",
    "JET_wrnExistingLogFileHasBadSignature",
    "JET_wrnExistingLogFileIsNotContiguous",
    "JET_wrnFileOpenReadOnly",
    "JET_wrnFinishWithUndo",
    "JET_wrnIdleFull",
    "JET_wrnKeyChanged",
    "JET_wrnNoErrorInfo",
    "JET_wrnNoIdleActivity",
    "JET_wrnNoWriteLock",
    "JET_wrnNyi",
    "JET_wrnPrimaryIndexOutOfDate",
    "JET_wrnRemainingVersions",
    "JET_wrnSecondaryIndexOutOfDate",
    "JET_wrnSeekNotEqual",
    "JET_wrnSeparateLongValue",
    "JET_wrnShrinkNotPossible",
    "JET_wrnSkipThisRecord",
    "JET_wrnSortOverflow",
    "JET_wrnTableEmpty",
    "JET_wrnTableInUseBySystem",
    "JET_wrnTargetInstanceRunning",
    "JET_wrnUniqueKey",
    "JET_wszConfigStoreReadControl",
    "JET_wszConfigStoreRelPathSysParamDefault",
    "JET_wszConfigStoreRelPathSysParamOverride",
    "JetAddColumnA",
    "JetAddColumnW",
    "JetAttachDatabase2A",
    "JetAttachDatabase2W",
    "JetAttachDatabaseA",
    "JetAttachDatabaseW",
    "JetBackupA",
    "JetBackupInstanceA",
    "JetBackupInstanceW",
    "JetBackupW",
    "JetBeginExternalBackup",
    "JetBeginExternalBackupInstance",
    "JetBeginSessionA",
    "JetBeginSessionW",
    "JetBeginTransaction",
    "JetBeginTransaction2",
    "JetBeginTransaction3",
    "JetCloseDatabase",
    "JetCloseFile",
    "JetCloseFileInstance",
    "JetCloseTable",
    "JetCommitTransaction",
    "JetCommitTransaction2",
    "JetCompactA",
    "JetCompactW",
    "JetComputeStats",
    "JetConfigureProcessForCrashDump",
    "JetCreateDatabase2A",
    "JetCreateDatabase2W",
    "JetCreateDatabaseA",
    "JetCreateDatabaseW",
    "JetCreateIndex2A",
    "JetCreateIndex2W",
    "JetCreateIndex3A",
    "JetCreateIndex3W",
    "JetCreateIndex4A",
    "JetCreateIndex4W",
    "JetCreateIndexA",
    "JetCreateIndexW",
    "JetCreateInstance2A",
    "JetCreateInstance2W",
    "JetCreateInstanceA",
    "JetCreateInstanceW",
    "JetCreateTableA",
    "JetCreateTableColumnIndex2A",
    "JetCreateTableColumnIndex2W",
    "JetCreateTableColumnIndex3A",
    "JetCreateTableColumnIndex3W",
    "JetCreateTableColumnIndex4A",
    "JetCreateTableColumnIndex4W",
    "JetCreateTableColumnIndexA",
    "JetCreateTableColumnIndexW",
    "JetCreateTableW",
    "JetDefragment2A",
    "JetDefragment2W",
    "JetDefragment3A",
    "JetDefragment3W",
    "JetDefragmentA",
    "JetDefragmentW",
    "JetDelete",
    "JetDeleteColumn2A",
    "JetDeleteColumn2W",
    "JetDeleteColumnA",
    "JetDeleteColumnW",
    "JetDeleteIndexA",
    "JetDeleteIndexW",
    "JetDeleteTableA",
    "JetDeleteTableW",
    "JetDetachDatabase2A",
    "JetDetachDatabase2W",
    "JetDetachDatabaseA",
    "JetDetachDatabaseW",
    "JetDupCursor",
    "JetDupSession",
    "JetEnableMultiInstanceA",
    "JetEnableMultiInstanceW",
    "JetEndExternalBackup",
    "JetEndExternalBackupInstance",
    "JetEndExternalBackupInstance2",
    "JetEndSession",
    "JetEnumerateColumns",
    "JetEscrowUpdate",
    "JetExternalRestore2A",
    "JetExternalRestore2W",
    "JetExternalRestoreA",
    "JetExternalRestoreW",
    "JetFreeBuffer",
    "JetGetAttachInfoA",
    "JetGetAttachInfoInstanceA",
    "JetGetAttachInfoInstanceW",
    "JetGetAttachInfoW",
    "JetGetBookmark",
    "JetGetColumnInfoA",
    "JetGetColumnInfoW",
    "JetGetCurrentIndexA",
    "JetGetCurrentIndexW",
    "JetGetCursorInfo",
    "JetGetDatabaseFileInfoA",
    "JetGetDatabaseFileInfoW",
    "JetGetDatabaseInfoA",
    "JetGetDatabaseInfoW",
    "JetGetErrorInfoW",
    "JetGetIndexInfoA",
    "JetGetIndexInfoW",
    "JetGetInstanceInfoA",
    "JetGetInstanceInfoW",
    "JetGetInstanceMiscInfo",
    "JetGetLS",
    "JetGetLock",
    "JetGetLogInfoA",
    "JetGetLogInfoInstance2A",
    "JetGetLogInfoInstance2W",
    "JetGetLogInfoInstanceA",
    "JetGetLogInfoInstanceW",
    "JetGetLogInfoW",
    "JetGetObjectInfoA",
    "JetGetObjectInfoW",
    "JetGetRecordPosition",
    "JetGetRecordSize",
    "JetGetRecordSize2",
    "JetGetSecondaryIndexBookmark",
    "JetGetSessionParameter",
    "JetGetSystemParameterA",
    "JetGetSystemParameterW",
    "JetGetTableColumnInfoA",
    "JetGetTableColumnInfoW",
    "JetGetTableIndexInfoA",
    "JetGetTableIndexInfoW",
    "JetGetTableInfoA",
    "JetGetTableInfoW",
    "JetGetThreadStats",
    "JetGetTruncateLogInfoInstanceA",
    "JetGetTruncateLogInfoInstanceW",
    "JetGetVersion",
    "JetGotoBookmark",
    "JetGotoPosition",
    "JetGotoSecondaryIndexBookmark",
    "JetGrowDatabase",
    "JetIdle",
    "JetIndexRecordCount",
    "JetInit",
    "JetInit2",
    "JetInit3A",
    "JetInit3W",
    "JetIntersectIndexes",
    "JetMakeKey",
    "JetMove",
    "JetOSSnapshotAbort",
    "JetOSSnapshotEnd",
    "JetOSSnapshotFreezeA",
    "JetOSSnapshotFreezeW",
    "JetOSSnapshotGetFreezeInfoA",
    "JetOSSnapshotGetFreezeInfoW",
    "JetOSSnapshotPrepare",
    "JetOSSnapshotPrepareInstance",
    "JetOSSnapshotThaw",
    "JetOSSnapshotTruncateLog",
    "JetOSSnapshotTruncateLogInstance",
    "JetOpenDatabaseA",
    "JetOpenDatabaseW",
    "JetOpenFileA",
    "JetOpenFileInstanceA",
    "JetOpenFileInstanceW",
    "JetOpenFileW",
    "JetOpenTableA",
    "JetOpenTableW",
    "JetOpenTempTable",
    "JetOpenTempTable2",
    "JetOpenTempTable3",
    "JetOpenTemporaryTable",
    "JetOpenTemporaryTable2",
    "JetPrepareUpdate",
    "JetPrereadIndexRanges",
    "JetPrereadKeys",
    "JetReadFile",
    "JetReadFileInstance",
    "JetRegisterCallback",
    "JetRenameColumnA",
    "JetRenameColumnW",
    "JetRenameTableA",
    "JetRenameTableW",
    "JetResetSessionContext",
    "JetResetTableSequential",
    "JetResizeDatabase",
    "JetRestore2A",
    "JetRestore2W",
    "JetRestoreA",
    "JetRestoreInstanceA",
    "JetRestoreInstanceW",
    "JetRestoreW",
    "JetRetrieveColumn",
    "JetRetrieveColumns",
    "JetRetrieveKey",
    "JetRollback",
    "JetSeek",
    "JetSetColumn",
    "JetSetColumnDefaultValueA",
    "JetSetColumnDefaultValueW",
    "JetSetColumns",
    "JetSetCurrentIndex2A",
    "JetSetCurrentIndex2W",
    "JetSetCurrentIndex3A",
    "JetSetCurrentIndex3W",
    "JetSetCurrentIndex4A",
    "JetSetCurrentIndex4W",
    "JetSetCurrentIndexA",
    "JetSetCurrentIndexW",
    "JetSetCursorFilter",
    "JetSetDatabaseSizeA",
    "JetSetDatabaseSizeW",
    "JetSetIndexRange",
    "JetSetLS",
    "JetSetSessionContext",
    "JetSetSessionParameter",
    "JetSetSystemParameterA",
    "JetSetSystemParameterW",
    "JetSetTableSequential",
    "JetStopBackup",
    "JetStopBackupInstance",
    "JetStopService",
    "JetStopServiceInstance",
    "JetStopServiceInstance2",
    "JetTerm",
    "JetTerm2",
    "JetTruncateLog",
    "JetTruncateLogInstance",
    "JetUnregisterCallback",
    "JetUpdate",
    "JetUpdate2",
    "cColumnInfoCols",
    "cIndexInfoCols",
    "cObjectInfoCols",
    "wrnBTNotVisibleAccumulated",
    "wrnBTNotVisibleRejected",
]
_arch_optional = [
]
