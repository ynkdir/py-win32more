from win32more import *
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
        f = globals()[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
PKEY_PhotoAcquire_RelativePathname = PROPERTYKEY(Fmtid='00f23377-7ac6-4b7a-8443-345e731fa57a', Pid=2)
PKEY_PhotoAcquire_FinalFilename = PROPERTYKEY(Fmtid='00f23377-7ac6-4b7a-8443-345e731fa57a', Pid=3)
PKEY_PhotoAcquire_GroupTag = PROPERTYKEY(Fmtid='00f23377-7ac6-4b7a-8443-345e731fa57a', Pid=4)
PKEY_PhotoAcquire_TransferResult = PROPERTYKEY(Fmtid='00f23377-7ac6-4b7a-8443-345e731fa57a', Pid=5)
PKEY_PhotoAcquire_OriginalFilename = PROPERTYKEY(Fmtid='00f23377-7ac6-4b7a-8443-345e731fa57a', Pid=6)
PKEY_PhotoAcquire_CameraSequenceNumber = PROPERTYKEY(Fmtid='00f23377-7ac6-4b7a-8443-345e731fa57a', Pid=7)
PKEY_PhotoAcquire_IntermediateFile = PROPERTYKEY(Fmtid='00f23377-7ac6-4b7a-8443-345e731fa57a', Pid=8)
PKEY_PhotoAcquire_SkipImport = PROPERTYKEY(Fmtid='00f23377-7ac6-4b7a-8443-345e731fa57a', Pid=9)
PKEY_PhotoAcquire_DuplicateDetectionID = PROPERTYKEY(Fmtid='00f23377-7ac6-4b7a-8443-345e731fa57a', Pid=10)
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
PhotoAcquire = Guid('00f26e02-e9f2-4a9f-9fdd-5a962fb26a98')
PhotoAcquireAutoPlayDropTarget = Guid('00f20eb5-8fd6-4d9d-b75e-36801766c8f1')
PhotoAcquireAutoPlayHWEventHandler = Guid('00f2b433-44e4-4d88-b2b0-2698a0a91dba')
PhotoAcquireOptionsDialog = Guid('00f210a1-62f0-438b-9f7e-9618d72a1831')
PhotoProgressDialog = Guid('00f24ca0-748f-4e8a-894f-0e0357c6799f')
PhotoAcquireDeviceSelectionDialog = Guid('00f29a34-b8a1-482c-bcf8-3ac7b0fe8f62')
def _define_IPhotoAcquireItem_head():
    class IPhotoAcquireItem(win32more.System.Com.IUnknown_head):
        Guid = Guid('00f21c97-28bf-4c02-b842-5e4e90139a30')
    return IPhotoAcquireItem
def _define_IPhotoAcquireItem():
    IPhotoAcquireItem = win32more.Media.PictureAcquisition.IPhotoAcquireItem_head
    IPhotoAcquireItem.GetItemName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(3, 'GetItemName', ((1, 'pbstrItemName'),)))
    IPhotoAcquireItem.GetThumbnail = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.SIZE,POINTER(win32more.Graphics.Gdi.HBITMAP), use_last_error=False)(4, 'GetThumbnail', ((1, 'sizeThumbnail'),(1, 'phbmpThumbnail'),)))
    IPhotoAcquireItem.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(5, 'GetProperty', ((1, 'key'),(1, 'pv'),)))
    IPhotoAcquireItem.SetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(6, 'SetProperty', ((1, 'key'),(1, 'pv'),)))
    IPhotoAcquireItem.GetStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IStream_head), use_last_error=False)(7, 'GetStream', ((1, 'ppStream'),)))
    IPhotoAcquireItem.CanDelete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(8, 'CanDelete', ((1, 'pfCanDelete'),)))
    IPhotoAcquireItem.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(9, 'Delete', ()))
    IPhotoAcquireItem.GetSubItemCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(10, 'GetSubItemCount', ((1, 'pnCount'),)))
    IPhotoAcquireItem.GetSubItemAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.PictureAcquisition.IPhotoAcquireItem_head), use_last_error=False)(11, 'GetSubItemAt', ((1, 'nItemIndex'),(1, 'ppPhotoAcquireItem'),)))
    return IPhotoAcquireItem
