from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Graphics.Gdi
import win32more.Media.PictureAcquisition
import win32more.System.Com
import win32more.System.Com.StructuredStorage
import win32more.UI.Shell.PropertiesSystem
import win32more.UI.WindowsAndMessaging
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
def _define_PKEY_PhotoAcquire_RelativePathname():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('00f23377-7ac6-4b7a-84-43-34-5e-73-1f-a5-7a'), pid=2)
def _define_PKEY_PhotoAcquire_FinalFilename():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('00f23377-7ac6-4b7a-84-43-34-5e-73-1f-a5-7a'), pid=3)
def _define_PKEY_PhotoAcquire_GroupTag():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('00f23377-7ac6-4b7a-84-43-34-5e-73-1f-a5-7a'), pid=4)
def _define_PKEY_PhotoAcquire_TransferResult():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('00f23377-7ac6-4b7a-84-43-34-5e-73-1f-a5-7a'), pid=5)
def _define_PKEY_PhotoAcquire_OriginalFilename():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('00f23377-7ac6-4b7a-84-43-34-5e-73-1f-a5-7a'), pid=6)
def _define_PKEY_PhotoAcquire_CameraSequenceNumber():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('00f23377-7ac6-4b7a-84-43-34-5e-73-1f-a5-7a'), pid=7)
def _define_PKEY_PhotoAcquire_IntermediateFile():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('00f23377-7ac6-4b7a-84-43-34-5e-73-1f-a5-7a'), pid=8)
def _define_PKEY_PhotoAcquire_SkipImport():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('00f23377-7ac6-4b7a-84-43-34-5e-73-1f-a5-7a'), pid=9)
def _define_PKEY_PhotoAcquire_DuplicateDetectionID():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('00f23377-7ac6-4b7a-84-43-34-5e-73-1f-a5-7a'), pid=10)
PROGRESS_INDETERMINATE = -1
PHOTOACQ_ERROR_RESTART_REQUIRED = -2147180543
PHOTOACQ_RUN_DEFAULT = 0
PHOTOACQ_NO_GALLERY_LAUNCH = 1
PHOTOACQ_DISABLE_AUTO_ROTATE = 2
PHOTOACQ_DISABLE_PLUGINS = 4
PHOTOACQ_DISABLE_GROUP_TAG_PROMPT = 8
PHOTOACQ_DISABLE_DB_INTEGRATION = 16
PHOTOACQ_DELETE_AFTER_ACQUIRE = 32
PHOTOACQ_DISABLE_DUPLICATE_DETECTION = 64
PHOTOACQ_ENABLE_THUMBNAIL_CACHING = 128
PHOTOACQ_DISABLE_METADATA_WRITE = 256
PHOTOACQ_DISABLE_THUMBNAIL_PROGRESS = 512
PHOTOACQ_DISABLE_SETTINGS_LINK = 1024
PHOTOACQ_ABORT_ON_SETTINGS_UPDATE = 2048
PHOTOACQ_IMPORT_VIDEO_AS_MULTIPLE_FILES = 4096
DSF_WPD_DEVICES = 1
DSF_WIA_CAMERAS = 2
DSF_WIA_SCANNERS = 4
DSF_STI_DEVICES = 8
DSF_TWAIN_DEVICES = 16
DSF_FS_DEVICES = 32
DSF_DV_DEVICES = 64
DSF_ALL_DEVICES = 65535
DSF_CPL_MODE = 65536
DSF_SHOW_OFFLINE = 131072
PAPS_PRESAVE = 0
PAPS_POSTSAVE = 1
PAPS_CLEANUP = 2
DEVICE_SELECTION_DEVICE_TYPE = Int32
DST_UNKNOWN_DEVICE = 0
DST_WPD_DEVICE = 1
DST_WIA_DEVICE = 2
DST_STI_DEVICE = 3
DSF_TWAIN_DEVICE = 4
DST_FS_DEVICE = 5
DST_DV_DEVICE = 6
ERROR_ADVISE_MESSAGE_TYPE = Int32
PHOTOACQUIRE_ERROR_SKIPRETRYCANCEL = 0
PHOTOACQUIRE_ERROR_RETRYCANCEL = 1
PHOTOACQUIRE_ERROR_YESNO = 2
PHOTOACQUIRE_ERROR_OK = 3
ERROR_ADVISE_RESULT = Int32
PHOTOACQUIRE_RESULT_YES = 0
PHOTOACQUIRE_RESULT_NO = 1
PHOTOACQUIRE_RESULT_OK = 2
PHOTOACQUIRE_RESULT_SKIP = 3
PHOTOACQUIRE_RESULT_SKIP_ALL = 4
PHOTOACQUIRE_RESULT_RETRY = 5
PHOTOACQUIRE_RESULT_ABORT = 6
def _define_IPhotoAcquire_head():
    class IPhotoAcquire(win32more.System.Com.IUnknown_head):
        Guid = Guid('00f23353-e31b-4955-a8-ad-ca-5e-bf-31-e2-ce')
    return IPhotoAcquire
