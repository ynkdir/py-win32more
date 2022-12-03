from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
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
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
def _define__MSGSESS_head():
    class _MSGSESS(Structure):
        pass
    return _MSGSESS
def _define__MSGSESS():
    _MSGSESS = win32more.Storage.Imapi._MSGSESS_head
    return _MSGSESS
IMAPI_SECTOR_SIZE = 2048
IMAPI2_DEFAULT_COMMAND_TIMEOUT = 10
DISPID_DDISCMASTER2EVENTS_DEVICEADDED = 256
DISPID_DDISCMASTER2EVENTS_DEVICEREMOVED = 257
DISPID_IDISCRECORDER2_EJECTMEDIA = 256
DISPID_IDISCRECORDER2_CLOSETRAY = 257
DISPID_IDISCRECORDER2_ACQUIREEXCLUSIVEACCESS = 258
DISPID_IDISCRECORDER2_RELEASEEXCLUSIVEACCESS = 259
DISPID_IDISCRECORDER2_DISABLEMCN = 260
DISPID_IDISCRECORDER2_ENABLEMCN = 261
DISPID_IDISCRECORDER2_INITIALIZEDISCRECORDER = 262
DISPID_IDISCRECORDER2_ACTIVEDISCRECORDER = 0
DISPID_IDISCRECORDER2_VENDORID = 513
DISPID_IDISCRECORDER2_PRODUCTID = 514
DISPID_IDISCRECORDER2_PRODUCTREVISION = 515
DISPID_IDISCRECORDER2_VOLUMENAME = 516
DISPID_IDISCRECORDER2_VOLUMEPATHNAMES = 517
DISPID_IDISCRECORDER2_DEVICECANLOADMEDIA = 518
DISPID_IDISCRECORDER2_LEGACYDEVICENUMBER = 519
DISPID_IDISCRECORDER2_SUPPORTEDFEATUREPAGES = 520
DISPID_IDISCRECORDER2_CURRENTFEATUREPAGES = 521
DISPID_IDISCRECORDER2_SUPPORTEDPROFILES = 522
DISPID_IDISCRECORDER2_CURRENTPROFILES = 523
DISPID_IDISCRECORDER2_SUPPORTEDMODEPAGES = 524
DISPID_IDISCRECORDER2_EXCLUSIVEACCESSOWNER = 525
DISPID_IWRITEENGINE2_WRITESECTION = 512
DISPID_IWRITEENGINE2_CANCELWRITE = 513
DISPID_IWRITEENGINE2_DISCRECORDER = 256
DISPID_IWRITEENGINE2_USESTREAMINGWRITE12 = 257
DISPID_IWRITEENGINE2_STARTINGSECTORSPERSECOND = 258
DISPID_IWRITEENGINE2_ENDINGSECTORSPERSECOND = 259
DISPID_IWRITEENGINE2_BYTESPERSECTOR = 260
DISPID_IWRITEENGINE2_WRITEINPROGRESS = 261
DISPID_IWRITEENGINE2EVENTARGS_STARTLBA = 256
DISPID_IWRITEENGINE2EVENTARGS_SECTORCOUNT = 257
DISPID_IWRITEENGINE2EVENTARGS_LASTREADLBA = 258
DISPID_IWRITEENGINE2EVENTARGS_LASTWRITTENLBA = 259
DISPID_IWRITEENGINE2EVENTARGS_TOTALDEVICEBUFFER = 260
DISPID_IWRITEENGINE2EVENTARGS_USEDDEVICEBUFFER = 261
DISPID_IWRITEENGINE2EVENTARGS_TOTALSYSTEMBUFFER = 262
DISPID_IWRITEENGINE2EVENTARGS_USEDSYSTEMBUFFER = 263
DISPID_IWRITEENGINE2EVENTARGS_FREESYSTEMBUFFER = 264
DISPID_DWRITEENGINE2EVENTS_UPDATE = 256
DISPID_IDISCFORMAT2_RECORDERSUPPORTED = 2048
DISPID_IDISCFORMAT2_MEDIASUPPORTED = 2049
DISPID_IDISCFORMAT2_MEDIAPHYSICALLYBLANK = 1792
DISPID_IDISCFORMAT2_MEDIAHEURISTICALLYBLANK = 1793
DISPID_IDISCFORMAT2_SUPPORTEDMEDIATYPES = 1794
DISPID_IDISCFORMAT2ERASE_RECORDER = 256
DISPID_IDISCFORMAT2ERASE_FULLERASE = 257
DISPID_IDISCFORMAT2ERASE_MEDIATYPE = 258
DISPID_IDISCFORMAT2ERASE_CLIENTNAME = 259
DISPID_IDISCFORMAT2ERASE_ERASEMEDIA = 513
DISPID_IDISCFORMAT2ERASEEVENTS_UPDATE = 512
DISPID_IDISCFORMAT2DATA_RECORDER = 256
DISPID_IDISCFORMAT2DATA_BUFFERUNDERRUNFREEDISABLED = 257
DISPID_IDISCFORMAT2DATA_POSTGAPALREADYINIMAGE = 260
DISPID_IDISCFORMAT2DATA_CURRENTMEDIASTATUS = 262
DISPID_IDISCFORMAT2DATA_WRITEPROTECTSTATUS = 263
DISPID_IDISCFORMAT2DATA_TOTALSECTORS = 264
DISPID_IDISCFORMAT2DATA_FREESECTORS = 265
DISPID_IDISCFORMAT2DATA_NEXTWRITABLEADDRESS = 266
DISPID_IDISCFORMAT2DATA_STARTSECTOROFPREVIOUSSESSION = 267
DISPID_IDISCFORMAT2DATA_LASTSECTOROFPREVIOUSSESSION = 268
DISPID_IDISCFORMAT2DATA_FORCEMEDIATOBECLOSED = 269
DISPID_IDISCFORMAT2DATA_DISABLEDVDCOMPATIBILITYMODE = 270
DISPID_IDISCFORMAT2DATA_CURRENTMEDIATYPE = 271
DISPID_IDISCFORMAT2DATA_CLIENTNAME = 272
DISPID_IDISCFORMAT2DATA_REQUESTEDWRITESPEED = 273
DISPID_IDISCFORMAT2DATA_REQUESTEDROTATIONTYPEISPURECAV = 274
DISPID_IDISCFORMAT2DATA_CURRENTWRITESPEED = 275
DISPID_IDISCFORMAT2DATA_CURRENTROTATIONTYPEISPURECAV = 276
DISPID_IDISCFORMAT2DATA_SUPPORTEDWRITESPEEDS = 277
DISPID_IDISCFORMAT2DATA_SUPPORTEDWRITESPEEDDESCRIPTORS = 278
DISPID_IDISCFORMAT2DATA_FORCEOVERWRITE = 279
DISPID_IDISCFORMAT2DATA_MUTLISESSIONINTERFACES = 280
DISPID_IDISCFORMAT2DATA_WRITE = 512
DISPID_IDISCFORMAT2DATA_CANCELWRITE = 513
DISPID_IDISCFORMAT2DATA_SETWRITESPEED = 514
DISPID_DDISCFORMAT2DATAEVENTS_UPDATE = 512
DISPID_IDISCFORMAT2DATAEVENTARGS_ELAPSEDTIME = 768
DISPID_IDISCFORMAT2DATAEVENTARGS_ESTIMATEDREMAININGTIME = 769
DISPID_IDISCFORMAT2DATAEVENTARGS_ESTIMATEDTOTALTIME = 770
DISPID_IDISCFORMAT2DATAEVENTARGS_CURRENTACTION = 771
DISPID_IDISCFORMAT2TAO_RECORDER = 256
DISPID_IDISCFORMAT2TAO_BUFFERUNDERRUNFREEDISABLED = 258
DISPID_IDISCFORMAT2TAO_NUMBEROFEXISTINGTRACKS = 259
DISPID_IDISCFORMAT2TAO_TOTALSECTORSONMEDIA = 260
DISPID_IDISCFORMAT2TAO_FREESECTORSONMEDIA = 261
DISPID_IDISCFORMAT2TAO_USEDSECTORSONMEDIA = 262
DISPID_IDISCFORMAT2TAO_DONOTFINALIZEMEDIA = 263
DISPID_IDISCFORMAT2TAO_EXPECTEDTABLEOFCONTENTS = 266
DISPID_IDISCFORMAT2TAO_CURRENTMEDIATYPE = 267
DISPID_IDISCFORMAT2TAO_CLIENTNAME = 270
DISPID_IDISCFORMAT2TAO_REQUESTEDWRITESPEED = 271
DISPID_IDISCFORMAT2TAO_REQUESTEDROTATIONTYPEISPURECAV = 272
DISPID_IDISCFORMAT2TAO_CURRENTWRITESPEED = 273
DISPID_IDISCFORMAT2TAO_CURRENTROTATIONTYPEISPURECAV = 274
DISPID_IDISCFORMAT2TAO_SUPPORTEDWRITESPEEDS = 275
DISPID_IDISCFORMAT2TAO_SUPPORTEDWRITESPEEDDESCRIPTORS = 276
DISPID_IDISCFORMAT2TAO_PREPAREMEDIA = 512
DISPID_IDISCFORMAT2TAO_ADDAUDIOTRACK = 513
DISPID_IDISCFORMAT2TAO_CANCELADDTRACK = 514
DISPID_IDISCFORMAT2TAO_FINISHMEDIA = 515
DISPID_IDISCFORMAT2TAO_SETWRITESPEED = 516
DISPID_DDISCFORMAT2TAOEVENTS_UPDATE = 512
DISPID_IDISCFORMAT2TAOEVENTARGS_CURRENTTRACKNUMBER = 768
DISPID_IDISCFORMAT2TAOEVENTARGS_CURRENTACTION = 769
DISPID_IDISCFORMAT2TAOEVENTARGS_ELAPSEDTIME = 770
DISPID_IDISCFORMAT2TAOEVENTARGS_ESTIMATEDREMAININGTIME = 771
DISPID_IDISCFORMAT2TAOEVENTARGS_ESTIMATEDTOTALTIME = 772
DISPID_IDISCFORMAT2RAWCD_RECORDER = 256
DISPID_IDISCFORMAT2RAWCD_BUFFERUNDERRUNFREEDISABLED = 258
DISPID_IDISCFORMAT2RAWCD_STARTOFNEXTSESSION = 259
DISPID_IDISCFORMAT2RAWCD_LASTPOSSIBLESTARTOFLEADOUT = 260
DISPID_IDISCFORMAT2RAWCD_CURRENTMEDIATYPE = 261
DISPID_IDISCFORMAT2RAWCD_SUPPORTEDDATASECTORTYPES = 264
DISPID_IDISCFORMAT2RAWCD_REQUESTEDDATASECTORTYPE = 265
DISPID_IDISCFORMAT2RAWCD_CLIENTNAME = 266
DISPID_IDISCFORMAT2RAWCD_REQUESTEDWRITESPEED = 267
DISPID_IDISCFORMAT2RAWCD_REQUESTEDROTATIONTYPEISPURECAV = 268
DISPID_IDISCFORMAT2RAWCD_CURRENTWRITESPEED = 269
DISPID_IDISCFORMAT2RAWCD_CURRENTROTATIONTYPEISPURECAV = 270
DISPID_IDISCFORMAT2RAWCD_SUPPORTEDWRITESPEEDS = 271
DISPID_IDISCFORMAT2RAWCD_SUPPORTEDWRITESPEEDDESCRIPTORS = 272
DISPID_IDISCFORMAT2RAWCD_PREPAREMEDIA = 512
DISPID_IDISCFORMAT2RAWCD_WRITEMEDIA = 513
DISPID_IDISCFORMAT2RAWCD_WRITEMEDIAWITHVALIDATION = 514
DISPID_IDISCFORMAT2RAWCD_CANCELWRITE = 515
DISPID_IDISCFORMAT2RAWCD_RELEASEMEDIA = 516
DISPID_IDISCFORMAT2RAWCD_SETWRITESPEED = 517
DISPID_DDISCFORMAT2RAWCDEVENTS_UPDATE = 512
DISPID_IDISCFORMAT2RAWCDEVENTARGS_CURRENTTRACKNUMBER = 768
DISPID_IDISCFORMAT2RAWCDEVENTARGS_CURRENTACTION = 769
DISPID_IDISCFORMAT2RAWCDEVENTARGS_ELAPSEDTIME = 768
DISPID_IDISCFORMAT2RAWCDEVENTARGS_ESTIMATEDREMAININGTIME = 769
DISPID_IDISCFORMAT2RAWCDEVENTARGS_ESTIMATEDTOTALTIME = 770
IMAPI_SECTORS_PER_SECOND_AT_1X_CD = 75
IMAPI_SECTORS_PER_SECOND_AT_1X_DVD = 680
IMAPI_SECTORS_PER_SECOND_AT_1X_BD = 2195
IMAPI_SECTORS_PER_SECOND_AT_1X_HD_DVD = 4568
DISPID_IMULTISESSION_SUPPORTEDONCURRENTMEDIA = 256
DISPID_IMULTISESSION_INUSE = 257
DISPID_IMULTISESSION_IMPORTRECORDER = 258
DISPID_IMULTISESSION_FIRSTDATASESSION = 512
DISPID_IMULTISESSION_STARTSECTOROFPREVIOUSSESSION = 513
DISPID_IMULTISESSION_LASTSECTOROFPREVIOUSSESSION = 514
DISPID_IMULTISESSION_NEXTWRITABLEADDRESS = 515
DISPID_IMULTISESSION_FREESECTORS = 516
DISPID_IMULTISESSION_WRITEUNITSIZE = 517
DISPID_IMULTISESSION_LASTWRITTENADDRESS = 518
DISPID_IMULTISESSION_SECTORSONMEDIA = 519
DISPID_IRAWCDIMAGECREATOR_CREATERESULTIMAGE = 512
DISPID_IRAWCDIMAGECREATOR_ADDTRACK = 513
DISPID_IRAWCDIMAGECREATOR_ADDSPECIALPREGAP = 514
DISPID_IRAWCDIMAGECREATOR_ADDSUBCODERWGENERATOR = 515
DISPID_IRAWCDIMAGECREATOR_RESULTINGIMAGETYPE = 256
DISPID_IRAWCDIMAGECREATOR_STARTOFLEADOUT = 257
DISPID_IRAWCDIMAGECREATOR_STARTOFLEADOUTLIMIT = 258
DISPID_IRAWCDIMAGECREATOR_DISABLEGAPLESSAUDIO = 259
DISPID_IRAWCDIMAGECREATOR_MEDIACATALOGNUMBER = 260
DISPID_IRAWCDIMAGECREATOR_STARTINGTRACKNUMBER = 261
DISPID_IRAWCDIMAGECREATOR_TRACKINFO = 262
DISPID_IRAWCDIMAGECREATOR_NUMBEROFEXISTINGTRACKS = 263
DISPID_IRAWCDIMAGECREATOR_USEDSECTORSONDISC = 264
DISPID_IRAWCDIMAGECREATOR_EXPECTEDTABLEOFCONTENTS = 265
DISPID_IRAWCDTRACKINFO_STARTINGLBA = 256
DISPID_IRAWCDTRACKINFO_SECTORCOUNT = 257
DISPID_IRAWCDTRACKINFO_TRACKNUMBER = 258
DISPID_IRAWCDTRACKINFO_SECTORTYPE = 259
DISPID_IRAWCDTRACKINFO_ISRC = 260
DISPID_IRAWCDTRACKINFO_DIGITALAUDIOCOPYSETTING = 261
DISPID_IRAWCDTRACKINFO_AUDIOHASPREEMPHASIS = 262
DISPID_IBLOCKRANGE_STARTLBA = 256
DISPID_IBLOCKRANGE_ENDLBA = 257
DISPID_IBLOCKRANGELIST_BLOCKRANGES = 256
IMAPILib2_MajorVersion = 1
IMAPILib2_MinorVersion = 0
IMAPI2FS_BOOT_ENTRY_COUNT_MAX = 32
DISPID_DFILESYSTEMIMAGEEVENTS_UPDATE = 256
DISPID_DFILESYSTEMIMAGEIMPORTEVENTS_UPDATEIMPORT = 257
IMAPI2FS_MajorVersion = 1
IMAPI2FS_MinorVersion = 0
IMAPI2FS_FullVersion_STR = '1.0'
IMAPI2FS_FullVersion_WSTR = '1.0'
MP_MSGCLASS_SYSTEM = 1
MP_MSGCLASS_REPLICATION = 2
MP_MSGCLASS_DELIVERY_REPORT = 3
MP_MSGCLASS_NONDELIVERY_REPORT = 4
MP_STATUS_SUCCESS = 0
MP_STATUS_RETRY = 1
MP_STATUS_ABORT_DELIVERY = 2
MP_STATUS_BAD_MAIL = 3
MP_STATUS_SUBMITTED = 4
MP_STATUS_CATEGORIZED = 5
MP_STATUS_ABANDON_DELIVERY = 6
RP_RECIP_FLAGS_RESERVED = 15
RP_DSN_NOTIFY_SUCCESS = 16777216
RP_DSN_NOTIFY_FAILURE = 33554432
RP_DSN_NOTIFY_DELAY = 67108864
RP_DSN_NOTIFY_NEVER = 134217728
RP_DSN_NOTIFY_MASK = 251658240
RP_HANDLED = 16
RP_GENERAL_FAILURE = 32
RP_DSN_HANDLED = 64
RP_DELIVERED = 272
RP_DSN_SENT_NDR = 1104
RP_FAILED = 2096
RP_UNRESOLVED = 4144
RP_ENPANDED = 8208
RP_EXPANDED = 8208
RP_DSN_SENT_DELAYED = 16384
RP_DSN_SENT_EXPANDED = 32832
RP_DSN_SENT_RELAYED = 65600
RP_DSN_SENT_DELIVERED = 131136
RP_REMOTE_MTA_NO_DSN = 524288
RP_ERROR_CONTEXT_STORE = 1048576
RP_ERROR_CONTEXT_CAT = 2097152
RP_ERROR_CONTEXT_MTA = 4194304
RP_VOLATILE_FLAGS_MASK = 4026531840
RP_DSN_NOTIFY_INVALID = 0
MPV_INBOUND_CUTOFF_EXCEEDED = 1
MPV_WRITE_CONTENT = 2
NMP_PROCESS_POST = 1
NMP_PROCESS_CONTROL = 2
NMP_PROCESS_MODERATOR = 4
def _define_GUID_SMTP_SOURCE_TYPE():
    return Guid('fb65c4dc-e468-11d1-aa-67-00-c0-4f-a3-45-f6')