USER_INPUT_STRING_TYPE = Int32
USER_INPUT_DEFAULT = 0
USER_INPUT_PATH_ELEMENT = 1
def _define_IUserInputString_head():
    class IUserInputString(win32more.System.Com.IUnknown_head):
        Guid = Guid('00f243a1-205b-45ba-ae26-abbc53aa7a6f')
    return IUserInputString
def _define_IUserInputString():
    IUserInputString = win32more.Media.PictureAcquisition.IUserInputString_head
    IUserInputString.GetSubmitButtonText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(3, 'GetSubmitButtonText', ((1, 'pbstrSubmitButtonText'),)))
    IUserInputString.GetPrompt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(4, 'GetPrompt', ((1, 'pbstrPromptTitle'),)))
    IUserInputString.GetStringId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(5, 'GetStringId', ((1, 'pbstrStringId'),)))
    IUserInputString.GetStringType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.PictureAcquisition.USER_INPUT_STRING_TYPE), use_last_error=False)(6, 'GetStringType', ((1, 'pnStringType'),)))
    IUserInputString.GetTooltipText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'GetTooltipText', ((1, 'pbstrTooltipText'),)))
    IUserInputString.GetMaxLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(8, 'GetMaxLength', ((1, 'pcchMaxLength'),)))
    IUserInputString.GetDefault = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'GetDefault', ((1, 'pbstrDefault'),)))
    IUserInputString.GetMruCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(10, 'GetMruCount', ((1, 'pnMruCount'),)))
    IUserInputString.GetMruEntryAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'GetMruEntryAt', ((1, 'nIndex'),(1, 'pbstrMruEntry'),)))
    IUserInputString.GetImage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Gdi.HBITMAP),POINTER(win32more.UI.WindowsAndMessaging.HICON), use_last_error=False)(12, 'GetImage', ((1, 'nSize'),(1, 'phBitmap'),(1, 'phIcon'),)))
    return IUserInputString
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
def _define_IPhotoAcquireProgressCB_head():
    class IPhotoAcquireProgressCB(win32more.System.Com.IUnknown_head):
        Guid = Guid('00f2ce1e-935e-4248-892c-130f32c45cb4')
    return IPhotoAcquireProgressCB