def _define_IPhotoAcquire():
    IPhotoAcquire = win32more.Media.PictureAcquisition.IPhotoAcquire_head
    IPhotoAcquire.CreatePhotoSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Media.PictureAcquisition.IPhotoAcquireSource_head))(3, 'CreatePhotoSource', ((1, 'pszDevice'),(1, 'ppPhotoAcquireSource'),)))
    IPhotoAcquire.Acquire = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.PictureAcquisition.IPhotoAcquireSource_head,win32more.Foundation.BOOL,win32more.Foundation.HWND,win32more.Foundation.PWSTR,win32more.Media.PictureAcquisition.IPhotoAcquireProgressCB_head)(4, 'Acquire', ((1, 'pPhotoAcquireSource'),(1, 'fShowProgress'),(1, 'hWndParent'),(1, 'pszApplicationName'),(1, 'pPhotoAcquireProgressCB'),)))
    IPhotoAcquire.EnumResults = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IEnumString_head))(5, 'EnumResults', ((1, 'ppEnumFilePaths'),)))
    win32more.System.Com.IUnknown
    return IPhotoAcquire
def _define_IPhotoAcquireDeviceSelectionDialog_head():
    class IPhotoAcquireDeviceSelectionDialog(win32more.System.Com.IUnknown_head):
        Guid = Guid('00f28837-55dd-4f37-aa-f5-68-55-a9-64-04-67')
    return IPhotoAcquireDeviceSelectionDialog
def _define_IPhotoAcquireDeviceSelectionDialog():
    IPhotoAcquireDeviceSelectionDialog = win32more.Media.PictureAcquisition.IPhotoAcquireDeviceSelectionDialog_head
    IPhotoAcquireDeviceSelectionDialog.SetTitle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(3, 'SetTitle', ((1, 'pszTitle'),)))
    IPhotoAcquireDeviceSelectionDialog.SetSubmitButtonText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(4, 'SetSubmitButtonText', ((1, 'pszSubmitButtonText'),)))
    IPhotoAcquireDeviceSelectionDialog.DoModal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32,POINTER(win32more.Foundation.BSTR),POINTER(win32more.Media.PictureAcquisition.DEVICE_SELECTION_DEVICE_TYPE))(5, 'DoModal', ((1, 'hWndParent'),(1, 'dwDeviceFlags'),(1, 'pbstrDeviceId'),(1, 'pnDeviceType'),)))
    win32more.System.Com.IUnknown
    return IPhotoAcquireDeviceSelectionDialog
def _define_IPhotoAcquireItem_head():
    class IPhotoAcquireItem(win32more.System.Com.IUnknown_head):
        Guid = Guid('00f21c97-28bf-4c02-b8-42-5e-4e-90-13-9a-30')
    return IPhotoAcquireItem
