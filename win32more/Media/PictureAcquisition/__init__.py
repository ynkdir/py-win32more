from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
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
        prototype = globals()[f'{name}_head']
    except KeyError:
        if name in _arch_optional:
            return None
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
def PKEY_PhotoAcquire_RelativePathname():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('00f23377-7ac6-4b7a-84-43-34-5e-73-1f-a5-7a'), pid=2)
def PKEY_PhotoAcquire_FinalFilename():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('00f23377-7ac6-4b7a-84-43-34-5e-73-1f-a5-7a'), pid=3)
def PKEY_PhotoAcquire_GroupTag():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('00f23377-7ac6-4b7a-84-43-34-5e-73-1f-a5-7a'), pid=4)
def PKEY_PhotoAcquire_TransferResult():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('00f23377-7ac6-4b7a-84-43-34-5e-73-1f-a5-7a'), pid=5)
def PKEY_PhotoAcquire_OriginalFilename():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('00f23377-7ac6-4b7a-84-43-34-5e-73-1f-a5-7a'), pid=6)
def PKEY_PhotoAcquire_CameraSequenceNumber():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('00f23377-7ac6-4b7a-84-43-34-5e-73-1f-a5-7a'), pid=7)
def PKEY_PhotoAcquire_IntermediateFile():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('00f23377-7ac6-4b7a-84-43-34-5e-73-1f-a5-7a'), pid=8)
def PKEY_PhotoAcquire_SkipImport():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('00f23377-7ac6-4b7a-84-43-34-5e-73-1f-a5-7a'), pid=9)
def PKEY_PhotoAcquire_DuplicateDetectionID():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('00f23377-7ac6-4b7a-84-43-34-5e-73-1f-a5-7a'), pid=10)
PROGRESS_INDETERMINATE: Int32 = -1
PHOTOACQ_ERROR_RESTART_REQUIRED: win32more.Foundation.HRESULT = -2147180543
PHOTOACQ_RUN_DEFAULT: UInt32 = 0
PHOTOACQ_NO_GALLERY_LAUNCH: UInt32 = 1
PHOTOACQ_DISABLE_AUTO_ROTATE: UInt32 = 2
PHOTOACQ_DISABLE_PLUGINS: UInt32 = 4
PHOTOACQ_DISABLE_GROUP_TAG_PROMPT: UInt32 = 8
PHOTOACQ_DISABLE_DB_INTEGRATION: UInt32 = 16
PHOTOACQ_DELETE_AFTER_ACQUIRE: UInt32 = 32
PHOTOACQ_DISABLE_DUPLICATE_DETECTION: UInt32 = 64
PHOTOACQ_ENABLE_THUMBNAIL_CACHING: UInt32 = 128
PHOTOACQ_DISABLE_METADATA_WRITE: UInt32 = 256
PHOTOACQ_DISABLE_THUMBNAIL_PROGRESS: UInt32 = 512
PHOTOACQ_DISABLE_SETTINGS_LINK: UInt32 = 1024
PHOTOACQ_ABORT_ON_SETTINGS_UPDATE: UInt32 = 2048
PHOTOACQ_IMPORT_VIDEO_AS_MULTIPLE_FILES: UInt32 = 4096
DSF_WPD_DEVICES: UInt32 = 1
DSF_WIA_CAMERAS: UInt32 = 2
DSF_WIA_SCANNERS: UInt32 = 4
DSF_STI_DEVICES: UInt32 = 8
DSF_TWAIN_DEVICES: UInt32 = 16
DSF_FS_DEVICES: UInt32 = 32
DSF_DV_DEVICES: UInt32 = 64
DSF_ALL_DEVICES: UInt32 = 65535
DSF_CPL_MODE: UInt32 = 65536
DSF_SHOW_OFFLINE: UInt32 = 131072
PAPS_PRESAVE: UInt32 = 0
PAPS_POSTSAVE: UInt32 = 1
PAPS_CLEANUP: UInt32 = 2
DEVICE_SELECTION_DEVICE_TYPE = Int32
DST_UNKNOWN_DEVICE: DEVICE_SELECTION_DEVICE_TYPE = 0
DST_WPD_DEVICE: DEVICE_SELECTION_DEVICE_TYPE = 1
DST_WIA_DEVICE: DEVICE_SELECTION_DEVICE_TYPE = 2
DST_STI_DEVICE: DEVICE_SELECTION_DEVICE_TYPE = 3
DSF_TWAIN_DEVICE: DEVICE_SELECTION_DEVICE_TYPE = 4
DST_FS_DEVICE: DEVICE_SELECTION_DEVICE_TYPE = 5
DST_DV_DEVICE: DEVICE_SELECTION_DEVICE_TYPE = 6
ERROR_ADVISE_MESSAGE_TYPE = Int32
PHOTOACQUIRE_ERROR_SKIPRETRYCANCEL: ERROR_ADVISE_MESSAGE_TYPE = 0
PHOTOACQUIRE_ERROR_RETRYCANCEL: ERROR_ADVISE_MESSAGE_TYPE = 1
PHOTOACQUIRE_ERROR_YESNO: ERROR_ADVISE_MESSAGE_TYPE = 2
PHOTOACQUIRE_ERROR_OK: ERROR_ADVISE_MESSAGE_TYPE = 3
ERROR_ADVISE_RESULT = Int32
PHOTOACQUIRE_RESULT_YES: ERROR_ADVISE_RESULT = 0
PHOTOACQUIRE_RESULT_NO: ERROR_ADVISE_RESULT = 1
PHOTOACQUIRE_RESULT_OK: ERROR_ADVISE_RESULT = 2
PHOTOACQUIRE_RESULT_SKIP: ERROR_ADVISE_RESULT = 3
PHOTOACQUIRE_RESULT_SKIP_ALL: ERROR_ADVISE_RESULT = 4
PHOTOACQUIRE_RESULT_RETRY: ERROR_ADVISE_RESULT = 5
PHOTOACQUIRE_RESULT_ABORT: ERROR_ADVISE_RESULT = 6
class IPhotoAcquire(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00f23353-e31b-4955-a8-ad-ca-5e-bf-31-e2-ce')
    @commethod(3)
    def CreatePhotoSource(pszDevice: win32more.Foundation.PWSTR, ppPhotoAcquireSource: POINTER(win32more.Media.PictureAcquisition.IPhotoAcquireSource_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Acquire(pPhotoAcquireSource: win32more.Media.PictureAcquisition.IPhotoAcquireSource_head, fShowProgress: win32more.Foundation.BOOL, hWndParent: win32more.Foundation.HWND, pszApplicationName: win32more.Foundation.PWSTR, pPhotoAcquireProgressCB: win32more.Media.PictureAcquisition.IPhotoAcquireProgressCB_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def EnumResults(ppEnumFilePaths: POINTER(win32more.System.Com.IEnumString_head)) -> win32more.Foundation.HRESULT: ...
class IPhotoAcquireDeviceSelectionDialog(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00f28837-55dd-4f37-aa-f5-68-55-a9-64-04-67')
    @commethod(3)
    def SetTitle(pszTitle: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetSubmitButtonText(pszSubmitButtonText: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def DoModal(hWndParent: win32more.Foundation.HWND, dwDeviceFlags: UInt32, pbstrDeviceId: POINTER(win32more.Foundation.BSTR), pnDeviceType: POINTER(win32more.Media.PictureAcquisition.DEVICE_SELECTION_DEVICE_TYPE)) -> win32more.Foundation.HRESULT: ...
class IPhotoAcquireItem(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00f21c97-28bf-4c02-b8-42-5e-4e-90-13-9a-30')
    @commethod(3)
    def GetItemName(pbstrItemName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetThumbnail(sizeThumbnail: win32more.Foundation.SIZE, phbmpThumbnail: POINTER(win32more.Graphics.Gdi.HBITMAP)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetProperty(key: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pv: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetProperty(key: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pv: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetStream(ppStream: POINTER(win32more.System.Com.IStream_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def CanDelete(pfCanDelete: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def Delete() -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetSubItemCount(pnCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetSubItemAt(nItemIndex: UInt32, ppPhotoAcquireItem: POINTER(win32more.Media.PictureAcquisition.IPhotoAcquireItem_head)) -> win32more.Foundation.HRESULT: ...
class IPhotoAcquireOptionsDialog(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00f2b3ee-bf64-47ee-89-f4-4d-ed-d7-96-43-f2')
    @commethod(3)
    def Initialize(pszRegistryRoot: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Create(hWndParent: win32more.Foundation.HWND, phWndDialog: POINTER(win32more.Foundation.HWND)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Destroy() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def DoModal(hWndParent: win32more.Foundation.HWND, ppnReturnCode: POINTER(IntPtr)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SaveData() -> win32more.Foundation.HRESULT: ...
class IPhotoAcquirePlugin(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00f2dceb-ecb8-4f77-8e-47-e7-a9-87-c8-3d-d0')
    @commethod(3)
    def Initialize(pPhotoAcquireSource: win32more.Media.PictureAcquisition.IPhotoAcquireSource_head, pPhotoAcquireProgressCB: win32more.Media.PictureAcquisition.IPhotoAcquireProgressCB_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def ProcessItem(dwAcquireStage: UInt32, pPhotoAcquireItem: win32more.Media.PictureAcquisition.IPhotoAcquireItem_head, pOriginalItemStream: win32more.System.Com.IStream_head, pszFinalFilename: win32more.Foundation.PWSTR, pPropertyStore: win32more.UI.Shell.PropertiesSystem.IPropertyStore_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def TransferComplete(hr: win32more.Foundation.HRESULT) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def DisplayConfigureDialog(hWndParent: win32more.Foundation.HWND) -> win32more.Foundation.HRESULT: ...
class IPhotoAcquireProgressCB(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00f2ce1e-935e-4248-89-2c-13-0f-32-c4-5c-b4')
    @commethod(3)
    def Cancelled(pfCancelled: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def StartEnumeration(pPhotoAcquireSource: win32more.Media.PictureAcquisition.IPhotoAcquireSource_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def FoundItem(pPhotoAcquireItem: win32more.Media.PictureAcquisition.IPhotoAcquireItem_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def EndEnumeration(hr: win32more.Foundation.HRESULT) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def StartTransfer(pPhotoAcquireSource: win32more.Media.PictureAcquisition.IPhotoAcquireSource_head) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def StartItemTransfer(nItemIndex: UInt32, pPhotoAcquireItem: win32more.Media.PictureAcquisition.IPhotoAcquireItem_head) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def DirectoryCreated(pszDirectory: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def UpdateTransferPercent(fOverall: win32more.Foundation.BOOL, nPercent: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def EndItemTransfer(nItemIndex: UInt32, pPhotoAcquireItem: win32more.Media.PictureAcquisition.IPhotoAcquireItem_head, hr: win32more.Foundation.HRESULT) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def EndTransfer(hr: win32more.Foundation.HRESULT) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def StartDelete(pPhotoAcquireSource: win32more.Media.PictureAcquisition.IPhotoAcquireSource_head) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def StartItemDelete(nItemIndex: UInt32, pPhotoAcquireItem: win32more.Media.PictureAcquisition.IPhotoAcquireItem_head) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def UpdateDeletePercent(nPercent: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def EndItemDelete(nItemIndex: UInt32, pPhotoAcquireItem: win32more.Media.PictureAcquisition.IPhotoAcquireItem_head, hr: win32more.Foundation.HRESULT) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def EndDelete(hr: win32more.Foundation.HRESULT) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def EndSession(hr: win32more.Foundation.HRESULT) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def GetDeleteAfterAcquire(pfDeleteAfterAcquire: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def ErrorAdvise(hr: win32more.Foundation.HRESULT, pszErrorMessage: win32more.Foundation.PWSTR, nMessageType: win32more.Media.PictureAcquisition.ERROR_ADVISE_MESSAGE_TYPE, pnErrorAdviseResult: POINTER(win32more.Media.PictureAcquisition.ERROR_ADVISE_RESULT)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def GetUserInput(riidType: POINTER(Guid), pUnknown: win32more.System.Com.IUnknown_head, pPropVarResult: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), pPropVarDefault: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
class IPhotoAcquireSettings(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00f2b868-dd67-487c-95-53-04-92-40-76-7e-91')
    @commethod(3)
    def InitializeFromRegistry(pszRegistryKey: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetFlags(dwPhotoAcquireFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetOutputFilenameTemplate(pszTemplate: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetSequencePaddingWidth(dwWidth: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetSequenceZeroPadding(fZeroPad: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetGroupTag(pszGroupTag: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetAcquisitionTime(pftAcquisitionTime: POINTER(win32more.Foundation.FILETIME_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetFlags(pdwPhotoAcquireFlags: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetOutputFilenameTemplate(pbstrTemplate: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetSequencePaddingWidth(pdwWidth: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetSequenceZeroPadding(pfZeroPad: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetGroupTag(pbstrGroupTag: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetAcquisitionTime(pftAcquisitionTime: POINTER(win32more.Foundation.FILETIME_head)) -> win32more.Foundation.HRESULT: ...
class IPhotoAcquireSource(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00f2c703-8613-4282-a5-3b-6e-c5-9c-58-83-ac')
    @commethod(3)
    def GetFriendlyName(pbstrFriendlyName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetDeviceIcons(nSize: UInt32, phLargeIcon: POINTER(win32more.UI.WindowsAndMessaging.HICON), phSmallIcon: POINTER(win32more.UI.WindowsAndMessaging.HICON)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def InitializeItemList(fForceEnumeration: win32more.Foundation.BOOL, pPhotoAcquireProgressCB: win32more.Media.PictureAcquisition.IPhotoAcquireProgressCB_head, pnItemCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetItemCount(pnItemCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetItemAt(nIndex: UInt32, ppPhotoAcquireItem: POINTER(win32more.Media.PictureAcquisition.IPhotoAcquireItem_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetPhotoAcquireSettings(ppPhotoAcquireSettings: POINTER(win32more.Media.PictureAcquisition.IPhotoAcquireSettings_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetDeviceId(pbstrDeviceId: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def BindToObject(riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IPhotoProgressActionCB(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00f242d0-b206-4e7d-b4-c1-47-55-bc-bb-9c-9f')
    @commethod(3)
    def DoAction(hWndParent: win32more.Foundation.HWND) -> win32more.Foundation.HRESULT: ...
class IPhotoProgressDialog(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00f246f9-0750-4f08-93-81-2c-d8-e9-06-a4-ae')
    @commethod(3)
    def Create(hwndParent: win32more.Foundation.HWND) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetWindow(phwndProgressDialog: POINTER(win32more.Foundation.HWND)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Destroy() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetTitle(pszTitle: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def ShowCheckbox(nCheckboxId: win32more.Media.PictureAcquisition.PROGRESS_DIALOG_CHECKBOX_ID, fShow: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetCheckboxText(nCheckboxId: win32more.Media.PictureAcquisition.PROGRESS_DIALOG_CHECKBOX_ID, pszCheckboxText: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetCheckboxCheck(nCheckboxId: win32more.Media.PictureAcquisition.PROGRESS_DIALOG_CHECKBOX_ID, fChecked: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetCheckboxTooltip(nCheckboxId: win32more.Media.PictureAcquisition.PROGRESS_DIALOG_CHECKBOX_ID, pszCheckboxTooltipText: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def IsCheckboxChecked(nCheckboxId: win32more.Media.PictureAcquisition.PROGRESS_DIALOG_CHECKBOX_ID, pfChecked: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def SetCaption(pszTitle: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def SetImage(nImageType: win32more.Media.PictureAcquisition.PROGRESS_DIALOG_IMAGE_TYPE, hIcon: win32more.UI.WindowsAndMessaging.HICON, hBitmap: win32more.Graphics.Gdi.HBITMAP) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def SetPercentComplete(nPercent: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def SetProgressText(pszProgressText: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def SetActionLinkCallback(pPhotoProgressActionCB: win32more.Media.PictureAcquisition.IPhotoProgressActionCB_head) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def SetActionLinkText(pszCaption: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def ShowActionLink(fShow: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def IsCancelled(pfCancelled: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def GetUserInput(riidType: POINTER(Guid), pUnknown: win32more.System.Com.IUnknown_head, pPropVarResult: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), pPropVarDefault: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
class IUserInputString(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00f243a1-205b-45ba-ae-26-ab-bc-53-aa-7a-6f')
    @commethod(3)
    def GetSubmitButtonText(pbstrSubmitButtonText: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetPrompt(pbstrPromptTitle: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetStringId(pbstrStringId: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetStringType(pnStringType: POINTER(win32more.Media.PictureAcquisition.USER_INPUT_STRING_TYPE)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetTooltipText(pbstrTooltipText: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetMaxLength(pcchMaxLength: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetDefault(pbstrDefault: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetMruCount(pnMruCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetMruEntryAt(nIndex: UInt32, pbstrMruEntry: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetImage(nSize: UInt32, phBitmap: POINTER(win32more.Graphics.Gdi.HBITMAP), phIcon: POINTER(win32more.UI.WindowsAndMessaging.HICON)) -> win32more.Foundation.HRESULT: ...
PhotoAcquire = Guid('00f26e02-e9f2-4a9f-9f-dd-5a-96-2f-b2-6a-98')
PhotoAcquireAutoPlayDropTarget = Guid('00f20eb5-8fd6-4d9d-b7-5e-36-80-17-66-c8-f1')
PhotoAcquireAutoPlayHWEventHandler = Guid('00f2b433-44e4-4d88-b2-b0-26-98-a0-a9-1d-ba')
PhotoAcquireDeviceSelectionDialog = Guid('00f29a34-b8a1-482c-bc-f8-3a-c7-b0-fe-8f-62')
PhotoAcquireOptionsDialog = Guid('00f210a1-62f0-438b-9f-7e-96-18-d7-2a-18-31')
PhotoProgressDialog = Guid('00f24ca0-748f-4e8a-89-4f-0e-03-57-c6-79-9f')
PROGRESS_DIALOG_CHECKBOX_ID = Int32
PROGRESS_DIALOG_CHECKBOX_ID_DEFAULT: PROGRESS_DIALOG_CHECKBOX_ID = 0
PROGRESS_DIALOG_IMAGE_TYPE = Int32
PROGRESS_DIALOG_ICON_SMALL: PROGRESS_DIALOG_IMAGE_TYPE = 0
PROGRESS_DIALOG_ICON_LARGE: PROGRESS_DIALOG_IMAGE_TYPE = 1
PROGRESS_DIALOG_ICON_THUMBNAIL: PROGRESS_DIALOG_IMAGE_TYPE = 2
PROGRESS_DIALOG_BITMAP_THUMBNAIL: PROGRESS_DIALOG_IMAGE_TYPE = 3
USER_INPUT_STRING_TYPE = Int32
USER_INPUT_DEFAULT: USER_INPUT_STRING_TYPE = 0
USER_INPUT_PATH_ELEMENT: USER_INPUT_STRING_TYPE = 1
make_head(_module, 'PKEY_PhotoAcquire_RelativePathname')
make_head(_module, 'PKEY_PhotoAcquire_FinalFilename')
make_head(_module, 'PKEY_PhotoAcquire_GroupTag')
make_head(_module, 'PKEY_PhotoAcquire_TransferResult')
make_head(_module, 'PKEY_PhotoAcquire_OriginalFilename')
make_head(_module, 'PKEY_PhotoAcquire_CameraSequenceNumber')
make_head(_module, 'PKEY_PhotoAcquire_IntermediateFile')
make_head(_module, 'PKEY_PhotoAcquire_SkipImport')
make_head(_module, 'PKEY_PhotoAcquire_DuplicateDetectionID')
make_head(_module, 'IPhotoAcquire')
make_head(_module, 'IPhotoAcquireDeviceSelectionDialog')
make_head(_module, 'IPhotoAcquireItem')
make_head(_module, 'IPhotoAcquireOptionsDialog')
make_head(_module, 'IPhotoAcquirePlugin')
make_head(_module, 'IPhotoAcquireProgressCB')
make_head(_module, 'IPhotoAcquireSettings')
make_head(_module, 'IPhotoAcquireSource')
make_head(_module, 'IPhotoProgressActionCB')
make_head(_module, 'IPhotoProgressDialog')
make_head(_module, 'IUserInputString')
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
_arch_optional = [
]