def _define_GUID_SMTPSVC_SOURCE():
    return Guid('1b3c0666-e470-11d1-aa-67-00-c0-4f-a3-45-f6')
def _define_CATID_SMTP_ON_INBOUND_COMMAND():
    return Guid('f6628c8d-0d5e-11d2-aa-68-00-c0-4f-a3-5b-82')
def _define_CATID_SMTP_ON_SERVER_RESPONSE():
    return Guid('f6628c8e-0d5e-11d2-aa-68-00-c0-4f-a3-5b-82')
def _define_CATID_SMTP_ON_SESSION_START():
    return Guid('f6628c8f-0d5e-11d2-aa-68-00-c0-4f-a3-5b-82')
def _define_CATID_SMTP_ON_MESSAGE_START():
    return Guid('f6628c90-0d5e-11d2-aa-68-00-c0-4f-a3-5b-82')
def _define_CATID_SMTP_ON_PER_RECIPIENT():
    return Guid('f6628c91-0d5e-11d2-aa-68-00-c0-4f-a3-5b-82')
def _define_CATID_SMTP_ON_BEFORE_DATA():
    return Guid('f6628c92-0d5e-11d2-aa-68-00-c0-4f-a3-5b-82')
def _define_CATID_SMTP_ON_SESSION_END():
    return Guid('f6628c93-0d5e-11d2-aa-68-00-c0-4f-a3-5b-82')
def _define_CATID_SMTP_STORE_DRIVER():
    return Guid('59175850-e533-11d1-aa-67-00-c0-4f-a3-45-f6')
def _define_CATID_SMTP_TRANSPORT_SUBMISSION():
    return Guid('ff3caa23-00b9-11d2-9d-fb-00-c0-4f-a3-22-ba')
def _define_CATID_SMTP_TRANSPORT_PRECATEGORIZE():
    return Guid('a3acfb0d-83ff-11d2-9e-14-00-c0-4f-a3-22-ba')
def _define_CATID_SMTP_TRANSPORT_CATEGORIZE():
    return Guid('960252a3-0a3a-11d2-9e-00-00-c0-4f-a3-22-ba')
def _define_CATID_SMTP_TRANSPORT_POSTCATEGORIZE():
    return Guid('76719654-05a6-11d2-9d-fd-00-c0-4f-a3-22-ba')
def _define_CATID_SMTP_TRANSPORT_ROUTER():
    return Guid('283430c9-1850-11d2-9e-03-00-c0-4f-a3-22-ba')
def _define_CATID_SMTP_MSGTRACKLOG():
    return Guid('c6df52aa-7db0-11d2-94-f4-00-c0-4f-79-f1-d6')
def _define_CATID_SMTP_DNSRESOLVERRECORDSINK():
    return Guid('bd0b4366-8e03-11d2-94-f6-00-c0-4f-79-f1-d6')
def _define_CATID_SMTP_MAXMSGSIZE():
    return Guid('ebf159de-a67e-11d2-94-f7-00-c0-4f-79-f1-d6')
def _define_CATID_SMTP_LOG():
    return Guid('93d0a538-2c1e-4b68-a7-c9-d7-3a-8a-a6-ee-97')
def _define_CATID_SMTP_GET_AUX_DOMAIN_INFO_FLAGS():
    return Guid('84ff368a-fab3-43d7-bc-df-69-2c-5b-46-e6-b1')
def _define_CLSID_SmtpCat():
    return Guid('b23c35b7-9219-11d2-9e-17-00-c0-4f-a3-22-ba')
def _define_CATID_SMTP_DSN():
    return Guid('22b55731-f5f8-4d23-bd-8f-87-b5-23-71-a7-3a')
SZ_PROGID_SMTPCAT = 'Smtp.Cat'
IMAPI_S_PROPERTIESIGNORED = 262656
IMAPI_S_BUFFER_TO_SMALL = 262657
IMAPI_E_NOTOPENED = -2147220981
IMAPI_E_NOTINITIALIZED = -2147220980
IMAPI_E_USERABORT = -2147220979
IMAPI_E_GENERIC = -2147220978
IMAPI_E_MEDIUM_NOTPRESENT = -2147220977
IMAPI_E_MEDIUM_INVALIDTYPE = -2147220976
IMAPI_E_DEVICE_NOPROPERTIES = -2147220975
IMAPI_E_DEVICE_NOTACCESSIBLE = -2147220974
IMAPI_E_DEVICE_NOTPRESENT = -2147220973
IMAPI_E_DEVICE_INVALIDTYPE = -2147220972
IMAPI_E_INITIALIZE_WRITE = -2147220971
IMAPI_E_INITIALIZE_ENDWRITE = -2147220970
IMAPI_E_FILESYSTEM = -2147220969
IMAPI_E_FILEACCESS = -2147220968
IMAPI_E_DISCINFO = -2147220967
IMAPI_E_TRACKNOTOPEN = -2147220966
IMAPI_E_TRACKOPEN = -2147220965
IMAPI_E_DISCFULL = -2147220964
IMAPI_E_BADJOLIETNAME = -2147220963
IMAPI_E_INVALIDIMAGE = -2147220962
IMAPI_E_NOACTIVEFORMAT = -2147220961
IMAPI_E_NOACTIVERECORDER = -2147220960
IMAPI_E_WRONGFORMAT = -2147220959
IMAPI_E_ALREADYOPEN = -2147220958
IMAPI_E_WRONGDISC = -2147220957
IMAPI_E_FILEEXISTS = -2147220956
IMAPI_E_STASHINUSE = -2147220955
IMAPI_E_DEVICE_STILL_IN_USE = -2147220954
IMAPI_E_LOSS_OF_STREAMING = -2147220953
IMAPI_E_COMPRESSEDSTASH = -2147220952
IMAPI_E_ENCRYPTEDSTASH = -2147220951
IMAPI_E_NOTENOUGHDISKFORSTASH = -2147220950
IMAPI_E_REMOVABLESTASH = -2147220949
IMAPI_E_CANNOT_WRITE_TO_MEDIA = -2147220948
IMAPI_E_TRACK_NOT_BIG_ENOUGH = -2147220947
IMAPI_E_BOOTIMAGE_AND_NONBLANK_DISC = -2147220946
def _define_OpenIMsgSession():
    try:
        return WINFUNCTYPE(Int32,win32more.System.Com.IMalloc_head,UInt32,POINTER(POINTER(win32more.Storage.Imapi._MSGSESS_head)))(('OpenIMsgSession', windll['MAPI32.dll']), ((1, 'lpMalloc'),(1, 'ulFlags'),(1, 'lppMsgSess'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CloseIMsgSession():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Storage.Imapi._MSGSESS_head))(('CloseIMsgSession', windll['MAPI32.dll']), ((1, 'lpMsgSess'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenIMsgOnIStg():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Storage.Imapi._MSGSESS_head),win32more.System.AddressBook.LPALLOCATEBUFFER,win32more.System.AddressBook.LPALLOCATEMORE,win32more.System.AddressBook.LPFREEBUFFER,win32more.System.Com.IMalloc_head,c_void_p,win32more.System.Com.StructuredStorage.IStorage_head,POINTER(win32more.Storage.Imapi.MSGCALLRELEASE),UInt32,UInt32,POINTER(win32more.System.AddressBook.IMessage_head))(('OpenIMsgOnIStg', windll['MAPI32.dll']), ((1, 'lpMsgSess'),(1, 'lpAllocateBuffer'),(1, 'lpAllocateMore'),(1, 'lpFreeBuffer'),(1, 'lpMalloc'),(1, 'lpMapiSup'),(1, 'lpStg'),(1, 'lpfMsgCallRelease'),(1, 'ulCallerData'),(1, 'ulFlags'),(1, 'lppMsg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetAttribIMsgOnIStg():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.System.AddressBook.SPropTagArray_head),POINTER(POINTER(win32more.Storage.Imapi.SPropAttrArray_head)))(('GetAttribIMsgOnIStg', windll['MAPI32.dll']), ((1, 'lpObject'),(1, 'lpPropTagArray'),(1, 'lppPropAttrArray'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetAttribIMsgOnIStg():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.System.AddressBook.SPropTagArray_head),POINTER(win32more.Storage.Imapi.SPropAttrArray_head),POINTER(POINTER(win32more.System.AddressBook.SPropProblemArray_head)))(('SetAttribIMsgOnIStg', windll['MAPI32.dll']), ((1, 'lpObject'),(1, 'lpPropTags'),(1, 'lpPropAttrs'),(1, 'lppPropProblems'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MapStorageSCode():
    try:
        return WINFUNCTYPE(Int32,Int32)(('MapStorageSCode', windll['MAPI32.dll']), ((1, 'StgSCode'),))
    except (FileNotFoundError, AttributeError):
        return None
BlockRange = Guid('b507ca27-2204-11dd-96-6a-00-1a-a0-1b-bc-58')
BlockRangeList = Guid('b507ca28-2204-11dd-96-6a-00-1a-a0-1b-bc-58')
BootOptions = Guid('2c941fce-975b-59be-a9-60-9a-2a-26-28-53-a5')
def _define_DDiscFormat2DataEvents_head():
    class DDiscFormat2DataEvents(win32more.System.Com.IDispatch_head):
        Guid = Guid('2735413c-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
    return DDiscFormat2DataEvents
def _define_DDiscFormat2DataEvents():
    DDiscFormat2DataEvents = win32more.Storage.Imapi.DDiscFormat2DataEvents_head
    DDiscFormat2DataEvents.Update = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head,win32more.System.Com.IDispatch_head)(7, 'Update', ((1, 'object'),(1, 'progress'),)))
    win32more.System.Com.IDispatch
    return DDiscFormat2DataEvents
def _define_DDiscFormat2EraseEvents_head():
    class DDiscFormat2EraseEvents(win32more.System.Com.IDispatch_head):
        Guid = Guid('2735413a-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
    return DDiscFormat2EraseEvents
def _define_DDiscFormat2EraseEvents():
    DDiscFormat2EraseEvents = win32more.Storage.Imapi.DDiscFormat2EraseEvents_head
    DDiscFormat2EraseEvents.Update = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head,Int32,Int32)(7, 'Update', ((1, 'object'),(1, 'elapsedSeconds'),(1, 'estimatedTotalSeconds'),)))
    win32more.System.Com.IDispatch
    return DDiscFormat2EraseEvents
def _define_DDiscFormat2RawCDEvents_head():
    class DDiscFormat2RawCDEvents(win32more.System.Com.IDispatch_head):
        Guid = Guid('27354142-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
    return DDiscFormat2RawCDEvents
def _define_DDiscFormat2RawCDEvents():
    DDiscFormat2RawCDEvents = win32more.Storage.Imapi.DDiscFormat2RawCDEvents_head
    DDiscFormat2RawCDEvents.Update = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head,win32more.System.Com.IDispatch_head)(7, 'Update', ((1, 'object'),(1, 'progress'),)))
    win32more.System.Com.IDispatch
    return DDiscFormat2RawCDEvents
def _define_DDiscFormat2TrackAtOnceEvents_head():
    class DDiscFormat2TrackAtOnceEvents(win32more.System.Com.IDispatch_head):
        Guid = Guid('2735413f-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
    return DDiscFormat2TrackAtOnceEvents
def _define_DDiscFormat2TrackAtOnceEvents():
    DDiscFormat2TrackAtOnceEvents = win32more.Storage.Imapi.DDiscFormat2TrackAtOnceEvents_head
    DDiscFormat2TrackAtOnceEvents.Update = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head,win32more.System.Com.IDispatch_head)(7, 'Update', ((1, 'object'),(1, 'progress'),)))
    win32more.System.Com.IDispatch
    return DDiscFormat2TrackAtOnceEvents
def _define_DDiscMaster2Events_head():
    class DDiscMaster2Events(win32more.System.Com.IDispatch_head):
        Guid = Guid('27354131-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
    return DDiscMaster2Events
def _define_DDiscMaster2Events():
    DDiscMaster2Events = win32more.Storage.Imapi.DDiscMaster2Events_head
    DDiscMaster2Events.NotifyDeviceAdded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head,win32more.Foundation.BSTR)(7, 'NotifyDeviceAdded', ((1, 'object'),(1, 'uniqueId'),)))
    DDiscMaster2Events.NotifyDeviceRemoved = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head,win32more.Foundation.BSTR)(8, 'NotifyDeviceRemoved', ((1, 'object'),(1, 'uniqueId'),)))
    win32more.System.Com.IDispatch
    return DDiscMaster2Events
def _define_DFileSystemImageEvents_head():
    class DFileSystemImageEvents(win32more.System.Com.IDispatch_head):
        Guid = Guid('2c941fdf-975b-59be-a9-60-9a-2a-26-28-53-a5')
    return DFileSystemImageEvents
def _define_DFileSystemImageEvents():
    DFileSystemImageEvents = win32more.Storage.Imapi.DFileSystemImageEvents_head
    DFileSystemImageEvents.Update = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head,win32more.Foundation.BSTR,Int32,Int32)(7, 'Update', ((1, 'object'),(1, 'currentFile'),(1, 'copiedSectors'),(1, 'totalSectors'),)))
    win32more.System.Com.IDispatch
    return DFileSystemImageEvents
def _define_DFileSystemImageImportEvents_head():
    class DFileSystemImageImportEvents(win32more.System.Com.IDispatch_head):
        Guid = Guid('d25c30f9-4087-4366-9e-24-e5-5b-e2-86-42-4b')
    return DFileSystemImageImportEvents
def _define_DFileSystemImageImportEvents():
    DFileSystemImageImportEvents = win32more.Storage.Imapi.DFileSystemImageImportEvents_head
    DFileSystemImageImportEvents.UpdateImport = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head,win32more.Storage.Imapi.FsiFileSystems,win32more.Foundation.BSTR,Int32,Int32,Int32,Int32)(7, 'UpdateImport', ((1, 'object'),(1, 'fileSystem'),(1, 'currentItem'),(1, 'importedDirectoryItems'),(1, 'totalDirectoryItems'),(1, 'importedFileItems'),(1, 'totalFileItems'),)))
    win32more.System.Com.IDispatch
    return DFileSystemImageImportEvents
DISC_RECORDER_STATE_FLAGS = UInt32
RECORDER_BURNING = 2
RECORDER_DOING_NOTHING = 0
RECORDER_OPENED = 1
def _define_DWriteEngine2Events_head():
    class DWriteEngine2Events(win32more.System.Com.IDispatch_head):
        Guid = Guid('27354137-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
    return DWriteEngine2Events
def _define_DWriteEngine2Events():
    DWriteEngine2Events = win32more.Storage.Imapi.DWriteEngine2Events_head
    DWriteEngine2Events.Update = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head,win32more.System.Com.IDispatch_head)(7, 'Update', ((1, 'object'),(1, 'progress'),)))
    win32more.System.Com.IDispatch
    return DWriteEngine2Events
EmulationType = Int32
EmulationType_EmulationNone = 0
EmulationType_Emulation12MFloppy = 1
EmulationType_Emulation144MFloppy = 2
EmulationType_Emulation288MFloppy = 3
EmulationType_EmulationHardDisk = 4
EnumFsiItems = Guid('2c941fc6-975b-59be-a9-60-9a-2a-26-28-53-a5')
EnumProgressItems = Guid('2c941fca-975b-59be-a9-60-9a-2a-26-28-53-a5')
FileSystemImageResult = Guid('2c941fcc-975b-59be-a9-60-9a-2a-26-28-53-a5')
FsiDirectoryItem = Guid('2c941fc8-975b-59be-a9-60-9a-2a-26-28-53-a5')
FsiFileItem = Guid('2c941fc7-975b-59be-a9-60-9a-2a-26-28-53-a5')
FsiFileSystems = Int32
FsiFileSystems_FsiFileSystemNone = 0
FsiFileSystems_FsiFileSystemISO9660 = 1
FsiFileSystems_FsiFileSystemJoliet = 2
FsiFileSystems_FsiFileSystemUDF = 4
FsiFileSystems_FsiFileSystemUnknown = 1073741824
FsiItemType = Int32
FsiItemType_FsiItemNotFound = 0
FsiItemType_FsiItemDirectory = 1
FsiItemType_FsiItemFile = 2
FsiNamedStreams = Guid('c6b6f8ed-6d19-44b4-b5-39-b1-59-b7-93-a3-2d')
FsiStream = Guid('2c941fcd-975b-59be-a9-60-9a-2a-26-28-53-a5')
def _define_IBlockRange_head():
    class IBlockRange(win32more.System.Com.IDispatch_head):
        Guid = Guid('b507ca25-2204-11dd-96-6a-00-1a-a0-1b-bc-58')
    return IBlockRange
def _define_IBlockRange():
    IBlockRange = win32more.Storage.Imapi.IBlockRange_head
    IBlockRange.get_StartLba = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_StartLba', ((1, 'value'),)))
    IBlockRange.get_EndLba = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(8, 'get_EndLba', ((1, 'value'),)))
    win32more.System.Com.IDispatch
    return IBlockRange
def _define_IBlockRangeList_head():
    class IBlockRangeList(win32more.System.Com.IDispatch_head):
        Guid = Guid('b507ca26-2204-11dd-96-6a-00-1a-a0-1b-bc-58')
    return IBlockRangeList
def _define_IBlockRangeList():
    IBlockRangeList = win32more.Storage.Imapi.IBlockRangeList_head
    IBlockRangeList.get_BlockRanges = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(7, 'get_BlockRanges', ((1, 'value'),)))
    win32more.System.Com.IDispatch
    return IBlockRangeList
def _define_IBootOptions_head():
    class IBootOptions(win32more.System.Com.IDispatch_head):
        Guid = Guid('2c941fd4-975b-59be-a9-60-9a-2a-26-28-53-a5')
    return IBootOptions
def _define_IBootOptions():
    IBootOptions = win32more.Storage.Imapi.IBootOptions_head
    IBootOptions.get_BootImage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IStream_head))(7, 'get_BootImage', ((1, 'pVal'),)))
    IBootOptions.get_Manufacturer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(8, 'get_Manufacturer', ((1, 'pVal'),)))
    IBootOptions.put_Manufacturer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(9, 'put_Manufacturer', ((1, 'newVal'),)))
    IBootOptions.get_PlatformId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Imapi.PlatformId))(10, 'get_PlatformId', ((1, 'pVal'),)))
    IBootOptions.put_PlatformId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Imapi.PlatformId)(11, 'put_PlatformId', ((1, 'newVal'),)))
    IBootOptions.get_Emulation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Imapi.EmulationType))(12, 'get_Emulation', ((1, 'pVal'),)))
    IBootOptions.put_Emulation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Imapi.EmulationType)(13, 'put_Emulation', ((1, 'newVal'),)))
    IBootOptions.get_ImageSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(14, 'get_ImageSize', ((1, 'pVal'),)))
    IBootOptions.AssignBootImage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head)(15, 'AssignBootImage', ((1, 'newVal'),)))
    win32more.System.Com.IDispatch
    return IBootOptions
