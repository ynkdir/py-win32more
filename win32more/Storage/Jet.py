from win32more import *
import win32more.Storage.Jet
import win32more.Foundation
import win32more.Storage.StructuredStorage

def __getattr__(name):
    if f"_define_{name}" not in globals():
        raise AttributeError()
    setattr(win32more.Storage.Jet, name, globals()[f"_define_{name}"]())
    return getattr(win32more.Storage.Jet, name)
def __dir__():
    return __all__
JET_bitConfigStoreReadControlInhibitRead = 1
JET_bitConfigStoreReadControlDisableAll = 2
JET_bitConfigStoreReadControlDefault = 0
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
JET_OSSNAPID = UIntPtr
JET_LS = UIntPtr
def _define_JET_INDEXID_head():
    class JET_INDEXID(Structure):
        pass
    return JET_INDEXID
def _define_JET_INDEXID():
    JET_INDEXID = win32more.Storage.Jet.JET_INDEXID_head
    JET_INDEXID._fields_ = [
        ("cbStruct", UInt32),
        ("rgbIndexId", Byte * 16),
    ]
    return JET_INDEXID
def _define_JET_PFNSTATUS():
    return CFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,UInt32,c_void_p, use_last_error=False)
def _define_JET_RSTMAP_A_head():
    class JET_RSTMAP_A(Structure):
        pass
    return JET_RSTMAP_A
def _define_JET_RSTMAP_A():
    JET_RSTMAP_A = win32more.Storage.Jet.JET_RSTMAP_A_head
    JET_RSTMAP_A._fields_ = [
        ("szDatabaseName", win32more.Foundation.PSTR),
        ("szNewDatabaseName", win32more.Foundation.PSTR),
    ]
    return JET_RSTMAP_A
def _define_JET_RSTMAP_W_head():
    class JET_RSTMAP_W(Structure):
        pass
    return JET_RSTMAP_W
def _define_JET_RSTMAP_W():
    JET_RSTMAP_W = win32more.Storage.Jet.JET_RSTMAP_W_head
    JET_RSTMAP_W._fields_ = [
        ("szDatabaseName", win32more.Foundation.PWSTR),
        ("szNewDatabaseName", win32more.Foundation.PWSTR),
    ]
    return JET_RSTMAP_W
def _define_CONVERT_A_head():
    class CONVERT_A(Structure):
        pass
    return CONVERT_A
def _define_CONVERT_A():
    CONVERT_A = win32more.Storage.Jet.CONVERT_A_head
    class CONVERT_A__Anonymous_e__Union(Union):
        pass
    class CONVERT_A__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    CONVERT_A__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ("_bitfield", UInt32),
    ]
    CONVERT_A__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    CONVERT_A__Anonymous_e__Union._fields_ = [
        ("fFlags", UInt32),
        ("Anonymous", CONVERT_A__Anonymous_e__Union__Anonymous_e__Struct),
    ]
    CONVERT_A._anonymous_ = [
        'Anonymous',
    ]
    CONVERT_A._fields_ = [
        ("szOldDll", win32more.Foundation.PSTR),
        ("Anonymous", CONVERT_A__Anonymous_e__Union),
    ]
    return CONVERT_A
def _define_CONVERT_W_head():
    class CONVERT_W(Structure):
        pass
    return CONVERT_W
def _define_CONVERT_W():
    CONVERT_W = win32more.Storage.Jet.CONVERT_W_head
    class CONVERT_W__Anonymous_e__Union(Union):
        pass
    class CONVERT_W__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    CONVERT_W__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ("_bitfield", UInt32),
    ]
    CONVERT_W__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    CONVERT_W__Anonymous_e__Union._fields_ = [
        ("fFlags", UInt32),
        ("Anonymous", CONVERT_W__Anonymous_e__Union__Anonymous_e__Struct),
    ]
    CONVERT_W._anonymous_ = [
        'Anonymous',
    ]
    CONVERT_W._fields_ = [
        ("szOldDll", win32more.Foundation.PWSTR),
        ("Anonymous", CONVERT_W__Anonymous_e__Union),
    ]
    return CONVERT_W
def _define_JET_CALLBACK():
    return CFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,win32more.Storage.StructuredStorage.JET_TABLEID,UInt32,c_void_p,c_void_p,c_void_p,win32more.Storage.StructuredStorage.JET_API_PTR, use_last_error=False)
def _define_JET_SNPROG_head():
    class JET_SNPROG(Structure):
        pass
    return JET_SNPROG
def _define_JET_SNPROG():
    JET_SNPROG = win32more.Storage.Jet.JET_SNPROG_head
    JET_SNPROG._fields_ = [
        ("cbStruct", UInt32),
        ("cunitDone", UInt32),
        ("cunitTotal", UInt32),
    ]
    return JET_SNPROG
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
        ("_bitfield", UInt32),
    ]
    JET_DBINFOUPGRADE__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    JET_DBINFOUPGRADE__Anonymous_e__Union._fields_ = [
        ("ulFlags", UInt32),
        ("Anonymous", JET_DBINFOUPGRADE__Anonymous_e__Union__Anonymous_e__Struct),
    ]
    JET_DBINFOUPGRADE._anonymous_ = [
        'Anonymous',
    ]
    JET_DBINFOUPGRADE._fields_ = [
        ("cbStruct", UInt32),
        ("cbFilesizeLow", UInt32),
        ("cbFilesizeHigh", UInt32),
        ("cbFreeSpaceRequiredLow", UInt32),
        ("cbFreeSpaceRequiredHigh", UInt32),
        ("csecToUpgrade", UInt32),
        ("Anonymous", JET_DBINFOUPGRADE__Anonymous_e__Union),
    ]
    return JET_DBINFOUPGRADE
def _define_JET_OBJECTINFO_head():
    class JET_OBJECTINFO(Structure):
        pass
    return JET_OBJECTINFO
def _define_JET_OBJECTINFO():
    JET_OBJECTINFO = win32more.Storage.Jet.JET_OBJECTINFO_head
    JET_OBJECTINFO._fields_ = [
        ("cbStruct", UInt32),
        ("objtyp", UInt32),
        ("dtCreate", Double),
        ("dtUpdate", Double),
        ("grbit", UInt32),
        ("flags", UInt32),
        ("cRecord", UInt32),
        ("cPage", UInt32),
    ]
    return JET_OBJECTINFO
def _define_JET_OBJECTLIST_head():
    class JET_OBJECTLIST(Structure):
        pass
    return JET_OBJECTLIST
def _define_JET_OBJECTLIST():
    JET_OBJECTLIST = win32more.Storage.Jet.JET_OBJECTLIST_head
    JET_OBJECTLIST._fields_ = [
        ("cbStruct", UInt32),
        ("tableid", win32more.Storage.StructuredStorage.JET_TABLEID),
        ("cRecord", UInt32),
        ("columnidcontainername", UInt32),
        ("columnidobjectname", UInt32),
        ("columnidobjtyp", UInt32),
        ("columniddtCreate", UInt32),
        ("columniddtUpdate", UInt32),
        ("columnidgrbit", UInt32),
        ("columnidflags", UInt32),
        ("columnidcRecord", UInt32),
        ("columnidcPage", UInt32),
    ]
    return JET_OBJECTLIST
def _define_JET_COLUMNLIST_head():
    class JET_COLUMNLIST(Structure):
        pass
    return JET_COLUMNLIST
def _define_JET_COLUMNLIST():
    JET_COLUMNLIST = win32more.Storage.Jet.JET_COLUMNLIST_head
    JET_COLUMNLIST._fields_ = [
        ("cbStruct", UInt32),
        ("tableid", win32more.Storage.StructuredStorage.JET_TABLEID),
        ("cRecord", UInt32),
        ("columnidPresentationOrder", UInt32),
        ("columnidcolumnname", UInt32),
        ("columnidcolumnid", UInt32),
        ("columnidcoltyp", UInt32),
        ("columnidCountry", UInt32),
        ("columnidLangid", UInt32),
        ("columnidCp", UInt32),
        ("columnidCollate", UInt32),
        ("columnidcbMax", UInt32),
        ("columnidgrbit", UInt32),
        ("columnidDefault", UInt32),
        ("columnidBaseTableName", UInt32),
        ("columnidBaseColumnName", UInt32),
        ("columnidDefinitionName", UInt32),
    ]
    return JET_COLUMNLIST
def _define_JET_COLUMNDEF_head():
    class JET_COLUMNDEF(Structure):
        pass
    return JET_COLUMNDEF
def _define_JET_COLUMNDEF():
    JET_COLUMNDEF = win32more.Storage.Jet.JET_COLUMNDEF_head
    JET_COLUMNDEF._fields_ = [
        ("cbStruct", UInt32),
        ("columnid", UInt32),
        ("coltyp", UInt32),
        ("wCountry", UInt16),
        ("langid", UInt16),
        ("cp", UInt16),
        ("wCollate", UInt16),
        ("cbMax", UInt32),
        ("grbit", UInt32),
    ]
    return JET_COLUMNDEF
def _define_JET_COLUMNBASE_A_head():
    class JET_COLUMNBASE_A(Structure):
        pass
    return JET_COLUMNBASE_A
def _define_JET_COLUMNBASE_A():
    JET_COLUMNBASE_A = win32more.Storage.Jet.JET_COLUMNBASE_A_head
    JET_COLUMNBASE_A._fields_ = [
        ("cbStruct", UInt32),
        ("columnid", UInt32),
        ("coltyp", UInt32),
        ("wCountry", UInt16),
        ("langid", UInt16),
        ("cp", UInt16),
        ("wFiller", UInt16),
        ("cbMax", UInt32),
        ("grbit", UInt32),
        ("szBaseTableName", win32more.Foundation.CHAR * 256),
        ("szBaseColumnName", win32more.Foundation.CHAR * 256),
    ]
    return JET_COLUMNBASE_A
def _define_JET_COLUMNBASE_W_head():
    class JET_COLUMNBASE_W(Structure):
        pass
    return JET_COLUMNBASE_W
def _define_JET_COLUMNBASE_W():
    JET_COLUMNBASE_W = win32more.Storage.Jet.JET_COLUMNBASE_W_head
    JET_COLUMNBASE_W._fields_ = [
        ("cbStruct", UInt32),
        ("columnid", UInt32),
        ("coltyp", UInt32),
        ("wCountry", UInt16),
        ("langid", UInt16),
        ("cp", UInt16),
        ("wFiller", UInt16),
        ("cbMax", UInt32),
        ("grbit", UInt32),
        ("szBaseTableName", Char * 256),
        ("szBaseColumnName", Char * 256),
    ]
    return JET_COLUMNBASE_W
def _define_JET_INDEXLIST_head():
    class JET_INDEXLIST(Structure):
        pass
    return JET_INDEXLIST
def _define_JET_INDEXLIST():
    JET_INDEXLIST = win32more.Storage.Jet.JET_INDEXLIST_head
    JET_INDEXLIST._fields_ = [
        ("cbStruct", UInt32),
        ("tableid", win32more.Storage.StructuredStorage.JET_TABLEID),
        ("cRecord", UInt32),
        ("columnidindexname", UInt32),
        ("columnidgrbitIndex", UInt32),
        ("columnidcKey", UInt32),
        ("columnidcEntry", UInt32),
        ("columnidcPage", UInt32),
        ("columnidcColumn", UInt32),
        ("columnidiColumn", UInt32),
        ("columnidcolumnid", UInt32),
        ("columnidcoltyp", UInt32),
        ("columnidCountry", UInt32),
        ("columnidLangid", UInt32),
        ("columnidCp", UInt32),
        ("columnidCollate", UInt32),
        ("columnidgrbitColumn", UInt32),
        ("columnidcolumnname", UInt32),
        ("columnidLCMapFlags", UInt32),
    ]
    return JET_INDEXLIST
def _define_JET_COLUMNCREATE_A_head():
    class JET_COLUMNCREATE_A(Structure):
        pass
    return JET_COLUMNCREATE_A
def _define_JET_COLUMNCREATE_A():
    JET_COLUMNCREATE_A = win32more.Storage.Jet.JET_COLUMNCREATE_A_head
    JET_COLUMNCREATE_A._fields_ = [
        ("cbStruct", UInt32),
        ("szColumnName", win32more.Foundation.PSTR),
        ("coltyp", UInt32),
        ("cbMax", UInt32),
        ("grbit", UInt32),
        ("pvDefault", c_void_p),
        ("cbDefault", UInt32),
        ("cp", UInt32),
        ("columnid", UInt32),
        ("err", Int32),
    ]
    return JET_COLUMNCREATE_A
def _define_JET_COLUMNCREATE_W_head():
    class JET_COLUMNCREATE_W(Structure):
        pass
    return JET_COLUMNCREATE_W
def _define_JET_COLUMNCREATE_W():
    JET_COLUMNCREATE_W = win32more.Storage.Jet.JET_COLUMNCREATE_W_head
    JET_COLUMNCREATE_W._fields_ = [
        ("cbStruct", UInt32),
        ("szColumnName", win32more.Foundation.PWSTR),
        ("coltyp", UInt32),
        ("cbMax", UInt32),
        ("grbit", UInt32),
        ("pvDefault", c_void_p),
        ("cbDefault", UInt32),
        ("cp", UInt32),
        ("columnid", UInt32),
        ("err", Int32),
    ]
    return JET_COLUMNCREATE_W
def _define_JET_USERDEFINEDDEFAULT_A_head():
    class JET_USERDEFINEDDEFAULT_A(Structure):
        pass
    return JET_USERDEFINEDDEFAULT_A
def _define_JET_USERDEFINEDDEFAULT_A():
    JET_USERDEFINEDDEFAULT_A = win32more.Storage.Jet.JET_USERDEFINEDDEFAULT_A_head
    JET_USERDEFINEDDEFAULT_A._fields_ = [
        ("szCallback", win32more.Foundation.PSTR),
        ("pbUserData", c_char_p_no),
        ("cbUserData", UInt32),
        ("szDependantColumns", win32more.Foundation.PSTR),
    ]
    return JET_USERDEFINEDDEFAULT_A
def _define_JET_USERDEFINEDDEFAULT_W_head():
    class JET_USERDEFINEDDEFAULT_W(Structure):
        pass
    return JET_USERDEFINEDDEFAULT_W
def _define_JET_USERDEFINEDDEFAULT_W():
    JET_USERDEFINEDDEFAULT_W = win32more.Storage.Jet.JET_USERDEFINEDDEFAULT_W_head
    JET_USERDEFINEDDEFAULT_W._fields_ = [
        ("szCallback", win32more.Foundation.PWSTR),
        ("pbUserData", c_char_p_no),
        ("cbUserData", UInt32),
        ("szDependantColumns", win32more.Foundation.PWSTR),
    ]
    return JET_USERDEFINEDDEFAULT_W
def _define_JET_CONDITIONALCOLUMN_A_head():
    class JET_CONDITIONALCOLUMN_A(Structure):
        pass
    return JET_CONDITIONALCOLUMN_A
def _define_JET_CONDITIONALCOLUMN_A():
    JET_CONDITIONALCOLUMN_A = win32more.Storage.Jet.JET_CONDITIONALCOLUMN_A_head
    JET_CONDITIONALCOLUMN_A._fields_ = [
        ("cbStruct", UInt32),
        ("szColumnName", win32more.Foundation.PSTR),
        ("grbit", UInt32),
    ]
    return JET_CONDITIONALCOLUMN_A
def _define_JET_CONDITIONALCOLUMN_W_head():
    class JET_CONDITIONALCOLUMN_W(Structure):
        pass
    return JET_CONDITIONALCOLUMN_W
def _define_JET_CONDITIONALCOLUMN_W():
    JET_CONDITIONALCOLUMN_W = win32more.Storage.Jet.JET_CONDITIONALCOLUMN_W_head
    JET_CONDITIONALCOLUMN_W._fields_ = [
        ("cbStruct", UInt32),
        ("szColumnName", win32more.Foundation.PWSTR),
        ("grbit", UInt32),
    ]
    return JET_CONDITIONALCOLUMN_W
def _define_JET_UNICODEINDEX_head():
    class JET_UNICODEINDEX(Structure):
        pass
    return JET_UNICODEINDEX
def _define_JET_UNICODEINDEX():
    JET_UNICODEINDEX = win32more.Storage.Jet.JET_UNICODEINDEX_head
    JET_UNICODEINDEX._fields_ = [
        ("lcid", UInt32),
        ("dwMapFlags", UInt32),
    ]
    return JET_UNICODEINDEX
def _define_JET_UNICODEINDEX2_head():
    class JET_UNICODEINDEX2(Structure):
        pass
    return JET_UNICODEINDEX2
def _define_JET_UNICODEINDEX2():
    JET_UNICODEINDEX2 = win32more.Storage.Jet.JET_UNICODEINDEX2_head
    JET_UNICODEINDEX2._fields_ = [
        ("szLocaleName", win32more.Foundation.PWSTR),
        ("dwMapFlags", UInt32),
    ]
    return JET_UNICODEINDEX2
def _define_JET_TUPLELIMITS_head():
    class JET_TUPLELIMITS(Structure):
        pass
    return JET_TUPLELIMITS
def _define_JET_TUPLELIMITS():
    JET_TUPLELIMITS = win32more.Storage.Jet.JET_TUPLELIMITS_head
    JET_TUPLELIMITS._fields_ = [
        ("chLengthMin", UInt32),
        ("chLengthMax", UInt32),
        ("chToIndexMax", UInt32),
        ("cchIncrement", UInt32),
        ("ichStart", UInt32),
    ]
    return JET_TUPLELIMITS
def _define_JET_SPACEHINTS_head():
    class JET_SPACEHINTS(Structure):
        pass
    return JET_SPACEHINTS
def _define_JET_SPACEHINTS():
    JET_SPACEHINTS = win32more.Storage.Jet.JET_SPACEHINTS_head
    JET_SPACEHINTS._fields_ = [
        ("cbStruct", UInt32),
        ("ulInitialDensity", UInt32),
        ("cbInitial", UInt32),
        ("grbit", UInt32),
        ("ulMaintDensity", UInt32),
        ("ulGrowth", UInt32),
        ("cbMinExtent", UInt32),
        ("cbMaxExtent", UInt32),
    ]
    return JET_SPACEHINTS
def _define_JET_INDEXCREATE_A_head():
    class JET_INDEXCREATE_A(Structure):
        pass
    return JET_INDEXCREATE_A
def _define_JET_INDEXCREATE_A():
    JET_INDEXCREATE_A = win32more.Storage.Jet.JET_INDEXCREATE_A_head
    class JET_INDEXCREATE_A__Anonymous1_e__Union(Union):
        pass
    JET_INDEXCREATE_A__Anonymous1_e__Union._fields_ = [
        ("lcid", UInt32),
        ("pidxunicode", POINTER(win32more.Storage.Jet.JET_UNICODEINDEX_head)),
    ]
    class JET_INDEXCREATE_A__Anonymous2_e__Union(Union):
        pass
    JET_INDEXCREATE_A__Anonymous2_e__Union._fields_ = [
        ("cbVarSegMac", UInt32),
        ("ptuplelimits", POINTER(win32more.Storage.Jet.JET_TUPLELIMITS_head)),
    ]
    JET_INDEXCREATE_A._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    JET_INDEXCREATE_A._fields_ = [
        ("cbStruct", UInt32),
        ("szIndexName", win32more.Foundation.PSTR),
        ("szKey", win32more.Foundation.PSTR),
        ("cbKey", UInt32),
        ("grbit", UInt32),
        ("ulDensity", UInt32),
        ("Anonymous1", JET_INDEXCREATE_A__Anonymous1_e__Union),
        ("Anonymous2", JET_INDEXCREATE_A__Anonymous2_e__Union),
        ("rgconditionalcolumn", POINTER(win32more.Storage.Jet.JET_CONDITIONALCOLUMN_A_head)),
        ("cConditionalColumn", UInt32),
        ("err", Int32),
        ("cbKeyMost", UInt32),
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
        ("lcid", UInt32),
        ("pidxunicode", POINTER(win32more.Storage.Jet.JET_UNICODEINDEX_head)),
    ]
    class JET_INDEXCREATE_W__Anonymous2_e__Union(Union):
        pass
    JET_INDEXCREATE_W__Anonymous2_e__Union._fields_ = [
        ("cbVarSegMac", UInt32),
        ("ptuplelimits", POINTER(win32more.Storage.Jet.JET_TUPLELIMITS_head)),
    ]
    JET_INDEXCREATE_W._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    JET_INDEXCREATE_W._fields_ = [
        ("cbStruct", UInt32),
        ("szIndexName", win32more.Foundation.PWSTR),
        ("szKey", win32more.Foundation.PWSTR),
        ("cbKey", UInt32),
        ("grbit", UInt32),
        ("ulDensity", UInt32),
        ("Anonymous1", JET_INDEXCREATE_W__Anonymous1_e__Union),
        ("Anonymous2", JET_INDEXCREATE_W__Anonymous2_e__Union),
        ("rgconditionalcolumn", POINTER(win32more.Storage.Jet.JET_CONDITIONALCOLUMN_W_head)),
        ("cConditionalColumn", UInt32),
        ("err", Int32),
        ("cbKeyMost", UInt32),
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
        ("lcid", UInt32),
        ("pidxunicode", POINTER(win32more.Storage.Jet.JET_UNICODEINDEX_head)),
    ]
    class JET_INDEXCREATE2_A__Anonymous2_e__Union(Union):
        pass
    JET_INDEXCREATE2_A__Anonymous2_e__Union._fields_ = [
        ("cbVarSegMac", UInt32),
        ("ptuplelimits", POINTER(win32more.Storage.Jet.JET_TUPLELIMITS_head)),
    ]
    JET_INDEXCREATE2_A._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    JET_INDEXCREATE2_A._fields_ = [
        ("cbStruct", UInt32),
        ("szIndexName", win32more.Foundation.PSTR),
        ("szKey", win32more.Foundation.PSTR),
        ("cbKey", UInt32),
        ("grbit", UInt32),
        ("ulDensity", UInt32),
        ("Anonymous1", JET_INDEXCREATE2_A__Anonymous1_e__Union),
        ("Anonymous2", JET_INDEXCREATE2_A__Anonymous2_e__Union),
        ("rgconditionalcolumn", POINTER(win32more.Storage.Jet.JET_CONDITIONALCOLUMN_A_head)),
        ("cConditionalColumn", UInt32),
        ("err", Int32),
        ("cbKeyMost", UInt32),
        ("pSpacehints", POINTER(win32more.Storage.Jet.JET_SPACEHINTS_head)),
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
        ("lcid", UInt32),
        ("pidxunicode", POINTER(win32more.Storage.Jet.JET_UNICODEINDEX_head)),
    ]
    class JET_INDEXCREATE2_W__Anonymous2_e__Union(Union):
        pass
    JET_INDEXCREATE2_W__Anonymous2_e__Union._fields_ = [
        ("cbVarSegMac", UInt32),
        ("ptuplelimits", POINTER(win32more.Storage.Jet.JET_TUPLELIMITS_head)),
    ]
    JET_INDEXCREATE2_W._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    JET_INDEXCREATE2_W._fields_ = [
        ("cbStruct", UInt32),
        ("szIndexName", win32more.Foundation.PWSTR),
        ("szKey", win32more.Foundation.PWSTR),
        ("cbKey", UInt32),
        ("grbit", UInt32),
        ("ulDensity", UInt32),
        ("Anonymous1", JET_INDEXCREATE2_W__Anonymous1_e__Union),
        ("Anonymous2", JET_INDEXCREATE2_W__Anonymous2_e__Union),
        ("rgconditionalcolumn", POINTER(win32more.Storage.Jet.JET_CONDITIONALCOLUMN_W_head)),
        ("cConditionalColumn", UInt32),
        ("err", Int32),
        ("cbKeyMost", UInt32),
        ("pSpacehints", POINTER(win32more.Storage.Jet.JET_SPACEHINTS_head)),
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
        ("cbVarSegMac", UInt32),
        ("ptuplelimits", POINTER(win32more.Storage.Jet.JET_TUPLELIMITS_head)),
    ]
    JET_INDEXCREATE3_A._anonymous_ = [
        'Anonymous',
    ]
    JET_INDEXCREATE3_A._fields_ = [
        ("cbStruct", UInt32),
        ("szIndexName", win32more.Foundation.PSTR),
        ("szKey", win32more.Foundation.PSTR),
        ("cbKey", UInt32),
        ("grbit", UInt32),
        ("ulDensity", UInt32),
        ("pidxunicode", POINTER(win32more.Storage.Jet.JET_UNICODEINDEX2_head)),
        ("Anonymous", JET_INDEXCREATE3_A__Anonymous_e__Union),
        ("rgconditionalcolumn", POINTER(win32more.Storage.Jet.JET_CONDITIONALCOLUMN_A_head)),
        ("cConditionalColumn", UInt32),
        ("err", Int32),
        ("cbKeyMost", UInt32),
        ("pSpacehints", POINTER(win32more.Storage.Jet.JET_SPACEHINTS_head)),
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
        ("cbVarSegMac", UInt32),
        ("ptuplelimits", POINTER(win32more.Storage.Jet.JET_TUPLELIMITS_head)),
    ]
    JET_INDEXCREATE3_W._anonymous_ = [
        'Anonymous',
    ]
    JET_INDEXCREATE3_W._fields_ = [
        ("cbStruct", UInt32),
        ("szIndexName", win32more.Foundation.PWSTR),
        ("szKey", win32more.Foundation.PWSTR),
        ("cbKey", UInt32),
        ("grbit", UInt32),
        ("ulDensity", UInt32),
        ("pidxunicode", POINTER(win32more.Storage.Jet.JET_UNICODEINDEX2_head)),
        ("Anonymous", JET_INDEXCREATE3_W__Anonymous_e__Union),
        ("rgconditionalcolumn", POINTER(win32more.Storage.Jet.JET_CONDITIONALCOLUMN_W_head)),
        ("cConditionalColumn", UInt32),
        ("err", Int32),
        ("cbKeyMost", UInt32),
        ("pSpacehints", POINTER(win32more.Storage.Jet.JET_SPACEHINTS_head)),
    ]
    return JET_INDEXCREATE3_W