def _define_IPhotoAcquireItem():
    IPhotoAcquireItem = win32more.Media.PictureAcquisition.IPhotoAcquireItem_head
    IPhotoAcquireItem.GetItemName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(3, 'GetItemName', ((1, 'pbstrItemName'),)))
    IPhotoAcquireItem.GetThumbnail = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.SIZE,POINTER(win32more.Graphics.Gdi.HBITMAP))(4, 'GetThumbnail', ((1, 'sizeThumbnail'),(1, 'phbmpThumbnail'),)))
    IPhotoAcquireItem.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(5, 'GetProperty', ((1, 'key'),(1, 'pv'),)))
    IPhotoAcquireItem.SetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(6, 'SetProperty', ((1, 'key'),(1, 'pv'),)))
    IPhotoAcquireItem.GetStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IStream_head))(7, 'GetStream', ((1, 'ppStream'),)))
    IPhotoAcquireItem.CanDelete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(8, 'CanDelete', ((1, 'pfCanDelete'),)))
    IPhotoAcquireItem.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(9, 'Delete', ()))
    IPhotoAcquireItem.GetSubItemCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(10, 'GetSubItemCount', ((1, 'pnCount'),)))
    IPhotoAcquireItem.GetSubItemAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.PictureAcquisition.IPhotoAcquireItem_head))(11, 'GetSubItemAt', ((1, 'nItemIndex'),(1, 'ppPhotoAcquireItem'),)))
    win32more.System.Com.IUnknown
    return IPhotoAcquireItem
def _define_IPhotoAcquireOptionsDialog_head():
    class IPhotoAcquireOptionsDialog(win32more.System.Com.IUnknown_head):
        Guid = Guid('00f2b3ee-bf64-47ee-89-f4-4d-ed-d7-96-43-f2')
    return IPhotoAcquireOptionsDialog
def _define_IPhotoAcquireOptionsDialog():
    IPhotoAcquireOptionsDialog = win32more.Media.PictureAcquisition.IPhotoAcquireOptionsDialog_head
    IPhotoAcquireOptionsDialog.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(3, 'Initialize', ((1, 'pszRegistryRoot'),)))
    IPhotoAcquireOptionsDialog.Create = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(win32more.Foundation.HWND))(4, 'Create', ((1, 'hWndParent'),(1, 'phWndDialog'),)))
    IPhotoAcquireOptionsDialog.Destroy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Destroy', ()))
    IPhotoAcquireOptionsDialog.DoModal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(IntPtr))(6, 'DoModal', ((1, 'hWndParent'),(1, 'ppnReturnCode'),)))
    IPhotoAcquireOptionsDialog.SaveData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(7, 'SaveData', ()))
    win32more.System.Com.IUnknown
    return IPhotoAcquireOptionsDialog
def _define_IPhotoAcquirePlugin_head():
    class IPhotoAcquirePlugin(win32more.System.Com.IUnknown_head):
        Guid = Guid('00f2dceb-ecb8-4f77-8e-47-e7-a9-87-c8-3d-d0')
    return IPhotoAcquirePlugin
def _define_IPhotoAcquirePlugin():
    IPhotoAcquirePlugin = win32more.Media.PictureAcquisition.IPhotoAcquirePlugin_head
    IPhotoAcquirePlugin.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.PictureAcquisition.IPhotoAcquireSource_head,win32more.Media.PictureAcquisition.IPhotoAcquireProgressCB_head)(3, 'Initialize', ((1, 'pPhotoAcquireSource'),(1, 'pPhotoAcquireProgressCB'),)))
    IPhotoAcquirePlugin.ProcessItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Media.PictureAcquisition.IPhotoAcquireItem_head,win32more.System.Com.IStream_head,win32more.Foundation.PWSTR,win32more.UI.Shell.PropertiesSystem.IPropertyStore_head)(4, 'ProcessItem', ((1, 'dwAcquireStage'),(1, 'pPhotoAcquireItem'),(1, 'pOriginalItemStream'),(1, 'pszFinalFilename'),(1, 'pPropertyStore'),)))
    IPhotoAcquirePlugin.TransferComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT)(5, 'TransferComplete', ((1, 'hr'),)))
    IPhotoAcquirePlugin.DisplayConfigureDialog = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND)(6, 'DisplayConfigureDialog', ((1, 'hWndParent'),)))
    win32more.System.Com.IUnknown
    return IPhotoAcquirePlugin
def _define_IPhotoAcquireProgressCB_head():
    class IPhotoAcquireProgressCB(win32more.System.Com.IUnknown_head):
        Guid = Guid('00f2ce1e-935e-4248-89-2c-13-0f-32-c4-5c-b4')
    return IPhotoAcquireProgressCB