def _define_IBurnVerification_head():
    class IBurnVerification(win32more.System.Com.IUnknown_head):
        Guid = Guid('d2ffd834-958b-426d-84-70-2a-13-87-9c-6a-91')
    return IBurnVerification
def _define_IBurnVerification():
    IBurnVerification = win32more.Storage.Imapi.IBurnVerification_head
    IBurnVerification.put_BurnVerificationLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Imapi.IMAPI_BURN_VERIFICATION_LEVEL)(3, 'put_BurnVerificationLevel', ((1, 'value'),)))
    IBurnVerification.get_BurnVerificationLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Imapi.IMAPI_BURN_VERIFICATION_LEVEL))(4, 'get_BurnVerificationLevel', ((1, 'value'),)))
    win32more.System.Com.IUnknown
    return IBurnVerification
def _define_IDiscFormat2_head():
    class IDiscFormat2(win32more.System.Com.IDispatch_head):
        Guid = Guid('27354152-8f64-5b0f-8f-00-5d-77-af-be-26-1e')
    return IDiscFormat2
def _define_IDiscFormat2():
    IDiscFormat2 = win32more.Storage.Imapi.IDiscFormat2_head
    IDiscFormat2.IsRecorderSupported = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Imapi.IDiscRecorder2_head,POINTER(win32more.Foundation.VARIANT_BOOL))(7, 'IsRecorderSupported', ((1, 'recorder'),(1, 'value'),)))
    IDiscFormat2.IsCurrentMediaSupported = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Imapi.IDiscRecorder2_head,POINTER(win32more.Foundation.VARIANT_BOOL))(8, 'IsCurrentMediaSupported', ((1, 'recorder'),(1, 'value'),)))
    IDiscFormat2.get_MediaPhysicallyBlank = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(9, 'get_MediaPhysicallyBlank', ((1, 'value'),)))
    IDiscFormat2.get_MediaHeuristicallyBlank = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(10, 'get_MediaHeuristicallyBlank', ((1, 'value'),)))
    IDiscFormat2.get_SupportedMediaTypes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(11, 'get_SupportedMediaTypes', ((1, 'value'),)))
    win32more.System.Com.IDispatch
    return IDiscFormat2
def _define_IDiscFormat2Data_head():
    class IDiscFormat2Data(win32more.Storage.Imapi.IDiscFormat2_head):
        Guid = Guid('27354153-9f64-5b0f-8f-00-5d-77-af-be-26-1e')
    return IDiscFormat2Data
def _define_IDiscFormat2Data():
    IDiscFormat2Data = win32more.Storage.Imapi.IDiscFormat2Data_head
    IDiscFormat2Data.put_Recorder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Imapi.IDiscRecorder2_head)(12, 'put_Recorder', ((1, 'value'),)))
    IDiscFormat2Data.get_Recorder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Imapi.IDiscRecorder2_head))(13, 'get_Recorder', ((1, 'value'),)))
    IDiscFormat2Data.put_BufferUnderrunFreeDisabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(14, 'put_BufferUnderrunFreeDisabled', ((1, 'value'),)))
    IDiscFormat2Data.get_BufferUnderrunFreeDisabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(15, 'get_BufferUnderrunFreeDisabled', ((1, 'value'),)))
    IDiscFormat2Data.put_PostgapAlreadyInImage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(16, 'put_PostgapAlreadyInImage', ((1, 'value'),)))
    IDiscFormat2Data.get_PostgapAlreadyInImage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(17, 'get_PostgapAlreadyInImage', ((1, 'value'),)))
    IDiscFormat2Data.get_CurrentMediaStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Imapi.IMAPI_FORMAT2_DATA_MEDIA_STATE))(18, 'get_CurrentMediaStatus', ((1, 'value'),)))
    IDiscFormat2Data.get_WriteProtectStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Imapi.IMAPI_MEDIA_WRITE_PROTECT_STATE))(19, 'get_WriteProtectStatus', ((1, 'value'),)))
    IDiscFormat2Data.get_TotalSectorsOnMedia = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(20, 'get_TotalSectorsOnMedia', ((1, 'value'),)))
    IDiscFormat2Data.get_FreeSectorsOnMedia = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(21, 'get_FreeSectorsOnMedia', ((1, 'value'),)))
    IDiscFormat2Data.get_NextWritableAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(22, 'get_NextWritableAddress', ((1, 'value'),)))
    IDiscFormat2Data.get_StartAddressOfPreviousSession = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(23, 'get_StartAddressOfPreviousSession', ((1, 'value'),)))
    IDiscFormat2Data.get_LastWrittenAddressOfPreviousSession = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(24, 'get_LastWrittenAddressOfPreviousSession', ((1, 'value'),)))
    IDiscFormat2Data.put_ForceMediaToBeClosed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(25, 'put_ForceMediaToBeClosed', ((1, 'value'),)))
    IDiscFormat2Data.get_ForceMediaToBeClosed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(26, 'get_ForceMediaToBeClosed', ((1, 'value'),)))
    IDiscFormat2Data.put_DisableConsumerDvdCompatibilityMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(27, 'put_DisableConsumerDvdCompatibilityMode', ((1, 'value'),)))
    IDiscFormat2Data.get_DisableConsumerDvdCompatibilityMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(28, 'get_DisableConsumerDvdCompatibilityMode', ((1, 'value'),)))
    IDiscFormat2Data.get_CurrentPhysicalMediaType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Imapi.IMAPI_MEDIA_PHYSICAL_TYPE))(29, 'get_CurrentPhysicalMediaType', ((1, 'value'),)))
    IDiscFormat2Data.put_ClientName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(30, 'put_ClientName', ((1, 'value'),)))
    IDiscFormat2Data.get_ClientName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(31, 'get_ClientName', ((1, 'value'),)))
    IDiscFormat2Data.get_RequestedWriteSpeed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(32, 'get_RequestedWriteSpeed', ((1, 'value'),)))
    IDiscFormat2Data.get_RequestedRotationTypeIsPureCAV = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(33, 'get_RequestedRotationTypeIsPureCAV', ((1, 'value'),)))
    IDiscFormat2Data.get_CurrentWriteSpeed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(34, 'get_CurrentWriteSpeed', ((1, 'value'),)))
    IDiscFormat2Data.get_CurrentRotationTypeIsPureCAV = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(35, 'get_CurrentRotationTypeIsPureCAV', ((1, 'value'),)))
    IDiscFormat2Data.get_SupportedWriteSpeeds = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(36, 'get_SupportedWriteSpeeds', ((1, 'supportedSpeeds'),)))
    IDiscFormat2Data.get_SupportedWriteSpeedDescriptors = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(37, 'get_SupportedWriteSpeedDescriptors', ((1, 'supportedSpeedDescriptors'),)))
    IDiscFormat2Data.put_ForceOverwrite = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(38, 'put_ForceOverwrite', ((1, 'value'),)))
    IDiscFormat2Data.get_ForceOverwrite = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(39, 'get_ForceOverwrite', ((1, 'value'),)))
    IDiscFormat2Data.get_MultisessionInterfaces = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(40, 'get_MultisessionInterfaces', ((1, 'value'),)))
    IDiscFormat2Data.Write = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head)(41, 'Write', ((1, 'data'),)))
    IDiscFormat2Data.CancelWrite = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(42, 'CancelWrite', ()))
    IDiscFormat2Data.SetWriteSpeed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.VARIANT_BOOL)(43, 'SetWriteSpeed', ((1, 'RequestedSectorsPerSecond'),(1, 'RotationTypeIsPureCAV'),)))
    win32more.Storage.Imapi.IDiscFormat2
    return IDiscFormat2Data
def _define_IDiscFormat2DataEventArgs_head():
    class IDiscFormat2DataEventArgs(win32more.Storage.Imapi.IWriteEngine2EventArgs_head):
        Guid = Guid('2735413d-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
    return IDiscFormat2DataEventArgs
def _define_IDiscFormat2DataEventArgs():
    IDiscFormat2DataEventArgs = win32more.Storage.Imapi.IDiscFormat2DataEventArgs_head
    IDiscFormat2DataEventArgs.get_ElapsedTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(14, 'get_ElapsedTime', ((1, 'value'),)))
    IDiscFormat2DataEventArgs.get_RemainingTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(15, 'get_RemainingTime', ((1, 'value'),)))
    IDiscFormat2DataEventArgs.get_TotalTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(16, 'get_TotalTime', ((1, 'value'),)))
    IDiscFormat2DataEventArgs.get_CurrentAction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Imapi.IMAPI_FORMAT2_DATA_WRITE_ACTION))(17, 'get_CurrentAction', ((1, 'value'),)))
    win32more.Storage.Imapi.IWriteEngine2EventArgs
    return IDiscFormat2DataEventArgs
def _define_IDiscFormat2Erase_head():
    class IDiscFormat2Erase(win32more.Storage.Imapi.IDiscFormat2_head):
        Guid = Guid('27354156-8f64-5b0f-8f-00-5d-77-af-be-26-1e')
    return IDiscFormat2Erase
def _define_IDiscFormat2Erase():
    IDiscFormat2Erase = win32more.Storage.Imapi.IDiscFormat2Erase_head
    IDiscFormat2Erase.put_Recorder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Imapi.IDiscRecorder2_head)(12, 'put_Recorder', ((1, 'value'),)))
    IDiscFormat2Erase.get_Recorder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Imapi.IDiscRecorder2_head))(13, 'get_Recorder', ((1, 'value'),)))
    IDiscFormat2Erase.put_FullErase = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(14, 'put_FullErase', ((1, 'value'),)))
    IDiscFormat2Erase.get_FullErase = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(15, 'get_FullErase', ((1, 'value'),)))
    IDiscFormat2Erase.get_CurrentPhysicalMediaType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Imapi.IMAPI_MEDIA_PHYSICAL_TYPE))(16, 'get_CurrentPhysicalMediaType', ((1, 'value'),)))
    IDiscFormat2Erase.put_ClientName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(17, 'put_ClientName', ((1, 'value'),)))
    IDiscFormat2Erase.get_ClientName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(18, 'get_ClientName', ((1, 'value'),)))
    IDiscFormat2Erase.EraseMedia = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(19, 'EraseMedia', ()))
    win32more.Storage.Imapi.IDiscFormat2
    return IDiscFormat2Erase
def _define_IDiscFormat2RawCD_head():
    class IDiscFormat2RawCD(win32more.Storage.Imapi.IDiscFormat2_head):
        Guid = Guid('27354155-8f64-5b0f-8f-00-5d-77-af-be-26-1e')
    return IDiscFormat2RawCD
def _define_IDiscFormat2RawCD():
    IDiscFormat2RawCD = win32more.Storage.Imapi.IDiscFormat2RawCD_head
    IDiscFormat2RawCD.PrepareMedia = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(12, 'PrepareMedia', ()))
    IDiscFormat2RawCD.WriteMedia = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head)(13, 'WriteMedia', ((1, 'data'),)))
    IDiscFormat2RawCD.WriteMedia2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,Int32)(14, 'WriteMedia2', ((1, 'data'),(1, 'streamLeadInSectors'),)))
    IDiscFormat2RawCD.CancelWrite = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(15, 'CancelWrite', ()))
    IDiscFormat2RawCD.ReleaseMedia = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(16, 'ReleaseMedia', ()))
    IDiscFormat2RawCD.SetWriteSpeed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.VARIANT_BOOL)(17, 'SetWriteSpeed', ((1, 'RequestedSectorsPerSecond'),(1, 'RotationTypeIsPureCAV'),)))
    IDiscFormat2RawCD.put_Recorder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Imapi.IDiscRecorder2_head)(18, 'put_Recorder', ((1, 'value'),)))
    IDiscFormat2RawCD.get_Recorder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Imapi.IDiscRecorder2_head))(19, 'get_Recorder', ((1, 'value'),)))
    IDiscFormat2RawCD.put_BufferUnderrunFreeDisabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(20, 'put_BufferUnderrunFreeDisabled', ((1, 'value'),)))
    IDiscFormat2RawCD.get_BufferUnderrunFreeDisabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(21, 'get_BufferUnderrunFreeDisabled', ((1, 'value'),)))
    IDiscFormat2RawCD.get_StartOfNextSession = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(22, 'get_StartOfNextSession', ((1, 'value'),)))
    IDiscFormat2RawCD.get_LastPossibleStartOfLeadout = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(23, 'get_LastPossibleStartOfLeadout', ((1, 'value'),)))
    IDiscFormat2RawCD.get_CurrentPhysicalMediaType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Imapi.IMAPI_MEDIA_PHYSICAL_TYPE))(24, 'get_CurrentPhysicalMediaType', ((1, 'value'),)))
    IDiscFormat2RawCD.get_SupportedSectorTypes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(25, 'get_SupportedSectorTypes', ((1, 'value'),)))
    IDiscFormat2RawCD.put_RequestedSectorType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Imapi.IMAPI_FORMAT2_RAW_CD_DATA_SECTOR_TYPE)(26, 'put_RequestedSectorType', ((1, 'value'),)))
    IDiscFormat2RawCD.get_RequestedSectorType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Imapi.IMAPI_FORMAT2_RAW_CD_DATA_SECTOR_TYPE))(27, 'get_RequestedSectorType', ((1, 'value'),)))
    IDiscFormat2RawCD.put_ClientName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(28, 'put_ClientName', ((1, 'value'),)))
    IDiscFormat2RawCD.get_ClientName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(29, 'get_ClientName', ((1, 'value'),)))
    IDiscFormat2RawCD.get_RequestedWriteSpeed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(30, 'get_RequestedWriteSpeed', ((1, 'value'),)))
    IDiscFormat2RawCD.get_RequestedRotationTypeIsPureCAV = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(31, 'get_RequestedRotationTypeIsPureCAV', ((1, 'value'),)))
    IDiscFormat2RawCD.get_CurrentWriteSpeed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(32, 'get_CurrentWriteSpeed', ((1, 'value'),)))
    IDiscFormat2RawCD.get_CurrentRotationTypeIsPureCAV = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(33, 'get_CurrentRotationTypeIsPureCAV', ((1, 'value'),)))
    IDiscFormat2RawCD.get_SupportedWriteSpeeds = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(34, 'get_SupportedWriteSpeeds', ((1, 'supportedSpeeds'),)))
    IDiscFormat2RawCD.get_SupportedWriteSpeedDescriptors = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(35, 'get_SupportedWriteSpeedDescriptors', ((1, 'supportedSpeedDescriptors'),)))
    win32more.Storage.Imapi.IDiscFormat2
    return IDiscFormat2RawCD
def _define_IDiscFormat2RawCDEventArgs_head():
    class IDiscFormat2RawCDEventArgs(win32more.Storage.Imapi.IWriteEngine2EventArgs_head):
        Guid = Guid('27354143-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
    return IDiscFormat2RawCDEventArgs
def _define_IDiscFormat2RawCDEventArgs():
    IDiscFormat2RawCDEventArgs = win32more.Storage.Imapi.IDiscFormat2RawCDEventArgs_head
    IDiscFormat2RawCDEventArgs.get_CurrentAction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Imapi.IMAPI_FORMAT2_RAW_CD_WRITE_ACTION))(14, 'get_CurrentAction', ((1, 'value'),)))
    IDiscFormat2RawCDEventArgs.get_ElapsedTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(15, 'get_ElapsedTime', ((1, 'value'),)))
    IDiscFormat2RawCDEventArgs.get_RemainingTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(16, 'get_RemainingTime', ((1, 'value'),)))
    win32more.Storage.Imapi.IWriteEngine2EventArgs
    return IDiscFormat2RawCDEventArgs
def _define_IDiscFormat2TrackAtOnce_head():
    class IDiscFormat2TrackAtOnce(win32more.Storage.Imapi.IDiscFormat2_head):
        Guid = Guid('27354154-8f64-5b0f-8f-00-5d-77-af-be-26-1e')
    return IDiscFormat2TrackAtOnce
