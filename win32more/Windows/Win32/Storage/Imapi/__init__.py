from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Storage.Imapi
import win32more.Windows.Win32.System.AddressBook
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Com.StructuredStorage
import win32more.Windows.Win32.System.Ole
IMAPI_SECTOR_SIZE: UInt32 = 2048
IMAPI2_DEFAULT_COMMAND_TIMEOUT: UInt32 = 10
DISPID_DDISCMASTER2EVENTS_DEVICEADDED: UInt32 = 256
DISPID_DDISCMASTER2EVENTS_DEVICEREMOVED: UInt32 = 257
DISPID_IDISCRECORDER2_EJECTMEDIA: UInt32 = 256
DISPID_IDISCRECORDER2_CLOSETRAY: UInt32 = 257
DISPID_IDISCRECORDER2_ACQUIREEXCLUSIVEACCESS: UInt32 = 258
DISPID_IDISCRECORDER2_RELEASEEXCLUSIVEACCESS: UInt32 = 259
DISPID_IDISCRECORDER2_DISABLEMCN: UInt32 = 260
DISPID_IDISCRECORDER2_ENABLEMCN: UInt32 = 261
DISPID_IDISCRECORDER2_INITIALIZEDISCRECORDER: UInt32 = 262
DISPID_IDISCRECORDER2_ACTIVEDISCRECORDER: UInt32 = 0
DISPID_IDISCRECORDER2_VENDORID: UInt32 = 513
DISPID_IDISCRECORDER2_PRODUCTID: UInt32 = 514
DISPID_IDISCRECORDER2_PRODUCTREVISION: UInt32 = 515
DISPID_IDISCRECORDER2_VOLUMENAME: UInt32 = 516
DISPID_IDISCRECORDER2_VOLUMEPATHNAMES: UInt32 = 517
DISPID_IDISCRECORDER2_DEVICECANLOADMEDIA: UInt32 = 518
DISPID_IDISCRECORDER2_LEGACYDEVICENUMBER: UInt32 = 519
DISPID_IDISCRECORDER2_SUPPORTEDFEATUREPAGES: UInt32 = 520
DISPID_IDISCRECORDER2_CURRENTFEATUREPAGES: UInt32 = 521
DISPID_IDISCRECORDER2_SUPPORTEDPROFILES: UInt32 = 522
DISPID_IDISCRECORDER2_CURRENTPROFILES: UInt32 = 523
DISPID_IDISCRECORDER2_SUPPORTEDMODEPAGES: UInt32 = 524
DISPID_IDISCRECORDER2_EXCLUSIVEACCESSOWNER: UInt32 = 525
DISPID_IWRITEENGINE2_WRITESECTION: UInt32 = 512
DISPID_IWRITEENGINE2_CANCELWRITE: UInt32 = 513
DISPID_IWRITEENGINE2_DISCRECORDER: UInt32 = 256
DISPID_IWRITEENGINE2_USESTREAMINGWRITE12: UInt32 = 257
DISPID_IWRITEENGINE2_STARTINGSECTORSPERSECOND: UInt32 = 258
DISPID_IWRITEENGINE2_ENDINGSECTORSPERSECOND: UInt32 = 259
DISPID_IWRITEENGINE2_BYTESPERSECTOR: UInt32 = 260
DISPID_IWRITEENGINE2_WRITEINPROGRESS: UInt32 = 261
DISPID_IWRITEENGINE2EVENTARGS_STARTLBA: UInt32 = 256
DISPID_IWRITEENGINE2EVENTARGS_SECTORCOUNT: UInt32 = 257
DISPID_IWRITEENGINE2EVENTARGS_LASTREADLBA: UInt32 = 258
DISPID_IWRITEENGINE2EVENTARGS_LASTWRITTENLBA: UInt32 = 259
DISPID_IWRITEENGINE2EVENTARGS_TOTALDEVICEBUFFER: UInt32 = 260
DISPID_IWRITEENGINE2EVENTARGS_USEDDEVICEBUFFER: UInt32 = 261
DISPID_IWRITEENGINE2EVENTARGS_TOTALSYSTEMBUFFER: UInt32 = 262
DISPID_IWRITEENGINE2EVENTARGS_USEDSYSTEMBUFFER: UInt32 = 263
DISPID_IWRITEENGINE2EVENTARGS_FREESYSTEMBUFFER: UInt32 = 264
DISPID_DWRITEENGINE2EVENTS_UPDATE: UInt32 = 256
DISPID_IDISCFORMAT2_RECORDERSUPPORTED: UInt32 = 2048
DISPID_IDISCFORMAT2_MEDIASUPPORTED: UInt32 = 2049
DISPID_IDISCFORMAT2_MEDIAPHYSICALLYBLANK: UInt32 = 1792
DISPID_IDISCFORMAT2_MEDIAHEURISTICALLYBLANK: UInt32 = 1793
DISPID_IDISCFORMAT2_SUPPORTEDMEDIATYPES: UInt32 = 1794
DISPID_IDISCFORMAT2ERASE_RECORDER: UInt32 = 256
DISPID_IDISCFORMAT2ERASE_FULLERASE: UInt32 = 257
DISPID_IDISCFORMAT2ERASE_MEDIATYPE: UInt32 = 258
DISPID_IDISCFORMAT2ERASE_CLIENTNAME: UInt32 = 259
DISPID_IDISCFORMAT2ERASE_ERASEMEDIA: UInt32 = 513
DISPID_IDISCFORMAT2ERASEEVENTS_UPDATE: UInt32 = 512
DISPID_IDISCFORMAT2DATA_RECORDER: UInt32 = 256
DISPID_IDISCFORMAT2DATA_BUFFERUNDERRUNFREEDISABLED: UInt32 = 257
DISPID_IDISCFORMAT2DATA_POSTGAPALREADYINIMAGE: UInt32 = 260
DISPID_IDISCFORMAT2DATA_CURRENTMEDIASTATUS: UInt32 = 262
DISPID_IDISCFORMAT2DATA_WRITEPROTECTSTATUS: UInt32 = 263
DISPID_IDISCFORMAT2DATA_TOTALSECTORS: UInt32 = 264
DISPID_IDISCFORMAT2DATA_FREESECTORS: UInt32 = 265
DISPID_IDISCFORMAT2DATA_NEXTWRITABLEADDRESS: UInt32 = 266
DISPID_IDISCFORMAT2DATA_STARTSECTOROFPREVIOUSSESSION: UInt32 = 267
DISPID_IDISCFORMAT2DATA_LASTSECTOROFPREVIOUSSESSION: UInt32 = 268
DISPID_IDISCFORMAT2DATA_FORCEMEDIATOBECLOSED: UInt32 = 269
DISPID_IDISCFORMAT2DATA_DISABLEDVDCOMPATIBILITYMODE: UInt32 = 270
DISPID_IDISCFORMAT2DATA_CURRENTMEDIATYPE: UInt32 = 271
DISPID_IDISCFORMAT2DATA_CLIENTNAME: UInt32 = 272
DISPID_IDISCFORMAT2DATA_REQUESTEDWRITESPEED: UInt32 = 273
DISPID_IDISCFORMAT2DATA_REQUESTEDROTATIONTYPEISPURECAV: UInt32 = 274
DISPID_IDISCFORMAT2DATA_CURRENTWRITESPEED: UInt32 = 275
DISPID_IDISCFORMAT2DATA_CURRENTROTATIONTYPEISPURECAV: UInt32 = 276
DISPID_IDISCFORMAT2DATA_SUPPORTEDWRITESPEEDS: UInt32 = 277
DISPID_IDISCFORMAT2DATA_SUPPORTEDWRITESPEEDDESCRIPTORS: UInt32 = 278
DISPID_IDISCFORMAT2DATA_FORCEOVERWRITE: UInt32 = 279
DISPID_IDISCFORMAT2DATA_MUTLISESSIONINTERFACES: UInt32 = 280
DISPID_IDISCFORMAT2DATA_WRITE: UInt32 = 512
DISPID_IDISCFORMAT2DATA_CANCELWRITE: UInt32 = 513
DISPID_IDISCFORMAT2DATA_SETWRITESPEED: UInt32 = 514
DISPID_DDISCFORMAT2DATAEVENTS_UPDATE: UInt32 = 512
DISPID_IDISCFORMAT2DATAEVENTARGS_ELAPSEDTIME: UInt32 = 768
DISPID_IDISCFORMAT2DATAEVENTARGS_ESTIMATEDREMAININGTIME: UInt32 = 769
DISPID_IDISCFORMAT2DATAEVENTARGS_ESTIMATEDTOTALTIME: UInt32 = 770
DISPID_IDISCFORMAT2DATAEVENTARGS_CURRENTACTION: UInt32 = 771
DISPID_IDISCFORMAT2TAO_RECORDER: UInt32 = 256
DISPID_IDISCFORMAT2TAO_BUFFERUNDERRUNFREEDISABLED: UInt32 = 258
DISPID_IDISCFORMAT2TAO_NUMBEROFEXISTINGTRACKS: UInt32 = 259
DISPID_IDISCFORMAT2TAO_TOTALSECTORSONMEDIA: UInt32 = 260
DISPID_IDISCFORMAT2TAO_FREESECTORSONMEDIA: UInt32 = 261
DISPID_IDISCFORMAT2TAO_USEDSECTORSONMEDIA: UInt32 = 262
DISPID_IDISCFORMAT2TAO_DONOTFINALIZEMEDIA: UInt32 = 263
DISPID_IDISCFORMAT2TAO_EXPECTEDTABLEOFCONTENTS: UInt32 = 266
DISPID_IDISCFORMAT2TAO_CURRENTMEDIATYPE: UInt32 = 267
DISPID_IDISCFORMAT2TAO_CLIENTNAME: UInt32 = 270
DISPID_IDISCFORMAT2TAO_REQUESTEDWRITESPEED: UInt32 = 271
DISPID_IDISCFORMAT2TAO_REQUESTEDROTATIONTYPEISPURECAV: UInt32 = 272
DISPID_IDISCFORMAT2TAO_CURRENTWRITESPEED: UInt32 = 273
DISPID_IDISCFORMAT2TAO_CURRENTROTATIONTYPEISPURECAV: UInt32 = 274
DISPID_IDISCFORMAT2TAO_SUPPORTEDWRITESPEEDS: UInt32 = 275
DISPID_IDISCFORMAT2TAO_SUPPORTEDWRITESPEEDDESCRIPTORS: UInt32 = 276
DISPID_IDISCFORMAT2TAO_PREPAREMEDIA: UInt32 = 512
DISPID_IDISCFORMAT2TAO_ADDAUDIOTRACK: UInt32 = 513
DISPID_IDISCFORMAT2TAO_CANCELADDTRACK: UInt32 = 514
DISPID_IDISCFORMAT2TAO_FINISHMEDIA: UInt32 = 515
DISPID_IDISCFORMAT2TAO_SETWRITESPEED: UInt32 = 516
DISPID_DDISCFORMAT2TAOEVENTS_UPDATE: UInt32 = 512
DISPID_IDISCFORMAT2TAOEVENTARGS_CURRENTTRACKNUMBER: UInt32 = 768
DISPID_IDISCFORMAT2TAOEVENTARGS_CURRENTACTION: UInt32 = 769
DISPID_IDISCFORMAT2TAOEVENTARGS_ELAPSEDTIME: UInt32 = 770
DISPID_IDISCFORMAT2TAOEVENTARGS_ESTIMATEDREMAININGTIME: UInt32 = 771
DISPID_IDISCFORMAT2TAOEVENTARGS_ESTIMATEDTOTALTIME: UInt32 = 772
DISPID_IDISCFORMAT2RAWCD_RECORDER: UInt32 = 256
DISPID_IDISCFORMAT2RAWCD_BUFFERUNDERRUNFREEDISABLED: UInt32 = 258
DISPID_IDISCFORMAT2RAWCD_STARTOFNEXTSESSION: UInt32 = 259
DISPID_IDISCFORMAT2RAWCD_LASTPOSSIBLESTARTOFLEADOUT: UInt32 = 260
DISPID_IDISCFORMAT2RAWCD_CURRENTMEDIATYPE: UInt32 = 261
DISPID_IDISCFORMAT2RAWCD_SUPPORTEDDATASECTORTYPES: UInt32 = 264
DISPID_IDISCFORMAT2RAWCD_REQUESTEDDATASECTORTYPE: UInt32 = 265
DISPID_IDISCFORMAT2RAWCD_CLIENTNAME: UInt32 = 266
DISPID_IDISCFORMAT2RAWCD_REQUESTEDWRITESPEED: UInt32 = 267
DISPID_IDISCFORMAT2RAWCD_REQUESTEDROTATIONTYPEISPURECAV: UInt32 = 268
DISPID_IDISCFORMAT2RAWCD_CURRENTWRITESPEED: UInt32 = 269
DISPID_IDISCFORMAT2RAWCD_CURRENTROTATIONTYPEISPURECAV: UInt32 = 270
DISPID_IDISCFORMAT2RAWCD_SUPPORTEDWRITESPEEDS: UInt32 = 271
DISPID_IDISCFORMAT2RAWCD_SUPPORTEDWRITESPEEDDESCRIPTORS: UInt32 = 272
DISPID_IDISCFORMAT2RAWCD_PREPAREMEDIA: UInt32 = 512
DISPID_IDISCFORMAT2RAWCD_WRITEMEDIA: UInt32 = 513
DISPID_IDISCFORMAT2RAWCD_WRITEMEDIAWITHVALIDATION: UInt32 = 514
DISPID_IDISCFORMAT2RAWCD_CANCELWRITE: UInt32 = 515
DISPID_IDISCFORMAT2RAWCD_RELEASEMEDIA: UInt32 = 516
DISPID_IDISCFORMAT2RAWCD_SETWRITESPEED: UInt32 = 517
DISPID_DDISCFORMAT2RAWCDEVENTS_UPDATE: UInt32 = 512
DISPID_IDISCFORMAT2RAWCDEVENTARGS_CURRENTTRACKNUMBER: UInt32 = 768
DISPID_IDISCFORMAT2RAWCDEVENTARGS_CURRENTACTION: UInt32 = 769
DISPID_IDISCFORMAT2RAWCDEVENTARGS_ELAPSEDTIME: UInt32 = 768
DISPID_IDISCFORMAT2RAWCDEVENTARGS_ESTIMATEDREMAININGTIME: UInt32 = 769
DISPID_IDISCFORMAT2RAWCDEVENTARGS_ESTIMATEDTOTALTIME: UInt32 = 770
IMAPI_SECTORS_PER_SECOND_AT_1X_CD: UInt32 = 75
IMAPI_SECTORS_PER_SECOND_AT_1X_DVD: UInt32 = 680
IMAPI_SECTORS_PER_SECOND_AT_1X_BD: UInt32 = 2195
IMAPI_SECTORS_PER_SECOND_AT_1X_HD_DVD: UInt32 = 4568
DISPID_IMULTISESSION_SUPPORTEDONCURRENTMEDIA: UInt32 = 256
DISPID_IMULTISESSION_INUSE: UInt32 = 257
DISPID_IMULTISESSION_IMPORTRECORDER: UInt32 = 258
DISPID_IMULTISESSION_FIRSTDATASESSION: UInt32 = 512
DISPID_IMULTISESSION_STARTSECTOROFPREVIOUSSESSION: UInt32 = 513
DISPID_IMULTISESSION_LASTSECTOROFPREVIOUSSESSION: UInt32 = 514
DISPID_IMULTISESSION_NEXTWRITABLEADDRESS: UInt32 = 515
DISPID_IMULTISESSION_FREESECTORS: UInt32 = 516
DISPID_IMULTISESSION_WRITEUNITSIZE: UInt32 = 517
DISPID_IMULTISESSION_LASTWRITTENADDRESS: UInt32 = 518
DISPID_IMULTISESSION_SECTORSONMEDIA: UInt32 = 519
DISPID_IRAWCDIMAGECREATOR_CREATERESULTIMAGE: UInt32 = 512
DISPID_IRAWCDIMAGECREATOR_ADDTRACK: UInt32 = 513
DISPID_IRAWCDIMAGECREATOR_ADDSPECIALPREGAP: UInt32 = 514
DISPID_IRAWCDIMAGECREATOR_ADDSUBCODERWGENERATOR: UInt32 = 515
DISPID_IRAWCDIMAGECREATOR_RESULTINGIMAGETYPE: UInt32 = 256
DISPID_IRAWCDIMAGECREATOR_STARTOFLEADOUT: UInt32 = 257
DISPID_IRAWCDIMAGECREATOR_STARTOFLEADOUTLIMIT: UInt32 = 258
DISPID_IRAWCDIMAGECREATOR_DISABLEGAPLESSAUDIO: UInt32 = 259
DISPID_IRAWCDIMAGECREATOR_MEDIACATALOGNUMBER: UInt32 = 260
DISPID_IRAWCDIMAGECREATOR_STARTINGTRACKNUMBER: UInt32 = 261
DISPID_IRAWCDIMAGECREATOR_TRACKINFO: UInt32 = 262
DISPID_IRAWCDIMAGECREATOR_NUMBEROFEXISTINGTRACKS: UInt32 = 263
DISPID_IRAWCDIMAGECREATOR_USEDSECTORSONDISC: UInt32 = 264
DISPID_IRAWCDIMAGECREATOR_EXPECTEDTABLEOFCONTENTS: UInt32 = 265
DISPID_IRAWCDTRACKINFO_STARTINGLBA: UInt32 = 256
DISPID_IRAWCDTRACKINFO_SECTORCOUNT: UInt32 = 257
DISPID_IRAWCDTRACKINFO_TRACKNUMBER: UInt32 = 258
DISPID_IRAWCDTRACKINFO_SECTORTYPE: UInt32 = 259
DISPID_IRAWCDTRACKINFO_ISRC: UInt32 = 260
DISPID_IRAWCDTRACKINFO_DIGITALAUDIOCOPYSETTING: UInt32 = 261
DISPID_IRAWCDTRACKINFO_AUDIOHASPREEMPHASIS: UInt32 = 262
DISPID_IBLOCKRANGE_STARTLBA: UInt32 = 256
DISPID_IBLOCKRANGE_ENDLBA: UInt32 = 257
DISPID_IBLOCKRANGELIST_BLOCKRANGES: UInt32 = 256
IMAPILib2_MajorVersion: UInt32 = 1
IMAPILib2_MinorVersion: UInt32 = 0
IMAPI2FS_BOOT_ENTRY_COUNT_MAX: UInt32 = 32
DISPID_DFILESYSTEMIMAGEEVENTS_UPDATE: UInt32 = 256
DISPID_DFILESYSTEMIMAGEIMPORTEVENTS_UPDATEIMPORT: UInt32 = 257
IMAPI2FS_MajorVersion: UInt32 = 1
IMAPI2FS_MinorVersion: UInt32 = 0
IMAPI2FS_FullVersion_STR: String = '1.0'
IMAPI2FS_FullVersion_WSTR: String = '1.0'
MP_MSGCLASS_SYSTEM: UInt32 = 1
MP_MSGCLASS_REPLICATION: UInt32 = 2
MP_MSGCLASS_DELIVERY_REPORT: UInt32 = 3
MP_MSGCLASS_NONDELIVERY_REPORT: UInt32 = 4
MP_STATUS_SUCCESS: UInt32 = 0
MP_STATUS_RETRY: UInt32 = 1
MP_STATUS_ABORT_DELIVERY: UInt32 = 2
MP_STATUS_BAD_MAIL: UInt32 = 3
MP_STATUS_SUBMITTED: UInt32 = 4
MP_STATUS_CATEGORIZED: UInt32 = 5
MP_STATUS_ABANDON_DELIVERY: UInt32 = 6
RP_RECIP_FLAGS_RESERVED: UInt32 = 15
RP_DSN_NOTIFY_SUCCESS: UInt32 = 16777216
RP_DSN_NOTIFY_FAILURE: UInt32 = 33554432
RP_DSN_NOTIFY_DELAY: UInt32 = 67108864
RP_DSN_NOTIFY_NEVER: UInt32 = 134217728
RP_DSN_NOTIFY_MASK: UInt32 = 251658240
RP_HANDLED: UInt32 = 16
RP_GENERAL_FAILURE: UInt32 = 32
RP_DSN_HANDLED: UInt32 = 64
RP_DELIVERED: UInt32 = 272
RP_DSN_SENT_NDR: UInt32 = 1104
RP_FAILED: UInt32 = 2096
RP_UNRESOLVED: UInt32 = 4144
RP_ENPANDED: UInt32 = 8208
RP_EXPANDED: UInt32 = 8208
RP_DSN_SENT_DELAYED: UInt32 = 16384
RP_DSN_SENT_EXPANDED: UInt32 = 32832
RP_DSN_SENT_RELAYED: UInt32 = 65600
RP_DSN_SENT_DELIVERED: UInt32 = 131136
RP_REMOTE_MTA_NO_DSN: UInt32 = 524288
RP_ERROR_CONTEXT_STORE: UInt32 = 1048576
RP_ERROR_CONTEXT_CAT: UInt32 = 2097152
RP_ERROR_CONTEXT_MTA: UInt32 = 4194304
RP_VOLATILE_FLAGS_MASK: UInt32 = 4026531840
RP_DSN_NOTIFY_INVALID: UInt32 = 0
MPV_INBOUND_CUTOFF_EXCEEDED: UInt32 = 1
MPV_WRITE_CONTENT: UInt32 = 2
NMP_PROCESS_POST: UInt32 = 1
NMP_PROCESS_CONTROL: UInt32 = 2
NMP_PROCESS_MODERATOR: UInt32 = 4
GUID_SMTP_SOURCE_TYPE: Guid = Guid('{fb65c4dc-e468-11d1-aa67-00c04fa345f6}')
GUID_SMTPSVC_SOURCE: Guid = Guid('{1b3c0666-e470-11d1-aa67-00c04fa345f6}')
CATID_SMTP_ON_INBOUND_COMMAND: Guid = Guid('{f6628c8d-0d5e-11d2-aa68-00c04fa35b82}')
CATID_SMTP_ON_SERVER_RESPONSE: Guid = Guid('{f6628c8e-0d5e-11d2-aa68-00c04fa35b82}')
CATID_SMTP_ON_SESSION_START: Guid = Guid('{f6628c8f-0d5e-11d2-aa68-00c04fa35b82}')
CATID_SMTP_ON_MESSAGE_START: Guid = Guid('{f6628c90-0d5e-11d2-aa68-00c04fa35b82}')
CATID_SMTP_ON_PER_RECIPIENT: Guid = Guid('{f6628c91-0d5e-11d2-aa68-00c04fa35b82}')
CATID_SMTP_ON_BEFORE_DATA: Guid = Guid('{f6628c92-0d5e-11d2-aa68-00c04fa35b82}')
CATID_SMTP_ON_SESSION_END: Guid = Guid('{f6628c93-0d5e-11d2-aa68-00c04fa35b82}')
CATID_SMTP_STORE_DRIVER: Guid = Guid('{59175850-e533-11d1-aa67-00c04fa345f6}')
CATID_SMTP_TRANSPORT_SUBMISSION: Guid = Guid('{ff3caa23-00b9-11d2-9dfb-00c04fa322ba}')
CATID_SMTP_TRANSPORT_PRECATEGORIZE: Guid = Guid('{a3acfb0d-83ff-11d2-9e14-00c04fa322ba}')
CATID_SMTP_TRANSPORT_CATEGORIZE: Guid = Guid('{960252a3-0a3a-11d2-9e00-00c04fa322ba}')
CATID_SMTP_TRANSPORT_POSTCATEGORIZE: Guid = Guid('{76719654-05a6-11d2-9dfd-00c04fa322ba}')
CATID_SMTP_TRANSPORT_ROUTER: Guid = Guid('{283430c9-1850-11d2-9e03-00c04fa322ba}')
CATID_SMTP_MSGTRACKLOG: Guid = Guid('{c6df52aa-7db0-11d2-94f4-00c04f79f1d6}')
CATID_SMTP_DNSRESOLVERRECORDSINK: Guid = Guid('{bd0b4366-8e03-11d2-94f6-00c04f79f1d6}')
CATID_SMTP_MAXMSGSIZE: Guid = Guid('{ebf159de-a67e-11d2-94f7-00c04f79f1d6}')
CATID_SMTP_LOG: Guid = Guid('{93d0a538-2c1e-4b68-a7c9-d73a8aa6ee97}')
CATID_SMTP_GET_AUX_DOMAIN_INFO_FLAGS: Guid = Guid('{84ff368a-fab3-43d7-bcdf-692c5b46e6b1}')
CLSID_SmtpCat: Guid = Guid('{b23c35b7-9219-11d2-9e17-00c04fa322ba}')
CATID_SMTP_DSN: Guid = Guid('{22b55731-f5f8-4d23-bd8f-87b52371a73a}')
SZ_PROGID_SMTPCAT: String = 'Smtp.Cat'
IMAPI_S_PROPERTIESIGNORED: win32more.Windows.Win32.Foundation.HRESULT = 262656
IMAPI_S_BUFFER_TO_SMALL: win32more.Windows.Win32.Foundation.HRESULT = 262657
IMAPI_E_NOTOPENED: win32more.Windows.Win32.Foundation.HRESULT = -2147220981
IMAPI_E_NOTINITIALIZED: win32more.Windows.Win32.Foundation.HRESULT = -2147220980
IMAPI_E_USERABORT: win32more.Windows.Win32.Foundation.HRESULT = -2147220979
IMAPI_E_GENERIC: win32more.Windows.Win32.Foundation.HRESULT = -2147220978
IMAPI_E_MEDIUM_NOTPRESENT: win32more.Windows.Win32.Foundation.HRESULT = -2147220977
IMAPI_E_MEDIUM_INVALIDTYPE: win32more.Windows.Win32.Foundation.HRESULT = -2147220976
IMAPI_E_DEVICE_NOPROPERTIES: win32more.Windows.Win32.Foundation.HRESULT = -2147220975
IMAPI_E_DEVICE_NOTACCESSIBLE: win32more.Windows.Win32.Foundation.HRESULT = -2147220974
IMAPI_E_DEVICE_NOTPRESENT: win32more.Windows.Win32.Foundation.HRESULT = -2147220973
IMAPI_E_DEVICE_INVALIDTYPE: win32more.Windows.Win32.Foundation.HRESULT = -2147220972
IMAPI_E_INITIALIZE_WRITE: win32more.Windows.Win32.Foundation.HRESULT = -2147220971
IMAPI_E_INITIALIZE_ENDWRITE: win32more.Windows.Win32.Foundation.HRESULT = -2147220970
IMAPI_E_FILESYSTEM: win32more.Windows.Win32.Foundation.HRESULT = -2147220969
IMAPI_E_FILEACCESS: win32more.Windows.Win32.Foundation.HRESULT = -2147220968
IMAPI_E_DISCINFO: win32more.Windows.Win32.Foundation.HRESULT = -2147220967
IMAPI_E_TRACKNOTOPEN: win32more.Windows.Win32.Foundation.HRESULT = -2147220966
IMAPI_E_TRACKOPEN: win32more.Windows.Win32.Foundation.HRESULT = -2147220965
IMAPI_E_DISCFULL: win32more.Windows.Win32.Foundation.HRESULT = -2147220964
IMAPI_E_BADJOLIETNAME: win32more.Windows.Win32.Foundation.HRESULT = -2147220963
IMAPI_E_INVALIDIMAGE: win32more.Windows.Win32.Foundation.HRESULT = -2147220962
IMAPI_E_NOACTIVEFORMAT: win32more.Windows.Win32.Foundation.HRESULT = -2147220961
IMAPI_E_NOACTIVERECORDER: win32more.Windows.Win32.Foundation.HRESULT = -2147220960
IMAPI_E_WRONGFORMAT: win32more.Windows.Win32.Foundation.HRESULT = -2147220959
IMAPI_E_ALREADYOPEN: win32more.Windows.Win32.Foundation.HRESULT = -2147220958
IMAPI_E_WRONGDISC: win32more.Windows.Win32.Foundation.HRESULT = -2147220957
IMAPI_E_FILEEXISTS: win32more.Windows.Win32.Foundation.HRESULT = -2147220956
IMAPI_E_STASHINUSE: win32more.Windows.Win32.Foundation.HRESULT = -2147220955
IMAPI_E_DEVICE_STILL_IN_USE: win32more.Windows.Win32.Foundation.HRESULT = -2147220954
IMAPI_E_LOSS_OF_STREAMING: win32more.Windows.Win32.Foundation.HRESULT = -2147220953
IMAPI_E_COMPRESSEDSTASH: win32more.Windows.Win32.Foundation.HRESULT = -2147220952
IMAPI_E_ENCRYPTEDSTASH: win32more.Windows.Win32.Foundation.HRESULT = -2147220951
IMAPI_E_NOTENOUGHDISKFORSTASH: win32more.Windows.Win32.Foundation.HRESULT = -2147220950
IMAPI_E_REMOVABLESTASH: win32more.Windows.Win32.Foundation.HRESULT = -2147220949
IMAPI_E_CANNOT_WRITE_TO_MEDIA: win32more.Windows.Win32.Foundation.HRESULT = -2147220948
IMAPI_E_TRACK_NOT_BIG_ENOUGH: win32more.Windows.Win32.Foundation.HRESULT = -2147220947
IMAPI_E_BOOTIMAGE_AND_NONBLANK_DISC: win32more.Windows.Win32.Foundation.HRESULT = -2147220946
@winfunctype('MAPI32.dll')
def OpenIMsgSession(lpMalloc: win32more.Windows.Win32.System.Com.IMalloc, ulFlags: UInt32, lppMsgSess: POINTER(win32more.Windows.Win32.Storage.Imapi.LPMSGSESS)) -> Int32: ...
@winfunctype('MAPI32.dll')
def CloseIMsgSession(lpMsgSess: win32more.Windows.Win32.Storage.Imapi.LPMSGSESS) -> Void: ...
@winfunctype('MAPI32.dll')
def OpenIMsgOnIStg(lpMsgSess: win32more.Windows.Win32.Storage.Imapi.LPMSGSESS, lpAllocateBuffer: win32more.Windows.Win32.System.AddressBook.LPALLOCATEBUFFER, lpAllocateMore: win32more.Windows.Win32.System.AddressBook.LPALLOCATEMORE, lpFreeBuffer: win32more.Windows.Win32.System.AddressBook.LPFREEBUFFER, lpMalloc: win32more.Windows.Win32.System.Com.IMalloc, lpMapiSup: VoidPtr, lpStg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage, lpfMsgCallRelease: POINTER(win32more.Windows.Win32.Storage.Imapi.MSGCALLRELEASE), ulCallerData: UInt32, ulFlags: UInt32, lppMsg: POINTER(win32more.Windows.Win32.System.AddressBook.IMessage)) -> Int32: ...
@winfunctype('MAPI32.dll')
def GetAttribIMsgOnIStg(lpObject: VoidPtr, lpPropTagArray: POINTER(win32more.Windows.Win32.System.AddressBook.SPropTagArray), lppPropAttrArray: POINTER(POINTER(win32more.Windows.Win32.Storage.Imapi.SPropAttrArray))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MAPI32.dll')
def SetAttribIMsgOnIStg(lpObject: VoidPtr, lpPropTags: POINTER(win32more.Windows.Win32.System.AddressBook.SPropTagArray), lpPropAttrs: POINTER(win32more.Windows.Win32.Storage.Imapi.SPropAttrArray), lppPropProblems: POINTER(POINTER(win32more.Windows.Win32.System.AddressBook.SPropProblemArray))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MAPI32.dll')
def MapStorageSCode(StgSCode: Int32) -> Int32: ...
BlockRange = Guid('{b507ca27-2204-11dd-966a-001aa01bbc58}')
BlockRangeList = Guid('{b507ca28-2204-11dd-966a-001aa01bbc58}')
BootOptions = Guid('{2c941fce-975b-59be-a960-9a2a262853a5}')
class DDiscFormat2DataEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{2735413c-7f64-5b0f-8f00-5d77afbe261e}')
    @commethod(7)
    def Update(self, object: win32more.Windows.Win32.System.Com.IDispatch, progress: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class DDiscFormat2EraseEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{2735413a-7f64-5b0f-8f00-5d77afbe261e}')
    @commethod(7)
    def Update(self, object: win32more.Windows.Win32.System.Com.IDispatch, elapsedSeconds: Int32, estimatedTotalSeconds: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class DDiscFormat2RawCDEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{27354142-7f64-5b0f-8f00-5d77afbe261e}')
    @commethod(7)
    def Update(self, object: win32more.Windows.Win32.System.Com.IDispatch, progress: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class DDiscFormat2TrackAtOnceEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{2735413f-7f64-5b0f-8f00-5d77afbe261e}')
    @commethod(7)
    def Update(self, object: win32more.Windows.Win32.System.Com.IDispatch, progress: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class DDiscMaster2Events(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{27354131-7f64-5b0f-8f00-5d77afbe261e}')
    @commethod(7)
    def NotifyDeviceAdded(self, object: win32more.Windows.Win32.System.Com.IDispatch, uniqueId: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def NotifyDeviceRemoved(self, object: win32more.Windows.Win32.System.Com.IDispatch, uniqueId: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class DFileSystemImageEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{2c941fdf-975b-59be-a960-9a2a262853a5}')
    @commethod(7)
    def Update(self, object: win32more.Windows.Win32.System.Com.IDispatch, currentFile: win32more.Windows.Win32.Foundation.BSTR, copiedSectors: Int32, totalSectors: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class DFileSystemImageImportEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{d25c30f9-4087-4366-9e24-e55be286424b}')
    @commethod(7)
    def UpdateImport(self, object: win32more.Windows.Win32.System.Com.IDispatch, fileSystem: win32more.Windows.Win32.Storage.Imapi.FsiFileSystems, currentItem: win32more.Windows.Win32.Foundation.BSTR, importedDirectoryItems: Int32, totalDirectoryItems: Int32, importedFileItems: Int32, totalFileItems: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
DISC_RECORDER_STATE_FLAGS = UInt32
RECORDER_BURNING: win32more.Windows.Win32.Storage.Imapi.DISC_RECORDER_STATE_FLAGS = 2
RECORDER_DOING_NOTHING: win32more.Windows.Win32.Storage.Imapi.DISC_RECORDER_STATE_FLAGS = 0
RECORDER_OPENED: win32more.Windows.Win32.Storage.Imapi.DISC_RECORDER_STATE_FLAGS = 1
class DWriteEngine2Events(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{27354137-7f64-5b0f-8f00-5d77afbe261e}')
    @commethod(7)
    def Update(self, object: win32more.Windows.Win32.System.Com.IDispatch, progress: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
EmulationType = Int32
EmulationNone: win32more.Windows.Win32.Storage.Imapi.EmulationType = 0
Emulation12MFloppy: win32more.Windows.Win32.Storage.Imapi.EmulationType = 1
Emulation144MFloppy: win32more.Windows.Win32.Storage.Imapi.EmulationType = 2
Emulation288MFloppy: win32more.Windows.Win32.Storage.Imapi.EmulationType = 3
EmulationHardDisk: win32more.Windows.Win32.Storage.Imapi.EmulationType = 4
EnumFsiItems = Guid('{2c941fc6-975b-59be-a960-9a2a262853a5}')
EnumProgressItems = Guid('{2c941fca-975b-59be-a960-9a2a262853a5}')
FileSystemImageResult = Guid('{2c941fcc-975b-59be-a960-9a2a262853a5}')
FsiDirectoryItem = Guid('{2c941fc8-975b-59be-a960-9a2a262853a5}')
FsiFileItem = Guid('{2c941fc7-975b-59be-a960-9a2a262853a5}')
FsiFileSystems = Int32
FsiFileSystemNone: win32more.Windows.Win32.Storage.Imapi.FsiFileSystems = 0
FsiFileSystemISO9660: win32more.Windows.Win32.Storage.Imapi.FsiFileSystems = 1
FsiFileSystemJoliet: win32more.Windows.Win32.Storage.Imapi.FsiFileSystems = 2
FsiFileSystemUDF: win32more.Windows.Win32.Storage.Imapi.FsiFileSystems = 4
FsiFileSystemUnknown: win32more.Windows.Win32.Storage.Imapi.FsiFileSystems = 1073741824
FsiItemType = Int32
FsiItemNotFound: win32more.Windows.Win32.Storage.Imapi.FsiItemType = 0
FsiItemDirectory: win32more.Windows.Win32.Storage.Imapi.FsiItemType = 1
FsiItemFile: win32more.Windows.Win32.Storage.Imapi.FsiItemType = 2
FsiNamedStreams = Guid('{c6b6f8ed-6d19-44b4-b539-b159b793a32d}')
FsiStream = Guid('{2c941fcd-975b-59be-a960-9a2a262853a5}')
class IBlockRange(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{b507ca25-2204-11dd-966a-001aa01bbc58}')
    @commethod(7)
    def get_StartLba(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_EndLba(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBlockRangeList(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{b507ca26-2204-11dd-966a-001aa01bbc58}')
    @commethod(7)
    def get_BlockRanges(self, value: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBootOptions(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{2c941fd4-975b-59be-a960-9a2a262853a5}')
    @commethod(7)
    def get_BootImage(self, pVal: POINTER(win32more.Windows.Win32.System.Com.IStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Manufacturer(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_Manufacturer(self, newVal: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_PlatformId(self, pVal: POINTER(win32more.Windows.Win32.Storage.Imapi.PlatformId)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_PlatformId(self, newVal: win32more.Windows.Win32.Storage.Imapi.PlatformId) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Emulation(self, pVal: POINTER(win32more.Windows.Win32.Storage.Imapi.EmulationType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_Emulation(self, newVal: win32more.Windows.Win32.Storage.Imapi.EmulationType) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_ImageSize(self, pVal: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def AssignBootImage(self, newVal: win32more.Windows.Win32.System.Com.IStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBurnVerification(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d2ffd834-958b-426d-8470-2a13879c6a91}')
    @commethod(3)
    def put_BurnVerificationLevel(self, value: win32more.Windows.Win32.Storage.Imapi.IMAPI_BURN_VERIFICATION_LEVEL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_BurnVerificationLevel(self, value: POINTER(win32more.Windows.Win32.Storage.Imapi.IMAPI_BURN_VERIFICATION_LEVEL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDiscFormat2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{27354152-8f64-5b0f-8f00-5d77afbe261e}')
    @commethod(7)
    def IsRecorderSupported(self, recorder: win32more.Windows.Win32.Storage.Imapi.IDiscRecorder2, value: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def IsCurrentMediaSupported(self, recorder: win32more.Windows.Win32.Storage.Imapi.IDiscRecorder2, value: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_MediaPhysicallyBlank(self, value: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_MediaHeuristicallyBlank(self, value: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_SupportedMediaTypes(self, value: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDiscFormat2Data(ComPtr):
    extends: win32more.Windows.Win32.Storage.Imapi.IDiscFormat2
    _iid_ = Guid('{27354153-9f64-5b0f-8f00-5d77afbe261e}')
    @commethod(12)
    def put_Recorder(self, value: win32more.Windows.Win32.Storage.Imapi.IDiscRecorder2) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Recorder(self, value: POINTER(win32more.Windows.Win32.Storage.Imapi.IDiscRecorder2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_BufferUnderrunFreeDisabled(self, value: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_BufferUnderrunFreeDisabled(self, value: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_PostgapAlreadyInImage(self, value: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_PostgapAlreadyInImage(self, value: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_CurrentMediaStatus(self, value: POINTER(win32more.Windows.Win32.Storage.Imapi.IMAPI_FORMAT2_DATA_MEDIA_STATE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_WriteProtectStatus(self, value: POINTER(win32more.Windows.Win32.Storage.Imapi.IMAPI_MEDIA_WRITE_PROTECT_STATE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_TotalSectorsOnMedia(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_FreeSectorsOnMedia(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_NextWritableAddress(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_StartAddressOfPreviousSession(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_LastWrittenAddressOfPreviousSession(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_ForceMediaToBeClosed(self, value: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_ForceMediaToBeClosed(self, value: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_DisableConsumerDvdCompatibilityMode(self, value: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_DisableConsumerDvdCompatibilityMode(self, value: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_CurrentPhysicalMediaType(self, value: POINTER(win32more.Windows.Win32.Storage.Imapi.IMAPI_MEDIA_PHYSICAL_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def put_ClientName(self, value: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_ClientName(self, value: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def get_RequestedWriteSpeed(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_RequestedRotationTypeIsPureCAV(self, value: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def get_CurrentWriteSpeed(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def get_CurrentRotationTypeIsPureCAV(self, value: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def get_SupportedWriteSpeeds(self, supportedSpeeds: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def get_SupportedWriteSpeedDescriptors(self, supportedSpeedDescriptors: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def put_ForceOverwrite(self, value: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def get_ForceOverwrite(self, value: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def get_MultisessionInterfaces(self, value: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def Write(self, data: win32more.Windows.Win32.System.Com.IStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def CancelWrite(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def SetWriteSpeed(self, RequestedSectorsPerSecond: Int32, RotationTypeIsPureCAV: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDiscFormat2DataEventArgs(ComPtr):
    extends: win32more.Windows.Win32.Storage.Imapi.IWriteEngine2EventArgs
    _iid_ = Guid('{2735413d-7f64-5b0f-8f00-5d77afbe261e}')
    @commethod(14)
    def get_ElapsedTime(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_RemainingTime(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_TotalTime(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_CurrentAction(self, value: POINTER(win32more.Windows.Win32.Storage.Imapi.IMAPI_FORMAT2_DATA_WRITE_ACTION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDiscFormat2Erase(ComPtr):
    extends: win32more.Windows.Win32.Storage.Imapi.IDiscFormat2
    _iid_ = Guid('{27354156-8f64-5b0f-8f00-5d77afbe261e}')
    @commethod(12)
    def put_Recorder(self, value: win32more.Windows.Win32.Storage.Imapi.IDiscRecorder2) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Recorder(self, value: POINTER(win32more.Windows.Win32.Storage.Imapi.IDiscRecorder2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_FullErase(self, value: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_FullErase(self, value: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_CurrentPhysicalMediaType(self, value: POINTER(win32more.Windows.Win32.Storage.Imapi.IMAPI_MEDIA_PHYSICAL_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_ClientName(self, value: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_ClientName(self, value: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def EraseMedia(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDiscFormat2RawCD(ComPtr):
    extends: win32more.Windows.Win32.Storage.Imapi.IDiscFormat2
    _iid_ = Guid('{27354155-8f64-5b0f-8f00-5d77afbe261e}')
    @commethod(12)
    def PrepareMedia(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def WriteMedia(self, data: win32more.Windows.Win32.System.Com.IStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def WriteMedia2(self, data: win32more.Windows.Win32.System.Com.IStream, streamLeadInSectors: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def CancelWrite(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def ReleaseMedia(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetWriteSpeed(self, RequestedSectorsPerSecond: Int32, RotationTypeIsPureCAV: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_Recorder(self, value: win32more.Windows.Win32.Storage.Imapi.IDiscRecorder2) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_Recorder(self, value: POINTER(win32more.Windows.Win32.Storage.Imapi.IDiscRecorder2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_BufferUnderrunFreeDisabled(self, value: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_BufferUnderrunFreeDisabled(self, value: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_StartOfNextSession(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_LastPossibleStartOfLeadout(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_CurrentPhysicalMediaType(self, value: POINTER(win32more.Windows.Win32.Storage.Imapi.IMAPI_MEDIA_PHYSICAL_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_SupportedSectorTypes(self, value: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_RequestedSectorType(self, value: win32more.Windows.Win32.Storage.Imapi.IMAPI_FORMAT2_RAW_CD_DATA_SECTOR_TYPE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_RequestedSectorType(self, value: POINTER(win32more.Windows.Win32.Storage.Imapi.IMAPI_FORMAT2_RAW_CD_DATA_SECTOR_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def put_ClientName(self, value: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_ClientName(self, value: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_RequestedWriteSpeed(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_RequestedRotationTypeIsPureCAV(self, value: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def get_CurrentWriteSpeed(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_CurrentRotationTypeIsPureCAV(self, value: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def get_SupportedWriteSpeeds(self, supportedSpeeds: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def get_SupportedWriteSpeedDescriptors(self, supportedSpeedDescriptors: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDiscFormat2RawCDEventArgs(ComPtr):
    extends: win32more.Windows.Win32.Storage.Imapi.IWriteEngine2EventArgs
    _iid_ = Guid('{27354143-7f64-5b0f-8f00-5d77afbe261e}')
    @commethod(14)
    def get_CurrentAction(self, value: POINTER(win32more.Windows.Win32.Storage.Imapi.IMAPI_FORMAT2_RAW_CD_WRITE_ACTION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_ElapsedTime(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_RemainingTime(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDiscFormat2TrackAtOnce(ComPtr):
    extends: win32more.Windows.Win32.Storage.Imapi.IDiscFormat2
    _iid_ = Guid('{27354154-8f64-5b0f-8f00-5d77afbe261e}')
    @commethod(12)
    def PrepareMedia(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def AddAudioTrack(self, data: win32more.Windows.Win32.System.Com.IStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def CancelAddTrack(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def ReleaseMedia(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetWriteSpeed(self, RequestedSectorsPerSecond: Int32, RotationTypeIsPureCAV: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_Recorder(self, value: win32more.Windows.Win32.Storage.Imapi.IDiscRecorder2) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_Recorder(self, value: POINTER(win32more.Windows.Win32.Storage.Imapi.IDiscRecorder2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def put_BufferUnderrunFreeDisabled(self, value: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_BufferUnderrunFreeDisabled(self, value: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_NumberOfExistingTracks(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_TotalSectorsOnMedia(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_FreeSectorsOnMedia(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_UsedSectorsOnMedia(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_DoNotFinalizeMedia(self, value: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_DoNotFinalizeMedia(self, value: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_ExpectedTableOfContents(self, value: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_CurrentPhysicalMediaType(self, value: POINTER(win32more.Windows.Win32.Storage.Imapi.IMAPI_MEDIA_PHYSICAL_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def put_ClientName(self, value: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_ClientName(self, value: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_RequestedWriteSpeed(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def get_RequestedRotationTypeIsPureCAV(self, value: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_CurrentWriteSpeed(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def get_CurrentRotationTypeIsPureCAV(self, value: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def get_SupportedWriteSpeeds(self, supportedSpeeds: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def get_SupportedWriteSpeedDescriptors(self, supportedSpeedDescriptors: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDiscFormat2TrackAtOnceEventArgs(ComPtr):
    extends: win32more.Windows.Win32.Storage.Imapi.IWriteEngine2EventArgs
    _iid_ = Guid('{27354140-7f64-5b0f-8f00-5d77afbe261e}')
    @commethod(14)
    def get_CurrentTrackNumber(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_CurrentAction(self, value: POINTER(win32more.Windows.Win32.Storage.Imapi.IMAPI_FORMAT2_TAO_WRITE_ACTION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_ElapsedTime(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_RemainingTime(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDiscMaster(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{520cca62-51a5-11d3-9144-00104ba11c5e}')
    @commethod(3)
    def Open(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EnumDiscMasterFormats(self, ppEnum: POINTER(win32more.Windows.Win32.Storage.Imapi.IEnumDiscMasterFormats)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetActiveDiscMasterFormat(self, lpiid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetActiveDiscMasterFormat(self, riid: POINTER(Guid), ppUnk: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def EnumDiscRecorders(self, ppEnum: POINTER(win32more.Windows.Win32.Storage.Imapi.IEnumDiscRecorders)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetActiveDiscRecorder(self, ppRecorder: POINTER(win32more.Windows.Win32.Storage.Imapi.IDiscRecorder)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetActiveDiscRecorder(self, pRecorder: win32more.Windows.Win32.Storage.Imapi.IDiscRecorder) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def ClearFormatContent(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def ProgressAdvise(self, pEvents: win32more.Windows.Win32.Storage.Imapi.IDiscMasterProgressEvents, pvCookie: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def ProgressUnadvise(self, vCookie: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def RecordDisc(self, bSimulate: Byte, bEjectAfterBurn: Byte) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def Close(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDiscMaster2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{27354130-7f64-5b0f-8f00-5d77afbe261e}')
    @commethod(7)
    def get__NewEnum(self, ppunk: POINTER(win32more.Windows.Win32.System.Ole.IEnumVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, index: Int32, value: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_IsSupportedEnvironment(self, value: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDiscMasterProgressEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ec9e51c1-4e5d-11d3-9144-00104ba11c5e}')
    @commethod(3)
    def QueryCancel(self, pbCancel: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def NotifyPnPActivity(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def NotifyAddProgress(self, nCompletedSteps: Int32, nTotalSteps: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def NotifyBlockProgress(self, nCompleted: Int32, nTotal: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def NotifyTrackProgress(self, nCurrentTrack: Int32, nTotalTracks: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def NotifyPreparingBurn(self, nEstimatedSeconds: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def NotifyClosingDisc(self, nEstimatedSeconds: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def NotifyBurnComplete(self, status: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def NotifyEraseComplete(self, status: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDiscRecorder(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{85ac9776-ca88-4cf2-894e-09598c078a41}')
    @commethod(3)
    def Init(self, pbyUniqueID: POINTER(Byte), nulIDSize: UInt32, nulDriveNumber: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetRecorderGUID(self, pbyUniqueID: POINTER(Byte), ulBufferSize: UInt32, pulReturnSizeRequired: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetRecorderType(self, fTypeCode: POINTER(win32more.Windows.Win32.Storage.Imapi.RECORDER_TYPES)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetDisplayNames(self, pbstrVendorID: POINTER(win32more.Windows.Win32.Foundation.BSTR), pbstrProductID: POINTER(win32more.Windows.Win32.Foundation.BSTR), pbstrRevision: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetBasePnPID(self, pbstrBasePnPID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetPath(self, pbstrPath: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRecorderProperties(self, ppPropStg: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyStorage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetRecorderProperties(self, pPropStg: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyStorage) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetRecorderState(self, pulDevStateFlags: POINTER(win32more.Windows.Win32.Storage.Imapi.DISC_RECORDER_STATE_FLAGS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def OpenExclusive(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def QueryMediaType(self, fMediaType: POINTER(win32more.Windows.Win32.Storage.Imapi.MEDIA_TYPES), fMediaFlags: POINTER(win32more.Windows.Win32.Storage.Imapi.MEDIA_FLAGS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def QueryMediaInfo(self, pbSessions: POINTER(Byte), pbLastTrack: POINTER(Byte), ulStartAddress: POINTER(UInt32), ulNextWritable: POINTER(UInt32), ulFreeBlocks: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Eject(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Erase(self, bFullErase: Byte) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def Close(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDiscRecorder2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{27354133-7f64-5b0f-8f00-5d77afbe261e}')
    @commethod(7)
    def EjectMedia(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CloseTray(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AcquireExclusiveAccess(self, force: win32more.Windows.Win32.Foundation.VARIANT_BOOL, __MIDL__IDiscRecorder20000: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def ReleaseExclusiveAccess(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def DisableMcn(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def EnableMcn(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def InitializeDiscRecorder(self, recorderUniqueId: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_ActiveDiscRecorder(self, value: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_VendorId(self, value: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_ProductId(self, value: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_ProductRevision(self, value: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_VolumeName(self, value: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_VolumePathNames(self, value: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_DeviceCanLoadMedia(self, value: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_LegacyDeviceNumber(self, legacyDeviceNumber: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_SupportedFeaturePages(self, value: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_CurrentFeaturePages(self, value: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_SupportedProfiles(self, value: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_CurrentProfiles(self, value: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_SupportedModePages(self, value: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_ExclusiveAccessOwner(self, value: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDiscRecorder2Ex(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{27354132-7f64-5b0f-8f00-5d77afbe261e}')
    @commethod(3)
    def SendCommandNoData(self, Cdb: POINTER(Byte), CdbSize: UInt32, SenseBuffer: POINTER(Byte), Timeout: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SendCommandSendDataToDevice(self, Cdb: POINTER(Byte), CdbSize: UInt32, SenseBuffer: POINTER(Byte), Timeout: UInt32, Buffer: POINTER(Byte), BufferSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SendCommandGetDataFromDevice(self, Cdb: POINTER(Byte), CdbSize: UInt32, SenseBuffer: POINTER(Byte), Timeout: UInt32, Buffer: POINTER(Byte), BufferSize: UInt32, BufferFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ReadDvdStructure(self, format: UInt32, address: UInt32, layer: UInt32, agid: UInt32, data: POINTER(POINTER(Byte)), count: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SendDvdStructure(self, format: UInt32, data: POINTER(Byte), count: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetAdapterDescriptor(self, data: POINTER(POINTER(Byte)), byteSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetDeviceDescriptor(self, data: POINTER(POINTER(Byte)), byteSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetDiscInformation(self, discInformation: POINTER(POINTER(Byte)), byteSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetTrackInformation(self, address: UInt32, addressType: win32more.Windows.Win32.Storage.Imapi.IMAPI_READ_TRACK_ADDRESS_TYPE, trackInformation: POINTER(POINTER(Byte)), byteSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetFeaturePage(self, requestedFeature: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE, currentFeatureOnly: win32more.Windows.Win32.Foundation.BOOLEAN, featureData: POINTER(POINTER(Byte)), byteSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetModePage(self, requestedModePage: win32more.Windows.Win32.Storage.Imapi.IMAPI_MODE_PAGE_TYPE, requestType: win32more.Windows.Win32.Storage.Imapi.IMAPI_MODE_PAGE_REQUEST_TYPE, modePageData: POINTER(POINTER(Byte)), byteSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetModePage(self, requestType: win32more.Windows.Win32.Storage.Imapi.IMAPI_MODE_PAGE_REQUEST_TYPE, data: POINTER(Byte), byteSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetSupportedFeaturePages(self, currentFeatureOnly: win32more.Windows.Win32.Foundation.BOOLEAN, featureData: POINTER(POINTER(win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE)), byteSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetSupportedProfiles(self, currentOnly: win32more.Windows.Win32.Foundation.BOOLEAN, profileTypes: POINTER(POINTER(win32more.Windows.Win32.Storage.Imapi.IMAPI_PROFILE_TYPE)), validProfiles: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetSupportedModePages(self, requestType: win32more.Windows.Win32.Storage.Imapi.IMAPI_MODE_PAGE_REQUEST_TYPE, modePageTypes: POINTER(POINTER(win32more.Windows.Win32.Storage.Imapi.IMAPI_MODE_PAGE_TYPE)), validPages: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetByteAlignmentMask(self, value: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetMaximumNonPageAlignedTransferSize(self, value: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetMaximumPageAlignedTransferSize(self, value: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumDiscMasterFormats(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ddf445e1-54ba-11d3-9144-00104ba11c5e}')
    @commethod(3)
    def Next(self, cFormats: UInt32, lpiidFormatID: POINTER(Guid), pcFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, cFormats: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.Storage.Imapi.IEnumDiscMasterFormats)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumDiscRecorders(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9b1921e1-54ac-11d3-9144-00104ba11c5e}')
    @commethod(3)
    def Next(self, cRecorders: UInt32, ppRecorder: POINTER(win32more.Windows.Win32.Storage.Imapi.IDiscRecorder), pcFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, cRecorders: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.Storage.Imapi.IEnumDiscRecorders)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumFsiItems(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2c941fda-975b-59be-a960-9a2a262853a5}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(win32more.Windows.Win32.Storage.Imapi.IFsiItem), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.Storage.Imapi.IEnumFsiItems)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumProgressItems(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2c941fd6-975b-59be-a960-9a2a262853a5}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(win32more.Windows.Win32.Storage.Imapi.IProgressItem), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.Storage.Imapi.IEnumProgressItems)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFileSystemImage(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{2c941fe1-975b-59be-a960-9a2a262853a5}')
    @commethod(7)
    def get_Root(self, pVal: POINTER(win32more.Windows.Win32.Storage.Imapi.IFsiDirectoryItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_SessionStartBlock(self, pVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_SessionStartBlock(self, newVal: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_FreeMediaBlocks(self, pVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_FreeMediaBlocks(self, newVal: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetMaxMediaBlocksFromDevice(self, discRecorder: win32more.Windows.Win32.Storage.Imapi.IDiscRecorder2) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_UsedBlocks(self, pVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_VolumeName(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_VolumeName(self, newVal: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_ImportedVolumeName(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_BootImageOptions(self, pVal: POINTER(win32more.Windows.Win32.Storage.Imapi.IBootOptions)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_BootImageOptions(self, newVal: win32more.Windows.Win32.Storage.Imapi.IBootOptions) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_FileCount(self, pVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_DirectoryCount(self, pVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_WorkingDirectory(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_WorkingDirectory(self, newVal: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_ChangePoint(self, pVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_StrictFileSystemCompliance(self, pVal: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_StrictFileSystemCompliance(self, newVal: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_UseRestrictedCharacterSet(self, pVal: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_UseRestrictedCharacterSet(self, newVal: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_FileSystemsToCreate(self, pVal: POINTER(win32more.Windows.Win32.Storage.Imapi.FsiFileSystems)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def put_FileSystemsToCreate(self, newVal: win32more.Windows.Win32.Storage.Imapi.FsiFileSystems) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_FileSystemsSupported(self, pVal: POINTER(win32more.Windows.Win32.Storage.Imapi.FsiFileSystems)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def put_UDFRevision(self, newVal: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def get_UDFRevision(self, pVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_UDFRevisionsSupported(self, pVal: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def ChooseImageDefaults(self, discRecorder: win32more.Windows.Win32.Storage.Imapi.IDiscRecorder2) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def ChooseImageDefaultsForMediaType(self, value: win32more.Windows.Win32.Storage.Imapi.IMAPI_MEDIA_PHYSICAL_TYPE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def put_ISO9660InterchangeLevel(self, newVal: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def get_ISO9660InterchangeLevel(self, pVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def get_ISO9660InterchangeLevelsSupported(self, pVal: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def CreateResultImage(self, resultStream: POINTER(win32more.Windows.Win32.Storage.Imapi.IFileSystemImageResult)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def Exists(self, fullPath: win32more.Windows.Win32.Foundation.BSTR, itemType: POINTER(win32more.Windows.Win32.Storage.Imapi.FsiItemType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def CalculateDiscIdentifier(self, discIdentifier: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def IdentifyFileSystemsOnDisc(self, discRecorder: win32more.Windows.Win32.Storage.Imapi.IDiscRecorder2, fileSystems: POINTER(win32more.Windows.Win32.Storage.Imapi.FsiFileSystems)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def GetDefaultFileSystemForImport(self, fileSystems: win32more.Windows.Win32.Storage.Imapi.FsiFileSystems, importDefault: POINTER(win32more.Windows.Win32.Storage.Imapi.FsiFileSystems)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def ImportFileSystem(self, importedFileSystem: POINTER(win32more.Windows.Win32.Storage.Imapi.FsiFileSystems)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def ImportSpecificFileSystem(self, fileSystemToUse: win32more.Windows.Win32.Storage.Imapi.FsiFileSystems) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def RollbackToChangePoint(self, changePoint: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def LockInChangePoint(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def CreateDirectoryItem(self, name: win32more.Windows.Win32.Foundation.BSTR, newItem: POINTER(win32more.Windows.Win32.Storage.Imapi.IFsiDirectoryItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def CreateFileItem(self, name: win32more.Windows.Win32.Foundation.BSTR, newItem: POINTER(win32more.Windows.Win32.Storage.Imapi.IFsiFileItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def get_VolumeNameUDF(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def get_VolumeNameJoliet(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def get_VolumeNameISO9660(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def get_StageFiles(self, pVal: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def put_StageFiles(self, newVal: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def get_MultisessionInterfaces(self, pVal: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def put_MultisessionInterfaces(self, newVal: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFileSystemImage2(ComPtr):
    extends: win32more.Windows.Win32.Storage.Imapi.IFileSystemImage
    _iid_ = Guid('{d7644b2c-1537-4767-b62f-f1387b02ddfd}')
    @commethod(57)
    def get_BootImageOptionsArray(self, pVal: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(58)
    def put_BootImageOptionsArray(self, newVal: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFileSystemImage3(ComPtr):
    extends: win32more.Windows.Win32.Storage.Imapi.IFileSystemImage2
    _iid_ = Guid('{7cff842c-7e97-4807-8304-910dd8f7c051}')
    @commethod(59)
    def get_CreateRedundantUdfMetadataFiles(self, pVal: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(60)
    def put_CreateRedundantUdfMetadataFiles(self, newVal: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(61)
    def ProbeSpecificFileSystem(self, fileSystemToProbe: win32more.Windows.Win32.Storage.Imapi.FsiFileSystems, isAppendable: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFileSystemImageResult(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{2c941fd8-975b-59be-a960-9a2a262853a5}')
    @commethod(7)
    def get_ImageStream(self, pVal: POINTER(win32more.Windows.Win32.System.Com.IStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_ProgressItems(self, pVal: POINTER(win32more.Windows.Win32.Storage.Imapi.IProgressItems)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_TotalBlocks(self, pVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_BlockSize(self, pVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_DiscId(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFileSystemImageResult2(ComPtr):
    extends: win32more.Windows.Win32.Storage.Imapi.IFileSystemImageResult
    _iid_ = Guid('{b507ca29-2204-11dd-966a-001aa01bbc58}')
    @commethod(12)
    def get_ModifiedBlocks(self, pVal: POINTER(win32more.Windows.Win32.Storage.Imapi.IBlockRangeList)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsiDirectoryItem(ComPtr):
    extends: win32more.Windows.Win32.Storage.Imapi.IFsiItem
    _iid_ = Guid('{2c941fdc-975b-59be-a960-9a2a262853a5}')
    @commethod(19)
    def get__NewEnum(self, NewEnum: POINTER(win32more.Windows.Win32.System.Ole.IEnumVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_Item(self, path: win32more.Windows.Win32.Foundation.BSTR, item: POINTER(win32more.Windows.Win32.Storage.Imapi.IFsiItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_Count(self, Count: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_EnumFsiItems(self, NewEnum: POINTER(win32more.Windows.Win32.Storage.Imapi.IEnumFsiItems)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def AddDirectory(self, path: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def AddFile(self, path: win32more.Windows.Win32.Foundation.BSTR, fileData: win32more.Windows.Win32.System.Com.IStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def AddTree(self, sourceDirectory: win32more.Windows.Win32.Foundation.BSTR, includeBaseDirectory: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def Add(self, item: win32more.Windows.Win32.Storage.Imapi.IFsiItem) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def Remove(self, path: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def RemoveTree(self, path: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsiDirectoryItem2(ComPtr):
    extends: win32more.Windows.Win32.Storage.Imapi.IFsiDirectoryItem
    _iid_ = Guid('{f7fb4b9b-6d96-4d7b-9115-201b144811ef}')
    @commethod(29)
    def AddTreeWithNamedStreams(self, sourceDirectory: win32more.Windows.Win32.Foundation.BSTR, includeBaseDirectory: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsiFileItem(ComPtr):
    extends: win32more.Windows.Win32.Storage.Imapi.IFsiItem
    _iid_ = Guid('{2c941fdb-975b-59be-a960-9a2a262853a5}')
    @commethod(19)
    def get_DataSize(self, pVal: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_DataSize32BitLow(self, pVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_DataSize32BitHigh(self, pVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_Data(self, pVal: POINTER(win32more.Windows.Win32.System.Com.IStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_Data(self, newVal: win32more.Windows.Win32.System.Com.IStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsiFileItem2(ComPtr):
    extends: win32more.Windows.Win32.Storage.Imapi.IFsiFileItem
    _iid_ = Guid('{199d0c19-11e1-40eb-8ec2-c8c822a07792}')
    @commethod(24)
    def get_FsiNamedStreams(self, streams: POINTER(win32more.Windows.Win32.Storage.Imapi.IFsiNamedStreams)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_IsNamedStream(self, pVal: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def AddStream(self, name: win32more.Windows.Win32.Foundation.BSTR, streamData: win32more.Windows.Win32.System.Com.IStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def RemoveStream(self, name: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_IsRealTime(self, pVal: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def put_IsRealTime(self, newVal: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsiItem(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{2c941fd9-975b-59be-a960-9a2a262853a5}')
    @commethod(7)
    def get_Name(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_FullPath(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_CreationTime(self, pVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_CreationTime(self, newVal: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_LastAccessedTime(self, pVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_LastAccessedTime(self, newVal: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_LastModifiedTime(self, pVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_LastModifiedTime(self, newVal: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_IsHidden(self, pVal: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_IsHidden(self, newVal: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def FileSystemName(self, fileSystem: win32more.Windows.Win32.Storage.Imapi.FsiFileSystems, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def FileSystemPath(self, fileSystem: win32more.Windows.Win32.Storage.Imapi.FsiFileSystems, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFsiNamedStreams(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{ed79ba56-5294-4250-8d46-f9aecee23459}')
    @commethod(7)
    def get__NewEnum(self, NewEnum: POINTER(win32more.Windows.Win32.System.Ole.IEnumVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, index: Int32, item: POINTER(win32more.Windows.Win32.Storage.Imapi.IFsiFileItem2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(self, count: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_EnumNamedStreams(self, NewEnum: POINTER(win32more.Windows.Win32.Storage.Imapi.IEnumFsiItems)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IIsoImageManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{6ca38be5-fbbb-4800-95a1-a438865eb0d4}')
    @commethod(7)
    def get_Path(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Stream(self, data: POINTER(win32more.Windows.Win32.System.Com.IStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetPath(self, Val: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetStream(self, data: win32more.Windows.Win32.System.Com.IStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Validate(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IJolietDiscMaster(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e3bc42ce-4e5c-11d3-9144-00104ba11c5e}')
    @commethod(3)
    def GetTotalDataBlocks(self, pnBlocks: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetUsedDataBlocks(self, pnBlocks: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDataBlockSize(self, pnBlockBytes: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AddData(self, pStorage: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage, lFileOverwrite: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetJolietProperties(self, ppPropStg: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyStorage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetJolietProperties(self, pPropStg: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyStorage) -> win32more.Windows.Win32.Foundation.HRESULT: ...
IMAPI_BURN_VERIFICATION_LEVEL = Int32
IMAPI_BURN_VERIFICATION_NONE: win32more.Windows.Win32.Storage.Imapi.IMAPI_BURN_VERIFICATION_LEVEL = 0
IMAPI_BURN_VERIFICATION_QUICK: win32more.Windows.Win32.Storage.Imapi.IMAPI_BURN_VERIFICATION_LEVEL = 1
IMAPI_BURN_VERIFICATION_FULL: win32more.Windows.Win32.Storage.Imapi.IMAPI_BURN_VERIFICATION_LEVEL = 2
IMAPI_CD_SECTOR_TYPE = Int32
IMAPI_CD_SECTOR_AUDIO: win32more.Windows.Win32.Storage.Imapi.IMAPI_CD_SECTOR_TYPE = 0
IMAPI_CD_SECTOR_MODE_ZERO: win32more.Windows.Win32.Storage.Imapi.IMAPI_CD_SECTOR_TYPE = 1
IMAPI_CD_SECTOR_MODE1: win32more.Windows.Win32.Storage.Imapi.IMAPI_CD_SECTOR_TYPE = 2
IMAPI_CD_SECTOR_MODE2FORM0: win32more.Windows.Win32.Storage.Imapi.IMAPI_CD_SECTOR_TYPE = 3
IMAPI_CD_SECTOR_MODE2FORM1: win32more.Windows.Win32.Storage.Imapi.IMAPI_CD_SECTOR_TYPE = 4
IMAPI_CD_SECTOR_MODE2FORM2: win32more.Windows.Win32.Storage.Imapi.IMAPI_CD_SECTOR_TYPE = 5
IMAPI_CD_SECTOR_MODE1RAW: win32more.Windows.Win32.Storage.Imapi.IMAPI_CD_SECTOR_TYPE = 6
IMAPI_CD_SECTOR_MODE2FORM0RAW: win32more.Windows.Win32.Storage.Imapi.IMAPI_CD_SECTOR_TYPE = 7
IMAPI_CD_SECTOR_MODE2FORM1RAW: win32more.Windows.Win32.Storage.Imapi.IMAPI_CD_SECTOR_TYPE = 8
IMAPI_CD_SECTOR_MODE2FORM2RAW: win32more.Windows.Win32.Storage.Imapi.IMAPI_CD_SECTOR_TYPE = 9
IMAPI_CD_TRACK_DIGITAL_COPY_SETTING = Int32
IMAPI_CD_TRACK_DIGITAL_COPY_PERMITTED: win32more.Windows.Win32.Storage.Imapi.IMAPI_CD_TRACK_DIGITAL_COPY_SETTING = 0
IMAPI_CD_TRACK_DIGITAL_COPY_PROHIBITED: win32more.Windows.Win32.Storage.Imapi.IMAPI_CD_TRACK_DIGITAL_COPY_SETTING = 1
IMAPI_CD_TRACK_DIGITAL_COPY_SCMS: win32more.Windows.Win32.Storage.Imapi.IMAPI_CD_TRACK_DIGITAL_COPY_SETTING = 2
IMAPI_FEATURE_PAGE_TYPE = Int32
IMAPI_FEATURE_PAGE_TYPE_PROFILE_LIST: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 0
IMAPI_FEATURE_PAGE_TYPE_CORE: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 1
IMAPI_FEATURE_PAGE_TYPE_MORPHING: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 2
IMAPI_FEATURE_PAGE_TYPE_REMOVABLE_MEDIUM: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 3
IMAPI_FEATURE_PAGE_TYPE_WRITE_PROTECT: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 4
IMAPI_FEATURE_PAGE_TYPE_RANDOMLY_READABLE: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 16
IMAPI_FEATURE_PAGE_TYPE_CD_MULTIREAD: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 29
IMAPI_FEATURE_PAGE_TYPE_CD_READ: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 30
IMAPI_FEATURE_PAGE_TYPE_DVD_READ: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 31
IMAPI_FEATURE_PAGE_TYPE_RANDOMLY_WRITABLE: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 32
IMAPI_FEATURE_PAGE_TYPE_INCREMENTAL_STREAMING_WRITABLE: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 33
IMAPI_FEATURE_PAGE_TYPE_SECTOR_ERASABLE: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 34
IMAPI_FEATURE_PAGE_TYPE_FORMATTABLE: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 35
IMAPI_FEATURE_PAGE_TYPE_HARDWARE_DEFECT_MANAGEMENT: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 36
IMAPI_FEATURE_PAGE_TYPE_WRITE_ONCE: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 37
IMAPI_FEATURE_PAGE_TYPE_RESTRICTED_OVERWRITE: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 38
IMAPI_FEATURE_PAGE_TYPE_CDRW_CAV_WRITE: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 39
IMAPI_FEATURE_PAGE_TYPE_MRW: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 40
IMAPI_FEATURE_PAGE_TYPE_ENHANCED_DEFECT_REPORTING: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 41
IMAPI_FEATURE_PAGE_TYPE_DVD_PLUS_RW: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 42
IMAPI_FEATURE_PAGE_TYPE_DVD_PLUS_R: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 43
IMAPI_FEATURE_PAGE_TYPE_RIGID_RESTRICTED_OVERWRITE: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 44
IMAPI_FEATURE_PAGE_TYPE_CD_TRACK_AT_ONCE: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 45
IMAPI_FEATURE_PAGE_TYPE_CD_MASTERING: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 46
IMAPI_FEATURE_PAGE_TYPE_DVD_DASH_WRITE: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 47
IMAPI_FEATURE_PAGE_TYPE_DOUBLE_DENSITY_CD_READ: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 48
IMAPI_FEATURE_PAGE_TYPE_DOUBLE_DENSITY_CD_R_WRITE: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 49
IMAPI_FEATURE_PAGE_TYPE_DOUBLE_DENSITY_CD_RW_WRITE: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 50
IMAPI_FEATURE_PAGE_TYPE_LAYER_JUMP_RECORDING: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 51
IMAPI_FEATURE_PAGE_TYPE_CD_RW_MEDIA_WRITE_SUPPORT: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 55
IMAPI_FEATURE_PAGE_TYPE_BD_PSEUDO_OVERWRITE: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 56
IMAPI_FEATURE_PAGE_TYPE_DVD_PLUS_R_DUAL_LAYER: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 59
IMAPI_FEATURE_PAGE_TYPE_BD_READ: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 64
IMAPI_FEATURE_PAGE_TYPE_BD_WRITE: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 65
IMAPI_FEATURE_PAGE_TYPE_HD_DVD_READ: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 80
IMAPI_FEATURE_PAGE_TYPE_HD_DVD_WRITE: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 81
IMAPI_FEATURE_PAGE_TYPE_POWER_MANAGEMENT: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 256
IMAPI_FEATURE_PAGE_TYPE_SMART: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 257
IMAPI_FEATURE_PAGE_TYPE_EMBEDDED_CHANGER: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 258
IMAPI_FEATURE_PAGE_TYPE_CD_ANALOG_PLAY: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 259
IMAPI_FEATURE_PAGE_TYPE_MICROCODE_UPDATE: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 260
IMAPI_FEATURE_PAGE_TYPE_TIMEOUT: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 261
IMAPI_FEATURE_PAGE_TYPE_DVD_CSS: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 262
IMAPI_FEATURE_PAGE_TYPE_REAL_TIME_STREAMING: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 263
IMAPI_FEATURE_PAGE_TYPE_LOGICAL_UNIT_SERIAL_NUMBER: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 264
IMAPI_FEATURE_PAGE_TYPE_MEDIA_SERIAL_NUMBER: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 265
IMAPI_FEATURE_PAGE_TYPE_DISC_CONTROL_BLOCKS: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 266
IMAPI_FEATURE_PAGE_TYPE_DVD_CPRM: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 267
IMAPI_FEATURE_PAGE_TYPE_FIRMWARE_INFORMATION: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 268
IMAPI_FEATURE_PAGE_TYPE_AACS: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 269
IMAPI_FEATURE_PAGE_TYPE_VCPS: win32more.Windows.Win32.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE = 272
IMAPI_FORMAT2_DATA_MEDIA_STATE = Int32
IMAPI_FORMAT2_DATA_MEDIA_STATE_UNKNOWN: win32more.Windows.Win32.Storage.Imapi.IMAPI_FORMAT2_DATA_MEDIA_STATE = 0
IMAPI_FORMAT2_DATA_MEDIA_STATE_INFORMATIONAL_MASK: win32more.Windows.Win32.Storage.Imapi.IMAPI_FORMAT2_DATA_MEDIA_STATE = 15
IMAPI_FORMAT2_DATA_MEDIA_STATE_UNSUPPORTED_MASK: win32more.Windows.Win32.Storage.Imapi.IMAPI_FORMAT2_DATA_MEDIA_STATE = 64512
IMAPI_FORMAT2_DATA_MEDIA_STATE_OVERWRITE_ONLY: win32more.Windows.Win32.Storage.Imapi.IMAPI_FORMAT2_DATA_MEDIA_STATE = 1
IMAPI_FORMAT2_DATA_MEDIA_STATE_RANDOMLY_WRITABLE: win32more.Windows.Win32.Storage.Imapi.IMAPI_FORMAT2_DATA_MEDIA_STATE = 1
IMAPI_FORMAT2_DATA_MEDIA_STATE_BLANK: win32more.Windows.Win32.Storage.Imapi.IMAPI_FORMAT2_DATA_MEDIA_STATE = 2
IMAPI_FORMAT2_DATA_MEDIA_STATE_APPENDABLE: win32more.Windows.Win32.Storage.Imapi.IMAPI_FORMAT2_DATA_MEDIA_STATE = 4
IMAPI_FORMAT2_DATA_MEDIA_STATE_FINAL_SESSION: win32more.Windows.Win32.Storage.Imapi.IMAPI_FORMAT2_DATA_MEDIA_STATE = 8
IMAPI_FORMAT2_DATA_MEDIA_STATE_DAMAGED: win32more.Windows.Win32.Storage.Imapi.IMAPI_FORMAT2_DATA_MEDIA_STATE = 1024
IMAPI_FORMAT2_DATA_MEDIA_STATE_ERASE_REQUIRED: win32more.Windows.Win32.Storage.Imapi.IMAPI_FORMAT2_DATA_MEDIA_STATE = 2048
IMAPI_FORMAT2_DATA_MEDIA_STATE_NON_EMPTY_SESSION: win32more.Windows.Win32.Storage.Imapi.IMAPI_FORMAT2_DATA_MEDIA_STATE = 4096
IMAPI_FORMAT2_DATA_MEDIA_STATE_WRITE_PROTECTED: win32more.Windows.Win32.Storage.Imapi.IMAPI_FORMAT2_DATA_MEDIA_STATE = 8192
IMAPI_FORMAT2_DATA_MEDIA_STATE_FINALIZED: win32more.Windows.Win32.Storage.Imapi.IMAPI_FORMAT2_DATA_MEDIA_STATE = 16384
IMAPI_FORMAT2_DATA_MEDIA_STATE_UNSUPPORTED_MEDIA: win32more.Windows.Win32.Storage.Imapi.IMAPI_FORMAT2_DATA_MEDIA_STATE = 32768
IMAPI_FORMAT2_DATA_WRITE_ACTION = Int32
IMAPI_FORMAT2_DATA_WRITE_ACTION_VALIDATING_MEDIA: win32more.Windows.Win32.Storage.Imapi.IMAPI_FORMAT2_DATA_WRITE_ACTION = 0
IMAPI_FORMAT2_DATA_WRITE_ACTION_FORMATTING_MEDIA: win32more.Windows.Win32.Storage.Imapi.IMAPI_FORMAT2_DATA_WRITE_ACTION = 1
IMAPI_FORMAT2_DATA_WRITE_ACTION_INITIALIZING_HARDWARE: win32more.Windows.Win32.Storage.Imapi.IMAPI_FORMAT2_DATA_WRITE_ACTION = 2
IMAPI_FORMAT2_DATA_WRITE_ACTION_CALIBRATING_POWER: win32more.Windows.Win32.Storage.Imapi.IMAPI_FORMAT2_DATA_WRITE_ACTION = 3
IMAPI_FORMAT2_DATA_WRITE_ACTION_WRITING_DATA: win32more.Windows.Win32.Storage.Imapi.IMAPI_FORMAT2_DATA_WRITE_ACTION = 4
IMAPI_FORMAT2_DATA_WRITE_ACTION_FINALIZATION: win32more.Windows.Win32.Storage.Imapi.IMAPI_FORMAT2_DATA_WRITE_ACTION = 5
IMAPI_FORMAT2_DATA_WRITE_ACTION_COMPLETED: win32more.Windows.Win32.Storage.Imapi.IMAPI_FORMAT2_DATA_WRITE_ACTION = 6
IMAPI_FORMAT2_DATA_WRITE_ACTION_VERIFYING: win32more.Windows.Win32.Storage.Imapi.IMAPI_FORMAT2_DATA_WRITE_ACTION = 7
IMAPI_FORMAT2_RAW_CD_DATA_SECTOR_TYPE = Int32
IMAPI_FORMAT2_RAW_CD_SUBCODE_PQ_ONLY: win32more.Windows.Win32.Storage.Imapi.IMAPI_FORMAT2_RAW_CD_DATA_SECTOR_TYPE = 1
IMAPI_FORMAT2_RAW_CD_SUBCODE_IS_COOKED: win32more.Windows.Win32.Storage.Imapi.IMAPI_FORMAT2_RAW_CD_DATA_SECTOR_TYPE = 2
IMAPI_FORMAT2_RAW_CD_SUBCODE_IS_RAW: win32more.Windows.Win32.Storage.Imapi.IMAPI_FORMAT2_RAW_CD_DATA_SECTOR_TYPE = 3
IMAPI_FORMAT2_RAW_CD_WRITE_ACTION = Int32
IMAPI_FORMAT2_RAW_CD_WRITE_ACTION_UNKNOWN: win32more.Windows.Win32.Storage.Imapi.IMAPI_FORMAT2_RAW_CD_WRITE_ACTION = 0
IMAPI_FORMAT2_RAW_CD_WRITE_ACTION_PREPARING: win32more.Windows.Win32.Storage.Imapi.IMAPI_FORMAT2_RAW_CD_WRITE_ACTION = 1
IMAPI_FORMAT2_RAW_CD_WRITE_ACTION_WRITING: win32more.Windows.Win32.Storage.Imapi.IMAPI_FORMAT2_RAW_CD_WRITE_ACTION = 2
IMAPI_FORMAT2_RAW_CD_WRITE_ACTION_FINISHING: win32more.Windows.Win32.Storage.Imapi.IMAPI_FORMAT2_RAW_CD_WRITE_ACTION = 3
IMAPI_FORMAT2_TAO_WRITE_ACTION = Int32
IMAPI_FORMAT2_TAO_WRITE_ACTION_UNKNOWN: win32more.Windows.Win32.Storage.Imapi.IMAPI_FORMAT2_TAO_WRITE_ACTION = 0
IMAPI_FORMAT2_TAO_WRITE_ACTION_PREPARING: win32more.Windows.Win32.Storage.Imapi.IMAPI_FORMAT2_TAO_WRITE_ACTION = 1
IMAPI_FORMAT2_TAO_WRITE_ACTION_WRITING: win32more.Windows.Win32.Storage.Imapi.IMAPI_FORMAT2_TAO_WRITE_ACTION = 2
IMAPI_FORMAT2_TAO_WRITE_ACTION_FINISHING: win32more.Windows.Win32.Storage.Imapi.IMAPI_FORMAT2_TAO_WRITE_ACTION = 3
IMAPI_FORMAT2_TAO_WRITE_ACTION_VERIFYING: win32more.Windows.Win32.Storage.Imapi.IMAPI_FORMAT2_TAO_WRITE_ACTION = 4
IMAPI_MEDIA_PHYSICAL_TYPE = Int32
IMAPI_MEDIA_TYPE_UNKNOWN: win32more.Windows.Win32.Storage.Imapi.IMAPI_MEDIA_PHYSICAL_TYPE = 0
IMAPI_MEDIA_TYPE_CDROM: win32more.Windows.Win32.Storage.Imapi.IMAPI_MEDIA_PHYSICAL_TYPE = 1
IMAPI_MEDIA_TYPE_CDR: win32more.Windows.Win32.Storage.Imapi.IMAPI_MEDIA_PHYSICAL_TYPE = 2
IMAPI_MEDIA_TYPE_CDRW: win32more.Windows.Win32.Storage.Imapi.IMAPI_MEDIA_PHYSICAL_TYPE = 3
IMAPI_MEDIA_TYPE_DVDROM: win32more.Windows.Win32.Storage.Imapi.IMAPI_MEDIA_PHYSICAL_TYPE = 4
IMAPI_MEDIA_TYPE_DVDRAM: win32more.Windows.Win32.Storage.Imapi.IMAPI_MEDIA_PHYSICAL_TYPE = 5
IMAPI_MEDIA_TYPE_DVDPLUSR: win32more.Windows.Win32.Storage.Imapi.IMAPI_MEDIA_PHYSICAL_TYPE = 6
IMAPI_MEDIA_TYPE_DVDPLUSRW: win32more.Windows.Win32.Storage.Imapi.IMAPI_MEDIA_PHYSICAL_TYPE = 7
IMAPI_MEDIA_TYPE_DVDPLUSR_DUALLAYER: win32more.Windows.Win32.Storage.Imapi.IMAPI_MEDIA_PHYSICAL_TYPE = 8
IMAPI_MEDIA_TYPE_DVDDASHR: win32more.Windows.Win32.Storage.Imapi.IMAPI_MEDIA_PHYSICAL_TYPE = 9
IMAPI_MEDIA_TYPE_DVDDASHRW: win32more.Windows.Win32.Storage.Imapi.IMAPI_MEDIA_PHYSICAL_TYPE = 10
IMAPI_MEDIA_TYPE_DVDDASHR_DUALLAYER: win32more.Windows.Win32.Storage.Imapi.IMAPI_MEDIA_PHYSICAL_TYPE = 11
IMAPI_MEDIA_TYPE_DISK: win32more.Windows.Win32.Storage.Imapi.IMAPI_MEDIA_PHYSICAL_TYPE = 12
IMAPI_MEDIA_TYPE_DVDPLUSRW_DUALLAYER: win32more.Windows.Win32.Storage.Imapi.IMAPI_MEDIA_PHYSICAL_TYPE = 13
IMAPI_MEDIA_TYPE_HDDVDROM: win32more.Windows.Win32.Storage.Imapi.IMAPI_MEDIA_PHYSICAL_TYPE = 14
IMAPI_MEDIA_TYPE_HDDVDR: win32more.Windows.Win32.Storage.Imapi.IMAPI_MEDIA_PHYSICAL_TYPE = 15
IMAPI_MEDIA_TYPE_HDDVDRAM: win32more.Windows.Win32.Storage.Imapi.IMAPI_MEDIA_PHYSICAL_TYPE = 16
IMAPI_MEDIA_TYPE_BDROM: win32more.Windows.Win32.Storage.Imapi.IMAPI_MEDIA_PHYSICAL_TYPE = 17
IMAPI_MEDIA_TYPE_BDR: win32more.Windows.Win32.Storage.Imapi.IMAPI_MEDIA_PHYSICAL_TYPE = 18
IMAPI_MEDIA_TYPE_BDRE: win32more.Windows.Win32.Storage.Imapi.IMAPI_MEDIA_PHYSICAL_TYPE = 19
IMAPI_MEDIA_TYPE_MAX: win32more.Windows.Win32.Storage.Imapi.IMAPI_MEDIA_PHYSICAL_TYPE = 19
IMAPI_MEDIA_WRITE_PROTECT_STATE = Int32
IMAPI_WRITEPROTECTED_UNTIL_POWERDOWN: win32more.Windows.Win32.Storage.Imapi.IMAPI_MEDIA_WRITE_PROTECT_STATE = 1
IMAPI_WRITEPROTECTED_BY_CARTRIDGE: win32more.Windows.Win32.Storage.Imapi.IMAPI_MEDIA_WRITE_PROTECT_STATE = 2
IMAPI_WRITEPROTECTED_BY_MEDIA_SPECIFIC_REASON: win32more.Windows.Win32.Storage.Imapi.IMAPI_MEDIA_WRITE_PROTECT_STATE = 4
IMAPI_WRITEPROTECTED_BY_SOFTWARE_WRITE_PROTECT: win32more.Windows.Win32.Storage.Imapi.IMAPI_MEDIA_WRITE_PROTECT_STATE = 8
IMAPI_WRITEPROTECTED_BY_DISC_CONTROL_BLOCK: win32more.Windows.Win32.Storage.Imapi.IMAPI_MEDIA_WRITE_PROTECT_STATE = 16
IMAPI_WRITEPROTECTED_READ_ONLY_MEDIA: win32more.Windows.Win32.Storage.Imapi.IMAPI_MEDIA_WRITE_PROTECT_STATE = 16384
IMAPI_MODE_PAGE_REQUEST_TYPE = Int32
IMAPI_MODE_PAGE_REQUEST_TYPE_CURRENT_VALUES: win32more.Windows.Win32.Storage.Imapi.IMAPI_MODE_PAGE_REQUEST_TYPE = 0
IMAPI_MODE_PAGE_REQUEST_TYPE_CHANGEABLE_VALUES: win32more.Windows.Win32.Storage.Imapi.IMAPI_MODE_PAGE_REQUEST_TYPE = 1
IMAPI_MODE_PAGE_REQUEST_TYPE_DEFAULT_VALUES: win32more.Windows.Win32.Storage.Imapi.IMAPI_MODE_PAGE_REQUEST_TYPE = 2
IMAPI_MODE_PAGE_REQUEST_TYPE_SAVED_VALUES: win32more.Windows.Win32.Storage.Imapi.IMAPI_MODE_PAGE_REQUEST_TYPE = 3
IMAPI_MODE_PAGE_TYPE = Int32
IMAPI_MODE_PAGE_TYPE_READ_WRITE_ERROR_RECOVERY: win32more.Windows.Win32.Storage.Imapi.IMAPI_MODE_PAGE_TYPE = 1
IMAPI_MODE_PAGE_TYPE_MRW: win32more.Windows.Win32.Storage.Imapi.IMAPI_MODE_PAGE_TYPE = 3
IMAPI_MODE_PAGE_TYPE_WRITE_PARAMETERS: win32more.Windows.Win32.Storage.Imapi.IMAPI_MODE_PAGE_TYPE = 5
IMAPI_MODE_PAGE_TYPE_CACHING: win32more.Windows.Win32.Storage.Imapi.IMAPI_MODE_PAGE_TYPE = 8
IMAPI_MODE_PAGE_TYPE_INFORMATIONAL_EXCEPTIONS: win32more.Windows.Win32.Storage.Imapi.IMAPI_MODE_PAGE_TYPE = 28
IMAPI_MODE_PAGE_TYPE_TIMEOUT_AND_PROTECT: win32more.Windows.Win32.Storage.Imapi.IMAPI_MODE_PAGE_TYPE = 29
IMAPI_MODE_PAGE_TYPE_POWER_CONDITION: win32more.Windows.Win32.Storage.Imapi.IMAPI_MODE_PAGE_TYPE = 26
IMAPI_MODE_PAGE_TYPE_LEGACY_CAPABILITIES: win32more.Windows.Win32.Storage.Imapi.IMAPI_MODE_PAGE_TYPE = 42
IMAPI_PROFILE_TYPE = Int32
IMAPI_PROFILE_TYPE_INVALID: win32more.Windows.Win32.Storage.Imapi.IMAPI_PROFILE_TYPE = 0
IMAPI_PROFILE_TYPE_NON_REMOVABLE_DISK: win32more.Windows.Win32.Storage.Imapi.IMAPI_PROFILE_TYPE = 1
IMAPI_PROFILE_TYPE_REMOVABLE_DISK: win32more.Windows.Win32.Storage.Imapi.IMAPI_PROFILE_TYPE = 2
IMAPI_PROFILE_TYPE_MO_ERASABLE: win32more.Windows.Win32.Storage.Imapi.IMAPI_PROFILE_TYPE = 3
IMAPI_PROFILE_TYPE_MO_WRITE_ONCE: win32more.Windows.Win32.Storage.Imapi.IMAPI_PROFILE_TYPE = 4
IMAPI_PROFILE_TYPE_AS_MO: win32more.Windows.Win32.Storage.Imapi.IMAPI_PROFILE_TYPE = 5
IMAPI_PROFILE_TYPE_CDROM: win32more.Windows.Win32.Storage.Imapi.IMAPI_PROFILE_TYPE = 8
IMAPI_PROFILE_TYPE_CD_RECORDABLE: win32more.Windows.Win32.Storage.Imapi.IMAPI_PROFILE_TYPE = 9
IMAPI_PROFILE_TYPE_CD_REWRITABLE: win32more.Windows.Win32.Storage.Imapi.IMAPI_PROFILE_TYPE = 10
IMAPI_PROFILE_TYPE_DVDROM: win32more.Windows.Win32.Storage.Imapi.IMAPI_PROFILE_TYPE = 16
IMAPI_PROFILE_TYPE_DVD_DASH_RECORDABLE: win32more.Windows.Win32.Storage.Imapi.IMAPI_PROFILE_TYPE = 17
IMAPI_PROFILE_TYPE_DVD_RAM: win32more.Windows.Win32.Storage.Imapi.IMAPI_PROFILE_TYPE = 18
IMAPI_PROFILE_TYPE_DVD_DASH_REWRITABLE: win32more.Windows.Win32.Storage.Imapi.IMAPI_PROFILE_TYPE = 19
IMAPI_PROFILE_TYPE_DVD_DASH_RW_SEQUENTIAL: win32more.Windows.Win32.Storage.Imapi.IMAPI_PROFILE_TYPE = 20
IMAPI_PROFILE_TYPE_DVD_DASH_R_DUAL_SEQUENTIAL: win32more.Windows.Win32.Storage.Imapi.IMAPI_PROFILE_TYPE = 21
IMAPI_PROFILE_TYPE_DVD_DASH_R_DUAL_LAYER_JUMP: win32more.Windows.Win32.Storage.Imapi.IMAPI_PROFILE_TYPE = 22
IMAPI_PROFILE_TYPE_DVD_PLUS_RW: win32more.Windows.Win32.Storage.Imapi.IMAPI_PROFILE_TYPE = 26
IMAPI_PROFILE_TYPE_DVD_PLUS_R: win32more.Windows.Win32.Storage.Imapi.IMAPI_PROFILE_TYPE = 27
IMAPI_PROFILE_TYPE_DDCDROM: win32more.Windows.Win32.Storage.Imapi.IMAPI_PROFILE_TYPE = 32
IMAPI_PROFILE_TYPE_DDCD_RECORDABLE: win32more.Windows.Win32.Storage.Imapi.IMAPI_PROFILE_TYPE = 33
IMAPI_PROFILE_TYPE_DDCD_REWRITABLE: win32more.Windows.Win32.Storage.Imapi.IMAPI_PROFILE_TYPE = 34
IMAPI_PROFILE_TYPE_DVD_PLUS_RW_DUAL: win32more.Windows.Win32.Storage.Imapi.IMAPI_PROFILE_TYPE = 42
IMAPI_PROFILE_TYPE_DVD_PLUS_R_DUAL: win32more.Windows.Win32.Storage.Imapi.IMAPI_PROFILE_TYPE = 43
IMAPI_PROFILE_TYPE_BD_ROM: win32more.Windows.Win32.Storage.Imapi.IMAPI_PROFILE_TYPE = 64
IMAPI_PROFILE_TYPE_BD_R_SEQUENTIAL: win32more.Windows.Win32.Storage.Imapi.IMAPI_PROFILE_TYPE = 65
IMAPI_PROFILE_TYPE_BD_R_RANDOM_RECORDING: win32more.Windows.Win32.Storage.Imapi.IMAPI_PROFILE_TYPE = 66
IMAPI_PROFILE_TYPE_BD_REWRITABLE: win32more.Windows.Win32.Storage.Imapi.IMAPI_PROFILE_TYPE = 67
IMAPI_PROFILE_TYPE_HD_DVD_ROM: win32more.Windows.Win32.Storage.Imapi.IMAPI_PROFILE_TYPE = 80
IMAPI_PROFILE_TYPE_HD_DVD_RECORDABLE: win32more.Windows.Win32.Storage.Imapi.IMAPI_PROFILE_TYPE = 81
IMAPI_PROFILE_TYPE_HD_DVD_RAM: win32more.Windows.Win32.Storage.Imapi.IMAPI_PROFILE_TYPE = 82
IMAPI_PROFILE_TYPE_NON_STANDARD: win32more.Windows.Win32.Storage.Imapi.IMAPI_PROFILE_TYPE = 65535
IMAPI_READ_TRACK_ADDRESS_TYPE = Int32
IMAPI_READ_TRACK_ADDRESS_TYPE_LBA: win32more.Windows.Win32.Storage.Imapi.IMAPI_READ_TRACK_ADDRESS_TYPE = 0
IMAPI_READ_TRACK_ADDRESS_TYPE_TRACK: win32more.Windows.Win32.Storage.Imapi.IMAPI_READ_TRACK_ADDRESS_TYPE = 1
IMAPI_READ_TRACK_ADDRESS_TYPE_SESSION: win32more.Windows.Win32.Storage.Imapi.IMAPI_READ_TRACK_ADDRESS_TYPE = 2
IMMPID_CPV_ENUM = Int32
IMMPID_CPV_BEFORE__: win32more.Windows.Win32.Storage.Imapi.IMMPID_CPV_ENUM = 32767
IMMPID_CP_START: win32more.Windows.Win32.Storage.Imapi.IMMPID_CPV_ENUM = 32768
IMMPID_CPV_AFTER__: win32more.Windows.Win32.Storage.Imapi.IMMPID_CPV_ENUM = 32769
IMMPID_MPV_ENUM = Int32
IMMPID_MPV_BEFORE__: win32more.Windows.Win32.Storage.Imapi.IMMPID_MPV_ENUM = 12287
IMMPID_MPV_STORE_DRIVER_HANDLE: win32more.Windows.Win32.Storage.Imapi.IMMPID_MPV_ENUM = 12288
IMMPID_MPV_MESSAGE_CREATION_FLAGS: win32more.Windows.Win32.Storage.Imapi.IMMPID_MPV_ENUM = 12289
IMMPID_MPV_MESSAGE_OPEN_HANDLES: win32more.Windows.Win32.Storage.Imapi.IMMPID_MPV_ENUM = 12290
IMMPID_MPV_TOTAL_OPEN_HANDLES: win32more.Windows.Win32.Storage.Imapi.IMMPID_MPV_ENUM = 12291
IMMPID_MPV_TOTAL_OPEN_PROPERTY_STREAM_HANDLES: win32more.Windows.Win32.Storage.Imapi.IMMPID_MPV_ENUM = 12292
IMMPID_MPV_TOTAL_OPEN_CONTENT_HANDLES: win32more.Windows.Win32.Storage.Imapi.IMMPID_MPV_ENUM = 12293
IMMPID_MPV_AFTER__: win32more.Windows.Win32.Storage.Imapi.IMMPID_MPV_ENUM = 12294
IMMPID_MP_ENUM = Int32
IMMPID_MP_BEFORE__: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4095
IMMPID_MP_RECIPIENT_LIST: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4096
IMMPID_MP_CONTENT_FILE_NAME: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4097
IMMPID_MP_SENDER_ADDRESS_SMTP: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4098
IMMPID_MP_SENDER_ADDRESS_X500: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4099
IMMPID_MP_SENDER_ADDRESS_X400: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4100
IMMPID_MP_SENDER_ADDRESS_LEGACY_EX_DN: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4101
IMMPID_MP_DOMAIN_LIST: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4102
IMMPID_MP_PICKUP_FILE_NAME: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4103
IMMPID_MP_AUTHENTICATED_USER_NAME: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4104
IMMPID_MP_CONNECTION_IP_ADDRESS: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4105
IMMPID_MP_HELO_DOMAIN: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4106
IMMPID_MP_EIGHTBIT_MIME_OPTION: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4107
IMMPID_MP_CHUNKING_OPTION: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4108
IMMPID_MP_BINARYMIME_OPTION: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4109
IMMPID_MP_REMOTE_AUTHENTICATION_TYPE: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4110
IMMPID_MP_ERROR_CODE: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4111
IMMPID_MP_DSN_ENVID_VALUE: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4112
IMMPID_MP_DSN_RET_VALUE: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4113
IMMPID_MP_REMOTE_SERVER_DSN_CAPABLE: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4114
IMMPID_MP_ARRIVAL_TIME: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4115
IMMPID_MP_MESSAGE_STATUS: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4116
IMMPID_MP_EXPIRE_DELAY: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4117
IMMPID_MP_EXPIRE_NDR: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4118
IMMPID_MP_LOCAL_EXPIRE_DELAY: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4119
IMMPID_MP_LOCAL_EXPIRE_NDR: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4120
IMMPID_MP_ARRIVAL_FILETIME: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4121
IMMPID_MP_HR_CAT_STATUS: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4122
IMMPID_MP_MSG_GUID: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4123
IMMPID_MP_SUPERSEDES_MSG_GUID: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4124
IMMPID_MP_SCANNED_FOR_CRLF_DOT_CRLF: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4125
IMMPID_MP_FOUND_EMBEDDED_CRLF_DOT_CRLF: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4126
IMMPID_MP_MSG_SIZE_HINT: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4127
IMMPID_MP_RFC822_MSG_ID: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4128
IMMPID_MP_RFC822_MSG_SUBJECT: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4129
IMMPID_MP_RFC822_FROM_ADDRESS: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4130
IMMPID_MP_RFC822_TO_ADDRESS: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4131
IMMPID_MP_RFC822_CC_ADDRESS: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4132
IMMPID_MP_RFC822_BCC_ADDRESS: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4133
IMMPID_MP_CONNECTION_SERVER_IP_ADDRESS: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4134
IMMPID_MP_SERVER_NAME: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4135
IMMPID_MP_SERVER_VERSION: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4136
IMMPID_MP_NUM_RECIPIENTS: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4137
IMMPID_MP_X_PRIORITY: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4138
IMMPID_MP_FROM_ADDRESS: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4139
IMMPID_MP_SENDER_ADDRESS: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4140
IMMPID_MP_DEFERRED_DELIVERY_FILETIME: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4141
IMMPID_MP_SENDER_ADDRESS_OTHER: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4142
IMMPID_MP_ORIGINAL_ARRIVAL_TIME: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4143
IMMPID_MP_MSGCLASS: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4144
IMMPID_MP_CONTENT_TYPE: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4145
IMMPID_MP_ENCRYPTION_TYPE: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4146
IMMPID_MP_CONNECTION_SERVER_PORT: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4147
IMMPID_MP_CLIENT_AUTH_USER: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4148
IMMPID_MP_CLIENT_AUTH_TYPE: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4149
IMMPID_MP_CRC_GLOBAL: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4150
IMMPID_MP_CRC_RECIPS: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4151
IMMPID_MP_INBOUND_MAIL_FROM_AUTH: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4152
IMMPID_MP_AFTER__: win32more.Windows.Win32.Storage.Imapi.IMMPID_MP_ENUM = 4153
IMMPID_NMP_ENUM = Int32
IMMPID_NMP_BEFORE__: win32more.Windows.Win32.Storage.Imapi.IMMPID_NMP_ENUM = 24575
IMMPID_NMP_SECONDARY_GROUPS: win32more.Windows.Win32.Storage.Imapi.IMMPID_NMP_ENUM = 24576
IMMPID_NMP_SECONDARY_ARTNUM: win32more.Windows.Win32.Storage.Imapi.IMMPID_NMP_ENUM = 24577
IMMPID_NMP_PRIMARY_GROUP: win32more.Windows.Win32.Storage.Imapi.IMMPID_NMP_ENUM = 24578
IMMPID_NMP_PRIMARY_ARTID: win32more.Windows.Win32.Storage.Imapi.IMMPID_NMP_ENUM = 24579
IMMPID_NMP_POST_TOKEN: win32more.Windows.Win32.Storage.Imapi.IMMPID_NMP_ENUM = 24580
IMMPID_NMP_NEWSGROUP_LIST: win32more.Windows.Win32.Storage.Imapi.IMMPID_NMP_ENUM = 24581
IMMPID_NMP_HEADERS: win32more.Windows.Win32.Storage.Imapi.IMMPID_NMP_ENUM = 24582
IMMPID_NMP_NNTP_PROCESSING: win32more.Windows.Win32.Storage.Imapi.IMMPID_NMP_ENUM = 24583
IMMPID_NMP_NNTP_APPROVED_HEADER: win32more.Windows.Win32.Storage.Imapi.IMMPID_NMP_ENUM = 24584
IMMPID_NMP_AFTER__: win32more.Windows.Win32.Storage.Imapi.IMMPID_NMP_ENUM = 24585
IMMPID_RPV_ENUM = Int32
IMMPID_RPV_BEFORE__: win32more.Windows.Win32.Storage.Imapi.IMMPID_RPV_ENUM = 16383
IMMPID_RPV_DONT_DELIVER: win32more.Windows.Win32.Storage.Imapi.IMMPID_RPV_ENUM = 16384
IMMPID_RPV_NO_NAME_COLLISIONS: win32more.Windows.Win32.Storage.Imapi.IMMPID_RPV_ENUM = 16385
IMMPID_RPV_AFTER__: win32more.Windows.Win32.Storage.Imapi.IMMPID_RPV_ENUM = 16386
IMMPID_RP_ENUM = Int32
IMMPID_RP_BEFORE__: win32more.Windows.Win32.Storage.Imapi.IMMPID_RP_ENUM = 8191
IMMPID_RP_DSN_NOTIFY_SUCCESS: win32more.Windows.Win32.Storage.Imapi.IMMPID_RP_ENUM = 8192
IMMPID_RP_DSN_NOTIFY_INVALID: win32more.Windows.Win32.Storage.Imapi.IMMPID_RP_ENUM = 8193
IMMPID_RP_ADDRESS_TYPE: win32more.Windows.Win32.Storage.Imapi.IMMPID_RP_ENUM = 8194
IMMPID_RP_ADDRESS: win32more.Windows.Win32.Storage.Imapi.IMMPID_RP_ENUM = 8195
IMMPID_RP_ADDRESS_TYPE_SMTP: win32more.Windows.Win32.Storage.Imapi.IMMPID_RP_ENUM = 8196
IMMPID_RP_ERROR_CODE: win32more.Windows.Win32.Storage.Imapi.IMMPID_RP_ENUM = 8197
IMMPID_RP_ERROR_STRING: win32more.Windows.Win32.Storage.Imapi.IMMPID_RP_ENUM = 8198
IMMPID_RP_DSN_NOTIFY_VALUE: win32more.Windows.Win32.Storage.Imapi.IMMPID_RP_ENUM = 8199
IMMPID_RP_DSN_ORCPT_VALUE: win32more.Windows.Win32.Storage.Imapi.IMMPID_RP_ENUM = 8200
IMMPID_RP_ADDRESS_SMTP: win32more.Windows.Win32.Storage.Imapi.IMMPID_RP_ENUM = 8201
IMMPID_RP_ADDRESS_X400: win32more.Windows.Win32.Storage.Imapi.IMMPID_RP_ENUM = 8202
IMMPID_RP_ADDRESS_X500: win32more.Windows.Win32.Storage.Imapi.IMMPID_RP_ENUM = 8203
IMMPID_RP_LEGACY_EX_DN: win32more.Windows.Win32.Storage.Imapi.IMMPID_RP_ENUM = 8204
IMMPID_RP_RECIPIENT_FLAGS: win32more.Windows.Win32.Storage.Imapi.IMMPID_RP_ENUM = 8205
IMMPID_RP_SMTP_STATUS_STRING: win32more.Windows.Win32.Storage.Imapi.IMMPID_RP_ENUM = 8206
IMMPID_RP_DSN_PRE_CAT_ADDRESS: win32more.Windows.Win32.Storage.Imapi.IMMPID_RP_ENUM = 8207
IMMPID_RP_MDB_GUID: win32more.Windows.Win32.Storage.Imapi.IMMPID_RP_ENUM = 8208
IMMPID_RP_USER_GUID: win32more.Windows.Win32.Storage.Imapi.IMMPID_RP_ENUM = 8209
IMMPID_RP_DOMAIN: win32more.Windows.Win32.Storage.Imapi.IMMPID_RP_ENUM = 8210
IMMPID_RP_ADDRESS_OTHER: win32more.Windows.Win32.Storage.Imapi.IMMPID_RP_ENUM = 8211
IMMPID_RP_DISPLAY_NAME: win32more.Windows.Win32.Storage.Imapi.IMMPID_RP_ENUM = 8212
IMMPID_RP_AFTER__: win32more.Windows.Win32.Storage.Imapi.IMMPID_RP_ENUM = 8213
class IMMP_MPV_STORE_DRIVER_HANDLE(Structure):
    guidSignature: Guid
class IMultisession(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{27354150-7f64-5b0f-8f00-5d77afbe261e}')
    @commethod(7)
    def get_IsSupportedOnCurrentMediaState(self, value: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_InUse(self, value: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_InUse(self, value: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_ImportRecorder(self, value: POINTER(win32more.Windows.Win32.Storage.Imapi.IDiscRecorder2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMultisessionRandomWrite(ComPtr):
    extends: win32more.Windows.Win32.Storage.Imapi.IMultisession
    _iid_ = Guid('{b507ca23-2204-11dd-966a-001aa01bbc58}')
    @commethod(11)
    def get_WriteUnitSize(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_LastWrittenAddress(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_TotalSectorsOnMedia(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMultisessionSequential(ComPtr):
    extends: win32more.Windows.Win32.Storage.Imapi.IMultisession
    _iid_ = Guid('{27354151-7f64-5b0f-8f00-5d77afbe261e}')
    @commethod(11)
    def get_IsFirstDataSession(self, value: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_StartAddressOfPreviousSession(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_LastWrittenAddressOfPreviousSession(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_NextWritableAddress(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_FreeSectorsOnMedia(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMultisessionSequential2(ComPtr):
    extends: win32more.Windows.Win32.Storage.Imapi.IMultisessionSequential
    _iid_ = Guid('{b507ca22-2204-11dd-966a-001aa01bbc58}')
    @commethod(16)
    def get_WriteUnitSize(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IProgressItem(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{2c941fd5-975b-59be-a960-9a2a262853a5}')
    @commethod(7)
    def get_Description(self, desc: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_FirstBlock(self, block: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_LastBlock(self, block: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_BlockCount(self, blocks: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IProgressItems(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{2c941fd7-975b-59be-a960-9a2a262853a5}')
    @commethod(7)
    def get__NewEnum(self, NewEnum: POINTER(win32more.Windows.Win32.System.Ole.IEnumVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, Index: Int32, item: POINTER(win32more.Windows.Win32.Storage.Imapi.IProgressItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(self, Count: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def ProgressItemFromBlock(self, block: UInt32, item: POINTER(win32more.Windows.Win32.Storage.Imapi.IProgressItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def ProgressItemFromDescription(self, description: win32more.Windows.Win32.Foundation.BSTR, item: POINTER(win32more.Windows.Win32.Storage.Imapi.IProgressItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_EnumProgressItems(self, NewEnum: POINTER(win32more.Windows.Win32.Storage.Imapi.IEnumProgressItems)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRawCDImageCreator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{25983550-9d65-49ce-b335-40630d901227}')
    @commethod(7)
    def CreateResultImage(self, resultStream: POINTER(win32more.Windows.Win32.System.Com.IStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def AddTrack(self, dataType: win32more.Windows.Win32.Storage.Imapi.IMAPI_CD_SECTOR_TYPE, data: win32more.Windows.Win32.System.Com.IStream, trackIndex: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AddSpecialPregap(self, data: win32more.Windows.Win32.System.Com.IStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def AddSubcodeRWGenerator(self, subcode: win32more.Windows.Win32.System.Com.IStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_ResultingImageType(self, value: win32more.Windows.Win32.Storage.Imapi.IMAPI_FORMAT2_RAW_CD_DATA_SECTOR_TYPE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_ResultingImageType(self, value: POINTER(win32more.Windows.Win32.Storage.Imapi.IMAPI_FORMAT2_RAW_CD_DATA_SECTOR_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_StartOfLeadout(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_StartOfLeadoutLimit(self, value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_StartOfLeadoutLimit(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_DisableGaplessAudio(self, value: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_DisableGaplessAudio(self, value: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_MediaCatalogNumber(self, value: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_MediaCatalogNumber(self, value: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_StartingTrackNumber(self, value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_StartingTrackNumber(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_TrackInfo(self, trackIndex: Int32, value: POINTER(win32more.Windows.Win32.Storage.Imapi.IRawCDImageTrackInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_NumberOfExistingTracks(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_LastUsedUserSectorInImage(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_ExpectedTableOfContents(self, value: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRawCDImageTrackInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{25983551-9d65-49ce-b335-40630d901227}')
    @commethod(7)
    def get_StartingLba(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_SectorCount(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_TrackNumber(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_SectorType(self, value: POINTER(win32more.Windows.Win32.Storage.Imapi.IMAPI_CD_SECTOR_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_ISRC(self, value: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_ISRC(self, value: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_DigitalAudioCopySetting(self, value: POINTER(win32more.Windows.Win32.Storage.Imapi.IMAPI_CD_TRACK_DIGITAL_COPY_SETTING)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_DigitalAudioCopySetting(self, value: win32more.Windows.Win32.Storage.Imapi.IMAPI_CD_TRACK_DIGITAL_COPY_SETTING) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_AudioHasPreemphasis(self, value: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_AudioHasPreemphasis(self, value: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_TrackIndexes(self, value: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def AddTrackIndex(self, lbaOffset: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def ClearTrackIndex(self, lbaOffset: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRedbookDiscMaster(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e3bc42cd-4e5c-11d3-9144-00104ba11c5e}')
    @commethod(3)
    def GetTotalAudioTracks(self, pnTracks: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetTotalAudioBlocks(self, pnBlocks: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetUsedAudioBlocks(self, pnBlocks: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetAvailableAudioTrackBlocks(self, pnBlocks: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetAudioBlockSize(self, pnBlockBytes: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CreateAudioTrack(self, nBlocks: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AddAudioTrackBlocks(self, pby: POINTER(Byte), cb: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CloseAudioTrack(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IStreamConcatenate(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IStream
    _iid_ = Guid('{27354146-7f64-5b0f-8f00-5d77afbe261e}')
    @commethod(14)
    def Initialize(self, stream1: win32more.Windows.Win32.System.Com.IStream, stream2: win32more.Windows.Win32.System.Com.IStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Initialize2(self, streams: POINTER(win32more.Windows.Win32.System.Com.IStream), streamCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Append(self, stream: win32more.Windows.Win32.System.Com.IStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def Append2(self, streams: POINTER(win32more.Windows.Win32.System.Com.IStream), streamCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IStreamInterleave(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IStream
    _iid_ = Guid('{27354147-7f64-5b0f-8f00-5d77afbe261e}')
    @commethod(14)
    def Initialize(self, streams: POINTER(win32more.Windows.Win32.System.Com.IStream), interleaveSizes: POINTER(UInt32), streamCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IStreamPseudoRandomBased(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IStream
    _iid_ = Guid('{27354145-7f64-5b0f-8f00-5d77afbe261e}')
    @commethod(14)
    def put_Seed(self, value: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Seed(self, value: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_ExtendedSeed(self, values: POINTER(UInt32), eCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_ExtendedSeed(self, values: POINTER(POINTER(UInt32)), eCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWriteEngine2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{27354135-7f64-5b0f-8f00-5d77afbe261e}')
    @commethod(7)
    def WriteSection(self, data: win32more.Windows.Win32.System.Com.IStream, startingBlockAddress: Int32, numberOfBlocks: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CancelWrite(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_Recorder(self, value: win32more.Windows.Win32.Storage.Imapi.IDiscRecorder2Ex) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Recorder(self, value: POINTER(win32more.Windows.Win32.Storage.Imapi.IDiscRecorder2Ex)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_UseStreamingWrite12(self, value: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_UseStreamingWrite12(self, value: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_StartingSectorsPerSecond(self, value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_StartingSectorsPerSecond(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_EndingSectorsPerSecond(self, value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_EndingSectorsPerSecond(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_BytesPerSector(self, value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_BytesPerSector(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_WriteInProgress(self, value: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWriteEngine2EventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{27354136-7f64-5b0f-8f00-5d77afbe261e}')
    @commethod(7)
    def get_StartLba(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_SectorCount(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_LastReadLba(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_LastWrittenLba(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_TotalSystemBuffer(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_UsedSystemBuffer(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_FreeSystemBuffer(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWriteSpeedDescriptor(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{27354144-7f64-5b0f-8f00-5d77afbe261e}')
    @commethod(7)
    def get_MediaType(self, value: POINTER(win32more.Windows.Win32.Storage.Imapi.IMAPI_MEDIA_PHYSICAL_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_RotationTypeIsPureCAV(self, value: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_WriteSpeed(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
LPMSGSESS = IntPtr
MEDIA_FLAGS = Int32
MEDIA_BLANK: win32more.Windows.Win32.Storage.Imapi.MEDIA_FLAGS = 1
MEDIA_RW: win32more.Windows.Win32.Storage.Imapi.MEDIA_FLAGS = 2
MEDIA_WRITABLE: win32more.Windows.Win32.Storage.Imapi.MEDIA_FLAGS = 4
MEDIA_FORMAT_UNUSABLE_BY_IMAPI: win32more.Windows.Win32.Storage.Imapi.MEDIA_FLAGS = 8
MEDIA_TYPES = Int32
MEDIA_CDDA_CDROM: win32more.Windows.Win32.Storage.Imapi.MEDIA_TYPES = 1
MEDIA_CD_ROM_XA: win32more.Windows.Win32.Storage.Imapi.MEDIA_TYPES = 2
MEDIA_CD_I: win32more.Windows.Win32.Storage.Imapi.MEDIA_TYPES = 3
MEDIA_CD_EXTRA: win32more.Windows.Win32.Storage.Imapi.MEDIA_TYPES = 4
MEDIA_CD_OTHER: win32more.Windows.Win32.Storage.Imapi.MEDIA_TYPES = 5
MEDIA_SPECIAL: win32more.Windows.Win32.Storage.Imapi.MEDIA_TYPES = 6
MSDiscMasterObj = Guid('{520cca63-51a5-11d3-9144-00104ba11c5e}')
MSDiscRecorderObj = Guid('{520cca61-51a5-11d3-9144-00104ba11c5e}')
MSEnumDiscRecordersObj = Guid('{8a03567a-63cb-4ba8-baf6-52119816d1ef}')
@winfunctype_pointer
def MSGCALLRELEASE(ulCallerData: UInt32, lpMessage: win32more.Windows.Win32.System.AddressBook.IMessage) -> Void: ...
MsftDiscFormat2Data = Guid('{2735412a-7f64-5b0f-8f00-5d77afbe261e}')
MsftDiscFormat2Erase = Guid('{2735412b-7f64-5b0f-8f00-5d77afbe261e}')
MsftDiscFormat2RawCD = Guid('{27354128-7f64-5b0f-8f00-5d77afbe261e}')
MsftDiscFormat2TrackAtOnce = Guid('{27354129-7f64-5b0f-8f00-5d77afbe261e}')
MsftDiscMaster2 = Guid('{2735412e-7f64-5b0f-8f00-5d77afbe261e}')
MsftDiscRecorder2 = Guid('{2735412d-7f64-5b0f-8f00-5d77afbe261e}')
MsftFileSystemImage = Guid('{2c941fc5-975b-59be-a960-9a2a262853a5}')
MsftIsoImageManager = Guid('{ceee3b62-8f56-4056-869b-ef16917e3efc}')
MsftMultisessionRandomWrite = Guid('{b507ca24-2204-11dd-966a-001aa01bbc58}')
MsftMultisessionSequential = Guid('{27354122-7f64-5b0f-8f00-5d77afbe261e}')
MsftRawCDImageCreator = Guid('{25983561-9d65-49ce-b335-40630d901227}')
MsftStreamConcatenate = Guid('{27354125-7f64-5b0f-8f00-5d77afbe261e}')
MsftStreamInterleave = Guid('{27354124-7f64-5b0f-8f00-5d77afbe261e}')
MsftStreamPrng001 = Guid('{27354126-7f64-5b0f-8f00-5d77afbe261e}')
MsftStreamZero = Guid('{27354127-7f64-5b0f-8f00-5d77afbe261e}')
MsftWriteEngine2 = Guid('{2735412c-7f64-5b0f-8f00-5d77afbe261e}')
MsftWriteSpeedDescriptor = Guid('{27354123-7f64-5b0f-8f00-5d77afbe261e}')
PlatformId = Int32
PlatformX86: win32more.Windows.Win32.Storage.Imapi.PlatformId = 0
PlatformPowerPC: win32more.Windows.Win32.Storage.Imapi.PlatformId = 1
PlatformMac: win32more.Windows.Win32.Storage.Imapi.PlatformId = 2
PlatformEFI: win32more.Windows.Win32.Storage.Imapi.PlatformId = 239
ProgressItem = Guid('{2c941fcb-975b-59be-a960-9a2a262853a5}')
ProgressItems = Guid('{2c941fc9-975b-59be-a960-9a2a262853a5}')
RECORDER_TYPES = Int32
RECORDER_CDR: win32more.Windows.Win32.Storage.Imapi.RECORDER_TYPES = 1
RECORDER_CDRW: win32more.Windows.Win32.Storage.Imapi.RECORDER_TYPES = 2
class SPropAttrArray(Structure):
    cValues: UInt32
    aPropAttr: UInt32 * 1
tagIMMPID_CPV_STRUCT = Guid('{a2a76b2a-e52d-11d1-aa64-00c04fa35b82}')
class tagIMMPID_GUIDLIST_ITEM(Structure):
    pguid: POINTER(Guid)
    dwStart: UInt32
    dwLast: UInt32
tagIMMPID_MPV_STRUCT = Guid('{cbe69706-c9bd-11d1-9ff2-00c04fa37348}')
tagIMMPID_MP_STRUCT = Guid('{13384cf0-b3c4-11d1-aa92-00aa006bc80b}')
tagIMMPID_NMP_STRUCT = Guid('{7433a9aa-20e2-11d2-94d6-00c04fa379f1}')
tagIMMPID_RPV_STRUCT = Guid('{79e82049-d320-11d1-9ff4-00c04fa37348}')
tagIMMPID_RP_STRUCT = Guid('{79e82048-d320-11d1-9ff4-00c04fa37348}')


make_ready(__name__)