def _define_IPhotoAcquireProgressCB():
    IPhotoAcquireProgressCB = win32more.Media.PictureAcquisition.IPhotoAcquireProgressCB_head
    IPhotoAcquireProgressCB.Cancelled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(3, 'Cancelled', ((1, 'pfCancelled'),)))
    IPhotoAcquireProgressCB.StartEnumeration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.PictureAcquisition.IPhotoAcquireSource_head)(4, 'StartEnumeration', ((1, 'pPhotoAcquireSource'),)))
    IPhotoAcquireProgressCB.FoundItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.PictureAcquisition.IPhotoAcquireItem_head)(5, 'FoundItem', ((1, 'pPhotoAcquireItem'),)))
    IPhotoAcquireProgressCB.EndEnumeration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT)(6, 'EndEnumeration', ((1, 'hr'),)))
    IPhotoAcquireProgressCB.StartTransfer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.PictureAcquisition.IPhotoAcquireSource_head)(7, 'StartTransfer', ((1, 'pPhotoAcquireSource'),)))
    IPhotoAcquireProgressCB.StartItemTransfer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Media.PictureAcquisition.IPhotoAcquireItem_head)(8, 'StartItemTransfer', ((1, 'nItemIndex'),(1, 'pPhotoAcquireItem'),)))
    IPhotoAcquireProgressCB.DirectoryCreated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(9, 'DirectoryCreated', ((1, 'pszDirectory'),)))
    IPhotoAcquireProgressCB.UpdateTransferPercent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,UInt32)(10, 'UpdateTransferPercent', ((1, 'fOverall'),(1, 'nPercent'),)))
    IPhotoAcquireProgressCB.EndItemTransfer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Media.PictureAcquisition.IPhotoAcquireItem_head,win32more.Foundation.HRESULT)(11, 'EndItemTransfer', ((1, 'nItemIndex'),(1, 'pPhotoAcquireItem'),(1, 'hr'),)))
    IPhotoAcquireProgressCB.EndTransfer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT)(12, 'EndTransfer', ((1, 'hr'),)))
    IPhotoAcquireProgressCB.StartDelete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.PictureAcquisition.IPhotoAcquireSource_head)(13, 'StartDelete', ((1, 'pPhotoAcquireSource'),)))
    IPhotoAcquireProgressCB.StartItemDelete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Media.PictureAcquisition.IPhotoAcquireItem_head)(14, 'StartItemDelete', ((1, 'nItemIndex'),(1, 'pPhotoAcquireItem'),)))
    IPhotoAcquireProgressCB.UpdateDeletePercent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(15, 'UpdateDeletePercent', ((1, 'nPercent'),)))
    IPhotoAcquireProgressCB.EndItemDelete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Media.PictureAcquisition.IPhotoAcquireItem_head,win32more.Foundation.HRESULT)(16, 'EndItemDelete', ((1, 'nItemIndex'),(1, 'pPhotoAcquireItem'),(1, 'hr'),)))
    IPhotoAcquireProgressCB.EndDelete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT)(17, 'EndDelete', ((1, 'hr'),)))
    IPhotoAcquireProgressCB.EndSession = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT)(18, 'EndSession', ((1, 'hr'),)))
    IPhotoAcquireProgressCB.GetDeleteAfterAcquire = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(19, 'GetDeleteAfterAcquire', ((1, 'pfDeleteAfterAcquire'),)))
    IPhotoAcquireProgressCB.ErrorAdvise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Media.PictureAcquisition.ERROR_ADVISE_MESSAGE_TYPE,POINTER(win32more.Media.PictureAcquisition.ERROR_ADVISE_RESULT))(20, 'ErrorAdvise', ((1, 'hr'),(1, 'pszErrorMessage'),(1, 'nMessageType'),(1, 'pnErrorAdviseResult'),)))
    IPhotoAcquireProgressCB.GetUserInput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IUnknown_head,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(21, 'GetUserInput', ((1, 'riidType'),(1, 'pUnknown'),(1, 'pPropVarResult'),(1, 'pPropVarDefault'),)))
    win32more.System.Com.IUnknown
    return IPhotoAcquireProgressCB
def _define_IPhotoAcquireSettings_head():
    class IPhotoAcquireSettings(win32more.System.Com.IUnknown_head):
        Guid = Guid('00f2b868-dd67-487c-95-53-04-92-40-76-7e-91')
    return IPhotoAcquireSettings
