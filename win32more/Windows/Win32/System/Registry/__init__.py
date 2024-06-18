from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security
import win32more.Windows.Win32.System.Registry
HKEY_CLASSES_ROOT: win32more.Windows.Win32.System.Registry.HKEY = -2147483648
HKEY_CURRENT_USER: win32more.Windows.Win32.System.Registry.HKEY = -2147483647
HKEY_LOCAL_MACHINE: win32more.Windows.Win32.System.Registry.HKEY = -2147483646
HKEY_USERS: win32more.Windows.Win32.System.Registry.HKEY = -2147483645
HKEY_PERFORMANCE_DATA: win32more.Windows.Win32.System.Registry.HKEY = -2147483644
HKEY_PERFORMANCE_TEXT: win32more.Windows.Win32.System.Registry.HKEY = -2147483568
HKEY_PERFORMANCE_NLSTEXT: win32more.Windows.Win32.System.Registry.HKEY = -2147483552
HKEY_CURRENT_CONFIG: win32more.Windows.Win32.System.Registry.HKEY = -2147483643
HKEY_DYN_DATA: win32more.Windows.Win32.System.Registry.HKEY = -2147483642
HKEY_CURRENT_USER_LOCAL_SETTINGS: win32more.Windows.Win32.System.Registry.HKEY = -2147483641
REG_PROCESS_APPKEY: UInt32 = 1
REG_USE_CURRENT_SECURITY_CONTEXT: UInt32 = 2
PROVIDER_KEEPS_VALUE_LENGTH: UInt32 = 1
REG_MUI_STRING_TRUNCATE: UInt32 = 1
REG_SECURE_CONNECTION: UInt32 = 1
REGSTR_KEY_CLASS: String = 'Class'
REGSTR_KEY_CONFIG: String = 'Config'
REGSTR_KEY_ENUM: String = 'Enum'
REGSTR_KEY_ROOTENUM: String = 'Root'
REGSTR_KEY_BIOSENUM: String = 'BIOS'
REGSTR_KEY_ACPIENUM: String = 'ACPI'
REGSTR_KEY_PCMCIAENUM: String = 'PCMCIA'
REGSTR_KEY_PCIENUM: String = 'PCI'
REGSTR_KEY_VPOWERDENUM: String = 'VPOWERD'
REGSTR_KEY_ISAENUM: String = 'ISAPnP'
REGSTR_KEY_EISAENUM: String = 'EISA'
REGSTR_KEY_LOGCONFIG: String = 'LogConfig'
REGSTR_KEY_SYSTEMBOARD: String = '*PNP0C01'
REGSTR_KEY_APM: String = '*PNP0C05'
REGSTR_KEY_INIUPDATE: String = 'IniUpdate'
REG_KEY_INSTDEV: String = 'Installed'
REGSTR_KEY_DOSOPTCDROM: String = 'CD-ROM'
REGSTR_KEY_DOSOPTMOUSE: String = 'MOUSE'
REGSTR_KEY_KNOWNDOCKINGSTATES: String = 'Hardware Profiles'
REGSTR_KEY_DEVICEPARAMETERS: String = 'Device Parameters'
REGSTR_KEY_DRIVERPARAMETERS: String = 'Driver Parameters'
REGSTR_DEFAULT_INSTANCE: String = '0000'
REGSTR_PATH_SETUP: String = 'Software\\Microsoft\\Windows\\CurrentVersion'
REGSTR_PATH_DRIVERSIGN: String = 'Software\\Microsoft\\Driver Signing'
REGSTR_PATH_NONDRIVERSIGN: String = 'Software\\Microsoft\\Non-Driver Signing'
REGSTR_PATH_DRIVERSIGN_POLICY: String = 'Software\\Policies\\Microsoft\\Windows NT\\Driver Signing'
REGSTR_PATH_NONDRIVERSIGN_POLICY: String = 'Software\\Policies\\Microsoft\\Windows NT\\Non-Driver Signing'
REGSTR_PATH_PIFCONVERT: String = 'Software\\Microsoft\\Windows\\CurrentVersion\\PIFConvert'
REGSTR_PATH_MSDOSOPTS: String = 'Software\\Microsoft\\Windows\\CurrentVersion\\MS-DOSOptions'
REGSTR_PATH_NOSUGGMSDOS: String = 'Software\\Microsoft\\Windows\\CurrentVersion\\NoMSDOSWarn'
REGSTR_PATH_NEWDOSBOX: String = 'Software\\Microsoft\\Windows\\CurrentVersion\\MS-DOSSpecialConfig'
REGSTR_PATH_RUNONCE: String = 'Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce'
REGSTR_PATH_RUNONCEEX: String = 'Software\\Microsoft\\Windows\\CurrentVersion\\RunOnceEx'
REGSTR_PATH_RUN: String = 'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
REGSTR_PATH_RUNSERVICESONCE: String = 'Software\\Microsoft\\Windows\\CurrentVersion\\RunServicesOnce'
REGSTR_PATH_RUNSERVICES: String = 'Software\\Microsoft\\Windows\\CurrentVersion\\RunServices'
REGSTR_PATH_EXPLORER: String = 'Software\\Microsoft\\Windows\\CurrentVersion\\Explorer'
REGSTR_PATH_PROPERTYSYSTEM: String = 'Software\\Microsoft\\Windows\\CurrentVersion\\PropertySystem'
REGSTR_PATH_DETECT: String = 'Software\\Microsoft\\Windows\\CurrentVersion\\Detect'
REGSTR_PATH_APPPATHS: String = 'Software\\Microsoft\\Windows\\CurrentVersion\\App Paths'
REGSTR_PATH_UNINSTALL: String = 'Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall'
REGSTR_PATH_REALMODENET: String = 'Software\\Microsoft\\Windows\\CurrentVersion\\Network\\Real Mode Net'
REGSTR_PATH_NETEQUIV: String = 'Software\\Microsoft\\Windows\\CurrentVersion\\Network\\Equivalent'
REGSTR_PATH_CVNETWORK: String = 'Software\\Microsoft\\Windows\\CurrentVersion\\Network'
REGSTR_PATH_WMI_SECURITY: String = 'System\\CurrentControlSet\\Control\\Wmi\\Security'
REGSTR_PATH_RELIABILITY: String = 'Software\\Microsoft\\Windows\\CurrentVersion\\Reliability'
REGSTR_PATH_RELIABILITY_POLICY: String = 'Software\\Policies\\Microsoft\\Windows NT\\Reliability'
REGSTR_PATH_RELIABILITY_POLICY_SHUTDOWNREASONUI: String = 'ShutdownReasonUI'
REGSTR_PATH_RELIABILITY_POLICY_SNAPSHOT: String = 'Snapshot'
REGSTR_PATH_RELIABILITY_POLICY_REPORTSNAPSHOT: String = 'ReportSnapshot'
REGSTR_PATH_REINSTALL: String = 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Reinstall'
REGSTR_PATH_NT_CURRENTVERSION: String = 'Software\\Microsoft\\Windows NT\\CurrentVersion'
REGSTR_PATH_VOLUMECACHE: String = 'Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VolumeCaches'
REGSTR_VAL_DISPLAY: String = 'display'
REGSTR_PATH_IDCONFIGDB: String = 'System\\CurrentControlSet\\Control\\IDConfigDB'
REGSTR_PATH_CRITICALDEVICEDATABASE: String = 'System\\CurrentControlSet\\Control\\CriticalDeviceDatabase'
REGSTR_PATH_CLASS: String = 'System\\CurrentControlSet\\Services\\Class'
REGSTR_PATH_DISPLAYSETTINGS: String = 'Display\\Settings'
REGSTR_PATH_FONTS: String = 'Display\\Fonts'
REGSTR_PATH_ENUM: String = 'Enum'
REGSTR_PATH_ROOT: String = 'Enum\\Root'
REGSTR_PATH_CURRENTCONTROLSET: String = 'System\\CurrentControlSet'
REGSTR_PATH_SYSTEMENUM: String = 'System\\CurrentControlSet\\Enum'
REGSTR_PATH_HWPROFILES: String = 'System\\CurrentControlSet\\Hardware Profiles'
REGSTR_PATH_HWPROFILESCURRENT: String = 'System\\CurrentControlSet\\Hardware Profiles\\Current'
REGSTR_PATH_CLASS_NT: String = 'System\\CurrentControlSet\\Control\\Class'
REGSTR_PATH_PER_HW_ID_STORAGE: String = 'Software\\Microsoft\\Windows NT\\CurrentVersion\\PerHwIdStorage'
REGSTR_PATH_DEVICE_CLASSES: String = 'System\\CurrentControlSet\\Control\\DeviceClasses'
REGSTR_PATH_CODEVICEINSTALLERS: String = 'System\\CurrentControlSet\\Control\\CoDeviceInstallers'
REGSTR_PATH_BUSINFORMATION: String = 'System\\CurrentControlSet\\Control\\PnP\\BusInformation'
REGSTR_PATH_SERVICES: String = 'System\\CurrentControlSet\\Services'
REGSTR_PATH_VXD: String = 'System\\CurrentControlSet\\Services\\VxD'
REGSTR_PATH_IOS: String = 'System\\CurrentControlSet\\Services\\VxD\\IOS'
REGSTR_PATH_VMM: String = 'System\\CurrentControlSet\\Services\\VxD\\VMM'
REGSTR_PATH_VPOWERD: String = 'System\\CurrentControlSet\\Services\\VxD\\VPOWERD'
REGSTR_PATH_VNETSUP: String = 'System\\CurrentControlSet\\Services\\VxD\\VNETSUP'
REGSTR_PATH_NWREDIR: String = 'System\\CurrentControlSet\\Services\\VxD\\NWREDIR'
REGSTR_PATH_NCPSERVER: String = 'System\\CurrentControlSet\\Services\\NcpServer\\Parameters'
REGSTR_PATH_VCOMM: String = 'System\\CurrentControlSet\\Services\\VxD\\VCOMM'
REGSTR_PATH_IOARB: String = 'System\\CurrentControlSet\\Services\\Arbitrators\\IOArb'
REGSTR_PATH_ADDRARB: String = 'System\\CurrentControlSet\\Services\\Arbitrators\\AddrArb'
REGSTR_PATH_DMAARB: String = 'System\\CurrentControlSet\\Services\\Arbitrators\\DMAArb'
REGSTR_PATH_IRQARB: String = 'System\\CurrentControlSet\\Services\\Arbitrators\\IRQArb'
REGSTR_PATH_CODEPAGE: String = 'System\\CurrentControlSet\\Control\\Nls\\Codepage'
REGSTR_PATH_FILESYSTEM: String = 'System\\CurrentControlSet\\Control\\FileSystem'
REGSTR_PATH_FILESYSTEM_NOVOLTRACK: String = 'System\\CurrentControlSet\\Control\\FileSystem\\NoVolTrack'
REGSTR_PATH_CDFS: String = 'System\\CurrentControlSet\\Control\\FileSystem\\CDFS'
REGSTR_PATH_WINBOOT: String = 'System\\CurrentControlSet\\Control\\WinBoot'
REGSTR_PATH_INSTALLEDFILES: String = 'System\\CurrentControlSet\\Control\\InstalledFiles'
REGSTR_PATH_VMM32FILES: String = 'System\\CurrentControlSet\\Control\\VMM32Files'
REGSTR_MAX_VALUE_LENGTH: UInt32 = 256
REGSTR_KEY_DEVICE_PROPERTIES: String = 'Properties'
REGSTR_VAL_SERVICE: String = 'Service'
REGSTR_VAL_CLASSGUID: String = 'ClassGUID'
REGSTR_VAL_DISABLECOUNT: String = 'DisableCount'
REGSTR_VAL_DOCKSTATE: String = 'DockState'
REGSTR_VAL_DEVICE_INSTANCE: String = 'DeviceInstance'
REGSTR_VAL_SYMBOLIC_LINK: String = 'SymbolicLink'
REGSTR_VAL_DEFAULT: String = 'Default'
REGSTR_VAL_LOWERFILTERS: String = 'LowerFilters'
REGSTR_VAL_UPPERFILTERS: String = 'UpperFilters'
REGSTR_VAL_LOCATION_INFORMATION: String = 'LocationInformation'
REGSTR_VAL_UI_NUMBER: String = 'UINumber'
REGSTR_VAL_UI_NUMBER_DESC_FORMAT: String = 'UINumberDescFormat'
REGSTR_VAL_CAPABILITIES: String = 'Capabilities'
REGSTR_VAL_ADDRESS: String = 'Address'
REGSTR_VAL_DEVICE_TYPE: String = 'DeviceType'
REGSTR_VAL_DEVICE_CHARACTERISTICS: String = 'DeviceCharacteristics'
REGSTR_VAL_DEVICE_SECURITY_DESCRIPTOR: String = 'Security'
REGSTR_VAL_DEVICE_EXCLUSIVE: String = 'Exclusive'
REGSTR_VAL_RESOURCE_PICKER_TAGS: String = 'ResourcePickerTags'
REGSTR_VAL_RESOURCE_PICKER_EXCEPTIONS: String = 'ResourcePickerExceptions'
REGSTR_VAL_CUSTOM_PROPERTY_CACHE_DATE: String = 'CustomPropertyCacheDate'
REGSTR_VAL_CUSTOM_PROPERTY_HW_ID_KEY: String = 'CustomPropertyHwIdKey'
REGSTR_VAL_LAST_UPDATE_TIME: String = 'LastUpdateTime'
REGSTR_VAL_CONTAINERID: String = 'ContainerID'
REGSTR_VAL_EJECT_PRIORITY: String = 'EjectPriority'
REGSTR_KEY_CONTROL: String = 'Control'
REGSTR_VAL_ACTIVESERVICE: String = 'ActiveService'
REGSTR_VAL_LINKED: String = 'Linked'
REGSTR_VAL_PHYSICALDEVICEOBJECT: String = 'PhysicalDeviceObject'
REGSTR_VAL_REMOVAL_POLICY: String = 'RemovalPolicy'
REGSTR_KEY_FILTERS: String = 'Filters'
REGSTR_VAL_LOWER_FILTER_DEFAULT_LEVEL: String = 'LowerFilterDefaultLevel'
REGSTR_VAL_UPPER_FILTER_DEFAULT_LEVEL: String = 'UpperFilterDefaultLevel'
REGSTR_KEY_LOWER_FILTER_LEVEL_DEFAULT: String = '*Lower'
REGSTR_KEY_UPPER_FILTER_LEVEL_DEFAULT: String = '*Upper'
REGSTR_VAL_LOWER_FILTER_LEVELS: String = 'LowerFilterLevels'
REGSTR_VAL_UPPER_FILTER_LEVELS: String = 'UpperFilterLevels'
REGSTR_VAL_CURRENT_VERSION: String = 'CurrentVersion'
REGSTR_VAL_CURRENT_BUILD: String = 'CurrentBuildNumber'
REGSTR_VAL_CURRENT_CSDVERSION: String = 'CSDVersion'
REGSTR_VAL_CURRENT_TYPE: String = 'CurrentType'
REGSTR_VAL_BITSPERPIXEL: String = 'BitsPerPixel'
REGSTR_VAL_RESOLUTION: String = 'Resolution'
REGSTR_VAL_DPILOGICALX: String = 'DPILogicalX'
REGSTR_VAL_DPILOGICALY: String = 'DPILogicalY'
REGSTR_VAL_DPIPHYSICALX: String = 'DPIPhysicalX'
REGSTR_VAL_DPIPHYSICALY: String = 'DPIPhysicalY'
REGSTR_VAL_REFRESHRATE: String = 'RefreshRate'
REGSTR_VAL_DISPLAYFLAGS: String = 'DisplayFlags'
REGSTR_PATH_CONTROLPANEL: String = 'Control Panel'
REGSTR_PATH_CONTROLSFOLDER: String = 'Software\\Microsoft\\Windows\\CurrentVersion\\Controls Folder'
REGSTR_VAL_DOSCP: String = 'OEMCP'
REGSTR_VAL_WINCP: String = 'ACP'
REGSTR_VAL_DONTUSEMEM: String = 'DontAllocLastMem'
REGSTR_VAL_SYSTEMROOT: String = 'SystemRoot'
REGSTR_VAL_BOOTCOUNT: String = 'BootCount'
REGSTR_VAL_REALNETSTART: String = 'RealNetStart'
REGSTR_VAL_MEDIA: String = 'MediaPath'
REGSTR_VAL_CONFIG: String = 'ConfigPath'
REGSTR_VAL_DEVICEPATH: String = 'DevicePath'
REGSTR_VAL_SRCPATH: String = 'SourcePath'
REGSTR_VAL_DRIVERCACHEPATH: String = 'DriverCachePath'
REGSTR_VAL_OLDWINDIR: String = 'OldWinDir'
REGSTR_VAL_SETUPFLAGS: String = 'SetupFlags'
REGSTR_VAL_REGOWNER: String = 'RegisteredOwner'
REGSTR_VAL_REGORGANIZATION: String = 'RegisteredOrganization'
REGSTR_VAL_LICENSINGINFO: String = 'LicensingInfo'
REGSTR_VAL_OLDMSDOSVER: String = 'OldMSDOSVer'
REGSTR_VAL_FIRSTINSTALLDATETIME: String = 'FirstInstallDateTime'
REGSTR_VAL_INSTALLTYPE: String = 'InstallType'
IT_COMPACT: UInt32 = 0
IT_TYPICAL: UInt32 = 1
IT_PORTABLE: UInt32 = 2
IT_CUSTOM: UInt32 = 3
REGSTR_VAL_WRAPPER: String = 'Wrapper'
REGSTR_KEY_RUNHISTORY: String = 'RunHistory'
REGSTR_VAL_LASTALIVEINTERVAL: String = 'TimeStampInterval'
REGSTR_VAL_DIRTYSHUTDOWN: String = 'DirtyShutdown'
REGSTR_VAL_DIRTYSHUTDOWNTIME: String = 'DirtyShutdownTime'
REGSTR_VAL_BT: String = '6005BT'
REGSTR_VAL_LASTCOMPUTERNAME: String = 'LastComputerName'
REGSTR_VAL_LASTALIVEBT: String = 'LastAliveBT'
REGSTR_VAL_LASTALIVESTAMP: String = 'LastAliveStamp'
REGSTR_VAL_LASTALIVESTAMPFORCED: String = 'LastAliveStampForced'
REGSTR_VAL_LASTALIVESTAMPINTERVAL: String = 'LastAliveStampInterval'
REGSTR_VAL_LASTALIVESTAMPPOLICYINTERVAL: String = 'LastAliveStampPolicyInterval'
REGSTR_VAL_LASTALIVEUPTIME: String = 'LastAliveUptime'
REGSTR_VAL_LASTALIVEPMPOLICY: String = 'LastAlivePMPolicy'
REGSTR_VAL_REASONCODE: String = 'ReasonCode'
REGSTR_VAL_COMMENT: String = 'Comment'
REGSTR_VAL_SHUTDOWNREASON: String = 'ShutdownReason'
REGSTR_VAL_SHUTDOWNREASON_CODE: String = 'ShutdownReasonCode'
REGSTR_VAL_SHUTDOWNREASON_COMMENT: String = 'ShutdownReasonComment'
REGSTR_VAL_SHUTDOWNREASON_PROCESS: String = 'ShutdownReasonProcess'
REGSTR_VAL_SHUTDOWNREASON_USERNAME: String = 'ShutdownReasonUserName'
REGSTR_VAL_SHOWREASONUI: String = 'ShutdownReasonUI'
REGSTR_VAL_SHUTDOWN_IGNORE_PREDEFINED: String = 'ShutdownIgnorePredefinedReasons'
REGSTR_VAL_SHUTDOWN_STATE_SNAPSHOT: String = 'ShutdownStateSnapshot'
REGSTR_KEY_SETUP: String = '\\Setup'
REGSTR_VAL_BOOTDIR: String = 'BootDir'
REGSTR_VAL_WINBOOTDIR: String = 'WinbootDir'
REGSTR_VAL_WINDIR: String = 'WinDir'
REGSTR_VAL_APPINSTPATH: String = 'AppInstallPath'
REGSTR_KEY_EBDFILESLOCAL: String = 'EBDFilesLocale'
REGSTR_KEY_EBDFILESKEYBOARD: String = 'EBDFilesKeyboard'
REGSTR_KEY_EBDAUTOEXECBATLOCAL: String = 'EBDAutoexecBatLocale'
REGSTR_KEY_EBDAUTOEXECBATKEYBOARD: String = 'EBDAutoexecBatKeyboard'
REGSTR_KEY_EBDCONFIGSYSLOCAL: String = 'EBDConfigSysLocale'
REGSTR_KEY_EBDCONFIGSYSKEYBOARD: String = 'EBDConfigSysKeyboard'
REGSTR_VAL_POLICY: String = 'Policy'
REGSTR_VAL_BEHAVIOR_ON_FAILED_VERIFY: String = 'BehaviorOnFailedVerify'
DRIVERSIGN_NONE: UInt32 = 0
DRIVERSIGN_WARNING: UInt32 = 1
DRIVERSIGN_BLOCKING: UInt32 = 2
REGSTR_VAL_MSDOSMODE: String = 'MSDOSMode'
REGSTR_VAL_MSDOSMODEDISCARD: String = 'Discard'
REGSTR_VAL_DOSOPTGLOBALFLAGS: String = 'GlobalFlags'
DOSOPTGF_DEFCLEAN: Int32 = 1
REGSTR_VAL_DOSOPTFLAGS: String = 'Flags'
REGSTR_VAL_OPTORDER: String = 'Order'
REGSTR_VAL_CONFIGSYS: String = 'Config.Sys'
REGSTR_VAL_AUTOEXEC: String = 'Autoexec.Bat'
REGSTR_VAL_STDDOSOPTION: String = 'StdOption'
REGSTR_VAL_DOSOPTTIP: String = 'TipText'
DOSOPTF_DEFAULT: Int32 = 1
DOSOPTF_SUPPORTED: Int32 = 2
DOSOPTF_ALWAYSUSE: Int32 = 4
DOSOPTF_USESPMODE: Int32 = 8
DOSOPTF_PROVIDESUMB: Int32 = 16
DOSOPTF_NEEDSETUP: Int32 = 32
DOSOPTF_INDOSSTART: Int32 = 64
DOSOPTF_MULTIPLE: Int32 = 128
SUF_FIRSTTIME: Int32 = 1
SUF_EXPRESS: Int32 = 2
SUF_BATCHINF: Int32 = 4
SUF_CLEAN: Int32 = 8
SUF_INSETUP: Int32 = 16
SUF_NETSETUP: Int32 = 32
SUF_NETHDBOOT: Int32 = 64
SUF_NETRPLBOOT: Int32 = 128
SUF_SBSCOPYOK: Int32 = 256
REGSTR_VAL_DOSPAGER: String = 'DOSPager'
REGSTR_VAL_VXDGROUPS: String = 'VXDGroups'
REGSTR_VAL_VPOWERDFLAGS: String = 'Flags'
VPDF_DISABLEPWRMGMT: UInt32 = 1
VPDF_FORCEAPM10MODE: UInt32 = 2
VPDF_SKIPINTELSLCHECK: UInt32 = 4
VPDF_DISABLEPWRSTATUSPOLL: UInt32 = 8
VPDF_DISABLERINGRESUME: UInt32 = 16
VPDF_SHOWMULTIBATT: UInt32 = 32
BIF_SHOWSIMILARDRIVERS: UInt32 = 1
BIF_RAWDEVICENEEDSDRIVER: UInt32 = 2
REGSTR_VAL_WORKGROUP: String = 'Workgroup'
REGSTR_VAL_DIRECTHOST: String = 'DirectHost'
REGSTR_VAL_FILESHARING: String = 'FileSharing'
REGSTR_VAL_PRINTSHARING: String = 'PrintSharing'
REGSTR_VAL_FIRSTNETDRIVE: String = 'FirstNetworkDrive'
REGSTR_VAL_MAXCONNECTIONS: String = 'MaxConnections'
REGSTR_VAL_APISUPPORT: String = 'APISupport'
REGSTR_VAL_MAXRETRY: String = 'MaxRetry'
REGSTR_VAL_MINRETRY: String = 'MinRetry'
REGSTR_VAL_SUPPORTLFN: String = 'SupportLFN'
REGSTR_VAL_SUPPORTBURST: String = 'SupportBurst'
REGSTR_VAL_SUPPORTTUNNELLING: String = 'SupportTunnelling'
REGSTR_VAL_FULLTRACE: String = 'FullTrace'
REGSTR_VAL_READCACHING: String = 'ReadCaching'
REGSTR_VAL_SHOWDOTS: String = 'ShowDots'
REGSTR_VAL_GAPTIME: String = 'GapTime'
REGSTR_VAL_SEARCHMODE: String = 'SearchMode'
REGSTR_VAL_SHELLVERSION: String = 'ShellVersion'
REGSTR_VAL_MAXLIP: String = 'MaxLIP'
REGSTR_VAL_PRESERVECASE: String = 'PreserveCase'
REGSTR_VAL_OPTIMIZESFN: String = 'OptimizeSFN'
REGSTR_VAL_NCP_BROWSEMASTER: String = 'BrowseMaster'
REGSTR_VAL_NCP_USEPEERBROWSING: String = 'Use_PeerBrowsing'
REGSTR_VAL_NCP_USESAP: String = 'Use_Sap'
REGSTR_VAL_PCCARD_POWER: String = 'EnablePowerManagement'
REGSTR_VAL_WIN31FILESYSTEM: String = 'Win31FileSystem'
REGSTR_VAL_PRESERVELONGNAMES: String = 'PreserveLongNames'
REGSTR_VAL_DRIVEWRITEBEHIND: String = 'DriveWriteBehind'
REGSTR_VAL_ASYNCFILECOMMIT: String = 'AsyncFileCommit'
REGSTR_VAL_PATHCACHECOUNT: String = 'PathCache'
REGSTR_VAL_NAMECACHECOUNT: String = 'NameCache'
REGSTR_VAL_CONTIGFILEALLOC: String = 'ContigFileAllocSize'
REGSTR_VAL_FREESPACERATIO: String = 'FreeSpaceRatio'
REGSTR_VAL_VOLIDLETIMEOUT: String = 'VolumeIdleTimeout'
REGSTR_VAL_BUFFIDLETIMEOUT: String = 'BufferIdleTimeout'
REGSTR_VAL_BUFFAGETIMEOUT: String = 'BufferAgeTimeout'
REGSTR_VAL_NAMENUMERICTAIL: String = 'NameNumericTail'
REGSTR_VAL_READAHEADTHRESHOLD: String = 'ReadAheadThreshold'
REGSTR_VAL_DOUBLEBUFFER: String = 'DoubleBuffer'
REGSTR_VAL_SOFTCOMPATMODE: String = 'SoftCompatMode'
REGSTR_VAL_DRIVESPINDOWN: String = 'DriveSpinDown'
REGSTR_VAL_FORCEPMIO: String = 'ForcePMIO'
REGSTR_VAL_FORCERMIO: String = 'ForceRMIO'
REGSTR_VAL_LASTBOOTPMDRVS: String = 'LastBootPMDrvs'
REGSTR_VAL_ACSPINDOWNPREVIOUS: String = 'ACSpinDownPrevious'
REGSTR_VAL_BATSPINDOWNPREVIOUS: String = 'BatSpinDownPrevious'
REGSTR_VAL_VIRTUALHDIRQ: String = 'VirtualHDIRQ'
REGSTR_VAL_SRVNAMECACHECOUNT: String = 'ServerNameCacheMax'
REGSTR_VAL_SRVNAMECACHE: String = 'ServerNameCache'
REGSTR_VAL_SRVNAMECACHENETPROV: String = 'ServerNameCacheNumNets'
REGSTR_VAL_AUTOMOUNT: String = 'AutoMountDrives'
REGSTR_VAL_COMPRESSIONMETHOD: String = 'CompressionAlgorithm'
REGSTR_VAL_COMPRESSIONTHRESHOLD: String = 'CompressionThreshold'
REGSTR_VAL_ACDRIVESPINDOWN: String = 'ACDriveSpinDown'
REGSTR_VAL_BATDRIVESPINDOWN: String = 'BatDriveSpinDown'
REGSTR_VAL_CDCACHESIZE: String = 'CacheSize'
REGSTR_VAL_CDPREFETCH: String = 'Prefetch'
REGSTR_VAL_CDPREFETCHTAIL: String = 'PrefetchTail'
REGSTR_VAL_CDRAWCACHE: String = 'RawCache'
REGSTR_VAL_CDEXTERRORS: String = 'ExtendedErrors'
REGSTR_VAL_CDSVDSENSE: String = 'SVDSense'
REGSTR_VAL_CDSHOWVERSIONS: String = 'ShowVersions'
REGSTR_VAL_CDCOMPATNAMES: String = 'MSCDEXCompatNames'
REGSTR_VAL_CDNOREADAHEAD: String = 'NoReadAhead'
REGSTR_VAL_SCSI: String = 'SCSI\\'
REGSTR_VAL_ESDI: String = 'ESDI\\'
REGSTR_VAL_FLOP: String = 'FLOP\\'
REGSTR_VAL_DISK: String = 'GenDisk'
REGSTR_VAL_CDROM: String = 'GenCD'
REGSTR_VAL_TAPE: String = 'TAPE'
REGSTR_VAL_SCANNER: String = 'SCANNER'
REGSTR_VAL_FLOPPY: String = 'FLOPPY'
REGSTR_VAL_SCSITID: String = 'SCSITargetID'
REGSTR_VAL_SCSILUN: String = 'SCSILUN'
REGSTR_VAL_REVLEVEL: String = 'RevisionLevel'
REGSTR_VAL_PRODUCTID: String = 'ProductId'
REGSTR_VAL_PRODUCTTYPE: String = 'ProductType'
REGSTR_VAL_DEVTYPE: String = 'DeviceType'
REGSTR_VAL_REMOVABLE: String = 'Removable'
REGSTR_VAL_CURDRVLET: String = 'CurrentDriveLetterAssignment'
REGSTR_VAL_USRDRVLET: String = 'UserDriveLetterAssignment'
REGSTR_VAL_SYNCDATAXFER: String = 'SyncDataXfer'
REGSTR_VAL_AUTOINSNOTE: String = 'AutoInsertNotification'
REGSTR_VAL_DISCONNECT: String = 'Disconnect'
REGSTR_VAL_INT13: String = 'Int13'
REGSTR_VAL_PMODE_INT13: String = 'PModeInt13'
REGSTR_VAL_USERSETTINGS: String = 'AdapterSettings'
REGSTR_VAL_NOIDE: String = 'NoIDE'
REGSTR_VAL_DISKCLASSNAME: String = 'DiskDrive'
REGSTR_VAL_CDROMCLASSNAME: String = 'CDROM'
REGSTR_VAL_FORCELOAD: String = 'ForceLoadPD'
REGSTR_VAL_FORCEFIFO: String = 'ForceFIFO'
REGSTR_VAL_FORCECL: String = 'ForceChangeLine'
REGSTR_VAL_NOUSECLASS: String = 'NoUseClass'
REGSTR_VAL_NOINSTALLCLASS: String = 'NoInstallClass'
REGSTR_VAL_NODISPLAYCLASS: String = 'NoDisplayClass'
REGSTR_VAL_SILENTINSTALL: String = 'SilentInstall'
REGSTR_VAL_FSFILTERCLASS: String = 'FSFilterClass'
REGSTR_KEY_PCMCIA_CLASS: String = 'PCMCIA'
REGSTR_KEY_SCSI_CLASS: String = 'SCSIAdapter'
REGSTR_KEY_PORTS_CLASS: String = 'ports'
REGSTR_KEY_MEDIA_CLASS: String = 'MEDIA'
REGSTR_KEY_DISPLAY_CLASS: String = 'Display'
REGSTR_KEY_KEYBOARD_CLASS: String = 'Keyboard'
REGSTR_KEY_MOUSE_CLASS: String = 'Mouse'
REGSTR_KEY_MONITOR_CLASS: String = 'Monitor'
REGSTR_KEY_MODEM_CLASS: String = 'Modem'
REGSTR_VAL_PCMCIA_OPT: String = 'Options'
PCMCIA_OPT_HAVE_SOCKET: Int32 = 1
PCMCIA_OPT_AUTOMEM: Int32 = 4
PCMCIA_OPT_NO_SOUND: Int32 = 8
PCMCIA_OPT_NO_AUDIO: Int32 = 16
PCMCIA_OPT_NO_APMREMOVE: Int32 = 32
REGSTR_VAL_PCMCIA_MEM: String = 'Memory'
PCMCIA_DEF_MEMBEGIN: UInt32 = 786432
PCMCIA_DEF_MEMEND: UInt32 = 16777215
PCMCIA_DEF_MEMLEN: UInt32 = 4096
REGSTR_VAL_PCMCIA_ALLOC: String = 'AllocMemWin'
REGSTR_VAL_PCMCIA_ATAD: String = 'ATADelay'
REGSTR_VAL_PCMCIA_SIZ: String = 'MinRegionSize'
PCMCIA_DEF_MIN_REGION: UInt32 = 65536
REGSTR_VAL_P1284MDL: String = 'Model'
REGSTR_VAL_P1284MFG: String = 'Manufacturer'
REGSTR_VAL_ISAPNP: String = 'ISAPNP'
REGSTR_VAL_ISAPNP_RDP_OVERRIDE: String = 'RDPOverRide'
REGSTR_VAL_PCI: String = 'PCI'
REGSTR_PCI_OPTIONS: String = 'Options'
REGSTR_PCI_DUAL_IDE: String = 'PCIDualIDE'
PCI_OPTIONS_USE_BIOS: Int32 = 1
PCI_OPTIONS_USE_IRQ_STEERING: Int32 = 2
AGP_FLAG_NO_1X_RATE: Int32 = 1
AGP_FLAG_NO_2X_RATE: Int32 = 2
AGP_FLAG_NO_4X_RATE: Int32 = 4
AGP_FLAG_NO_8X_RATE: Int32 = 8
AGP_FLAG_REVERSE_INITIALIZATION: Int32 = 128
AGP_FLAG_NO_SBA_ENABLE: Int32 = 256
AGP_FLAG_NO_FW_ENABLE: Int32 = 512
AGP_FLAG_SPECIAL_TARGET: Int32 = 1048575
AGP_FLAG_SPECIAL_RESERVE: Int32 = 1015808
REGSTR_KEY_CRASHES: String = 'Crashes'
REGSTR_KEY_DANGERS: String = 'Dangers'
REGSTR_KEY_DETMODVARS: String = 'DetModVars'
REGSTR_KEY_NDISINFO: String = 'NDISInfo'
REGSTR_VAL_PROTINIPATH: String = 'ProtIniPath'
REGSTR_VAL_RESOURCES: String = 'Resources'
REGSTR_VAL_CRASHFUNCS: String = 'CrashFuncs'
REGSTR_VAL_CLASS: String = 'Class'
REGSTR_VAL_CLASSDESC: String = 'ClassDesc'
REGSTR_VAL_DEVDESC: String = 'DeviceDesc'
REGSTR_VAL_BOOTCONFIG: String = 'BootConfig'
REGSTR_VAL_DETFUNC: String = 'DetFunc'
REGSTR_VAL_DETFLAGS: String = 'DetFlags'
REGSTR_VAL_COMPATIBLEIDS: String = 'CompatibleIDs'
REGSTR_VAL_DETCONFIG: String = 'DetConfig'
REGSTR_VAL_VERIFYKEY: String = 'VerifyKey'
REGSTR_VAL_COMINFO: String = 'ComInfo'
REGSTR_VAL_INFNAME: String = 'InfName'
REGSTR_VAL_CARDSPECIFIC: String = 'CardSpecific'
REGSTR_VAL_NETOSTYPE: String = 'NetOSType'
REGSTR_DATA_NETOS_NDIS: String = 'NDIS'
REGSTR_DATA_NETOS_ODI: String = 'ODI'
REGSTR_DATA_NETOS_IPX: String = 'IPX'
REGSTR_VAL_MFG: String = 'Mfg'
REGSTR_VAL_SCAN_ONLY_FIRST: String = 'ScanOnlyFirstDrive'
REGSTR_VAL_SHARE_IRQ: String = 'ForceIRQSharing'
REGSTR_VAL_NONSTANDARD_ATAPI: String = 'NonStandardATAPI'
REGSTR_VAL_IDE_FORCE_SERIALIZE: String = 'ForceSerialization'
REGSTR_VAL_MAX_HCID_LEN: UInt32 = 1024
REGSTR_VAL_HWREV: String = 'HWRevision'
REGSTR_VAL_ENABLEINTS: String = 'EnableInts'
REGDF_NOTDETIO: UInt32 = 1
REGDF_NOTDETMEM: UInt32 = 2
REGDF_NOTDETIRQ: UInt32 = 4
REGDF_NOTDETDMA: UInt32 = 8
REGDF_NEEDFULLCONFIG: UInt32 = 16
REGDF_GENFORCEDCONFIG: UInt32 = 32
REGDF_NODETCONFIG: UInt32 = 32768
REGDF_CONFLICTIO: UInt32 = 65536
REGDF_CONFLICTMEM: UInt32 = 131072
REGDF_CONFLICTIRQ: UInt32 = 262144
REGDF_CONFLICTDMA: UInt32 = 524288
REGDF_MAPIRQ2TO9: UInt32 = 1048576
REGDF_NOTVERIFIED: UInt32 = 2147483648
REGSTR_VAL_APMBIOSVER: String = 'APMBiosVer'
REGSTR_VAL_APMFLAGS: String = 'APMFlags'
REGSTR_VAL_SLSUPPORT: String = 'SLSupport'
REGSTR_VAL_MACHINETYPE: String = 'MachineType'
REGSTR_VAL_SETUPMACHINETYPE: String = 'SetupMachineType'
REGSTR_MACHTYPE_UNKNOWN: String = 'Unknown'
REGSTR_MACHTYPE_IBMPC: String = 'IBM PC'
REGSTR_MACHTYPE_IBMPCJR: String = 'IBM PCjr'
REGSTR_MACHTYPE_IBMPCCONV: String = 'IBM PC Convertible'
REGSTR_MACHTYPE_IBMPCXT: String = 'IBM PC/XT'
REGSTR_MACHTYPE_IBMPCXT_286: String = 'IBM PC/XT 286'
REGSTR_MACHTYPE_IBMPCAT: String = 'IBM PC/AT'
REGSTR_MACHTYPE_IBMPS2_25: String = 'IBM PS/2-25'
REGSTR_MACHTYPE_IBMPS2_30_286: String = 'IBM PS/2-30 286'
REGSTR_MACHTYPE_IBMPS2_30: String = 'IBM PS/2-30'
REGSTR_MACHTYPE_IBMPS2_50: String = 'IBM PS/2-50'
REGSTR_MACHTYPE_IBMPS2_50Z: String = 'IBM PS/2-50Z'
REGSTR_MACHTYPE_IBMPS2_55SX: String = 'IBM PS/2-55SX'
REGSTR_MACHTYPE_IBMPS2_60: String = 'IBM PS/2-60'
REGSTR_MACHTYPE_IBMPS2_65SX: String = 'IBM PS/2-65SX'
REGSTR_MACHTYPE_IBMPS2_70: String = 'IBM PS/2-70'
REGSTR_MACHTYPE_IBMPS2_P70: String = 'IBM PS/2-P70'
REGSTR_MACHTYPE_IBMPS2_70_80: String = 'IBM PS/2-70/80'
REGSTR_MACHTYPE_IBMPS2_80: String = 'IBM PS/2-80'
REGSTR_MACHTYPE_IBMPS2_90: String = 'IBM PS/2-90'
REGSTR_MACHTYPE_IBMPS1: String = 'IBM PS/1'
REGSTR_MACHTYPE_PHOENIX_PCAT: String = 'Phoenix PC/AT Compatible'
REGSTR_MACHTYPE_HP_VECTRA: String = 'HP Vectra'
REGSTR_MACHTYPE_ATT_PC: String = 'AT&T PC'
REGSTR_MACHTYPE_ZENITH_PC: String = 'Zenith PC'
REGSTR_VAL_APMMENUSUSPEND: String = 'APMMenuSuspend'
APMMENUSUSPEND_DISABLED: UInt32 = 0
APMMENUSUSPEND_ENABLED: UInt32 = 1
APMMENUSUSPEND_UNDOCKED: UInt32 = 2
APMMENUSUSPEND_NOCHANGE: UInt32 = 128
REGSTR_VAL_APMACTIMEOUT: String = 'APMACTimeout'
REGSTR_VAL_APMBATTIMEOUT: String = 'APMBatTimeout'
APMTIMEOUT_DISABLED: UInt32 = 0
REGSTR_VAL_APMSHUTDOWNPOWER: String = 'APMShutDownPower'
REGSTR_VAL_BUSTYPE: String = 'BusType'
REGSTR_VAL_CPU: String = 'CPU'
REGSTR_VAL_NDP: String = 'NDP'
REGSTR_VAL_PNPBIOSVER: String = 'PnPBIOSVer'
REGSTR_VAL_PNPSTRUCOFFSET: String = 'PnPStrucOffset'
REGSTR_VAL_PCIBIOSVER: String = 'PCIBIOSVer'
REGSTR_VAL_HWMECHANISM: String = 'HWMechanism'
REGSTR_VAL_LASTPCIBUSNUM: String = 'LastPCIBusNum'
REGSTR_VAL_CONVMEM: String = 'ConvMem'
REGSTR_VAL_EXTMEM: String = 'ExtMem'
REGSTR_VAL_COMPUTERNAME: String = 'ComputerName'
REGSTR_VAL_BIOSNAME: String = 'BIOSName'
REGSTR_VAL_BIOSVERSION: String = 'BIOSVersion'
REGSTR_VAL_BIOSDATE: String = 'BIOSDate'
REGSTR_VAL_MODEL: String = 'Model'
REGSTR_VAL_SUBMODEL: String = 'Submodel'
REGSTR_VAL_REVISION: String = 'Revision'
REGSTR_VAL_FIFODEPTH: String = 'FIFODepth'
REGSTR_VAL_RDINTTHRESHOLD: String = 'RDIntThreshold'
REGSTR_VAL_WRINTTHRESHOLD: String = 'WRIntThreshold'
REGSTR_VAL_PRIORITY: String = 'Priority'
REGSTR_VAL_DRIVER: String = 'Driver'
REGSTR_VAL_FUNCDESC: String = 'FunctionDesc'
REGSTR_VAL_FORCEDCONFIG: String = 'ForcedConfig'
REGSTR_VAL_CONFIGFLAGS: String = 'ConfigFlags'
REGSTR_VAL_CSCONFIGFLAGS: String = 'CSConfigFlags'
CSCONFIGFLAG_BITS: UInt32 = 7
CSCONFIGFLAG_DISABLED: UInt32 = 1
CSCONFIGFLAG_DO_NOT_CREATE: UInt32 = 2
CSCONFIGFLAG_DO_NOT_START: UInt32 = 4
DMSTATEFLAG_APPLYTOALL: UInt32 = 1
REGSTR_VAL_ROOT_DEVNODE: String = 'HTREE\\ROOT\\0'
REGSTR_VAL_RESERVED_DEVNODE: String = 'HTREE\\RESERVED\\0'
REGSTR_PATH_MULTI_FUNCTION: String = 'MF'
REGSTR_VAL_RESOURCE_MAP: String = 'ResourceMap'
REGSTR_PATH_CHILD_PREFIX: String = 'Child'
NUM_RESOURCE_MAP: UInt32 = 256
REGSTR_VAL_MF_FLAGS: String = 'MFFlags'
MF_FLAGS_EVEN_IF_NO_RESOURCE: UInt32 = 1
MF_FLAGS_NO_CREATE_IF_NO_RESOURCE: UInt32 = 2
MF_FLAGS_FILL_IN_UNKNOWN_RESOURCE: UInt32 = 4
MF_FLAGS_CREATE_BUT_NO_SHOW_DISABLED: UInt32 = 8
REGSTR_VAL_EISA_RANGES: String = 'EISARanges'
REGSTR_VAL_EISA_FUNCTIONS: String = 'EISAFunctions'
REGSTR_VAL_EISA_FUNCTIONS_MASK: String = 'EISAFunctionsMask'
REGSTR_VAL_EISA_FLAGS: String = 'EISAFlags'
REGSTR_VAL_EISA_SIMULATE_INT15: String = 'EISASimulateInt15'
EISAFLAG_NO_IO_MERGE: UInt32 = 1
EISAFLAG_SLOT_IO_FIRST: UInt32 = 2
EISA_NO_MAX_FUNCTION: UInt32 = 255
NUM_EISA_RANGES: UInt32 = 4
REGSTR_VAL_DRVDESC: String = 'DriverDesc'
REGSTR_VAL_DEVLOADER: String = 'DevLoader'
REGSTR_VAL_STATICVXD: String = 'StaticVxD'
REGSTR_VAL_PROPERTIES: String = 'Properties'
REGSTR_VAL_MANUFACTURER: String = 'Manufacturer'
REGSTR_VAL_EXISTS: String = 'Exists'
REGSTR_VAL_CMENUMFLAGS: String = 'CMEnumFlags'
REGSTR_VAL_CMDRIVFLAGS: String = 'CMDrivFlags'
REGSTR_VAL_ENUMERATOR: String = 'Enumerator'
REGSTR_VAL_DEVICEDRIVER: String = 'DeviceDriver'
REGSTR_VAL_PORTNAME: String = 'PortName'
REGSTR_VAL_INFPATH: String = 'InfPath'
REGSTR_VAL_INFSECTION: String = 'InfSection'
REGSTR_VAL_INFSECTIONEXT: String = 'InfSectionExt'
REGSTR_VAL_POLLING: String = 'Polling'
REGSTR_VAL_DONTLOADIFCONFLICT: String = 'DontLoadIfConflict'
REGSTR_VAL_PORTSUBCLASS: String = 'PortSubClass'
REGSTR_VAL_NETCLEAN: String = 'NetClean'
REGSTR_VAL_IDE_NO_SERIALIZE: String = 'IDENoSerialize'
REGSTR_VAL_NOCMOSORFDPT: String = 'NoCMOSorFDPT'
REGSTR_VAL_COMVERIFYBASE: String = 'COMVerifyBase'
REGSTR_VAL_MATCHINGDEVID: String = 'MatchingDeviceId'
REGSTR_VAL_DRIVERDATE: String = 'DriverDate'
REGSTR_VAL_DRIVERDATEDATA: String = 'DriverDateData'
REGSTR_VAL_DRIVERVERSION: String = 'DriverVersion'
REGSTR_VAL_LOCATION_INFORMATION_OVERRIDE: String = 'LocationInformationOverride'
REGSTR_KEY_OVERRIDE: String = 'Override'
REGSTR_VAL_CONFIGMG: String = 'CONFIGMG'
REGSTR_VAL_SYSDM: String = 'SysDM'
REGSTR_VAL_SYSDMFUNC: String = 'SysDMFunc'
REGSTR_VAL_PRIVATE: String = 'Private'
REGSTR_VAL_PRIVATEFUNC: String = 'PrivateFunc'
REGSTR_VAL_DETECT: String = 'Detect'
REGSTR_VAL_DETECTFUNC: String = 'DetectFunc'
REGSTR_VAL_ASKFORCONFIG: String = 'AskForConfig'
REGSTR_VAL_ASKFORCONFIGFUNC: String = 'AskForConfigFunc'
REGSTR_VAL_WAITFORUNDOCK: String = 'WaitForUndock'
REGSTR_VAL_WAITFORUNDOCKFUNC: String = 'WaitForUndockFunc'
REGSTR_VAL_REMOVEROMOKAY: String = 'RemoveRomOkay'
REGSTR_VAL_REMOVEROMOKAYFUNC: String = 'RemoveRomOkayFunc'
REGSTR_VAL_CURCONFIG: String = 'CurrentConfig'
REGSTR_VAL_FRIENDLYNAME: String = 'FriendlyName'
REGSTR_VAL_CURRENTCONFIG: String = 'CurrentConfig'
REGSTR_VAL_MAP: String = 'Map'
REGSTR_VAL_ID: String = 'CurrentID'
REGSTR_VAL_DOCKED: String = 'CurrentDockedState'
REGSTR_VAL_CHECKSUM: String = 'CurrentChecksum'
REGSTR_VAL_HWDETECT: String = 'HardwareDetect'
REGSTR_VAL_INHIBITRESULTS: String = 'InhibitResults'
REGSTR_VAL_PROFILEFLAGS: String = 'ProfileFlags'
REGSTR_KEY_PCMCIA: String = 'PCMCIA\\'
REGSTR_KEY_PCUNKNOWN: String = 'UNKNOWN_MANUFACTURER'
REGSTR_VAL_PCSSDRIVER: String = 'Driver'
REGSTR_KEY_PCMTD: String = 'MTD-'
REGSTR_VAL_PCMTDRIVER: String = 'MTD'
REGSTR_VAL_HARDWAREID: String = 'HardwareID'
REGSTR_VAL_INSTALLER: String = 'Installer'
REGSTR_VAL_INSTALLER_32: String = 'Installer32'
REGSTR_VAL_INSICON: String = 'Icon'
REGSTR_VAL_ENUMPROPPAGES: String = 'EnumPropPages'
REGSTR_VAL_ENUMPROPPAGES_32: String = 'EnumPropPages32'
REGSTR_VAL_BASICPROPERTIES: String = 'BasicProperties'
REGSTR_VAL_BASICPROPERTIES_32: String = 'BasicProperties32'
REGSTR_VAL_COINSTALLERS_32: String = 'CoInstallers32'
REGSTR_VAL_PRIVATEPROBLEM: String = 'PrivateProblem'
REGSTR_KEY_CURRENT: String = 'Current'
REGSTR_KEY_DEFAULT: String = 'Default'
REGSTR_KEY_MODES: String = 'Modes'
REGSTR_VAL_MODE: String = 'Mode'
REGSTR_VAL_BPP: String = 'BPP'
REGSTR_VAL_HRES: String = 'HRes'
REGSTR_VAL_VRES: String = 'VRes'
REGSTR_VAL_FONTSIZE: String = 'FontSize'
REGSTR_VAL_DRV: String = 'drv'
REGSTR_VAL_GRB: String = 'grb'
REGSTR_VAL_VDD: String = 'vdd'
REGSTR_VAL_VER: String = 'Ver'
REGSTR_VAL_MAXRES: String = 'MaxResolution'
REGSTR_VAL_DPMS: String = 'DPMS'
REGSTR_VAL_RESUMERESET: String = 'ResumeReset'
REGSTR_KEY_SYSTEM: String = 'System'
REGSTR_KEY_USER: String = 'User'
REGSTR_VAL_DPI: String = 'dpi'
REGSTR_VAL_PCICOPTIONS: String = 'PCICOptions'
PCIC_DEFAULT_IRQMASK: UInt32 = 20152
PCIC_DEFAULT_NUMSOCKETS: UInt32 = 0
REGSTR_VAL_PCICIRQMAP: String = 'PCICIRQMap'
REGSTR_PATH_APPEARANCE: String = 'Control Panel\\Appearance'
REGSTR_PATH_LOOKSCHEMES: String = 'Control Panel\\Appearance\\Schemes'
REGSTR_VAL_CUSTOMCOLORS: String = 'CustomColors'
REGSTR_PATH_SCREENSAVE: String = 'Control Panel\\Desktop'
REGSTR_VALUE_USESCRPASSWORD: String = 'ScreenSaveUsePassword'
REGSTR_VALUE_SCRPASSWORD: String = 'ScreenSave_Data'
REGSTR_VALUE_LOWPOWERTIMEOUT: String = 'ScreenSaveLowPowerTimeout'
REGSTR_VALUE_POWEROFFTIMEOUT: String = 'ScreenSavePowerOffTimeout'
REGSTR_VALUE_LOWPOWERACTIVE: String = 'ScreenSaveLowPowerActive'
REGSTR_VALUE_POWEROFFACTIVE: String = 'ScreenSavePowerOffActive'
REGSTR_PATH_WINDOWSAPPLETS: String = 'Software\\Microsoft\\Windows\\CurrentVersion\\Applets'
REGSTR_PATH_SYSTRAY: String = 'Software\\Microsoft\\Windows\\CurrentVersion\\Applets\\SysTray'
REGSTR_VAL_SYSTRAYSVCS: String = 'Services'
REGSTR_VAL_SYSTRAYBATFLAGS: String = 'PowerFlags'
REGSTR_VAL_SYSTRAYPCCARDFLAGS: String = 'PCMCIAFlags'
REGSTR_PATH_NETWORK_USERSETTINGS: String = 'Network'
REGSTR_KEY_NETWORK_PERSISTENT: String = '\\Persistent'
REGSTR_KEY_NETWORK_RECENT: String = '\\Recent'
REGSTR_VAL_REMOTE_PATH: String = 'RemotePath'
REGSTR_VAL_USER_NAME: String = 'UserName'
REGSTR_VAL_PROVIDER_NAME: String = 'ProviderName'
REGSTR_VAL_CONNECTION_TYPE: String = 'ConnectionType'
REGSTR_VAL_UPGRADE: String = 'Upgrade'
REGSTR_KEY_LOGON: String = '\\Logon'
REGSTR_VAL_MUSTBEVALIDATED: String = 'MustBeValidated'
REGSTR_VAL_RUNLOGINSCRIPT: String = 'ProcessLoginScript'
REGSTR_KEY_NETWORKPROVIDER: String = '\\NetworkProvider'
REGSTR_VAL_AUTHENT_AGENT: String = 'AuthenticatingAgent'
REGSTR_VAL_PREFREDIR: String = 'PreferredRedir'
REGSTR_VAL_AUTOSTART: String = 'AutoStart'
REGSTR_VAL_AUTOLOGON: String = 'AutoLogon'
REGSTR_VAL_NETCARD: String = 'Netcard'
REGSTR_VAL_TRANSPORT: String = 'Transport'
REGSTR_VAL_DYNAMIC: String = 'Dynamic'
REGSTR_VAL_TRANSITION: String = 'Transition'
REGSTR_VAL_STATICDRIVE: String = 'StaticDrive'
REGSTR_VAL_LOADHI: String = 'LoadHi'
REGSTR_VAL_LOADRMDRIVERS: String = 'LoadRMDrivers'
REGSTR_VAL_SETUPN: String = 'SetupN'
REGSTR_VAL_SETUPNPATH: String = 'SetupNPath'
REGSTR_VAL_WRKGRP_FORCEMAPPING: String = 'WrkgrpForceMapping'
REGSTR_VAL_WRKGRP_REQUIRED: String = 'WrkgrpRequired'
REGSTR_PATH_CURRENT_CONTROL_SET: String = 'System\\CurrentControlSet\\Control'
REGSTR_VAL_CURRENT_USER: String = 'Current User'
REGSTR_PATH_PWDPROVIDER: String = 'System\\CurrentControlSet\\Control\\PwdProvider'
REGSTR_VAL_PWDPROVIDER_PATH: String = 'ProviderPath'
REGSTR_VAL_PWDPROVIDER_DESC: String = 'Description'
REGSTR_VAL_PWDPROVIDER_CHANGEPWD: String = 'ChangePassword'
REGSTR_VAL_PWDPROVIDER_CHANGEPWDHWND: String = 'ChangePasswordHwnd'
REGSTR_VAL_PWDPROVIDER_GETPWDSTATUS: String = 'GetPasswordStatus'
REGSTR_VAL_PWDPROVIDER_ISNP: String = 'NetworkProvider'
REGSTR_VAL_PWDPROVIDER_CHANGEORDER: String = 'ChangeOrder'
REGSTR_PATH_POLICIES: String = 'Software\\Microsoft\\Windows\\CurrentVersion\\Policies'
REGSTR_PATH_UPDATE: String = 'System\\CurrentControlSet\\Control\\Update'
REGSTR_VALUE_ENABLE: String = 'Enable'
REGSTR_VALUE_VERBOSE: String = 'Verbose'
REGSTR_VALUE_NETPATH: String = 'NetworkPath'
REGSTR_VALUE_DEFAULTLOC: String = 'UseDefaultNetLocation'
REGSTR_KEY_NETWORK: String = 'Network'
REGSTR_KEY_PRINTERS: String = 'Printers'
REGSTR_KEY_WINOLDAPP: String = 'WinOldApp'
REGSTR_KEY_EXPLORER: String = 'Explorer'
REGSTR_VAL_NOFILESHARING: String = 'NoFileSharing'
REGSTR_VAL_NOPRINTSHARING: String = 'NoPrintSharing'
REGSTR_VAL_NOFILESHARINGCTRL: String = 'NoFileSharingControl'
REGSTR_VAL_NOPRINTSHARINGCTRL: String = 'NoPrintSharingControl'
REGSTR_VAL_HIDESHAREPWDS: String = 'HideSharePwds'
REGSTR_VAL_DISABLEPWDCACHING: String = 'DisablePwdCaching'
REGSTR_VAL_ALPHANUMPWDS: String = 'AlphanumPwds'
REGSTR_VAL_NETSETUP_DISABLE: String = 'NoNetSetup'
REGSTR_VAL_NETSETUP_NOCONFIGPAGE: String = 'NoNetSetupConfigPage'
REGSTR_VAL_NETSETUP_NOIDPAGE: String = 'NoNetSetupIDPage'
REGSTR_VAL_NETSETUP_NOSECURITYPAGE: String = 'NoNetSetupSecurityPage'
REGSTR_VAL_SYSTEMCPL_NOVIRTMEMPAGE: String = 'NoVirtMemPage'
REGSTR_VAL_SYSTEMCPL_NODEVMGRPAGE: String = 'NoDevMgrPage'
REGSTR_VAL_SYSTEMCPL_NOCONFIGPAGE: String = 'NoConfigPage'
REGSTR_VAL_SYSTEMCPL_NOFILESYSPAGE: String = 'NoFileSysPage'
REGSTR_VAL_DISPCPL_NODISPCPL: String = 'NoDispCPL'
REGSTR_VAL_DISPCPL_NOBACKGROUNDPAGE: String = 'NoDispBackgroundPage'
REGSTR_VAL_DISPCPL_NOSCRSAVPAGE: String = 'NoDispScrSavPage'
REGSTR_VAL_DISPCPL_NOAPPEARANCEPAGE: String = 'NoDispAppearancePage'
REGSTR_VAL_DISPCPL_NOSETTINGSPAGE: String = 'NoDispSettingsPage'
REGSTR_VAL_SECCPL_NOSECCPL: String = 'NoSecCPL'
REGSTR_VAL_SECCPL_NOPWDPAGE: String = 'NoPwdPage'
REGSTR_VAL_SECCPL_NOADMINPAGE: String = 'NoAdminPage'
REGSTR_VAL_SECCPL_NOPROFILEPAGE: String = 'NoProfilePage'
REGSTR_VAL_PRINTERS_HIDETABS: String = 'NoPrinterTabs'
REGSTR_VAL_PRINTERS_NODELETE: String = 'NoDeletePrinter'
REGSTR_VAL_PRINTERS_NOADD: String = 'NoAddPrinter'
REGSTR_VAL_WINOLDAPP_DISABLED: String = 'Disabled'
REGSTR_VAL_WINOLDAPP_NOREALMODE: String = 'NoRealMode'
REGSTR_VAL_NOENTIRENETWORK: String = 'NoEntireNetwork'
REGSTR_VAL_NOWORKGROUPCONTENTS: String = 'NoWorkgroupContents'
REGSTR_VAL_UNDOCK_WITHOUT_LOGON: String = 'UndockWithoutLogon'
REGSTR_VAL_MINPWDLEN: String = 'MinPwdLen'
REGSTR_VAL_PWDEXPIRATION: String = 'PwdExpiration'
REGSTR_VAL_WIN31PROVIDER: String = 'Win31Provider'
REGSTR_VAL_DISABLEREGTOOLS: String = 'DisableRegistryTools'
REGSTR_PATH_WINLOGON: String = 'Software\\Microsoft\\Windows\\CurrentVersion\\Winlogon'
REGSTR_VAL_LEGALNOTICECAPTION: String = 'LegalNoticeCaption'
REGSTR_VAL_LEGALNOTICETEXT: String = 'LegalNoticeText'
REGSTR_VAL_DRIVE_SPINDOWN: String = 'NoDispSpinDown'
REGSTR_VAL_SHUTDOWN_FLAGS: String = 'ShutdownFlags'
REGSTR_VAL_RESTRICTRUN: String = 'RestrictRun'
REGSTR_KEY_POL_USERS: String = 'Users'
REGSTR_KEY_POL_COMPUTERS: String = 'Computers'
REGSTR_KEY_POL_USERGROUPS: String = 'UserGroups'
REGSTR_KEY_POL_DEFAULT: String = '.default'
REGSTR_KEY_POL_USERGROUPDATA: String = 'GroupData\\UserGroups\\Priority'
REGSTR_PATH_TIMEZONE: String = 'System\\CurrentControlSet\\Control\\TimeZoneInformation'
REGSTR_VAL_TZBIAS: String = 'Bias'
REGSTR_VAL_TZDLTBIAS: String = 'DaylightBias'
REGSTR_VAL_TZSTDBIAS: String = 'StandardBias'
REGSTR_VAL_TZACTBIAS: String = 'ActiveTimeBias'
REGSTR_VAL_TZDLTFLAG: String = 'DaylightFlag'
REGSTR_VAL_TZSTDSTART: String = 'StandardStart'
REGSTR_VAL_TZDLTSTART: String = 'DaylightStart'
REGSTR_VAL_TZDLTNAME: String = 'DaylightName'
REGSTR_VAL_TZSTDNAME: String = 'StandardName'
REGSTR_VAL_TZNOCHANGESTART: String = 'NoChangeStart'
REGSTR_VAL_TZNOCHANGEEND: String = 'NoChangeEnd'
REGSTR_VAL_TZNOAUTOTIME: String = 'DisableAutoDaylightTimeSet'
REGSTR_PATH_FLOATINGPOINTPROCESSOR: String = 'HARDWARE\\DESCRIPTION\\System\\FloatingPointProcessor'
REGSTR_PATH_FLOATINGPOINTPROCESSOR0: String = 'HARDWARE\\DESCRIPTION\\System\\FloatingPointProcessor\\0'
REGSTR_PATH_COMPUTRNAME: String = 'System\\CurrentControlSet\\Control\\ComputerName\\ComputerName'
REGSTR_VAL_COMPUTRNAME: String = 'ComputerName'
REGSTR_PATH_SHUTDOWN: String = 'System\\CurrentControlSet\\Control\\Shutdown'
REGSTR_VAL_FORCEREBOOT: String = 'ForceReboot'
REGSTR_VAL_SETUPPROGRAMRAN: String = 'SetupProgramRan'
REGSTR_VAL_DOES_POLLING: String = 'PollingSupportNeeded'
REGSTR_PATH_KNOWNDLLS: String = 'System\\CurrentControlSet\\Control\\SessionManager\\KnownDLLs'
REGSTR_PATH_KNOWN16DLLS: String = 'System\\CurrentControlSet\\Control\\SessionManager\\Known16DLLs'
REGSTR_PATH_CHECKVERDLLS: String = 'System\\CurrentControlSet\\Control\\SessionManager\\CheckVerDLLs'
REGSTR_PATH_WARNVERDLLS: String = 'System\\CurrentControlSet\\Control\\SessionManager\\WarnVerDLLs'
REGSTR_PATH_HACKINIFILE: String = 'System\\CurrentControlSet\\Control\\SessionManager\\HackIniFiles'
REGSTR_PATH_CHECKBADAPPS: String = 'System\\CurrentControlSet\\Control\\SessionManager\\CheckBadApps'
REGSTR_PATH_APPPATCH: String = 'System\\CurrentControlSet\\Control\\SessionManager\\AppPatches'
REGSTR_PATH_CHECKBADAPPS400: String = 'System\\CurrentControlSet\\Control\\SessionManager\\CheckBadApps400'
REGSTR_PATH_KNOWNVXDS: String = 'System\\CurrentControlSet\\Control\\SessionManager\\KnownVxDs'
REGSTR_VAL_UNINSTALLER_DISPLAYNAME: String = 'DisplayName'
REGSTR_VAL_UNINSTALLER_COMMANDLINE: String = 'UninstallString'
REGSTR_VAL_REINSTALL_DISPLAYNAME: String = 'DisplayName'
REGSTR_VAL_REINSTALL_STRING: String = 'ReinstallString'
REGSTR_VAL_REINSTALL_DEVICEINSTANCEIDS: String = 'DeviceInstanceIds'
REGSTR_PATH_DESKTOP: String = 'Control Panel\\Desktop'
REGSTR_PATH_MOUSE: String = 'Control Panel\\Mouse'
REGSTR_PATH_KEYBOARD: String = 'Control Panel\\Keyboard'
REGSTR_PATH_COLORS: String = 'Control Panel\\Colors'
REGSTR_PATH_SOUND: String = 'Control Panel\\Sound'
REGSTR_PATH_METRICS: String = 'Control Panel\\Desktop\\WindowMetrics'
REGSTR_PATH_ICONS: String = 'Control Panel\\Icons'
REGSTR_PATH_CURSORS: String = 'Control Panel\\Cursors'
REGSTR_PATH_CHECKDISK: String = 'Software\\Microsoft\\Windows\\CurrentVersion\\Applets\\Check Drive'
REGSTR_PATH_CHECKDISKSET: String = 'Settings'
REGSTR_PATH_CHECKDISKUDRVS: String = 'NoUnknownDDErrDrvs'
REGSTR_PATH_FAULT: String = 'Software\\Microsoft\\Windows\\CurrentVersion\\Fault'
REGSTR_VAL_FAULT_LOGFILE: String = 'LogFile'
REGSTR_PATH_AEDEBUG: String = 'Software\\Microsoft\\Windows NT\\CurrentVersion\\AeDebug'
REGSTR_VAL_AEDEBUG_DEBUGGER: String = 'Debugger'
REGSTR_VAL_AEDEBUG_AUTO: String = 'Auto'
REGSTR_PATH_GRPCONV: String = 'Software\\Microsoft\\Windows\\CurrentVersion\\GrpConv'
REGSTR_VAL_REGITEMDELETEMESSAGE: String = 'Removal Message'
REGSTR_PATH_LASTCHECK: String = 'Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\LastCheck'
REGSTR_PATH_LASTOPTIMIZE: String = 'Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\LastOptimize'
REGSTR_PATH_LASTBACKUP: String = 'Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\LastBackup'
REGSTR_PATH_CHKLASTCHECK: String = 'Software\\Microsoft\\Windows\\CurrentVersion\\Applets\\Check Drive\\LastCheck'
REGSTR_PATH_CHKLASTSURFAN: String = 'Software\\Microsoft\\Windows\\CurrentVersion\\Applets\\Check Drive\\LastSurfaceAnalysis'
DTRESULTOK: UInt32 = 0
DTRESULTFIX: UInt32 = 1
DTRESULTPROB: UInt32 = 2
DTRESULTPART: UInt32 = 3
REGSTR_KEY_SHARES: String = 'Software\\Microsoft\\Windows\\CurrentVersion\\Network\\LanMan'
REGSTR_VAL_SHARES_FLAGS: String = 'Flags'
REGSTR_VAL_SHARES_TYPE: String = 'Type'
REGSTR_VAL_SHARES_PATH: String = 'Path'
REGSTR_VAL_SHARES_REMARK: String = 'Remark'
REGSTR_VAL_SHARES_RW_PASS: String = 'Parm1'
REGSTR_VAL_SHARES_RO_PASS: String = 'Parm2'
REGSTR_PATH_PRINT: String = 'System\\CurrentControlSet\\Control\\Print'
REGSTR_PATH_PRINTERS: String = 'System\\CurrentControlSet\\Control\\Print\\Printers'
REGSTR_PATH_PROVIDERS: String = 'System\\CurrentControlSet\\Control\\Print\\Providers'
REGSTR_PATH_MONITORS: String = 'System\\CurrentControlSet\\Control\\Print\\Monitors'
REGSTR_PATH_ENVIRONMENTS: String = 'System\\CurrentControlSet\\Control\\Print\\Environments'
REGSTR_VAL_START_ON_BOOT: String = 'StartOnBoot'
REGSTR_VAL_PRINTERS_MASK: String = 'PrintersMask'
REGSTR_VAL_DOS_SPOOL_MASK: String = 'DOSSpoolMask'
REGSTR_KEY_CURRENT_ENV: String = '\\Windows 4.0'
REGSTR_KEY_DRIVERS: String = '\\Drivers'
REGSTR_KEY_PRINT_PROC: String = '\\Print Processors'
REGSTR_PATH_EVENTLABELS: String = 'AppEvents\\EventLabels'
REGSTR_PATH_SCHEMES: String = 'AppEvents\\Schemes'
REGSTR_PATH_MULTIMEDIA_AUDIO: String = 'Software\\Microsoft\\Multimedia\\Audio'
REGSTR_KEY_JOYCURR: String = 'CurrentJoystickSettings'
REGSTR_KEY_JOYSETTINGS: String = 'JoystickSettings'
REGSTR_VAL_JOYUSERVALUES: String = 'JoystickUserValues'
REGSTR_VAL_JOYCALLOUT: String = 'JoystickCallout'
REGSTR_VAL_JOYNCONFIG: String = 'Joystick%dConfiguration'
REGSTR_VAL_JOYNOEMNAME: String = 'Joystick%dOEMName'
REGSTR_VAL_JOYNOEMCALLOUT: String = 'Joystick%dOEMCallout'
REGSTR_VAL_JOYOEMCALLOUT: String = 'OEMCallout'
REGSTR_VAL_JOYOEMNAME: String = 'OEMName'
REGSTR_VAL_JOYOEMDATA: String = 'OEMData'
REGSTR_VAL_JOYOEMXYLABEL: String = 'OEMXYLabel'
REGSTR_VAL_JOYOEMZLABEL: String = 'OEMZLabel'
REGSTR_VAL_JOYOEMRLABEL: String = 'OEMRLabel'
REGSTR_VAL_JOYOEMPOVLABEL: String = 'OEMPOVLabel'
REGSTR_VAL_JOYOEMULABEL: String = 'OEMULabel'
REGSTR_VAL_JOYOEMVLABEL: String = 'OEMVLabel'
REGSTR_VAL_JOYOEMTESTMOVEDESC: String = 'OEMTestMoveDesc'
REGSTR_VAL_JOYOEMTESTBUTTONDESC: String = 'OEMTestButtonDesc'
REGSTR_VAL_JOYOEMTESTMOVECAP: String = 'OEMTestMoveCap'
REGSTR_VAL_JOYOEMTESTBUTTONCAP: String = 'OEMTestButtonCap'
REGSTR_VAL_JOYOEMTESTWINCAP: String = 'OEMTestWinCap'
REGSTR_VAL_JOYOEMCALCAP: String = 'OEMCalCap'
REGSTR_VAL_JOYOEMCALWINCAP: String = 'OEMCalWinCap'
REGSTR_VAL_JOYOEMCAL1: String = 'OEMCal1'
REGSTR_VAL_JOYOEMCAL2: String = 'OEMCal2'
REGSTR_VAL_JOYOEMCAL3: String = 'OEMCal3'
REGSTR_VAL_JOYOEMCAL4: String = 'OEMCal4'
REGSTR_VAL_JOYOEMCAL5: String = 'OEMCal5'
REGSTR_VAL_JOYOEMCAL6: String = 'OEMCal6'
REGSTR_VAL_JOYOEMCAL7: String = 'OEMCal7'
REGSTR_VAL_JOYOEMCAL8: String = 'OEMCal8'
REGSTR_VAL_JOYOEMCAL9: String = 'OEMCal9'
REGSTR_VAL_JOYOEMCAL10: String = 'OEMCal10'
REGSTR_VAL_JOYOEMCAL11: String = 'OEMCal11'
REGSTR_VAL_JOYOEMCAL12: String = 'OEMCal12'
REGSTR_VAL_AUDIO_BITMAP: String = 'bitmap'
REGSTR_VAL_AUDIO_ICON: String = 'icon'
REGSTR_PATH_DEVICEINSTALLER: String = 'Software\\Microsoft\\Windows\\CurrentVersion\\Device Installer'
REGSTR_PATH_DIFX: String = 'Software\\Microsoft\\Windows\\CurrentVersion\\DIFX'
REGSTR_VAL_SEARCHOPTIONS: String = 'SearchOptions'
REGSTR_PATH_BIOSINFO: String = 'System\\CurrentControlSet\\Control\\BiosInfo'
REGSTR_PATH_PCIIR: String = 'System\\CurrentControlSet\\Control\\Pnp\\PciIrqRouting'
REGSTR_VAL_OPTIONS: String = 'Options'
REGSTR_VAL_STAT: String = 'Status'
REGSTR_VAL_TABLE_STAT: String = 'TableStatus'
REGSTR_VAL_MINIPORT_STAT: String = 'MiniportStatus'
PIR_OPTION_ENABLED: UInt32 = 1
PIR_OPTION_REGISTRY: UInt32 = 2
PIR_OPTION_MSSPEC: UInt32 = 4
PIR_OPTION_REALMODE: UInt32 = 8
PIR_OPTION_DEFAULT: UInt32 = 15
PIR_STATUS_ERROR: UInt32 = 0
PIR_STATUS_ENABLED: UInt32 = 1
PIR_STATUS_DISABLED: UInt32 = 2
PIR_STATUS_MAX: UInt32 = 3
PIR_STATUS_TABLE_REGISTRY: UInt32 = 0
PIR_STATUS_TABLE_MSSPEC: UInt32 = 1
PIR_STATUS_TABLE_REALMODE: UInt32 = 2
PIR_STATUS_TABLE_NONE: UInt32 = 3
PIR_STATUS_TABLE_ERROR: UInt32 = 4
PIR_STATUS_TABLE_BAD: UInt32 = 5
PIR_STATUS_TABLE_SUCCESS: UInt32 = 6
PIR_STATUS_TABLE_MAX: UInt32 = 7
PIR_STATUS_MINIPORT_NORMAL: UInt32 = 0
PIR_STATUS_MINIPORT_COMPATIBLE: UInt32 = 1
PIR_STATUS_MINIPORT_OVERRIDE: UInt32 = 2
PIR_STATUS_MINIPORT_NONE: UInt32 = 3
PIR_STATUS_MINIPORT_ERROR: UInt32 = 4
PIR_STATUS_MINIPORT_NOKEY: UInt32 = 5
PIR_STATUS_MINIPORT_SUCCESS: UInt32 = 6
PIR_STATUS_MINIPORT_INVALID: UInt32 = 7
PIR_STATUS_MINIPORT_MAX: UInt32 = 8
REGSTR_PATH_LASTGOOD: String = 'System\\LastKnownGoodRecovery\\LastGood'
REGSTR_PATH_LASTGOODTMP: String = 'System\\LastKnownGoodRecovery\\LastGood.Tmp'
LASTGOOD_OPERATION: UInt32 = 255
LASTGOOD_OPERATION_NOPOSTPROC: UInt32 = 0
LASTGOOD_OPERATION_DELETE: UInt32 = 1
@winfunctype('ADVAPI32.dll')
def RegCloseKey(hKey: win32more.Windows.Win32.System.Registry.HKEY) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RegOverridePredefKey(hKey: win32more.Windows.Win32.System.Registry.HKEY, hNewHKey: win32more.Windows.Win32.System.Registry.HKEY) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RegOpenUserClassesRoot(hToken: win32more.Windows.Win32.Foundation.HANDLE, dwOptions: UInt32, samDesired: UInt32, phkResult: POINTER(win32more.Windows.Win32.System.Registry.HKEY)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RegOpenCurrentUser(samDesired: UInt32, phkResult: POINTER(win32more.Windows.Win32.System.Registry.HKEY)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RegDisablePredefinedCache() -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RegDisablePredefinedCacheEx() -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RegConnectRegistryA(lpMachineName: win32more.Windows.Win32.Foundation.PSTR, hKey: win32more.Windows.Win32.System.Registry.HKEY, phkResult: POINTER(win32more.Windows.Win32.System.Registry.HKEY)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RegConnectRegistryW(lpMachineName: win32more.Windows.Win32.Foundation.PWSTR, hKey: win32more.Windows.Win32.System.Registry.HKEY, phkResult: POINTER(win32more.Windows.Win32.System.Registry.HKEY)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
RegConnectRegistry = UnicodeAlias('RegConnectRegistryW')
@winfunctype('ADVAPI32.dll')
def RegConnectRegistryExA(lpMachineName: win32more.Windows.Win32.Foundation.PSTR, hKey: win32more.Windows.Win32.System.Registry.HKEY, Flags: UInt32, phkResult: POINTER(win32more.Windows.Win32.System.Registry.HKEY)) -> Int32: ...
@winfunctype('ADVAPI32.dll')
def RegConnectRegistryExW(lpMachineName: win32more.Windows.Win32.Foundation.PWSTR, hKey: win32more.Windows.Win32.System.Registry.HKEY, Flags: UInt32, phkResult: POINTER(win32more.Windows.Win32.System.Registry.HKEY)) -> Int32: ...
RegConnectRegistryEx = UnicodeAlias('RegConnectRegistryExW')
@winfunctype('ADVAPI32.dll')
def RegCreateKeyA(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpSubKey: win32more.Windows.Win32.Foundation.PSTR, phkResult: POINTER(win32more.Windows.Win32.System.Registry.HKEY)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RegCreateKeyW(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpSubKey: win32more.Windows.Win32.Foundation.PWSTR, phkResult: POINTER(win32more.Windows.Win32.System.Registry.HKEY)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
RegCreateKey = UnicodeAlias('RegCreateKeyW')
@winfunctype('ADVAPI32.dll')
def RegCreateKeyExA(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpSubKey: win32more.Windows.Win32.Foundation.PSTR, Reserved: UInt32, lpClass: win32more.Windows.Win32.Foundation.PSTR, dwOptions: win32more.Windows.Win32.System.Registry.REG_OPEN_CREATE_OPTIONS, samDesired: win32more.Windows.Win32.System.Registry.REG_SAM_FLAGS, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), phkResult: POINTER(win32more.Windows.Win32.System.Registry.HKEY), lpdwDisposition: POINTER(win32more.Windows.Win32.System.Registry.REG_CREATE_KEY_DISPOSITION)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RegCreateKeyExW(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpSubKey: win32more.Windows.Win32.Foundation.PWSTR, Reserved: UInt32, lpClass: win32more.Windows.Win32.Foundation.PWSTR, dwOptions: win32more.Windows.Win32.System.Registry.REG_OPEN_CREATE_OPTIONS, samDesired: win32more.Windows.Win32.System.Registry.REG_SAM_FLAGS, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), phkResult: POINTER(win32more.Windows.Win32.System.Registry.HKEY), lpdwDisposition: POINTER(win32more.Windows.Win32.System.Registry.REG_CREATE_KEY_DISPOSITION)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
RegCreateKeyEx = UnicodeAlias('RegCreateKeyExW')
@winfunctype('ADVAPI32.dll')
def RegCreateKeyTransactedA(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpSubKey: win32more.Windows.Win32.Foundation.PSTR, Reserved: UInt32, lpClass: win32more.Windows.Win32.Foundation.PSTR, dwOptions: win32more.Windows.Win32.System.Registry.REG_OPEN_CREATE_OPTIONS, samDesired: win32more.Windows.Win32.System.Registry.REG_SAM_FLAGS, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), phkResult: POINTER(win32more.Windows.Win32.System.Registry.HKEY), lpdwDisposition: POINTER(win32more.Windows.Win32.System.Registry.REG_CREATE_KEY_DISPOSITION), hTransaction: win32more.Windows.Win32.Foundation.HANDLE, pExtendedParemeter: VoidPtr) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RegCreateKeyTransactedW(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpSubKey: win32more.Windows.Win32.Foundation.PWSTR, Reserved: UInt32, lpClass: win32more.Windows.Win32.Foundation.PWSTR, dwOptions: win32more.Windows.Win32.System.Registry.REG_OPEN_CREATE_OPTIONS, samDesired: win32more.Windows.Win32.System.Registry.REG_SAM_FLAGS, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), phkResult: POINTER(win32more.Windows.Win32.System.Registry.HKEY), lpdwDisposition: POINTER(win32more.Windows.Win32.System.Registry.REG_CREATE_KEY_DISPOSITION), hTransaction: win32more.Windows.Win32.Foundation.HANDLE, pExtendedParemeter: VoidPtr) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
RegCreateKeyTransacted = UnicodeAlias('RegCreateKeyTransactedW')
@winfunctype('ADVAPI32.dll')
def RegDeleteKeyA(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpSubKey: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RegDeleteKeyW(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpSubKey: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
RegDeleteKey = UnicodeAlias('RegDeleteKeyW')
@winfunctype('ADVAPI32.dll')
def RegDeleteKeyExA(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpSubKey: win32more.Windows.Win32.Foundation.PSTR, samDesired: UInt32, Reserved: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RegDeleteKeyExW(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpSubKey: win32more.Windows.Win32.Foundation.PWSTR, samDesired: UInt32, Reserved: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
RegDeleteKeyEx = UnicodeAlias('RegDeleteKeyExW')
@winfunctype('ADVAPI32.dll')
def RegDeleteKeyTransactedA(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpSubKey: win32more.Windows.Win32.Foundation.PSTR, samDesired: UInt32, Reserved: UInt32, hTransaction: win32more.Windows.Win32.Foundation.HANDLE, pExtendedParameter: VoidPtr) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RegDeleteKeyTransactedW(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpSubKey: win32more.Windows.Win32.Foundation.PWSTR, samDesired: UInt32, Reserved: UInt32, hTransaction: win32more.Windows.Win32.Foundation.HANDLE, pExtendedParameter: VoidPtr) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
RegDeleteKeyTransacted = UnicodeAlias('RegDeleteKeyTransactedW')
@winfunctype('ADVAPI32.dll')
def RegDisableReflectionKey(hBase: win32more.Windows.Win32.System.Registry.HKEY) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RegEnableReflectionKey(hBase: win32more.Windows.Win32.System.Registry.HKEY) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RegQueryReflectionKey(hBase: win32more.Windows.Win32.System.Registry.HKEY, bIsReflectionDisabled: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RegDeleteValueA(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpValueName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RegDeleteValueW(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpValueName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
RegDeleteValue = UnicodeAlias('RegDeleteValueW')
@winfunctype('ADVAPI32.dll')
def RegEnumKeyA(hKey: win32more.Windows.Win32.System.Registry.HKEY, dwIndex: UInt32, lpName: win32more.Windows.Win32.Foundation.PSTR, cchName: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RegEnumKeyW(hKey: win32more.Windows.Win32.System.Registry.HKEY, dwIndex: UInt32, lpName: win32more.Windows.Win32.Foundation.PWSTR, cchName: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
RegEnumKey = UnicodeAlias('RegEnumKeyW')
@winfunctype('ADVAPI32.dll')
def RegEnumKeyExA(hKey: win32more.Windows.Win32.System.Registry.HKEY, dwIndex: UInt32, lpName: win32more.Windows.Win32.Foundation.PSTR, lpcchName: POINTER(UInt32), lpReserved: POINTER(UInt32), lpClass: win32more.Windows.Win32.Foundation.PSTR, lpcchClass: POINTER(UInt32), lpftLastWriteTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RegEnumKeyExW(hKey: win32more.Windows.Win32.System.Registry.HKEY, dwIndex: UInt32, lpName: win32more.Windows.Win32.Foundation.PWSTR, lpcchName: POINTER(UInt32), lpReserved: POINTER(UInt32), lpClass: win32more.Windows.Win32.Foundation.PWSTR, lpcchClass: POINTER(UInt32), lpftLastWriteTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
RegEnumKeyEx = UnicodeAlias('RegEnumKeyExW')
@winfunctype('ADVAPI32.dll')
def RegEnumValueA(hKey: win32more.Windows.Win32.System.Registry.HKEY, dwIndex: UInt32, lpValueName: win32more.Windows.Win32.Foundation.PSTR, lpcchValueName: POINTER(UInt32), lpReserved: POINTER(UInt32), lpType: POINTER(UInt32), lpData: POINTER(Byte), lpcbData: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RegEnumValueW(hKey: win32more.Windows.Win32.System.Registry.HKEY, dwIndex: UInt32, lpValueName: win32more.Windows.Win32.Foundation.PWSTR, lpcchValueName: POINTER(UInt32), lpReserved: POINTER(UInt32), lpType: POINTER(UInt32), lpData: POINTER(Byte), lpcbData: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
RegEnumValue = UnicodeAlias('RegEnumValueW')
@winfunctype('ADVAPI32.dll')
def RegFlushKey(hKey: win32more.Windows.Win32.System.Registry.HKEY) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RegGetKeySecurity(hKey: win32more.Windows.Win32.System.Registry.HKEY, SecurityInformation: win32more.Windows.Win32.Security.OBJECT_SECURITY_INFORMATION, pSecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, lpcbSecurityDescriptor: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RegLoadKeyA(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpSubKey: win32more.Windows.Win32.Foundation.PSTR, lpFile: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RegLoadKeyW(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpSubKey: win32more.Windows.Win32.Foundation.PWSTR, lpFile: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
RegLoadKey = UnicodeAlias('RegLoadKeyW')
@winfunctype('ADVAPI32.dll')
def RegNotifyChangeKeyValue(hKey: win32more.Windows.Win32.System.Registry.HKEY, bWatchSubtree: win32more.Windows.Win32.Foundation.BOOL, dwNotifyFilter: win32more.Windows.Win32.System.Registry.REG_NOTIFY_FILTER, hEvent: win32more.Windows.Win32.Foundation.HANDLE, fAsynchronous: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RegOpenKeyA(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpSubKey: win32more.Windows.Win32.Foundation.PSTR, phkResult: POINTER(win32more.Windows.Win32.System.Registry.HKEY)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RegOpenKeyW(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpSubKey: win32more.Windows.Win32.Foundation.PWSTR, phkResult: POINTER(win32more.Windows.Win32.System.Registry.HKEY)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
RegOpenKey = UnicodeAlias('RegOpenKeyW')
@winfunctype('ADVAPI32.dll')
def RegOpenKeyExA(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpSubKey: win32more.Windows.Win32.Foundation.PSTR, ulOptions: UInt32, samDesired: win32more.Windows.Win32.System.Registry.REG_SAM_FLAGS, phkResult: POINTER(win32more.Windows.Win32.System.Registry.HKEY)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RegOpenKeyExW(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpSubKey: win32more.Windows.Win32.Foundation.PWSTR, ulOptions: UInt32, samDesired: win32more.Windows.Win32.System.Registry.REG_SAM_FLAGS, phkResult: POINTER(win32more.Windows.Win32.System.Registry.HKEY)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
RegOpenKeyEx = UnicodeAlias('RegOpenKeyExW')
@winfunctype('ADVAPI32.dll')
def RegOpenKeyTransactedA(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpSubKey: win32more.Windows.Win32.Foundation.PSTR, ulOptions: UInt32, samDesired: win32more.Windows.Win32.System.Registry.REG_SAM_FLAGS, phkResult: POINTER(win32more.Windows.Win32.System.Registry.HKEY), hTransaction: win32more.Windows.Win32.Foundation.HANDLE, pExtendedParemeter: VoidPtr) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RegOpenKeyTransactedW(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpSubKey: win32more.Windows.Win32.Foundation.PWSTR, ulOptions: UInt32, samDesired: win32more.Windows.Win32.System.Registry.REG_SAM_FLAGS, phkResult: POINTER(win32more.Windows.Win32.System.Registry.HKEY), hTransaction: win32more.Windows.Win32.Foundation.HANDLE, pExtendedParemeter: VoidPtr) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
RegOpenKeyTransacted = UnicodeAlias('RegOpenKeyTransactedW')
@winfunctype('ADVAPI32.dll')
def RegQueryInfoKeyA(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpClass: win32more.Windows.Win32.Foundation.PSTR, lpcchClass: POINTER(UInt32), lpReserved: POINTER(UInt32), lpcSubKeys: POINTER(UInt32), lpcbMaxSubKeyLen: POINTER(UInt32), lpcbMaxClassLen: POINTER(UInt32), lpcValues: POINTER(UInt32), lpcbMaxValueNameLen: POINTER(UInt32), lpcbMaxValueLen: POINTER(UInt32), lpcbSecurityDescriptor: POINTER(UInt32), lpftLastWriteTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RegQueryInfoKeyW(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpClass: win32more.Windows.Win32.Foundation.PWSTR, lpcchClass: POINTER(UInt32), lpReserved: POINTER(UInt32), lpcSubKeys: POINTER(UInt32), lpcbMaxSubKeyLen: POINTER(UInt32), lpcbMaxClassLen: POINTER(UInt32), lpcValues: POINTER(UInt32), lpcbMaxValueNameLen: POINTER(UInt32), lpcbMaxValueLen: POINTER(UInt32), lpcbSecurityDescriptor: POINTER(UInt32), lpftLastWriteTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
RegQueryInfoKey = UnicodeAlias('RegQueryInfoKeyW')
@winfunctype('ADVAPI32.dll')
def RegQueryValueA(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpSubKey: win32more.Windows.Win32.Foundation.PSTR, lpData: win32more.Windows.Win32.Foundation.PSTR, lpcbData: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RegQueryValueW(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpSubKey: win32more.Windows.Win32.Foundation.PWSTR, lpData: win32more.Windows.Win32.Foundation.PWSTR, lpcbData: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
RegQueryValue = UnicodeAlias('RegQueryValueW')
@winfunctype('ADVAPI32.dll')
def RegQueryMultipleValuesA(hKey: win32more.Windows.Win32.System.Registry.HKEY, val_list: POINTER(win32more.Windows.Win32.System.Registry.VALENTA), num_vals: UInt32, lpValueBuf: win32more.Windows.Win32.Foundation.PSTR, ldwTotsize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RegQueryMultipleValuesW(hKey: win32more.Windows.Win32.System.Registry.HKEY, val_list: POINTER(win32more.Windows.Win32.System.Registry.VALENTW), num_vals: UInt32, lpValueBuf: win32more.Windows.Win32.Foundation.PWSTR, ldwTotsize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
RegQueryMultipleValues = UnicodeAlias('RegQueryMultipleValuesW')
@winfunctype('ADVAPI32.dll')
def RegQueryValueExA(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpValueName: win32more.Windows.Win32.Foundation.PSTR, lpReserved: POINTER(UInt32), lpType: POINTER(win32more.Windows.Win32.System.Registry.REG_VALUE_TYPE), lpData: POINTER(Byte), lpcbData: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RegQueryValueExW(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpValueName: win32more.Windows.Win32.Foundation.PWSTR, lpReserved: POINTER(UInt32), lpType: POINTER(win32more.Windows.Win32.System.Registry.REG_VALUE_TYPE), lpData: POINTER(Byte), lpcbData: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
RegQueryValueEx = UnicodeAlias('RegQueryValueExW')
@winfunctype('ADVAPI32.dll')
def RegReplaceKeyA(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpSubKey: win32more.Windows.Win32.Foundation.PSTR, lpNewFile: win32more.Windows.Win32.Foundation.PSTR, lpOldFile: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RegReplaceKeyW(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpSubKey: win32more.Windows.Win32.Foundation.PWSTR, lpNewFile: win32more.Windows.Win32.Foundation.PWSTR, lpOldFile: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
RegReplaceKey = UnicodeAlias('RegReplaceKeyW')
@winfunctype('ADVAPI32.dll')
def RegRestoreKeyA(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpFile: win32more.Windows.Win32.Foundation.PSTR, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RegRestoreKeyW(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpFile: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
RegRestoreKey = UnicodeAlias('RegRestoreKeyW')
@winfunctype('ADVAPI32.dll')
def RegRenameKey(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpSubKeyName: win32more.Windows.Win32.Foundation.PWSTR, lpNewKeyName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RegSaveKeyA(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpFile: win32more.Windows.Win32.Foundation.PSTR, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RegSaveKeyW(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpFile: win32more.Windows.Win32.Foundation.PWSTR, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
RegSaveKey = UnicodeAlias('RegSaveKeyW')
@winfunctype('ADVAPI32.dll')
def RegSetKeySecurity(hKey: win32more.Windows.Win32.System.Registry.HKEY, SecurityInformation: win32more.Windows.Win32.Security.OBJECT_SECURITY_INFORMATION, pSecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RegSetValueA(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpSubKey: win32more.Windows.Win32.Foundation.PSTR, dwType: win32more.Windows.Win32.System.Registry.REG_VALUE_TYPE, lpData: win32more.Windows.Win32.Foundation.PSTR, cbData: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RegSetValueW(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpSubKey: win32more.Windows.Win32.Foundation.PWSTR, dwType: win32more.Windows.Win32.System.Registry.REG_VALUE_TYPE, lpData: win32more.Windows.Win32.Foundation.PWSTR, cbData: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
RegSetValue = UnicodeAlias('RegSetValueW')
@winfunctype('ADVAPI32.dll')
def RegSetValueExA(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpValueName: win32more.Windows.Win32.Foundation.PSTR, Reserved: UInt32, dwType: win32more.Windows.Win32.System.Registry.REG_VALUE_TYPE, lpData: POINTER(Byte), cbData: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RegSetValueExW(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpValueName: win32more.Windows.Win32.Foundation.PWSTR, Reserved: UInt32, dwType: win32more.Windows.Win32.System.Registry.REG_VALUE_TYPE, lpData: POINTER(Byte), cbData: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
RegSetValueEx = UnicodeAlias('RegSetValueExW')
@winfunctype('ADVAPI32.dll')
def RegUnLoadKeyA(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpSubKey: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RegUnLoadKeyW(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpSubKey: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
RegUnLoadKey = UnicodeAlias('RegUnLoadKeyW')
@winfunctype('ADVAPI32.dll')
def RegDeleteKeyValueA(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpSubKey: win32more.Windows.Win32.Foundation.PSTR, lpValueName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RegDeleteKeyValueW(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpSubKey: win32more.Windows.Win32.Foundation.PWSTR, lpValueName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
RegDeleteKeyValue = UnicodeAlias('RegDeleteKeyValueW')
@winfunctype('ADVAPI32.dll')
def RegSetKeyValueA(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpSubKey: win32more.Windows.Win32.Foundation.PSTR, lpValueName: win32more.Windows.Win32.Foundation.PSTR, dwType: UInt32, lpData: VoidPtr, cbData: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RegSetKeyValueW(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpSubKey: win32more.Windows.Win32.Foundation.PWSTR, lpValueName: win32more.Windows.Win32.Foundation.PWSTR, dwType: UInt32, lpData: VoidPtr, cbData: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
RegSetKeyValue = UnicodeAlias('RegSetKeyValueW')
@winfunctype('ADVAPI32.dll')
def RegDeleteTreeA(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpSubKey: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RegDeleteTreeW(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpSubKey: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
RegDeleteTree = UnicodeAlias('RegDeleteTreeW')
@winfunctype('ADVAPI32.dll')
def RegCopyTreeA(hKeySrc: win32more.Windows.Win32.System.Registry.HKEY, lpSubKey: win32more.Windows.Win32.Foundation.PSTR, hKeyDest: win32more.Windows.Win32.System.Registry.HKEY) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RegGetValueA(hkey: win32more.Windows.Win32.System.Registry.HKEY, lpSubKey: win32more.Windows.Win32.Foundation.PSTR, lpValue: win32more.Windows.Win32.Foundation.PSTR, dwFlags: win32more.Windows.Win32.System.Registry.REG_ROUTINE_FLAGS, pdwType: POINTER(win32more.Windows.Win32.System.Registry.REG_VALUE_TYPE), pvData: VoidPtr, pcbData: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RegGetValueW(hkey: win32more.Windows.Win32.System.Registry.HKEY, lpSubKey: win32more.Windows.Win32.Foundation.PWSTR, lpValue: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: win32more.Windows.Win32.System.Registry.REG_ROUTINE_FLAGS, pdwType: POINTER(win32more.Windows.Win32.System.Registry.REG_VALUE_TYPE), pvData: VoidPtr, pcbData: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
RegGetValue = UnicodeAlias('RegGetValueW')
@winfunctype('ADVAPI32.dll')
def RegCopyTreeW(hKeySrc: win32more.Windows.Win32.System.Registry.HKEY, lpSubKey: win32more.Windows.Win32.Foundation.PWSTR, hKeyDest: win32more.Windows.Win32.System.Registry.HKEY) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
RegCopyTree = UnicodeAlias('RegCopyTreeW')
@winfunctype('ADVAPI32.dll')
def RegLoadMUIStringA(hKey: win32more.Windows.Win32.System.Registry.HKEY, pszValue: win32more.Windows.Win32.Foundation.PSTR, pszOutBuf: win32more.Windows.Win32.Foundation.PSTR, cbOutBuf: UInt32, pcbData: POINTER(UInt32), Flags: UInt32, pszDirectory: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RegLoadMUIStringW(hKey: win32more.Windows.Win32.System.Registry.HKEY, pszValue: win32more.Windows.Win32.Foundation.PWSTR, pszOutBuf: win32more.Windows.Win32.Foundation.PWSTR, cbOutBuf: UInt32, pcbData: POINTER(UInt32), Flags: UInt32, pszDirectory: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
RegLoadMUIString = UnicodeAlias('RegLoadMUIStringW')
@winfunctype('ADVAPI32.dll')
def RegLoadAppKeyA(lpFile: win32more.Windows.Win32.Foundation.PSTR, phkResult: POINTER(win32more.Windows.Win32.System.Registry.HKEY), samDesired: UInt32, dwOptions: UInt32, Reserved: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RegLoadAppKeyW(lpFile: win32more.Windows.Win32.Foundation.PWSTR, phkResult: POINTER(win32more.Windows.Win32.System.Registry.HKEY), samDesired: UInt32, dwOptions: UInt32, Reserved: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
RegLoadAppKey = UnicodeAlias('RegLoadAppKeyW')
@winfunctype('ADVAPI32.dll')
def RegSaveKeyExA(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpFile: win32more.Windows.Win32.Foundation.PSTR, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), Flags: win32more.Windows.Win32.System.Registry.REG_SAVE_FORMAT) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('ADVAPI32.dll')
def RegSaveKeyExW(hKey: win32more.Windows.Win32.System.Registry.HKEY, lpFile: win32more.Windows.Win32.Foundation.PWSTR, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), Flags: win32more.Windows.Win32.System.Registry.REG_SAVE_FORMAT) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
RegSaveKeyEx = UnicodeAlias('RegSaveKeyExW')
@winfunctype('api-ms-win-core-state-helpers-l1-1-0.dll')
def GetRegistryValueWithFallbackW(hkeyPrimary: win32more.Windows.Win32.System.Registry.HKEY, pwszPrimarySubKey: win32more.Windows.Win32.Foundation.PWSTR, hkeyFallback: win32more.Windows.Win32.System.Registry.HKEY, pwszFallbackSubKey: win32more.Windows.Win32.Foundation.PWSTR, pwszValue: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, pdwType: POINTER(UInt32), pvData: VoidPtr, cbDataIn: UInt32, pcbDataOut: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
class DSKTLSYSTEMTIME(Structure):
    wYear: UInt16
    wMonth: UInt16
    wDayOfWeek: UInt16
    wDay: UInt16
    wHour: UInt16
    wMinute: UInt16
    wSecond: UInt16
    wMilliseconds: UInt16
    wResult: UInt16
HKEY = VoidPtr
@cfunctype_pointer
def PQUERYHANDLER(keycontext: VoidPtr, val_list: POINTER(win32more.Windows.Win32.System.Registry.val_context), num_vals: UInt32, outputbuffer: VoidPtr, total_outlen: POINTER(UInt32), input_blen: UInt32) -> UInt32: ...
class PVALUEA(Structure):
    pv_valuename: win32more.Windows.Win32.Foundation.PSTR
    pv_valuelen: Int32
    pv_value_context: VoidPtr
    pv_type: UInt32
class PVALUEW(Structure):
    pv_valuename: win32more.Windows.Win32.Foundation.PWSTR
    pv_valuelen: Int32
    pv_value_context: VoidPtr
    pv_type: UInt32
PVALUE = UnicodeAlias('PVALUEW')
REG_CREATE_KEY_DISPOSITION = UInt32
REG_CREATED_NEW_KEY: win32more.Windows.Win32.System.Registry.REG_CREATE_KEY_DISPOSITION = 1
REG_OPENED_EXISTING_KEY: win32more.Windows.Win32.System.Registry.REG_CREATE_KEY_DISPOSITION = 2
REG_NOTIFY_FILTER = UInt32
REG_NOTIFY_CHANGE_NAME: win32more.Windows.Win32.System.Registry.REG_NOTIFY_FILTER = 1
REG_NOTIFY_CHANGE_ATTRIBUTES: win32more.Windows.Win32.System.Registry.REG_NOTIFY_FILTER = 2
REG_NOTIFY_CHANGE_LAST_SET: win32more.Windows.Win32.System.Registry.REG_NOTIFY_FILTER = 4
REG_NOTIFY_CHANGE_SECURITY: win32more.Windows.Win32.System.Registry.REG_NOTIFY_FILTER = 8
REG_NOTIFY_THREAD_AGNOSTIC: win32more.Windows.Win32.System.Registry.REG_NOTIFY_FILTER = 268435456
REG_OPEN_CREATE_OPTIONS = UInt32
REG_OPTION_RESERVED: win32more.Windows.Win32.System.Registry.REG_OPEN_CREATE_OPTIONS = 0
REG_OPTION_NON_VOLATILE: win32more.Windows.Win32.System.Registry.REG_OPEN_CREATE_OPTIONS = 0
REG_OPTION_VOLATILE: win32more.Windows.Win32.System.Registry.REG_OPEN_CREATE_OPTIONS = 1
REG_OPTION_CREATE_LINK: win32more.Windows.Win32.System.Registry.REG_OPEN_CREATE_OPTIONS = 2
REG_OPTION_BACKUP_RESTORE: win32more.Windows.Win32.System.Registry.REG_OPEN_CREATE_OPTIONS = 4
REG_OPTION_OPEN_LINK: win32more.Windows.Win32.System.Registry.REG_OPEN_CREATE_OPTIONS = 8
REG_OPTION_DONT_VIRTUALIZE: win32more.Windows.Win32.System.Registry.REG_OPEN_CREATE_OPTIONS = 16
class REG_PROVIDER(Structure):
    pi_R0_1val: win32more.Windows.Win32.System.Registry.PQUERYHANDLER
    pi_R0_allvals: win32more.Windows.Win32.System.Registry.PQUERYHANDLER
    pi_R3_1val: win32more.Windows.Win32.System.Registry.PQUERYHANDLER
    pi_R3_allvals: win32more.Windows.Win32.System.Registry.PQUERYHANDLER
    pi_flags: UInt32
    pi_key_context: VoidPtr
REG_RESTORE_KEY_FLAGS = Int32
REG_FORCE_RESTORE: win32more.Windows.Win32.System.Registry.REG_RESTORE_KEY_FLAGS = 8
REG_WHOLE_HIVE_VOLATILE: win32more.Windows.Win32.System.Registry.REG_RESTORE_KEY_FLAGS = 1
REG_ROUTINE_FLAGS = UInt32
RRF_RT_DWORD: win32more.Windows.Win32.System.Registry.REG_ROUTINE_FLAGS = 24
RRF_RT_QWORD: win32more.Windows.Win32.System.Registry.REG_ROUTINE_FLAGS = 72
RRF_RT_REG_NONE: win32more.Windows.Win32.System.Registry.REG_ROUTINE_FLAGS = 1
RRF_RT_REG_SZ: win32more.Windows.Win32.System.Registry.REG_ROUTINE_FLAGS = 2
RRF_RT_REG_EXPAND_SZ: win32more.Windows.Win32.System.Registry.REG_ROUTINE_FLAGS = 4
RRF_RT_REG_BINARY: win32more.Windows.Win32.System.Registry.REG_ROUTINE_FLAGS = 8
RRF_RT_REG_DWORD: win32more.Windows.Win32.System.Registry.REG_ROUTINE_FLAGS = 16
RRF_RT_REG_MULTI_SZ: win32more.Windows.Win32.System.Registry.REG_ROUTINE_FLAGS = 32
RRF_RT_REG_QWORD: win32more.Windows.Win32.System.Registry.REG_ROUTINE_FLAGS = 64
RRF_RT_ANY: win32more.Windows.Win32.System.Registry.REG_ROUTINE_FLAGS = 65535
RRF_SUBKEY_WOW6464KEY: win32more.Windows.Win32.System.Registry.REG_ROUTINE_FLAGS = 65536
RRF_SUBKEY_WOW6432KEY: win32more.Windows.Win32.System.Registry.REG_ROUTINE_FLAGS = 131072
RRF_WOW64_MASK: win32more.Windows.Win32.System.Registry.REG_ROUTINE_FLAGS = 196608
RRF_NOEXPAND: win32more.Windows.Win32.System.Registry.REG_ROUTINE_FLAGS = 268435456
RRF_ZEROONFAILURE: win32more.Windows.Win32.System.Registry.REG_ROUTINE_FLAGS = 536870912
REG_SAM_FLAGS = UInt32
KEY_QUERY_VALUE: win32more.Windows.Win32.System.Registry.REG_SAM_FLAGS = 1
KEY_SET_VALUE: win32more.Windows.Win32.System.Registry.REG_SAM_FLAGS = 2
KEY_CREATE_SUB_KEY: win32more.Windows.Win32.System.Registry.REG_SAM_FLAGS = 4
KEY_ENUMERATE_SUB_KEYS: win32more.Windows.Win32.System.Registry.REG_SAM_FLAGS = 8
KEY_NOTIFY: win32more.Windows.Win32.System.Registry.REG_SAM_FLAGS = 16
KEY_CREATE_LINK: win32more.Windows.Win32.System.Registry.REG_SAM_FLAGS = 32
KEY_WOW64_32KEY: win32more.Windows.Win32.System.Registry.REG_SAM_FLAGS = 512
KEY_WOW64_64KEY: win32more.Windows.Win32.System.Registry.REG_SAM_FLAGS = 256
KEY_WOW64_RES: win32more.Windows.Win32.System.Registry.REG_SAM_FLAGS = 768
KEY_READ: win32more.Windows.Win32.System.Registry.REG_SAM_FLAGS = 131097
KEY_WRITE: win32more.Windows.Win32.System.Registry.REG_SAM_FLAGS = 131078
KEY_EXECUTE: win32more.Windows.Win32.System.Registry.REG_SAM_FLAGS = 131097
KEY_ALL_ACCESS: win32more.Windows.Win32.System.Registry.REG_SAM_FLAGS = 983103
REG_SAVE_FORMAT = UInt32
REG_STANDARD_FORMAT: win32more.Windows.Win32.System.Registry.REG_SAVE_FORMAT = 1
REG_LATEST_FORMAT: win32more.Windows.Win32.System.Registry.REG_SAVE_FORMAT = 2
REG_NO_COMPRESSION: win32more.Windows.Win32.System.Registry.REG_SAVE_FORMAT = 4
REG_VALUE_TYPE = UInt32
REG_NONE: win32more.Windows.Win32.System.Registry.REG_VALUE_TYPE = 0
REG_SZ: win32more.Windows.Win32.System.Registry.REG_VALUE_TYPE = 1
REG_EXPAND_SZ: win32more.Windows.Win32.System.Registry.REG_VALUE_TYPE = 2
REG_BINARY: win32more.Windows.Win32.System.Registry.REG_VALUE_TYPE = 3
REG_DWORD: win32more.Windows.Win32.System.Registry.REG_VALUE_TYPE = 4
REG_DWORD_LITTLE_ENDIAN: win32more.Windows.Win32.System.Registry.REG_VALUE_TYPE = 4
REG_DWORD_BIG_ENDIAN: win32more.Windows.Win32.System.Registry.REG_VALUE_TYPE = 5
REG_LINK: win32more.Windows.Win32.System.Registry.REG_VALUE_TYPE = 6
REG_MULTI_SZ: win32more.Windows.Win32.System.Registry.REG_VALUE_TYPE = 7
REG_RESOURCE_LIST: win32more.Windows.Win32.System.Registry.REG_VALUE_TYPE = 8
REG_FULL_RESOURCE_DESCRIPTOR: win32more.Windows.Win32.System.Registry.REG_VALUE_TYPE = 9
REG_RESOURCE_REQUIREMENTS_LIST: win32more.Windows.Win32.System.Registry.REG_VALUE_TYPE = 10
REG_QWORD: win32more.Windows.Win32.System.Registry.REG_VALUE_TYPE = 11
REG_QWORD_LITTLE_ENDIAN: win32more.Windows.Win32.System.Registry.REG_VALUE_TYPE = 11
class VALENTA(Structure):
    ve_valuename: win32more.Windows.Win32.Foundation.PSTR
    ve_valuelen: UInt32
    ve_valueptr: UIntPtr
    ve_type: win32more.Windows.Win32.System.Registry.REG_VALUE_TYPE
class VALENTW(Structure):
    ve_valuename: win32more.Windows.Win32.Foundation.PWSTR
    ve_valuelen: UInt32
    ve_valueptr: UIntPtr
    ve_type: win32more.Windows.Win32.System.Registry.REG_VALUE_TYPE
VALENT = UnicodeAlias('VALENTW')
class val_context(Structure):
    valuelen: Int32
    value_context: VoidPtr
    val_buff_ptr: VoidPtr


make_ready(__name__)
