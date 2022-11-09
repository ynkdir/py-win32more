from win32more.base import *
import win32more.Data.Xml.MsXml
import win32more.Foundation
import win32more.Storage.VirtualDiskService
import win32more.Storage.Vss
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
VSS_ASSOC_NO_MAX_SPACE = -1
VSS_ASSOC_REMOVE = 0
VSS_E_BAD_STATE = -2147212543
VSS_E_UNEXPECTED = -2147212542
VSS_E_PROVIDER_ALREADY_REGISTERED = -2147212541
VSS_E_PROVIDER_NOT_REGISTERED = -2147212540
VSS_E_PROVIDER_VETO = -2147212538
VSS_E_PROVIDER_IN_USE = -2147212537
VSS_E_OBJECT_NOT_FOUND = -2147212536
VSS_S_ASYNC_PENDING = 271113
VSS_S_ASYNC_FINISHED = 271114
VSS_S_ASYNC_CANCELLED = 271115
VSS_E_VOLUME_NOT_SUPPORTED = -2147212532
VSS_E_VOLUME_NOT_SUPPORTED_BY_PROVIDER = -2147212530
VSS_E_OBJECT_ALREADY_EXISTS = -2147212531
VSS_E_UNEXPECTED_PROVIDER_ERROR = -2147212529
VSS_E_CORRUPT_XML_DOCUMENT = -2147212528
VSS_E_INVALID_XML_DOCUMENT = -2147212527
VSS_E_MAXIMUM_NUMBER_OF_VOLUMES_REACHED = -2147212526
VSS_E_FLUSH_WRITES_TIMEOUT = -2147212525
VSS_E_HOLD_WRITES_TIMEOUT = -2147212524
VSS_E_UNEXPECTED_WRITER_ERROR = -2147212523
VSS_E_SNAPSHOT_SET_IN_PROGRESS = -2147212522
VSS_E_MAXIMUM_NUMBER_OF_SNAPSHOTS_REACHED = -2147212521
VSS_E_WRITER_INFRASTRUCTURE = -2147212520
VSS_E_WRITER_NOT_RESPONDING = -2147212519
VSS_E_WRITER_ALREADY_SUBSCRIBED = -2147212518
VSS_E_UNSUPPORTED_CONTEXT = -2147212517
VSS_E_VOLUME_IN_USE = -2147212515
VSS_E_MAXIMUM_DIFFAREA_ASSOCIATIONS_REACHED = -2147212514
VSS_E_INSUFFICIENT_STORAGE = -2147212513
VSS_E_NO_SNAPSHOTS_IMPORTED = -2147212512
VSS_S_SOME_SNAPSHOTS_NOT_IMPORTED = 271137
VSS_E_SOME_SNAPSHOTS_NOT_IMPORTED = -2147212511
VSS_E_MAXIMUM_NUMBER_OF_REMOTE_MACHINES_REACHED = -2147212510
VSS_E_REMOTE_SERVER_UNAVAILABLE = -2147212509
VSS_E_REMOTE_SERVER_UNSUPPORTED = -2147212508
VSS_E_REVERT_IN_PROGRESS = -2147212507
VSS_E_REVERT_VOLUME_LOST = -2147212506
VSS_E_REBOOT_REQUIRED = -2147212505
VSS_E_TRANSACTION_FREEZE_TIMEOUT = -2147212504
VSS_E_TRANSACTION_THAW_TIMEOUT = -2147212503
VSS_E_VOLUME_NOT_LOCAL = -2147212499
VSS_E_CLUSTER_TIMEOUT = -2147212498
VSS_E_WRITERERROR_INCONSISTENTSNAPSHOT = -2147212304
VSS_E_WRITERERROR_OUTOFRESOURCES = -2147212303
VSS_E_WRITERERROR_TIMEOUT = -2147212302
VSS_E_WRITERERROR_RETRYABLE = -2147212301
VSS_E_WRITERERROR_NONRETRYABLE = -2147212300
VSS_E_WRITERERROR_RECOVERY_FAILED = -2147212299
VSS_E_BREAK_REVERT_ID_FAILED = -2147212298
VSS_E_LEGACY_PROVIDER = -2147212297
VSS_E_MISSING_DISK = -2147212296
VSS_E_MISSING_HIDDEN_VOLUME = -2147212295
VSS_E_MISSING_VOLUME = -2147212294
VSS_E_AUTORECOVERY_FAILED = -2147212293
VSS_E_DYNAMIC_DISK_ERROR = -2147212292
VSS_E_NONTRANSPORTABLE_BCD = -2147212291
VSS_E_CANNOT_REVERT_DISKID = -2147212290
VSS_E_RESYNC_IN_PROGRESS = -2147212289
VSS_E_CLUSTER_ERROR = -2147212288
VSS_E_UNSELECTED_VOLUME = -2147212502
VSS_E_SNAPSHOT_NOT_IN_SET = -2147212501
VSS_E_NESTED_VOLUME_LIMIT = -2147212500
VSS_E_NOT_SUPPORTED = -2147212497
VSS_E_WRITERERROR_PARTIAL_FAILURE = -2147212490
VSS_E_ASRERROR_DISK_ASSIGNMENT_FAILED = -2147212287
VSS_E_ASRERROR_DISK_RECREATION_FAILED = -2147212286
VSS_E_ASRERROR_NO_ARCPATH = -2147212285
VSS_E_ASRERROR_MISSING_DYNDISK = -2147212284
VSS_E_ASRERROR_SHARED_CRIDISK = -2147212283
VSS_E_ASRERROR_DATADISK_RDISK0 = -2147212282
VSS_E_ASRERROR_RDISK0_TOOSMALL = -2147212281
VSS_E_ASRERROR_CRITICAL_DISKS_TOO_SMALL = -2147212280
VSS_E_WRITER_STATUS_NOT_AVAILABLE = -2147212279
VSS_E_ASRERROR_DYNAMIC_VHD_NOT_SUPPORTED = -2147212278
VSS_E_CRITICAL_VOLUME_ON_INVALID_DISK = -2147212271
VSS_E_ASRERROR_RDISK_FOR_SYSTEM_DISK_NOT_FOUND = -2147212270
VSS_E_ASRERROR_NO_PHYSICAL_DISK_AVAILABLE = -2147212269
VSS_E_ASRERROR_FIXED_PHYSICAL_DISK_AVAILABLE_AFTER_DISK_EXCLUSION = -2147212268
VSS_E_ASRERROR_CRITICAL_DISK_CANNOT_BE_EXCLUDED = -2147212267
VSS_E_ASRERROR_SYSTEM_PARTITION_HIDDEN = -2147212266
VSS_E_FSS_TIMEOUT = -2147212265
VSS_OBJECT_TYPE = Int32
VSS_OBJECT_UNKNOWN = 0
VSS_OBJECT_NONE = 1
VSS_OBJECT_SNAPSHOT_SET = 2
VSS_OBJECT_SNAPSHOT = 3
VSS_OBJECT_PROVIDER = 4
VSS_OBJECT_TYPE_COUNT = 5
VSS_SNAPSHOT_STATE = Int32
VSS_SS_UNKNOWN = 0
VSS_SS_PREPARING = 1
VSS_SS_PROCESSING_PREPARE = 2
VSS_SS_PREPARED = 3
VSS_SS_PROCESSING_PRECOMMIT = 4
VSS_SS_PRECOMMITTED = 5
VSS_SS_PROCESSING_COMMIT = 6
VSS_SS_COMMITTED = 7
VSS_SS_PROCESSING_POSTCOMMIT = 8
VSS_SS_PROCESSING_PREFINALCOMMIT = 9
VSS_SS_PREFINALCOMMITTED = 10
VSS_SS_PROCESSING_POSTFINALCOMMIT = 11
VSS_SS_CREATED = 12
VSS_SS_ABORTED = 13
VSS_SS_DELETED = 14
VSS_SS_POSTCOMMITTED = 15
VSS_SS_COUNT = 16
VSS_VOLUME_SNAPSHOT_ATTRIBUTES = Int32
VSS_VOLSNAP_ATTR_PERSISTENT = 1
VSS_VOLSNAP_ATTR_NO_AUTORECOVERY = 2
VSS_VOLSNAP_ATTR_CLIENT_ACCESSIBLE = 4
VSS_VOLSNAP_ATTR_NO_AUTO_RELEASE = 8
VSS_VOLSNAP_ATTR_NO_WRITERS = 16
VSS_VOLSNAP_ATTR_TRANSPORTABLE = 32
VSS_VOLSNAP_ATTR_NOT_SURFACED = 64
VSS_VOLSNAP_ATTR_NOT_TRANSACTED = 128
VSS_VOLSNAP_ATTR_HARDWARE_ASSISTED = 65536
VSS_VOLSNAP_ATTR_DIFFERENTIAL = 131072
VSS_VOLSNAP_ATTR_PLEX = 262144
VSS_VOLSNAP_ATTR_IMPORTED = 524288
VSS_VOLSNAP_ATTR_EXPOSED_LOCALLY = 1048576
VSS_VOLSNAP_ATTR_EXPOSED_REMOTELY = 2097152
VSS_VOLSNAP_ATTR_AUTORECOVER = 4194304
VSS_VOLSNAP_ATTR_ROLLBACK_RECOVERY = 8388608
VSS_VOLSNAP_ATTR_DELAYED_POSTSNAPSHOT = 16777216
VSS_VOLSNAP_ATTR_TXF_RECOVERY = 33554432
VSS_VOLSNAP_ATTR_FILE_SHARE = 67108864
VSS_SNAPSHOT_CONTEXT = Int32
VSS_CTX_BACKUP = 0
VSS_CTX_FILE_SHARE_BACKUP = 16
VSS_CTX_NAS_ROLLBACK = 25
VSS_CTX_APP_ROLLBACK = 9
VSS_CTX_CLIENT_ACCESSIBLE = 29
VSS_CTX_CLIENT_ACCESSIBLE_WRITERS = 13
VSS_CTX_ALL = -1
VSS_PROVIDER_CAPABILITIES = Int32
VSS_PRV_CAPABILITY_LEGACY = 1
VSS_PRV_CAPABILITY_COMPLIANT = 2
VSS_PRV_CAPABILITY_LUN_REPOINT = 4
VSS_PRV_CAPABILITY_LUN_RESYNC = 8
VSS_PRV_CAPABILITY_OFFLINE_CREATION = 16
VSS_PRV_CAPABILITY_MULTIPLE_IMPORT = 32
VSS_PRV_CAPABILITY_RECYCLING = 64
VSS_PRV_CAPABILITY_PLEX = 128
VSS_PRV_CAPABILITY_DIFFERENTIAL = 256
VSS_PRV_CAPABILITY_CLUSTERED = 512
VSS_HARDWARE_OPTIONS = Int32
VSS_BREAKEX_FLAG_MASK_LUNS = 1
VSS_BREAKEX_FLAG_MAKE_READ_WRITE = 2
VSS_BREAKEX_FLAG_REVERT_IDENTITY_ALL = 4
VSS_BREAKEX_FLAG_REVERT_IDENTITY_NONE = 8
VSS_ONLUNSTATECHANGE_NOTIFY_READ_WRITE = 256
VSS_ONLUNSTATECHANGE_NOTIFY_LUN_PRE_RECOVERY = 512
VSS_ONLUNSTATECHANGE_NOTIFY_LUN_POST_RECOVERY = 1024
VSS_ONLUNSTATECHANGE_DO_MASK_LUNS = 2048
VSS_RECOVERY_OPTIONS = Int32
VSS_RECOVERY_REVERT_IDENTITY_ALL = 256
VSS_RECOVERY_NO_VOLUME_CHECK = 512
VSS_WRITER_STATE = Int32
VSS_WS_UNKNOWN = 0
VSS_WS_STABLE = 1
VSS_WS_WAITING_FOR_FREEZE = 2
VSS_WS_WAITING_FOR_THAW = 3
VSS_WS_WAITING_FOR_POST_SNAPSHOT = 4
VSS_WS_WAITING_FOR_BACKUP_COMPLETE = 5
VSS_WS_FAILED_AT_IDENTIFY = 6
VSS_WS_FAILED_AT_PREPARE_BACKUP = 7
VSS_WS_FAILED_AT_PREPARE_SNAPSHOT = 8
VSS_WS_FAILED_AT_FREEZE = 9
VSS_WS_FAILED_AT_THAW = 10
VSS_WS_FAILED_AT_POST_SNAPSHOT = 11
VSS_WS_FAILED_AT_BACKUP_COMPLETE = 12
VSS_WS_FAILED_AT_PRE_RESTORE = 13
VSS_WS_FAILED_AT_POST_RESTORE = 14
VSS_WS_FAILED_AT_BACKUPSHUTDOWN = 15
VSS_WS_COUNT = 16
VSS_BACKUP_TYPE = Int32
VSS_BT_UNDEFINED = 0
VSS_BT_FULL = 1
VSS_BT_INCREMENTAL = 2
VSS_BT_DIFFERENTIAL = 3
VSS_BT_LOG = 4
VSS_BT_COPY = 5
VSS_BT_OTHER = 6
VSS_RESTORE_TYPE = Int32
VSS_RTYPE_UNDEFINED = 0
VSS_RTYPE_BY_COPY = 1
VSS_RTYPE_IMPORT = 2
VSS_RTYPE_OTHER = 3
VSS_ROLLFORWARD_TYPE = Int32
VSS_RF_UNDEFINED = 0
VSS_RF_NONE = 1
VSS_RF_ALL = 2
VSS_RF_PARTIAL = 3
VSS_PROVIDER_TYPE = Int32
VSS_PROV_UNKNOWN = 0
VSS_PROV_SYSTEM = 1
VSS_PROV_SOFTWARE = 2
VSS_PROV_HARDWARE = 3
VSS_PROV_FILESHARE = 4
VSS_APPLICATION_LEVEL = Int32
VSS_APP_UNKNOWN = 0
VSS_APP_SYSTEM = 1
VSS_APP_BACK_END = 2
VSS_APP_FRONT_END = 3
VSS_APP_SYSTEM_RM = 4
VSS_APP_AUTO = -1
VSS_SNAPSHOT_COMPATIBILITY = Int32
VSS_SC_DISABLE_DEFRAG = 1
VSS_SC_DISABLE_CONTENTINDEX = 2
VSS_SNAPSHOT_PROPERTY_ID = Int32
VSS_SPROPID_UNKNOWN = 0
VSS_SPROPID_SNAPSHOT_ID = 1
VSS_SPROPID_SNAPSHOT_SET_ID = 2
VSS_SPROPID_SNAPSHOTS_COUNT = 3
VSS_SPROPID_SNAPSHOT_DEVICE = 4
VSS_SPROPID_ORIGINAL_VOLUME = 5
VSS_SPROPID_ORIGINATING_MACHINE = 6
VSS_SPROPID_SERVICE_MACHINE = 7
VSS_SPROPID_EXPOSED_NAME = 8
VSS_SPROPID_EXPOSED_PATH = 9
VSS_SPROPID_PROVIDER_ID = 10
VSS_SPROPID_SNAPSHOT_ATTRIBUTES = 11
VSS_SPROPID_CREATION_TIMESTAMP = 12
VSS_SPROPID_STATUS = 13
VSS_FILE_SPEC_BACKUP_TYPE = Int32
VSS_FSBT_FULL_BACKUP_REQUIRED = 1
VSS_FSBT_DIFFERENTIAL_BACKUP_REQUIRED = 2
VSS_FSBT_INCREMENTAL_BACKUP_REQUIRED = 4
VSS_FSBT_LOG_BACKUP_REQUIRED = 8
VSS_FSBT_FULL_SNAPSHOT_REQUIRED = 256
VSS_FSBT_DIFFERENTIAL_SNAPSHOT_REQUIRED = 512
VSS_FSBT_INCREMENTAL_SNAPSHOT_REQUIRED = 1024
VSS_FSBT_LOG_SNAPSHOT_REQUIRED = 2048
VSS_FSBT_CREATED_DURING_BACKUP = 65536
VSS_FSBT_ALL_BACKUP_REQUIRED = 15
VSS_FSBT_ALL_SNAPSHOT_REQUIRED = 3840
VSS_BACKUP_SCHEMA = Int32
VSS_BS_UNDEFINED = 0
VSS_BS_DIFFERENTIAL = 1
VSS_BS_INCREMENTAL = 2
VSS_BS_EXCLUSIVE_INCREMENTAL_DIFFERENTIAL = 4
VSS_BS_LOG = 8
VSS_BS_COPY = 16
VSS_BS_TIMESTAMPED = 32
VSS_BS_LAST_MODIFY = 64
VSS_BS_LSN = 128
VSS_BS_WRITER_SUPPORTS_NEW_TARGET = 256
VSS_BS_WRITER_SUPPORTS_RESTORE_WITH_MOVE = 512
VSS_BS_INDEPENDENT_SYSTEM_STATE = 1024
VSS_BS_ROLLFORWARD_RESTORE = 4096
VSS_BS_RESTORE_RENAME = 8192
VSS_BS_AUTHORITATIVE_RESTORE = 16384
VSS_BS_WRITER_SUPPORTS_PARALLEL_RESTORES = 32768
def _define_VSS_SNAPSHOT_PROP_head():
    class VSS_SNAPSHOT_PROP(Structure):
        pass
    return VSS_SNAPSHOT_PROP