def _define_IPhotoAcquireProgressCB():
    IPhotoAcquireProgressCB = win32more.Media.PictureAcquisition.IPhotoAcquireProgressCB_head
    IPhotoAcquireProgressCB.Cancelled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'Cancelled', ((1, 'pfCancelled'),)))
    IPhotoAcquireProgressCB.StartEnumeration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.PictureAcquisition.IPhotoAcquireSource_head, use_last_error=False)(4, 'StartEnumeration', ((1, 'pPhotoAcquireSource'),)))
    IPhotoAcquireProgressCB.FoundItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.PictureAcquisition.IPhotoAcquireItem_head, use_last_error=False)(5, 'FoundItem', ((1, 'pPhotoAcquireItem'),)))
    IPhotoAcquireProgressCB.EndEnumeration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT, use_last_error=False)(6, 'EndEnumeration', ((1, 'hr'),)))
    IPhotoAcquireProgressCB.StartTransfer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.PictureAcquisition.IPhotoAcquireSource_head, use_last_error=False)(7, 'StartTransfer', ((1, 'pPhotoAcquireSource'),)))
    IPhotoAcquireProgressCB.StartItemTransfer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Media.PictureAcquisition.IPhotoAcquireItem_head, use_last_error=False)(8, 'StartItemTransfer', ((1, 'nItemIndex'),(1, 'pPhotoAcquireItem'),)))
    IPhotoAcquireProgressCB.DirectoryCreated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(9, 'DirectoryCreated', ((1, 'pszDirectory'),)))
    IPhotoAcquireProgressCB.UpdateTransferPercent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,UInt32, use_last_error=False)(10, 'UpdateTransferPercent', ((1, 'fOverall'),(1, 'nPercent'),)))
    IPhotoAcquireProgressCB.EndItemTransfer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Media.PictureAcquisition.IPhotoAcquireItem_head,win32more.Foundation.HRESULT, use_last_error=False)(11, 'EndItemTransfer', ((1, 'nItemIndex'),(1, 'pPhotoAcquireItem'),(1, 'hr'),)))
    IPhotoAcquireProgressCB.EndTransfer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT, use_last_error=False)(12, 'EndTransfer', ((1, 'hr'),)))
    IPhotoAcquireProgressCB.StartDelete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.PictureAcquisition.IPhotoAcquireSource_head, use_last_error=False)(13, 'StartDelete', ((1, 'pPhotoAcquireSource'),)))
    IPhotoAcquireProgressCB.StartItemDelete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Media.PictureAcquisition.IPhotoAcquireItem_head, use_last_error=False)(14, 'StartItemDelete', ((1, 'nItemIndex'),(1, 'pPhotoAcquireItem'),)))
    IPhotoAcquireProgressCB.UpdateDeletePercent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(15, 'UpdateDeletePercent', ((1, 'nPercent'),)))
    IPhotoAcquireProgressCB.EndItemDelete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Media.PictureAcquisition.IPhotoAcquireItem_head,win32more.Foundation.HRESULT, use_last_error=False)(16, 'EndItemDelete', ((1, 'nItemIndex'),(1, 'pPhotoAcquireItem'),(1, 'hr'),)))
    IPhotoAcquireProgressCB.EndDelete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT, use_last_error=False)(17, 'EndDelete', ((1, 'hr'),)))
    IPhotoAcquireProgressCB.EndSession = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT, use_last_error=False)(18, 'EndSession', ((1, 'hr'),)))
    IPhotoAcquireProgressCB.GetDeleteAfterAcquire = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(19, 'GetDeleteAfterAcquire', ((1, 'pfDeleteAfterAcquire'),)))
    IPhotoAcquireProgressCB.ErrorAdvise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Media.PictureAcquisition.ERROR_ADVISE_MESSAGE_TYPE,POINTER(win32more.Media.PictureAcquisition.ERROR_ADVISE_RESULT), use_last_error=False)(20, 'ErrorAdvise', ((1, 'hr'),(1, 'pszErrorMessage'),(1, 'nMessageType'),(1, 'pnErrorAdviseResult'),)))
    IPhotoAcquireProgressCB.GetUserInput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IUnknown_head,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(21, 'GetUserInput', ((1, 'riidType'),(1, 'pUnknown'),(1, 'pPropVarResult'),(1, 'pPropVarDefault'),)))
    return IPhotoAcquireProgressCB
def _define_IPhotoProgressActionCB_head():
    class IPhotoProgressActionCB(win32more.System.Com.IUnknown_head):
        Guid = Guid('00f242d0-b206-4e7d-b4c1-4755bcbb9c9f')
    return IPhotoProgressActionCB
def _define_IPhotoProgressActionCB():
    IPhotoProgressActionCB = win32more.Media.PictureAcquisition.IPhotoProgressActionCB_head
    IPhotoProgressActionCB.DoAction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND, use_last_error=False)(3, 'DoAction', ((1, 'hWndParent'),)))
    return IPhotoProgressActionCB
PROGRESS_DIALOG_IMAGE_TYPE = Int32
PROGRESS_DIALOG_ICON_SMALL = 0
PROGRESS_DIALOG_ICON_LARGE = 1
PROGRESS_DIALOG_ICON_THUMBNAIL = 2
PROGRESS_DIALOG_BITMAP_THUMBNAIL = 3
PROGRESS_DIALOG_CHECKBOX_ID = Int32
PROGRESS_DIALOG_CHECKBOX_ID_DEFAULT = 0
def _define_IPhotoProgressDialog_head():
    class IPhotoProgressDialog(win32more.System.Com.IUnknown_head):
        Guid = Guid('00f246f9-0750-4f08-9381-2cd8e906a4ae')
    return IPhotoProgressDialog