def _define_IPhotoAcquireSettings():
    IPhotoAcquireSettings = win32more.Media.PictureAcquisition.IPhotoAcquireSettings_head
    IPhotoAcquireSettings.InitializeFromRegistry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(3, 'InitializeFromRegistry', ((1, 'pszRegistryKey'),)))
    IPhotoAcquireSettings.SetFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'SetFlags', ((1, 'dwPhotoAcquireFlags'),)))
    IPhotoAcquireSettings.SetOutputFilenameTemplate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(5, 'SetOutputFilenameTemplate', ((1, 'pszTemplate'),)))
    IPhotoAcquireSettings.SetSequencePaddingWidth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(6, 'SetSequencePaddingWidth', ((1, 'dwWidth'),)))
    IPhotoAcquireSettings.SetSequenceZeroPadding = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(7, 'SetSequenceZeroPadding', ((1, 'fZeroPad'),)))
    IPhotoAcquireSettings.SetGroupTag = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(8, 'SetGroupTag', ((1, 'pszGroupTag'),)))
    IPhotoAcquireSettings.SetAcquisitionTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.FILETIME_head))(9, 'SetAcquisitionTime', ((1, 'pftAcquisitionTime'),)))
    IPhotoAcquireSettings.GetFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(10, 'GetFlags', ((1, 'pdwPhotoAcquireFlags'),)))
    IPhotoAcquireSettings.GetOutputFilenameTemplate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(11, 'GetOutputFilenameTemplate', ((1, 'pbstrTemplate'),)))
    IPhotoAcquireSettings.GetSequencePaddingWidth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(12, 'GetSequencePaddingWidth', ((1, 'pdwWidth'),)))
    IPhotoAcquireSettings.GetSequenceZeroPadding = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(13, 'GetSequenceZeroPadding', ((1, 'pfZeroPad'),)))
    IPhotoAcquireSettings.GetGroupTag = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(14, 'GetGroupTag', ((1, 'pbstrGroupTag'),)))
    IPhotoAcquireSettings.GetAcquisitionTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.FILETIME_head))(15, 'GetAcquisitionTime', ((1, 'pftAcquisitionTime'),)))
    win32more.System.Com.IUnknown
    return IPhotoAcquireSettings
def _define_IPhotoAcquireSource_head():
    class IPhotoAcquireSource(win32more.System.Com.IUnknown_head):
        Guid = Guid('00f2c703-8613-4282-a5-3b-6e-c5-9c-58-83-ac')
    return IPhotoAcquireSource
def _define_IPhotoAcquireSource():
    IPhotoAcquireSource = win32more.Media.PictureAcquisition.IPhotoAcquireSource_head
    IPhotoAcquireSource.GetFriendlyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(3, 'GetFriendlyName', ((1, 'pbstrFriendlyName'),)))
    IPhotoAcquireSource.GetDeviceIcons = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.WindowsAndMessaging.HICON),POINTER(win32more.UI.WindowsAndMessaging.HICON))(4, 'GetDeviceIcons', ((1, 'nSize'),(1, 'phLargeIcon'),(1, 'phSmallIcon'),)))
    IPhotoAcquireSource.InitializeItemList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,win32more.Media.PictureAcquisition.IPhotoAcquireProgressCB_head,POINTER(UInt32))(5, 'InitializeItemList', ((1, 'fForceEnumeration'),(1, 'pPhotoAcquireProgressCB'),(1, 'pnItemCount'),)))
    IPhotoAcquireSource.GetItemCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(6, 'GetItemCount', ((1, 'pnItemCount'),)))
    IPhotoAcquireSource.GetItemAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.PictureAcquisition.IPhotoAcquireItem_head))(7, 'GetItemAt', ((1, 'nIndex'),(1, 'ppPhotoAcquireItem'),)))
    IPhotoAcquireSource.GetPhotoAcquireSettings = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.PictureAcquisition.IPhotoAcquireSettings_head))(8, 'GetPhotoAcquireSettings', ((1, 'ppPhotoAcquireSettings'),)))
    IPhotoAcquireSource.GetDeviceId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'GetDeviceId', ((1, 'pbstrDeviceId'),)))
    IPhotoAcquireSource.BindToObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p))(10, 'BindToObject', ((1, 'riid'),(1, 'ppv'),)))
    win32more.System.Com.IUnknown
    return IPhotoAcquireSource