def _define_VSS_SNAPSHOT_PROP():
    VSS_SNAPSHOT_PROP = win32more.Storage.Vss.VSS_SNAPSHOT_PROP_head
    VSS_SNAPSHOT_PROP._fields_ = [
        ("m_SnapshotId", Guid),
        ("m_SnapshotSetId", Guid),
        ("m_lSnapshotsCount", Int32),
        ("m_pwszSnapshotDeviceObject", POINTER(UInt16)),
        ("m_pwszOriginalVolumeName", POINTER(UInt16)),
        ("m_pwszOriginatingMachine", POINTER(UInt16)),
        ("m_pwszServiceMachine", POINTER(UInt16)),
        ("m_pwszExposedName", POINTER(UInt16)),
        ("m_pwszExposedPath", POINTER(UInt16)),
        ("m_ProviderId", Guid),
        ("m_lSnapshotAttributes", Int32),
        ("m_tsCreationTimestamp", Int64),
        ("m_eStatus", win32more.Storage.Vss.VSS_SNAPSHOT_STATE),
    ]
    return VSS_SNAPSHOT_PROP
def _define_VSS_PROVIDER_PROP_head():
    class VSS_PROVIDER_PROP(Structure):
        pass
    return VSS_PROVIDER_PROP
def _define_VSS_PROVIDER_PROP():
    VSS_PROVIDER_PROP = win32more.Storage.Vss.VSS_PROVIDER_PROP_head
    VSS_PROVIDER_PROP._fields_ = [
        ("m_ProviderId", Guid),
        ("m_pwszProviderName", POINTER(UInt16)),
        ("m_eProviderType", win32more.Storage.Vss.VSS_PROVIDER_TYPE),
        ("m_pwszProviderVersion", POINTER(UInt16)),
        ("m_ProviderVersionId", Guid),
        ("m_ClassId", Guid),
    ]
    return VSS_PROVIDER_PROP
def _define_VSS_OBJECT_UNION_head():
    class VSS_OBJECT_UNION(Union):
        pass
    return VSS_OBJECT_UNION
def _define_VSS_OBJECT_UNION():
    VSS_OBJECT_UNION = win32more.Storage.Vss.VSS_OBJECT_UNION_head
    VSS_OBJECT_UNION._fields_ = [
        ("Snap", win32more.Storage.Vss.VSS_SNAPSHOT_PROP),
        ("Prov", win32more.Storage.Vss.VSS_PROVIDER_PROP),
    ]
    return VSS_OBJECT_UNION
def _define_VSS_OBJECT_PROP_head():
    class VSS_OBJECT_PROP(Structure):
        pass
    return VSS_OBJECT_PROP
def _define_VSS_OBJECT_PROP():
    VSS_OBJECT_PROP = win32more.Storage.Vss.VSS_OBJECT_PROP_head
    VSS_OBJECT_PROP._fields_ = [
        ("Type", win32more.Storage.Vss.VSS_OBJECT_TYPE),
        ("Obj", win32more.Storage.Vss.VSS_OBJECT_UNION),
    ]
    return VSS_OBJECT_PROP
def _define_IVssEnumObject_head():
    class IVssEnumObject(win32more.System.Com.IUnknown_head):
        Guid = Guid('ae1c7110-2f60-11d3-8a39-00c04f72d8e3')
    return IVssEnumObject
def _define_IVssEnumObject():
    IVssEnumObject = win32more.Storage.Vss.IVssEnumObject_head
    IVssEnumObject.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Storage.Vss.VSS_OBJECT_PROP),POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'celt'),(1, 'rgelt'),(1, 'pceltFetched'),)))
    IVssEnumObject.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'Skip', ((1, 'celt'),)))
    IVssEnumObject.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IVssEnumObject.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Vss.IVssEnumObject_head), use_last_error=False)(6, 'Clone', ((1, 'ppenum'),)))
    win32more.System.Com.IUnknown
    return IVssEnumObject
def _define_IVssAsync_head():
    class IVssAsync(win32more.System.Com.IUnknown_head):
        Guid = Guid('507c37b4-cf5b-4e95-b0af-14eb9767467e')
    return IVssAsync
def _define_IVssAsync():
    IVssAsync = win32more.Storage.Vss.IVssAsync_head
    IVssAsync.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Cancel', ()))
    IVssAsync.Wait = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'Wait', ((1, 'dwMilliseconds'),)))
    IVssAsync.QueryStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HRESULT),POINTER(Int32), use_last_error=False)(5, 'QueryStatus', ((1, 'pHrResult'),(1, 'pReserved'),)))
    win32more.System.Com.IUnknown
    return IVssAsync
VSS_USAGE_TYPE = Int32
VSS_UT_UNDEFINED = 0
VSS_UT_BOOTABLESYSTEMSTATE = 1
VSS_UT_SYSTEMSERVICE = 2
VSS_UT_USERDATA = 3
VSS_UT_OTHER = 4
VSS_SOURCE_TYPE = Int32
VSS_ST_UNDEFINED = 0
VSS_ST_TRANSACTEDDB = 1
VSS_ST_NONTRANSACTEDDB = 2
VSS_ST_OTHER = 3
VSS_RESTOREMETHOD_ENUM = Int32
VSS_RME_UNDEFINED = 0
VSS_RME_RESTORE_IF_NOT_THERE = 1
VSS_RME_RESTORE_IF_CAN_REPLACE = 2
VSS_RME_STOP_RESTORE_START = 3
VSS_RME_RESTORE_TO_ALTERNATE_LOCATION = 4
VSS_RME_RESTORE_AT_REBOOT = 5
VSS_RME_RESTORE_AT_REBOOT_IF_CANNOT_REPLACE = 6
VSS_RME_CUSTOM = 7
VSS_RME_RESTORE_STOP_START = 8
VSS_WRITERRESTORE_ENUM = Int32
VSS_WRE_UNDEFINED = 0
VSS_WRE_NEVER = 1
VSS_WRE_IF_REPLACE_FAILS = 2
VSS_WRE_ALWAYS = 3
VSS_COMPONENT_TYPE = Int32
VSS_CT_UNDEFINED = 0
VSS_CT_DATABASE = 1
VSS_CT_FILEGROUP = 2
VSS_ALTERNATE_WRITER_STATE = Int32
VSS_AWS_UNDEFINED = 0
VSS_AWS_NO_ALTERNATE_WRITER = 1
VSS_AWS_ALTERNATE_WRITER_EXISTS = 2
VSS_AWS_THIS_IS_ALTERNATE_WRITER = 3
VSS_SUBSCRIBE_MASK = Int32
VSS_SM_POST_SNAPSHOT_FLAG = 1
VSS_SM_BACKUP_EVENTS_FLAG = 2
VSS_SM_RESTORE_EVENTS_FLAG = 4
VSS_SM_IO_THROTTLING_FLAG = 8
VSS_SM_ALL_FLAGS = -1
VSS_RESTORE_TARGET = Int32
VSS_RT_UNDEFINED = 0
VSS_RT_ORIGINAL = 1
VSS_RT_ALTERNATE = 2
VSS_RT_DIRECTED = 3
VSS_RT_ORIGINAL_LOCATION = 4
VSS_FILE_RESTORE_STATUS = Int32
VSS_RS_UNDEFINED = 0
VSS_RS_NONE = 1
VSS_RS_ALL = 2
VSS_RS_FAILED = 3
VSS_COMPONENT_FLAGS = Int32
VSS_CF_BACKUP_RECOVERY = 1
VSS_CF_APP_ROLLBACK_RECOVERY = 2
VSS_CF_NOT_SYSTEM_STATE = 4
def _define_IVssExamineWriterMetadata_head():
    class IVssExamineWriterMetadata(Structure):
        pass
    return IVssExamineWriterMetadata
def _define_IVssExamineWriterMetadata():
    IVssExamineWriterMetadata = win32more.Storage.Vss.IVssExamineWriterMetadata_head
    return IVssExamineWriterMetadata
def _define_IVssWMFiledesc_head():
    class IVssWMFiledesc(win32more.System.Com.IUnknown_head):
        Guid = Guid(None)
    return IVssWMFiledesc
def _define_IVssWMFiledesc():
    IVssWMFiledesc = win32more.Storage.Vss.IVssWMFiledesc_head
    IVssWMFiledesc.GetPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(3, 'GetPath', ((1, 'pbstrPath'),)))
    IVssWMFiledesc.GetFilespec = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(4, 'GetFilespec', ((1, 'pbstrFilespec'),)))
    IVssWMFiledesc.GetRecursive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Boolean), use_last_error=False)(5, 'GetRecursive', ((1, 'pbRecursive'),)))
    IVssWMFiledesc.GetAlternateLocation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(6, 'GetAlternateLocation', ((1, 'pbstrAlternateLocation'),)))
    IVssWMFiledesc.GetBackupTypeMask = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(7, 'GetBackupTypeMask', ((1, 'pdwTypeMask'),)))
    win32more.System.Com.IUnknown
    return IVssWMFiledesc
def _define_IVssWMDependency_head():
    class IVssWMDependency(win32more.System.Com.IUnknown_head):
        Guid = Guid(None)
    return IVssWMDependency
def _define_IVssWMDependency():
    IVssWMDependency = win32more.Storage.Vss.IVssWMDependency_head
    IVssWMDependency.GetWriterId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(3, 'GetWriterId', ((1, 'pWriterId'),)))
    IVssWMDependency.GetLogicalPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(4, 'GetLogicalPath', ((1, 'pbstrLogicalPath'),)))
    IVssWMDependency.GetComponentName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(5, 'GetComponentName', ((1, 'pbstrComponentName'),)))
    win32more.System.Com.IUnknown
    return IVssWMDependency