def _define_IDiscFormat2TrackAtOnce():
    IDiscFormat2TrackAtOnce = win32more.Storage.Imapi.IDiscFormat2TrackAtOnce_head
    IDiscFormat2TrackAtOnce.PrepareMedia = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(12, 'PrepareMedia', ()))
    IDiscFormat2TrackAtOnce.AddAudioTrack = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head)(13, 'AddAudioTrack', ((1, 'data'),)))
    IDiscFormat2TrackAtOnce.CancelAddTrack = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(14, 'CancelAddTrack', ()))
    IDiscFormat2TrackAtOnce.ReleaseMedia = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(15, 'ReleaseMedia', ()))
    IDiscFormat2TrackAtOnce.SetWriteSpeed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.VARIANT_BOOL)(16, 'SetWriteSpeed', ((1, 'RequestedSectorsPerSecond'),(1, 'RotationTypeIsPureCAV'),)))
    IDiscFormat2TrackAtOnce.put_Recorder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Imapi.IDiscRecorder2_head)(17, 'put_Recorder', ((1, 'value'),)))
    IDiscFormat2TrackAtOnce.get_Recorder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Imapi.IDiscRecorder2_head))(18, 'get_Recorder', ((1, 'value'),)))
    IDiscFormat2TrackAtOnce.put_BufferUnderrunFreeDisabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(19, 'put_BufferUnderrunFreeDisabled', ((1, 'value'),)))
    IDiscFormat2TrackAtOnce.get_BufferUnderrunFreeDisabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(20, 'get_BufferUnderrunFreeDisabled', ((1, 'value'),)))
    IDiscFormat2TrackAtOnce.get_NumberOfExistingTracks = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(21, 'get_NumberOfExistingTracks', ((1, 'value'),)))
    IDiscFormat2TrackAtOnce.get_TotalSectorsOnMedia = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(22, 'get_TotalSectorsOnMedia', ((1, 'value'),)))
    IDiscFormat2TrackAtOnce.get_FreeSectorsOnMedia = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(23, 'get_FreeSectorsOnMedia', ((1, 'value'),)))
    IDiscFormat2TrackAtOnce.get_UsedSectorsOnMedia = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(24, 'get_UsedSectorsOnMedia', ((1, 'value'),)))
    IDiscFormat2TrackAtOnce.put_DoNotFinalizeMedia = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(25, 'put_DoNotFinalizeMedia', ((1, 'value'),)))
    IDiscFormat2TrackAtOnce.get_DoNotFinalizeMedia = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(26, 'get_DoNotFinalizeMedia', ((1, 'value'),)))
    IDiscFormat2TrackAtOnce.get_ExpectedTableOfContents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(27, 'get_ExpectedTableOfContents', ((1, 'value'),)))
    IDiscFormat2TrackAtOnce.get_CurrentPhysicalMediaType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Imapi.IMAPI_MEDIA_PHYSICAL_TYPE))(28, 'get_CurrentPhysicalMediaType', ((1, 'value'),)))
    IDiscFormat2TrackAtOnce.put_ClientName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(29, 'put_ClientName', ((1, 'value'),)))
    IDiscFormat2TrackAtOnce.get_ClientName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(30, 'get_ClientName', ((1, 'value'),)))
    IDiscFormat2TrackAtOnce.get_RequestedWriteSpeed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(31, 'get_RequestedWriteSpeed', ((1, 'value'),)))
    IDiscFormat2TrackAtOnce.get_RequestedRotationTypeIsPureCAV = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(32, 'get_RequestedRotationTypeIsPureCAV', ((1, 'value'),)))
    IDiscFormat2TrackAtOnce.get_CurrentWriteSpeed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(33, 'get_CurrentWriteSpeed', ((1, 'value'),)))
    IDiscFormat2TrackAtOnce.get_CurrentRotationTypeIsPureCAV = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(34, 'get_CurrentRotationTypeIsPureCAV', ((1, 'value'),)))
    IDiscFormat2TrackAtOnce.get_SupportedWriteSpeeds = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(35, 'get_SupportedWriteSpeeds', ((1, 'supportedSpeeds'),)))
    IDiscFormat2TrackAtOnce.get_SupportedWriteSpeedDescriptors = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(36, 'get_SupportedWriteSpeedDescriptors', ((1, 'supportedSpeedDescriptors'),)))
    win32more.Storage.Imapi.IDiscFormat2
    return IDiscFormat2TrackAtOnce
def _define_IDiscFormat2TrackAtOnceEventArgs_head():
    class IDiscFormat2TrackAtOnceEventArgs(win32more.Storage.Imapi.IWriteEngine2EventArgs_head):
        Guid = Guid('27354140-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
    return IDiscFormat2TrackAtOnceEventArgs
def _define_IDiscFormat2TrackAtOnceEventArgs():
    IDiscFormat2TrackAtOnceEventArgs = win32more.Storage.Imapi.IDiscFormat2TrackAtOnceEventArgs_head
    IDiscFormat2TrackAtOnceEventArgs.get_CurrentTrackNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(14, 'get_CurrentTrackNumber', ((1, 'value'),)))
    IDiscFormat2TrackAtOnceEventArgs.get_CurrentAction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Imapi.IMAPI_FORMAT2_TAO_WRITE_ACTION))(15, 'get_CurrentAction', ((1, 'value'),)))
    IDiscFormat2TrackAtOnceEventArgs.get_ElapsedTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(16, 'get_ElapsedTime', ((1, 'value'),)))
    IDiscFormat2TrackAtOnceEventArgs.get_RemainingTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(17, 'get_RemainingTime', ((1, 'value'),)))
    win32more.Storage.Imapi.IWriteEngine2EventArgs
    return IDiscFormat2TrackAtOnceEventArgs
def _define_IDiscMaster_head():
    class IDiscMaster(win32more.System.Com.IUnknown_head):
        Guid = Guid('520cca62-51a5-11d3-91-44-00-10-4b-a1-1c-5e')
    return IDiscMaster
def _define_IDiscMaster():
    IDiscMaster = win32more.Storage.Imapi.IDiscMaster_head
    IDiscMaster.Open = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'Open', ()))
    IDiscMaster.EnumDiscMasterFormats = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Imapi.IEnumDiscMasterFormats_head))(4, 'EnumDiscMasterFormats', ((1, 'ppEnum'),)))
    IDiscMaster.GetActiveDiscMasterFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(5, 'GetActiveDiscMasterFormat', ((1, 'lpiid'),)))
    IDiscMaster.SetActiveDiscMasterFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p))(6, 'SetActiveDiscMasterFormat', ((1, 'riid'),(1, 'ppUnk'),)))
    IDiscMaster.EnumDiscRecorders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Imapi.IEnumDiscRecorders_head))(7, 'EnumDiscRecorders', ((1, 'ppEnum'),)))
    IDiscMaster.GetActiveDiscRecorder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Imapi.IDiscRecorder_head))(8, 'GetActiveDiscRecorder', ((1, 'ppRecorder'),)))
    IDiscMaster.SetActiveDiscRecorder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Imapi.IDiscRecorder_head)(9, 'SetActiveDiscRecorder', ((1, 'pRecorder'),)))
    IDiscMaster.ClearFormatContent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(10, 'ClearFormatContent', ()))
    IDiscMaster.ProgressAdvise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Imapi.IDiscMasterProgressEvents_head,POINTER(UIntPtr))(11, 'ProgressAdvise', ((1, 'pEvents'),(1, 'pvCookie'),)))
    IDiscMaster.ProgressUnadvise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UIntPtr)(12, 'ProgressUnadvise', ((1, 'vCookie'),)))
    IDiscMaster.RecordDisc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Byte,Byte)(13, 'RecordDisc', ((1, 'bSimulate'),(1, 'bEjectAfterBurn'),)))
    IDiscMaster.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(14, 'Close', ()))
    win32more.System.Com.IUnknown
    return IDiscMaster
def _define_IDiscMaster2_head():
    class IDiscMaster2(win32more.System.Com.IDispatch_head):
        Guid = Guid('27354130-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
    return IDiscMaster2
def _define_IDiscMaster2():
    IDiscMaster2 = win32more.Storage.Imapi.IDiscMaster2_head
    IDiscMaster2.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.IEnumVARIANT_head))(7, 'get__NewEnum', ((1, 'ppunk'),)))
    IDiscMaster2.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BSTR))(8, 'get_Item', ((1, 'index'),(1, 'value'),)))
    IDiscMaster2.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(9, 'get_Count', ((1, 'value'),)))
    IDiscMaster2.get_IsSupportedEnvironment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(10, 'get_IsSupportedEnvironment', ((1, 'value'),)))
    win32more.System.Com.IDispatch
    return IDiscMaster2
def _define_IDiscMasterProgressEvents_head():
    class IDiscMasterProgressEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('ec9e51c1-4e5d-11d3-91-44-00-10-4b-a1-1c-5e')
    return IDiscMasterProgressEvents
def _define_IDiscMasterProgressEvents():
    IDiscMasterProgressEvents = win32more.Storage.Imapi.IDiscMasterProgressEvents_head
    IDiscMasterProgressEvents.QueryCancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no)(3, 'QueryCancel', ((1, 'pbCancel'),)))
    IDiscMasterProgressEvents.NotifyPnPActivity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'NotifyPnPActivity', ()))
    IDiscMasterProgressEvents.NotifyAddProgress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32)(5, 'NotifyAddProgress', ((1, 'nCompletedSteps'),(1, 'nTotalSteps'),)))
    IDiscMasterProgressEvents.NotifyBlockProgress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32)(6, 'NotifyBlockProgress', ((1, 'nCompleted'),(1, 'nTotal'),)))
    IDiscMasterProgressEvents.NotifyTrackProgress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32)(7, 'NotifyTrackProgress', ((1, 'nCurrentTrack'),(1, 'nTotalTracks'),)))
    IDiscMasterProgressEvents.NotifyPreparingBurn = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(8, 'NotifyPreparingBurn', ((1, 'nEstimatedSeconds'),)))
    IDiscMasterProgressEvents.NotifyClosingDisc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(9, 'NotifyClosingDisc', ((1, 'nEstimatedSeconds'),)))
    IDiscMasterProgressEvents.NotifyBurnComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT)(10, 'NotifyBurnComplete', ((1, 'status'),)))
    IDiscMasterProgressEvents.NotifyEraseComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT)(11, 'NotifyEraseComplete', ((1, 'status'),)))
    win32more.System.Com.IUnknown
    return IDiscMasterProgressEvents
def _define_IDiscRecorder_head():
    class IDiscRecorder(win32more.System.Com.IUnknown_head):
        Guid = Guid('85ac9776-ca88-4cf2-89-4e-09-59-8c-07-8a-41')
    return IDiscRecorder
def _define_IDiscRecorder():
    IDiscRecorder = win32more.Storage.Imapi.IDiscRecorder_head
    IDiscRecorder.Init = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,UInt32,UInt32)(3, 'Init', ((1, 'pbyUniqueID'),(1, 'nulIDSize'),(1, 'nulDriveNumber'),)))
    IDiscRecorder.GetRecorderGUID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,UInt32,POINTER(UInt32))(4, 'GetRecorderGUID', ((1, 'pbyUniqueID'),(1, 'ulBufferSize'),(1, 'pulReturnSizeRequired'),)))
    IDiscRecorder.GetRecorderType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Imapi.RECORDER_TYPES))(5, 'GetRecorderType', ((1, 'fTypeCode'),)))
    IDiscRecorder.GetDisplayNames = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR),POINTER(win32more.Foundation.BSTR),POINTER(win32more.Foundation.BSTR))(6, 'GetDisplayNames', ((1, 'pbstrVendorID'),(1, 'pbstrProductID'),(1, 'pbstrRevision'),)))
    IDiscRecorder.GetBasePnPID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'GetBasePnPID', ((1, 'pbstrBasePnPID'),)))
    IDiscRecorder.GetPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(8, 'GetPath', ((1, 'pbstrPath'),)))
    IDiscRecorder.GetRecorderProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.IPropertyStorage_head))(9, 'GetRecorderProperties', ((1, 'ppPropStg'),)))
    IDiscRecorder.SetRecorderProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyStorage_head)(10, 'SetRecorderProperties', ((1, 'pPropStg'),)))
    IDiscRecorder.GetRecorderState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Imapi.DISC_RECORDER_STATE_FLAGS))(11, 'GetRecorderState', ((1, 'pulDevStateFlags'),)))
    IDiscRecorder.OpenExclusive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(12, 'OpenExclusive', ()))
    IDiscRecorder.QueryMediaType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Imapi.MEDIA_TYPES),POINTER(win32more.Storage.Imapi.MEDIA_FLAGS))(13, 'QueryMediaType', ((1, 'fMediaType'),(1, 'fMediaFlags'),)))
    IDiscRecorder.QueryMediaInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,c_char_p_no,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32))(14, 'QueryMediaInfo', ((1, 'pbSessions'),(1, 'pbLastTrack'),(1, 'ulStartAddress'),(1, 'ulNextWritable'),(1, 'ulFreeBlocks'),)))
    IDiscRecorder.Eject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(15, 'Eject', ()))
    IDiscRecorder.Erase = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Byte)(16, 'Erase', ((1, 'bFullErase'),)))
    IDiscRecorder.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(17, 'Close', ()))
    win32more.System.Com.IUnknown
    return IDiscRecorder
def _define_IDiscRecorder2_head():
    class IDiscRecorder2(win32more.System.Com.IDispatch_head):
        Guid = Guid('27354133-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
    return IDiscRecorder2
def _define_IDiscRecorder2():
    IDiscRecorder2 = win32more.Storage.Imapi.IDiscRecorder2_head
    IDiscRecorder2.EjectMedia = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(7, 'EjectMedia', ()))
    IDiscRecorder2.CloseTray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(8, 'CloseTray', ()))
    IDiscRecorder2.AcquireExclusiveAccess = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL,win32more.Foundation.BSTR)(9, 'AcquireExclusiveAccess', ((1, 'force'),(1, '__MIDL__IDiscRecorder20000'),)))
    IDiscRecorder2.ReleaseExclusiveAccess = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(10, 'ReleaseExclusiveAccess', ()))
    IDiscRecorder2.DisableMcn = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(11, 'DisableMcn', ()))
    IDiscRecorder2.EnableMcn = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(12, 'EnableMcn', ()))
    IDiscRecorder2.InitializeDiscRecorder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(13, 'InitializeDiscRecorder', ((1, 'recorderUniqueId'),)))
    IDiscRecorder2.get_ActiveDiscRecorder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(14, 'get_ActiveDiscRecorder', ((1, 'value'),)))
    IDiscRecorder2.get_VendorId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(15, 'get_VendorId', ((1, 'value'),)))
    IDiscRecorder2.get_ProductId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(16, 'get_ProductId', ((1, 'value'),)))
    IDiscRecorder2.get_ProductRevision = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(17, 'get_ProductRevision', ((1, 'value'),)))
    IDiscRecorder2.get_VolumeName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(18, 'get_VolumeName', ((1, 'value'),)))
    IDiscRecorder2.get_VolumePathNames = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(19, 'get_VolumePathNames', ((1, 'value'),)))
    IDiscRecorder2.get_DeviceCanLoadMedia = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(20, 'get_DeviceCanLoadMedia', ((1, 'value'),)))
    IDiscRecorder2.get_LegacyDeviceNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(21, 'get_LegacyDeviceNumber', ((1, 'legacyDeviceNumber'),)))
    IDiscRecorder2.get_SupportedFeaturePages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(22, 'get_SupportedFeaturePages', ((1, 'value'),)))
    IDiscRecorder2.get_CurrentFeaturePages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(23, 'get_CurrentFeaturePages', ((1, 'value'),)))
    IDiscRecorder2.get_SupportedProfiles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(24, 'get_SupportedProfiles', ((1, 'value'),)))
    IDiscRecorder2.get_CurrentProfiles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(25, 'get_CurrentProfiles', ((1, 'value'),)))
    IDiscRecorder2.get_SupportedModePages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(26, 'get_SupportedModePages', ((1, 'value'),)))
    IDiscRecorder2.get_ExclusiveAccessOwner = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(27, 'get_ExclusiveAccessOwner', ((1, 'value'),)))
    win32more.System.Com.IDispatch
    return IDiscRecorder2
def _define_IDiscRecorder2Ex_head():
    class IDiscRecorder2Ex(win32more.System.Com.IUnknown_head):
        Guid = Guid('27354132-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
    return IDiscRecorder2Ex
def _define_IDiscRecorder2Ex():
    IDiscRecorder2Ex = win32more.Storage.Imapi.IDiscRecorder2Ex_head
    IDiscRecorder2Ex.SendCommandNoData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,UInt32,c_char_p_no,UInt32)(3, 'SendCommandNoData', ((1, 'Cdb'),(1, 'CdbSize'),(1, 'SenseBuffer'),(1, 'Timeout'),)))
    IDiscRecorder2Ex.SendCommandSendDataToDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,UInt32,c_char_p_no,UInt32,c_char_p_no,UInt32)(4, 'SendCommandSendDataToDevice', ((1, 'Cdb'),(1, 'CdbSize'),(1, 'SenseBuffer'),(1, 'Timeout'),(1, 'Buffer'),(1, 'BufferSize'),)))
    IDiscRecorder2Ex.SendCommandGetDataFromDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,UInt32,c_char_p_no,UInt32,c_char_p_no,UInt32,POINTER(UInt32))(5, 'SendCommandGetDataFromDevice', ((1, 'Cdb'),(1, 'CdbSize'),(1, 'SenseBuffer'),(1, 'Timeout'),(1, 'Buffer'),(1, 'BufferSize'),(1, 'BufferFetched'),)))
    IDiscRecorder2Ex.ReadDvdStructure = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,UInt32,POINTER(c_char_p_no),POINTER(UInt32))(6, 'ReadDvdStructure', ((1, 'format'),(1, 'address'),(1, 'layer'),(1, 'agid'),(1, 'data'),(1, 'count'),)))
    IDiscRecorder2Ex.SendDvdStructure = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_char_p_no,UInt32)(7, 'SendDvdStructure', ((1, 'format'),(1, 'data'),(1, 'count'),)))
    IDiscRecorder2Ex.GetAdapterDescriptor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(c_char_p_no),POINTER(UInt32))(8, 'GetAdapterDescriptor', ((1, 'data'),(1, 'byteSize'),)))
    IDiscRecorder2Ex.GetDeviceDescriptor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(c_char_p_no),POINTER(UInt32))(9, 'GetDeviceDescriptor', ((1, 'data'),(1, 'byteSize'),)))
    IDiscRecorder2Ex.GetDiscInformation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(c_char_p_no),POINTER(UInt32))(10, 'GetDiscInformation', ((1, 'discInformation'),(1, 'byteSize'),)))
    IDiscRecorder2Ex.GetTrackInformation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Storage.Imapi.IMAPI_READ_TRACK_ADDRESS_TYPE,POINTER(c_char_p_no),POINTER(UInt32))(11, 'GetTrackInformation', ((1, 'address'),(1, 'addressType'),(1, 'trackInformation'),(1, 'byteSize'),)))
    IDiscRecorder2Ex.GetFeaturePage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE,win32more.Foundation.BOOLEAN,POINTER(c_char_p_no),POINTER(UInt32))(12, 'GetFeaturePage', ((1, 'requestedFeature'),(1, 'currentFeatureOnly'),(1, 'featureData'),(1, 'byteSize'),)))
    IDiscRecorder2Ex.GetModePage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Imapi.IMAPI_MODE_PAGE_TYPE,win32more.Storage.Imapi.IMAPI_MODE_PAGE_REQUEST_TYPE,POINTER(c_char_p_no),POINTER(UInt32))(13, 'GetModePage', ((1, 'requestedModePage'),(1, 'requestType'),(1, 'modePageData'),(1, 'byteSize'),)))
    IDiscRecorder2Ex.SetModePage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Imapi.IMAPI_MODE_PAGE_REQUEST_TYPE,c_char_p_no,UInt32)(14, 'SetModePage', ((1, 'requestType'),(1, 'data'),(1, 'byteSize'),)))
    IDiscRecorder2Ex.GetSupportedFeaturePages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOLEAN,POINTER(POINTER(win32more.Storage.Imapi.IMAPI_FEATURE_PAGE_TYPE)),POINTER(UInt32))(15, 'GetSupportedFeaturePages', ((1, 'currentFeatureOnly'),(1, 'featureData'),(1, 'byteSize'),)))
    IDiscRecorder2Ex.GetSupportedProfiles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOLEAN,POINTER(POINTER(win32more.Storage.Imapi.IMAPI_PROFILE_TYPE)),POINTER(UInt32))(16, 'GetSupportedProfiles', ((1, 'currentOnly'),(1, 'profileTypes'),(1, 'validProfiles'),)))
    IDiscRecorder2Ex.GetSupportedModePages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Imapi.IMAPI_MODE_PAGE_REQUEST_TYPE,POINTER(POINTER(win32more.Storage.Imapi.IMAPI_MODE_PAGE_TYPE)),POINTER(UInt32))(17, 'GetSupportedModePages', ((1, 'requestType'),(1, 'modePageTypes'),(1, 'validPages'),)))
    IDiscRecorder2Ex.GetByteAlignmentMask = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(18, 'GetByteAlignmentMask', ((1, 'value'),)))
    IDiscRecorder2Ex.GetMaximumNonPageAlignedTransferSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(19, 'GetMaximumNonPageAlignedTransferSize', ((1, 'value'),)))
    IDiscRecorder2Ex.GetMaximumPageAlignedTransferSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(20, 'GetMaximumPageAlignedTransferSize', ((1, 'value'),)))
    win32more.System.Com.IUnknown
    return IDiscRecorder2Ex
