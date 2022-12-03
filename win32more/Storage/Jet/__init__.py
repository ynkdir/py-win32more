from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Storage.Jet
import win32more.Storage.StructuredStorage
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
JET_VERSION = 1280
JET_wszConfigStoreReadControl = 'CsReadControl'
JET_bitConfigStoreReadControlInhibitRead = 1
JET_bitConfigStoreReadControlDisableAll = 2
JET_bitConfigStoreReadControlDefault = 0
JET_wszConfigStoreRelPathSysParamDefault = 'SysParamDefault'
JET_wszConfigStoreRelPathSysParamOverride = 'SysParamOverride'
JET_bitDefragmentBatchStart = 1
JET_bitDefragmentBatchStop = 2
JET_bitDefragmentAvailSpaceTreesOnly = 64
JET_bitDefragmentNoPartialMerges = 128
JET_bitDefragmentBTree = 256
JET_cbtypNull = 0
JET_cbtypFinalize = 1
JET_cbtypBeforeInsert = 2
JET_cbtypAfterInsert = 4
JET_cbtypBeforeReplace = 8
JET_cbtypAfterReplace = 16
JET_cbtypBeforeDelete = 32
JET_cbtypAfterDelete = 64
JET_cbtypUserDefinedDefaultValue = 128
JET_cbtypOnlineDefragCompleted = 256
JET_cbtypFreeCursorLS = 512
JET_cbtypFreeTableLS = 1024
JET_bitTableInfoUpdatable = 1
JET_bitTableInfoBookmark = 2
JET_bitTableInfoRollback = 4
JET_bitObjectSystem = 2147483648
JET_bitObjectTableFixedDDL = 1073741824
JET_bitObjectTableTemplate = 536870912
JET_bitObjectTableDerived = 268435456
JET_bitObjectTableNoFixedVarColumnsInDerivedTables = 67108864
cObjectInfoCols = 9
cColumnInfoCols = 14
cIndexInfoCols = 15
JET_MAX_COMPUTERNAME_LENGTH = 15
JET_bitDurableCommitCallbackLogUnavailable = 1
JET_cbBookmarkMost = 256
JET_cbNameMost = 64
JET_cbFullNameMost = 255
JET_cbColumnLVPageOverhead = 82
JET_cbLVDefaultValueMost = 255
JET_cbColumnMost = 255
JET_cbLVColumnMost = 2147483647
JET_cbKeyMost8KBytePage = 2000
JET_cbKeyMost4KBytePage = 1000
JET_cbKeyMost2KBytePage = 500
JET_cbKeyMostMin = 255
JET_cbKeyMost = 255
JET_cbLimitKeyMost = 256
JET_cbPrimaryKeyMost = 255
JET_cbSecondaryKeyMost = 255
JET_ccolKeyMost = 16
JET_ccolMost = 65248
JET_ccolFixedMost = 127
JET_ccolVarMost = 128
JET_EventLoggingDisable = 0
JET_EventLoggingLevelMin = 1
JET_EventLoggingLevelLow = 25
JET_EventLoggingLevelMedium = 50
JET_EventLoggingLevelHigh = 75
JET_EventLoggingLevelMax = 100
JET_IOPriorityNormal = 0
JET_IOPriorityLow = 1
JET_configDefault = 1
JET_configRemoveQuotas = 2
JET_configLowDiskFootprint = 4
JET_configMediumDiskFootprint = 8
JET_configLowMemory = 16
JET_configDynamicMediumMemory = 32
JET_configLowPower = 64
JET_configSSDProfileIO = 128
JET_configRunSilent = 256
JET_configUnthrottledMemory = 512
JET_configHighConcurrencyScaling = 1024
JET_paramSystemPath = 0
JET_paramTempPath = 1
JET_paramLogFilePath = 2
JET_paramBaseName = 3
JET_paramEventSource = 4
JET_paramMaxSessions = 5
JET_paramMaxOpenTables = 6
JET_paramPreferredMaxOpenTables = 7
JET_paramCachedClosedTables = 125
JET_paramMaxCursors = 8
JET_paramMaxVerPages = 9
JET_paramPreferredVerPages = 63
JET_paramGlobalMinVerPages = 81
JET_paramVersionStoreTaskQueueMax = 105
JET_paramMaxTemporaryTables = 10
JET_paramLogFileSize = 11
JET_paramLogBuffers = 12
JET_paramWaitLogFlush = 13
JET_paramLogCheckpointPeriod = 14
JET_paramLogWaitingUserMax = 15
JET_paramCommitDefault = 16
JET_paramCircularLog = 17
JET_paramDbExtensionSize = 18
JET_paramPageTempDBMin = 19
JET_paramPageFragment = 20
JET_paramEnableFileCache = 126
JET_paramVerPageSize = 128
JET_paramConfiguration = 129
JET_paramEnableAdvanced = 130
JET_paramMaxColtyp = 131
JET_paramBatchIOBufferMax = 22
JET_paramCacheSize = 41
JET_paramCacheSizeMin = 60
JET_paramCacheSizeMax = 23
JET_paramCheckpointDepthMax = 24
JET_paramLRUKCorrInterval = 25
JET_paramLRUKHistoryMax = 26
JET_paramLRUKPolicy = 27
JET_paramLRUKTimeout = 28
JET_paramLRUKTrxCorrInterval = 29
JET_paramOutstandingIOMax = 30
JET_paramStartFlushThreshold = 31
JET_paramStopFlushThreshold = 32
JET_paramEnableViewCache = 127
JET_paramCheckpointIOMax = 135
JET_paramTableClass1Name = 137
JET_paramTableClass2Name = 138
JET_paramTableClass3Name = 139
JET_paramTableClass4Name = 140
JET_paramTableClass5Name = 141
JET_paramTableClass6Name = 142
JET_paramTableClass7Name = 143
JET_paramTableClass8Name = 144
JET_paramTableClass9Name = 145
JET_paramTableClass10Name = 146
JET_paramTableClass11Name = 147
JET_paramTableClass12Name = 148
JET_paramTableClass13Name = 149
JET_paramTableClass14Name = 150
JET_paramTableClass15Name = 151
JET_paramIOPriority = 152
JET_paramRecovery = 34
JET_paramEnableOnlineDefrag = 35
JET_paramCheckFormatWhenOpenFail = 44
JET_paramEnableTempTableVersioning = 46
JET_paramIgnoreLogVersion = 47
JET_paramDeleteOldLogs = 48
JET_paramEventSourceKey = 49
JET_paramNoInformationEvent = 50
JET_paramEventLoggingLevel = 51
JET_paramDeleteOutOfRangeLogs = 52
JET_paramAccessDeniedRetryPeriod = 53
JET_paramEnableIndexChecking = 45
JET_paramEnableIndexCleanup = 54
JET_paramDatabasePageSize = 64
JET_paramDisableCallbacks = 65
JET_paramLogFileCreateAsynch = 69
JET_paramErrorToString = 70
JET_paramZeroDatabaseDuringBackup = 71
JET_paramUnicodeIndexDefault = 72
JET_paramRuntimeCallback = 73
JET_paramCleanupMismatchedLogFiles = 77
JET_paramRecordUpgradeDirtyLevel = 78
JET_paramOSSnapshotTimeout = 82
JET_paramExceptionAction = 98
JET_paramEventLogCache = 99
JET_paramCreatePathIfNotExist = 100
JET_paramPageHintCacheSize = 101
JET_paramOneDatabasePerSession = 102
JET_paramMaxInstances = 104
JET_paramDisablePerfmon = 107
JET_paramIndexTuplesLengthMin = 110
JET_paramIndexTuplesLengthMax = 111
JET_paramIndexTuplesToIndexMax = 112
JET_paramAlternateDatabaseRecoveryPath = 113
JET_paramIndexTupleIncrement = 132
JET_paramIndexTupleStart = 133
JET_paramKeyMost = 134
JET_paramLegacyFileNames = 136
JET_paramEnablePersistedCallbacks = 156
JET_paramWaypointLatency = 153
JET_paramDefragmentSequentialBTrees = 160
JET_paramDefragmentSequentialBTreesDensityCheckFrequency = 161
JET_paramIOThrottlingTimeQuanta = 162
JET_paramLVChunkSizeMost = 163
JET_paramMaxCoalesceReadSize = 164
JET_paramMaxCoalesceWriteSize = 165
JET_paramMaxCoalesceReadGapSize = 166
JET_paramMaxCoalesceWriteGapSize = 167
JET_paramEnableDBScanInRecovery = 169
JET_paramDbScanThrottle = 170
JET_paramDbScanIntervalMinSec = 171
JET_paramDbScanIntervalMaxSec = 172
JET_paramCachePriority = 177
JET_paramMaxTransactionSize = 178
JET_paramPrereadIOMax = 179
JET_paramEnableDBScanSerialization = 180
JET_paramHungIOThreshold = 181
JET_paramHungIOActions = 182
JET_paramMinDataForXpress = 183
JET_paramEnableShrinkDatabase = 184
JET_paramProcessFriendlyName = 186
JET_paramDurableCommitCallback = 187
JET_paramEnableSqm = 188
JET_paramConfigStoreSpec = 189
JET_paramUseFlushForWriteDurability = 214
JET_paramEnableRBS = 215
JET_paramRBSFilePath = 216
JET_paramMaxValueInvalid = 217
JET_sesparamCommitDefault = 4097
JET_sesparamTransactionLevel = 4099
JET_sesparamOperationContext = 4100
JET_sesparamCorrelationID = 4101
JET_sesparamMaxValueInvalid = 4110
JET_bitESE98FileNames = 1
JET_bitEightDotThreeSoftCompat = 2
JET_bitHungIOEvent = 1
JET_bitShrinkDatabaseOff = 0
JET_bitShrinkDatabaseOn = 1
JET_bitShrinkDatabaseRealtime = 2
JET_bitShrinkDatabaseTrim = 1
JET_bitReplayIgnoreMissingDB = 4
JET_bitRecoveryWithoutUndo = 8
JET_bitTruncateLogsAfterRecovery = 16
JET_bitReplayMissingMapEntryDB = 32
JET_bitLogStreamMustExist = 64
JET_bitReplayIgnoreLostLogs = 128
JET_bitKeepDbAttachedAtEndOfRecovery = 4096
JET_bitTermComplete = 1
JET_bitTermAbrupt = 2
JET_bitTermStopBackup = 4
JET_bitTermDirty = 8
JET_bitIdleFlushBuffers = 1
JET_bitIdleCompact = 2
JET_bitIdleStatus = 4
JET_bitDbReadOnly = 1
JET_bitDbExclusive = 2
JET_bitDbDeleteCorruptIndexes = 16
JET_bitDbDeleteUnicodeIndexes = 1024
JET_bitDbUpgrade = 512
JET_bitDbEnableBackgroundMaintenance = 2048
JET_bitDbPurgeCacheOnAttach = 4096
JET_bitForceDetach = 1
JET_bitDbRecoveryOff = 8
JET_bitDbShadowingOff = 128
JET_bitDbOverwriteExisting = 512
JET_bitBackupIncremental = 1
JET_bitBackupAtomic = 4
JET_bitBackupSnapshot = 16
JET_bitBackupEndNormal = 1
JET_bitBackupEndAbort = 2
JET_bitBackupTruncateDone = 256
JET_bitTableCreateFixedDDL = 1
JET_bitTableCreateTemplateTable = 2
JET_bitTableCreateNoFixedVarColumnsInDerivedTables = 4
JET_bitTableCreateImmutableStructure = 8
JET_bitColumnFixed = 1
JET_bitColumnTagged = 2
JET_bitColumnNotNULL = 4
JET_bitColumnVersion = 8
JET_bitColumnAutoincrement = 16
JET_bitColumnUpdatable = 32
JET_bitColumnTTKey = 64
JET_bitColumnTTDescending = 128
JET_bitColumnMultiValued = 1024
JET_bitColumnEscrowUpdate = 2048
JET_bitColumnUnversioned = 4096
JET_bitColumnMaybeNull = 8192
JET_bitColumnFinalize = 16384
JET_bitColumnUserDefinedDefault = 32768
JET_bitColumnDeleteOnZero = 131072
JET_bitColumnCompressed = 524288
JET_bitDeleteColumnIgnoreTemplateColumns = 1
JET_bitMoveFirst = 0
JET_bitNoMove = 2
JET_bitNewKey = 1
JET_bitStrLimit = 2
JET_bitSubStrLimit = 4
JET_bitNormalizedKey = 8
JET_bitKeyDataZeroLength = 16
JET_bitFullColumnStartLimit = 256
JET_bitFullColumnEndLimit = 512
JET_bitPartialColumnStartLimit = 1024
JET_bitPartialColumnEndLimit = 2048
JET_bitRangeInclusive = 1
JET_bitRangeUpperLimit = 2
JET_bitRangeInstantDuration = 4
JET_bitRangeRemove = 8
JET_bitReadLock = 1
JET_bitWriteLock = 2
JET_MoveFirst = 2147483648
JET_MovePrevious = -1
JET_MoveLast = 2147483647
JET_bitMoveKeyNE = 1
JET_bitSeekEQ = 1
JET_bitSeekLT = 2
JET_bitSeekLE = 4
JET_bitSeekGE = 8
JET_bitSeekGT = 16
JET_bitSetIndexRange = 32
JET_bitCheckUniqueness = 64
JET_bitBookmarkPermitVirtualCurrency = 1
JET_bitIndexColumnMustBeNull = 1
JET_bitIndexColumnMustBeNonNull = 2
JET_bitRecordInIndex = 1
JET_bitRecordNotInIndex = 2
JET_bitIndexUnique = 1
JET_bitIndexPrimary = 2
JET_bitIndexDisallowNull = 4
JET_bitIndexIgnoreNull = 8
JET_bitIndexIgnoreAnyNull = 32
JET_bitIndexIgnoreFirstNull = 64
JET_bitIndexLazyFlush = 128
JET_bitIndexEmpty = 256
JET_bitIndexUnversioned = 512
JET_bitIndexSortNullsHigh = 1024
JET_bitIndexUnicode = 2048
JET_bitIndexTuples = 4096
JET_bitIndexTupleLimits = 8192
JET_bitIndexCrossProduct = 16384
JET_bitIndexKeyMost = 32768
JET_bitIndexDisallowTruncation = 65536
JET_bitIndexNestedTable = 131072
JET_bitIndexDotNetGuid = 262144
JET_bitIndexImmutableStructure = 524288
JET_bitKeyAscending = 0
JET_bitKeyDescending = 1
JET_bitTableDenyWrite = 1
JET_bitTableDenyRead = 2
JET_bitTableReadOnly = 4
JET_bitTableUpdatable = 8
JET_bitTablePermitDDL = 16
JET_bitTableNoCache = 32
JET_bitTablePreread = 64
JET_bitTableOpportuneRead = 128
JET_bitTableSequential = 32768
JET_bitTableClassMask = 2031616
JET_bitTableClassNone = 0
JET_bitTableClass1 = 65536
JET_bitTableClass2 = 131072
JET_bitTableClass3 = 196608
JET_bitTableClass4 = 262144
JET_bitTableClass5 = 327680
JET_bitTableClass6 = 393216
JET_bitTableClass7 = 458752
JET_bitTableClass8 = 524288
JET_bitTableClass9 = 589824
JET_bitTableClass10 = 655360
JET_bitTableClass11 = 720896
JET_bitTableClass12 = 786432
JET_bitTableClass13 = 851968
JET_bitTableClass14 = 917504
JET_bitTableClass15 = 983040
JET_bitLSReset = 1
JET_bitLSCursor = 2
JET_bitLSTable = 4
JET_bitPrereadForward = 1
JET_bitPrereadBackward = 2
JET_bitPrereadFirstPage = 4
JET_bitPrereadNormalizedKey = 8
JET_bitTTIndexed = 1
JET_bitTTUnique = 2
JET_bitTTUpdatable = 4
JET_bitTTScrollable = 8
JET_bitTTSortNullsHigh = 16
JET_bitTTForceMaterialization = 32
JET_bitTTErrorOnDuplicateInsertion = 32
JET_bitTTForwardOnly = 64
JET_bitTTIntrinsicLVsOnly = 128
JET_bitTTDotNetGuid = 256
JET_bitSetAppendLV = 1
JET_bitSetOverwriteLV = 4
JET_bitSetSizeLV = 8
JET_bitSetZeroLength = 32
JET_bitSetSeparateLV = 64
JET_bitSetUniqueMultiValues = 128
JET_bitSetUniqueNormalizedMultiValues = 256
JET_bitSetRevertToDefaultValue = 512
JET_bitSetIntrinsicLV = 1024
JET_bitSetUncompressed = 65536
JET_bitSetCompressed = 131072
JET_bitSetContiguousLV = 262144
JET_bitSpaceHintsUtilizeParentSpace = 1
JET_bitCreateHintAppendSequential = 2
JET_bitCreateHintHotpointSequential = 4
JET_bitRetrieveHintReserve1 = 8
JET_bitRetrieveHintTableScanForward = 16
JET_bitRetrieveHintTableScanBackward = 32
JET_bitRetrieveHintReserve2 = 64
JET_bitRetrieveHintReserve3 = 128
JET_bitDeleteHintTableSequential = 256
JET_prepInsert = 0
JET_prepReplace = 2
JET_prepCancel = 3
JET_prepReplaceNoLock = 4
JET_prepInsertCopy = 5
JET_prepInsertCopyDeleteOriginal = 7
JET_prepInsertCopyReplaceOriginal = 9
JET_sqmDisable = 0
JET_sqmEnable = 1
JET_sqmFromCEIP = 2
JET_bitUpdateCheckESE97Compatibility = 1
JET_bitEscrowNoRollback = 1
JET_bitRetrieveCopy = 1
JET_bitRetrieveFromIndex = 2
JET_bitRetrieveFromPrimaryBookmark = 4
JET_bitRetrieveTag = 8
JET_bitRetrieveNull = 16
JET_bitRetrieveIgnoreDefault = 32
JET_bitRetrieveTuple = 2048
JET_bitZeroLength = 1
JET_bitEnumerateCopy = 1
JET_bitEnumerateIgnoreDefault = 32
JET_bitEnumeratePresenceOnly = 131072
JET_bitEnumerateTaggedOnly = 262144
JET_bitEnumerateCompressOutput = 524288
JET_bitEnumerateIgnoreUserDefinedDefault = 1048576
JET_bitEnumerateInRecordOnly = 2097152
JET_bitRecordSizeInCopyBuffer = 1
JET_bitRecordSizeRunningTotal = 2
JET_bitRecordSizeLocal = 4
JET_bitTransactionReadOnly = 1
JET_bitCommitLazyFlush = 1
JET_bitWaitLastLevel0Commit = 2
JET_bitWaitAllLevel0Commit = 8
JET_bitForceNewLog = 16
JET_bitRollbackAll = 1
JET_bitIncrementalSnapshot = 1
JET_bitCopySnapshot = 2
JET_bitContinueAfterThaw = 4
JET_bitExplicitPrepare = 8
JET_bitAllDatabasesSnapshot = 1
JET_bitAbortSnapshot = 1
JET_DbInfoFilename = 0
JET_DbInfoConnect = 1
JET_DbInfoCountry = 2
JET_DbInfoLCID = 3
JET_DbInfoLangid = 3
JET_DbInfoCp = 4
JET_DbInfoCollate = 5
JET_DbInfoOptions = 6
JET_DbInfoTransactions = 7
JET_DbInfoVersion = 8
JET_DbInfoIsam = 9
JET_DbInfoFilesize = 10
JET_DbInfoSpaceOwned = 11
JET_DbInfoSpaceAvailable = 12
JET_DbInfoUpgrade = 13
JET_DbInfoMisc = 14
JET_DbInfoDBInUse = 15
JET_DbInfoPageSize = 17
JET_DbInfoFileType = 19
JET_DbInfoFilesizeOnDisk = 21
JET_dbstateJustCreated = 1
JET_dbstateDirtyShutdown = 2
JET_dbstateCleanShutdown = 3
JET_dbstateBeingConverted = 4
JET_dbstateForceDetach = 5
JET_filetypeUnknown = 0
JET_filetypeDatabase = 1
JET_filetypeLog = 3
JET_filetypeCheckpoint = 4
JET_filetypeTempDatabase = 5
JET_filetypeFlushMap = 7
JET_revertstateNone = 0
JET_revertstateInProgress = 1
JET_revertstateCopingLogs = 2
JET_revertstateCompleted = 3
JET_bitDeleteAllExistingLogs = 1
JET_coltypNil = 0
JET_coltypBit = 1
JET_coltypUnsignedByte = 2
JET_coltypShort = 3
JET_coltypLong = 4
JET_coltypCurrency = 5
JET_coltypIEEESingle = 6
JET_coltypIEEEDouble = 7
JET_coltypDateTime = 8
JET_coltypBinary = 9
JET_coltypText = 10
JET_coltypLongBinary = 11
JET_coltypLongText = 12
JET_coltypMax = 13
JET_coltypSLV = 13
JET_coltypUnsignedLong = 14
JET_coltypLongLong = 15
JET_coltypGUID = 16
JET_coltypUnsignedShort = 17
JET_coltypUnsignedLongLong = 18
JET_ColInfoGrbitNonDerivedColumnsOnly = 2147483648
JET_ColInfoGrbitMinimalInfo = 1073741824
JET_ColInfoGrbitSortByColumnid = 536870912
JET_objtypNil = 0
JET_objtypTable = 1
JET_bitCompactStats = 32
JET_bitCompactRepair = 64
JET_snpRepair = 2
JET_snpCompact = 4
JET_snpRestore = 8
JET_snpBackup = 9
JET_snpUpgrade = 10
JET_snpScrub = 11
JET_snpUpgradeRecordFormat = 12
JET_sntBegin = 5
JET_sntRequirements = 7
JET_sntProgress = 0
JET_sntComplete = 6
JET_sntFail = 3
JET_ExceptionMsgBox = 1
JET_ExceptionNone = 2
JET_ExceptionFailFast = 4
JET_OnlineDefragDisable = 0
JET_OnlineDefragAllOBSOLETE = 1
JET_OnlineDefragDatabases = 2
JET_OnlineDefragSpaceTrees = 4
JET_OnlineDefragAll = 65535
JET_bitResizeDatabaseOnlyGrow = 1
JET_bitResizeDatabaseOnlyShrink = 2
JET_bitStopServiceAll = 0
JET_bitStopServiceBackgroundUserTasks = 2
JET_bitStopServiceQuiesceCaches = 4
JET_bitStopServiceResume = 2147483648
JET_errSuccess = 0
JET_wrnNyi = -1
JET_errRfsFailure = -100
JET_errRfsNotArmed = -101
JET_errFileClose = -102
JET_errOutOfThreads = -103
JET_errTooManyIO = -105
JET_errTaskDropped = -106
JET_errInternalError = -107
JET_errDisabledFunctionality = -112
JET_errUnloadableOSFunctionality = -113
JET_errDatabaseBufferDependenciesCorrupted = -255
JET_wrnRemainingVersions = 321
JET_errPreviousVersion = -322
JET_errPageBoundary = -323
JET_errKeyBoundary = -324
JET_errBadPageLink = -327
JET_errBadBookmark = -328
JET_errNTSystemCallFailed = -334
JET_errBadParentPageLink = -338
JET_errSPAvailExtCacheOutOfSync = -340
JET_errSPAvailExtCorrupted = -341
JET_errSPAvailExtCacheOutOfMemory = -342
JET_errSPOwnExtCorrupted = -343
JET_errDbTimeCorrupted = -344
JET_wrnUniqueKey = 345
JET_errKeyTruncated = -346
JET_errDatabaseLeakInSpace = -348
JET_errBadEmptyPage = -351
wrnBTNotVisibleRejected = 352
wrnBTNotVisibleAccumulated = 353
JET_errBadLineCount = -354
JET_errPageTagCorrupted = -357
JET_errNodeCorrupted = -358
JET_wrnSeparateLongValue = 406
JET_errKeyTooBig = -408
JET_errCannotSeparateIntrinsicLV = -416
JET_errSeparatedLongValue = -421
JET_errMustBeSeparateLongValue = -423
JET_errInvalidPreread = -424
JET_errInvalidLoggedOperation = -500
JET_errLogFileCorrupt = -501
JET_errNoBackupDirectory = -503
JET_errBackupDirectoryNotEmpty = -504
JET_errBackupInProgress = -505
JET_errRestoreInProgress = -506
JET_errMissingPreviousLogFile = -509
JET_errLogWriteFail = -510
JET_errLogDisabledDueToRecoveryFailure = -511
JET_errCannotLogDuringRecoveryRedo = -512
JET_errLogGenerationMismatch = -513
JET_errBadLogVersion = -514
JET_errInvalidLogSequence = -515
JET_errLoggingDisabled = -516
JET_errLogBufferTooSmall = -517
JET_errLogSequenceEnd = -519
JET_errNoBackup = -520
JET_errInvalidBackupSequence = -521
JET_errBackupNotAllowedYet = -523
JET_errDeleteBackupFileFail = -524
JET_errMakeBackupDirectoryFail = -525
JET_errInvalidBackup = -526
JET_errRecoveredWithErrors = -527
JET_errMissingLogFile = -528
JET_errLogDiskFull = -529
JET_errBadLogSignature = -530
JET_errBadDbSignature = -531
JET_errBadCheckpointSignature = -532
JET_errCheckpointCorrupt = -533
JET_errMissingPatchPage = -534
JET_errBadPatchPage = -535
JET_errRedoAbruptEnded = -536
JET_errPatchFileMissing = -538
JET_errDatabaseLogSetMismatch = -539
JET_errDatabaseStreamingFileMismatch = -540
JET_errLogFileSizeMismatch = -541
JET_errCheckpointFileNotFound = -542
JET_errRequiredLogFilesMissing = -543
JET_errSoftRecoveryOnBackupDatabase = -544
JET_errLogFileSizeMismatchDatabasesConsistent = -545
JET_errLogSectorSizeMismatch = -546
JET_errLogSectorSizeMismatchDatabasesConsistent = -547
JET_errLogSequenceEndDatabasesConsistent = -548
JET_errStreamingDataNotLogged = -549
JET_errDatabaseDirtyShutdown = -550
JET_errDatabaseInconsistent = -550
JET_errConsistentTimeMismatch = -551
JET_errDatabasePatchFileMismatch = -552
JET_errEndingRestoreLogTooLow = -553
JET_errStartingRestoreLogTooHigh = -554
JET_errGivenLogFileHasBadSignature = -555
JET_errGivenLogFileIsNotContiguous = -556
JET_errMissingRestoreLogFiles = -557
JET_wrnExistingLogFileHasBadSignature = 558
JET_wrnExistingLogFileIsNotContiguous = 559
JET_errMissingFullBackup = -560
JET_errBadBackupDatabaseSize = -561
JET_errDatabaseAlreadyUpgraded = -562
JET_errDatabaseIncompleteUpgrade = -563
JET_wrnSkipThisRecord = 564
JET_errMissingCurrentLogFiles = -565
JET_errDbTimeTooOld = -566
JET_errDbTimeTooNew = -567
JET_errMissingFileToBackup = -569
JET_errLogTornWriteDuringHardRestore = -570
JET_errLogTornWriteDuringHardRecovery = -571
JET_errLogCorruptDuringHardRestore = -573
JET_errLogCorruptDuringHardRecovery = -574
JET_errMustDisableLoggingForDbUpgrade = -575
JET_errBadRestoreTargetInstance = -577
JET_wrnTargetInstanceRunning = 578
JET_errRecoveredWithoutUndo = -579
JET_errDatabasesNotFromSameSnapshot = -580
JET_errSoftRecoveryOnSnapshot = -581
JET_errCommittedLogFilesMissing = -582
JET_errSectorSizeNotSupported = -583
JET_errRecoveredWithoutUndoDatabasesConsistent = -584
JET_wrnCommittedLogFilesLost = 585
JET_errCommittedLogFileCorrupt = -586
JET_wrnCommittedLogFilesRemoved = 587
JET_wrnFinishWithUndo = 588
JET_errLogSequenceChecksumMismatch = -590
JET_wrnDatabaseRepaired = 595
JET_errPageInitializedMismatch = -596
JET_errUnicodeTranslationBufferTooSmall = -601
JET_errUnicodeTranslationFail = -602
JET_errUnicodeNormalizationNotSupported = -603
JET_errUnicodeLanguageValidationFailure = -604
JET_errExistingLogFileHasBadSignature = -610
JET_errExistingLogFileIsNotContiguous = -611
JET_errLogReadVerifyFailure = -612
JET_errCheckpointDepthTooDeep = -614
JET_errRestoreOfNonBackupDatabase = -615
JET_errLogFileNotCopied = -616
JET_errTransactionTooLong = -618
JET_errEngineFormatVersionNoLongerSupportedTooLow = -619
JET_errEngineFormatVersionNotYetImplementedTooHigh = -620
JET_errEngineFormatVersionParamTooLowForRequestedFeature = -621
JET_errEngineFormatVersionSpecifiedTooLowForLogVersion = -622
JET_errEngineFormatVersionSpecifiedTooLowForDatabaseVersion = -623
JET_errBackupAbortByServer = -801
JET_errInvalidGrbit = -900
JET_errTermInProgress = -1000
JET_errFeatureNotAvailable = -1001
JET_errInvalidName = -1002
JET_errInvalidParameter = -1003
JET_wrnColumnNull = 1004
JET_wrnBufferTruncated = 1006
JET_wrnDatabaseAttached = 1007
JET_errDatabaseFileReadOnly = -1008
JET_wrnSortOverflow = 1009
JET_errInvalidDatabaseId = -1010
JET_errOutOfMemory = -1011
JET_errOutOfDatabaseSpace = -1012
JET_errOutOfCursors = -1013
JET_errOutOfBuffers = -1014
JET_errTooManyIndexes = -1015
JET_errTooManyKeys = -1016
JET_errRecordDeleted = -1017
JET_errReadVerifyFailure = -1018
JET_errPageNotInitialized = -1019
JET_errOutOfFileHandles = -1020
JET_errDiskReadVerificationFailure = -1021
JET_errDiskIO = -1022
JET_errInvalidPath = -1023
JET_errInvalidSystemPath = -1024
JET_errInvalidLogDirectory = -1025
JET_errRecordTooBig = -1026
JET_errTooManyOpenDatabases = -1027
JET_errInvalidDatabase = -1028
JET_errNotInitialized = -1029
JET_errAlreadyInitialized = -1030
JET_errInitInProgress = -1031
JET_errFileAccessDenied = -1032
JET_errBufferTooSmall = -1038
JET_wrnSeekNotEqual = 1039
JET_errTooManyColumns = -1040
JET_errContainerNotEmpty = -1043
JET_errInvalidFilename = -1044
JET_errInvalidBookmark = -1045
JET_errColumnInUse = -1046
JET_errInvalidBufferSize = -1047
JET_errColumnNotUpdatable = -1048
JET_errIndexInUse = -1051
JET_errLinkNotSupported = -1052
JET_errNullKeyDisallowed = -1053
JET_errNotInTransaction = -1054
JET_wrnNoErrorInfo = 1055
JET_errMustRollback = -1057
JET_wrnNoIdleActivity = 1058
JET_errTooManyActiveUsers = -1059
JET_errInvalidCountry = -1061
JET_errInvalidLanguageId = -1062
JET_errInvalidCodePage = -1063
JET_errInvalidLCMapStringFlags = -1064
JET_errVersionStoreEntryTooBig = -1065
JET_errVersionStoreOutOfMemoryAndCleanupTimedOut = -1066
JET_wrnNoWriteLock = 1067
JET_wrnColumnSetNull = 1068
JET_errVersionStoreOutOfMemory = -1069
JET_errCannotIndex = -1071
JET_errRecordNotDeleted = -1072
JET_errTooManyMempoolEntries = -1073
JET_errOutOfObjectIDs = -1074
JET_errOutOfLongValueIDs = -1075
JET_errOutOfAutoincrementValues = -1076
JET_errOutOfDbtimeValues = -1077
JET_errOutOfSequentialIndexValues = -1078
JET_errRunningInOneInstanceMode = -1080
JET_errRunningInMultiInstanceMode = -1081
JET_errSystemParamsAlreadySet = -1082
JET_errSystemPathInUse = -1083
JET_errLogFilePathInUse = -1084
JET_errTempPathInUse = -1085
JET_errInstanceNameInUse = -1086
JET_errSystemParameterConflict = -1087
JET_errInstanceUnavailable = -1090
JET_errDatabaseUnavailable = -1091
JET_errInstanceUnavailableDueToFatalLogDiskFull = -1092
JET_errInvalidSesparamId = -1093
JET_errTooManyRecords = -1094
JET_errInvalidDbparamId = -1095
JET_errOutOfSessions = -1101
JET_errWriteConflict = -1102
JET_errTransTooDeep = -1103
JET_errInvalidSesid = -1104
JET_errWriteConflictPrimaryIndex = -1105
JET_errInTransaction = -1108
JET_errRollbackRequired = -1109
JET_errTransReadOnly = -1110
JET_errSessionWriteConflict = -1111
JET_errRecordTooBigForBackwardCompatibility = -1112
JET_errCannotMaterializeForwardOnlySort = -1113
JET_errSesidTableIdMismatch = -1114
JET_errInvalidInstance = -1115
JET_errDirtyShutdown = -1116
JET_errReadPgnoVerifyFailure = -1118
JET_errReadLostFlushVerifyFailure = -1119
JET_errFileSystemCorruption = -1121
JET_wrnShrinkNotPossible = 1122
JET_errRecoveryVerifyFailure = -1123
JET_errFilteredMoveNotSupported = -1124
JET_errDatabaseDuplicate = -1201
JET_errDatabaseInUse = -1202
JET_errDatabaseNotFound = -1203
JET_errDatabaseInvalidName = -1204
JET_errDatabaseInvalidPages = -1205
JET_errDatabaseCorrupted = -1206
JET_errDatabaseLocked = -1207
JET_errCannotDisableVersioning = -1208
JET_errInvalidDatabaseVersion = -1209
JET_errDatabase200Format = -1210
JET_errDatabase400Format = -1211
JET_errDatabase500Format = -1212
JET_errPageSizeMismatch = -1213
JET_errTooManyInstances = -1214
JET_errDatabaseSharingViolation = -1215
JET_errAttachedDatabaseMismatch = -1216
JET_errDatabaseInvalidPath = -1217
JET_errDatabaseIdInUse = -1218
JET_errForceDetachNotAllowed = -1219
JET_errCatalogCorrupted = -1220
JET_errPartiallyAttachedDB = -1221
JET_errDatabaseSignInUse = -1222
JET_errDatabaseCorruptedNoRepair = -1224
JET_errInvalidCreateDbVersion = -1225
JET_errDatabaseNotReady = -1230
JET_errDatabaseAttachedForRecovery = -1231
JET_errTransactionsNotReadyDuringRecovery = -1232
JET_wrnTableEmpty = 1301
JET_errTableLocked = -1302
JET_errTableDuplicate = -1303
JET_errTableInUse = -1304
JET_errObjectNotFound = -1305
JET_errDensityInvalid = -1307
JET_errTableNotEmpty = -1308
JET_errInvalidTableId = -1310
JET_errTooManyOpenTables = -1311
JET_errIllegalOperation = -1312
JET_errTooManyOpenTablesAndCleanupTimedOut = -1313
JET_errObjectDuplicate = -1314
JET_errInvalidObject = -1316
JET_errCannotDeleteTempTable = -1317
JET_errCannotDeleteSystemTable = -1318
JET_errCannotDeleteTemplateTable = -1319
JET_errExclusiveTableLockRequired = -1322
JET_errFixedDDL = -1323
JET_errFixedInheritedDDL = -1324
JET_errCannotNestDDL = -1325
JET_errDDLNotInheritable = -1326
JET_wrnTableInUseBySystem = 1327
JET_errInvalidSettings = -1328
JET_errClientRequestToStopJetService = -1329
JET_errCannotAddFixedVarColumnToDerivedTable = -1330
JET_errIndexCantBuild = -1401
JET_errIndexHasPrimary = -1402
JET_errIndexDuplicate = -1403
JET_errIndexNotFound = -1404
JET_errIndexMustStay = -1405
JET_errIndexInvalidDef = -1406
JET_errInvalidCreateIndex = -1409
JET_errTooManyOpenIndexes = -1410
JET_errMultiValuedIndexViolation = -1411
JET_errIndexBuildCorrupted = -1412
JET_errPrimaryIndexCorrupted = -1413
JET_errSecondaryIndexCorrupted = -1414
JET_wrnCorruptIndexDeleted = 1415
JET_errInvalidIndexId = -1416
JET_wrnPrimaryIndexOutOfDate = 1417
JET_wrnSecondaryIndexOutOfDate = 1418
JET_errIndexTuplesSecondaryIndexOnly = -1430
JET_errIndexTuplesTooManyColumns = -1431
JET_errIndexTuplesOneColumnOnly = -1431
JET_errIndexTuplesNonUniqueOnly = -1432
JET_errIndexTuplesTextBinaryColumnsOnly = -1433
JET_errIndexTuplesTextColumnsOnly = -1433
JET_errIndexTuplesVarSegMacNotAllowed = -1434
JET_errIndexTuplesInvalidLimits = -1435
JET_errIndexTuplesCannotRetrieveFromIndex = -1436
JET_errIndexTuplesKeyTooSmall = -1437
JET_errInvalidLVChunkSize = -1438
JET_errColumnCannotBeEncrypted = -1439
JET_errCannotIndexOnEncryptedColumn = -1440
JET_errColumnLong = -1501
JET_errColumnNoChunk = -1502
JET_errColumnDoesNotFit = -1503
JET_errNullInvalid = -1504
JET_errColumnIndexed = -1505
JET_errColumnTooBig = -1506
JET_errColumnNotFound = -1507
JET_errColumnDuplicate = -1508
JET_errMultiValuedColumnMustBeTagged = -1509
JET_errColumnRedundant = -1510
JET_errInvalidColumnType = -1511
JET_wrnColumnMaxTruncated = 1512
JET_errTaggedNotNULL = -1514
JET_errNoCurrentIndex = -1515
JET_errKeyIsMade = -1516
JET_errBadColumnId = -1517
JET_errBadItagSequence = -1518
JET_errColumnInRelationship = -1519
JET_wrnCopyLongValue = 1520
JET_errCannotBeTagged = -1521
JET_errDefaultValueTooBig = -1524
JET_errMultiValuedDuplicate = -1525
JET_errLVCorrupted = -1526
JET_errMultiValuedDuplicateAfterTruncation = -1528
JET_errDerivedColumnCorruption = -1529
JET_errInvalidPlaceholderColumn = -1530
JET_wrnColumnSkipped = 1531
JET_wrnColumnNotLocal = 1532
JET_wrnColumnMoreTags = 1533
JET_wrnColumnTruncated = 1534
JET_wrnColumnPresent = 1535
JET_wrnColumnSingleValue = 1536
JET_wrnColumnDefault = 1537
JET_errColumnCannotBeCompressed = -1538
JET_wrnColumnNotInRecord = 1539
JET_errColumnNoEncryptionKey = -1540
JET_wrnColumnReference = 1541
JET_errRecordNotFound = -1601
JET_errRecordNoCopy = -1602
JET_errNoCurrentRecord = -1603
JET_errRecordPrimaryChanged = -1604
JET_errKeyDuplicate = -1605
JET_errAlreadyPrepared = -1607
JET_errKeyNotMade = -1608
JET_errUpdateNotPrepared = -1609
JET_wrnDataHasChanged = 1610
JET_errDataHasChanged = -1611
JET_wrnKeyChanged = 1618
JET_errLanguageNotSupported = -1619
JET_errDecompressionFailed = -1620
JET_errUpdateMustVersion = -1621
JET_errDecryptionFailed = -1622
JET_errEncryptionBadItag = -1623
JET_errTooManySorts = -1701
JET_errInvalidOnSort = -1702
JET_errTempFileOpenError = -1803
JET_errTooManyAttachedDatabases = -1805
JET_errDiskFull = -1808
JET_errPermissionDenied = -1809
JET_errFileNotFound = -1811
JET_errFileInvalidType = -1812
JET_wrnFileOpenReadOnly = 1813
JET_errFileAlreadyExists = -1814
JET_errAfterInitialization = -1850
JET_errLogCorrupted = -1852
JET_errInvalidOperation = -1906
JET_errAccessDenied = -1907
JET_wrnIdleFull = 1908
JET_errTooManySplits = -1909
JET_errSessionSharingViolation = -1910
JET_errEntryPointNotFound = -1911
JET_errSessionContextAlreadySet = -1912
JET_errSessionContextNotSetByThisThread = -1913
JET_errSessionInUse = -1914
JET_errRecordFormatConversionFailed = -1915
JET_errOneDatabasePerSession = -1916
JET_errRollbackError = -1917
JET_errFlushMapVersionUnsupported = -1918
JET_errFlushMapDatabaseMismatch = -1919
JET_errFlushMapUnrecoverable = -1920
JET_wrnDefragAlreadyRunning = 2000
JET_wrnDefragNotRunning = 2001
JET_errDatabaseAlreadyRunningMaintenance = -2004
JET_wrnCallbackNotRegistered = 2100
JET_errCallbackFailed = -2101
JET_errCallbackNotResolved = -2102
JET_errSpaceHintsInvalid = -2103
JET_errOSSnapshotInvalidSequence = -2401
JET_errOSSnapshotTimeOut = -2402
JET_errOSSnapshotNotAllowed = -2403
JET_errOSSnapshotInvalidSnapId = -2404
JET_errLSCallbackNotSpecified = -3000
JET_errLSAlreadySet = -3001
JET_errLSNotSet = -3002
JET_errFileIOSparse = -4000
JET_errFileIOBeyondEOF = -4001
JET_errFileIOAbort = -4002
JET_errFileIORetry = -4003
JET_errFileIOFail = -4004
JET_errFileCompressed = -4005
JET_BASE_NAME_LENGTH = 3
JET_bitDumpMinimum = 1
JET_bitDumpMaximum = 2
JET_bitDumpCacheMinimum = 4
JET_bitDumpCacheMaximum = 8
JET_bitDumpCacheIncludeDirtyPages = 16
JET_bitDumpCacheIncludeCachedPages = 32
JET_bitDumpCacheIncludeCorruptedPages = 64
JET_bitDumpCacheNoDecommit = 128
def _define_JetInit():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Storage.StructuredStorage.JET_INSTANCE))(('JetInit', windll['ESENT.dll']), ((1, 'pinstance'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetInit2():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Storage.StructuredStorage.JET_INSTANCE),UInt32)(('JetInit2', windll['ESENT.dll']), ((1, 'pinstance'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetInit3A():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Storage.StructuredStorage.JET_INSTANCE),POINTER(win32more.Storage.Jet.JET_RSTINFO_A_head),UInt32)(('JetInit3A', windll['ESENT.dll']), ((1, 'pinstance'),(1, 'prstInfo'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetInit3W():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Storage.StructuredStorage.JET_INSTANCE),POINTER(win32more.Storage.Jet.JET_RSTINFO_W_head),UInt32)(('JetInit3W', windll['ESENT.dll']), ((1, 'pinstance'),(1, 'prstInfo'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateInstanceA():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Storage.StructuredStorage.JET_INSTANCE),POINTER(SByte))(('JetCreateInstanceA', windll['ESENT.dll']), ((1, 'pinstance'),(1, 'szInstanceName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateInstanceW():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Storage.StructuredStorage.JET_INSTANCE),POINTER(UInt16))(('JetCreateInstanceW', windll['ESENT.dll']), ((1, 'pinstance'),(1, 'szInstanceName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateInstance2A():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Storage.StructuredStorage.JET_INSTANCE),POINTER(SByte),POINTER(SByte),UInt32)(('JetCreateInstance2A', windll['ESENT.dll']), ((1, 'pinstance'),(1, 'szInstanceName'),(1, 'szDisplayName'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateInstance2W():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Storage.StructuredStorage.JET_INSTANCE),POINTER(UInt16),POINTER(UInt16),UInt32)(('JetCreateInstance2W', windll['ESENT.dll']), ((1, 'pinstance'),(1, 'szInstanceName'),(1, 'szDisplayName'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetInstanceMiscInfo():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,c_void_p,UInt32,UInt32)(('JetGetInstanceMiscInfo', windll['ESENT.dll']), ((1, 'instance'),(1, 'pvResult'),(1, 'cbMax'),(1, 'InfoLevel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetTerm():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE)(('JetTerm', windll['ESENT.dll']), ((1, 'instance'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetTerm2():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,UInt32)(('JetTerm2', windll['ESENT.dll']), ((1, 'instance'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetStopService():
    try:
        return WINFUNCTYPE(Int32,)(('JetStopService', windll['ESENT.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetStopServiceInstance():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE)(('JetStopServiceInstance', windll['ESENT.dll']), ((1, 'instance'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetStopServiceInstance2():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,UInt32)(('JetStopServiceInstance2', windll['ESENT.dll']), ((1, 'instance'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetStopBackup():
    try:
        return WINFUNCTYPE(Int32,)(('JetStopBackup', windll['ESENT.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetStopBackupInstance():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE)(('JetStopBackupInstance', windll['ESENT.dll']), ((1, 'instance'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetSetSystemParameterA():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Storage.StructuredStorage.JET_INSTANCE),win32more.Storage.StructuredStorage.JET_SESID,UInt32,win32more.Storage.StructuredStorage.JET_API_PTR,POINTER(SByte))(('JetSetSystemParameterA', windll['ESENT.dll']), ((1, 'pinstance'),(1, 'sesid'),(1, 'paramid'),(1, 'lParam'),(1, 'szParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetSetSystemParameterW():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Storage.StructuredStorage.JET_INSTANCE),win32more.Storage.StructuredStorage.JET_SESID,UInt32,win32more.Storage.StructuredStorage.JET_API_PTR,POINTER(UInt16))(('JetSetSystemParameterW', windll['ESENT.dll']), ((1, 'pinstance'),(1, 'sesid'),(1, 'paramid'),(1, 'lParam'),(1, 'szParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetSystemParameterA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(win32more.Storage.StructuredStorage.JET_API_PTR),POINTER(SByte),UInt32)(('JetGetSystemParameterA', windll['ESENT.dll']), ((1, 'instance'),(1, 'sesid'),(1, 'paramid'),(1, 'plParam'),(1, 'szParam'),(1, 'cbMax'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetSystemParameterW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(win32more.Storage.StructuredStorage.JET_API_PTR),POINTER(UInt16),UInt32)(('JetGetSystemParameterW', windll['ESENT.dll']), ((1, 'instance'),(1, 'sesid'),(1, 'paramid'),(1, 'plParam'),(1, 'szParam'),(1, 'cbMax'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetEnableMultiInstanceA():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Storage.Jet.JET_SETSYSPARAM_A_head),UInt32,POINTER(UInt32))(('JetEnableMultiInstanceA', windll['ESENT.dll']), ((1, 'psetsysparam'),(1, 'csetsysparam'),(1, 'pcsetsucceed'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetEnableMultiInstanceW():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Storage.Jet.JET_SETSYSPARAM_W_head),UInt32,POINTER(UInt32))(('JetEnableMultiInstanceW', windll['ESENT.dll']), ((1, 'psetsysparam'),(1, 'csetsysparam'),(1, 'pcsetsucceed'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetThreadStats():
    try:
        return WINFUNCTYPE(Int32,c_void_p,UInt32)(('JetGetThreadStats', windll['ESENT.dll']), ((1, 'pvResult'),(1, 'cbMax'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetBeginSessionA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,POINTER(win32more.Storage.StructuredStorage.JET_SESID),POINTER(SByte),POINTER(SByte))(('JetBeginSessionA', windll['ESENT.dll']), ((1, 'instance'),(1, 'psesid'),(1, 'szUserName'),(1, 'szPassword'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetBeginSessionW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,POINTER(win32more.Storage.StructuredStorage.JET_SESID),POINTER(UInt16),POINTER(UInt16))(('JetBeginSessionW', windll['ESENT.dll']), ((1, 'instance'),(1, 'psesid'),(1, 'szUserName'),(1, 'szPassword'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetDupSession():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(win32more.Storage.StructuredStorage.JET_SESID))(('JetDupSession', windll['ESENT.dll']), ((1, 'sesid'),(1, 'psesid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetEndSession():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32)(('JetEndSession', windll['ESENT.dll']), ((1, 'sesid'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetVersion():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(UInt32))(('JetGetVersion', windll['ESENT.dll']), ((1, 'sesid'),(1, 'pwVersion'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetIdle():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32)(('JetIdle', windll['ESENT.dll']), ((1, 'sesid'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateDatabaseA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(SByte),POINTER(SByte),POINTER(UInt32),UInt32)(('JetCreateDatabaseA', windll['ESENT.dll']), ((1, 'sesid'),(1, 'szFilename'),(1, 'szConnect'),(1, 'pdbid'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateDatabaseW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(UInt16),POINTER(UInt16),POINTER(UInt32),UInt32)(('JetCreateDatabaseW', windll['ESENT.dll']), ((1, 'sesid'),(1, 'szFilename'),(1, 'szConnect'),(1, 'pdbid'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateDatabase2A():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(SByte),UInt32,POINTER(UInt32),UInt32)(('JetCreateDatabase2A', windll['ESENT.dll']), ((1, 'sesid'),(1, 'szFilename'),(1, 'cpgDatabaseSizeMax'),(1, 'pdbid'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateDatabase2W():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(UInt16),UInt32,POINTER(UInt32),UInt32)(('JetCreateDatabase2W', windll['ESENT.dll']), ((1, 'sesid'),(1, 'szFilename'),(1, 'cpgDatabaseSizeMax'),(1, 'pdbid'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetAttachDatabaseA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(SByte),UInt32)(('JetAttachDatabaseA', windll['ESENT.dll']), ((1, 'sesid'),(1, 'szFilename'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetAttachDatabaseW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(UInt16),UInt32)(('JetAttachDatabaseW', windll['ESENT.dll']), ((1, 'sesid'),(1, 'szFilename'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetAttachDatabase2A():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(SByte),UInt32,UInt32)(('JetAttachDatabase2A', windll['ESENT.dll']), ((1, 'sesid'),(1, 'szFilename'),(1, 'cpgDatabaseSizeMax'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetAttachDatabase2W():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(UInt16),UInt32,UInt32)(('JetAttachDatabase2W', windll['ESENT.dll']), ((1, 'sesid'),(1, 'szFilename'),(1, 'cpgDatabaseSizeMax'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetDetachDatabaseA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(SByte))(('JetDetachDatabaseA', windll['ESENT.dll']), ((1, 'sesid'),(1, 'szFilename'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetDetachDatabaseW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(UInt16))(('JetDetachDatabaseW', windll['ESENT.dll']), ((1, 'sesid'),(1, 'szFilename'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetDetachDatabase2A():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(SByte),UInt32)(('JetDetachDatabase2A', windll['ESENT.dll']), ((1, 'sesid'),(1, 'szFilename'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetDetachDatabase2W():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(UInt16),UInt32)(('JetDetachDatabase2W', windll['ESENT.dll']), ((1, 'sesid'),(1, 'szFilename'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetObjectInfoA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,UInt32,POINTER(SByte),POINTER(SByte),c_void_p,UInt32,UInt32)(('JetGetObjectInfoA', windll['ESENT.dll']), ((1, 'sesid'),(1, 'dbid'),(1, 'objtyp'),(1, 'szContainerName'),(1, 'szObjectName'),(1, 'pvResult'),(1, 'cbMax'),(1, 'InfoLevel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetObjectInfoW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,UInt32,POINTER(UInt16),POINTER(UInt16),c_void_p,UInt32,UInt32)(('JetGetObjectInfoW', windll['ESENT.dll']), ((1, 'sesid'),(1, 'dbid'),(1, 'objtyp'),(1, 'szContainerName'),(1, 'szObjectName'),(1, 'pvResult'),(1, 'cbMax'),(1, 'InfoLevel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetTableInfoA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,c_void_p,UInt32,UInt32)(('JetGetTableInfoA', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'pvResult'),(1, 'cbMax'),(1, 'InfoLevel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetTableInfoW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,c_void_p,UInt32,UInt32)(('JetGetTableInfoW', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'pvResult'),(1, 'cbMax'),(1, 'InfoLevel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateTableA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(SByte),UInt32,UInt32,POINTER(win32more.Storage.StructuredStorage.JET_TABLEID))(('JetCreateTableA', windll['ESENT.dll']), ((1, 'sesid'),(1, 'dbid'),(1, 'szTableName'),(1, 'lPages'),(1, 'lDensity'),(1, 'ptableid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateTableW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(UInt16),UInt32,UInt32,POINTER(win32more.Storage.StructuredStorage.JET_TABLEID))(('JetCreateTableW', windll['ESENT.dll']), ((1, 'sesid'),(1, 'dbid'),(1, 'szTableName'),(1, 'lPages'),(1, 'lDensity'),(1, 'ptableid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateTableColumnIndexA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(win32more.Storage.Jet.JET_TABLECREATE_A_head))(('JetCreateTableColumnIndexA', windll['ESENT.dll']), ((1, 'sesid'),(1, 'dbid'),(1, 'ptablecreate'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateTableColumnIndexW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(win32more.Storage.Jet.JET_TABLECREATE_W_head))(('JetCreateTableColumnIndexW', windll['ESENT.dll']), ((1, 'sesid'),(1, 'dbid'),(1, 'ptablecreate'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateTableColumnIndex2A():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(win32more.Storage.Jet.JET_TABLECREATE2_A_head))(('JetCreateTableColumnIndex2A', windll['ESENT.dll']), ((1, 'sesid'),(1, 'dbid'),(1, 'ptablecreate'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateTableColumnIndex2W():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(win32more.Storage.Jet.JET_TABLECREATE2_W_head))(('JetCreateTableColumnIndex2W', windll['ESENT.dll']), ((1, 'sesid'),(1, 'dbid'),(1, 'ptablecreate'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateTableColumnIndex3A():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(win32more.Storage.Jet.JET_TABLECREATE3_A_head))(('JetCreateTableColumnIndex3A', windll['ESENT.dll']), ((1, 'sesid'),(1, 'dbid'),(1, 'ptablecreate'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateTableColumnIndex3W():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(win32more.Storage.Jet.JET_TABLECREATE3_W_head))(('JetCreateTableColumnIndex3W', windll['ESENT.dll']), ((1, 'sesid'),(1, 'dbid'),(1, 'ptablecreate'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateTableColumnIndex4A():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(win32more.Storage.Jet.JET_TABLECREATE4_A_head))(('JetCreateTableColumnIndex4A', windll['ESENT.dll']), ((1, 'sesid'),(1, 'dbid'),(1, 'ptablecreate'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateTableColumnIndex4W():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(win32more.Storage.Jet.JET_TABLECREATE4_W_head))(('JetCreateTableColumnIndex4W', windll['ESENT.dll']), ((1, 'sesid'),(1, 'dbid'),(1, 'ptablecreate'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetDeleteTableA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(SByte))(('JetDeleteTableA', windll['ESENT.dll']), ((1, 'sesid'),(1, 'dbid'),(1, 'szTableName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetDeleteTableW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(UInt16))(('JetDeleteTableW', windll['ESENT.dll']), ((1, 'sesid'),(1, 'dbid'),(1, 'szTableName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetRenameTableA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(SByte),POINTER(SByte))(('JetRenameTableA', windll['ESENT.dll']), ((1, 'sesid'),(1, 'dbid'),(1, 'szName'),(1, 'szNameNew'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetRenameTableW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(UInt16),POINTER(UInt16))(('JetRenameTableW', windll['ESENT.dll']), ((1, 'sesid'),(1, 'dbid'),(1, 'szName'),(1, 'szNameNew'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetTableColumnInfoA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(SByte),c_void_p,UInt32,UInt32)(('JetGetTableColumnInfoA', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'szColumnName'),(1, 'pvResult'),(1, 'cbMax'),(1, 'InfoLevel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetTableColumnInfoW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(UInt16),c_void_p,UInt32,UInt32)(('JetGetTableColumnInfoW', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'szColumnName'),(1, 'pvResult'),(1, 'cbMax'),(1, 'InfoLevel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetColumnInfoA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(SByte),POINTER(SByte),c_void_p,UInt32,UInt32)(('JetGetColumnInfoA', windll['ESENT.dll']), ((1, 'sesid'),(1, 'dbid'),(1, 'szTableName'),(1, 'pColumnNameOrId'),(1, 'pvResult'),(1, 'cbMax'),(1, 'InfoLevel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetColumnInfoW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(UInt16),POINTER(UInt16),c_void_p,UInt32,UInt32)(('JetGetColumnInfoW', windll['ESENT.dll']), ((1, 'sesid'),(1, 'dbid'),(1, 'szTableName'),(1, 'pwColumnNameOrId'),(1, 'pvResult'),(1, 'cbMax'),(1, 'InfoLevel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetAddColumnA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(SByte),POINTER(win32more.Storage.Jet.JET_COLUMNDEF_head),c_void_p,UInt32,POINTER(UInt32))(('JetAddColumnA', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'szColumnName'),(1, 'pcolumndef'),(1, 'pvDefault'),(1, 'cbDefault'),(1, 'pcolumnid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetAddColumnW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(UInt16),POINTER(win32more.Storage.Jet.JET_COLUMNDEF_head),c_void_p,UInt32,POINTER(UInt32))(('JetAddColumnW', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'szColumnName'),(1, 'pcolumndef'),(1, 'pvDefault'),(1, 'cbDefault'),(1, 'pcolumnid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetDeleteColumnA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(SByte))(('JetDeleteColumnA', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'szColumnName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetDeleteColumnW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(UInt16))(('JetDeleteColumnW', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'szColumnName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetDeleteColumn2A():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(SByte),UInt32)(('JetDeleteColumn2A', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'szColumnName'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetDeleteColumn2W():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(UInt16),UInt32)(('JetDeleteColumn2W', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'szColumnName'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetRenameColumnA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(SByte),POINTER(SByte),UInt32)(('JetRenameColumnA', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'szName'),(1, 'szNameNew'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetRenameColumnW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(UInt16),POINTER(UInt16),UInt32)(('JetRenameColumnW', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'szName'),(1, 'szNameNew'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetSetColumnDefaultValueA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(SByte),POINTER(SByte),c_void_p,UInt32,UInt32)(('JetSetColumnDefaultValueA', windll['ESENT.dll']), ((1, 'sesid'),(1, 'dbid'),(1, 'szTableName'),(1, 'szColumnName'),(1, 'pvData'),(1, 'cbData'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetSetColumnDefaultValueW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(UInt16),POINTER(UInt16),c_void_p,UInt32,UInt32)(('JetSetColumnDefaultValueW', windll['ESENT.dll']), ((1, 'sesid'),(1, 'dbid'),(1, 'szTableName'),(1, 'szColumnName'),(1, 'pvData'),(1, 'cbData'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetTableIndexInfoA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(SByte),c_void_p,UInt32,UInt32)(('JetGetTableIndexInfoA', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'szIndexName'),(1, 'pvResult'),(1, 'cbResult'),(1, 'InfoLevel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetTableIndexInfoW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(UInt16),c_void_p,UInt32,UInt32)(('JetGetTableIndexInfoW', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'szIndexName'),(1, 'pvResult'),(1, 'cbResult'),(1, 'InfoLevel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetIndexInfoA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(SByte),POINTER(SByte),c_void_p,UInt32,UInt32)(('JetGetIndexInfoA', windll['ESENT.dll']), ((1, 'sesid'),(1, 'dbid'),(1, 'szTableName'),(1, 'szIndexName'),(1, 'pvResult'),(1, 'cbResult'),(1, 'InfoLevel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetIndexInfoW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(UInt16),POINTER(UInt16),c_void_p,UInt32,UInt32)(('JetGetIndexInfoW', windll['ESENT.dll']), ((1, 'sesid'),(1, 'dbid'),(1, 'szTableName'),(1, 'szIndexName'),(1, 'pvResult'),(1, 'cbResult'),(1, 'InfoLevel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateIndexA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(SByte),UInt32,win32more.Foundation.PSTR,UInt32,UInt32)(('JetCreateIndexA', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'szIndexName'),(1, 'grbit'),(1, 'szKey'),(1, 'cbKey'),(1, 'lDensity'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateIndexW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(UInt16),UInt32,win32more.Foundation.PWSTR,UInt32,UInt32)(('JetCreateIndexW', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'szIndexName'),(1, 'grbit'),(1, 'szKey'),(1, 'cbKey'),(1, 'lDensity'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateIndex2A():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(win32more.Storage.Jet.JET_INDEXCREATE_A_head),UInt32)(('JetCreateIndex2A', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'pindexcreate'),(1, 'cIndexCreate'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateIndex2W():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(win32more.Storage.Jet.JET_INDEXCREATE_W_head),UInt32)(('JetCreateIndex2W', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'pindexcreate'),(1, 'cIndexCreate'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateIndex3A():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(win32more.Storage.Jet.JET_INDEXCREATE2_A_head),UInt32)(('JetCreateIndex3A', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'pindexcreate'),(1, 'cIndexCreate'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateIndex3W():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(win32more.Storage.Jet.JET_INDEXCREATE2_W_head),UInt32)(('JetCreateIndex3W', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'pindexcreate'),(1, 'cIndexCreate'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateIndex4A():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(win32more.Storage.Jet.JET_INDEXCREATE3_A_head),UInt32)(('JetCreateIndex4A', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'pindexcreate'),(1, 'cIndexCreate'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateIndex4W():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(win32more.Storage.Jet.JET_INDEXCREATE3_W_head),UInt32)(('JetCreateIndex4W', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'pindexcreate'),(1, 'cIndexCreate'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetDeleteIndexA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(SByte))(('JetDeleteIndexA', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'szIndexName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetDeleteIndexW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(UInt16))(('JetDeleteIndexW', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'szIndexName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetBeginTransaction():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID)(('JetBeginTransaction', windll['ESENT.dll']), ((1, 'sesid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetBeginTransaction2():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32)(('JetBeginTransaction2', windll['ESENT.dll']), ((1, 'sesid'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetBeginTransaction3():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,Int64,UInt32)(('JetBeginTransaction3', windll['ESENT.dll']), ((1, 'sesid'),(1, 'trxid'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCommitTransaction():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32)(('JetCommitTransaction', windll['ESENT.dll']), ((1, 'sesid'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCommitTransaction2():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,UInt32,POINTER(win32more.Storage.Jet.JET_COMMIT_ID_head))(('JetCommitTransaction2', windll['ESENT.dll']), ((1, 'sesid'),(1, 'grbit'),(1, 'cmsecDurableCommit'),(1, 'pCommitId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetRollback():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32)(('JetRollback', windll['ESENT.dll']), ((1, 'sesid'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetDatabaseInfoA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,c_void_p,UInt32,UInt32)(('JetGetDatabaseInfoA', windll['ESENT.dll']), ((1, 'sesid'),(1, 'dbid'),(1, 'pvResult'),(1, 'cbMax'),(1, 'InfoLevel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetDatabaseInfoW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,c_void_p,UInt32,UInt32)(('JetGetDatabaseInfoW', windll['ESENT.dll']), ((1, 'sesid'),(1, 'dbid'),(1, 'pvResult'),(1, 'cbMax'),(1, 'InfoLevel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetDatabaseFileInfoA():
    try:
        return WINFUNCTYPE(Int32,POINTER(SByte),c_void_p,UInt32,UInt32)(('JetGetDatabaseFileInfoA', windll['ESENT.dll']), ((1, 'szDatabaseName'),(1, 'pvResult'),(1, 'cbMax'),(1, 'InfoLevel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetDatabaseFileInfoW():
    try:
        return WINFUNCTYPE(Int32,POINTER(UInt16),c_void_p,UInt32,UInt32)(('JetGetDatabaseFileInfoW', windll['ESENT.dll']), ((1, 'szDatabaseName'),(1, 'pvResult'),(1, 'cbMax'),(1, 'InfoLevel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOpenDatabaseA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(SByte),POINTER(SByte),POINTER(UInt32),UInt32)(('JetOpenDatabaseA', windll['ESENT.dll']), ((1, 'sesid'),(1, 'szFilename'),(1, 'szConnect'),(1, 'pdbid'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOpenDatabaseW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(UInt16),POINTER(UInt16),POINTER(UInt32),UInt32)(('JetOpenDatabaseW', windll['ESENT.dll']), ((1, 'sesid'),(1, 'szFilename'),(1, 'szConnect'),(1, 'pdbid'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCloseDatabase():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,UInt32)(('JetCloseDatabase', windll['ESENT.dll']), ((1, 'sesid'),(1, 'dbid'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOpenTableA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(SByte),c_void_p,UInt32,UInt32,POINTER(win32more.Storage.StructuredStorage.JET_TABLEID))(('JetOpenTableA', windll['ESENT.dll']), ((1, 'sesid'),(1, 'dbid'),(1, 'szTableName'),(1, 'pvParameters'),(1, 'cbParameters'),(1, 'grbit'),(1, 'ptableid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOpenTableW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(UInt16),c_void_p,UInt32,UInt32,POINTER(win32more.Storage.StructuredStorage.JET_TABLEID))(('JetOpenTableW', windll['ESENT.dll']), ((1, 'sesid'),(1, 'dbid'),(1, 'szTableName'),(1, 'pvParameters'),(1, 'cbParameters'),(1, 'grbit'),(1, 'ptableid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetSetTableSequential():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,UInt32)(('JetSetTableSequential', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetResetTableSequential():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,UInt32)(('JetResetTableSequential', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCloseTable():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID)(('JetCloseTable', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetDelete():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID)(('JetDelete', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetUpdate():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,c_void_p,UInt32,POINTER(UInt32))(('JetUpdate', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'pvBookmark'),(1, 'cbBookmark'),(1, 'pcbActual'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetUpdate2():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,c_void_p,UInt32,POINTER(UInt32),UInt32)(('JetUpdate2', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'pvBookmark'),(1, 'cbBookmark'),(1, 'pcbActual'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetEscrowUpdate():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,UInt32,c_void_p,UInt32,c_void_p,UInt32,POINTER(UInt32),UInt32)(('JetEscrowUpdate', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'columnid'),(1, 'pv'),(1, 'cbMax'),(1, 'pvOld'),(1, 'cbOldMax'),(1, 'pcbOldActual'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetRetrieveColumn():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,UInt32,c_void_p,UInt32,POINTER(UInt32),UInt32,POINTER(win32more.Storage.Jet.JET_RETINFO_head))(('JetRetrieveColumn', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'columnid'),(1, 'pvData'),(1, 'cbData'),(1, 'pcbActual'),(1, 'grbit'),(1, 'pretinfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetRetrieveColumns():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(win32more.Storage.Jet.JET_RETRIEVECOLUMN_head),UInt32)(('JetRetrieveColumns', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'pretrievecolumn'),(1, 'cretrievecolumn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetEnumerateColumns():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,UInt32,POINTER(win32more.Storage.Jet.JET_ENUMCOLUMNID_head),POINTER(UInt32),POINTER(POINTER(win32more.Storage.Jet.JET_ENUMCOLUMN_head)),win32more.Storage.Jet.JET_PFNREALLOC,c_void_p,UInt32,UInt32)(('JetEnumerateColumns', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'cEnumColumnId'),(1, 'rgEnumColumnId'),(1, 'pcEnumColumn'),(1, 'prgEnumColumn'),(1, 'pfnRealloc'),(1, 'pvReallocContext'),(1, 'cbDataMost'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetRecordSize():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(win32more.Storage.Jet.JET_RECSIZE_head),UInt32)(('JetGetRecordSize', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'precsize'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetRecordSize2():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(win32more.Storage.Jet.JET_RECSIZE2_head),UInt32)(('JetGetRecordSize2', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'precsize'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetSetColumn():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,UInt32,c_void_p,UInt32,UInt32,POINTER(win32more.Storage.Jet.JET_SETINFO_head))(('JetSetColumn', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'columnid'),(1, 'pvData'),(1, 'cbData'),(1, 'grbit'),(1, 'psetinfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetSetColumns():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(win32more.Storage.Jet.JET_SETCOLUMN_head),UInt32)(('JetSetColumns', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'psetcolumn'),(1, 'csetcolumn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetPrepareUpdate():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,UInt32)(('JetPrepareUpdate', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'prep'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetRecordPosition():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(win32more.Storage.Jet.JET_RECPOS_head),UInt32)(('JetGetRecordPosition', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'precpos'),(1, 'cbRecpos'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGotoPosition():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(win32more.Storage.Jet.JET_RECPOS_head))(('JetGotoPosition', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'precpos'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetCursorInfo():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,c_void_p,UInt32,UInt32)(('JetGetCursorInfo', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'pvResult'),(1, 'cbMax'),(1, 'InfoLevel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetDupCursor():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(win32more.Storage.StructuredStorage.JET_TABLEID),UInt32)(('JetDupCursor', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'ptableid'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetCurrentIndexA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(SByte),UInt32)(('JetGetCurrentIndexA', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'szIndexName'),(1, 'cbIndexName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetCurrentIndexW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(UInt16),UInt32)(('JetGetCurrentIndexW', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'szIndexName'),(1, 'cbIndexName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetSetCurrentIndexA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(SByte))(('JetSetCurrentIndexA', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'szIndexName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetSetCurrentIndexW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(UInt16))(('JetSetCurrentIndexW', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'szIndexName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetSetCurrentIndex2A():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(SByte),UInt32)(('JetSetCurrentIndex2A', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'szIndexName'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetSetCurrentIndex2W():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(UInt16),UInt32)(('JetSetCurrentIndex2W', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'szIndexName'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetSetCurrentIndex3A():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(SByte),UInt32,UInt32)(('JetSetCurrentIndex3A', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'szIndexName'),(1, 'grbit'),(1, 'itagSequence'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetSetCurrentIndex3W():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(UInt16),UInt32,UInt32)(('JetSetCurrentIndex3W', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'szIndexName'),(1, 'grbit'),(1, 'itagSequence'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetSetCurrentIndex4A():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(SByte),POINTER(win32more.Storage.Jet.JET_INDEXID_head),UInt32,UInt32)(('JetSetCurrentIndex4A', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'szIndexName'),(1, 'pindexid'),(1, 'grbit'),(1, 'itagSequence'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetSetCurrentIndex4W():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(UInt16),POINTER(win32more.Storage.Jet.JET_INDEXID_head),UInt32,UInt32)(('JetSetCurrentIndex4W', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'szIndexName'),(1, 'pindexid'),(1, 'grbit'),(1, 'itagSequence'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetMove():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,Int32,UInt32)(('JetMove', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'cRow'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetSetCursorFilter():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(win32more.Storage.Jet.JET_INDEX_COLUMN_head),UInt32,UInt32)(('JetSetCursorFilter', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'rgColumnFilters'),(1, 'cColumnFilters'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetLock():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,UInt32)(('JetGetLock', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetMakeKey():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,c_void_p,UInt32,UInt32)(('JetMakeKey', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'pvData'),(1, 'cbData'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetSeek():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,UInt32)(('JetSeek', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetPrereadKeys():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(c_void_p),POINTER(UInt32),Int32,POINTER(Int32),UInt32)(('JetPrereadKeys', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'rgpvKeys'),(1, 'rgcbKeys'),(1, 'ckeys'),(1, 'pckeysPreread'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetPrereadIndexRanges():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(win32more.Storage.Jet.JET_INDEX_RANGE_head),UInt32,POINTER(UInt32),POINTER(UInt32),UInt32,UInt32)(('JetPrereadIndexRanges', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'rgIndexRanges'),(1, 'cIndexRanges'),(1, 'pcRangesPreread'),(1, 'rgcolumnidPreread'),(1, 'ccolumnidPreread'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetBookmark():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,c_void_p,UInt32,POINTER(UInt32))(('JetGetBookmark', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'pvBookmark'),(1, 'cbMax'),(1, 'pcbActual'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetSecondaryIndexBookmark():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,c_void_p,UInt32,POINTER(UInt32),c_void_p,UInt32,POINTER(UInt32),UInt32)(('JetGetSecondaryIndexBookmark', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'pvSecondaryKey'),(1, 'cbSecondaryKeyMax'),(1, 'pcbSecondaryKeyActual'),(1, 'pvPrimaryBookmark'),(1, 'cbPrimaryBookmarkMax'),(1, 'pcbPrimaryBookmarkActual'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCompactA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(SByte),POINTER(SByte),win32more.Storage.Jet.JET_PFNSTATUS,POINTER(win32more.Storage.Jet.JET_CONVERT_A_head),UInt32)(('JetCompactA', windll['ESENT.dll']), ((1, 'sesid'),(1, 'szDatabaseSrc'),(1, 'szDatabaseDest'),(1, 'pfnStatus'),(1, 'pconvert'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCompactW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(UInt16),POINTER(UInt16),win32more.Storage.Jet.JET_PFNSTATUS,POINTER(win32more.Storage.Jet.JET_CONVERT_W_head),UInt32)(('JetCompactW', windll['ESENT.dll']), ((1, 'sesid'),(1, 'szDatabaseSrc'),(1, 'szDatabaseDest'),(1, 'pfnStatus'),(1, 'pconvert'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetDefragmentA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(SByte),POINTER(UInt32),POINTER(UInt32),UInt32)(('JetDefragmentA', windll['ESENT.dll']), ((1, 'sesid'),(1, 'dbid'),(1, 'szTableName'),(1, 'pcPasses'),(1, 'pcSeconds'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetDefragmentW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(UInt16),POINTER(UInt32),POINTER(UInt32),UInt32)(('JetDefragmentW', windll['ESENT.dll']), ((1, 'sesid'),(1, 'dbid'),(1, 'szTableName'),(1, 'pcPasses'),(1, 'pcSeconds'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetDefragment2A():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(SByte),POINTER(UInt32),POINTER(UInt32),win32more.Storage.Jet.JET_CALLBACK,UInt32)(('JetDefragment2A', windll['ESENT.dll']), ((1, 'sesid'),(1, 'dbid'),(1, 'szTableName'),(1, 'pcPasses'),(1, 'pcSeconds'),(1, 'callback'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetDefragment2W():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(UInt16),POINTER(UInt32),POINTER(UInt32),win32more.Storage.Jet.JET_CALLBACK,UInt32)(('JetDefragment2W', windll['ESENT.dll']), ((1, 'sesid'),(1, 'dbid'),(1, 'szTableName'),(1, 'pcPasses'),(1, 'pcSeconds'),(1, 'callback'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetDefragment3A():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(SByte),POINTER(SByte),POINTER(UInt32),POINTER(UInt32),win32more.Storage.Jet.JET_CALLBACK,c_void_p,UInt32)(('JetDefragment3A', windll['ESENT.dll']), ((1, 'sesid'),(1, 'szDatabaseName'),(1, 'szTableName'),(1, 'pcPasses'),(1, 'pcSeconds'),(1, 'callback'),(1, 'pvContext'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetDefragment3W():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(UInt16),POINTER(UInt16),POINTER(UInt32),POINTER(UInt32),win32more.Storage.Jet.JET_CALLBACK,c_void_p,UInt32)(('JetDefragment3W', windll['ESENT.dll']), ((1, 'sesid'),(1, 'szDatabaseName'),(1, 'szTableName'),(1, 'pcPasses'),(1, 'pcSeconds'),(1, 'callback'),(1, 'pvContext'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetSetDatabaseSizeA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(SByte),UInt32,POINTER(UInt32))(('JetSetDatabaseSizeA', windll['ESENT.dll']), ((1, 'sesid'),(1, 'szDatabaseName'),(1, 'cpg'),(1, 'pcpgReal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetSetDatabaseSizeW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(UInt16),UInt32,POINTER(UInt32))(('JetSetDatabaseSizeW', windll['ESENT.dll']), ((1, 'sesid'),(1, 'szDatabaseName'),(1, 'cpg'),(1, 'pcpgReal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGrowDatabase():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,UInt32,POINTER(UInt32))(('JetGrowDatabase', windll['ESENT.dll']), ((1, 'sesid'),(1, 'dbid'),(1, 'cpg'),(1, 'pcpgReal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetResizeDatabase():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,UInt32,POINTER(UInt32),UInt32)(('JetResizeDatabase', windll['ESENT.dll']), ((1, 'sesid'),(1, 'dbid'),(1, 'cpgTarget'),(1, 'pcpgActual'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetSetSessionContext():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_API_PTR)(('JetSetSessionContext', windll['ESENT.dll']), ((1, 'sesid'),(1, 'ulContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetResetSessionContext():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID)(('JetResetSessionContext', windll['ESENT.dll']), ((1, 'sesid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGotoBookmark():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,c_void_p,UInt32)(('JetGotoBookmark', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'pvBookmark'),(1, 'cbBookmark'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGotoSecondaryIndexBookmark():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,c_void_p,UInt32,c_void_p,UInt32,UInt32)(('JetGotoSecondaryIndexBookmark', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'pvSecondaryKey'),(1, 'cbSecondaryKey'),(1, 'pvPrimaryBookmark'),(1, 'cbPrimaryBookmark'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetIntersectIndexes():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(win32more.Storage.Jet.JET_INDEXRANGE_head),UInt32,POINTER(win32more.Storage.Jet.JET_RECORDLIST_head),UInt32)(('JetIntersectIndexes', windll['ESENT.dll']), ((1, 'sesid'),(1, 'rgindexrange'),(1, 'cindexrange'),(1, 'precordlist'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetComputeStats():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID)(('JetComputeStats', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOpenTempTable():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(win32more.Storage.Jet.JET_COLUMNDEF_head),UInt32,UInt32,POINTER(win32more.Storage.StructuredStorage.JET_TABLEID),POINTER(UInt32))(('JetOpenTempTable', windll['ESENT.dll']), ((1, 'sesid'),(1, 'prgcolumndef'),(1, 'ccolumn'),(1, 'grbit'),(1, 'ptableid'),(1, 'prgcolumnid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOpenTempTable2():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(win32more.Storage.Jet.JET_COLUMNDEF_head),UInt32,UInt32,UInt32,POINTER(win32more.Storage.StructuredStorage.JET_TABLEID),POINTER(UInt32))(('JetOpenTempTable2', windll['ESENT.dll']), ((1, 'sesid'),(1, 'prgcolumndef'),(1, 'ccolumn'),(1, 'lcid'),(1, 'grbit'),(1, 'ptableid'),(1, 'prgcolumnid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOpenTempTable3():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(win32more.Storage.Jet.JET_COLUMNDEF_head),UInt32,POINTER(win32more.Storage.Jet.JET_UNICODEINDEX_head),UInt32,POINTER(win32more.Storage.StructuredStorage.JET_TABLEID),POINTER(UInt32))(('JetOpenTempTable3', windll['ESENT.dll']), ((1, 'sesid'),(1, 'prgcolumndef'),(1, 'ccolumn'),(1, 'pidxunicode'),(1, 'grbit'),(1, 'ptableid'),(1, 'prgcolumnid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOpenTemporaryTable():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(win32more.Storage.Jet.JET_OPENTEMPORARYTABLE_head))(('JetOpenTemporaryTable', windll['ESENT.dll']), ((1, 'sesid'),(1, 'popentemporarytable'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOpenTemporaryTable2():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(win32more.Storage.Jet.JET_OPENTEMPORARYTABLE2_head))(('JetOpenTemporaryTable2', windll['ESENT.dll']), ((1, 'sesid'),(1, 'popentemporarytable'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetBackupA():
    try:
        return WINFUNCTYPE(Int32,POINTER(SByte),UInt32,win32more.Storage.Jet.JET_PFNSTATUS)(('JetBackupA', windll['ESENT.dll']), ((1, 'szBackupPath'),(1, 'grbit'),(1, 'pfnStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetBackupW():
    try:
        return WINFUNCTYPE(Int32,POINTER(UInt16),UInt32,win32more.Storage.Jet.JET_PFNSTATUS)(('JetBackupW', windll['ESENT.dll']), ((1, 'szBackupPath'),(1, 'grbit'),(1, 'pfnStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetBackupInstanceA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,POINTER(SByte),UInt32,win32more.Storage.Jet.JET_PFNSTATUS)(('JetBackupInstanceA', windll['ESENT.dll']), ((1, 'instance'),(1, 'szBackupPath'),(1, 'grbit'),(1, 'pfnStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetBackupInstanceW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,POINTER(UInt16),UInt32,win32more.Storage.Jet.JET_PFNSTATUS)(('JetBackupInstanceW', windll['ESENT.dll']), ((1, 'instance'),(1, 'szBackupPath'),(1, 'grbit'),(1, 'pfnStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetRestoreA():
    try:
        return WINFUNCTYPE(Int32,POINTER(SByte),win32more.Storage.Jet.JET_PFNSTATUS)(('JetRestoreA', windll['ESENT.dll']), ((1, 'szSource'),(1, 'pfn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetRestoreW():
    try:
        return WINFUNCTYPE(Int32,POINTER(UInt16),win32more.Storage.Jet.JET_PFNSTATUS)(('JetRestoreW', windll['ESENT.dll']), ((1, 'szSource'),(1, 'pfn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetRestore2A():
    try:
        return WINFUNCTYPE(Int32,POINTER(SByte),POINTER(SByte),win32more.Storage.Jet.JET_PFNSTATUS)(('JetRestore2A', windll['ESENT.dll']), ((1, 'sz'),(1, 'szDest'),(1, 'pfn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetRestore2W():
    try:
        return WINFUNCTYPE(Int32,POINTER(UInt16),POINTER(UInt16),win32more.Storage.Jet.JET_PFNSTATUS)(('JetRestore2W', windll['ESENT.dll']), ((1, 'sz'),(1, 'szDest'),(1, 'pfn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetRestoreInstanceA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,POINTER(SByte),POINTER(SByte),win32more.Storage.Jet.JET_PFNSTATUS)(('JetRestoreInstanceA', windll['ESENT.dll']), ((1, 'instance'),(1, 'sz'),(1, 'szDest'),(1, 'pfn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetRestoreInstanceW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,POINTER(UInt16),POINTER(UInt16),win32more.Storage.Jet.JET_PFNSTATUS)(('JetRestoreInstanceW', windll['ESENT.dll']), ((1, 'instance'),(1, 'sz'),(1, 'szDest'),(1, 'pfn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetSetIndexRange():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,UInt32)(('JetSetIndexRange', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableidSrc'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetIndexRecordCount():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(UInt32),UInt32)(('JetIndexRecordCount', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'pcrec'),(1, 'crecMax'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetRetrieveKey():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,c_void_p,UInt32,POINTER(UInt32),UInt32)(('JetRetrieveKey', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'pvKey'),(1, 'cbMax'),(1, 'pcbActual'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetBeginExternalBackup():
    try:
        return WINFUNCTYPE(Int32,UInt32)(('JetBeginExternalBackup', windll['ESENT.dll']), ((1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetBeginExternalBackupInstance():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,UInt32)(('JetBeginExternalBackupInstance', windll['ESENT.dll']), ((1, 'instance'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetAttachInfoA():
    try:
        return WINFUNCTYPE(Int32,POINTER(SByte),UInt32,POINTER(UInt32))(('JetGetAttachInfoA', windll['ESENT.dll']), ((1, 'szzDatabases'),(1, 'cbMax'),(1, 'pcbActual'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetAttachInfoW():
    try:
        return WINFUNCTYPE(Int32,POINTER(UInt16),UInt32,POINTER(UInt32))(('JetGetAttachInfoW', windll['ESENT.dll']), ((1, 'wszzDatabases'),(1, 'cbMax'),(1, 'pcbActual'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetAttachInfoInstanceA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,POINTER(SByte),UInt32,POINTER(UInt32))(('JetGetAttachInfoInstanceA', windll['ESENT.dll']), ((1, 'instance'),(1, 'szzDatabases'),(1, 'cbMax'),(1, 'pcbActual'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetAttachInfoInstanceW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,POINTER(UInt16),UInt32,POINTER(UInt32))(('JetGetAttachInfoInstanceW', windll['ESENT.dll']), ((1, 'instance'),(1, 'szzDatabases'),(1, 'cbMax'),(1, 'pcbActual'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOpenFileA():
    try:
        return WINFUNCTYPE(Int32,POINTER(SByte),POINTER(win32more.Storage.StructuredStorage.JET_HANDLE),POINTER(UInt32),POINTER(UInt32))(('JetOpenFileA', windll['ESENT.dll']), ((1, 'szFileName'),(1, 'phfFile'),(1, 'pulFileSizeLow'),(1, 'pulFileSizeHigh'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOpenFileW():
    try:
        return WINFUNCTYPE(Int32,POINTER(UInt16),POINTER(win32more.Storage.StructuredStorage.JET_HANDLE),POINTER(UInt32),POINTER(UInt32))(('JetOpenFileW', windll['ESENT.dll']), ((1, 'szFileName'),(1, 'phfFile'),(1, 'pulFileSizeLow'),(1, 'pulFileSizeHigh'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOpenFileInstanceA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,POINTER(SByte),POINTER(win32more.Storage.StructuredStorage.JET_HANDLE),POINTER(UInt32),POINTER(UInt32))(('JetOpenFileInstanceA', windll['ESENT.dll']), ((1, 'instance'),(1, 'szFileName'),(1, 'phfFile'),(1, 'pulFileSizeLow'),(1, 'pulFileSizeHigh'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOpenFileInstanceW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,POINTER(UInt16),POINTER(win32more.Storage.StructuredStorage.JET_HANDLE),POINTER(UInt32),POINTER(UInt32))(('JetOpenFileInstanceW', windll['ESENT.dll']), ((1, 'instance'),(1, 'szFileName'),(1, 'phfFile'),(1, 'pulFileSizeLow'),(1, 'pulFileSizeHigh'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetReadFile():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_HANDLE,c_void_p,UInt32,POINTER(UInt32))(('JetReadFile', windll['ESENT.dll']), ((1, 'hfFile'),(1, 'pv'),(1, 'cb'),(1, 'pcbActual'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetReadFileInstance():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,win32more.Storage.StructuredStorage.JET_HANDLE,c_void_p,UInt32,POINTER(UInt32))(('JetReadFileInstance', windll['ESENT.dll']), ((1, 'instance'),(1, 'hfFile'),(1, 'pv'),(1, 'cb'),(1, 'pcbActual'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCloseFile():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_HANDLE)(('JetCloseFile', windll['ESENT.dll']), ((1, 'hfFile'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCloseFileInstance():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,win32more.Storage.StructuredStorage.JET_HANDLE)(('JetCloseFileInstance', windll['ESENT.dll']), ((1, 'instance'),(1, 'hfFile'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetLogInfoA():
    try:
        return WINFUNCTYPE(Int32,POINTER(SByte),UInt32,POINTER(UInt32))(('JetGetLogInfoA', windll['ESENT.dll']), ((1, 'szzLogs'),(1, 'cbMax'),(1, 'pcbActual'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetLogInfoW():
    try:
        return WINFUNCTYPE(Int32,POINTER(UInt16),UInt32,POINTER(UInt32))(('JetGetLogInfoW', windll['ESENT.dll']), ((1, 'szzLogs'),(1, 'cbMax'),(1, 'pcbActual'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetLogInfoInstanceA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,POINTER(SByte),UInt32,POINTER(UInt32))(('JetGetLogInfoInstanceA', windll['ESENT.dll']), ((1, 'instance'),(1, 'szzLogs'),(1, 'cbMax'),(1, 'pcbActual'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetLogInfoInstanceW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,POINTER(UInt16),UInt32,POINTER(UInt32))(('JetGetLogInfoInstanceW', windll['ESENT.dll']), ((1, 'instance'),(1, 'wszzLogs'),(1, 'cbMax'),(1, 'pcbActual'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetLogInfoInstance2A():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,POINTER(SByte),UInt32,POINTER(UInt32),POINTER(win32more.Storage.Jet.JET_LOGINFO_A_head))(('JetGetLogInfoInstance2A', windll['ESENT.dll']), ((1, 'instance'),(1, 'szzLogs'),(1, 'cbMax'),(1, 'pcbActual'),(1, 'pLogInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetLogInfoInstance2W():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,POINTER(UInt16),UInt32,POINTER(UInt32),POINTER(win32more.Storage.Jet.JET_LOGINFO_W_head))(('JetGetLogInfoInstance2W', windll['ESENT.dll']), ((1, 'instance'),(1, 'wszzLogs'),(1, 'cbMax'),(1, 'pcbActual'),(1, 'pLogInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetTruncateLogInfoInstanceA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,POINTER(SByte),UInt32,POINTER(UInt32))(('JetGetTruncateLogInfoInstanceA', windll['ESENT.dll']), ((1, 'instance'),(1, 'szzLogs'),(1, 'cbMax'),(1, 'pcbActual'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetTruncateLogInfoInstanceW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,POINTER(UInt16),UInt32,POINTER(UInt32))(('JetGetTruncateLogInfoInstanceW', windll['ESENT.dll']), ((1, 'instance'),(1, 'wszzLogs'),(1, 'cbMax'),(1, 'pcbActual'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetTruncateLog():
    try:
        return WINFUNCTYPE(Int32,)(('JetTruncateLog', windll['ESENT.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetTruncateLogInstance():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE)(('JetTruncateLogInstance', windll['ESENT.dll']), ((1, 'instance'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetEndExternalBackup():
    try:
        return WINFUNCTYPE(Int32,)(('JetEndExternalBackup', windll['ESENT.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetEndExternalBackupInstance():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE)(('JetEndExternalBackupInstance', windll['ESENT.dll']), ((1, 'instance'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetEndExternalBackupInstance2():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,UInt32)(('JetEndExternalBackupInstance2', windll['ESENT.dll']), ((1, 'instance'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetExternalRestoreA():
    try:
        return WINFUNCTYPE(Int32,POINTER(SByte),POINTER(SByte),POINTER(win32more.Storage.Jet.JET_RSTMAP_A_head),Int32,POINTER(SByte),Int32,Int32,win32more.Storage.Jet.JET_PFNSTATUS)(('JetExternalRestoreA', windll['ESENT.dll']), ((1, 'szCheckpointFilePath'),(1, 'szLogPath'),(1, 'rgrstmap'),(1, 'crstfilemap'),(1, 'szBackupLogPath'),(1, 'genLow'),(1, 'genHigh'),(1, 'pfn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetExternalRestoreW():
    try:
        return WINFUNCTYPE(Int32,POINTER(UInt16),POINTER(UInt16),POINTER(win32more.Storage.Jet.JET_RSTMAP_W_head),Int32,POINTER(UInt16),Int32,Int32,win32more.Storage.Jet.JET_PFNSTATUS)(('JetExternalRestoreW', windll['ESENT.dll']), ((1, 'szCheckpointFilePath'),(1, 'szLogPath'),(1, 'rgrstmap'),(1, 'crstfilemap'),(1, 'szBackupLogPath'),(1, 'genLow'),(1, 'genHigh'),(1, 'pfn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetExternalRestore2A():
    try:
        return WINFUNCTYPE(Int32,POINTER(SByte),POINTER(SByte),POINTER(win32more.Storage.Jet.JET_RSTMAP_A_head),Int32,POINTER(SByte),POINTER(win32more.Storage.Jet.JET_LOGINFO_A_head),POINTER(SByte),POINTER(SByte),POINTER(SByte),win32more.Storage.Jet.JET_PFNSTATUS)(('JetExternalRestore2A', windll['ESENT.dll']), ((1, 'szCheckpointFilePath'),(1, 'szLogPath'),(1, 'rgrstmap'),(1, 'crstfilemap'),(1, 'szBackupLogPath'),(1, 'pLogInfo'),(1, 'szTargetInstanceName'),(1, 'szTargetInstanceLogPath'),(1, 'szTargetInstanceCheckpointPath'),(1, 'pfn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetExternalRestore2W():
    try:
        return WINFUNCTYPE(Int32,POINTER(UInt16),POINTER(UInt16),POINTER(win32more.Storage.Jet.JET_RSTMAP_W_head),Int32,POINTER(UInt16),POINTER(win32more.Storage.Jet.JET_LOGINFO_W_head),POINTER(UInt16),POINTER(UInt16),POINTER(UInt16),win32more.Storage.Jet.JET_PFNSTATUS)(('JetExternalRestore2W', windll['ESENT.dll']), ((1, 'szCheckpointFilePath'),(1, 'szLogPath'),(1, 'rgrstmap'),(1, 'crstfilemap'),(1, 'szBackupLogPath'),(1, 'pLogInfo'),(1, 'szTargetInstanceName'),(1, 'szTargetInstanceLogPath'),(1, 'szTargetInstanceCheckpointPath'),(1, 'pfn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetRegisterCallback():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,UInt32,win32more.Storage.Jet.JET_CALLBACK,c_void_p,POINTER(win32more.Storage.StructuredStorage.JET_HANDLE))(('JetRegisterCallback', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'cbtyp'),(1, 'pCallback'),(1, 'pvContext'),(1, 'phCallbackId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetUnregisterCallback():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,UInt32,win32more.Storage.StructuredStorage.JET_HANDLE)(('JetUnregisterCallback', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'cbtyp'),(1, 'hCallbackId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetInstanceInfoA():
    try:
        return WINFUNCTYPE(Int32,POINTER(UInt32),POINTER(POINTER(win32more.Storage.Jet.JET_INSTANCE_INFO_A_head)))(('JetGetInstanceInfoA', windll['ESENT.dll']), ((1, 'pcInstanceInfo'),(1, 'paInstanceInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetInstanceInfoW():
    try:
        return WINFUNCTYPE(Int32,POINTER(UInt32),POINTER(POINTER(win32more.Storage.Jet.JET_INSTANCE_INFO_W_head)))(('JetGetInstanceInfoW', windll['ESENT.dll']), ((1, 'pcInstanceInfo'),(1, 'paInstanceInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetFreeBuffer():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSTR)(('JetFreeBuffer', windll['ESENT.dll']), ((1, 'pbBuf'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetSetLS():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,win32more.Storage.Jet.JET_LS,UInt32)(('JetSetLS', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'ls'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetLS():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(win32more.Storage.Jet.JET_LS),UInt32)(('JetGetLS', windll['ESENT.dll']), ((1, 'sesid'),(1, 'tableid'),(1, 'pls'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOSSnapshotPrepare():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Storage.Jet.JET_OSSNAPID),UInt32)(('JetOSSnapshotPrepare', windll['ESENT.dll']), ((1, 'psnapId'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOSSnapshotPrepareInstance():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.Jet.JET_OSSNAPID,win32more.Storage.StructuredStorage.JET_INSTANCE,UInt32)(('JetOSSnapshotPrepareInstance', windll['ESENT.dll']), ((1, 'snapId'),(1, 'instance'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOSSnapshotFreezeA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.Jet.JET_OSSNAPID,POINTER(UInt32),POINTER(POINTER(win32more.Storage.Jet.JET_INSTANCE_INFO_A_head)),UInt32)(('JetOSSnapshotFreezeA', windll['ESENT.dll']), ((1, 'snapId'),(1, 'pcInstanceInfo'),(1, 'paInstanceInfo'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOSSnapshotFreezeW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.Jet.JET_OSSNAPID,POINTER(UInt32),POINTER(POINTER(win32more.Storage.Jet.JET_INSTANCE_INFO_W_head)),UInt32)(('JetOSSnapshotFreezeW', windll['ESENT.dll']), ((1, 'snapId'),(1, 'pcInstanceInfo'),(1, 'paInstanceInfo'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOSSnapshotThaw():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.Jet.JET_OSSNAPID,UInt32)(('JetOSSnapshotThaw', windll['ESENT.dll']), ((1, 'snapId'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOSSnapshotAbort():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.Jet.JET_OSSNAPID,UInt32)(('JetOSSnapshotAbort', windll['ESENT.dll']), ((1, 'snapId'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOSSnapshotTruncateLog():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.Jet.JET_OSSNAPID,UInt32)(('JetOSSnapshotTruncateLog', windll['ESENT.dll']), ((1, 'snapId'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOSSnapshotTruncateLogInstance():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.Jet.JET_OSSNAPID,win32more.Storage.StructuredStorage.JET_INSTANCE,UInt32)(('JetOSSnapshotTruncateLogInstance', windll['ESENT.dll']), ((1, 'snapId'),(1, 'instance'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOSSnapshotGetFreezeInfoA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.Jet.JET_OSSNAPID,POINTER(UInt32),POINTER(POINTER(win32more.Storage.Jet.JET_INSTANCE_INFO_A_head)),UInt32)(('JetOSSnapshotGetFreezeInfoA', windll['ESENT.dll']), ((1, 'snapId'),(1, 'pcInstanceInfo'),(1, 'paInstanceInfo'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOSSnapshotGetFreezeInfoW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.Jet.JET_OSSNAPID,POINTER(UInt32),POINTER(POINTER(win32more.Storage.Jet.JET_INSTANCE_INFO_W_head)),UInt32)(('JetOSSnapshotGetFreezeInfoW', windll['ESENT.dll']), ((1, 'snapId'),(1, 'pcInstanceInfo'),(1, 'paInstanceInfo'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOSSnapshotEnd():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.Jet.JET_OSSNAPID,UInt32)(('JetOSSnapshotEnd', windll['ESENT.dll']), ((1, 'snapId'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetConfigureProcessForCrashDump():
    try:
        return WINFUNCTYPE(Int32,UInt32)(('JetConfigureProcessForCrashDump', windll['ESENT.dll']), ((1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetErrorInfoW():
    try:
        return WINFUNCTYPE(Int32,c_void_p,c_void_p,UInt32,UInt32,UInt32)(('JetGetErrorInfoW', windll['ESENT.dll']), ((1, 'pvContext'),(1, 'pvResult'),(1, 'cbMax'),(1, 'InfoLevel'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetSetSessionParameter():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,c_void_p,UInt32)(('JetSetSessionParameter', windll['ESENT.dll']), ((1, 'sesid'),(1, 'sesparamid'),(1, 'pvParam'),(1, 'cbParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetSessionParameter():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,c_void_p,UInt32,POINTER(UInt32))(('JetGetSessionParameter', windll['ESENT.dll']), ((1, 'sesid'),(1, 'sesparamid'),(1, 'pvParam'),(1, 'cbParamMax'),(1, 'pcbParamActual'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JET_BKINFO_head():
    class JET_BKINFO(Structure):
        pass
    return JET_BKINFO
def _define_JET_BKINFO():
    JET_BKINFO = win32more.Storage.Jet.JET_BKINFO_head
    class JET_BKINFO__Anonymous_e__Union(Union):
        pass
    JET_BKINFO__Anonymous_e__Union._fields_ = [
        ('logtimeMark', win32more.Storage.Jet.JET_LOGTIME),
        ('bklogtimeMark', win32more.Storage.Jet.JET_BKLOGTIME),
    ]
    JET_BKINFO._pack_ = 1
    JET_BKINFO._anonymous_ = [
        'Anonymous',
    ]
    JET_BKINFO._fields_ = [
        ('lgposMark', win32more.Storage.Jet.JET_LGPOS),
        ('Anonymous', JET_BKINFO__Anonymous_e__Union),
        ('genLow', UInt32),
        ('genHigh', UInt32),
    ]
    return JET_BKINFO
def _define_JET_BKLOGTIME_head():
    class JET_BKLOGTIME(Structure):
        pass
    return JET_BKLOGTIME
def _define_JET_BKLOGTIME():
    JET_BKLOGTIME = win32more.Storage.Jet.JET_BKLOGTIME_head
    class JET_BKLOGTIME__Anonymous1_e__Union(Union):
        pass
    class JET_BKLOGTIME__Anonymous1_e__Union__Anonymous_e__Struct(Structure):
        pass
    JET_BKLOGTIME__Anonymous1_e__Union__Anonymous_e__Struct._fields_ = [
        ('_bitfield', Byte),
    ]
    JET_BKLOGTIME__Anonymous1_e__Union._anonymous_ = [
        'Anonymous',
    ]
    JET_BKLOGTIME__Anonymous1_e__Union._fields_ = [
        ('bFiller1', win32more.Foundation.CHAR),
        ('Anonymous', JET_BKLOGTIME__Anonymous1_e__Union__Anonymous_e__Struct),
    ]
    class JET_BKLOGTIME__Anonymous2_e__Union(Union):
        pass
    class JET_BKLOGTIME__Anonymous2_e__Union__Anonymous_e__Struct(Structure):
        pass
    JET_BKLOGTIME__Anonymous2_e__Union__Anonymous_e__Struct._fields_ = [
        ('_bitfield', Byte),
    ]
    JET_BKLOGTIME__Anonymous2_e__Union._anonymous_ = [
        'Anonymous',
    ]
    JET_BKLOGTIME__Anonymous2_e__Union._fields_ = [
        ('bFiller2', win32more.Foundation.CHAR),
        ('Anonymous', JET_BKLOGTIME__Anonymous2_e__Union__Anonymous_e__Struct),
    ]
    JET_BKLOGTIME._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    JET_BKLOGTIME._fields_ = [
        ('bSeconds', win32more.Foundation.CHAR),
        ('bMinutes', win32more.Foundation.CHAR),
        ('bHours', win32more.Foundation.CHAR),
        ('bDay', win32more.Foundation.CHAR),
        ('bMonth', win32more.Foundation.CHAR),
        ('bYear', win32more.Foundation.CHAR),
        ('Anonymous1', JET_BKLOGTIME__Anonymous1_e__Union),
        ('Anonymous2', JET_BKLOGTIME__Anonymous2_e__Union),
    ]
    return JET_BKLOGTIME
def _define_JET_CALLBACK():
    return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,win32more.Storage.StructuredStorage.JET_TABLEID,UInt32,c_void_p,c_void_p,c_void_p,win32more.Storage.StructuredStorage.JET_API_PTR)
def _define_JET_COLUMNBASE_A_head():
    class JET_COLUMNBASE_A(Structure):
        pass
    return JET_COLUMNBASE_A
def _define_JET_COLUMNBASE_A():
    JET_COLUMNBASE_A = win32more.Storage.Jet.JET_COLUMNBASE_A_head
    JET_COLUMNBASE_A._fields_ = [
        ('cbStruct', UInt32),
        ('columnid', UInt32),
        ('coltyp', UInt32),
        ('wCountry', UInt16),
        ('langid', UInt16),
        ('cp', UInt16),
        ('wFiller', UInt16),
        ('cbMax', UInt32),
        ('grbit', UInt32),
        ('szBaseTableName', win32more.Foundation.CHAR * 256),
        ('szBaseColumnName', win32more.Foundation.CHAR * 256),
    ]
    return JET_COLUMNBASE_A
def _define_JET_COLUMNBASE_W_head():
    class JET_COLUMNBASE_W(Structure):
        pass
    return JET_COLUMNBASE_W
def _define_JET_COLUMNBASE_W():
    JET_COLUMNBASE_W = win32more.Storage.Jet.JET_COLUMNBASE_W_head
    JET_COLUMNBASE_W._fields_ = [
        ('cbStruct', UInt32),
        ('columnid', UInt32),
        ('coltyp', UInt32),
        ('wCountry', UInt16),
        ('langid', UInt16),
        ('cp', UInt16),
        ('wFiller', UInt16),
        ('cbMax', UInt32),
        ('grbit', UInt32),
        ('szBaseTableName', Char * 256),
        ('szBaseColumnName', Char * 256),
    ]
    return JET_COLUMNBASE_W
def _define_JET_COLUMNCREATE_A_head():
    class JET_COLUMNCREATE_A(Structure):
        pass
    return JET_COLUMNCREATE_A
def _define_JET_COLUMNCREATE_A():
    JET_COLUMNCREATE_A = win32more.Storage.Jet.JET_COLUMNCREATE_A_head
    JET_COLUMNCREATE_A._fields_ = [
        ('cbStruct', UInt32),
        ('szColumnName', win32more.Foundation.PSTR),
        ('coltyp', UInt32),
        ('cbMax', UInt32),
        ('grbit', UInt32),
        ('pvDefault', c_void_p),
        ('cbDefault', UInt32),
        ('cp', UInt32),
        ('columnid', UInt32),
        ('err', Int32),
    ]
    return JET_COLUMNCREATE_A
def _define_JET_COLUMNCREATE_W_head():
    class JET_COLUMNCREATE_W(Structure):
        pass
    return JET_COLUMNCREATE_W
def _define_JET_COLUMNCREATE_W():
    JET_COLUMNCREATE_W = win32more.Storage.Jet.JET_COLUMNCREATE_W_head
    JET_COLUMNCREATE_W._fields_ = [
        ('cbStruct', UInt32),
        ('szColumnName', win32more.Foundation.PWSTR),
        ('coltyp', UInt32),
        ('cbMax', UInt32),
        ('grbit', UInt32),
        ('pvDefault', c_void_p),
        ('cbDefault', UInt32),
        ('cp', UInt32),
        ('columnid', UInt32),
        ('err', Int32),
    ]
    return JET_COLUMNCREATE_W
def _define_JET_COLUMNDEF_head():
    class JET_COLUMNDEF(Structure):
        pass
    return JET_COLUMNDEF
def _define_JET_COLUMNDEF():
    JET_COLUMNDEF = win32more.Storage.Jet.JET_COLUMNDEF_head
    JET_COLUMNDEF._fields_ = [
        ('cbStruct', UInt32),
        ('columnid', UInt32),
        ('coltyp', UInt32),
        ('wCountry', UInt16),
        ('langid', UInt16),
        ('cp', UInt16),
        ('wCollate', UInt16),
        ('cbMax', UInt32),
        ('grbit', UInt32),
    ]
    return JET_COLUMNDEF
def _define_JET_COLUMNLIST_head():
    class JET_COLUMNLIST(Structure):
        pass
    return JET_COLUMNLIST
def _define_JET_COLUMNLIST():
    JET_COLUMNLIST = win32more.Storage.Jet.JET_COLUMNLIST_head
    JET_COLUMNLIST._fields_ = [
        ('cbStruct', UInt32),
        ('tableid', win32more.Storage.StructuredStorage.JET_TABLEID),
        ('cRecord', UInt32),
        ('columnidPresentationOrder', UInt32),
        ('columnidcolumnname', UInt32),
        ('columnidcolumnid', UInt32),
        ('columnidcoltyp', UInt32),
        ('columnidCountry', UInt32),
        ('columnidLangid', UInt32),
        ('columnidCp', UInt32),
        ('columnidCollate', UInt32),
        ('columnidcbMax', UInt32),
        ('columnidgrbit', UInt32),
        ('columnidDefault', UInt32),
        ('columnidBaseTableName', UInt32),
        ('columnidBaseColumnName', UInt32),
        ('columnidDefinitionName', UInt32),
    ]
    return JET_COLUMNLIST
def _define_JET_COMMIT_ID_head():
    class JET_COMMIT_ID(Structure):
        pass
    return JET_COMMIT_ID
def _define_JET_COMMIT_ID():
    JET_COMMIT_ID = win32more.Storage.Jet.JET_COMMIT_ID_head
    JET_COMMIT_ID._fields_ = [
        ('signLog', win32more.Storage.Jet.JET_SIGNATURE),
        ('reserved', Int32),
        ('commitId', Int64),
    ]
    return JET_COMMIT_ID
def _define_JET_CONDITIONALCOLUMN_A_head():
    class JET_CONDITIONALCOLUMN_A(Structure):
        pass
    return JET_CONDITIONALCOLUMN_A
def _define_JET_CONDITIONALCOLUMN_A():
    JET_CONDITIONALCOLUMN_A = win32more.Storage.Jet.JET_CONDITIONALCOLUMN_A_head
    JET_CONDITIONALCOLUMN_A._fields_ = [
        ('cbStruct', UInt32),
        ('szColumnName', win32more.Foundation.PSTR),
        ('grbit', UInt32),
    ]
    return JET_CONDITIONALCOLUMN_A
def _define_JET_CONDITIONALCOLUMN_W_head():
    class JET_CONDITIONALCOLUMN_W(Structure):
        pass
    return JET_CONDITIONALCOLUMN_W
def _define_JET_CONDITIONALCOLUMN_W():
    JET_CONDITIONALCOLUMN_W = win32more.Storage.Jet.JET_CONDITIONALCOLUMN_W_head
    JET_CONDITIONALCOLUMN_W._fields_ = [
        ('cbStruct', UInt32),
        ('szColumnName', win32more.Foundation.PWSTR),
        ('grbit', UInt32),
    ]
    return JET_CONDITIONALCOLUMN_W
def _define_JET_CONVERT_A_head():
    class JET_CONVERT_A(Structure):
        pass
    return JET_CONVERT_A
def _define_JET_CONVERT_A():
    JET_CONVERT_A = win32more.Storage.Jet.JET_CONVERT_A_head
    class JET_CONVERT_A__Anonymous_e__Union(Union):
        pass
    class JET_CONVERT_A__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    JET_CONVERT_A__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ('_bitfield', UInt32),
    ]
    JET_CONVERT_A__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    JET_CONVERT_A__Anonymous_e__Union._fields_ = [
        ('fFlags', UInt32),
        ('Anonymous', JET_CONVERT_A__Anonymous_e__Union__Anonymous_e__Struct),
    ]
    JET_CONVERT_A._anonymous_ = [
        'Anonymous',
    ]
    JET_CONVERT_A._fields_ = [
        ('szOldDll', win32more.Foundation.PSTR),
        ('Anonymous', JET_CONVERT_A__Anonymous_e__Union),
    ]
    return JET_CONVERT_A
def _define_JET_CONVERT_W_head():
    class JET_CONVERT_W(Structure):
        pass
    return JET_CONVERT_W
def _define_JET_CONVERT_W():
    JET_CONVERT_W = win32more.Storage.Jet.JET_CONVERT_W_head
    class JET_CONVERT_W__Anonymous_e__Union(Union):
        pass
    class JET_CONVERT_W__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    JET_CONVERT_W__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ('_bitfield', UInt32),
    ]
    JET_CONVERT_W__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    JET_CONVERT_W__Anonymous_e__Union._fields_ = [
        ('fFlags', UInt32),
        ('Anonymous', JET_CONVERT_W__Anonymous_e__Union__Anonymous_e__Struct),
    ]
    JET_CONVERT_W._anonymous_ = [
        'Anonymous',
    ]
    JET_CONVERT_W._fields_ = [
        ('szOldDll', win32more.Foundation.PWSTR),
        ('Anonymous', JET_CONVERT_W__Anonymous_e__Union),
    ]
    return JET_CONVERT_W
def _define_JET_DBINFOMISC_head():
    class JET_DBINFOMISC(Structure):
        pass
    return JET_DBINFOMISC
def _define_JET_DBINFOMISC():
    JET_DBINFOMISC = win32more.Storage.Jet.JET_DBINFOMISC_head
    JET_DBINFOMISC._fields_ = [
        ('ulVersion', UInt32),
        ('ulUpdate', UInt32),
        ('signDb', win32more.Storage.Jet.JET_SIGNATURE),
        ('dbstate', UInt32),
        ('lgposConsistent', win32more.Storage.Jet.JET_LGPOS),
        ('logtimeConsistent', win32more.Storage.Jet.JET_LOGTIME),
        ('logtimeAttach', win32more.Storage.Jet.JET_LOGTIME),
        ('lgposAttach', win32more.Storage.Jet.JET_LGPOS),
        ('logtimeDetach', win32more.Storage.Jet.JET_LOGTIME),
        ('lgposDetach', win32more.Storage.Jet.JET_LGPOS),
        ('signLog', win32more.Storage.Jet.JET_SIGNATURE),
        ('bkinfoFullPrev', win32more.Storage.Jet.JET_BKINFO),
        ('bkinfoIncPrev', win32more.Storage.Jet.JET_BKINFO),
        ('bkinfoFullCur', win32more.Storage.Jet.JET_BKINFO),
        ('fShadowingDisabled', UInt32),
        ('fUpgradeDb', UInt32),
        ('dwMajorVersion', UInt32),
        ('dwMinorVersion', UInt32),
        ('dwBuildNumber', UInt32),
        ('lSPNumber', Int32),
        ('cbPageSize', UInt32),
    ]
    return JET_DBINFOMISC
def _define_JET_DBINFOMISC2_head():
    class JET_DBINFOMISC2(Structure):
        pass
    return JET_DBINFOMISC2
def _define_JET_DBINFOMISC2():
    JET_DBINFOMISC2 = win32more.Storage.Jet.JET_DBINFOMISC2_head
    JET_DBINFOMISC2._fields_ = [
        ('ulVersion', UInt32),
        ('ulUpdate', UInt32),
        ('signDb', win32more.Storage.Jet.JET_SIGNATURE),
        ('dbstate', UInt32),
        ('lgposConsistent', win32more.Storage.Jet.JET_LGPOS),
        ('logtimeConsistent', win32more.Storage.Jet.JET_LOGTIME),
        ('logtimeAttach', win32more.Storage.Jet.JET_LOGTIME),
        ('lgposAttach', win32more.Storage.Jet.JET_LGPOS),
        ('logtimeDetach', win32more.Storage.Jet.JET_LOGTIME),
        ('lgposDetach', win32more.Storage.Jet.JET_LGPOS),
        ('signLog', win32more.Storage.Jet.JET_SIGNATURE),
        ('bkinfoFullPrev', win32more.Storage.Jet.JET_BKINFO),
        ('bkinfoIncPrev', win32more.Storage.Jet.JET_BKINFO),
        ('bkinfoFullCur', win32more.Storage.Jet.JET_BKINFO),
        ('fShadowingDisabled', UInt32),
        ('fUpgradeDb', UInt32),
        ('dwMajorVersion', UInt32),
        ('dwMinorVersion', UInt32),
        ('dwBuildNumber', UInt32),
        ('lSPNumber', Int32),
        ('cbPageSize', UInt32),
        ('genMinRequired', UInt32),
        ('genMaxRequired', UInt32),
        ('logtimeGenMaxCreate', win32more.Storage.Jet.JET_LOGTIME),
        ('ulRepairCount', UInt32),
        ('logtimeRepair', win32more.Storage.Jet.JET_LOGTIME),
        ('ulRepairCountOld', UInt32),
        ('ulECCFixSuccess', UInt32),
        ('logtimeECCFixSuccess', win32more.Storage.Jet.JET_LOGTIME),
        ('ulECCFixSuccessOld', UInt32),
        ('ulECCFixFail', UInt32),
        ('logtimeECCFixFail', win32more.Storage.Jet.JET_LOGTIME),
        ('ulECCFixFailOld', UInt32),
        ('ulBadChecksum', UInt32),
        ('logtimeBadChecksum', win32more.Storage.Jet.JET_LOGTIME),
        ('ulBadChecksumOld', UInt32),
    ]
    return JET_DBINFOMISC2
def _define_JET_DBINFOMISC3_head():
    class JET_DBINFOMISC3(Structure):
        pass
    return JET_DBINFOMISC3
def _define_JET_DBINFOMISC3():
    JET_DBINFOMISC3 = win32more.Storage.Jet.JET_DBINFOMISC3_head
    JET_DBINFOMISC3._fields_ = [
        ('ulVersion', UInt32),
        ('ulUpdate', UInt32),
        ('signDb', win32more.Storage.Jet.JET_SIGNATURE),
        ('dbstate', UInt32),
        ('lgposConsistent', win32more.Storage.Jet.JET_LGPOS),
        ('logtimeConsistent', win32more.Storage.Jet.JET_LOGTIME),
        ('logtimeAttach', win32more.Storage.Jet.JET_LOGTIME),
        ('lgposAttach', win32more.Storage.Jet.JET_LGPOS),
        ('logtimeDetach', win32more.Storage.Jet.JET_LOGTIME),
        ('lgposDetach', win32more.Storage.Jet.JET_LGPOS),
        ('signLog', win32more.Storage.Jet.JET_SIGNATURE),
        ('bkinfoFullPrev', win32more.Storage.Jet.JET_BKINFO),
        ('bkinfoIncPrev', win32more.Storage.Jet.JET_BKINFO),
        ('bkinfoFullCur', win32more.Storage.Jet.JET_BKINFO),
        ('fShadowingDisabled', UInt32),
        ('fUpgradeDb', UInt32),
        ('dwMajorVersion', UInt32),
        ('dwMinorVersion', UInt32),
        ('dwBuildNumber', UInt32),
        ('lSPNumber', Int32),
        ('cbPageSize', UInt32),
        ('genMinRequired', UInt32),
        ('genMaxRequired', UInt32),
        ('logtimeGenMaxCreate', win32more.Storage.Jet.JET_LOGTIME),
        ('ulRepairCount', UInt32),
        ('logtimeRepair', win32more.Storage.Jet.JET_LOGTIME),
        ('ulRepairCountOld', UInt32),
        ('ulECCFixSuccess', UInt32),
        ('logtimeECCFixSuccess', win32more.Storage.Jet.JET_LOGTIME),
        ('ulECCFixSuccessOld', UInt32),
        ('ulECCFixFail', UInt32),
        ('logtimeECCFixFail', win32more.Storage.Jet.JET_LOGTIME),
        ('ulECCFixFailOld', UInt32),
        ('ulBadChecksum', UInt32),
        ('logtimeBadChecksum', win32more.Storage.Jet.JET_LOGTIME),
        ('ulBadChecksumOld', UInt32),
        ('genCommitted', UInt32),
    ]
    return JET_DBINFOMISC3
def _define_JET_DBINFOMISC4_head():
    class JET_DBINFOMISC4(Structure):
        pass
    return JET_DBINFOMISC4
def _define_JET_DBINFOMISC4():
    JET_DBINFOMISC4 = win32more.Storage.Jet.JET_DBINFOMISC4_head
    JET_DBINFOMISC4._fields_ = [
        ('ulVersion', UInt32),
        ('ulUpdate', UInt32),
        ('signDb', win32more.Storage.Jet.JET_SIGNATURE),
        ('dbstate', UInt32),
        ('lgposConsistent', win32more.Storage.Jet.JET_LGPOS),
        ('logtimeConsistent', win32more.Storage.Jet.JET_LOGTIME),
        ('logtimeAttach', win32more.Storage.Jet.JET_LOGTIME),
        ('lgposAttach', win32more.Storage.Jet.JET_LGPOS),
        ('logtimeDetach', win32more.Storage.Jet.JET_LOGTIME),
        ('lgposDetach', win32more.Storage.Jet.JET_LGPOS),
        ('signLog', win32more.Storage.Jet.JET_SIGNATURE),
        ('bkinfoFullPrev', win32more.Storage.Jet.JET_BKINFO),
        ('bkinfoIncPrev', win32more.Storage.Jet.JET_BKINFO),
        ('bkinfoFullCur', win32more.Storage.Jet.JET_BKINFO),
        ('fShadowingDisabled', UInt32),
        ('fUpgradeDb', UInt32),
        ('dwMajorVersion', UInt32),
        ('dwMinorVersion', UInt32),
        ('dwBuildNumber', UInt32),
        ('lSPNumber', Int32),
        ('cbPageSize', UInt32),
        ('genMinRequired', UInt32),
        ('genMaxRequired', UInt32),
        ('logtimeGenMaxCreate', win32more.Storage.Jet.JET_LOGTIME),
        ('ulRepairCount', UInt32),
        ('logtimeRepair', win32more.Storage.Jet.JET_LOGTIME),
        ('ulRepairCountOld', UInt32),
        ('ulECCFixSuccess', UInt32),
        ('logtimeECCFixSuccess', win32more.Storage.Jet.JET_LOGTIME),
        ('ulECCFixSuccessOld', UInt32),
        ('ulECCFixFail', UInt32),
        ('logtimeECCFixFail', win32more.Storage.Jet.JET_LOGTIME),
        ('ulECCFixFailOld', UInt32),
        ('ulBadChecksum', UInt32),
        ('logtimeBadChecksum', win32more.Storage.Jet.JET_LOGTIME),
        ('ulBadChecksumOld', UInt32),
        ('genCommitted', UInt32),
        ('bkinfoCopyPrev', win32more.Storage.Jet.JET_BKINFO),
        ('bkinfoDiffPrev', win32more.Storage.Jet.JET_BKINFO),
    ]
    return JET_DBINFOMISC4
def _define_JET_DBINFOUPGRADE_head():
    class JET_DBINFOUPGRADE(Structure):
        pass
    return JET_DBINFOUPGRADE
def _define_JET_DBINFOUPGRADE():
    JET_DBINFOUPGRADE = win32more.Storage.Jet.JET_DBINFOUPGRADE_head
    class JET_DBINFOUPGRADE__Anonymous_e__Union(Union):
        pass
    class JET_DBINFOUPGRADE__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    JET_DBINFOUPGRADE__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ('_bitfield', UInt32),
    ]
    JET_DBINFOUPGRADE__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    JET_DBINFOUPGRADE__Anonymous_e__Union._fields_ = [
        ('ulFlags', UInt32),
        ('Anonymous', JET_DBINFOUPGRADE__Anonymous_e__Union__Anonymous_e__Struct),
    ]
    JET_DBINFOUPGRADE._anonymous_ = [
        'Anonymous',
    ]
    JET_DBINFOUPGRADE._fields_ = [
        ('cbStruct', UInt32),
        ('cbFilesizeLow', UInt32),
        ('cbFilesizeHigh', UInt32),
        ('cbFreeSpaceRequiredLow', UInt32),
        ('cbFreeSpaceRequiredHigh', UInt32),
        ('csecToUpgrade', UInt32),
        ('Anonymous', JET_DBINFOUPGRADE__Anonymous_e__Union),
    ]
    return JET_DBINFOUPGRADE
def _define_JET_ENUMCOLUMN_head():
    class JET_ENUMCOLUMN(Structure):
        pass
    return JET_ENUMCOLUMN
def _define_JET_ENUMCOLUMN():
    JET_ENUMCOLUMN = win32more.Storage.Jet.JET_ENUMCOLUMN_head
    class JET_ENUMCOLUMN__Anonymous_e__Union(Union):
        pass
    class JET_ENUMCOLUMN__Anonymous_e__Union__Anonymous1_e__Struct(Structure):
        pass
    JET_ENUMCOLUMN__Anonymous_e__Union__Anonymous1_e__Struct._fields_ = [
        ('cEnumColumnValue', UInt32),
        ('rgEnumColumnValue', POINTER(win32more.Storage.Jet.JET_ENUMCOLUMNVALUE_head)),
    ]
    class JET_ENUMCOLUMN__Anonymous_e__Union__Anonymous2_e__Struct(Structure):
        pass
    JET_ENUMCOLUMN__Anonymous_e__Union__Anonymous2_e__Struct._fields_ = [
        ('cbData', UInt32),
        ('pvData', c_void_p),
    ]
    JET_ENUMCOLUMN__Anonymous_e__Union._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    JET_ENUMCOLUMN__Anonymous_e__Union._fields_ = [
        ('Anonymous1', JET_ENUMCOLUMN__Anonymous_e__Union__Anonymous1_e__Struct),
        ('Anonymous2', JET_ENUMCOLUMN__Anonymous_e__Union__Anonymous2_e__Struct),
    ]
    JET_ENUMCOLUMN._anonymous_ = [
        'Anonymous',
    ]
    JET_ENUMCOLUMN._fields_ = [
        ('columnid', UInt32),
        ('err', Int32),
        ('Anonymous', JET_ENUMCOLUMN__Anonymous_e__Union),
    ]
    return JET_ENUMCOLUMN
def _define_JET_ENUMCOLUMNID_head():
    class JET_ENUMCOLUMNID(Structure):
        pass
    return JET_ENUMCOLUMNID
def _define_JET_ENUMCOLUMNID():
    JET_ENUMCOLUMNID = win32more.Storage.Jet.JET_ENUMCOLUMNID_head
    JET_ENUMCOLUMNID._fields_ = [
        ('columnid', UInt32),
        ('ctagSequence', UInt32),
        ('rgtagSequence', POINTER(UInt32)),
    ]
    return JET_ENUMCOLUMNID
def _define_JET_ENUMCOLUMNVALUE_head():
    class JET_ENUMCOLUMNVALUE(Structure):
        pass
    return JET_ENUMCOLUMNVALUE
def _define_JET_ENUMCOLUMNVALUE():
    JET_ENUMCOLUMNVALUE = win32more.Storage.Jet.JET_ENUMCOLUMNVALUE_head
    JET_ENUMCOLUMNVALUE._fields_ = [
        ('itagSequence', UInt32),
        ('err', Int32),
        ('cbData', UInt32),
        ('pvData', c_void_p),
    ]
    return JET_ENUMCOLUMNVALUE
JET_ERRCAT = Int32
JET_errcatUnknown = 0
JET_errcatError = 1
JET_errcatOperation = 2
JET_errcatFatal = 3
JET_errcatIO = 4
JET_errcatResource = 5
JET_errcatMemory = 6
JET_errcatQuota = 7
JET_errcatDisk = 8
JET_errcatData = 9
JET_errcatCorruption = 10
JET_errcatInconsistent = 11
JET_errcatFragmentation = 12
JET_errcatApi = 13
JET_errcatUsage = 14
JET_errcatState = 15
JET_errcatObsolete = 16
JET_errcatMax = 17
def _define_JET_ERRINFOBASIC_W_head():
    class JET_ERRINFOBASIC_W(Structure):
        pass
    return JET_ERRINFOBASIC_W
def _define_JET_ERRINFOBASIC_W():
    JET_ERRINFOBASIC_W = win32more.Storage.Jet.JET_ERRINFOBASIC_W_head
    JET_ERRINFOBASIC_W._fields_ = [
        ('cbStruct', UInt32),
        ('errValue', Int32),
        ('errcatMostSpecific', win32more.Storage.Jet.JET_ERRCAT),
        ('rgCategoricalHierarchy', Byte * 8),
        ('lSourceLine', UInt32),
        ('rgszSourceFile', Char * 64),
    ]
    return JET_ERRINFOBASIC_W
def _define_JET_INDEX_COLUMN_head():
    class JET_INDEX_COLUMN(Structure):
        pass
    return JET_INDEX_COLUMN
def _define_JET_INDEX_COLUMN():
    JET_INDEX_COLUMN = win32more.Storage.Jet.JET_INDEX_COLUMN_head
    JET_INDEX_COLUMN._fields_ = [
        ('columnid', UInt32),
        ('relop', win32more.Storage.Jet.JET_RELOP),
        ('pv', c_void_p),
        ('cb', UInt32),
        ('grbit', UInt32),
    ]
    return JET_INDEX_COLUMN
def _define_JET_INDEX_RANGE_head():
    class JET_INDEX_RANGE(Structure):
        pass
    return JET_INDEX_RANGE
def _define_JET_INDEX_RANGE():
    JET_INDEX_RANGE = win32more.Storage.Jet.JET_INDEX_RANGE_head
    JET_INDEX_RANGE._fields_ = [
        ('rgStartColumns', POINTER(win32more.Storage.Jet.JET_INDEX_COLUMN_head)),
        ('cStartColumns', UInt32),
        ('rgEndColumns', POINTER(win32more.Storage.Jet.JET_INDEX_COLUMN_head)),
        ('cEndColumns', UInt32),
    ]
    return JET_INDEX_RANGE
JET_INDEXCHECKING = Int32
JET_IndexCheckingOff = 0
JET_IndexCheckingOn = 1
JET_IndexCheckingDeferToOpenTable = 2
JET_IndexCheckingMax = 3
def _define_JET_INDEXCREATE_A_head():
    class JET_INDEXCREATE_A(Structure):
        pass
    return JET_INDEXCREATE_A
def _define_JET_INDEXCREATE_A():
    JET_INDEXCREATE_A = win32more.Storage.Jet.JET_INDEXCREATE_A_head
    class JET_INDEXCREATE_A__Anonymous1_e__Union(Union):
        pass
    JET_INDEXCREATE_A__Anonymous1_e__Union._fields_ = [
        ('lcid', UInt32),
        ('pidxunicode', POINTER(win32more.Storage.Jet.JET_UNICODEINDEX_head)),
    ]
    class JET_INDEXCREATE_A__Anonymous2_e__Union(Union):
        pass
    JET_INDEXCREATE_A__Anonymous2_e__Union._fields_ = [
        ('cbVarSegMac', UInt32),
        ('ptuplelimits', POINTER(win32more.Storage.Jet.JET_TUPLELIMITS_head)),
    ]
    JET_INDEXCREATE_A._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    JET_INDEXCREATE_A._fields_ = [
        ('cbStruct', UInt32),
        ('szIndexName', win32more.Foundation.PSTR),
        ('szKey', win32more.Foundation.PSTR),
        ('cbKey', UInt32),
        ('grbit', UInt32),
        ('ulDensity', UInt32),
        ('Anonymous1', JET_INDEXCREATE_A__Anonymous1_e__Union),
        ('Anonymous2', JET_INDEXCREATE_A__Anonymous2_e__Union),
        ('rgconditionalcolumn', POINTER(win32more.Storage.Jet.JET_CONDITIONALCOLUMN_A_head)),
        ('cConditionalColumn', UInt32),
        ('err', Int32),
        ('cbKeyMost', UInt32),
    ]
    return JET_INDEXCREATE_A
def _define_JET_INDEXCREATE_W_head():
    class JET_INDEXCREATE_W(Structure):
        pass
    return JET_INDEXCREATE_W
def _define_JET_INDEXCREATE_W():
    JET_INDEXCREATE_W = win32more.Storage.Jet.JET_INDEXCREATE_W_head
    class JET_INDEXCREATE_W__Anonymous1_e__Union(Union):
        pass
    JET_INDEXCREATE_W__Anonymous1_e__Union._fields_ = [
        ('lcid', UInt32),
        ('pidxunicode', POINTER(win32more.Storage.Jet.JET_UNICODEINDEX_head)),
    ]
    class JET_INDEXCREATE_W__Anonymous2_e__Union(Union):
        pass
    JET_INDEXCREATE_W__Anonymous2_e__Union._fields_ = [
        ('cbVarSegMac', UInt32),
        ('ptuplelimits', POINTER(win32more.Storage.Jet.JET_TUPLELIMITS_head)),
    ]
    JET_INDEXCREATE_W._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    JET_INDEXCREATE_W._fields_ = [
        ('cbStruct', UInt32),
        ('szIndexName', win32more.Foundation.PWSTR),
        ('szKey', win32more.Foundation.PWSTR),
        ('cbKey', UInt32),
        ('grbit', UInt32),
        ('ulDensity', UInt32),
        ('Anonymous1', JET_INDEXCREATE_W__Anonymous1_e__Union),
        ('Anonymous2', JET_INDEXCREATE_W__Anonymous2_e__Union),
        ('rgconditionalcolumn', POINTER(win32more.Storage.Jet.JET_CONDITIONALCOLUMN_W_head)),
        ('cConditionalColumn', UInt32),
        ('err', Int32),
        ('cbKeyMost', UInt32),
    ]
    return JET_INDEXCREATE_W
def _define_JET_INDEXCREATE2_A_head():
    class JET_INDEXCREATE2_A(Structure):
        pass
    return JET_INDEXCREATE2_A
def _define_JET_INDEXCREATE2_A():
    JET_INDEXCREATE2_A = win32more.Storage.Jet.JET_INDEXCREATE2_A_head
    class JET_INDEXCREATE2_A__Anonymous1_e__Union(Union):
        pass
    JET_INDEXCREATE2_A__Anonymous1_e__Union._fields_ = [
        ('lcid', UInt32),
        ('pidxunicode', POINTER(win32more.Storage.Jet.JET_UNICODEINDEX_head)),
    ]
    class JET_INDEXCREATE2_A__Anonymous2_e__Union(Union):
        pass
    JET_INDEXCREATE2_A__Anonymous2_e__Union._fields_ = [
        ('cbVarSegMac', UInt32),
        ('ptuplelimits', POINTER(win32more.Storage.Jet.JET_TUPLELIMITS_head)),
    ]
    JET_INDEXCREATE2_A._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    JET_INDEXCREATE2_A._fields_ = [
        ('cbStruct', UInt32),
        ('szIndexName', win32more.Foundation.PSTR),
        ('szKey', win32more.Foundation.PSTR),
        ('cbKey', UInt32),
        ('grbit', UInt32),
        ('ulDensity', UInt32),
        ('Anonymous1', JET_INDEXCREATE2_A__Anonymous1_e__Union),
        ('Anonymous2', JET_INDEXCREATE2_A__Anonymous2_e__Union),
        ('rgconditionalcolumn', POINTER(win32more.Storage.Jet.JET_CONDITIONALCOLUMN_A_head)),
        ('cConditionalColumn', UInt32),
        ('err', Int32),
        ('cbKeyMost', UInt32),
        ('pSpacehints', POINTER(win32more.Storage.Jet.JET_SPACEHINTS_head)),
    ]
    return JET_INDEXCREATE2_A
def _define_JET_INDEXCREATE2_W_head():
    class JET_INDEXCREATE2_W(Structure):
        pass
    return JET_INDEXCREATE2_W
def _define_JET_INDEXCREATE2_W():
    JET_INDEXCREATE2_W = win32more.Storage.Jet.JET_INDEXCREATE2_W_head
    class JET_INDEXCREATE2_W__Anonymous1_e__Union(Union):
        pass
    JET_INDEXCREATE2_W__Anonymous1_e__Union._fields_ = [
        ('lcid', UInt32),
        ('pidxunicode', POINTER(win32more.Storage.Jet.JET_UNICODEINDEX_head)),
    ]
    class JET_INDEXCREATE2_W__Anonymous2_e__Union(Union):
        pass
    JET_INDEXCREATE2_W__Anonymous2_e__Union._fields_ = [
        ('cbVarSegMac', UInt32),
        ('ptuplelimits', POINTER(win32more.Storage.Jet.JET_TUPLELIMITS_head)),
    ]
    JET_INDEXCREATE2_W._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    JET_INDEXCREATE2_W._fields_ = [
        ('cbStruct', UInt32),
        ('szIndexName', win32more.Foundation.PWSTR),
        ('szKey', win32more.Foundation.PWSTR),
        ('cbKey', UInt32),
        ('grbit', UInt32),
        ('ulDensity', UInt32),
        ('Anonymous1', JET_INDEXCREATE2_W__Anonymous1_e__Union),
        ('Anonymous2', JET_INDEXCREATE2_W__Anonymous2_e__Union),
        ('rgconditionalcolumn', POINTER(win32more.Storage.Jet.JET_CONDITIONALCOLUMN_W_head)),
        ('cConditionalColumn', UInt32),
        ('err', Int32),
        ('cbKeyMost', UInt32),
        ('pSpacehints', POINTER(win32more.Storage.Jet.JET_SPACEHINTS_head)),
    ]
    return JET_INDEXCREATE2_W
def _define_JET_INDEXCREATE3_A_head():
    class JET_INDEXCREATE3_A(Structure):
        pass
    return JET_INDEXCREATE3_A
def _define_JET_INDEXCREATE3_A():
    JET_INDEXCREATE3_A = win32more.Storage.Jet.JET_INDEXCREATE3_A_head
    class JET_INDEXCREATE3_A__Anonymous_e__Union(Union):
        pass
    JET_INDEXCREATE3_A__Anonymous_e__Union._fields_ = [
        ('cbVarSegMac', UInt32),
        ('ptuplelimits', POINTER(win32more.Storage.Jet.JET_TUPLELIMITS_head)),
    ]
    JET_INDEXCREATE3_A._anonymous_ = [
        'Anonymous',
    ]
    JET_INDEXCREATE3_A._fields_ = [
        ('cbStruct', UInt32),
        ('szIndexName', win32more.Foundation.PSTR),
        ('szKey', win32more.Foundation.PSTR),
        ('cbKey', UInt32),
        ('grbit', UInt32),
        ('ulDensity', UInt32),
        ('pidxunicode', POINTER(win32more.Storage.Jet.JET_UNICODEINDEX2_head)),
        ('Anonymous', JET_INDEXCREATE3_A__Anonymous_e__Union),
        ('rgconditionalcolumn', POINTER(win32more.Storage.Jet.JET_CONDITIONALCOLUMN_A_head)),
        ('cConditionalColumn', UInt32),
        ('err', Int32),
        ('cbKeyMost', UInt32),
        ('pSpacehints', POINTER(win32more.Storage.Jet.JET_SPACEHINTS_head)),
    ]
    return JET_INDEXCREATE3_A
def _define_JET_INDEXCREATE3_W_head():
    class JET_INDEXCREATE3_W(Structure):
        pass
    return JET_INDEXCREATE3_W
def _define_JET_INDEXCREATE3_W():
    JET_INDEXCREATE3_W = win32more.Storage.Jet.JET_INDEXCREATE3_W_head
    class JET_INDEXCREATE3_W__Anonymous_e__Union(Union):
        pass
    JET_INDEXCREATE3_W__Anonymous_e__Union._fields_ = [
        ('cbVarSegMac', UInt32),
        ('ptuplelimits', POINTER(win32more.Storage.Jet.JET_TUPLELIMITS_head)),
    ]
    JET_INDEXCREATE3_W._anonymous_ = [
        'Anonymous',
    ]
    JET_INDEXCREATE3_W._fields_ = [
        ('cbStruct', UInt32),
        ('szIndexName', win32more.Foundation.PWSTR),
        ('szKey', win32more.Foundation.PWSTR),
        ('cbKey', UInt32),
        ('grbit', UInt32),
        ('ulDensity', UInt32),
        ('pidxunicode', POINTER(win32more.Storage.Jet.JET_UNICODEINDEX2_head)),
        ('Anonymous', JET_INDEXCREATE3_W__Anonymous_e__Union),
        ('rgconditionalcolumn', POINTER(win32more.Storage.Jet.JET_CONDITIONALCOLUMN_W_head)),
        ('cConditionalColumn', UInt32),
        ('err', Int32),
        ('cbKeyMost', UInt32),
        ('pSpacehints', POINTER(win32more.Storage.Jet.JET_SPACEHINTS_head)),
    ]
    return JET_INDEXCREATE3_W
def _define_JET_INDEXID_head():
    class JET_INDEXID(Structure):
        pass
    return JET_INDEXID
def _define_JET_INDEXID():
    JET_INDEXID = win32more.Storage.Jet.JET_INDEXID_head
    JET_INDEXID._fields_ = [
        ('cbStruct', UInt32),
        ('rgbIndexId', Byte * 16),
    ]
    return JET_INDEXID
def _define_JET_INDEXLIST_head():
    class JET_INDEXLIST(Structure):
        pass
    return JET_INDEXLIST
def _define_JET_INDEXLIST():
    JET_INDEXLIST = win32more.Storage.Jet.JET_INDEXLIST_head
    JET_INDEXLIST._fields_ = [
        ('cbStruct', UInt32),
        ('tableid', win32more.Storage.StructuredStorage.JET_TABLEID),
        ('cRecord', UInt32),
        ('columnidindexname', UInt32),
        ('columnidgrbitIndex', UInt32),
        ('columnidcKey', UInt32),
        ('columnidcEntry', UInt32),
        ('columnidcPage', UInt32),
        ('columnidcColumn', UInt32),
        ('columnidiColumn', UInt32),
        ('columnidcolumnid', UInt32),
        ('columnidcoltyp', UInt32),
        ('columnidCountry', UInt32),
        ('columnidLangid', UInt32),
        ('columnidCp', UInt32),
        ('columnidCollate', UInt32),
        ('columnidgrbitColumn', UInt32),
        ('columnidcolumnname', UInt32),
        ('columnidLCMapFlags', UInt32),
    ]
    return JET_INDEXLIST
def _define_JET_INDEXRANGE_head():
    class JET_INDEXRANGE(Structure):
        pass
    return JET_INDEXRANGE
def _define_JET_INDEXRANGE():
    JET_INDEXRANGE = win32more.Storage.Jet.JET_INDEXRANGE_head
    JET_INDEXRANGE._fields_ = [
        ('cbStruct', UInt32),
        ('tableid', win32more.Storage.StructuredStorage.JET_TABLEID),
        ('grbit', UInt32),
    ]
    return JET_INDEXRANGE
def _define_JET_INSTANCE_INFO_A_head():
    class JET_INSTANCE_INFO_A(Structure):
        pass
    return JET_INSTANCE_INFO_A
def _define_JET_INSTANCE_INFO_A():
    JET_INSTANCE_INFO_A = win32more.Storage.Jet.JET_INSTANCE_INFO_A_head
    JET_INSTANCE_INFO_A._fields_ = [
        ('hInstanceId', win32more.Storage.StructuredStorage.JET_INSTANCE),
        ('szInstanceName', win32more.Foundation.PSTR),
        ('cDatabases', win32more.Storage.StructuredStorage.JET_API_PTR),
        ('szDatabaseFileName', POINTER(POINTER(SByte))),
        ('szDatabaseDisplayName', POINTER(POINTER(SByte))),
        ('szDatabaseSLVFileName_Obsolete', POINTER(POINTER(SByte))),
    ]
    return JET_INSTANCE_INFO_A
def _define_JET_INSTANCE_INFO_W_head():
    class JET_INSTANCE_INFO_W(Structure):
        pass
    return JET_INSTANCE_INFO_W
def _define_JET_INSTANCE_INFO_W():
    JET_INSTANCE_INFO_W = win32more.Storage.Jet.JET_INSTANCE_INFO_W_head
    JET_INSTANCE_INFO_W._fields_ = [
        ('hInstanceId', win32more.Storage.StructuredStorage.JET_INSTANCE),
        ('szInstanceName', win32more.Foundation.PWSTR),
        ('cDatabases', win32more.Storage.StructuredStorage.JET_API_PTR),
        ('szDatabaseFileName', POINTER(POINTER(UInt16))),
        ('szDatabaseDisplayName', POINTER(POINTER(UInt16))),
        ('szDatabaseSLVFileName_Obsolete', POINTER(POINTER(UInt16))),
    ]
    return JET_INSTANCE_INFO_W
def _define_JET_LGPOS_head():
    class JET_LGPOS(Structure):
        pass
    return JET_LGPOS
def _define_JET_LGPOS():
    JET_LGPOS = win32more.Storage.Jet.JET_LGPOS_head
    JET_LGPOS._pack_ = 1
    JET_LGPOS._fields_ = [
        ('ib', UInt16),
        ('isec', UInt16),
        ('lGeneration', Int32),
    ]
    return JET_LGPOS
def _define_JET_LOGINFO_A_head():
    class JET_LOGINFO_A(Structure):
        pass
    return JET_LOGINFO_A
def _define_JET_LOGINFO_A():
    JET_LOGINFO_A = win32more.Storage.Jet.JET_LOGINFO_A_head
    JET_LOGINFO_A._fields_ = [
        ('cbSize', UInt32),
        ('ulGenLow', UInt32),
        ('ulGenHigh', UInt32),
        ('szBaseName', win32more.Foundation.CHAR * 4),
    ]
    return JET_LOGINFO_A
def _define_JET_LOGINFO_W_head():
    class JET_LOGINFO_W(Structure):
        pass
    return JET_LOGINFO_W
def _define_JET_LOGINFO_W():
    JET_LOGINFO_W = win32more.Storage.Jet.JET_LOGINFO_W_head
    JET_LOGINFO_W._fields_ = [
        ('cbSize', UInt32),
        ('ulGenLow', UInt32),
        ('ulGenHigh', UInt32),
        ('szBaseName', Char * 4),
    ]
    return JET_LOGINFO_W
def _define_JET_LOGTIME_head():
    class JET_LOGTIME(Structure):
        pass
    return JET_LOGTIME
def _define_JET_LOGTIME():
    JET_LOGTIME = win32more.Storage.Jet.JET_LOGTIME_head
    class JET_LOGTIME__Anonymous1_e__Union(Union):
        pass
    class JET_LOGTIME__Anonymous1_e__Union__Anonymous_e__Struct(Structure):
        pass
    JET_LOGTIME__Anonymous1_e__Union__Anonymous_e__Struct._fields_ = [
        ('_bitfield', Byte),
    ]
    JET_LOGTIME__Anonymous1_e__Union._anonymous_ = [
        'Anonymous',
    ]
    JET_LOGTIME__Anonymous1_e__Union._fields_ = [
        ('bFiller1', win32more.Foundation.CHAR),
        ('Anonymous', JET_LOGTIME__Anonymous1_e__Union__Anonymous_e__Struct),
    ]
    class JET_LOGTIME__Anonymous2_e__Union(Union):
        pass
    class JET_LOGTIME__Anonymous2_e__Union__Anonymous_e__Struct(Structure):
        pass
    JET_LOGTIME__Anonymous2_e__Union__Anonymous_e__Struct._fields_ = [
        ('_bitfield', Byte),
    ]
    JET_LOGTIME__Anonymous2_e__Union._anonymous_ = [
        'Anonymous',
    ]
    JET_LOGTIME__Anonymous2_e__Union._fields_ = [
        ('bFiller2', win32more.Foundation.CHAR),
        ('Anonymous', JET_LOGTIME__Anonymous2_e__Union__Anonymous_e__Struct),
    ]
    JET_LOGTIME._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    JET_LOGTIME._fields_ = [
        ('bSeconds', win32more.Foundation.CHAR),
        ('bMinutes', win32more.Foundation.CHAR),
        ('bHours', win32more.Foundation.CHAR),
        ('bDay', win32more.Foundation.CHAR),
        ('bMonth', win32more.Foundation.CHAR),
        ('bYear', win32more.Foundation.CHAR),
        ('Anonymous1', JET_LOGTIME__Anonymous1_e__Union),
        ('Anonymous2', JET_LOGTIME__Anonymous2_e__Union),
    ]
    return JET_LOGTIME
JET_LS = UIntPtr
def _define_JET_OBJECTINFO_head():
    class JET_OBJECTINFO(Structure):
        pass
    return JET_OBJECTINFO
def _define_JET_OBJECTINFO():
    JET_OBJECTINFO = win32more.Storage.Jet.JET_OBJECTINFO_head
    JET_OBJECTINFO._fields_ = [
        ('cbStruct', UInt32),
        ('objtyp', UInt32),
        ('dtCreate', Double),
        ('dtUpdate', Double),
        ('grbit', UInt32),
        ('flags', UInt32),
        ('cRecord', UInt32),
        ('cPage', UInt32),
    ]
    return JET_OBJECTINFO
def _define_JET_OBJECTLIST_head():
    class JET_OBJECTLIST(Structure):
        pass
    return JET_OBJECTLIST
def _define_JET_OBJECTLIST():
    JET_OBJECTLIST = win32more.Storage.Jet.JET_OBJECTLIST_head
    JET_OBJECTLIST._fields_ = [
        ('cbStruct', UInt32),
        ('tableid', win32more.Storage.StructuredStorage.JET_TABLEID),
        ('cRecord', UInt32),
        ('columnidcontainername', UInt32),
        ('columnidobjectname', UInt32),
        ('columnidobjtyp', UInt32),
        ('columniddtCreate', UInt32),
        ('columniddtUpdate', UInt32),
        ('columnidgrbit', UInt32),
        ('columnidflags', UInt32),
        ('columnidcRecord', UInt32),
        ('columnidcPage', UInt32),
    ]
    return JET_OBJECTLIST
def _define_JET_OPENTEMPORARYTABLE_head():
    class JET_OPENTEMPORARYTABLE(Structure):
        pass
    return JET_OPENTEMPORARYTABLE
def _define_JET_OPENTEMPORARYTABLE():
    JET_OPENTEMPORARYTABLE = win32more.Storage.Jet.JET_OPENTEMPORARYTABLE_head
    JET_OPENTEMPORARYTABLE._fields_ = [
        ('cbStruct', UInt32),
        ('prgcolumndef', POINTER(win32more.Storage.Jet.JET_COLUMNDEF_head)),
        ('ccolumn', UInt32),
        ('pidxunicode', POINTER(win32more.Storage.Jet.JET_UNICODEINDEX_head)),
        ('grbit', UInt32),
        ('prgcolumnid', POINTER(UInt32)),
        ('cbKeyMost', UInt32),
        ('cbVarSegMac', UInt32),
        ('tableid', win32more.Storage.StructuredStorage.JET_TABLEID),
    ]
    return JET_OPENTEMPORARYTABLE
def _define_JET_OPENTEMPORARYTABLE2_head():
    class JET_OPENTEMPORARYTABLE2(Structure):
        pass
    return JET_OPENTEMPORARYTABLE2
def _define_JET_OPENTEMPORARYTABLE2():
    JET_OPENTEMPORARYTABLE2 = win32more.Storage.Jet.JET_OPENTEMPORARYTABLE2_head
    JET_OPENTEMPORARYTABLE2._fields_ = [
        ('cbStruct', UInt32),
        ('prgcolumndef', POINTER(win32more.Storage.Jet.JET_COLUMNDEF_head)),
        ('ccolumn', UInt32),
        ('pidxunicode', POINTER(win32more.Storage.Jet.JET_UNICODEINDEX2_head)),
        ('grbit', UInt32),
        ('prgcolumnid', POINTER(UInt32)),
        ('cbKeyMost', UInt32),
        ('cbVarSegMac', UInt32),
        ('tableid', win32more.Storage.StructuredStorage.JET_TABLEID),
    ]
    return JET_OPENTEMPORARYTABLE2
def _define_JET_OPERATIONCONTEXT_head():
    class JET_OPERATIONCONTEXT(Structure):
        pass
    return JET_OPERATIONCONTEXT
def _define_JET_OPERATIONCONTEXT():
    JET_OPERATIONCONTEXT = win32more.Storage.Jet.JET_OPERATIONCONTEXT_head
    JET_OPERATIONCONTEXT._fields_ = [
        ('ulUserID', UInt32),
        ('nOperationID', Byte),
        ('nOperationType', Byte),
        ('nClientType', Byte),
        ('fFlags', Byte),
    ]
    return JET_OPERATIONCONTEXT
JET_OSSNAPID = UIntPtr
def _define_JET_PFNDURABLECOMMITCALLBACK():
    return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,POINTER(win32more.Storage.Jet.JET_COMMIT_ID_head),UInt32)
def _define_JET_PFNREALLOC():
    return WINFUNCTYPE(c_void_p,c_void_p,c_void_p,UInt32)
def _define_JET_PFNSTATUS():
    return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,UInt32,c_void_p)
def _define_JET_RBSINFOMISC_head():
    class JET_RBSINFOMISC(Structure):
        pass
    return JET_RBSINFOMISC
def _define_JET_RBSINFOMISC():
    JET_RBSINFOMISC = win32more.Storage.Jet.JET_RBSINFOMISC_head
    JET_RBSINFOMISC._fields_ = [
        ('lRBSGeneration', Int32),
        ('logtimeCreate', win32more.Storage.Jet.JET_LOGTIME),
        ('logtimeCreatePrevRBS', win32more.Storage.Jet.JET_LOGTIME),
        ('ulMajor', UInt32),
        ('ulMinor', UInt32),
        ('cbLogicalFileSize', UInt64),
    ]
    return JET_RBSINFOMISC
def _define_JET_RBSREVERTINFOMISC_head():
    class JET_RBSREVERTINFOMISC(Structure):
        pass
    return JET_RBSREVERTINFOMISC
def _define_JET_RBSREVERTINFOMISC():
    JET_RBSREVERTINFOMISC = win32more.Storage.Jet.JET_RBSREVERTINFOMISC_head
    JET_RBSREVERTINFOMISC._fields_ = [
        ('lGenMinRevertStart', Int32),
        ('lGenMaxRevertStart', Int32),
        ('lGenMinRevertEnd', Int32),
        ('lGenMaxRevertEnd', Int32),
        ('logtimeRevertFrom', win32more.Storage.Jet.JET_LOGTIME),
        ('cSecRevert', UInt64),
        ('cPagesReverted', UInt64),
    ]
    return JET_RBSREVERTINFOMISC
def _define_JET_RECORDLIST_head():
    class JET_RECORDLIST(Structure):
        pass
    return JET_RECORDLIST
def _define_JET_RECORDLIST():
    JET_RECORDLIST = win32more.Storage.Jet.JET_RECORDLIST_head
    JET_RECORDLIST._fields_ = [
        ('cbStruct', UInt32),
        ('tableid', win32more.Storage.StructuredStorage.JET_TABLEID),
        ('cRecord', UInt32),
        ('columnidBookmark', UInt32),
    ]
    return JET_RECORDLIST
def _define_JET_RECPOS_head():
    class JET_RECPOS(Structure):
        pass
    return JET_RECPOS
def _define_JET_RECPOS():
    JET_RECPOS = win32more.Storage.Jet.JET_RECPOS_head
    JET_RECPOS._fields_ = [
        ('cbStruct', UInt32),
        ('centriesLT', UInt32),
        ('centriesInRange', UInt32),
        ('centriesTotal', UInt32),
    ]
    return JET_RECPOS
def _define_JET_RECSIZE_head():
    class JET_RECSIZE(Structure):
        pass
    return JET_RECSIZE
def _define_JET_RECSIZE():
    JET_RECSIZE = win32more.Storage.Jet.JET_RECSIZE_head
    JET_RECSIZE._fields_ = [
        ('cbData', UInt64),
        ('cbLongValueData', UInt64),
        ('cbOverhead', UInt64),
        ('cbLongValueOverhead', UInt64),
        ('cNonTaggedColumns', UInt64),
        ('cTaggedColumns', UInt64),
        ('cLongValues', UInt64),
        ('cMultiValues', UInt64),
    ]
    return JET_RECSIZE
def _define_JET_RECSIZE2_head():
    class JET_RECSIZE2(Structure):
        pass
    return JET_RECSIZE2
def _define_JET_RECSIZE2():
    JET_RECSIZE2 = win32more.Storage.Jet.JET_RECSIZE2_head
    JET_RECSIZE2._fields_ = [
        ('cbData', UInt64),
        ('cbLongValueData', UInt64),
        ('cbOverhead', UInt64),
        ('cbLongValueOverhead', UInt64),
        ('cNonTaggedColumns', UInt64),
        ('cTaggedColumns', UInt64),
        ('cLongValues', UInt64),
        ('cMultiValues', UInt64),
        ('cCompressedColumns', UInt64),
        ('cbDataCompressed', UInt64),
        ('cbLongValueDataCompressed', UInt64),
    ]
    return JET_RECSIZE2
JET_RELOP = Int32
JET_relopEquals = 0
JET_relopPrefixEquals = 1
JET_relopNotEquals = 2
JET_relopLessThanOrEqual = 3
JET_relopLessThan = 4
JET_relopGreaterThanOrEqual = 5
JET_relopGreaterThan = 6
JET_relopBitmaskEqualsZero = 7
JET_relopBitmaskNotEqualsZero = 8
def _define_JET_RETINFO_head():
    class JET_RETINFO(Structure):
        pass
    return JET_RETINFO
def _define_JET_RETINFO():
    JET_RETINFO = win32more.Storage.Jet.JET_RETINFO_head
    JET_RETINFO._fields_ = [
        ('cbStruct', UInt32),
        ('ibLongValue', UInt32),
        ('itagSequence', UInt32),
        ('columnidNextTagged', UInt32),
    ]
    return JET_RETINFO
def _define_JET_RETRIEVECOLUMN_head():
    class JET_RETRIEVECOLUMN(Structure):
        pass
    return JET_RETRIEVECOLUMN
def _define_JET_RETRIEVECOLUMN():
    JET_RETRIEVECOLUMN = win32more.Storage.Jet.JET_RETRIEVECOLUMN_head
    JET_RETRIEVECOLUMN._fields_ = [
        ('columnid', UInt32),
        ('pvData', c_void_p),
        ('cbData', UInt32),
        ('cbActual', UInt32),
        ('grbit', UInt32),
        ('ibLongValue', UInt32),
        ('itagSequence', UInt32),
        ('columnidNextTagged', UInt32),
        ('err', Int32),
    ]
    return JET_RETRIEVECOLUMN
def _define_JET_RSTINFO_A_head():
    class JET_RSTINFO_A(Structure):
        pass
    return JET_RSTINFO_A
def _define_JET_RSTINFO_A():
    JET_RSTINFO_A = win32more.Storage.Jet.JET_RSTINFO_A_head
    JET_RSTINFO_A._fields_ = [
        ('cbStruct', UInt32),
        ('rgrstmap', POINTER(win32more.Storage.Jet.JET_RSTMAP_A_head)),
        ('crstmap', Int32),
        ('lgposStop', win32more.Storage.Jet.JET_LGPOS),
        ('logtimeStop', win32more.Storage.Jet.JET_LOGTIME),
        ('pfnStatus', win32more.Storage.Jet.JET_PFNSTATUS),
    ]
    return JET_RSTINFO_A
def _define_JET_RSTINFO_W_head():
    class JET_RSTINFO_W(Structure):
        pass
    return JET_RSTINFO_W
def _define_JET_RSTINFO_W():
    JET_RSTINFO_W = win32more.Storage.Jet.JET_RSTINFO_W_head
    JET_RSTINFO_W._fields_ = [
        ('cbStruct', UInt32),
        ('rgrstmap', POINTER(win32more.Storage.Jet.JET_RSTMAP_W_head)),
        ('crstmap', Int32),
        ('lgposStop', win32more.Storage.Jet.JET_LGPOS),
        ('logtimeStop', win32more.Storage.Jet.JET_LOGTIME),
        ('pfnStatus', win32more.Storage.Jet.JET_PFNSTATUS),
    ]
    return JET_RSTINFO_W
def _define_JET_RSTMAP_A_head():
    class JET_RSTMAP_A(Structure):
        pass
    return JET_RSTMAP_A
def _define_JET_RSTMAP_A():
    JET_RSTMAP_A = win32more.Storage.Jet.JET_RSTMAP_A_head
    JET_RSTMAP_A._fields_ = [
        ('szDatabaseName', win32more.Foundation.PSTR),
        ('szNewDatabaseName', win32more.Foundation.PSTR),
    ]
    return JET_RSTMAP_A
def _define_JET_RSTMAP_W_head():
    class JET_RSTMAP_W(Structure):
        pass
    return JET_RSTMAP_W
def _define_JET_RSTMAP_W():
    JET_RSTMAP_W = win32more.Storage.Jet.JET_RSTMAP_W_head
    JET_RSTMAP_W._fields_ = [
        ('szDatabaseName', win32more.Foundation.PWSTR),
        ('szNewDatabaseName', win32more.Foundation.PWSTR),
    ]
    return JET_RSTMAP_W
def _define_JET_SETCOLUMN_head():
    class JET_SETCOLUMN(Structure):
        pass
    return JET_SETCOLUMN
def _define_JET_SETCOLUMN():
    JET_SETCOLUMN = win32more.Storage.Jet.JET_SETCOLUMN_head
    JET_SETCOLUMN._fields_ = [
        ('columnid', UInt32),
        ('pvData', c_void_p),
        ('cbData', UInt32),
        ('grbit', UInt32),
        ('ibLongValue', UInt32),
        ('itagSequence', UInt32),
        ('err', Int32),
    ]
    return JET_SETCOLUMN
def _define_JET_SETINFO_head():
    class JET_SETINFO(Structure):
        pass
    return JET_SETINFO
def _define_JET_SETINFO():
    JET_SETINFO = win32more.Storage.Jet.JET_SETINFO_head
    JET_SETINFO._fields_ = [
        ('cbStruct', UInt32),
        ('ibLongValue', UInt32),
        ('itagSequence', UInt32),
    ]
    return JET_SETINFO
def _define_JET_SETSYSPARAM_A_head():
    class JET_SETSYSPARAM_A(Structure):
        pass
    return JET_SETSYSPARAM_A
def _define_JET_SETSYSPARAM_A():
    JET_SETSYSPARAM_A = win32more.Storage.Jet.JET_SETSYSPARAM_A_head
    JET_SETSYSPARAM_A._fields_ = [
        ('paramid', UInt32),
        ('lParam', win32more.Storage.StructuredStorage.JET_API_PTR),
        ('sz', win32more.Foundation.PSTR),
        ('err', Int32),
    ]
    return JET_SETSYSPARAM_A
def _define_JET_SETSYSPARAM_W_head():
    class JET_SETSYSPARAM_W(Structure):
        pass
    return JET_SETSYSPARAM_W
def _define_JET_SETSYSPARAM_W():
    JET_SETSYSPARAM_W = win32more.Storage.Jet.JET_SETSYSPARAM_W_head
    JET_SETSYSPARAM_W._fields_ = [
        ('paramid', UInt32),
        ('lParam', win32more.Storage.StructuredStorage.JET_API_PTR),
        ('sz', win32more.Foundation.PWSTR),
        ('err', Int32),
    ]
    return JET_SETSYSPARAM_W
def _define_JET_SIGNATURE_head():
    class JET_SIGNATURE(Structure):
        pass
    return JET_SIGNATURE
def _define_JET_SIGNATURE():
    JET_SIGNATURE = win32more.Storage.Jet.JET_SIGNATURE_head
    JET_SIGNATURE._pack_ = 1
    JET_SIGNATURE._fields_ = [
        ('ulRandom', UInt32),
        ('logtimeCreate', win32more.Storage.Jet.JET_LOGTIME),
        ('szComputerName', win32more.Foundation.CHAR * 16),
    ]
    return JET_SIGNATURE
def _define_JET_SNPROG_head():
    class JET_SNPROG(Structure):
        pass
    return JET_SNPROG
def _define_JET_SNPROG():
    JET_SNPROG = win32more.Storage.Jet.JET_SNPROG_head
    JET_SNPROG._fields_ = [
        ('cbStruct', UInt32),
        ('cunitDone', UInt32),
        ('cunitTotal', UInt32),
    ]
    return JET_SNPROG
def _define_JET_SPACEHINTS_head():
    class JET_SPACEHINTS(Structure):
        pass
    return JET_SPACEHINTS
def _define_JET_SPACEHINTS():
    JET_SPACEHINTS = win32more.Storage.Jet.JET_SPACEHINTS_head
    JET_SPACEHINTS._fields_ = [
        ('cbStruct', UInt32),
        ('ulInitialDensity', UInt32),
        ('cbInitial', UInt32),
        ('grbit', UInt32),
        ('ulMaintDensity', UInt32),
        ('ulGrowth', UInt32),
        ('cbMinExtent', UInt32),
        ('cbMaxExtent', UInt32),
    ]
    return JET_SPACEHINTS
def _define_JET_TABLECREATE_A_head():
    class JET_TABLECREATE_A(Structure):
        pass
    return JET_TABLECREATE_A
def _define_JET_TABLECREATE_A():
    JET_TABLECREATE_A = win32more.Storage.Jet.JET_TABLECREATE_A_head
    JET_TABLECREATE_A._fields_ = [
        ('cbStruct', UInt32),
        ('szTableName', win32more.Foundation.PSTR),
        ('szTemplateTableName', win32more.Foundation.PSTR),
        ('ulPages', UInt32),
        ('ulDensity', UInt32),
        ('rgcolumncreate', POINTER(win32more.Storage.Jet.JET_COLUMNCREATE_A_head)),
        ('cColumns', UInt32),
        ('rgindexcreate', POINTER(win32more.Storage.Jet.JET_INDEXCREATE_A_head)),
        ('cIndexes', UInt32),
        ('grbit', UInt32),
        ('tableid', win32more.Storage.StructuredStorage.JET_TABLEID),
        ('cCreated', UInt32),
    ]
    return JET_TABLECREATE_A
def _define_JET_TABLECREATE_W_head():
    class JET_TABLECREATE_W(Structure):
        pass
    return JET_TABLECREATE_W
def _define_JET_TABLECREATE_W():
    JET_TABLECREATE_W = win32more.Storage.Jet.JET_TABLECREATE_W_head
    JET_TABLECREATE_W._fields_ = [
        ('cbStruct', UInt32),
        ('szTableName', win32more.Foundation.PWSTR),
        ('szTemplateTableName', win32more.Foundation.PWSTR),
        ('ulPages', UInt32),
        ('ulDensity', UInt32),
        ('rgcolumncreate', POINTER(win32more.Storage.Jet.JET_COLUMNCREATE_W_head)),
        ('cColumns', UInt32),
        ('rgindexcreate', POINTER(win32more.Storage.Jet.JET_INDEXCREATE_W_head)),
        ('cIndexes', UInt32),
        ('grbit', UInt32),
        ('tableid', win32more.Storage.StructuredStorage.JET_TABLEID),
        ('cCreated', UInt32),
    ]
    return JET_TABLECREATE_W
def _define_JET_TABLECREATE2_A_head():
    class JET_TABLECREATE2_A(Structure):
        pass
    return JET_TABLECREATE2_A
def _define_JET_TABLECREATE2_A():
    JET_TABLECREATE2_A = win32more.Storage.Jet.JET_TABLECREATE2_A_head
    JET_TABLECREATE2_A._fields_ = [
        ('cbStruct', UInt32),
        ('szTableName', win32more.Foundation.PSTR),
        ('szTemplateTableName', win32more.Foundation.PSTR),
        ('ulPages', UInt32),
        ('ulDensity', UInt32),
        ('rgcolumncreate', POINTER(win32more.Storage.Jet.JET_COLUMNCREATE_A_head)),
        ('cColumns', UInt32),
        ('rgindexcreate', POINTER(win32more.Storage.Jet.JET_INDEXCREATE_A_head)),
        ('cIndexes', UInt32),
        ('szCallback', win32more.Foundation.PSTR),
        ('cbtyp', UInt32),
        ('grbit', UInt32),
        ('tableid', win32more.Storage.StructuredStorage.JET_TABLEID),
        ('cCreated', UInt32),
    ]
    return JET_TABLECREATE2_A
def _define_JET_TABLECREATE2_W_head():
    class JET_TABLECREATE2_W(Structure):
        pass
    return JET_TABLECREATE2_W
def _define_JET_TABLECREATE2_W():
    JET_TABLECREATE2_W = win32more.Storage.Jet.JET_TABLECREATE2_W_head
    JET_TABLECREATE2_W._fields_ = [
        ('cbStruct', UInt32),
        ('szTableName', win32more.Foundation.PWSTR),
        ('szTemplateTableName', win32more.Foundation.PWSTR),
        ('ulPages', UInt32),
        ('ulDensity', UInt32),
        ('rgcolumncreate', POINTER(win32more.Storage.Jet.JET_COLUMNCREATE_W_head)),
        ('cColumns', UInt32),
        ('rgindexcreate', POINTER(win32more.Storage.Jet.JET_INDEXCREATE_W_head)),
        ('cIndexes', UInt32),
        ('szCallback', win32more.Foundation.PWSTR),
        ('cbtyp', UInt32),
        ('grbit', UInt32),
        ('tableid', win32more.Storage.StructuredStorage.JET_TABLEID),
        ('cCreated', UInt32),
    ]
    return JET_TABLECREATE2_W
def _define_JET_TABLECREATE3_A_head():
    class JET_TABLECREATE3_A(Structure):
        pass
    return JET_TABLECREATE3_A
def _define_JET_TABLECREATE3_A():
    JET_TABLECREATE3_A = win32more.Storage.Jet.JET_TABLECREATE3_A_head
    JET_TABLECREATE3_A._fields_ = [
        ('cbStruct', UInt32),
        ('szTableName', win32more.Foundation.PSTR),
        ('szTemplateTableName', win32more.Foundation.PSTR),
        ('ulPages', UInt32),
        ('ulDensity', UInt32),
        ('rgcolumncreate', POINTER(win32more.Storage.Jet.JET_COLUMNCREATE_A_head)),
        ('cColumns', UInt32),
        ('rgindexcreate', POINTER(win32more.Storage.Jet.JET_INDEXCREATE2_A_head)),
        ('cIndexes', UInt32),
        ('szCallback', win32more.Foundation.PSTR),
        ('cbtyp', UInt32),
        ('grbit', UInt32),
        ('pSeqSpacehints', POINTER(win32more.Storage.Jet.JET_SPACEHINTS_head)),
        ('pLVSpacehints', POINTER(win32more.Storage.Jet.JET_SPACEHINTS_head)),
        ('cbSeparateLV', UInt32),
        ('tableid', win32more.Storage.StructuredStorage.JET_TABLEID),
        ('cCreated', UInt32),
    ]
    return JET_TABLECREATE3_A
def _define_JET_TABLECREATE3_W_head():
    class JET_TABLECREATE3_W(Structure):
        pass
    return JET_TABLECREATE3_W
def _define_JET_TABLECREATE3_W():
    JET_TABLECREATE3_W = win32more.Storage.Jet.JET_TABLECREATE3_W_head
    JET_TABLECREATE3_W._fields_ = [
        ('cbStruct', UInt32),
        ('szTableName', win32more.Foundation.PWSTR),
        ('szTemplateTableName', win32more.Foundation.PWSTR),
        ('ulPages', UInt32),
        ('ulDensity', UInt32),
        ('rgcolumncreate', POINTER(win32more.Storage.Jet.JET_COLUMNCREATE_W_head)),
        ('cColumns', UInt32),
        ('rgindexcreate', POINTER(win32more.Storage.Jet.JET_INDEXCREATE2_W_head)),
        ('cIndexes', UInt32),
        ('szCallback', win32more.Foundation.PWSTR),
        ('cbtyp', UInt32),
        ('grbit', UInt32),
        ('pSeqSpacehints', POINTER(win32more.Storage.Jet.JET_SPACEHINTS_head)),
        ('pLVSpacehints', POINTER(win32more.Storage.Jet.JET_SPACEHINTS_head)),
        ('cbSeparateLV', UInt32),
        ('tableid', win32more.Storage.StructuredStorage.JET_TABLEID),
        ('cCreated', UInt32),
    ]
    return JET_TABLECREATE3_W
def _define_JET_TABLECREATE4_A_head():
    class JET_TABLECREATE4_A(Structure):
        pass
    return JET_TABLECREATE4_A
def _define_JET_TABLECREATE4_A():
    JET_TABLECREATE4_A = win32more.Storage.Jet.JET_TABLECREATE4_A_head
    JET_TABLECREATE4_A._fields_ = [
        ('cbStruct', UInt32),
        ('szTableName', win32more.Foundation.PSTR),
        ('szTemplateTableName', win32more.Foundation.PSTR),
        ('ulPages', UInt32),
        ('ulDensity', UInt32),
        ('rgcolumncreate', POINTER(win32more.Storage.Jet.JET_COLUMNCREATE_A_head)),
        ('cColumns', UInt32),
        ('rgindexcreate', POINTER(win32more.Storage.Jet.JET_INDEXCREATE3_A_head)),
        ('cIndexes', UInt32),
        ('szCallback', win32more.Foundation.PSTR),
        ('cbtyp', UInt32),
        ('grbit', UInt32),
        ('pSeqSpacehints', POINTER(win32more.Storage.Jet.JET_SPACEHINTS_head)),
        ('pLVSpacehints', POINTER(win32more.Storage.Jet.JET_SPACEHINTS_head)),
        ('cbSeparateLV', UInt32),
        ('tableid', win32more.Storage.StructuredStorage.JET_TABLEID),
        ('cCreated', UInt32),
    ]
    return JET_TABLECREATE4_A
def _define_JET_TABLECREATE4_W_head():
    class JET_TABLECREATE4_W(Structure):
        pass
    return JET_TABLECREATE4_W
def _define_JET_TABLECREATE4_W():
    JET_TABLECREATE4_W = win32more.Storage.Jet.JET_TABLECREATE4_W_head
    JET_TABLECREATE4_W._fields_ = [
        ('cbStruct', UInt32),
        ('szTableName', win32more.Foundation.PWSTR),
        ('szTemplateTableName', win32more.Foundation.PWSTR),
        ('ulPages', UInt32),
        ('ulDensity', UInt32),
        ('rgcolumncreate', POINTER(win32more.Storage.Jet.JET_COLUMNCREATE_W_head)),
        ('cColumns', UInt32),
        ('rgindexcreate', POINTER(win32more.Storage.Jet.JET_INDEXCREATE3_W_head)),
        ('cIndexes', UInt32),
        ('szCallback', win32more.Foundation.PWSTR),
        ('cbtyp', UInt32),
        ('grbit', UInt32),
        ('pSeqSpacehints', POINTER(win32more.Storage.Jet.JET_SPACEHINTS_head)),
        ('pLVSpacehints', POINTER(win32more.Storage.Jet.JET_SPACEHINTS_head)),
        ('cbSeparateLV', UInt32),
        ('tableid', win32more.Storage.StructuredStorage.JET_TABLEID),
        ('cCreated', UInt32),
    ]
    return JET_TABLECREATE4_W
def _define_JET_THREADSTATS_head():
    class JET_THREADSTATS(Structure):
        pass
    return JET_THREADSTATS
def _define_JET_THREADSTATS():
    JET_THREADSTATS = win32more.Storage.Jet.JET_THREADSTATS_head
    JET_THREADSTATS._fields_ = [
        ('cbStruct', UInt32),
        ('cPageReferenced', UInt32),
        ('cPageRead', UInt32),
        ('cPagePreread', UInt32),
        ('cPageDirtied', UInt32),
        ('cPageRedirtied', UInt32),
        ('cLogRecord', UInt32),
        ('cbLogRecord', UInt32),
    ]
    return JET_THREADSTATS
def _define_JET_THREADSTATS2_head():
    class JET_THREADSTATS2(Structure):
        pass
    return JET_THREADSTATS2
def _define_JET_THREADSTATS2():
    JET_THREADSTATS2 = win32more.Storage.Jet.JET_THREADSTATS2_head
    JET_THREADSTATS2._fields_ = [
        ('cbStruct', UInt32),
        ('cPageReferenced', UInt32),
        ('cPageRead', UInt32),
        ('cPagePreread', UInt32),
        ('cPageDirtied', UInt32),
        ('cPageRedirtied', UInt32),
        ('cLogRecord', UInt32),
        ('cbLogRecord', UInt32),
        ('cusecPageCacheMiss', UInt64),
        ('cPageCacheMiss', UInt32),
    ]
    return JET_THREADSTATS2
def _define_JET_TUPLELIMITS_head():
    class JET_TUPLELIMITS(Structure):
        pass
    return JET_TUPLELIMITS
def _define_JET_TUPLELIMITS():
    JET_TUPLELIMITS = win32more.Storage.Jet.JET_TUPLELIMITS_head
    JET_TUPLELIMITS._fields_ = [
        ('chLengthMin', UInt32),
        ('chLengthMax', UInt32),
        ('chToIndexMax', UInt32),
        ('cchIncrement', UInt32),
        ('ichStart', UInt32),
    ]
    return JET_TUPLELIMITS
def _define_JET_UNICODEINDEX_head():
    class JET_UNICODEINDEX(Structure):
        pass
    return JET_UNICODEINDEX
def _define_JET_UNICODEINDEX():
    JET_UNICODEINDEX = win32more.Storage.Jet.JET_UNICODEINDEX_head
    JET_UNICODEINDEX._fields_ = [
        ('lcid', UInt32),
        ('dwMapFlags', UInt32),
    ]
    return JET_UNICODEINDEX
def _define_JET_UNICODEINDEX2_head():
    class JET_UNICODEINDEX2(Structure):
        pass
    return JET_UNICODEINDEX2
def _define_JET_UNICODEINDEX2():
    JET_UNICODEINDEX2 = win32more.Storage.Jet.JET_UNICODEINDEX2_head
    JET_UNICODEINDEX2._fields_ = [
        ('szLocaleName', win32more.Foundation.PWSTR),
        ('dwMapFlags', UInt32),
    ]
    return JET_UNICODEINDEX2
def _define_JET_USERDEFINEDDEFAULT_A_head():
    class JET_USERDEFINEDDEFAULT_A(Structure):
        pass
    return JET_USERDEFINEDDEFAULT_A
def _define_JET_USERDEFINEDDEFAULT_A():
    JET_USERDEFINEDDEFAULT_A = win32more.Storage.Jet.JET_USERDEFINEDDEFAULT_A_head
    JET_USERDEFINEDDEFAULT_A._fields_ = [
        ('szCallback', win32more.Foundation.PSTR),
        ('pbUserData', c_char_p_no),
        ('cbUserData', UInt32),
        ('szDependantColumns', win32more.Foundation.PSTR),
    ]
    return JET_USERDEFINEDDEFAULT_A
def _define_JET_USERDEFINEDDEFAULT_W_head():
    class JET_USERDEFINEDDEFAULT_W(Structure):
        pass
    return JET_USERDEFINEDDEFAULT_W
def _define_JET_USERDEFINEDDEFAULT_W():
    JET_USERDEFINEDDEFAULT_W = win32more.Storage.Jet.JET_USERDEFINEDDEFAULT_W_head
    JET_USERDEFINEDDEFAULT_W._fields_ = [
        ('szCallback', win32more.Foundation.PWSTR),
        ('pbUserData', c_char_p_no),
        ('cbUserData', UInt32),
        ('szDependantColumns', win32more.Foundation.PWSTR),
    ]
    return JET_USERDEFINEDDEFAULT_W
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