def _define_IVssComponent_head():
    class IVssComponent(win32more.System.Com.IUnknown_head):
        Guid = Guid('d2c72c96-c121-4518-b627-e5a93d010ead')
    return IVssComponent
def _define_IVssComponent():
    IVssComponent = win32more.Storage.Vss.IVssComponent_head
    IVssComponent.GetLogicalPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(3, 'GetLogicalPath', ((1, 'pbstrPath'),)))
    IVssComponent.GetComponentType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Vss.VSS_COMPONENT_TYPE), use_last_error=False)(4, 'GetComponentType', ((1, 'pct'),)))
    IVssComponent.GetComponentName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(5, 'GetComponentName', ((1, 'pbstrName'),)))
    IVssComponent.GetBackupSucceeded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Boolean), use_last_error=False)(6, 'GetBackupSucceeded', ((1, 'pbSucceeded'),)))
    IVssComponent.GetAlternateLocationMappingCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(7, 'GetAlternateLocationMappingCount', ((1, 'pcMappings'),)))
    IVssComponent.GetAlternateLocationMapping = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Storage.Vss.IVssWMFiledesc_head), use_last_error=False)(8, 'GetAlternateLocationMapping', ((1, 'iMapping'),(1, 'ppFiledesc'),)))
    IVssComponent.SetBackupMetadata = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(9, 'SetBackupMetadata', ((1, 'wszData'),)))
    IVssComponent.GetBackupMetadata = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'GetBackupMetadata', ((1, 'pbstrData'),)))
    IVssComponent.AddPartialFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(11, 'AddPartialFile', ((1, 'wszPath'),(1, 'wszFilename'),(1, 'wszRanges'),(1, 'wszMetadata'),)))
    IVssComponent.GetPartialFileCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(12, 'GetPartialFileCount', ((1, 'pcPartialFiles'),)))
    IVssComponent.GetPartialFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.BSTR),POINTER(win32more.Foundation.BSTR),POINTER(win32more.Foundation.BSTR),POINTER(win32more.Foundation.BSTR), use_last_error=False)(13, 'GetPartialFile', ((1, 'iPartialFile'),(1, 'pbstrPath'),(1, 'pbstrFilename'),(1, 'pbstrRange'),(1, 'pbstrMetadata'),)))
    IVssComponent.IsSelectedForRestore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Boolean), use_last_error=False)(14, 'IsSelectedForRestore', ((1, 'pbSelectedForRestore'),)))
    IVssComponent.GetAdditionalRestores = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Boolean), use_last_error=False)(15, 'GetAdditionalRestores', ((1, 'pbAdditionalRestores'),)))
    IVssComponent.GetNewTargetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(16, 'GetNewTargetCount', ((1, 'pcNewTarget'),)))
    IVssComponent.GetNewTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Storage.Vss.IVssWMFiledesc_head), use_last_error=False)(17, 'GetNewTarget', ((1, 'iNewTarget'),(1, 'ppFiledesc'),)))
    IVssComponent.AddDirectedTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(18, 'AddDirectedTarget', ((1, 'wszSourcePath'),(1, 'wszSourceFilename'),(1, 'wszSourceRangeList'),(1, 'wszDestinationPath'),(1, 'wszDestinationFilename'),(1, 'wszDestinationRangeList'),)))
    IVssComponent.GetDirectedTargetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(19, 'GetDirectedTargetCount', ((1, 'pcDirectedTarget'),)))
    IVssComponent.GetDirectedTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.BSTR),POINTER(win32more.Foundation.BSTR),POINTER(win32more.Foundation.BSTR),POINTER(win32more.Foundation.BSTR),POINTER(win32more.Foundation.BSTR),POINTER(win32more.Foundation.BSTR), use_last_error=False)(20, 'GetDirectedTarget', ((1, 'iDirectedTarget'),(1, 'pbstrSourcePath'),(1, 'pbstrSourceFileName'),(1, 'pbstrSourceRangeList'),(1, 'pbstrDestinationPath'),(1, 'pbstrDestinationFilename'),(1, 'pbstrDestinationRangeList'),)))
    IVssComponent.SetRestoreMetadata = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(21, 'SetRestoreMetadata', ((1, 'wszRestoreMetadata'),)))
    IVssComponent.GetRestoreMetadata = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(22, 'GetRestoreMetadata', ((1, 'pbstrRestoreMetadata'),)))
    IVssComponent.SetRestoreTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Vss.VSS_RESTORE_TARGET, use_last_error=False)(23, 'SetRestoreTarget', ((1, 'target'),)))
    IVssComponent.GetRestoreTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Vss.VSS_RESTORE_TARGET), use_last_error=False)(24, 'GetRestoreTarget', ((1, 'pTarget'),)))
    IVssComponent.SetPreRestoreFailureMsg = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(25, 'SetPreRestoreFailureMsg', ((1, 'wszPreRestoreFailureMsg'),)))
    IVssComponent.GetPreRestoreFailureMsg = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(26, 'GetPreRestoreFailureMsg', ((1, 'pbstrPreRestoreFailureMsg'),)))
    IVssComponent.SetPostRestoreFailureMsg = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(27, 'SetPostRestoreFailureMsg', ((1, 'wszPostRestoreFailureMsg'),)))
    IVssComponent.GetPostRestoreFailureMsg = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(28, 'GetPostRestoreFailureMsg', ((1, 'pbstrPostRestoreFailureMsg'),)))
    IVssComponent.SetBackupStamp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(29, 'SetBackupStamp', ((1, 'wszBackupStamp'),)))
    IVssComponent.GetBackupStamp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(30, 'GetBackupStamp', ((1, 'pbstrBackupStamp'),)))
    IVssComponent.GetPreviousBackupStamp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(31, 'GetPreviousBackupStamp', ((1, 'pbstrBackupStamp'),)))
    IVssComponent.GetBackupOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(32, 'GetBackupOptions', ((1, 'pbstrBackupOptions'),)))
    IVssComponent.GetRestoreOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(33, 'GetRestoreOptions', ((1, 'pbstrRestoreOptions'),)))
    IVssComponent.GetRestoreSubcomponentCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(34, 'GetRestoreSubcomponentCount', ((1, 'pcRestoreSubcomponent'),)))
    IVssComponent.GetRestoreSubcomponent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.BSTR),POINTER(win32more.Foundation.BSTR),POINTER(Boolean), use_last_error=False)(35, 'GetRestoreSubcomponent', ((1, 'iComponent'),(1, 'pbstrLogicalPath'),(1, 'pbstrComponentName'),(1, 'pbRepair'),)))
    IVssComponent.GetFileRestoreStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Vss.VSS_FILE_RESTORE_STATUS), use_last_error=False)(36, 'GetFileRestoreStatus', ((1, 'pStatus'),)))
    IVssComponent.AddDifferencedFilesByLastModifyTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.BOOL,win32more.Foundation.FILETIME, use_last_error=False)(37, 'AddDifferencedFilesByLastModifyTime', ((1, 'wszPath'),(1, 'wszFilespec'),(1, 'bRecursive'),(1, 'ftLastModifyTime'),)))
    IVssComponent.AddDifferencedFilesByLastModifyLSN = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.BOOL,win32more.Foundation.BSTR, use_last_error=False)(38, 'AddDifferencedFilesByLastModifyLSN', ((1, 'wszPath'),(1, 'wszFilespec'),(1, 'bRecursive'),(1, 'bstrLsnString'),)))
    IVssComponent.GetDifferencedFilesCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(39, 'GetDifferencedFilesCount', ((1, 'pcDifferencedFiles'),)))
    IVssComponent.GetDifferencedFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.BSTR),POINTER(win32more.Foundation.BSTR),POINTER(win32more.Foundation.BOOL),POINTER(win32more.Foundation.BSTR),POINTER(win32more.Foundation.FILETIME_head), use_last_error=False)(40, 'GetDifferencedFile', ((1, 'iDifferencedFile'),(1, 'pbstrPath'),(1, 'pbstrFilespec'),(1, 'pbRecursive'),(1, 'pbstrLsnString'),(1, 'pftLastModifyTime'),)))
    win32more.System.Com.IUnknown
    return IVssComponent
def _define_IVssWriterComponents_head():
    class IVssWriterComponents(c_void_p):
        Guid = Guid(None)
    return IVssWriterComponents
def _define_IVssWriterComponents():
    IVssWriterComponents = win32more.Storage.Vss.IVssWriterComponents_head
    IVssWriterComponents.GetComponentCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(0, 'GetComponentCount', ((1, 'pcComponents'),)))
    IVssWriterComponents.GetWriterInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid), use_last_error=False)(1, 'GetWriterInfo', ((1, 'pidInstance'),(1, 'pidWriter'),)))
    IVssWriterComponents.GetComponent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Storage.Vss.IVssComponent_head), use_last_error=False)(2, 'GetComponent', ((1, 'iComponent'),(1, 'ppComponent'),)))
    return IVssWriterComponents
def _define_IVssComponentEx_head():
    class IVssComponentEx(win32more.Storage.Vss.IVssComponent_head):
        Guid = Guid('156c8b5e-f131-4bd7-9c97-d1923be7e1fa')
    return IVssComponentEx
def _define_IVssComponentEx():
    IVssComponentEx = win32more.Storage.Vss.IVssComponentEx_head
    IVssComponentEx.SetPrepareForBackupFailureMsg = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(41, 'SetPrepareForBackupFailureMsg', ((1, 'wszFailureMsg'),)))
    IVssComponentEx.SetPostSnapshotFailureMsg = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(42, 'SetPostSnapshotFailureMsg', ((1, 'wszFailureMsg'),)))
    IVssComponentEx.GetPrepareForBackupFailureMsg = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(43, 'GetPrepareForBackupFailureMsg', ((1, 'pbstrFailureMsg'),)))
    IVssComponentEx.GetPostSnapshotFailureMsg = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(44, 'GetPostSnapshotFailureMsg', ((1, 'pbstrFailureMsg'),)))
    IVssComponentEx.GetAuthoritativeRestore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Boolean), use_last_error=False)(45, 'GetAuthoritativeRestore', ((1, 'pbAuth'),)))
    IVssComponentEx.GetRollForward = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Vss.VSS_ROLLFORWARD_TYPE),POINTER(win32more.Foundation.BSTR), use_last_error=False)(46, 'GetRollForward', ((1, 'pRollType'),(1, 'pbstrPoint'),)))
    IVssComponentEx.GetRestoreName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(47, 'GetRestoreName', ((1, 'pbstrName'),)))
    win32more.Storage.Vss.IVssComponent
    return IVssComponentEx
def _define_IVssComponentEx2_head():
    class IVssComponentEx2(win32more.Storage.Vss.IVssComponentEx_head):
        Guid = Guid('3b5be0f2-07a9-4e4b-bdd3-cfdc8e2c0d2d')
    return IVssComponentEx2
def _define_IVssComponentEx2():
    IVssComponentEx2 = win32more.Storage.Vss.IVssComponentEx2_head
    IVssComponentEx2.SetFailure = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT,win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(48, 'SetFailure', ((1, 'hr'),(1, 'hrApplication'),(1, 'wszApplicationMessage'),(1, 'dwReserved'),)))
    IVssComponentEx2.GetFailure = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HRESULT),POINTER(win32more.Foundation.HRESULT),POINTER(win32more.Foundation.BSTR),POINTER(UInt32), use_last_error=False)(49, 'GetFailure', ((1, 'phr'),(1, 'phrApplication'),(1, 'pbstrApplicationMessage'),(1, 'pdwReserved'),)))
    win32more.Storage.Vss.IVssComponentEx
    return IVssComponentEx2
def _define_IVssCreateWriterMetadata_head():
    class IVssCreateWriterMetadata(c_void_p):
        Guid = Guid(None)
    return IVssCreateWriterMetadata