def _define_IEnumDiscMasterFormats_head():
    class IEnumDiscMasterFormats(win32more.System.Com.IUnknown_head):
        Guid = Guid('ddf445e1-54ba-11d3-91-44-00-10-4b-a1-1c-5e')
    return IEnumDiscMasterFormats
def _define_IEnumDiscMasterFormats():
    IEnumDiscMasterFormats = win32more.Storage.Imapi.IEnumDiscMasterFormats_head
    IEnumDiscMasterFormats.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(UInt32))(3, 'Next', ((1, 'cFormats'),(1, 'lpiidFormatID'),(1, 'pcFetched'),)))
    IEnumDiscMasterFormats.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'Skip', ((1, 'cFormats'),)))
    IEnumDiscMasterFormats.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Reset', ()))
    IEnumDiscMasterFormats.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Imapi.IEnumDiscMasterFormats_head))(6, 'Clone', ((1, 'ppEnum'),)))
    win32more.System.Com.IUnknown
    return IEnumDiscMasterFormats
def _define_IEnumDiscRecorders_head():
    class IEnumDiscRecorders(win32more.System.Com.IUnknown_head):
        Guid = Guid('9b1921e1-54ac-11d3-91-44-00-10-4b-a1-1c-5e')
    return IEnumDiscRecorders
def _define_IEnumDiscRecorders():
    IEnumDiscRecorders = win32more.Storage.Imapi.IEnumDiscRecorders_head
    IEnumDiscRecorders.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Storage.Imapi.IDiscRecorder_head),POINTER(UInt32))(3, 'Next', ((1, 'cRecorders'),(1, 'ppRecorder'),(1, 'pcFetched'),)))
    IEnumDiscRecorders.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'Skip', ((1, 'cRecorders'),)))
    IEnumDiscRecorders.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Reset', ()))
    IEnumDiscRecorders.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Imapi.IEnumDiscRecorders_head))(6, 'Clone', ((1, 'ppEnum'),)))
    win32more.System.Com.IUnknown
    return IEnumDiscRecorders
def _define_IEnumFsiItems_head():
    class IEnumFsiItems(win32more.System.Com.IUnknown_head):
        Guid = Guid('2c941fda-975b-59be-a9-60-9a-2a-26-28-53-a5')
    return IEnumFsiItems
def _define_IEnumFsiItems():
    IEnumFsiItems = win32more.Storage.Imapi.IEnumFsiItems_head
    IEnumFsiItems.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Storage.Imapi.IFsiItem_head),POINTER(UInt32))(3, 'Next', ((1, 'celt'),(1, 'rgelt'),(1, 'pceltFetched'),)))
    IEnumFsiItems.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'Skip', ((1, 'celt'),)))
    IEnumFsiItems.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Reset', ()))
    IEnumFsiItems.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Imapi.IEnumFsiItems_head))(6, 'Clone', ((1, 'ppEnum'),)))
    win32more.System.Com.IUnknown
    return IEnumFsiItems
def _define_IEnumProgressItems_head():
    class IEnumProgressItems(win32more.System.Com.IUnknown_head):
        Guid = Guid('2c941fd6-975b-59be-a9-60-9a-2a-26-28-53-a5')
    return IEnumProgressItems
def _define_IEnumProgressItems():
    IEnumProgressItems = win32more.Storage.Imapi.IEnumProgressItems_head
    IEnumProgressItems.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Storage.Imapi.IProgressItem_head),POINTER(UInt32))(3, 'Next', ((1, 'celt'),(1, 'rgelt'),(1, 'pceltFetched'),)))
    IEnumProgressItems.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'Skip', ((1, 'celt'),)))
    IEnumProgressItems.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Reset', ()))
    IEnumProgressItems.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Imapi.IEnumProgressItems_head))(6, 'Clone', ((1, 'ppEnum'),)))
    win32more.System.Com.IUnknown
    return IEnumProgressItems
def _define_IFileSystemImage_head():
    class IFileSystemImage(win32more.System.Com.IDispatch_head):
        Guid = Guid('2c941fe1-975b-59be-a9-60-9a-2a-26-28-53-a5')
    return IFileSystemImage
def _define_IFileSystemImage():
    IFileSystemImage = win32more.Storage.Imapi.IFileSystemImage_head
    IFileSystemImage.get_Root = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Imapi.IFsiDirectoryItem_head))(7, 'get_Root', ((1, 'pVal'),)))
    IFileSystemImage.get_SessionStartBlock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(8, 'get_SessionStartBlock', ((1, 'pVal'),)))
    IFileSystemImage.put_SessionStartBlock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(9, 'put_SessionStartBlock', ((1, 'newVal'),)))
    IFileSystemImage.get_FreeMediaBlocks = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(10, 'get_FreeMediaBlocks', ((1, 'pVal'),)))
    IFileSystemImage.put_FreeMediaBlocks = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(11, 'put_FreeMediaBlocks', ((1, 'newVal'),)))
    IFileSystemImage.SetMaxMediaBlocksFromDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Imapi.IDiscRecorder2_head)(12, 'SetMaxMediaBlocksFromDevice', ((1, 'discRecorder'),)))
    IFileSystemImage.get_UsedBlocks = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(13, 'get_UsedBlocks', ((1, 'pVal'),)))
    IFileSystemImage.get_VolumeName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(14, 'get_VolumeName', ((1, 'pVal'),)))
    IFileSystemImage.put_VolumeName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(15, 'put_VolumeName', ((1, 'newVal'),)))
    IFileSystemImage.get_ImportedVolumeName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(16, 'get_ImportedVolumeName', ((1, 'pVal'),)))
    IFileSystemImage.get_BootImageOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Imapi.IBootOptions_head))(17, 'get_BootImageOptions', ((1, 'pVal'),)))
    IFileSystemImage.put_BootImageOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Imapi.IBootOptions_head)(18, 'put_BootImageOptions', ((1, 'newVal'),)))
    IFileSystemImage.get_FileCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(19, 'get_FileCount', ((1, 'pVal'),)))
    IFileSystemImage.get_DirectoryCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(20, 'get_DirectoryCount', ((1, 'pVal'),)))
    IFileSystemImage.get_WorkingDirectory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(21, 'get_WorkingDirectory', ((1, 'pVal'),)))
    IFileSystemImage.put_WorkingDirectory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(22, 'put_WorkingDirectory', ((1, 'newVal'),)))
    IFileSystemImage.get_ChangePoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(23, 'get_ChangePoint', ((1, 'pVal'),)))
    IFileSystemImage.get_StrictFileSystemCompliance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(24, 'get_StrictFileSystemCompliance', ((1, 'pVal'),)))
    IFileSystemImage.put_StrictFileSystemCompliance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(25, 'put_StrictFileSystemCompliance', ((1, 'newVal'),)))
    IFileSystemImage.get_UseRestrictedCharacterSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(26, 'get_UseRestrictedCharacterSet', ((1, 'pVal'),)))
    IFileSystemImage.put_UseRestrictedCharacterSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(27, 'put_UseRestrictedCharacterSet', ((1, 'newVal'),)))
    IFileSystemImage.get_FileSystemsToCreate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Imapi.FsiFileSystems))(28, 'get_FileSystemsToCreate', ((1, 'pVal'),)))
    IFileSystemImage.put_FileSystemsToCreate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Imapi.FsiFileSystems)(29, 'put_FileSystemsToCreate', ((1, 'newVal'),)))
    IFileSystemImage.get_FileSystemsSupported = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Imapi.FsiFileSystems))(30, 'get_FileSystemsSupported', ((1, 'pVal'),)))
    IFileSystemImage.put_UDFRevision = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(31, 'put_UDFRevision', ((1, 'newVal'),)))
    IFileSystemImage.get_UDFRevision = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(32, 'get_UDFRevision', ((1, 'pVal'),)))
    IFileSystemImage.get_UDFRevisionsSupported = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(33, 'get_UDFRevisionsSupported', ((1, 'pVal'),)))
    IFileSystemImage.ChooseImageDefaults = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Imapi.IDiscRecorder2_head)(34, 'ChooseImageDefaults', ((1, 'discRecorder'),)))
    IFileSystemImage.ChooseImageDefaultsForMediaType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Imapi.IMAPI_MEDIA_PHYSICAL_TYPE)(35, 'ChooseImageDefaultsForMediaType', ((1, 'value'),)))
    IFileSystemImage.put_ISO9660InterchangeLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(36, 'put_ISO9660InterchangeLevel', ((1, 'newVal'),)))
    IFileSystemImage.get_ISO9660InterchangeLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(37, 'get_ISO9660InterchangeLevel', ((1, 'pVal'),)))
    IFileSystemImage.get_ISO9660InterchangeLevelsSupported = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(38, 'get_ISO9660InterchangeLevelsSupported', ((1, 'pVal'),)))
    IFileSystemImage.CreateResultImage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Imapi.IFileSystemImageResult_head))(39, 'CreateResultImage', ((1, 'resultStream'),)))
    IFileSystemImage.Exists = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Storage.Imapi.FsiItemType))(40, 'Exists', ((1, 'fullPath'),(1, 'itemType'),)))
    IFileSystemImage.CalculateDiscIdentifier = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(41, 'CalculateDiscIdentifier', ((1, 'discIdentifier'),)))
    IFileSystemImage.IdentifyFileSystemsOnDisc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Imapi.IDiscRecorder2_head,POINTER(win32more.Storage.Imapi.FsiFileSystems))(42, 'IdentifyFileSystemsOnDisc', ((1, 'discRecorder'),(1, 'fileSystems'),)))
    IFileSystemImage.GetDefaultFileSystemForImport = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Imapi.FsiFileSystems,POINTER(win32more.Storage.Imapi.FsiFileSystems))(43, 'GetDefaultFileSystemForImport', ((1, 'fileSystems'),(1, 'importDefault'),)))
    IFileSystemImage.ImportFileSystem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Imapi.FsiFileSystems))(44, 'ImportFileSystem', ((1, 'importedFileSystem'),)))
    IFileSystemImage.ImportSpecificFileSystem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Imapi.FsiFileSystems)(45, 'ImportSpecificFileSystem', ((1, 'fileSystemToUse'),)))
    IFileSystemImage.RollbackToChangePoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(46, 'RollbackToChangePoint', ((1, 'changePoint'),)))
    IFileSystemImage.LockInChangePoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(47, 'LockInChangePoint', ()))
    IFileSystemImage.CreateDirectoryItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Storage.Imapi.IFsiDirectoryItem_head))(48, 'CreateDirectoryItem', ((1, 'name'),(1, 'newItem'),)))
    IFileSystemImage.CreateFileItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Storage.Imapi.IFsiFileItem_head))(49, 'CreateFileItem', ((1, 'name'),(1, 'newItem'),)))
    IFileSystemImage.get_VolumeNameUDF = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(50, 'get_VolumeNameUDF', ((1, 'pVal'),)))
    IFileSystemImage.get_VolumeNameJoliet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(51, 'get_VolumeNameJoliet', ((1, 'pVal'),)))
    IFileSystemImage.get_VolumeNameISO9660 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(52, 'get_VolumeNameISO9660', ((1, 'pVal'),)))
    IFileSystemImage.get_StageFiles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(53, 'get_StageFiles', ((1, 'pVal'),)))
    IFileSystemImage.put_StageFiles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(54, 'put_StageFiles', ((1, 'newVal'),)))
    IFileSystemImage.get_MultisessionInterfaces = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(55, 'get_MultisessionInterfaces', ((1, 'pVal'),)))
    IFileSystemImage.put_MultisessionInterfaces = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head))(56, 'put_MultisessionInterfaces', ((1, 'newVal'),)))
    win32more.System.Com.IDispatch
    return IFileSystemImage
def _define_IFileSystemImage2_head():
    class IFileSystemImage2(win32more.Storage.Imapi.IFileSystemImage_head):
        Guid = Guid('d7644b2c-1537-4767-b6-2f-f1-38-7b-02-dd-fd')
    return IFileSystemImage2
def _define_IFileSystemImage2():
    IFileSystemImage2 = win32more.Storage.Imapi.IFileSystemImage2_head
    IFileSystemImage2.get_BootImageOptionsArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(57, 'get_BootImageOptionsArray', ((1, 'pVal'),)))
    IFileSystemImage2.put_BootImageOptionsArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head))(58, 'put_BootImageOptionsArray', ((1, 'newVal'),)))
    win32more.Storage.Imapi.IFileSystemImage
    return IFileSystemImage2
def _define_IFileSystemImage3_head():
    class IFileSystemImage3(win32more.Storage.Imapi.IFileSystemImage2_head):
        Guid = Guid('7cff842c-7e97-4807-83-04-91-0d-d8-f7-c0-51')
    return IFileSystemImage3
def _define_IFileSystemImage3():
    IFileSystemImage3 = win32more.Storage.Imapi.IFileSystemImage3_head
    IFileSystemImage3.get_CreateRedundantUdfMetadataFiles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(59, 'get_CreateRedundantUdfMetadataFiles', ((1, 'pVal'),)))
    IFileSystemImage3.put_CreateRedundantUdfMetadataFiles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(60, 'put_CreateRedundantUdfMetadataFiles', ((1, 'newVal'),)))
    IFileSystemImage3.ProbeSpecificFileSystem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Imapi.FsiFileSystems,POINTER(win32more.Foundation.VARIANT_BOOL))(61, 'ProbeSpecificFileSystem', ((1, 'fileSystemToProbe'),(1, 'isAppendable'),)))
    win32more.Storage.Imapi.IFileSystemImage2
    return IFileSystemImage3
def _define_IFileSystemImageResult_head():
    class IFileSystemImageResult(win32more.System.Com.IDispatch_head):
        Guid = Guid('2c941fd8-975b-59be-a9-60-9a-2a-26-28-53-a5')
    return IFileSystemImageResult
def _define_IFileSystemImageResult():
    IFileSystemImageResult = win32more.Storage.Imapi.IFileSystemImageResult_head
    IFileSystemImageResult.get_ImageStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IStream_head))(7, 'get_ImageStream', ((1, 'pVal'),)))
    IFileSystemImageResult.get_ProgressItems = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Imapi.IProgressItems_head))(8, 'get_ProgressItems', ((1, 'pVal'),)))
    IFileSystemImageResult.get_TotalBlocks = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(9, 'get_TotalBlocks', ((1, 'pVal'),)))
    IFileSystemImageResult.get_BlockSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(10, 'get_BlockSize', ((1, 'pVal'),)))
    IFileSystemImageResult.get_DiscId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(11, 'get_DiscId', ((1, 'pVal'),)))
    win32more.System.Com.IDispatch
    return IFileSystemImageResult
def _define_IFileSystemImageResult2_head():
    class IFileSystemImageResult2(win32more.Storage.Imapi.IFileSystemImageResult_head):
        Guid = Guid('b507ca29-2204-11dd-96-6a-00-1a-a0-1b-bc-58')
    return IFileSystemImageResult2
def _define_IFileSystemImageResult2():
    IFileSystemImageResult2 = win32more.Storage.Imapi.IFileSystemImageResult2_head
    IFileSystemImageResult2.get_ModifiedBlocks = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Imapi.IBlockRangeList_head))(12, 'get_ModifiedBlocks', ((1, 'pVal'),)))
    win32more.Storage.Imapi.IFileSystemImageResult
    return IFileSystemImageResult2
def _define_IFsiDirectoryItem_head():
    class IFsiDirectoryItem(win32more.Storage.Imapi.IFsiItem_head):
        Guid = Guid('2c941fdc-975b-59be-a9-60-9a-2a-26-28-53-a5')
    return IFsiDirectoryItem
def _define_IFsiDirectoryItem():
    IFsiDirectoryItem = win32more.Storage.Imapi.IFsiDirectoryItem_head
    IFsiDirectoryItem.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.IEnumVARIANT_head))(19, 'get__NewEnum', ((1, 'NewEnum'),)))
    IFsiDirectoryItem.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Storage.Imapi.IFsiItem_head))(20, 'get_Item', ((1, 'path'),(1, 'item'),)))
    IFsiDirectoryItem.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(21, 'get_Count', ((1, 'Count'),)))
    IFsiDirectoryItem.get_EnumFsiItems = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Imapi.IEnumFsiItems_head))(22, 'get_EnumFsiItems', ((1, 'NewEnum'),)))
    IFsiDirectoryItem.AddDirectory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(23, 'AddDirectory', ((1, 'path'),)))
    IFsiDirectoryItem.AddFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.IStream_head)(24, 'AddFile', ((1, 'path'),(1, 'fileData'),)))
    IFsiDirectoryItem.AddTree = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.VARIANT_BOOL)(25, 'AddTree', ((1, 'sourceDirectory'),(1, 'includeBaseDirectory'),)))
    IFsiDirectoryItem.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Imapi.IFsiItem_head)(26, 'Add', ((1, 'item'),)))
    IFsiDirectoryItem.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(27, 'Remove', ((1, 'path'),)))
    IFsiDirectoryItem.RemoveTree = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(28, 'RemoveTree', ((1, 'path'),)))
    win32more.Storage.Imapi.IFsiItem
    return IFsiDirectoryItem
