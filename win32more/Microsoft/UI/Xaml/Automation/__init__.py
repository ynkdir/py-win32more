from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
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
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, EasyCastStructure, EasyCastUnion, ComPtr, make_ready
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Microsoft.UI.Xaml
import win32more.Microsoft.UI.Xaml.Automation
import win32more.Microsoft.UI.Xaml.Automation.Peers
import win32more.Windows.Foundation.Collections
class _AnnotationPatternIdentifiers_Meta_(ComPtr.__class__):
    pass
class AnnotationPatternIdentifiers(ComPtr, metaclass=_AnnotationPatternIdentifiers_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Automation.IAnnotationPatternIdentifiers
    _classid_ = 'Microsoft.UI.Xaml.Automation.AnnotationPatternIdentifiers'
    @winrt_classmethod
    def get_AnnotationTypeIdProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAnnotationPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_AnnotationTypeNameProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAnnotationPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_AuthorProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAnnotationPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_DateTimeProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAnnotationPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_TargetProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAnnotationPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    _AnnotationPatternIdentifiers_Meta_.AnnotationTypeIdProperty = property(get_AnnotationTypeIdProperty.__wrapped__, None)
    _AnnotationPatternIdentifiers_Meta_.AnnotationTypeNameProperty = property(get_AnnotationTypeNameProperty.__wrapped__, None)
    _AnnotationPatternIdentifiers_Meta_.AuthorProperty = property(get_AuthorProperty.__wrapped__, None)
    _AnnotationPatternIdentifiers_Meta_.DateTimeProperty = property(get_DateTimeProperty.__wrapped__, None)
    _AnnotationPatternIdentifiers_Meta_.TargetProperty = property(get_TargetProperty.__wrapped__, None)
AnnotationType = Int32
AnnotationType_Unknown: AnnotationType = 60000
AnnotationType_SpellingError: AnnotationType = 60001
AnnotationType_GrammarError: AnnotationType = 60002
AnnotationType_Comment: AnnotationType = 60003
AnnotationType_FormulaError: AnnotationType = 60004
AnnotationType_TrackChanges: AnnotationType = 60005
AnnotationType_Header: AnnotationType = 60006
AnnotationType_Footer: AnnotationType = 60007
AnnotationType_Highlighted: AnnotationType = 60008
AnnotationType_Endnote: AnnotationType = 60009
AnnotationType_Footnote: AnnotationType = 60010
AnnotationType_InsertionChange: AnnotationType = 60011
AnnotationType_DeletionChange: AnnotationType = 60012
AnnotationType_MoveChange: AnnotationType = 60013
AnnotationType_FormatChange: AnnotationType = 60014
AnnotationType_UnsyncedChange: AnnotationType = 60015
AnnotationType_EditingLockedChange: AnnotationType = 60016
AnnotationType_ExternalChange: AnnotationType = 60017
AnnotationType_ConflictingChange: AnnotationType = 60018
AnnotationType_Author: AnnotationType = 60019
AnnotationType_AdvancedProofingIssue: AnnotationType = 60020
AnnotationType_DataValidationError: AnnotationType = 60021
AnnotationType_CircularReferenceError: AnnotationType = 60022
AutomationActiveEnd = Int32
AutomationActiveEnd_None: AutomationActiveEnd = 0
AutomationActiveEnd_Start: AutomationActiveEnd = 1
AutomationActiveEnd_End: AutomationActiveEnd = 2
AutomationAnimationStyle = Int32
AutomationAnimationStyle_None: AutomationAnimationStyle = 0
AutomationAnimationStyle_LasVegasLights: AutomationAnimationStyle = 1
AutomationAnimationStyle_BlinkingBackground: AutomationAnimationStyle = 2
AutomationAnimationStyle_SparkleText: AutomationAnimationStyle = 3
AutomationAnimationStyle_MarchingBlackAnts: AutomationAnimationStyle = 4
AutomationAnimationStyle_MarchingRedAnts: AutomationAnimationStyle = 5
AutomationAnimationStyle_Shimmer: AutomationAnimationStyle = 6
AutomationAnimationStyle_Other: AutomationAnimationStyle = 7
class _AutomationAnnotation_Meta_(ComPtr.__class__):
    pass
class AutomationAnnotation(ComPtr, metaclass=_AutomationAnnotation_Meta_):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Automation.IAutomationAnnotation
    _classid_ = 'Microsoft.UI.Xaml.Automation.AutomationAnnotation'
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationAnnotationFactory, type: win32more.Microsoft.UI.Xaml.Automation.AnnotationType) -> win32more.Microsoft.UI.Xaml.Automation.AutomationAnnotation: ...
    @winrt_factorymethod
    def CreateWithElementParameter(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationAnnotationFactory, type: win32more.Microsoft.UI.Xaml.Automation.AnnotationType, element: win32more.Microsoft.UI.Xaml.UIElement) -> win32more.Microsoft.UI.Xaml.Automation.AutomationAnnotation: ...
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Automation.AutomationAnnotation: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Microsoft.UI.Xaml.Automation.IAutomationAnnotation) -> win32more.Microsoft.UI.Xaml.Automation.AnnotationType: ...
    @winrt_mixinmethod
    def put_Type(self: win32more.Microsoft.UI.Xaml.Automation.IAutomationAnnotation, value: win32more.Microsoft.UI.Xaml.Automation.AnnotationType) -> Void: ...
    @winrt_mixinmethod
    def get_Element(self: win32more.Microsoft.UI.Xaml.Automation.IAutomationAnnotation) -> win32more.Microsoft.UI.Xaml.UIElement: ...
    @winrt_mixinmethod
    def put_Element(self: win32more.Microsoft.UI.Xaml.Automation.IAutomationAnnotation, value: win32more.Microsoft.UI.Xaml.UIElement) -> Void: ...
    @winrt_classmethod
    def get_TypeProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationAnnotationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ElementProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationAnnotationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    Type = property(get_Type, put_Type)
    Element = property(get_Element, put_Element)
    _AutomationAnnotation_Meta_.TypeProperty = property(get_TypeProperty.__wrapped__, None)
    _AutomationAnnotation_Meta_.ElementProperty = property(get_ElementProperty.__wrapped__, None)
AutomationBulletStyle = Int32
AutomationBulletStyle_None: AutomationBulletStyle = 0
AutomationBulletStyle_HollowRoundBullet: AutomationBulletStyle = 1
AutomationBulletStyle_FilledRoundBullet: AutomationBulletStyle = 2
AutomationBulletStyle_HollowSquareBullet: AutomationBulletStyle = 3
AutomationBulletStyle_FilledSquareBullet: AutomationBulletStyle = 4
AutomationBulletStyle_DashBullet: AutomationBulletStyle = 5
AutomationBulletStyle_Other: AutomationBulletStyle = 6
AutomationCaretBidiMode = Int32
LTR: AutomationCaretBidiMode = 0
RTL: AutomationCaretBidiMode = 1
AutomationCaretPosition = Int32
AutomationCaretPosition_Unknown: AutomationCaretPosition = 0
AutomationCaretPosition_EndOfLine: AutomationCaretPosition = 1
AutomationCaretPosition_BeginningOfLine: AutomationCaretPosition = 2
class _AutomationElementIdentifiers_Meta_(ComPtr.__class__):
    pass