def _define_IVssCreateWriterMetadata():
    IVssCreateWriterMetadata = win32more.Storage.Vss.IVssCreateWriterMetadata_head
    IVssCreateWriterMetadata.AddIncludeFiles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,Byte,win32more.Foundation.PWSTR, use_last_error=False)(0, 'AddIncludeFiles', ((1, 'wszPath'),(1, 'wszFilespec'),(1, 'bRecursive'),(1, 'wszAlternateLocation'),)))
    IVssCreateWriterMetadata.AddExcludeFiles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,Byte, use_last_error=False)(1, 'AddExcludeFiles', ((1, 'wszPath'),(1, 'wszFilespec'),(1, 'bRecursive'),)))
    IVssCreateWriterMetadata.AddComponent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Vss.VSS_COMPONENT_TYPE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,c_char_p_no,UInt32,Byte,Byte,Byte,Byte,UInt32, use_last_error=False)(2, 'AddComponent', ((1, 'ct'),(1, 'wszLogicalPath'),(1, 'wszComponentName'),(1, 'wszCaption'),(1, 'pbIcon'),(1, 'cbIcon'),(1, 'bRestoreMetadata'),(1, 'bNotifyOnBackupComplete'),(1, 'bSelectable'),(1, 'bSelectableForRestore'),(1, 'dwComponentFlags'),)))
    IVssCreateWriterMetadata.AddDatabaseFiles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(3, 'AddDatabaseFiles', ((1, 'wszLogicalPath'),(1, 'wszDatabaseName'),(1, 'wszPath'),(1, 'wszFilespec'),(1, 'dwBackupTypeMask'),)))
    IVssCreateWriterMetadata.AddDatabaseLogFiles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(4, 'AddDatabaseLogFiles', ((1, 'wszLogicalPath'),(1, 'wszDatabaseName'),(1, 'wszPath'),(1, 'wszFilespec'),(1, 'dwBackupTypeMask'),)))
    IVssCreateWriterMetadata.AddFilesToFileGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,Byte,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(5, 'AddFilesToFileGroup', ((1, 'wszLogicalPath'),(1, 'wszGroupName'),(1, 'wszPath'),(1, 'wszFilespec'),(1, 'bRecursive'),(1, 'wszAlternateLocation'),(1, 'dwBackupTypeMask'),)))
    IVssCreateWriterMetadata.SetRestoreMethod = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Vss.VSS_RESTOREMETHOD_ENUM,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Storage.Vss.VSS_WRITERRESTORE_ENUM,Byte, use_last_error=False)(6, 'SetRestoreMethod', ((1, 'method'),(1, 'wszService'),(1, 'wszUserProcedure'),(1, 'writerRestore'),(1, 'bRebootRequired'),)))
    IVssCreateWriterMetadata.AddAlternateLocationMapping = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,Byte,win32more.Foundation.PWSTR, use_last_error=False)(7, 'AddAlternateLocationMapping', ((1, 'wszSourcePath'),(1, 'wszSourceFilespec'),(1, 'bRecursive'),(1, 'wszDestination'),)))
    IVssCreateWriterMetadata.AddComponentDependency = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,Guid,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(8, 'AddComponentDependency', ((1, 'wszForLogicalPath'),(1, 'wszForComponentName'),(1, 'onWriterId'),(1, 'wszOnLogicalPath'),(1, 'wszOnComponentName'),)))
    IVssCreateWriterMetadata.SetBackupSchema = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(9, 'SetBackupSchema', ((1, 'dwSchemaMask'),)))
    IVssCreateWriterMetadata.GetDocument = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Data.Xml.MsXml.IXMLDOMDocument_head), use_last_error=False)(10, 'GetDocument', ((1, 'pDoc'),)))
    IVssCreateWriterMetadata.SaveAsXML = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'SaveAsXML', ((1, 'pbstrXML'),)))
    return IVssCreateWriterMetadata
def _define_IVssWriterImpl_head():
    class IVssWriterImpl(win32more.System.Com.IUnknown_head):
        Guid = Guid(None)
    return IVssWriterImpl
def _define_IVssWriterImpl():
    IVssWriterImpl = win32more.Storage.Vss.IVssWriterImpl_head
    IVssWriterImpl.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,UInt32,win32more.Storage.Vss.VSS_USAGE_TYPE,win32more.Storage.Vss.VSS_SOURCE_TYPE,win32more.Storage.Vss.VSS_APPLICATION_LEVEL,UInt32,win32more.Storage.Vss.VSS_ALTERNATE_WRITER_STATE,Byte, use_last_error=False)(3, 'Initialize', ((1, 'writerId'),(1, 'wszWriterName'),(1, 'wszWriterInstanceName'),(1, 'dwMajorVersion'),(1, 'dwMinorVersion'),(1, 'ut'),(1, 'st'),(1, 'nLevel'),(1, 'dwTimeout'),(1, 'aws'),(1, 'bIOThrottlingOnly'),)))
    IVssWriterImpl.Subscribe = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(4, 'Subscribe', ((1, 'dwSubscribeTimeout'),(1, 'dwEventFlags'),)))
    IVssWriterImpl.Unsubscribe = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Unsubscribe', ()))
    IVssWriterImpl.Uninitialize = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(6, 'Uninitialize', ()))
    IVssWriterImpl.GetCurrentVolumeArray = COMMETHOD(WINFUNCTYPE(POINTER(win32more.Foundation.PWSTR), use_last_error=False)(7, 'GetCurrentVolumeArray', ()))
    IVssWriterImpl.GetCurrentVolumeCount = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(8, 'GetCurrentVolumeCount', ()))
    IVssWriterImpl.GetSnapshotDeviceName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(9, 'GetSnapshotDeviceName', ((1, 'wszOriginalVolume'),(1, 'ppwszSnapshotDevice'),)))
    IVssWriterImpl.GetCurrentSnapshotSetId = COMMETHOD(WINFUNCTYPE(Guid, use_last_error=False)(10, 'GetCurrentSnapshotSetId', ()))
    IVssWriterImpl.GetContext = COMMETHOD(WINFUNCTYPE(Int32, use_last_error=False)(11, 'GetContext', ()))
    IVssWriterImpl.GetCurrentLevel = COMMETHOD(WINFUNCTYPE(win32more.Storage.Vss.VSS_APPLICATION_LEVEL, use_last_error=False)(12, 'GetCurrentLevel', ()))
    IVssWriterImpl.IsPathAffected = COMMETHOD(WINFUNCTYPE(Boolean,win32more.Foundation.PWSTR, use_last_error=False)(13, 'IsPathAffected', ((1, 'wszPath'),)))
    IVssWriterImpl.IsBootableSystemStateBackedUp = COMMETHOD(WINFUNCTYPE(Boolean, use_last_error=False)(14, 'IsBootableSystemStateBackedUp', ()))
    IVssWriterImpl.AreComponentsSelected = COMMETHOD(WINFUNCTYPE(Boolean, use_last_error=False)(15, 'AreComponentsSelected', ()))
    IVssWriterImpl.GetBackupType = COMMETHOD(WINFUNCTYPE(win32more.Storage.Vss.VSS_BACKUP_TYPE, use_last_error=False)(16, 'GetBackupType', ()))
    IVssWriterImpl.GetRestoreType = COMMETHOD(WINFUNCTYPE(win32more.Storage.Vss.VSS_RESTORE_TYPE, use_last_error=False)(17, 'GetRestoreType', ()))
    IVssWriterImpl.SetWriterFailure = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT, use_last_error=False)(18, 'SetWriterFailure', ((1, 'hr'),)))
    IVssWriterImpl.IsPartialFileSupportEnabled = COMMETHOD(WINFUNCTYPE(Boolean, use_last_error=False)(19, 'IsPartialFileSupportEnabled', ()))
    IVssWriterImpl.InstallAlternateWriter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,Guid, use_last_error=False)(20, 'InstallAlternateWriter', ((1, 'idWriter'),(1, 'clsid'),)))
    IVssWriterImpl.GetIdentityInformation = COMMETHOD(WINFUNCTYPE(POINTER(win32more.Storage.Vss.IVssExamineWriterMetadata_head), use_last_error=False)(21, 'GetIdentityInformation', ()))
    IVssWriterImpl.SetWriterFailureEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT,win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(22, 'SetWriterFailureEx', ((1, 'hr'),(1, 'hrApplication'),(1, 'wszApplicationMessage'),)))
    IVssWriterImpl.GetSessionId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(23, 'GetSessionId', ((1, 'idSession'),)))
    IVssWriterImpl.IsWriterShuttingDown = COMMETHOD(WINFUNCTYPE(Boolean, use_last_error=False)(24, 'IsWriterShuttingDown', ()))
    win32more.System.Com.IUnknown
    return IVssWriterImpl
def _define_IVssCreateExpressWriterMetadata_head():
    class IVssCreateExpressWriterMetadata(win32more.System.Com.IUnknown_head):
        Guid = Guid('9c772e77-b26e-427f-92dd-c996f41ea5e3')
    return IVssCreateExpressWriterMetadata
def _define_IVssCreateExpressWriterMetadata():
    IVssCreateExpressWriterMetadata = win32more.Storage.Vss.IVssCreateExpressWriterMetadata_head
    IVssCreateExpressWriterMetadata.AddExcludeFiles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,Byte, use_last_error=False)(3, 'AddExcludeFiles', ((1, 'wszPath'),(1, 'wszFilespec'),(1, 'bRecursive'),)))
    IVssCreateExpressWriterMetadata.AddComponent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Vss.VSS_COMPONENT_TYPE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,c_char_p_no,UInt32,Byte,Byte,Byte,Byte,UInt32, use_last_error=False)(4, 'AddComponent', ((1, 'ct'),(1, 'wszLogicalPath'),(1, 'wszComponentName'),(1, 'wszCaption'),(1, 'pbIcon'),(1, 'cbIcon'),(1, 'bRestoreMetadata'),(1, 'bNotifyOnBackupComplete'),(1, 'bSelectable'),(1, 'bSelectableForRestore'),(1, 'dwComponentFlags'),)))
    IVssCreateExpressWriterMetadata.AddFilesToFileGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,Byte,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(5, 'AddFilesToFileGroup', ((1, 'wszLogicalPath'),(1, 'wszGroupName'),(1, 'wszPath'),(1, 'wszFilespec'),(1, 'bRecursive'),(1, 'wszAlternateLocation'),(1, 'dwBackupTypeMask'),)))
    IVssCreateExpressWriterMetadata.SetRestoreMethod = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Vss.VSS_RESTOREMETHOD_ENUM,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Storage.Vss.VSS_WRITERRESTORE_ENUM,Byte, use_last_error=False)(6, 'SetRestoreMethod', ((1, 'method'),(1, 'wszService'),(1, 'wszUserProcedure'),(1, 'writerRestore'),(1, 'bRebootRequired'),)))
    IVssCreateExpressWriterMetadata.AddComponentDependency = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,Guid,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(7, 'AddComponentDependency', ((1, 'wszForLogicalPath'),(1, 'wszForComponentName'),(1, 'onWriterId'),(1, 'wszOnLogicalPath'),(1, 'wszOnComponentName'),)))
    IVssCreateExpressWriterMetadata.SetBackupSchema = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(8, 'SetBackupSchema', ((1, 'dwSchemaMask'),)))
    IVssCreateExpressWriterMetadata.SaveAsXML = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'SaveAsXML', ((1, 'pbstrXML'),)))
    win32more.System.Com.IUnknown
    return IVssCreateExpressWriterMetadata
def _define_IVssExpressWriter_head():
    class IVssExpressWriter(win32more.System.Com.IUnknown_head):
        Guid = Guid('e33affdc-59c7-47b1-97d5-4266598f6235')
    return IVssExpressWriter
def _define_IVssExpressWriter():
    IVssExpressWriter = win32more.Storage.Vss.IVssExpressWriter_head
    IVssExpressWriter.CreateMetadata = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,win32more.Foundation.PWSTR,win32more.Storage.Vss.VSS_USAGE_TYPE,UInt32,UInt32,UInt32,POINTER(win32more.Storage.Vss.IVssCreateExpressWriterMetadata_head), use_last_error=False)(3, 'CreateMetadata', ((1, 'writerId'),(1, 'writerName'),(1, 'usageType'),(1, 'versionMajor'),(1, 'versionMinor'),(1, 'reserved'),(1, 'ppMetadata'),)))
    IVssExpressWriter.LoadMetadata = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(4, 'LoadMetadata', ((1, 'metadata'),(1, 'reserved'),)))
    IVssExpressWriter.Register = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Register', ()))
    IVssExpressWriter.Unregister = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid, use_last_error=False)(6, 'Unregister', ((1, 'writerId'),)))
    win32more.System.Com.IUnknown
    return IVssExpressWriter
VssSnapshotMgmt = Guid('0b5a2c52-3eb9-470a-96e2-6c6d4570e40f')
VSS_MGMT_OBJECT_TYPE = Int32
VSS_MGMT_OBJECT_UNKNOWN = 0
VSS_MGMT_OBJECT_VOLUME = 1
VSS_MGMT_OBJECT_DIFF_VOLUME = 2
VSS_MGMT_OBJECT_DIFF_AREA = 3
def _define_VSS_VOLUME_PROP_head():
    class VSS_VOLUME_PROP(Structure):
        pass
    return VSS_VOLUME_PROP
def _define_VSS_VOLUME_PROP():
    VSS_VOLUME_PROP = win32more.Storage.Vss.VSS_VOLUME_PROP_head
    VSS_VOLUME_PROP._fields_ = [
        ("m_pwszVolumeName", POINTER(UInt16)),
        ("m_pwszVolumeDisplayName", POINTER(UInt16)),
    ]
    return VSS_VOLUME_PROP
def _define_VSS_DIFF_VOLUME_PROP_head():
    class VSS_DIFF_VOLUME_PROP(Structure):
        pass
    return VSS_DIFF_VOLUME_PROP
def _define_VSS_DIFF_VOLUME_PROP():
    VSS_DIFF_VOLUME_PROP = win32more.Storage.Vss.VSS_DIFF_VOLUME_PROP_head
    VSS_DIFF_VOLUME_PROP._fields_ = [
        ("m_pwszVolumeName", POINTER(UInt16)),
        ("m_pwszVolumeDisplayName", POINTER(UInt16)),
        ("m_llVolumeFreeSpace", Int64),
        ("m_llVolumeTotalSpace", Int64),
    ]
    return VSS_DIFF_VOLUME_PROP
def _define_VSS_DIFF_AREA_PROP_head():
    class VSS_DIFF_AREA_PROP(Structure):
        pass
    return VSS_DIFF_AREA_PROP
def _define_VSS_DIFF_AREA_PROP():
    VSS_DIFF_AREA_PROP = win32more.Storage.Vss.VSS_DIFF_AREA_PROP_head
    VSS_DIFF_AREA_PROP._fields_ = [
        ("m_pwszVolumeName", POINTER(UInt16)),
        ("m_pwszDiffAreaVolumeName", POINTER(UInt16)),
        ("m_llMaximumDiffSpace", Int64),
        ("m_llAllocatedDiffSpace", Int64),
        ("m_llUsedDiffSpace", Int64),
    ]
    return VSS_DIFF_AREA_PROP