def _define_IFsiDirectoryItem2_head():
    class IFsiDirectoryItem2(win32more.Storage.Imapi.IFsiDirectoryItem_head):
        Guid = Guid('f7fb4b9b-6d96-4d7b-91-15-20-1b-14-48-11-ef')
    return IFsiDirectoryItem2
def _define_IFsiDirectoryItem2():
    IFsiDirectoryItem2 = win32more.Storage.Imapi.IFsiDirectoryItem2_head
    IFsiDirectoryItem2.AddTreeWithNamedStreams = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.VARIANT_BOOL)(29, 'AddTreeWithNamedStreams', ((1, 'sourceDirectory'),(1, 'includeBaseDirectory'),)))
    win32more.Storage.Imapi.IFsiDirectoryItem
    return IFsiDirectoryItem2
def _define_IFsiFileItem_head():
    class IFsiFileItem(win32more.Storage.Imapi.IFsiItem_head):
        Guid = Guid('2c941fdb-975b-59be-a9-60-9a-2a-26-28-53-a5')
    return IFsiFileItem
def _define_IFsiFileItem():
    IFsiFileItem = win32more.Storage.Imapi.IFsiFileItem_head
    IFsiFileItem.get_DataSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int64))(19, 'get_DataSize', ((1, 'pVal'),)))
    IFsiFileItem.get_DataSize32BitLow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(20, 'get_DataSize32BitLow', ((1, 'pVal'),)))
    IFsiFileItem.get_DataSize32BitHigh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(21, 'get_DataSize32BitHigh', ((1, 'pVal'),)))
    IFsiFileItem.get_Data = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IStream_head))(22, 'get_Data', ((1, 'pVal'),)))
    IFsiFileItem.put_Data = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head)(23, 'put_Data', ((1, 'newVal'),)))
    win32more.Storage.Imapi.IFsiItem
    return IFsiFileItem
def _define_IFsiFileItem2_head():
    class IFsiFileItem2(win32more.Storage.Imapi.IFsiFileItem_head):
        Guid = Guid('199d0c19-11e1-40eb-8e-c2-c8-c8-22-a0-77-92')
    return IFsiFileItem2
def _define_IFsiFileItem2():
    IFsiFileItem2 = win32more.Storage.Imapi.IFsiFileItem2_head
    IFsiFileItem2.get_FsiNamedStreams = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Imapi.IFsiNamedStreams_head))(24, 'get_FsiNamedStreams', ((1, 'streams'),)))
    IFsiFileItem2.get_IsNamedStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(25, 'get_IsNamedStream', ((1, 'pVal'),)))
    IFsiFileItem2.AddStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.IStream_head)(26, 'AddStream', ((1, 'name'),(1, 'streamData'),)))
    IFsiFileItem2.RemoveStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(27, 'RemoveStream', ((1, 'name'),)))
    IFsiFileItem2.get_IsRealTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(28, 'get_IsRealTime', ((1, 'pVal'),)))
    IFsiFileItem2.put_IsRealTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(29, 'put_IsRealTime', ((1, 'newVal'),)))
    win32more.Storage.Imapi.IFsiFileItem
    return IFsiFileItem2
def _define_IFsiItem_head():
    class IFsiItem(win32more.System.Com.IDispatch_head):
        Guid = Guid('2c941fd9-975b-59be-a9-60-9a-2a-26-28-53-a5')
    return IFsiItem
def _define_IFsiItem():
    IFsiItem = win32more.Storage.Imapi.IFsiItem_head
    IFsiItem.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_Name', ((1, 'pVal'),)))
    IFsiItem.get_FullPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(8, 'get_FullPath', ((1, 'pVal'),)))
    IFsiItem.get_CreationTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(9, 'get_CreationTime', ((1, 'pVal'),)))
    IFsiItem.put_CreationTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double)(10, 'put_CreationTime', ((1, 'newVal'),)))
    IFsiItem.get_LastAccessedTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(11, 'get_LastAccessedTime', ((1, 'pVal'),)))
    IFsiItem.put_LastAccessedTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double)(12, 'put_LastAccessedTime', ((1, 'newVal'),)))
    IFsiItem.get_LastModifiedTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(13, 'get_LastModifiedTime', ((1, 'pVal'),)))
    IFsiItem.put_LastModifiedTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double)(14, 'put_LastModifiedTime', ((1, 'newVal'),)))
    IFsiItem.get_IsHidden = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(15, 'get_IsHidden', ((1, 'pVal'),)))
    IFsiItem.put_IsHidden = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(16, 'put_IsHidden', ((1, 'newVal'),)))
    IFsiItem.FileSystemName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Imapi.FsiFileSystems,POINTER(win32more.Foundation.BSTR))(17, 'FileSystemName', ((1, 'fileSystem'),(1, 'pVal'),)))
    IFsiItem.FileSystemPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Imapi.FsiFileSystems,POINTER(win32more.Foundation.BSTR))(18, 'FileSystemPath', ((1, 'fileSystem'),(1, 'pVal'),)))
    win32more.System.Com.IDispatch
    return IFsiItem
def _define_IFsiNamedStreams_head():
    class IFsiNamedStreams(win32more.System.Com.IDispatch_head):
        Guid = Guid('ed79ba56-5294-4250-8d-46-f9-ae-ce-e2-34-59')
    return IFsiNamedStreams
def _define_IFsiNamedStreams():
    IFsiNamedStreams = win32more.Storage.Imapi.IFsiNamedStreams_head
    IFsiNamedStreams.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.IEnumVARIANT_head))(7, 'get__NewEnum', ((1, 'NewEnum'),)))
    IFsiNamedStreams.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Storage.Imapi.IFsiFileItem2_head))(8, 'get_Item', ((1, 'index'),(1, 'item'),)))
    IFsiNamedStreams.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(9, 'get_Count', ((1, 'count'),)))
    IFsiNamedStreams.get_EnumNamedStreams = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Imapi.IEnumFsiItems_head))(10, 'get_EnumNamedStreams', ((1, 'NewEnum'),)))
    win32more.System.Com.IDispatch
    return IFsiNamedStreams
def _define_IIsoImageManager_head():
    class IIsoImageManager(win32more.System.Com.IDispatch_head):
        Guid = Guid('6ca38be5-fbbb-4800-95-a1-a4-38-86-5e-b0-d4')
    return IIsoImageManager
def _define_IIsoImageManager():
    IIsoImageManager = win32more.Storage.Imapi.IIsoImageManager_head
    IIsoImageManager.get_Path = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_Path', ((1, 'pVal'),)))
    IIsoImageManager.get_Stream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IStream_head))(8, 'get_Stream', ((1, 'data'),)))
    IIsoImageManager.SetPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(9, 'SetPath', ((1, 'Val'),)))
    IIsoImageManager.SetStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head)(10, 'SetStream', ((1, 'data'),)))
    IIsoImageManager.Validate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(11, 'Validate', ()))
    win32more.System.Com.IDispatch
    return IIsoImageManager
def _define_IJolietDiscMaster_head():
    class IJolietDiscMaster(win32more.System.Com.IUnknown_head):
        Guid = Guid('e3bc42ce-4e5c-11d3-91-44-00-10-4b-a1-1c-5e')
    return IJolietDiscMaster
def _define_IJolietDiscMaster():
    IJolietDiscMaster = win32more.Storage.Imapi.IJolietDiscMaster_head
    IJolietDiscMaster.GetTotalDataBlocks = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(3, 'GetTotalDataBlocks', ((1, 'pnBlocks'),)))
    IJolietDiscMaster.GetUsedDataBlocks = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(4, 'GetUsedDataBlocks', ((1, 'pnBlocks'),)))
    IJolietDiscMaster.GetDataBlockSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(5, 'GetDataBlockSize', ((1, 'pnBlockBytes'),)))
    IJolietDiscMaster.AddData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IStorage_head,Int32)(6, 'AddData', ((1, 'pStorage'),(1, 'lFileOverwrite'),)))
    IJolietDiscMaster.GetJolietProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.IPropertyStorage_head))(7, 'GetJolietProperties', ((1, 'ppPropStg'),)))
    IJolietDiscMaster.SetJolietProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyStorage_head)(8, 'SetJolietProperties', ((1, 'pPropStg'),)))
    win32more.System.Com.IUnknown
    return IJolietDiscMaster
IMAPI_BURN_VERIFICATION_LEVEL = Int32
IMAPI_BURN_VERIFICATION_NONE = 0
IMAPI_BURN_VERIFICATION_QUICK = 1
IMAPI_BURN_VERIFICATION_FULL = 2
IMAPI_CD_SECTOR_TYPE = Int32
IMAPI_CD_SECTOR_AUDIO = 0
IMAPI_CD_SECTOR_MODE_ZERO = 1
IMAPI_CD_SECTOR_MODE1 = 2
IMAPI_CD_SECTOR_MODE2FORM0 = 3
IMAPI_CD_SECTOR_MODE2FORM1 = 4
IMAPI_CD_SECTOR_MODE2FORM2 = 5
IMAPI_CD_SECTOR_MODE1RAW = 6
IMAPI_CD_SECTOR_MODE2FORM0RAW = 7
IMAPI_CD_SECTOR_MODE2FORM1RAW = 8
IMAPI_CD_SECTOR_MODE2FORM2RAW = 9
IMAPI_CD_TRACK_DIGITAL_COPY_SETTING = Int32
IMAPI_CD_TRACK_DIGITAL_COPY_PERMITTED = 0
IMAPI_CD_TRACK_DIGITAL_COPY_PROHIBITED = 1
IMAPI_CD_TRACK_DIGITAL_COPY_SCMS = 2
IMAPI_FEATURE_PAGE_TYPE = Int32
IMAPI_FEATURE_PAGE_TYPE_PROFILE_LIST = 0
IMAPI_FEATURE_PAGE_TYPE_CORE = 1
IMAPI_FEATURE_PAGE_TYPE_MORPHING = 2
IMAPI_FEATURE_PAGE_TYPE_REMOVABLE_MEDIUM = 3
IMAPI_FEATURE_PAGE_TYPE_WRITE_PROTECT = 4
IMAPI_FEATURE_PAGE_TYPE_RANDOMLY_READABLE = 16
IMAPI_FEATURE_PAGE_TYPE_CD_MULTIREAD = 29
IMAPI_FEATURE_PAGE_TYPE_CD_READ = 30
IMAPI_FEATURE_PAGE_TYPE_DVD_READ = 31
IMAPI_FEATURE_PAGE_TYPE_RANDOMLY_WRITABLE = 32
IMAPI_FEATURE_PAGE_TYPE_INCREMENTAL_STREAMING_WRITABLE = 33
IMAPI_FEATURE_PAGE_TYPE_SECTOR_ERASABLE = 34
IMAPI_FEATURE_PAGE_TYPE_FORMATTABLE = 35
IMAPI_FEATURE_PAGE_TYPE_HARDWARE_DEFECT_MANAGEMENT = 36
IMAPI_FEATURE_PAGE_TYPE_WRITE_ONCE = 37
IMAPI_FEATURE_PAGE_TYPE_RESTRICTED_OVERWRITE = 38
IMAPI_FEATURE_PAGE_TYPE_CDRW_CAV_WRITE = 39
IMAPI_FEATURE_PAGE_TYPE_MRW = 40
IMAPI_FEATURE_PAGE_TYPE_ENHANCED_DEFECT_REPORTING = 41
IMAPI_FEATURE_PAGE_TYPE_DVD_PLUS_RW = 42
IMAPI_FEATURE_PAGE_TYPE_DVD_PLUS_R = 43
IMAPI_FEATURE_PAGE_TYPE_RIGID_RESTRICTED_OVERWRITE = 44
IMAPI_FEATURE_PAGE_TYPE_CD_TRACK_AT_ONCE = 45
IMAPI_FEATURE_PAGE_TYPE_CD_MASTERING = 46
IMAPI_FEATURE_PAGE_TYPE_DVD_DASH_WRITE = 47
IMAPI_FEATURE_PAGE_TYPE_DOUBLE_DENSITY_CD_READ = 48
IMAPI_FEATURE_PAGE_TYPE_DOUBLE_DENSITY_CD_R_WRITE = 49
IMAPI_FEATURE_PAGE_TYPE_DOUBLE_DENSITY_CD_RW_WRITE = 50
IMAPI_FEATURE_PAGE_TYPE_LAYER_JUMP_RECORDING = 51
IMAPI_FEATURE_PAGE_TYPE_CD_RW_MEDIA_WRITE_SUPPORT = 55
IMAPI_FEATURE_PAGE_TYPE_BD_PSEUDO_OVERWRITE = 56
IMAPI_FEATURE_PAGE_TYPE_DVD_PLUS_R_DUAL_LAYER = 59
IMAPI_FEATURE_PAGE_TYPE_BD_READ = 64
IMAPI_FEATURE_PAGE_TYPE_BD_WRITE = 65
IMAPI_FEATURE_PAGE_TYPE_HD_DVD_READ = 80
IMAPI_FEATURE_PAGE_TYPE_HD_DVD_WRITE = 81
IMAPI_FEATURE_PAGE_TYPE_POWER_MANAGEMENT = 256
IMAPI_FEATURE_PAGE_TYPE_SMART = 257
IMAPI_FEATURE_PAGE_TYPE_EMBEDDED_CHANGER = 258
IMAPI_FEATURE_PAGE_TYPE_CD_ANALOG_PLAY = 259
IMAPI_FEATURE_PAGE_TYPE_MICROCODE_UPDATE = 260
IMAPI_FEATURE_PAGE_TYPE_TIMEOUT = 261
IMAPI_FEATURE_PAGE_TYPE_DVD_CSS = 262
IMAPI_FEATURE_PAGE_TYPE_REAL_TIME_STREAMING = 263
IMAPI_FEATURE_PAGE_TYPE_LOGICAL_UNIT_SERIAL_NUMBER = 264
IMAPI_FEATURE_PAGE_TYPE_MEDIA_SERIAL_NUMBER = 265
IMAPI_FEATURE_PAGE_TYPE_DISC_CONTROL_BLOCKS = 266
IMAPI_FEATURE_PAGE_TYPE_DVD_CPRM = 267
IMAPI_FEATURE_PAGE_TYPE_FIRMWARE_INFORMATION = 268
IMAPI_FEATURE_PAGE_TYPE_AACS = 269
IMAPI_FEATURE_PAGE_TYPE_VCPS = 272
IMAPI_FORMAT2_DATA_MEDIA_STATE = Int32
IMAPI_FORMAT2_DATA_MEDIA_STATE_UNKNOWN = 0
IMAPI_FORMAT2_DATA_MEDIA_STATE_INFORMATIONAL_MASK = 15
IMAPI_FORMAT2_DATA_MEDIA_STATE_UNSUPPORTED_MASK = 64512
IMAPI_FORMAT2_DATA_MEDIA_STATE_OVERWRITE_ONLY = 1
IMAPI_FORMAT2_DATA_MEDIA_STATE_RANDOMLY_WRITABLE = 1
IMAPI_FORMAT2_DATA_MEDIA_STATE_BLANK = 2
IMAPI_FORMAT2_DATA_MEDIA_STATE_APPENDABLE = 4
IMAPI_FORMAT2_DATA_MEDIA_STATE_FINAL_SESSION = 8
IMAPI_FORMAT2_DATA_MEDIA_STATE_DAMAGED = 1024
IMAPI_FORMAT2_DATA_MEDIA_STATE_ERASE_REQUIRED = 2048
IMAPI_FORMAT2_DATA_MEDIA_STATE_NON_EMPTY_SESSION = 4096
IMAPI_FORMAT2_DATA_MEDIA_STATE_WRITE_PROTECTED = 8192
IMAPI_FORMAT2_DATA_MEDIA_STATE_FINALIZED = 16384
IMAPI_FORMAT2_DATA_MEDIA_STATE_UNSUPPORTED_MEDIA = 32768
IMAPI_FORMAT2_DATA_WRITE_ACTION = Int32
IMAPI_FORMAT2_DATA_WRITE_ACTION_VALIDATING_MEDIA = 0
IMAPI_FORMAT2_DATA_WRITE_ACTION_FORMATTING_MEDIA = 1
IMAPI_FORMAT2_DATA_WRITE_ACTION_INITIALIZING_HARDWARE = 2
IMAPI_FORMAT2_DATA_WRITE_ACTION_CALIBRATING_POWER = 3
IMAPI_FORMAT2_DATA_WRITE_ACTION_WRITING_DATA = 4
IMAPI_FORMAT2_DATA_WRITE_ACTION_FINALIZATION = 5
IMAPI_FORMAT2_DATA_WRITE_ACTION_COMPLETED = 6
IMAPI_FORMAT2_DATA_WRITE_ACTION_VERIFYING = 7
IMAPI_FORMAT2_RAW_CD_DATA_SECTOR_TYPE = Int32
IMAPI_FORMAT2_RAW_CD_SUBCODE_PQ_ONLY = 1
IMAPI_FORMAT2_RAW_CD_SUBCODE_IS_COOKED = 2
IMAPI_FORMAT2_RAW_CD_SUBCODE_IS_RAW = 3
IMAPI_FORMAT2_RAW_CD_WRITE_ACTION = Int32
IMAPI_FORMAT2_RAW_CD_WRITE_ACTION_UNKNOWN = 0
IMAPI_FORMAT2_RAW_CD_WRITE_ACTION_PREPARING = 1
IMAPI_FORMAT2_RAW_CD_WRITE_ACTION_WRITING = 2
IMAPI_FORMAT2_RAW_CD_WRITE_ACTION_FINISHING = 3
IMAPI_FORMAT2_TAO_WRITE_ACTION = Int32
IMAPI_FORMAT2_TAO_WRITE_ACTION_UNKNOWN = 0
IMAPI_FORMAT2_TAO_WRITE_ACTION_PREPARING = 1
IMAPI_FORMAT2_TAO_WRITE_ACTION_WRITING = 2
IMAPI_FORMAT2_TAO_WRITE_ACTION_FINISHING = 3
IMAPI_FORMAT2_TAO_WRITE_ACTION_VERIFYING = 4
IMAPI_MEDIA_PHYSICAL_TYPE = Int32
IMAPI_MEDIA_TYPE_UNKNOWN = 0
IMAPI_MEDIA_TYPE_CDROM = 1
IMAPI_MEDIA_TYPE_CDR = 2
IMAPI_MEDIA_TYPE_CDRW = 3
IMAPI_MEDIA_TYPE_DVDROM = 4
IMAPI_MEDIA_TYPE_DVDRAM = 5
IMAPI_MEDIA_TYPE_DVDPLUSR = 6
IMAPI_MEDIA_TYPE_DVDPLUSRW = 7
IMAPI_MEDIA_TYPE_DVDPLUSR_DUALLAYER = 8
IMAPI_MEDIA_TYPE_DVDDASHR = 9
IMAPI_MEDIA_TYPE_DVDDASHRW = 10
IMAPI_MEDIA_TYPE_DVDDASHR_DUALLAYER = 11
IMAPI_MEDIA_TYPE_DISK = 12
IMAPI_MEDIA_TYPE_DVDPLUSRW_DUALLAYER = 13
IMAPI_MEDIA_TYPE_HDDVDROM = 14
IMAPI_MEDIA_TYPE_HDDVDR = 15
IMAPI_MEDIA_TYPE_HDDVDRAM = 16
IMAPI_MEDIA_TYPE_BDROM = 17
IMAPI_MEDIA_TYPE_BDR = 18
IMAPI_MEDIA_TYPE_BDRE = 19
IMAPI_MEDIA_TYPE_MAX = 19
IMAPI_MEDIA_WRITE_PROTECT_STATE = Int32
IMAPI_WRITEPROTECTED_UNTIL_POWERDOWN = 1
IMAPI_WRITEPROTECTED_BY_CARTRIDGE = 2
IMAPI_WRITEPROTECTED_BY_MEDIA_SPECIFIC_REASON = 4
IMAPI_WRITEPROTECTED_BY_SOFTWARE_WRITE_PROTECT = 8
IMAPI_WRITEPROTECTED_BY_DISC_CONTROL_BLOCK = 16
IMAPI_WRITEPROTECTED_READ_ONLY_MEDIA = 16384
IMAPI_MODE_PAGE_REQUEST_TYPE = Int32
IMAPI_MODE_PAGE_REQUEST_TYPE_CURRENT_VALUES = 0
IMAPI_MODE_PAGE_REQUEST_TYPE_CHANGEABLE_VALUES = 1
IMAPI_MODE_PAGE_REQUEST_TYPE_DEFAULT_VALUES = 2
IMAPI_MODE_PAGE_REQUEST_TYPE_SAVED_VALUES = 3
IMAPI_MODE_PAGE_TYPE = Int32
IMAPI_MODE_PAGE_TYPE_READ_WRITE_ERROR_RECOVERY = 1
IMAPI_MODE_PAGE_TYPE_MRW = 3
IMAPI_MODE_PAGE_TYPE_WRITE_PARAMETERS = 5
IMAPI_MODE_PAGE_TYPE_CACHING = 8
IMAPI_MODE_PAGE_TYPE_INFORMATIONAL_EXCEPTIONS = 28
IMAPI_MODE_PAGE_TYPE_TIMEOUT_AND_PROTECT = 29
IMAPI_MODE_PAGE_TYPE_POWER_CONDITION = 26
IMAPI_MODE_PAGE_TYPE_LEGACY_CAPABILITIES = 42
IMAPI_PROFILE_TYPE = Int32
IMAPI_PROFILE_TYPE_INVALID = 0
IMAPI_PROFILE_TYPE_NON_REMOVABLE_DISK = 1
IMAPI_PROFILE_TYPE_REMOVABLE_DISK = 2
IMAPI_PROFILE_TYPE_MO_ERASABLE = 3
IMAPI_PROFILE_TYPE_MO_WRITE_ONCE = 4
IMAPI_PROFILE_TYPE_AS_MO = 5
IMAPI_PROFILE_TYPE_CDROM = 8
IMAPI_PROFILE_TYPE_CD_RECORDABLE = 9
IMAPI_PROFILE_TYPE_CD_REWRITABLE = 10
IMAPI_PROFILE_TYPE_DVDROM = 16
IMAPI_PROFILE_TYPE_DVD_DASH_RECORDABLE = 17
IMAPI_PROFILE_TYPE_DVD_RAM = 18
IMAPI_PROFILE_TYPE_DVD_DASH_REWRITABLE = 19
IMAPI_PROFILE_TYPE_DVD_DASH_RW_SEQUENTIAL = 20
IMAPI_PROFILE_TYPE_DVD_DASH_R_DUAL_SEQUENTIAL = 21
IMAPI_PROFILE_TYPE_DVD_DASH_R_DUAL_LAYER_JUMP = 22
IMAPI_PROFILE_TYPE_DVD_PLUS_RW = 26
IMAPI_PROFILE_TYPE_DVD_PLUS_R = 27
IMAPI_PROFILE_TYPE_DDCDROM = 32
IMAPI_PROFILE_TYPE_DDCD_RECORDABLE = 33
IMAPI_PROFILE_TYPE_DDCD_REWRITABLE = 34
IMAPI_PROFILE_TYPE_DVD_PLUS_RW_DUAL = 42
IMAPI_PROFILE_TYPE_DVD_PLUS_R_DUAL = 43
IMAPI_PROFILE_TYPE_BD_ROM = 64
IMAPI_PROFILE_TYPE_BD_R_SEQUENTIAL = 65
IMAPI_PROFILE_TYPE_BD_R_RANDOM_RECORDING = 66
IMAPI_PROFILE_TYPE_BD_REWRITABLE = 67
IMAPI_PROFILE_TYPE_HD_DVD_ROM = 80
IMAPI_PROFILE_TYPE_HD_DVD_RECORDABLE = 81
IMAPI_PROFILE_TYPE_HD_DVD_RAM = 82
IMAPI_PROFILE_TYPE_NON_STANDARD = 65535
IMAPI_READ_TRACK_ADDRESS_TYPE = Int32
IMAPI_READ_TRACK_ADDRESS_TYPE_LBA = 0
IMAPI_READ_TRACK_ADDRESS_TYPE_TRACK = 1
IMAPI_READ_TRACK_ADDRESS_TYPE_SESSION = 2
def _define_IMMP_MPV_STORE_DRIVER_HANDLE_head():
    class IMMP_MPV_STORE_DRIVER_HANDLE(Structure):
        pass
    return IMMP_MPV_STORE_DRIVER_HANDLE