def _define_JET_TABLECREATE_A_head():
    class JET_TABLECREATE_A(Structure):
        pass
    return JET_TABLECREATE_A
def _define_JET_TABLECREATE_A():
    JET_TABLECREATE_A = win32more.Storage.Jet.JET_TABLECREATE_A_head
    JET_TABLECREATE_A._fields_ = [
        ("cbStruct", UInt32),
        ("szTableName", win32more.Foundation.PSTR),
        ("szTemplateTableName", win32more.Foundation.PSTR),
        ("ulPages", UInt32),
        ("ulDensity", UInt32),
        ("rgcolumncreate", POINTER(win32more.Storage.Jet.JET_COLUMNCREATE_A_head)),
        ("cColumns", UInt32),
        ("rgindexcreate", POINTER(win32more.Storage.Jet.JET_INDEXCREATE_A_head)),
        ("cIndexes", UInt32),
        ("grbit", UInt32),
        ("tableid", win32more.Storage.StructuredStorage.JET_TABLEID),
        ("cCreated", UInt32),
    ]
    return JET_TABLECREATE_A
def _define_JET_TABLECREATE_W_head():
    class JET_TABLECREATE_W(Structure):
        pass
    return JET_TABLECREATE_W
def _define_JET_TABLECREATE_W():
    JET_TABLECREATE_W = win32more.Storage.Jet.JET_TABLECREATE_W_head
    JET_TABLECREATE_W._fields_ = [
        ("cbStruct", UInt32),
        ("szTableName", win32more.Foundation.PWSTR),
        ("szTemplateTableName", win32more.Foundation.PWSTR),
        ("ulPages", UInt32),
        ("ulDensity", UInt32),
        ("rgcolumncreate", POINTER(win32more.Storage.Jet.JET_COLUMNCREATE_W_head)),
        ("cColumns", UInt32),
        ("rgindexcreate", POINTER(win32more.Storage.Jet.JET_INDEXCREATE_W_head)),
        ("cIndexes", UInt32),
        ("grbit", UInt32),
        ("tableid", win32more.Storage.StructuredStorage.JET_TABLEID),
        ("cCreated", UInt32),
    ]
    return JET_TABLECREATE_W
def _define_JET_TABLECREATE2_A_head():
    class JET_TABLECREATE2_A(Structure):
        pass
    return JET_TABLECREATE2_A
def _define_JET_TABLECREATE2_A():
    JET_TABLECREATE2_A = win32more.Storage.Jet.JET_TABLECREATE2_A_head
    JET_TABLECREATE2_A._fields_ = [
        ("cbStruct", UInt32),
        ("szTableName", win32more.Foundation.PSTR),
        ("szTemplateTableName", win32more.Foundation.PSTR),
        ("ulPages", UInt32),
        ("ulDensity", UInt32),
        ("rgcolumncreate", POINTER(win32more.Storage.Jet.JET_COLUMNCREATE_A_head)),
        ("cColumns", UInt32),
        ("rgindexcreate", POINTER(win32more.Storage.Jet.JET_INDEXCREATE_A_head)),
        ("cIndexes", UInt32),
        ("szCallback", win32more.Foundation.PSTR),
        ("cbtyp", UInt32),
        ("grbit", UInt32),
        ("tableid", win32more.Storage.StructuredStorage.JET_TABLEID),
        ("cCreated", UInt32),
    ]
    return JET_TABLECREATE2_A
def _define_JET_TABLECREATE2_W_head():
    class JET_TABLECREATE2_W(Structure):
        pass
    return JET_TABLECREATE2_W
def _define_JET_TABLECREATE2_W():
    JET_TABLECREATE2_W = win32more.Storage.Jet.JET_TABLECREATE2_W_head
    JET_TABLECREATE2_W._fields_ = [
        ("cbStruct", UInt32),
        ("szTableName", win32more.Foundation.PWSTR),
        ("szTemplateTableName", win32more.Foundation.PWSTR),
        ("ulPages", UInt32),
        ("ulDensity", UInt32),
        ("rgcolumncreate", POINTER(win32more.Storage.Jet.JET_COLUMNCREATE_W_head)),
        ("cColumns", UInt32),
        ("rgindexcreate", POINTER(win32more.Storage.Jet.JET_INDEXCREATE_W_head)),
        ("cIndexes", UInt32),
        ("szCallback", win32more.Foundation.PWSTR),
        ("cbtyp", UInt32),
        ("grbit", UInt32),
        ("tableid", win32more.Storage.StructuredStorage.JET_TABLEID),
        ("cCreated", UInt32),
    ]
    return JET_TABLECREATE2_W
def _define_JET_TABLECREATE3_A_head():
    class JET_TABLECREATE3_A(Structure):
        pass
    return JET_TABLECREATE3_A
def _define_JET_TABLECREATE3_A():
    JET_TABLECREATE3_A = win32more.Storage.Jet.JET_TABLECREATE3_A_head
    JET_TABLECREATE3_A._fields_ = [
        ("cbStruct", UInt32),
        ("szTableName", win32more.Foundation.PSTR),
        ("szTemplateTableName", win32more.Foundation.PSTR),
        ("ulPages", UInt32),
        ("ulDensity", UInt32),
        ("rgcolumncreate", POINTER(win32more.Storage.Jet.JET_COLUMNCREATE_A_head)),
        ("cColumns", UInt32),
        ("rgindexcreate", POINTER(win32more.Storage.Jet.JET_INDEXCREATE2_A_head)),
        ("cIndexes", UInt32),
        ("szCallback", win32more.Foundation.PSTR),
        ("cbtyp", UInt32),
        ("grbit", UInt32),
        ("pSeqSpacehints", POINTER(win32more.Storage.Jet.JET_SPACEHINTS_head)),
        ("pLVSpacehints", POINTER(win32more.Storage.Jet.JET_SPACEHINTS_head)),
        ("cbSeparateLV", UInt32),
        ("tableid", win32more.Storage.StructuredStorage.JET_TABLEID),
        ("cCreated", UInt32),
    ]
    return JET_TABLECREATE3_A
def _define_JET_TABLECREATE3_W_head():
    class JET_TABLECREATE3_W(Structure):
        pass
    return JET_TABLECREATE3_W
def _define_JET_TABLECREATE3_W():
    JET_TABLECREATE3_W = win32more.Storage.Jet.JET_TABLECREATE3_W_head
    JET_TABLECREATE3_W._fields_ = [
        ("cbStruct", UInt32),
        ("szTableName", win32more.Foundation.PWSTR),
        ("szTemplateTableName", win32more.Foundation.PWSTR),
        ("ulPages", UInt32),
        ("ulDensity", UInt32),
        ("rgcolumncreate", POINTER(win32more.Storage.Jet.JET_COLUMNCREATE_W_head)),
        ("cColumns", UInt32),
        ("rgindexcreate", POINTER(win32more.Storage.Jet.JET_INDEXCREATE2_W_head)),
        ("cIndexes", UInt32),
        ("szCallback", win32more.Foundation.PWSTR),
        ("cbtyp", UInt32),
        ("grbit", UInt32),
        ("pSeqSpacehints", POINTER(win32more.Storage.Jet.JET_SPACEHINTS_head)),
        ("pLVSpacehints", POINTER(win32more.Storage.Jet.JET_SPACEHINTS_head)),
        ("cbSeparateLV", UInt32),
        ("tableid", win32more.Storage.StructuredStorage.JET_TABLEID),
        ("cCreated", UInt32),
    ]
    return JET_TABLECREATE3_W
def _define_JET_TABLECREATE4_A_head():
    class JET_TABLECREATE4_A(Structure):
        pass
    return JET_TABLECREATE4_A
def _define_JET_TABLECREATE4_A():
    JET_TABLECREATE4_A = win32more.Storage.Jet.JET_TABLECREATE4_A_head
    JET_TABLECREATE4_A._fields_ = [
        ("cbStruct", UInt32),
        ("szTableName", win32more.Foundation.PSTR),
        ("szTemplateTableName", win32more.Foundation.PSTR),
        ("ulPages", UInt32),
        ("ulDensity", UInt32),
        ("rgcolumncreate", POINTER(win32more.Storage.Jet.JET_COLUMNCREATE_A_head)),
        ("cColumns", UInt32),
        ("rgindexcreate", POINTER(win32more.Storage.Jet.JET_INDEXCREATE3_A_head)),
        ("cIndexes", UInt32),
        ("szCallback", win32more.Foundation.PSTR),
        ("cbtyp", UInt32),
        ("grbit", UInt32),
        ("pSeqSpacehints", POINTER(win32more.Storage.Jet.JET_SPACEHINTS_head)),
        ("pLVSpacehints", POINTER(win32more.Storage.Jet.JET_SPACEHINTS_head)),
        ("cbSeparateLV", UInt32),
        ("tableid", win32more.Storage.StructuredStorage.JET_TABLEID),
        ("cCreated", UInt32),
    ]
    return JET_TABLECREATE4_A
def _define_JET_TABLECREATE4_W_head():
    class JET_TABLECREATE4_W(Structure):
        pass
    return JET_TABLECREATE4_W
def _define_JET_TABLECREATE4_W():
    JET_TABLECREATE4_W = win32more.Storage.Jet.JET_TABLECREATE4_W_head
    JET_TABLECREATE4_W._fields_ = [
        ("cbStruct", UInt32),
        ("szTableName", win32more.Foundation.PWSTR),
        ("szTemplateTableName", win32more.Foundation.PWSTR),
        ("ulPages", UInt32),
        ("ulDensity", UInt32),
        ("rgcolumncreate", POINTER(win32more.Storage.Jet.JET_COLUMNCREATE_W_head)),
        ("cColumns", UInt32),
        ("rgindexcreate", POINTER(win32more.Storage.Jet.JET_INDEXCREATE3_W_head)),
        ("cIndexes", UInt32),
        ("szCallback", win32more.Foundation.PWSTR),
        ("cbtyp", UInt32),
        ("grbit", UInt32),
        ("pSeqSpacehints", POINTER(win32more.Storage.Jet.JET_SPACEHINTS_head)),
        ("pLVSpacehints", POINTER(win32more.Storage.Jet.JET_SPACEHINTS_head)),
        ("cbSeparateLV", UInt32),
        ("tableid", win32more.Storage.StructuredStorage.JET_TABLEID),
        ("cCreated", UInt32),
    ]
    return JET_TABLECREATE4_W
def _define_JET_OPENTEMPORARYTABLE_head():
    class JET_OPENTEMPORARYTABLE(Structure):
        pass
    return JET_OPENTEMPORARYTABLE
def _define_JET_OPENTEMPORARYTABLE():
    JET_OPENTEMPORARYTABLE = win32more.Storage.Jet.JET_OPENTEMPORARYTABLE_head
    JET_OPENTEMPORARYTABLE._fields_ = [
        ("cbStruct", UInt32),
        ("prgcolumndef", POINTER(win32more.Storage.Jet.JET_COLUMNDEF_head)),
        ("ccolumn", UInt32),
        ("pidxunicode", POINTER(win32more.Storage.Jet.JET_UNICODEINDEX_head)),
        ("grbit", UInt32),
        ("prgcolumnid", POINTER(UInt32)),
        ("cbKeyMost", UInt32),
        ("cbVarSegMac", UInt32),
        ("tableid", win32more.Storage.StructuredStorage.JET_TABLEID),
    ]
    return JET_OPENTEMPORARYTABLE
def _define_JET_OPENTEMPORARYTABLE2_head():
    class JET_OPENTEMPORARYTABLE2(Structure):
        pass
    return JET_OPENTEMPORARYTABLE2
def _define_JET_OPENTEMPORARYTABLE2():
    JET_OPENTEMPORARYTABLE2 = win32more.Storage.Jet.JET_OPENTEMPORARYTABLE2_head
    JET_OPENTEMPORARYTABLE2._fields_ = [
        ("cbStruct", UInt32),
        ("prgcolumndef", POINTER(win32more.Storage.Jet.JET_COLUMNDEF_head)),
        ("ccolumn", UInt32),
        ("pidxunicode", POINTER(win32more.Storage.Jet.JET_UNICODEINDEX2_head)),
        ("grbit", UInt32),
        ("prgcolumnid", POINTER(UInt32)),
        ("cbKeyMost", UInt32),
        ("cbVarSegMac", UInt32),
        ("tableid", win32more.Storage.StructuredStorage.JET_TABLEID),
    ]
    return JET_OPENTEMPORARYTABLE2
def _define_JET_RETINFO_head():
    class JET_RETINFO(Structure):
        pass
    return JET_RETINFO
def _define_JET_RETINFO():
    JET_RETINFO = win32more.Storage.Jet.JET_RETINFO_head
    JET_RETINFO._fields_ = [
        ("cbStruct", UInt32),
        ("ibLongValue", UInt32),
        ("itagSequence", UInt32),
        ("columnidNextTagged", UInt32),
    ]
    return JET_RETINFO
def _define_JET_SETINFO_head():
    class JET_SETINFO(Structure):
        pass
    return JET_SETINFO
def _define_JET_SETINFO():
    JET_SETINFO = win32more.Storage.Jet.JET_SETINFO_head
    JET_SETINFO._fields_ = [
        ("cbStruct", UInt32),
        ("ibLongValue", UInt32),
        ("itagSequence", UInt32),
    ]
    return JET_SETINFO
def _define_JET_RECPOS_head():
    class JET_RECPOS(Structure):
        pass
    return JET_RECPOS
def _define_JET_RECPOS():
    JET_RECPOS = win32more.Storage.Jet.JET_RECPOS_head
    JET_RECPOS._fields_ = [
        ("cbStruct", UInt32),
        ("centriesLT", UInt32),
        ("centriesInRange", UInt32),
        ("centriesTotal", UInt32),
    ]
    return JET_RECPOS
def _define_JET_RECORDLIST_head():
    class JET_RECORDLIST(Structure):
        pass
    return JET_RECORDLIST
def _define_JET_RECORDLIST():
    JET_RECORDLIST = win32more.Storage.Jet.JET_RECORDLIST_head
    JET_RECORDLIST._fields_ = [
        ("cbStruct", UInt32),
        ("tableid", win32more.Storage.StructuredStorage.JET_TABLEID),
        ("cRecord", UInt32),
        ("columnidBookmark", UInt32),
    ]
    return JET_RECORDLIST
def _define_JET_INDEXRANGE_head():
    class JET_INDEXRANGE(Structure):
        pass
    return JET_INDEXRANGE
def _define_JET_INDEXRANGE():
    JET_INDEXRANGE = win32more.Storage.Jet.JET_INDEXRANGE_head
    JET_INDEXRANGE._fields_ = [
        ("cbStruct", UInt32),
        ("tableid", win32more.Storage.StructuredStorage.JET_TABLEID),
        ("grbit", UInt32),
    ]
    return JET_INDEXRANGE
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
def _define_JET_INDEX_COLUMN_head():
    class JET_INDEX_COLUMN(Structure):
        pass
    return JET_INDEX_COLUMN
def _define_JET_INDEX_COLUMN():
    JET_INDEX_COLUMN = win32more.Storage.Jet.JET_INDEX_COLUMN_head
    JET_INDEX_COLUMN._fields_ = [
        ("columnid", UInt32),
        ("relop", win32more.Storage.Jet.JET_RELOP),
        ("pv", c_void_p),
        ("cb", UInt32),
        ("grbit", UInt32),
    ]
    return JET_INDEX_COLUMN
def _define_JET_INDEX_RANGE_head():
    class JET_INDEX_RANGE(Structure):
        pass
    return JET_INDEX_RANGE
def _define_JET_INDEX_RANGE():
    JET_INDEX_RANGE = win32more.Storage.Jet.JET_INDEX_RANGE_head
    JET_INDEX_RANGE._fields_ = [
        ("rgStartColumns", POINTER(win32more.Storage.Jet.JET_INDEX_COLUMN_head)),
        ("cStartColumns", UInt32),
        ("rgEndColumns", POINTER(win32more.Storage.Jet.JET_INDEX_COLUMN_head)),
        ("cEndColumns", UInt32),
    ]
    return JET_INDEX_RANGE
def _define_JET_LOGTIME_head():
    class JET_LOGTIME(Structure):
        pass
    return JET_LOGTIME
def _define_JET_LOGTIME():
    JET_LOGTIME = win32more.Storage.Jet.JET_LOGTIME_head
    class JET_LOGTIME__Anonymous2_e__Union(Union):
        pass
    class JET_LOGTIME__Anonymous2_e__Union__Anonymous_e__Struct(Structure):
        pass
    JET_LOGTIME__Anonymous2_e__Union__Anonymous_e__Struct._fields_ = [
        ("_bitfield", Byte),
    ]
    JET_LOGTIME__Anonymous2_e__Union._anonymous_ = [
        'Anonymous',
    ]
    JET_LOGTIME__Anonymous2_e__Union._fields_ = [
        ("bFiller2", win32more.Foundation.CHAR),
        ("Anonymous", JET_LOGTIME__Anonymous2_e__Union__Anonymous_e__Struct),
    ]
    class JET_LOGTIME__Anonymous1_e__Union(Union):
        pass
    class JET_LOGTIME__Anonymous1_e__Union__Anonymous_e__Struct(Structure):
        pass
    JET_LOGTIME__Anonymous1_e__Union__Anonymous_e__Struct._fields_ = [
        ("_bitfield", Byte),
    ]
    JET_LOGTIME__Anonymous1_e__Union._anonymous_ = [
        'Anonymous',
    ]
    JET_LOGTIME__Anonymous1_e__Union._fields_ = [
        ("bFiller1", win32more.Foundation.CHAR),
        ("Anonymous", JET_LOGTIME__Anonymous1_e__Union__Anonymous_e__Struct),
    ]
    JET_LOGTIME._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    JET_LOGTIME._fields_ = [
        ("bSeconds", win32more.Foundation.CHAR),
        ("bMinutes", win32more.Foundation.CHAR),
        ("bHours", win32more.Foundation.CHAR),
        ("bDay", win32more.Foundation.CHAR),
        ("bMonth", win32more.Foundation.CHAR),
        ("bYear", win32more.Foundation.CHAR),
        ("Anonymous1", JET_LOGTIME__Anonymous1_e__Union),
        ("Anonymous2", JET_LOGTIME__Anonymous2_e__Union),
    ]
    return JET_LOGTIME
def _define_JET_BKLOGTIME_head():
    class JET_BKLOGTIME(Structure):
        pass
    return JET_BKLOGTIME
def _define_JET_BKLOGTIME():
    JET_BKLOGTIME = win32more.Storage.Jet.JET_BKLOGTIME_head
    class JET_BKLOGTIME__Anonymous2_e__Union(Union):
        pass
    class JET_BKLOGTIME__Anonymous2_e__Union__Anonymous_e__Struct(Structure):
        pass
    JET_BKLOGTIME__Anonymous2_e__Union__Anonymous_e__Struct._fields_ = [
        ("_bitfield", Byte),
    ]
    JET_BKLOGTIME__Anonymous2_e__Union._anonymous_ = [
        'Anonymous',
    ]
    JET_BKLOGTIME__Anonymous2_e__Union._fields_ = [
        ("bFiller2", win32more.Foundation.CHAR),
        ("Anonymous", JET_BKLOGTIME__Anonymous2_e__Union__Anonymous_e__Struct),
    ]
    class JET_BKLOGTIME__Anonymous1_e__Union(Union):
        pass
    class JET_BKLOGTIME__Anonymous1_e__Union__Anonymous_e__Struct(Structure):
        pass
    JET_BKLOGTIME__Anonymous1_e__Union__Anonymous_e__Struct._fields_ = [
        ("_bitfield", Byte),
    ]
    JET_BKLOGTIME__Anonymous1_e__Union._anonymous_ = [
        'Anonymous',
    ]
    JET_BKLOGTIME__Anonymous1_e__Union._fields_ = [
        ("bFiller1", win32more.Foundation.CHAR),
        ("Anonymous", JET_BKLOGTIME__Anonymous1_e__Union__Anonymous_e__Struct),
    ]
    JET_BKLOGTIME._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    JET_BKLOGTIME._fields_ = [
        ("bSeconds", win32more.Foundation.CHAR),
        ("bMinutes", win32more.Foundation.CHAR),
        ("bHours", win32more.Foundation.CHAR),
        ("bDay", win32more.Foundation.CHAR),
        ("bMonth", win32more.Foundation.CHAR),
        ("bYear", win32more.Foundation.CHAR),
        ("Anonymous1", JET_BKLOGTIME__Anonymous1_e__Union),
        ("Anonymous2", JET_BKLOGTIME__Anonymous2_e__Union),
    ]
    return JET_BKLOGTIME
def _define_JET_LGPOS_head():
    class JET_LGPOS(Structure):
        pass
    return JET_LGPOS
def _define_JET_LGPOS():
    JET_LGPOS = win32more.Storage.Jet.JET_LGPOS_head
    JET_LGPOS._pack_ = 1
    JET_LGPOS._fields_ = [
        ("ib", UInt16),
        ("isec", UInt16),
        ("lGeneration", Int32),
    ]
    return JET_LGPOS
def _define_JET_SIGNATURE_head():
    class JET_SIGNATURE(Structure):
        pass
    return JET_SIGNATURE
def _define_JET_SIGNATURE():
    JET_SIGNATURE = win32more.Storage.Jet.JET_SIGNATURE_head
    JET_SIGNATURE._pack_ = 1
    JET_SIGNATURE._fields_ = [
        ("ulRandom", UInt32),
        ("logtimeCreate", win32more.Storage.Jet.JET_LOGTIME),
        ("szComputerName", win32more.Foundation.CHAR * 16),
    ]
    return JET_SIGNATURE
def _define_JET_BKINFO_head():
    class JET_BKINFO(Structure):
        pass
    return JET_BKINFO
def _define_JET_BKINFO():
    JET_BKINFO = win32more.Storage.Jet.JET_BKINFO_head
    class JET_BKINFO__Anonymous_e__Union(Union):
        pass
    JET_BKINFO__Anonymous_e__Union._fields_ = [
        ("logtimeMark", win32more.Storage.Jet.JET_LOGTIME),
        ("bklogtimeMark", win32more.Storage.Jet.JET_BKLOGTIME),
    ]
    JET_BKINFO._pack_ = 1
    JET_BKINFO._anonymous_ = [
        'Anonymous',
    ]
    JET_BKINFO._fields_ = [
        ("lgposMark", win32more.Storage.Jet.JET_LGPOS),
        ("Anonymous", JET_BKINFO__Anonymous_e__Union),
        ("genLow", UInt32),
        ("genHigh", UInt32),
    ]
    return JET_BKINFO
def _define_JET_DBINFOMISC_head():
    class JET_DBINFOMISC(Structure):
        pass
    return JET_DBINFOMISC