def _define_VSS_MGMT_OBJECT_UNION_head():
    class VSS_MGMT_OBJECT_UNION(Union):
        pass
    return VSS_MGMT_OBJECT_UNION
def _define_VSS_MGMT_OBJECT_UNION():
    VSS_MGMT_OBJECT_UNION = win32more.Storage.Vss.VSS_MGMT_OBJECT_UNION_head
    VSS_MGMT_OBJECT_UNION._fields_ = [
        ("Vol", win32more.Storage.Vss.VSS_VOLUME_PROP),
        ("DiffVol", win32more.Storage.Vss.VSS_DIFF_VOLUME_PROP),
        ("DiffArea", win32more.Storage.Vss.VSS_DIFF_AREA_PROP),
    ]
    return VSS_MGMT_OBJECT_UNION
def _define_VSS_MGMT_OBJECT_PROP_head():
    class VSS_MGMT_OBJECT_PROP(Structure):
        pass
    return VSS_MGMT_OBJECT_PROP
def _define_VSS_MGMT_OBJECT_PROP():
    VSS_MGMT_OBJECT_PROP = win32more.Storage.Vss.VSS_MGMT_OBJECT_PROP_head
    VSS_MGMT_OBJECT_PROP._fields_ = [
        ("Type", win32more.Storage.Vss.VSS_MGMT_OBJECT_TYPE),
        ("Obj", win32more.Storage.Vss.VSS_MGMT_OBJECT_UNION),
    ]
    return VSS_MGMT_OBJECT_PROP
VSS_PROTECTION_LEVEL = Int32
VSS_PROTECTION_LEVEL_ORIGINAL_VOLUME = 0
VSS_PROTECTION_LEVEL_SNAPSHOT = 1
VSS_PROTECTION_FAULT = Int32
VSS_PROTECTION_FAULT_NONE = 0
VSS_PROTECTION_FAULT_DIFF_AREA_MISSING = 1
VSS_PROTECTION_FAULT_IO_FAILURE_DURING_ONLINE = 2
VSS_PROTECTION_FAULT_META_DATA_CORRUPTION = 3
VSS_PROTECTION_FAULT_MEMORY_ALLOCATION_FAILURE = 4
VSS_PROTECTION_FAULT_MAPPED_MEMORY_FAILURE = 5
VSS_PROTECTION_FAULT_COW_READ_FAILURE = 6
VSS_PROTECTION_FAULT_COW_WRITE_FAILURE = 7
VSS_PROTECTION_FAULT_DIFF_AREA_FULL = 8
VSS_PROTECTION_FAULT_GROW_TOO_SLOW = 9
VSS_PROTECTION_FAULT_GROW_FAILED = 10
VSS_PROTECTION_FAULT_DESTROY_ALL_SNAPSHOTS = 11
VSS_PROTECTION_FAULT_FILE_SYSTEM_FAILURE = 12
VSS_PROTECTION_FAULT_IO_FAILURE = 13
VSS_PROTECTION_FAULT_DIFF_AREA_REMOVED = 14
VSS_PROTECTION_FAULT_EXTERNAL_WRITER_TO_DIFF_AREA = 15
VSS_PROTECTION_FAULT_MOUNT_DURING_CLUSTER_OFFLINE = 16
def _define_VSS_VOLUME_PROTECTION_INFO_head():
    class VSS_VOLUME_PROTECTION_INFO(Structure):
        pass
    return VSS_VOLUME_PROTECTION_INFO
def _define_VSS_VOLUME_PROTECTION_INFO():
    VSS_VOLUME_PROTECTION_INFO = win32more.Storage.Vss.VSS_VOLUME_PROTECTION_INFO_head
    VSS_VOLUME_PROTECTION_INFO._fields_ = [
        ("m_protectionLevel", win32more.Storage.Vss.VSS_PROTECTION_LEVEL),
        ("m_volumeIsOfflineForProtection", win32more.Foundation.BOOL),
        ("m_protectionFault", win32more.Storage.Vss.VSS_PROTECTION_FAULT),
        ("m_failureStatus", Int32),
        ("m_volumeHasUnusedDiffArea", win32more.Foundation.BOOL),
        ("m_reserved", UInt32),
    ]
    return VSS_VOLUME_PROTECTION_INFO
def _define_IVssSnapshotMgmt_head():
    class IVssSnapshotMgmt(win32more.System.Com.IUnknown_head):
        Guid = Guid('fa7df749-66e7-4986-a27f-e2f04ae53772')
    return IVssSnapshotMgmt
def _define_IVssSnapshotMgmt():
    IVssSnapshotMgmt = win32more.Storage.Vss.IVssSnapshotMgmt_head
    IVssSnapshotMgmt.GetProviderMgmtInterface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,POINTER(Guid),POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(3, 'GetProviderMgmtInterface', ((1, 'ProviderId'),(1, 'InterfaceId'),(1, 'ppItf'),)))
    IVssSnapshotMgmt.QueryVolumesSupportedForSnapshots = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,Int32,POINTER(win32more.Storage.Vss.IVssEnumMgmtObject_head), use_last_error=False)(4, 'QueryVolumesSupportedForSnapshots', ((1, 'ProviderId'),(1, 'lContext'),(1, 'ppEnum'),)))
    IVssSnapshotMgmt.QuerySnapshotsByVolume = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16),Guid,POINTER(win32more.Storage.Vss.IVssEnumObject_head), use_last_error=False)(5, 'QuerySnapshotsByVolume', ((1, 'pwszVolumeName'),(1, 'ProviderId'),(1, 'ppEnum'),)))
    win32more.System.Com.IUnknown
    return IVssSnapshotMgmt
def _define_IVssSnapshotMgmt2_head():
    class IVssSnapshotMgmt2(win32more.System.Com.IUnknown_head):
        Guid = Guid('0f61ec39-fe82-45f2-a3f0-768b5d427102')
    return IVssSnapshotMgmt2
def _define_IVssSnapshotMgmt2():
    IVssSnapshotMgmt2 = win32more.Storage.Vss.IVssSnapshotMgmt2_head
    IVssSnapshotMgmt2.GetMinDiffAreaSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int64), use_last_error=False)(3, 'GetMinDiffAreaSize', ((1, 'pllMinDiffAreaSize'),)))
    win32more.System.Com.IUnknown
    return IVssSnapshotMgmt2
def _define_IVssDifferentialSoftwareSnapshotMgmt_head():
    class IVssDifferentialSoftwareSnapshotMgmt(win32more.System.Com.IUnknown_head):
        Guid = Guid('214a0f28-b737-4026-b847-4f9e37d79529')
    return IVssDifferentialSoftwareSnapshotMgmt
def _define_IVssDifferentialSoftwareSnapshotMgmt():
    IVssDifferentialSoftwareSnapshotMgmt = win32more.Storage.Vss.IVssDifferentialSoftwareSnapshotMgmt_head
    IVssDifferentialSoftwareSnapshotMgmt.AddDiffArea = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16),POINTER(UInt16),Int64, use_last_error=False)(3, 'AddDiffArea', ((1, 'pwszVolumeName'),(1, 'pwszDiffAreaVolumeName'),(1, 'llMaximumDiffSpace'),)))
    IVssDifferentialSoftwareSnapshotMgmt.ChangeDiffAreaMaximumSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16),POINTER(UInt16),Int64, use_last_error=False)(4, 'ChangeDiffAreaMaximumSize', ((1, 'pwszVolumeName'),(1, 'pwszDiffAreaVolumeName'),(1, 'llMaximumDiffSpace'),)))
    IVssDifferentialSoftwareSnapshotMgmt.QueryVolumesSupportedForDiffAreas = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16),POINTER(win32more.Storage.Vss.IVssEnumMgmtObject_head), use_last_error=False)(5, 'QueryVolumesSupportedForDiffAreas', ((1, 'pwszOriginalVolumeName'),(1, 'ppEnum'),)))
    IVssDifferentialSoftwareSnapshotMgmt.QueryDiffAreasForVolume = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16),POINTER(win32more.Storage.Vss.IVssEnumMgmtObject_head), use_last_error=False)(6, 'QueryDiffAreasForVolume', ((1, 'pwszVolumeName'),(1, 'ppEnum'),)))
    IVssDifferentialSoftwareSnapshotMgmt.QueryDiffAreasOnVolume = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16),POINTER(win32more.Storage.Vss.IVssEnumMgmtObject_head), use_last_error=False)(7, 'QueryDiffAreasOnVolume', ((1, 'pwszVolumeName'),(1, 'ppEnum'),)))
    IVssDifferentialSoftwareSnapshotMgmt.QueryDiffAreasForSnapshot = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,POINTER(win32more.Storage.Vss.IVssEnumMgmtObject_head), use_last_error=False)(8, 'QueryDiffAreasForSnapshot', ((1, 'SnapshotId'),(1, 'ppEnum'),)))
    win32more.System.Com.IUnknown
    return IVssDifferentialSoftwareSnapshotMgmt
def _define_IVssDifferentialSoftwareSnapshotMgmt2_head():
    class IVssDifferentialSoftwareSnapshotMgmt2(win32more.Storage.Vss.IVssDifferentialSoftwareSnapshotMgmt_head):
        Guid = Guid('949d7353-675f-4275-8969-f044c6277815')
    return IVssDifferentialSoftwareSnapshotMgmt2
def _define_IVssDifferentialSoftwareSnapshotMgmt2():
    IVssDifferentialSoftwareSnapshotMgmt2 = win32more.Storage.Vss.IVssDifferentialSoftwareSnapshotMgmt2_head
    IVssDifferentialSoftwareSnapshotMgmt2.ChangeDiffAreaMaximumSizeEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16),POINTER(UInt16),Int64,win32more.Foundation.BOOL, use_last_error=False)(9, 'ChangeDiffAreaMaximumSizeEx', ((1, 'pwszVolumeName'),(1, 'pwszDiffAreaVolumeName'),(1, 'llMaximumDiffSpace'),(1, 'bVolatile'),)))
    IVssDifferentialSoftwareSnapshotMgmt2.MigrateDiffAreas = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16),POINTER(UInt16),POINTER(UInt16), use_last_error=False)(10, 'MigrateDiffAreas', ((1, 'pwszVolumeName'),(1, 'pwszDiffAreaVolumeName'),(1, 'pwszNewDiffAreaVolumeName'),)))
    IVssDifferentialSoftwareSnapshotMgmt2.QueryMigrationStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16),POINTER(UInt16),POINTER(win32more.Storage.Vss.IVssAsync_head), use_last_error=False)(11, 'QueryMigrationStatus', ((1, 'pwszVolumeName'),(1, 'pwszDiffAreaVolumeName'),(1, 'ppAsync'),)))
    IVssDifferentialSoftwareSnapshotMgmt2.SetSnapshotPriority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,Byte, use_last_error=False)(12, 'SetSnapshotPriority', ((1, 'idSnapshot'),(1, 'priority'),)))
    win32more.Storage.Vss.IVssDifferentialSoftwareSnapshotMgmt
    return IVssDifferentialSoftwareSnapshotMgmt2
def _define_IVssDifferentialSoftwareSnapshotMgmt3_head():
    class IVssDifferentialSoftwareSnapshotMgmt3(win32more.Storage.Vss.IVssDifferentialSoftwareSnapshotMgmt2_head):
        Guid = Guid('383f7e71-a4c5-401f-b27f-f826289f8458')
    return IVssDifferentialSoftwareSnapshotMgmt3
def _define_IVssDifferentialSoftwareSnapshotMgmt3():
    IVssDifferentialSoftwareSnapshotMgmt3 = win32more.Storage.Vss.IVssDifferentialSoftwareSnapshotMgmt3_head
    IVssDifferentialSoftwareSnapshotMgmt3.SetVolumeProtectLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16),win32more.Storage.Vss.VSS_PROTECTION_LEVEL, use_last_error=False)(13, 'SetVolumeProtectLevel', ((1, 'pwszVolumeName'),(1, 'protectionLevel'),)))
    IVssDifferentialSoftwareSnapshotMgmt3.GetVolumeProtectLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16),POINTER(win32more.Storage.Vss.VSS_VOLUME_PROTECTION_INFO_head), use_last_error=False)(14, 'GetVolumeProtectLevel', ((1, 'pwszVolumeName'),(1, 'protectionLevel'),)))
    IVssDifferentialSoftwareSnapshotMgmt3.ClearVolumeProtectFault = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16), use_last_error=False)(15, 'ClearVolumeProtectFault', ((1, 'pwszVolumeName'),)))
    IVssDifferentialSoftwareSnapshotMgmt3.DeleteUnusedDiffAreas = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16), use_last_error=False)(16, 'DeleteUnusedDiffAreas', ((1, 'pwszDiffAreaVolumeName'),)))
    IVssDifferentialSoftwareSnapshotMgmt3.QuerySnapshotDeltaBitmap = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,Guid,POINTER(UInt32),POINTER(UInt32),POINTER(c_char_p_no), use_last_error=False)(17, 'QuerySnapshotDeltaBitmap', ((1, 'idSnapshotOlder'),(1, 'idSnapshotYounger'),(1, 'pcBlockSizePerBit'),(1, 'pcBitmapLength'),(1, 'ppbBitmap'),)))
    win32more.Storage.Vss.IVssDifferentialSoftwareSnapshotMgmt2
    return IVssDifferentialSoftwareSnapshotMgmt3