def _define_IMMP_MPV_STORE_DRIVER_HANDLE():
    IMMP_MPV_STORE_DRIVER_HANDLE = win32more.Storage.Imapi.IMMP_MPV_STORE_DRIVER_HANDLE_head
    IMMP_MPV_STORE_DRIVER_HANDLE._fields_ = [
        ('guidSignature', Guid),
    ]
    return IMMP_MPV_STORE_DRIVER_HANDLE
IMMPID_CPV_ENUM = Int32
IMMPID_CPV_BEFORE__ = 32767
IMMPID_CP_START = 32768
IMMPID_CPV_AFTER__ = 32769
IMMPID_MP_ENUM = Int32
IMMPID_MP_BEFORE__ = 4095
IMMPID_MP_RECIPIENT_LIST = 4096
IMMPID_MP_CONTENT_FILE_NAME = 4097
IMMPID_MP_SENDER_ADDRESS_SMTP = 4098
IMMPID_MP_SENDER_ADDRESS_X500 = 4099
IMMPID_MP_SENDER_ADDRESS_X400 = 4100
IMMPID_MP_SENDER_ADDRESS_LEGACY_EX_DN = 4101
IMMPID_MP_DOMAIN_LIST = 4102
IMMPID_MP_PICKUP_FILE_NAME = 4103
IMMPID_MP_AUTHENTICATED_USER_NAME = 4104
IMMPID_MP_CONNECTION_IP_ADDRESS = 4105
IMMPID_MP_HELO_DOMAIN = 4106
IMMPID_MP_EIGHTBIT_MIME_OPTION = 4107
IMMPID_MP_CHUNKING_OPTION = 4108
IMMPID_MP_BINARYMIME_OPTION = 4109
IMMPID_MP_REMOTE_AUTHENTICATION_TYPE = 4110
IMMPID_MP_ERROR_CODE = 4111
IMMPID_MP_DSN_ENVID_VALUE = 4112
IMMPID_MP_DSN_RET_VALUE = 4113
IMMPID_MP_REMOTE_SERVER_DSN_CAPABLE = 4114
IMMPID_MP_ARRIVAL_TIME = 4115
IMMPID_MP_MESSAGE_STATUS = 4116
IMMPID_MP_EXPIRE_DELAY = 4117
IMMPID_MP_EXPIRE_NDR = 4118
IMMPID_MP_LOCAL_EXPIRE_DELAY = 4119
IMMPID_MP_LOCAL_EXPIRE_NDR = 4120
IMMPID_MP_ARRIVAL_FILETIME = 4121
IMMPID_MP_HR_CAT_STATUS = 4122
IMMPID_MP_MSG_GUID = 4123
IMMPID_MP_SUPERSEDES_MSG_GUID = 4124
IMMPID_MP_SCANNED_FOR_CRLF_DOT_CRLF = 4125
IMMPID_MP_FOUND_EMBEDDED_CRLF_DOT_CRLF = 4126
IMMPID_MP_MSG_SIZE_HINT = 4127
IMMPID_MP_RFC822_MSG_ID = 4128
IMMPID_MP_RFC822_MSG_SUBJECT = 4129
IMMPID_MP_RFC822_FROM_ADDRESS = 4130
IMMPID_MP_RFC822_TO_ADDRESS = 4131
IMMPID_MP_RFC822_CC_ADDRESS = 4132
IMMPID_MP_RFC822_BCC_ADDRESS = 4133
IMMPID_MP_CONNECTION_SERVER_IP_ADDRESS = 4134
IMMPID_MP_SERVER_NAME = 4135
IMMPID_MP_SERVER_VERSION = 4136
IMMPID_MP_NUM_RECIPIENTS = 4137
IMMPID_MP_X_PRIORITY = 4138
IMMPID_MP_FROM_ADDRESS = 4139
IMMPID_MP_SENDER_ADDRESS = 4140
IMMPID_MP_DEFERRED_DELIVERY_FILETIME = 4141
IMMPID_MP_SENDER_ADDRESS_OTHER = 4142
IMMPID_MP_ORIGINAL_ARRIVAL_TIME = 4143
IMMPID_MP_MSGCLASS = 4144
IMMPID_MP_CONTENT_TYPE = 4145
IMMPID_MP_ENCRYPTION_TYPE = 4146
IMMPID_MP_CONNECTION_SERVER_PORT = 4147
IMMPID_MP_CLIENT_AUTH_USER = 4148
IMMPID_MP_CLIENT_AUTH_TYPE = 4149
IMMPID_MP_CRC_GLOBAL = 4150
IMMPID_MP_CRC_RECIPS = 4151
IMMPID_MP_INBOUND_MAIL_FROM_AUTH = 4152
IMMPID_MP_AFTER__ = 4153
IMMPID_MPV_ENUM = Int32
IMMPID_MPV_BEFORE__ = 12287
IMMPID_MPV_STORE_DRIVER_HANDLE = 12288
IMMPID_MPV_MESSAGE_CREATION_FLAGS = 12289
IMMPID_MPV_MESSAGE_OPEN_HANDLES = 12290
IMMPID_MPV_TOTAL_OPEN_HANDLES = 12291
IMMPID_MPV_TOTAL_OPEN_PROPERTY_STREAM_HANDLES = 12292
IMMPID_MPV_TOTAL_OPEN_CONTENT_HANDLES = 12293
IMMPID_MPV_AFTER__ = 12294
IMMPID_NMP_ENUM = Int32
IMMPID_NMP_BEFORE__ = 24575
IMMPID_NMP_SECONDARY_GROUPS = 24576
IMMPID_NMP_SECONDARY_ARTNUM = 24577
IMMPID_NMP_PRIMARY_GROUP = 24578
IMMPID_NMP_PRIMARY_ARTID = 24579
IMMPID_NMP_POST_TOKEN = 24580
IMMPID_NMP_NEWSGROUP_LIST = 24581
IMMPID_NMP_HEADERS = 24582
IMMPID_NMP_NNTP_PROCESSING = 24583
IMMPID_NMP_NNTP_APPROVED_HEADER = 24584
IMMPID_NMP_AFTER__ = 24585
IMMPID_RP_ENUM = Int32
IMMPID_RP_BEFORE__ = 8191
IMMPID_RP_DSN_NOTIFY_SUCCESS = 8192
IMMPID_RP_DSN_NOTIFY_INVALID = 8193
IMMPID_RP_ADDRESS_TYPE = 8194
IMMPID_RP_ADDRESS = 8195
IMMPID_RP_ADDRESS_TYPE_SMTP = 8196
IMMPID_RP_ERROR_CODE = 8197
IMMPID_RP_ERROR_STRING = 8198
IMMPID_RP_DSN_NOTIFY_VALUE = 8199
IMMPID_RP_DSN_ORCPT_VALUE = 8200
IMMPID_RP_ADDRESS_SMTP = 8201
IMMPID_RP_ADDRESS_X400 = 8202
IMMPID_RP_ADDRESS_X500 = 8203
IMMPID_RP_LEGACY_EX_DN = 8204
IMMPID_RP_RECIPIENT_FLAGS = 8205
IMMPID_RP_SMTP_STATUS_STRING = 8206
IMMPID_RP_DSN_PRE_CAT_ADDRESS = 8207
IMMPID_RP_MDB_GUID = 8208
IMMPID_RP_USER_GUID = 8209
IMMPID_RP_DOMAIN = 8210
IMMPID_RP_ADDRESS_OTHER = 8211
IMMPID_RP_DISPLAY_NAME = 8212
IMMPID_RP_AFTER__ = 8213
IMMPID_RPV_ENUM = Int32
IMMPID_RPV_BEFORE__ = 16383
IMMPID_RPV_DONT_DELIVER = 16384
IMMPID_RPV_NO_NAME_COLLISIONS = 16385
IMMPID_RPV_AFTER__ = 16386
def _define_IMultisession_head():
    class IMultisession(win32more.System.Com.IDispatch_head):
        Guid = Guid('27354150-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
    return IMultisession
def _define_IMultisession():
    IMultisession = win32more.Storage.Imapi.IMultisession_head
    IMultisession.get_IsSupportedOnCurrentMediaState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(7, 'get_IsSupportedOnCurrentMediaState', ((1, 'value'),)))
    IMultisession.put_InUse = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(8, 'put_InUse', ((1, 'value'),)))
    IMultisession.get_InUse = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(9, 'get_InUse', ((1, 'value'),)))
    IMultisession.get_ImportRecorder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Imapi.IDiscRecorder2_head))(10, 'get_ImportRecorder', ((1, 'value'),)))
    win32more.System.Com.IDispatch
    return IMultisession
def _define_IMultisessionRandomWrite_head():
    class IMultisessionRandomWrite(win32more.Storage.Imapi.IMultisession_head):
        Guid = Guid('b507ca23-2204-11dd-96-6a-00-1a-a0-1b-bc-58')
    return IMultisessionRandomWrite
def _define_IMultisessionRandomWrite():
    IMultisessionRandomWrite = win32more.Storage.Imapi.IMultisessionRandomWrite_head
    IMultisessionRandomWrite.get_WriteUnitSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(11, 'get_WriteUnitSize', ((1, 'value'),)))
    IMultisessionRandomWrite.get_LastWrittenAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(12, 'get_LastWrittenAddress', ((1, 'value'),)))
    IMultisessionRandomWrite.get_TotalSectorsOnMedia = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(13, 'get_TotalSectorsOnMedia', ((1, 'value'),)))
    win32more.Storage.Imapi.IMultisession
    return IMultisessionRandomWrite
def _define_IMultisessionSequential_head():
    class IMultisessionSequential(win32more.Storage.Imapi.IMultisession_head):
        Guid = Guid('27354151-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
    return IMultisessionSequential
def _define_IMultisessionSequential():
    IMultisessionSequential = win32more.Storage.Imapi.IMultisessionSequential_head
    IMultisessionSequential.get_IsFirstDataSession = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(11, 'get_IsFirstDataSession', ((1, 'value'),)))
    IMultisessionSequential.get_StartAddressOfPreviousSession = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(12, 'get_StartAddressOfPreviousSession', ((1, 'value'),)))
    IMultisessionSequential.get_LastWrittenAddressOfPreviousSession = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(13, 'get_LastWrittenAddressOfPreviousSession', ((1, 'value'),)))
    IMultisessionSequential.get_NextWritableAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(14, 'get_NextWritableAddress', ((1, 'value'),)))
    IMultisessionSequential.get_FreeSectorsOnMedia = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(15, 'get_FreeSectorsOnMedia', ((1, 'value'),)))
    win32more.Storage.Imapi.IMultisession
    return IMultisessionSequential
def _define_IMultisessionSequential2_head():
    class IMultisessionSequential2(win32more.Storage.Imapi.IMultisessionSequential_head):
        Guid = Guid('b507ca22-2204-11dd-96-6a-00-1a-a0-1b-bc-58')
    return IMultisessionSequential2
def _define_IMultisessionSequential2():
    IMultisessionSequential2 = win32more.Storage.Imapi.IMultisessionSequential2_head
    IMultisessionSequential2.get_WriteUnitSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(16, 'get_WriteUnitSize', ((1, 'value'),)))
    win32more.Storage.Imapi.IMultisessionSequential
    return IMultisessionSequential2
def _define_IProgressItem_head():
    class IProgressItem(win32more.System.Com.IDispatch_head):
        Guid = Guid('2c941fd5-975b-59be-a9-60-9a-2a-26-28-53-a5')
    return IProgressItem
def _define_IProgressItem():
    IProgressItem = win32more.Storage.Imapi.IProgressItem_head
    IProgressItem.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_Description', ((1, 'desc'),)))
    IProgressItem.get_FirstBlock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(8, 'get_FirstBlock', ((1, 'block'),)))
    IProgressItem.get_LastBlock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(9, 'get_LastBlock', ((1, 'block'),)))
    IProgressItem.get_BlockCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(10, 'get_BlockCount', ((1, 'blocks'),)))
    win32more.System.Com.IDispatch
    return IProgressItem
def _define_IProgressItems_head():
    class IProgressItems(win32more.System.Com.IDispatch_head):
        Guid = Guid('2c941fd7-975b-59be-a9-60-9a-2a-26-28-53-a5')
    return IProgressItems