def _define_IPhotoProgressActionCB_head():
    class IPhotoProgressActionCB(win32more.System.Com.IUnknown_head):
        Guid = Guid('00f242d0-b206-4e7d-b4-c1-47-55-bc-bb-9c-9f')
    return IPhotoProgressActionCB
def _define_IPhotoProgressActionCB():
    IPhotoProgressActionCB = win32more.Media.PictureAcquisition.IPhotoProgressActionCB_head
    IPhotoProgressActionCB.DoAction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND)(3, 'DoAction', ((1, 'hWndParent'),)))
    win32more.System.Com.IUnknown
    return IPhotoProgressActionCB
def _define_IPhotoProgressDialog_head():
    class IPhotoProgressDialog(win32more.System.Com.IUnknown_head):
        Guid = Guid('00f246f9-0750-4f08-93-81-2c-d8-e9-06-a4-ae')
    return IPhotoProgressDialog
def _define_IPhotoProgressDialog():
    IPhotoProgressDialog = win32more.Media.PictureAcquisition.IPhotoProgressDialog_head
    IPhotoProgressDialog.Create = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND)(3, 'Create', ((1, 'hwndParent'),)))
    IPhotoProgressDialog.GetWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HWND))(4, 'GetWindow', ((1, 'phwndProgressDialog'),)))
    IPhotoProgressDialog.Destroy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Destroy', ()))
    IPhotoProgressDialog.SetTitle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(6, 'SetTitle', ((1, 'pszTitle'),)))
    IPhotoProgressDialog.ShowCheckbox = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.PictureAcquisition.PROGRESS_DIALOG_CHECKBOX_ID,win32more.Foundation.BOOL)(7, 'ShowCheckbox', ((1, 'nCheckboxId'),(1, 'fShow'),)))
    IPhotoProgressDialog.SetCheckboxText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.PictureAcquisition.PROGRESS_DIALOG_CHECKBOX_ID,win32more.Foundation.PWSTR)(8, 'SetCheckboxText', ((1, 'nCheckboxId'),(1, 'pszCheckboxText'),)))
    IPhotoProgressDialog.SetCheckboxCheck = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.PictureAcquisition.PROGRESS_DIALOG_CHECKBOX_ID,win32more.Foundation.BOOL)(9, 'SetCheckboxCheck', ((1, 'nCheckboxId'),(1, 'fChecked'),)))
    IPhotoProgressDialog.SetCheckboxTooltip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.PictureAcquisition.PROGRESS_DIALOG_CHECKBOX_ID,win32more.Foundation.PWSTR)(10, 'SetCheckboxTooltip', ((1, 'nCheckboxId'),(1, 'pszCheckboxTooltipText'),)))
    IPhotoProgressDialog.IsCheckboxChecked = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.PictureAcquisition.PROGRESS_DIALOG_CHECKBOX_ID,POINTER(win32more.Foundation.BOOL))(11, 'IsCheckboxChecked', ((1, 'nCheckboxId'),(1, 'pfChecked'),)))
    IPhotoProgressDialog.SetCaption = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(12, 'SetCaption', ((1, 'pszTitle'),)))
    IPhotoProgressDialog.SetImage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.PictureAcquisition.PROGRESS_DIALOG_IMAGE_TYPE,win32more.UI.WindowsAndMessaging.HICON,win32more.Graphics.Gdi.HBITMAP)(13, 'SetImage', ((1, 'nImageType'),(1, 'hIcon'),(1, 'hBitmap'),)))
    IPhotoProgressDialog.SetPercentComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(14, 'SetPercentComplete', ((1, 'nPercent'),)))
    IPhotoProgressDialog.SetProgressText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(15, 'SetProgressText', ((1, 'pszProgressText'),)))
    IPhotoProgressDialog.SetActionLinkCallback = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.PictureAcquisition.IPhotoProgressActionCB_head)(16, 'SetActionLinkCallback', ((1, 'pPhotoProgressActionCB'),)))
    IPhotoProgressDialog.SetActionLinkText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(17, 'SetActionLinkText', ((1, 'pszCaption'),)))
    IPhotoProgressDialog.ShowActionLink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(18, 'ShowActionLink', ((1, 'fShow'),)))
    IPhotoProgressDialog.IsCancelled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(19, 'IsCancelled', ((1, 'pfCancelled'),)))
    IPhotoProgressDialog.GetUserInput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IUnknown_head,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(20, 'GetUserInput', ((1, 'riidType'),(1, 'pUnknown'),(1, 'pPropVarResult'),(1, 'pPropVarDefault'),)))
    win32more.System.Com.IUnknown
    return IPhotoProgressDialog