def _define_IVssEnumMgmtObject_head():
    class IVssEnumMgmtObject(win32more.System.Com.IUnknown_head):
        Guid = Guid('01954e6b-9254-4e6e-808c-c9e05d007696')
    return IVssEnumMgmtObject
def _define_IVssEnumMgmtObject():
    IVssEnumMgmtObject = win32more.Storage.Vss.IVssEnumMgmtObject_head
    IVssEnumMgmtObject.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Storage.Vss.VSS_MGMT_OBJECT_PROP),POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'celt'),(1, 'rgelt'),(1, 'pceltFetched'),)))
    IVssEnumMgmtObject.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'Skip', ((1, 'celt'),)))
    IVssEnumMgmtObject.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IVssEnumMgmtObject.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Vss.IVssEnumMgmtObject_head), use_last_error=False)(6, 'Clone', ((1, 'ppenum'),)))
    win32more.System.Com.IUnknown
    return IVssEnumMgmtObject
VSSCoordinator = Guid('e579ab5f-1cc4-44b4-bed9-de0991ff0623')
def _define_IVssAdmin_head():
    class IVssAdmin(win32more.System.Com.IUnknown_head):
        Guid = Guid('77ed5996-2f63-11d3-8a39-00c04f72d8e3')
    return IVssAdmin
def _define_IVssAdmin():
    IVssAdmin = win32more.Storage.Vss.IVssAdmin_head
    IVssAdmin.RegisterProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,Guid,POINTER(UInt16),win32more.Storage.Vss.VSS_PROVIDER_TYPE,POINTER(UInt16),Guid, use_last_error=False)(3, 'RegisterProvider', ((1, 'pProviderId'),(1, 'ClassId'),(1, 'pwszProviderName'),(1, 'eProviderType'),(1, 'pwszProviderVersion'),(1, 'ProviderVersionId'),)))
    IVssAdmin.UnregisterProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid, use_last_error=False)(4, 'UnregisterProvider', ((1, 'ProviderId'),)))
    IVssAdmin.QueryProviders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Vss.IVssEnumObject_head), use_last_error=False)(5, 'QueryProviders', ((1, 'ppEnum'),)))
    IVssAdmin.AbortAllSnapshotsInProgress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'AbortAllSnapshotsInProgress', ()))
    win32more.System.Com.IUnknown
    return IVssAdmin
def _define_IVssAdminEx_head():
    class IVssAdminEx(win32more.Storage.Vss.IVssAdmin_head):
        Guid = Guid('7858a9f8-b1fa-41a6-964f-b9b36b8cd8d8')
    return IVssAdminEx
def _define_IVssAdminEx():
    IVssAdminEx = win32more.Storage.Vss.IVssAdminEx_head
    IVssAdminEx.GetProviderCapability = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,POINTER(UInt64), use_last_error=False)(7, 'GetProviderCapability', ((1, 'pProviderId'),(1, 'pllOriginalCapabilityMask'),)))
    IVssAdminEx.GetProviderContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,POINTER(Int32), use_last_error=False)(8, 'GetProviderContext', ((1, 'ProviderId'),(1, 'plContext'),)))
    IVssAdminEx.SetProviderContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,Int32, use_last_error=False)(9, 'SetProviderContext', ((1, 'ProviderId'),(1, 'lContext'),)))
    win32more.Storage.Vss.IVssAdmin
    return IVssAdminEx
def _define_IVssSoftwareSnapshotProvider_head():
    class IVssSoftwareSnapshotProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('609e123e-2c5a-44d3-8f01-0b1d9a47d1ff')
    return IVssSoftwareSnapshotProvider
def _define_IVssSoftwareSnapshotProvider():
    IVssSoftwareSnapshotProvider = win32more.Storage.Vss.IVssSoftwareSnapshotProvider_head
    IVssSoftwareSnapshotProvider.SetContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(3, 'SetContext', ((1, 'lContext'),)))
    IVssSoftwareSnapshotProvider.GetSnapshotProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,POINTER(win32more.Storage.Vss.VSS_SNAPSHOT_PROP_head), use_last_error=False)(4, 'GetSnapshotProperties', ((1, 'SnapshotId'),(1, 'pProp'),)))
    IVssSoftwareSnapshotProvider.Query = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,win32more.Storage.Vss.VSS_OBJECT_TYPE,win32more.Storage.Vss.VSS_OBJECT_TYPE,POINTER(win32more.Storage.Vss.IVssEnumObject_head), use_last_error=False)(5, 'Query', ((1, 'QueriedObjectId'),(1, 'eQueriedObjectType'),(1, 'eReturnedObjectsType'),(1, 'ppEnum'),)))
    IVssSoftwareSnapshotProvider.DeleteSnapshots = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,win32more.Storage.Vss.VSS_OBJECT_TYPE,win32more.Foundation.BOOL,POINTER(Int32),POINTER(Guid), use_last_error=False)(6, 'DeleteSnapshots', ((1, 'SourceObjectId'),(1, 'eSourceObjectType'),(1, 'bForceDelete'),(1, 'plDeletedSnapshots'),(1, 'pNondeletedSnapshotID'),)))
    IVssSoftwareSnapshotProvider.BeginPrepareSnapshot = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,Guid,POINTER(UInt16),Int32, use_last_error=False)(7, 'BeginPrepareSnapshot', ((1, 'SnapshotSetId'),(1, 'SnapshotId'),(1, 'pwszVolumeName'),(1, 'lNewContext'),)))
    IVssSoftwareSnapshotProvider.IsVolumeSupported = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16),POINTER(win32more.Foundation.BOOL), use_last_error=False)(8, 'IsVolumeSupported', ((1, 'pwszVolumeName'),(1, 'pbSupportedByThisProvider'),)))
    IVssSoftwareSnapshotProvider.IsVolumeSnapshotted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16),POINTER(win32more.Foundation.BOOL),POINTER(Int32), use_last_error=False)(9, 'IsVolumeSnapshotted', ((1, 'pwszVolumeName'),(1, 'pbSnapshotsPresent'),(1, 'plSnapshotCompatibility'),)))
    IVssSoftwareSnapshotProvider.SetSnapshotProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,win32more.Storage.Vss.VSS_SNAPSHOT_PROPERTY_ID,win32more.System.Com.VARIANT, use_last_error=False)(10, 'SetSnapshotProperty', ((1, 'SnapshotId'),(1, 'eSnapshotPropertyId'),(1, 'vProperty'),)))
    IVssSoftwareSnapshotProvider.RevertToSnapshot = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid, use_last_error=False)(11, 'RevertToSnapshot', ((1, 'SnapshotId'),)))
    IVssSoftwareSnapshotProvider.QueryRevertStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16),POINTER(win32more.Storage.Vss.IVssAsync_head), use_last_error=False)(12, 'QueryRevertStatus', ((1, 'pwszVolume'),(1, 'ppAsync'),)))
    win32more.System.Com.IUnknown
    return IVssSoftwareSnapshotProvider
def _define_IVssProviderCreateSnapshotSet_head():
    class IVssProviderCreateSnapshotSet(win32more.System.Com.IUnknown_head):
        Guid = Guid('5f894e5b-1e39-4778-8e23-9abad9f0e08c')
    return IVssProviderCreateSnapshotSet
def _define_IVssProviderCreateSnapshotSet():
    IVssProviderCreateSnapshotSet = win32more.Storage.Vss.IVssProviderCreateSnapshotSet_head
    IVssProviderCreateSnapshotSet.EndPrepareSnapshots = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid, use_last_error=False)(3, 'EndPrepareSnapshots', ((1, 'SnapshotSetId'),)))
    IVssProviderCreateSnapshotSet.PreCommitSnapshots = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid, use_last_error=False)(4, 'PreCommitSnapshots', ((1, 'SnapshotSetId'),)))
    IVssProviderCreateSnapshotSet.CommitSnapshots = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid, use_last_error=False)(5, 'CommitSnapshots', ((1, 'SnapshotSetId'),)))
    IVssProviderCreateSnapshotSet.PostCommitSnapshots = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,Int32, use_last_error=False)(6, 'PostCommitSnapshots', ((1, 'SnapshotSetId'),(1, 'lSnapshotsCount'),)))
    IVssProviderCreateSnapshotSet.PreFinalCommitSnapshots = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid, use_last_error=False)(7, 'PreFinalCommitSnapshots', ((1, 'SnapshotSetId'),)))
    IVssProviderCreateSnapshotSet.PostFinalCommitSnapshots = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid, use_last_error=False)(8, 'PostFinalCommitSnapshots', ((1, 'SnapshotSetId'),)))
    IVssProviderCreateSnapshotSet.AbortSnapshots = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid, use_last_error=False)(9, 'AbortSnapshots', ((1, 'SnapshotSetId'),)))
    win32more.System.Com.IUnknown
    return IVssProviderCreateSnapshotSet
def _define_IVssProviderNotifications_head():
    class IVssProviderNotifications(win32more.System.Com.IUnknown_head):
        Guid = Guid('e561901f-03a5-4afe-86d0-72baeece7004')
    return IVssProviderNotifications
def _define_IVssProviderNotifications():
    IVssProviderNotifications = win32more.Storage.Vss.IVssProviderNotifications_head
    IVssProviderNotifications.OnLoad = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(3, 'OnLoad', ((1, 'pCallback'),)))
    IVssProviderNotifications.OnUnload = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(4, 'OnUnload', ((1, 'bForceUnload'),)))
    win32more.System.Com.IUnknown
    return IVssProviderNotifications
def _define_IVssHardwareSnapshotProvider_head():
    class IVssHardwareSnapshotProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('9593a157-44e9-4344-bbeb-44fbf9b06b10')
    return IVssHardwareSnapshotProvider
def _define_IVssHardwareSnapshotProvider():
    IVssHardwareSnapshotProvider = win32more.Storage.Vss.IVssHardwareSnapshotProvider_head
    IVssHardwareSnapshotProvider.AreLunsSupported = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(POINTER(UInt16)),POINTER(win32more.Storage.VirtualDiskService.VDS_LUN_INFORMATION),POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'AreLunsSupported', ((1, 'lLunCount'),(1, 'lContext'),(1, 'rgwszDevices'),(1, 'pLunInformation'),(1, 'pbIsSupported'),)))
    IVssHardwareSnapshotProvider.FillInLunInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16),POINTER(win32more.Storage.VirtualDiskService.VDS_LUN_INFORMATION_head),POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'FillInLunInfo', ((1, 'wszDeviceName'),(1, 'pLunInfo'),(1, 'pbIsSupported'),)))
    IVssHardwareSnapshotProvider.BeginPrepareSnapshot = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,Guid,Int32,Int32,POINTER(POINTER(UInt16)),POINTER(win32more.Storage.VirtualDiskService.VDS_LUN_INFORMATION), use_last_error=False)(5, 'BeginPrepareSnapshot', ((1, 'SnapshotSetId'),(1, 'SnapshotId'),(1, 'lContext'),(1, 'lLunCount'),(1, 'rgDeviceNames'),(1, 'rgLunInformation'),)))
    IVssHardwareSnapshotProvider.GetTargetLuns = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(POINTER(UInt16)),POINTER(win32more.Storage.VirtualDiskService.VDS_LUN_INFORMATION),POINTER(win32more.Storage.VirtualDiskService.VDS_LUN_INFORMATION), use_last_error=False)(6, 'GetTargetLuns', ((1, 'lLunCount'),(1, 'rgDeviceNames'),(1, 'rgSourceLuns'),(1, 'rgDestinationLuns'),)))
    IVssHardwareSnapshotProvider.LocateLuns = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Storage.VirtualDiskService.VDS_LUN_INFORMATION), use_last_error=False)(7, 'LocateLuns', ((1, 'lLunCount'),(1, 'rgSourceLuns'),)))
    IVssHardwareSnapshotProvider.OnLunEmpty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16),POINTER(win32more.Storage.VirtualDiskService.VDS_LUN_INFORMATION_head), use_last_error=False)(8, 'OnLunEmpty', ((1, 'wszDeviceName'),(1, 'pInformation'),)))
    win32more.System.Com.IUnknown
    return IVssHardwareSnapshotProvider
def _define_IVssHardwareSnapshotProviderEx_head():
    class IVssHardwareSnapshotProviderEx(win32more.Storage.Vss.IVssHardwareSnapshotProvider_head):
        Guid = Guid('7f5ba925-cdb1-4d11-a71f-339eb7e709fd')
    return IVssHardwareSnapshotProviderEx
def _define_IVssHardwareSnapshotProviderEx():
    IVssHardwareSnapshotProviderEx = win32more.Storage.Vss.IVssHardwareSnapshotProviderEx_head
    IVssHardwareSnapshotProviderEx.GetProviderCapabilities = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64), use_last_error=False)(9, 'GetProviderCapabilities', ((1, 'pllOriginalCapabilityMask'),)))
    IVssHardwareSnapshotProviderEx.OnLunStateChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.VDS_LUN_INFORMATION),POINTER(win32more.Storage.VirtualDiskService.VDS_LUN_INFORMATION),UInt32,UInt32, use_last_error=False)(10, 'OnLunStateChange', ((1, 'pSnapshotLuns'),(1, 'pOriginalLuns'),(1, 'dwCount'),(1, 'dwFlags'),)))
    IVssHardwareSnapshotProviderEx.ResyncLuns = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.VDS_LUN_INFORMATION),POINTER(win32more.Storage.VirtualDiskService.VDS_LUN_INFORMATION),UInt32,POINTER(win32more.Storage.Vss.IVssAsync_head), use_last_error=False)(11, 'ResyncLuns', ((1, 'pSourceLuns'),(1, 'pTargetLuns'),(1, 'dwCount'),(1, 'ppAsync'),)))
    IVssHardwareSnapshotProviderEx.OnReuseLuns = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.VDS_LUN_INFORMATION),POINTER(win32more.Storage.VirtualDiskService.VDS_LUN_INFORMATION),UInt32, use_last_error=False)(12, 'OnReuseLuns', ((1, 'pSnapshotLuns'),(1, 'pOriginalLuns'),(1, 'dwCount'),)))
    win32more.Storage.Vss.IVssHardwareSnapshotProvider
    return IVssHardwareSnapshotProviderEx