def _define_IPhotoProgressDialog():
    IPhotoProgressDialog = win32more.Media.PictureAcquisition.IPhotoProgressDialog_head
    IPhotoProgressDialog.Create = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND, use_last_error=False)(3, 'Create', ((1, 'hwndParent'),)))
    IPhotoProgressDialog.GetWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HWND), use_last_error=False)(4, 'GetWindow', ((1, 'phwndProgressDialog'),)))
    IPhotoProgressDialog.Destroy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Destroy', ()))
    IPhotoProgressDialog.SetTitle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(6, 'SetTitle', ((1, 'pszTitle'),)))
    IPhotoProgressDialog.ShowCheckbox = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.PictureAcquisition.PROGRESS_DIALOG_CHECKBOX_ID,win32more.Foundation.BOOL, use_last_error=False)(7, 'ShowCheckbox', ((1, 'nCheckboxId'),(1, 'fShow'),)))
    IPhotoProgressDialog.SetCheckboxText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.PictureAcquisition.PROGRESS_DIALOG_CHECKBOX_ID,win32more.Foundation.PWSTR, use_last_error=False)(8, 'SetCheckboxText', ((1, 'nCheckboxId'),(1, 'pszCheckboxText'),)))
    IPhotoProgressDialog.SetCheckboxCheck = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.PictureAcquisition.PROGRESS_DIALOG_CHECKBOX_ID,win32more.Foundation.BOOL, use_last_error=False)(9, 'SetCheckboxCheck', ((1, 'nCheckboxId'),(1, 'fChecked'),)))
    IPhotoProgressDialog.SetCheckboxTooltip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.PictureAcquisition.PROGRESS_DIALOG_CHECKBOX_ID,win32more.Foundation.PWSTR, use_last_error=False)(10, 'SetCheckboxTooltip', ((1, 'nCheckboxId'),(1, 'pszCheckboxTooltipText'),)))
    IPhotoProgressDialog.IsCheckboxChecked = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.PictureAcquisition.PROGRESS_DIALOG_CHECKBOX_ID,POINTER(win32more.Foundation.BOOL), use_last_error=False)(11, 'IsCheckboxChecked', ((1, 'nCheckboxId'),(1, 'pfChecked'),)))
    IPhotoProgressDialog.SetCaption = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(12, 'SetCaption', ((1, 'pszTitle'),)))
    IPhotoProgressDialog.SetImage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.PictureAcquisition.PROGRESS_DIALOG_IMAGE_TYPE,win32more.UI.WindowsAndMessaging.HICON,win32more.Graphics.Gdi.HBITMAP, use_last_error=False)(13, 'SetImage', ((1, 'nImageType'),(1, 'hIcon'),(1, 'hBitmap'),)))
    IPhotoProgressDialog.SetPercentComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(14, 'SetPercentComplete', ((1, 'nPercent'),)))
    IPhotoProgressDialog.SetProgressText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(15, 'SetProgressText', ((1, 'pszProgressText'),)))
    IPhotoProgressDialog.SetActionLinkCallback = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.PictureAcquisition.IPhotoProgressActionCB_head, use_last_error=False)(16, 'SetActionLinkCallback', ((1, 'pPhotoProgressActionCB'),)))
    IPhotoProgressDialog.SetActionLinkText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(17, 'SetActionLinkText', ((1, 'pszCaption'),)))
    IPhotoProgressDialog.ShowActionLink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(18, 'ShowActionLink', ((1, 'fShow'),)))
    IPhotoProgressDialog.IsCancelled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(19, 'IsCancelled', ((1, 'pfCancelled'),)))
    IPhotoProgressDialog.GetUserInput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IUnknown_head,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(20, 'GetUserInput', ((1, 'riidType'),(1, 'pUnknown'),(1, 'pPropVarResult'),(1, 'pPropVarDefault'),)))
    return IPhotoProgressDialog