def _define_JET_DBINFOMISC():
    JET_DBINFOMISC = win32more.Storage.Jet.JET_DBINFOMISC_head
    JET_DBINFOMISC._fields_ = [
        ("ulVersion", UInt32),
        ("ulUpdate", UInt32),
        ("signDb", win32more.Storage.Jet.JET_SIGNATURE),
        ("dbstate", UInt32),
        ("lgposConsistent", win32more.Storage.Jet.JET_LGPOS),
        ("logtimeConsistent", win32more.Storage.Jet.JET_LOGTIME),
        ("logtimeAttach", win32more.Storage.Jet.JET_LOGTIME),
        ("lgposAttach", win32more.Storage.Jet.JET_LGPOS),
        ("logtimeDetach", win32more.Storage.Jet.JET_LOGTIME),
        ("lgposDetach", win32more.Storage.Jet.JET_LGPOS),
        ("signLog", win32more.Storage.Jet.JET_SIGNATURE),
        ("bkinfoFullPrev", win32more.Storage.Jet.JET_BKINFO),
        ("bkinfoIncPrev", win32more.Storage.Jet.JET_BKINFO),
        ("bkinfoFullCur", win32more.Storage.Jet.JET_BKINFO),
        ("fShadowingDisabled", UInt32),
        ("fUpgradeDb", UInt32),
        ("dwMajorVersion", UInt32),
        ("dwMinorVersion", UInt32),
        ("dwBuildNumber", UInt32),
        ("lSPNumber", Int32),
        ("cbPageSize", UInt32),
    ]
    return JET_DBINFOMISC
def _define_JET_DBINFOMISC2_head():
    class JET_DBINFOMISC2(Structure):
        pass
    return JET_DBINFOMISC2
def _define_JET_DBINFOMISC2():
    JET_DBINFOMISC2 = win32more.Storage.Jet.JET_DBINFOMISC2_head
    JET_DBINFOMISC2._fields_ = [
        ("ulVersion", UInt32),
        ("ulUpdate", UInt32),
        ("signDb", win32more.Storage.Jet.JET_SIGNATURE),
        ("dbstate", UInt32),
        ("lgposConsistent", win32more.Storage.Jet.JET_LGPOS),
        ("logtimeConsistent", win32more.Storage.Jet.JET_LOGTIME),
        ("logtimeAttach", win32more.Storage.Jet.JET_LOGTIME),
        ("lgposAttach", win32more.Storage.Jet.JET_LGPOS),
        ("logtimeDetach", win32more.Storage.Jet.JET_LOGTIME),
        ("lgposDetach", win32more.Storage.Jet.JET_LGPOS),
        ("signLog", win32more.Storage.Jet.JET_SIGNATURE),
        ("bkinfoFullPrev", win32more.Storage.Jet.JET_BKINFO),
        ("bkinfoIncPrev", win32more.Storage.Jet.JET_BKINFO),
        ("bkinfoFullCur", win32more.Storage.Jet.JET_BKINFO),
        ("fShadowingDisabled", UInt32),
        ("fUpgradeDb", UInt32),
        ("dwMajorVersion", UInt32),
        ("dwMinorVersion", UInt32),
        ("dwBuildNumber", UInt32),
        ("lSPNumber", Int32),
        ("cbPageSize", UInt32),
        ("genMinRequired", UInt32),
        ("genMaxRequired", UInt32),
        ("logtimeGenMaxCreate", win32more.Storage.Jet.JET_LOGTIME),
        ("ulRepairCount", UInt32),
        ("logtimeRepair", win32more.Storage.Jet.JET_LOGTIME),
        ("ulRepairCountOld", UInt32),
        ("ulECCFixSuccess", UInt32),
        ("logtimeECCFixSuccess", win32more.Storage.Jet.JET_LOGTIME),
        ("ulECCFixSuccessOld", UInt32),
        ("ulECCFixFail", UInt32),
        ("logtimeECCFixFail", win32more.Storage.Jet.JET_LOGTIME),
        ("ulECCFixFailOld", UInt32),
        ("ulBadChecksum", UInt32),
        ("logtimeBadChecksum", win32more.Storage.Jet.JET_LOGTIME),
        ("ulBadChecksumOld", UInt32),
    ]
    return JET_DBINFOMISC2
def _define_JET_DBINFOMISC3_head():
    class JET_DBINFOMISC3(Structure):
        pass
    return JET_DBINFOMISC3
def _define_JET_DBINFOMISC3():
    JET_DBINFOMISC3 = win32more.Storage.Jet.JET_DBINFOMISC3_head
    JET_DBINFOMISC3._fields_ = [
        ("ulVersion", UInt32),
        ("ulUpdate", UInt32),
        ("signDb", win32more.Storage.Jet.JET_SIGNATURE),
        ("dbstate", UInt32),
        ("lgposConsistent", win32more.Storage.Jet.JET_LGPOS),
        ("logtimeConsistent", win32more.Storage.Jet.JET_LOGTIME),
        ("logtimeAttach", win32more.Storage.Jet.JET_LOGTIME),
        ("lgposAttach", win32more.Storage.Jet.JET_LGPOS),
        ("logtimeDetach", win32more.Storage.Jet.JET_LOGTIME),
        ("lgposDetach", win32more.Storage.Jet.JET_LGPOS),
        ("signLog", win32more.Storage.Jet.JET_SIGNATURE),
        ("bkinfoFullPrev", win32more.Storage.Jet.JET_BKINFO),
        ("bkinfoIncPrev", win32more.Storage.Jet.JET_BKINFO),
        ("bkinfoFullCur", win32more.Storage.Jet.JET_BKINFO),
        ("fShadowingDisabled", UInt32),
        ("fUpgradeDb", UInt32),
        ("dwMajorVersion", UInt32),
        ("dwMinorVersion", UInt32),
        ("dwBuildNumber", UInt32),
        ("lSPNumber", Int32),
        ("cbPageSize", UInt32),
        ("genMinRequired", UInt32),
        ("genMaxRequired", UInt32),
        ("logtimeGenMaxCreate", win32more.Storage.Jet.JET_LOGTIME),
        ("ulRepairCount", UInt32),
        ("logtimeRepair", win32more.Storage.Jet.JET_LOGTIME),
        ("ulRepairCountOld", UInt32),
        ("ulECCFixSuccess", UInt32),
        ("logtimeECCFixSuccess", win32more.Storage.Jet.JET_LOGTIME),
        ("ulECCFixSuccessOld", UInt32),
        ("ulECCFixFail", UInt32),
        ("logtimeECCFixFail", win32more.Storage.Jet.JET_LOGTIME),
        ("ulECCFixFailOld", UInt32),
        ("ulBadChecksum", UInt32),
        ("logtimeBadChecksum", win32more.Storage.Jet.JET_LOGTIME),
        ("ulBadChecksumOld", UInt32),
        ("genCommitted", UInt32),
    ]
    return JET_DBINFOMISC3
def _define_JET_DBINFOMISC4_head():
    class JET_DBINFOMISC4(Structure):
        pass
    return JET_DBINFOMISC4
def _define_JET_DBINFOMISC4():
    JET_DBINFOMISC4 = win32more.Storage.Jet.JET_DBINFOMISC4_head
    JET_DBINFOMISC4._fields_ = [
        ("ulVersion", UInt32),
        ("ulUpdate", UInt32),
        ("signDb", win32more.Storage.Jet.JET_SIGNATURE),
        ("dbstate", UInt32),
        ("lgposConsistent", win32more.Storage.Jet.JET_LGPOS),
        ("logtimeConsistent", win32more.Storage.Jet.JET_LOGTIME),
        ("logtimeAttach", win32more.Storage.Jet.JET_LOGTIME),
        ("lgposAttach", win32more.Storage.Jet.JET_LGPOS),
        ("logtimeDetach", win32more.Storage.Jet.JET_LOGTIME),
        ("lgposDetach", win32more.Storage.Jet.JET_LGPOS),
        ("signLog", win32more.Storage.Jet.JET_SIGNATURE),
        ("bkinfoFullPrev", win32more.Storage.Jet.JET_BKINFO),
        ("bkinfoIncPrev", win32more.Storage.Jet.JET_BKINFO),
        ("bkinfoFullCur", win32more.Storage.Jet.JET_BKINFO),
        ("fShadowingDisabled", UInt32),
        ("fUpgradeDb", UInt32),
        ("dwMajorVersion", UInt32),
        ("dwMinorVersion", UInt32),
        ("dwBuildNumber", UInt32),
        ("lSPNumber", Int32),
        ("cbPageSize", UInt32),
        ("genMinRequired", UInt32),
        ("genMaxRequired", UInt32),
        ("logtimeGenMaxCreate", win32more.Storage.Jet.JET_LOGTIME),
        ("ulRepairCount", UInt32),
        ("logtimeRepair", win32more.Storage.Jet.JET_LOGTIME),
        ("ulRepairCountOld", UInt32),
        ("ulECCFixSuccess", UInt32),
        ("logtimeECCFixSuccess", win32more.Storage.Jet.JET_LOGTIME),
        ("ulECCFixSuccessOld", UInt32),
        ("ulECCFixFail", UInt32),
        ("logtimeECCFixFail", win32more.Storage.Jet.JET_LOGTIME),
        ("ulECCFixFailOld", UInt32),
        ("ulBadChecksum", UInt32),
        ("logtimeBadChecksum", win32more.Storage.Jet.JET_LOGTIME),
        ("ulBadChecksumOld", UInt32),
        ("genCommitted", UInt32),
        ("bkinfoCopyPrev", win32more.Storage.Jet.JET_BKINFO),
        ("bkinfoDiffPrev", win32more.Storage.Jet.JET_BKINFO),
    ]
    return JET_DBINFOMISC4
def _define_JET_THREADSTATS_head():
    class JET_THREADSTATS(Structure):
        pass
    return JET_THREADSTATS
def _define_JET_THREADSTATS():
    JET_THREADSTATS = win32more.Storage.Jet.JET_THREADSTATS_head
    JET_THREADSTATS._fields_ = [
        ("cbStruct", UInt32),
        ("cPageReferenced", UInt32),
        ("cPageRead", UInt32),
        ("cPagePreread", UInt32),
        ("cPageDirtied", UInt32),
        ("cPageRedirtied", UInt32),
        ("cLogRecord", UInt32),
        ("cbLogRecord", UInt32),
    ]
    return JET_THREADSTATS
def _define_JET_THREADSTATS2_head():
    class JET_THREADSTATS2(Structure):
        pass
    return JET_THREADSTATS2
def _define_JET_THREADSTATS2():
    JET_THREADSTATS2 = win32more.Storage.Jet.JET_THREADSTATS2_head
    JET_THREADSTATS2._fields_ = [
        ("cbStruct", UInt32),
        ("cPageReferenced", UInt32),
        ("cPageRead", UInt32),
        ("cPagePreread", UInt32),
        ("cPageDirtied", UInt32),
        ("cPageRedirtied", UInt32),
        ("cLogRecord", UInt32),
        ("cbLogRecord", UInt32),
        ("cusecPageCacheMiss", UInt64),
        ("cPageCacheMiss", UInt32),
    ]
    return JET_THREADSTATS2
def _define_JET_RSTINFO_A_head():
    class JET_RSTINFO_A(Structure):
        pass
    return JET_RSTINFO_A
def _define_JET_RSTINFO_A():
    JET_RSTINFO_A = win32more.Storage.Jet.JET_RSTINFO_A_head
    JET_RSTINFO_A._fields_ = [
        ("cbStruct", UInt32),
        ("rgrstmap", POINTER(win32more.Storage.Jet.JET_RSTMAP_A_head)),
        ("crstmap", Int32),
        ("lgposStop", win32more.Storage.Jet.JET_LGPOS),
        ("logtimeStop", win32more.Storage.Jet.JET_LOGTIME),
        ("pfnStatus", win32more.Storage.Jet.JET_PFNSTATUS),
    ]
    return JET_RSTINFO_A
def _define_JET_RSTINFO_W_head():
    class JET_RSTINFO_W(Structure):
        pass
    return JET_RSTINFO_W
def _define_JET_RSTINFO_W():
    JET_RSTINFO_W = win32more.Storage.Jet.JET_RSTINFO_W_head
    JET_RSTINFO_W._fields_ = [
        ("cbStruct", UInt32),
        ("rgrstmap", POINTER(win32more.Storage.Jet.JET_RSTMAP_W_head)),
        ("crstmap", Int32),
        ("lgposStop", win32more.Storage.Jet.JET_LGPOS),
        ("logtimeStop", win32more.Storage.Jet.JET_LOGTIME),
        ("pfnStatus", win32more.Storage.Jet.JET_PFNSTATUS),
    ]
    return JET_RSTINFO_W
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
        ("cbStruct", UInt32),
        ("errValue", Int32),
        ("errcatMostSpecific", win32more.Storage.Jet.JET_ERRCAT),
        ("rgCategoricalHierarchy", Byte * 8),
        ("lSourceLine", UInt32),
        ("rgszSourceFile", Char * 64),
    ]
    return JET_ERRINFOBASIC_W
def _define_JET_COMMIT_ID_head():
    class JET_COMMIT_ID(Structure):
        pass
    return JET_COMMIT_ID
def _define_JET_COMMIT_ID():
    JET_COMMIT_ID = win32more.Storage.Jet.JET_COMMIT_ID_head
    JET_COMMIT_ID._fields_ = [
        ("signLog", win32more.Storage.Jet.JET_SIGNATURE),
        ("reserved", Int32),
        ("commitId", Int64),
    ]
    return JET_COMMIT_ID
def _define_JET_PFNDURABLECOMMITCALLBACK():
    return CFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,POINTER(win32more.Storage.Jet.JET_COMMIT_ID_head),UInt32, use_last_error=False)
def _define_JET_RBSINFOMISC_head():
    class JET_RBSINFOMISC(Structure):
        pass
    return JET_RBSINFOMISC
def _define_JET_RBSINFOMISC():
    JET_RBSINFOMISC = win32more.Storage.Jet.JET_RBSINFOMISC_head
    JET_RBSINFOMISC._fields_ = [
        ("lRBSGeneration", Int32),
        ("logtimeCreate", win32more.Storage.Jet.JET_LOGTIME),
        ("logtimeCreatePrevRBS", win32more.Storage.Jet.JET_LOGTIME),
        ("ulMajor", UInt32),
        ("ulMinor", UInt32),
        ("cbLogicalFileSize", UInt64),
    ]
    return JET_RBSINFOMISC
def _define_JET_RBSREVERTINFOMISC_head():
    class JET_RBSREVERTINFOMISC(Structure):
        pass
    return JET_RBSREVERTINFOMISC
def _define_JET_RBSREVERTINFOMISC():
    JET_RBSREVERTINFOMISC = win32more.Storage.Jet.JET_RBSREVERTINFOMISC_head
    JET_RBSREVERTINFOMISC._fields_ = [
        ("lGenMinRevertStart", Int32),
        ("lGenMaxRevertStart", Int32),
        ("lGenMinRevertEnd", Int32),
        ("lGenMaxRevertEnd", Int32),
        ("logtimeRevertFrom", win32more.Storage.Jet.JET_LOGTIME),
        ("cSecRevert", UInt64),
        ("cPagesReverted", UInt64),
    ]
    return JET_RBSREVERTINFOMISC
JET_INDEXCHECKING = Int32
JET_IndexCheckingOff = 0
JET_IndexCheckingOn = 1
JET_IndexCheckingDeferToOpenTable = 2
JET_IndexCheckingMax = 3
def _define_JET_OPERATIONCONTEXT_head():
    class JET_OPERATIONCONTEXT(Structure):
        pass
    return JET_OPERATIONCONTEXT
def _define_JET_OPERATIONCONTEXT():
    JET_OPERATIONCONTEXT = win32more.Storage.Jet.JET_OPERATIONCONTEXT_head
    JET_OPERATIONCONTEXT._fields_ = [
        ("ulUserID", UInt32),
        ("nOperationID", Byte),
        ("nOperationType", Byte),
        ("nClientType", Byte),
        ("fFlags", Byte),
    ]
    return JET_OPERATIONCONTEXT
def _define_JET_SETCOLUMN_head():
    class JET_SETCOLUMN(Structure):
        pass
    return JET_SETCOLUMN
def _define_JET_SETCOLUMN():
    JET_SETCOLUMN = win32more.Storage.Jet.JET_SETCOLUMN_head
    JET_SETCOLUMN._fields_ = [
        ("columnid", UInt32),
        ("pvData", c_void_p),
        ("cbData", UInt32),
        ("grbit", UInt32),
        ("ibLongValue", UInt32),
        ("itagSequence", UInt32),
        ("err", Int32),
    ]
    return JET_SETCOLUMN
def _define_JET_SETSYSPARAM_A_head():
    class JET_SETSYSPARAM_A(Structure):
        pass
    return JET_SETSYSPARAM_A
def _define_JET_SETSYSPARAM_A():
    JET_SETSYSPARAM_A = win32more.Storage.Jet.JET_SETSYSPARAM_A_head
    JET_SETSYSPARAM_A._fields_ = [
        ("paramid", UInt32),
        ("lParam", win32more.Storage.StructuredStorage.JET_API_PTR),
        ("sz", win32more.Foundation.PSTR),
        ("err", Int32),
    ]
    return JET_SETSYSPARAM_A
def _define_JET_SETSYSPARAM_W_head():
    class JET_SETSYSPARAM_W(Structure):
        pass
    return JET_SETSYSPARAM_W
def _define_JET_SETSYSPARAM_W():
    JET_SETSYSPARAM_W = win32more.Storage.Jet.JET_SETSYSPARAM_W_head
    JET_SETSYSPARAM_W._fields_ = [
        ("paramid", UInt32),
        ("lParam", win32more.Storage.StructuredStorage.JET_API_PTR),
        ("sz", win32more.Foundation.PWSTR),
        ("err", Int32),
    ]
    return JET_SETSYSPARAM_W
def _define_JET_RETRIEVECOLUMN_head():
    class JET_RETRIEVECOLUMN(Structure):
        pass
    return JET_RETRIEVECOLUMN
def _define_JET_RETRIEVECOLUMN():
    JET_RETRIEVECOLUMN = win32more.Storage.Jet.JET_RETRIEVECOLUMN_head
    JET_RETRIEVECOLUMN._fields_ = [
        ("columnid", UInt32),
        ("pvData", c_void_p),
        ("cbData", UInt32),
        ("cbActual", UInt32),
        ("grbit", UInt32),
        ("ibLongValue", UInt32),
        ("itagSequence", UInt32),
        ("columnidNextTagged", UInt32),
        ("err", Int32),
    ]
    return JET_RETRIEVECOLUMN
def _define_JET_ENUMCOLUMNID_head():
    class JET_ENUMCOLUMNID(Structure):
        pass
    return JET_ENUMCOLUMNID
def _define_JET_ENUMCOLUMNID():
    JET_ENUMCOLUMNID = win32more.Storage.Jet.JET_ENUMCOLUMNID_head
    JET_ENUMCOLUMNID._fields_ = [
        ("columnid", UInt32),
        ("ctagSequence", UInt32),
        ("rgtagSequence", POINTER(UInt32)),
    ]
    return JET_ENUMCOLUMNID
def _define_JET_ENUMCOLUMNVALUE_head():
    class JET_ENUMCOLUMNVALUE(Structure):
        pass
    return JET_ENUMCOLUMNVALUE
def _define_JET_ENUMCOLUMNVALUE():
    JET_ENUMCOLUMNVALUE = win32more.Storage.Jet.JET_ENUMCOLUMNVALUE_head
    JET_ENUMCOLUMNVALUE._fields_ = [
        ("itagSequence", UInt32),
        ("err", Int32),
        ("cbData", UInt32),
        ("pvData", c_void_p),
    ]
    return JET_ENUMCOLUMNVALUE
def _define_JET_ENUMCOLUMN_head():
    class JET_ENUMCOLUMN(Structure):
        pass
    return JET_ENUMCOLUMN
def _define_JET_ENUMCOLUMN():
    JET_ENUMCOLUMN = win32more.Storage.Jet.JET_ENUMCOLUMN_head
    class JET_ENUMCOLUMN__Anonymous_e__Union(Union):
        pass
    class JET_ENUMCOLUMN__Anonymous_e__Union__Anonymous2_e__Struct(Structure):
        pass
    JET_ENUMCOLUMN__Anonymous_e__Union__Anonymous2_e__Struct._fields_ = [
        ("cbData", UInt32),
        ("pvData", c_void_p),
    ]
    class JET_ENUMCOLUMN__Anonymous_e__Union__Anonymous1_e__Struct(Structure):
        pass
    JET_ENUMCOLUMN__Anonymous_e__Union__Anonymous1_e__Struct._fields_ = [
        ("cEnumColumnValue", UInt32),
        ("rgEnumColumnValue", POINTER(win32more.Storage.Jet.JET_ENUMCOLUMNVALUE_head)),
    ]
    JET_ENUMCOLUMN__Anonymous_e__Union._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    JET_ENUMCOLUMN__Anonymous_e__Union._fields_ = [
        ("Anonymous1", JET_ENUMCOLUMN__Anonymous_e__Union__Anonymous1_e__Struct),
        ("Anonymous2", JET_ENUMCOLUMN__Anonymous_e__Union__Anonymous2_e__Struct),
    ]
    JET_ENUMCOLUMN._anonymous_ = [
        'Anonymous',
    ]
    JET_ENUMCOLUMN._fields_ = [
        ("columnid", UInt32),
        ("err", Int32),
        ("Anonymous", JET_ENUMCOLUMN__Anonymous_e__Union),
    ]
    return JET_ENUMCOLUMN
def _define_JET_PFNREALLOC():
    return CFUNCTYPE(c_void_p,c_void_p,c_void_p,UInt32, use_last_error=False)
def _define_JET_RECSIZE_head():
    class JET_RECSIZE(Structure):
        pass
    return JET_RECSIZE
def _define_JET_RECSIZE():
    JET_RECSIZE = win32more.Storage.Jet.JET_RECSIZE_head
    JET_RECSIZE._fields_ = [
        ("cbData", UInt64),
        ("cbLongValueData", UInt64),
        ("cbOverhead", UInt64),
        ("cbLongValueOverhead", UInt64),
        ("cNonTaggedColumns", UInt64),
        ("cTaggedColumns", UInt64),
        ("cLongValues", UInt64),
        ("cMultiValues", UInt64),
    ]
    return JET_RECSIZE
def _define_JET_RECSIZE2_head():
    class JET_RECSIZE2(Structure):
        pass
    return JET_RECSIZE2
def _define_JET_RECSIZE2():
    JET_RECSIZE2 = win32more.Storage.Jet.JET_RECSIZE2_head
    JET_RECSIZE2._fields_ = [
        ("cbData", UInt64),
        ("cbLongValueData", UInt64),
        ("cbOverhead", UInt64),
        ("cbLongValueOverhead", UInt64),
        ("cNonTaggedColumns", UInt64),
        ("cTaggedColumns", UInt64),
        ("cLongValues", UInt64),
        ("cMultiValues", UInt64),
        ("cCompressedColumns", UInt64),
        ("cbDataCompressed", UInt64),
        ("cbLongValueDataCompressed", UInt64),
    ]
    return JET_RECSIZE2
def _define_JET_LOGINFO_A_head():
    class JET_LOGINFO_A(Structure):
        pass
    return JET_LOGINFO_A
def _define_JET_LOGINFO_A():
    JET_LOGINFO_A = win32more.Storage.Jet.JET_LOGINFO_A_head
    JET_LOGINFO_A._fields_ = [
        ("cbSize", UInt32),
        ("ulGenLow", UInt32),
        ("ulGenHigh", UInt32),
        ("szBaseName", win32more.Foundation.CHAR * 4),
    ]
    return JET_LOGINFO_A
def _define_JET_LOGINFO_W_head():
    class JET_LOGINFO_W(Structure):
        pass
    return JET_LOGINFO_W
def _define_JET_LOGINFO_W():
    JET_LOGINFO_W = win32more.Storage.Jet.JET_LOGINFO_W_head
    JET_LOGINFO_W._fields_ = [
        ("cbSize", UInt32),
        ("ulGenLow", UInt32),
        ("ulGenHigh", UInt32),
        ("szBaseName", Char * 4),
    ]
    return JET_LOGINFO_W
def _define_JET_INSTANCE_INFO_A_head():
    class JET_INSTANCE_INFO_A(Structure):
        pass
    return JET_INSTANCE_INFO_A
def _define_JET_INSTANCE_INFO_A():
    JET_INSTANCE_INFO_A = win32more.Storage.Jet.JET_INSTANCE_INFO_A_head
    JET_INSTANCE_INFO_A._fields_ = [
        ("hInstanceId", win32more.Storage.StructuredStorage.JET_INSTANCE),
        ("szInstanceName", win32more.Foundation.PSTR),
        ("cDatabases", win32more.Storage.StructuredStorage.JET_API_PTR),
        ("szDatabaseFileName", POINTER(POINTER(SByte))),
        ("szDatabaseDisplayName", POINTER(POINTER(SByte))),
        ("szDatabaseSLVFileName_Obsolete", POINTER(POINTER(SByte))),
    ]
    return JET_INSTANCE_INFO_A