def _define_IVssFileShareSnapshotProvider_head():
    class IVssFileShareSnapshotProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('c8636060-7c2e-11df-8c4a-0800200c9a66')
    return IVssFileShareSnapshotProvider
def _define_IVssFileShareSnapshotProvider():
    IVssFileShareSnapshotProvider = win32more.Storage.Vss.IVssFileShareSnapshotProvider_head
    IVssFileShareSnapshotProvider.SetContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(3, 'SetContext', ((1, 'lContext'),)))
    IVssFileShareSnapshotProvider.GetSnapshotProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,POINTER(win32more.Storage.Vss.VSS_SNAPSHOT_PROP_head), use_last_error=False)(4, 'GetSnapshotProperties', ((1, 'SnapshotId'),(1, 'pProp'),)))
    IVssFileShareSnapshotProvider.Query = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,win32more.Storage.Vss.VSS_OBJECT_TYPE,win32more.Storage.Vss.VSS_OBJECT_TYPE,POINTER(win32more.Storage.Vss.IVssEnumObject_head), use_last_error=False)(5, 'Query', ((1, 'QueriedObjectId'),(1, 'eQueriedObjectType'),(1, 'eReturnedObjectsType'),(1, 'ppEnum'),)))
    IVssFileShareSnapshotProvider.DeleteSnapshots = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,win32more.Storage.Vss.VSS_OBJECT_TYPE,win32more.Foundation.BOOL,POINTER(Int32),POINTER(Guid), use_last_error=False)(6, 'DeleteSnapshots', ((1, 'SourceObjectId'),(1, 'eSourceObjectType'),(1, 'bForceDelete'),(1, 'plDeletedSnapshots'),(1, 'pNondeletedSnapshotID'),)))
    IVssFileShareSnapshotProvider.BeginPrepareSnapshot = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,Guid,POINTER(UInt16),Int32,Guid, use_last_error=False)(7, 'BeginPrepareSnapshot', ((1, 'SnapshotSetId'),(1, 'SnapshotId'),(1, 'pwszSharePath'),(1, 'lNewContext'),(1, 'ProviderId'),)))
    IVssFileShareSnapshotProvider.IsPathSupported = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16),POINTER(win32more.Foundation.BOOL), use_last_error=False)(8, 'IsPathSupported', ((1, 'pwszSharePath'),(1, 'pbSupportedByThisProvider'),)))
    IVssFileShareSnapshotProvider.IsPathSnapshotted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16),POINTER(win32more.Foundation.BOOL),POINTER(Int32), use_last_error=False)(9, 'IsPathSnapshotted', ((1, 'pwszSharePath'),(1, 'pbSnapshotsPresent'),(1, 'plSnapshotCompatibility'),)))
    IVssFileShareSnapshotProvider.SetSnapshotProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,win32more.Storage.Vss.VSS_SNAPSHOT_PROPERTY_ID,win32more.System.Com.VARIANT, use_last_error=False)(10, 'SetSnapshotProperty', ((1, 'SnapshotId'),(1, 'eSnapshotPropertyId'),(1, 'vProperty'),)))
    win32more.System.Com.IUnknown
    return IVssFileShareSnapshotProvider