def _define_IPhotoAcquireSource_head():
    class IPhotoAcquireSource(win32more.System.Com.IUnknown_head):
        Guid = Guid('00f2c703-8613-4282-a53b-6ec59c5883ac')
    return IPhotoAcquireSource
def _define_IPhotoAcquireSource():
    IPhotoAcquireSource = win32more.Media.PictureAcquisition.IPhotoAcquireSource_head
    IPhotoAcquireSource.GetFriendlyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(3, 'GetFriendlyName', ((1, 'pbstrFriendlyName'),)))
    IPhotoAcquireSource.GetDeviceIcons = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.WindowsAndMessaging.HICON),POINTER(win32more.UI.WindowsAndMessaging.HICON), use_last_error=False)(4, 'GetDeviceIcons', ((1, 'nSize'),(1, 'phLargeIcon'),(1, 'phSmallIcon'),)))
    IPhotoAcquireSource.InitializeItemList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,win32more.Media.PictureAcquisition.IPhotoAcquireProgressCB_head,POINTER(UInt32), use_last_error=False)(5, 'InitializeItemList', ((1, 'fForceEnumeration'),(1, 'pPhotoAcquireProgressCB'),(1, 'pnItemCount'),)))
    IPhotoAcquireSource.GetItemCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(6, 'GetItemCount', ((1, 'pnItemCount'),)))
    IPhotoAcquireSource.GetItemAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.PictureAcquisition.IPhotoAcquireItem_head), use_last_error=False)(7, 'GetItemAt', ((1, 'nIndex'),(1, 'ppPhotoAcquireItem'),)))
    IPhotoAcquireSource.GetPhotoAcquireSettings = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.PictureAcquisition.IPhotoAcquireSettings_head), use_last_error=False)(8, 'GetPhotoAcquireSettings', ((1, 'ppPhotoAcquireSettings'),)))
    IPhotoAcquireSource.GetDeviceId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'GetDeviceId', ((1, 'pbstrDeviceId'),)))
    IPhotoAcquireSource.BindToObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(10, 'BindToObject', ((1, 'riid'),(1, 'ppv'),)))
    return IPhotoAcquireSource
def _define_IPhotoAcquire_head():
    class IPhotoAcquire(win32more.System.Com.IUnknown_head):
        Guid = Guid('00f23353-e31b-4955-a8ad-ca5ebf31e2ce')
    return IPhotoAcquire
def _define_IPhotoAcquire():
    IPhotoAcquire = win32more.Media.PictureAcquisition.IPhotoAcquire_head
    IPhotoAcquire.CreatePhotoSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Media.PictureAcquisition.IPhotoAcquireSource_head), use_last_error=False)(3, 'CreatePhotoSource', ((1, 'pszDevice'),(1, 'ppPhotoAcquireSource'),)))
    IPhotoAcquire.Acquire = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.PictureAcquisition.IPhotoAcquireSource_head,win32more.Foundation.BOOL,win32more.Foundation.HWND,win32more.Foundation.PWSTR,win32more.Media.PictureAcquisition.IPhotoAcquireProgressCB_head, use_last_error=False)(4, 'Acquire', ((1, 'pPhotoAcquireSource'),(1, 'fShowProgress'),(1, 'hWndParent'),(1, 'pszApplicationName'),(1, 'pPhotoAcquireProgressCB'),)))
    IPhotoAcquire.EnumResults = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IEnumString_head), use_last_error=False)(5, 'EnumResults', ((1, 'ppEnumFilePaths'),)))
    return IPhotoAcquire
def _define_IPhotoAcquireSettings_head():
    class IPhotoAcquireSettings(win32more.System.Com.IUnknown_head):
        Guid = Guid('00f2b868-dd67-487c-9553-049240767e91')
    return IPhotoAcquireSettings