def _define_IUserInputString_head():
    class IUserInputString(win32more.System.Com.IUnknown_head):
        Guid = Guid('00f243a1-205b-45ba-ae-26-ab-bc-53-aa-7a-6f')
    return IUserInputString
def _define_IUserInputString():
    IUserInputString = win32more.Media.PictureAcquisition.IUserInputString_head
    IUserInputString.GetSubmitButtonText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(3, 'GetSubmitButtonText', ((1, 'pbstrSubmitButtonText'),)))
    IUserInputString.GetPrompt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(4, 'GetPrompt', ((1, 'pbstrPromptTitle'),)))
    IUserInputString.GetStringId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(5, 'GetStringId', ((1, 'pbstrStringId'),)))
    IUserInputString.GetStringType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.PictureAcquisition.USER_INPUT_STRING_TYPE))(6, 'GetStringType', ((1, 'pnStringType'),)))
    IUserInputString.GetTooltipText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'GetTooltipText', ((1, 'pbstrTooltipText'),)))
    IUserInputString.GetMaxLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(8, 'GetMaxLength', ((1, 'pcchMaxLength'),)))
    IUserInputString.GetDefault = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'GetDefault', ((1, 'pbstrDefault'),)))
    IUserInputString.GetMruCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(10, 'GetMruCount', ((1, 'pnMruCount'),)))
    IUserInputString.GetMruEntryAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.BSTR))(11, 'GetMruEntryAt', ((1, 'nIndex'),(1, 'pbstrMruEntry'),)))
    IUserInputString.GetImage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Gdi.HBITMAP),POINTER(win32more.UI.WindowsAndMessaging.HICON))(12, 'GetImage', ((1, 'nSize'),(1, 'phBitmap'),(1, 'phIcon'),)))
    win32more.System.Com.IUnknown
    return IUserInputString