def _define_JET_INSTANCE_INFO_W_head():
    class JET_INSTANCE_INFO_W(Structure):
        pass
    return JET_INSTANCE_INFO_W
def _define_JET_INSTANCE_INFO_W():
    JET_INSTANCE_INFO_W = win32more.Storage.Jet.JET_INSTANCE_INFO_W_head
    JET_INSTANCE_INFO_W._fields_ = [
        ("hInstanceId", win32more.Storage.StructuredStorage.JET_INSTANCE),
        ("szInstanceName", win32more.Foundation.PWSTR),
        ("cDatabases", win32more.Storage.StructuredStorage.JET_API_PTR),
        ("szDatabaseFileName", POINTER(POINTER(UInt16))),
        ("szDatabaseDisplayName", POINTER(POINTER(UInt16))),
        ("szDatabaseSLVFileName_Obsolete", POINTER(POINTER(UInt16))),
    ]
    return JET_INSTANCE_INFO_W
def _define_JetInit():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Storage.StructuredStorage.JET_INSTANCE), use_last_error=False)(("JetInit", windll["ESENT"]), ((1, 'pinstance'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetInit2():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Storage.StructuredStorage.JET_INSTANCE),UInt32, use_last_error=False)(("JetInit2", windll["ESENT"]), ((1, 'pinstance'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetInit3A():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Storage.StructuredStorage.JET_INSTANCE),POINTER(win32more.Storage.Jet.JET_RSTINFO_A_head),UInt32, use_last_error=False)(("JetInit3A", windll["ESENT"]), ((1, 'pinstance'),(1, 'prstInfo'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetInit3W():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Storage.StructuredStorage.JET_INSTANCE),POINTER(win32more.Storage.Jet.JET_RSTINFO_W_head),UInt32, use_last_error=False)(("JetInit3W", windll["ESENT"]), ((1, 'pinstance'),(1, 'prstInfo'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetInit3():
    return win32more.Storage.Jet.JetInit3W
def _define_JetCreateInstanceA():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Storage.StructuredStorage.JET_INSTANCE),POINTER(SByte), use_last_error=False)(("JetCreateInstanceA", windll["ESENT"]), ((1, 'pinstance'),(1, 'szInstanceName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateInstanceW():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Storage.StructuredStorage.JET_INSTANCE),POINTER(UInt16), use_last_error=False)(("JetCreateInstanceW", windll["ESENT"]), ((1, 'pinstance'),(1, 'szInstanceName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateInstance():
    return win32more.Storage.Jet.JetCreateInstanceW
def _define_JetCreateInstance2A():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Storage.StructuredStorage.JET_INSTANCE),POINTER(SByte),POINTER(SByte),UInt32, use_last_error=False)(("JetCreateInstance2A", windll["ESENT"]), ((1, 'pinstance'),(1, 'szInstanceName'),(1, 'szDisplayName'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateInstance2W():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Storage.StructuredStorage.JET_INSTANCE),POINTER(UInt16),POINTER(UInt16),UInt32, use_last_error=False)(("JetCreateInstance2W", windll["ESENT"]), ((1, 'pinstance'),(1, 'szInstanceName'),(1, 'szDisplayName'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateInstance2():
    return win32more.Storage.Jet.JetCreateInstance2W
def _define_JetGetInstanceMiscInfo():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,c_void_p,UInt32,UInt32, use_last_error=False)(("JetGetInstanceMiscInfo", windll["ESENT"]), ((1, 'instance'),(1, 'pvResult'),(1, 'cbMax'),(1, 'InfoLevel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetTerm():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE, use_last_error=False)(("JetTerm", windll["ESENT"]), ((1, 'instance'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetTerm2():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,UInt32, use_last_error=False)(("JetTerm2", windll["ESENT"]), ((1, 'instance'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetStopService():
    try:
        return WINFUNCTYPE(Int32, use_last_error=False)(("JetStopService", windll["ESENT"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetStopServiceInstance():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE, use_last_error=False)(("JetStopServiceInstance", windll["ESENT"]), ((1, 'instance'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetStopServiceInstance2():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,UInt32, use_last_error=False)(("JetStopServiceInstance2", windll["ESENT"]), ((1, 'instance'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetStopBackup():
    try:
        return WINFUNCTYPE(Int32, use_last_error=False)(("JetStopBackup", windll["ESENT"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetStopBackupInstance():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE, use_last_error=False)(("JetStopBackupInstance", windll["ESENT"]), ((1, 'instance'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetSetSystemParameterA():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Storage.StructuredStorage.JET_INSTANCE),win32more.Storage.StructuredStorage.JET_SESID,UInt32,win32more.Storage.StructuredStorage.JET_API_PTR,POINTER(SByte), use_last_error=False)(("JetSetSystemParameterA", windll["ESENT"]), ((1, 'pinstance'),(1, 'sesid'),(1, 'paramid'),(1, 'lParam'),(1, 'szParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetSetSystemParameterW():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Storage.StructuredStorage.JET_INSTANCE),win32more.Storage.StructuredStorage.JET_SESID,UInt32,win32more.Storage.StructuredStorage.JET_API_PTR,POINTER(UInt16), use_last_error=False)(("JetSetSystemParameterW", windll["ESENT"]), ((1, 'pinstance'),(1, 'sesid'),(1, 'paramid'),(1, 'lParam'),(1, 'szParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetSetSystemParameter():
    return win32more.Storage.Jet.JetSetSystemParameterW
def _define_JetGetSystemParameterA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(win32more.Storage.StructuredStorage.JET_API_PTR),POINTER(SByte),UInt32, use_last_error=False)(("JetGetSystemParameterA", windll["ESENT"]), ((1, 'instance'),(1, 'sesid'),(1, 'paramid'),(1, 'plParam'),(1, 'szParam'),(1, 'cbMax'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetSystemParameterW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(win32more.Storage.StructuredStorage.JET_API_PTR),POINTER(UInt16),UInt32, use_last_error=False)(("JetGetSystemParameterW", windll["ESENT"]), ((1, 'instance'),(1, 'sesid'),(1, 'paramid'),(1, 'plParam'),(1, 'szParam'),(1, 'cbMax'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetSystemParameter():
    return win32more.Storage.Jet.JetGetSystemParameterW
def _define_JetEnableMultiInstanceA():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Storage.Jet.JET_SETSYSPARAM_A),UInt32,POINTER(UInt32), use_last_error=False)(("JetEnableMultiInstanceA", windll["ESENT"]), ((1, 'psetsysparam'),(1, 'csetsysparam'),(1, 'pcsetsucceed'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetEnableMultiInstanceW():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Storage.Jet.JET_SETSYSPARAM_W),UInt32,POINTER(UInt32), use_last_error=False)(("JetEnableMultiInstanceW", windll["ESENT"]), ((1, 'psetsysparam'),(1, 'csetsysparam'),(1, 'pcsetsucceed'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetEnableMultiInstance():
    return win32more.Storage.Jet.JetEnableMultiInstanceW
def _define_JetGetThreadStats():
    try:
        return WINFUNCTYPE(Int32,c_void_p,UInt32, use_last_error=False)(("JetGetThreadStats", windll["ESENT"]), ((1, 'pvResult'),(1, 'cbMax'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetBeginSessionA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,POINTER(win32more.Storage.StructuredStorage.JET_SESID),POINTER(SByte),POINTER(SByte), use_last_error=False)(("JetBeginSessionA", windll["ESENT"]), ((1, 'instance'),(1, 'psesid'),(1, 'szUserName'),(1, 'szPassword'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetBeginSessionW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,POINTER(win32more.Storage.StructuredStorage.JET_SESID),POINTER(UInt16),POINTER(UInt16), use_last_error=False)(("JetBeginSessionW", windll["ESENT"]), ((1, 'instance'),(1, 'psesid'),(1, 'szUserName'),(1, 'szPassword'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetBeginSession():
    return win32more.Storage.Jet.JetBeginSessionW
def _define_JetDupSession():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(win32more.Storage.StructuredStorage.JET_SESID), use_last_error=False)(("JetDupSession", windll["ESENT"]), ((1, 'sesid'),(1, 'psesid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetEndSession():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32, use_last_error=False)(("JetEndSession", windll["ESENT"]), ((1, 'sesid'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetVersion():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(UInt32), use_last_error=False)(("JetGetVersion", windll["ESENT"]), ((1, 'sesid'),(1, 'pwVersion'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetIdle():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32, use_last_error=False)(("JetIdle", windll["ESENT"]), ((1, 'sesid'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateDatabaseA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(SByte),POINTER(SByte),POINTER(UInt32),UInt32, use_last_error=False)(("JetCreateDatabaseA", windll["ESENT"]), ((1, 'sesid'),(1, 'szFilename'),(1, 'szConnect'),(1, 'pdbid'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateDatabaseW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(UInt16),POINTER(UInt16),POINTER(UInt32),UInt32, use_last_error=False)(("JetCreateDatabaseW", windll["ESENT"]), ((1, 'sesid'),(1, 'szFilename'),(1, 'szConnect'),(1, 'pdbid'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateDatabase():
    return win32more.Storage.Jet.JetCreateDatabaseW
def _define_JetCreateDatabase2A():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(SByte),UInt32,POINTER(UInt32),UInt32, use_last_error=False)(("JetCreateDatabase2A", windll["ESENT"]), ((1, 'sesid'),(1, 'szFilename'),(1, 'cpgDatabaseSizeMax'),(1, 'pdbid'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateDatabase2W():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(UInt16),UInt32,POINTER(UInt32),UInt32, use_last_error=False)(("JetCreateDatabase2W", windll["ESENT"]), ((1, 'sesid'),(1, 'szFilename'),(1, 'cpgDatabaseSizeMax'),(1, 'pdbid'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateDatabase2():
    return win32more.Storage.Jet.JetCreateDatabase2W
def _define_JetAttachDatabaseA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(SByte),UInt32, use_last_error=False)(("JetAttachDatabaseA", windll["ESENT"]), ((1, 'sesid'),(1, 'szFilename'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetAttachDatabaseW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(UInt16),UInt32, use_last_error=False)(("JetAttachDatabaseW", windll["ESENT"]), ((1, 'sesid'),(1, 'szFilename'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetAttachDatabase():
    return win32more.Storage.Jet.JetAttachDatabaseW
def _define_JetAttachDatabase2A():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(SByte),UInt32,UInt32, use_last_error=False)(("JetAttachDatabase2A", windll["ESENT"]), ((1, 'sesid'),(1, 'szFilename'),(1, 'cpgDatabaseSizeMax'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetAttachDatabase2W():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(UInt16),UInt32,UInt32, use_last_error=False)(("JetAttachDatabase2W", windll["ESENT"]), ((1, 'sesid'),(1, 'szFilename'),(1, 'cpgDatabaseSizeMax'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetAttachDatabase2():
    return win32more.Storage.Jet.JetAttachDatabase2W
def _define_JetDetachDatabaseA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(SByte), use_last_error=False)(("JetDetachDatabaseA", windll["ESENT"]), ((1, 'sesid'),(1, 'szFilename'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetDetachDatabaseW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(UInt16), use_last_error=False)(("JetDetachDatabaseW", windll["ESENT"]), ((1, 'sesid'),(1, 'szFilename'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetDetachDatabase():
    return win32more.Storage.Jet.JetDetachDatabaseW
def _define_JetDetachDatabase2A():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(SByte),UInt32, use_last_error=False)(("JetDetachDatabase2A", windll["ESENT"]), ((1, 'sesid'),(1, 'szFilename'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetDetachDatabase2W():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(UInt16),UInt32, use_last_error=False)(("JetDetachDatabase2W", windll["ESENT"]), ((1, 'sesid'),(1, 'szFilename'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetDetachDatabase2():
    return win32more.Storage.Jet.JetDetachDatabase2W
def _define_JetGetObjectInfoA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,UInt32,POINTER(SByte),POINTER(SByte),c_void_p,UInt32,UInt32, use_last_error=False)(("JetGetObjectInfoA", windll["ESENT"]), ((1, 'sesid'),(1, 'dbid'),(1, 'objtyp'),(1, 'szContainerName'),(1, 'szObjectName'),(1, 'pvResult'),(1, 'cbMax'),(1, 'InfoLevel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetObjectInfoW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,UInt32,POINTER(UInt16),POINTER(UInt16),c_void_p,UInt32,UInt32, use_last_error=False)(("JetGetObjectInfoW", windll["ESENT"]), ((1, 'sesid'),(1, 'dbid'),(1, 'objtyp'),(1, 'szContainerName'),(1, 'szObjectName'),(1, 'pvResult'),(1, 'cbMax'),(1, 'InfoLevel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetObjectInfo():
    return win32more.Storage.Jet.JetGetObjectInfoW
def _define_JetGetTableInfoA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,c_void_p,UInt32,UInt32, use_last_error=False)(("JetGetTableInfoA", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'pvResult'),(1, 'cbMax'),(1, 'InfoLevel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetTableInfoW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,c_void_p,UInt32,UInt32, use_last_error=False)(("JetGetTableInfoW", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'pvResult'),(1, 'cbMax'),(1, 'InfoLevel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetTableInfo():
    return win32more.Storage.Jet.JetGetTableInfoW
def _define_JetCreateTableA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(SByte),UInt32,UInt32,POINTER(win32more.Storage.StructuredStorage.JET_TABLEID), use_last_error=False)(("JetCreateTableA", windll["ESENT"]), ((1, 'sesid'),(1, 'dbid'),(1, 'szTableName'),(1, 'lPages'),(1, 'lDensity'),(1, 'ptableid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateTableW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(UInt16),UInt32,UInt32,POINTER(win32more.Storage.StructuredStorage.JET_TABLEID), use_last_error=False)(("JetCreateTableW", windll["ESENT"]), ((1, 'sesid'),(1, 'dbid'),(1, 'szTableName'),(1, 'lPages'),(1, 'lDensity'),(1, 'ptableid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateTable():
    return win32more.Storage.Jet.JetCreateTableW
def _define_JetCreateTableColumnIndexA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(win32more.Storage.Jet.JET_TABLECREATE_A_head), use_last_error=False)(("JetCreateTableColumnIndexA", windll["ESENT"]), ((1, 'sesid'),(1, 'dbid'),(1, 'ptablecreate'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateTableColumnIndexW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(win32more.Storage.Jet.JET_TABLECREATE_W_head), use_last_error=False)(("JetCreateTableColumnIndexW", windll["ESENT"]), ((1, 'sesid'),(1, 'dbid'),(1, 'ptablecreate'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateTableColumnIndex():
    return win32more.Storage.Jet.JetCreateTableColumnIndexW
def _define_JetCreateTableColumnIndex2A():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(win32more.Storage.Jet.JET_TABLECREATE2_A_head), use_last_error=False)(("JetCreateTableColumnIndex2A", windll["ESENT"]), ((1, 'sesid'),(1, 'dbid'),(1, 'ptablecreate'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateTableColumnIndex2W():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(win32more.Storage.Jet.JET_TABLECREATE2_W_head), use_last_error=False)(("JetCreateTableColumnIndex2W", windll["ESENT"]), ((1, 'sesid'),(1, 'dbid'),(1, 'ptablecreate'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateTableColumnIndex2():
    return win32more.Storage.Jet.JetCreateTableColumnIndex2W
def _define_JetCreateTableColumnIndex3A():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(win32more.Storage.Jet.JET_TABLECREATE3_A_head), use_last_error=False)(("JetCreateTableColumnIndex3A", windll["ESENT"]), ((1, 'sesid'),(1, 'dbid'),(1, 'ptablecreate'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateTableColumnIndex3W():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(win32more.Storage.Jet.JET_TABLECREATE3_W_head), use_last_error=False)(("JetCreateTableColumnIndex3W", windll["ESENT"]), ((1, 'sesid'),(1, 'dbid'),(1, 'ptablecreate'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateTableColumnIndex3():
    return win32more.Storage.Jet.JetCreateTableColumnIndex3W
def _define_JetCreateTableColumnIndex4A():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(win32more.Storage.Jet.JET_TABLECREATE4_A_head), use_last_error=False)(("JetCreateTableColumnIndex4A", windll["ESENT"]), ((1, 'sesid'),(1, 'dbid'),(1, 'ptablecreate'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateTableColumnIndex4W():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(win32more.Storage.Jet.JET_TABLECREATE4_W_head), use_last_error=False)(("JetCreateTableColumnIndex4W", windll["ESENT"]), ((1, 'sesid'),(1, 'dbid'),(1, 'ptablecreate'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateTableColumnIndex4():
    return win32more.Storage.Jet.JetCreateTableColumnIndex4W
def _define_JetDeleteTableA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(SByte), use_last_error=False)(("JetDeleteTableA", windll["ESENT"]), ((1, 'sesid'),(1, 'dbid'),(1, 'szTableName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetDeleteTableW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(UInt16), use_last_error=False)(("JetDeleteTableW", windll["ESENT"]), ((1, 'sesid'),(1, 'dbid'),(1, 'szTableName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetDeleteTable():
    return win32more.Storage.Jet.JetDeleteTableW
def _define_JetRenameTableA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(SByte),POINTER(SByte), use_last_error=False)(("JetRenameTableA", windll["ESENT"]), ((1, 'sesid'),(1, 'dbid'),(1, 'szName'),(1, 'szNameNew'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetRenameTableW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(UInt16),POINTER(UInt16), use_last_error=False)(("JetRenameTableW", windll["ESENT"]), ((1, 'sesid'),(1, 'dbid'),(1, 'szName'),(1, 'szNameNew'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetRenameTable():
    return win32more.Storage.Jet.JetRenameTableW
def _define_JetGetTableColumnInfoA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(SByte),c_void_p,UInt32,UInt32, use_last_error=False)(("JetGetTableColumnInfoA", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'szColumnName'),(1, 'pvResult'),(1, 'cbMax'),(1, 'InfoLevel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetTableColumnInfoW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(UInt16),c_void_p,UInt32,UInt32, use_last_error=False)(("JetGetTableColumnInfoW", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'szColumnName'),(1, 'pvResult'),(1, 'cbMax'),(1, 'InfoLevel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetTableColumnInfo():
    return win32more.Storage.Jet.JetGetTableColumnInfoW
def _define_JetGetColumnInfoA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(SByte),POINTER(SByte),c_void_p,UInt32,UInt32, use_last_error=False)(("JetGetColumnInfoA", windll["ESENT"]), ((1, 'sesid'),(1, 'dbid'),(1, 'szTableName'),(1, 'pColumnNameOrId'),(1, 'pvResult'),(1, 'cbMax'),(1, 'InfoLevel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetColumnInfoW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(UInt16),POINTER(UInt16),c_void_p,UInt32,UInt32, use_last_error=False)(("JetGetColumnInfoW", windll["ESENT"]), ((1, 'sesid'),(1, 'dbid'),(1, 'szTableName'),(1, 'pwColumnNameOrId'),(1, 'pvResult'),(1, 'cbMax'),(1, 'InfoLevel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetColumnInfo():
    return win32more.Storage.Jet.JetGetColumnInfoW
def _define_JetAddColumnA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(SByte),POINTER(win32more.Storage.Jet.JET_COLUMNDEF_head),c_void_p,UInt32,POINTER(UInt32), use_last_error=False)(("JetAddColumnA", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'szColumnName'),(1, 'pcolumndef'),(1, 'pvDefault'),(1, 'cbDefault'),(1, 'pcolumnid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetAddColumnW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(UInt16),POINTER(win32more.Storage.Jet.JET_COLUMNDEF_head),c_void_p,UInt32,POINTER(UInt32), use_last_error=False)(("JetAddColumnW", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'szColumnName'),(1, 'pcolumndef'),(1, 'pvDefault'),(1, 'cbDefault'),(1, 'pcolumnid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetAddColumn():
    return win32more.Storage.Jet.JetAddColumnW
def _define_JetDeleteColumnA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(SByte), use_last_error=False)(("JetDeleteColumnA", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'szColumnName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetDeleteColumnW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(UInt16), use_last_error=False)(("JetDeleteColumnW", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'szColumnName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetDeleteColumn():
    return win32more.Storage.Jet.JetDeleteColumnW
def _define_JetDeleteColumn2A():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(SByte),UInt32, use_last_error=False)(("JetDeleteColumn2A", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'szColumnName'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetDeleteColumn2W():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(UInt16),UInt32, use_last_error=False)(("JetDeleteColumn2W", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'szColumnName'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetDeleteColumn2():
    return win32more.Storage.Jet.JetDeleteColumn2W
def _define_JetRenameColumnA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(SByte),POINTER(SByte),UInt32, use_last_error=False)(("JetRenameColumnA", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'szName'),(1, 'szNameNew'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetRenameColumnW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(UInt16),POINTER(UInt16),UInt32, use_last_error=False)(("JetRenameColumnW", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'szName'),(1, 'szNameNew'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetRenameColumn():
    return win32more.Storage.Jet.JetRenameColumnW
def _define_JetSetColumnDefaultValueA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(SByte),POINTER(SByte),c_void_p,UInt32,UInt32, use_last_error=False)(("JetSetColumnDefaultValueA", windll["ESENT"]), ((1, 'sesid'),(1, 'dbid'),(1, 'szTableName'),(1, 'szColumnName'),(1, 'pvData'),(1, 'cbData'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetSetColumnDefaultValueW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(UInt16),POINTER(UInt16),c_void_p,UInt32,UInt32, use_last_error=False)(("JetSetColumnDefaultValueW", windll["ESENT"]), ((1, 'sesid'),(1, 'dbid'),(1, 'szTableName'),(1, 'szColumnName'),(1, 'pvData'),(1, 'cbData'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetSetColumnDefaultValue():
    return win32more.Storage.Jet.JetSetColumnDefaultValueW
def _define_JetGetTableIndexInfoA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(SByte),c_void_p,UInt32,UInt32, use_last_error=False)(("JetGetTableIndexInfoA", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'szIndexName'),(1, 'pvResult'),(1, 'cbResult'),(1, 'InfoLevel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetTableIndexInfoW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(UInt16),c_void_p,UInt32,UInt32, use_last_error=False)(("JetGetTableIndexInfoW", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'szIndexName'),(1, 'pvResult'),(1, 'cbResult'),(1, 'InfoLevel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetTableIndexInfo():
    return win32more.Storage.Jet.JetGetTableIndexInfoW
def _define_JetGetIndexInfoA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(SByte),POINTER(SByte),c_void_p,UInt32,UInt32, use_last_error=False)(("JetGetIndexInfoA", windll["ESENT"]), ((1, 'sesid'),(1, 'dbid'),(1, 'szTableName'),(1, 'szIndexName'),(1, 'pvResult'),(1, 'cbResult'),(1, 'InfoLevel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetIndexInfoW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(UInt16),POINTER(UInt16),c_void_p,UInt32,UInt32, use_last_error=False)(("JetGetIndexInfoW", windll["ESENT"]), ((1, 'sesid'),(1, 'dbid'),(1, 'szTableName'),(1, 'szIndexName'),(1, 'pvResult'),(1, 'cbResult'),(1, 'InfoLevel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetIndexInfo():
    return win32more.Storage.Jet.JetGetIndexInfoW
def _define_JetCreateIndexA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(SByte),UInt32,win32more.Foundation.PSTR,UInt32,UInt32, use_last_error=False)(("JetCreateIndexA", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'szIndexName'),(1, 'grbit'),(1, 'szKey'),(1, 'cbKey'),(1, 'lDensity'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateIndexW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(UInt16),UInt32,win32more.Foundation.PWSTR,UInt32,UInt32, use_last_error=False)(("JetCreateIndexW", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'szIndexName'),(1, 'grbit'),(1, 'szKey'),(1, 'cbKey'),(1, 'lDensity'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateIndex():
    return win32more.Storage.Jet.JetCreateIndexW
def _define_JetCreateIndex2A():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(win32more.Storage.Jet.JET_INDEXCREATE_A),UInt32, use_last_error=False)(("JetCreateIndex2A", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'pindexcreate'),(1, 'cIndexCreate'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateIndex2W():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(win32more.Storage.Jet.JET_INDEXCREATE_W),UInt32, use_last_error=False)(("JetCreateIndex2W", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'pindexcreate'),(1, 'cIndexCreate'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateIndex2():
    return win32more.Storage.Jet.JetCreateIndex2W
def _define_JetCreateIndex3A():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(win32more.Storage.Jet.JET_INDEXCREATE2_A),UInt32, use_last_error=False)(("JetCreateIndex3A", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'pindexcreate'),(1, 'cIndexCreate'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateIndex3W():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(win32more.Storage.Jet.JET_INDEXCREATE2_W),UInt32, use_last_error=False)(("JetCreateIndex3W", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'pindexcreate'),(1, 'cIndexCreate'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateIndex3():
    return win32more.Storage.Jet.JetCreateIndex3W
def _define_JetCreateIndex4A():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(win32more.Storage.Jet.JET_INDEXCREATE3_A),UInt32, use_last_error=False)(("JetCreateIndex4A", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'pindexcreate'),(1, 'cIndexCreate'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateIndex4W():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(win32more.Storage.Jet.JET_INDEXCREATE3_W),UInt32, use_last_error=False)(("JetCreateIndex4W", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'pindexcreate'),(1, 'cIndexCreate'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCreateIndex4():
    return win32more.Storage.Jet.JetCreateIndex4W
def _define_JetDeleteIndexA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(SByte), use_last_error=False)(("JetDeleteIndexA", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'szIndexName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetDeleteIndexW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(UInt16), use_last_error=False)(("JetDeleteIndexW", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'szIndexName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetDeleteIndex():
    return win32more.Storage.Jet.JetDeleteIndexW
def _define_JetBeginTransaction():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID, use_last_error=False)(("JetBeginTransaction", windll["ESENT"]), ((1, 'sesid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetBeginTransaction2():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32, use_last_error=False)(("JetBeginTransaction2", windll["ESENT"]), ((1, 'sesid'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetBeginTransaction3():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,Int64,UInt32, use_last_error=False)(("JetBeginTransaction3", windll["ESENT"]), ((1, 'sesid'),(1, 'trxid'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCommitTransaction():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32, use_last_error=False)(("JetCommitTransaction", windll["ESENT"]), ((1, 'sesid'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCommitTransaction2():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,UInt32,POINTER(win32more.Storage.Jet.JET_COMMIT_ID_head), use_last_error=False)(("JetCommitTransaction2", windll["ESENT"]), ((1, 'sesid'),(1, 'grbit'),(1, 'cmsecDurableCommit'),(1, 'pCommitId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetRollback():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32, use_last_error=False)(("JetRollback", windll["ESENT"]), ((1, 'sesid'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetDatabaseInfoA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,c_void_p,UInt32,UInt32, use_last_error=False)(("JetGetDatabaseInfoA", windll["ESENT"]), ((1, 'sesid'),(1, 'dbid'),(1, 'pvResult'),(1, 'cbMax'),(1, 'InfoLevel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetDatabaseInfoW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,c_void_p,UInt32,UInt32, use_last_error=False)(("JetGetDatabaseInfoW", windll["ESENT"]), ((1, 'sesid'),(1, 'dbid'),(1, 'pvResult'),(1, 'cbMax'),(1, 'InfoLevel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetDatabaseInfo():
    return win32more.Storage.Jet.JetGetDatabaseInfoW
def _define_JetGetDatabaseFileInfoA():
    try:
        return WINFUNCTYPE(Int32,POINTER(SByte),c_void_p,UInt32,UInt32, use_last_error=False)(("JetGetDatabaseFileInfoA", windll["ESENT"]), ((1, 'szDatabaseName'),(1, 'pvResult'),(1, 'cbMax'),(1, 'InfoLevel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetDatabaseFileInfoW():
    try:
        return WINFUNCTYPE(Int32,POINTER(UInt16),c_void_p,UInt32,UInt32, use_last_error=False)(("JetGetDatabaseFileInfoW", windll["ESENT"]), ((1, 'szDatabaseName'),(1, 'pvResult'),(1, 'cbMax'),(1, 'InfoLevel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetDatabaseFileInfo():
    return win32more.Storage.Jet.JetGetDatabaseFileInfoW
def _define_JetOpenDatabaseA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(SByte),POINTER(SByte),POINTER(UInt32),UInt32, use_last_error=False)(("JetOpenDatabaseA", windll["ESENT"]), ((1, 'sesid'),(1, 'szFilename'),(1, 'szConnect'),(1, 'pdbid'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOpenDatabaseW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(UInt16),POINTER(UInt16),POINTER(UInt32),UInt32, use_last_error=False)(("JetOpenDatabaseW", windll["ESENT"]), ((1, 'sesid'),(1, 'szFilename'),(1, 'szConnect'),(1, 'pdbid'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOpenDatabase():
    return win32more.Storage.Jet.JetOpenDatabaseW
def _define_JetCloseDatabase():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,UInt32, use_last_error=False)(("JetCloseDatabase", windll["ESENT"]), ((1, 'sesid'),(1, 'dbid'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOpenTableA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(SByte),c_void_p,UInt32,UInt32,POINTER(win32more.Storage.StructuredStorage.JET_TABLEID), use_last_error=False)(("JetOpenTableA", windll["ESENT"]), ((1, 'sesid'),(1, 'dbid'),(1, 'szTableName'),(1, 'pvParameters'),(1, 'cbParameters'),(1, 'grbit'),(1, 'ptableid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOpenTableW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(UInt16),c_void_p,UInt32,UInt32,POINTER(win32more.Storage.StructuredStorage.JET_TABLEID), use_last_error=False)(("JetOpenTableW", windll["ESENT"]), ((1, 'sesid'),(1, 'dbid'),(1, 'szTableName'),(1, 'pvParameters'),(1, 'cbParameters'),(1, 'grbit'),(1, 'ptableid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOpenTable():
    return win32more.Storage.Jet.JetOpenTableW
def _define_JetSetTableSequential():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,UInt32, use_last_error=False)(("JetSetTableSequential", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetResetTableSequential():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,UInt32, use_last_error=False)(("JetResetTableSequential", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCloseTable():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID, use_last_error=False)(("JetCloseTable", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetDelete():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID, use_last_error=False)(("JetDelete", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetUpdate():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,c_void_p,UInt32,POINTER(UInt32), use_last_error=False)(("JetUpdate", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'pvBookmark'),(1, 'cbBookmark'),(1, 'pcbActual'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetUpdate2():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,c_void_p,UInt32,POINTER(UInt32),UInt32, use_last_error=False)(("JetUpdate2", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'pvBookmark'),(1, 'cbBookmark'),(1, 'pcbActual'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetEscrowUpdate():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,UInt32,c_void_p,UInt32,c_void_p,UInt32,POINTER(UInt32),UInt32, use_last_error=False)(("JetEscrowUpdate", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'columnid'),(1, 'pv'),(1, 'cbMax'),(1, 'pvOld'),(1, 'cbOldMax'),(1, 'pcbOldActual'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetRetrieveColumn():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,UInt32,c_void_p,UInt32,POINTER(UInt32),UInt32,POINTER(win32more.Storage.Jet.JET_RETINFO_head), use_last_error=False)(("JetRetrieveColumn", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'columnid'),(1, 'pvData'),(1, 'cbData'),(1, 'pcbActual'),(1, 'grbit'),(1, 'pretinfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetRetrieveColumns():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(win32more.Storage.Jet.JET_RETRIEVECOLUMN),UInt32, use_last_error=False)(("JetRetrieveColumns", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'pretrievecolumn'),(1, 'cretrievecolumn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetEnumerateColumns():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,UInt32,POINTER(win32more.Storage.Jet.JET_ENUMCOLUMNID),POINTER(UInt32),POINTER(POINTER(win32more.Storage.Jet.JET_ENUMCOLUMN_head)),win32more.Storage.Jet.JET_PFNREALLOC,c_void_p,UInt32,UInt32, use_last_error=False)(("JetEnumerateColumns", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'cEnumColumnId'),(1, 'rgEnumColumnId'),(1, 'pcEnumColumn'),(1, 'prgEnumColumn'),(1, 'pfnRealloc'),(1, 'pvReallocContext'),(1, 'cbDataMost'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetRecordSize():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(win32more.Storage.Jet.JET_RECSIZE_head),UInt32, use_last_error=False)(("JetGetRecordSize", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'precsize'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetRecordSize2():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(win32more.Storage.Jet.JET_RECSIZE2_head),UInt32, use_last_error=False)(("JetGetRecordSize2", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'precsize'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetSetColumn():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,UInt32,c_void_p,UInt32,UInt32,POINTER(win32more.Storage.Jet.JET_SETINFO_head), use_last_error=False)(("JetSetColumn", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'columnid'),(1, 'pvData'),(1, 'cbData'),(1, 'grbit'),(1, 'psetinfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetSetColumns():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(win32more.Storage.Jet.JET_SETCOLUMN),UInt32, use_last_error=False)(("JetSetColumns", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'psetcolumn'),(1, 'csetcolumn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetPrepareUpdate():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,UInt32, use_last_error=False)(("JetPrepareUpdate", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'prep'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetRecordPosition():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(win32more.Storage.Jet.JET_RECPOS_head),UInt32, use_last_error=False)(("JetGetRecordPosition", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'precpos'),(1, 'cbRecpos'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGotoPosition():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(win32more.Storage.Jet.JET_RECPOS_head), use_last_error=False)(("JetGotoPosition", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'precpos'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetCursorInfo():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,c_void_p,UInt32,UInt32, use_last_error=False)(("JetGetCursorInfo", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'pvResult'),(1, 'cbMax'),(1, 'InfoLevel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetDupCursor():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(win32more.Storage.StructuredStorage.JET_TABLEID),UInt32, use_last_error=False)(("JetDupCursor", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'ptableid'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetCurrentIndexA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(SByte),UInt32, use_last_error=False)(("JetGetCurrentIndexA", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'szIndexName'),(1, 'cbIndexName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetCurrentIndexW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(UInt16),UInt32, use_last_error=False)(("JetGetCurrentIndexW", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'szIndexName'),(1, 'cbIndexName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetCurrentIndex():
    return win32more.Storage.Jet.JetGetCurrentIndexW
def _define_JetSetCurrentIndexA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(SByte), use_last_error=False)(("JetSetCurrentIndexA", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'szIndexName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetSetCurrentIndexW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(UInt16), use_last_error=False)(("JetSetCurrentIndexW", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'szIndexName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetSetCurrentIndex():
    return win32more.Storage.Jet.JetSetCurrentIndexW
def _define_JetSetCurrentIndex2A():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(SByte),UInt32, use_last_error=False)(("JetSetCurrentIndex2A", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'szIndexName'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetSetCurrentIndex2W():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(UInt16),UInt32, use_last_error=False)(("JetSetCurrentIndex2W", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'szIndexName'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetSetCurrentIndex2():
    return win32more.Storage.Jet.JetSetCurrentIndex2W
def _define_JetSetCurrentIndex3A():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(SByte),UInt32,UInt32, use_last_error=False)(("JetSetCurrentIndex3A", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'szIndexName'),(1, 'grbit'),(1, 'itagSequence'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetSetCurrentIndex3W():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(UInt16),UInt32,UInt32, use_last_error=False)(("JetSetCurrentIndex3W", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'szIndexName'),(1, 'grbit'),(1, 'itagSequence'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetSetCurrentIndex3():
    return win32more.Storage.Jet.JetSetCurrentIndex3W
def _define_JetSetCurrentIndex4A():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(SByte),POINTER(win32more.Storage.Jet.JET_INDEXID_head),UInt32,UInt32, use_last_error=False)(("JetSetCurrentIndex4A", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'szIndexName'),(1, 'pindexid'),(1, 'grbit'),(1, 'itagSequence'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetSetCurrentIndex4W():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(UInt16),POINTER(win32more.Storage.Jet.JET_INDEXID_head),UInt32,UInt32, use_last_error=False)(("JetSetCurrentIndex4W", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'szIndexName'),(1, 'pindexid'),(1, 'grbit'),(1, 'itagSequence'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetSetCurrentIndex4():
    return win32more.Storage.Jet.JetSetCurrentIndex4W
def _define_JetMove():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,Int32,UInt32, use_last_error=False)(("JetMove", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'cRow'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetSetCursorFilter():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(win32more.Storage.Jet.JET_INDEX_COLUMN),UInt32,UInt32, use_last_error=False)(("JetSetCursorFilter", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'rgColumnFilters'),(1, 'cColumnFilters'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetLock():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,UInt32, use_last_error=False)(("JetGetLock", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetMakeKey():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,c_void_p,UInt32,UInt32, use_last_error=False)(("JetMakeKey", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'pvData'),(1, 'cbData'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetSeek():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,UInt32, use_last_error=False)(("JetSeek", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetPrereadKeys():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(c_void_p),POINTER(UInt32),Int32,POINTER(Int32),UInt32, use_last_error=False)(("JetPrereadKeys", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'rgpvKeys'),(1, 'rgcbKeys'),(1, 'ckeys'),(1, 'pckeysPreread'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetPrereadIndexRanges():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(win32more.Storage.Jet.JET_INDEX_RANGE),UInt32,POINTER(UInt32),POINTER(UInt32),UInt32,UInt32, use_last_error=False)(("JetPrereadIndexRanges", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'rgIndexRanges'),(1, 'cIndexRanges'),(1, 'pcRangesPreread'),(1, 'rgcolumnidPreread'),(1, 'ccolumnidPreread'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetBookmark():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,c_void_p,UInt32,POINTER(UInt32), use_last_error=False)(("JetGetBookmark", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'pvBookmark'),(1, 'cbMax'),(1, 'pcbActual'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetSecondaryIndexBookmark():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,c_void_p,UInt32,POINTER(UInt32),c_void_p,UInt32,POINTER(UInt32),UInt32, use_last_error=False)(("JetGetSecondaryIndexBookmark", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'pvSecondaryKey'),(1, 'cbSecondaryKeyMax'),(1, 'pcbSecondaryKeyActual'),(1, 'pvPrimaryBookmark'),(1, 'cbPrimaryBookmarkMax'),(1, 'pcbPrimaryBookmarkActual'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCompactA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(SByte),POINTER(SByte),win32more.Storage.Jet.JET_PFNSTATUS,POINTER(win32more.Storage.Jet.CONVERT_A_head),UInt32, use_last_error=False)(("JetCompactA", windll["ESENT"]), ((1, 'sesid'),(1, 'szDatabaseSrc'),(1, 'szDatabaseDest'),(1, 'pfnStatus'),(1, 'pconvert'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCompactW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(UInt16),POINTER(UInt16),win32more.Storage.Jet.JET_PFNSTATUS,POINTER(win32more.Storage.Jet.CONVERT_W_head),UInt32, use_last_error=False)(("JetCompactW", windll["ESENT"]), ((1, 'sesid'),(1, 'szDatabaseSrc'),(1, 'szDatabaseDest'),(1, 'pfnStatus'),(1, 'pconvert'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCompact():
    return win32more.Storage.Jet.JetCompactW
def _define_JetDefragmentA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(SByte),POINTER(UInt32),POINTER(UInt32),UInt32, use_last_error=False)(("JetDefragmentA", windll["ESENT"]), ((1, 'sesid'),(1, 'dbid'),(1, 'szTableName'),(1, 'pcPasses'),(1, 'pcSeconds'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetDefragmentW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(UInt16),POINTER(UInt32),POINTER(UInt32),UInt32, use_last_error=False)(("JetDefragmentW", windll["ESENT"]), ((1, 'sesid'),(1, 'dbid'),(1, 'szTableName'),(1, 'pcPasses'),(1, 'pcSeconds'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetDefragment():
    return win32more.Storage.Jet.JetDefragmentW
def _define_JetDefragment2A():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(SByte),POINTER(UInt32),POINTER(UInt32),win32more.Storage.Jet.JET_CALLBACK,UInt32, use_last_error=False)(("JetDefragment2A", windll["ESENT"]), ((1, 'sesid'),(1, 'dbid'),(1, 'szTableName'),(1, 'pcPasses'),(1, 'pcSeconds'),(1, 'callback'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetDefragment2W():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(UInt16),POINTER(UInt32),POINTER(UInt32),win32more.Storage.Jet.JET_CALLBACK,UInt32, use_last_error=False)(("JetDefragment2W", windll["ESENT"]), ((1, 'sesid'),(1, 'dbid'),(1, 'szTableName'),(1, 'pcPasses'),(1, 'pcSeconds'),(1, 'callback'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetDefragment2():
    return win32more.Storage.Jet.JetDefragment2W
def _define_JetDefragment3A():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(SByte),POINTER(SByte),POINTER(UInt32),POINTER(UInt32),win32more.Storage.Jet.JET_CALLBACK,c_void_p,UInt32, use_last_error=False)(("JetDefragment3A", windll["ESENT"]), ((1, 'sesid'),(1, 'szDatabaseName'),(1, 'szTableName'),(1, 'pcPasses'),(1, 'pcSeconds'),(1, 'callback'),(1, 'pvContext'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetDefragment3W():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(UInt16),POINTER(UInt16),POINTER(UInt32),POINTER(UInt32),win32more.Storage.Jet.JET_CALLBACK,c_void_p,UInt32, use_last_error=False)(("JetDefragment3W", windll["ESENT"]), ((1, 'sesid'),(1, 'szDatabaseName'),(1, 'szTableName'),(1, 'pcPasses'),(1, 'pcSeconds'),(1, 'callback'),(1, 'pvContext'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetDefragment3():
    return win32more.Storage.Jet.JetDefragment3W
def _define_JetSetDatabaseSizeA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(SByte),UInt32,POINTER(UInt32), use_last_error=False)(("JetSetDatabaseSizeA", windll["ESENT"]), ((1, 'sesid'),(1, 'szDatabaseName'),(1, 'cpg'),(1, 'pcpgReal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetSetDatabaseSizeW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(UInt16),UInt32,POINTER(UInt32), use_last_error=False)(("JetSetDatabaseSizeW", windll["ESENT"]), ((1, 'sesid'),(1, 'szDatabaseName'),(1, 'cpg'),(1, 'pcpgReal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetSetDatabaseSize():
    return win32more.Storage.Jet.JetSetDatabaseSizeW
def _define_JetGrowDatabase():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,UInt32,POINTER(UInt32), use_last_error=False)(("JetGrowDatabase", windll["ESENT"]), ((1, 'sesid'),(1, 'dbid'),(1, 'cpg'),(1, 'pcpgReal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetResizeDatabase():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,UInt32,POINTER(UInt32),UInt32, use_last_error=False)(("JetResizeDatabase", windll["ESENT"]), ((1, 'sesid'),(1, 'dbid'),(1, 'cpgTarget'),(1, 'pcpgActual'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetSetSessionContext():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_API_PTR, use_last_error=False)(("JetSetSessionContext", windll["ESENT"]), ((1, 'sesid'),(1, 'ulContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetResetSessionContext():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID, use_last_error=False)(("JetResetSessionContext", windll["ESENT"]), ((1, 'sesid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGotoBookmark():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,c_void_p,UInt32, use_last_error=False)(("JetGotoBookmark", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'pvBookmark'),(1, 'cbBookmark'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGotoSecondaryIndexBookmark():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,c_void_p,UInt32,c_void_p,UInt32,UInt32, use_last_error=False)(("JetGotoSecondaryIndexBookmark", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'pvSecondaryKey'),(1, 'cbSecondaryKey'),(1, 'pvPrimaryBookmark'),(1, 'cbPrimaryBookmark'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetIntersectIndexes():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(win32more.Storage.Jet.JET_INDEXRANGE),UInt32,POINTER(win32more.Storage.Jet.JET_RECORDLIST_head),UInt32, use_last_error=False)(("JetIntersectIndexes", windll["ESENT"]), ((1, 'sesid'),(1, 'rgindexrange'),(1, 'cindexrange'),(1, 'precordlist'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetComputeStats():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID, use_last_error=False)(("JetComputeStats", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOpenTempTable():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(win32more.Storage.Jet.JET_COLUMNDEF),UInt32,UInt32,POINTER(win32more.Storage.StructuredStorage.JET_TABLEID),POINTER(UInt32), use_last_error=False)(("JetOpenTempTable", windll["ESENT"]), ((1, 'sesid'),(1, 'prgcolumndef'),(1, 'ccolumn'),(1, 'grbit'),(1, 'ptableid'),(1, 'prgcolumnid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOpenTempTable2():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(win32more.Storage.Jet.JET_COLUMNDEF),UInt32,UInt32,UInt32,POINTER(win32more.Storage.StructuredStorage.JET_TABLEID),POINTER(UInt32), use_last_error=False)(("JetOpenTempTable2", windll["ESENT"]), ((1, 'sesid'),(1, 'prgcolumndef'),(1, 'ccolumn'),(1, 'lcid'),(1, 'grbit'),(1, 'ptableid'),(1, 'prgcolumnid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOpenTempTable3():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(win32more.Storage.Jet.JET_COLUMNDEF),UInt32,POINTER(win32more.Storage.Jet.JET_UNICODEINDEX_head),UInt32,POINTER(win32more.Storage.StructuredStorage.JET_TABLEID),POINTER(UInt32), use_last_error=False)(("JetOpenTempTable3", windll["ESENT"]), ((1, 'sesid'),(1, 'prgcolumndef'),(1, 'ccolumn'),(1, 'pidxunicode'),(1, 'grbit'),(1, 'ptableid'),(1, 'prgcolumnid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOpenTemporaryTable():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(win32more.Storage.Jet.JET_OPENTEMPORARYTABLE_head), use_last_error=False)(("JetOpenTemporaryTable", windll["ESENT"]), ((1, 'sesid'),(1, 'popentemporarytable'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOpenTemporaryTable2():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,POINTER(win32more.Storage.Jet.JET_OPENTEMPORARYTABLE2_head), use_last_error=False)(("JetOpenTemporaryTable2", windll["ESENT"]), ((1, 'sesid'),(1, 'popentemporarytable'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetBackupA():
    try:
        return WINFUNCTYPE(Int32,POINTER(SByte),UInt32,win32more.Storage.Jet.JET_PFNSTATUS, use_last_error=False)(("JetBackupA", windll["ESENT"]), ((1, 'szBackupPath'),(1, 'grbit'),(1, 'pfnStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetBackupW():
    try:
        return WINFUNCTYPE(Int32,POINTER(UInt16),UInt32,win32more.Storage.Jet.JET_PFNSTATUS, use_last_error=False)(("JetBackupW", windll["ESENT"]), ((1, 'szBackupPath'),(1, 'grbit'),(1, 'pfnStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetBackup():
    return win32more.Storage.Jet.JetBackupW
def _define_JetBackupInstanceA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,POINTER(SByte),UInt32,win32more.Storage.Jet.JET_PFNSTATUS, use_last_error=False)(("JetBackupInstanceA", windll["ESENT"]), ((1, 'instance'),(1, 'szBackupPath'),(1, 'grbit'),(1, 'pfnStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetBackupInstanceW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,POINTER(UInt16),UInt32,win32more.Storage.Jet.JET_PFNSTATUS, use_last_error=False)(("JetBackupInstanceW", windll["ESENT"]), ((1, 'instance'),(1, 'szBackupPath'),(1, 'grbit'),(1, 'pfnStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetBackupInstance():
    return win32more.Storage.Jet.JetBackupInstanceW
def _define_JetRestoreA():
    try:
        return WINFUNCTYPE(Int32,POINTER(SByte),win32more.Storage.Jet.JET_PFNSTATUS, use_last_error=False)(("JetRestoreA", windll["ESENT"]), ((1, 'szSource'),(1, 'pfn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetRestoreW():
    try:
        return WINFUNCTYPE(Int32,POINTER(UInt16),win32more.Storage.Jet.JET_PFNSTATUS, use_last_error=False)(("JetRestoreW", windll["ESENT"]), ((1, 'szSource'),(1, 'pfn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetRestore():
    return win32more.Storage.Jet.JetRestoreW
def _define_JetRestore2A():
    try:
        return WINFUNCTYPE(Int32,POINTER(SByte),POINTER(SByte),win32more.Storage.Jet.JET_PFNSTATUS, use_last_error=False)(("JetRestore2A", windll["ESENT"]), ((1, 'sz'),(1, 'szDest'),(1, 'pfn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetRestore2W():
    try:
        return WINFUNCTYPE(Int32,POINTER(UInt16),POINTER(UInt16),win32more.Storage.Jet.JET_PFNSTATUS, use_last_error=False)(("JetRestore2W", windll["ESENT"]), ((1, 'sz'),(1, 'szDest'),(1, 'pfn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetRestore2():
    return win32more.Storage.Jet.JetRestore2W
def _define_JetRestoreInstanceA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,POINTER(SByte),POINTER(SByte),win32more.Storage.Jet.JET_PFNSTATUS, use_last_error=False)(("JetRestoreInstanceA", windll["ESENT"]), ((1, 'instance'),(1, 'sz'),(1, 'szDest'),(1, 'pfn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetRestoreInstanceW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,POINTER(UInt16),POINTER(UInt16),win32more.Storage.Jet.JET_PFNSTATUS, use_last_error=False)(("JetRestoreInstanceW", windll["ESENT"]), ((1, 'instance'),(1, 'sz'),(1, 'szDest'),(1, 'pfn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetRestoreInstance():
    return win32more.Storage.Jet.JetRestoreInstanceW
def _define_JetSetIndexRange():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,UInt32, use_last_error=False)(("JetSetIndexRange", windll["ESENT"]), ((1, 'sesid'),(1, 'tableidSrc'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetIndexRecordCount():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(UInt32),UInt32, use_last_error=False)(("JetIndexRecordCount", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'pcrec'),(1, 'crecMax'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetRetrieveKey():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,c_void_p,UInt32,POINTER(UInt32),UInt32, use_last_error=False)(("JetRetrieveKey", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'pvKey'),(1, 'cbMax'),(1, 'pcbActual'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetBeginExternalBackup():
    try:
        return WINFUNCTYPE(Int32,UInt32, use_last_error=False)(("JetBeginExternalBackup", windll["ESENT"]), ((1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetBeginExternalBackupInstance():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,UInt32, use_last_error=False)(("JetBeginExternalBackupInstance", windll["ESENT"]), ((1, 'instance'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetAttachInfoA():
    try:
        return WINFUNCTYPE(Int32,POINTER(SByte),UInt32,POINTER(UInt32), use_last_error=False)(("JetGetAttachInfoA", windll["ESENT"]), ((1, 'szzDatabases'),(1, 'cbMax'),(1, 'pcbActual'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetAttachInfoW():
    try:
        return WINFUNCTYPE(Int32,POINTER(UInt16),UInt32,POINTER(UInt32), use_last_error=False)(("JetGetAttachInfoW", windll["ESENT"]), ((1, 'wszzDatabases'),(1, 'cbMax'),(1, 'pcbActual'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetAttachInfo():
    return win32more.Storage.Jet.JetGetAttachInfoW
def _define_JetGetAttachInfoInstanceA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,POINTER(SByte),UInt32,POINTER(UInt32), use_last_error=False)(("JetGetAttachInfoInstanceA", windll["ESENT"]), ((1, 'instance'),(1, 'szzDatabases'),(1, 'cbMax'),(1, 'pcbActual'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetAttachInfoInstanceW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,POINTER(UInt16),UInt32,POINTER(UInt32), use_last_error=False)(("JetGetAttachInfoInstanceW", windll["ESENT"]), ((1, 'instance'),(1, 'szzDatabases'),(1, 'cbMax'),(1, 'pcbActual'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetAttachInfoInstance():
    return win32more.Storage.Jet.JetGetAttachInfoInstanceW
def _define_JetOpenFileA():
    try:
        return WINFUNCTYPE(Int32,POINTER(SByte),POINTER(win32more.Storage.StructuredStorage.JET_HANDLE),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("JetOpenFileA", windll["ESENT"]), ((1, 'szFileName'),(1, 'phfFile'),(1, 'pulFileSizeLow'),(1, 'pulFileSizeHigh'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOpenFileW():
    try:
        return WINFUNCTYPE(Int32,POINTER(UInt16),POINTER(win32more.Storage.StructuredStorage.JET_HANDLE),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("JetOpenFileW", windll["ESENT"]), ((1, 'szFileName'),(1, 'phfFile'),(1, 'pulFileSizeLow'),(1, 'pulFileSizeHigh'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOpenFile():
    return win32more.Storage.Jet.JetOpenFileW
def _define_JetOpenFileInstanceA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,POINTER(SByte),POINTER(win32more.Storage.StructuredStorage.JET_HANDLE),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("JetOpenFileInstanceA", windll["ESENT"]), ((1, 'instance'),(1, 'szFileName'),(1, 'phfFile'),(1, 'pulFileSizeLow'),(1, 'pulFileSizeHigh'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOpenFileInstanceW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,POINTER(UInt16),POINTER(win32more.Storage.StructuredStorage.JET_HANDLE),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("JetOpenFileInstanceW", windll["ESENT"]), ((1, 'instance'),(1, 'szFileName'),(1, 'phfFile'),(1, 'pulFileSizeLow'),(1, 'pulFileSizeHigh'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOpenFileInstance():
    return win32more.Storage.Jet.JetOpenFileInstanceW
def _define_JetReadFile():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_HANDLE,c_void_p,UInt32,POINTER(UInt32), use_last_error=False)(("JetReadFile", windll["ESENT"]), ((1, 'hfFile'),(1, 'pv'),(1, 'cb'),(1, 'pcbActual'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetReadFileInstance():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,win32more.Storage.StructuredStorage.JET_HANDLE,c_void_p,UInt32,POINTER(UInt32), use_last_error=False)(("JetReadFileInstance", windll["ESENT"]), ((1, 'instance'),(1, 'hfFile'),(1, 'pv'),(1, 'cb'),(1, 'pcbActual'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCloseFile():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_HANDLE, use_last_error=False)(("JetCloseFile", windll["ESENT"]), ((1, 'hfFile'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetCloseFileInstance():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,win32more.Storage.StructuredStorage.JET_HANDLE, use_last_error=False)(("JetCloseFileInstance", windll["ESENT"]), ((1, 'instance'),(1, 'hfFile'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetLogInfoA():
    try:
        return WINFUNCTYPE(Int32,POINTER(SByte),UInt32,POINTER(UInt32), use_last_error=False)(("JetGetLogInfoA", windll["ESENT"]), ((1, 'szzLogs'),(1, 'cbMax'),(1, 'pcbActual'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetLogInfoW():
    try:
        return WINFUNCTYPE(Int32,POINTER(UInt16),UInt32,POINTER(UInt32), use_last_error=False)(("JetGetLogInfoW", windll["ESENT"]), ((1, 'szzLogs'),(1, 'cbMax'),(1, 'pcbActual'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetLogInfo():
    return win32more.Storage.Jet.JetGetLogInfoW
def _define_JetGetLogInfoInstanceA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,POINTER(SByte),UInt32,POINTER(UInt32), use_last_error=False)(("JetGetLogInfoInstanceA", windll["ESENT"]), ((1, 'instance'),(1, 'szzLogs'),(1, 'cbMax'),(1, 'pcbActual'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetLogInfoInstanceW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,POINTER(UInt16),UInt32,POINTER(UInt32), use_last_error=False)(("JetGetLogInfoInstanceW", windll["ESENT"]), ((1, 'instance'),(1, 'wszzLogs'),(1, 'cbMax'),(1, 'pcbActual'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetLogInfoInstance():
    return win32more.Storage.Jet.JetGetLogInfoInstanceW
def _define_JetGetLogInfoInstance2A():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,POINTER(SByte),UInt32,POINTER(UInt32),POINTER(win32more.Storage.Jet.JET_LOGINFO_A_head), use_last_error=False)(("JetGetLogInfoInstance2A", windll["ESENT"]), ((1, 'instance'),(1, 'szzLogs'),(1, 'cbMax'),(1, 'pcbActual'),(1, 'pLogInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetLogInfoInstance2W():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,POINTER(UInt16),UInt32,POINTER(UInt32),POINTER(win32more.Storage.Jet.JET_LOGINFO_W_head), use_last_error=False)(("JetGetLogInfoInstance2W", windll["ESENT"]), ((1, 'instance'),(1, 'wszzLogs'),(1, 'cbMax'),(1, 'pcbActual'),(1, 'pLogInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetLogInfoInstance2():
    return win32more.Storage.Jet.JetGetLogInfoInstance2W
def _define_JetGetTruncateLogInfoInstanceA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,POINTER(SByte),UInt32,POINTER(UInt32), use_last_error=False)(("JetGetTruncateLogInfoInstanceA", windll["ESENT"]), ((1, 'instance'),(1, 'szzLogs'),(1, 'cbMax'),(1, 'pcbActual'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetTruncateLogInfoInstanceW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,POINTER(UInt16),UInt32,POINTER(UInt32), use_last_error=False)(("JetGetTruncateLogInfoInstanceW", windll["ESENT"]), ((1, 'instance'),(1, 'wszzLogs'),(1, 'cbMax'),(1, 'pcbActual'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetTruncateLogInfoInstance():
    return win32more.Storage.Jet.JetGetTruncateLogInfoInstanceW
def _define_JetTruncateLog():
    try:
        return WINFUNCTYPE(Int32, use_last_error=False)(("JetTruncateLog", windll["ESENT"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetTruncateLogInstance():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE, use_last_error=False)(("JetTruncateLogInstance", windll["ESENT"]), ((1, 'instance'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetEndExternalBackup():
    try:
        return WINFUNCTYPE(Int32, use_last_error=False)(("JetEndExternalBackup", windll["ESENT"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetEndExternalBackupInstance():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE, use_last_error=False)(("JetEndExternalBackupInstance", windll["ESENT"]), ((1, 'instance'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetEndExternalBackupInstance2():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_INSTANCE,UInt32, use_last_error=False)(("JetEndExternalBackupInstance2", windll["ESENT"]), ((1, 'instance'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetExternalRestoreA():
    try:
        return WINFUNCTYPE(Int32,POINTER(SByte),POINTER(SByte),POINTER(win32more.Storage.Jet.JET_RSTMAP_A),Int32,POINTER(SByte),Int32,Int32,win32more.Storage.Jet.JET_PFNSTATUS, use_last_error=False)(("JetExternalRestoreA", windll["ESENT"]), ((1, 'szCheckpointFilePath'),(1, 'szLogPath'),(1, 'rgrstmap'),(1, 'crstfilemap'),(1, 'szBackupLogPath'),(1, 'genLow'),(1, 'genHigh'),(1, 'pfn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetExternalRestoreW():
    try:
        return WINFUNCTYPE(Int32,POINTER(UInt16),POINTER(UInt16),POINTER(win32more.Storage.Jet.JET_RSTMAP_W),Int32,POINTER(UInt16),Int32,Int32,win32more.Storage.Jet.JET_PFNSTATUS, use_last_error=False)(("JetExternalRestoreW", windll["ESENT"]), ((1, 'szCheckpointFilePath'),(1, 'szLogPath'),(1, 'rgrstmap'),(1, 'crstfilemap'),(1, 'szBackupLogPath'),(1, 'genLow'),(1, 'genHigh'),(1, 'pfn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetExternalRestore():
    return win32more.Storage.Jet.JetExternalRestoreW
def _define_JetExternalRestore2A():
    try:
        return WINFUNCTYPE(Int32,POINTER(SByte),POINTER(SByte),POINTER(win32more.Storage.Jet.JET_RSTMAP_A),Int32,POINTER(SByte),POINTER(win32more.Storage.Jet.JET_LOGINFO_A_head),POINTER(SByte),POINTER(SByte),POINTER(SByte),win32more.Storage.Jet.JET_PFNSTATUS, use_last_error=False)(("JetExternalRestore2A", windll["ESENT"]), ((1, 'szCheckpointFilePath'),(1, 'szLogPath'),(1, 'rgrstmap'),(1, 'crstfilemap'),(1, 'szBackupLogPath'),(1, 'pLogInfo'),(1, 'szTargetInstanceName'),(1, 'szTargetInstanceLogPath'),(1, 'szTargetInstanceCheckpointPath'),(1, 'pfn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetExternalRestore2W():
    try:
        return WINFUNCTYPE(Int32,POINTER(UInt16),POINTER(UInt16),POINTER(win32more.Storage.Jet.JET_RSTMAP_W),Int32,POINTER(UInt16),POINTER(win32more.Storage.Jet.JET_LOGINFO_W_head),POINTER(UInt16),POINTER(UInt16),POINTER(UInt16),win32more.Storage.Jet.JET_PFNSTATUS, use_last_error=False)(("JetExternalRestore2W", windll["ESENT"]), ((1, 'szCheckpointFilePath'),(1, 'szLogPath'),(1, 'rgrstmap'),(1, 'crstfilemap'),(1, 'szBackupLogPath'),(1, 'pLogInfo'),(1, 'szTargetInstanceName'),(1, 'szTargetInstanceLogPath'),(1, 'szTargetInstanceCheckpointPath'),(1, 'pfn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetExternalRestore2():
    return win32more.Storage.Jet.JetExternalRestore2W
def _define_JetRegisterCallback():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,UInt32,win32more.Storage.Jet.JET_CALLBACK,c_void_p,POINTER(win32more.Storage.StructuredStorage.JET_HANDLE), use_last_error=False)(("JetRegisterCallback", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'cbtyp'),(1, 'pCallback'),(1, 'pvContext'),(1, 'phCallbackId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetUnregisterCallback():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,UInt32,win32more.Storage.StructuredStorage.JET_HANDLE, use_last_error=False)(("JetUnregisterCallback", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'cbtyp'),(1, 'hCallbackId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetInstanceInfoA():
    try:
        return WINFUNCTYPE(Int32,POINTER(UInt32),POINTER(POINTER(win32more.Storage.Jet.JET_INSTANCE_INFO_A_head)), use_last_error=False)(("JetGetInstanceInfoA", windll["ESENT"]), ((1, 'pcInstanceInfo'),(1, 'paInstanceInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetInstanceInfoW():
    try:
        return WINFUNCTYPE(Int32,POINTER(UInt32),POINTER(POINTER(win32more.Storage.Jet.JET_INSTANCE_INFO_W_head)), use_last_error=False)(("JetGetInstanceInfoW", windll["ESENT"]), ((1, 'pcInstanceInfo'),(1, 'paInstanceInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetInstanceInfo():
    return win32more.Storage.Jet.JetGetInstanceInfoW
def _define_JetFreeBuffer():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSTR, use_last_error=False)(("JetFreeBuffer", windll["ESENT"]), ((1, 'pbBuf'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetSetLS():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,win32more.Storage.Jet.JET_LS,UInt32, use_last_error=False)(("JetSetLS", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'ls'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetLS():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,win32more.Storage.StructuredStorage.JET_TABLEID,POINTER(win32more.Storage.Jet.JET_LS),UInt32, use_last_error=False)(("JetGetLS", windll["ESENT"]), ((1, 'sesid'),(1, 'tableid'),(1, 'pls'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOSSnapshotPrepare():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Storage.Jet.JET_OSSNAPID),UInt32, use_last_error=False)(("JetOSSnapshotPrepare", windll["ESENT"]), ((1, 'psnapId'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOSSnapshotPrepareInstance():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.Jet.JET_OSSNAPID,win32more.Storage.StructuredStorage.JET_INSTANCE,UInt32, use_last_error=False)(("JetOSSnapshotPrepareInstance", windll["ESENT"]), ((1, 'snapId'),(1, 'instance'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOSSnapshotFreezeA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.Jet.JET_OSSNAPID,POINTER(UInt32),POINTER(POINTER(win32more.Storage.Jet.JET_INSTANCE_INFO_A_head)),UInt32, use_last_error=False)(("JetOSSnapshotFreezeA", windll["ESENT"]), ((1, 'snapId'),(1, 'pcInstanceInfo'),(1, 'paInstanceInfo'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOSSnapshotFreezeW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.Jet.JET_OSSNAPID,POINTER(UInt32),POINTER(POINTER(win32more.Storage.Jet.JET_INSTANCE_INFO_W_head)),UInt32, use_last_error=False)(("JetOSSnapshotFreezeW", windll["ESENT"]), ((1, 'snapId'),(1, 'pcInstanceInfo'),(1, 'paInstanceInfo'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOSSnapshotFreeze():
    return win32more.Storage.Jet.JetOSSnapshotFreezeW
def _define_JetOSSnapshotThaw():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.Jet.JET_OSSNAPID,UInt32, use_last_error=False)(("JetOSSnapshotThaw", windll["ESENT"]), ((1, 'snapId'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOSSnapshotAbort():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.Jet.JET_OSSNAPID,UInt32, use_last_error=False)(("JetOSSnapshotAbort", windll["ESENT"]), ((1, 'snapId'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOSSnapshotTruncateLog():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.Jet.JET_OSSNAPID,UInt32, use_last_error=False)(("JetOSSnapshotTruncateLog", windll["ESENT"]), ((1, 'snapId'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOSSnapshotTruncateLogInstance():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.Jet.JET_OSSNAPID,win32more.Storage.StructuredStorage.JET_INSTANCE,UInt32, use_last_error=False)(("JetOSSnapshotTruncateLogInstance", windll["ESENT"]), ((1, 'snapId'),(1, 'instance'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOSSnapshotGetFreezeInfoA():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.Jet.JET_OSSNAPID,POINTER(UInt32),POINTER(POINTER(win32more.Storage.Jet.JET_INSTANCE_INFO_A_head)),UInt32, use_last_error=False)(("JetOSSnapshotGetFreezeInfoA", windll["ESENT"]), ((1, 'snapId'),(1, 'pcInstanceInfo'),(1, 'paInstanceInfo'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOSSnapshotGetFreezeInfoW():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.Jet.JET_OSSNAPID,POINTER(UInt32),POINTER(POINTER(win32more.Storage.Jet.JET_INSTANCE_INFO_W_head)),UInt32, use_last_error=False)(("JetOSSnapshotGetFreezeInfoW", windll["ESENT"]), ((1, 'snapId'),(1, 'pcInstanceInfo'),(1, 'paInstanceInfo'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetOSSnapshotGetFreezeInfo():
    return win32more.Storage.Jet.JetOSSnapshotGetFreezeInfoW
def _define_JetOSSnapshotEnd():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.Jet.JET_OSSNAPID,UInt32, use_last_error=False)(("JetOSSnapshotEnd", windll["ESENT"]), ((1, 'snapId'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetConfigureProcessForCrashDump():
    try:
        return WINFUNCTYPE(Int32,UInt32, use_last_error=False)(("JetConfigureProcessForCrashDump", windll["ESENT"]), ((1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetErrorInfoW():
    try:
        return WINFUNCTYPE(Int32,c_void_p,c_void_p,UInt32,UInt32,UInt32, use_last_error=False)(("JetGetErrorInfoW", windll["ESENT"]), ((1, 'pvContext'),(1, 'pvResult'),(1, 'cbMax'),(1, 'InfoLevel'),(1, 'grbit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetSetSessionParameter():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,c_void_p,UInt32, use_last_error=False)(("JetSetSessionParameter", windll["ESENT"]), ((1, 'sesid'),(1, 'sesparamid'),(1, 'pvParam'),(1, 'cbParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_JetGetSessionParameter():
    try:
        return WINFUNCTYPE(Int32,win32more.Storage.StructuredStorage.JET_SESID,UInt32,POINTER(Void),UInt32,POINTER(UInt32), use_last_error=False)(("JetGetSessionParameter", windll["ESENT"]), ((1, 'sesid'),(1, 'sesparamid'),(1, 'pvParam'),(1, 'cbParamMax'),(1, 'pcbParamActual'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "JET_bitConfigStoreReadControlInhibitRead",
    "JET_bitConfigStoreReadControlDisableAll",
    "JET_bitConfigStoreReadControlDefault",
    "JET_bitDefragmentBatchStart",
    "JET_bitDefragmentBatchStop",
    "JET_bitDefragmentAvailSpaceTreesOnly",
    "JET_bitDefragmentNoPartialMerges",
    "JET_bitDefragmentBTree",
    "JET_cbtypNull",
    "JET_cbtypFinalize",
    "JET_cbtypBeforeInsert",
    "JET_cbtypAfterInsert",
    "JET_cbtypBeforeReplace",
    "JET_cbtypAfterReplace",
    "JET_cbtypBeforeDelete",
    "JET_cbtypAfterDelete",
    "JET_cbtypUserDefinedDefaultValue",
    "JET_cbtypOnlineDefragCompleted",
    "JET_cbtypFreeCursorLS",
    "JET_cbtypFreeTableLS",
    "JET_bitTableInfoUpdatable",
    "JET_bitTableInfoBookmark",
    "JET_bitTableInfoRollback",
    "JET_bitObjectSystem",
    "JET_bitObjectTableFixedDDL",
    "JET_bitObjectTableTemplate",
    "JET_bitObjectTableDerived",
    "JET_bitObjectTableNoFixedVarColumnsInDerivedTables",
    "JET_MAX_COMPUTERNAME_LENGTH",
    "JET_bitDurableCommitCallbackLogUnavailable",
    "JET_cbBookmarkMost",
    "JET_cbNameMost",
    "JET_cbFullNameMost",
    "JET_cbColumnLVPageOverhead",
    "JET_cbLVDefaultValueMost",
    "JET_cbColumnMost",
    "JET_cbLVColumnMost",
    "JET_cbKeyMost8KBytePage",
    "JET_cbKeyMost4KBytePage",
    "JET_cbKeyMost2KBytePage",
    "JET_cbKeyMostMin",
    "JET_cbKeyMost",
    "JET_cbLimitKeyMost",
    "JET_cbPrimaryKeyMost",
    "JET_cbSecondaryKeyMost",
    "JET_ccolKeyMost",
    "JET_ccolMost",
    "JET_ccolFixedMost",
    "JET_ccolVarMost",
    "JET_EventLoggingDisable",
    "JET_EventLoggingLevelMin",
    "JET_EventLoggingLevelLow",
    "JET_EventLoggingLevelMedium",
    "JET_EventLoggingLevelHigh",
    "JET_EventLoggingLevelMax",
    "JET_IOPriorityNormal",
    "JET_IOPriorityLow",
    "JET_configDefault",
    "JET_configRemoveQuotas",
    "JET_configLowDiskFootprint",
    "JET_configMediumDiskFootprint",
    "JET_configLowMemory",
    "JET_configDynamicMediumMemory",
    "JET_configLowPower",
    "JET_configSSDProfileIO",
    "JET_configRunSilent",
    "JET_configUnthrottledMemory",
    "JET_configHighConcurrencyScaling",
    "JET_paramSystemPath",
    "JET_paramTempPath",
    "JET_paramLogFilePath",
    "JET_paramBaseName",
    "JET_paramEventSource",
    "JET_paramMaxSessions",
    "JET_paramMaxOpenTables",
    "JET_paramPreferredMaxOpenTables",
    "JET_paramCachedClosedTables",
    "JET_paramMaxCursors",
    "JET_paramMaxVerPages",
    "JET_paramPreferredVerPages",
    "JET_paramGlobalMinVerPages",
    "JET_paramVersionStoreTaskQueueMax",
    "JET_paramMaxTemporaryTables",
    "JET_paramLogFileSize",
    "JET_paramLogBuffers",
    "JET_paramWaitLogFlush",
    "JET_paramLogCheckpointPeriod",
    "JET_paramLogWaitingUserMax",
    "JET_paramCommitDefault",
    "JET_paramCircularLog",
    "JET_paramDbExtensionSize",
    "JET_paramPageTempDBMin",
    "JET_paramPageFragment",
    "JET_paramEnableFileCache",
    "JET_paramVerPageSize",
    "JET_paramConfiguration",
    "JET_paramEnableAdvanced",
    "JET_paramMaxColtyp",
    "JET_paramBatchIOBufferMax",
    "JET_paramCacheSize",
    "JET_paramCacheSizeMin",
    "JET_paramCacheSizeMax",
    "JET_paramCheckpointDepthMax",
    "JET_paramLRUKCorrInterval",
    "JET_paramLRUKHistoryMax",
    "JET_paramLRUKPolicy",
    "JET_paramLRUKTimeout",
    "JET_paramLRUKTrxCorrInterval",
    "JET_paramOutstandingIOMax",
    "JET_paramStartFlushThreshold",
    "JET_paramStopFlushThreshold",
    "JET_paramEnableViewCache",
    "JET_paramCheckpointIOMax",
    "JET_paramTableClass1Name",
    "JET_paramTableClass2Name",
    "JET_paramTableClass3Name",
    "JET_paramTableClass4Name",
    "JET_paramTableClass5Name",
    "JET_paramTableClass6Name",
    "JET_paramTableClass7Name",
    "JET_paramTableClass8Name",
    "JET_paramTableClass9Name",
    "JET_paramTableClass10Name",
    "JET_paramTableClass11Name",
    "JET_paramTableClass12Name",
    "JET_paramTableClass13Name",
    "JET_paramTableClass14Name",
    "JET_paramTableClass15Name",
    "JET_paramIOPriority",
    "JET_paramRecovery",
    "JET_paramEnableOnlineDefrag",
    "JET_paramCheckFormatWhenOpenFail",
    "JET_paramEnableTempTableVersioning",
    "JET_paramIgnoreLogVersion",
    "JET_paramDeleteOldLogs",
    "JET_paramEventSourceKey",
    "JET_paramNoInformationEvent",
    "JET_paramEventLoggingLevel",
    "JET_paramDeleteOutOfRangeLogs",
    "JET_paramAccessDeniedRetryPeriod",
    "JET_paramEnableIndexChecking",
    "JET_paramEnableIndexCleanup",
    "JET_paramDatabasePageSize",
    "JET_paramDisableCallbacks",
    "JET_paramLogFileCreateAsynch",
    "JET_paramErrorToString",
    "JET_paramZeroDatabaseDuringBackup",
    "JET_paramUnicodeIndexDefault",
    "JET_paramRuntimeCallback",
    "JET_paramCleanupMismatchedLogFiles",
    "JET_paramRecordUpgradeDirtyLevel",
    "JET_paramOSSnapshotTimeout",
    "JET_paramExceptionAction",
    "JET_paramEventLogCache",
    "JET_paramCreatePathIfNotExist",
    "JET_paramPageHintCacheSize",
    "JET_paramOneDatabasePerSession",
    "JET_paramMaxInstances",
    "JET_paramDisablePerfmon",
    "JET_paramIndexTuplesLengthMin",
    "JET_paramIndexTuplesLengthMax",
    "JET_paramIndexTuplesToIndexMax",
    "JET_paramAlternateDatabaseRecoveryPath",
    "JET_paramIndexTupleIncrement",
    "JET_paramIndexTupleStart",
    "JET_paramKeyMost",
    "JET_paramLegacyFileNames",
    "JET_paramEnablePersistedCallbacks",
    "JET_paramWaypointLatency",
    "JET_paramDefragmentSequentialBTrees",
    "JET_paramDefragmentSequentialBTreesDensityCheckFrequency",
    "JET_paramIOThrottlingTimeQuanta",
    "JET_paramLVChunkSizeMost",
    "JET_paramMaxCoalesceReadSize",
    "JET_paramMaxCoalesceWriteSize",
    "JET_paramMaxCoalesceReadGapSize",
    "JET_paramMaxCoalesceWriteGapSize",
    "JET_paramEnableDBScanInRecovery",
    "JET_paramDbScanThrottle",
    "JET_paramDbScanIntervalMinSec",
    "JET_paramDbScanIntervalMaxSec",
    "JET_paramCachePriority",
    "JET_paramMaxTransactionSize",
    "JET_paramPrereadIOMax",
    "JET_paramEnableDBScanSerialization",
    "JET_paramHungIOThreshold",
    "JET_paramHungIOActions",
    "JET_paramMinDataForXpress",
    "JET_paramEnableShrinkDatabase",
    "JET_paramProcessFriendlyName",
    "JET_paramDurableCommitCallback",
    "JET_paramEnableSqm",
    "JET_paramConfigStoreSpec",
    "JET_paramUseFlushForWriteDurability",
    "JET_paramEnableRBS",
    "JET_paramRBSFilePath",
    "JET_paramMaxValueInvalid",
    "JET_sesparamCommitDefault",
    "JET_sesparamTransactionLevel",
    "JET_sesparamOperationContext",
    "JET_sesparamCorrelationID",
    "JET_sesparamMaxValueInvalid",
    "JET_bitESE98FileNames",
    "JET_bitEightDotThreeSoftCompat",
    "JET_bitHungIOEvent",
    "JET_bitShrinkDatabaseOff",
    "JET_bitShrinkDatabaseOn",
    "JET_bitShrinkDatabaseRealtime",
    "JET_bitShrinkDatabaseTrim",
    "JET_bitReplayIgnoreMissingDB",
    "JET_bitRecoveryWithoutUndo",
    "JET_bitTruncateLogsAfterRecovery",
    "JET_bitReplayMissingMapEntryDB",
    "JET_bitLogStreamMustExist",
    "JET_bitReplayIgnoreLostLogs",
    "JET_bitKeepDbAttachedAtEndOfRecovery",
    "JET_bitTermComplete",
    "JET_bitTermAbrupt",
    "JET_bitTermStopBackup",
    "JET_bitTermDirty",
    "JET_bitIdleFlushBuffers",
    "JET_bitIdleCompact",
    "JET_bitIdleStatus",
    "JET_bitDbReadOnly",
    "JET_bitDbExclusive",
    "JET_bitDbDeleteCorruptIndexes",
    "JET_bitDbDeleteUnicodeIndexes",
    "JET_bitDbUpgrade",
    "JET_bitDbEnableBackgroundMaintenance",
    "JET_bitDbPurgeCacheOnAttach",
    "JET_bitForceDetach",
    "JET_bitDbRecoveryOff",
    "JET_bitDbShadowingOff",
    "JET_bitDbOverwriteExisting",
    "JET_bitBackupIncremental",
    "JET_bitBackupAtomic",
    "JET_bitBackupSnapshot",
    "JET_bitBackupEndNormal",
    "JET_bitBackupEndAbort",
    "JET_bitBackupTruncateDone",
    "JET_bitTableCreateFixedDDL",
    "JET_bitTableCreateTemplateTable",
    "JET_bitTableCreateNoFixedVarColumnsInDerivedTables",
    "JET_bitTableCreateImmutableStructure",
    "JET_bitColumnFixed",
    "JET_bitColumnTagged",
    "JET_bitColumnNotNULL",
    "JET_bitColumnVersion",
    "JET_bitColumnAutoincrement",
    "JET_bitColumnUpdatable",
    "JET_bitColumnTTKey",
    "JET_bitColumnTTDescending",
    "JET_bitColumnMultiValued",
    "JET_bitColumnEscrowUpdate",
    "JET_bitColumnUnversioned",
    "JET_bitColumnMaybeNull",
    "JET_bitColumnFinalize",
    "JET_bitColumnUserDefinedDefault",
    "JET_bitColumnDeleteOnZero",
    "JET_bitColumnCompressed",
    "JET_bitDeleteColumnIgnoreTemplateColumns",
    "JET_bitMoveFirst",
    "JET_bitNoMove",
    "JET_bitNewKey",
    "JET_bitStrLimit",
    "JET_bitSubStrLimit",
    "JET_bitNormalizedKey",
    "JET_bitKeyDataZeroLength",
    "JET_bitFullColumnStartLimit",
    "JET_bitFullColumnEndLimit",
    "JET_bitPartialColumnStartLimit",
    "JET_bitPartialColumnEndLimit",
    "JET_bitRangeInclusive",
    "JET_bitRangeUpperLimit",
    "JET_bitRangeInstantDuration",
    "JET_bitRangeRemove",
    "JET_bitReadLock",
    "JET_bitWriteLock",
    "JET_MoveFirst",
    "JET_MovePrevious",
    "JET_MoveLast",
    "JET_bitMoveKeyNE",
    "JET_bitSeekEQ",
    "JET_bitSeekLT",
    "JET_bitSeekLE",
    "JET_bitSeekGE",
    "JET_bitSeekGT",
    "JET_bitSetIndexRange",
    "JET_bitCheckUniqueness",
    "JET_bitBookmarkPermitVirtualCurrency",
    "JET_bitIndexColumnMustBeNull",
    "JET_bitIndexColumnMustBeNonNull",
    "JET_bitRecordInIndex",
    "JET_bitRecordNotInIndex",
    "JET_bitIndexUnique",
    "JET_bitIndexPrimary",
    "JET_bitIndexDisallowNull",
    "JET_bitIndexIgnoreNull",
    "JET_bitIndexIgnoreAnyNull",
    "JET_bitIndexIgnoreFirstNull",
    "JET_bitIndexLazyFlush",
    "JET_bitIndexEmpty",
    "JET_bitIndexUnversioned",
    "JET_bitIndexSortNullsHigh",
    "JET_bitIndexUnicode",
    "JET_bitIndexTuples",
    "JET_bitIndexTupleLimits",
    "JET_bitIndexCrossProduct",
    "JET_bitIndexKeyMost",
    "JET_bitIndexDisallowTruncation",
    "JET_bitIndexNestedTable",
    "JET_bitIndexDotNetGuid",
    "JET_bitIndexImmutableStructure",
    "JET_bitKeyAscending",
    "JET_bitKeyDescending",
    "JET_bitTableDenyWrite",
    "JET_bitTableDenyRead",
    "JET_bitTableReadOnly",
    "JET_bitTableUpdatable",
    "JET_bitTablePermitDDL",
    "JET_bitTableNoCache",
    "JET_bitTablePreread",
    "JET_bitTableOpportuneRead",
    "JET_bitTableSequential",
    "JET_bitTableClassMask",
    "JET_bitTableClassNone",
    "JET_bitTableClass1",
    "JET_bitTableClass2",
    "JET_bitTableClass3",
    "JET_bitTableClass4",
    "JET_bitTableClass5",
    "JET_bitTableClass6",
    "JET_bitTableClass7",
    "JET_bitTableClass8",
    "JET_bitTableClass9",
    "JET_bitTableClass10",
    "JET_bitTableClass11",
    "JET_bitTableClass12",
    "JET_bitTableClass13",
    "JET_bitTableClass14",
    "JET_bitTableClass15",
    "JET_bitLSReset",
    "JET_bitLSCursor",
    "JET_bitLSTable",
    "JET_bitPrereadForward",
    "JET_bitPrereadBackward",
    "JET_bitPrereadFirstPage",
    "JET_bitPrereadNormalizedKey",
    "JET_bitTTIndexed",
    "JET_bitTTUnique",
    "JET_bitTTUpdatable",
    "JET_bitTTScrollable",
    "JET_bitTTSortNullsHigh",
    "JET_bitTTForceMaterialization",
    "JET_bitTTErrorOnDuplicateInsertion",
    "JET_bitTTForwardOnly",
    "JET_bitTTIntrinsicLVsOnly",
    "JET_bitTTDotNetGuid",
    "JET_bitSetAppendLV",
    "JET_bitSetOverwriteLV",
    "JET_bitSetSizeLV",
    "JET_bitSetZeroLength",
    "JET_bitSetSeparateLV",
    "JET_bitSetUniqueMultiValues",
    "JET_bitSetUniqueNormalizedMultiValues",
    "JET_bitSetRevertToDefaultValue",
    "JET_bitSetIntrinsicLV",
    "JET_bitSetUncompressed",
    "JET_bitSetCompressed",
    "JET_bitSetContiguousLV",
    "JET_bitSpaceHintsUtilizeParentSpace",
    "JET_bitCreateHintAppendSequential",
    "JET_bitCreateHintHotpointSequential",
    "JET_bitRetrieveHintReserve1",
    "JET_bitRetrieveHintTableScanForward",
    "JET_bitRetrieveHintTableScanBackward",
    "JET_bitRetrieveHintReserve2",
    "JET_bitRetrieveHintReserve3",
    "JET_bitDeleteHintTableSequential",
    "JET_prepInsert",
    "JET_prepReplace",
    "JET_prepCancel",
    "JET_prepReplaceNoLock",
    "JET_prepInsertCopy",
    "JET_prepInsertCopyDeleteOriginal",
    "JET_prepInsertCopyReplaceOriginal",
    "JET_sqmDisable",
    "JET_sqmEnable",
    "JET_sqmFromCEIP",
    "JET_bitUpdateCheckESE97Compatibility",
    "JET_bitEscrowNoRollback",
    "JET_bitRetrieveCopy",
    "JET_bitRetrieveFromIndex",
    "JET_bitRetrieveFromPrimaryBookmark",
    "JET_bitRetrieveTag",
    "JET_bitRetrieveNull",
    "JET_bitRetrieveIgnoreDefault",
    "JET_bitRetrieveTuple",
    "JET_bitZeroLength",
    "JET_bitEnumerateCopy",
    "JET_bitEnumerateIgnoreDefault",
    "JET_bitEnumeratePresenceOnly",
    "JET_bitEnumerateTaggedOnly",
    "JET_bitEnumerateCompressOutput",
    "JET_bitEnumerateIgnoreUserDefinedDefault",
    "JET_bitEnumerateInRecordOnly",
    "JET_bitRecordSizeInCopyBuffer",
    "JET_bitRecordSizeRunningTotal",
    "JET_bitRecordSizeLocal",
    "JET_bitTransactionReadOnly",
    "JET_bitCommitLazyFlush",
    "JET_bitWaitLastLevel0Commit",
    "JET_bitWaitAllLevel0Commit",
    "JET_bitForceNewLog",
    "JET_bitRollbackAll",
    "JET_bitIncrementalSnapshot",
    "JET_bitCopySnapshot",
    "JET_bitContinueAfterThaw",
    "JET_bitExplicitPrepare",
    "JET_bitAllDatabasesSnapshot",
    "JET_bitAbortSnapshot",
    "JET_DbInfoFilename",
    "JET_DbInfoConnect",
    "JET_DbInfoCountry",
    "JET_DbInfoLCID",
    "JET_DbInfoLangid",
    "JET_DbInfoCp",
    "JET_DbInfoCollate",
    "JET_DbInfoOptions",
    "JET_DbInfoTransactions",
    "JET_DbInfoVersion",
    "JET_DbInfoIsam",
    "JET_DbInfoFilesize",
    "JET_DbInfoSpaceOwned",
    "JET_DbInfoSpaceAvailable",
    "JET_DbInfoUpgrade",
    "JET_DbInfoMisc",
    "JET_DbInfoDBInUse",
    "JET_DbInfoPageSize",
    "JET_DbInfoFileType",
    "JET_DbInfoFilesizeOnDisk",
    "JET_dbstateJustCreated",
    "JET_dbstateDirtyShutdown",
    "JET_dbstateCleanShutdown",
    "JET_dbstateBeingConverted",
    "JET_dbstateForceDetach",
    "JET_filetypeUnknown",
    "JET_filetypeDatabase",
    "JET_filetypeLog",
    "JET_filetypeCheckpoint",
    "JET_filetypeTempDatabase",
    "JET_filetypeFlushMap",
    "JET_revertstateNone",
    "JET_revertstateInProgress",
    "JET_revertstateCopingLogs",
    "JET_revertstateCompleted",
    "JET_bitDeleteAllExistingLogs",
    "JET_coltypNil",
    "JET_coltypBit",
    "JET_coltypUnsignedByte",
    "JET_coltypShort",
    "JET_coltypLong",
    "JET_coltypCurrency",
    "JET_coltypIEEESingle",
    "JET_coltypIEEEDouble",
    "JET_coltypDateTime",
    "JET_coltypBinary",
    "JET_coltypText",
    "JET_coltypLongBinary",
    "JET_coltypLongText",
    "JET_coltypMax",
    "JET_coltypSLV",
    "JET_coltypUnsignedLong",
    "JET_coltypLongLong",
    "JET_coltypGUID",
    "JET_coltypUnsignedShort",
    "JET_coltypUnsignedLongLong",
    "JET_ColInfoGrbitNonDerivedColumnsOnly",
    "JET_ColInfoGrbitMinimalInfo",
    "JET_ColInfoGrbitSortByColumnid",
    "JET_objtypNil",
    "JET_objtypTable",
    "JET_bitCompactStats",
    "JET_bitCompactRepair",
    "JET_snpRepair",
    "JET_snpCompact",
    "JET_snpRestore",
    "JET_snpBackup",
    "JET_snpUpgrade",
    "JET_snpScrub",
    "JET_snpUpgradeRecordFormat",
    "JET_sntBegin",
    "JET_sntRequirements",
    "JET_sntProgress",
    "JET_sntComplete",
    "JET_sntFail",
    "JET_ExceptionMsgBox",
    "JET_ExceptionNone",
    "JET_ExceptionFailFast",
    "JET_OnlineDefragDisable",
    "JET_OnlineDefragAllOBSOLETE",
    "JET_OnlineDefragDatabases",
    "JET_OnlineDefragSpaceTrees",
    "JET_OnlineDefragAll",
    "JET_bitResizeDatabaseOnlyGrow",
    "JET_bitResizeDatabaseOnlyShrink",
    "JET_bitStopServiceAll",
    "JET_bitStopServiceBackgroundUserTasks",
    "JET_bitStopServiceQuiesceCaches",
    "JET_bitStopServiceResume",
    "JET_errSuccess",
    "JET_wrnNyi",
    "JET_errRfsFailure",
    "JET_errRfsNotArmed",
    "JET_errFileClose",
    "JET_errOutOfThreads",
    "JET_errTooManyIO",
    "JET_errTaskDropped",
    "JET_errInternalError",
    "JET_errDisabledFunctionality",
    "JET_errUnloadableOSFunctionality",
    "JET_errDatabaseBufferDependenciesCorrupted",
    "JET_wrnRemainingVersions",
    "JET_errPreviousVersion",
    "JET_errPageBoundary",
    "JET_errKeyBoundary",
    "JET_errBadPageLink",
    "JET_errBadBookmark",
    "JET_errNTSystemCallFailed",
    "JET_errBadParentPageLink",
    "JET_errSPAvailExtCacheOutOfSync",
    "JET_errSPAvailExtCorrupted",
    "JET_errSPAvailExtCacheOutOfMemory",
    "JET_errSPOwnExtCorrupted",
    "JET_errDbTimeCorrupted",
    "JET_wrnUniqueKey",
    "JET_errKeyTruncated",
    "JET_errDatabaseLeakInSpace",
    "JET_errBadEmptyPage",
    "JET_errBadLineCount",
    "JET_errPageTagCorrupted",
    "JET_errNodeCorrupted",
    "JET_wrnSeparateLongValue",
    "JET_errKeyTooBig",
    "JET_errCannotSeparateIntrinsicLV",
    "JET_errSeparatedLongValue",
    "JET_errMustBeSeparateLongValue",
    "JET_errInvalidPreread",
    "JET_errInvalidLoggedOperation",
    "JET_errLogFileCorrupt",
    "JET_errNoBackupDirectory",
    "JET_errBackupDirectoryNotEmpty",
    "JET_errBackupInProgress",
    "JET_errRestoreInProgress",
    "JET_errMissingPreviousLogFile",
    "JET_errLogWriteFail",
    "JET_errLogDisabledDueToRecoveryFailure",
    "JET_errCannotLogDuringRecoveryRedo",
    "JET_errLogGenerationMismatch",
    "JET_errBadLogVersion",
    "JET_errInvalidLogSequence",
    "JET_errLoggingDisabled",
    "JET_errLogBufferTooSmall",
    "JET_errLogSequenceEnd",
    "JET_errNoBackup",
    "JET_errInvalidBackupSequence",
    "JET_errBackupNotAllowedYet",
    "JET_errDeleteBackupFileFail",
    "JET_errMakeBackupDirectoryFail",
    "JET_errInvalidBackup",
    "JET_errRecoveredWithErrors",
    "JET_errMissingLogFile",
    "JET_errLogDiskFull",
    "JET_errBadLogSignature",
    "JET_errBadDbSignature",
    "JET_errBadCheckpointSignature",
    "JET_errCheckpointCorrupt",
    "JET_errMissingPatchPage",
    "JET_errBadPatchPage",
    "JET_errRedoAbruptEnded",
    "JET_errPatchFileMissing",
    "JET_errDatabaseLogSetMismatch",
    "JET_errDatabaseStreamingFileMismatch",
    "JET_errLogFileSizeMismatch",
    "JET_errCheckpointFileNotFound",
    "JET_errRequiredLogFilesMissing",
    "JET_errSoftRecoveryOnBackupDatabase",
    "JET_errLogFileSizeMismatchDatabasesConsistent",
    "JET_errLogSectorSizeMismatch",
    "JET_errLogSectorSizeMismatchDatabasesConsistent",
    "JET_errLogSequenceEndDatabasesConsistent",
    "JET_errStreamingDataNotLogged",
    "JET_errDatabaseDirtyShutdown",
    "JET_errDatabaseInconsistent",
    "JET_errConsistentTimeMismatch",
    "JET_errDatabasePatchFileMismatch",
    "JET_errEndingRestoreLogTooLow",
    "JET_errStartingRestoreLogTooHigh",
    "JET_errGivenLogFileHasBadSignature",
    "JET_errGivenLogFileIsNotContiguous",
    "JET_errMissingRestoreLogFiles",
    "JET_wrnExistingLogFileHasBadSignature",
    "JET_wrnExistingLogFileIsNotContiguous",
    "JET_errMissingFullBackup",
    "JET_errBadBackupDatabaseSize",
    "JET_errDatabaseAlreadyUpgraded",
    "JET_errDatabaseIncompleteUpgrade",
    "JET_wrnSkipThisRecord",
    "JET_errMissingCurrentLogFiles",
    "JET_errDbTimeTooOld",
    "JET_errDbTimeTooNew",
    "JET_errMissingFileToBackup",
    "JET_errLogTornWriteDuringHardRestore",
    "JET_errLogTornWriteDuringHardRecovery",
    "JET_errLogCorruptDuringHardRestore",
    "JET_errLogCorruptDuringHardRecovery",
    "JET_errMustDisableLoggingForDbUpgrade",
    "JET_errBadRestoreTargetInstance",
    "JET_wrnTargetInstanceRunning",
    "JET_errRecoveredWithoutUndo",
    "JET_errDatabasesNotFromSameSnapshot",
    "JET_errSoftRecoveryOnSnapshot",
    "JET_errCommittedLogFilesMissing",
    "JET_errSectorSizeNotSupported",
    "JET_errRecoveredWithoutUndoDatabasesConsistent",
    "JET_wrnCommittedLogFilesLost",
    "JET_errCommittedLogFileCorrupt",
    "JET_wrnCommittedLogFilesRemoved",
    "JET_wrnFinishWithUndo",
    "JET_errLogSequenceChecksumMismatch",
    "JET_wrnDatabaseRepaired",
    "JET_errPageInitializedMismatch",
    "JET_errUnicodeTranslationBufferTooSmall",
    "JET_errUnicodeTranslationFail",
    "JET_errUnicodeNormalizationNotSupported",
    "JET_errUnicodeLanguageValidationFailure",
    "JET_errExistingLogFileHasBadSignature",
    "JET_errExistingLogFileIsNotContiguous",
    "JET_errLogReadVerifyFailure",
    "JET_errCheckpointDepthTooDeep",
    "JET_errRestoreOfNonBackupDatabase",
    "JET_errLogFileNotCopied",
    "JET_errTransactionTooLong",
    "JET_errEngineFormatVersionNoLongerSupportedTooLow",
    "JET_errEngineFormatVersionNotYetImplementedTooHigh",
    "JET_errEngineFormatVersionParamTooLowForRequestedFeature",
    "JET_errEngineFormatVersionSpecifiedTooLowForLogVersion",
    "JET_errEngineFormatVersionSpecifiedTooLowForDatabaseVersion",
    "JET_errBackupAbortByServer",
    "JET_errInvalidGrbit",
    "JET_errTermInProgress",
    "JET_errFeatureNotAvailable",
    "JET_errInvalidName",
    "JET_errInvalidParameter",
    "JET_wrnColumnNull",
    "JET_wrnBufferTruncated",
    "JET_wrnDatabaseAttached",
    "JET_errDatabaseFileReadOnly",
    "JET_wrnSortOverflow",
    "JET_errInvalidDatabaseId",
    "JET_errOutOfMemory",
    "JET_errOutOfDatabaseSpace",
    "JET_errOutOfCursors",
    "JET_errOutOfBuffers",
    "JET_errTooManyIndexes",
    "JET_errTooManyKeys",
    "JET_errRecordDeleted",
    "JET_errReadVerifyFailure",
    "JET_errPageNotInitialized",
    "JET_errOutOfFileHandles",
    "JET_errDiskReadVerificationFailure",
    "JET_errDiskIO",
    "JET_errInvalidPath",
    "JET_errInvalidSystemPath",
    "JET_errInvalidLogDirectory",
    "JET_errRecordTooBig",
    "JET_errTooManyOpenDatabases",
    "JET_errInvalidDatabase",
    "JET_errNotInitialized",
    "JET_errAlreadyInitialized",
    "JET_errInitInProgress",
    "JET_errFileAccessDenied",
    "JET_errBufferTooSmall",
    "JET_wrnSeekNotEqual",
    "JET_errTooManyColumns",
    "JET_errContainerNotEmpty",
    "JET_errInvalidFilename",
    "JET_errInvalidBookmark",
    "JET_errColumnInUse",
    "JET_errInvalidBufferSize",
    "JET_errColumnNotUpdatable",
    "JET_errIndexInUse",
    "JET_errLinkNotSupported",
    "JET_errNullKeyDisallowed",
    "JET_errNotInTransaction",
    "JET_wrnNoErrorInfo",
    "JET_errMustRollback",
    "JET_wrnNoIdleActivity",
    "JET_errTooManyActiveUsers",
    "JET_errInvalidCountry",
    "JET_errInvalidLanguageId",
    "JET_errInvalidCodePage",
    "JET_errInvalidLCMapStringFlags",
    "JET_errVersionStoreEntryTooBig",
    "JET_errVersionStoreOutOfMemoryAndCleanupTimedOut",
    "JET_wrnNoWriteLock",
    "JET_wrnColumnSetNull",
    "JET_errVersionStoreOutOfMemory",
    "JET_errCannotIndex",
    "JET_errRecordNotDeleted",
    "JET_errTooManyMempoolEntries",
    "JET_errOutOfObjectIDs",
    "JET_errOutOfLongValueIDs",
    "JET_errOutOfAutoincrementValues",
    "JET_errOutOfDbtimeValues",
    "JET_errOutOfSequentialIndexValues",
    "JET_errRunningInOneInstanceMode",
    "JET_errRunningInMultiInstanceMode",
    "JET_errSystemParamsAlreadySet",
    "JET_errSystemPathInUse",
    "JET_errLogFilePathInUse",
    "JET_errTempPathInUse",
    "JET_errInstanceNameInUse",
    "JET_errSystemParameterConflict",
    "JET_errInstanceUnavailable",
    "JET_errDatabaseUnavailable",
    "JET_errInstanceUnavailableDueToFatalLogDiskFull",
    "JET_errInvalidSesparamId",
    "JET_errTooManyRecords",
    "JET_errInvalidDbparamId",
    "JET_errOutOfSessions",
    "JET_errWriteConflict",
    "JET_errTransTooDeep",
    "JET_errInvalidSesid",
    "JET_errWriteConflictPrimaryIndex",
    "JET_errInTransaction",
    "JET_errRollbackRequired",
    "JET_errTransReadOnly",
    "JET_errSessionWriteConflict",
    "JET_errRecordTooBigForBackwardCompatibility",
    "JET_errCannotMaterializeForwardOnlySort",
    "JET_errSesidTableIdMismatch",
    "JET_errInvalidInstance",
    "JET_errDirtyShutdown",
    "JET_errReadPgnoVerifyFailure",
    "JET_errReadLostFlushVerifyFailure",
    "JET_errFileSystemCorruption",
    "JET_wrnShrinkNotPossible",
    "JET_errRecoveryVerifyFailure",
    "JET_errFilteredMoveNotSupported",
    "JET_errDatabaseDuplicate",
    "JET_errDatabaseInUse",
    "JET_errDatabaseNotFound",
    "JET_errDatabaseInvalidName",
    "JET_errDatabaseInvalidPages",
    "JET_errDatabaseCorrupted",
    "JET_errDatabaseLocked",
    "JET_errCannotDisableVersioning",
    "JET_errInvalidDatabaseVersion",
    "JET_errDatabase200Format",
    "JET_errDatabase400Format",
    "JET_errDatabase500Format",
    "JET_errPageSizeMismatch",
    "JET_errTooManyInstances",
    "JET_errDatabaseSharingViolation",
    "JET_errAttachedDatabaseMismatch",
    "JET_errDatabaseInvalidPath",
    "JET_errDatabaseIdInUse",
    "JET_errForceDetachNotAllowed",
    "JET_errCatalogCorrupted",
    "JET_errPartiallyAttachedDB",
    "JET_errDatabaseSignInUse",
    "JET_errDatabaseCorruptedNoRepair",
    "JET_errInvalidCreateDbVersion",
    "JET_errDatabaseNotReady",
    "JET_errDatabaseAttachedForRecovery",
    "JET_errTransactionsNotReadyDuringRecovery",
    "JET_wrnTableEmpty",
    "JET_errTableLocked",
    "JET_errTableDuplicate",
    "JET_errTableInUse",
    "JET_errObjectNotFound",
    "JET_errDensityInvalid",
    "JET_errTableNotEmpty",
    "JET_errInvalidTableId",
    "JET_errTooManyOpenTables",
    "JET_errIllegalOperation",
    "JET_errTooManyOpenTablesAndCleanupTimedOut",
    "JET_errObjectDuplicate",
    "JET_errInvalidObject",
    "JET_errCannotDeleteTempTable",
    "JET_errCannotDeleteSystemTable",
    "JET_errCannotDeleteTemplateTable",
    "JET_errExclusiveTableLockRequired",
    "JET_errFixedDDL",
    "JET_errFixedInheritedDDL",
    "JET_errCannotNestDDL",
    "JET_errDDLNotInheritable",
    "JET_wrnTableInUseBySystem",
    "JET_errInvalidSettings",
    "JET_errClientRequestToStopJetService",
    "JET_errCannotAddFixedVarColumnToDerivedTable",
    "JET_errIndexCantBuild",
    "JET_errIndexHasPrimary",
    "JET_errIndexDuplicate",
    "JET_errIndexNotFound",
    "JET_errIndexMustStay",
    "JET_errIndexInvalidDef",
    "JET_errInvalidCreateIndex",
    "JET_errTooManyOpenIndexes",
    "JET_errMultiValuedIndexViolation",
    "JET_errIndexBuildCorrupted",
    "JET_errPrimaryIndexCorrupted",
    "JET_errSecondaryIndexCorrupted",
    "JET_wrnCorruptIndexDeleted",
    "JET_errInvalidIndexId",
    "JET_wrnPrimaryIndexOutOfDate",
    "JET_wrnSecondaryIndexOutOfDate",
    "JET_errIndexTuplesSecondaryIndexOnly",
    "JET_errIndexTuplesTooManyColumns",
    "JET_errIndexTuplesOneColumnOnly",
    "JET_errIndexTuplesNonUniqueOnly",
    "JET_errIndexTuplesTextBinaryColumnsOnly",
    "JET_errIndexTuplesTextColumnsOnly",
    "JET_errIndexTuplesVarSegMacNotAllowed",
    "JET_errIndexTuplesInvalidLimits",
    "JET_errIndexTuplesCannotRetrieveFromIndex",
    "JET_errIndexTuplesKeyTooSmall",
    "JET_errInvalidLVChunkSize",
    "JET_errColumnCannotBeEncrypted",
    "JET_errCannotIndexOnEncryptedColumn",
    "JET_errColumnLong",
    "JET_errColumnNoChunk",
    "JET_errColumnDoesNotFit",
    "JET_errNullInvalid",
    "JET_errColumnIndexed",
    "JET_errColumnTooBig",
    "JET_errColumnNotFound",
    "JET_errColumnDuplicate",
    "JET_errMultiValuedColumnMustBeTagged",
    "JET_errColumnRedundant",
    "JET_errInvalidColumnType",
    "JET_wrnColumnMaxTruncated",
    "JET_errTaggedNotNULL",
    "JET_errNoCurrentIndex",
    "JET_errKeyIsMade",
    "JET_errBadColumnId",
    "JET_errBadItagSequence",
    "JET_errColumnInRelationship",
    "JET_wrnCopyLongValue",
    "JET_errCannotBeTagged",
    "JET_errDefaultValueTooBig",
    "JET_errMultiValuedDuplicate",
    "JET_errLVCorrupted",
    "JET_errMultiValuedDuplicateAfterTruncation",
    "JET_errDerivedColumnCorruption",
    "JET_errInvalidPlaceholderColumn",
    "JET_wrnColumnSkipped",
    "JET_wrnColumnNotLocal",
    "JET_wrnColumnMoreTags",
    "JET_wrnColumnTruncated",
    "JET_wrnColumnPresent",
    "JET_wrnColumnSingleValue",
    "JET_wrnColumnDefault",
    "JET_errColumnCannotBeCompressed",
    "JET_wrnColumnNotInRecord",
    "JET_errColumnNoEncryptionKey",
    "JET_wrnColumnReference",
    "JET_errRecordNotFound",
    "JET_errRecordNoCopy",
    "JET_errNoCurrentRecord",
    "JET_errRecordPrimaryChanged",
    "JET_errKeyDuplicate",
    "JET_errAlreadyPrepared",
    "JET_errKeyNotMade",
    "JET_errUpdateNotPrepared",
    "JET_wrnDataHasChanged",
    "JET_errDataHasChanged",
    "JET_wrnKeyChanged",
    "JET_errLanguageNotSupported",
    "JET_errDecompressionFailed",
    "JET_errUpdateMustVersion",
    "JET_errDecryptionFailed",
    "JET_errEncryptionBadItag",
    "JET_errTooManySorts",
    "JET_errInvalidOnSort",
    "JET_errTempFileOpenError",
    "JET_errTooManyAttachedDatabases",
    "JET_errDiskFull",
    "JET_errPermissionDenied",
    "JET_errFileNotFound",
    "JET_errFileInvalidType",
    "JET_wrnFileOpenReadOnly",
    "JET_errFileAlreadyExists",
    "JET_errAfterInitialization",
    "JET_errLogCorrupted",
    "JET_errInvalidOperation",
    "JET_errAccessDenied",
    "JET_wrnIdleFull",
    "JET_errTooManySplits",
    "JET_errSessionSharingViolation",
    "JET_errEntryPointNotFound",
    "JET_errSessionContextAlreadySet",
    "JET_errSessionContextNotSetByThisThread",
    "JET_errSessionInUse",
    "JET_errRecordFormatConversionFailed",
    "JET_errOneDatabasePerSession",
    "JET_errRollbackError",
    "JET_errFlushMapVersionUnsupported",
    "JET_errFlushMapDatabaseMismatch",
    "JET_errFlushMapUnrecoverable",
    "JET_wrnDefragAlreadyRunning",
    "JET_wrnDefragNotRunning",
    "JET_errDatabaseAlreadyRunningMaintenance",
    "JET_wrnCallbackNotRegistered",
    "JET_errCallbackFailed",
    "JET_errCallbackNotResolved",
    "JET_errSpaceHintsInvalid",
    "JET_errOSSnapshotInvalidSequence",
    "JET_errOSSnapshotTimeOut",
    "JET_errOSSnapshotNotAllowed",
    "JET_errOSSnapshotInvalidSnapId",
    "JET_errLSCallbackNotSpecified",
    "JET_errLSAlreadySet",
    "JET_errLSNotSet",
    "JET_errFileIOSparse",
    "JET_errFileIOBeyondEOF",
    "JET_errFileIOAbort",
    "JET_errFileIORetry",
    "JET_errFileIOFail",
    "JET_errFileCompressed",
    "JET_BASE_NAME_LENGTH",
    "JET_bitDumpMinimum",
    "JET_bitDumpMaximum",
    "JET_bitDumpCacheMinimum",
    "JET_bitDumpCacheMaximum",
    "JET_bitDumpCacheIncludeDirtyPages",
    "JET_bitDumpCacheIncludeCachedPages",
    "JET_bitDumpCacheIncludeCorruptedPages",
    "JET_bitDumpCacheNoDecommit",
    "JET_OSSNAPID",
    "JET_LS",
    "JET_INDEXID",
    "JET_PFNSTATUS",
    "JET_RSTMAP_A",
    "JET_RSTMAP_W",
    "CONVERT_A",
    "CONVERT_W",
    "JET_CALLBACK",
    "JET_SNPROG",
    "JET_DBINFOUPGRADE",
    "JET_OBJECTINFO",
    "JET_OBJECTLIST",
    "JET_COLUMNLIST",
    "JET_COLUMNDEF",
    "JET_COLUMNBASE_A",
    "JET_COLUMNBASE_W",
    "JET_INDEXLIST",
    "JET_COLUMNCREATE_A",
    "JET_COLUMNCREATE_W",
    "JET_USERDEFINEDDEFAULT_A",
    "JET_USERDEFINEDDEFAULT_W",
    "JET_CONDITIONALCOLUMN_A",
    "JET_CONDITIONALCOLUMN_W",
    "JET_UNICODEINDEX",
    "JET_UNICODEINDEX2",
    "JET_TUPLELIMITS",
    "JET_SPACEHINTS",
    "JET_INDEXCREATE_A",
    "JET_INDEXCREATE_W",
    "JET_INDEXCREATE2_A",
    "JET_INDEXCREATE2_W",
    "JET_INDEXCREATE3_A",
    "JET_INDEXCREATE3_W",
    "JET_TABLECREATE_A",
    "JET_TABLECREATE_W",
    "JET_TABLECREATE2_A",
    "JET_TABLECREATE2_W",
    "JET_TABLECREATE3_A",
    "JET_TABLECREATE3_W",
    "JET_TABLECREATE4_A",
    "JET_TABLECREATE4_W",
    "JET_OPENTEMPORARYTABLE",
    "JET_OPENTEMPORARYTABLE2",
    "JET_RETINFO",
    "JET_SETINFO",
    "JET_RECPOS",
    "JET_RECORDLIST",
    "JET_INDEXRANGE",
    "JET_RELOP",
    "JET_relopEquals",
    "JET_relopPrefixEquals",
    "JET_relopNotEquals",
    "JET_relopLessThanOrEqual",
    "JET_relopLessThan",
    "JET_relopGreaterThanOrEqual",
    "JET_relopGreaterThan",
    "JET_relopBitmaskEqualsZero",
    "JET_relopBitmaskNotEqualsZero",
    "JET_INDEX_COLUMN",
    "JET_INDEX_RANGE",
    "JET_LOGTIME",
    "JET_BKLOGTIME",
    "JET_LGPOS",
    "JET_SIGNATURE",
    "JET_BKINFO",
    "JET_DBINFOMISC",
    "JET_DBINFOMISC2",
    "JET_DBINFOMISC3",
    "JET_DBINFOMISC4",
    "JET_THREADSTATS",
    "JET_THREADSTATS2",
    "JET_RSTINFO_A",
    "JET_RSTINFO_W",
    "JET_ERRCAT",
    "JET_errcatUnknown",
    "JET_errcatError",
    "JET_errcatOperation",
    "JET_errcatFatal",
    "JET_errcatIO",
    "JET_errcatResource",
    "JET_errcatMemory",
    "JET_errcatQuota",
    "JET_errcatDisk",
    "JET_errcatData",
    "JET_errcatCorruption",
    "JET_errcatInconsistent",
    "JET_errcatFragmentation",
    "JET_errcatApi",
    "JET_errcatUsage",
    "JET_errcatState",
    "JET_errcatObsolete",
    "JET_errcatMax",
    "JET_ERRINFOBASIC_W",
    "JET_COMMIT_ID",
    "JET_PFNDURABLECOMMITCALLBACK",
    "JET_RBSINFOMISC",
    "JET_RBSREVERTINFOMISC",
    "JET_INDEXCHECKING",
    "JET_IndexCheckingOff",
    "JET_IndexCheckingOn",
    "JET_IndexCheckingDeferToOpenTable",
    "JET_IndexCheckingMax",
    "JET_OPERATIONCONTEXT",
    "JET_SETCOLUMN",
    "JET_SETSYSPARAM_A",
    "JET_SETSYSPARAM_W",
    "JET_RETRIEVECOLUMN",
    "JET_ENUMCOLUMNID",
    "JET_ENUMCOLUMNVALUE",
    "JET_ENUMCOLUMN",
    "JET_PFNREALLOC",
    "JET_RECSIZE",
    "JET_RECSIZE2",
    "JET_LOGINFO_A",
    "JET_LOGINFO_W",
    "JET_INSTANCE_INFO_A",
    "JET_INSTANCE_INFO_W",
    "JetInit",
    "JetInit2",
    "JetInit3A",
    "JetInit3W",
    "JetInit3",
    "JetCreateInstanceA",
    "JetCreateInstanceW",
    "JetCreateInstance",
    "JetCreateInstance2A",
    "JetCreateInstance2W",
    "JetCreateInstance2",
    "JetGetInstanceMiscInfo",
    "JetTerm",
    "JetTerm2",
    "JetStopService",
    "JetStopServiceInstance",
    "JetStopServiceInstance2",
    "JetStopBackup",
    "JetStopBackupInstance",
    "JetSetSystemParameterA",
    "JetSetSystemParameterW",
    "JetSetSystemParameter",
    "JetGetSystemParameterA",
    "JetGetSystemParameterW",
    "JetGetSystemParameter",
    "JetEnableMultiInstanceA",
    "JetEnableMultiInstanceW",
    "JetEnableMultiInstance",
    "JetGetThreadStats",
    "JetBeginSessionA",
    "JetBeginSessionW",
    "JetBeginSession",
    "JetDupSession",
    "JetEndSession",
    "JetGetVersion",
    "JetIdle",
    "JetCreateDatabaseA",
    "JetCreateDatabaseW",
    "JetCreateDatabase",
    "JetCreateDatabase2A",
    "JetCreateDatabase2W",
    "JetCreateDatabase2",
    "JetAttachDatabaseA",
    "JetAttachDatabaseW",
    "JetAttachDatabase",
    "JetAttachDatabase2A",
    "JetAttachDatabase2W",
    "JetAttachDatabase2",
    "JetDetachDatabaseA",
    "JetDetachDatabaseW",
    "JetDetachDatabase",
    "JetDetachDatabase2A",
    "JetDetachDatabase2W",
    "JetDetachDatabase2",
    "JetGetObjectInfoA",
    "JetGetObjectInfoW",
    "JetGetObjectInfo",
    "JetGetTableInfoA",
    "JetGetTableInfoW",
    "JetGetTableInfo",
    "JetCreateTableA",
    "JetCreateTableW",
    "JetCreateTable",
    "JetCreateTableColumnIndexA",
    "JetCreateTableColumnIndexW",
    "JetCreateTableColumnIndex",
    "JetCreateTableColumnIndex2A",
    "JetCreateTableColumnIndex2W",
    "JetCreateTableColumnIndex2",
    "JetCreateTableColumnIndex3A",
    "JetCreateTableColumnIndex3W",
    "JetCreateTableColumnIndex3",
    "JetCreateTableColumnIndex4A",
    "JetCreateTableColumnIndex4W",
    "JetCreateTableColumnIndex4",
    "JetDeleteTableA",
    "JetDeleteTableW",
    "JetDeleteTable",
    "JetRenameTableA",
    "JetRenameTableW",
    "JetRenameTable",
    "JetGetTableColumnInfoA",
    "JetGetTableColumnInfoW",
    "JetGetTableColumnInfo",
    "JetGetColumnInfoA",
    "JetGetColumnInfoW",
    "JetGetColumnInfo",
    "JetAddColumnA",
    "JetAddColumnW",
    "JetAddColumn",
    "JetDeleteColumnA",
    "JetDeleteColumnW",
    "JetDeleteColumn",
    "JetDeleteColumn2A",
    "JetDeleteColumn2W",
    "JetDeleteColumn2",
    "JetRenameColumnA",
    "JetRenameColumnW",
    "JetRenameColumn",
    "JetSetColumnDefaultValueA",
    "JetSetColumnDefaultValueW",
    "JetSetColumnDefaultValue",
    "JetGetTableIndexInfoA",
    "JetGetTableIndexInfoW",
    "JetGetTableIndexInfo",
    "JetGetIndexInfoA",
    "JetGetIndexInfoW",
    "JetGetIndexInfo",
    "JetCreateIndexA",
    "JetCreateIndexW",
    "JetCreateIndex",
    "JetCreateIndex2A",
    "JetCreateIndex2W",
    "JetCreateIndex2",
    "JetCreateIndex3A",
    "JetCreateIndex3W",
    "JetCreateIndex3",
    "JetCreateIndex4A",
    "JetCreateIndex4W",
    "JetCreateIndex4",
    "JetDeleteIndexA",
    "JetDeleteIndexW",
    "JetDeleteIndex",
    "JetBeginTransaction",
    "JetBeginTransaction2",
    "JetBeginTransaction3",
    "JetCommitTransaction",
    "JetCommitTransaction2",
    "JetRollback",
    "JetGetDatabaseInfoA",
    "JetGetDatabaseInfoW",
    "JetGetDatabaseInfo",
    "JetGetDatabaseFileInfoA",
    "JetGetDatabaseFileInfoW",
    "JetGetDatabaseFileInfo",
    "JetOpenDatabaseA",
    "JetOpenDatabaseW",
    "JetOpenDatabase",
    "JetCloseDatabase",
    "JetOpenTableA",
    "JetOpenTableW",
    "JetOpenTable",
    "JetSetTableSequential",
    "JetResetTableSequential",
    "JetCloseTable",
    "JetDelete",
    "JetUpdate",
    "JetUpdate2",
    "JetEscrowUpdate",
    "JetRetrieveColumn",
    "JetRetrieveColumns",
    "JetEnumerateColumns",
    "JetGetRecordSize",
    "JetGetRecordSize2",
    "JetSetColumn",
    "JetSetColumns",
    "JetPrepareUpdate",
    "JetGetRecordPosition",
    "JetGotoPosition",
    "JetGetCursorInfo",
    "JetDupCursor",
    "JetGetCurrentIndexA",
    "JetGetCurrentIndexW",
    "JetGetCurrentIndex",
    "JetSetCurrentIndexA",
    "JetSetCurrentIndexW",
    "JetSetCurrentIndex",
    "JetSetCurrentIndex2A",
    "JetSetCurrentIndex2W",
    "JetSetCurrentIndex2",
    "JetSetCurrentIndex3A",
    "JetSetCurrentIndex3W",
    "JetSetCurrentIndex3",
    "JetSetCurrentIndex4A",
    "JetSetCurrentIndex4W",
    "JetSetCurrentIndex4",
    "JetMove",
    "JetSetCursorFilter",
    "JetGetLock",
    "JetMakeKey",
    "JetSeek",
    "JetPrereadKeys",
    "JetPrereadIndexRanges",
    "JetGetBookmark",
    "JetGetSecondaryIndexBookmark",
    "JetCompactA",
    "JetCompactW",
    "JetCompact",
    "JetDefragmentA",
    "JetDefragmentW",
    "JetDefragment",
    "JetDefragment2A",
    "JetDefragment2W",
    "JetDefragment2",
    "JetDefragment3A",
    "JetDefragment3W",
    "JetDefragment3",
    "JetSetDatabaseSizeA",
    "JetSetDatabaseSizeW",
    "JetSetDatabaseSize",
    "JetGrowDatabase",
    "JetResizeDatabase",
    "JetSetSessionContext",
    "JetResetSessionContext",
    "JetGotoBookmark",
    "JetGotoSecondaryIndexBookmark",
    "JetIntersectIndexes",
    "JetComputeStats",
    "JetOpenTempTable",
    "JetOpenTempTable2",
    "JetOpenTempTable3",
    "JetOpenTemporaryTable",
    "JetOpenTemporaryTable2",
    "JetBackupA",
    "JetBackupW",
    "JetBackup",
    "JetBackupInstanceA",
    "JetBackupInstanceW",
    "JetBackupInstance",
    "JetRestoreA",
    "JetRestoreW",
    "JetRestore",
    "JetRestore2A",
    "JetRestore2W",
    "JetRestore2",
    "JetRestoreInstanceA",
    "JetRestoreInstanceW",
    "JetRestoreInstance",
    "JetSetIndexRange",
    "JetIndexRecordCount",
    "JetRetrieveKey",
    "JetBeginExternalBackup",
    "JetBeginExternalBackupInstance",
    "JetGetAttachInfoA",
    "JetGetAttachInfoW",
    "JetGetAttachInfo",
    "JetGetAttachInfoInstanceA",
    "JetGetAttachInfoInstanceW",
    "JetGetAttachInfoInstance",
    "JetOpenFileA",
    "JetOpenFileW",
    "JetOpenFile",
    "JetOpenFileInstanceA",
    "JetOpenFileInstanceW",
    "JetOpenFileInstance",
    "JetReadFile",
    "JetReadFileInstance",
    "JetCloseFile",
    "JetCloseFileInstance",
    "JetGetLogInfoA",
    "JetGetLogInfoW",
    "JetGetLogInfo",
    "JetGetLogInfoInstanceA",
    "JetGetLogInfoInstanceW",
    "JetGetLogInfoInstance",
    "JetGetLogInfoInstance2A",
    "JetGetLogInfoInstance2W",
    "JetGetLogInfoInstance2",
    "JetGetTruncateLogInfoInstanceA",
    "JetGetTruncateLogInfoInstanceW",
    "JetGetTruncateLogInfoInstance",
    "JetTruncateLog",
    "JetTruncateLogInstance",
    "JetEndExternalBackup",
    "JetEndExternalBackupInstance",
    "JetEndExternalBackupInstance2",
    "JetExternalRestoreA",
    "JetExternalRestoreW",
    "JetExternalRestore",
    "JetExternalRestore2A",
    "JetExternalRestore2W",
    "JetExternalRestore2",
    "JetRegisterCallback",
    "JetUnregisterCallback",
    "JetGetInstanceInfoA",
    "JetGetInstanceInfoW",
    "JetGetInstanceInfo",
    "JetFreeBuffer",
    "JetSetLS",
    "JetGetLS",
    "JetOSSnapshotPrepare",
    "JetOSSnapshotPrepareInstance",
    "JetOSSnapshotFreezeA",
    "JetOSSnapshotFreezeW",
    "JetOSSnapshotFreeze",
    "JetOSSnapshotThaw",
    "JetOSSnapshotAbort",
    "JetOSSnapshotTruncateLog",
    "JetOSSnapshotTruncateLogInstance",
    "JetOSSnapshotGetFreezeInfoA",
    "JetOSSnapshotGetFreezeInfoW",
    "JetOSSnapshotGetFreezeInfo",
    "JetOSSnapshotEnd",
    "JetConfigureProcessForCrashDump",
    "JetGetErrorInfoW",
    "JetSetSessionParameter",
    "JetGetSessionParameter",
]