def _define_IPhotoAcquireSettings():
    IPhotoAcquireSettings = win32more.Media.PictureAcquisition.IPhotoAcquireSettings_head
    IPhotoAcquireSettings.InitializeFromRegistry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(3, 'InitializeFromRegistry', ((1, 'pszRegistryKey'),)))
    IPhotoAcquireSettings.SetFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'SetFlags', ((1, 'dwPhotoAcquireFlags'),)))
    IPhotoAcquireSettings.SetOutputFilenameTemplate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(5, 'SetOutputFilenameTemplate', ((1, 'pszTemplate'),)))
    IPhotoAcquireSettings.SetSequencePaddingWidth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'SetSequencePaddingWidth', ((1, 'dwWidth'),)))
    IPhotoAcquireSettings.SetSequenceZeroPadding = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(7, 'SetSequenceZeroPadding', ((1, 'fZeroPad'),)))
    IPhotoAcquireSettings.SetGroupTag = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(8, 'SetGroupTag', ((1, 'pszGroupTag'),)))
    IPhotoAcquireSettings.SetAcquisitionTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.FILETIME_head), use_last_error=False)(9, 'SetAcquisitionTime', ((1, 'pftAcquisitionTime'),)))
    IPhotoAcquireSettings.GetFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(10, 'GetFlags', ((1, 'pdwPhotoAcquireFlags'),)))
    IPhotoAcquireSettings.GetOutputFilenameTemplate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'GetOutputFilenameTemplate', ((1, 'pbstrTemplate'),)))
    IPhotoAcquireSettings.GetSequencePaddingWidth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(12, 'GetSequencePaddingWidth', ((1, 'pdwWidth'),)))
    IPhotoAcquireSettings.GetSequenceZeroPadding = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(13, 'GetSequenceZeroPadding', ((1, 'pfZeroPad'),)))
    IPhotoAcquireSettings.GetGroupTag = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(14, 'GetGroupTag', ((1, 'pbstrGroupTag'),)))
    IPhotoAcquireSettings.GetAcquisitionTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.FILETIME_head), use_last_error=False)(15, 'GetAcquisitionTime', ((1, 'pftAcquisitionTime'),)))
    return IPhotoAcquireSettings
def _define_IPhotoAcquireOptionsDialog_head():
    class IPhotoAcquireOptionsDialog(win32more.System.Com.IUnknown_head):
        Guid = Guid('00f2b3ee-bf64-47ee-89f4-4dedd79643f2')
    return IPhotoAcquireOptionsDialog
def _define_IPhotoAcquireOptionsDialog():
    IPhotoAcquireOptionsDialog = win32more.Media.PictureAcquisition.IPhotoAcquireOptionsDialog_head
    IPhotoAcquireOptionsDialog.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(3, 'Initialize', ((1, 'pszRegistryRoot'),)))
    IPhotoAcquireOptionsDialog.Create = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(win32more.Foundation.HWND), use_last_error=False)(4, 'Create', ((1, 'hWndParent'),(1, 'phWndDialog'),)))
    IPhotoAcquireOptionsDialog.Destroy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Destroy', ()))
    IPhotoAcquireOptionsDialog.DoModal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(IntPtr), use_last_error=False)(6, 'DoModal', ((1, 'hWndParent'),(1, 'ppnReturnCode'),)))
    IPhotoAcquireOptionsDialog.SaveData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'SaveData', ()))
    return IPhotoAcquireOptionsDialog
DEVICE_SELECTION_DEVICE_TYPE = Int32
DST_UNKNOWN_DEVICE = 0
DST_WPD_DEVICE = 1
DST_WIA_DEVICE = 2
DST_STI_DEVICE = 3
DSF_TWAIN_DEVICE = 4
DST_FS_DEVICE = 5
DST_DV_DEVICE = 6
def _define_IPhotoAcquireDeviceSelectionDialog_head():
    class IPhotoAcquireDeviceSelectionDialog(win32more.System.Com.IUnknown_head):
        Guid = Guid('00f28837-55dd-4f37-aaf5-6855a9640467')
    return IPhotoAcquireDeviceSelectionDialog