PhotoAcquire = Guid('00f26e02-e9f2-4a9f-9f-dd-5a-96-2f-b2-6a-98')
PhotoAcquireAutoPlayDropTarget = Guid('00f20eb5-8fd6-4d9d-b7-5e-36-80-17-66-c8-f1')
PhotoAcquireAutoPlayHWEventHandler = Guid('00f2b433-44e4-4d88-b2-b0-26-98-a0-a9-1d-ba')
PhotoAcquireDeviceSelectionDialog = Guid('00f29a34-b8a1-482c-bc-f8-3a-c7-b0-fe-8f-62')
PhotoAcquireOptionsDialog = Guid('00f210a1-62f0-438b-9f-7e-96-18-d7-2a-18-31')
PhotoProgressDialog = Guid('00f24ca0-748f-4e8a-89-4f-0e-03-57-c6-79-9f')
PROGRESS_DIALOG_CHECKBOX_ID = Int32
PROGRESS_DIALOG_CHECKBOX_ID_DEFAULT = 0
PROGRESS_DIALOG_IMAGE_TYPE = Int32
PROGRESS_DIALOG_ICON_SMALL = 0
PROGRESS_DIALOG_ICON_LARGE = 1
PROGRESS_DIALOG_ICON_THUMBNAIL = 2
PROGRESS_DIALOG_BITMAP_THUMBNAIL = 3
USER_INPUT_STRING_TYPE = Int32
USER_INPUT_DEFAULT = 0
USER_INPUT_PATH_ELEMENT = 1
__all__ = [
    "DEVICE_SELECTION_DEVICE_TYPE",
    "DSF_ALL_DEVICES",
    "DSF_CPL_MODE",
    "DSF_DV_DEVICES",
    "DSF_FS_DEVICES",
    "DSF_SHOW_OFFLINE",
    "DSF_STI_DEVICES",
    "DSF_TWAIN_DEVICE",
    "DSF_TWAIN_DEVICES",
    "DSF_WIA_CAMERAS",
    "DSF_WIA_SCANNERS",
    "DSF_WPD_DEVICES",
    "DST_DV_DEVICE",
    "DST_FS_DEVICE",
    "DST_STI_DEVICE",
    "DST_UNKNOWN_DEVICE",
    "DST_WIA_DEVICE",
    "DST_WPD_DEVICE",
    "ERROR_ADVISE_MESSAGE_TYPE",
    "ERROR_ADVISE_RESULT",
    "IPhotoAcquire",
    "IPhotoAcquireDeviceSelectionDialog",
    "IPhotoAcquireItem",
    "IPhotoAcquireOptionsDialog",
    "IPhotoAcquirePlugin",
    "IPhotoAcquireProgressCB",
    "IPhotoAcquireSettings",
    "IPhotoAcquireSource",
    "IPhotoProgressActionCB",
    "IPhotoProgressDialog",
    "IUserInputString",
    "PAPS_CLEANUP",
    "PAPS_POSTSAVE",
    "PAPS_PRESAVE",
    "PHOTOACQUIRE_ERROR_OK",
    "PHOTOACQUIRE_ERROR_RETRYCANCEL",
    "PHOTOACQUIRE_ERROR_SKIPRETRYCANCEL",
    "PHOTOACQUIRE_ERROR_YESNO",
    "PHOTOACQUIRE_RESULT_ABORT",
    "PHOTOACQUIRE_RESULT_NO",
    "PHOTOACQUIRE_RESULT_OK",
    "PHOTOACQUIRE_RESULT_RETRY",
    "PHOTOACQUIRE_RESULT_SKIP",
    "PHOTOACQUIRE_RESULT_SKIP_ALL",
    "PHOTOACQUIRE_RESULT_YES",
    "PHOTOACQ_ABORT_ON_SETTINGS_UPDATE",
    "PHOTOACQ_DELETE_AFTER_ACQUIRE",
    "PHOTOACQ_DISABLE_AUTO_ROTATE",
    "PHOTOACQ_DISABLE_DB_INTEGRATION",
    "PHOTOACQ_DISABLE_DUPLICATE_DETECTION",
    "PHOTOACQ_DISABLE_GROUP_TAG_PROMPT",
    "PHOTOACQ_DISABLE_METADATA_WRITE",
    "PHOTOACQ_DISABLE_PLUGINS",
    "PHOTOACQ_DISABLE_SETTINGS_LINK",
    "PHOTOACQ_DISABLE_THUMBNAIL_PROGRESS",
    "PHOTOACQ_ENABLE_THUMBNAIL_CACHING",
    "PHOTOACQ_ERROR_RESTART_REQUIRED",
    "PHOTOACQ_IMPORT_VIDEO_AS_MULTIPLE_FILES",
    "PHOTOACQ_NO_GALLERY_LAUNCH",
    "PHOTOACQ_RUN_DEFAULT",
    "PKEY_PhotoAcquire_CameraSequenceNumber",
    "PKEY_PhotoAcquire_DuplicateDetectionID",
    "PKEY_PhotoAcquire_FinalFilename",
    "PKEY_PhotoAcquire_GroupTag",
    "PKEY_PhotoAcquire_IntermediateFile",
    "PKEY_PhotoAcquire_OriginalFilename",
    "PKEY_PhotoAcquire_RelativePathname",
    "PKEY_PhotoAcquire_SkipImport",
    "PKEY_PhotoAcquire_TransferResult",
    "PROGRESS_DIALOG_BITMAP_THUMBNAIL",
    "PROGRESS_DIALOG_CHECKBOX_ID",
    "PROGRESS_DIALOG_CHECKBOX_ID_DEFAULT",
    "PROGRESS_DIALOG_ICON_LARGE",
    "PROGRESS_DIALOG_ICON_SMALL",
    "PROGRESS_DIALOG_ICON_THUMBNAIL",
    "PROGRESS_DIALOG_IMAGE_TYPE",
    "PROGRESS_INDETERMINATE",
    "PhotoAcquire",
    "PhotoAcquireAutoPlayDropTarget",
    "PhotoAcquireAutoPlayHWEventHandler",
    "PhotoAcquireDeviceSelectionDialog",
    "PhotoAcquireOptionsDialog",
    "PhotoProgressDialog",
    "USER_INPUT_DEFAULT",
    "USER_INPUT_PATH_ELEMENT",
    "USER_INPUT_STRING_TYPE",
]
