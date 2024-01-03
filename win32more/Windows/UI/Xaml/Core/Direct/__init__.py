from __future__ import annotations
import sys
from typing import Generic, TypeVar
if sys.version_info < (3, 9):
    from typing_extensions import Annotated
else:
    from typing import Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, winrt_overload, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation
import win32more.Windows.UI
import win32more.Windows.UI.Xaml
import win32more.Windows.UI.Xaml.Core.Direct
import win32more.Windows.UI.Xaml.Media
import win32more.Windows.UI.Xaml.Media.Media3D
class IXamlDirect(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Core.Direct.IXamlDirect'
    _iid_ = Guid('{5ffa1295-add2-590f-a051-70989b866ade}')
    @winrt_commethod(6)
    def GetObject(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(7)
    def GetXamlDirectObject(self, object: win32more.Windows.Win32.System.WinRT.IInspectable) -> win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject: ...
    @winrt_commethod(8)
    def CreateInstance(self, typeIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlTypeIndex) -> win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject: ...
    @winrt_commethod(9)
    def SetObjectProperty(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(10)
    def SetXamlDirectObjectProperty(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex, value: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject) -> Void: ...
    @winrt_commethod(11)
    def SetBooleanProperty(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def SetDoubleProperty(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex, value: Double) -> Void: ...
    @winrt_commethod(13)
    def SetInt32Property(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex, value: Int32) -> Void: ...
    @winrt_commethod(14)
    def SetStringProperty(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex, value: WinRT_String) -> Void: ...
    @winrt_commethod(15)
    def SetDateTimeProperty(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    @winrt_commethod(16)
    def SetPointProperty(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(17)
    def SetRectProperty(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex, value: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_commethod(18)
    def SetSizeProperty(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex, value: win32more.Windows.Foundation.Size) -> Void: ...
    @winrt_commethod(19)
    def SetTimeSpanProperty(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(20)
    def SetColorProperty(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(21)
    def SetCornerRadiusProperty(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex, value: win32more.Windows.UI.Xaml.CornerRadius) -> Void: ...
    @winrt_commethod(22)
    def SetDurationProperty(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex, value: win32more.Windows.UI.Xaml.Duration) -> Void: ...
    @winrt_commethod(23)
    def SetGridLengthProperty(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex, value: win32more.Windows.UI.Xaml.GridLength) -> Void: ...
    @winrt_commethod(24)
    def SetThicknessProperty(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex, value: win32more.Windows.UI.Xaml.Thickness) -> Void: ...
    @winrt_commethod(25)
    def SetMatrixProperty(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex, value: win32more.Windows.UI.Xaml.Media.Matrix) -> Void: ...
    @winrt_commethod(26)
    def SetMatrix3DProperty(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex, value: win32more.Windows.UI.Xaml.Media.Media3D.Matrix3D) -> Void: ...
    @winrt_commethod(27)
    def SetEnumProperty(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex, value: UInt32) -> Void: ...
    @winrt_commethod(28)
    def GetObjectProperty(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(29)
    def GetXamlDirectObjectProperty(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex) -> win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject: ...
    @winrt_commethod(30)
    def GetBooleanProperty(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex) -> Boolean: ...
    @winrt_commethod(31)
    def GetDoubleProperty(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex) -> Double: ...
    @winrt_commethod(32)
    def GetInt32Property(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex) -> Int32: ...
    @winrt_commethod(33)
    def GetStringProperty(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex) -> WinRT_String: ...
    @winrt_commethod(34)
    def GetDateTimeProperty(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(35)
    def GetPointProperty(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(36)
    def GetRectProperty(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(37)
    def GetSizeProperty(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex) -> win32more.Windows.Foundation.Size: ...
    @winrt_commethod(38)
    def GetTimeSpanProperty(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(39)
    def GetColorProperty(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(40)
    def GetCornerRadiusProperty(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex) -> win32more.Windows.UI.Xaml.CornerRadius: ...
    @winrt_commethod(41)
    def GetDurationProperty(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex) -> win32more.Windows.UI.Xaml.Duration: ...
    @winrt_commethod(42)
    def GetGridLengthProperty(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex) -> win32more.Windows.UI.Xaml.GridLength: ...
    @winrt_commethod(43)
    def GetThicknessProperty(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex) -> win32more.Windows.UI.Xaml.Thickness: ...
    @winrt_commethod(44)
    def GetMatrixProperty(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex) -> win32more.Windows.UI.Xaml.Media.Matrix: ...
    @winrt_commethod(45)
    def GetMatrix3DProperty(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex) -> win32more.Windows.UI.Xaml.Media.Media3D.Matrix3D: ...
    @winrt_commethod(46)
    def GetEnumProperty(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex) -> UInt32: ...
    @winrt_commethod(47)
    def ClearProperty(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex) -> Void: ...
    @winrt_commethod(48)
    def GetCollectionCount(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject) -> UInt32: ...
    @winrt_commethod(49)
    def GetXamlDirectObjectFromCollectionAt(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, index: UInt32) -> win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject: ...
    @winrt_commethod(50)
    def AddToCollection(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, value: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject) -> Void: ...
    @winrt_commethod(51)
    def InsertIntoCollectionAt(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, index: UInt32, value: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject) -> Void: ...
    @winrt_commethod(52)
    def RemoveFromCollection(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, value: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject) -> Boolean: ...
    @winrt_commethod(53)
    def RemoveFromCollectionAt(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, index: UInt32) -> Void: ...
    @winrt_commethod(54)
    def ClearCollection(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject) -> Void: ...
    @winrt_commethod(55)
    def AddEventHandler(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, eventIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlEventIndex, handler: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(56)
    def AddEventHandler_HandledEventsToo(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, eventIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlEventIndex, handler: win32more.Windows.Win32.System.WinRT.IInspectable, handledEventsToo: Boolean) -> Void: ...
    @winrt_commethod(57)
    def RemoveEventHandler(self, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, eventIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlEventIndex, handler: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
class IXamlDirectObject(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Core.Direct.IXamlDirectObject'
    _iid_ = Guid('{10614a82-cee4-4645-ba25-d071ce778355}')
class IXamlDirectStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Core.Direct.IXamlDirectStatics'
    _iid_ = Guid('{321887cc-14e4-5c6f-878d-fbb604ad7d17}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.UI.Xaml.Core.Direct.XamlDirect: ...
class XamlDirect(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect
    _classid_ = 'Windows.UI.Xaml.Core.Direct.XamlDirect'
    @winrt_mixinmethod
    def GetObject(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def GetXamlDirectObject(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, object: win32more.Windows.Win32.System.WinRT.IInspectable) -> win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject: ...
    @winrt_mixinmethod
    def CreateInstance(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, typeIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlTypeIndex) -> win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject: ...
    @winrt_mixinmethod
    def SetObjectProperty(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def SetXamlDirectObjectProperty(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex, value: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject) -> Void: ...
    @winrt_mixinmethod
    def SetBooleanProperty(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def SetDoubleProperty(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex, value: Double) -> Void: ...
    @winrt_mixinmethod
    def SetInt32Property(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def SetStringProperty(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def SetDateTimeProperty(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    @winrt_mixinmethod
    def SetPointProperty(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def SetRectProperty(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex, value: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_mixinmethod
    def SetSizeProperty(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex, value: win32more.Windows.Foundation.Size) -> Void: ...
    @winrt_mixinmethod
    def SetTimeSpanProperty(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def SetColorProperty(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def SetCornerRadiusProperty(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex, value: win32more.Windows.UI.Xaml.CornerRadius) -> Void: ...
    @winrt_mixinmethod
    def SetDurationProperty(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex, value: win32more.Windows.UI.Xaml.Duration) -> Void: ...
    @winrt_mixinmethod
    def SetGridLengthProperty(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex, value: win32more.Windows.UI.Xaml.GridLength) -> Void: ...
    @winrt_mixinmethod
    def SetThicknessProperty(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex, value: win32more.Windows.UI.Xaml.Thickness) -> Void: ...
    @winrt_mixinmethod
    def SetMatrixProperty(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex, value: win32more.Windows.UI.Xaml.Media.Matrix) -> Void: ...
    @winrt_mixinmethod
    def SetMatrix3DProperty(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex, value: win32more.Windows.UI.Xaml.Media.Media3D.Matrix3D) -> Void: ...
    @winrt_mixinmethod
    def SetEnumProperty(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def GetObjectProperty(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def GetXamlDirectObjectProperty(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex) -> win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject: ...
    @winrt_mixinmethod
    def GetBooleanProperty(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex) -> Boolean: ...
    @winrt_mixinmethod
    def GetDoubleProperty(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex) -> Double: ...
    @winrt_mixinmethod
    def GetInt32Property(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex) -> Int32: ...
    @winrt_mixinmethod
    def GetStringProperty(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetDateTimeProperty(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def GetPointProperty(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def GetRectProperty(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def GetSizeProperty(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex) -> win32more.Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def GetTimeSpanProperty(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def GetColorProperty(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def GetCornerRadiusProperty(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex) -> win32more.Windows.UI.Xaml.CornerRadius: ...
    @winrt_mixinmethod
    def GetDurationProperty(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex) -> win32more.Windows.UI.Xaml.Duration: ...
    @winrt_mixinmethod
    def GetGridLengthProperty(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex) -> win32more.Windows.UI.Xaml.GridLength: ...
    @winrt_mixinmethod
    def GetThicknessProperty(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex) -> win32more.Windows.UI.Xaml.Thickness: ...
    @winrt_mixinmethod
    def GetMatrixProperty(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex) -> win32more.Windows.UI.Xaml.Media.Matrix: ...
    @winrt_mixinmethod
    def GetMatrix3DProperty(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex) -> win32more.Windows.UI.Xaml.Media.Media3D.Matrix3D: ...
    @winrt_mixinmethod
    def GetEnumProperty(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex) -> UInt32: ...
    @winrt_mixinmethod
    def ClearProperty(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, propertyIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex) -> Void: ...
    @winrt_mixinmethod
    def GetCollectionCount(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject) -> UInt32: ...
    @winrt_mixinmethod
    def GetXamlDirectObjectFromCollectionAt(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, index: UInt32) -> win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject: ...
    @winrt_mixinmethod
    def AddToCollection(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, value: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject) -> Void: ...
    @winrt_mixinmethod
    def InsertIntoCollectionAt(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, index: UInt32, value: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject) -> Void: ...
    @winrt_mixinmethod
    def RemoveFromCollection(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, value: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject) -> Boolean: ...
    @winrt_mixinmethod
    def RemoveFromCollectionAt(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def ClearCollection(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject) -> Void: ...
    @winrt_mixinmethod
    def AddEventHandler(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, eventIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlEventIndex, handler: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def AddEventHandler_HandledEventsToo(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, eventIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlEventIndex, handler: win32more.Windows.Win32.System.WinRT.IInspectable, handledEventsToo: Boolean) -> Void: ...
    @winrt_mixinmethod
    def RemoveEventHandler(self: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirect, xamlDirectObject: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectObject, eventIndex: win32more.Windows.UI.Xaml.Core.Direct.XamlEventIndex, handler: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.UI.Xaml.Core.Direct.IXamlDirectStatics) -> win32more.Windows.UI.Xaml.Core.Direct.XamlDirect: ...
XamlDirectContract: UInt32 = 327680
XamlEventIndex = Int32
FrameworkElement_DataContextChanged: XamlEventIndex = 16
FrameworkElement_SizeChanged: XamlEventIndex = 17
FrameworkElement_LayoutUpdated: XamlEventIndex = 18
UIElement_KeyUp: XamlEventIndex = 22
UIElement_KeyDown: XamlEventIndex = 23
UIElement_GotFocus: XamlEventIndex = 24
UIElement_LostFocus: XamlEventIndex = 25
UIElement_DragStarting: XamlEventIndex = 26
UIElement_DropCompleted: XamlEventIndex = 27
UIElement_CharacterReceived: XamlEventIndex = 28
UIElement_DragEnter: XamlEventIndex = 29
UIElement_DragLeave: XamlEventIndex = 30
UIElement_DragOver: XamlEventIndex = 31
UIElement_Drop: XamlEventIndex = 32
UIElement_PointerPressed: XamlEventIndex = 38
UIElement_PointerMoved: XamlEventIndex = 39
UIElement_PointerReleased: XamlEventIndex = 40
UIElement_PointerEntered: XamlEventIndex = 41
UIElement_PointerExited: XamlEventIndex = 42
UIElement_PointerCaptureLost: XamlEventIndex = 43
UIElement_PointerCanceled: XamlEventIndex = 44
UIElement_PointerWheelChanged: XamlEventIndex = 45
UIElement_Tapped: XamlEventIndex = 46
UIElement_DoubleTapped: XamlEventIndex = 47
UIElement_Holding: XamlEventIndex = 48
UIElement_ContextRequested: XamlEventIndex = 49
UIElement_ContextCanceled: XamlEventIndex = 50
UIElement_RightTapped: XamlEventIndex = 51
UIElement_ManipulationStarting: XamlEventIndex = 52
UIElement_ManipulationInertiaStarting: XamlEventIndex = 53
UIElement_ManipulationStarted: XamlEventIndex = 54
UIElement_ManipulationDelta: XamlEventIndex = 55
UIElement_ManipulationCompleted: XamlEventIndex = 56
UIElement_ProcessKeyboardAccelerators: XamlEventIndex = 60
UIElement_GettingFocus: XamlEventIndex = 61
UIElement_LosingFocus: XamlEventIndex = 62
UIElement_NoFocusCandidateFound: XamlEventIndex = 63
UIElement_PreviewKeyDown: XamlEventIndex = 64
UIElement_PreviewKeyUp: XamlEventIndex = 65
UIElement_BringIntoViewRequested: XamlEventIndex = 66
AppBar_Opening: XamlEventIndex = 109
AppBar_Opened: XamlEventIndex = 110
AppBar_Closing: XamlEventIndex = 111
AppBar_Closed: XamlEventIndex = 112
AutoSuggestBox_SuggestionChosen: XamlEventIndex = 113
AutoSuggestBox_TextChanged: XamlEventIndex = 114
AutoSuggestBox_QuerySubmitted: XamlEventIndex = 115
CalendarDatePicker_CalendarViewDayItemChanging: XamlEventIndex = 116
CalendarDatePicker_DateChanged: XamlEventIndex = 117
CalendarDatePicker_Opened: XamlEventIndex = 118
CalendarDatePicker_Closed: XamlEventIndex = 119
CalendarView_CalendarViewDayItemChanging: XamlEventIndex = 120
CalendarView_SelectedDatesChanged: XamlEventIndex = 121
ComboBox_DropDownClosed: XamlEventIndex = 122
ComboBox_DropDownOpened: XamlEventIndex = 123
CommandBar_DynamicOverflowItemsChanging: XamlEventIndex = 124
ContentDialog_Closing: XamlEventIndex = 126
ContentDialog_Closed: XamlEventIndex = 127
ContentDialog_Opened: XamlEventIndex = 128
ContentDialog_PrimaryButtonClick: XamlEventIndex = 129
ContentDialog_SecondaryButtonClick: XamlEventIndex = 130
ContentDialog_CloseButtonClick: XamlEventIndex = 131
Control_FocusEngaged: XamlEventIndex = 132
Control_FocusDisengaged: XamlEventIndex = 133
DatePicker_DateChanged: XamlEventIndex = 135
Frame_Navigated: XamlEventIndex = 136
Frame_Navigating: XamlEventIndex = 137
Frame_NavigationFailed: XamlEventIndex = 138
Frame_NavigationStopped: XamlEventIndex = 139
Hub_SectionHeaderClick: XamlEventIndex = 143
Hub_SectionsInViewChanged: XamlEventIndex = 144
ItemsPresenter_HorizontalSnapPointsChanged: XamlEventIndex = 148
ItemsPresenter_VerticalSnapPointsChanged: XamlEventIndex = 149
ListViewBase_ItemClick: XamlEventIndex = 150
ListViewBase_DragItemsStarting: XamlEventIndex = 151
ListViewBase_DragItemsCompleted: XamlEventIndex = 152
ListViewBase_ContainerContentChanging: XamlEventIndex = 153
ListViewBase_ChoosingItemContainer: XamlEventIndex = 154
ListViewBase_ChoosingGroupHeaderContainer: XamlEventIndex = 155
MediaTransportControls_ThumbnailRequested: XamlEventIndex = 167
MenuFlyoutItem_Click: XamlEventIndex = 168
RichEditBox_TextChanging: XamlEventIndex = 177
ScrollViewer_ViewChanging: XamlEventIndex = 192
ScrollViewer_ViewChanged: XamlEventIndex = 193
ScrollViewer_DirectManipulationStarted: XamlEventIndex = 194
ScrollViewer_DirectManipulationCompleted: XamlEventIndex = 195
SearchBox_QueryChanged: XamlEventIndex = 196
SearchBox_SuggestionsRequested: XamlEventIndex = 197
SearchBox_QuerySubmitted: XamlEventIndex = 198
SearchBox_ResultSuggestionChosen: XamlEventIndex = 199
SearchBox_PrepareForFocusOnKeyboardInput: XamlEventIndex = 200
SemanticZoom_ViewChangeStarted: XamlEventIndex = 201
SemanticZoom_ViewChangeCompleted: XamlEventIndex = 202
SettingsFlyout_BackClick: XamlEventIndex = 203
StackPanel_HorizontalSnapPointsChanged: XamlEventIndex = 208
StackPanel_VerticalSnapPointsChanged: XamlEventIndex = 209
TimePicker_TimeChanged: XamlEventIndex = 227
ToggleSwitch_Toggled: XamlEventIndex = 228
ToolTip_Closed: XamlEventIndex = 229
ToolTip_Opened: XamlEventIndex = 230
VirtualizingStackPanel_CleanUpVirtualizedItemEvent: XamlEventIndex = 231
WebView_SeparateProcessLost: XamlEventIndex = 232
WebView_LoadCompleted: XamlEventIndex = 233
WebView_ScriptNotify: XamlEventIndex = 234
WebView_NavigationFailed: XamlEventIndex = 235
WebView_NavigationStarting: XamlEventIndex = 236
WebView_ContentLoading: XamlEventIndex = 237
WebView_DOMContentLoaded: XamlEventIndex = 238
WebView_NavigationCompleted: XamlEventIndex = 239
WebView_FrameNavigationStarting: XamlEventIndex = 240
WebView_FrameContentLoading: XamlEventIndex = 241
WebView_FrameDOMContentLoaded: XamlEventIndex = 242
WebView_FrameNavigationCompleted: XamlEventIndex = 243
WebView_LongRunningScriptDetected: XamlEventIndex = 244
WebView_UnsafeContentWarningDisplaying: XamlEventIndex = 245
WebView_UnviewableContentIdentified: XamlEventIndex = 246
WebView_ContainsFullScreenElementChanged: XamlEventIndex = 247
WebView_UnsupportedUriSchemeIdentified: XamlEventIndex = 248
WebView_NewWindowRequested: XamlEventIndex = 249
WebView_PermissionRequested: XamlEventIndex = 250
ButtonBase_Click: XamlEventIndex = 256
CarouselPanel_HorizontalSnapPointsChanged: XamlEventIndex = 257
CarouselPanel_VerticalSnapPointsChanged: XamlEventIndex = 258
OrientedVirtualizingPanel_HorizontalSnapPointsChanged: XamlEventIndex = 263
OrientedVirtualizingPanel_VerticalSnapPointsChanged: XamlEventIndex = 264
RangeBase_ValueChanged: XamlEventIndex = 267
ScrollBar_Scroll: XamlEventIndex = 268
Selector_SelectionChanged: XamlEventIndex = 269
Thumb_DragStarted: XamlEventIndex = 270
Thumb_DragDelta: XamlEventIndex = 271
Thumb_DragCompleted: XamlEventIndex = 272
ToggleButton_Checked: XamlEventIndex = 273
ToggleButton_Unchecked: XamlEventIndex = 274
ToggleButton_Indeterminate: XamlEventIndex = 275
WebView_WebResourceRequested: XamlEventIndex = 283
ScrollViewer_AnchorRequested: XamlEventIndex = 291
DatePicker_SelectedDateChanged: XamlEventIndex = 322
TimePicker_SelectedTimeChanged: XamlEventIndex = 323
XamlPropertyIndex = Int32
AutomationProperties_AcceleratorKey: XamlPropertyIndex = 5
AutomationProperties_AccessibilityView: XamlPropertyIndex = 6
AutomationProperties_AccessKey: XamlPropertyIndex = 7
AutomationProperties_AutomationId: XamlPropertyIndex = 8
AutomationProperties_ControlledPeers: XamlPropertyIndex = 9
AutomationProperties_HelpText: XamlPropertyIndex = 10
AutomationProperties_IsRequiredForForm: XamlPropertyIndex = 11
AutomationProperties_ItemStatus: XamlPropertyIndex = 12
AutomationProperties_ItemType: XamlPropertyIndex = 13
AutomationProperties_LabeledBy: XamlPropertyIndex = 14
AutomationProperties_LiveSetting: XamlPropertyIndex = 15
AutomationProperties_Name: XamlPropertyIndex = 16
ToolTipService_Placement: XamlPropertyIndex = 24
ToolTipService_PlacementTarget: XamlPropertyIndex = 25
ToolTipService_ToolTip: XamlPropertyIndex = 26
Typography_AnnotationAlternates: XamlPropertyIndex = 28
Typography_Capitals: XamlPropertyIndex = 29
Typography_CapitalSpacing: XamlPropertyIndex = 30
Typography_CaseSensitiveForms: XamlPropertyIndex = 31
Typography_ContextualAlternates: XamlPropertyIndex = 32
Typography_ContextualLigatures: XamlPropertyIndex = 33
Typography_ContextualSwashes: XamlPropertyIndex = 34
Typography_DiscretionaryLigatures: XamlPropertyIndex = 35
Typography_EastAsianExpertForms: XamlPropertyIndex = 36
Typography_EastAsianLanguage: XamlPropertyIndex = 37
Typography_EastAsianWidths: XamlPropertyIndex = 38
Typography_Fraction: XamlPropertyIndex = 39
Typography_HistoricalForms: XamlPropertyIndex = 40
Typography_HistoricalLigatures: XamlPropertyIndex = 41
Typography_Kerning: XamlPropertyIndex = 42
Typography_MathematicalGreek: XamlPropertyIndex = 43
Typography_NumeralAlignment: XamlPropertyIndex = 44
Typography_NumeralStyle: XamlPropertyIndex = 45
Typography_SlashedZero: XamlPropertyIndex = 46
Typography_StandardLigatures: XamlPropertyIndex = 47
Typography_StandardSwashes: XamlPropertyIndex = 48
Typography_StylisticAlternates: XamlPropertyIndex = 49
Typography_StylisticSet1: XamlPropertyIndex = 50
Typography_StylisticSet10: XamlPropertyIndex = 51
Typography_StylisticSet11: XamlPropertyIndex = 52
Typography_StylisticSet12: XamlPropertyIndex = 53
Typography_StylisticSet13: XamlPropertyIndex = 54
Typography_StylisticSet14: XamlPropertyIndex = 55
Typography_StylisticSet15: XamlPropertyIndex = 56
Typography_StylisticSet16: XamlPropertyIndex = 57
Typography_StylisticSet17: XamlPropertyIndex = 58
Typography_StylisticSet18: XamlPropertyIndex = 59
Typography_StylisticSet19: XamlPropertyIndex = 60
Typography_StylisticSet2: XamlPropertyIndex = 61
Typography_StylisticSet20: XamlPropertyIndex = 62
Typography_StylisticSet3: XamlPropertyIndex = 63
Typography_StylisticSet4: XamlPropertyIndex = 64
Typography_StylisticSet5: XamlPropertyIndex = 65
Typography_StylisticSet6: XamlPropertyIndex = 66
Typography_StylisticSet7: XamlPropertyIndex = 67
Typography_StylisticSet8: XamlPropertyIndex = 68
Typography_StylisticSet9: XamlPropertyIndex = 69
Typography_Variants: XamlPropertyIndex = 70
AutomationPeer_EventsSource: XamlPropertyIndex = 75
AutoSuggestBoxSuggestionChosenEventArgs_SelectedItem: XamlPropertyIndex = 76
AutoSuggestBoxTextChangedEventArgs_Reason: XamlPropertyIndex = 77
Brush_Opacity: XamlPropertyIndex = 78
Brush_RelativeTransform: XamlPropertyIndex = 79
Brush_Transform: XamlPropertyIndex = 80
CollectionViewSource_IsSourceGrouped: XamlPropertyIndex = 81
CollectionViewSource_ItemsPath: XamlPropertyIndex = 82
CollectionViewSource_Source: XamlPropertyIndex = 83
CollectionViewSource_View: XamlPropertyIndex = 84
ColorKeyFrame_KeyTime: XamlPropertyIndex = 90
ColorKeyFrame_Value: XamlPropertyIndex = 91
ColumnDefinition_ActualWidth: XamlPropertyIndex = 92
ColumnDefinition_MaxWidth: XamlPropertyIndex = 93
ColumnDefinition_MinWidth: XamlPropertyIndex = 94
ColumnDefinition_Width: XamlPropertyIndex = 95
ComboBoxTemplateSettings_DropDownClosedHeight: XamlPropertyIndex = 96
ComboBoxTemplateSettings_DropDownOffset: XamlPropertyIndex = 97
ComboBoxTemplateSettings_DropDownOpenedHeight: XamlPropertyIndex = 98
ComboBoxTemplateSettings_SelectedItemDirection: XamlPropertyIndex = 99
DoubleKeyFrame_KeyTime: XamlPropertyIndex = 107
DoubleKeyFrame_Value: XamlPropertyIndex = 108
EasingFunctionBase_EasingMode: XamlPropertyIndex = 111
FlyoutBase_AttachedFlyout: XamlPropertyIndex = 114
FlyoutBase_Placement: XamlPropertyIndex = 115
Geometry_Bounds: XamlPropertyIndex = 118
Geometry_Transform: XamlPropertyIndex = 119
GradientStop_Color: XamlPropertyIndex = 120
GradientStop_Offset: XamlPropertyIndex = 121
GroupStyle_ContainerStyle: XamlPropertyIndex = 124
GroupStyle_ContainerStyleSelector: XamlPropertyIndex = 125
GroupStyle_HeaderContainerStyle: XamlPropertyIndex = 126
GroupStyle_HeaderTemplate: XamlPropertyIndex = 127
GroupStyle_HeaderTemplateSelector: XamlPropertyIndex = 128
GroupStyle_HidesIfEmpty: XamlPropertyIndex = 129
GroupStyle_Panel: XamlPropertyIndex = 130
InertiaExpansionBehavior_DesiredDeceleration: XamlPropertyIndex = 144
InertiaExpansionBehavior_DesiredExpansion: XamlPropertyIndex = 145
InertiaRotationBehavior_DesiredDeceleration: XamlPropertyIndex = 146
InertiaRotationBehavior_DesiredRotation: XamlPropertyIndex = 147
InertiaTranslationBehavior_DesiredDeceleration: XamlPropertyIndex = 148
InertiaTranslationBehavior_DesiredDisplacement: XamlPropertyIndex = 149
InputScope_Names: XamlPropertyIndex = 150
InputScopeName_NameValue: XamlPropertyIndex = 151
KeySpline_ControlPoint1: XamlPropertyIndex = 153
KeySpline_ControlPoint2: XamlPropertyIndex = 154
ManipulationPivot_Center: XamlPropertyIndex = 159
ManipulationPivot_Radius: XamlPropertyIndex = 160
ObjectKeyFrame_KeyTime: XamlPropertyIndex = 183
ObjectKeyFrame_Value: XamlPropertyIndex = 184
PageStackEntry_SourcePageType: XamlPropertyIndex = 185
PathFigure_IsClosed: XamlPropertyIndex = 192
PathFigure_IsFilled: XamlPropertyIndex = 193
PathFigure_Segments: XamlPropertyIndex = 194
PathFigure_StartPoint: XamlPropertyIndex = 195
Pointer_IsInContact: XamlPropertyIndex = 199
Pointer_IsInRange: XamlPropertyIndex = 200
Pointer_PointerDeviceType: XamlPropertyIndex = 201
Pointer_PointerId: XamlPropertyIndex = 202
PointKeyFrame_KeyTime: XamlPropertyIndex = 205
PointKeyFrame_Value: XamlPropertyIndex = 206
PrintDocument_DocumentSource: XamlPropertyIndex = 209
ProgressBarTemplateSettings_ContainerAnimationEndPosition: XamlPropertyIndex = 211
ProgressBarTemplateSettings_ContainerAnimationStartPosition: XamlPropertyIndex = 212
ProgressBarTemplateSettings_EllipseAnimationEndPosition: XamlPropertyIndex = 213
ProgressBarTemplateSettings_EllipseAnimationWellPosition: XamlPropertyIndex = 214
ProgressBarTemplateSettings_EllipseDiameter: XamlPropertyIndex = 215
ProgressBarTemplateSettings_EllipseOffset: XamlPropertyIndex = 216
ProgressBarTemplateSettings_IndicatorLengthDelta: XamlPropertyIndex = 217
ProgressRingTemplateSettings_EllipseDiameter: XamlPropertyIndex = 218
ProgressRingTemplateSettings_EllipseOffset: XamlPropertyIndex = 219
ProgressRingTemplateSettings_MaxSideLength: XamlPropertyIndex = 220
PropertyPath_Path: XamlPropertyIndex = 221
RowDefinition_ActualHeight: XamlPropertyIndex = 226
RowDefinition_Height: XamlPropertyIndex = 227
RowDefinition_MaxHeight: XamlPropertyIndex = 228
RowDefinition_MinHeight: XamlPropertyIndex = 229
SetterBase_IsSealed: XamlPropertyIndex = 233
SettingsFlyoutTemplateSettings_BorderBrush: XamlPropertyIndex = 234
SettingsFlyoutTemplateSettings_BorderThickness: XamlPropertyIndex = 235
SettingsFlyoutTemplateSettings_ContentTransitions: XamlPropertyIndex = 236
SettingsFlyoutTemplateSettings_HeaderBackground: XamlPropertyIndex = 237
SettingsFlyoutTemplateSettings_HeaderForeground: XamlPropertyIndex = 238
SettingsFlyoutTemplateSettings_IconSource: XamlPropertyIndex = 239
Style_BasedOn: XamlPropertyIndex = 244
Style_IsSealed: XamlPropertyIndex = 245
Style_Setters: XamlPropertyIndex = 246
Style_TargetType: XamlPropertyIndex = 247
TextElement_CharacterSpacing: XamlPropertyIndex = 249
TextElement_FontFamily: XamlPropertyIndex = 250
TextElement_FontSize: XamlPropertyIndex = 251
TextElement_FontStretch: XamlPropertyIndex = 252
TextElement_FontStyle: XamlPropertyIndex = 253
TextElement_FontWeight: XamlPropertyIndex = 254
TextElement_Foreground: XamlPropertyIndex = 255
TextElement_IsTextScaleFactorEnabled: XamlPropertyIndex = 256
TextElement_Language: XamlPropertyIndex = 257
Timeline_AutoReverse: XamlPropertyIndex = 263
Timeline_BeginTime: XamlPropertyIndex = 264
Timeline_Duration: XamlPropertyIndex = 265
Timeline_FillBehavior: XamlPropertyIndex = 266
Timeline_RepeatBehavior: XamlPropertyIndex = 267
Timeline_SpeedRatio: XamlPropertyIndex = 268
TimelineMarker_Text: XamlPropertyIndex = 269
TimelineMarker_Time: XamlPropertyIndex = 270
TimelineMarker_Type: XamlPropertyIndex = 271
ToggleSwitchTemplateSettings_CurtainCurrentToOffOffset: XamlPropertyIndex = 273
ToggleSwitchTemplateSettings_CurtainCurrentToOnOffset: XamlPropertyIndex = 274
ToggleSwitchTemplateSettings_CurtainOffToOnOffset: XamlPropertyIndex = 275
ToggleSwitchTemplateSettings_CurtainOnToOffOffset: XamlPropertyIndex = 276
ToggleSwitchTemplateSettings_KnobCurrentToOffOffset: XamlPropertyIndex = 277
ToggleSwitchTemplateSettings_KnobCurrentToOnOffset: XamlPropertyIndex = 278
ToggleSwitchTemplateSettings_KnobOffToOnOffset: XamlPropertyIndex = 279
ToggleSwitchTemplateSettings_KnobOnToOffOffset: XamlPropertyIndex = 280
ToolTipTemplateSettings_FromHorizontalOffset: XamlPropertyIndex = 281
ToolTipTemplateSettings_FromVerticalOffset: XamlPropertyIndex = 282
UIElement_AllowDrop: XamlPropertyIndex = 292
UIElement_CacheMode: XamlPropertyIndex = 293
UIElement_Clip: XamlPropertyIndex = 295
UIElement_CompositeMode: XamlPropertyIndex = 296
UIElement_IsDoubleTapEnabled: XamlPropertyIndex = 297
UIElement_IsHitTestVisible: XamlPropertyIndex = 298
UIElement_IsHoldingEnabled: XamlPropertyIndex = 299
UIElement_IsRightTapEnabled: XamlPropertyIndex = 300
UIElement_IsTapEnabled: XamlPropertyIndex = 301
UIElement_ManipulationMode: XamlPropertyIndex = 302
UIElement_Opacity: XamlPropertyIndex = 303
UIElement_PointerCaptures: XamlPropertyIndex = 304
UIElement_Projection: XamlPropertyIndex = 305
UIElement_RenderSize: XamlPropertyIndex = 306
UIElement_RenderTransform: XamlPropertyIndex = 307
UIElement_RenderTransformOrigin: XamlPropertyIndex = 308
UIElement_Transitions: XamlPropertyIndex = 309
UIElement_UseLayoutRounding: XamlPropertyIndex = 311
UIElement_Visibility: XamlPropertyIndex = 312
VisualState_Storyboard: XamlPropertyIndex = 322
VisualStateGroup_States: XamlPropertyIndex = 323
VisualStateGroup_Transitions: XamlPropertyIndex = 324
VisualStateManager_CustomVisualStateManager: XamlPropertyIndex = 325
VisualStateManager_VisualStateGroups: XamlPropertyIndex = 326
VisualTransition_From: XamlPropertyIndex = 327
VisualTransition_GeneratedDuration: XamlPropertyIndex = 328
VisualTransition_GeneratedEasingFunction: XamlPropertyIndex = 329
VisualTransition_Storyboard: XamlPropertyIndex = 330
VisualTransition_To: XamlPropertyIndex = 331
ArcSegment_IsLargeArc: XamlPropertyIndex = 332
ArcSegment_Point: XamlPropertyIndex = 333
ArcSegment_RotationAngle: XamlPropertyIndex = 334
ArcSegment_Size: XamlPropertyIndex = 335
ArcSegment_SweepDirection: XamlPropertyIndex = 336
BackEase_Amplitude: XamlPropertyIndex = 337
BeginStoryboard_Storyboard: XamlPropertyIndex = 338
BezierSegment_Point1: XamlPropertyIndex = 339
BezierSegment_Point2: XamlPropertyIndex = 340
BezierSegment_Point3: XamlPropertyIndex = 341
BitmapSource_PixelHeight: XamlPropertyIndex = 342
BitmapSource_PixelWidth: XamlPropertyIndex = 343
Block_LineHeight: XamlPropertyIndex = 344
Block_LineStackingStrategy: XamlPropertyIndex = 345
Block_Margin: XamlPropertyIndex = 346
Block_TextAlignment: XamlPropertyIndex = 347
BounceEase_Bounces: XamlPropertyIndex = 348
BounceEase_Bounciness: XamlPropertyIndex = 349
ColorAnimation_By: XamlPropertyIndex = 350
ColorAnimation_EasingFunction: XamlPropertyIndex = 351
ColorAnimation_EnableDependentAnimation: XamlPropertyIndex = 352
ColorAnimation_From: XamlPropertyIndex = 353
ColorAnimation_To: XamlPropertyIndex = 354
ColorAnimationUsingKeyFrames_EnableDependentAnimation: XamlPropertyIndex = 355
ColorAnimationUsingKeyFrames_KeyFrames: XamlPropertyIndex = 356
ContentThemeTransition_HorizontalOffset: XamlPropertyIndex = 357
ContentThemeTransition_VerticalOffset: XamlPropertyIndex = 358
ControlTemplate_TargetType: XamlPropertyIndex = 359
DispatcherTimer_Interval: XamlPropertyIndex = 362
DoubleAnimation_By: XamlPropertyIndex = 363
DoubleAnimation_EasingFunction: XamlPropertyIndex = 364
DoubleAnimation_EnableDependentAnimation: XamlPropertyIndex = 365
DoubleAnimation_From: XamlPropertyIndex = 366
DoubleAnimation_To: XamlPropertyIndex = 367
DoubleAnimationUsingKeyFrames_EnableDependentAnimation: XamlPropertyIndex = 368
DoubleAnimationUsingKeyFrames_KeyFrames: XamlPropertyIndex = 369
EasingColorKeyFrame_EasingFunction: XamlPropertyIndex = 372
EasingDoubleKeyFrame_EasingFunction: XamlPropertyIndex = 373
EasingPointKeyFrame_EasingFunction: XamlPropertyIndex = 374
EdgeUIThemeTransition_Edge: XamlPropertyIndex = 375
ElasticEase_Oscillations: XamlPropertyIndex = 376
ElasticEase_Springiness: XamlPropertyIndex = 377
EllipseGeometry_Center: XamlPropertyIndex = 378
EllipseGeometry_RadiusX: XamlPropertyIndex = 379
EllipseGeometry_RadiusY: XamlPropertyIndex = 380
EntranceThemeTransition_FromHorizontalOffset: XamlPropertyIndex = 381
EntranceThemeTransition_FromVerticalOffset: XamlPropertyIndex = 382
EntranceThemeTransition_IsStaggeringEnabled: XamlPropertyIndex = 383
EventTrigger_Actions: XamlPropertyIndex = 384
EventTrigger_RoutedEvent: XamlPropertyIndex = 385
ExponentialEase_Exponent: XamlPropertyIndex = 386
Flyout_Content: XamlPropertyIndex = 387
Flyout_FlyoutPresenterStyle: XamlPropertyIndex = 388
FrameworkElement_ActualHeight: XamlPropertyIndex = 389
FrameworkElement_ActualWidth: XamlPropertyIndex = 390
FrameworkElement_DataContext: XamlPropertyIndex = 391
FrameworkElement_FlowDirection: XamlPropertyIndex = 392
FrameworkElement_Height: XamlPropertyIndex = 393
FrameworkElement_HorizontalAlignment: XamlPropertyIndex = 394
FrameworkElement_Language: XamlPropertyIndex = 396
FrameworkElement_Margin: XamlPropertyIndex = 397
FrameworkElement_MaxHeight: XamlPropertyIndex = 398
FrameworkElement_MaxWidth: XamlPropertyIndex = 399
FrameworkElement_MinHeight: XamlPropertyIndex = 400
FrameworkElement_MinWidth: XamlPropertyIndex = 401
FrameworkElement_Parent: XamlPropertyIndex = 402
FrameworkElement_RequestedTheme: XamlPropertyIndex = 403
FrameworkElement_Resources: XamlPropertyIndex = 404
FrameworkElement_Style: XamlPropertyIndex = 405
FrameworkElement_Tag: XamlPropertyIndex = 406
FrameworkElement_Triggers: XamlPropertyIndex = 407
FrameworkElement_VerticalAlignment: XamlPropertyIndex = 408
FrameworkElement_Width: XamlPropertyIndex = 409
FrameworkElementAutomationPeer_Owner: XamlPropertyIndex = 410
GeometryGroup_Children: XamlPropertyIndex = 411
GeometryGroup_FillRule: XamlPropertyIndex = 412
GradientBrush_ColorInterpolationMode: XamlPropertyIndex = 413
GradientBrush_GradientStops: XamlPropertyIndex = 414
GradientBrush_MappingMode: XamlPropertyIndex = 415
GradientBrush_SpreadMethod: XamlPropertyIndex = 416
GridViewItemTemplateSettings_DragItemsCount: XamlPropertyIndex = 417
ItemAutomationPeer_Item: XamlPropertyIndex = 419
ItemAutomationPeer_ItemsControlAutomationPeer: XamlPropertyIndex = 420
LineGeometry_EndPoint: XamlPropertyIndex = 422
LineGeometry_StartPoint: XamlPropertyIndex = 423
LineSegment_Point: XamlPropertyIndex = 424
ListViewItemTemplateSettings_DragItemsCount: XamlPropertyIndex = 425
Matrix3DProjection_ProjectionMatrix: XamlPropertyIndex = 426
MenuFlyout_Items: XamlPropertyIndex = 427
MenuFlyout_MenuFlyoutPresenterStyle: XamlPropertyIndex = 428
ObjectAnimationUsingKeyFrames_EnableDependentAnimation: XamlPropertyIndex = 429
ObjectAnimationUsingKeyFrames_KeyFrames: XamlPropertyIndex = 430
PaneThemeTransition_Edge: XamlPropertyIndex = 431
PathGeometry_Figures: XamlPropertyIndex = 432
PathGeometry_FillRule: XamlPropertyIndex = 433
PlaneProjection_CenterOfRotationX: XamlPropertyIndex = 434
PlaneProjection_CenterOfRotationY: XamlPropertyIndex = 435
PlaneProjection_CenterOfRotationZ: XamlPropertyIndex = 436
PlaneProjection_GlobalOffsetX: XamlPropertyIndex = 437
PlaneProjection_GlobalOffsetY: XamlPropertyIndex = 438
PlaneProjection_GlobalOffsetZ: XamlPropertyIndex = 439
PlaneProjection_LocalOffsetX: XamlPropertyIndex = 440
PlaneProjection_LocalOffsetY: XamlPropertyIndex = 441
PlaneProjection_LocalOffsetZ: XamlPropertyIndex = 442
PlaneProjection_ProjectionMatrix: XamlPropertyIndex = 443
PlaneProjection_RotationX: XamlPropertyIndex = 444
PlaneProjection_RotationY: XamlPropertyIndex = 445
PlaneProjection_RotationZ: XamlPropertyIndex = 446
PointAnimation_By: XamlPropertyIndex = 447
PointAnimation_EasingFunction: XamlPropertyIndex = 448
PointAnimation_EnableDependentAnimation: XamlPropertyIndex = 449
PointAnimation_From: XamlPropertyIndex = 450
PointAnimation_To: XamlPropertyIndex = 451
PointAnimationUsingKeyFrames_EnableDependentAnimation: XamlPropertyIndex = 452
PointAnimationUsingKeyFrames_KeyFrames: XamlPropertyIndex = 453
PolyBezierSegment_Points: XamlPropertyIndex = 456
PolyLineSegment_Points: XamlPropertyIndex = 457
PolyQuadraticBezierSegment_Points: XamlPropertyIndex = 458
PopupThemeTransition_FromHorizontalOffset: XamlPropertyIndex = 459
PopupThemeTransition_FromVerticalOffset: XamlPropertyIndex = 460
PowerEase_Power: XamlPropertyIndex = 461
QuadraticBezierSegment_Point1: XamlPropertyIndex = 466
QuadraticBezierSegment_Point2: XamlPropertyIndex = 467
RectangleGeometry_Rect: XamlPropertyIndex = 470
RelativeSource_Mode: XamlPropertyIndex = 471
RenderTargetBitmap_PixelHeight: XamlPropertyIndex = 472
RenderTargetBitmap_PixelWidth: XamlPropertyIndex = 473
Setter_Property: XamlPropertyIndex = 474
Setter_Value: XamlPropertyIndex = 475
SolidColorBrush_Color: XamlPropertyIndex = 476
SplineColorKeyFrame_KeySpline: XamlPropertyIndex = 477
SplineDoubleKeyFrame_KeySpline: XamlPropertyIndex = 478
SplinePointKeyFrame_KeySpline: XamlPropertyIndex = 479
TileBrush_AlignmentX: XamlPropertyIndex = 483
TileBrush_AlignmentY: XamlPropertyIndex = 484
TileBrush_Stretch: XamlPropertyIndex = 485
Binding_Converter: XamlPropertyIndex = 487
Binding_ConverterLanguage: XamlPropertyIndex = 488
Binding_ConverterParameter: XamlPropertyIndex = 489
Binding_ElementName: XamlPropertyIndex = 490
Binding_FallbackValue: XamlPropertyIndex = 491
Binding_Mode: XamlPropertyIndex = 492
Binding_Path: XamlPropertyIndex = 493
Binding_RelativeSource: XamlPropertyIndex = 494
Binding_Source: XamlPropertyIndex = 495
Binding_TargetNullValue: XamlPropertyIndex = 496
Binding_UpdateSourceTrigger: XamlPropertyIndex = 497
BitmapImage_CreateOptions: XamlPropertyIndex = 498
BitmapImage_DecodePixelHeight: XamlPropertyIndex = 499
BitmapImage_DecodePixelType: XamlPropertyIndex = 500
BitmapImage_DecodePixelWidth: XamlPropertyIndex = 501
BitmapImage_UriSource: XamlPropertyIndex = 502
Border_Background: XamlPropertyIndex = 503
Border_BorderBrush: XamlPropertyIndex = 504
Border_BorderThickness: XamlPropertyIndex = 505
Border_Child: XamlPropertyIndex = 506
Border_ChildTransitions: XamlPropertyIndex = 507
Border_CornerRadius: XamlPropertyIndex = 508
Border_Padding: XamlPropertyIndex = 509
CaptureElement_Source: XamlPropertyIndex = 510
CaptureElement_Stretch: XamlPropertyIndex = 511
CompositeTransform_CenterX: XamlPropertyIndex = 514
CompositeTransform_CenterY: XamlPropertyIndex = 515
CompositeTransform_Rotation: XamlPropertyIndex = 516
CompositeTransform_ScaleX: XamlPropertyIndex = 517
CompositeTransform_ScaleY: XamlPropertyIndex = 518
CompositeTransform_SkewX: XamlPropertyIndex = 519
CompositeTransform_SkewY: XamlPropertyIndex = 520
CompositeTransform_TranslateX: XamlPropertyIndex = 521
CompositeTransform_TranslateY: XamlPropertyIndex = 522
ContentPresenter_CharacterSpacing: XamlPropertyIndex = 523
ContentPresenter_Content: XamlPropertyIndex = 524
ContentPresenter_ContentTemplate: XamlPropertyIndex = 525
ContentPresenter_ContentTemplateSelector: XamlPropertyIndex = 526
ContentPresenter_ContentTransitions: XamlPropertyIndex = 527
ContentPresenter_FontFamily: XamlPropertyIndex = 528
ContentPresenter_FontSize: XamlPropertyIndex = 529
ContentPresenter_FontStretch: XamlPropertyIndex = 530
ContentPresenter_FontStyle: XamlPropertyIndex = 531
ContentPresenter_FontWeight: XamlPropertyIndex = 532
ContentPresenter_Foreground: XamlPropertyIndex = 533
ContentPresenter_IsTextScaleFactorEnabled: XamlPropertyIndex = 534
ContentPresenter_LineStackingStrategy: XamlPropertyIndex = 535
ContentPresenter_MaxLines: XamlPropertyIndex = 536
ContentPresenter_OpticalMarginAlignment: XamlPropertyIndex = 537
ContentPresenter_TextLineBounds: XamlPropertyIndex = 539
ContentPresenter_TextWrapping: XamlPropertyIndex = 540
Control_Background: XamlPropertyIndex = 541
Control_BorderBrush: XamlPropertyIndex = 542
Control_BorderThickness: XamlPropertyIndex = 543
Control_CharacterSpacing: XamlPropertyIndex = 544
Control_FocusState: XamlPropertyIndex = 546
Control_FontFamily: XamlPropertyIndex = 547
Control_FontSize: XamlPropertyIndex = 548
Control_FontStretch: XamlPropertyIndex = 549
Control_FontStyle: XamlPropertyIndex = 550
Control_FontWeight: XamlPropertyIndex = 551
Control_Foreground: XamlPropertyIndex = 552
Control_HorizontalContentAlignment: XamlPropertyIndex = 553
Control_IsEnabled: XamlPropertyIndex = 554
Control_IsTabStop: XamlPropertyIndex = 555
Control_IsTextScaleFactorEnabled: XamlPropertyIndex = 556
Control_Padding: XamlPropertyIndex = 557
Control_TabIndex: XamlPropertyIndex = 558
Control_TabNavigation: XamlPropertyIndex = 559
Control_Template: XamlPropertyIndex = 560
Control_VerticalContentAlignment: XamlPropertyIndex = 561
DragItemThemeAnimation_TargetName: XamlPropertyIndex = 565
DragOverThemeAnimation_Direction: XamlPropertyIndex = 566
DragOverThemeAnimation_TargetName: XamlPropertyIndex = 567
DragOverThemeAnimation_ToOffset: XamlPropertyIndex = 568
DropTargetItemThemeAnimation_TargetName: XamlPropertyIndex = 569
FadeInThemeAnimation_TargetName: XamlPropertyIndex = 570
FadeOutThemeAnimation_TargetName: XamlPropertyIndex = 571
Glyphs_Fill: XamlPropertyIndex = 574
Glyphs_FontRenderingEmSize: XamlPropertyIndex = 575
Glyphs_FontUri: XamlPropertyIndex = 576
Glyphs_Indices: XamlPropertyIndex = 577
Glyphs_OriginX: XamlPropertyIndex = 578
Glyphs_OriginY: XamlPropertyIndex = 579
Glyphs_StyleSimulations: XamlPropertyIndex = 580
Glyphs_UnicodeString: XamlPropertyIndex = 581
IconElement_Foreground: XamlPropertyIndex = 584
Image_NineGrid: XamlPropertyIndex = 586
Image_PlayToSource: XamlPropertyIndex = 587
Image_Source: XamlPropertyIndex = 588
Image_Stretch: XamlPropertyIndex = 589
ImageBrush_ImageSource: XamlPropertyIndex = 591
InlineUIContainer_Child: XamlPropertyIndex = 592
ItemsPresenter_Footer: XamlPropertyIndex = 594
ItemsPresenter_FooterTemplate: XamlPropertyIndex = 595
ItemsPresenter_FooterTransitions: XamlPropertyIndex = 596
ItemsPresenter_Header: XamlPropertyIndex = 597
ItemsPresenter_HeaderTemplate: XamlPropertyIndex = 598
ItemsPresenter_HeaderTransitions: XamlPropertyIndex = 599
ItemsPresenter_Padding: XamlPropertyIndex = 601
LinearGradientBrush_EndPoint: XamlPropertyIndex = 602
LinearGradientBrush_StartPoint: XamlPropertyIndex = 603
MatrixTransform_Matrix: XamlPropertyIndex = 604
MediaElement_ActualStereo3DVideoPackingMode: XamlPropertyIndex = 605
MediaElement_AreTransportControlsEnabled: XamlPropertyIndex = 606
MediaElement_AspectRatioHeight: XamlPropertyIndex = 607
MediaElement_AspectRatioWidth: XamlPropertyIndex = 608
MediaElement_AudioCategory: XamlPropertyIndex = 609
MediaElement_AudioDeviceType: XamlPropertyIndex = 610
MediaElement_AudioStreamCount: XamlPropertyIndex = 611
MediaElement_AudioStreamIndex: XamlPropertyIndex = 612
MediaElement_AutoPlay: XamlPropertyIndex = 613
MediaElement_Balance: XamlPropertyIndex = 614
MediaElement_BufferingProgress: XamlPropertyIndex = 615
MediaElement_CanPause: XamlPropertyIndex = 616
MediaElement_CanSeek: XamlPropertyIndex = 617
MediaElement_CurrentState: XamlPropertyIndex = 618
MediaElement_DefaultPlaybackRate: XamlPropertyIndex = 619
MediaElement_DownloadProgress: XamlPropertyIndex = 620
MediaElement_DownloadProgressOffset: XamlPropertyIndex = 621
MediaElement_IsAudioOnly: XamlPropertyIndex = 623
MediaElement_IsFullWindow: XamlPropertyIndex = 624
MediaElement_IsLooping: XamlPropertyIndex = 625
MediaElement_IsMuted: XamlPropertyIndex = 626
MediaElement_IsStereo3DVideo: XamlPropertyIndex = 627
MediaElement_Markers: XamlPropertyIndex = 628
MediaElement_NaturalDuration: XamlPropertyIndex = 629
MediaElement_NaturalVideoHeight: XamlPropertyIndex = 630
MediaElement_NaturalVideoWidth: XamlPropertyIndex = 631
MediaElement_PlaybackRate: XamlPropertyIndex = 632
MediaElement_PlayToPreferredSourceUri: XamlPropertyIndex = 633
MediaElement_PlayToSource: XamlPropertyIndex = 634
MediaElement_Position: XamlPropertyIndex = 635
MediaElement_PosterSource: XamlPropertyIndex = 636
MediaElement_ProtectionManager: XamlPropertyIndex = 637
MediaElement_RealTimePlayback: XamlPropertyIndex = 638
MediaElement_Source: XamlPropertyIndex = 639
MediaElement_Stereo3DVideoPackingMode: XamlPropertyIndex = 640
MediaElement_Stereo3DVideoRenderMode: XamlPropertyIndex = 641
MediaElement_Stretch: XamlPropertyIndex = 642
MediaElement_TransportControls: XamlPropertyIndex = 643
MediaElement_Volume: XamlPropertyIndex = 644
Panel_Background: XamlPropertyIndex = 647
Panel_Children: XamlPropertyIndex = 648
Panel_ChildrenTransitions: XamlPropertyIndex = 649
Panel_IsItemsHost: XamlPropertyIndex = 651
Paragraph_Inlines: XamlPropertyIndex = 652
Paragraph_TextIndent: XamlPropertyIndex = 653
PointerDownThemeAnimation_TargetName: XamlPropertyIndex = 660
PointerUpThemeAnimation_TargetName: XamlPropertyIndex = 662
PopInThemeAnimation_FromHorizontalOffset: XamlPropertyIndex = 664
PopInThemeAnimation_FromVerticalOffset: XamlPropertyIndex = 665
PopInThemeAnimation_TargetName: XamlPropertyIndex = 666
PopOutThemeAnimation_TargetName: XamlPropertyIndex = 667
Popup_Child: XamlPropertyIndex = 668
Popup_ChildTransitions: XamlPropertyIndex = 669
Popup_HorizontalOffset: XamlPropertyIndex = 670
Popup_IsLightDismissEnabled: XamlPropertyIndex = 673
Popup_IsOpen: XamlPropertyIndex = 674
Popup_VerticalOffset: XamlPropertyIndex = 676
RepositionThemeAnimation_FromHorizontalOffset: XamlPropertyIndex = 683
RepositionThemeAnimation_FromVerticalOffset: XamlPropertyIndex = 684
RepositionThemeAnimation_TargetName: XamlPropertyIndex = 685
ResourceDictionary_MergedDictionaries: XamlPropertyIndex = 687
ResourceDictionary_Source: XamlPropertyIndex = 688
ResourceDictionary_ThemeDictionaries: XamlPropertyIndex = 689
RichTextBlock_Blocks: XamlPropertyIndex = 691
RichTextBlock_CharacterSpacing: XamlPropertyIndex = 692
RichTextBlock_FontFamily: XamlPropertyIndex = 693
RichTextBlock_FontSize: XamlPropertyIndex = 694
RichTextBlock_FontStretch: XamlPropertyIndex = 695
RichTextBlock_FontStyle: XamlPropertyIndex = 696
RichTextBlock_FontWeight: XamlPropertyIndex = 697
RichTextBlock_Foreground: XamlPropertyIndex = 698
RichTextBlock_HasOverflowContent: XamlPropertyIndex = 699
RichTextBlock_IsColorFontEnabled: XamlPropertyIndex = 700
RichTextBlock_IsTextScaleFactorEnabled: XamlPropertyIndex = 701
RichTextBlock_IsTextSelectionEnabled: XamlPropertyIndex = 702
RichTextBlock_LineHeight: XamlPropertyIndex = 703
RichTextBlock_LineStackingStrategy: XamlPropertyIndex = 704
RichTextBlock_MaxLines: XamlPropertyIndex = 705
RichTextBlock_OpticalMarginAlignment: XamlPropertyIndex = 706
RichTextBlock_OverflowContentTarget: XamlPropertyIndex = 707
RichTextBlock_Padding: XamlPropertyIndex = 708
RichTextBlock_SelectedText: XamlPropertyIndex = 709
RichTextBlock_SelectionHighlightColor: XamlPropertyIndex = 710
RichTextBlock_TextAlignment: XamlPropertyIndex = 711
RichTextBlock_TextIndent: XamlPropertyIndex = 712
RichTextBlock_TextLineBounds: XamlPropertyIndex = 713
RichTextBlock_TextReadingOrder: XamlPropertyIndex = 714
RichTextBlock_TextTrimming: XamlPropertyIndex = 715
RichTextBlock_TextWrapping: XamlPropertyIndex = 716
RichTextBlockOverflow_HasOverflowContent: XamlPropertyIndex = 717
RichTextBlockOverflow_MaxLines: XamlPropertyIndex = 718
RichTextBlockOverflow_OverflowContentTarget: XamlPropertyIndex = 719
RichTextBlockOverflow_Padding: XamlPropertyIndex = 720
RotateTransform_Angle: XamlPropertyIndex = 721
RotateTransform_CenterX: XamlPropertyIndex = 722
RotateTransform_CenterY: XamlPropertyIndex = 723
Run_FlowDirection: XamlPropertyIndex = 725
Run_Text: XamlPropertyIndex = 726
ScaleTransform_CenterX: XamlPropertyIndex = 727
ScaleTransform_CenterY: XamlPropertyIndex = 728
ScaleTransform_ScaleX: XamlPropertyIndex = 729
ScaleTransform_ScaleY: XamlPropertyIndex = 730
SetterBaseCollection_IsSealed: XamlPropertyIndex = 732
Shape_Fill: XamlPropertyIndex = 733
Shape_GeometryTransform: XamlPropertyIndex = 734
Shape_Stretch: XamlPropertyIndex = 735
Shape_Stroke: XamlPropertyIndex = 736
Shape_StrokeDashArray: XamlPropertyIndex = 737
Shape_StrokeDashCap: XamlPropertyIndex = 738
Shape_StrokeDashOffset: XamlPropertyIndex = 739
Shape_StrokeEndLineCap: XamlPropertyIndex = 740
Shape_StrokeLineJoin: XamlPropertyIndex = 741
Shape_StrokeMiterLimit: XamlPropertyIndex = 742
Shape_StrokeStartLineCap: XamlPropertyIndex = 743
Shape_StrokeThickness: XamlPropertyIndex = 744
SkewTransform_AngleX: XamlPropertyIndex = 745
SkewTransform_AngleY: XamlPropertyIndex = 746
SkewTransform_CenterX: XamlPropertyIndex = 747
SkewTransform_CenterY: XamlPropertyIndex = 748
Span_Inlines: XamlPropertyIndex = 749
SplitCloseThemeAnimation_ClosedLength: XamlPropertyIndex = 750
SplitCloseThemeAnimation_ClosedTarget: XamlPropertyIndex = 751
SplitCloseThemeAnimation_ClosedTargetName: XamlPropertyIndex = 752
SplitCloseThemeAnimation_ContentTarget: XamlPropertyIndex = 753
SplitCloseThemeAnimation_ContentTargetName: XamlPropertyIndex = 754
SplitCloseThemeAnimation_ContentTranslationDirection: XamlPropertyIndex = 755
SplitCloseThemeAnimation_ContentTranslationOffset: XamlPropertyIndex = 756
SplitCloseThemeAnimation_OffsetFromCenter: XamlPropertyIndex = 757
SplitCloseThemeAnimation_OpenedLength: XamlPropertyIndex = 758
SplitCloseThemeAnimation_OpenedTarget: XamlPropertyIndex = 759
SplitCloseThemeAnimation_OpenedTargetName: XamlPropertyIndex = 760
SplitOpenThemeAnimation_ClosedLength: XamlPropertyIndex = 761
SplitOpenThemeAnimation_ClosedTarget: XamlPropertyIndex = 762
SplitOpenThemeAnimation_ClosedTargetName: XamlPropertyIndex = 763
SplitOpenThemeAnimation_ContentTarget: XamlPropertyIndex = 764
SplitOpenThemeAnimation_ContentTargetName: XamlPropertyIndex = 765
SplitOpenThemeAnimation_ContentTranslationDirection: XamlPropertyIndex = 766
SplitOpenThemeAnimation_ContentTranslationOffset: XamlPropertyIndex = 767
SplitOpenThemeAnimation_OffsetFromCenter: XamlPropertyIndex = 768
SplitOpenThemeAnimation_OpenedLength: XamlPropertyIndex = 769
SplitOpenThemeAnimation_OpenedTarget: XamlPropertyIndex = 770
SplitOpenThemeAnimation_OpenedTargetName: XamlPropertyIndex = 771
Storyboard_Children: XamlPropertyIndex = 772
Storyboard_TargetName: XamlPropertyIndex = 774
Storyboard_TargetProperty: XamlPropertyIndex = 775
SwipeBackThemeAnimation_FromHorizontalOffset: XamlPropertyIndex = 776
SwipeBackThemeAnimation_FromVerticalOffset: XamlPropertyIndex = 777
SwipeBackThemeAnimation_TargetName: XamlPropertyIndex = 778
SwipeHintThemeAnimation_TargetName: XamlPropertyIndex = 779
SwipeHintThemeAnimation_ToHorizontalOffset: XamlPropertyIndex = 780
SwipeHintThemeAnimation_ToVerticalOffset: XamlPropertyIndex = 781
TextBlock_CharacterSpacing: XamlPropertyIndex = 782
TextBlock_FontFamily: XamlPropertyIndex = 783
TextBlock_FontSize: XamlPropertyIndex = 784
TextBlock_FontStretch: XamlPropertyIndex = 785
TextBlock_FontStyle: XamlPropertyIndex = 786
TextBlock_FontWeight: XamlPropertyIndex = 787
TextBlock_Foreground: XamlPropertyIndex = 788
TextBlock_Inlines: XamlPropertyIndex = 789
TextBlock_IsColorFontEnabled: XamlPropertyIndex = 790
TextBlock_IsTextScaleFactorEnabled: XamlPropertyIndex = 791
TextBlock_IsTextSelectionEnabled: XamlPropertyIndex = 792
TextBlock_LineHeight: XamlPropertyIndex = 793
TextBlock_LineStackingStrategy: XamlPropertyIndex = 794
TextBlock_MaxLines: XamlPropertyIndex = 795
TextBlock_OpticalMarginAlignment: XamlPropertyIndex = 796
TextBlock_Padding: XamlPropertyIndex = 797
TextBlock_SelectedText: XamlPropertyIndex = 798
TextBlock_SelectionHighlightColor: XamlPropertyIndex = 799
TextBlock_Text: XamlPropertyIndex = 800
TextBlock_TextAlignment: XamlPropertyIndex = 801
TextBlock_TextDecorations: XamlPropertyIndex = 802
TextBlock_TextLineBounds: XamlPropertyIndex = 803
TextBlock_TextReadingOrder: XamlPropertyIndex = 804
TextBlock_TextTrimming: XamlPropertyIndex = 805
TextBlock_TextWrapping: XamlPropertyIndex = 806
TransformGroup_Children: XamlPropertyIndex = 811
TransformGroup_Value: XamlPropertyIndex = 812
TranslateTransform_X: XamlPropertyIndex = 814
TranslateTransform_Y: XamlPropertyIndex = 815
Viewbox_Child: XamlPropertyIndex = 819
Viewbox_Stretch: XamlPropertyIndex = 820
Viewbox_StretchDirection: XamlPropertyIndex = 821
WebViewBrush_SourceName: XamlPropertyIndex = 825
AppBarSeparator_IsCompact: XamlPropertyIndex = 826
BitmapIcon_UriSource: XamlPropertyIndex = 827
Canvas_Left: XamlPropertyIndex = 828
Canvas_Top: XamlPropertyIndex = 829
Canvas_ZIndex: XamlPropertyIndex = 830
ContentControl_Content: XamlPropertyIndex = 832
ContentControl_ContentTemplate: XamlPropertyIndex = 833
ContentControl_ContentTemplateSelector: XamlPropertyIndex = 834
ContentControl_ContentTransitions: XamlPropertyIndex = 835
DatePicker_CalendarIdentifier: XamlPropertyIndex = 837
DatePicker_Date: XamlPropertyIndex = 838
DatePicker_DayFormat: XamlPropertyIndex = 839
DatePicker_DayVisible: XamlPropertyIndex = 840
DatePicker_Header: XamlPropertyIndex = 841
DatePicker_HeaderTemplate: XamlPropertyIndex = 842
DatePicker_MaxYear: XamlPropertyIndex = 843
DatePicker_MinYear: XamlPropertyIndex = 844
DatePicker_MonthFormat: XamlPropertyIndex = 845
DatePicker_MonthVisible: XamlPropertyIndex = 846
DatePicker_Orientation: XamlPropertyIndex = 847
DatePicker_YearFormat: XamlPropertyIndex = 848
DatePicker_YearVisible: XamlPropertyIndex = 849
FontIcon_FontFamily: XamlPropertyIndex = 851
FontIcon_FontSize: XamlPropertyIndex = 852
FontIcon_FontStyle: XamlPropertyIndex = 853
FontIcon_FontWeight: XamlPropertyIndex = 854
FontIcon_Glyph: XamlPropertyIndex = 855
FontIcon_IsTextScaleFactorEnabled: XamlPropertyIndex = 856
Grid_Column: XamlPropertyIndex = 857
Grid_ColumnDefinitions: XamlPropertyIndex = 858
Grid_ColumnSpan: XamlPropertyIndex = 859
Grid_Row: XamlPropertyIndex = 860
Grid_RowDefinitions: XamlPropertyIndex = 861
Grid_RowSpan: XamlPropertyIndex = 862
Hub_DefaultSectionIndex: XamlPropertyIndex = 863
Hub_Header: XamlPropertyIndex = 864
Hub_HeaderTemplate: XamlPropertyIndex = 865
Hub_IsActiveView: XamlPropertyIndex = 866
Hub_IsZoomedInView: XamlPropertyIndex = 867
Hub_Orientation: XamlPropertyIndex = 868
Hub_SectionHeaders: XamlPropertyIndex = 869
Hub_Sections: XamlPropertyIndex = 870
Hub_SectionsInView: XamlPropertyIndex = 871
Hub_SemanticZoomOwner: XamlPropertyIndex = 872
HubSection_ContentTemplate: XamlPropertyIndex = 873
HubSection_Header: XamlPropertyIndex = 874
HubSection_HeaderTemplate: XamlPropertyIndex = 875
HubSection_IsHeaderInteractive: XamlPropertyIndex = 876
Hyperlink_NavigateUri: XamlPropertyIndex = 877
ItemsControl_DisplayMemberPath: XamlPropertyIndex = 879
ItemsControl_GroupStyle: XamlPropertyIndex = 880
ItemsControl_GroupStyleSelector: XamlPropertyIndex = 881
ItemsControl_IsGrouping: XamlPropertyIndex = 882
ItemsControl_ItemContainerStyle: XamlPropertyIndex = 884
ItemsControl_ItemContainerStyleSelector: XamlPropertyIndex = 885
ItemsControl_ItemContainerTransitions: XamlPropertyIndex = 886
ItemsControl_Items: XamlPropertyIndex = 887
ItemsControl_ItemsPanel: XamlPropertyIndex = 889
ItemsControl_ItemsSource: XamlPropertyIndex = 890
ItemsControl_ItemTemplate: XamlPropertyIndex = 891
ItemsControl_ItemTemplateSelector: XamlPropertyIndex = 892
Line_X1: XamlPropertyIndex = 893
Line_X2: XamlPropertyIndex = 894
Line_Y1: XamlPropertyIndex = 895
Line_Y2: XamlPropertyIndex = 896
MediaTransportControls_IsFastForwardButtonVisible: XamlPropertyIndex = 898
MediaTransportControls_IsFastRewindButtonVisible: XamlPropertyIndex = 900
MediaTransportControls_IsFullWindowButtonVisible: XamlPropertyIndex = 902
MediaTransportControls_IsPlaybackRateButtonVisible: XamlPropertyIndex = 904
MediaTransportControls_IsSeekBarVisible: XamlPropertyIndex = 905
MediaTransportControls_IsStopButtonVisible: XamlPropertyIndex = 908
MediaTransportControls_IsVolumeButtonVisible: XamlPropertyIndex = 910
MediaTransportControls_IsZoomButtonVisible: XamlPropertyIndex = 912
PasswordBox_Header: XamlPropertyIndex = 913
PasswordBox_HeaderTemplate: XamlPropertyIndex = 914
PasswordBox_IsPasswordRevealButtonEnabled: XamlPropertyIndex = 915
PasswordBox_MaxLength: XamlPropertyIndex = 916
PasswordBox_Password: XamlPropertyIndex = 917
PasswordBox_PasswordChar: XamlPropertyIndex = 918
PasswordBox_PlaceholderText: XamlPropertyIndex = 919
PasswordBox_PreventKeyboardDisplayOnProgrammaticFocus: XamlPropertyIndex = 920
PasswordBox_SelectionHighlightColor: XamlPropertyIndex = 921
Path_Data: XamlPropertyIndex = 922
PathIcon_Data: XamlPropertyIndex = 923
Polygon_FillRule: XamlPropertyIndex = 924
Polygon_Points: XamlPropertyIndex = 925
Polyline_FillRule: XamlPropertyIndex = 926
Polyline_Points: XamlPropertyIndex = 927
ProgressRing_IsActive: XamlPropertyIndex = 928
ProgressRing_TemplateSettings: XamlPropertyIndex = 929
RangeBase_LargeChange: XamlPropertyIndex = 930
RangeBase_Maximum: XamlPropertyIndex = 931
RangeBase_Minimum: XamlPropertyIndex = 932
RangeBase_SmallChange: XamlPropertyIndex = 933
RangeBase_Value: XamlPropertyIndex = 934
Rectangle_RadiusX: XamlPropertyIndex = 935
Rectangle_RadiusY: XamlPropertyIndex = 936
RichEditBox_AcceptsReturn: XamlPropertyIndex = 937
RichEditBox_Header: XamlPropertyIndex = 938
RichEditBox_HeaderTemplate: XamlPropertyIndex = 939
RichEditBox_InputScope: XamlPropertyIndex = 940
RichEditBox_IsColorFontEnabled: XamlPropertyIndex = 941
RichEditBox_IsReadOnly: XamlPropertyIndex = 942
RichEditBox_IsSpellCheckEnabled: XamlPropertyIndex = 943
RichEditBox_IsTextPredictionEnabled: XamlPropertyIndex = 944
RichEditBox_PlaceholderText: XamlPropertyIndex = 945
RichEditBox_PreventKeyboardDisplayOnProgrammaticFocus: XamlPropertyIndex = 946
RichEditBox_SelectionHighlightColor: XamlPropertyIndex = 947
RichEditBox_TextAlignment: XamlPropertyIndex = 948
RichEditBox_TextWrapping: XamlPropertyIndex = 949
SearchBox_ChooseSuggestionOnEnter: XamlPropertyIndex = 950
SearchBox_FocusOnKeyboardInput: XamlPropertyIndex = 951
SearchBox_PlaceholderText: XamlPropertyIndex = 952
SearchBox_QueryText: XamlPropertyIndex = 953
SearchBox_SearchHistoryContext: XamlPropertyIndex = 954
SearchBox_SearchHistoryEnabled: XamlPropertyIndex = 955
SemanticZoom_CanChangeViews: XamlPropertyIndex = 956
SemanticZoom_IsZoomedInViewActive: XamlPropertyIndex = 957
SemanticZoom_IsZoomOutButtonEnabled: XamlPropertyIndex = 958
SemanticZoom_ZoomedInView: XamlPropertyIndex = 959
SemanticZoom_ZoomedOutView: XamlPropertyIndex = 960
StackPanel_AreScrollSnapPointsRegular: XamlPropertyIndex = 961
StackPanel_Orientation: XamlPropertyIndex = 962
SymbolIcon_Symbol: XamlPropertyIndex = 963
TextBox_AcceptsReturn: XamlPropertyIndex = 964
TextBox_Header: XamlPropertyIndex = 965
TextBox_HeaderTemplate: XamlPropertyIndex = 966
TextBox_InputScope: XamlPropertyIndex = 967
TextBox_IsColorFontEnabled: XamlPropertyIndex = 968
TextBox_IsReadOnly: XamlPropertyIndex = 971
TextBox_IsSpellCheckEnabled: XamlPropertyIndex = 972
TextBox_IsTextPredictionEnabled: XamlPropertyIndex = 973
TextBox_MaxLength: XamlPropertyIndex = 974
TextBox_PlaceholderText: XamlPropertyIndex = 975
TextBox_PreventKeyboardDisplayOnProgrammaticFocus: XamlPropertyIndex = 976
TextBox_SelectedText: XamlPropertyIndex = 977
TextBox_SelectionHighlightColor: XamlPropertyIndex = 978
TextBox_SelectionLength: XamlPropertyIndex = 979
TextBox_SelectionStart: XamlPropertyIndex = 980
TextBox_Text: XamlPropertyIndex = 981
TextBox_TextAlignment: XamlPropertyIndex = 982
TextBox_TextWrapping: XamlPropertyIndex = 983
Thumb_IsDragging: XamlPropertyIndex = 984
TickBar_Fill: XamlPropertyIndex = 985
TimePicker_ClockIdentifier: XamlPropertyIndex = 986
TimePicker_Header: XamlPropertyIndex = 987
TimePicker_HeaderTemplate: XamlPropertyIndex = 988
TimePicker_MinuteIncrement: XamlPropertyIndex = 989
TimePicker_Time: XamlPropertyIndex = 990
ToggleSwitch_Header: XamlPropertyIndex = 991
ToggleSwitch_HeaderTemplate: XamlPropertyIndex = 992
ToggleSwitch_IsOn: XamlPropertyIndex = 993
ToggleSwitch_OffContent: XamlPropertyIndex = 994
ToggleSwitch_OffContentTemplate: XamlPropertyIndex = 995
ToggleSwitch_OnContent: XamlPropertyIndex = 996
ToggleSwitch_OnContentTemplate: XamlPropertyIndex = 997
ToggleSwitch_TemplateSettings: XamlPropertyIndex = 998
UserControl_Content: XamlPropertyIndex = 999
VariableSizedWrapGrid_ColumnSpan: XamlPropertyIndex = 1000
VariableSizedWrapGrid_HorizontalChildrenAlignment: XamlPropertyIndex = 1001
VariableSizedWrapGrid_ItemHeight: XamlPropertyIndex = 1002
VariableSizedWrapGrid_ItemWidth: XamlPropertyIndex = 1003
VariableSizedWrapGrid_MaximumRowsOrColumns: XamlPropertyIndex = 1004
VariableSizedWrapGrid_Orientation: XamlPropertyIndex = 1005
VariableSizedWrapGrid_RowSpan: XamlPropertyIndex = 1006
VariableSizedWrapGrid_VerticalChildrenAlignment: XamlPropertyIndex = 1007
WebView_AllowedScriptNotifyUris: XamlPropertyIndex = 1008
WebView_CanGoBack: XamlPropertyIndex = 1009
WebView_CanGoForward: XamlPropertyIndex = 1010
WebView_ContainsFullScreenElement: XamlPropertyIndex = 1011
WebView_DataTransferPackage: XamlPropertyIndex = 1012
WebView_DefaultBackgroundColor: XamlPropertyIndex = 1013
WebView_DocumentTitle: XamlPropertyIndex = 1014
WebView_Source: XamlPropertyIndex = 1015
AppBar_ClosedDisplayMode: XamlPropertyIndex = 1016
AppBar_IsOpen: XamlPropertyIndex = 1017
AppBar_IsSticky: XamlPropertyIndex = 1018
AutoSuggestBox_AutoMaximizeSuggestionArea: XamlPropertyIndex = 1019
AutoSuggestBox_Header: XamlPropertyIndex = 1020
AutoSuggestBox_IsSuggestionListOpen: XamlPropertyIndex = 1021
AutoSuggestBox_MaxSuggestionListHeight: XamlPropertyIndex = 1022
AutoSuggestBox_PlaceholderText: XamlPropertyIndex = 1023
AutoSuggestBox_Text: XamlPropertyIndex = 1024
AutoSuggestBox_TextBoxStyle: XamlPropertyIndex = 1025
AutoSuggestBox_TextMemberPath: XamlPropertyIndex = 1026
AutoSuggestBox_UpdateTextOnSelect: XamlPropertyIndex = 1027
ButtonBase_ClickMode: XamlPropertyIndex = 1029
ButtonBase_Command: XamlPropertyIndex = 1030
ButtonBase_CommandParameter: XamlPropertyIndex = 1031
ButtonBase_IsPointerOver: XamlPropertyIndex = 1032
ButtonBase_IsPressed: XamlPropertyIndex = 1033
ContentDialog_FullSizeDesired: XamlPropertyIndex = 1034
ContentDialog_IsPrimaryButtonEnabled: XamlPropertyIndex = 1035
ContentDialog_IsSecondaryButtonEnabled: XamlPropertyIndex = 1036
ContentDialog_PrimaryButtonCommand: XamlPropertyIndex = 1037
ContentDialog_PrimaryButtonCommandParameter: XamlPropertyIndex = 1038
ContentDialog_PrimaryButtonText: XamlPropertyIndex = 1039
ContentDialog_SecondaryButtonCommand: XamlPropertyIndex = 1040
ContentDialog_SecondaryButtonCommandParameter: XamlPropertyIndex = 1041
ContentDialog_SecondaryButtonText: XamlPropertyIndex = 1042
ContentDialog_Title: XamlPropertyIndex = 1043
ContentDialog_TitleTemplate: XamlPropertyIndex = 1044
Frame_BackStack: XamlPropertyIndex = 1045
Frame_BackStackDepth: XamlPropertyIndex = 1046
Frame_CacheSize: XamlPropertyIndex = 1047
Frame_CanGoBack: XamlPropertyIndex = 1048
Frame_CanGoForward: XamlPropertyIndex = 1049
Frame_CurrentSourcePageType: XamlPropertyIndex = 1050
Frame_ForwardStack: XamlPropertyIndex = 1051
Frame_SourcePageType: XamlPropertyIndex = 1052
GridViewItemPresenter_CheckBrush: XamlPropertyIndex = 1053
GridViewItemPresenter_CheckHintBrush: XamlPropertyIndex = 1054
GridViewItemPresenter_CheckSelectingBrush: XamlPropertyIndex = 1055
GridViewItemPresenter_ContentMargin: XamlPropertyIndex = 1056
GridViewItemPresenter_DisabledOpacity: XamlPropertyIndex = 1057
GridViewItemPresenter_DragBackground: XamlPropertyIndex = 1058
GridViewItemPresenter_DragForeground: XamlPropertyIndex = 1059
GridViewItemPresenter_DragOpacity: XamlPropertyIndex = 1060
GridViewItemPresenter_FocusBorderBrush: XamlPropertyIndex = 1061
GridViewItemPresenter_GridViewItemPresenterHorizontalContentAlignment: XamlPropertyIndex = 1062
GridViewItemPresenter_GridViewItemPresenterPadding: XamlPropertyIndex = 1063
GridViewItemPresenter_PlaceholderBackground: XamlPropertyIndex = 1064
GridViewItemPresenter_PointerOverBackground: XamlPropertyIndex = 1065
GridViewItemPresenter_PointerOverBackgroundMargin: XamlPropertyIndex = 1066
GridViewItemPresenter_ReorderHintOffset: XamlPropertyIndex = 1067
GridViewItemPresenter_SelectedBackground: XamlPropertyIndex = 1068
GridViewItemPresenter_SelectedBorderThickness: XamlPropertyIndex = 1069
GridViewItemPresenter_SelectedForeground: XamlPropertyIndex = 1070
GridViewItemPresenter_SelectedPointerOverBackground: XamlPropertyIndex = 1071
GridViewItemPresenter_SelectedPointerOverBorderBrush: XamlPropertyIndex = 1072
GridViewItemPresenter_SelectionCheckMarkVisualEnabled: XamlPropertyIndex = 1073
GridViewItemPresenter_GridViewItemPresenterVerticalContentAlignment: XamlPropertyIndex = 1074
ItemsStackPanel_CacheLength: XamlPropertyIndex = 1076
ItemsStackPanel_GroupHeaderPlacement: XamlPropertyIndex = 1077
ItemsStackPanel_GroupPadding: XamlPropertyIndex = 1078
ItemsStackPanel_ItemsUpdatingScrollMode: XamlPropertyIndex = 1079
ItemsStackPanel_Orientation: XamlPropertyIndex = 1080
ItemsWrapGrid_CacheLength: XamlPropertyIndex = 1081
ItemsWrapGrid_GroupHeaderPlacement: XamlPropertyIndex = 1082
ItemsWrapGrid_GroupPadding: XamlPropertyIndex = 1083
ItemsWrapGrid_ItemHeight: XamlPropertyIndex = 1084
ItemsWrapGrid_ItemWidth: XamlPropertyIndex = 1085
ItemsWrapGrid_MaximumRowsOrColumns: XamlPropertyIndex = 1086
ItemsWrapGrid_Orientation: XamlPropertyIndex = 1087
ListViewItemPresenter_CheckBrush: XamlPropertyIndex = 1088
ListViewItemPresenter_CheckHintBrush: XamlPropertyIndex = 1089
ListViewItemPresenter_CheckSelectingBrush: XamlPropertyIndex = 1090
ListViewItemPresenter_ContentMargin: XamlPropertyIndex = 1091
ListViewItemPresenter_DisabledOpacity: XamlPropertyIndex = 1092
ListViewItemPresenter_DragBackground: XamlPropertyIndex = 1093
ListViewItemPresenter_DragForeground: XamlPropertyIndex = 1094
ListViewItemPresenter_DragOpacity: XamlPropertyIndex = 1095
ListViewItemPresenter_FocusBorderBrush: XamlPropertyIndex = 1096
ListViewItemPresenter_ListViewItemPresenterHorizontalContentAlignment: XamlPropertyIndex = 1097
ListViewItemPresenter_ListViewItemPresenterPadding: XamlPropertyIndex = 1098
ListViewItemPresenter_PlaceholderBackground: XamlPropertyIndex = 1099
ListViewItemPresenter_PointerOverBackground: XamlPropertyIndex = 1100
ListViewItemPresenter_PointerOverBackgroundMargin: XamlPropertyIndex = 1101
ListViewItemPresenter_ReorderHintOffset: XamlPropertyIndex = 1102
ListViewItemPresenter_SelectedBackground: XamlPropertyIndex = 1103
ListViewItemPresenter_SelectedBorderThickness: XamlPropertyIndex = 1104
ListViewItemPresenter_SelectedForeground: XamlPropertyIndex = 1105
ListViewItemPresenter_SelectedPointerOverBackground: XamlPropertyIndex = 1106
ListViewItemPresenter_SelectedPointerOverBorderBrush: XamlPropertyIndex = 1107
ListViewItemPresenter_SelectionCheckMarkVisualEnabled: XamlPropertyIndex = 1108
ListViewItemPresenter_ListViewItemPresenterVerticalContentAlignment: XamlPropertyIndex = 1109
MenuFlyoutItem_Command: XamlPropertyIndex = 1110
MenuFlyoutItem_CommandParameter: XamlPropertyIndex = 1111
MenuFlyoutItem_Text: XamlPropertyIndex = 1112
Page_BottomAppBar: XamlPropertyIndex = 1114
Page_Frame: XamlPropertyIndex = 1115
Page_NavigationCacheMode: XamlPropertyIndex = 1116
Page_TopAppBar: XamlPropertyIndex = 1117
ProgressBar_IsIndeterminate: XamlPropertyIndex = 1118
ProgressBar_ShowError: XamlPropertyIndex = 1119
ProgressBar_ShowPaused: XamlPropertyIndex = 1120
ProgressBar_TemplateSettings: XamlPropertyIndex = 1121
ScrollBar_IndicatorMode: XamlPropertyIndex = 1122
ScrollBar_Orientation: XamlPropertyIndex = 1123
ScrollBar_ViewportSize: XamlPropertyIndex = 1124
Selector_IsSynchronizedWithCurrentItem: XamlPropertyIndex = 1126
Selector_SelectedIndex: XamlPropertyIndex = 1127
Selector_SelectedItem: XamlPropertyIndex = 1128
Selector_SelectedValue: XamlPropertyIndex = 1129
Selector_SelectedValuePath: XamlPropertyIndex = 1130
SelectorItem_IsSelected: XamlPropertyIndex = 1131
SettingsFlyout_HeaderBackground: XamlPropertyIndex = 1132
SettingsFlyout_HeaderForeground: XamlPropertyIndex = 1133
SettingsFlyout_IconSource: XamlPropertyIndex = 1134
SettingsFlyout_TemplateSettings: XamlPropertyIndex = 1135
SettingsFlyout_Title: XamlPropertyIndex = 1136
Slider_Header: XamlPropertyIndex = 1137
Slider_HeaderTemplate: XamlPropertyIndex = 1138
Slider_IntermediateValue: XamlPropertyIndex = 1139
Slider_IsDirectionReversed: XamlPropertyIndex = 1140
Slider_IsThumbToolTipEnabled: XamlPropertyIndex = 1141
Slider_Orientation: XamlPropertyIndex = 1142
Slider_SnapsTo: XamlPropertyIndex = 1143
Slider_StepFrequency: XamlPropertyIndex = 1144
Slider_ThumbToolTipValueConverter: XamlPropertyIndex = 1145
Slider_TickFrequency: XamlPropertyIndex = 1146
Slider_TickPlacement: XamlPropertyIndex = 1147
SwapChainPanel_CompositionScaleX: XamlPropertyIndex = 1148
SwapChainPanel_CompositionScaleY: XamlPropertyIndex = 1149
ToolTip_HorizontalOffset: XamlPropertyIndex = 1150
ToolTip_IsOpen: XamlPropertyIndex = 1151
ToolTip_Placement: XamlPropertyIndex = 1152
ToolTip_PlacementTarget: XamlPropertyIndex = 1153
ToolTip_TemplateSettings: XamlPropertyIndex = 1154
ToolTip_VerticalOffset: XamlPropertyIndex = 1155
Button_Flyout: XamlPropertyIndex = 1156
ComboBox_Header: XamlPropertyIndex = 1157
ComboBox_HeaderTemplate: XamlPropertyIndex = 1158
ComboBox_IsDropDownOpen: XamlPropertyIndex = 1159
ComboBox_IsEditable: XamlPropertyIndex = 1160
ComboBox_IsSelectionBoxHighlighted: XamlPropertyIndex = 1161
ComboBox_MaxDropDownHeight: XamlPropertyIndex = 1162
ComboBox_PlaceholderText: XamlPropertyIndex = 1163
ComboBox_SelectionBoxItem: XamlPropertyIndex = 1164
ComboBox_SelectionBoxItemTemplate: XamlPropertyIndex = 1165
ComboBox_TemplateSettings: XamlPropertyIndex = 1166
CommandBar_PrimaryCommands: XamlPropertyIndex = 1167
CommandBar_SecondaryCommands: XamlPropertyIndex = 1168
FlipView_UseTouchAnimationsForAllNavigation: XamlPropertyIndex = 1169
HyperlinkButton_NavigateUri: XamlPropertyIndex = 1170
ListBox_SelectedItems: XamlPropertyIndex = 1171
ListBox_SelectionMode: XamlPropertyIndex = 1172
ListViewBase_CanDragItems: XamlPropertyIndex = 1173
ListViewBase_CanReorderItems: XamlPropertyIndex = 1174
ListViewBase_DataFetchSize: XamlPropertyIndex = 1175
ListViewBase_Footer: XamlPropertyIndex = 1176
ListViewBase_FooterTemplate: XamlPropertyIndex = 1177
ListViewBase_FooterTransitions: XamlPropertyIndex = 1178
ListViewBase_Header: XamlPropertyIndex = 1179
ListViewBase_HeaderTemplate: XamlPropertyIndex = 1180
ListViewBase_HeaderTransitions: XamlPropertyIndex = 1181
ListViewBase_IncrementalLoadingThreshold: XamlPropertyIndex = 1182
ListViewBase_IncrementalLoadingTrigger: XamlPropertyIndex = 1183
ListViewBase_IsActiveView: XamlPropertyIndex = 1184
ListViewBase_IsItemClickEnabled: XamlPropertyIndex = 1185
ListViewBase_IsSwipeEnabled: XamlPropertyIndex = 1186
ListViewBase_IsZoomedInView: XamlPropertyIndex = 1187
ListViewBase_ReorderMode: XamlPropertyIndex = 1188
ListViewBase_SelectedItems: XamlPropertyIndex = 1189
ListViewBase_SelectionMode: XamlPropertyIndex = 1190
ListViewBase_SemanticZoomOwner: XamlPropertyIndex = 1191
ListViewBase_ShowsScrollingPlaceholders: XamlPropertyIndex = 1192
RepeatButton_Delay: XamlPropertyIndex = 1193
RepeatButton_Interval: XamlPropertyIndex = 1194
ScrollViewer_BringIntoViewOnFocusChange: XamlPropertyIndex = 1195
ScrollViewer_ComputedHorizontalScrollBarVisibility: XamlPropertyIndex = 1196
ScrollViewer_ComputedVerticalScrollBarVisibility: XamlPropertyIndex = 1197
ScrollViewer_ExtentHeight: XamlPropertyIndex = 1198
ScrollViewer_ExtentWidth: XamlPropertyIndex = 1199
ScrollViewer_HorizontalOffset: XamlPropertyIndex = 1200
ScrollViewer_HorizontalScrollBarVisibility: XamlPropertyIndex = 1201
ScrollViewer_HorizontalScrollMode: XamlPropertyIndex = 1202
ScrollViewer_HorizontalSnapPointsAlignment: XamlPropertyIndex = 1203
ScrollViewer_HorizontalSnapPointsType: XamlPropertyIndex = 1204
ScrollViewer_IsDeferredScrollingEnabled: XamlPropertyIndex = 1205
ScrollViewer_IsHorizontalRailEnabled: XamlPropertyIndex = 1206
ScrollViewer_IsHorizontalScrollChainingEnabled: XamlPropertyIndex = 1207
ScrollViewer_IsScrollInertiaEnabled: XamlPropertyIndex = 1208
ScrollViewer_IsVerticalRailEnabled: XamlPropertyIndex = 1209
ScrollViewer_IsVerticalScrollChainingEnabled: XamlPropertyIndex = 1210
ScrollViewer_IsZoomChainingEnabled: XamlPropertyIndex = 1211
ScrollViewer_IsZoomInertiaEnabled: XamlPropertyIndex = 1212
ScrollViewer_LeftHeader: XamlPropertyIndex = 1213
ScrollViewer_MaxZoomFactor: XamlPropertyIndex = 1214
ScrollViewer_MinZoomFactor: XamlPropertyIndex = 1215
ScrollViewer_ScrollableHeight: XamlPropertyIndex = 1216
ScrollViewer_ScrollableWidth: XamlPropertyIndex = 1217
ScrollViewer_TopHeader: XamlPropertyIndex = 1218
ScrollViewer_TopLeftHeader: XamlPropertyIndex = 1219
ScrollViewer_VerticalOffset: XamlPropertyIndex = 1220
ScrollViewer_VerticalScrollBarVisibility: XamlPropertyIndex = 1221
ScrollViewer_VerticalScrollMode: XamlPropertyIndex = 1222
ScrollViewer_VerticalSnapPointsAlignment: XamlPropertyIndex = 1223
ScrollViewer_VerticalSnapPointsType: XamlPropertyIndex = 1224
ScrollViewer_ViewportHeight: XamlPropertyIndex = 1225
ScrollViewer_ViewportWidth: XamlPropertyIndex = 1226
ScrollViewer_ZoomFactor: XamlPropertyIndex = 1227
ScrollViewer_ZoomMode: XamlPropertyIndex = 1228
ScrollViewer_ZoomSnapPoints: XamlPropertyIndex = 1229
ScrollViewer_ZoomSnapPointsType: XamlPropertyIndex = 1230
ToggleButton_IsChecked: XamlPropertyIndex = 1231
ToggleButton_IsThreeState: XamlPropertyIndex = 1232
ToggleMenuFlyoutItem_IsChecked: XamlPropertyIndex = 1233
VirtualizingStackPanel_AreScrollSnapPointsRegular: XamlPropertyIndex = 1234
VirtualizingStackPanel_IsVirtualizing: XamlPropertyIndex = 1236
VirtualizingStackPanel_Orientation: XamlPropertyIndex = 1237
VirtualizingStackPanel_VirtualizationMode: XamlPropertyIndex = 1238
WrapGrid_HorizontalChildrenAlignment: XamlPropertyIndex = 1239
WrapGrid_ItemHeight: XamlPropertyIndex = 1240
WrapGrid_ItemWidth: XamlPropertyIndex = 1241
WrapGrid_MaximumRowsOrColumns: XamlPropertyIndex = 1242
WrapGrid_Orientation: XamlPropertyIndex = 1243
WrapGrid_VerticalChildrenAlignment: XamlPropertyIndex = 1244
AppBarButton_Icon: XamlPropertyIndex = 1245
AppBarButton_IsCompact: XamlPropertyIndex = 1246
AppBarButton_Label: XamlPropertyIndex = 1247
AppBarToggleButton_Icon: XamlPropertyIndex = 1248
AppBarToggleButton_IsCompact: XamlPropertyIndex = 1249
AppBarToggleButton_Label: XamlPropertyIndex = 1250
GridViewItem_TemplateSettings: XamlPropertyIndex = 1251
ListViewItem_TemplateSettings: XamlPropertyIndex = 1252
RadioButton_GroupName: XamlPropertyIndex = 1253
Glyphs_ColorFontPaletteIndex: XamlPropertyIndex = 1267
Glyphs_IsColorFontEnabled: XamlPropertyIndex = 1268
CalendarViewTemplateSettings_HasMoreContentAfter: XamlPropertyIndex = 1274
CalendarViewTemplateSettings_HasMoreContentBefore: XamlPropertyIndex = 1275
CalendarViewTemplateSettings_HasMoreViews: XamlPropertyIndex = 1276
CalendarViewTemplateSettings_HeaderText: XamlPropertyIndex = 1277
CalendarViewTemplateSettings_WeekDay1: XamlPropertyIndex = 1280
CalendarViewTemplateSettings_WeekDay2: XamlPropertyIndex = 1281
CalendarViewTemplateSettings_WeekDay3: XamlPropertyIndex = 1282
CalendarViewTemplateSettings_WeekDay4: XamlPropertyIndex = 1283
CalendarViewTemplateSettings_WeekDay5: XamlPropertyIndex = 1284
CalendarViewTemplateSettings_WeekDay6: XamlPropertyIndex = 1285
CalendarViewTemplateSettings_WeekDay7: XamlPropertyIndex = 1286
CalendarView_CalendarIdentifier: XamlPropertyIndex = 1291
CalendarView_DayOfWeekFormat: XamlPropertyIndex = 1299
CalendarView_DisplayMode: XamlPropertyIndex = 1302
CalendarView_FirstDayOfWeek: XamlPropertyIndex = 1303
CalendarView_IsOutOfScopeEnabled: XamlPropertyIndex = 1317
CalendarView_IsTodayHighlighted: XamlPropertyIndex = 1318
CalendarView_MaxDate: XamlPropertyIndex = 1320
CalendarView_MinDate: XamlPropertyIndex = 1321
CalendarView_NumberOfWeeksInView: XamlPropertyIndex = 1327
CalendarView_SelectedDates: XamlPropertyIndex = 1333
CalendarView_SelectionMode: XamlPropertyIndex = 1335
CalendarView_TemplateSettings: XamlPropertyIndex = 1336
CalendarViewDayItem_Date: XamlPropertyIndex = 1339
CalendarViewDayItem_IsBlackout: XamlPropertyIndex = 1340
MediaTransportControls_IsFastForwardEnabled: XamlPropertyIndex = 1382
MediaTransportControls_IsFastRewindEnabled: XamlPropertyIndex = 1383
MediaTransportControls_IsFullWindowEnabled: XamlPropertyIndex = 1384
MediaTransportControls_IsPlaybackRateEnabled: XamlPropertyIndex = 1385
MediaTransportControls_IsSeekEnabled: XamlPropertyIndex = 1386
MediaTransportControls_IsStopEnabled: XamlPropertyIndex = 1387
MediaTransportControls_IsVolumeEnabled: XamlPropertyIndex = 1388
MediaTransportControls_IsZoomEnabled: XamlPropertyIndex = 1389
ContentPresenter_LineHeight: XamlPropertyIndex = 1425
CalendarViewTemplateSettings_MinViewWidth: XamlPropertyIndex = 1435
ListViewBase_SelectedRanges: XamlPropertyIndex = 1459
SplitViewTemplateSettings_CompactPaneGridLength: XamlPropertyIndex = 1462
SplitViewTemplateSettings_NegativeOpenPaneLength: XamlPropertyIndex = 1463
SplitViewTemplateSettings_NegativeOpenPaneLengthMinusCompactLength: XamlPropertyIndex = 1464
SplitViewTemplateSettings_OpenPaneGridLength: XamlPropertyIndex = 1465
SplitViewTemplateSettings_OpenPaneLengthMinusCompactLength: XamlPropertyIndex = 1466
SplitView_CompactPaneLength: XamlPropertyIndex = 1467
SplitView_Content: XamlPropertyIndex = 1468
SplitView_DisplayMode: XamlPropertyIndex = 1469
SplitView_IsPaneOpen: XamlPropertyIndex = 1470
SplitView_OpenPaneLength: XamlPropertyIndex = 1471
SplitView_Pane: XamlPropertyIndex = 1472
SplitView_PanePlacement: XamlPropertyIndex = 1473
SplitView_TemplateSettings: XamlPropertyIndex = 1474
UIElement_Transform3D: XamlPropertyIndex = 1475
CompositeTransform3D_CenterX: XamlPropertyIndex = 1476
CompositeTransform3D_CenterY: XamlPropertyIndex = 1478
CompositeTransform3D_CenterZ: XamlPropertyIndex = 1480
CompositeTransform3D_RotationX: XamlPropertyIndex = 1482
CompositeTransform3D_RotationY: XamlPropertyIndex = 1484
CompositeTransform3D_RotationZ: XamlPropertyIndex = 1486
CompositeTransform3D_ScaleX: XamlPropertyIndex = 1488
CompositeTransform3D_ScaleY: XamlPropertyIndex = 1490
CompositeTransform3D_ScaleZ: XamlPropertyIndex = 1492
CompositeTransform3D_TranslateX: XamlPropertyIndex = 1494
CompositeTransform3D_TranslateY: XamlPropertyIndex = 1496
CompositeTransform3D_TranslateZ: XamlPropertyIndex = 1498
PerspectiveTransform3D_Depth: XamlPropertyIndex = 1500
PerspectiveTransform3D_OffsetX: XamlPropertyIndex = 1501
PerspectiveTransform3D_OffsetY: XamlPropertyIndex = 1502
RelativePanel_Above: XamlPropertyIndex = 1508
RelativePanel_AlignBottomWith: XamlPropertyIndex = 1509
RelativePanel_AlignLeftWith: XamlPropertyIndex = 1510
RelativePanel_AlignRightWith: XamlPropertyIndex = 1515
RelativePanel_AlignTopWith: XamlPropertyIndex = 1516
RelativePanel_Below: XamlPropertyIndex = 1517
RelativePanel_LeftOf: XamlPropertyIndex = 1520
RelativePanel_RightOf: XamlPropertyIndex = 1521
SplitViewTemplateSettings_OpenPaneLength: XamlPropertyIndex = 1524
PasswordBox_PasswordRevealMode: XamlPropertyIndex = 1527
SplitView_PaneBackground: XamlPropertyIndex = 1528
ItemsStackPanel_AreStickyGroupHeadersEnabled: XamlPropertyIndex = 1529
ItemsWrapGrid_AreStickyGroupHeadersEnabled: XamlPropertyIndex = 1530
MenuFlyoutSubItem_Items: XamlPropertyIndex = 1531
MenuFlyoutSubItem_Text: XamlPropertyIndex = 1532
UIElement_CanDrag: XamlPropertyIndex = 1534
DataTemplate_ExtensionInstance: XamlPropertyIndex = 1535
RelativePanel_AlignHorizontalCenterWith: XamlPropertyIndex = 1552
RelativePanel_AlignVerticalCenterWith: XamlPropertyIndex = 1553
TargetPropertyPath_Path: XamlPropertyIndex = 1555
TargetPropertyPath_Target: XamlPropertyIndex = 1556
VisualState_Setters: XamlPropertyIndex = 1558
VisualState_StateTriggers: XamlPropertyIndex = 1559
AdaptiveTrigger_MinWindowHeight: XamlPropertyIndex = 1560
AdaptiveTrigger_MinWindowWidth: XamlPropertyIndex = 1561
Setter_Target: XamlPropertyIndex = 1562
CalendarView_BlackoutForeground: XamlPropertyIndex = 1565
CalendarView_CalendarItemBackground: XamlPropertyIndex = 1566
CalendarView_CalendarItemBorderBrush: XamlPropertyIndex = 1567
CalendarView_CalendarItemBorderThickness: XamlPropertyIndex = 1568
CalendarView_CalendarItemForeground: XamlPropertyIndex = 1569
CalendarView_CalendarViewDayItemStyle: XamlPropertyIndex = 1570
CalendarView_DayItemFontFamily: XamlPropertyIndex = 1571
CalendarView_DayItemFontSize: XamlPropertyIndex = 1572
CalendarView_DayItemFontStyle: XamlPropertyIndex = 1573
CalendarView_DayItemFontWeight: XamlPropertyIndex = 1574
CalendarView_FirstOfMonthLabelFontFamily: XamlPropertyIndex = 1575
CalendarView_FirstOfMonthLabelFontSize: XamlPropertyIndex = 1576
CalendarView_FirstOfMonthLabelFontStyle: XamlPropertyIndex = 1577
CalendarView_FirstOfMonthLabelFontWeight: XamlPropertyIndex = 1578
CalendarView_FirstOfYearDecadeLabelFontFamily: XamlPropertyIndex = 1579
CalendarView_FirstOfYearDecadeLabelFontSize: XamlPropertyIndex = 1580
CalendarView_FirstOfYearDecadeLabelFontStyle: XamlPropertyIndex = 1581
CalendarView_FirstOfYearDecadeLabelFontWeight: XamlPropertyIndex = 1582
CalendarView_FocusBorderBrush: XamlPropertyIndex = 1583
CalendarView_HorizontalDayItemAlignment: XamlPropertyIndex = 1584
CalendarView_HorizontalFirstOfMonthLabelAlignment: XamlPropertyIndex = 1585
CalendarView_HoverBorderBrush: XamlPropertyIndex = 1586
CalendarView_MonthYearItemFontFamily: XamlPropertyIndex = 1588
CalendarView_MonthYearItemFontSize: XamlPropertyIndex = 1589
CalendarView_MonthYearItemFontStyle: XamlPropertyIndex = 1590
CalendarView_MonthYearItemFontWeight: XamlPropertyIndex = 1591
CalendarView_OutOfScopeBackground: XamlPropertyIndex = 1592
CalendarView_OutOfScopeForeground: XamlPropertyIndex = 1593
CalendarView_PressedBorderBrush: XamlPropertyIndex = 1594
CalendarView_PressedForeground: XamlPropertyIndex = 1595
CalendarView_SelectedBorderBrush: XamlPropertyIndex = 1596
CalendarView_SelectedForeground: XamlPropertyIndex = 1597
CalendarView_SelectedHoverBorderBrush: XamlPropertyIndex = 1598
CalendarView_SelectedPressedBorderBrush: XamlPropertyIndex = 1599
CalendarView_TodayFontWeight: XamlPropertyIndex = 1600
CalendarView_TodayForeground: XamlPropertyIndex = 1601
CalendarView_VerticalDayItemAlignment: XamlPropertyIndex = 1602
CalendarView_VerticalFirstOfMonthLabelAlignment: XamlPropertyIndex = 1603
MediaTransportControls_IsCompact: XamlPropertyIndex = 1605
RelativePanel_AlignBottomWithPanel: XamlPropertyIndex = 1606
RelativePanel_AlignHorizontalCenterWithPanel: XamlPropertyIndex = 1607
RelativePanel_AlignLeftWithPanel: XamlPropertyIndex = 1608
RelativePanel_AlignRightWithPanel: XamlPropertyIndex = 1609
RelativePanel_AlignTopWithPanel: XamlPropertyIndex = 1610
RelativePanel_AlignVerticalCenterWithPanel: XamlPropertyIndex = 1611
ListViewBase_IsMultiSelectCheckBoxEnabled: XamlPropertyIndex = 1612
AutomationProperties_Level: XamlPropertyIndex = 1614
AutomationProperties_PositionInSet: XamlPropertyIndex = 1615
AutomationProperties_SizeOfSet: XamlPropertyIndex = 1616
ListViewItemPresenter_CheckBoxBrush: XamlPropertyIndex = 1617
ListViewItemPresenter_CheckMode: XamlPropertyIndex = 1618
ListViewItemPresenter_PressedBackground: XamlPropertyIndex = 1620
ListViewItemPresenter_SelectedPressedBackground: XamlPropertyIndex = 1621
Control_IsTemplateFocusTarget: XamlPropertyIndex = 1623
Control_UseSystemFocusVisuals: XamlPropertyIndex = 1624
ListViewItemPresenter_FocusSecondaryBorderBrush: XamlPropertyIndex = 1628
ListViewItemPresenter_PointerOverForeground: XamlPropertyIndex = 1630
FontIcon_MirroredWhenRightToLeft: XamlPropertyIndex = 1631
CalendarViewTemplateSettings_CenterX: XamlPropertyIndex = 1632
CalendarViewTemplateSettings_CenterY: XamlPropertyIndex = 1633
CalendarViewTemplateSettings_ClipRect: XamlPropertyIndex = 1634
PasswordBox_TextReadingOrder: XamlPropertyIndex = 1650
RichEditBox_TextReadingOrder: XamlPropertyIndex = 1651
TextBox_TextReadingOrder: XamlPropertyIndex = 1652
WebView_ExecutionMode: XamlPropertyIndex = 1653
WebView_DeferredPermissionRequests: XamlPropertyIndex = 1655
WebView_Settings: XamlPropertyIndex = 1656
RichEditBox_DesiredCandidateWindowAlignment: XamlPropertyIndex = 1660
TextBox_DesiredCandidateWindowAlignment: XamlPropertyIndex = 1662
CalendarDatePicker_CalendarIdentifier: XamlPropertyIndex = 1663
CalendarDatePicker_CalendarViewStyle: XamlPropertyIndex = 1664
CalendarDatePicker_Date: XamlPropertyIndex = 1665
CalendarDatePicker_DateFormat: XamlPropertyIndex = 1666
CalendarDatePicker_DayOfWeekFormat: XamlPropertyIndex = 1667
CalendarDatePicker_DisplayMode: XamlPropertyIndex = 1668
CalendarDatePicker_FirstDayOfWeek: XamlPropertyIndex = 1669
CalendarDatePicker_Header: XamlPropertyIndex = 1670
CalendarDatePicker_HeaderTemplate: XamlPropertyIndex = 1671
CalendarDatePicker_IsCalendarOpen: XamlPropertyIndex = 1672
CalendarDatePicker_IsGroupLabelVisible: XamlPropertyIndex = 1673
CalendarDatePicker_IsOutOfScopeEnabled: XamlPropertyIndex = 1674
CalendarDatePicker_IsTodayHighlighted: XamlPropertyIndex = 1675
CalendarDatePicker_MaxDate: XamlPropertyIndex = 1676
CalendarDatePicker_MinDate: XamlPropertyIndex = 1677
CalendarDatePicker_PlaceholderText: XamlPropertyIndex = 1678
CalendarView_IsGroupLabelVisible: XamlPropertyIndex = 1679
ContentPresenter_Background: XamlPropertyIndex = 1680
ContentPresenter_BorderBrush: XamlPropertyIndex = 1681
ContentPresenter_BorderThickness: XamlPropertyIndex = 1682
ContentPresenter_CornerRadius: XamlPropertyIndex = 1683
ContentPresenter_Padding: XamlPropertyIndex = 1684
Grid_BorderBrush: XamlPropertyIndex = 1685
Grid_BorderThickness: XamlPropertyIndex = 1686
Grid_CornerRadius: XamlPropertyIndex = 1687
Grid_Padding: XamlPropertyIndex = 1688
RelativePanel_BorderBrush: XamlPropertyIndex = 1689
RelativePanel_BorderThickness: XamlPropertyIndex = 1690
RelativePanel_CornerRadius: XamlPropertyIndex = 1691
RelativePanel_Padding: XamlPropertyIndex = 1692
StackPanel_BorderBrush: XamlPropertyIndex = 1693
StackPanel_BorderThickness: XamlPropertyIndex = 1694
StackPanel_CornerRadius: XamlPropertyIndex = 1695
StackPanel_Padding: XamlPropertyIndex = 1696
PasswordBox_InputScope: XamlPropertyIndex = 1697
MediaTransportControlsHelper_DropoutOrder: XamlPropertyIndex = 1698
AutoSuggestBoxQuerySubmittedEventArgs_ChosenSuggestion: XamlPropertyIndex = 1699
AutoSuggestBoxQuerySubmittedEventArgs_QueryText: XamlPropertyIndex = 1700
AutoSuggestBox_QueryIcon: XamlPropertyIndex = 1701
StateTrigger_IsActive: XamlPropertyIndex = 1702
ContentPresenter_HorizontalContentAlignment: XamlPropertyIndex = 1703
ContentPresenter_VerticalContentAlignment: XamlPropertyIndex = 1704
AppBarTemplateSettings_ClipRect: XamlPropertyIndex = 1705
AppBarTemplateSettings_CompactRootMargin: XamlPropertyIndex = 1706
AppBarTemplateSettings_CompactVerticalDelta: XamlPropertyIndex = 1707
AppBarTemplateSettings_HiddenRootMargin: XamlPropertyIndex = 1708
AppBarTemplateSettings_HiddenVerticalDelta: XamlPropertyIndex = 1709
AppBarTemplateSettings_MinimalRootMargin: XamlPropertyIndex = 1710
AppBarTemplateSettings_MinimalVerticalDelta: XamlPropertyIndex = 1711
CommandBarTemplateSettings_ContentHeight: XamlPropertyIndex = 1712
CommandBarTemplateSettings_NegativeOverflowContentHeight: XamlPropertyIndex = 1713
CommandBarTemplateSettings_OverflowContentClipRect: XamlPropertyIndex = 1714
CommandBarTemplateSettings_OverflowContentHeight: XamlPropertyIndex = 1715
CommandBarTemplateSettings_OverflowContentHorizontalOffset: XamlPropertyIndex = 1716
CommandBarTemplateSettings_OverflowContentMaxHeight: XamlPropertyIndex = 1717
CommandBarTemplateSettings_OverflowContentMinWidth: XamlPropertyIndex = 1718
AppBar_TemplateSettings: XamlPropertyIndex = 1719
CommandBar_CommandBarOverflowPresenterStyle: XamlPropertyIndex = 1720
CommandBar_CommandBarTemplateSettings: XamlPropertyIndex = 1721
DrillInThemeAnimation_EntranceTarget: XamlPropertyIndex = 1722
DrillInThemeAnimation_EntranceTargetName: XamlPropertyIndex = 1723
DrillInThemeAnimation_ExitTarget: XamlPropertyIndex = 1724
DrillInThemeAnimation_ExitTargetName: XamlPropertyIndex = 1725
DrillOutThemeAnimation_EntranceTarget: XamlPropertyIndex = 1726
DrillOutThemeAnimation_EntranceTargetName: XamlPropertyIndex = 1727
DrillOutThemeAnimation_ExitTarget: XamlPropertyIndex = 1728
DrillOutThemeAnimation_ExitTargetName: XamlPropertyIndex = 1729
XamlBindingHelper_DataTemplateComponent: XamlPropertyIndex = 1730
AutomationProperties_Annotations: XamlPropertyIndex = 1732
AutomationAnnotation_Element: XamlPropertyIndex = 1733
AutomationAnnotation_Type: XamlPropertyIndex = 1734
AutomationPeerAnnotation_Peer: XamlPropertyIndex = 1735
AutomationPeerAnnotation_Type: XamlPropertyIndex = 1736
Hyperlink_UnderlineStyle: XamlPropertyIndex = 1741
CalendarView_DisabledForeground: XamlPropertyIndex = 1742
CalendarView_TodayBackground: XamlPropertyIndex = 1743
CalendarView_TodayBlackoutBackground: XamlPropertyIndex = 1744
CalendarView_TodaySelectedInnerBorderBrush: XamlPropertyIndex = 1747
Control_IsFocusEngaged: XamlPropertyIndex = 1749
Control_IsFocusEngagementEnabled: XamlPropertyIndex = 1752
RichEditBox_ClipboardCopyFormat: XamlPropertyIndex = 1754
CommandBarTemplateSettings_OverflowContentMaxWidth: XamlPropertyIndex = 1757
ComboBoxTemplateSettings_DropDownContentMinWidth: XamlPropertyIndex = 1758
MenuFlyoutPresenterTemplateSettings_FlyoutContentMinWidth: XamlPropertyIndex = 1762
MenuFlyoutPresenter_TemplateSettings: XamlPropertyIndex = 1763
AutomationProperties_LandmarkType: XamlPropertyIndex = 1766
AutomationProperties_LocalizedLandmarkType: XamlPropertyIndex = 1767
RepositionThemeTransition_IsStaggeringEnabled: XamlPropertyIndex = 1769
ListBox_SingleSelectionFollowsFocus: XamlPropertyIndex = 1770
ListViewBase_SingleSelectionFollowsFocus: XamlPropertyIndex = 1771
BitmapImage_AutoPlay: XamlPropertyIndex = 1773
BitmapImage_IsAnimatedBitmap: XamlPropertyIndex = 1774
BitmapImage_IsPlaying: XamlPropertyIndex = 1775
AutomationProperties_FullDescription: XamlPropertyIndex = 1776
AutomationProperties_IsDataValidForForm: XamlPropertyIndex = 1777
AutomationProperties_IsPeripheral: XamlPropertyIndex = 1778
AutomationProperties_LocalizedControlType: XamlPropertyIndex = 1779
FlyoutBase_AllowFocusOnInteraction: XamlPropertyIndex = 1780
TextElement_AllowFocusOnInteraction: XamlPropertyIndex = 1781
FrameworkElement_AllowFocusOnInteraction: XamlPropertyIndex = 1782
Control_RequiresPointer: XamlPropertyIndex = 1783
UIElement_ContextFlyout: XamlPropertyIndex = 1785
TextElement_AccessKey: XamlPropertyIndex = 1786
UIElement_AccessKeyScopeOwner: XamlPropertyIndex = 1787
UIElement_IsAccessKeyScope: XamlPropertyIndex = 1788
AutomationProperties_DescribedBy: XamlPropertyIndex = 1790
UIElement_AccessKey: XamlPropertyIndex = 1803
Control_XYFocusDown: XamlPropertyIndex = 1804
Control_XYFocusLeft: XamlPropertyIndex = 1805
Control_XYFocusRight: XamlPropertyIndex = 1806
Control_XYFocusUp: XamlPropertyIndex = 1807
Hyperlink_XYFocusDown: XamlPropertyIndex = 1808
Hyperlink_XYFocusLeft: XamlPropertyIndex = 1809
Hyperlink_XYFocusRight: XamlPropertyIndex = 1810
Hyperlink_XYFocusUp: XamlPropertyIndex = 1811
WebView_XYFocusDown: XamlPropertyIndex = 1812
WebView_XYFocusLeft: XamlPropertyIndex = 1813
WebView_XYFocusRight: XamlPropertyIndex = 1814
WebView_XYFocusUp: XamlPropertyIndex = 1815
CommandBarTemplateSettings_EffectiveOverflowButtonVisibility: XamlPropertyIndex = 1816
AppBarSeparator_IsInOverflow: XamlPropertyIndex = 1817
CommandBar_DefaultLabelPosition: XamlPropertyIndex = 1818
CommandBar_IsDynamicOverflowEnabled: XamlPropertyIndex = 1819
CommandBar_OverflowButtonVisibility: XamlPropertyIndex = 1820
AppBarButton_IsInOverflow: XamlPropertyIndex = 1821
AppBarButton_LabelPosition: XamlPropertyIndex = 1822
AppBarToggleButton_IsInOverflow: XamlPropertyIndex = 1823
AppBarToggleButton_LabelPosition: XamlPropertyIndex = 1824
FlyoutBase_LightDismissOverlayMode: XamlPropertyIndex = 1825
Popup_LightDismissOverlayMode: XamlPropertyIndex = 1827
CalendarDatePicker_LightDismissOverlayMode: XamlPropertyIndex = 1829
DatePicker_LightDismissOverlayMode: XamlPropertyIndex = 1830
SplitView_LightDismissOverlayMode: XamlPropertyIndex = 1831
TimePicker_LightDismissOverlayMode: XamlPropertyIndex = 1832
AppBar_LightDismissOverlayMode: XamlPropertyIndex = 1833
AutoSuggestBox_LightDismissOverlayMode: XamlPropertyIndex = 1834
ComboBox_LightDismissOverlayMode: XamlPropertyIndex = 1835
AppBarSeparator_DynamicOverflowOrder: XamlPropertyIndex = 1836
AppBarButton_DynamicOverflowOrder: XamlPropertyIndex = 1837
AppBarToggleButton_DynamicOverflowOrder: XamlPropertyIndex = 1838
FrameworkElement_FocusVisualMargin: XamlPropertyIndex = 1839
FrameworkElement_FocusVisualPrimaryBrush: XamlPropertyIndex = 1840
FrameworkElement_FocusVisualPrimaryThickness: XamlPropertyIndex = 1841
FrameworkElement_FocusVisualSecondaryBrush: XamlPropertyIndex = 1842
FrameworkElement_FocusVisualSecondaryThickness: XamlPropertyIndex = 1843
FlyoutBase_AllowFocusWhenDisabled: XamlPropertyIndex = 1846
FrameworkElement_AllowFocusWhenDisabled: XamlPropertyIndex = 1847
ComboBox_IsTextSearchEnabled: XamlPropertyIndex = 1848
TextElement_ExitDisplayModeOnAccessKeyInvoked: XamlPropertyIndex = 1849
UIElement_ExitDisplayModeOnAccessKeyInvoked: XamlPropertyIndex = 1850
MediaPlayerPresenter_IsFullWindow: XamlPropertyIndex = 1851
MediaPlayerPresenter_MediaPlayer: XamlPropertyIndex = 1852
MediaPlayerPresenter_Stretch: XamlPropertyIndex = 1853
MediaPlayerElement_AreTransportControlsEnabled: XamlPropertyIndex = 1854
MediaPlayerElement_AutoPlay: XamlPropertyIndex = 1855
MediaPlayerElement_IsFullWindow: XamlPropertyIndex = 1856
MediaPlayerElement_MediaPlayer: XamlPropertyIndex = 1857
MediaPlayerElement_PosterSource: XamlPropertyIndex = 1858
MediaPlayerElement_Source: XamlPropertyIndex = 1859
MediaPlayerElement_Stretch: XamlPropertyIndex = 1860
MediaPlayerElement_TransportControls: XamlPropertyIndex = 1861
MediaTransportControls_FastPlayFallbackBehaviour: XamlPropertyIndex = 1862
MediaTransportControls_IsNextTrackButtonVisible: XamlPropertyIndex = 1863
MediaTransportControls_IsPreviousTrackButtonVisible: XamlPropertyIndex = 1864
MediaTransportControls_IsSkipBackwardButtonVisible: XamlPropertyIndex = 1865
MediaTransportControls_IsSkipBackwardEnabled: XamlPropertyIndex = 1866
MediaTransportControls_IsSkipForwardButtonVisible: XamlPropertyIndex = 1867
MediaTransportControls_IsSkipForwardEnabled: XamlPropertyIndex = 1868
FlyoutBase_ElementSoundMode: XamlPropertyIndex = 1869
Control_ElementSoundMode: XamlPropertyIndex = 1870
Hyperlink_ElementSoundMode: XamlPropertyIndex = 1871
AutomationProperties_FlowsFrom: XamlPropertyIndex = 1876
AutomationProperties_FlowsTo: XamlPropertyIndex = 1877
TextElement_TextDecorations: XamlPropertyIndex = 1879
RichTextBlock_TextDecorations: XamlPropertyIndex = 1881
Control_DefaultStyleResourceUri: XamlPropertyIndex = 1882
ContentDialog_PrimaryButtonStyle: XamlPropertyIndex = 1884
ContentDialog_SecondaryButtonStyle: XamlPropertyIndex = 1885
TextElement_KeyTipHorizontalOffset: XamlPropertyIndex = 1890
TextElement_KeyTipPlacementMode: XamlPropertyIndex = 1891
TextElement_KeyTipVerticalOffset: XamlPropertyIndex = 1892
UIElement_KeyTipHorizontalOffset: XamlPropertyIndex = 1893
UIElement_KeyTipPlacementMode: XamlPropertyIndex = 1894
UIElement_KeyTipVerticalOffset: XamlPropertyIndex = 1895
FlyoutBase_OverlayInputPassThroughElement: XamlPropertyIndex = 1896
UIElement_XYFocusKeyboardNavigation: XamlPropertyIndex = 1897
AutomationProperties_Culture: XamlPropertyIndex = 1898
UIElement_XYFocusDownNavigationStrategy: XamlPropertyIndex = 1918
UIElement_XYFocusLeftNavigationStrategy: XamlPropertyIndex = 1919
UIElement_XYFocusRightNavigationStrategy: XamlPropertyIndex = 1920
UIElement_XYFocusUpNavigationStrategy: XamlPropertyIndex = 1921
Hyperlink_XYFocusDownNavigationStrategy: XamlPropertyIndex = 1922
Hyperlink_XYFocusLeftNavigationStrategy: XamlPropertyIndex = 1923
Hyperlink_XYFocusRightNavigationStrategy: XamlPropertyIndex = 1924
Hyperlink_XYFocusUpNavigationStrategy: XamlPropertyIndex = 1925
TextElement_AccessKeyScopeOwner: XamlPropertyIndex = 1926
TextElement_IsAccessKeyScope: XamlPropertyIndex = 1927
Hyperlink_FocusState: XamlPropertyIndex = 1934
ContentDialog_CloseButtonCommand: XamlPropertyIndex = 1936
ContentDialog_CloseButtonCommandParameter: XamlPropertyIndex = 1937
ContentDialog_CloseButtonStyle: XamlPropertyIndex = 1938
ContentDialog_CloseButtonText: XamlPropertyIndex = 1939
ContentDialog_DefaultButton: XamlPropertyIndex = 1940
RichEditBox_SelectionHighlightColorWhenNotFocused: XamlPropertyIndex = 1941
TextBox_SelectionHighlightColorWhenNotFocused: XamlPropertyIndex = 1942
SvgImageSource_RasterizePixelHeight: XamlPropertyIndex = 1948
SvgImageSource_RasterizePixelWidth: XamlPropertyIndex = 1949
SvgImageSource_UriSource: XamlPropertyIndex = 1950
LoadedImageSurface_DecodedPhysicalSize: XamlPropertyIndex = 1955
LoadedImageSurface_DecodedSize: XamlPropertyIndex = 1956
LoadedImageSurface_NaturalSize: XamlPropertyIndex = 1957
ComboBox_SelectionChangedTrigger: XamlPropertyIndex = 1958
XamlCompositionBrushBase_FallbackColor: XamlPropertyIndex = 1960
UIElement_Lights: XamlPropertyIndex = 1962
MenuFlyoutItem_Icon: XamlPropertyIndex = 1963
MenuFlyoutSubItem_Icon: XamlPropertyIndex = 1964
BitmapIcon_ShowAsMonochrome: XamlPropertyIndex = 1965
UIElement_HighContrastAdjustment: XamlPropertyIndex = 1967
RichEditBox_MaxLength: XamlPropertyIndex = 1968
UIElement_TabFocusNavigation: XamlPropertyIndex = 1969
Control_IsTemplateKeyTipTarget: XamlPropertyIndex = 1970
Hyperlink_IsTabStop: XamlPropertyIndex = 1972
Hyperlink_TabIndex: XamlPropertyIndex = 1973
MediaTransportControls_IsRepeatButtonVisible: XamlPropertyIndex = 1974
MediaTransportControls_IsRepeatEnabled: XamlPropertyIndex = 1975
MediaTransportControls_ShowAndHideAutomatically: XamlPropertyIndex = 1976
RichEditBox_DisabledFormattingAccelerators: XamlPropertyIndex = 1977
RichEditBox_CharacterCasing: XamlPropertyIndex = 1978
TextBox_CharacterCasing: XamlPropertyIndex = 1979
RichTextBlock_IsTextTrimmed: XamlPropertyIndex = 1980
RichTextBlockOverflow_IsTextTrimmed: XamlPropertyIndex = 1981
TextBlock_IsTextTrimmed: XamlPropertyIndex = 1982
TextHighlighter_Background: XamlPropertyIndex = 1985
TextHighlighter_Foreground: XamlPropertyIndex = 1986
TextHighlighter_Ranges: XamlPropertyIndex = 1987
RichTextBlock_TextHighlighters: XamlPropertyIndex = 1988
TextBlock_TextHighlighters: XamlPropertyIndex = 1989
FrameworkElement_ActualTheme: XamlPropertyIndex = 1992
Grid_ColumnSpacing: XamlPropertyIndex = 1993
Grid_RowSpacing: XamlPropertyIndex = 1994
StackPanel_Spacing: XamlPropertyIndex = 1995
Block_HorizontalTextAlignment: XamlPropertyIndex = 1996
RichTextBlock_HorizontalTextAlignment: XamlPropertyIndex = 1997
TextBlock_HorizontalTextAlignment: XamlPropertyIndex = 1998
RichEditBox_HorizontalTextAlignment: XamlPropertyIndex = 1999
TextBox_HorizontalTextAlignment: XamlPropertyIndex = 2000
TextBox_PlaceholderForeground: XamlPropertyIndex = 2001
ComboBox_PlaceholderForeground: XamlPropertyIndex = 2002
KeyboardAccelerator_IsEnabled: XamlPropertyIndex = 2003
KeyboardAccelerator_Key: XamlPropertyIndex = 2004
KeyboardAccelerator_Modifiers: XamlPropertyIndex = 2005
KeyboardAccelerator_ScopeOwner: XamlPropertyIndex = 2006
UIElement_KeyboardAccelerators: XamlPropertyIndex = 2007
ListViewItemPresenter_RevealBackground: XamlPropertyIndex = 2009
ListViewItemPresenter_RevealBackgroundShowsAboveContent: XamlPropertyIndex = 2010
ListViewItemPresenter_RevealBorderBrush: XamlPropertyIndex = 2011
ListViewItemPresenter_RevealBorderThickness: XamlPropertyIndex = 2012
UIElement_KeyTipTarget: XamlPropertyIndex = 2014
AppBarButtonTemplateSettings_KeyboardAcceleratorTextMinWidth: XamlPropertyIndex = 2015
AppBarToggleButtonTemplateSettings_KeyboardAcceleratorTextMinWidth: XamlPropertyIndex = 2016
MenuFlyoutItemTemplateSettings_KeyboardAcceleratorTextMinWidth: XamlPropertyIndex = 2017
MenuFlyoutItem_TemplateSettings: XamlPropertyIndex = 2019
AppBarButton_TemplateSettings: XamlPropertyIndex = 2021
AppBarToggleButton_TemplateSettings: XamlPropertyIndex = 2023
UIElement_KeyboardAcceleratorPlacementMode: XamlPropertyIndex = 2028
MediaTransportControls_IsCompactOverlayButtonVisible: XamlPropertyIndex = 2032
MediaTransportControls_IsCompactOverlayEnabled: XamlPropertyIndex = 2033
UIElement_KeyboardAcceleratorPlacementTarget: XamlPropertyIndex = 2061
UIElement_CenterPoint: XamlPropertyIndex = 2062
UIElement_Rotation: XamlPropertyIndex = 2063
UIElement_RotationAxis: XamlPropertyIndex = 2064
UIElement_Scale: XamlPropertyIndex = 2065
UIElement_TransformMatrix: XamlPropertyIndex = 2066
UIElement_Translation: XamlPropertyIndex = 2067
TextBox_HandwritingView: XamlPropertyIndex = 2068
AutomationProperties_HeadingLevel: XamlPropertyIndex = 2069
TextBox_IsHandwritingViewEnabled: XamlPropertyIndex = 2076
RichEditBox_ContentLinkProviders: XamlPropertyIndex = 2078
RichEditBox_ContentLinkBackgroundColor: XamlPropertyIndex = 2079
RichEditBox_ContentLinkForegroundColor: XamlPropertyIndex = 2080
HandwritingView_AreCandidatesEnabled: XamlPropertyIndex = 2081
HandwritingView_IsOpen: XamlPropertyIndex = 2082
HandwritingView_PlacementTarget: XamlPropertyIndex = 2084
HandwritingView_PlacementAlignment: XamlPropertyIndex = 2085
RichEditBox_HandwritingView: XamlPropertyIndex = 2086
RichEditBox_IsHandwritingViewEnabled: XamlPropertyIndex = 2087
MenuFlyoutItem_KeyboardAcceleratorTextOverride: XamlPropertyIndex = 2090
AppBarButton_KeyboardAcceleratorTextOverride: XamlPropertyIndex = 2091
AppBarToggleButton_KeyboardAcceleratorTextOverride: XamlPropertyIndex = 2092
ContentLink_Background: XamlPropertyIndex = 2093
ContentLink_Cursor: XamlPropertyIndex = 2094
ContentLink_ElementSoundMode: XamlPropertyIndex = 2095
ContentLink_FocusState: XamlPropertyIndex = 2096
ContentLink_IsTabStop: XamlPropertyIndex = 2097
ContentLink_TabIndex: XamlPropertyIndex = 2098
ContentLink_XYFocusDown: XamlPropertyIndex = 2099
ContentLink_XYFocusDownNavigationStrategy: XamlPropertyIndex = 2100
ContentLink_XYFocusLeft: XamlPropertyIndex = 2101
ContentLink_XYFocusLeftNavigationStrategy: XamlPropertyIndex = 2102
ContentLink_XYFocusRight: XamlPropertyIndex = 2103
ContentLink_XYFocusRightNavigationStrategy: XamlPropertyIndex = 2104
ContentLink_XYFocusUp: XamlPropertyIndex = 2105
ContentLink_XYFocusUpNavigationStrategy: XamlPropertyIndex = 2106
IconSource_Foreground: XamlPropertyIndex = 2112
BitmapIconSource_ShowAsMonochrome: XamlPropertyIndex = 2113
BitmapIconSource_UriSource: XamlPropertyIndex = 2114
FontIconSource_FontFamily: XamlPropertyIndex = 2115
FontIconSource_FontSize: XamlPropertyIndex = 2116
FontIconSource_FontStyle: XamlPropertyIndex = 2117
FontIconSource_FontWeight: XamlPropertyIndex = 2118
FontIconSource_Glyph: XamlPropertyIndex = 2119
FontIconSource_IsTextScaleFactorEnabled: XamlPropertyIndex = 2120
FontIconSource_MirroredWhenRightToLeft: XamlPropertyIndex = 2121
PathIconSource_Data: XamlPropertyIndex = 2122
SymbolIconSource_Symbol: XamlPropertyIndex = 2123
UIElement_Shadow: XamlPropertyIndex = 2130
IconSourceElement_IconSource: XamlPropertyIndex = 2131
PasswordBox_CanPasteClipboardContent: XamlPropertyIndex = 2137
TextBox_CanPasteClipboardContent: XamlPropertyIndex = 2138
TextBox_CanRedo: XamlPropertyIndex = 2139
TextBox_CanUndo: XamlPropertyIndex = 2140
FlyoutBase_ShowMode: XamlPropertyIndex = 2141
FlyoutBase_Target: XamlPropertyIndex = 2142
Control_CornerRadius: XamlPropertyIndex = 2143
AutomationProperties_IsDialog: XamlPropertyIndex = 2149
AppBarElementContainer_DynamicOverflowOrder: XamlPropertyIndex = 2150
AppBarElementContainer_IsCompact: XamlPropertyIndex = 2151
AppBarElementContainer_IsInOverflow: XamlPropertyIndex = 2152
ScrollContentPresenter_CanContentRenderOutsideBounds: XamlPropertyIndex = 2157
ScrollViewer_CanContentRenderOutsideBounds: XamlPropertyIndex = 2158
RichEditBox_SelectionFlyout: XamlPropertyIndex = 2159
TextBox_SelectionFlyout: XamlPropertyIndex = 2160
Border_BackgroundSizing: XamlPropertyIndex = 2161
ContentPresenter_BackgroundSizing: XamlPropertyIndex = 2162
Control_BackgroundSizing: XamlPropertyIndex = 2163
Grid_BackgroundSizing: XamlPropertyIndex = 2164
RelativePanel_BackgroundSizing: XamlPropertyIndex = 2165
StackPanel_BackgroundSizing: XamlPropertyIndex = 2166
ScrollViewer_HorizontalAnchorRatio: XamlPropertyIndex = 2170
ScrollViewer_VerticalAnchorRatio: XamlPropertyIndex = 2171
ComboBox_Text: XamlPropertyIndex = 2208
TextBox_Description: XamlPropertyIndex = 2217
ToolTip_PlacementRect: XamlPropertyIndex = 2218
RichTextBlock_SelectionFlyout: XamlPropertyIndex = 2219
TextBlock_SelectionFlyout: XamlPropertyIndex = 2220
PasswordBox_SelectionFlyout: XamlPropertyIndex = 2221
Border_BackgroundTransition: XamlPropertyIndex = 2222
ContentPresenter_BackgroundTransition: XamlPropertyIndex = 2223
Panel_BackgroundTransition: XamlPropertyIndex = 2224
ColorPaletteResources_Accent: XamlPropertyIndex = 2227
ColorPaletteResources_AltHigh: XamlPropertyIndex = 2228
ColorPaletteResources_AltLow: XamlPropertyIndex = 2229
ColorPaletteResources_AltMedium: XamlPropertyIndex = 2230
ColorPaletteResources_AltMediumHigh: XamlPropertyIndex = 2231
ColorPaletteResources_AltMediumLow: XamlPropertyIndex = 2232
ColorPaletteResources_BaseHigh: XamlPropertyIndex = 2233
ColorPaletteResources_BaseLow: XamlPropertyIndex = 2234
ColorPaletteResources_BaseMedium: XamlPropertyIndex = 2235
ColorPaletteResources_BaseMediumHigh: XamlPropertyIndex = 2236
ColorPaletteResources_BaseMediumLow: XamlPropertyIndex = 2237
ColorPaletteResources_ChromeAltLow: XamlPropertyIndex = 2238
ColorPaletteResources_ChromeBlackHigh: XamlPropertyIndex = 2239
ColorPaletteResources_ChromeBlackLow: XamlPropertyIndex = 2240
ColorPaletteResources_ChromeBlackMedium: XamlPropertyIndex = 2241
ColorPaletteResources_ChromeBlackMediumLow: XamlPropertyIndex = 2242
ColorPaletteResources_ChromeDisabledHigh: XamlPropertyIndex = 2243
ColorPaletteResources_ChromeDisabledLow: XamlPropertyIndex = 2244
ColorPaletteResources_ChromeGray: XamlPropertyIndex = 2245
ColorPaletteResources_ChromeHigh: XamlPropertyIndex = 2246
ColorPaletteResources_ChromeLow: XamlPropertyIndex = 2247
ColorPaletteResources_ChromeMedium: XamlPropertyIndex = 2248
ColorPaletteResources_ChromeMediumLow: XamlPropertyIndex = 2249
ColorPaletteResources_ChromeWhite: XamlPropertyIndex = 2250
ColorPaletteResources_ErrorText: XamlPropertyIndex = 2252
ColorPaletteResources_ListLow: XamlPropertyIndex = 2253
ColorPaletteResources_ListMedium: XamlPropertyIndex = 2254
UIElement_TranslationTransition: XamlPropertyIndex = 2255
UIElement_OpacityTransition: XamlPropertyIndex = 2256
UIElement_RotationTransition: XamlPropertyIndex = 2257
UIElement_ScaleTransition: XamlPropertyIndex = 2258
BrushTransition_Duration: XamlPropertyIndex = 2261
ScalarTransition_Duration: XamlPropertyIndex = 2262
Vector3Transition_Duration: XamlPropertyIndex = 2263
Vector3Transition_Components: XamlPropertyIndex = 2266
FlyoutBase_IsOpen: XamlPropertyIndex = 2267
StandardUICommand_Kind: XamlPropertyIndex = 2275
UIElement_CanBeScrollAnchor: XamlPropertyIndex = 2276
ThemeShadow_Receivers: XamlPropertyIndex = 2279
ScrollContentPresenter_SizesContentToTemplatedParent: XamlPropertyIndex = 2280
ComboBox_TextBoxStyle: XamlPropertyIndex = 2281
Frame_IsNavigationStackEnabled: XamlPropertyIndex = 2282
RichEditBox_ProofingMenuFlyout: XamlPropertyIndex = 2283
TextBox_ProofingMenuFlyout: XamlPropertyIndex = 2284
ScrollViewer_ReduceViewportForCoreInputViewOcclusions: XamlPropertyIndex = 2295
FlyoutBase_AreOpenCloseAnimationsEnabled: XamlPropertyIndex = 2296
FlyoutBase_InputDevicePrefersPrimaryCommands: XamlPropertyIndex = 2297
CalendarDatePicker_Description: XamlPropertyIndex = 2300
PasswordBox_Description: XamlPropertyIndex = 2308
RichEditBox_Description: XamlPropertyIndex = 2316
AutoSuggestBox_Description: XamlPropertyIndex = 2331
ComboBox_Description: XamlPropertyIndex = 2339
XamlUICommand_AccessKey: XamlPropertyIndex = 2347
XamlUICommand_Command: XamlPropertyIndex = 2348
XamlUICommand_Description: XamlPropertyIndex = 2349
XamlUICommand_IconSource: XamlPropertyIndex = 2350
XamlUICommand_KeyboardAccelerators: XamlPropertyIndex = 2351
XamlUICommand_Label: XamlPropertyIndex = 2352
DatePicker_SelectedDate: XamlPropertyIndex = 2355
TimePicker_SelectedTime: XamlPropertyIndex = 2356
AppBarTemplateSettings_NegativeCompactVerticalDelta: XamlPropertyIndex = 2367
AppBarTemplateSettings_NegativeHiddenVerticalDelta: XamlPropertyIndex = 2368
AppBarTemplateSettings_NegativeMinimalVerticalDelta: XamlPropertyIndex = 2369
FlyoutBase_ShouldConstrainToRootBounds: XamlPropertyIndex = 2378
Popup_ShouldConstrainToRootBounds: XamlPropertyIndex = 2379
FlyoutPresenter_IsDefaultShadowEnabled: XamlPropertyIndex = 2380
MenuFlyoutPresenter_IsDefaultShadowEnabled: XamlPropertyIndex = 2381
UIElement_ActualOffset: XamlPropertyIndex = 2382
UIElement_ActualSize: XamlPropertyIndex = 2383
CommandBarTemplateSettings_OverflowContentCompactYTranslation: XamlPropertyIndex = 2384
CommandBarTemplateSettings_OverflowContentHiddenYTranslation: XamlPropertyIndex = 2385
CommandBarTemplateSettings_OverflowContentMinimalYTranslation: XamlPropertyIndex = 2386
HandwritingView_IsCommandBarOpen: XamlPropertyIndex = 2395
HandwritingView_IsSwitchToKeyboardEnabled: XamlPropertyIndex = 2396
ListViewItemPresenter_SelectionIndicatorVisualEnabled: XamlPropertyIndex = 2399
ListViewItemPresenter_SelectionIndicatorBrush: XamlPropertyIndex = 2400
ListViewItemPresenter_SelectionIndicatorMode: XamlPropertyIndex = 2401
ListViewItemPresenter_SelectionIndicatorPointerOverBrush: XamlPropertyIndex = 2402
ListViewItemPresenter_SelectionIndicatorPressedBrush: XamlPropertyIndex = 2403
ListViewItemPresenter_SelectedBorderBrush: XamlPropertyIndex = 2410
ListViewItemPresenter_SelectedInnerBorderBrush: XamlPropertyIndex = 2411
ListViewItemPresenter_CheckBoxCornerRadius: XamlPropertyIndex = 2412
ListViewItemPresenter_SelectionIndicatorCornerRadius: XamlPropertyIndex = 2413
ListViewItemPresenter_SelectedDisabledBorderBrush: XamlPropertyIndex = 2414
ListViewItemPresenter_SelectedPressedBorderBrush: XamlPropertyIndex = 2415
ListViewItemPresenter_SelectedDisabledBackground: XamlPropertyIndex = 2416
ListViewItemPresenter_PointerOverBorderBrush: XamlPropertyIndex = 2417
ListViewItemPresenter_CheckBoxPointerOverBrush: XamlPropertyIndex = 2418
ListViewItemPresenter_CheckBoxPressedBrush: XamlPropertyIndex = 2419
ListViewItemPresenter_CheckDisabledBrush: XamlPropertyIndex = 2420
ListViewItemPresenter_CheckPressedBrush: XamlPropertyIndex = 2421
ListViewItemPresenter_CheckBoxBorderBrush: XamlPropertyIndex = 2422
ListViewItemPresenter_CheckBoxDisabledBorderBrush: XamlPropertyIndex = 2423
ListViewItemPresenter_CheckBoxPressedBorderBrush: XamlPropertyIndex = 2424
ListViewItemPresenter_CheckBoxDisabledBrush: XamlPropertyIndex = 2425
ListViewItemPresenter_CheckBoxSelectedBrush: XamlPropertyIndex = 2426
ListViewItemPresenter_CheckBoxSelectedDisabledBrush: XamlPropertyIndex = 2427
ListViewItemPresenter_CheckBoxSelectedPointerOverBrush: XamlPropertyIndex = 2428
ListViewItemPresenter_CheckBoxSelectedPressedBrush: XamlPropertyIndex = 2429
ListViewItemPresenter_CheckBoxPointerOverBorderBrush: XamlPropertyIndex = 2430
ListViewItemPresenter_SelectionIndicatorDisabledBrush: XamlPropertyIndex = 2431
CalendarView_BlackoutBackground: XamlPropertyIndex = 2432
CalendarView_BlackoutStrikethroughBrush: XamlPropertyIndex = 2433
CalendarView_CalendarItemCornerRadius: XamlPropertyIndex = 2434
CalendarView_CalendarItemDisabledBackground: XamlPropertyIndex = 2435
CalendarView_CalendarItemHoverBackground: XamlPropertyIndex = 2436
CalendarView_CalendarItemPressedBackground: XamlPropertyIndex = 2437
CalendarView_DayItemMargin: XamlPropertyIndex = 2438
CalendarView_FirstOfMonthLabelMargin: XamlPropertyIndex = 2439
CalendarView_FirstOfYearDecadeLabelMargin: XamlPropertyIndex = 2440
CalendarView_MonthYearItemMargin: XamlPropertyIndex = 2441
CalendarView_OutOfScopeHoverForeground: XamlPropertyIndex = 2442
CalendarView_OutOfScopePressedForeground: XamlPropertyIndex = 2443
CalendarView_SelectedDisabledBorderBrush: XamlPropertyIndex = 2444
CalendarView_SelectedDisabledForeground: XamlPropertyIndex = 2445
CalendarView_SelectedHoverForeground: XamlPropertyIndex = 2446
CalendarView_SelectedPressedForeground: XamlPropertyIndex = 2447
CalendarView_TodayBlackoutForeground: XamlPropertyIndex = 2448
CalendarView_TodayDisabledBackground: XamlPropertyIndex = 2449
CalendarView_TodayHoverBackground: XamlPropertyIndex = 2450
CalendarView_TodayPressedBackground: XamlPropertyIndex = 2451
Popup_ActualPlacement: XamlPropertyIndex = 2452
Popup_DesiredPlacement: XamlPropertyIndex = 2453
Popup_PlacementTarget: XamlPropertyIndex = 2454
AutomationProperties_AutomationControlType: XamlPropertyIndex = 2455
XamlTypeIndex = Int32
XamlTypeIndex_AutoSuggestBoxSuggestionChosenEventArgs: XamlTypeIndex = 34
XamlTypeIndex_AutoSuggestBoxTextChangedEventArgs: XamlTypeIndex = 35
XamlTypeIndex_CollectionViewSource: XamlTypeIndex = 41
XamlTypeIndex_ColumnDefinition: XamlTypeIndex = 44
XamlTypeIndex_GradientStop: XamlTypeIndex = 64
XamlTypeIndex_InputScope: XamlTypeIndex = 74
XamlTypeIndex_InputScopeName: XamlTypeIndex = 75
XamlTypeIndex_KeySpline: XamlTypeIndex = 78
XamlTypeIndex_PathFigure: XamlTypeIndex = 93
XamlTypeIndex_PrintDocument: XamlTypeIndex = 100
XamlTypeIndex_RowDefinition: XamlTypeIndex = 106
XamlTypeIndex_Style: XamlTypeIndex = 114
XamlTypeIndex_TimelineMarker: XamlTypeIndex = 126
XamlTypeIndex_VisualState: XamlTypeIndex = 137
XamlTypeIndex_VisualStateGroup: XamlTypeIndex = 138
XamlTypeIndex_VisualStateManager: XamlTypeIndex = 139
XamlTypeIndex_VisualTransition: XamlTypeIndex = 140
XamlTypeIndex_AddDeleteThemeTransition: XamlTypeIndex = 177
XamlTypeIndex_ArcSegment: XamlTypeIndex = 178
XamlTypeIndex_BackEase: XamlTypeIndex = 179
XamlTypeIndex_BeginStoryboard: XamlTypeIndex = 180
XamlTypeIndex_BezierSegment: XamlTypeIndex = 181
XamlTypeIndex_BindingBase: XamlTypeIndex = 182
XamlTypeIndex_BitmapCache: XamlTypeIndex = 183
XamlTypeIndex_BounceEase: XamlTypeIndex = 186
XamlTypeIndex_CircleEase: XamlTypeIndex = 187
XamlTypeIndex_ColorAnimation: XamlTypeIndex = 188
XamlTypeIndex_ColorAnimationUsingKeyFrames: XamlTypeIndex = 189
XamlTypeIndex_ContentThemeTransition: XamlTypeIndex = 190
XamlTypeIndex_ControlTemplate: XamlTypeIndex = 191
XamlTypeIndex_CubicEase: XamlTypeIndex = 192
XamlTypeIndex_DataTemplate: XamlTypeIndex = 194
XamlTypeIndex_DiscreteColorKeyFrame: XamlTypeIndex = 195
XamlTypeIndex_DiscreteDoubleKeyFrame: XamlTypeIndex = 196
XamlTypeIndex_DiscreteObjectKeyFrame: XamlTypeIndex = 197
XamlTypeIndex_DiscretePointKeyFrame: XamlTypeIndex = 198
XamlTypeIndex_DoubleAnimation: XamlTypeIndex = 200
XamlTypeIndex_DoubleAnimationUsingKeyFrames: XamlTypeIndex = 201
XamlTypeIndex_EasingColorKeyFrame: XamlTypeIndex = 204
XamlTypeIndex_EasingDoubleKeyFrame: XamlTypeIndex = 205
XamlTypeIndex_EasingPointKeyFrame: XamlTypeIndex = 206
XamlTypeIndex_EdgeUIThemeTransition: XamlTypeIndex = 207
XamlTypeIndex_ElasticEase: XamlTypeIndex = 208
XamlTypeIndex_EllipseGeometry: XamlTypeIndex = 209
XamlTypeIndex_EntranceThemeTransition: XamlTypeIndex = 210
XamlTypeIndex_EventTrigger: XamlTypeIndex = 211
XamlTypeIndex_ExponentialEase: XamlTypeIndex = 212
XamlTypeIndex_Flyout: XamlTypeIndex = 213
XamlTypeIndex_GeometryGroup: XamlTypeIndex = 216
XamlTypeIndex_ItemsPanelTemplate: XamlTypeIndex = 227
XamlTypeIndex_LinearColorKeyFrame: XamlTypeIndex = 230
XamlTypeIndex_LinearDoubleKeyFrame: XamlTypeIndex = 231
XamlTypeIndex_LinearPointKeyFrame: XamlTypeIndex = 232
XamlTypeIndex_LineGeometry: XamlTypeIndex = 233
XamlTypeIndex_LineSegment: XamlTypeIndex = 234
XamlTypeIndex_Matrix3DProjection: XamlTypeIndex = 236
XamlTypeIndex_MenuFlyout: XamlTypeIndex = 238
XamlTypeIndex_ObjectAnimationUsingKeyFrames: XamlTypeIndex = 240
XamlTypeIndex_PaneThemeTransition: XamlTypeIndex = 241
XamlTypeIndex_PathGeometry: XamlTypeIndex = 243
XamlTypeIndex_PlaneProjection: XamlTypeIndex = 244
XamlTypeIndex_PointAnimation: XamlTypeIndex = 245
XamlTypeIndex_PointAnimationUsingKeyFrames: XamlTypeIndex = 246
XamlTypeIndex_PolyBezierSegment: XamlTypeIndex = 248
XamlTypeIndex_PolyLineSegment: XamlTypeIndex = 249
XamlTypeIndex_PolyQuadraticBezierSegment: XamlTypeIndex = 250
XamlTypeIndex_PopupThemeTransition: XamlTypeIndex = 251
XamlTypeIndex_PowerEase: XamlTypeIndex = 252
XamlTypeIndex_QuadraticBezierSegment: XamlTypeIndex = 254
XamlTypeIndex_QuadraticEase: XamlTypeIndex = 255
XamlTypeIndex_QuarticEase: XamlTypeIndex = 256
XamlTypeIndex_QuinticEase: XamlTypeIndex = 257
XamlTypeIndex_RectangleGeometry: XamlTypeIndex = 258
XamlTypeIndex_RelativeSource: XamlTypeIndex = 259
XamlTypeIndex_RenderTargetBitmap: XamlTypeIndex = 260
XamlTypeIndex_ReorderThemeTransition: XamlTypeIndex = 261
XamlTypeIndex_RepositionThemeTransition: XamlTypeIndex = 262
XamlTypeIndex_Setter: XamlTypeIndex = 263
XamlTypeIndex_SineEase: XamlTypeIndex = 264
XamlTypeIndex_SolidColorBrush: XamlTypeIndex = 265
XamlTypeIndex_SplineColorKeyFrame: XamlTypeIndex = 266
XamlTypeIndex_SplineDoubleKeyFrame: XamlTypeIndex = 267
XamlTypeIndex_SplinePointKeyFrame: XamlTypeIndex = 268
XamlTypeIndex_BitmapImage: XamlTypeIndex = 285
XamlTypeIndex_Border: XamlTypeIndex = 286
XamlTypeIndex_CaptureElement: XamlTypeIndex = 288
XamlTypeIndex_CompositeTransform: XamlTypeIndex = 295
XamlTypeIndex_ContentPresenter: XamlTypeIndex = 296
XamlTypeIndex_DragItemThemeAnimation: XamlTypeIndex = 302
XamlTypeIndex_DragOverThemeAnimation: XamlTypeIndex = 303
XamlTypeIndex_DropTargetItemThemeAnimation: XamlTypeIndex = 304
XamlTypeIndex_FadeInThemeAnimation: XamlTypeIndex = 306
XamlTypeIndex_FadeOutThemeAnimation: XamlTypeIndex = 307
XamlTypeIndex_Glyphs: XamlTypeIndex = 312
XamlTypeIndex_Image: XamlTypeIndex = 326
XamlTypeIndex_ImageBrush: XamlTypeIndex = 328
XamlTypeIndex_InlineUIContainer: XamlTypeIndex = 329
XamlTypeIndex_ItemsPresenter: XamlTypeIndex = 332
XamlTypeIndex_LinearGradientBrush: XamlTypeIndex = 334
XamlTypeIndex_LineBreak: XamlTypeIndex = 335
XamlTypeIndex_MatrixTransform: XamlTypeIndex = 340
XamlTypeIndex_MediaElement: XamlTypeIndex = 342
XamlTypeIndex_Paragraph: XamlTypeIndex = 349
XamlTypeIndex_PointerDownThemeAnimation: XamlTypeIndex = 357
XamlTypeIndex_PointerUpThemeAnimation: XamlTypeIndex = 359
XamlTypeIndex_PopInThemeAnimation: XamlTypeIndex = 361
XamlTypeIndex_PopOutThemeAnimation: XamlTypeIndex = 362
XamlTypeIndex_Popup: XamlTypeIndex = 363
XamlTypeIndex_RepositionThemeAnimation: XamlTypeIndex = 370
XamlTypeIndex_ResourceDictionary: XamlTypeIndex = 371
XamlTypeIndex_RichTextBlock: XamlTypeIndex = 374
XamlTypeIndex_RichTextBlockOverflow: XamlTypeIndex = 376
XamlTypeIndex_RotateTransform: XamlTypeIndex = 378
XamlTypeIndex_Run: XamlTypeIndex = 380
XamlTypeIndex_ScaleTransform: XamlTypeIndex = 381
XamlTypeIndex_SkewTransform: XamlTypeIndex = 389
XamlTypeIndex_Span: XamlTypeIndex = 390
XamlTypeIndex_SplitCloseThemeAnimation: XamlTypeIndex = 391
XamlTypeIndex_SplitOpenThemeAnimation: XamlTypeIndex = 392
XamlTypeIndex_Storyboard: XamlTypeIndex = 393
XamlTypeIndex_SwipeBackThemeAnimation: XamlTypeIndex = 394
XamlTypeIndex_SwipeHintThemeAnimation: XamlTypeIndex = 395
XamlTypeIndex_TextBlock: XamlTypeIndex = 396
XamlTypeIndex_TransformGroup: XamlTypeIndex = 411
XamlTypeIndex_TranslateTransform: XamlTypeIndex = 413
XamlTypeIndex_Viewbox: XamlTypeIndex = 417
XamlTypeIndex_WebViewBrush: XamlTypeIndex = 423
XamlTypeIndex_AppBarSeparator: XamlTypeIndex = 427
XamlTypeIndex_BitmapIcon: XamlTypeIndex = 429
XamlTypeIndex_Bold: XamlTypeIndex = 430
XamlTypeIndex_Canvas: XamlTypeIndex = 432
XamlTypeIndex_ContentControl: XamlTypeIndex = 435
XamlTypeIndex_DatePicker: XamlTypeIndex = 436
XamlTypeIndex_DependencyObjectCollection: XamlTypeIndex = 437
XamlTypeIndex_Ellipse: XamlTypeIndex = 438
XamlTypeIndex_FontIcon: XamlTypeIndex = 440
XamlTypeIndex_Grid: XamlTypeIndex = 442
XamlTypeIndex_Hub: XamlTypeIndex = 445
XamlTypeIndex_HubSection: XamlTypeIndex = 446
XamlTypeIndex_Hyperlink: XamlTypeIndex = 447
XamlTypeIndex_Italic: XamlTypeIndex = 449
XamlTypeIndex_ItemsControl: XamlTypeIndex = 451
XamlTypeIndex_Line: XamlTypeIndex = 452
XamlTypeIndex_MediaTransportControls: XamlTypeIndex = 458
XamlTypeIndex_PasswordBox: XamlTypeIndex = 462
XamlTypeIndex_Path: XamlTypeIndex = 463
XamlTypeIndex_PathIcon: XamlTypeIndex = 464
XamlTypeIndex_Polygon: XamlTypeIndex = 465
XamlTypeIndex_Polyline: XamlTypeIndex = 466
XamlTypeIndex_ProgressRing: XamlTypeIndex = 468
XamlTypeIndex_Rectangle: XamlTypeIndex = 470
XamlTypeIndex_RichEditBox: XamlTypeIndex = 473
XamlTypeIndex_ScrollContentPresenter: XamlTypeIndex = 476
XamlTypeIndex_SearchBox: XamlTypeIndex = 477
XamlTypeIndex_SemanticZoom: XamlTypeIndex = 479
XamlTypeIndex_StackPanel: XamlTypeIndex = 481
XamlTypeIndex_SymbolIcon: XamlTypeIndex = 482
XamlTypeIndex_TextBox: XamlTypeIndex = 483
XamlTypeIndex_Thumb: XamlTypeIndex = 485
XamlTypeIndex_TickBar: XamlTypeIndex = 486
XamlTypeIndex_TimePicker: XamlTypeIndex = 487
XamlTypeIndex_ToggleSwitch: XamlTypeIndex = 489
XamlTypeIndex_Underline: XamlTypeIndex = 490
XamlTypeIndex_UserControl: XamlTypeIndex = 491
XamlTypeIndex_VariableSizedWrapGrid: XamlTypeIndex = 492
XamlTypeIndex_WebView: XamlTypeIndex = 494
XamlTypeIndex_AppBar: XamlTypeIndex = 495
XamlTypeIndex_AutoSuggestBox: XamlTypeIndex = 499
XamlTypeIndex_CarouselPanel: XamlTypeIndex = 502
XamlTypeIndex_ContentDialog: XamlTypeIndex = 506
XamlTypeIndex_FlyoutPresenter: XamlTypeIndex = 508
XamlTypeIndex_Frame: XamlTypeIndex = 509
XamlTypeIndex_GridViewItemPresenter: XamlTypeIndex = 511
XamlTypeIndex_GroupItem: XamlTypeIndex = 512
XamlTypeIndex_ItemsStackPanel: XamlTypeIndex = 514
XamlTypeIndex_ItemsWrapGrid: XamlTypeIndex = 515
XamlTypeIndex_ListViewItemPresenter: XamlTypeIndex = 520
XamlTypeIndex_MenuFlyoutItem: XamlTypeIndex = 521
XamlTypeIndex_MenuFlyoutPresenter: XamlTypeIndex = 522
XamlTypeIndex_MenuFlyoutSeparator: XamlTypeIndex = 523
XamlTypeIndex_Page: XamlTypeIndex = 525
XamlTypeIndex_ProgressBar: XamlTypeIndex = 528
XamlTypeIndex_ScrollBar: XamlTypeIndex = 530
XamlTypeIndex_SettingsFlyout: XamlTypeIndex = 533
XamlTypeIndex_Slider: XamlTypeIndex = 534
XamlTypeIndex_SwapChainBackgroundPanel: XamlTypeIndex = 535
XamlTypeIndex_SwapChainPanel: XamlTypeIndex = 536
XamlTypeIndex_ToolTip: XamlTypeIndex = 538
XamlTypeIndex_Button: XamlTypeIndex = 540
XamlTypeIndex_ComboBoxItem: XamlTypeIndex = 541
XamlTypeIndex_CommandBar: XamlTypeIndex = 542
XamlTypeIndex_FlipViewItem: XamlTypeIndex = 543
XamlTypeIndex_GridViewHeaderItem: XamlTypeIndex = 545
XamlTypeIndex_HyperlinkButton: XamlTypeIndex = 546
XamlTypeIndex_ListBoxItem: XamlTypeIndex = 547
XamlTypeIndex_ListViewHeaderItem: XamlTypeIndex = 550
XamlTypeIndex_RepeatButton: XamlTypeIndex = 551
XamlTypeIndex_ScrollViewer: XamlTypeIndex = 552
XamlTypeIndex_ToggleButton: XamlTypeIndex = 553
XamlTypeIndex_ToggleMenuFlyoutItem: XamlTypeIndex = 554
XamlTypeIndex_VirtualizingStackPanel: XamlTypeIndex = 555
XamlTypeIndex_WrapGrid: XamlTypeIndex = 556
XamlTypeIndex_AppBarButton: XamlTypeIndex = 557
XamlTypeIndex_AppBarToggleButton: XamlTypeIndex = 558
XamlTypeIndex_CheckBox: XamlTypeIndex = 559
XamlTypeIndex_GridViewItem: XamlTypeIndex = 560
XamlTypeIndex_ListViewItem: XamlTypeIndex = 561
XamlTypeIndex_RadioButton: XamlTypeIndex = 562
XamlTypeIndex_Binding: XamlTypeIndex = 564
XamlTypeIndex_ComboBox: XamlTypeIndex = 566
XamlTypeIndex_FlipView: XamlTypeIndex = 567
XamlTypeIndex_ListBox: XamlTypeIndex = 568
XamlTypeIndex_GridView: XamlTypeIndex = 570
XamlTypeIndex_ListView: XamlTypeIndex = 571
XamlTypeIndex_CalendarView: XamlTypeIndex = 707
XamlTypeIndex_CalendarViewDayItem: XamlTypeIndex = 709
XamlTypeIndex_CalendarPanel: XamlTypeIndex = 723
XamlTypeIndex_SplitView: XamlTypeIndex = 728
XamlTypeIndex_CompositeTransform3D: XamlTypeIndex = 732
XamlTypeIndex_PerspectiveTransform3D: XamlTypeIndex = 733
XamlTypeIndex_RelativePanel: XamlTypeIndex = 744
XamlTypeIndex_InkCanvas: XamlTypeIndex = 748
XamlTypeIndex_MenuFlyoutSubItem: XamlTypeIndex = 749
XamlTypeIndex_AdaptiveTrigger: XamlTypeIndex = 757
XamlTypeIndex_SoftwareBitmapSource: XamlTypeIndex = 761
XamlTypeIndex_StateTrigger: XamlTypeIndex = 767
XamlTypeIndex_CalendarDatePicker: XamlTypeIndex = 774
XamlTypeIndex_AutoSuggestBoxQuerySubmittedEventArgs: XamlTypeIndex = 778
XamlTypeIndex_CommandBarOverflowPresenter: XamlTypeIndex = 781
XamlTypeIndex_DrillInThemeAnimation: XamlTypeIndex = 782
XamlTypeIndex_DrillOutThemeAnimation: XamlTypeIndex = 783
XamlTypeIndex_AutomationAnnotation: XamlTypeIndex = 789
XamlTypeIndex_AutomationPeerAnnotation: XamlTypeIndex = 790
XamlTypeIndex_MediaPlayerPresenter: XamlTypeIndex = 828
XamlTypeIndex_MediaPlayerElement: XamlTypeIndex = 829
XamlTypeIndex_XamlLight: XamlTypeIndex = 855
XamlTypeIndex_SvgImageSource: XamlTypeIndex = 860
XamlTypeIndex_KeyboardAccelerator: XamlTypeIndex = 897
XamlTypeIndex_HandwritingView: XamlTypeIndex = 920
XamlTypeIndex_ContentLink: XamlTypeIndex = 925
XamlTypeIndex_BitmapIconSource: XamlTypeIndex = 929
XamlTypeIndex_FontIconSource: XamlTypeIndex = 930
XamlTypeIndex_PathIconSource: XamlTypeIndex = 931
XamlTypeIndex_SymbolIconSource: XamlTypeIndex = 933
XamlTypeIndex_IconSourceElement: XamlTypeIndex = 939
XamlTypeIndex_AppBarElementContainer: XamlTypeIndex = 945
XamlTypeIndex_ColorPaletteResources: XamlTypeIndex = 952
XamlTypeIndex_StandardUICommand: XamlTypeIndex = 961
XamlTypeIndex_ThemeShadow: XamlTypeIndex = 964
XamlTypeIndex_XamlUICommand: XamlTypeIndex = 969


make_ready(__name__)