def _define_IPhotoAcquireDeviceSelectionDialog():
    IPhotoAcquireDeviceSelectionDialog = win32more.Media.PictureAcquisition.IPhotoAcquireDeviceSelectionDialog_head
    IPhotoAcquireDeviceSelectionDialog.SetTitle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(3, 'SetTitle', ((1, 'pszTitle'),)))
    IPhotoAcquireDeviceSelectionDialog.SetSubmitButtonText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(4, 'SetSubmitButtonText', ((1, 'pszSubmitButtonText'),)))
    IPhotoAcquireDeviceSelectionDialog.DoModal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32,POINTER(win32more.Foundation.BSTR),POINTER(win32more.Media.PictureAcquisition.DEVICE_SELECTION_DEVICE_TYPE), use_last_error=False)(5, 'DoModal', ((1, 'hWndParent'),(1, 'dwDeviceFlags'),(1, 'pbstrDeviceId'),(1, 'pnDeviceType'),)))
    return IPhotoAcquireDeviceSelectionDialog
def _define_IPhotoAcquirePlugin_head():
    class IPhotoAcquirePlugin(win32more.System.Com.IUnknown_head):
        Guid = Guid('00f2dceb-ecb8-4f77-8e47-e7a987c83dd0')
    return IPhotoAcquirePlugin
def _define_IPhotoAcquirePlugin():
    IPhotoAcquirePlugin = win32more.Media.PictureAcquisition.IPhotoAcquirePlugin_head
    IPhotoAcquirePlugin.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.PictureAcquisition.IPhotoAcquireSource_head,win32more.Media.PictureAcquisition.IPhotoAcquireProgressCB_head, use_last_error=False)(3, 'Initialize', ((1, 'pPhotoAcquireSource'),(1, 'pPhotoAcquireProgressCB'),)))
    IPhotoAcquirePlugin.ProcessItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Media.PictureAcquisition.IPhotoAcquireItem_head,win32more.System.Com.IStream_head,win32more.Foundation.PWSTR,win32more.UI.Shell.PropertiesSystem.IPropertyStore_head, use_last_error=False)(4, 'ProcessItem', ((1, 'dwAcquireStage'),(1, 'pPhotoAcquireItem'),(1, 'pOriginalItemStream'),(1, 'pszFinalFilename'),(1, 'pPropertyStore'),)))
    IPhotoAcquirePlugin.TransferComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT, use_last_error=False)(5, 'TransferComplete', ((1, 'hr'),)))
    IPhotoAcquirePlugin.DisplayConfigureDialog = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND, use_last_error=False)(6, 'DisplayConfigureDialog', ((1, 'hWndParent'),)))
    return IPhotoAcquirePlugin
