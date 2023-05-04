from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Graphics.Printing
import Windows.Graphics.Printing.OptionDetails
import Windows.Storage.Streams
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IPrintBindingOptionDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.IPrintBindingOptionDetails'
    _iid_ = Guid('{c3f4cc98-9564-4f16-a055-a98b9a49e9d3}')
    @winrt_commethod(6)
    def put_WarningText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_WarningText(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_Description(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_Description(self) -> WinRT_String: ...
    WarningText = property(get_WarningText, put_WarningText)
    Description = property(get_Description, put_Description)
class IPrintBorderingOptionDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.IPrintBorderingOptionDetails'
    _iid_ = Guid('{4d73bc8f-fb53-4eb2-985f-1d91de0b7639}')
    @winrt_commethod(6)
    def put_WarningText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_WarningText(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_Description(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_Description(self) -> WinRT_String: ...
    WarningText = property(get_WarningText, put_WarningText)
    Description = property(get_Description, put_Description)
class IPrintCollationOptionDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.IPrintCollationOptionDetails'
    _iid_ = Guid('{d6abb166-a5a6-40dc-acc3-739f28f1e5d3}')
    @winrt_commethod(6)
    def put_WarningText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_WarningText(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_Description(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_Description(self) -> WinRT_String: ...
    WarningText = property(get_WarningText, put_WarningText)
    Description = property(get_Description, put_Description)
class IPrintColorModeOptionDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.IPrintColorModeOptionDetails'
    _iid_ = Guid('{dba97704-f1d6-4843-a484-9b447cdcf3b6}')
    @winrt_commethod(6)
    def put_WarningText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_WarningText(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_Description(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_Description(self) -> WinRT_String: ...
    WarningText = property(get_WarningText, put_WarningText)
    Description = property(get_Description, put_Description)
class IPrintCopiesOptionDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.IPrintCopiesOptionDetails'
    _iid_ = Guid('{42053099-4339-4343-898d-2c47b5e0c341}')
    @winrt_commethod(6)
    def put_WarningText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_WarningText(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_Description(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_Description(self) -> WinRT_String: ...
    WarningText = property(get_WarningText, put_WarningText)
    Description = property(get_Description, put_Description)
class IPrintCustomItemDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.IPrintCustomItemDetails'
    _iid_ = Guid('{5704b637-5c3a-449a-aa36-b3291b1192fd}')
    @winrt_commethod(6)
    def get_ItemId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_ItemDisplayName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_ItemDisplayName(self) -> WinRT_String: ...
    ItemId = property(get_ItemId, None)
    ItemDisplayName = property(get_ItemDisplayName, put_ItemDisplayName)
class IPrintCustomItemListOptionDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.IPrintCustomItemListOptionDetails'
    _iid_ = Guid('{a5fafd88-58f2-4ebd-b90f-51e4f2944c5d}')
    @winrt_commethod(6)
    def AddItem(self, itemId: WinRT_String, displayName: WinRT_String) -> Void: ...
class IPrintCustomItemListOptionDetails2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.IPrintCustomItemListOptionDetails2'
    _iid_ = Guid('{c9d6353d-651c-4a39-906e-1091a1801bf1}')
    @winrt_commethod(6)
    def AddItem(self, itemId: WinRT_String, displayName: WinRT_String, description: WinRT_String, icon: Windows.Storage.Streams.IRandomAccessStreamWithContentType) -> Void: ...
class IPrintCustomItemListOptionDetails3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.IPrintCustomItemListOptionDetails3'
    _iid_ = Guid('{4fa1b53f-3c34-4868-a407-fc5eab259b21}')
    @winrt_commethod(6)
    def put_WarningText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_WarningText(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_Description(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_Description(self) -> WinRT_String: ...
    WarningText = property(get_WarningText, put_WarningText)
    Description = property(get_Description, put_Description)
class IPrintCustomOptionDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.IPrintCustomOptionDetails'
    _iid_ = Guid('{e32bde1c-28af-4b90-95da-a3acf320b929}')
    @winrt_commethod(6)
    def put_DisplayName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_DisplayName(self) -> WinRT_String: ...
    DisplayName = property(get_DisplayName, put_DisplayName)
class IPrintCustomTextOptionDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.IPrintCustomTextOptionDetails'
    _iid_ = Guid('{2ad171f8-c8bd-4905-9192-0d75136e8b31}')
    @winrt_commethod(6)
    def put_MaxCharacters(self, value: UInt32) -> Void: ...
    @winrt_commethod(7)
    def get_MaxCharacters(self) -> UInt32: ...
    MaxCharacters = property(get_MaxCharacters, put_MaxCharacters)
class IPrintCustomTextOptionDetails2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.IPrintCustomTextOptionDetails2'
    _iid_ = Guid('{cea70b54-b977-4718-8338-7ed2b0d86fe3}')
    @winrt_commethod(6)
    def put_WarningText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_WarningText(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_Description(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_Description(self) -> WinRT_String: ...
    WarningText = property(get_WarningText, put_WarningText)
    Description = property(get_Description, put_Description)
class IPrintCustomToggleOptionDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.IPrintCustomToggleOptionDetails'
    _iid_ = Guid('{9db4d514-e461-4608-8ee9-db6f5ed073c6}')
    @winrt_commethod(6)
    def put_WarningText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_WarningText(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_Description(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_Description(self) -> WinRT_String: ...
    WarningText = property(get_WarningText, put_WarningText)
    Description = property(get_Description, put_Description)
class IPrintDuplexOptionDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.IPrintDuplexOptionDetails'
    _iid_ = Guid('{fcd94591-d4a4-44fa-b3fe-42e0ba28d5ad}')
    @winrt_commethod(6)
    def put_WarningText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_WarningText(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_Description(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_Description(self) -> WinRT_String: ...
    WarningText = property(get_WarningText, put_WarningText)
    Description = property(get_Description, put_Description)
class IPrintHolePunchOptionDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.IPrintHolePunchOptionDetails'
    _iid_ = Guid('{a6de1f18-482c-4657-9d71-8ddddbea1e1e}')
    @winrt_commethod(6)
    def put_WarningText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_WarningText(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_Description(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_Description(self) -> WinRT_String: ...
    WarningText = property(get_WarningText, put_WarningText)
    Description = property(get_Description, put_Description)
class IPrintItemListOptionDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.IPrintItemListOptionDetails'
    _iid_ = Guid('{9a2257bf-fe61-43d8-a24f-a3f6ab7320e7}')
    @winrt_commethod(6)
    def get_Items(self) -> Windows.Foundation.Collections.IVectorView[Windows.Win32.System.WinRT.IInspectable_head]: ...
    Items = property(get_Items, None)
class IPrintMediaSizeOptionDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.IPrintMediaSizeOptionDetails'
    _iid_ = Guid('{6c8d5bcf-c0bf-47c8-b84a-628e7d0d1a1d}')
    @winrt_commethod(6)
    def put_WarningText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_WarningText(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_Description(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_Description(self) -> WinRT_String: ...
    WarningText = property(get_WarningText, put_WarningText)
    Description = property(get_Description, put_Description)
class IPrintMediaTypeOptionDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.IPrintMediaTypeOptionDetails'
    _iid_ = Guid('{f8c7000b-abf3-4abc-8e86-22abc5744a43}')
    @winrt_commethod(6)
    def put_WarningText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_WarningText(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_Description(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_Description(self) -> WinRT_String: ...
    WarningText = property(get_WarningText, put_WarningText)
    Description = property(get_Description, put_Description)
class IPrintNumberOptionDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.IPrintNumberOptionDetails'
    _iid_ = Guid('{4d01bbaf-645c-4de9-965f-6fc6bbc47cab}')
    @winrt_commethod(6)
    def get_MinValue(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_MaxValue(self) -> UInt32: ...
    MinValue = property(get_MinValue, None)
    MaxValue = property(get_MaxValue, None)
class IPrintOptionDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails'
    _iid_ = Guid('{390686cf-d682-495f-adfe-d7333f5c1808}')
    @winrt_commethod(6)
    def get_OptionId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_OptionType(self) -> Windows.Graphics.Printing.OptionDetails.PrintOptionType: ...
    @winrt_commethod(8)
    def put_ErrorText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_ErrorText(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def put_State(self, value: Windows.Graphics.Printing.OptionDetails.PrintOptionStates) -> Void: ...
    @winrt_commethod(11)
    def get_State(self) -> Windows.Graphics.Printing.OptionDetails.PrintOptionStates: ...
    @winrt_commethod(12)
    def get_Value(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(13)
    def TrySetValue(self, value: Windows.Win32.System.WinRT.IInspectable_head) -> Boolean: ...
    OptionId = property(get_OptionId, None)
    OptionType = property(get_OptionType, None)
    ErrorText = property(get_ErrorText, put_ErrorText)
    State = property(get_State, put_State)
    Value = property(get_Value, None)
class IPrintOrientationOptionDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.IPrintOrientationOptionDetails'
    _iid_ = Guid('{46c38879-66e0-4da0-87b4-d25457824eb7}')
    @winrt_commethod(6)
    def put_WarningText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_WarningText(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_Description(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_Description(self) -> WinRT_String: ...
    WarningText = property(get_WarningText, put_WarningText)
    Description = property(get_Description, put_Description)
class IPrintPageRangeOptionDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.IPrintPageRangeOptionDetails'
    _iid_ = Guid('{5a19e4b7-2be8-4aa7-9ea5-defbe8713b4e}')
    @winrt_commethod(6)
    def put_WarningText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_WarningText(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_Description(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_Description(self) -> WinRT_String: ...
    WarningText = property(get_WarningText, put_WarningText)
    Description = property(get_Description, put_Description)
class IPrintQualityOptionDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.IPrintQualityOptionDetails'
    _iid_ = Guid('{2dd06ba1-ce1a-44e6-84f9-3a92ea1e3044}')
    @winrt_commethod(6)
    def put_WarningText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_WarningText(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_Description(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_Description(self) -> WinRT_String: ...
    WarningText = property(get_WarningText, put_WarningText)
    Description = property(get_Description, put_Description)
class IPrintStapleOptionDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.IPrintStapleOptionDetails'
    _iid_ = Guid('{d43175bd-9c0b-44e0-84f6-ceebce653800}')
    @winrt_commethod(6)
    def put_WarningText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_WarningText(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_Description(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_Description(self) -> WinRT_String: ...
    WarningText = property(get_WarningText, put_WarningText)
    Description = property(get_Description, put_Description)
class IPrintTaskOptionChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.IPrintTaskOptionChangedEventArgs'
    _iid_ = Guid('{65197d05-a5ee-4307-9407-9acad147679c}')
    @winrt_commethod(6)
    def get_OptionId(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    OptionId = property(get_OptionId, None)
class IPrintTaskOptionDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.IPrintTaskOptionDetails'
    _iid_ = Guid('{f5720af1-a89e-42a6-81af-f8e010b38a68}')
    @winrt_commethod(6)
    def get_Options(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails]: ...
    @winrt_commethod(7)
    def CreateItemListOption(self, optionId: WinRT_String, displayName: WinRT_String) -> Windows.Graphics.Printing.OptionDetails.PrintCustomItemListOptionDetails: ...
    @winrt_commethod(8)
    def CreateTextOption(self, optionId: WinRT_String, displayName: WinRT_String) -> Windows.Graphics.Printing.OptionDetails.PrintCustomTextOptionDetails: ...
    @winrt_commethod(9)
    def add_OptionChanged(self, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Printing.OptionDetails.PrintTaskOptionDetails, Windows.Graphics.Printing.OptionDetails.PrintTaskOptionChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_OptionChanged(self, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_BeginValidation(self, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Printing.OptionDetails.PrintTaskOptionDetails, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_BeginValidation(self, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Options = property(get_Options, None)
class IPrintTaskOptionDetails2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.IPrintTaskOptionDetails2'
    _iid_ = Guid('{53730a09-f968-4692-a177-c074597186db}')
    @winrt_commethod(6)
    def CreateToggleOption(self, optionId: WinRT_String, displayName: WinRT_String) -> Windows.Graphics.Printing.OptionDetails.PrintCustomToggleOptionDetails: ...
class IPrintTaskOptionDetailsStatic(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.IPrintTaskOptionDetailsStatic'
    _iid_ = Guid('{135da193-0961-4b6e-8766-f13b7fbccd58}')
    @winrt_commethod(6)
    def GetFromPrintTaskOptions(self, printTaskOptions: Windows.Graphics.Printing.PrintTaskOptions) -> Windows.Graphics.Printing.OptionDetails.PrintTaskOptionDetails: ...
class IPrintTextOptionDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.IPrintTextOptionDetails'
    _iid_ = Guid('{ad75e563-5ce4-46bc-9918-ab9fad144c5b}')
    @winrt_commethod(6)
    def get_MaxCharacters(self) -> UInt32: ...
    MaxCharacters = property(get_MaxCharacters, None)
class PrintBindingOptionDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.PrintBindingOptionDetails'
    @winrt_mixinmethod
    def get_OptionId(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_OptionType(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Graphics.Printing.OptionDetails.PrintOptionType: ...
    @winrt_mixinmethod
    def put_ErrorText(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ErrorText(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_State(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: Windows.Graphics.Printing.OptionDetails.PrintOptionStates) -> Void: ...
    @winrt_mixinmethod
    def get_State(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Graphics.Printing.OptionDetails.PrintOptionStates: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def TrySetValue(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: Windows.Win32.System.WinRT.IInspectable_head) -> Boolean: ...
    @winrt_mixinmethod
    def get_Items(self: Windows.Graphics.Printing.OptionDetails.IPrintItemListOptionDetails) -> Windows.Foundation.Collections.IVectorView[Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def put_WarningText(self: Windows.Graphics.Printing.OptionDetails.IPrintBindingOptionDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_WarningText(self: Windows.Graphics.Printing.OptionDetails.IPrintBindingOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Description(self: Windows.Graphics.Printing.OptionDetails.IPrintBindingOptionDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.Graphics.Printing.OptionDetails.IPrintBindingOptionDetails) -> WinRT_String: ...
    OptionId = property(get_OptionId, None)
    OptionType = property(get_OptionType, None)
    ErrorText = property(get_ErrorText, put_ErrorText)
    State = property(get_State, put_State)
    Value = property(get_Value, None)
    Items = property(get_Items, None)
    WarningText = property(get_WarningText, put_WarningText)
    Description = property(get_Description, put_Description)
class PrintBorderingOptionDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.PrintBorderingOptionDetails'
    @winrt_mixinmethod
    def get_OptionId(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_OptionType(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Graphics.Printing.OptionDetails.PrintOptionType: ...
    @winrt_mixinmethod
    def put_ErrorText(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ErrorText(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_State(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: Windows.Graphics.Printing.OptionDetails.PrintOptionStates) -> Void: ...
    @winrt_mixinmethod
    def get_State(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Graphics.Printing.OptionDetails.PrintOptionStates: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def TrySetValue(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: Windows.Win32.System.WinRT.IInspectable_head) -> Boolean: ...
    @winrt_mixinmethod
    def get_Items(self: Windows.Graphics.Printing.OptionDetails.IPrintItemListOptionDetails) -> Windows.Foundation.Collections.IVectorView[Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def put_WarningText(self: Windows.Graphics.Printing.OptionDetails.IPrintBorderingOptionDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_WarningText(self: Windows.Graphics.Printing.OptionDetails.IPrintBorderingOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Description(self: Windows.Graphics.Printing.OptionDetails.IPrintBorderingOptionDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.Graphics.Printing.OptionDetails.IPrintBorderingOptionDetails) -> WinRT_String: ...
    OptionId = property(get_OptionId, None)
    OptionType = property(get_OptionType, None)
    ErrorText = property(get_ErrorText, put_ErrorText)
    State = property(get_State, put_State)
    Value = property(get_Value, None)
    Items = property(get_Items, None)
    WarningText = property(get_WarningText, put_WarningText)
    Description = property(get_Description, put_Description)
class PrintCollationOptionDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.PrintCollationOptionDetails'
    @winrt_mixinmethod
    def get_OptionId(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_OptionType(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Graphics.Printing.OptionDetails.PrintOptionType: ...
    @winrt_mixinmethod
    def put_ErrorText(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ErrorText(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_State(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: Windows.Graphics.Printing.OptionDetails.PrintOptionStates) -> Void: ...
    @winrt_mixinmethod
    def get_State(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Graphics.Printing.OptionDetails.PrintOptionStates: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def TrySetValue(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: Windows.Win32.System.WinRT.IInspectable_head) -> Boolean: ...
    @winrt_mixinmethod
    def get_Items(self: Windows.Graphics.Printing.OptionDetails.IPrintItemListOptionDetails) -> Windows.Foundation.Collections.IVectorView[Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def put_WarningText(self: Windows.Graphics.Printing.OptionDetails.IPrintCollationOptionDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_WarningText(self: Windows.Graphics.Printing.OptionDetails.IPrintCollationOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Description(self: Windows.Graphics.Printing.OptionDetails.IPrintCollationOptionDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.Graphics.Printing.OptionDetails.IPrintCollationOptionDetails) -> WinRT_String: ...
    OptionId = property(get_OptionId, None)
    OptionType = property(get_OptionType, None)
    ErrorText = property(get_ErrorText, put_ErrorText)
    State = property(get_State, put_State)
    Value = property(get_Value, None)
    Items = property(get_Items, None)
    WarningText = property(get_WarningText, put_WarningText)
    Description = property(get_Description, put_Description)
class PrintColorModeOptionDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.PrintColorModeOptionDetails'
    @winrt_mixinmethod
    def get_OptionId(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_OptionType(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Graphics.Printing.OptionDetails.PrintOptionType: ...
    @winrt_mixinmethod
    def put_ErrorText(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ErrorText(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_State(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: Windows.Graphics.Printing.OptionDetails.PrintOptionStates) -> Void: ...
    @winrt_mixinmethod
    def get_State(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Graphics.Printing.OptionDetails.PrintOptionStates: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def TrySetValue(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: Windows.Win32.System.WinRT.IInspectable_head) -> Boolean: ...
    @winrt_mixinmethod
    def get_Items(self: Windows.Graphics.Printing.OptionDetails.IPrintItemListOptionDetails) -> Windows.Foundation.Collections.IVectorView[Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def put_WarningText(self: Windows.Graphics.Printing.OptionDetails.IPrintColorModeOptionDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_WarningText(self: Windows.Graphics.Printing.OptionDetails.IPrintColorModeOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Description(self: Windows.Graphics.Printing.OptionDetails.IPrintColorModeOptionDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.Graphics.Printing.OptionDetails.IPrintColorModeOptionDetails) -> WinRT_String: ...
    OptionId = property(get_OptionId, None)
    OptionType = property(get_OptionType, None)
    ErrorText = property(get_ErrorText, put_ErrorText)
    State = property(get_State, put_State)
    Value = property(get_Value, None)
    Items = property(get_Items, None)
    WarningText = property(get_WarningText, put_WarningText)
    Description = property(get_Description, put_Description)
class PrintCopiesOptionDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.PrintCopiesOptionDetails'
    @winrt_mixinmethod
    def get_OptionId(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_OptionType(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Graphics.Printing.OptionDetails.PrintOptionType: ...
    @winrt_mixinmethod
    def put_ErrorText(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ErrorText(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_State(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: Windows.Graphics.Printing.OptionDetails.PrintOptionStates) -> Void: ...
    @winrt_mixinmethod
    def get_State(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Graphics.Printing.OptionDetails.PrintOptionStates: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def TrySetValue(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: Windows.Win32.System.WinRT.IInspectable_head) -> Boolean: ...
    @winrt_mixinmethod
    def get_MinValue(self: Windows.Graphics.Printing.OptionDetails.IPrintNumberOptionDetails) -> UInt32: ...
    @winrt_mixinmethod
    def get_MaxValue(self: Windows.Graphics.Printing.OptionDetails.IPrintNumberOptionDetails) -> UInt32: ...
    @winrt_mixinmethod
    def put_WarningText(self: Windows.Graphics.Printing.OptionDetails.IPrintCopiesOptionDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_WarningText(self: Windows.Graphics.Printing.OptionDetails.IPrintCopiesOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Description(self: Windows.Graphics.Printing.OptionDetails.IPrintCopiesOptionDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.Graphics.Printing.OptionDetails.IPrintCopiesOptionDetails) -> WinRT_String: ...
    OptionId = property(get_OptionId, None)
    OptionType = property(get_OptionType, None)
    ErrorText = property(get_ErrorText, put_ErrorText)
    State = property(get_State, put_State)
    Value = property(get_Value, None)
    MinValue = property(get_MinValue, None)
    MaxValue = property(get_MaxValue, None)
    WarningText = property(get_WarningText, put_WarningText)
    Description = property(get_Description, put_Description)
class PrintCustomItemDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Printing.OptionDetails.IPrintCustomItemDetails
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.PrintCustomItemDetails'
    @winrt_mixinmethod
    def get_ItemId(self: Windows.Graphics.Printing.OptionDetails.IPrintCustomItemDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ItemDisplayName(self: Windows.Graphics.Printing.OptionDetails.IPrintCustomItemDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ItemDisplayName(self: Windows.Graphics.Printing.OptionDetails.IPrintCustomItemDetails) -> WinRT_String: ...
    ItemId = property(get_ItemId, None)
    ItemDisplayName = property(get_ItemDisplayName, put_ItemDisplayName)
class PrintCustomItemListOptionDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.PrintCustomItemListOptionDetails'
    @winrt_mixinmethod
    def get_OptionId(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_OptionType(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Graphics.Printing.OptionDetails.PrintOptionType: ...
    @winrt_mixinmethod
    def put_ErrorText(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ErrorText(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_State(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: Windows.Graphics.Printing.OptionDetails.PrintOptionStates) -> Void: ...
    @winrt_mixinmethod
    def get_State(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Graphics.Printing.OptionDetails.PrintOptionStates: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def TrySetValue(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: Windows.Win32.System.WinRT.IInspectable_head) -> Boolean: ...
    @winrt_mixinmethod
    def put_DisplayName(self: Windows.Graphics.Printing.OptionDetails.IPrintCustomOptionDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.Graphics.Printing.OptionDetails.IPrintCustomOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Items(self: Windows.Graphics.Printing.OptionDetails.IPrintItemListOptionDetails) -> Windows.Foundation.Collections.IVectorView[Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def AddItem(self: Windows.Graphics.Printing.OptionDetails.IPrintCustomItemListOptionDetails, itemId: WinRT_String, displayName: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def AddItem(self: Windows.Graphics.Printing.OptionDetails.IPrintCustomItemListOptionDetails, itemId: WinRT_String, displayName: WinRT_String, description: WinRT_String, icon: Windows.Storage.Streams.IRandomAccessStreamWithContentType) -> Void: ...
    @winrt_mixinmethod
    def put_WarningText(self: Windows.Graphics.Printing.OptionDetails.IPrintCustomItemListOptionDetails3, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_WarningText(self: Windows.Graphics.Printing.OptionDetails.IPrintCustomItemListOptionDetails3) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Description(self: Windows.Graphics.Printing.OptionDetails.IPrintCustomItemListOptionDetails3, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.Graphics.Printing.OptionDetails.IPrintCustomItemListOptionDetails3) -> WinRT_String: ...
    OptionId = property(get_OptionId, None)
    OptionType = property(get_OptionType, None)
    ErrorText = property(get_ErrorText, put_ErrorText)
    State = property(get_State, put_State)
    Value = property(get_Value, None)
    DisplayName = property(get_DisplayName, put_DisplayName)
    Items = property(get_Items, None)
    WarningText = property(get_WarningText, put_WarningText)
    Description = property(get_Description, put_Description)
class PrintCustomTextOptionDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.PrintCustomTextOptionDetails'
    @winrt_mixinmethod
    def get_OptionId(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_OptionType(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Graphics.Printing.OptionDetails.PrintOptionType: ...
    @winrt_mixinmethod
    def put_ErrorText(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ErrorText(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_State(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: Windows.Graphics.Printing.OptionDetails.PrintOptionStates) -> Void: ...
    @winrt_mixinmethod
    def get_State(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Graphics.Printing.OptionDetails.PrintOptionStates: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def TrySetValue(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: Windows.Win32.System.WinRT.IInspectable_head) -> Boolean: ...
    @winrt_mixinmethod
    def put_DisplayName(self: Windows.Graphics.Printing.OptionDetails.IPrintCustomOptionDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.Graphics.Printing.OptionDetails.IPrintCustomOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_MaxCharacters(self: Windows.Graphics.Printing.OptionDetails.IPrintCustomTextOptionDetails, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_MaxCharacters(self: Windows.Graphics.Printing.OptionDetails.IPrintCustomTextOptionDetails) -> UInt32: ...
    @winrt_mixinmethod
    def put_WarningText(self: Windows.Graphics.Printing.OptionDetails.IPrintCustomTextOptionDetails2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_WarningText(self: Windows.Graphics.Printing.OptionDetails.IPrintCustomTextOptionDetails2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Description(self: Windows.Graphics.Printing.OptionDetails.IPrintCustomTextOptionDetails2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.Graphics.Printing.OptionDetails.IPrintCustomTextOptionDetails2) -> WinRT_String: ...
    OptionId = property(get_OptionId, None)
    OptionType = property(get_OptionType, None)
    ErrorText = property(get_ErrorText, put_ErrorText)
    State = property(get_State, put_State)
    Value = property(get_Value, None)
    DisplayName = property(get_DisplayName, put_DisplayName)
    MaxCharacters = property(get_MaxCharacters, put_MaxCharacters)
    WarningText = property(get_WarningText, put_WarningText)
    Description = property(get_Description, put_Description)
class PrintCustomToggleOptionDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.PrintCustomToggleOptionDetails'
    @winrt_mixinmethod
    def get_OptionId(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_OptionType(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Graphics.Printing.OptionDetails.PrintOptionType: ...
    @winrt_mixinmethod
    def put_ErrorText(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ErrorText(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_State(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: Windows.Graphics.Printing.OptionDetails.PrintOptionStates) -> Void: ...
    @winrt_mixinmethod
    def get_State(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Graphics.Printing.OptionDetails.PrintOptionStates: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def TrySetValue(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: Windows.Win32.System.WinRT.IInspectable_head) -> Boolean: ...
    @winrt_mixinmethod
    def put_DisplayName(self: Windows.Graphics.Printing.OptionDetails.IPrintCustomOptionDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.Graphics.Printing.OptionDetails.IPrintCustomOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_WarningText(self: Windows.Graphics.Printing.OptionDetails.IPrintCustomToggleOptionDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_WarningText(self: Windows.Graphics.Printing.OptionDetails.IPrintCustomToggleOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Description(self: Windows.Graphics.Printing.OptionDetails.IPrintCustomToggleOptionDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.Graphics.Printing.OptionDetails.IPrintCustomToggleOptionDetails) -> WinRT_String: ...
    OptionId = property(get_OptionId, None)
    OptionType = property(get_OptionType, None)
    ErrorText = property(get_ErrorText, put_ErrorText)
    State = property(get_State, put_State)
    Value = property(get_Value, None)
    DisplayName = property(get_DisplayName, put_DisplayName)
    WarningText = property(get_WarningText, put_WarningText)
    Description = property(get_Description, put_Description)
class PrintDuplexOptionDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.PrintDuplexOptionDetails'
    @winrt_mixinmethod
    def get_OptionId(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_OptionType(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Graphics.Printing.OptionDetails.PrintOptionType: ...
    @winrt_mixinmethod
    def put_ErrorText(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ErrorText(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_State(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: Windows.Graphics.Printing.OptionDetails.PrintOptionStates) -> Void: ...
    @winrt_mixinmethod
    def get_State(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Graphics.Printing.OptionDetails.PrintOptionStates: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def TrySetValue(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: Windows.Win32.System.WinRT.IInspectable_head) -> Boolean: ...
    @winrt_mixinmethod
    def get_Items(self: Windows.Graphics.Printing.OptionDetails.IPrintItemListOptionDetails) -> Windows.Foundation.Collections.IVectorView[Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def put_WarningText(self: Windows.Graphics.Printing.OptionDetails.IPrintDuplexOptionDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_WarningText(self: Windows.Graphics.Printing.OptionDetails.IPrintDuplexOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Description(self: Windows.Graphics.Printing.OptionDetails.IPrintDuplexOptionDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.Graphics.Printing.OptionDetails.IPrintDuplexOptionDetails) -> WinRT_String: ...
    OptionId = property(get_OptionId, None)
    OptionType = property(get_OptionType, None)
    ErrorText = property(get_ErrorText, put_ErrorText)
    State = property(get_State, put_State)
    Value = property(get_Value, None)
    Items = property(get_Items, None)
    WarningText = property(get_WarningText, put_WarningText)
    Description = property(get_Description, put_Description)
class PrintHolePunchOptionDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.PrintHolePunchOptionDetails'
    @winrt_mixinmethod
    def get_OptionId(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_OptionType(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Graphics.Printing.OptionDetails.PrintOptionType: ...
    @winrt_mixinmethod
    def put_ErrorText(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ErrorText(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_State(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: Windows.Graphics.Printing.OptionDetails.PrintOptionStates) -> Void: ...
    @winrt_mixinmethod
    def get_State(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Graphics.Printing.OptionDetails.PrintOptionStates: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def TrySetValue(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: Windows.Win32.System.WinRT.IInspectable_head) -> Boolean: ...
    @winrt_mixinmethod
    def get_Items(self: Windows.Graphics.Printing.OptionDetails.IPrintItemListOptionDetails) -> Windows.Foundation.Collections.IVectorView[Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def put_WarningText(self: Windows.Graphics.Printing.OptionDetails.IPrintHolePunchOptionDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_WarningText(self: Windows.Graphics.Printing.OptionDetails.IPrintHolePunchOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Description(self: Windows.Graphics.Printing.OptionDetails.IPrintHolePunchOptionDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.Graphics.Printing.OptionDetails.IPrintHolePunchOptionDetails) -> WinRT_String: ...
    OptionId = property(get_OptionId, None)
    OptionType = property(get_OptionType, None)
    ErrorText = property(get_ErrorText, put_ErrorText)
    State = property(get_State, put_State)
    Value = property(get_Value, None)
    Items = property(get_Items, None)
    WarningText = property(get_WarningText, put_WarningText)
    Description = property(get_Description, put_Description)
class PrintMediaSizeOptionDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.PrintMediaSizeOptionDetails'
    @winrt_mixinmethod
    def get_OptionId(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_OptionType(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Graphics.Printing.OptionDetails.PrintOptionType: ...
    @winrt_mixinmethod
    def put_ErrorText(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ErrorText(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_State(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: Windows.Graphics.Printing.OptionDetails.PrintOptionStates) -> Void: ...
    @winrt_mixinmethod
    def get_State(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Graphics.Printing.OptionDetails.PrintOptionStates: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def TrySetValue(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: Windows.Win32.System.WinRT.IInspectable_head) -> Boolean: ...
    @winrt_mixinmethod
    def get_Items(self: Windows.Graphics.Printing.OptionDetails.IPrintItemListOptionDetails) -> Windows.Foundation.Collections.IVectorView[Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def put_WarningText(self: Windows.Graphics.Printing.OptionDetails.IPrintMediaSizeOptionDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_WarningText(self: Windows.Graphics.Printing.OptionDetails.IPrintMediaSizeOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Description(self: Windows.Graphics.Printing.OptionDetails.IPrintMediaSizeOptionDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.Graphics.Printing.OptionDetails.IPrintMediaSizeOptionDetails) -> WinRT_String: ...
    OptionId = property(get_OptionId, None)
    OptionType = property(get_OptionType, None)
    ErrorText = property(get_ErrorText, put_ErrorText)
    State = property(get_State, put_State)
    Value = property(get_Value, None)
    Items = property(get_Items, None)
    WarningText = property(get_WarningText, put_WarningText)
    Description = property(get_Description, put_Description)
class PrintMediaTypeOptionDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.PrintMediaTypeOptionDetails'
    @winrt_mixinmethod
    def get_OptionId(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_OptionType(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Graphics.Printing.OptionDetails.PrintOptionType: ...
    @winrt_mixinmethod
    def put_ErrorText(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ErrorText(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_State(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: Windows.Graphics.Printing.OptionDetails.PrintOptionStates) -> Void: ...
    @winrt_mixinmethod
    def get_State(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Graphics.Printing.OptionDetails.PrintOptionStates: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def TrySetValue(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: Windows.Win32.System.WinRT.IInspectable_head) -> Boolean: ...
    @winrt_mixinmethod
    def get_Items(self: Windows.Graphics.Printing.OptionDetails.IPrintItemListOptionDetails) -> Windows.Foundation.Collections.IVectorView[Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def put_WarningText(self: Windows.Graphics.Printing.OptionDetails.IPrintMediaTypeOptionDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_WarningText(self: Windows.Graphics.Printing.OptionDetails.IPrintMediaTypeOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Description(self: Windows.Graphics.Printing.OptionDetails.IPrintMediaTypeOptionDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.Graphics.Printing.OptionDetails.IPrintMediaTypeOptionDetails) -> WinRT_String: ...
    OptionId = property(get_OptionId, None)
    OptionType = property(get_OptionType, None)
    ErrorText = property(get_ErrorText, put_ErrorText)
    State = property(get_State, put_State)
    Value = property(get_Value, None)
    Items = property(get_Items, None)
    WarningText = property(get_WarningText, put_WarningText)
    Description = property(get_Description, put_Description)
PrintOptionStates = UInt32
PrintOptionStates_None: PrintOptionStates = 0
PrintOptionStates_Enabled: PrintOptionStates = 1
PrintOptionStates_Constrained: PrintOptionStates = 2
PrintOptionType = Int32
PrintOptionType_Unknown: PrintOptionType = 0
PrintOptionType_Number: PrintOptionType = 1
PrintOptionType_Text: PrintOptionType = 2
PrintOptionType_ItemList: PrintOptionType = 3
PrintOptionType_Toggle: PrintOptionType = 4
class PrintOrientationOptionDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.PrintOrientationOptionDetails'
    @winrt_mixinmethod
    def get_OptionId(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_OptionType(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Graphics.Printing.OptionDetails.PrintOptionType: ...
    @winrt_mixinmethod
    def put_ErrorText(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ErrorText(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_State(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: Windows.Graphics.Printing.OptionDetails.PrintOptionStates) -> Void: ...
    @winrt_mixinmethod
    def get_State(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Graphics.Printing.OptionDetails.PrintOptionStates: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def TrySetValue(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: Windows.Win32.System.WinRT.IInspectable_head) -> Boolean: ...
    @winrt_mixinmethod
    def get_Items(self: Windows.Graphics.Printing.OptionDetails.IPrintItemListOptionDetails) -> Windows.Foundation.Collections.IVectorView[Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def put_WarningText(self: Windows.Graphics.Printing.OptionDetails.IPrintOrientationOptionDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_WarningText(self: Windows.Graphics.Printing.OptionDetails.IPrintOrientationOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Description(self: Windows.Graphics.Printing.OptionDetails.IPrintOrientationOptionDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.Graphics.Printing.OptionDetails.IPrintOrientationOptionDetails) -> WinRT_String: ...
    OptionId = property(get_OptionId, None)
    OptionType = property(get_OptionType, None)
    ErrorText = property(get_ErrorText, put_ErrorText)
    State = property(get_State, put_State)
    Value = property(get_Value, None)
    Items = property(get_Items, None)
    WarningText = property(get_WarningText, put_WarningText)
    Description = property(get_Description, put_Description)
class PrintPageRangeOptionDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.PrintPageRangeOptionDetails'
    @winrt_mixinmethod
    def get_OptionId(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_OptionType(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Graphics.Printing.OptionDetails.PrintOptionType: ...
    @winrt_mixinmethod
    def put_ErrorText(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ErrorText(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_State(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: Windows.Graphics.Printing.OptionDetails.PrintOptionStates) -> Void: ...
    @winrt_mixinmethod
    def get_State(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Graphics.Printing.OptionDetails.PrintOptionStates: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def TrySetValue(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: Windows.Win32.System.WinRT.IInspectable_head) -> Boolean: ...
    @winrt_mixinmethod
    def put_WarningText(self: Windows.Graphics.Printing.OptionDetails.IPrintPageRangeOptionDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_WarningText(self: Windows.Graphics.Printing.OptionDetails.IPrintPageRangeOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Description(self: Windows.Graphics.Printing.OptionDetails.IPrintPageRangeOptionDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.Graphics.Printing.OptionDetails.IPrintPageRangeOptionDetails) -> WinRT_String: ...
    OptionId = property(get_OptionId, None)
    OptionType = property(get_OptionType, None)
    ErrorText = property(get_ErrorText, put_ErrorText)
    State = property(get_State, put_State)
    Value = property(get_Value, None)
    WarningText = property(get_WarningText, put_WarningText)
    Description = property(get_Description, put_Description)
class PrintQualityOptionDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.PrintQualityOptionDetails'
    @winrt_mixinmethod
    def get_OptionId(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_OptionType(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Graphics.Printing.OptionDetails.PrintOptionType: ...
    @winrt_mixinmethod
    def put_ErrorText(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ErrorText(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_State(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: Windows.Graphics.Printing.OptionDetails.PrintOptionStates) -> Void: ...
    @winrt_mixinmethod
    def get_State(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Graphics.Printing.OptionDetails.PrintOptionStates: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def TrySetValue(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: Windows.Win32.System.WinRT.IInspectable_head) -> Boolean: ...
    @winrt_mixinmethod
    def get_Items(self: Windows.Graphics.Printing.OptionDetails.IPrintItemListOptionDetails) -> Windows.Foundation.Collections.IVectorView[Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def put_WarningText(self: Windows.Graphics.Printing.OptionDetails.IPrintQualityOptionDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_WarningText(self: Windows.Graphics.Printing.OptionDetails.IPrintQualityOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Description(self: Windows.Graphics.Printing.OptionDetails.IPrintQualityOptionDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.Graphics.Printing.OptionDetails.IPrintQualityOptionDetails) -> WinRT_String: ...
    OptionId = property(get_OptionId, None)
    OptionType = property(get_OptionType, None)
    ErrorText = property(get_ErrorText, put_ErrorText)
    State = property(get_State, put_State)
    Value = property(get_Value, None)
    Items = property(get_Items, None)
    WarningText = property(get_WarningText, put_WarningText)
    Description = property(get_Description, put_Description)
class PrintStapleOptionDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.PrintStapleOptionDetails'
    @winrt_mixinmethod
    def get_OptionId(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_OptionType(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Graphics.Printing.OptionDetails.PrintOptionType: ...
    @winrt_mixinmethod
    def put_ErrorText(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ErrorText(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_State(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: Windows.Graphics.Printing.OptionDetails.PrintOptionStates) -> Void: ...
    @winrt_mixinmethod
    def get_State(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Graphics.Printing.OptionDetails.PrintOptionStates: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def TrySetValue(self: Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails, value: Windows.Win32.System.WinRT.IInspectable_head) -> Boolean: ...
    @winrt_mixinmethod
    def get_Items(self: Windows.Graphics.Printing.OptionDetails.IPrintItemListOptionDetails) -> Windows.Foundation.Collections.IVectorView[Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def put_WarningText(self: Windows.Graphics.Printing.OptionDetails.IPrintStapleOptionDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_WarningText(self: Windows.Graphics.Printing.OptionDetails.IPrintStapleOptionDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Description(self: Windows.Graphics.Printing.OptionDetails.IPrintStapleOptionDetails, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.Graphics.Printing.OptionDetails.IPrintStapleOptionDetails) -> WinRT_String: ...
    OptionId = property(get_OptionId, None)
    OptionType = property(get_OptionType, None)
    ErrorText = property(get_ErrorText, put_ErrorText)
    State = property(get_State, put_State)
    Value = property(get_Value, None)
    Items = property(get_Items, None)
    WarningText = property(get_WarningText, put_WarningText)
    Description = property(get_Description, put_Description)
class PrintTaskOptionChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Printing.OptionDetails.IPrintTaskOptionChangedEventArgs
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.PrintTaskOptionChangedEventArgs'
    @winrt_mixinmethod
    def get_OptionId(self: Windows.Graphics.Printing.OptionDetails.IPrintTaskOptionChangedEventArgs) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    OptionId = property(get_OptionId, None)
class PrintTaskOptionDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Printing.OptionDetails.IPrintTaskOptionDetails
    _classid_ = 'Windows.Graphics.Printing.OptionDetails.PrintTaskOptionDetails'
    @winrt_mixinmethod
    def get_Options(self: Windows.Graphics.Printing.OptionDetails.IPrintTaskOptionDetails) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Graphics.Printing.OptionDetails.IPrintOptionDetails]: ...
    @winrt_mixinmethod
    def CreateItemListOption(self: Windows.Graphics.Printing.OptionDetails.IPrintTaskOptionDetails, optionId: WinRT_String, displayName: WinRT_String) -> Windows.Graphics.Printing.OptionDetails.PrintCustomItemListOptionDetails: ...
    @winrt_mixinmethod
    def CreateTextOption(self: Windows.Graphics.Printing.OptionDetails.IPrintTaskOptionDetails, optionId: WinRT_String, displayName: WinRT_String) -> Windows.Graphics.Printing.OptionDetails.PrintCustomTextOptionDetails: ...
    @winrt_mixinmethod
    def add_OptionChanged(self: Windows.Graphics.Printing.OptionDetails.IPrintTaskOptionDetails, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Printing.OptionDetails.PrintTaskOptionDetails, Windows.Graphics.Printing.OptionDetails.PrintTaskOptionChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_OptionChanged(self: Windows.Graphics.Printing.OptionDetails.IPrintTaskOptionDetails, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_BeginValidation(self: Windows.Graphics.Printing.OptionDetails.IPrintTaskOptionDetails, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Printing.OptionDetails.PrintTaskOptionDetails, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_BeginValidation(self: Windows.Graphics.Printing.OptionDetails.IPrintTaskOptionDetails, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetPageDescription(self: Windows.Graphics.Printing.IPrintTaskOptionsCore, jobPageNumber: UInt32) -> Windows.Graphics.Printing.PrintPageDescription: ...
    @winrt_mixinmethod
    def get_DisplayedOptions(self: Windows.Graphics.Printing.IPrintTaskOptionsCoreUIConfiguration) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def CreateToggleOption(self: Windows.Graphics.Printing.OptionDetails.IPrintTaskOptionDetails2, optionId: WinRT_String, displayName: WinRT_String) -> Windows.Graphics.Printing.OptionDetails.PrintCustomToggleOptionDetails: ...
    @winrt_classmethod
    def GetFromPrintTaskOptions(cls: Windows.Graphics.Printing.OptionDetails.IPrintTaskOptionDetailsStatic, printTaskOptions: Windows.Graphics.Printing.PrintTaskOptions) -> Windows.Graphics.Printing.OptionDetails.PrintTaskOptionDetails: ...
    Options = property(get_Options, None)
    DisplayedOptions = property(get_DisplayedOptions, None)
make_head(_module, 'IPrintBindingOptionDetails')
make_head(_module, 'IPrintBorderingOptionDetails')
make_head(_module, 'IPrintCollationOptionDetails')
make_head(_module, 'IPrintColorModeOptionDetails')
make_head(_module, 'IPrintCopiesOptionDetails')
make_head(_module, 'IPrintCustomItemDetails')
make_head(_module, 'IPrintCustomItemListOptionDetails')
make_head(_module, 'IPrintCustomItemListOptionDetails2')
make_head(_module, 'IPrintCustomItemListOptionDetails3')
make_head(_module, 'IPrintCustomOptionDetails')
make_head(_module, 'IPrintCustomTextOptionDetails')
make_head(_module, 'IPrintCustomTextOptionDetails2')
make_head(_module, 'IPrintCustomToggleOptionDetails')
make_head(_module, 'IPrintDuplexOptionDetails')
make_head(_module, 'IPrintHolePunchOptionDetails')
make_head(_module, 'IPrintItemListOptionDetails')
make_head(_module, 'IPrintMediaSizeOptionDetails')
make_head(_module, 'IPrintMediaTypeOptionDetails')
make_head(_module, 'IPrintNumberOptionDetails')
make_head(_module, 'IPrintOptionDetails')
make_head(_module, 'IPrintOrientationOptionDetails')
make_head(_module, 'IPrintPageRangeOptionDetails')
make_head(_module, 'IPrintQualityOptionDetails')
make_head(_module, 'IPrintStapleOptionDetails')
make_head(_module, 'IPrintTaskOptionChangedEventArgs')
make_head(_module, 'IPrintTaskOptionDetails')
make_head(_module, 'IPrintTaskOptionDetails2')
make_head(_module, 'IPrintTaskOptionDetailsStatic')
make_head(_module, 'IPrintTextOptionDetails')
make_head(_module, 'PrintBindingOptionDetails')
make_head(_module, 'PrintBorderingOptionDetails')
make_head(_module, 'PrintCollationOptionDetails')
make_head(_module, 'PrintColorModeOptionDetails')
make_head(_module, 'PrintCopiesOptionDetails')
make_head(_module, 'PrintCustomItemDetails')
make_head(_module, 'PrintCustomItemListOptionDetails')
make_head(_module, 'PrintCustomTextOptionDetails')
make_head(_module, 'PrintCustomToggleOptionDetails')
make_head(_module, 'PrintDuplexOptionDetails')
make_head(_module, 'PrintHolePunchOptionDetails')
make_head(_module, 'PrintMediaSizeOptionDetails')
make_head(_module, 'PrintMediaTypeOptionDetails')
make_head(_module, 'PrintOrientationOptionDetails')
make_head(_module, 'PrintPageRangeOptionDetails')
make_head(_module, 'PrintQualityOptionDetails')
make_head(_module, 'PrintStapleOptionDetails')
make_head(_module, 'PrintTaskOptionChangedEventArgs')
make_head(_module, 'PrintTaskOptionDetails')
