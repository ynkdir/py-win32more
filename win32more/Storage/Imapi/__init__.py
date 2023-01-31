from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Storage.Imapi
import win32more.System.AddressBook
import win32more.System.Com
import win32more.System.Com.StructuredStorage
import win32more.System.Ole
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
GUID_SMTP_SOURCE_TYPE: Guid = Guid('fb65c4dc-e468-11d1-aa-67-00-c0-4f-a3-45-f6')
GUID_SMTPSVC_SOURCE: Guid = Guid('1b3c0666-e470-11d1-aa-67-00-c0-4f-a3-45-f6')
CATID_SMTP_ON_INBOUND_COMMAND: Guid = Guid('f6628c8d-0d5e-11d2-aa-68-00-c0-4f-a3-5b-82')
CATID_SMTP_ON_SERVER_RESPONSE: Guid = Guid('f6628c8e-0d5e-11d2-aa-68-00-c0-4f-a3-5b-82')
CATID_SMTP_ON_SESSION_START: Guid = Guid('f6628c8f-0d5e-11d2-aa-68-00-c0-4f-a3-5b-82')
CATID_SMTP_ON_MESSAGE_START: Guid = Guid('f6628c90-0d5e-11d2-aa-68-00-c0-4f-a3-5b-82')
CATID_SMTP_ON_PER_RECIPIENT: Guid = Guid('f6628c91-0d5e-11d2-aa-68-00-c0-4f-a3-5b-82')
CATID_SMTP_ON_BEFORE_DATA: Guid = Guid('f6628c92-0d5e-11d2-aa-68-00-c0-4f-a3-5b-82')
CATID_SMTP_ON_SESSION_END: Guid = Guid('f6628c93-0d5e-11d2-aa-68-00-c0-4f-a3-5b-82')
CATID_SMTP_STORE_DRIVER: Guid = Guid('59175850-e533-11d1-aa-67-00-c0-4f-a3-45-f6')
CATID_SMTP_TRANSPORT_SUBMISSION: Guid = Guid('ff3caa23-00b9-11d2-9d-fb-00-c0-4f-a3-22-ba')
CATID_SMTP_TRANSPORT_PRECATEGORIZE: Guid = Guid('a3acfb0d-83ff-11d2-9e-14-00-c0-4f-a3-22-ba')
CATID_SMTP_TRANSPORT_CATEGORIZE: Guid = Guid('960252a3-0a3a-11d2-9e-00-00-c0-4f-a3-22-ba')
CATID_SMTP_TRANSPORT_POSTCATEGORIZE: Guid = Guid('76719654-05a6-11d2-9d-fd-00-c0-4f-a3-22-ba')
CATID_SMTP_TRANSPORT_ROUTER: Guid = Guid('283430c9-1850-11d2-9e-03-00-c0-4f-a3-22-ba')
CATID_SMTP_MSGTRACKLOG: Guid = Guid('c6df52aa-7db0-11d2-94-f4-00-c0-4f-79-f1-d6')
CATID_SMTP_DNSRESOLVERRECORDSINK: Guid = Guid('bd0b4366-8e03-11d2-94-f6-00-c0-4f-79-f1-d6')
CATID_SMTP_MAXMSGSIZE: Guid = Guid('ebf159de-a67e-11d2-94-f7-00-c0-4f-79-f1-d6')
CATID_SMTP_LOG: Guid = Guid('93d0a538-2c1e-4b68-a7-c9-d7-3a-8a-a6-ee-97')
CATID_SMTP_GET_AUX_DOMAIN_INFO_FLAGS: Guid = Guid('84ff368a-fab3-43d7-bc-df-69-2c-5b-46-e6-b1')
CLSID_SmtpCat: Guid = Guid('b23c35b7-9219-11d2-9e-17-00-c0-4f-a3-22-ba')
CATID_SMTP_DSN: Guid = Guid('22b55731-f5f8-4d23-bd-8f-87-b5-23-71-a7-3a')
SZ_PROGID_SMTPCAT: String = 'Smtp.Cat'
IMAPI_S_PROPERTIESIGNORED: win32more.Foundation.HRESULT = 262656
IMAPI_S_BUFFER_TO_SMALL: win32more.Foundation.HRESULT = 262657
IMAPI_E_NOTOPENED: win32more.Foundation.HRESULT = -2147220981
IMAPI_E_NOTINITIALIZED: win32more.Foundation.HRESULT = -2147220980
IMAPI_E_USERABORT: win32more.Foundation.HRESULT = -2147220979
IMAPI_E_GENERIC: win32more.Foundation.HRESULT = -2147220978
IMAPI_E_MEDIUM_NOTPRESENT: win32more.Foundation.HRESULT = -2147220977
IMAPI_E_MEDIUM_INVALIDTYPE: win32more.Foundation.HRESULT = -2147220976
IMAPI_E_DEVICE_NOPROPERTIES: win32more.Foundation.HRESULT = -2147220975
IMAPI_E_DEVICE_NOTACCESSIBLE: win32more.Foundation.HRESULT = -2147220974
IMAPI_E_DEVICE_NOTPRESENT: win32more.Foundation.HRESULT = -2147220973
IMAPI_E_DEVICE_INVALIDTYPE: win32more.Foundation.HRESULT = -2147220972
IMAPI_E_INITIALIZE_WRITE: win32more.Foundation.HRESULT = -2147220971
IMAPI_E_INITIALIZE_ENDWRITE: win32more.Foundation.HRESULT = -2147220970
IMAPI_E_FILESYSTEM: win32more.Foundation.HRESULT = -2147220969
IMAPI_E_FILEACCESS: win32more.Foundation.HRESULT = -2147220968
IMAPI_E_DISCINFO: win32more.Foundation.HRESULT = -2147220967
IMAPI_E_TRACKNOTOPEN: win32more.Foundation.HRESULT = -2147220966
IMAPI_E_TRACKOPEN: win32more.Foundation.HRESULT = -2147220965
IMAPI_E_DISCFULL: win32more.Foundation.HRESULT = -2147220964
IMAPI_E_BADJOLIETNAME: win32more.Foundation.HRESULT = -2147220963
IMAPI_E_INVALIDIMAGE: win32more.Foundation.HRESULT = -2147220962
IMAPI_E_NOACTIVEFORMAT: win32more.Foundation.HRESULT = -2147220961
IMAPI_E_NOACTIVERECORDER: win32more.Foundation.HRESULT = -2147220960
IMAPI_E_WRONGFORMAT: win32more.Foundation.HRESULT = -2147220959
IMAPI_E_ALREADYOPEN: win32more.Foundation.HRESULT = -2147220958
IMAPI_E_WRONGDISC: win32more.Foundation.HRESULT = -2147220957
IMAPI_E_FILEEXISTS: win32more.Foundation.HRESULT = -2147220956
IMAPI_E_STASHINUSE: win32more.Foundation.HRESULT = -2147220955
IMAPI_E_DEVICE_STILL_IN_USE: win32more.Foundation.HRESULT = -2147220954
IMAPI_E_LOSS_OF_STREAMING: win32more.Foundation.HRESULT = -2147220953
IMAPI_E_COMPRESSEDSTASH: win32more.Foundation.HRESULT = -2147220952
IMAPI_E_ENCRYPTEDSTASH: win32more.Foundation.HRESULT = -2147220951
IMAPI_E_NOTENOUGHDISKFORSTASH: win32more.Foundation.HRESULT = -2147220950
IMAPI_E_REMOVABLESTASH: win32more.Foundation.HRESULT = -2147220949
IMAPI_E_CANNOT_WRITE_TO_MEDIA: win32more.Foundation.HRESULT = -2147220948
IMAPI_E_TRACK_NOT_BIG_ENOUGH: win32more.Foundation.HRESULT = -2147220947
IMAPI_E_BOOTIMAGE_AND_NONBLANK_DISC: win32more.Foundation.HRESULT = -2147220946
@winfunctype('MAPI32.dll')
def OpenIMsgSession(lpMalloc: win32more.System.Com.IMalloc_head, ulFlags: UInt32, lppMsgSess: POINTER(POINTER(win32more.Storage.Imapi._MSGSESS_head))) -> Int32: ...
@winfunctype('MAPI32.dll')
def CloseIMsgSession(lpMsgSess: POINTER(win32more.Storage.Imapi._MSGSESS_head)) -> Void: ...
@winfunctype('MAPI32.dll')
def OpenIMsgOnIStg(lpMsgSess: POINTER(win32more.Storage.Imapi._MSGSESS_head), lpAllocateBuffer: win32more.System.AddressBook.LPALLOCATEBUFFER, lpAllocateMore: win32more.System.AddressBook.LPALLOCATEMORE, lpFreeBuffer: win32more.System.AddressBook.LPFREEBUFFER, lpMalloc: win32more.System.Com.IMalloc_head, lpMapiSup: c_void_p, lpStg: win32more.System.Com.StructuredStorage.IStorage_head, lpfMsgCallRelease: POINTER(win32more.Storage.Imapi.MSGCALLRELEASE), ulCallerData: UInt32, ulFlags: UInt32, lppMsg: POINTER(win32more.System.AddressBook.IMessage_head)) -> Int32: ...
@winfunctype('MAPI32.dll')
def GetAttribIMsgOnIStg(lpObject: c_void_p, lpPropTagArray: POINTER(win32more.System.AddressBook.SPropTagArray_head), lppPropAttrArray: POINTER(POINTER(win32more.Storage.Imapi.SPropAttrArray_head))) -> win32more.Foundation.HRESULT: ...
@winfunctype('MAPI32.dll')
def SetAttribIMsgOnIStg(lpObject: c_void_p, lpPropTags: POINTER(win32more.System.AddressBook.SPropTagArray_head), lpPropAttrs: POINTER(win32more.Storage.Imapi.SPropAttrArray_head), lppPropProblems: POINTER(POINTER(win32more.System.AddressBook.SPropProblemArray_head))) -> win32more.Foundation.HRESULT: ...
@winfunctype('MAPI32.dll')
def MapStorageSCode(StgSCode: Int32) -> Int32: ...
BlockRange = Guid('b507ca27-2204-11dd-96-6a-00-1a-a0-1b-bc-58')
BlockRangeList = Guid('b507ca28-2204-11dd-96-6a-00-1a-a0-1b-bc-58')
BootOptions = Guid('2c941fce-975b-59be-a9-60-9a-2a-26-28-53-a5')
class DDiscFormat2DataEvents(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('2735413c-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
    @commethod(7)
    def Update(object: win32more.System.Com.IDispatch_head, progress: win32more.System.Com.IDispatch_head) -> win32more.Foundation.HRESULT: ...
class DDiscFormat2EraseEvents(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('2735413a-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
    @commethod(7)
    def Update(object: win32more.System.Com.IDispatch_head, elapsedSeconds: Int32, estimatedTotalSeconds: Int32) -> win32more.Foundation.HRESULT: ...
class DDiscFormat2RawCDEvents(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('27354142-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
    @commethod(7)
    def Update(object: win32more.System.Com.IDispatch_head, progress: win32more.System.Com.IDispatch_head) -> win32more.Foundation.HRESULT: ...
class DDiscFormat2TrackAtOnceEvents(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('2735413f-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
    @commethod(7)
    def Update(object: win32more.System.Com.IDispatch_head, progress: win32more.System.Com.IDispatch_head) -> win32more.Foundation.HRESULT: ...
class DDiscMaster2Events(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('27354131-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
    @commethod(7)
    def NotifyDeviceAdded(object: win32more.System.Com.IDispatch_head, uniqueId: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def NotifyDeviceRemoved(object: win32more.System.Com.IDispatch_head, uniqueId: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class DFileSystemImageEvents(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('2c941fdf-975b-59be-a9-60-9a-2a-26-28-53-a5')
    @commethod(7)
    def Update(object: win32more.System.Com.IDispatch_head, currentFile: win32more.Foundation.BSTR, copiedSectors: Int32, totalSectors: Int32) -> win32more.Foundation.HRESULT: ...
class DFileSystemImageImportEvents(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('d25c30f9-4087-4366-9e-24-e5-5b-e2-86-42-4b')
    @commethod(7)
    def UpdateImport(object: win32more.System.Com.IDispatch_head, fileSystem: win32more.Storage.Imapi.FsiFileSystems, currentItem: win32more.Foundation.BSTR, importedDirectoryItems: Int32, totalDirectoryItems: Int32, importedFileItems: Int32, totalFileItems: Int32) -> win32more.Foundation.HRESULT: ...
DISC_RECORDER_STATE_FLAGS = UInt32
RECORDER_BURNING: DISC_RECORDER_STATE_FLAGS = 2
RECORDER_DOING_NOTHING: DISC_RECORDER_STATE_FLAGS = 0
RECORDER_OPENED: DISC_RECORDER_STATE_FLAGS = 1
class DWriteEngine2Events(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('27354137-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
    @commethod(7)
    def Update(object: win32more.System.Com.IDispatch_head, progress: win32more.System.Com.IDispatch_head) -> win32more.Foundation.HRESULT: ...
EmulationType = Int32
EmulationType_EmulationNone: EmulationType = 0
EmulationType_Emulation12MFloppy: EmulationType = 1
EmulationType_Emulation144MFloppy: EmulationType = 2
EmulationType_Emulation288MFloppy: EmulationType = 3
EmulationType_EmulationHardDisk: EmulationType = 4
EnumFsiItems = Guid('2c941fc6-975b-59be-a9-60-9a-2a-26-28-53-a5')
EnumProgressItems = Guid('2c941fca-975b-59be-a9-60-9a-2a-26-28-53-a5')
FileSystemImageResult = Guid('2c941fcc-975b-59be-a9-60-9a-2a-26-28-53-a5')
FsiDirectoryItem = Guid('2c941fc8-975b-59be-a9-60-9a-2a-26-28-53-a5')
FsiFileItem = Guid('2c941fc7-975b-59be-a9-60-9a-2a-26-28-53-a5')
FsiFileSystems = Int32
FsiFileSystems_FsiFileSystemNone: FsiFileSystems = 0
FsiFileSystems_FsiFileSystemISO9660: FsiFileSystems = 1
FsiFileSystems_FsiFileSystemJoliet: FsiFileSystems = 2
FsiFileSystems_FsiFileSystemUDF: FsiFileSystems = 4
FsiFileSystems_FsiFileSystemUnknown: FsiFileSystems = 1073741824
FsiItemType = Int32
FsiItemType_FsiItemNotFound: FsiItemType = 0
FsiItemType_FsiItemDirectory: FsiItemType = 1
FsiItemType_FsiItemFile: FsiItemType = 2
FsiNamedStreams = Guid('c6b6f8ed-6d19-44b4-b5-39-b1-59-b7-93-a3-2d')
FsiStream = Guid('2c941fcd-975b-59be-a9-60-9a-2a-26-28-53-a5')
class IBlockRange(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('b507ca25-2204-11dd-96-6a-00-1a-a0-1b-bc-58')
    @commethod(7)
    def get_StartLba(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_EndLba(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IBlockRangeList(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('b507ca26-2204-11dd-96-6a-00-1a-a0-1b-bc-58')
    @commethod(7)
    def get_BlockRanges(value: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
class IBootOptions(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('2c941fd4-975b-59be-a9-60-9a-2a-26-28-53-a5')
    @commethod(7)
    def get_BootImage(pVal: POINTER(win32more.System.Com.IStream_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Manufacturer(pVal: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def put_Manufacturer(newVal: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_PlatformId(pVal: POINTER(win32more.Storage.Imapi.PlatformId)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def put_PlatformId(newVal: win32more.Storage.Imapi.PlatformId) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_Emulation(pVal: POINTER(win32more.Storage.Imapi.EmulationType)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def put_Emulation(newVal: win32more.Storage.Imapi.EmulationType) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_ImageSize(pVal: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def AssignBootImage(newVal: win32more.System.Com.IStream_head) -> win32more.Foundation.HRESULT: ...
class IBurnVerification(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('d2ffd834-958b-426d-84-70-2a-13-87-9c-6a-91')
    @commethod(3)
    def put_BurnVerificationLevel(value: win32more.Storage.Imapi.IMAPI_BURN_VERIFICATION_LEVEL) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def get_BurnVerificationLevel(value: POINTER(win32more.Storage.Imapi.IMAPI_BURN_VERIFICATION_LEVEL)) -> win32more.Foundation.HRESULT: ...
class IDiscFormat2(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('27354152-8f64-5b0f-8f-00-5d-77-af-be-26-1e')
    @commethod(7)
    def IsRecorderSupported(recorder: win32more.Storage.Imapi.IDiscRecorder2_head, value: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def IsCurrentMediaSupported(recorder: win32more.Storage.Imapi.IDiscRecorder2_head, value: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_MediaPhysicallyBlank(value: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_MediaHeuristicallyBlank(value: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_SupportedMediaTypes(value: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
class IDiscFormat2Data(c_void_p):
    extends: win32more.Storage.Imapi.IDiscFormat2
    Guid = Guid('27354153-9f64-5b0f-8f-00-5d-77-af-be-26-1e')
    @commethod(12)
    def put_Recorder(value: win32more.Storage.Imapi.IDiscRecorder2_head) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_Recorder(value: POINTER(win32more.Storage.Imapi.IDiscRecorder2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def put_BufferUnderrunFreeDisabled(value: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_BufferUnderrunFreeDisabled(value: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def put_PostgapAlreadyInImage(value: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_PostgapAlreadyInImage(value: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def get_CurrentMediaStatus(value: POINTER(win32more.Storage.Imapi.IMAPI_FORMAT2_DATA_MEDIA_STATE)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_WriteProtectStatus(value: POINTER(win32more.Storage.Imapi.IMAPI_MEDIA_WRITE_PROTECT_STATE)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def get_TotalSectorsOnMedia(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def get_FreeSectorsOnMedia(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def get_NextWritableAddress(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def get_StartAddressOfPreviousSession(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def get_LastWrittenAddressOfPreviousSession(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def put_ForceMediaToBeClosed(value: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def get_ForceMediaToBeClosed(value: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def put_DisableConsumerDvdCompatibilityMode(value: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def get_DisableConsumerDvdCompatibilityMode(value: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def get_CurrentPhysicalMediaType(value: POINTER(win32more.Storage.Imapi.IMAPI_MEDIA_PHYSICAL_TYPE)) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def put_ClientName(value: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def get_ClientName(value: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def get_RequestedWriteSpeed(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def get_RequestedRotationTypeIsPureCAV(value: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def get_CurrentWriteSpeed(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def get_CurrentRotationTypeIsPureCAV(value: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def get_SupportedWriteSpeeds(supportedSpeeds: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def get_SupportedWriteSpeedDescriptors(supportedSpeedDescriptors: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def put_ForceOverwrite(value: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def get_ForceOverwrite(value: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def get_MultisessionInterfaces(value: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(41)
    def Write(data: win32more.System.Com.IStream_head) -> win32more.Foundation.HRESULT: ...
    @commethod(42)
    def CancelWrite() -> win32more.Foundation.HRESULT: ...
    @commethod(43)
    def SetWriteSpeed(RequestedSectorsPerSecond: Int32, RotationTypeIsPureCAV: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
class IDiscFormat2DataEventArgs(c_void_p):
    extends: win32more.Storage.Imapi.IWriteEngine2EventArgs
    Guid = Guid('2735413d-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
    @commethod(14)
    def get_ElapsedTime(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_RemainingTime(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_TotalTime(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_CurrentAction(value: POINTER(win32more.Storage.Imapi.IMAPI_FORMAT2_DATA_WRITE_ACTION)) -> win32more.Foundation.HRESULT: ...
class IDiscFormat2Erase(c_void_p):
    extends: win32more.Storage.Imapi.IDiscFormat2
    Guid = Guid('27354156-8f64-5b0f-8f-00-5d-77-af-be-26-1e')
    @commethod(12)
    def put_Recorder(value: win32more.Storage.Imapi.IDiscRecorder2_head) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_Recorder(value: POINTER(win32more.Storage.Imapi.IDiscRecorder2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def put_FullErase(value: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_FullErase(value: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_CurrentPhysicalMediaType(value: POINTER(win32more.Storage.Imapi.IMAPI_MEDIA_PHYSICAL_TYPE)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def put_ClientName(value: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def get_ClientName(value: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def EraseMedia() -> win32more.Foundation.HRESULT: ...
class IDiscFormat2RawCD(c_void_p):
    extends: win32more.Storage.Imapi.IDiscFormat2
    Guid = Guid('27354155-8f64-5b0f-8f-00-5d-77-af-be-26-1e')
    @commethod(12)
    def PrepareMedia() -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def WriteMedia(data: win32more.System.Com.IStream_head) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def WriteMedia2(data: win32more.System.Com.IStream_head, streamLeadInSectors: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def CancelWrite() -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def ReleaseMedia() -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def SetWriteSpeed(RequestedSectorsPerSecond: Int32, RotationTypeIsPureCAV: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def put_Recorder(value: win32more.Storage.Imapi.IDiscRecorder2_head) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_Recorder(value: POINTER(win32more.Storage.Imapi.IDiscRecorder2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def put_BufferUnderrunFreeDisabled(value: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def get_BufferUnderrunFreeDisabled(value: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def get_StartOfNextSession(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def get_LastPossibleStartOfLeadout(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def get_CurrentPhysicalMediaType(value: POINTER(win32more.Storage.Imapi.IMAPI_MEDIA_PHYSICAL_TYPE)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def get_SupportedSectorTypes(value: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def put_RequestedSectorType(value: win32more.Storage.Imapi.IMAPI_FORMAT2_RAW_CD_DATA_SECTOR_TYPE) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def get_RequestedSectorType(value: POINTER(win32more.Storage.Imapi.IMAPI_FORMAT2_RAW_CD_DATA_SECTOR_TYPE)) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def put_ClientName(value: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def get_ClientName(value: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def get_RequestedWriteSpeed(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def get_RequestedRotationTypeIsPureCAV(value: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def get_CurrentWriteSpeed(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def get_CurrentRotationTypeIsPureCAV(value: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def get_SupportedWriteSpeeds(supportedSpeeds: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def get_SupportedWriteSpeedDescriptors(supportedSpeedDescriptors: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
class IDiscFormat2RawCDEventArgs(c_void_p):
    extends: win32more.Storage.Imapi.IWriteEngine2EventArgs
    Guid = Guid('27354143-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
    @commethod(14)
    def get_CurrentAction(value: POINTER(win32more.Storage.Imapi.IMAPI_FORMAT2_RAW_CD_WRITE_ACTION)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_ElapsedTime(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_RemainingTime(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IDiscFormat2TrackAtOnce(c_void_p):
    extends: win32more.Storage.Imapi.IDiscFormat2
    Guid = Guid('27354154-8f64-5b0f-8f-00-5d-77-af-be-26-1e')
    @commethod(12)
    def PrepareMedia() -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def AddAudioTrack(data: win32more.System.Com.IStream_head) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def CancelAddTrack() -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def ReleaseMedia() -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def SetWriteSpeed(RequestedSectorsPerSecond: Int32, RotationTypeIsPureCAV: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def put_Recorder(value: win32more.Storage.Imapi.IDiscRecorder2_head) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def get_Recorder(value: POINTER(win32more.Storage.Imapi.IDiscRecorder2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def put_BufferUnderrunFreeDisabled(value: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def get_BufferUnderrunFreeDisabled(value: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def get_NumberOfExistingTracks(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def get_TotalSectorsOnMedia(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def get_FreeSectorsOnMedia(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def get_UsedSectorsOnMedia(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def put_DoNotFinalizeMedia(value: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def get_DoNotFinalizeMedia(value: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def get_ExpectedTableOfContents(value: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def get_CurrentPhysicalMediaType(value: POINTER(win32more.Storage.Imapi.IMAPI_MEDIA_PHYSICAL_TYPE)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def put_ClientName(value: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def get_ClientName(value: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def get_RequestedWriteSpeed(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def get_RequestedRotationTypeIsPureCAV(value: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def get_CurrentWriteSpeed(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def get_CurrentRotationTypeIsPureCAV(value: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def get_SupportedWriteSpeeds(supportedSpeeds: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def get_SupportedWriteSpeedDescriptors(supportedSpeedDescriptors: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
class IDiscFormat2TrackAtOnceEventArgs(c_void_p):
    extends: win32more.Storage.Imapi.IWriteEngine2EventArgs
    Guid = Guid('27354140-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
    @commethod(14)
    def get_CurrentTrackNumber(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_CurrentAction(value: POINTER(win32more.Storage.Imapi.IMAPI_FORMAT2_TAO_WRITE_ACTION)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_ElapsedTime(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_RemainingTime(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IDiscMaster(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('520cca62-51a5-11d3-91-44-00-10-4b-a1-1c-5e')
    @commethod(3)
    def Open() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def EnumDiscMasterFormats(ppEnum: POINTER(win32more.Storage.Imapi.IEnumDiscMasterFormats_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetActiveDiscMasterFormat(lpiid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetActiveDiscMasterFormat(riid: POINTER(Guid), ppUnk: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def EnumDiscRecorders(ppEnum: POINTER(win32more.Storage.Imapi.IEnumDiscRecorders_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetActiveDiscRecorder(ppRecorder: POINTER(win32more.Storage.Imapi.IDiscRecorder_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetActiveDiscRecorder(pRecorder: win32more.Storage.Imapi.IDiscRecorder_head) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def ClearFormatContent() -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def ProgressAdvise(pEvents: win32more.Storage.Imapi.IDiscMasterProgressEvents_head, pvCookie: POINTER(UIntPtr)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def ProgressUnadvise(vCookie: UIntPtr) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def RecordDisc(bSimulate: Byte, bEjectAfterBurn: Byte) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def Close() -> win32more.Foundation.HRESULT: ...
class IDiscMaster2(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('27354130-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
    @commethod(7)
    def get__NewEnum(ppunk: POINTER(win32more.System.Ole.IEnumVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(index: Int32, value: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_IsSupportedEnvironment(value: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
class IDiscMasterProgressEvents(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ec9e51c1-4e5d-11d3-91-44-00-10-4b-a1-1c-5e')
    @commethod(3)
    def QueryCancel(pbCancel: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def NotifyPnPActivity() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def NotifyAddProgress(nCompletedSteps: Int32, nTotalSteps: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def NotifyBlockProgress(nCompleted: Int32, nTotal: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def NotifyTrackProgress(nCurrentTrack: Int32, nTotalTracks: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def NotifyPreparingBurn(nEstimatedSeconds: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def NotifyClosingDisc(nEstimatedSeconds: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def NotifyBurnComplete(status: win32more.Foundation.HRESULT) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def NotifyEraseComplete(status: win32more.Foundation.HRESULT) -> win32more.Foundation.HRESULT: ...
class IDiscRecorder(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('85ac9776-ca88-4cf2-89-4e-09-59-8c-07-8a-41')
    @commethod(3)
    def Init(pbyUniqueID: c_char_p_no, nulIDSize: UInt32, nulDriveNumber: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetRecorderGUID(pbyUniqueID: c_char_p_no, ulBufferSize: UInt32, pulReturnSizeRequired: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetRecorderType(fTypeCode: POINTER(win32more.Storage.Imapi.RECORDER_TYPES)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetDisplayNames(pbstrVendorID: POINTER(win32more.Foundation.BSTR), pbstrProductID: POINTER(win32more.Foundation.BSTR), pbstrRevision: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetBasePnPID(pbstrBasePnPID: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetPath(pbstrPath: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetRecorderProperties(ppPropStg: POINTER(win32more.System.Com.StructuredStorage.IPropertyStorage_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetRecorderProperties(pPropStg: win32more.System.Com.StructuredStorage.IPropertyStorage_head) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetRecorderState(pulDevStateFlags: POINTER(win32more.Storage.Imapi.DISC_RECORDER_STATE_FLAGS)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def OpenExclusive() -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def QueryMediaType(fMediaType: POINTER(win32more.Storage.Imapi.MEDIA_TYPES), fMediaFlags: POINTER(win32more.Storage.Imapi.MEDIA_FLAGS)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def QueryMediaInfo(pbSessions: c_char_p_no, pbLastTrack: c_char_p_no, ulStartAddress: POINTER(UInt32), ulNextWritable: POINTER(UInt32), ulFreeBlocks: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def Eject() -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def Erase(bFullErase: Byte) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def Close() -> win32more.Foundation.HRESULT: ...
class IDiscRecorder2(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('27354133-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
    @commethod(7)
    def EjectMedia() -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def CloseTray() -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def AcquireExclusiveAccess(force: win32more.Foundation.VARIANT_BOOL, __MIDL__IDiscRecorder20000: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def ReleaseExclusiveAccess() -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def DisableMcn() -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def EnableMcn() -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def InitializeDiscRecorder(recorderUniqueId: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_ActiveDiscRecorder(value: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_VendorId(value: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_ProductId(value: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_ProductRevision(value: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def get_VolumeName(value: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_VolumePathNames(value: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def get_DeviceCanLoadMedia(value: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def get_LegacyDeviceNumber(legacyDeviceNumber: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def get_SupportedFeaturePages(value: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def get_CurrentFeaturePages(value: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def get_SupportedProfiles(value: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def get_CurrentProfiles(value: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def get_SupportedModePages(value: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def get_ExclusiveAccessOwner(value: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IDiscRecorder2Ex(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('27354132-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
    @commethod(3)
    def SendCommandNoData(Cdb: c_char_p_no, CdbSize: UInt32, SenseBuffer: c_char_p_no, Timeout: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SendCommandSendDataToDevice(Cdb: c_char_p_no, CdbSize: UInt32, SenseBuffer: c_char_p_no, Timeout: UInt32, Buffer: c_char_p_no, BufferSize: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SendCommandGetDataFromDevice(Cdb: c_char_p_no, CdbSize: UInt32, SenseBuffer: c_char_p_no, Timeout: UInt32, Buffer: c_char_p_no, BufferSize: UInt32, BufferFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def ReadDvdStructure(format: UInt32, address: UInt32, layer: UInt32, agid: UInt32, data: POINTER(c_char_p_no), count: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SendDvdStructure(format: UInt32, data: c_char_p_no, count: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetAdapterDescriptor(data: POINTER(c_char_p_no), byteSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetDeviceDescriptor(data: POINTER(c_char_p_no), byteSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetDiscInformation(discInformation: POINTER(c_char_p_no), byteSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetTrackInformation(address: UInt32, addressType: win32more.Storage.Imapi.IMAPI_READ_TRACK_ADDRESS_TYPE, trackInformation: POINTER(c_char_p_no), byteSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetFeaturePage(requestedFeature: win32more.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE, currentFeatureOnly: win32more.Foundation.BOOLEAN, featureData: POINTER(c_char_p_no), byteSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetModePage(requestedModePage: win32more.Storage.Imapi.IMAPI_MODE_PAGE_TYPE, requestType: win32more.Storage.Imapi.IMAPI_MODE_PAGE_REQUEST_TYPE, modePageData: POINTER(c_char_p_no), byteSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def SetModePage(requestType: win32more.Storage.Imapi.IMAPI_MODE_PAGE_REQUEST_TYPE, data: c_char_p_no, byteSize: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetSupportedFeaturePages(currentFeatureOnly: win32more.Foundation.BOOLEAN, featureData: POINTER(POINTER(win32more.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE)), byteSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def GetSupportedProfiles(currentOnly: win32more.Foundation.BOOLEAN, profileTypes: POINTER(POINTER(win32more.Storage.Imapi.IMAPI_PROFILE_TYPE)), validProfiles: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def GetSupportedModePages(requestType: win32more.Storage.Imapi.IMAPI_MODE_PAGE_REQUEST_TYPE, modePageTypes: POINTER(POINTER(win32more.Storage.Imapi.IMAPI_MODE_PAGE_TYPE)), validPages: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def GetByteAlignmentMask(value: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def GetMaximumNonPageAlignedTransferSize(value: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def GetMaximumPageAlignedTransferSize(value: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IEnumDiscMasterFormats(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ddf445e1-54ba-11d3-91-44-00-10-4b-a1-1c-5e')
    @commethod(3)
    def Next(cFormats: UInt32, lpiidFormatID: POINTER(Guid), pcFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(cFormats: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppEnum: POINTER(win32more.Storage.Imapi.IEnumDiscMasterFormats_head)) -> win32more.Foundation.HRESULT: ...
class IEnumDiscRecorders(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('9b1921e1-54ac-11d3-91-44-00-10-4b-a1-1c-5e')
    @commethod(3)
    def Next(cRecorders: UInt32, ppRecorder: POINTER(win32more.Storage.Imapi.IDiscRecorder_head), pcFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(cRecorders: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppEnum: POINTER(win32more.Storage.Imapi.IEnumDiscRecorders_head)) -> win32more.Foundation.HRESULT: ...
class IEnumFsiItems(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('2c941fda-975b-59be-a9-60-9a-2a-26-28-53-a5')
    @commethod(3)
    def Next(celt: UInt32, rgelt: POINTER(win32more.Storage.Imapi.IFsiItem_head), pceltFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppEnum: POINTER(win32more.Storage.Imapi.IEnumFsiItems_head)) -> win32more.Foundation.HRESULT: ...
class IEnumProgressItems(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('2c941fd6-975b-59be-a9-60-9a-2a-26-28-53-a5')
    @commethod(3)
    def Next(celt: UInt32, rgelt: POINTER(win32more.Storage.Imapi.IProgressItem_head), pceltFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppEnum: POINTER(win32more.Storage.Imapi.IEnumProgressItems_head)) -> win32more.Foundation.HRESULT: ...
class IFileSystemImage(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('2c941fe1-975b-59be-a9-60-9a-2a-26-28-53-a5')
    @commethod(7)
    def get_Root(pVal: POINTER(win32more.Storage.Imapi.IFsiDirectoryItem_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_SessionStartBlock(pVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def put_SessionStartBlock(newVal: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_FreeMediaBlocks(pVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def put_FreeMediaBlocks(newVal: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def SetMaxMediaBlocksFromDevice(discRecorder: win32more.Storage.Imapi.IDiscRecorder2_head) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_UsedBlocks(pVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_VolumeName(pVal: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def put_VolumeName(newVal: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_ImportedVolumeName(pVal: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_BootImageOptions(pVal: POINTER(win32more.Storage.Imapi.IBootOptions_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def put_BootImageOptions(newVal: win32more.Storage.Imapi.IBootOptions_head) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_FileCount(pVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def get_DirectoryCount(pVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def get_WorkingDirectory(pVal: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def put_WorkingDirectory(newVal: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def get_ChangePoint(pVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def get_StrictFileSystemCompliance(pVal: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def put_StrictFileSystemCompliance(newVal: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def get_UseRestrictedCharacterSet(pVal: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def put_UseRestrictedCharacterSet(newVal: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def get_FileSystemsToCreate(pVal: POINTER(win32more.Storage.Imapi.FsiFileSystems)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def put_FileSystemsToCreate(newVal: win32more.Storage.Imapi.FsiFileSystems) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def get_FileSystemsSupported(pVal: POINTER(win32more.Storage.Imapi.FsiFileSystems)) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def put_UDFRevision(newVal: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def get_UDFRevision(pVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def get_UDFRevisionsSupported(pVal: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def ChooseImageDefaults(discRecorder: win32more.Storage.Imapi.IDiscRecorder2_head) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def ChooseImageDefaultsForMediaType(value: win32more.Storage.Imapi.IMAPI_MEDIA_PHYSICAL_TYPE) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def put_ISO9660InterchangeLevel(newVal: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def get_ISO9660InterchangeLevel(pVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def get_ISO9660InterchangeLevelsSupported(pVal: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def CreateResultImage(resultStream: POINTER(win32more.Storage.Imapi.IFileSystemImageResult_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def Exists(fullPath: win32more.Foundation.BSTR, itemType: POINTER(win32more.Storage.Imapi.FsiItemType)) -> win32more.Foundation.HRESULT: ...
    @commethod(41)
    def CalculateDiscIdentifier(discIdentifier: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(42)
    def IdentifyFileSystemsOnDisc(discRecorder: win32more.Storage.Imapi.IDiscRecorder2_head, fileSystems: POINTER(win32more.Storage.Imapi.FsiFileSystems)) -> win32more.Foundation.HRESULT: ...
    @commethod(43)
    def GetDefaultFileSystemForImport(fileSystems: win32more.Storage.Imapi.FsiFileSystems, importDefault: POINTER(win32more.Storage.Imapi.FsiFileSystems)) -> win32more.Foundation.HRESULT: ...
    @commethod(44)
    def ImportFileSystem(importedFileSystem: POINTER(win32more.Storage.Imapi.FsiFileSystems)) -> win32more.Foundation.HRESULT: ...
    @commethod(45)
    def ImportSpecificFileSystem(fileSystemToUse: win32more.Storage.Imapi.FsiFileSystems) -> win32more.Foundation.HRESULT: ...
    @commethod(46)
    def RollbackToChangePoint(changePoint: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(47)
    def LockInChangePoint() -> win32more.Foundation.HRESULT: ...
    @commethod(48)
    def CreateDirectoryItem(name: win32more.Foundation.BSTR, newItem: POINTER(win32more.Storage.Imapi.IFsiDirectoryItem_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(49)
    def CreateFileItem(name: win32more.Foundation.BSTR, newItem: POINTER(win32more.Storage.Imapi.IFsiFileItem_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(50)
    def get_VolumeNameUDF(pVal: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(51)
    def get_VolumeNameJoliet(pVal: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(52)
    def get_VolumeNameISO9660(pVal: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(53)
    def get_StageFiles(pVal: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(54)
    def put_StageFiles(newVal: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(55)
    def get_MultisessionInterfaces(pVal: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(56)
    def put_MultisessionInterfaces(newVal: POINTER(win32more.System.Com.SAFEARRAY_head)) -> win32more.Foundation.HRESULT: ...
class IFileSystemImage2(c_void_p):
    extends: win32more.Storage.Imapi.IFileSystemImage
    Guid = Guid('d7644b2c-1537-4767-b6-2f-f1-38-7b-02-dd-fd')
    @commethod(57)
    def get_BootImageOptionsArray(pVal: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(58)
    def put_BootImageOptionsArray(newVal: POINTER(win32more.System.Com.SAFEARRAY_head)) -> win32more.Foundation.HRESULT: ...
class IFileSystemImage3(c_void_p):
    extends: win32more.Storage.Imapi.IFileSystemImage2
    Guid = Guid('7cff842c-7e97-4807-83-04-91-0d-d8-f7-c0-51')
    @commethod(59)
    def get_CreateRedundantUdfMetadataFiles(pVal: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(60)
    def put_CreateRedundantUdfMetadataFiles(newVal: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(61)
    def ProbeSpecificFileSystem(fileSystemToProbe: win32more.Storage.Imapi.FsiFileSystems, isAppendable: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
class IFileSystemImageResult(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('2c941fd8-975b-59be-a9-60-9a-2a-26-28-53-a5')
    @commethod(7)
    def get_ImageStream(pVal: POINTER(win32more.System.Com.IStream_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_ProgressItems(pVal: POINTER(win32more.Storage.Imapi.IProgressItems_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_TotalBlocks(pVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_BlockSize(pVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_DiscId(pVal: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IFileSystemImageResult2(c_void_p):
    extends: win32more.Storage.Imapi.IFileSystemImageResult
    Guid = Guid('b507ca29-2204-11dd-96-6a-00-1a-a0-1b-bc-58')
    @commethod(12)
    def get_ModifiedBlocks(pVal: POINTER(win32more.Storage.Imapi.IBlockRangeList_head)) -> win32more.Foundation.HRESULT: ...
class IFsiDirectoryItem(c_void_p):
    extends: win32more.Storage.Imapi.IFsiItem
    Guid = Guid('2c941fdc-975b-59be-a9-60-9a-2a-26-28-53-a5')
    @commethod(19)
    def get__NewEnum(NewEnum: POINTER(win32more.System.Ole.IEnumVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def get_Item(path: win32more.Foundation.BSTR, item: POINTER(win32more.Storage.Imapi.IFsiItem_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def get_Count(Count: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def get_EnumFsiItems(NewEnum: POINTER(win32more.Storage.Imapi.IEnumFsiItems_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def AddDirectory(path: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def AddFile(path: win32more.Foundation.BSTR, fileData: win32more.System.Com.IStream_head) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def AddTree(sourceDirectory: win32more.Foundation.BSTR, includeBaseDirectory: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def Add(item: win32more.Storage.Imapi.IFsiItem_head) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def Remove(path: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def RemoveTree(path: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class IFsiDirectoryItem2(c_void_p):
    extends: win32more.Storage.Imapi.IFsiDirectoryItem
    Guid = Guid('f7fb4b9b-6d96-4d7b-91-15-20-1b-14-48-11-ef')
    @commethod(29)
    def AddTreeWithNamedStreams(sourceDirectory: win32more.Foundation.BSTR, includeBaseDirectory: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
class IFsiFileItem(c_void_p):
    extends: win32more.Storage.Imapi.IFsiItem
    Guid = Guid('2c941fdb-975b-59be-a9-60-9a-2a-26-28-53-a5')
    @commethod(19)
    def get_DataSize(pVal: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def get_DataSize32BitLow(pVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def get_DataSize32BitHigh(pVal: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def get_Data(pVal: POINTER(win32more.System.Com.IStream_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def put_Data(newVal: win32more.System.Com.IStream_head) -> win32more.Foundation.HRESULT: ...
class IFsiFileItem2(c_void_p):
    extends: win32more.Storage.Imapi.IFsiFileItem
    Guid = Guid('199d0c19-11e1-40eb-8e-c2-c8-c8-22-a0-77-92')
    @commethod(24)
    def get_FsiNamedStreams(streams: POINTER(win32more.Storage.Imapi.IFsiNamedStreams_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def get_IsNamedStream(pVal: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def AddStream(name: win32more.Foundation.BSTR, streamData: win32more.System.Com.IStream_head) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def RemoveStream(name: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def get_IsRealTime(pVal: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def put_IsRealTime(newVal: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
class IFsiItem(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('2c941fd9-975b-59be-a9-60-9a-2a-26-28-53-a5')
    @commethod(7)
    def get_Name(pVal: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_FullPath(pVal: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_CreationTime(pVal: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_CreationTime(newVal: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_LastAccessedTime(pVal: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def put_LastAccessedTime(newVal: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_LastModifiedTime(pVal: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def put_LastModifiedTime(newVal: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_IsHidden(pVal: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def put_IsHidden(newVal: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def FileSystemName(fileSystem: win32more.Storage.Imapi.FsiFileSystems, pVal: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def FileSystemPath(fileSystem: win32more.Storage.Imapi.FsiFileSystems, pVal: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IFsiNamedStreams(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('ed79ba56-5294-4250-8d-46-f9-ae-ce-e2-34-59')
    @commethod(7)
    def get__NewEnum(NewEnum: POINTER(win32more.System.Ole.IEnumVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(index: Int32, item: POINTER(win32more.Storage.Imapi.IFsiFileItem2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(count: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_EnumNamedStreams(NewEnum: POINTER(win32more.Storage.Imapi.IEnumFsiItems_head)) -> win32more.Foundation.HRESULT: ...
class IIsoImageManager(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('6ca38be5-fbbb-4800-95-a1-a4-38-86-5e-b0-d4')
    @commethod(7)
    def get_Path(pVal: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Stream(data: POINTER(win32more.System.Com.IStream_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetPath(Val: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetStream(data: win32more.System.Com.IStream_head) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Validate() -> win32more.Foundation.HRESULT: ...
class IJolietDiscMaster(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('e3bc42ce-4e5c-11d3-91-44-00-10-4b-a1-1c-5e')
    @commethod(3)
    def GetTotalDataBlocks(pnBlocks: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetUsedDataBlocks(pnBlocks: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetDataBlockSize(pnBlockBytes: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def AddData(pStorage: win32more.System.Com.StructuredStorage.IStorage_head, lFileOverwrite: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetJolietProperties(ppPropStg: POINTER(win32more.System.Com.StructuredStorage.IPropertyStorage_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetJolietProperties(pPropStg: win32more.System.Com.StructuredStorage.IPropertyStorage_head) -> win32more.Foundation.HRESULT: ...
IMAPI_BURN_VERIFICATION_LEVEL = Int32
IMAPI_BURN_VERIFICATION_NONE: IMAPI_BURN_VERIFICATION_LEVEL = 0
IMAPI_BURN_VERIFICATION_QUICK: IMAPI_BURN_VERIFICATION_LEVEL = 1
IMAPI_BURN_VERIFICATION_FULL: IMAPI_BURN_VERIFICATION_LEVEL = 2
IMAPI_CD_SECTOR_TYPE = Int32
IMAPI_CD_SECTOR_AUDIO: IMAPI_CD_SECTOR_TYPE = 0
IMAPI_CD_SECTOR_MODE_ZERO: IMAPI_CD_SECTOR_TYPE = 1
IMAPI_CD_SECTOR_MODE1: IMAPI_CD_SECTOR_TYPE = 2
IMAPI_CD_SECTOR_MODE2FORM0: IMAPI_CD_SECTOR_TYPE = 3
IMAPI_CD_SECTOR_MODE2FORM1: IMAPI_CD_SECTOR_TYPE = 4
IMAPI_CD_SECTOR_MODE2FORM2: IMAPI_CD_SECTOR_TYPE = 5
IMAPI_CD_SECTOR_MODE1RAW: IMAPI_CD_SECTOR_TYPE = 6
IMAPI_CD_SECTOR_MODE2FORM0RAW: IMAPI_CD_SECTOR_TYPE = 7
IMAPI_CD_SECTOR_MODE2FORM1RAW: IMAPI_CD_SECTOR_TYPE = 8
IMAPI_CD_SECTOR_MODE2FORM2RAW: IMAPI_CD_SECTOR_TYPE = 9
IMAPI_CD_TRACK_DIGITAL_COPY_SETTING = Int32
IMAPI_CD_TRACK_DIGITAL_COPY_PERMITTED: IMAPI_CD_TRACK_DIGITAL_COPY_SETTING = 0
IMAPI_CD_TRACK_DIGITAL_COPY_PROHIBITED: IMAPI_CD_TRACK_DIGITAL_COPY_SETTING = 1
IMAPI_CD_TRACK_DIGITAL_COPY_SCMS: IMAPI_CD_TRACK_DIGITAL_COPY_SETTING = 2
IMAPI_FEATURE_PAGE_TYPE = Int32
IMAPI_FEATURE_PAGE_TYPE_PROFILE_LIST: IMAPI_FEATURE_PAGE_TYPE = 0
IMAPI_FEATURE_PAGE_TYPE_CORE: IMAPI_FEATURE_PAGE_TYPE = 1
IMAPI_FEATURE_PAGE_TYPE_MORPHING: IMAPI_FEATURE_PAGE_TYPE = 2
IMAPI_FEATURE_PAGE_TYPE_REMOVABLE_MEDIUM: IMAPI_FEATURE_PAGE_TYPE = 3
IMAPI_FEATURE_PAGE_TYPE_WRITE_PROTECT: IMAPI_FEATURE_PAGE_TYPE = 4
IMAPI_FEATURE_PAGE_TYPE_RANDOMLY_READABLE: IMAPI_FEATURE_PAGE_TYPE = 16
IMAPI_FEATURE_PAGE_TYPE_CD_MULTIREAD: IMAPI_FEATURE_PAGE_TYPE = 29
IMAPI_FEATURE_PAGE_TYPE_CD_READ: IMAPI_FEATURE_PAGE_TYPE = 30
IMAPI_FEATURE_PAGE_TYPE_DVD_READ: IMAPI_FEATURE_PAGE_TYPE = 31
IMAPI_FEATURE_PAGE_TYPE_RANDOMLY_WRITABLE: IMAPI_FEATURE_PAGE_TYPE = 32
IMAPI_FEATURE_PAGE_TYPE_INCREMENTAL_STREAMING_WRITABLE: IMAPI_FEATURE_PAGE_TYPE = 33
IMAPI_FEATURE_PAGE_TYPE_SECTOR_ERASABLE: IMAPI_FEATURE_PAGE_TYPE = 34
IMAPI_FEATURE_PAGE_TYPE_FORMATTABLE: IMAPI_FEATURE_PAGE_TYPE = 35
IMAPI_FEATURE_PAGE_TYPE_HARDWARE_DEFECT_MANAGEMENT: IMAPI_FEATURE_PAGE_TYPE = 36
IMAPI_FEATURE_PAGE_TYPE_WRITE_ONCE: IMAPI_FEATURE_PAGE_TYPE = 37
IMAPI_FEATURE_PAGE_TYPE_RESTRICTED_OVERWRITE: IMAPI_FEATURE_PAGE_TYPE = 38
IMAPI_FEATURE_PAGE_TYPE_CDRW_CAV_WRITE: IMAPI_FEATURE_PAGE_TYPE = 39
IMAPI_FEATURE_PAGE_TYPE_MRW: IMAPI_FEATURE_PAGE_TYPE = 40
IMAPI_FEATURE_PAGE_TYPE_ENHANCED_DEFECT_REPORTING: IMAPI_FEATURE_PAGE_TYPE = 41
IMAPI_FEATURE_PAGE_TYPE_DVD_PLUS_RW: IMAPI_FEATURE_PAGE_TYPE = 42
IMAPI_FEATURE_PAGE_TYPE_DVD_PLUS_R: IMAPI_FEATURE_PAGE_TYPE = 43
IMAPI_FEATURE_PAGE_TYPE_RIGID_RESTRICTED_OVERWRITE: IMAPI_FEATURE_PAGE_TYPE = 44
IMAPI_FEATURE_PAGE_TYPE_CD_TRACK_AT_ONCE: IMAPI_FEATURE_PAGE_TYPE = 45
IMAPI_FEATURE_PAGE_TYPE_CD_MASTERING: IMAPI_FEATURE_PAGE_TYPE = 46
IMAPI_FEATURE_PAGE_TYPE_DVD_DASH_WRITE: IMAPI_FEATURE_PAGE_TYPE = 47
IMAPI_FEATURE_PAGE_TYPE_DOUBLE_DENSITY_CD_READ: IMAPI_FEATURE_PAGE_TYPE = 48
IMAPI_FEATURE_PAGE_TYPE_DOUBLE_DENSITY_CD_R_WRITE: IMAPI_FEATURE_PAGE_TYPE = 49
IMAPI_FEATURE_PAGE_TYPE_DOUBLE_DENSITY_CD_RW_WRITE: IMAPI_FEATURE_PAGE_TYPE = 50
IMAPI_FEATURE_PAGE_TYPE_LAYER_JUMP_RECORDING: IMAPI_FEATURE_PAGE_TYPE = 51
IMAPI_FEATURE_PAGE_TYPE_CD_RW_MEDIA_WRITE_SUPPORT: IMAPI_FEATURE_PAGE_TYPE = 55
IMAPI_FEATURE_PAGE_TYPE_BD_PSEUDO_OVERWRITE: IMAPI_FEATURE_PAGE_TYPE = 56
IMAPI_FEATURE_PAGE_TYPE_DVD_PLUS_R_DUAL_LAYER: IMAPI_FEATURE_PAGE_TYPE = 59
IMAPI_FEATURE_PAGE_TYPE_BD_READ: IMAPI_FEATURE_PAGE_TYPE = 64
IMAPI_FEATURE_PAGE_TYPE_BD_WRITE: IMAPI_FEATURE_PAGE_TYPE = 65
IMAPI_FEATURE_PAGE_TYPE_HD_DVD_READ: IMAPI_FEATURE_PAGE_TYPE = 80
IMAPI_FEATURE_PAGE_TYPE_HD_DVD_WRITE: IMAPI_FEATURE_PAGE_TYPE = 81
IMAPI_FEATURE_PAGE_TYPE_POWER_MANAGEMENT: IMAPI_FEATURE_PAGE_TYPE = 256
IMAPI_FEATURE_PAGE_TYPE_SMART: IMAPI_FEATURE_PAGE_TYPE = 257
IMAPI_FEATURE_PAGE_TYPE_EMBEDDED_CHANGER: IMAPI_FEATURE_PAGE_TYPE = 258
IMAPI_FEATURE_PAGE_TYPE_CD_ANALOG_PLAY: IMAPI_FEATURE_PAGE_TYPE = 259
IMAPI_FEATURE_PAGE_TYPE_MICROCODE_UPDATE: IMAPI_FEATURE_PAGE_TYPE = 260
IMAPI_FEATURE_PAGE_TYPE_TIMEOUT: IMAPI_FEATURE_PAGE_TYPE = 261
IMAPI_FEATURE_PAGE_TYPE_DVD_CSS: IMAPI_FEATURE_PAGE_TYPE = 262
IMAPI_FEATURE_PAGE_TYPE_REAL_TIME_STREAMING: IMAPI_FEATURE_PAGE_TYPE = 263
IMAPI_FEATURE_PAGE_TYPE_LOGICAL_UNIT_SERIAL_NUMBER: IMAPI_FEATURE_PAGE_TYPE = 264
IMAPI_FEATURE_PAGE_TYPE_MEDIA_SERIAL_NUMBER: IMAPI_FEATURE_PAGE_TYPE = 265
IMAPI_FEATURE_PAGE_TYPE_DISC_CONTROL_BLOCKS: IMAPI_FEATURE_PAGE_TYPE = 266
IMAPI_FEATURE_PAGE_TYPE_DVD_CPRM: IMAPI_FEATURE_PAGE_TYPE = 267
IMAPI_FEATURE_PAGE_TYPE_FIRMWARE_INFORMATION: IMAPI_FEATURE_PAGE_TYPE = 268
IMAPI_FEATURE_PAGE_TYPE_AACS: IMAPI_FEATURE_PAGE_TYPE = 269
IMAPI_FEATURE_PAGE_TYPE_VCPS: IMAPI_FEATURE_PAGE_TYPE = 272
IMAPI_FORMAT2_DATA_MEDIA_STATE = Int32
IMAPI_FORMAT2_DATA_MEDIA_STATE_UNKNOWN: IMAPI_FORMAT2_DATA_MEDIA_STATE = 0
IMAPI_FORMAT2_DATA_MEDIA_STATE_INFORMATIONAL_MASK: IMAPI_FORMAT2_DATA_MEDIA_STATE = 15
IMAPI_FORMAT2_DATA_MEDIA_STATE_UNSUPPORTED_MASK: IMAPI_FORMAT2_DATA_MEDIA_STATE = 64512
IMAPI_FORMAT2_DATA_MEDIA_STATE_OVERWRITE_ONLY: IMAPI_FORMAT2_DATA_MEDIA_STATE = 1
IMAPI_FORMAT2_DATA_MEDIA_STATE_RANDOMLY_WRITABLE: IMAPI_FORMAT2_DATA_MEDIA_STATE = 1
IMAPI_FORMAT2_DATA_MEDIA_STATE_BLANK: IMAPI_FORMAT2_DATA_MEDIA_STATE = 2
IMAPI_FORMAT2_DATA_MEDIA_STATE_APPENDABLE: IMAPI_FORMAT2_DATA_MEDIA_STATE = 4
IMAPI_FORMAT2_DATA_MEDIA_STATE_FINAL_SESSION: IMAPI_FORMAT2_DATA_MEDIA_STATE = 8
IMAPI_FORMAT2_DATA_MEDIA_STATE_DAMAGED: IMAPI_FORMAT2_DATA_MEDIA_STATE = 1024
IMAPI_FORMAT2_DATA_MEDIA_STATE_ERASE_REQUIRED: IMAPI_FORMAT2_DATA_MEDIA_STATE = 2048
IMAPI_FORMAT2_DATA_MEDIA_STATE_NON_EMPTY_SESSION: IMAPI_FORMAT2_DATA_MEDIA_STATE = 4096
IMAPI_FORMAT2_DATA_MEDIA_STATE_WRITE_PROTECTED: IMAPI_FORMAT2_DATA_MEDIA_STATE = 8192
IMAPI_FORMAT2_DATA_MEDIA_STATE_FINALIZED: IMAPI_FORMAT2_DATA_MEDIA_STATE = 16384
IMAPI_FORMAT2_DATA_MEDIA_STATE_UNSUPPORTED_MEDIA: IMAPI_FORMAT2_DATA_MEDIA_STATE = 32768
IMAPI_FORMAT2_DATA_WRITE_ACTION = Int32
IMAPI_FORMAT2_DATA_WRITE_ACTION_VALIDATING_MEDIA: IMAPI_FORMAT2_DATA_WRITE_ACTION = 0
IMAPI_FORMAT2_DATA_WRITE_ACTION_FORMATTING_MEDIA: IMAPI_FORMAT2_DATA_WRITE_ACTION = 1
IMAPI_FORMAT2_DATA_WRITE_ACTION_INITIALIZING_HARDWARE: IMAPI_FORMAT2_DATA_WRITE_ACTION = 2
IMAPI_FORMAT2_DATA_WRITE_ACTION_CALIBRATING_POWER: IMAPI_FORMAT2_DATA_WRITE_ACTION = 3
IMAPI_FORMAT2_DATA_WRITE_ACTION_WRITING_DATA: IMAPI_FORMAT2_DATA_WRITE_ACTION = 4
IMAPI_FORMAT2_DATA_WRITE_ACTION_FINALIZATION: IMAPI_FORMAT2_DATA_WRITE_ACTION = 5
IMAPI_FORMAT2_DATA_WRITE_ACTION_COMPLETED: IMAPI_FORMAT2_DATA_WRITE_ACTION = 6
IMAPI_FORMAT2_DATA_WRITE_ACTION_VERIFYING: IMAPI_FORMAT2_DATA_WRITE_ACTION = 7
IMAPI_FORMAT2_RAW_CD_DATA_SECTOR_TYPE = Int32
IMAPI_FORMAT2_RAW_CD_SUBCODE_PQ_ONLY: IMAPI_FORMAT2_RAW_CD_DATA_SECTOR_TYPE = 1
IMAPI_FORMAT2_RAW_CD_SUBCODE_IS_COOKED: IMAPI_FORMAT2_RAW_CD_DATA_SECTOR_TYPE = 2
IMAPI_FORMAT2_RAW_CD_SUBCODE_IS_RAW: IMAPI_FORMAT2_RAW_CD_DATA_SECTOR_TYPE = 3
IMAPI_FORMAT2_RAW_CD_WRITE_ACTION = Int32
IMAPI_FORMAT2_RAW_CD_WRITE_ACTION_UNKNOWN: IMAPI_FORMAT2_RAW_CD_WRITE_ACTION = 0
IMAPI_FORMAT2_RAW_CD_WRITE_ACTION_PREPARING: IMAPI_FORMAT2_RAW_CD_WRITE_ACTION = 1
IMAPI_FORMAT2_RAW_CD_WRITE_ACTION_WRITING: IMAPI_FORMAT2_RAW_CD_WRITE_ACTION = 2
IMAPI_FORMAT2_RAW_CD_WRITE_ACTION_FINISHING: IMAPI_FORMAT2_RAW_CD_WRITE_ACTION = 3
IMAPI_FORMAT2_TAO_WRITE_ACTION = Int32
IMAPI_FORMAT2_TAO_WRITE_ACTION_UNKNOWN: IMAPI_FORMAT2_TAO_WRITE_ACTION = 0
IMAPI_FORMAT2_TAO_WRITE_ACTION_PREPARING: IMAPI_FORMAT2_TAO_WRITE_ACTION = 1
IMAPI_FORMAT2_TAO_WRITE_ACTION_WRITING: IMAPI_FORMAT2_TAO_WRITE_ACTION = 2
IMAPI_FORMAT2_TAO_WRITE_ACTION_FINISHING: IMAPI_FORMAT2_TAO_WRITE_ACTION = 3
IMAPI_FORMAT2_TAO_WRITE_ACTION_VERIFYING: IMAPI_FORMAT2_TAO_WRITE_ACTION = 4
IMAPI_MEDIA_PHYSICAL_TYPE = Int32
IMAPI_MEDIA_TYPE_UNKNOWN: IMAPI_MEDIA_PHYSICAL_TYPE = 0
IMAPI_MEDIA_TYPE_CDROM: IMAPI_MEDIA_PHYSICAL_TYPE = 1
IMAPI_MEDIA_TYPE_CDR: IMAPI_MEDIA_PHYSICAL_TYPE = 2
IMAPI_MEDIA_TYPE_CDRW: IMAPI_MEDIA_PHYSICAL_TYPE = 3
IMAPI_MEDIA_TYPE_DVDROM: IMAPI_MEDIA_PHYSICAL_TYPE = 4
IMAPI_MEDIA_TYPE_DVDRAM: IMAPI_MEDIA_PHYSICAL_TYPE = 5
IMAPI_MEDIA_TYPE_DVDPLUSR: IMAPI_MEDIA_PHYSICAL_TYPE = 6
IMAPI_MEDIA_TYPE_DVDPLUSRW: IMAPI_MEDIA_PHYSICAL_TYPE = 7
IMAPI_MEDIA_TYPE_DVDPLUSR_DUALLAYER: IMAPI_MEDIA_PHYSICAL_TYPE = 8
IMAPI_MEDIA_TYPE_DVDDASHR: IMAPI_MEDIA_PHYSICAL_TYPE = 9
IMAPI_MEDIA_TYPE_DVDDASHRW: IMAPI_MEDIA_PHYSICAL_TYPE = 10
IMAPI_MEDIA_TYPE_DVDDASHR_DUALLAYER: IMAPI_MEDIA_PHYSICAL_TYPE = 11
IMAPI_MEDIA_TYPE_DISK: IMAPI_MEDIA_PHYSICAL_TYPE = 12
IMAPI_MEDIA_TYPE_DVDPLUSRW_DUALLAYER: IMAPI_MEDIA_PHYSICAL_TYPE = 13
IMAPI_MEDIA_TYPE_HDDVDROM: IMAPI_MEDIA_PHYSICAL_TYPE = 14
IMAPI_MEDIA_TYPE_HDDVDR: IMAPI_MEDIA_PHYSICAL_TYPE = 15
IMAPI_MEDIA_TYPE_HDDVDRAM: IMAPI_MEDIA_PHYSICAL_TYPE = 16
IMAPI_MEDIA_TYPE_BDROM: IMAPI_MEDIA_PHYSICAL_TYPE = 17
IMAPI_MEDIA_TYPE_BDR: IMAPI_MEDIA_PHYSICAL_TYPE = 18
IMAPI_MEDIA_TYPE_BDRE: IMAPI_MEDIA_PHYSICAL_TYPE = 19
IMAPI_MEDIA_TYPE_MAX: IMAPI_MEDIA_PHYSICAL_TYPE = 19
IMAPI_MEDIA_WRITE_PROTECT_STATE = Int32
IMAPI_WRITEPROTECTED_UNTIL_POWERDOWN: IMAPI_MEDIA_WRITE_PROTECT_STATE = 1
IMAPI_WRITEPROTECTED_BY_CARTRIDGE: IMAPI_MEDIA_WRITE_PROTECT_STATE = 2
IMAPI_WRITEPROTECTED_BY_MEDIA_SPECIFIC_REASON: IMAPI_MEDIA_WRITE_PROTECT_STATE = 4
IMAPI_WRITEPROTECTED_BY_SOFTWARE_WRITE_PROTECT: IMAPI_MEDIA_WRITE_PROTECT_STATE = 8
IMAPI_WRITEPROTECTED_BY_DISC_CONTROL_BLOCK: IMAPI_MEDIA_WRITE_PROTECT_STATE = 16
IMAPI_WRITEPROTECTED_READ_ONLY_MEDIA: IMAPI_MEDIA_WRITE_PROTECT_STATE = 16384
IMAPI_MODE_PAGE_REQUEST_TYPE = Int32
IMAPI_MODE_PAGE_REQUEST_TYPE_CURRENT_VALUES: IMAPI_MODE_PAGE_REQUEST_TYPE = 0
IMAPI_MODE_PAGE_REQUEST_TYPE_CHANGEABLE_VALUES: IMAPI_MODE_PAGE_REQUEST_TYPE = 1
IMAPI_MODE_PAGE_REQUEST_TYPE_DEFAULT_VALUES: IMAPI_MODE_PAGE_REQUEST_TYPE = 2
IMAPI_MODE_PAGE_REQUEST_TYPE_SAVED_VALUES: IMAPI_MODE_PAGE_REQUEST_TYPE = 3
IMAPI_MODE_PAGE_TYPE = Int32
IMAPI_MODE_PAGE_TYPE_READ_WRITE_ERROR_RECOVERY: IMAPI_MODE_PAGE_TYPE = 1
IMAPI_MODE_PAGE_TYPE_MRW: IMAPI_MODE_PAGE_TYPE = 3
IMAPI_MODE_PAGE_TYPE_WRITE_PARAMETERS: IMAPI_MODE_PAGE_TYPE = 5
IMAPI_MODE_PAGE_TYPE_CACHING: IMAPI_MODE_PAGE_TYPE = 8
IMAPI_MODE_PAGE_TYPE_INFORMATIONAL_EXCEPTIONS: IMAPI_MODE_PAGE_TYPE = 28
IMAPI_MODE_PAGE_TYPE_TIMEOUT_AND_PROTECT: IMAPI_MODE_PAGE_TYPE = 29
IMAPI_MODE_PAGE_TYPE_POWER_CONDITION: IMAPI_MODE_PAGE_TYPE = 26
IMAPI_MODE_PAGE_TYPE_LEGACY_CAPABILITIES: IMAPI_MODE_PAGE_TYPE = 42
IMAPI_PROFILE_TYPE = Int32
IMAPI_PROFILE_TYPE_INVALID: IMAPI_PROFILE_TYPE = 0
IMAPI_PROFILE_TYPE_NON_REMOVABLE_DISK: IMAPI_PROFILE_TYPE = 1
IMAPI_PROFILE_TYPE_REMOVABLE_DISK: IMAPI_PROFILE_TYPE = 2
IMAPI_PROFILE_TYPE_MO_ERASABLE: IMAPI_PROFILE_TYPE = 3
IMAPI_PROFILE_TYPE_MO_WRITE_ONCE: IMAPI_PROFILE_TYPE = 4
IMAPI_PROFILE_TYPE_AS_MO: IMAPI_PROFILE_TYPE = 5
IMAPI_PROFILE_TYPE_CDROM: IMAPI_PROFILE_TYPE = 8
IMAPI_PROFILE_TYPE_CD_RECORDABLE: IMAPI_PROFILE_TYPE = 9
IMAPI_PROFILE_TYPE_CD_REWRITABLE: IMAPI_PROFILE_TYPE = 10
IMAPI_PROFILE_TYPE_DVDROM: IMAPI_PROFILE_TYPE = 16
IMAPI_PROFILE_TYPE_DVD_DASH_RECORDABLE: IMAPI_PROFILE_TYPE = 17
IMAPI_PROFILE_TYPE_DVD_RAM: IMAPI_PROFILE_TYPE = 18
IMAPI_PROFILE_TYPE_DVD_DASH_REWRITABLE: IMAPI_PROFILE_TYPE = 19
IMAPI_PROFILE_TYPE_DVD_DASH_RW_SEQUENTIAL: IMAPI_PROFILE_TYPE = 20
IMAPI_PROFILE_TYPE_DVD_DASH_R_DUAL_SEQUENTIAL: IMAPI_PROFILE_TYPE = 21
IMAPI_PROFILE_TYPE_DVD_DASH_R_DUAL_LAYER_JUMP: IMAPI_PROFILE_TYPE = 22
IMAPI_PROFILE_TYPE_DVD_PLUS_RW: IMAPI_PROFILE_TYPE = 26
IMAPI_PROFILE_TYPE_DVD_PLUS_R: IMAPI_PROFILE_TYPE = 27
IMAPI_PROFILE_TYPE_DDCDROM: IMAPI_PROFILE_TYPE = 32
IMAPI_PROFILE_TYPE_DDCD_RECORDABLE: IMAPI_PROFILE_TYPE = 33
IMAPI_PROFILE_TYPE_DDCD_REWRITABLE: IMAPI_PROFILE_TYPE = 34
IMAPI_PROFILE_TYPE_DVD_PLUS_RW_DUAL: IMAPI_PROFILE_TYPE = 42
IMAPI_PROFILE_TYPE_DVD_PLUS_R_DUAL: IMAPI_PROFILE_TYPE = 43
IMAPI_PROFILE_TYPE_BD_ROM: IMAPI_PROFILE_TYPE = 64
IMAPI_PROFILE_TYPE_BD_R_SEQUENTIAL: IMAPI_PROFILE_TYPE = 65
IMAPI_PROFILE_TYPE_BD_R_RANDOM_RECORDING: IMAPI_PROFILE_TYPE = 66
IMAPI_PROFILE_TYPE_BD_REWRITABLE: IMAPI_PROFILE_TYPE = 67
IMAPI_PROFILE_TYPE_HD_DVD_ROM: IMAPI_PROFILE_TYPE = 80
IMAPI_PROFILE_TYPE_HD_DVD_RECORDABLE: IMAPI_PROFILE_TYPE = 81
IMAPI_PROFILE_TYPE_HD_DVD_RAM: IMAPI_PROFILE_TYPE = 82
IMAPI_PROFILE_TYPE_NON_STANDARD: IMAPI_PROFILE_TYPE = 65535
IMAPI_READ_TRACK_ADDRESS_TYPE = Int32
IMAPI_READ_TRACK_ADDRESS_TYPE_LBA: IMAPI_READ_TRACK_ADDRESS_TYPE = 0
IMAPI_READ_TRACK_ADDRESS_TYPE_TRACK: IMAPI_READ_TRACK_ADDRESS_TYPE = 1
IMAPI_READ_TRACK_ADDRESS_TYPE_SESSION: IMAPI_READ_TRACK_ADDRESS_TYPE = 2
IMMPID_CPV_ENUM = Int32
IMMPID_CPV_BEFORE__: IMMPID_CPV_ENUM = 32767
IMMPID_CP_START: IMMPID_CPV_ENUM = 32768
IMMPID_CPV_AFTER__: IMMPID_CPV_ENUM = 32769
IMMPID_MPV_ENUM = Int32
IMMPID_MPV_BEFORE__: IMMPID_MPV_ENUM = 12287
IMMPID_MPV_STORE_DRIVER_HANDLE: IMMPID_MPV_ENUM = 12288
IMMPID_MPV_MESSAGE_CREATION_FLAGS: IMMPID_MPV_ENUM = 12289
IMMPID_MPV_MESSAGE_OPEN_HANDLES: IMMPID_MPV_ENUM = 12290
IMMPID_MPV_TOTAL_OPEN_HANDLES: IMMPID_MPV_ENUM = 12291
IMMPID_MPV_TOTAL_OPEN_PROPERTY_STREAM_HANDLES: IMMPID_MPV_ENUM = 12292
IMMPID_MPV_TOTAL_OPEN_CONTENT_HANDLES: IMMPID_MPV_ENUM = 12293
IMMPID_MPV_AFTER__: IMMPID_MPV_ENUM = 12294
IMMPID_MP_ENUM = Int32
IMMPID_MP_BEFORE__: IMMPID_MP_ENUM = 4095
IMMPID_MP_RECIPIENT_LIST: IMMPID_MP_ENUM = 4096
IMMPID_MP_CONTENT_FILE_NAME: IMMPID_MP_ENUM = 4097
IMMPID_MP_SENDER_ADDRESS_SMTP: IMMPID_MP_ENUM = 4098
IMMPID_MP_SENDER_ADDRESS_X500: IMMPID_MP_ENUM = 4099
IMMPID_MP_SENDER_ADDRESS_X400: IMMPID_MP_ENUM = 4100
IMMPID_MP_SENDER_ADDRESS_LEGACY_EX_DN: IMMPID_MP_ENUM = 4101
IMMPID_MP_DOMAIN_LIST: IMMPID_MP_ENUM = 4102
IMMPID_MP_PICKUP_FILE_NAME: IMMPID_MP_ENUM = 4103
IMMPID_MP_AUTHENTICATED_USER_NAME: IMMPID_MP_ENUM = 4104
IMMPID_MP_CONNECTION_IP_ADDRESS: IMMPID_MP_ENUM = 4105
IMMPID_MP_HELO_DOMAIN: IMMPID_MP_ENUM = 4106
IMMPID_MP_EIGHTBIT_MIME_OPTION: IMMPID_MP_ENUM = 4107
IMMPID_MP_CHUNKING_OPTION: IMMPID_MP_ENUM = 4108
IMMPID_MP_BINARYMIME_OPTION: IMMPID_MP_ENUM = 4109
IMMPID_MP_REMOTE_AUTHENTICATION_TYPE: IMMPID_MP_ENUM = 4110
IMMPID_MP_ERROR_CODE: IMMPID_MP_ENUM = 4111
IMMPID_MP_DSN_ENVID_VALUE: IMMPID_MP_ENUM = 4112
IMMPID_MP_DSN_RET_VALUE: IMMPID_MP_ENUM = 4113
IMMPID_MP_REMOTE_SERVER_DSN_CAPABLE: IMMPID_MP_ENUM = 4114
IMMPID_MP_ARRIVAL_TIME: IMMPID_MP_ENUM = 4115
IMMPID_MP_MESSAGE_STATUS: IMMPID_MP_ENUM = 4116
IMMPID_MP_EXPIRE_DELAY: IMMPID_MP_ENUM = 4117
IMMPID_MP_EXPIRE_NDR: IMMPID_MP_ENUM = 4118
IMMPID_MP_LOCAL_EXPIRE_DELAY: IMMPID_MP_ENUM = 4119
IMMPID_MP_LOCAL_EXPIRE_NDR: IMMPID_MP_ENUM = 4120
IMMPID_MP_ARRIVAL_FILETIME: IMMPID_MP_ENUM = 4121
IMMPID_MP_HR_CAT_STATUS: IMMPID_MP_ENUM = 4122
IMMPID_MP_MSG_GUID: IMMPID_MP_ENUM = 4123
IMMPID_MP_SUPERSEDES_MSG_GUID: IMMPID_MP_ENUM = 4124
IMMPID_MP_SCANNED_FOR_CRLF_DOT_CRLF: IMMPID_MP_ENUM = 4125
IMMPID_MP_FOUND_EMBEDDED_CRLF_DOT_CRLF: IMMPID_MP_ENUM = 4126
IMMPID_MP_MSG_SIZE_HINT: IMMPID_MP_ENUM = 4127
IMMPID_MP_RFC822_MSG_ID: IMMPID_MP_ENUM = 4128
IMMPID_MP_RFC822_MSG_SUBJECT: IMMPID_MP_ENUM = 4129
IMMPID_MP_RFC822_FROM_ADDRESS: IMMPID_MP_ENUM = 4130
IMMPID_MP_RFC822_TO_ADDRESS: IMMPID_MP_ENUM = 4131
IMMPID_MP_RFC822_CC_ADDRESS: IMMPID_MP_ENUM = 4132
IMMPID_MP_RFC822_BCC_ADDRESS: IMMPID_MP_ENUM = 4133
IMMPID_MP_CONNECTION_SERVER_IP_ADDRESS: IMMPID_MP_ENUM = 4134
IMMPID_MP_SERVER_NAME: IMMPID_MP_ENUM = 4135
IMMPID_MP_SERVER_VERSION: IMMPID_MP_ENUM = 4136
IMMPID_MP_NUM_RECIPIENTS: IMMPID_MP_ENUM = 4137
IMMPID_MP_X_PRIORITY: IMMPID_MP_ENUM = 4138
IMMPID_MP_FROM_ADDRESS: IMMPID_MP_ENUM = 4139
IMMPID_MP_SENDER_ADDRESS: IMMPID_MP_ENUM = 4140
IMMPID_MP_DEFERRED_DELIVERY_FILETIME: IMMPID_MP_ENUM = 4141
IMMPID_MP_SENDER_ADDRESS_OTHER: IMMPID_MP_ENUM = 4142
IMMPID_MP_ORIGINAL_ARRIVAL_TIME: IMMPID_MP_ENUM = 4143
IMMPID_MP_MSGCLASS: IMMPID_MP_ENUM = 4144
IMMPID_MP_CONTENT_TYPE: IMMPID_MP_ENUM = 4145
IMMPID_MP_ENCRYPTION_TYPE: IMMPID_MP_ENUM = 4146
IMMPID_MP_CONNECTION_SERVER_PORT: IMMPID_MP_ENUM = 4147
IMMPID_MP_CLIENT_AUTH_USER: IMMPID_MP_ENUM = 4148
IMMPID_MP_CLIENT_AUTH_TYPE: IMMPID_MP_ENUM = 4149
IMMPID_MP_CRC_GLOBAL: IMMPID_MP_ENUM = 4150
IMMPID_MP_CRC_RECIPS: IMMPID_MP_ENUM = 4151
IMMPID_MP_INBOUND_MAIL_FROM_AUTH: IMMPID_MP_ENUM = 4152
IMMPID_MP_AFTER__: IMMPID_MP_ENUM = 4153
IMMPID_NMP_ENUM = Int32
IMMPID_NMP_BEFORE__: IMMPID_NMP_ENUM = 24575
IMMPID_NMP_SECONDARY_GROUPS: IMMPID_NMP_ENUM = 24576
IMMPID_NMP_SECONDARY_ARTNUM: IMMPID_NMP_ENUM = 24577
IMMPID_NMP_PRIMARY_GROUP: IMMPID_NMP_ENUM = 24578
IMMPID_NMP_PRIMARY_ARTID: IMMPID_NMP_ENUM = 24579
IMMPID_NMP_POST_TOKEN: IMMPID_NMP_ENUM = 24580
IMMPID_NMP_NEWSGROUP_LIST: IMMPID_NMP_ENUM = 24581
IMMPID_NMP_HEADERS: IMMPID_NMP_ENUM = 24582
IMMPID_NMP_NNTP_PROCESSING: IMMPID_NMP_ENUM = 24583
IMMPID_NMP_NNTP_APPROVED_HEADER: IMMPID_NMP_ENUM = 24584
IMMPID_NMP_AFTER__: IMMPID_NMP_ENUM = 24585
IMMPID_RPV_ENUM = Int32
IMMPID_RPV_BEFORE__: IMMPID_RPV_ENUM = 16383
IMMPID_RPV_DONT_DELIVER: IMMPID_RPV_ENUM = 16384
IMMPID_RPV_NO_NAME_COLLISIONS: IMMPID_RPV_ENUM = 16385
IMMPID_RPV_AFTER__: IMMPID_RPV_ENUM = 16386
IMMPID_RP_ENUM = Int32
IMMPID_RP_BEFORE__: IMMPID_RP_ENUM = 8191
IMMPID_RP_DSN_NOTIFY_SUCCESS: IMMPID_RP_ENUM = 8192
IMMPID_RP_DSN_NOTIFY_INVALID: IMMPID_RP_ENUM = 8193
IMMPID_RP_ADDRESS_TYPE: IMMPID_RP_ENUM = 8194
IMMPID_RP_ADDRESS: IMMPID_RP_ENUM = 8195
IMMPID_RP_ADDRESS_TYPE_SMTP: IMMPID_RP_ENUM = 8196
IMMPID_RP_ERROR_CODE: IMMPID_RP_ENUM = 8197
IMMPID_RP_ERROR_STRING: IMMPID_RP_ENUM = 8198
IMMPID_RP_DSN_NOTIFY_VALUE: IMMPID_RP_ENUM = 8199
IMMPID_RP_DSN_ORCPT_VALUE: IMMPID_RP_ENUM = 8200
IMMPID_RP_ADDRESS_SMTP: IMMPID_RP_ENUM = 8201
IMMPID_RP_ADDRESS_X400: IMMPID_RP_ENUM = 8202
IMMPID_RP_ADDRESS_X500: IMMPID_RP_ENUM = 8203
IMMPID_RP_LEGACY_EX_DN: IMMPID_RP_ENUM = 8204
IMMPID_RP_RECIPIENT_FLAGS: IMMPID_RP_ENUM = 8205
IMMPID_RP_SMTP_STATUS_STRING: IMMPID_RP_ENUM = 8206
IMMPID_RP_DSN_PRE_CAT_ADDRESS: IMMPID_RP_ENUM = 8207
IMMPID_RP_MDB_GUID: IMMPID_RP_ENUM = 8208
IMMPID_RP_USER_GUID: IMMPID_RP_ENUM = 8209
IMMPID_RP_DOMAIN: IMMPID_RP_ENUM = 8210
IMMPID_RP_ADDRESS_OTHER: IMMPID_RP_ENUM = 8211
IMMPID_RP_DISPLAY_NAME: IMMPID_RP_ENUM = 8212
IMMPID_RP_AFTER__: IMMPID_RP_ENUM = 8213
class IMMP_MPV_STORE_DRIVER_HANDLE(Structure):
    guidSignature: Guid
class IMultisession(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('27354150-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
    @commethod(7)
    def get_IsSupportedOnCurrentMediaState(value: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_InUse(value: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_InUse(value: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_ImportRecorder(value: POINTER(win32more.Storage.Imapi.IDiscRecorder2_head)) -> win32more.Foundation.HRESULT: ...
class IMultisessionRandomWrite(c_void_p):
    extends: win32more.Storage.Imapi.IMultisession
    Guid = Guid('b507ca23-2204-11dd-96-6a-00-1a-a0-1b-bc-58')
    @commethod(11)
    def get_WriteUnitSize(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_LastWrittenAddress(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_TotalSectorsOnMedia(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IMultisessionSequential(c_void_p):
    extends: win32more.Storage.Imapi.IMultisession
    Guid = Guid('27354151-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
    @commethod(11)
    def get_IsFirstDataSession(value: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_StartAddressOfPreviousSession(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_LastWrittenAddressOfPreviousSession(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_NextWritableAddress(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_FreeSectorsOnMedia(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IMultisessionSequential2(c_void_p):
    extends: win32more.Storage.Imapi.IMultisessionSequential
    Guid = Guid('b507ca22-2204-11dd-96-6a-00-1a-a0-1b-bc-58')
    @commethod(16)
    def get_WriteUnitSize(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IProgressItem(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('2c941fd5-975b-59be-a9-60-9a-2a-26-28-53-a5')
    @commethod(7)
    def get_Description(desc: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_FirstBlock(block: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_LastBlock(block: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_BlockCount(blocks: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IProgressItems(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('2c941fd7-975b-59be-a9-60-9a-2a-26-28-53-a5')
    @commethod(7)
    def get__NewEnum(NewEnum: POINTER(win32more.System.Ole.IEnumVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(Index: Int32, item: POINTER(win32more.Storage.Imapi.IProgressItem_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(Count: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def ProgressItemFromBlock(block: UInt32, item: POINTER(win32more.Storage.Imapi.IProgressItem_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def ProgressItemFromDescription(description: win32more.Foundation.BSTR, item: POINTER(win32more.Storage.Imapi.IProgressItem_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_EnumProgressItems(NewEnum: POINTER(win32more.Storage.Imapi.IEnumProgressItems_head)) -> win32more.Foundation.HRESULT: ...
class IRawCDImageCreator(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('25983550-9d65-49ce-b3-35-40-63-0d-90-12-27')
    @commethod(7)
    def CreateResultImage(resultStream: POINTER(win32more.System.Com.IStream_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def AddTrack(dataType: win32more.Storage.Imapi.IMAPI_CD_SECTOR_TYPE, data: win32more.System.Com.IStream_head, trackIndex: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def AddSpecialPregap(data: win32more.System.Com.IStream_head) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def AddSubcodeRWGenerator(subcode: win32more.System.Com.IStream_head) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def put_ResultingImageType(value: win32more.Storage.Imapi.IMAPI_FORMAT2_RAW_CD_DATA_SECTOR_TYPE) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_ResultingImageType(value: POINTER(win32more.Storage.Imapi.IMAPI_FORMAT2_RAW_CD_DATA_SECTOR_TYPE)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_StartOfLeadout(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def put_StartOfLeadoutLimit(value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_StartOfLeadoutLimit(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def put_DisableGaplessAudio(value: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_DisableGaplessAudio(value: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def put_MediaCatalogNumber(value: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_MediaCatalogNumber(value: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def put_StartingTrackNumber(value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def get_StartingTrackNumber(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def get_TrackInfo(trackIndex: Int32, value: POINTER(win32more.Storage.Imapi.IRawCDImageTrackInfo_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def get_NumberOfExistingTracks(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def get_LastUsedUserSectorInImage(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def get_ExpectedTableOfContents(value: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
class IRawCDImageTrackInfo(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('25983551-9d65-49ce-b3-35-40-63-0d-90-12-27')
    @commethod(7)
    def get_StartingLba(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_SectorCount(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_TrackNumber(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_SectorType(value: POINTER(win32more.Storage.Imapi.IMAPI_CD_SECTOR_TYPE)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_ISRC(value: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def put_ISRC(value: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_DigitalAudioCopySetting(value: POINTER(win32more.Storage.Imapi.IMAPI_CD_TRACK_DIGITAL_COPY_SETTING)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def put_DigitalAudioCopySetting(value: win32more.Storage.Imapi.IMAPI_CD_TRACK_DIGITAL_COPY_SETTING) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_AudioHasPreemphasis(value: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def put_AudioHasPreemphasis(value: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_TrackIndexes(value: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def AddTrackIndex(lbaOffset: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def ClearTrackIndex(lbaOffset: Int32) -> win32more.Foundation.HRESULT: ...
class IRedbookDiscMaster(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('e3bc42cd-4e5c-11d3-91-44-00-10-4b-a1-1c-5e')
    @commethod(3)
    def GetTotalAudioTracks(pnTracks: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetTotalAudioBlocks(pnBlocks: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetUsedAudioBlocks(pnBlocks: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetAvailableAudioTrackBlocks(pnBlocks: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetAudioBlockSize(pnBlockBytes: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def CreateAudioTrack(nBlocks: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def AddAudioTrackBlocks(pby: c_char_p_no, cb: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def CloseAudioTrack() -> win32more.Foundation.HRESULT: ...
class IStreamConcatenate(c_void_p):
    extends: win32more.System.Com.IStream
    Guid = Guid('27354146-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
    @commethod(14)
    def Initialize(stream1: win32more.System.Com.IStream_head, stream2: win32more.System.Com.IStream_head) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def Initialize2(streams: POINTER(win32more.System.Com.IStream_head), streamCount: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def Append(stream: win32more.System.Com.IStream_head) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def Append2(streams: POINTER(win32more.System.Com.IStream_head), streamCount: UInt32) -> win32more.Foundation.HRESULT: ...
class IStreamInterleave(c_void_p):
    extends: win32more.System.Com.IStream
    Guid = Guid('27354147-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
    @commethod(14)
    def Initialize(streams: POINTER(win32more.System.Com.IStream_head), interleaveSizes: POINTER(UInt32), streamCount: UInt32) -> win32more.Foundation.HRESULT: ...
class IStreamPseudoRandomBased(c_void_p):
    extends: win32more.System.Com.IStream
    Guid = Guid('27354145-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
    @commethod(14)
    def put_Seed(value: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_Seed(value: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def put_ExtendedSeed(values: POINTER(UInt32), eCount: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_ExtendedSeed(values: POINTER(POINTER(UInt32)), eCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IWriteEngine2(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('27354135-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
    @commethod(7)
    def WriteSection(data: win32more.System.Com.IStream_head, startingBlockAddress: Int32, numberOfBlocks: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def CancelWrite() -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def put_Recorder(value: win32more.Storage.Imapi.IDiscRecorder2Ex_head) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_Recorder(value: POINTER(win32more.Storage.Imapi.IDiscRecorder2Ex_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def put_UseStreamingWrite12(value: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_UseStreamingWrite12(value: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def put_StartingSectorsPerSecond(value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_StartingSectorsPerSecond(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def put_EndingSectorsPerSecond(value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_EndingSectorsPerSecond(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def put_BytesPerSector(value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def get_BytesPerSector(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_WriteInProgress(value: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
class IWriteEngine2EventArgs(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('27354136-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
    @commethod(7)
    def get_StartLba(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_SectorCount(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_LastReadLba(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_LastWrittenLba(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_TotalSystemBuffer(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_UsedSystemBuffer(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_FreeSystemBuffer(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IWriteSpeedDescriptor(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('27354144-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
    @commethod(7)
    def get_MediaType(value: POINTER(win32more.Storage.Imapi.IMAPI_MEDIA_PHYSICAL_TYPE)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_RotationTypeIsPureCAV(value: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_WriteSpeed(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
MEDIA_FLAGS = Int32
MEDIA_BLANK: MEDIA_FLAGS = 1
MEDIA_RW: MEDIA_FLAGS = 2
MEDIA_WRITABLE: MEDIA_FLAGS = 4
MEDIA_FORMAT_UNUSABLE_BY_IMAPI: MEDIA_FLAGS = 8
MEDIA_TYPES = Int32
MEDIA_CDDA_CDROM: MEDIA_TYPES = 1
MEDIA_CD_ROM_XA: MEDIA_TYPES = 2
MEDIA_CD_I: MEDIA_TYPES = 3
MEDIA_CD_EXTRA: MEDIA_TYPES = 4
MEDIA_CD_OTHER: MEDIA_TYPES = 5
MEDIA_SPECIAL: MEDIA_TYPES = 6
MSDiscMasterObj = Guid('520cca63-51a5-11d3-91-44-00-10-4b-a1-1c-5e')
MSDiscRecorderObj = Guid('520cca61-51a5-11d3-91-44-00-10-4b-a1-1c-5e')
MSEnumDiscRecordersObj = Guid('8a03567a-63cb-4ba8-ba-f6-52-11-98-16-d1-ef')
@winfunctype_pointer
def MSGCALLRELEASE(ulCallerData: UInt32, lpMessage: win32more.System.AddressBook.IMessage_head) -> Void: ...
MsftDiscFormat2Data = Guid('2735412a-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
MsftDiscFormat2Erase = Guid('2735412b-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
MsftDiscFormat2RawCD = Guid('27354128-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
MsftDiscFormat2TrackAtOnce = Guid('27354129-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
MsftDiscMaster2 = Guid('2735412e-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
MsftDiscRecorder2 = Guid('2735412d-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
MsftFileSystemImage = Guid('2c941fc5-975b-59be-a9-60-9a-2a-26-28-53-a5')
MsftIsoImageManager = Guid('ceee3b62-8f56-4056-86-9b-ef-16-91-7e-3e-fc')
MsftMultisessionRandomWrite = Guid('b507ca24-2204-11dd-96-6a-00-1a-a0-1b-bc-58')
MsftMultisessionSequential = Guid('27354122-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
MsftRawCDImageCreator = Guid('25983561-9d65-49ce-b3-35-40-63-0d-90-12-27')
MsftStreamConcatenate = Guid('27354125-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
MsftStreamInterleave = Guid('27354124-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
MsftStreamPrng001 = Guid('27354126-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
MsftStreamZero = Guid('27354127-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
MsftWriteEngine2 = Guid('2735412c-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
MsftWriteSpeedDescriptor = Guid('27354123-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
PlatformId = Int32
PlatformId_PlatformX86: PlatformId = 0
PlatformId_PlatformPowerPC: PlatformId = 1
PlatformId_PlatformMac: PlatformId = 2
PlatformId_PlatformEFI: PlatformId = 239
ProgressItem = Guid('2c941fcb-975b-59be-a9-60-9a-2a-26-28-53-a5')
ProgressItems = Guid('2c941fc9-975b-59be-a9-60-9a-2a-26-28-53-a5')
RECORDER_TYPES = Int32
RECORDER_CDR: RECORDER_TYPES = 1
RECORDER_CDRW: RECORDER_TYPES = 2
class SPropAttrArray(Structure):
    cValues: UInt32
    aPropAttr: UInt32 * 1
class _MSGSESS(Structure):
    pass
tagIMMPID_CPV_STRUCT = Guid('a2a76b2a-e52d-11d1-aa-64-00-c0-4f-a3-5b-82')
class tagIMMPID_GUIDLIST_ITEM(Structure):
    pguid: POINTER(Guid)
    dwStart: UInt32
    dwLast: UInt32
tagIMMPID_MPV_STRUCT = Guid('cbe69706-c9bd-11d1-9f-f2-00-c0-4f-a3-73-48')
tagIMMPID_MP_STRUCT = Guid('13384cf0-b3c4-11d1-aa-92-00-aa-00-6b-c8-0b')
tagIMMPID_NMP_STRUCT = Guid('7433a9aa-20e2-11d2-94-d6-00-c0-4f-a3-79-f1')
tagIMMPID_RPV_STRUCT = Guid('79e82049-d320-11d1-9f-f4-00-c0-4f-a3-73-48')
tagIMMPID_RP_STRUCT = Guid('79e82048-d320-11d1-9f-f4-00-c0-4f-a3-73-48')
make_head(_module, 'DDiscFormat2DataEvents')
make_head(_module, 'DDiscFormat2EraseEvents')
make_head(_module, 'DDiscFormat2RawCDEvents')
make_head(_module, 'DDiscFormat2TrackAtOnceEvents')
make_head(_module, 'DDiscMaster2Events')
make_head(_module, 'DFileSystemImageEvents')
make_head(_module, 'DFileSystemImageImportEvents')
make_head(_module, 'DWriteEngine2Events')
make_head(_module, 'IBlockRange')
make_head(_module, 'IBlockRangeList')
make_head(_module, 'IBootOptions')
make_head(_module, 'IBurnVerification')
make_head(_module, 'IDiscFormat2')
make_head(_module, 'IDiscFormat2Data')
make_head(_module, 'IDiscFormat2DataEventArgs')
make_head(_module, 'IDiscFormat2Erase')
make_head(_module, 'IDiscFormat2RawCD')
make_head(_module, 'IDiscFormat2RawCDEventArgs')
make_head(_module, 'IDiscFormat2TrackAtOnce')
make_head(_module, 'IDiscFormat2TrackAtOnceEventArgs')
make_head(_module, 'IDiscMaster')
make_head(_module, 'IDiscMaster2')
make_head(_module, 'IDiscMasterProgressEvents')
make_head(_module, 'IDiscRecorder')
make_head(_module, 'IDiscRecorder2')
make_head(_module, 'IDiscRecorder2Ex')
make_head(_module, 'IEnumDiscMasterFormats')
make_head(_module, 'IEnumDiscRecorders')
make_head(_module, 'IEnumFsiItems')
make_head(_module, 'IEnumProgressItems')
make_head(_module, 'IFileSystemImage')
make_head(_module, 'IFileSystemImage2')
make_head(_module, 'IFileSystemImage3')
make_head(_module, 'IFileSystemImageResult')
make_head(_module, 'IFileSystemImageResult2')
make_head(_module, 'IFsiDirectoryItem')
make_head(_module, 'IFsiDirectoryItem2')
make_head(_module, 'IFsiFileItem')
make_head(_module, 'IFsiFileItem2')
make_head(_module, 'IFsiItem')
make_head(_module, 'IFsiNamedStreams')
make_head(_module, 'IIsoImageManager')
make_head(_module, 'IJolietDiscMaster')
make_head(_module, 'IMMP_MPV_STORE_DRIVER_HANDLE')
make_head(_module, 'IMultisession')
make_head(_module, 'IMultisessionRandomWrite')
make_head(_module, 'IMultisessionSequential')
make_head(_module, 'IMultisessionSequential2')
make_head(_module, 'IProgressItem')
make_head(_module, 'IProgressItems')
make_head(_module, 'IRawCDImageCreator')
make_head(_module, 'IRawCDImageTrackInfo')
make_head(_module, 'IRedbookDiscMaster')
make_head(_module, 'IStreamConcatenate')
make_head(_module, 'IStreamInterleave')
make_head(_module, 'IStreamPseudoRandomBased')
make_head(_module, 'IWriteEngine2')
make_head(_module, 'IWriteEngine2EventArgs')
make_head(_module, 'IWriteSpeedDescriptor')
make_head(_module, 'MSGCALLRELEASE')
make_head(_module, 'SPropAttrArray')
make_head(_module, '_MSGSESS')
make_head(_module, 'tagIMMPID_GUIDLIST_ITEM')
__all__ = [
    "BlockRange",
    "BlockRangeList",
    "BootOptions",
    "CATID_SMTP_DNSRESOLVERRECORDSINK",
    "CATID_SMTP_DSN",
    "CATID_SMTP_GET_AUX_DOMAIN_INFO_FLAGS",
    "CATID_SMTP_LOG",
    "CATID_SMTP_MAXMSGSIZE",
    "CATID_SMTP_MSGTRACKLOG",
    "CATID_SMTP_ON_BEFORE_DATA",
    "CATID_SMTP_ON_INBOUND_COMMAND",
    "CATID_SMTP_ON_MESSAGE_START",
    "CATID_SMTP_ON_PER_RECIPIENT",
    "CATID_SMTP_ON_SERVER_RESPONSE",
    "CATID_SMTP_ON_SESSION_END",
    "CATID_SMTP_ON_SESSION_START",
    "CATID_SMTP_STORE_DRIVER",
    "CATID_SMTP_TRANSPORT_CATEGORIZE",
    "CATID_SMTP_TRANSPORT_POSTCATEGORIZE",
    "CATID_SMTP_TRANSPORT_PRECATEGORIZE",
    "CATID_SMTP_TRANSPORT_ROUTER",
    "CATID_SMTP_TRANSPORT_SUBMISSION",
    "CLSID_SmtpCat",
    "CloseIMsgSession",
    "DDiscFormat2DataEvents",
    "DDiscFormat2EraseEvents",
    "DDiscFormat2RawCDEvents",
    "DDiscFormat2TrackAtOnceEvents",
    "DDiscMaster2Events",
    "DFileSystemImageEvents",
    "DFileSystemImageImportEvents",
    "DISC_RECORDER_STATE_FLAGS",
    "DISPID_DDISCFORMAT2DATAEVENTS_UPDATE",
    "DISPID_DDISCFORMAT2RAWCDEVENTS_UPDATE",
    "DISPID_DDISCFORMAT2TAOEVENTS_UPDATE",
    "DISPID_DDISCMASTER2EVENTS_DEVICEADDED",
    "DISPID_DDISCMASTER2EVENTS_DEVICEREMOVED",
    "DISPID_DFILESYSTEMIMAGEEVENTS_UPDATE",
    "DISPID_DFILESYSTEMIMAGEIMPORTEVENTS_UPDATEIMPORT",
    "DISPID_DWRITEENGINE2EVENTS_UPDATE",
    "DISPID_IBLOCKRANGELIST_BLOCKRANGES",
    "DISPID_IBLOCKRANGE_ENDLBA",
    "DISPID_IBLOCKRANGE_STARTLBA",
    "DISPID_IDISCFORMAT2DATAEVENTARGS_CURRENTACTION",
    "DISPID_IDISCFORMAT2DATAEVENTARGS_ELAPSEDTIME",
    "DISPID_IDISCFORMAT2DATAEVENTARGS_ESTIMATEDREMAININGTIME",
    "DISPID_IDISCFORMAT2DATAEVENTARGS_ESTIMATEDTOTALTIME",
    "DISPID_IDISCFORMAT2DATA_BUFFERUNDERRUNFREEDISABLED",
    "DISPID_IDISCFORMAT2DATA_CANCELWRITE",
    "DISPID_IDISCFORMAT2DATA_CLIENTNAME",
    "DISPID_IDISCFORMAT2DATA_CURRENTMEDIASTATUS",
    "DISPID_IDISCFORMAT2DATA_CURRENTMEDIATYPE",
    "DISPID_IDISCFORMAT2DATA_CURRENTROTATIONTYPEISPURECAV",
    "DISPID_IDISCFORMAT2DATA_CURRENTWRITESPEED",
    "DISPID_IDISCFORMAT2DATA_DISABLEDVDCOMPATIBILITYMODE",
    "DISPID_IDISCFORMAT2DATA_FORCEMEDIATOBECLOSED",
    "DISPID_IDISCFORMAT2DATA_FORCEOVERWRITE",
    "DISPID_IDISCFORMAT2DATA_FREESECTORS",
    "DISPID_IDISCFORMAT2DATA_LASTSECTOROFPREVIOUSSESSION",
    "DISPID_IDISCFORMAT2DATA_MUTLISESSIONINTERFACES",
    "DISPID_IDISCFORMAT2DATA_NEXTWRITABLEADDRESS",
    "DISPID_IDISCFORMAT2DATA_POSTGAPALREADYINIMAGE",
    "DISPID_IDISCFORMAT2DATA_RECORDER",
    "DISPID_IDISCFORMAT2DATA_REQUESTEDROTATIONTYPEISPURECAV",
    "DISPID_IDISCFORMAT2DATA_REQUESTEDWRITESPEED",
    "DISPID_IDISCFORMAT2DATA_SETWRITESPEED",
    "DISPID_IDISCFORMAT2DATA_STARTSECTOROFPREVIOUSSESSION",
    "DISPID_IDISCFORMAT2DATA_SUPPORTEDWRITESPEEDDESCRIPTORS",
    "DISPID_IDISCFORMAT2DATA_SUPPORTEDWRITESPEEDS",
    "DISPID_IDISCFORMAT2DATA_TOTALSECTORS",
    "DISPID_IDISCFORMAT2DATA_WRITE",
    "DISPID_IDISCFORMAT2DATA_WRITEPROTECTSTATUS",
    "DISPID_IDISCFORMAT2ERASEEVENTS_UPDATE",
    "DISPID_IDISCFORMAT2ERASE_CLIENTNAME",
    "DISPID_IDISCFORMAT2ERASE_ERASEMEDIA",
    "DISPID_IDISCFORMAT2ERASE_FULLERASE",
    "DISPID_IDISCFORMAT2ERASE_MEDIATYPE",
    "DISPID_IDISCFORMAT2ERASE_RECORDER",
    "DISPID_IDISCFORMAT2RAWCDEVENTARGS_CURRENTACTION",
    "DISPID_IDISCFORMAT2RAWCDEVENTARGS_CURRENTTRACKNUMBER",
    "DISPID_IDISCFORMAT2RAWCDEVENTARGS_ELAPSEDTIME",
    "DISPID_IDISCFORMAT2RAWCDEVENTARGS_ESTIMATEDREMAININGTIME",
    "DISPID_IDISCFORMAT2RAWCDEVENTARGS_ESTIMATEDTOTALTIME",
    "DISPID_IDISCFORMAT2RAWCD_BUFFERUNDERRUNFREEDISABLED",
    "DISPID_IDISCFORMAT2RAWCD_CANCELWRITE",
    "DISPID_IDISCFORMAT2RAWCD_CLIENTNAME",
    "DISPID_IDISCFORMAT2RAWCD_CURRENTMEDIATYPE",
    "DISPID_IDISCFORMAT2RAWCD_CURRENTROTATIONTYPEISPURECAV",
    "DISPID_IDISCFORMAT2RAWCD_CURRENTWRITESPEED",
    "DISPID_IDISCFORMAT2RAWCD_LASTPOSSIBLESTARTOFLEADOUT",
    "DISPID_IDISCFORMAT2RAWCD_PREPAREMEDIA",
    "DISPID_IDISCFORMAT2RAWCD_RECORDER",
    "DISPID_IDISCFORMAT2RAWCD_RELEASEMEDIA",
    "DISPID_IDISCFORMAT2RAWCD_REQUESTEDDATASECTORTYPE",
    "DISPID_IDISCFORMAT2RAWCD_REQUESTEDROTATIONTYPEISPURECAV",
    "DISPID_IDISCFORMAT2RAWCD_REQUESTEDWRITESPEED",
    "DISPID_IDISCFORMAT2RAWCD_SETWRITESPEED",
    "DISPID_IDISCFORMAT2RAWCD_STARTOFNEXTSESSION",
    "DISPID_IDISCFORMAT2RAWCD_SUPPORTEDDATASECTORTYPES",
    "DISPID_IDISCFORMAT2RAWCD_SUPPORTEDWRITESPEEDDESCRIPTORS",
    "DISPID_IDISCFORMAT2RAWCD_SUPPORTEDWRITESPEEDS",
    "DISPID_IDISCFORMAT2RAWCD_WRITEMEDIA",
    "DISPID_IDISCFORMAT2RAWCD_WRITEMEDIAWITHVALIDATION",
    "DISPID_IDISCFORMAT2TAOEVENTARGS_CURRENTACTION",
    "DISPID_IDISCFORMAT2TAOEVENTARGS_CURRENTTRACKNUMBER",
    "DISPID_IDISCFORMAT2TAOEVENTARGS_ELAPSEDTIME",
    "DISPID_IDISCFORMAT2TAOEVENTARGS_ESTIMATEDREMAININGTIME",
    "DISPID_IDISCFORMAT2TAOEVENTARGS_ESTIMATEDTOTALTIME",
    "DISPID_IDISCFORMAT2TAO_ADDAUDIOTRACK",
    "DISPID_IDISCFORMAT2TAO_BUFFERUNDERRUNFREEDISABLED",
    "DISPID_IDISCFORMAT2TAO_CANCELADDTRACK",
    "DISPID_IDISCFORMAT2TAO_CLIENTNAME",
    "DISPID_IDISCFORMAT2TAO_CURRENTMEDIATYPE",
    "DISPID_IDISCFORMAT2TAO_CURRENTROTATIONTYPEISPURECAV",
    "DISPID_IDISCFORMAT2TAO_CURRENTWRITESPEED",
    "DISPID_IDISCFORMAT2TAO_DONOTFINALIZEMEDIA",
    "DISPID_IDISCFORMAT2TAO_EXPECTEDTABLEOFCONTENTS",
    "DISPID_IDISCFORMAT2TAO_FINISHMEDIA",
    "DISPID_IDISCFORMAT2TAO_FREESECTORSONMEDIA",
    "DISPID_IDISCFORMAT2TAO_NUMBEROFEXISTINGTRACKS",
    "DISPID_IDISCFORMAT2TAO_PREPAREMEDIA",
    "DISPID_IDISCFORMAT2TAO_RECORDER",
    "DISPID_IDISCFORMAT2TAO_REQUESTEDROTATIONTYPEISPURECAV",
    "DISPID_IDISCFORMAT2TAO_REQUESTEDWRITESPEED",
    "DISPID_IDISCFORMAT2TAO_SETWRITESPEED",
    "DISPID_IDISCFORMAT2TAO_SUPPORTEDWRITESPEEDDESCRIPTORS",
    "DISPID_IDISCFORMAT2TAO_SUPPORTEDWRITESPEEDS",
    "DISPID_IDISCFORMAT2TAO_TOTALSECTORSONMEDIA",
    "DISPID_IDISCFORMAT2TAO_USEDSECTORSONMEDIA",
    "DISPID_IDISCFORMAT2_MEDIAHEURISTICALLYBLANK",
    "DISPID_IDISCFORMAT2_MEDIAPHYSICALLYBLANK",
    "DISPID_IDISCFORMAT2_MEDIASUPPORTED",
    "DISPID_IDISCFORMAT2_RECORDERSUPPORTED",
    "DISPID_IDISCFORMAT2_SUPPORTEDMEDIATYPES",
    "DISPID_IDISCRECORDER2_ACQUIREEXCLUSIVEACCESS",
    "DISPID_IDISCRECORDER2_ACTIVEDISCRECORDER",
    "DISPID_IDISCRECORDER2_CLOSETRAY",
    "DISPID_IDISCRECORDER2_CURRENTFEATUREPAGES",
    "DISPID_IDISCRECORDER2_CURRENTPROFILES",
    "DISPID_IDISCRECORDER2_DEVICECANLOADMEDIA",
    "DISPID_IDISCRECORDER2_DISABLEMCN",
    "DISPID_IDISCRECORDER2_EJECTMEDIA",
    "DISPID_IDISCRECORDER2_ENABLEMCN",
    "DISPID_IDISCRECORDER2_EXCLUSIVEACCESSOWNER",
    "DISPID_IDISCRECORDER2_INITIALIZEDISCRECORDER",
    "DISPID_IDISCRECORDER2_LEGACYDEVICENUMBER",
    "DISPID_IDISCRECORDER2_PRODUCTID",
    "DISPID_IDISCRECORDER2_PRODUCTREVISION",
    "DISPID_IDISCRECORDER2_RELEASEEXCLUSIVEACCESS",
    "DISPID_IDISCRECORDER2_SUPPORTEDFEATUREPAGES",
    "DISPID_IDISCRECORDER2_SUPPORTEDMODEPAGES",
    "DISPID_IDISCRECORDER2_SUPPORTEDPROFILES",
    "DISPID_IDISCRECORDER2_VENDORID",
    "DISPID_IDISCRECORDER2_VOLUMENAME",
    "DISPID_IDISCRECORDER2_VOLUMEPATHNAMES",
    "DISPID_IMULTISESSION_FIRSTDATASESSION",
    "DISPID_IMULTISESSION_FREESECTORS",
    "DISPID_IMULTISESSION_IMPORTRECORDER",
    "DISPID_IMULTISESSION_INUSE",
    "DISPID_IMULTISESSION_LASTSECTOROFPREVIOUSSESSION",
    "DISPID_IMULTISESSION_LASTWRITTENADDRESS",
    "DISPID_IMULTISESSION_NEXTWRITABLEADDRESS",
    "DISPID_IMULTISESSION_SECTORSONMEDIA",
    "DISPID_IMULTISESSION_STARTSECTOROFPREVIOUSSESSION",
    "DISPID_IMULTISESSION_SUPPORTEDONCURRENTMEDIA",
    "DISPID_IMULTISESSION_WRITEUNITSIZE",
    "DISPID_IRAWCDIMAGECREATOR_ADDSPECIALPREGAP",
    "DISPID_IRAWCDIMAGECREATOR_ADDSUBCODERWGENERATOR",
    "DISPID_IRAWCDIMAGECREATOR_ADDTRACK",
    "DISPID_IRAWCDIMAGECREATOR_CREATERESULTIMAGE",
    "DISPID_IRAWCDIMAGECREATOR_DISABLEGAPLESSAUDIO",
    "DISPID_IRAWCDIMAGECREATOR_EXPECTEDTABLEOFCONTENTS",
    "DISPID_IRAWCDIMAGECREATOR_MEDIACATALOGNUMBER",
    "DISPID_IRAWCDIMAGECREATOR_NUMBEROFEXISTINGTRACKS",
    "DISPID_IRAWCDIMAGECREATOR_RESULTINGIMAGETYPE",
    "DISPID_IRAWCDIMAGECREATOR_STARTINGTRACKNUMBER",
    "DISPID_IRAWCDIMAGECREATOR_STARTOFLEADOUT",
    "DISPID_IRAWCDIMAGECREATOR_STARTOFLEADOUTLIMIT",
    "DISPID_IRAWCDIMAGECREATOR_TRACKINFO",
    "DISPID_IRAWCDIMAGECREATOR_USEDSECTORSONDISC",
    "DISPID_IRAWCDTRACKINFO_AUDIOHASPREEMPHASIS",
    "DISPID_IRAWCDTRACKINFO_DIGITALAUDIOCOPYSETTING",
    "DISPID_IRAWCDTRACKINFO_ISRC",
    "DISPID_IRAWCDTRACKINFO_SECTORCOUNT",
    "DISPID_IRAWCDTRACKINFO_SECTORTYPE",
    "DISPID_IRAWCDTRACKINFO_STARTINGLBA",
    "DISPID_IRAWCDTRACKINFO_TRACKNUMBER",
    "DISPID_IWRITEENGINE2EVENTARGS_FREESYSTEMBUFFER",
    "DISPID_IWRITEENGINE2EVENTARGS_LASTREADLBA",
    "DISPID_IWRITEENGINE2EVENTARGS_LASTWRITTENLBA",
    "DISPID_IWRITEENGINE2EVENTARGS_SECTORCOUNT",
    "DISPID_IWRITEENGINE2EVENTARGS_STARTLBA",
    "DISPID_IWRITEENGINE2EVENTARGS_TOTALDEVICEBUFFER",
    "DISPID_IWRITEENGINE2EVENTARGS_TOTALSYSTEMBUFFER",
    "DISPID_IWRITEENGINE2EVENTARGS_USEDDEVICEBUFFER",
    "DISPID_IWRITEENGINE2EVENTARGS_USEDSYSTEMBUFFER",
    "DISPID_IWRITEENGINE2_BYTESPERSECTOR",
    "DISPID_IWRITEENGINE2_CANCELWRITE",
    "DISPID_IWRITEENGINE2_DISCRECORDER",
    "DISPID_IWRITEENGINE2_ENDINGSECTORSPERSECOND",
    "DISPID_IWRITEENGINE2_STARTINGSECTORSPERSECOND",
    "DISPID_IWRITEENGINE2_USESTREAMINGWRITE12",
    "DISPID_IWRITEENGINE2_WRITEINPROGRESS",
    "DISPID_IWRITEENGINE2_WRITESECTION",
    "DWriteEngine2Events",
    "EmulationType",
    "EmulationType_Emulation12MFloppy",
    "EmulationType_Emulation144MFloppy",
    "EmulationType_Emulation288MFloppy",
    "EmulationType_EmulationHardDisk",
    "EmulationType_EmulationNone",
    "EnumFsiItems",
    "EnumProgressItems",
    "FileSystemImageResult",
    "FsiDirectoryItem",
    "FsiFileItem",
    "FsiFileSystems",
    "FsiFileSystems_FsiFileSystemISO9660",
    "FsiFileSystems_FsiFileSystemJoliet",
    "FsiFileSystems_FsiFileSystemNone",
    "FsiFileSystems_FsiFileSystemUDF",
    "FsiFileSystems_FsiFileSystemUnknown",
    "FsiItemType",
    "FsiItemType_FsiItemDirectory",
    "FsiItemType_FsiItemFile",
    "FsiItemType_FsiItemNotFound",
    "FsiNamedStreams",
    "FsiStream",
    "GUID_SMTPSVC_SOURCE",
    "GUID_SMTP_SOURCE_TYPE",
    "GetAttribIMsgOnIStg",
    "IBlockRange",
    "IBlockRangeList",
    "IBootOptions",
    "IBurnVerification",
    "IDiscFormat2",
    "IDiscFormat2Data",
    "IDiscFormat2DataEventArgs",
    "IDiscFormat2Erase",
    "IDiscFormat2RawCD",
    "IDiscFormat2RawCDEventArgs",
    "IDiscFormat2TrackAtOnce",
    "IDiscFormat2TrackAtOnceEventArgs",
    "IDiscMaster",
    "IDiscMaster2",
    "IDiscMasterProgressEvents",
    "IDiscRecorder",
    "IDiscRecorder2",
    "IDiscRecorder2Ex",
    "IEnumDiscMasterFormats",
    "IEnumDiscRecorders",
    "IEnumFsiItems",
    "IEnumProgressItems",
    "IFileSystemImage",
    "IFileSystemImage2",
    "IFileSystemImage3",
    "IFileSystemImageResult",
    "IFileSystemImageResult2",
    "IFsiDirectoryItem",
    "IFsiDirectoryItem2",
    "IFsiFileItem",
    "IFsiFileItem2",
    "IFsiItem",
    "IFsiNamedStreams",
    "IIsoImageManager",
    "IJolietDiscMaster",
    "IMAPI2FS_BOOT_ENTRY_COUNT_MAX",
    "IMAPI2FS_FullVersion_STR",
    "IMAPI2FS_FullVersion_WSTR",
    "IMAPI2FS_MajorVersion",
    "IMAPI2FS_MinorVersion",
    "IMAPI2_DEFAULT_COMMAND_TIMEOUT",
    "IMAPILib2_MajorVersion",
    "IMAPILib2_MinorVersion",
    "IMAPI_BURN_VERIFICATION_FULL",
    "IMAPI_BURN_VERIFICATION_LEVEL",
    "IMAPI_BURN_VERIFICATION_NONE",
    "IMAPI_BURN_VERIFICATION_QUICK",
    "IMAPI_CD_SECTOR_AUDIO",
    "IMAPI_CD_SECTOR_MODE1",
    "IMAPI_CD_SECTOR_MODE1RAW",
    "IMAPI_CD_SECTOR_MODE2FORM0",
    "IMAPI_CD_SECTOR_MODE2FORM0RAW",
    "IMAPI_CD_SECTOR_MODE2FORM1",
    "IMAPI_CD_SECTOR_MODE2FORM1RAW",
    "IMAPI_CD_SECTOR_MODE2FORM2",
    "IMAPI_CD_SECTOR_MODE2FORM2RAW",
    "IMAPI_CD_SECTOR_MODE_ZERO",
    "IMAPI_CD_SECTOR_TYPE",
    "IMAPI_CD_TRACK_DIGITAL_COPY_PERMITTED",
    "IMAPI_CD_TRACK_DIGITAL_COPY_PROHIBITED",
    "IMAPI_CD_TRACK_DIGITAL_COPY_SCMS",
    "IMAPI_CD_TRACK_DIGITAL_COPY_SETTING",
    "IMAPI_E_ALREADYOPEN",
    "IMAPI_E_BADJOLIETNAME",
    "IMAPI_E_BOOTIMAGE_AND_NONBLANK_DISC",
    "IMAPI_E_CANNOT_WRITE_TO_MEDIA",
    "IMAPI_E_COMPRESSEDSTASH",
    "IMAPI_E_DEVICE_INVALIDTYPE",
    "IMAPI_E_DEVICE_NOPROPERTIES",
    "IMAPI_E_DEVICE_NOTACCESSIBLE",
    "IMAPI_E_DEVICE_NOTPRESENT",
    "IMAPI_E_DEVICE_STILL_IN_USE",
    "IMAPI_E_DISCFULL",
    "IMAPI_E_DISCINFO",
    "IMAPI_E_ENCRYPTEDSTASH",
    "IMAPI_E_FILEACCESS",
    "IMAPI_E_FILEEXISTS",
    "IMAPI_E_FILESYSTEM",
    "IMAPI_E_GENERIC",
    "IMAPI_E_INITIALIZE_ENDWRITE",
    "IMAPI_E_INITIALIZE_WRITE",
    "IMAPI_E_INVALIDIMAGE",
    "IMAPI_E_LOSS_OF_STREAMING",
    "IMAPI_E_MEDIUM_INVALIDTYPE",
    "IMAPI_E_MEDIUM_NOTPRESENT",
    "IMAPI_E_NOACTIVEFORMAT",
    "IMAPI_E_NOACTIVERECORDER",
    "IMAPI_E_NOTENOUGHDISKFORSTASH",
    "IMAPI_E_NOTINITIALIZED",
    "IMAPI_E_NOTOPENED",
    "IMAPI_E_REMOVABLESTASH",
    "IMAPI_E_STASHINUSE",
    "IMAPI_E_TRACKNOTOPEN",
    "IMAPI_E_TRACKOPEN",
    "IMAPI_E_TRACK_NOT_BIG_ENOUGH",
    "IMAPI_E_USERABORT",
    "IMAPI_E_WRONGDISC",
    "IMAPI_E_WRONGFORMAT",
    "IMAPI_FEATURE_PAGE_TYPE",
    "IMAPI_FEATURE_PAGE_TYPE_AACS",
    "IMAPI_FEATURE_PAGE_TYPE_BD_PSEUDO_OVERWRITE",
    "IMAPI_FEATURE_PAGE_TYPE_BD_READ",
    "IMAPI_FEATURE_PAGE_TYPE_BD_WRITE",
    "IMAPI_FEATURE_PAGE_TYPE_CDRW_CAV_WRITE",
    "IMAPI_FEATURE_PAGE_TYPE_CD_ANALOG_PLAY",
    "IMAPI_FEATURE_PAGE_TYPE_CD_MASTERING",
    "IMAPI_FEATURE_PAGE_TYPE_CD_MULTIREAD",
    "IMAPI_FEATURE_PAGE_TYPE_CD_READ",
    "IMAPI_FEATURE_PAGE_TYPE_CD_RW_MEDIA_WRITE_SUPPORT",
    "IMAPI_FEATURE_PAGE_TYPE_CD_TRACK_AT_ONCE",
    "IMAPI_FEATURE_PAGE_TYPE_CORE",
    "IMAPI_FEATURE_PAGE_TYPE_DISC_CONTROL_BLOCKS",
    "IMAPI_FEATURE_PAGE_TYPE_DOUBLE_DENSITY_CD_READ",
    "IMAPI_FEATURE_PAGE_TYPE_DOUBLE_DENSITY_CD_RW_WRITE",
    "IMAPI_FEATURE_PAGE_TYPE_DOUBLE_DENSITY_CD_R_WRITE",
    "IMAPI_FEATURE_PAGE_TYPE_DVD_CPRM",
    "IMAPI_FEATURE_PAGE_TYPE_DVD_CSS",
    "IMAPI_FEATURE_PAGE_TYPE_DVD_DASH_WRITE",
    "IMAPI_FEATURE_PAGE_TYPE_DVD_PLUS_R",
    "IMAPI_FEATURE_PAGE_TYPE_DVD_PLUS_RW",
    "IMAPI_FEATURE_PAGE_TYPE_DVD_PLUS_R_DUAL_LAYER",
    "IMAPI_FEATURE_PAGE_TYPE_DVD_READ",
    "IMAPI_FEATURE_PAGE_TYPE_EMBEDDED_CHANGER",
    "IMAPI_FEATURE_PAGE_TYPE_ENHANCED_DEFECT_REPORTING",
    "IMAPI_FEATURE_PAGE_TYPE_FIRMWARE_INFORMATION",
    "IMAPI_FEATURE_PAGE_TYPE_FORMATTABLE",
    "IMAPI_FEATURE_PAGE_TYPE_HARDWARE_DEFECT_MANAGEMENT",
    "IMAPI_FEATURE_PAGE_TYPE_HD_DVD_READ",
    "IMAPI_FEATURE_PAGE_TYPE_HD_DVD_WRITE",
    "IMAPI_FEATURE_PAGE_TYPE_INCREMENTAL_STREAMING_WRITABLE",
    "IMAPI_FEATURE_PAGE_TYPE_LAYER_JUMP_RECORDING",
    "IMAPI_FEATURE_PAGE_TYPE_LOGICAL_UNIT_SERIAL_NUMBER",
    "IMAPI_FEATURE_PAGE_TYPE_MEDIA_SERIAL_NUMBER",
    "IMAPI_FEATURE_PAGE_TYPE_MICROCODE_UPDATE",
    "IMAPI_FEATURE_PAGE_TYPE_MORPHING",
    "IMAPI_FEATURE_PAGE_TYPE_MRW",
    "IMAPI_FEATURE_PAGE_TYPE_POWER_MANAGEMENT",
    "IMAPI_FEATURE_PAGE_TYPE_PROFILE_LIST",
    "IMAPI_FEATURE_PAGE_TYPE_RANDOMLY_READABLE",
    "IMAPI_FEATURE_PAGE_TYPE_RANDOMLY_WRITABLE",
    "IMAPI_FEATURE_PAGE_TYPE_REAL_TIME_STREAMING",
    "IMAPI_FEATURE_PAGE_TYPE_REMOVABLE_MEDIUM",
    "IMAPI_FEATURE_PAGE_TYPE_RESTRICTED_OVERWRITE",
    "IMAPI_FEATURE_PAGE_TYPE_RIGID_RESTRICTED_OVERWRITE",
    "IMAPI_FEATURE_PAGE_TYPE_SECTOR_ERASABLE",
    "IMAPI_FEATURE_PAGE_TYPE_SMART",
    "IMAPI_FEATURE_PAGE_TYPE_TIMEOUT",
    "IMAPI_FEATURE_PAGE_TYPE_VCPS",
    "IMAPI_FEATURE_PAGE_TYPE_WRITE_ONCE",
    "IMAPI_FEATURE_PAGE_TYPE_WRITE_PROTECT",
    "IMAPI_FORMAT2_DATA_MEDIA_STATE",
    "IMAPI_FORMAT2_DATA_MEDIA_STATE_APPENDABLE",
    "IMAPI_FORMAT2_DATA_MEDIA_STATE_BLANK",
    "IMAPI_FORMAT2_DATA_MEDIA_STATE_DAMAGED",
    "IMAPI_FORMAT2_DATA_MEDIA_STATE_ERASE_REQUIRED",
    "IMAPI_FORMAT2_DATA_MEDIA_STATE_FINALIZED",
    "IMAPI_FORMAT2_DATA_MEDIA_STATE_FINAL_SESSION",
    "IMAPI_FORMAT2_DATA_MEDIA_STATE_INFORMATIONAL_MASK",
    "IMAPI_FORMAT2_DATA_MEDIA_STATE_NON_EMPTY_SESSION",
    "IMAPI_FORMAT2_DATA_MEDIA_STATE_OVERWRITE_ONLY",
    "IMAPI_FORMAT2_DATA_MEDIA_STATE_RANDOMLY_WRITABLE",
    "IMAPI_FORMAT2_DATA_MEDIA_STATE_UNKNOWN",
    "IMAPI_FORMAT2_DATA_MEDIA_STATE_UNSUPPORTED_MASK",
    "IMAPI_FORMAT2_DATA_MEDIA_STATE_UNSUPPORTED_MEDIA",
    "IMAPI_FORMAT2_DATA_MEDIA_STATE_WRITE_PROTECTED",
    "IMAPI_FORMAT2_DATA_WRITE_ACTION",
    "IMAPI_FORMAT2_DATA_WRITE_ACTION_CALIBRATING_POWER",
    "IMAPI_FORMAT2_DATA_WRITE_ACTION_COMPLETED",
    "IMAPI_FORMAT2_DATA_WRITE_ACTION_FINALIZATION",
    "IMAPI_FORMAT2_DATA_WRITE_ACTION_FORMATTING_MEDIA",
    "IMAPI_FORMAT2_DATA_WRITE_ACTION_INITIALIZING_HARDWARE",
    "IMAPI_FORMAT2_DATA_WRITE_ACTION_VALIDATING_MEDIA",
    "IMAPI_FORMAT2_DATA_WRITE_ACTION_VERIFYING",
    "IMAPI_FORMAT2_DATA_WRITE_ACTION_WRITING_DATA",
    "IMAPI_FORMAT2_RAW_CD_DATA_SECTOR_TYPE",
    "IMAPI_FORMAT2_RAW_CD_SUBCODE_IS_COOKED",
    "IMAPI_FORMAT2_RAW_CD_SUBCODE_IS_RAW",
    "IMAPI_FORMAT2_RAW_CD_SUBCODE_PQ_ONLY",
    "IMAPI_FORMAT2_RAW_CD_WRITE_ACTION",
    "IMAPI_FORMAT2_RAW_CD_WRITE_ACTION_FINISHING",
    "IMAPI_FORMAT2_RAW_CD_WRITE_ACTION_PREPARING",
    "IMAPI_FORMAT2_RAW_CD_WRITE_ACTION_UNKNOWN",
    "IMAPI_FORMAT2_RAW_CD_WRITE_ACTION_WRITING",
    "IMAPI_FORMAT2_TAO_WRITE_ACTION",
    "IMAPI_FORMAT2_TAO_WRITE_ACTION_FINISHING",
    "IMAPI_FORMAT2_TAO_WRITE_ACTION_PREPARING",
    "IMAPI_FORMAT2_TAO_WRITE_ACTION_UNKNOWN",
    "IMAPI_FORMAT2_TAO_WRITE_ACTION_VERIFYING",
    "IMAPI_FORMAT2_TAO_WRITE_ACTION_WRITING",
    "IMAPI_MEDIA_PHYSICAL_TYPE",
    "IMAPI_MEDIA_TYPE_BDR",
    "IMAPI_MEDIA_TYPE_BDRE",
    "IMAPI_MEDIA_TYPE_BDROM",
    "IMAPI_MEDIA_TYPE_CDR",
    "IMAPI_MEDIA_TYPE_CDROM",
    "IMAPI_MEDIA_TYPE_CDRW",
    "IMAPI_MEDIA_TYPE_DISK",
    "IMAPI_MEDIA_TYPE_DVDDASHR",
    "IMAPI_MEDIA_TYPE_DVDDASHRW",
    "IMAPI_MEDIA_TYPE_DVDDASHR_DUALLAYER",
    "IMAPI_MEDIA_TYPE_DVDPLUSR",
    "IMAPI_MEDIA_TYPE_DVDPLUSRW",
    "IMAPI_MEDIA_TYPE_DVDPLUSRW_DUALLAYER",
    "IMAPI_MEDIA_TYPE_DVDPLUSR_DUALLAYER",
    "IMAPI_MEDIA_TYPE_DVDRAM",
    "IMAPI_MEDIA_TYPE_DVDROM",
    "IMAPI_MEDIA_TYPE_HDDVDR",
    "IMAPI_MEDIA_TYPE_HDDVDRAM",
    "IMAPI_MEDIA_TYPE_HDDVDROM",
    "IMAPI_MEDIA_TYPE_MAX",
    "IMAPI_MEDIA_TYPE_UNKNOWN",
    "IMAPI_MEDIA_WRITE_PROTECT_STATE",
    "IMAPI_MODE_PAGE_REQUEST_TYPE",
    "IMAPI_MODE_PAGE_REQUEST_TYPE_CHANGEABLE_VALUES",
    "IMAPI_MODE_PAGE_REQUEST_TYPE_CURRENT_VALUES",
    "IMAPI_MODE_PAGE_REQUEST_TYPE_DEFAULT_VALUES",
    "IMAPI_MODE_PAGE_REQUEST_TYPE_SAVED_VALUES",
    "IMAPI_MODE_PAGE_TYPE",
    "IMAPI_MODE_PAGE_TYPE_CACHING",
    "IMAPI_MODE_PAGE_TYPE_INFORMATIONAL_EXCEPTIONS",
    "IMAPI_MODE_PAGE_TYPE_LEGACY_CAPABILITIES",
    "IMAPI_MODE_PAGE_TYPE_MRW",
    "IMAPI_MODE_PAGE_TYPE_POWER_CONDITION",
    "IMAPI_MODE_PAGE_TYPE_READ_WRITE_ERROR_RECOVERY",
    "IMAPI_MODE_PAGE_TYPE_TIMEOUT_AND_PROTECT",
    "IMAPI_MODE_PAGE_TYPE_WRITE_PARAMETERS",
    "IMAPI_PROFILE_TYPE",
    "IMAPI_PROFILE_TYPE_AS_MO",
    "IMAPI_PROFILE_TYPE_BD_REWRITABLE",
    "IMAPI_PROFILE_TYPE_BD_ROM",
    "IMAPI_PROFILE_TYPE_BD_R_RANDOM_RECORDING",
    "IMAPI_PROFILE_TYPE_BD_R_SEQUENTIAL",
    "IMAPI_PROFILE_TYPE_CDROM",
    "IMAPI_PROFILE_TYPE_CD_RECORDABLE",
    "IMAPI_PROFILE_TYPE_CD_REWRITABLE",
    "IMAPI_PROFILE_TYPE_DDCDROM",
    "IMAPI_PROFILE_TYPE_DDCD_RECORDABLE",
    "IMAPI_PROFILE_TYPE_DDCD_REWRITABLE",
    "IMAPI_PROFILE_TYPE_DVDROM",
    "IMAPI_PROFILE_TYPE_DVD_DASH_RECORDABLE",
    "IMAPI_PROFILE_TYPE_DVD_DASH_REWRITABLE",
    "IMAPI_PROFILE_TYPE_DVD_DASH_RW_SEQUENTIAL",
    "IMAPI_PROFILE_TYPE_DVD_DASH_R_DUAL_LAYER_JUMP",
    "IMAPI_PROFILE_TYPE_DVD_DASH_R_DUAL_SEQUENTIAL",
    "IMAPI_PROFILE_TYPE_DVD_PLUS_R",
    "IMAPI_PROFILE_TYPE_DVD_PLUS_RW",
    "IMAPI_PROFILE_TYPE_DVD_PLUS_RW_DUAL",
    "IMAPI_PROFILE_TYPE_DVD_PLUS_R_DUAL",
    "IMAPI_PROFILE_TYPE_DVD_RAM",
    "IMAPI_PROFILE_TYPE_HD_DVD_RAM",
    "IMAPI_PROFILE_TYPE_HD_DVD_RECORDABLE",
    "IMAPI_PROFILE_TYPE_HD_DVD_ROM",
    "IMAPI_PROFILE_TYPE_INVALID",
    "IMAPI_PROFILE_TYPE_MO_ERASABLE",
    "IMAPI_PROFILE_TYPE_MO_WRITE_ONCE",
    "IMAPI_PROFILE_TYPE_NON_REMOVABLE_DISK",
    "IMAPI_PROFILE_TYPE_NON_STANDARD",
    "IMAPI_PROFILE_TYPE_REMOVABLE_DISK",
    "IMAPI_READ_TRACK_ADDRESS_TYPE",
    "IMAPI_READ_TRACK_ADDRESS_TYPE_LBA",
    "IMAPI_READ_TRACK_ADDRESS_TYPE_SESSION",
    "IMAPI_READ_TRACK_ADDRESS_TYPE_TRACK",
    "IMAPI_SECTORS_PER_SECOND_AT_1X_BD",
    "IMAPI_SECTORS_PER_SECOND_AT_1X_CD",
    "IMAPI_SECTORS_PER_SECOND_AT_1X_DVD",
    "IMAPI_SECTORS_PER_SECOND_AT_1X_HD_DVD",
    "IMAPI_SECTOR_SIZE",
    "IMAPI_S_BUFFER_TO_SMALL",
    "IMAPI_S_PROPERTIESIGNORED",
    "IMAPI_WRITEPROTECTED_BY_CARTRIDGE",
    "IMAPI_WRITEPROTECTED_BY_DISC_CONTROL_BLOCK",
    "IMAPI_WRITEPROTECTED_BY_MEDIA_SPECIFIC_REASON",
    "IMAPI_WRITEPROTECTED_BY_SOFTWARE_WRITE_PROTECT",
    "IMAPI_WRITEPROTECTED_READ_ONLY_MEDIA",
    "IMAPI_WRITEPROTECTED_UNTIL_POWERDOWN",
    "IMMPID_CPV_AFTER__",
    "IMMPID_CPV_BEFORE__",
    "IMMPID_CPV_ENUM",
    "IMMPID_CP_START",
    "IMMPID_MPV_AFTER__",
    "IMMPID_MPV_BEFORE__",
    "IMMPID_MPV_ENUM",
    "IMMPID_MPV_MESSAGE_CREATION_FLAGS",
    "IMMPID_MPV_MESSAGE_OPEN_HANDLES",
    "IMMPID_MPV_STORE_DRIVER_HANDLE",
    "IMMPID_MPV_TOTAL_OPEN_CONTENT_HANDLES",
    "IMMPID_MPV_TOTAL_OPEN_HANDLES",
    "IMMPID_MPV_TOTAL_OPEN_PROPERTY_STREAM_HANDLES",
    "IMMPID_MP_AFTER__",
    "IMMPID_MP_ARRIVAL_FILETIME",
    "IMMPID_MP_ARRIVAL_TIME",
    "IMMPID_MP_AUTHENTICATED_USER_NAME",
    "IMMPID_MP_BEFORE__",
    "IMMPID_MP_BINARYMIME_OPTION",
    "IMMPID_MP_CHUNKING_OPTION",
    "IMMPID_MP_CLIENT_AUTH_TYPE",
    "IMMPID_MP_CLIENT_AUTH_USER",
    "IMMPID_MP_CONNECTION_IP_ADDRESS",
    "IMMPID_MP_CONNECTION_SERVER_IP_ADDRESS",
    "IMMPID_MP_CONNECTION_SERVER_PORT",
    "IMMPID_MP_CONTENT_FILE_NAME",
    "IMMPID_MP_CONTENT_TYPE",
    "IMMPID_MP_CRC_GLOBAL",
    "IMMPID_MP_CRC_RECIPS",
    "IMMPID_MP_DEFERRED_DELIVERY_FILETIME",
    "IMMPID_MP_DOMAIN_LIST",
    "IMMPID_MP_DSN_ENVID_VALUE",
    "IMMPID_MP_DSN_RET_VALUE",
    "IMMPID_MP_EIGHTBIT_MIME_OPTION",
    "IMMPID_MP_ENCRYPTION_TYPE",
    "IMMPID_MP_ENUM",
    "IMMPID_MP_ERROR_CODE",
    "IMMPID_MP_EXPIRE_DELAY",
    "IMMPID_MP_EXPIRE_NDR",
    "IMMPID_MP_FOUND_EMBEDDED_CRLF_DOT_CRLF",
    "IMMPID_MP_FROM_ADDRESS",
    "IMMPID_MP_HELO_DOMAIN",
    "IMMPID_MP_HR_CAT_STATUS",
    "IMMPID_MP_INBOUND_MAIL_FROM_AUTH",
    "IMMPID_MP_LOCAL_EXPIRE_DELAY",
    "IMMPID_MP_LOCAL_EXPIRE_NDR",
    "IMMPID_MP_MESSAGE_STATUS",
    "IMMPID_MP_MSGCLASS",
    "IMMPID_MP_MSG_GUID",
    "IMMPID_MP_MSG_SIZE_HINT",
    "IMMPID_MP_NUM_RECIPIENTS",
    "IMMPID_MP_ORIGINAL_ARRIVAL_TIME",
    "IMMPID_MP_PICKUP_FILE_NAME",
    "IMMPID_MP_RECIPIENT_LIST",
    "IMMPID_MP_REMOTE_AUTHENTICATION_TYPE",
    "IMMPID_MP_REMOTE_SERVER_DSN_CAPABLE",
    "IMMPID_MP_RFC822_BCC_ADDRESS",
    "IMMPID_MP_RFC822_CC_ADDRESS",
    "IMMPID_MP_RFC822_FROM_ADDRESS",
    "IMMPID_MP_RFC822_MSG_ID",
    "IMMPID_MP_RFC822_MSG_SUBJECT",
    "IMMPID_MP_RFC822_TO_ADDRESS",
    "IMMPID_MP_SCANNED_FOR_CRLF_DOT_CRLF",
    "IMMPID_MP_SENDER_ADDRESS",
    "IMMPID_MP_SENDER_ADDRESS_LEGACY_EX_DN",
    "IMMPID_MP_SENDER_ADDRESS_OTHER",
    "IMMPID_MP_SENDER_ADDRESS_SMTP",
    "IMMPID_MP_SENDER_ADDRESS_X400",
    "IMMPID_MP_SENDER_ADDRESS_X500",
    "IMMPID_MP_SERVER_NAME",
    "IMMPID_MP_SERVER_VERSION",
    "IMMPID_MP_SUPERSEDES_MSG_GUID",
    "IMMPID_MP_X_PRIORITY",
    "IMMPID_NMP_AFTER__",
    "IMMPID_NMP_BEFORE__",
    "IMMPID_NMP_ENUM",
    "IMMPID_NMP_HEADERS",
    "IMMPID_NMP_NEWSGROUP_LIST",
    "IMMPID_NMP_NNTP_APPROVED_HEADER",
    "IMMPID_NMP_NNTP_PROCESSING",
    "IMMPID_NMP_POST_TOKEN",
    "IMMPID_NMP_PRIMARY_ARTID",
    "IMMPID_NMP_PRIMARY_GROUP",
    "IMMPID_NMP_SECONDARY_ARTNUM",
    "IMMPID_NMP_SECONDARY_GROUPS",
    "IMMPID_RPV_AFTER__",
    "IMMPID_RPV_BEFORE__",
    "IMMPID_RPV_DONT_DELIVER",
    "IMMPID_RPV_ENUM",
    "IMMPID_RPV_NO_NAME_COLLISIONS",
    "IMMPID_RP_ADDRESS",
    "IMMPID_RP_ADDRESS_OTHER",
    "IMMPID_RP_ADDRESS_SMTP",
    "IMMPID_RP_ADDRESS_TYPE",
    "IMMPID_RP_ADDRESS_TYPE_SMTP",
    "IMMPID_RP_ADDRESS_X400",
    "IMMPID_RP_ADDRESS_X500",
    "IMMPID_RP_AFTER__",
    "IMMPID_RP_BEFORE__",
    "IMMPID_RP_DISPLAY_NAME",
    "IMMPID_RP_DOMAIN",
    "IMMPID_RP_DSN_NOTIFY_INVALID",
    "IMMPID_RP_DSN_NOTIFY_SUCCESS",
    "IMMPID_RP_DSN_NOTIFY_VALUE",
    "IMMPID_RP_DSN_ORCPT_VALUE",
    "IMMPID_RP_DSN_PRE_CAT_ADDRESS",
    "IMMPID_RP_ENUM",
    "IMMPID_RP_ERROR_CODE",
    "IMMPID_RP_ERROR_STRING",
    "IMMPID_RP_LEGACY_EX_DN",
    "IMMPID_RP_MDB_GUID",
    "IMMPID_RP_RECIPIENT_FLAGS",
    "IMMPID_RP_SMTP_STATUS_STRING",
    "IMMPID_RP_USER_GUID",
    "IMMP_MPV_STORE_DRIVER_HANDLE",
    "IMultisession",
    "IMultisessionRandomWrite",
    "IMultisessionSequential",
    "IMultisessionSequential2",
    "IProgressItem",
    "IProgressItems",
    "IRawCDImageCreator",
    "IRawCDImageTrackInfo",
    "IRedbookDiscMaster",
    "IStreamConcatenate",
    "IStreamInterleave",
    "IStreamPseudoRandomBased",
    "IWriteEngine2",
    "IWriteEngine2EventArgs",
    "IWriteSpeedDescriptor",
    "MEDIA_BLANK",
    "MEDIA_CDDA_CDROM",
    "MEDIA_CD_EXTRA",
    "MEDIA_CD_I",
    "MEDIA_CD_OTHER",
    "MEDIA_CD_ROM_XA",
    "MEDIA_FLAGS",
    "MEDIA_FORMAT_UNUSABLE_BY_IMAPI",
    "MEDIA_RW",
    "MEDIA_SPECIAL",
    "MEDIA_TYPES",
    "MEDIA_WRITABLE",
    "MPV_INBOUND_CUTOFF_EXCEEDED",
    "MPV_WRITE_CONTENT",
    "MP_MSGCLASS_DELIVERY_REPORT",
    "MP_MSGCLASS_NONDELIVERY_REPORT",
    "MP_MSGCLASS_REPLICATION",
    "MP_MSGCLASS_SYSTEM",
    "MP_STATUS_ABANDON_DELIVERY",
    "MP_STATUS_ABORT_DELIVERY",
    "MP_STATUS_BAD_MAIL",
    "MP_STATUS_CATEGORIZED",
    "MP_STATUS_RETRY",
    "MP_STATUS_SUBMITTED",
    "MP_STATUS_SUCCESS",
    "MSDiscMasterObj",
    "MSDiscRecorderObj",
    "MSEnumDiscRecordersObj",
    "MSGCALLRELEASE",
    "MapStorageSCode",
    "MsftDiscFormat2Data",
    "MsftDiscFormat2Erase",
    "MsftDiscFormat2RawCD",
    "MsftDiscFormat2TrackAtOnce",
    "MsftDiscMaster2",
    "MsftDiscRecorder2",
    "MsftFileSystemImage",
    "MsftIsoImageManager",
    "MsftMultisessionRandomWrite",
    "MsftMultisessionSequential",
    "MsftRawCDImageCreator",
    "MsftStreamConcatenate",
    "MsftStreamInterleave",
    "MsftStreamPrng001",
    "MsftStreamZero",
    "MsftWriteEngine2",
    "MsftWriteSpeedDescriptor",
    "NMP_PROCESS_CONTROL",
    "NMP_PROCESS_MODERATOR",
    "NMP_PROCESS_POST",
    "OpenIMsgOnIStg",
    "OpenIMsgSession",
    "PlatformId",
    "PlatformId_PlatformEFI",
    "PlatformId_PlatformMac",
    "PlatformId_PlatformPowerPC",
    "PlatformId_PlatformX86",
    "ProgressItem",
    "ProgressItems",
    "RECORDER_BURNING",
    "RECORDER_CDR",
    "RECORDER_CDRW",
    "RECORDER_DOING_NOTHING",
    "RECORDER_OPENED",
    "RECORDER_TYPES",
    "RP_DELIVERED",
    "RP_DSN_HANDLED",
    "RP_DSN_NOTIFY_DELAY",
    "RP_DSN_NOTIFY_FAILURE",
    "RP_DSN_NOTIFY_INVALID",
    "RP_DSN_NOTIFY_MASK",
    "RP_DSN_NOTIFY_NEVER",
    "RP_DSN_NOTIFY_SUCCESS",
    "RP_DSN_SENT_DELAYED",
    "RP_DSN_SENT_DELIVERED",
    "RP_DSN_SENT_EXPANDED",
    "RP_DSN_SENT_NDR",
    "RP_DSN_SENT_RELAYED",
    "RP_ENPANDED",
    "RP_ERROR_CONTEXT_CAT",
    "RP_ERROR_CONTEXT_MTA",
    "RP_ERROR_CONTEXT_STORE",
    "RP_EXPANDED",
    "RP_FAILED",
    "RP_GENERAL_FAILURE",
    "RP_HANDLED",
    "RP_RECIP_FLAGS_RESERVED",
    "RP_REMOTE_MTA_NO_DSN",
    "RP_UNRESOLVED",
    "RP_VOLATILE_FLAGS_MASK",
    "SPropAttrArray",
    "SZ_PROGID_SMTPCAT",
    "SetAttribIMsgOnIStg",
    "_MSGSESS",
    "tagIMMPID_CPV_STRUCT",
    "tagIMMPID_GUIDLIST_ITEM",
    "tagIMMPID_MPV_STRUCT",
    "tagIMMPID_MP_STRUCT",
    "tagIMMPID_NMP_STRUCT",
    "tagIMMPID_RPV_STRUCT",
    "tagIMMPID_RP_STRUCT",
]
_arch_optional = [
]