class AutomationElementIdentifiers(ComPtr, metaclass=_AutomationElementIdentifiers_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Automation.IAutomationElementIdentifiers
    _classid_ = 'Microsoft.UI.Xaml.Automation.AutomationElementIdentifiers'
    @winrt_classmethod
    def get_AcceleratorKeyProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_AccessKeyProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_AutomationIdProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_BoundingRectangleProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_ClassNameProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_ClickablePointProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_ControlTypeProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_HasKeyboardFocusProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_HelpTextProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_IsContentElementProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_IsControlElementProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_IsEnabledProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_IsKeyboardFocusableProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_IsOffscreenProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_IsPasswordProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_IsRequiredForFormProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_ItemStatusProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_ItemTypeProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_LabeledByProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_LocalizedControlTypeProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_NameProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_OrientationProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_LiveSettingProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_ControlledPeersProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_PositionInSetProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_SizeOfSetProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_LevelProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_AnnotationsProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_LandmarkTypeProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_LocalizedLandmarkTypeProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_IsPeripheralProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_IsDataValidForFormProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_FullDescriptionProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_DescribedByProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_FlowsToProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_FlowsFromProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_CultureProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_HeadingLevelProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_IsDialogProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    _AutomationElementIdentifiers_Meta_.AcceleratorKeyProperty = property(get_AcceleratorKeyProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.AccessKeyProperty = property(get_AccessKeyProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.AutomationIdProperty = property(get_AutomationIdProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.BoundingRectangleProperty = property(get_BoundingRectangleProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.ClassNameProperty = property(get_ClassNameProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.ClickablePointProperty = property(get_ClickablePointProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.ControlTypeProperty = property(get_ControlTypeProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.HasKeyboardFocusProperty = property(get_HasKeyboardFocusProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.HelpTextProperty = property(get_HelpTextProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.IsContentElementProperty = property(get_IsContentElementProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.IsControlElementProperty = property(get_IsControlElementProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.IsEnabledProperty = property(get_IsEnabledProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.IsKeyboardFocusableProperty = property(get_IsKeyboardFocusableProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.IsOffscreenProperty = property(get_IsOffscreenProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.IsPasswordProperty = property(get_IsPasswordProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.IsRequiredForFormProperty = property(get_IsRequiredForFormProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.ItemStatusProperty = property(get_ItemStatusProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.ItemTypeProperty = property(get_ItemTypeProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.LabeledByProperty = property(get_LabeledByProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.LocalizedControlTypeProperty = property(get_LocalizedControlTypeProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.NameProperty = property(get_NameProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.OrientationProperty = property(get_OrientationProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.LiveSettingProperty = property(get_LiveSettingProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.ControlledPeersProperty = property(get_ControlledPeersProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.PositionInSetProperty = property(get_PositionInSetProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.SizeOfSetProperty = property(get_SizeOfSetProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.LevelProperty = property(get_LevelProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.AnnotationsProperty = property(get_AnnotationsProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.LandmarkTypeProperty = property(get_LandmarkTypeProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.LocalizedLandmarkTypeProperty = property(get_LocalizedLandmarkTypeProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.IsPeripheralProperty = property(get_IsPeripheralProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.IsDataValidForFormProperty = property(get_IsDataValidForFormProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.FullDescriptionProperty = property(get_FullDescriptionProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.DescribedByProperty = property(get_DescribedByProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.FlowsToProperty = property(get_FlowsToProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.FlowsFromProperty = property(get_FlowsFromProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.CultureProperty = property(get_CultureProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.HeadingLevelProperty = property(get_HeadingLevelProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.IsDialogProperty = property(get_IsDialogProperty.__wrapped__, None)
AutomationFlowDirections = Int32
AutomationFlowDirections_Default: AutomationFlowDirections = 0
AutomationFlowDirections_RightToLeft: AutomationFlowDirections = 1
AutomationFlowDirections_BottomToTop: AutomationFlowDirections = 2
AutomationFlowDirections_Vertical: AutomationFlowDirections = 3
AutomationOutlineStyles = Int32
AutomationOutlineStyles_None: AutomationOutlineStyles = 0
AutomationOutlineStyles_Outline: AutomationOutlineStyles = 1
AutomationOutlineStyles_Shadow: AutomationOutlineStyles = 2
AutomationOutlineStyles_Engraved: AutomationOutlineStyles = 3
AutomationOutlineStyles_Embossed: AutomationOutlineStyles = 4
class _AutomationProperties_Meta_(ComPtr.__class__):
    pass
class AutomationProperties(ComPtr, metaclass=_AutomationProperties_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Automation.IAutomationProperties
    _classid_ = 'Microsoft.UI.Xaml.Automation.AutomationProperties'
    @winrt_classmethod
    def get_AutomationControlTypeProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics2) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetAutomationControlType(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics2, element: win32more.Microsoft.UI.Xaml.UIElement) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationControlType: ...
    @winrt_classmethod
    def SetAutomationControlType(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics2, element: win32more.Microsoft.UI.Xaml.UIElement, value: win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationControlType) -> Void: ...
    @winrt_classmethod
    def get_AcceleratorKeyProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetAcceleratorKey(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_classmethod
    def SetAcceleratorKey(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_AccessKeyProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetAccessKey(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_classmethod
    def SetAccessKey(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_AutomationIdProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetAutomationId(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_classmethod
    def SetAutomationId(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_HelpTextProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetHelpText(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_classmethod
    def SetHelpText(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_IsRequiredForFormProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetIsRequiredForForm(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> Boolean: ...
    @winrt_classmethod
    def SetIsRequiredForForm(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_ItemStatusProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetItemStatus(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_classmethod
    def SetItemStatus(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_ItemTypeProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetItemType(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_classmethod
    def SetItemType(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_LabeledByProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetLabeledBy(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> win32more.Microsoft.UI.Xaml.UIElement: ...
    @winrt_classmethod
    def SetLabeledBy(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: win32more.Microsoft.UI.Xaml.UIElement) -> Void: ...
    @winrt_classmethod
    def get_NameProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetName(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_classmethod
    def SetName(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_LiveSettingProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetLiveSetting(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationLiveSetting: ...
    @winrt_classmethod
    def SetLiveSetting(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationLiveSetting) -> Void: ...
    @winrt_classmethod
    def get_AccessibilityViewProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetAccessibilityView(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AccessibilityView: ...
    @winrt_classmethod
    def SetAccessibilityView(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: win32more.Microsoft.UI.Xaml.Automation.Peers.AccessibilityView) -> Void: ...
    @winrt_classmethod
    def get_ControlledPeersProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetControlledPeers(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.UIElement]: ...
    @winrt_classmethod
    def get_PositionInSetProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetPositionInSet(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> Int32: ...
    @winrt_classmethod
    def SetPositionInSet(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: Int32) -> Void: ...
    @winrt_classmethod
    def get_SizeOfSetProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetSizeOfSet(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> Int32: ...
    @winrt_classmethod
    def SetSizeOfSet(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: Int32) -> Void: ...
    @winrt_classmethod
    def get_LevelProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetLevel(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> Int32: ...
    @winrt_classmethod
    def SetLevel(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: Int32) -> Void: ...
    @winrt_classmethod
    def get_AnnotationsProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetAnnotations(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Automation.AutomationAnnotation]: ...
    @winrt_classmethod
    def get_LandmarkTypeProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetLandmarkType(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationLandmarkType: ...
    @winrt_classmethod
    def SetLandmarkType(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationLandmarkType) -> Void: ...
    @winrt_classmethod
    def get_LocalizedLandmarkTypeProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetLocalizedLandmarkType(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_classmethod
    def SetLocalizedLandmarkType(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_IsPeripheralProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetIsPeripheral(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> Boolean: ...
    @winrt_classmethod
    def SetIsPeripheral(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_IsDataValidForFormProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetIsDataValidForForm(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> Boolean: ...
    @winrt_classmethod
    def SetIsDataValidForForm(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_FullDescriptionProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetFullDescription(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_classmethod
    def SetFullDescription(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_LocalizedControlTypeProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetLocalizedControlType(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_classmethod
    def SetLocalizedControlType(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_DescribedByProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetDescribedBy(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.DependencyObject]: ...
    @winrt_classmethod
    def get_FlowsToProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetFlowsTo(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.DependencyObject]: ...
    @winrt_classmethod
    def get_FlowsFromProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetFlowsFrom(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.DependencyObject]: ...
    @winrt_classmethod
    def get_CultureProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetCulture(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> Int32: ...
    @winrt_classmethod
    def SetCulture(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: Int32) -> Void: ...
    @winrt_classmethod
    def get_HeadingLevelProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetHeadingLevel(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationHeadingLevel: ...
    @winrt_classmethod
    def SetHeadingLevel(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationHeadingLevel) -> Void: ...
    @winrt_classmethod
    def get_IsDialogProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetIsDialog(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> Boolean: ...
    @winrt_classmethod
    def SetIsDialog(cls: win32more.Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: Boolean) -> Void: ...
    _AutomationProperties_Meta_.AutomationControlTypeProperty = property(get_AutomationControlTypeProperty.__wrapped__, None)
    _AutomationProperties_Meta_.AcceleratorKeyProperty = property(get_AcceleratorKeyProperty.__wrapped__, None)
    _AutomationProperties_Meta_.AccessKeyProperty = property(get_AccessKeyProperty.__wrapped__, None)
    _AutomationProperties_Meta_.AutomationIdProperty = property(get_AutomationIdProperty.__wrapped__, None)
    _AutomationProperties_Meta_.HelpTextProperty = property(get_HelpTextProperty.__wrapped__, None)
    _AutomationProperties_Meta_.IsRequiredForFormProperty = property(get_IsRequiredForFormProperty.__wrapped__, None)
    _AutomationProperties_Meta_.ItemStatusProperty = property(get_ItemStatusProperty.__wrapped__, None)
    _AutomationProperties_Meta_.ItemTypeProperty = property(get_ItemTypeProperty.__wrapped__, None)
    _AutomationProperties_Meta_.LabeledByProperty = property(get_LabeledByProperty.__wrapped__, None)
    _AutomationProperties_Meta_.NameProperty = property(get_NameProperty.__wrapped__, None)
    _AutomationProperties_Meta_.LiveSettingProperty = property(get_LiveSettingProperty.__wrapped__, None)
    _AutomationProperties_Meta_.AccessibilityViewProperty = property(get_AccessibilityViewProperty.__wrapped__, None)
    _AutomationProperties_Meta_.ControlledPeersProperty = property(get_ControlledPeersProperty.__wrapped__, None)
    _AutomationProperties_Meta_.PositionInSetProperty = property(get_PositionInSetProperty.__wrapped__, None)
    _AutomationProperties_Meta_.SizeOfSetProperty = property(get_SizeOfSetProperty.__wrapped__, None)
    _AutomationProperties_Meta_.LevelProperty = property(get_LevelProperty.__wrapped__, None)
    _AutomationProperties_Meta_.AnnotationsProperty = property(get_AnnotationsProperty.__wrapped__, None)
    _AutomationProperties_Meta_.LandmarkTypeProperty = property(get_LandmarkTypeProperty.__wrapped__, None)
    _AutomationProperties_Meta_.LocalizedLandmarkTypeProperty = property(get_LocalizedLandmarkTypeProperty.__wrapped__, None)
    _AutomationProperties_Meta_.IsPeripheralProperty = property(get_IsPeripheralProperty.__wrapped__, None)
    _AutomationProperties_Meta_.IsDataValidForFormProperty = property(get_IsDataValidForFormProperty.__wrapped__, None)
    _AutomationProperties_Meta_.FullDescriptionProperty = property(get_FullDescriptionProperty.__wrapped__, None)
    _AutomationProperties_Meta_.LocalizedControlTypeProperty = property(get_LocalizedControlTypeProperty.__wrapped__, None)
    _AutomationProperties_Meta_.DescribedByProperty = property(get_DescribedByProperty.__wrapped__, None)
    _AutomationProperties_Meta_.FlowsToProperty = property(get_FlowsToProperty.__wrapped__, None)
    _AutomationProperties_Meta_.FlowsFromProperty = property(get_FlowsFromProperty.__wrapped__, None)
    _AutomationProperties_Meta_.CultureProperty = property(get_CultureProperty.__wrapped__, None)
    _AutomationProperties_Meta_.HeadingLevelProperty = property(get_HeadingLevelProperty.__wrapped__, None)
    _AutomationProperties_Meta_.IsDialogProperty = property(get_IsDialogProperty.__wrapped__, None)
class AutomationProperty(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Automation.IAutomationProperty
    _classid_ = 'Microsoft.UI.Xaml.Automation.AutomationProperty'
AutomationStyleId = Int32
AutomationStyleId_Heading1: AutomationStyleId = 70001
AutomationStyleId_Heading2: AutomationStyleId = 70002
AutomationStyleId_Heading3: AutomationStyleId = 70003
AutomationStyleId_Heading4: AutomationStyleId = 70004
AutomationStyleId_Heading5: AutomationStyleId = 70005
AutomationStyleId_Heading6: AutomationStyleId = 70006
AutomationStyleId_Heading7: AutomationStyleId = 70007
AutomationStyleId_Heading8: AutomationStyleId = 70008
AutomationStyleId_Heading9: AutomationStyleId = 70009
AutomationStyleId_Title: AutomationStyleId = 70010
AutomationStyleId_Subtitle: AutomationStyleId = 70011
AutomationStyleId_Normal: AutomationStyleId = 70012
AutomationStyleId_Emphasis: AutomationStyleId = 70013
AutomationStyleId_Quote: AutomationStyleId = 70014
AutomationStyleId_BulletedList: AutomationStyleId = 70015
AutomationTextDecorationLineStyle = Int32
AutomationTextDecorationLineStyle_None: AutomationTextDecorationLineStyle = 0
AutomationTextDecorationLineStyle_Single: AutomationTextDecorationLineStyle = 1
AutomationTextDecorationLineStyle_WordsOnly: AutomationTextDecorationLineStyle = 2
AutomationTextDecorationLineStyle_Double: AutomationTextDecorationLineStyle = 3
AutomationTextDecorationLineStyle_Dot: AutomationTextDecorationLineStyle = 4
AutomationTextDecorationLineStyle_Dash: AutomationTextDecorationLineStyle = 5
AutomationTextDecorationLineStyle_DashDot: AutomationTextDecorationLineStyle = 6
AutomationTextDecorationLineStyle_DashDotDot: AutomationTextDecorationLineStyle = 7
AutomationTextDecorationLineStyle_Wavy: AutomationTextDecorationLineStyle = 8
AutomationTextDecorationLineStyle_ThickSingle: AutomationTextDecorationLineStyle = 9
AutomationTextDecorationLineStyle_DoubleWavy: AutomationTextDecorationLineStyle = 10
AutomationTextDecorationLineStyle_ThickWavy: AutomationTextDecorationLineStyle = 11
AutomationTextDecorationLineStyle_LongDash: AutomationTextDecorationLineStyle = 12
AutomationTextDecorationLineStyle_ThickDash: AutomationTextDecorationLineStyle = 13
AutomationTextDecorationLineStyle_ThickDashDot: AutomationTextDecorationLineStyle = 14
AutomationTextDecorationLineStyle_ThickDashDotDot: AutomationTextDecorationLineStyle = 15
AutomationTextDecorationLineStyle_ThickDot: AutomationTextDecorationLineStyle = 16
AutomationTextDecorationLineStyle_ThickLongDash: AutomationTextDecorationLineStyle = 17
AutomationTextDecorationLineStyle_Other: AutomationTextDecorationLineStyle = 18
AutomationTextEditChangeType = Int32
AutomationTextEditChangeType_None: AutomationTextEditChangeType = 0
AutomationTextEditChangeType_AutoCorrect: AutomationTextEditChangeType = 1
AutomationTextEditChangeType_Composition: AutomationTextEditChangeType = 2
AutomationTextEditChangeType_CompositionFinalized: AutomationTextEditChangeType = 3
class _DockPatternIdentifiers_Meta_(ComPtr.__class__):
    pass
class DockPatternIdentifiers(ComPtr, metaclass=_DockPatternIdentifiers_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Automation.IDockPatternIdentifiers
    _classid_ = 'Microsoft.UI.Xaml.Automation.DockPatternIdentifiers'
    @winrt_classmethod
    def get_DockPositionProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IDockPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    _DockPatternIdentifiers_Meta_.DockPositionProperty = property(get_DockPositionProperty.__wrapped__, None)
DockPosition = Int32
DockPosition_Top: DockPosition = 0
DockPosition_Left: DockPosition = 1
DockPosition_Bottom: DockPosition = 2
DockPosition_Right: DockPosition = 3
DockPosition_Fill: DockPosition = 4
DockPosition_None: DockPosition = 5
class _DragPatternIdentifiers_Meta_(ComPtr.__class__):
    pass
class DragPatternIdentifiers(ComPtr, metaclass=_DragPatternIdentifiers_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Automation.IDragPatternIdentifiers
    _classid_ = 'Microsoft.UI.Xaml.Automation.DragPatternIdentifiers'
    @winrt_classmethod
    def get_DropEffectProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IDragPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_DropEffectsProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IDragPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_GrabbedItemsProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IDragPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_IsGrabbedProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IDragPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    _DragPatternIdentifiers_Meta_.DropEffectProperty = property(get_DropEffectProperty.__wrapped__, None)
    _DragPatternIdentifiers_Meta_.DropEffectsProperty = property(get_DropEffectsProperty.__wrapped__, None)
    _DragPatternIdentifiers_Meta_.GrabbedItemsProperty = property(get_GrabbedItemsProperty.__wrapped__, None)
    _DragPatternIdentifiers_Meta_.IsGrabbedProperty = property(get_IsGrabbedProperty.__wrapped__, None)
class _DropTargetPatternIdentifiers_Meta_(ComPtr.__class__):
    pass
class DropTargetPatternIdentifiers(ComPtr, metaclass=_DropTargetPatternIdentifiers_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Automation.IDropTargetPatternIdentifiers
    _classid_ = 'Microsoft.UI.Xaml.Automation.DropTargetPatternIdentifiers'
    @winrt_classmethod
    def get_DropTargetEffectProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IDropTargetPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_DropTargetEffectsProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IDropTargetPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    _DropTargetPatternIdentifiers_Meta_.DropTargetEffectProperty = property(get_DropTargetEffectProperty.__wrapped__, None)
    _DropTargetPatternIdentifiers_Meta_.DropTargetEffectsProperty = property(get_DropTargetEffectsProperty.__wrapped__, None)
class _ExpandCollapsePatternIdentifiers_Meta_(ComPtr.__class__):
    pass
class ExpandCollapsePatternIdentifiers(ComPtr, metaclass=_ExpandCollapsePatternIdentifiers_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Automation.IExpandCollapsePatternIdentifiers
    _classid_ = 'Microsoft.UI.Xaml.Automation.ExpandCollapsePatternIdentifiers'
    @winrt_classmethod
    def get_ExpandCollapseStateProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IExpandCollapsePatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    _ExpandCollapsePatternIdentifiers_Meta_.ExpandCollapseStateProperty = property(get_ExpandCollapseStateProperty.__wrapped__, None)
ExpandCollapseState = Int32
ExpandCollapseState_Collapsed: ExpandCollapseState = 0
ExpandCollapseState_Expanded: ExpandCollapseState = 1
ExpandCollapseState_PartiallyExpanded: ExpandCollapseState = 2
ExpandCollapseState_LeafNode: ExpandCollapseState = 3
class _GridItemPatternIdentifiers_Meta_(ComPtr.__class__):
    pass
class GridItemPatternIdentifiers(ComPtr, metaclass=_GridItemPatternIdentifiers_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Automation.IGridItemPatternIdentifiers
    _classid_ = 'Microsoft.UI.Xaml.Automation.GridItemPatternIdentifiers'
    @winrt_classmethod
    def get_ColumnProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IGridItemPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_ColumnSpanProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IGridItemPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_ContainingGridProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IGridItemPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_RowProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IGridItemPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_RowSpanProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IGridItemPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    _GridItemPatternIdentifiers_Meta_.ColumnProperty = property(get_ColumnProperty.__wrapped__, None)
    _GridItemPatternIdentifiers_Meta_.ColumnSpanProperty = property(get_ColumnSpanProperty.__wrapped__, None)
    _GridItemPatternIdentifiers_Meta_.ContainingGridProperty = property(get_ContainingGridProperty.__wrapped__, None)
    _GridItemPatternIdentifiers_Meta_.RowProperty = property(get_RowProperty.__wrapped__, None)
    _GridItemPatternIdentifiers_Meta_.RowSpanProperty = property(get_RowSpanProperty.__wrapped__, None)
class _GridPatternIdentifiers_Meta_(ComPtr.__class__):
    pass
class GridPatternIdentifiers(ComPtr, metaclass=_GridPatternIdentifiers_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Automation.IGridPatternIdentifiers
    _classid_ = 'Microsoft.UI.Xaml.Automation.GridPatternIdentifiers'
    @winrt_classmethod
    def get_ColumnCountProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IGridPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_RowCountProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IGridPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    _GridPatternIdentifiers_Meta_.ColumnCountProperty = property(get_ColumnCountProperty.__wrapped__, None)
    _GridPatternIdentifiers_Meta_.RowCountProperty = property(get_RowCountProperty.__wrapped__, None)
class IAnnotationPatternIdentifiers(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.IAnnotationPatternIdentifiers'
    _iid_ = Guid('{92d76915-0cd3-59cd-8ae0-c9004628ba1e}')
class IAnnotationPatternIdentifiersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.IAnnotationPatternIdentifiersStatics'
    _iid_ = Guid('{20a136e2-4a47-5de5-9e1e-ecfc6d92f52a}')
    @winrt_commethod(6)
    def get_AnnotationTypeIdProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_AnnotationTypeNameProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(8)
    def get_AuthorProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(9)
    def get_DateTimeProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(10)
    def get_TargetProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    AnnotationTypeIdProperty = property(get_AnnotationTypeIdProperty, None)
    AnnotationTypeNameProperty = property(get_AnnotationTypeNameProperty, None)
    AuthorProperty = property(get_AuthorProperty, None)
    DateTimeProperty = property(get_DateTimeProperty, None)
    TargetProperty = property(get_TargetProperty, None)
class IAutomationAnnotation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.IAutomationAnnotation'
    _iid_ = Guid('{c2cc46ad-1414-5f1b-808a-89e5d53d82fe}')
    @winrt_commethod(6)
    def get_Type(self) -> win32more.Microsoft.UI.Xaml.Automation.AnnotationType: ...
    @winrt_commethod(7)
    def put_Type(self, value: win32more.Microsoft.UI.Xaml.Automation.AnnotationType) -> Void: ...
    @winrt_commethod(8)
    def get_Element(self) -> win32more.Microsoft.UI.Xaml.UIElement: ...
    @winrt_commethod(9)
    def put_Element(self, value: win32more.Microsoft.UI.Xaml.UIElement) -> Void: ...
    Type = property(get_Type, put_Type)
    Element = property(get_Element, put_Element)
class IAutomationAnnotationFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.IAutomationAnnotationFactory'
    _iid_ = Guid('{95f82773-eac5-572e-87de-24d9514b9a89}')
    @winrt_commethod(6)
    def CreateInstance(self, type: win32more.Microsoft.UI.Xaml.Automation.AnnotationType) -> win32more.Microsoft.UI.Xaml.Automation.AutomationAnnotation: ...
    @winrt_commethod(7)
    def CreateWithElementParameter(self, type: win32more.Microsoft.UI.Xaml.Automation.AnnotationType, element: win32more.Microsoft.UI.Xaml.UIElement) -> win32more.Microsoft.UI.Xaml.Automation.AutomationAnnotation: ...
class IAutomationAnnotationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.IAutomationAnnotationStatics'
    _iid_ = Guid('{c5abdc1e-fc26-5444-a8b3-59b2c0a95578}')
    @winrt_commethod(6)
    def get_TypeProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_ElementProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    TypeProperty = property(get_TypeProperty, None)
    ElementProperty = property(get_ElementProperty, None)
class IAutomationElementIdentifiers(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.IAutomationElementIdentifiers'
    _iid_ = Guid('{2fb51a33-b0cf-5a4c-9ed3-267eca7aeefc}')
class IAutomationElementIdentifiersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.IAutomationElementIdentifiersStatics'
    _iid_ = Guid('{72af6b8c-3e12-5e7a-a2ec-26dc193f9df9}')
    @winrt_commethod(6)
    def get_AcceleratorKeyProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_AccessKeyProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(8)
    def get_AutomationIdProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(9)
    def get_BoundingRectangleProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(10)
    def get_ClassNameProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(11)
    def get_ClickablePointProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(12)
    def get_ControlTypeProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(13)
    def get_HasKeyboardFocusProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(14)
    def get_HelpTextProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(15)
    def get_IsContentElementProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(16)
    def get_IsControlElementProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(17)
    def get_IsEnabledProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(18)
    def get_IsKeyboardFocusableProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(19)
    def get_IsOffscreenProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(20)
    def get_IsPasswordProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(21)
    def get_IsRequiredForFormProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(22)
    def get_ItemStatusProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(23)
    def get_ItemTypeProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(24)
    def get_LabeledByProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(25)
    def get_LocalizedControlTypeProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(26)
    def get_NameProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(27)
    def get_OrientationProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(28)
    def get_LiveSettingProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(29)
    def get_ControlledPeersProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(30)
    def get_PositionInSetProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(31)
    def get_SizeOfSetProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(32)
    def get_LevelProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(33)
    def get_AnnotationsProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(34)
    def get_LandmarkTypeProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(35)
    def get_LocalizedLandmarkTypeProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(36)
    def get_IsPeripheralProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(37)
    def get_IsDataValidForFormProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(38)
    def get_FullDescriptionProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(39)
    def get_DescribedByProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(40)
    def get_FlowsToProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(41)
    def get_FlowsFromProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(42)
    def get_CultureProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(43)
    def get_HeadingLevelProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(44)
    def get_IsDialogProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    AcceleratorKeyProperty = property(get_AcceleratorKeyProperty, None)
    AccessKeyProperty = property(get_AccessKeyProperty, None)
    AutomationIdProperty = property(get_AutomationIdProperty, None)
    BoundingRectangleProperty = property(get_BoundingRectangleProperty, None)
    ClassNameProperty = property(get_ClassNameProperty, None)
    ClickablePointProperty = property(get_ClickablePointProperty, None)
    ControlTypeProperty = property(get_ControlTypeProperty, None)
    HasKeyboardFocusProperty = property(get_HasKeyboardFocusProperty, None)
    HelpTextProperty = property(get_HelpTextProperty, None)
    IsContentElementProperty = property(get_IsContentElementProperty, None)
    IsControlElementProperty = property(get_IsControlElementProperty, None)
    IsEnabledProperty = property(get_IsEnabledProperty, None)
    IsKeyboardFocusableProperty = property(get_IsKeyboardFocusableProperty, None)
    IsOffscreenProperty = property(get_IsOffscreenProperty, None)
    IsPasswordProperty = property(get_IsPasswordProperty, None)
    IsRequiredForFormProperty = property(get_IsRequiredForFormProperty, None)
    ItemStatusProperty = property(get_ItemStatusProperty, None)
    ItemTypeProperty = property(get_ItemTypeProperty, None)
    LabeledByProperty = property(get_LabeledByProperty, None)
    LocalizedControlTypeProperty = property(get_LocalizedControlTypeProperty, None)
    NameProperty = property(get_NameProperty, None)
    OrientationProperty = property(get_OrientationProperty, None)
    LiveSettingProperty = property(get_LiveSettingProperty, None)
    ControlledPeersProperty = property(get_ControlledPeersProperty, None)
    PositionInSetProperty = property(get_PositionInSetProperty, None)
    SizeOfSetProperty = property(get_SizeOfSetProperty, None)
    LevelProperty = property(get_LevelProperty, None)
    AnnotationsProperty = property(get_AnnotationsProperty, None)
    LandmarkTypeProperty = property(get_LandmarkTypeProperty, None)
    LocalizedLandmarkTypeProperty = property(get_LocalizedLandmarkTypeProperty, None)
    IsPeripheralProperty = property(get_IsPeripheralProperty, None)
    IsDataValidForFormProperty = property(get_IsDataValidForFormProperty, None)
    FullDescriptionProperty = property(get_FullDescriptionProperty, None)
    DescribedByProperty = property(get_DescribedByProperty, None)
    FlowsToProperty = property(get_FlowsToProperty, None)
    FlowsFromProperty = property(get_FlowsFromProperty, None)
    CultureProperty = property(get_CultureProperty, None)
    HeadingLevelProperty = property(get_HeadingLevelProperty, None)
    IsDialogProperty = property(get_IsDialogProperty, None)
class IAutomationProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.IAutomationProperties'
    _iid_ = Guid('{525c6a71-dd8a-52a0-977b-db1b02f8e896}')
class IAutomationPropertiesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics'
    _iid_ = Guid('{b1e3e0f3-112f-5966-87dc-7862d4ad50e5}')
    @winrt_commethod(6)
    def get_AcceleratorKeyProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def GetAcceleratorKey(self, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_commethod(8)
    def SetAcceleratorKey(self, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_AccessKeyProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def GetAccessKey(self, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_commethod(11)
    def SetAccessKey(self, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_AutomationIdProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def GetAutomationId(self, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_commethod(14)
    def SetAutomationId(self, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_commethod(15)
    def get_HelpTextProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(16)
    def GetHelpText(self, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_commethod(17)
    def SetHelpText(self, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_commethod(18)
    def get_IsRequiredForFormProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(19)
    def GetIsRequiredForForm(self, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> Boolean: ...
    @winrt_commethod(20)
    def SetIsRequiredForForm(self, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: Boolean) -> Void: ...
    @winrt_commethod(21)
    def get_ItemStatusProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(22)
    def GetItemStatus(self, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_commethod(23)
    def SetItemStatus(self, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_commethod(24)
    def get_ItemTypeProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(25)
    def GetItemType(self, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_commethod(26)
    def SetItemType(self, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_commethod(27)
    def get_LabeledByProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(28)
    def GetLabeledBy(self, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> win32more.Microsoft.UI.Xaml.UIElement: ...
    @winrt_commethod(29)
    def SetLabeledBy(self, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: win32more.Microsoft.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(30)
    def get_NameProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(31)
    def GetName(self, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_commethod(32)
    def SetName(self, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_commethod(33)
    def get_LiveSettingProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(34)
    def GetLiveSetting(self, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationLiveSetting: ...
    @winrt_commethod(35)
    def SetLiveSetting(self, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationLiveSetting) -> Void: ...
    @winrt_commethod(36)
    def get_AccessibilityViewProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(37)
    def GetAccessibilityView(self, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AccessibilityView: ...
    @winrt_commethod(38)
    def SetAccessibilityView(self, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: win32more.Microsoft.UI.Xaml.Automation.Peers.AccessibilityView) -> Void: ...
    @winrt_commethod(39)
    def get_ControlledPeersProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(40)
    def GetControlledPeers(self, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.UIElement]: ...
    @winrt_commethod(41)
    def get_PositionInSetProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(42)
    def GetPositionInSet(self, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> Int32: ...
    @winrt_commethod(43)
    def SetPositionInSet(self, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: Int32) -> Void: ...
    @winrt_commethod(44)
    def get_SizeOfSetProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(45)
    def GetSizeOfSet(self, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> Int32: ...
    @winrt_commethod(46)
    def SetSizeOfSet(self, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: Int32) -> Void: ...
    @winrt_commethod(47)
    def get_LevelProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(48)
    def GetLevel(self, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> Int32: ...
    @winrt_commethod(49)
    def SetLevel(self, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: Int32) -> Void: ...
    @winrt_commethod(50)
    def get_AnnotationsProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(51)
    def GetAnnotations(self, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Automation.AutomationAnnotation]: ...
    @winrt_commethod(52)
    def get_LandmarkTypeProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(53)
    def GetLandmarkType(self, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationLandmarkType: ...
    @winrt_commethod(54)
    def SetLandmarkType(self, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationLandmarkType) -> Void: ...
    @winrt_commethod(55)
    def get_LocalizedLandmarkTypeProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(56)
    def GetLocalizedLandmarkType(self, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_commethod(57)
    def SetLocalizedLandmarkType(self, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_commethod(58)
    def get_IsPeripheralProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(59)
    def GetIsPeripheral(self, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> Boolean: ...
    @winrt_commethod(60)
    def SetIsPeripheral(self, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: Boolean) -> Void: ...
    @winrt_commethod(61)
    def get_IsDataValidForFormProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(62)
    def GetIsDataValidForForm(self, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> Boolean: ...
    @winrt_commethod(63)
    def SetIsDataValidForForm(self, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: Boolean) -> Void: ...
    @winrt_commethod(64)
    def get_FullDescriptionProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(65)
    def GetFullDescription(self, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_commethod(66)
    def SetFullDescription(self, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_commethod(67)
    def get_LocalizedControlTypeProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(68)
    def GetLocalizedControlType(self, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_commethod(69)
    def SetLocalizedControlType(self, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_commethod(70)
    def get_DescribedByProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(71)
    def GetDescribedBy(self, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.DependencyObject]: ...
    @winrt_commethod(72)
    def get_FlowsToProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(73)
    def GetFlowsTo(self, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.DependencyObject]: ...
    @winrt_commethod(74)
    def get_FlowsFromProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(75)
    def GetFlowsFrom(self, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.DependencyObject]: ...
    @winrt_commethod(76)
    def get_CultureProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(77)
    def GetCulture(self, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> Int32: ...
    @winrt_commethod(78)
    def SetCulture(self, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: Int32) -> Void: ...
    @winrt_commethod(79)
    def get_HeadingLevelProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(80)
    def GetHeadingLevel(self, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationHeadingLevel: ...
    @winrt_commethod(81)
    def SetHeadingLevel(self, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationHeadingLevel) -> Void: ...
    @winrt_commethod(82)
    def get_IsDialogProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(83)
    def GetIsDialog(self, element: win32more.Microsoft.UI.Xaml.DependencyObject) -> Boolean: ...
    @winrt_commethod(84)
    def SetIsDialog(self, element: win32more.Microsoft.UI.Xaml.DependencyObject, value: Boolean) -> Void: ...
    AcceleratorKeyProperty = property(get_AcceleratorKeyProperty, None)
    AccessKeyProperty = property(get_AccessKeyProperty, None)
    AutomationIdProperty = property(get_AutomationIdProperty, None)
    HelpTextProperty = property(get_HelpTextProperty, None)
    IsRequiredForFormProperty = property(get_IsRequiredForFormProperty, None)
    ItemStatusProperty = property(get_ItemStatusProperty, None)
    ItemTypeProperty = property(get_ItemTypeProperty, None)
    LabeledByProperty = property(get_LabeledByProperty, None)
    NameProperty = property(get_NameProperty, None)
    LiveSettingProperty = property(get_LiveSettingProperty, None)
    AccessibilityViewProperty = property(get_AccessibilityViewProperty, None)
    ControlledPeersProperty = property(get_ControlledPeersProperty, None)
    PositionInSetProperty = property(get_PositionInSetProperty, None)
    SizeOfSetProperty = property(get_SizeOfSetProperty, None)
    LevelProperty = property(get_LevelProperty, None)
    AnnotationsProperty = property(get_AnnotationsProperty, None)
    LandmarkTypeProperty = property(get_LandmarkTypeProperty, None)
    LocalizedLandmarkTypeProperty = property(get_LocalizedLandmarkTypeProperty, None)
    IsPeripheralProperty = property(get_IsPeripheralProperty, None)
    IsDataValidForFormProperty = property(get_IsDataValidForFormProperty, None)
    FullDescriptionProperty = property(get_FullDescriptionProperty, None)
    LocalizedControlTypeProperty = property(get_LocalizedControlTypeProperty, None)
    DescribedByProperty = property(get_DescribedByProperty, None)
    FlowsToProperty = property(get_FlowsToProperty, None)
    FlowsFromProperty = property(get_FlowsFromProperty, None)
    CultureProperty = property(get_CultureProperty, None)
    HeadingLevelProperty = property(get_HeadingLevelProperty, None)
    IsDialogProperty = property(get_IsDialogProperty, None)
class IAutomationPropertiesStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.IAutomationPropertiesStatics2'
    _iid_ = Guid('{d933a3ed-e90a-5df0-853d-cad17a0b9ec8}')
    @winrt_commethod(6)
    def get_AutomationControlTypeProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def GetAutomationControlType(self, element: win32more.Microsoft.UI.Xaml.UIElement) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationControlType: ...
    @winrt_commethod(8)
    def SetAutomationControlType(self, element: win32more.Microsoft.UI.Xaml.UIElement, value: win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationControlType) -> Void: ...
    AutomationControlTypeProperty = property(get_AutomationControlTypeProperty, None)
class IAutomationProperty(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.IAutomationProperty'
    _iid_ = Guid('{5ca6b2c8-ff86-5a41-aa18-6948fae592cf}')
class IDockPatternIdentifiers(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.IDockPatternIdentifiers'
    _iid_ = Guid('{75574f99-d145-547e-972b-7d879f93c03e}')
class IDockPatternIdentifiersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.IDockPatternIdentifiersStatics'
    _iid_ = Guid('{02d5a72c-f49d-53a9-b9fb-af2719d16ccf}')
    @winrt_commethod(6)
    def get_DockPositionProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    DockPositionProperty = property(get_DockPositionProperty, None)
class IDragPatternIdentifiers(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.IDragPatternIdentifiers'
    _iid_ = Guid('{aa2fdfd5-fb45-5d2b-8d92-a8e7b07061c2}')
class IDragPatternIdentifiersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.IDragPatternIdentifiersStatics'
    _iid_ = Guid('{482eee70-0bfc-5552-9e7d-8dffc526b2f7}')
    @winrt_commethod(6)
    def get_DropEffectProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_DropEffectsProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(8)
    def get_GrabbedItemsProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(9)
    def get_IsGrabbedProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    DropEffectProperty = property(get_DropEffectProperty, None)
    DropEffectsProperty = property(get_DropEffectsProperty, None)
    GrabbedItemsProperty = property(get_GrabbedItemsProperty, None)
    IsGrabbedProperty = property(get_IsGrabbedProperty, None)
class IDropTargetPatternIdentifiers(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.IDropTargetPatternIdentifiers'
    _iid_ = Guid('{133e8ff3-1ddd-5cbb-b908-1484d7c04da7}')
class IDropTargetPatternIdentifiersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.IDropTargetPatternIdentifiersStatics'
    _iid_ = Guid('{6da6f0bd-b942-5283-be35-501ae87f88c7}')
    @winrt_commethod(6)
    def get_DropTargetEffectProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_DropTargetEffectsProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    DropTargetEffectProperty = property(get_DropTargetEffectProperty, None)
    DropTargetEffectsProperty = property(get_DropTargetEffectsProperty, None)
class IExpandCollapsePatternIdentifiers(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.IExpandCollapsePatternIdentifiers'
    _iid_ = Guid('{cec15d9f-8630-569a-86a0-524bbea618ff}')
class IExpandCollapsePatternIdentifiersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.IExpandCollapsePatternIdentifiersStatics'
    _iid_ = Guid('{283101f4-c40c-55bf-a23b-d62b73b6aa35}')
    @winrt_commethod(6)
    def get_ExpandCollapseStateProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    ExpandCollapseStateProperty = property(get_ExpandCollapseStateProperty, None)
class IGridItemPatternIdentifiers(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.IGridItemPatternIdentifiers'
    _iid_ = Guid('{93609087-1114-557d-b17b-f801e41cebbb}')
class IGridItemPatternIdentifiersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.IGridItemPatternIdentifiersStatics'
    _iid_ = Guid('{8072bc18-87d0-5a02-a0a1-f9aec968c0e7}')
    @winrt_commethod(6)
    def get_ColumnProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_ColumnSpanProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(8)
    def get_ContainingGridProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(9)
    def get_RowProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(10)
    def get_RowSpanProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    ColumnProperty = property(get_ColumnProperty, None)
    ColumnSpanProperty = property(get_ColumnSpanProperty, None)
    ContainingGridProperty = property(get_ContainingGridProperty, None)
    RowProperty = property(get_RowProperty, None)
    RowSpanProperty = property(get_RowSpanProperty, None)
class IGridPatternIdentifiers(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.IGridPatternIdentifiers'
    _iid_ = Guid('{e5e1e250-c37c-54a2-8c61-1d9ccd3bb39c}')
class IGridPatternIdentifiersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.IGridPatternIdentifiersStatics'
    _iid_ = Guid('{e861604c-101f-5a6d-a308-3714f510f744}')
    @winrt_commethod(6)
    def get_ColumnCountProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_RowCountProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    ColumnCountProperty = property(get_ColumnCountProperty, None)
    RowCountProperty = property(get_RowCountProperty, None)
class IMultipleViewPatternIdentifiers(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.IMultipleViewPatternIdentifiers'
    _iid_ = Guid('{70e4c847-2b82-5ecf-b808-e9d453c1fe53}')
class IMultipleViewPatternIdentifiersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.IMultipleViewPatternIdentifiersStatics'
    _iid_ = Guid('{ac71daef-d094-5c90-94af-1fa474ab45fe}')
    @winrt_commethod(6)
    def get_CurrentViewProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_SupportedViewsProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    CurrentViewProperty = property(get_CurrentViewProperty, None)
    SupportedViewsProperty = property(get_SupportedViewsProperty, None)
class IRangeValuePatternIdentifiers(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.IRangeValuePatternIdentifiers'
    _iid_ = Guid('{c114db37-6a75-5ef1-a542-d3b13f92cbfe}')
class IRangeValuePatternIdentifiersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.IRangeValuePatternIdentifiersStatics'
    _iid_ = Guid('{0aaa9ad7-f9b8-52a1-bc96-2a97fe389ed0}')
    @winrt_commethod(6)
    def get_IsReadOnlyProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_LargeChangeProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(8)
    def get_MaximumProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(9)
    def get_MinimumProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(10)
    def get_SmallChangeProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(11)
    def get_ValueProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    IsReadOnlyProperty = property(get_IsReadOnlyProperty, None)
    LargeChangeProperty = property(get_LargeChangeProperty, None)
    MaximumProperty = property(get_MaximumProperty, None)
    MinimumProperty = property(get_MinimumProperty, None)
    SmallChangeProperty = property(get_SmallChangeProperty, None)
    ValueProperty = property(get_ValueProperty, None)
class IScrollPatternIdentifiers(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.IScrollPatternIdentifiers'
    _iid_ = Guid('{04f1a4b8-edc7-55f2-96df-a9c7e809372e}')
class IScrollPatternIdentifiersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.IScrollPatternIdentifiersStatics'
    _iid_ = Guid('{0f94f2f0-e0d2-5a24-b415-8d1506ce47aa}')
    @winrt_commethod(6)
    def get_HorizontallyScrollableProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_HorizontalScrollPercentProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(8)
    def get_HorizontalViewSizeProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(9)
    def get_NoScroll(self) -> Double: ...
    @winrt_commethod(10)
    def get_VerticallyScrollableProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(11)
    def get_VerticalScrollPercentProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(12)
    def get_VerticalViewSizeProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    HorizontallyScrollableProperty = property(get_HorizontallyScrollableProperty, None)
    HorizontalScrollPercentProperty = property(get_HorizontalScrollPercentProperty, None)
    HorizontalViewSizeProperty = property(get_HorizontalViewSizeProperty, None)
    NoScroll = property(get_NoScroll, None)
    VerticallyScrollableProperty = property(get_VerticallyScrollableProperty, None)
    VerticalScrollPercentProperty = property(get_VerticalScrollPercentProperty, None)
    VerticalViewSizeProperty = property(get_VerticalViewSizeProperty, None)
class ISelectionItemPatternIdentifiers(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.ISelectionItemPatternIdentifiers'
    _iid_ = Guid('{ce3a549d-a2cb-594d-a2a4-44778c09cca5}')
class ISelectionItemPatternIdentifiersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.ISelectionItemPatternIdentifiersStatics'
    _iid_ = Guid('{2b8ead7c-4e03-5b84-9e34-8b7384cbd862}')
    @winrt_commethod(6)
    def get_IsSelectedProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_SelectionContainerProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    IsSelectedProperty = property(get_IsSelectedProperty, None)
    SelectionContainerProperty = property(get_SelectionContainerProperty, None)
class ISelectionPatternIdentifiers(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.ISelectionPatternIdentifiers'
    _iid_ = Guid('{401743d2-1fba-5d05-b89f-631676453237}')
class ISelectionPatternIdentifiersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.ISelectionPatternIdentifiersStatics'
    _iid_ = Guid('{f3ed111b-b20a-5e5e-a232-07f607fd5c07}')
    @winrt_commethod(6)
    def get_CanSelectMultipleProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_IsSelectionRequiredProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(8)
    def get_SelectionProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    CanSelectMultipleProperty = property(get_CanSelectMultipleProperty, None)
    IsSelectionRequiredProperty = property(get_IsSelectionRequiredProperty, None)
    SelectionProperty = property(get_SelectionProperty, None)
class ISpreadsheetItemPatternIdentifiers(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.ISpreadsheetItemPatternIdentifiers'
    _iid_ = Guid('{dca2ec46-8564-5c9c-ba90-2c08455f697b}')
class ISpreadsheetItemPatternIdentifiersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.ISpreadsheetItemPatternIdentifiersStatics'
    _iid_ = Guid('{7eb10f80-8d3a-59ad-a2b9-05d8cecf18db}')
    @winrt_commethod(6)
    def get_FormulaProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    FormulaProperty = property(get_FormulaProperty, None)
class IStylesPatternIdentifiers(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.IStylesPatternIdentifiers'
    _iid_ = Guid('{13aeca5e-b496-5df5-aea5-330e1f0490eb}')
class IStylesPatternIdentifiersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.IStylesPatternIdentifiersStatics'
    _iid_ = Guid('{b232287a-bc4c-581e-a33c-3d6aee10d04b}')
    @winrt_commethod(6)
    def get_ExtendedPropertiesProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_FillColorProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(8)
    def get_FillPatternColorProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(9)
    def get_FillPatternStyleProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(10)
    def get_ShapeProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(11)
    def get_StyleIdProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(12)
    def get_StyleNameProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    ExtendedPropertiesProperty = property(get_ExtendedPropertiesProperty, None)
    FillColorProperty = property(get_FillColorProperty, None)
    FillPatternColorProperty = property(get_FillPatternColorProperty, None)
    FillPatternStyleProperty = property(get_FillPatternStyleProperty, None)
    ShapeProperty = property(get_ShapeProperty, None)
    StyleIdProperty = property(get_StyleIdProperty, None)
    StyleNameProperty = property(get_StyleNameProperty, None)
class ITableItemPatternIdentifiers(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.ITableItemPatternIdentifiers'
    _iid_ = Guid('{b4de5d03-a5b4-5ca1-8715-16c8c6a10fcc}')
class ITableItemPatternIdentifiersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.ITableItemPatternIdentifiersStatics'
    _iid_ = Guid('{81d24bd7-66fb-53ef-9b32-d00f9c240a14}')
    @winrt_commethod(6)
    def get_ColumnHeaderItemsProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_RowHeaderItemsProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    ColumnHeaderItemsProperty = property(get_ColumnHeaderItemsProperty, None)
    RowHeaderItemsProperty = property(get_RowHeaderItemsProperty, None)
class ITablePatternIdentifiers(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.ITablePatternIdentifiers'
    _iid_ = Guid('{3d7f9c0b-ff8f-50fa-bc01-2cc3c2e06e2c}')
class ITablePatternIdentifiersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.ITablePatternIdentifiersStatics'
    _iid_ = Guid('{3660935e-bcbb-5848-8e9a-264854f7a19a}')
    @winrt_commethod(6)
    def get_ColumnHeadersProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_RowHeadersProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(8)
    def get_RowOrColumnMajorProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    ColumnHeadersProperty = property(get_ColumnHeadersProperty, None)
    RowHeadersProperty = property(get_RowHeadersProperty, None)
    RowOrColumnMajorProperty = property(get_RowOrColumnMajorProperty, None)
class ITogglePatternIdentifiers(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.ITogglePatternIdentifiers'
    _iid_ = Guid('{a0d2df4c-ba59-51d9-9c01-034d7941c280}')
class ITogglePatternIdentifiersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.ITogglePatternIdentifiersStatics'
    _iid_ = Guid('{862920b5-dcb3-5691-a456-c2f15c476dfb}')
    @winrt_commethod(6)
    def get_ToggleStateProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    ToggleStateProperty = property(get_ToggleStateProperty, None)
class ITransformPattern2Identifiers(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.ITransformPattern2Identifiers'
    _iid_ = Guid('{6ef7595c-db8c-51b0-878b-34b7ef12f4da}')
class ITransformPattern2IdentifiersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.ITransformPattern2IdentifiersStatics'
    _iid_ = Guid('{d9876ff5-89ed-5333-8111-ad25a28bee8b}')
    @winrt_commethod(6)
    def get_CanZoomProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_ZoomLevelProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(8)
    def get_MaxZoomProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(9)
    def get_MinZoomProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    CanZoomProperty = property(get_CanZoomProperty, None)
    ZoomLevelProperty = property(get_ZoomLevelProperty, None)
    MaxZoomProperty = property(get_MaxZoomProperty, None)
    MinZoomProperty = property(get_MinZoomProperty, None)
class ITransformPatternIdentifiers(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.ITransformPatternIdentifiers'
    _iid_ = Guid('{2348187b-c50f-5a0e-bc05-305ac71b3b6b}')
class ITransformPatternIdentifiersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.ITransformPatternIdentifiersStatics'
    _iid_ = Guid('{cb7d84e4-5429-5188-8aa0-5f96558a8790}')
    @winrt_commethod(6)
    def get_CanMoveProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_CanResizeProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(8)
    def get_CanRotateProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    CanMoveProperty = property(get_CanMoveProperty, None)
    CanResizeProperty = property(get_CanResizeProperty, None)
    CanRotateProperty = property(get_CanRotateProperty, None)
class IValuePatternIdentifiers(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.IValuePatternIdentifiers'
    _iid_ = Guid('{fb493395-fb97-59d5-9323-4651ce964b55}')
class IValuePatternIdentifiersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.IValuePatternIdentifiersStatics'
    _iid_ = Guid('{2019faf5-ce64-59a7-bc13-0677c3146724}')
    @winrt_commethod(6)
    def get_IsReadOnlyProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_ValueProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    IsReadOnlyProperty = property(get_IsReadOnlyProperty, None)
    ValueProperty = property(get_ValueProperty, None)
class IWindowPatternIdentifiers(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.IWindowPatternIdentifiers'
    _iid_ = Guid('{bec579e1-91be-5d8f-aaca-6ad8839872d2}')
class IWindowPatternIdentifiersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.IWindowPatternIdentifiersStatics'
    _iid_ = Guid('{06762744-d3d7-5441-b879-373681d47f64}')
    @winrt_commethod(6)
    def get_CanMaximizeProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_CanMinimizeProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(8)
    def get_IsModalProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(9)
    def get_IsTopmostProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(10)
    def get_WindowInteractionStateProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(11)
    def get_WindowVisualStateProperty(self) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    CanMaximizeProperty = property(get_CanMaximizeProperty, None)
    CanMinimizeProperty = property(get_CanMinimizeProperty, None)
    IsModalProperty = property(get_IsModalProperty, None)
    IsTopmostProperty = property(get_IsTopmostProperty, None)
    WindowInteractionStateProperty = property(get_WindowInteractionStateProperty, None)
    WindowVisualStateProperty = property(get_WindowVisualStateProperty, None)
class _MultipleViewPatternIdentifiers_Meta_(ComPtr.__class__):
    pass
class MultipleViewPatternIdentifiers(ComPtr, metaclass=_MultipleViewPatternIdentifiers_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Automation.IMultipleViewPatternIdentifiers
    _classid_ = 'Microsoft.UI.Xaml.Automation.MultipleViewPatternIdentifiers'
    @winrt_classmethod
    def get_CurrentViewProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IMultipleViewPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_SupportedViewsProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IMultipleViewPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    _MultipleViewPatternIdentifiers_Meta_.CurrentViewProperty = property(get_CurrentViewProperty.__wrapped__, None)
    _MultipleViewPatternIdentifiers_Meta_.SupportedViewsProperty = property(get_SupportedViewsProperty.__wrapped__, None)
class _RangeValuePatternIdentifiers_Meta_(ComPtr.__class__):
    pass
class RangeValuePatternIdentifiers(ComPtr, metaclass=_RangeValuePatternIdentifiers_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Automation.IRangeValuePatternIdentifiers
    _classid_ = 'Microsoft.UI.Xaml.Automation.RangeValuePatternIdentifiers'
    @winrt_classmethod
    def get_IsReadOnlyProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IRangeValuePatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_LargeChangeProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IRangeValuePatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_MaximumProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IRangeValuePatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_MinimumProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IRangeValuePatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_SmallChangeProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IRangeValuePatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_ValueProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IRangeValuePatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    _RangeValuePatternIdentifiers_Meta_.IsReadOnlyProperty = property(get_IsReadOnlyProperty.__wrapped__, None)
    _RangeValuePatternIdentifiers_Meta_.LargeChangeProperty = property(get_LargeChangeProperty.__wrapped__, None)
    _RangeValuePatternIdentifiers_Meta_.MaximumProperty = property(get_MaximumProperty.__wrapped__, None)
    _RangeValuePatternIdentifiers_Meta_.MinimumProperty = property(get_MinimumProperty.__wrapped__, None)
    _RangeValuePatternIdentifiers_Meta_.SmallChangeProperty = property(get_SmallChangeProperty.__wrapped__, None)
    _RangeValuePatternIdentifiers_Meta_.ValueProperty = property(get_ValueProperty.__wrapped__, None)
RowOrColumnMajor = Int32
RowOrColumnMajor_RowMajor: RowOrColumnMajor = 0
RowOrColumnMajor_ColumnMajor: RowOrColumnMajor = 1
RowOrColumnMajor_Indeterminate: RowOrColumnMajor = 2
ScrollAmount = Int32
ScrollAmount_LargeDecrement: ScrollAmount = 0
ScrollAmount_SmallDecrement: ScrollAmount = 1
ScrollAmount_NoAmount: ScrollAmount = 2
ScrollAmount_LargeIncrement: ScrollAmount = 3
ScrollAmount_SmallIncrement: ScrollAmount = 4
class _ScrollPatternIdentifiers_Meta_(ComPtr.__class__):
    pass
class ScrollPatternIdentifiers(ComPtr, metaclass=_ScrollPatternIdentifiers_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Automation.IScrollPatternIdentifiers
    _classid_ = 'Microsoft.UI.Xaml.Automation.ScrollPatternIdentifiers'
    @winrt_classmethod
    def get_HorizontallyScrollableProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IScrollPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_HorizontalScrollPercentProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IScrollPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_HorizontalViewSizeProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IScrollPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_NoScroll(cls: win32more.Microsoft.UI.Xaml.Automation.IScrollPatternIdentifiersStatics) -> Double: ...
    @winrt_classmethod
    def get_VerticallyScrollableProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IScrollPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_VerticalScrollPercentProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IScrollPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_VerticalViewSizeProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IScrollPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    _ScrollPatternIdentifiers_Meta_.HorizontallyScrollableProperty = property(get_HorizontallyScrollableProperty.__wrapped__, None)
    _ScrollPatternIdentifiers_Meta_.HorizontalScrollPercentProperty = property(get_HorizontalScrollPercentProperty.__wrapped__, None)
    _ScrollPatternIdentifiers_Meta_.HorizontalViewSizeProperty = property(get_HorizontalViewSizeProperty.__wrapped__, None)
    _ScrollPatternIdentifiers_Meta_.NoScroll = property(get_NoScroll.__wrapped__, None)
    _ScrollPatternIdentifiers_Meta_.VerticallyScrollableProperty = property(get_VerticallyScrollableProperty.__wrapped__, None)
    _ScrollPatternIdentifiers_Meta_.VerticalScrollPercentProperty = property(get_VerticalScrollPercentProperty.__wrapped__, None)
    _ScrollPatternIdentifiers_Meta_.VerticalViewSizeProperty = property(get_VerticalViewSizeProperty.__wrapped__, None)
class _SelectionItemPatternIdentifiers_Meta_(ComPtr.__class__):
    pass
class SelectionItemPatternIdentifiers(ComPtr, metaclass=_SelectionItemPatternIdentifiers_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Automation.ISelectionItemPatternIdentifiers
    _classid_ = 'Microsoft.UI.Xaml.Automation.SelectionItemPatternIdentifiers'
    @winrt_classmethod
    def get_IsSelectedProperty(cls: win32more.Microsoft.UI.Xaml.Automation.ISelectionItemPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_SelectionContainerProperty(cls: win32more.Microsoft.UI.Xaml.Automation.ISelectionItemPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    _SelectionItemPatternIdentifiers_Meta_.IsSelectedProperty = property(get_IsSelectedProperty.__wrapped__, None)
    _SelectionItemPatternIdentifiers_Meta_.SelectionContainerProperty = property(get_SelectionContainerProperty.__wrapped__, None)
class _SelectionPatternIdentifiers_Meta_(ComPtr.__class__):
    pass
class SelectionPatternIdentifiers(ComPtr, metaclass=_SelectionPatternIdentifiers_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Automation.ISelectionPatternIdentifiers
    _classid_ = 'Microsoft.UI.Xaml.Automation.SelectionPatternIdentifiers'
    @winrt_classmethod
    def get_CanSelectMultipleProperty(cls: win32more.Microsoft.UI.Xaml.Automation.ISelectionPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_IsSelectionRequiredProperty(cls: win32more.Microsoft.UI.Xaml.Automation.ISelectionPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_SelectionProperty(cls: win32more.Microsoft.UI.Xaml.Automation.ISelectionPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    _SelectionPatternIdentifiers_Meta_.CanSelectMultipleProperty = property(get_CanSelectMultipleProperty.__wrapped__, None)
    _SelectionPatternIdentifiers_Meta_.IsSelectionRequiredProperty = property(get_IsSelectionRequiredProperty.__wrapped__, None)
    _SelectionPatternIdentifiers_Meta_.SelectionProperty = property(get_SelectionProperty.__wrapped__, None)
class _SpreadsheetItemPatternIdentifiers_Meta_(ComPtr.__class__):
    pass
class SpreadsheetItemPatternIdentifiers(ComPtr, metaclass=_SpreadsheetItemPatternIdentifiers_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Automation.ISpreadsheetItemPatternIdentifiers
    _classid_ = 'Microsoft.UI.Xaml.Automation.SpreadsheetItemPatternIdentifiers'
    @winrt_classmethod
    def get_FormulaProperty(cls: win32more.Microsoft.UI.Xaml.Automation.ISpreadsheetItemPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    _SpreadsheetItemPatternIdentifiers_Meta_.FormulaProperty = property(get_FormulaProperty.__wrapped__, None)
class _StylesPatternIdentifiers_Meta_(ComPtr.__class__):
    pass
class StylesPatternIdentifiers(ComPtr, metaclass=_StylesPatternIdentifiers_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Automation.IStylesPatternIdentifiers
    _classid_ = 'Microsoft.UI.Xaml.Automation.StylesPatternIdentifiers'
    @winrt_classmethod
    def get_ExtendedPropertiesProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IStylesPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_FillColorProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IStylesPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_FillPatternColorProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IStylesPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_FillPatternStyleProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IStylesPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_ShapeProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IStylesPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_StyleIdProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IStylesPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_StyleNameProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IStylesPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    _StylesPatternIdentifiers_Meta_.ExtendedPropertiesProperty = property(get_ExtendedPropertiesProperty.__wrapped__, None)
    _StylesPatternIdentifiers_Meta_.FillColorProperty = property(get_FillColorProperty.__wrapped__, None)
    _StylesPatternIdentifiers_Meta_.FillPatternColorProperty = property(get_FillPatternColorProperty.__wrapped__, None)
    _StylesPatternIdentifiers_Meta_.FillPatternStyleProperty = property(get_FillPatternStyleProperty.__wrapped__, None)
    _StylesPatternIdentifiers_Meta_.ShapeProperty = property(get_ShapeProperty.__wrapped__, None)
    _StylesPatternIdentifiers_Meta_.StyleIdProperty = property(get_StyleIdProperty.__wrapped__, None)
    _StylesPatternIdentifiers_Meta_.StyleNameProperty = property(get_StyleNameProperty.__wrapped__, None)
SupportedTextSelection = Int32
SupportedTextSelection_None: SupportedTextSelection = 0
SupportedTextSelection_Single: SupportedTextSelection = 1
SupportedTextSelection_Multiple: SupportedTextSelection = 2
SynchronizedInputType = Int32
SynchronizedInputType_KeyUp: SynchronizedInputType = 1
SynchronizedInputType_KeyDown: SynchronizedInputType = 2
SynchronizedInputType_LeftMouseUp: SynchronizedInputType = 4
SynchronizedInputType_LeftMouseDown: SynchronizedInputType = 8
SynchronizedInputType_RightMouseUp: SynchronizedInputType = 16
SynchronizedInputType_RightMouseDown: SynchronizedInputType = 32
class _TableItemPatternIdentifiers_Meta_(ComPtr.__class__):
    pass
class TableItemPatternIdentifiers(ComPtr, metaclass=_TableItemPatternIdentifiers_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Automation.ITableItemPatternIdentifiers
    _classid_ = 'Microsoft.UI.Xaml.Automation.TableItemPatternIdentifiers'
    @winrt_classmethod
    def get_ColumnHeaderItemsProperty(cls: win32more.Microsoft.UI.Xaml.Automation.ITableItemPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_RowHeaderItemsProperty(cls: win32more.Microsoft.UI.Xaml.Automation.ITableItemPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    _TableItemPatternIdentifiers_Meta_.ColumnHeaderItemsProperty = property(get_ColumnHeaderItemsProperty.__wrapped__, None)
    _TableItemPatternIdentifiers_Meta_.RowHeaderItemsProperty = property(get_RowHeaderItemsProperty.__wrapped__, None)
class _TablePatternIdentifiers_Meta_(ComPtr.__class__):
    pass
class TablePatternIdentifiers(ComPtr, metaclass=_TablePatternIdentifiers_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Automation.ITablePatternIdentifiers
    _classid_ = 'Microsoft.UI.Xaml.Automation.TablePatternIdentifiers'
    @winrt_classmethod
    def get_ColumnHeadersProperty(cls: win32more.Microsoft.UI.Xaml.Automation.ITablePatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_RowHeadersProperty(cls: win32more.Microsoft.UI.Xaml.Automation.ITablePatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_RowOrColumnMajorProperty(cls: win32more.Microsoft.UI.Xaml.Automation.ITablePatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    _TablePatternIdentifiers_Meta_.ColumnHeadersProperty = property(get_ColumnHeadersProperty.__wrapped__, None)
    _TablePatternIdentifiers_Meta_.RowHeadersProperty = property(get_RowHeadersProperty.__wrapped__, None)
    _TablePatternIdentifiers_Meta_.RowOrColumnMajorProperty = property(get_RowOrColumnMajorProperty.__wrapped__, None)
class _TogglePatternIdentifiers_Meta_(ComPtr.__class__):
    pass
class TogglePatternIdentifiers(ComPtr, metaclass=_TogglePatternIdentifiers_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Automation.ITogglePatternIdentifiers
    _classid_ = 'Microsoft.UI.Xaml.Automation.TogglePatternIdentifiers'
    @winrt_classmethod
    def get_ToggleStateProperty(cls: win32more.Microsoft.UI.Xaml.Automation.ITogglePatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    _TogglePatternIdentifiers_Meta_.ToggleStateProperty = property(get_ToggleStateProperty.__wrapped__, None)
ToggleState = Int32
ToggleState_Off: ToggleState = 0
ToggleState_On: ToggleState = 1
ToggleState_Indeterminate: ToggleState = 2
class _TransformPattern2Identifiers_Meta_(ComPtr.__class__):
    pass
class TransformPattern2Identifiers(ComPtr, metaclass=_TransformPattern2Identifiers_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Automation.ITransformPattern2Identifiers
    _classid_ = 'Microsoft.UI.Xaml.Automation.TransformPattern2Identifiers'
    @winrt_classmethod
    def get_CanZoomProperty(cls: win32more.Microsoft.UI.Xaml.Automation.ITransformPattern2IdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_ZoomLevelProperty(cls: win32more.Microsoft.UI.Xaml.Automation.ITransformPattern2IdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_MaxZoomProperty(cls: win32more.Microsoft.UI.Xaml.Automation.ITransformPattern2IdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_MinZoomProperty(cls: win32more.Microsoft.UI.Xaml.Automation.ITransformPattern2IdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    _TransformPattern2Identifiers_Meta_.CanZoomProperty = property(get_CanZoomProperty.__wrapped__, None)
    _TransformPattern2Identifiers_Meta_.ZoomLevelProperty = property(get_ZoomLevelProperty.__wrapped__, None)
    _TransformPattern2Identifiers_Meta_.MaxZoomProperty = property(get_MaxZoomProperty.__wrapped__, None)
    _TransformPattern2Identifiers_Meta_.MinZoomProperty = property(get_MinZoomProperty.__wrapped__, None)
class _TransformPatternIdentifiers_Meta_(ComPtr.__class__):
    pass
class TransformPatternIdentifiers(ComPtr, metaclass=_TransformPatternIdentifiers_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Automation.ITransformPatternIdentifiers
    _classid_ = 'Microsoft.UI.Xaml.Automation.TransformPatternIdentifiers'
    @winrt_classmethod
    def get_CanMoveProperty(cls: win32more.Microsoft.UI.Xaml.Automation.ITransformPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_CanResizeProperty(cls: win32more.Microsoft.UI.Xaml.Automation.ITransformPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_CanRotateProperty(cls: win32more.Microsoft.UI.Xaml.Automation.ITransformPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    _TransformPatternIdentifiers_Meta_.CanMoveProperty = property(get_CanMoveProperty.__wrapped__, None)
    _TransformPatternIdentifiers_Meta_.CanResizeProperty = property(get_CanResizeProperty.__wrapped__, None)
    _TransformPatternIdentifiers_Meta_.CanRotateProperty = property(get_CanRotateProperty.__wrapped__, None)
class _ValuePatternIdentifiers_Meta_(ComPtr.__class__):
    pass
class ValuePatternIdentifiers(ComPtr, metaclass=_ValuePatternIdentifiers_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Automation.IValuePatternIdentifiers
    _classid_ = 'Microsoft.UI.Xaml.Automation.ValuePatternIdentifiers'
    @winrt_classmethod
    def get_IsReadOnlyProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IValuePatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_ValueProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IValuePatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    _ValuePatternIdentifiers_Meta_.IsReadOnlyProperty = property(get_IsReadOnlyProperty.__wrapped__, None)
    _ValuePatternIdentifiers_Meta_.ValueProperty = property(get_ValueProperty.__wrapped__, None)
WindowInteractionState = Int32
WindowInteractionState_Running: WindowInteractionState = 0
WindowInteractionState_Closing: WindowInteractionState = 1
WindowInteractionState_ReadyForUserInteraction: WindowInteractionState = 2
WindowInteractionState_BlockedByModalWindow: WindowInteractionState = 3
WindowInteractionState_NotResponding: WindowInteractionState = 4
class _WindowPatternIdentifiers_Meta_(ComPtr.__class__):
    pass
class WindowPatternIdentifiers(ComPtr, metaclass=_WindowPatternIdentifiers_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Automation.IWindowPatternIdentifiers
    _classid_ = 'Microsoft.UI.Xaml.Automation.WindowPatternIdentifiers'
    @winrt_classmethod
    def get_CanMaximizeProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IWindowPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_CanMinimizeProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IWindowPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_IsModalProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IWindowPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_IsTopmostProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IWindowPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_WindowInteractionStateProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IWindowPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_WindowVisualStateProperty(cls: win32more.Microsoft.UI.Xaml.Automation.IWindowPatternIdentifiersStatics) -> win32more.Microsoft.UI.Xaml.Automation.AutomationProperty: ...
    _WindowPatternIdentifiers_Meta_.CanMaximizeProperty = property(get_CanMaximizeProperty.__wrapped__, None)
    _WindowPatternIdentifiers_Meta_.CanMinimizeProperty = property(get_CanMinimizeProperty.__wrapped__, None)
    _WindowPatternIdentifiers_Meta_.IsModalProperty = property(get_IsModalProperty.__wrapped__, None)
    _WindowPatternIdentifiers_Meta_.IsTopmostProperty = property(get_IsTopmostProperty.__wrapped__, None)
    _WindowPatternIdentifiers_Meta_.WindowInteractionStateProperty = property(get_WindowInteractionStateProperty.__wrapped__, None)
    _WindowPatternIdentifiers_Meta_.WindowVisualStateProperty = property(get_WindowVisualStateProperty.__wrapped__, None)
WindowVisualState = Int32
WindowVisualState_Normal: WindowVisualState = 0
WindowVisualState_Maximized: WindowVisualState = 1
WindowVisualState_Minimized: WindowVisualState = 2
ZoomUnit = Int32
ZoomUnit_NoAmount: ZoomUnit = 0
ZoomUnit_LargeDecrement: ZoomUnit = 1
ZoomUnit_SmallDecrement: ZoomUnit = 2
ZoomUnit_LargeIncrement: ZoomUnit = 3
ZoomUnit_SmallIncrement: ZoomUnit = 4
make_ready(__name__)