def _define_IProgressItems():
    IProgressItems = win32more.Storage.Imapi.IProgressItems_head
    IProgressItems.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.IEnumVARIANT_head))(7, 'get__NewEnum', ((1, 'NewEnum'),)))
    IProgressItems.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Storage.Imapi.IProgressItem_head))(8, 'get_Item', ((1, 'Index'),(1, 'item'),)))
    IProgressItems.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(9, 'get_Count', ((1, 'Count'),)))
    IProgressItems.ProgressItemFromBlock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Storage.Imapi.IProgressItem_head))(10, 'ProgressItemFromBlock', ((1, 'block'),(1, 'item'),)))
    IProgressItems.ProgressItemFromDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Storage.Imapi.IProgressItem_head))(11, 'ProgressItemFromDescription', ((1, 'description'),(1, 'item'),)))
    IProgressItems.get_EnumProgressItems = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Imapi.IEnumProgressItems_head))(12, 'get_EnumProgressItems', ((1, 'NewEnum'),)))
    win32more.System.Com.IDispatch
    return IProgressItems
def _define_IRawCDImageCreator_head():
    class IRawCDImageCreator(win32more.System.Com.IDispatch_head):
        Guid = Guid('25983550-9d65-49ce-b3-35-40-63-0d-90-12-27')
    return IRawCDImageCreator
def _define_IRawCDImageCreator():
    IRawCDImageCreator = win32more.Storage.Imapi.IRawCDImageCreator_head
    IRawCDImageCreator.CreateResultImage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IStream_head))(7, 'CreateResultImage', ((1, 'resultStream'),)))
    IRawCDImageCreator.AddTrack = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Imapi.IMAPI_CD_SECTOR_TYPE,win32more.System.Com.IStream_head,POINTER(Int32))(8, 'AddTrack', ((1, 'dataType'),(1, 'data'),(1, 'trackIndex'),)))
    IRawCDImageCreator.AddSpecialPregap = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head)(9, 'AddSpecialPregap', ((1, 'data'),)))
    IRawCDImageCreator.AddSubcodeRWGenerator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head)(10, 'AddSubcodeRWGenerator', ((1, 'subcode'),)))
    IRawCDImageCreator.put_ResultingImageType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Imapi.IMAPI_FORMAT2_RAW_CD_DATA_SECTOR_TYPE)(11, 'put_ResultingImageType', ((1, 'value'),)))
    IRawCDImageCreator.get_ResultingImageType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Imapi.IMAPI_FORMAT2_RAW_CD_DATA_SECTOR_TYPE))(12, 'get_ResultingImageType', ((1, 'value'),)))
    IRawCDImageCreator.get_StartOfLeadout = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(13, 'get_StartOfLeadout', ((1, 'value'),)))
    IRawCDImageCreator.put_StartOfLeadoutLimit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(14, 'put_StartOfLeadoutLimit', ((1, 'value'),)))
    IRawCDImageCreator.get_StartOfLeadoutLimit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(15, 'get_StartOfLeadoutLimit', ((1, 'value'),)))
    IRawCDImageCreator.put_DisableGaplessAudio = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(16, 'put_DisableGaplessAudio', ((1, 'value'),)))
    IRawCDImageCreator.get_DisableGaplessAudio = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(17, 'get_DisableGaplessAudio', ((1, 'value'),)))
    IRawCDImageCreator.put_MediaCatalogNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(18, 'put_MediaCatalogNumber', ((1, 'value'),)))
    IRawCDImageCreator.get_MediaCatalogNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(19, 'get_MediaCatalogNumber', ((1, 'value'),)))
    IRawCDImageCreator.put_StartingTrackNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(20, 'put_StartingTrackNumber', ((1, 'value'),)))
    IRawCDImageCreator.get_StartingTrackNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(21, 'get_StartingTrackNumber', ((1, 'value'),)))
    IRawCDImageCreator.get_TrackInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Storage.Imapi.IRawCDImageTrackInfo_head))(22, 'get_TrackInfo', ((1, 'trackIndex'),(1, 'value'),)))
    IRawCDImageCreator.get_NumberOfExistingTracks = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(23, 'get_NumberOfExistingTracks', ((1, 'value'),)))
    IRawCDImageCreator.get_LastUsedUserSectorInImage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(24, 'get_LastUsedUserSectorInImage', ((1, 'value'),)))
    IRawCDImageCreator.get_ExpectedTableOfContents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(25, 'get_ExpectedTableOfContents', ((1, 'value'),)))
    win32more.System.Com.IDispatch
    return IRawCDImageCreator
def _define_IRawCDImageTrackInfo_head():
    class IRawCDImageTrackInfo(win32more.System.Com.IDispatch_head):
        Guid = Guid('25983551-9d65-49ce-b3-35-40-63-0d-90-12-27')
    return IRawCDImageTrackInfo
def _define_IRawCDImageTrackInfo():
    IRawCDImageTrackInfo = win32more.Storage.Imapi.IRawCDImageTrackInfo_head
    IRawCDImageTrackInfo.get_StartingLba = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_StartingLba', ((1, 'value'),)))
    IRawCDImageTrackInfo.get_SectorCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(8, 'get_SectorCount', ((1, 'value'),)))
    IRawCDImageTrackInfo.get_TrackNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(9, 'get_TrackNumber', ((1, 'value'),)))
    IRawCDImageTrackInfo.get_SectorType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Imapi.IMAPI_CD_SECTOR_TYPE))(10, 'get_SectorType', ((1, 'value'),)))
    IRawCDImageTrackInfo.get_ISRC = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(11, 'get_ISRC', ((1, 'value'),)))
    IRawCDImageTrackInfo.put_ISRC = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(12, 'put_ISRC', ((1, 'value'),)))
    IRawCDImageTrackInfo.get_DigitalAudioCopySetting = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Imapi.IMAPI_CD_TRACK_DIGITAL_COPY_SETTING))(13, 'get_DigitalAudioCopySetting', ((1, 'value'),)))
    IRawCDImageTrackInfo.put_DigitalAudioCopySetting = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Imapi.IMAPI_CD_TRACK_DIGITAL_COPY_SETTING)(14, 'put_DigitalAudioCopySetting', ((1, 'value'),)))
    IRawCDImageTrackInfo.get_AudioHasPreemphasis = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(15, 'get_AudioHasPreemphasis', ((1, 'value'),)))
    IRawCDImageTrackInfo.put_AudioHasPreemphasis = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(16, 'put_AudioHasPreemphasis', ((1, 'value'),)))
    IRawCDImageTrackInfo.get_TrackIndexes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(17, 'get_TrackIndexes', ((1, 'value'),)))
    IRawCDImageTrackInfo.AddTrackIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(18, 'AddTrackIndex', ((1, 'lbaOffset'),)))
    IRawCDImageTrackInfo.ClearTrackIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(19, 'ClearTrackIndex', ((1, 'lbaOffset'),)))
    win32more.System.Com.IDispatch
    return IRawCDImageTrackInfo
def _define_IRedbookDiscMaster_head():
    class IRedbookDiscMaster(win32more.System.Com.IUnknown_head):
        Guid = Guid('e3bc42cd-4e5c-11d3-91-44-00-10-4b-a1-1c-5e')
    return IRedbookDiscMaster
def _define_IRedbookDiscMaster():
    IRedbookDiscMaster = win32more.Storage.Imapi.IRedbookDiscMaster_head
    IRedbookDiscMaster.GetTotalAudioTracks = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(3, 'GetTotalAudioTracks', ((1, 'pnTracks'),)))
    IRedbookDiscMaster.GetTotalAudioBlocks = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(4, 'GetTotalAudioBlocks', ((1, 'pnBlocks'),)))
    IRedbookDiscMaster.GetUsedAudioBlocks = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(5, 'GetUsedAudioBlocks', ((1, 'pnBlocks'),)))
    IRedbookDiscMaster.GetAvailableAudioTrackBlocks = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(6, 'GetAvailableAudioTrackBlocks', ((1, 'pnBlocks'),)))
    IRedbookDiscMaster.GetAudioBlockSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'GetAudioBlockSize', ((1, 'pnBlockBytes'),)))
    IRedbookDiscMaster.CreateAudioTrack = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(8, 'CreateAudioTrack', ((1, 'nBlocks'),)))
    IRedbookDiscMaster.AddAudioTrackBlocks = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,Int32)(9, 'AddAudioTrackBlocks', ((1, 'pby'),(1, 'cb'),)))
    IRedbookDiscMaster.CloseAudioTrack = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(10, 'CloseAudioTrack', ()))
    win32more.System.Com.IUnknown
    return IRedbookDiscMaster
def _define_IStreamConcatenate_head():
    class IStreamConcatenate(win32more.System.Com.IStream_head):
        Guid = Guid('27354146-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
    return IStreamConcatenate
def _define_IStreamConcatenate():
    IStreamConcatenate = win32more.Storage.Imapi.IStreamConcatenate_head
    IStreamConcatenate.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.System.Com.IStream_head)(14, 'Initialize', ((1, 'stream1'),(1, 'stream2'),)))
    IStreamConcatenate.Initialize2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IStream_head),UInt32)(15, 'Initialize2', ((1, 'streams'),(1, 'streamCount'),)))
    IStreamConcatenate.Append = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head)(16, 'Append', ((1, 'stream'),)))
    IStreamConcatenate.Append2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IStream_head),UInt32)(17, 'Append2', ((1, 'streams'),(1, 'streamCount'),)))
    win32more.System.Com.IStream
    return IStreamConcatenate
def _define_IStreamInterleave_head():
    class IStreamInterleave(win32more.System.Com.IStream_head):
        Guid = Guid('27354147-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
    return IStreamInterleave
def _define_IStreamInterleave():
    IStreamInterleave = win32more.Storage.Imapi.IStreamInterleave_head
    IStreamInterleave.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IStream_head),POINTER(UInt32),UInt32)(14, 'Initialize', ((1, 'streams'),(1, 'interleaveSizes'),(1, 'streamCount'),)))
    win32more.System.Com.IStream
    return IStreamInterleave
def _define_IStreamPseudoRandomBased_head():
    class IStreamPseudoRandomBased(win32more.System.Com.IStream_head):
        Guid = Guid('27354145-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
    return IStreamPseudoRandomBased
def _define_IStreamPseudoRandomBased():
    IStreamPseudoRandomBased = win32more.Storage.Imapi.IStreamPseudoRandomBased_head
    IStreamPseudoRandomBased.put_Seed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(14, 'put_Seed', ((1, 'value'),)))
    IStreamPseudoRandomBased.get_Seed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(15, 'get_Seed', ((1, 'value'),)))
    IStreamPseudoRandomBased.put_ExtendedSeed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),UInt32)(16, 'put_ExtendedSeed', ((1, 'values'),(1, 'eCount'),)))
    IStreamPseudoRandomBased.get_ExtendedSeed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(UInt32)),POINTER(UInt32))(17, 'get_ExtendedSeed', ((1, 'values'),(1, 'eCount'),)))
    win32more.System.Com.IStream
    return IStreamPseudoRandomBased
def _define_IWriteEngine2_head():
    class IWriteEngine2(win32more.System.Com.IDispatch_head):
        Guid = Guid('27354135-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
    return IWriteEngine2
def _define_IWriteEngine2():
    IWriteEngine2 = win32more.Storage.Imapi.IWriteEngine2_head
    IWriteEngine2.WriteSection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,Int32,Int32)(7, 'WriteSection', ((1, 'data'),(1, 'startingBlockAddress'),(1, 'numberOfBlocks'),)))
    IWriteEngine2.CancelWrite = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(8, 'CancelWrite', ()))
    IWriteEngine2.put_Recorder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Imapi.IDiscRecorder2Ex_head)(9, 'put_Recorder', ((1, 'value'),)))
    IWriteEngine2.get_Recorder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Imapi.IDiscRecorder2Ex_head))(10, 'get_Recorder', ((1, 'value'),)))
    IWriteEngine2.put_UseStreamingWrite12 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(11, 'put_UseStreamingWrite12', ((1, 'value'),)))
    IWriteEngine2.get_UseStreamingWrite12 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(12, 'get_UseStreamingWrite12', ((1, 'value'),)))
    IWriteEngine2.put_StartingSectorsPerSecond = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(13, 'put_StartingSectorsPerSecond', ((1, 'value'),)))
    IWriteEngine2.get_StartingSectorsPerSecond = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(14, 'get_StartingSectorsPerSecond', ((1, 'value'),)))
    IWriteEngine2.put_EndingSectorsPerSecond = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(15, 'put_EndingSectorsPerSecond', ((1, 'value'),)))
    IWriteEngine2.get_EndingSectorsPerSecond = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(16, 'get_EndingSectorsPerSecond', ((1, 'value'),)))
    IWriteEngine2.put_BytesPerSector = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(17, 'put_BytesPerSector', ((1, 'value'),)))
    IWriteEngine2.get_BytesPerSector = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(18, 'get_BytesPerSector', ((1, 'value'),)))
    IWriteEngine2.get_WriteInProgress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(19, 'get_WriteInProgress', ((1, 'value'),)))
    win32more.System.Com.IDispatch
    return IWriteEngine2
def _define_IWriteEngine2EventArgs_head():
    class IWriteEngine2EventArgs(win32more.System.Com.IDispatch_head):
        Guid = Guid('27354136-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
    return IWriteEngine2EventArgs
def _define_IWriteEngine2EventArgs():
    IWriteEngine2EventArgs = win32more.Storage.Imapi.IWriteEngine2EventArgs_head
    IWriteEngine2EventArgs.get_StartLba = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_StartLba', ((1, 'value'),)))
    IWriteEngine2EventArgs.get_SectorCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(8, 'get_SectorCount', ((1, 'value'),)))
    IWriteEngine2EventArgs.get_LastReadLba = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(9, 'get_LastReadLba', ((1, 'value'),)))
    IWriteEngine2EventArgs.get_LastWrittenLba = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(10, 'get_LastWrittenLba', ((1, 'value'),)))
    IWriteEngine2EventArgs.get_TotalSystemBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(11, 'get_TotalSystemBuffer', ((1, 'value'),)))
    IWriteEngine2EventArgs.get_UsedSystemBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(12, 'get_UsedSystemBuffer', ((1, 'value'),)))
    IWriteEngine2EventArgs.get_FreeSystemBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(13, 'get_FreeSystemBuffer', ((1, 'value'),)))
    win32more.System.Com.IDispatch
    return IWriteEngine2EventArgs
def _define_IWriteSpeedDescriptor_head():
    class IWriteSpeedDescriptor(win32more.System.Com.IDispatch_head):
        Guid = Guid('27354144-7f64-5b0f-8f-00-5d-77-af-be-26-1e')
    return IWriteSpeedDescriptor
def _define_IWriteSpeedDescriptor():
    IWriteSpeedDescriptor = win32more.Storage.Imapi.IWriteSpeedDescriptor_head
    IWriteSpeedDescriptor.get_MediaType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Imapi.IMAPI_MEDIA_PHYSICAL_TYPE))(7, 'get_MediaType', ((1, 'value'),)))
    IWriteSpeedDescriptor.get_RotationTypeIsPureCAV = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(8, 'get_RotationTypeIsPureCAV', ((1, 'value'),)))
    IWriteSpeedDescriptor.get_WriteSpeed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(9, 'get_WriteSpeed', ((1, 'value'),)))
    win32more.System.Com.IDispatch
    return IWriteSpeedDescriptor
MEDIA_FLAGS = Int32
MEDIA_BLANK = 1
MEDIA_RW = 2
MEDIA_WRITABLE = 4
MEDIA_FORMAT_UNUSABLE_BY_IMAPI = 8
MEDIA_TYPES = Int32
MEDIA_CDDA_CDROM = 1
MEDIA_CD_ROM_XA = 2
MEDIA_CD_I = 3
MEDIA_CD_EXTRA = 4
MEDIA_CD_OTHER = 5
MEDIA_SPECIAL = 6
MSDiscMasterObj = Guid('520cca63-51a5-11d3-91-44-00-10-4b-a1-1c-5e')
MSDiscRecorderObj = Guid('520cca61-51a5-11d3-91-44-00-10-4b-a1-1c-5e')
MSEnumDiscRecordersObj = Guid('8a03567a-63cb-4ba8-ba-f6-52-11-98-16-d1-ef')
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
def _define_MSGCALLRELEASE():
    return WINFUNCTYPE(Void,UInt32,win32more.System.AddressBook.IMessage_head)
PlatformId = Int32
PlatformId_PlatformX86 = 0
PlatformId_PlatformPowerPC = 1
PlatformId_PlatformMac = 2
PlatformId_PlatformEFI = 239
ProgressItem = Guid('2c941fcb-975b-59be-a9-60-9a-2a-26-28-53-a5')
ProgressItems = Guid('2c941fc9-975b-59be-a9-60-9a-2a-26-28-53-a5')
RECORDER_TYPES = Int32
RECORDER_CDR = 1
RECORDER_CDRW = 2
def _define_SPropAttrArray_head():
    class SPropAttrArray(Structure):
        pass
    return SPropAttrArray
def _define_SPropAttrArray():
    SPropAttrArray = win32more.Storage.Imapi.SPropAttrArray_head
    SPropAttrArray._fields_ = [
        ('cValues', UInt32),
        ('aPropAttr', UInt32 * 1),
    ]
    return SPropAttrArray
tagIMMPID_CPV_STRUCT = Guid('a2a76b2a-e52d-11d1-aa-64-00-c0-4f-a3-5b-82')
def _define_tagIMMPID_GUIDLIST_ITEM_head():
    class tagIMMPID_GUIDLIST_ITEM(Structure):
        pass
    return tagIMMPID_GUIDLIST_ITEM
def _define_tagIMMPID_GUIDLIST_ITEM():
    tagIMMPID_GUIDLIST_ITEM = win32more.Storage.Imapi.tagIMMPID_GUIDLIST_ITEM_head
    tagIMMPID_GUIDLIST_ITEM._fields_ = [
        ('pguid', POINTER(Guid)),
        ('dwStart', UInt32),
        ('dwLast', UInt32),
    ]
    return tagIMMPID_GUIDLIST_ITEM
tagIMMPID_MP_STRUCT = Guid('13384cf0-b3c4-11d1-aa-92-00-aa-00-6b-c8-0b')
tagIMMPID_MPV_STRUCT = Guid('cbe69706-c9bd-11d1-9f-f2-00-c0-4f-a3-73-48')
tagIMMPID_NMP_STRUCT = Guid('7433a9aa-20e2-11d2-94-d6-00-c0-4f-a3-79-f1')
tagIMMPID_RP_STRUCT = Guid('79e82048-d320-11d1-9f-f4-00-c0-4f-a3-73-48')
tagIMMPID_RPV_STRUCT = Guid('79e82049-d320-11d1-9f-f4-00-c0-4f-a3-73-48')
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