__all__ = [
    "PKEY_PhotoAcquire_RelativePathname",
    "PKEY_PhotoAcquire_FinalFilename",
    "PKEY_PhotoAcquire_GroupTag",
    "PKEY_PhotoAcquire_TransferResult",
    "PKEY_PhotoAcquire_OriginalFilename",
    "PKEY_PhotoAcquire_CameraSequenceNumber",
    "PKEY_PhotoAcquire_IntermediateFile",
    "PKEY_PhotoAcquire_SkipImport",
    "PKEY_PhotoAcquire_DuplicateDetectionID",
    "PROGRESS_INDETERMINATE",
    "PHOTOACQ_ERROR_RESTART_REQUIRED",
    "PHOTOACQ_RUN_DEFAULT",
    "PHOTOACQ_NO_GALLERY_LAUNCH",
    "PHOTOACQ_DISABLE_AUTO_ROTATE",
    "PHOTOACQ_DISABLE_PLUGINS",
    "PHOTOACQ_DISABLE_GROUP_TAG_PROMPT",
    "PHOTOACQ_DISABLE_DB_INTEGRATION",
    "PHOTOACQ_DELETE_AFTER_ACQUIRE",
    "PHOTOACQ_DISABLE_DUPLICATE_DETECTION",
    "PHOTOACQ_ENABLE_THUMBNAIL_CACHING",
    "PHOTOACQ_DISABLE_METADATA_WRITE",
    "PHOTOACQ_DISABLE_THUMBNAIL_PROGRESS",
    "PHOTOACQ_DISABLE_SETTINGS_LINK",
    "PHOTOACQ_ABORT_ON_SETTINGS_UPDATE",
    "PHOTOACQ_IMPORT_VIDEO_AS_MULTIPLE_FILES",
    "DSF_WPD_DEVICES",
    "DSF_WIA_CAMERAS",
    "DSF_WIA_SCANNERS",
    "DSF_STI_DEVICES",
    "DSF_TWAIN_DEVICES",
    "DSF_FS_DEVICES",
    "DSF_DV_DEVICES",
    "DSF_ALL_DEVICES",
    "DSF_CPL_MODE",
    "DSF_SHOW_OFFLINE",
    "PAPS_PRESAVE",
    "PAPS_POSTSAVE",
    "PAPS_CLEANUP",
    "PhotoAcquire",
    "PhotoAcquireAutoPlayDropTarget",
    "PhotoAcquireAutoPlayHWEventHandler",
    "PhotoAcquireOptionsDialog",
    "PhotoProgressDialog",
    "PhotoAcquireDeviceSelectionDialog",
    "IPhotoAcquireItem",
    "USER_INPUT_STRING_TYPE",
    "USER_INPUT_DEFAULT",
    "USER_INPUT_PATH_ELEMENT",
    "IUserInputString",
    "ERROR_ADVISE_MESSAGE_TYPE",
    "PHOTOACQUIRE_ERROR_SKIPRETRYCANCEL",
    "PHOTOACQUIRE_ERROR_RETRYCANCEL",
    "PHOTOACQUIRE_ERROR_YESNO",
    "PHOTOACQUIRE_ERROR_OK",
    "ERROR_ADVISE_RESULT",
    "PHOTOACQUIRE_RESULT_YES",
    "PHOTOACQUIRE_RESULT_NO",
    "PHOTOACQUIRE_RESULT_OK",
    "PHOTOACQUIRE_RESULT_SKIP",
    "PHOTOACQUIRE_RESULT_SKIP_ALL",
    "PHOTOACQUIRE_RESULT_RETRY",
    "PHOTOACQUIRE_RESULT_ABORT",
    "IPhotoAcquireProgressCB",
    "IPhotoProgressActionCB",
    "PROGRESS_DIALOG_IMAGE_TYPE",
    "PROGRESS_DIALOG_ICON_SMALL",
    "PROGRESS_DIALOG_ICON_LARGE",
    "PROGRESS_DIALOG_ICON_THUMBNAIL",
    "PROGRESS_DIALOG_BITMAP_THUMBNAIL",
    "PROGRESS_DIALOG_CHECKBOX_ID",
    "PROGRESS_DIALOG_CHECKBOX_ID_DEFAULT",
    "IPhotoProgressDialog",
    "IPhotoAcquireSource",
    "IPhotoAcquire",
    "IPhotoAcquireSettings",
    "IPhotoAcquireOptionsDialog",
    "DEVICE_SELECTION_DEVICE_TYPE",
    "DST_UNKNOWN_DEVICE",
    "DST_WPD_DEVICE",
    "DST_WIA_DEVICE",
    "DST_STI_DEVICE",
    "DSF_TWAIN_DEVICE",
    "DST_FS_DEVICE",
    "DST_DV_DEVICE",
    "IPhotoAcquireDeviceSelectionDialog",
    "IPhotoAcquirePlugin",
]