def _define_CreateVssExpressWriterInternal():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Vss.IVssExpressWriter_head), use_last_error=False)(("CreateVssExpressWriterInternal", windll["VSSAPI"]), ((1, 'ppWriter'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "VSS_ASSOC_NO_MAX_SPACE",
    "VSS_ASSOC_REMOVE",
    "VSS_E_BAD_STATE",
    "VSS_E_UNEXPECTED",
    "VSS_E_PROVIDER_ALREADY_REGISTERED",
    "VSS_E_PROVIDER_NOT_REGISTERED",
    "VSS_E_PROVIDER_VETO",
    "VSS_E_PROVIDER_IN_USE",
    "VSS_E_OBJECT_NOT_FOUND",
    "VSS_S_ASYNC_PENDING",
    "VSS_S_ASYNC_FINISHED",
    "VSS_S_ASYNC_CANCELLED",
    "VSS_E_VOLUME_NOT_SUPPORTED",
    "VSS_E_VOLUME_NOT_SUPPORTED_BY_PROVIDER",
    "VSS_E_OBJECT_ALREADY_EXISTS",
    "VSS_E_UNEXPECTED_PROVIDER_ERROR",
    "VSS_E_CORRUPT_XML_DOCUMENT",
    "VSS_E_INVALID_XML_DOCUMENT",
    "VSS_E_MAXIMUM_NUMBER_OF_VOLUMES_REACHED",
    "VSS_E_FLUSH_WRITES_TIMEOUT",
    "VSS_E_HOLD_WRITES_TIMEOUT",
    "VSS_E_UNEXPECTED_WRITER_ERROR",
    "VSS_E_SNAPSHOT_SET_IN_PROGRESS",
    "VSS_E_MAXIMUM_NUMBER_OF_SNAPSHOTS_REACHED",
    "VSS_E_WRITER_INFRASTRUCTURE",
    "VSS_E_WRITER_NOT_RESPONDING",
    "VSS_E_WRITER_ALREADY_SUBSCRIBED",
    "VSS_E_UNSUPPORTED_CONTEXT",
    "VSS_E_VOLUME_IN_USE",
    "VSS_E_MAXIMUM_DIFFAREA_ASSOCIATIONS_REACHED",
    "VSS_E_INSUFFICIENT_STORAGE",
    "VSS_E_NO_SNAPSHOTS_IMPORTED",
    "VSS_S_SOME_SNAPSHOTS_NOT_IMPORTED",
    "VSS_E_SOME_SNAPSHOTS_NOT_IMPORTED",
    "VSS_E_MAXIMUM_NUMBER_OF_REMOTE_MACHINES_REACHED",
    "VSS_E_REMOTE_SERVER_UNAVAILABLE",
    "VSS_E_REMOTE_SERVER_UNSUPPORTED",
    "VSS_E_REVERT_IN_PROGRESS",
    "VSS_E_REVERT_VOLUME_LOST",
    "VSS_E_REBOOT_REQUIRED",
    "VSS_E_TRANSACTION_FREEZE_TIMEOUT",
    "VSS_E_TRANSACTION_THAW_TIMEOUT",
    "VSS_E_VOLUME_NOT_LOCAL",
    "VSS_E_CLUSTER_TIMEOUT",
    "VSS_E_WRITERERROR_INCONSISTENTSNAPSHOT",
    "VSS_E_WRITERERROR_OUTOFRESOURCES",
    "VSS_E_WRITERERROR_TIMEOUT",
    "VSS_E_WRITERERROR_RETRYABLE",
    "VSS_E_WRITERERROR_NONRETRYABLE",
    "VSS_E_WRITERERROR_RECOVERY_FAILED",
    "VSS_E_BREAK_REVERT_ID_FAILED",
    "VSS_E_LEGACY_PROVIDER",
    "VSS_E_MISSING_DISK",
    "VSS_E_MISSING_HIDDEN_VOLUME",
    "VSS_E_MISSING_VOLUME",
    "VSS_E_AUTORECOVERY_FAILED",
    "VSS_E_DYNAMIC_DISK_ERROR",
    "VSS_E_NONTRANSPORTABLE_BCD",
    "VSS_E_CANNOT_REVERT_DISKID",
    "VSS_E_RESYNC_IN_PROGRESS",
    "VSS_E_CLUSTER_ERROR",
    "VSS_E_UNSELECTED_VOLUME",
    "VSS_E_SNAPSHOT_NOT_IN_SET",
    "VSS_E_NESTED_VOLUME_LIMIT",
    "VSS_E_NOT_SUPPORTED",
    "VSS_E_WRITERERROR_PARTIAL_FAILURE",
    "VSS_E_ASRERROR_DISK_ASSIGNMENT_FAILED",
    "VSS_E_ASRERROR_DISK_RECREATION_FAILED",
    "VSS_E_ASRERROR_NO_ARCPATH",
    "VSS_E_ASRERROR_MISSING_DYNDISK",
    "VSS_E_ASRERROR_SHARED_CRIDISK",
    "VSS_E_ASRERROR_DATADISK_RDISK0",
    "VSS_E_ASRERROR_RDISK0_TOOSMALL",
    "VSS_E_ASRERROR_CRITICAL_DISKS_TOO_SMALL",
    "VSS_E_WRITER_STATUS_NOT_AVAILABLE",
    "VSS_E_ASRERROR_DYNAMIC_VHD_NOT_SUPPORTED",
    "VSS_E_CRITICAL_VOLUME_ON_INVALID_DISK",
    "VSS_E_ASRERROR_RDISK_FOR_SYSTEM_DISK_NOT_FOUND",
    "VSS_E_ASRERROR_NO_PHYSICAL_DISK_AVAILABLE",
    "VSS_E_ASRERROR_FIXED_PHYSICAL_DISK_AVAILABLE_AFTER_DISK_EXCLUSION",
    "VSS_E_ASRERROR_CRITICAL_DISK_CANNOT_BE_EXCLUDED",
    "VSS_E_ASRERROR_SYSTEM_PARTITION_HIDDEN",
    "VSS_E_FSS_TIMEOUT",
    "VSS_OBJECT_TYPE",
    "VSS_OBJECT_UNKNOWN",
    "VSS_OBJECT_NONE",
    "VSS_OBJECT_SNAPSHOT_SET",
    "VSS_OBJECT_SNAPSHOT",
    "VSS_OBJECT_PROVIDER",
    "VSS_OBJECT_TYPE_COUNT",
    "VSS_SNAPSHOT_STATE",
    "VSS_SS_UNKNOWN",
    "VSS_SS_PREPARING",
    "VSS_SS_PROCESSING_PREPARE",
    "VSS_SS_PREPARED",
    "VSS_SS_PROCESSING_PRECOMMIT",
    "VSS_SS_PRECOMMITTED",
    "VSS_SS_PROCESSING_COMMIT",
    "VSS_SS_COMMITTED",
    "VSS_SS_PROCESSING_POSTCOMMIT",
    "VSS_SS_PROCESSING_PREFINALCOMMIT",
    "VSS_SS_PREFINALCOMMITTED",
    "VSS_SS_PROCESSING_POSTFINALCOMMIT",
    "VSS_SS_CREATED",
    "VSS_SS_ABORTED",
    "VSS_SS_DELETED",
    "VSS_SS_POSTCOMMITTED",
    "VSS_SS_COUNT",
    "VSS_VOLUME_SNAPSHOT_ATTRIBUTES",
    "VSS_VOLSNAP_ATTR_PERSISTENT",
    "VSS_VOLSNAP_ATTR_NO_AUTORECOVERY",
    "VSS_VOLSNAP_ATTR_CLIENT_ACCESSIBLE",
    "VSS_VOLSNAP_ATTR_NO_AUTO_RELEASE",
    "VSS_VOLSNAP_ATTR_NO_WRITERS",
    "VSS_VOLSNAP_ATTR_TRANSPORTABLE",
    "VSS_VOLSNAP_ATTR_NOT_SURFACED",
    "VSS_VOLSNAP_ATTR_NOT_TRANSACTED",
    "VSS_VOLSNAP_ATTR_HARDWARE_ASSISTED",
    "VSS_VOLSNAP_ATTR_DIFFERENTIAL",
    "VSS_VOLSNAP_ATTR_PLEX",
    "VSS_VOLSNAP_ATTR_IMPORTED",
    "VSS_VOLSNAP_ATTR_EXPOSED_LOCALLY",
    "VSS_VOLSNAP_ATTR_EXPOSED_REMOTELY",
    "VSS_VOLSNAP_ATTR_AUTORECOVER",
    "VSS_VOLSNAP_ATTR_ROLLBACK_RECOVERY",
    "VSS_VOLSNAP_ATTR_DELAYED_POSTSNAPSHOT",
    "VSS_VOLSNAP_ATTR_TXF_RECOVERY",
    "VSS_VOLSNAP_ATTR_FILE_SHARE",
    "VSS_SNAPSHOT_CONTEXT",
    "VSS_CTX_BACKUP",
    "VSS_CTX_FILE_SHARE_BACKUP",
    "VSS_CTX_NAS_ROLLBACK",
    "VSS_CTX_APP_ROLLBACK",
    "VSS_CTX_CLIENT_ACCESSIBLE",
    "VSS_CTX_CLIENT_ACCESSIBLE_WRITERS",
    "VSS_CTX_ALL",
    "VSS_PROVIDER_CAPABILITIES",
    "VSS_PRV_CAPABILITY_LEGACY",
    "VSS_PRV_CAPABILITY_COMPLIANT",
    "VSS_PRV_CAPABILITY_LUN_REPOINT",
    "VSS_PRV_CAPABILITY_LUN_RESYNC",
    "VSS_PRV_CAPABILITY_OFFLINE_CREATION",
    "VSS_PRV_CAPABILITY_MULTIPLE_IMPORT",
    "VSS_PRV_CAPABILITY_RECYCLING",
    "VSS_PRV_CAPABILITY_PLEX",
    "VSS_PRV_CAPABILITY_DIFFERENTIAL",
    "VSS_PRV_CAPABILITY_CLUSTERED",
    "VSS_HARDWARE_OPTIONS",
    "VSS_BREAKEX_FLAG_MASK_LUNS",
    "VSS_BREAKEX_FLAG_MAKE_READ_WRITE",
    "VSS_BREAKEX_FLAG_REVERT_IDENTITY_ALL",
    "VSS_BREAKEX_FLAG_REVERT_IDENTITY_NONE",
    "VSS_ONLUNSTATECHANGE_NOTIFY_READ_WRITE",
    "VSS_ONLUNSTATECHANGE_NOTIFY_LUN_PRE_RECOVERY",
    "VSS_ONLUNSTATECHANGE_NOTIFY_LUN_POST_RECOVERY",
    "VSS_ONLUNSTATECHANGE_DO_MASK_LUNS",
    "VSS_RECOVERY_OPTIONS",
    "VSS_RECOVERY_REVERT_IDENTITY_ALL",
    "VSS_RECOVERY_NO_VOLUME_CHECK",
    "VSS_WRITER_STATE",
    "VSS_WS_UNKNOWN",
    "VSS_WS_STABLE",
    "VSS_WS_WAITING_FOR_FREEZE",
    "VSS_WS_WAITING_FOR_THAW",
    "VSS_WS_WAITING_FOR_POST_SNAPSHOT",
    "VSS_WS_WAITING_FOR_BACKUP_COMPLETE",
    "VSS_WS_FAILED_AT_IDENTIFY",
    "VSS_WS_FAILED_AT_PREPARE_BACKUP",
    "VSS_WS_FAILED_AT_PREPARE_SNAPSHOT",
    "VSS_WS_FAILED_AT_FREEZE",
    "VSS_WS_FAILED_AT_THAW",
    "VSS_WS_FAILED_AT_POST_SNAPSHOT",
    "VSS_WS_FAILED_AT_BACKUP_COMPLETE",
    "VSS_WS_FAILED_AT_PRE_RESTORE",
    "VSS_WS_FAILED_AT_POST_RESTORE",
    "VSS_WS_FAILED_AT_BACKUPSHUTDOWN",
    "VSS_WS_COUNT",
    "VSS_BACKUP_TYPE",
    "VSS_BT_UNDEFINED",
    "VSS_BT_FULL",
    "VSS_BT_INCREMENTAL",
    "VSS_BT_DIFFERENTIAL",
    "VSS_BT_LOG",
    "VSS_BT_COPY",
    "VSS_BT_OTHER",
    "VSS_RESTORE_TYPE",
    "VSS_RTYPE_UNDEFINED",
    "VSS_RTYPE_BY_COPY",
    "VSS_RTYPE_IMPORT",
    "VSS_RTYPE_OTHER",
    "VSS_ROLLFORWARD_TYPE",
    "VSS_RF_UNDEFINED",
    "VSS_RF_NONE",
    "VSS_RF_ALL",
    "VSS_RF_PARTIAL",
    "VSS_PROVIDER_TYPE",
    "VSS_PROV_UNKNOWN",
    "VSS_PROV_SYSTEM",
    "VSS_PROV_SOFTWARE",
    "VSS_PROV_HARDWARE",
    "VSS_PROV_FILESHARE",
    "VSS_APPLICATION_LEVEL",
    "VSS_APP_UNKNOWN",
    "VSS_APP_SYSTEM",
    "VSS_APP_BACK_END",
    "VSS_APP_FRONT_END",
    "VSS_APP_SYSTEM_RM",
    "VSS_APP_AUTO",
    "VSS_SNAPSHOT_COMPATIBILITY",
    "VSS_SC_DISABLE_DEFRAG",
    "VSS_SC_DISABLE_CONTENTINDEX",
    "VSS_SNAPSHOT_PROPERTY_ID",
    "VSS_SPROPID_UNKNOWN",
    "VSS_SPROPID_SNAPSHOT_ID",
    "VSS_SPROPID_SNAPSHOT_SET_ID",
    "VSS_SPROPID_SNAPSHOTS_COUNT",
    "VSS_SPROPID_SNAPSHOT_DEVICE",
    "VSS_SPROPID_ORIGINAL_VOLUME",
    "VSS_SPROPID_ORIGINATING_MACHINE",
    "VSS_SPROPID_SERVICE_MACHINE",
    "VSS_SPROPID_EXPOSED_NAME",
    "VSS_SPROPID_EXPOSED_PATH",
    "VSS_SPROPID_PROVIDER_ID",
    "VSS_SPROPID_SNAPSHOT_ATTRIBUTES",
    "VSS_SPROPID_CREATION_TIMESTAMP",
    "VSS_SPROPID_STATUS",
    "VSS_FILE_SPEC_BACKUP_TYPE",
    "VSS_FSBT_FULL_BACKUP_REQUIRED",
    "VSS_FSBT_DIFFERENTIAL_BACKUP_REQUIRED",
    "VSS_FSBT_INCREMENTAL_BACKUP_REQUIRED",
    "VSS_FSBT_LOG_BACKUP_REQUIRED",
    "VSS_FSBT_FULL_SNAPSHOT_REQUIRED",
    "VSS_FSBT_DIFFERENTIAL_SNAPSHOT_REQUIRED",
    "VSS_FSBT_INCREMENTAL_SNAPSHOT_REQUIRED",
    "VSS_FSBT_LOG_SNAPSHOT_REQUIRED",
    "VSS_FSBT_CREATED_DURING_BACKUP",
    "VSS_FSBT_ALL_BACKUP_REQUIRED",
    "VSS_FSBT_ALL_SNAPSHOT_REQUIRED",
    "VSS_BACKUP_SCHEMA",
    "VSS_BS_UNDEFINED",
    "VSS_BS_DIFFERENTIAL",
    "VSS_BS_INCREMENTAL",
    "VSS_BS_EXCLUSIVE_INCREMENTAL_DIFFERENTIAL",
    "VSS_BS_LOG",
    "VSS_BS_COPY",
    "VSS_BS_TIMESTAMPED",
    "VSS_BS_LAST_MODIFY",
    "VSS_BS_LSN",
    "VSS_BS_WRITER_SUPPORTS_NEW_TARGET",
    "VSS_BS_WRITER_SUPPORTS_RESTORE_WITH_MOVE",
    "VSS_BS_INDEPENDENT_SYSTEM_STATE",
    "VSS_BS_ROLLFORWARD_RESTORE",
    "VSS_BS_RESTORE_RENAME",
    "VSS_BS_AUTHORITATIVE_RESTORE",
    "VSS_BS_WRITER_SUPPORTS_PARALLEL_RESTORES",
    "VSS_SNAPSHOT_PROP",
    "VSS_PROVIDER_PROP",
    "VSS_OBJECT_UNION",
    "VSS_OBJECT_PROP",
    "IVssEnumObject",
    "IVssAsync",
    "VSS_USAGE_TYPE",
    "VSS_UT_UNDEFINED",
    "VSS_UT_BOOTABLESYSTEMSTATE",
    "VSS_UT_SYSTEMSERVICE",
    "VSS_UT_USERDATA",
    "VSS_UT_OTHER",
    "VSS_SOURCE_TYPE",
    "VSS_ST_UNDEFINED",
    "VSS_ST_TRANSACTEDDB",
    "VSS_ST_NONTRANSACTEDDB",
    "VSS_ST_OTHER",
    "VSS_RESTOREMETHOD_ENUM",
    "VSS_RME_UNDEFINED",
    "VSS_RME_RESTORE_IF_NOT_THERE",
    "VSS_RME_RESTORE_IF_CAN_REPLACE",
    "VSS_RME_STOP_RESTORE_START",
    "VSS_RME_RESTORE_TO_ALTERNATE_LOCATION",
    "VSS_RME_RESTORE_AT_REBOOT",
    "VSS_RME_RESTORE_AT_REBOOT_IF_CANNOT_REPLACE",
    "VSS_RME_CUSTOM",
    "VSS_RME_RESTORE_STOP_START",
    "VSS_WRITERRESTORE_ENUM",
    "VSS_WRE_UNDEFINED",
    "VSS_WRE_NEVER",
    "VSS_WRE_IF_REPLACE_FAILS",
    "VSS_WRE_ALWAYS",
    "VSS_COMPONENT_TYPE",
    "VSS_CT_UNDEFINED",
    "VSS_CT_DATABASE",
    "VSS_CT_FILEGROUP",
    "VSS_ALTERNATE_WRITER_STATE",
    "VSS_AWS_UNDEFINED",
    "VSS_AWS_NO_ALTERNATE_WRITER",
    "VSS_AWS_ALTERNATE_WRITER_EXISTS",
    "VSS_AWS_THIS_IS_ALTERNATE_WRITER",
    "VSS_SUBSCRIBE_MASK",
    "VSS_SM_POST_SNAPSHOT_FLAG",
    "VSS_SM_BACKUP_EVENTS_FLAG",
    "VSS_SM_RESTORE_EVENTS_FLAG",
    "VSS_SM_IO_THROTTLING_FLAG",
    "VSS_SM_ALL_FLAGS",
    "VSS_RESTORE_TARGET",
    "VSS_RT_UNDEFINED",
    "VSS_RT_ORIGINAL",
    "VSS_RT_ALTERNATE",
    "VSS_RT_DIRECTED",
    "VSS_RT_ORIGINAL_LOCATION",
    "VSS_FILE_RESTORE_STATUS",
    "VSS_RS_UNDEFINED",
    "VSS_RS_NONE",
    "VSS_RS_ALL",
    "VSS_RS_FAILED",
    "VSS_COMPONENT_FLAGS",
    "VSS_CF_BACKUP_RECOVERY",
    "VSS_CF_APP_ROLLBACK_RECOVERY",
    "VSS_CF_NOT_SYSTEM_STATE",
    "IVssExamineWriterMetadata",
    "IVssWMFiledesc",
    "IVssWMDependency",
    "IVssComponent",
    "IVssWriterComponents",
    "IVssComponentEx",
    "IVssComponentEx2",
    "IVssCreateWriterMetadata",
    "IVssWriterImpl",
    "IVssCreateExpressWriterMetadata",
    "IVssExpressWriter",
    "VssSnapshotMgmt",
    "VSS_MGMT_OBJECT_TYPE",
    "VSS_MGMT_OBJECT_UNKNOWN",
    "VSS_MGMT_OBJECT_VOLUME",
    "VSS_MGMT_OBJECT_DIFF_VOLUME",
    "VSS_MGMT_OBJECT_DIFF_AREA",
    "VSS_VOLUME_PROP",
    "VSS_DIFF_VOLUME_PROP",
    "VSS_DIFF_AREA_PROP",
    "VSS_MGMT_OBJECT_UNION",
    "VSS_MGMT_OBJECT_PROP",
    "VSS_PROTECTION_LEVEL",
    "VSS_PROTECTION_LEVEL_ORIGINAL_VOLUME",
    "VSS_PROTECTION_LEVEL_SNAPSHOT",
    "VSS_PROTECTION_FAULT",
    "VSS_PROTECTION_FAULT_NONE",
    "VSS_PROTECTION_FAULT_DIFF_AREA_MISSING",
    "VSS_PROTECTION_FAULT_IO_FAILURE_DURING_ONLINE",
    "VSS_PROTECTION_FAULT_META_DATA_CORRUPTION",
    "VSS_PROTECTION_FAULT_MEMORY_ALLOCATION_FAILURE",
    "VSS_PROTECTION_FAULT_MAPPED_MEMORY_FAILURE",
    "VSS_PROTECTION_FAULT_COW_READ_FAILURE",
    "VSS_PROTECTION_FAULT_COW_WRITE_FAILURE",
    "VSS_PROTECTION_FAULT_DIFF_AREA_FULL",
    "VSS_PROTECTION_FAULT_GROW_TOO_SLOW",
    "VSS_PROTECTION_FAULT_GROW_FAILED",
    "VSS_PROTECTION_FAULT_DESTROY_ALL_SNAPSHOTS",
    "VSS_PROTECTION_FAULT_FILE_SYSTEM_FAILURE",
    "VSS_PROTECTION_FAULT_IO_FAILURE",
    "VSS_PROTECTION_FAULT_DIFF_AREA_REMOVED",
    "VSS_PROTECTION_FAULT_EXTERNAL_WRITER_TO_DIFF_AREA",
    "VSS_PROTECTION_FAULT_MOUNT_DURING_CLUSTER_OFFLINE",
    "VSS_VOLUME_PROTECTION_INFO",
    "IVssSnapshotMgmt",
    "IVssSnapshotMgmt2",
    "IVssDifferentialSoftwareSnapshotMgmt",
    "IVssDifferentialSoftwareSnapshotMgmt2",
    "IVssDifferentialSoftwareSnapshotMgmt3",
    "IVssEnumMgmtObject",
    "VSSCoordinator",
    "IVssAdmin",
    "IVssAdminEx",
    "IVssSoftwareSnapshotProvider",
    "IVssProviderCreateSnapshotSet",
    "IVssProviderNotifications",
    "IVssHardwareSnapshotProvider",
    "IVssHardwareSnapshotProviderEx",
    "IVssFileShareSnapshotProvider",
    "CreateVssExpressWriterInternal",
]
