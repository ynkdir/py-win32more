from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation.Collections
import win32more.Windows.UI.Xaml
import win32more.Windows.UI.Xaml.Automation
import win32more.Windows.UI.Xaml.Automation.Peers
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class _AnnotationPatternIdentifiers_Meta_(ComPtr.__class__):
    pass
class AnnotationPatternIdentifiers(ComPtr, metaclass=_AnnotationPatternIdentifiers_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Automation.IAnnotationPatternIdentifiers
    _classid_ = 'Windows.UI.Xaml.Automation.AnnotationPatternIdentifiers'
    @winrt_classmethod
    def get_AnnotationTypeIdProperty(cls: win32more.Windows.UI.Xaml.Automation.IAnnotationPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_AnnotationTypeNameProperty(cls: win32more.Windows.UI.Xaml.Automation.IAnnotationPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_AuthorProperty(cls: win32more.Windows.UI.Xaml.Automation.IAnnotationPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_DateTimeProperty(cls: win32more.Windows.UI.Xaml.Automation.IAnnotationPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_TargetProperty(cls: win32more.Windows.UI.Xaml.Automation.IAnnotationPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
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
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Automation.IAutomationAnnotation
    _classid_ = 'Windows.UI.Xaml.Automation.AutomationAnnotation'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Automation.AutomationAnnotation: ...
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Automation.IAutomationAnnotationFactory, type: win32more.Windows.UI.Xaml.Automation.AnnotationType) -> win32more.Windows.UI.Xaml.Automation.AutomationAnnotation: ...
    @winrt_factorymethod
    def CreateWithElementParameter(cls: win32more.Windows.UI.Xaml.Automation.IAutomationAnnotationFactory, type: win32more.Windows.UI.Xaml.Automation.AnnotationType, element: win32more.Windows.UI.Xaml.UIElement) -> win32more.Windows.UI.Xaml.Automation.AutomationAnnotation: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.UI.Xaml.Automation.IAutomationAnnotation) -> win32more.Windows.UI.Xaml.Automation.AnnotationType: ...
    @winrt_mixinmethod
    def put_Type(self: win32more.Windows.UI.Xaml.Automation.IAutomationAnnotation, value: win32more.Windows.UI.Xaml.Automation.AnnotationType) -> Void: ...
    @winrt_mixinmethod
    def get_Element(self: win32more.Windows.UI.Xaml.Automation.IAutomationAnnotation) -> win32more.Windows.UI.Xaml.UIElement: ...
    @winrt_mixinmethod
    def put_Element(self: win32more.Windows.UI.Xaml.Automation.IAutomationAnnotation, value: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_classmethod
    def get_TypeProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationAnnotationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ElementProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationAnnotationStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
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
    default_interface: win32more.Windows.UI.Xaml.Automation.IAutomationElementIdentifiers
    _classid_ = 'Windows.UI.Xaml.Automation.AutomationElementIdentifiers'
    @winrt_classmethod
    def get_IsDialogProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics8) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_HeadingLevelProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics7) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_CultureProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics6) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_IsPeripheralProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics5) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_IsDataValidForFormProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics5) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_FullDescriptionProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics5) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_DescribedByProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics5) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_FlowsToProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics5) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_FlowsFromProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics5) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_LandmarkTypeProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics4) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_LocalizedLandmarkTypeProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics4) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_PositionInSetProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics3) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_SizeOfSetProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics3) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_LevelProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics3) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_AnnotationsProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics3) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_ControlledPeersProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics2) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_AcceleratorKeyProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_AccessKeyProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_AutomationIdProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_BoundingRectangleProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_ClassNameProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_ClickablePointProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_ControlTypeProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_HasKeyboardFocusProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_HelpTextProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_IsContentElementProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_IsControlElementProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_IsEnabledProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_IsKeyboardFocusableProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_IsOffscreenProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_IsPasswordProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_IsRequiredForFormProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_ItemStatusProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_ItemTypeProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_LabeledByProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_LocalizedControlTypeProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_NameProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_OrientationProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_LiveSettingProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    _AutomationElementIdentifiers_Meta_.IsDialogProperty = property(get_IsDialogProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.HeadingLevelProperty = property(get_HeadingLevelProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.CultureProperty = property(get_CultureProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.IsPeripheralProperty = property(get_IsPeripheralProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.IsDataValidForFormProperty = property(get_IsDataValidForFormProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.FullDescriptionProperty = property(get_FullDescriptionProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.DescribedByProperty = property(get_DescribedByProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.FlowsToProperty = property(get_FlowsToProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.FlowsFromProperty = property(get_FlowsFromProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.LandmarkTypeProperty = property(get_LandmarkTypeProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.LocalizedLandmarkTypeProperty = property(get_LocalizedLandmarkTypeProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.PositionInSetProperty = property(get_PositionInSetProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.SizeOfSetProperty = property(get_SizeOfSetProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.LevelProperty = property(get_LevelProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.AnnotationsProperty = property(get_AnnotationsProperty.__wrapped__, None)
    _AutomationElementIdentifiers_Meta_.ControlledPeersProperty = property(get_ControlledPeersProperty.__wrapped__, None)
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
    default_interface: win32more.Windows.UI.Xaml.Automation.IAutomationProperties
    _classid_ = 'Windows.UI.Xaml.Automation.AutomationProperties'
    @winrt_classmethod
    def get_AutomationControlTypeProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics9) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetAutomationControlType(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics9, element: win32more.Windows.UI.Xaml.UIElement) -> win32more.Windows.UI.Xaml.Automation.Peers.AutomationControlType: ...
    @winrt_classmethod
    def SetAutomationControlType(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics9, element: win32more.Windows.UI.Xaml.UIElement, value: win32more.Windows.UI.Xaml.Automation.Peers.AutomationControlType) -> Void: ...
    @winrt_classmethod
    def get_IsDialogProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics8) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetIsDialog(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics8, element: win32more.Windows.UI.Xaml.DependencyObject) -> Boolean: ...
    @winrt_classmethod
    def SetIsDialog(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics8, element: win32more.Windows.UI.Xaml.DependencyObject, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_HeadingLevelProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics7) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetHeadingLevel(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics7, element: win32more.Windows.UI.Xaml.DependencyObject) -> win32more.Windows.UI.Xaml.Automation.Peers.AutomationHeadingLevel: ...
    @winrt_classmethod
    def SetHeadingLevel(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics7, element: win32more.Windows.UI.Xaml.DependencyObject, value: win32more.Windows.UI.Xaml.Automation.Peers.AutomationHeadingLevel) -> Void: ...
    @winrt_classmethod
    def get_CultureProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics6) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetCulture(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics6, element: win32more.Windows.UI.Xaml.DependencyObject) -> Int32: ...
    @winrt_classmethod
    def SetCulture(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics6, element: win32more.Windows.UI.Xaml.DependencyObject, value: Int32) -> Void: ...
    @winrt_classmethod
    def get_IsPeripheralProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics5) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetIsPeripheral(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics5, element: win32more.Windows.UI.Xaml.DependencyObject) -> Boolean: ...
    @winrt_classmethod
    def SetIsPeripheral(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics5, element: win32more.Windows.UI.Xaml.DependencyObject, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_IsDataValidForFormProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics5) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetIsDataValidForForm(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics5, element: win32more.Windows.UI.Xaml.DependencyObject) -> Boolean: ...
    @winrt_classmethod
    def SetIsDataValidForForm(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics5, element: win32more.Windows.UI.Xaml.DependencyObject, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_FullDescriptionProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics5) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetFullDescription(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics5, element: win32more.Windows.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_classmethod
    def SetFullDescription(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics5, element: win32more.Windows.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_LocalizedControlTypeProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics5) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetLocalizedControlType(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics5, element: win32more.Windows.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_classmethod
    def SetLocalizedControlType(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics5, element: win32more.Windows.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_DescribedByProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics5) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetDescribedBy(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics5, element: win32more.Windows.UI.Xaml.DependencyObject) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.DependencyObject]: ...
    @winrt_classmethod
    def get_FlowsToProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics5) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetFlowsTo(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics5, element: win32more.Windows.UI.Xaml.DependencyObject) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.DependencyObject]: ...
    @winrt_classmethod
    def get_FlowsFromProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics5) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetFlowsFrom(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics5, element: win32more.Windows.UI.Xaml.DependencyObject) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.DependencyObject]: ...
    @winrt_classmethod
    def get_LandmarkTypeProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics4) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetLandmarkType(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics4, element: win32more.Windows.UI.Xaml.DependencyObject) -> win32more.Windows.UI.Xaml.Automation.Peers.AutomationLandmarkType: ...
    @winrt_classmethod
    def SetLandmarkType(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics4, element: win32more.Windows.UI.Xaml.DependencyObject, value: win32more.Windows.UI.Xaml.Automation.Peers.AutomationLandmarkType) -> Void: ...
    @winrt_classmethod
    def get_LocalizedLandmarkTypeProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics4) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetLocalizedLandmarkType(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics4, element: win32more.Windows.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_classmethod
    def SetLocalizedLandmarkType(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics4, element: win32more.Windows.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_PositionInSetProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics3) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetPositionInSet(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics3, element: win32more.Windows.UI.Xaml.DependencyObject) -> Int32: ...
    @winrt_classmethod
    def SetPositionInSet(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics3, element: win32more.Windows.UI.Xaml.DependencyObject, value: Int32) -> Void: ...
    @winrt_classmethod
    def get_SizeOfSetProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics3) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetSizeOfSet(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics3, element: win32more.Windows.UI.Xaml.DependencyObject) -> Int32: ...
    @winrt_classmethod
    def SetSizeOfSet(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics3, element: win32more.Windows.UI.Xaml.DependencyObject, value: Int32) -> Void: ...
    @winrt_classmethod
    def get_LevelProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics3) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetLevel(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics3, element: win32more.Windows.UI.Xaml.DependencyObject) -> Int32: ...
    @winrt_classmethod
    def SetLevel(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics3, element: win32more.Windows.UI.Xaml.DependencyObject, value: Int32) -> Void: ...
    @winrt_classmethod
    def get_AnnotationsProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics3) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetAnnotations(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics3, element: win32more.Windows.UI.Xaml.DependencyObject) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Automation.AutomationAnnotation]: ...
    @winrt_classmethod
    def get_AccessibilityViewProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics2) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetAccessibilityView(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics2, element: win32more.Windows.UI.Xaml.DependencyObject) -> win32more.Windows.UI.Xaml.Automation.Peers.AccessibilityView: ...
    @winrt_classmethod
    def SetAccessibilityView(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics2, element: win32more.Windows.UI.Xaml.DependencyObject, value: win32more.Windows.UI.Xaml.Automation.Peers.AccessibilityView) -> Void: ...
    @winrt_classmethod
    def get_ControlledPeersProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics2) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetControlledPeers(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics2, element: win32more.Windows.UI.Xaml.DependencyObject) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.UIElement]: ...
    @winrt_classmethod
    def get_AcceleratorKeyProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetAcceleratorKey(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Windows.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_classmethod
    def SetAcceleratorKey(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Windows.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_AccessKeyProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetAccessKey(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Windows.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_classmethod
    def SetAccessKey(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Windows.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_AutomationIdProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetAutomationId(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Windows.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_classmethod
    def SetAutomationId(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Windows.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_HelpTextProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetHelpText(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Windows.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_classmethod
    def SetHelpText(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Windows.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_IsRequiredForFormProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetIsRequiredForForm(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Windows.UI.Xaml.DependencyObject) -> Boolean: ...
    @winrt_classmethod
    def SetIsRequiredForForm(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Windows.UI.Xaml.DependencyObject, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_ItemStatusProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetItemStatus(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Windows.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_classmethod
    def SetItemStatus(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Windows.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_ItemTypeProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetItemType(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Windows.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_classmethod
    def SetItemType(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Windows.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_LabeledByProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetLabeledBy(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Windows.UI.Xaml.DependencyObject) -> win32more.Windows.UI.Xaml.UIElement: ...
    @winrt_classmethod
    def SetLabeledBy(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Windows.UI.Xaml.DependencyObject, value: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_classmethod
    def get_NameProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetName(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Windows.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_classmethod
    def SetName(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Windows.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_LiveSettingProperty(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetLiveSetting(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Windows.UI.Xaml.DependencyObject) -> win32more.Windows.UI.Xaml.Automation.Peers.AutomationLiveSetting: ...
    @winrt_classmethod
    def SetLiveSetting(cls: win32more.Windows.UI.Xaml.Automation.IAutomationPropertiesStatics, element: win32more.Windows.UI.Xaml.DependencyObject, value: win32more.Windows.UI.Xaml.Automation.Peers.AutomationLiveSetting) -> Void: ...
    _AutomationProperties_Meta_.AutomationControlTypeProperty = property(get_AutomationControlTypeProperty.__wrapped__, None)
    _AutomationProperties_Meta_.IsDialogProperty = property(get_IsDialogProperty.__wrapped__, None)
    _AutomationProperties_Meta_.HeadingLevelProperty = property(get_HeadingLevelProperty.__wrapped__, None)
    _AutomationProperties_Meta_.CultureProperty = property(get_CultureProperty.__wrapped__, None)
    _AutomationProperties_Meta_.IsPeripheralProperty = property(get_IsPeripheralProperty.__wrapped__, None)
    _AutomationProperties_Meta_.IsDataValidForFormProperty = property(get_IsDataValidForFormProperty.__wrapped__, None)
    _AutomationProperties_Meta_.FullDescriptionProperty = property(get_FullDescriptionProperty.__wrapped__, None)
    _AutomationProperties_Meta_.LocalizedControlTypeProperty = property(get_LocalizedControlTypeProperty.__wrapped__, None)
    _AutomationProperties_Meta_.DescribedByProperty = property(get_DescribedByProperty.__wrapped__, None)
    _AutomationProperties_Meta_.FlowsToProperty = property(get_FlowsToProperty.__wrapped__, None)
    _AutomationProperties_Meta_.FlowsFromProperty = property(get_FlowsFromProperty.__wrapped__, None)
    _AutomationProperties_Meta_.LandmarkTypeProperty = property(get_LandmarkTypeProperty.__wrapped__, None)
    _AutomationProperties_Meta_.LocalizedLandmarkTypeProperty = property(get_LocalizedLandmarkTypeProperty.__wrapped__, None)
    _AutomationProperties_Meta_.PositionInSetProperty = property(get_PositionInSetProperty.__wrapped__, None)
    _AutomationProperties_Meta_.SizeOfSetProperty = property(get_SizeOfSetProperty.__wrapped__, None)
    _AutomationProperties_Meta_.LevelProperty = property(get_LevelProperty.__wrapped__, None)
    _AutomationProperties_Meta_.AnnotationsProperty = property(get_AnnotationsProperty.__wrapped__, None)
    _AutomationProperties_Meta_.AccessibilityViewProperty = property(get_AccessibilityViewProperty.__wrapped__, None)
    _AutomationProperties_Meta_.ControlledPeersProperty = property(get_ControlledPeersProperty.__wrapped__, None)
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
class AutomationProperty(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Automation.IAutomationProperty
    _classid_ = 'Windows.UI.Xaml.Automation.AutomationProperty'
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
    default_interface: win32more.Windows.UI.Xaml.Automation.IDockPatternIdentifiers
    _classid_ = 'Windows.UI.Xaml.Automation.DockPatternIdentifiers'
    @winrt_classmethod
    def get_DockPositionProperty(cls: win32more.Windows.UI.Xaml.Automation.IDockPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
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
    default_interface: win32more.Windows.UI.Xaml.Automation.IDragPatternIdentifiers
    _classid_ = 'Windows.UI.Xaml.Automation.DragPatternIdentifiers'
    @winrt_classmethod
    def get_DropEffectProperty(cls: win32more.Windows.UI.Xaml.Automation.IDragPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_DropEffectsProperty(cls: win32more.Windows.UI.Xaml.Automation.IDragPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_GrabbedItemsProperty(cls: win32more.Windows.UI.Xaml.Automation.IDragPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_IsGrabbedProperty(cls: win32more.Windows.UI.Xaml.Automation.IDragPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    _DragPatternIdentifiers_Meta_.DropEffectProperty = property(get_DropEffectProperty.__wrapped__, None)
    _DragPatternIdentifiers_Meta_.DropEffectsProperty = property(get_DropEffectsProperty.__wrapped__, None)
    _DragPatternIdentifiers_Meta_.GrabbedItemsProperty = property(get_GrabbedItemsProperty.__wrapped__, None)
    _DragPatternIdentifiers_Meta_.IsGrabbedProperty = property(get_IsGrabbedProperty.__wrapped__, None)
class _DropTargetPatternIdentifiers_Meta_(ComPtr.__class__):
    pass
class DropTargetPatternIdentifiers(ComPtr, metaclass=_DropTargetPatternIdentifiers_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Automation.IDropTargetPatternIdentifiers
    _classid_ = 'Windows.UI.Xaml.Automation.DropTargetPatternIdentifiers'
    @winrt_classmethod
    def get_DropTargetEffectProperty(cls: win32more.Windows.UI.Xaml.Automation.IDropTargetPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_DropTargetEffectsProperty(cls: win32more.Windows.UI.Xaml.Automation.IDropTargetPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    _DropTargetPatternIdentifiers_Meta_.DropTargetEffectProperty = property(get_DropTargetEffectProperty.__wrapped__, None)
    _DropTargetPatternIdentifiers_Meta_.DropTargetEffectsProperty = property(get_DropTargetEffectsProperty.__wrapped__, None)
class _ExpandCollapsePatternIdentifiers_Meta_(ComPtr.__class__):
    pass
class ExpandCollapsePatternIdentifiers(ComPtr, metaclass=_ExpandCollapsePatternIdentifiers_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Automation.IExpandCollapsePatternIdentifiers
    _classid_ = 'Windows.UI.Xaml.Automation.ExpandCollapsePatternIdentifiers'
    @winrt_classmethod
    def get_ExpandCollapseStateProperty(cls: win32more.Windows.UI.Xaml.Automation.IExpandCollapsePatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
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
    default_interface: win32more.Windows.UI.Xaml.Automation.IGridItemPatternIdentifiers
    _classid_ = 'Windows.UI.Xaml.Automation.GridItemPatternIdentifiers'
    @winrt_classmethod
    def get_ColumnProperty(cls: win32more.Windows.UI.Xaml.Automation.IGridItemPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_ColumnSpanProperty(cls: win32more.Windows.UI.Xaml.Automation.IGridItemPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_ContainingGridProperty(cls: win32more.Windows.UI.Xaml.Automation.IGridItemPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_RowProperty(cls: win32more.Windows.UI.Xaml.Automation.IGridItemPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_RowSpanProperty(cls: win32more.Windows.UI.Xaml.Automation.IGridItemPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    _GridItemPatternIdentifiers_Meta_.ColumnProperty = property(get_ColumnProperty.__wrapped__, None)
    _GridItemPatternIdentifiers_Meta_.ColumnSpanProperty = property(get_ColumnSpanProperty.__wrapped__, None)
    _GridItemPatternIdentifiers_Meta_.ContainingGridProperty = property(get_ContainingGridProperty.__wrapped__, None)
    _GridItemPatternIdentifiers_Meta_.RowProperty = property(get_RowProperty.__wrapped__, None)
    _GridItemPatternIdentifiers_Meta_.RowSpanProperty = property(get_RowSpanProperty.__wrapped__, None)
class _GridPatternIdentifiers_Meta_(ComPtr.__class__):
    pass
class GridPatternIdentifiers(ComPtr, metaclass=_GridPatternIdentifiers_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Automation.IGridPatternIdentifiers
    _classid_ = 'Windows.UI.Xaml.Automation.GridPatternIdentifiers'
    @winrt_classmethod
    def get_ColumnCountProperty(cls: win32more.Windows.UI.Xaml.Automation.IGridPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_RowCountProperty(cls: win32more.Windows.UI.Xaml.Automation.IGridPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    _GridPatternIdentifiers_Meta_.ColumnCountProperty = property(get_ColumnCountProperty.__wrapped__, None)
    _GridPatternIdentifiers_Meta_.RowCountProperty = property(get_RowCountProperty.__wrapped__, None)
class IAnnotationPatternIdentifiers(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IAnnotationPatternIdentifiers'
    _iid_ = Guid('{d475a0c1-48b2-4e40-a6cf-3dc4b638c0de}')
class IAnnotationPatternIdentifiersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IAnnotationPatternIdentifiersStatics'
    _iid_ = Guid('{e0e3a35d-d167-46dc-95ab-330af61aebb5}')
    @winrt_commethod(6)
    def get_AnnotationTypeIdProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_AnnotationTypeNameProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(8)
    def get_AuthorProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(9)
    def get_DateTimeProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(10)
    def get_TargetProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    AnnotationTypeIdProperty = property(get_AnnotationTypeIdProperty, None)
    AnnotationTypeNameProperty = property(get_AnnotationTypeNameProperty, None)
    AuthorProperty = property(get_AuthorProperty, None)
    DateTimeProperty = property(get_DateTimeProperty, None)
    TargetProperty = property(get_TargetProperty, None)
class IAutomationAnnotation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IAutomationAnnotation'
    _iid_ = Guid('{fb3c30ca-03d8-4618-91bf-e4d84f4af318}')
    @winrt_commethod(6)
    def get_Type(self) -> win32more.Windows.UI.Xaml.Automation.AnnotationType: ...
    @winrt_commethod(7)
    def put_Type(self, value: win32more.Windows.UI.Xaml.Automation.AnnotationType) -> Void: ...
    @winrt_commethod(8)
    def get_Element(self) -> win32more.Windows.UI.Xaml.UIElement: ...
    @winrt_commethod(9)
    def put_Element(self, value: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
    Type = property(get_Type, put_Type)
    Element = property(get_Element, put_Element)
class IAutomationAnnotationFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IAutomationAnnotationFactory'
    _iid_ = Guid('{4906fa52-ddc0-4e69-b76b-019d928d822f}')
    @winrt_commethod(6)
    def CreateInstance(self, type: win32more.Windows.UI.Xaml.Automation.AnnotationType) -> win32more.Windows.UI.Xaml.Automation.AutomationAnnotation: ...
    @winrt_commethod(7)
    def CreateWithElementParameter(self, type: win32more.Windows.UI.Xaml.Automation.AnnotationType, element: win32more.Windows.UI.Xaml.UIElement) -> win32more.Windows.UI.Xaml.Automation.AutomationAnnotation: ...
class IAutomationAnnotationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IAutomationAnnotationStatics'
    _iid_ = Guid('{e503eab7-4ee5-48cb-b5b8-bbcd46c9d1da}')
    @winrt_commethod(6)
    def get_TypeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_ElementProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    TypeProperty = property(get_TypeProperty, None)
    ElementProperty = property(get_ElementProperty, None)
class IAutomationElementIdentifiers(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IAutomationElementIdentifiers'
    _iid_ = Guid('{e68a63cf-4345-4e2d-8a6a-49cce1fa2dcc}')
class IAutomationElementIdentifiersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics'
    _iid_ = Guid('{4549399f-8340-4d67-b9bf-8c2ac6a0773a}')
    @winrt_commethod(6)
    def get_AcceleratorKeyProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_AccessKeyProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(8)
    def get_AutomationIdProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(9)
    def get_BoundingRectangleProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(10)
    def get_ClassNameProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(11)
    def get_ClickablePointProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(12)
    def get_ControlTypeProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(13)
    def get_HasKeyboardFocusProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(14)
    def get_HelpTextProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(15)
    def get_IsContentElementProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(16)
    def get_IsControlElementProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(17)
    def get_IsEnabledProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(18)
    def get_IsKeyboardFocusableProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(19)
    def get_IsOffscreenProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(20)
    def get_IsPasswordProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(21)
    def get_IsRequiredForFormProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(22)
    def get_ItemStatusProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(23)
    def get_ItemTypeProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(24)
    def get_LabeledByProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(25)
    def get_LocalizedControlTypeProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(26)
    def get_NameProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(27)
    def get_OrientationProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(28)
    def get_LiveSettingProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
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
class IAutomationElementIdentifiersStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics2'
    _iid_ = Guid('{b5cbb1e2-d55f-46a9-9eda-1a4742515dc3}')
    @winrt_commethod(6)
    def get_ControlledPeersProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    ControlledPeersProperty = property(get_ControlledPeersProperty, None)
class IAutomationElementIdentifiersStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics3'
    _iid_ = Guid('{0f5cbebd-b3eb-4083-adc7-0c2f39bb3543}')
    @winrt_commethod(6)
    def get_PositionInSetProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_SizeOfSetProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(8)
    def get_LevelProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(9)
    def get_AnnotationsProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    PositionInSetProperty = property(get_PositionInSetProperty, None)
    SizeOfSetProperty = property(get_SizeOfSetProperty, None)
    LevelProperty = property(get_LevelProperty, None)
    AnnotationsProperty = property(get_AnnotationsProperty, None)
class IAutomationElementIdentifiersStatics4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics4'
    _iid_ = Guid('{5af51f75-5913-4d78-b330-a6f50b73ed9b}')
    @winrt_commethod(6)
    def get_LandmarkTypeProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_LocalizedLandmarkTypeProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    LandmarkTypeProperty = property(get_LandmarkTypeProperty, None)
    LocalizedLandmarkTypeProperty = property(get_LocalizedLandmarkTypeProperty, None)
class IAutomationElementIdentifiersStatics5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics5'
    _iid_ = Guid('{986a8206-de59-42f9-a1e7-62b8af9e756d}')
    @winrt_commethod(6)
    def get_IsPeripheralProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_IsDataValidForFormProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(8)
    def get_FullDescriptionProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(9)
    def get_DescribedByProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(10)
    def get_FlowsToProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(11)
    def get_FlowsFromProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    IsPeripheralProperty = property(get_IsPeripheralProperty, None)
    IsDataValidForFormProperty = property(get_IsDataValidForFormProperty, None)
    FullDescriptionProperty = property(get_FullDescriptionProperty, None)
    DescribedByProperty = property(get_DescribedByProperty, None)
    FlowsToProperty = property(get_FlowsToProperty, None)
    FlowsFromProperty = property(get_FlowsFromProperty, None)
class IAutomationElementIdentifiersStatics6(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics6'
    _iid_ = Guid('{de52b00d-8328-4eae-8035-f8db99c8bac4}')
    @winrt_commethod(6)
    def get_CultureProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    CultureProperty = property(get_CultureProperty, None)
class IAutomationElementIdentifiersStatics7(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics7'
    _iid_ = Guid('{00f1abb2-742c-446a-a8f6-1672b10d2874}')
    @winrt_commethod(6)
    def get_HeadingLevelProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    HeadingLevelProperty = property(get_HeadingLevelProperty, None)
class IAutomationElementIdentifiersStatics8(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics8'
    _iid_ = Guid('{8517b060-806c-5dc5-bc41-891bb5a47adf}')
    @winrt_commethod(6)
    def get_IsDialogProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    IsDialogProperty = property(get_IsDialogProperty, None)
class IAutomationProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IAutomationProperties'
    _iid_ = Guid('{68d7232c-e622-48e9-af0b-1ffa33cc5cba}')
class IAutomationPropertiesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IAutomationPropertiesStatics'
    _iid_ = Guid('{b618fd7b-32d0-4970-9c42-7c039ac7be78}')
    @winrt_commethod(6)
    def get_AcceleratorKeyProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def GetAcceleratorKey(self, element: win32more.Windows.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_commethod(8)
    def SetAcceleratorKey(self, element: win32more.Windows.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_AccessKeyProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def GetAccessKey(self, element: win32more.Windows.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_commethod(11)
    def SetAccessKey(self, element: win32more.Windows.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_AutomationIdProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def GetAutomationId(self, element: win32more.Windows.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_commethod(14)
    def SetAutomationId(self, element: win32more.Windows.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_commethod(15)
    def get_HelpTextProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(16)
    def GetHelpText(self, element: win32more.Windows.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_commethod(17)
    def SetHelpText(self, element: win32more.Windows.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_commethod(18)
    def get_IsRequiredForFormProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(19)
    def GetIsRequiredForForm(self, element: win32more.Windows.UI.Xaml.DependencyObject) -> Boolean: ...
    @winrt_commethod(20)
    def SetIsRequiredForForm(self, element: win32more.Windows.UI.Xaml.DependencyObject, value: Boolean) -> Void: ...
    @winrt_commethod(21)
    def get_ItemStatusProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(22)
    def GetItemStatus(self, element: win32more.Windows.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_commethod(23)
    def SetItemStatus(self, element: win32more.Windows.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_commethod(24)
    def get_ItemTypeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(25)
    def GetItemType(self, element: win32more.Windows.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_commethod(26)
    def SetItemType(self, element: win32more.Windows.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_commethod(27)
    def get_LabeledByProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(28)
    def GetLabeledBy(self, element: win32more.Windows.UI.Xaml.DependencyObject) -> win32more.Windows.UI.Xaml.UIElement: ...
    @winrt_commethod(29)
    def SetLabeledBy(self, element: win32more.Windows.UI.Xaml.DependencyObject, value: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(30)
    def get_NameProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(31)
    def GetName(self, element: win32more.Windows.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_commethod(32)
    def SetName(self, element: win32more.Windows.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_commethod(33)
    def get_LiveSettingProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(34)
    def GetLiveSetting(self, element: win32more.Windows.UI.Xaml.DependencyObject) -> win32more.Windows.UI.Xaml.Automation.Peers.AutomationLiveSetting: ...
    @winrt_commethod(35)
    def SetLiveSetting(self, element: win32more.Windows.UI.Xaml.DependencyObject, value: win32more.Windows.UI.Xaml.Automation.Peers.AutomationLiveSetting) -> Void: ...
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
class IAutomationPropertiesStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IAutomationPropertiesStatics2'
    _iid_ = Guid('{3976547f-7089-4801-8f1d-aab78090d1a0}')
    @winrt_commethod(6)
    def get_AccessibilityViewProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def GetAccessibilityView(self, element: win32more.Windows.UI.Xaml.DependencyObject) -> win32more.Windows.UI.Xaml.Automation.Peers.AccessibilityView: ...
    @winrt_commethod(8)
    def SetAccessibilityView(self, element: win32more.Windows.UI.Xaml.DependencyObject, value: win32more.Windows.UI.Xaml.Automation.Peers.AccessibilityView) -> Void: ...
    @winrt_commethod(9)
    def get_ControlledPeersProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def GetControlledPeers(self, element: win32more.Windows.UI.Xaml.DependencyObject) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.UIElement]: ...
    AccessibilityViewProperty = property(get_AccessibilityViewProperty, None)
    ControlledPeersProperty = property(get_ControlledPeersProperty, None)
class IAutomationPropertiesStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IAutomationPropertiesStatics3'
    _iid_ = Guid('{7b75d735-5cb1-42ad-9b57-5faba8c1867f}')
    @winrt_commethod(6)
    def get_PositionInSetProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def GetPositionInSet(self, element: win32more.Windows.UI.Xaml.DependencyObject) -> Int32: ...
    @winrt_commethod(8)
    def SetPositionInSet(self, element: win32more.Windows.UI.Xaml.DependencyObject, value: Int32) -> Void: ...
    @winrt_commethod(9)
    def get_SizeOfSetProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def GetSizeOfSet(self, element: win32more.Windows.UI.Xaml.DependencyObject) -> Int32: ...
    @winrt_commethod(11)
    def SetSizeOfSet(self, element: win32more.Windows.UI.Xaml.DependencyObject, value: Int32) -> Void: ...
    @winrt_commethod(12)
    def get_LevelProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def GetLevel(self, element: win32more.Windows.UI.Xaml.DependencyObject) -> Int32: ...
    @winrt_commethod(14)
    def SetLevel(self, element: win32more.Windows.UI.Xaml.DependencyObject, value: Int32) -> Void: ...
    @winrt_commethod(15)
    def get_AnnotationsProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(16)
    def GetAnnotations(self, element: win32more.Windows.UI.Xaml.DependencyObject) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Automation.AutomationAnnotation]: ...
    PositionInSetProperty = property(get_PositionInSetProperty, None)
    SizeOfSetProperty = property(get_SizeOfSetProperty, None)
    LevelProperty = property(get_LevelProperty, None)
    AnnotationsProperty = property(get_AnnotationsProperty, None)
class IAutomationPropertiesStatics4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IAutomationPropertiesStatics4'
    _iid_ = Guid('{f7d62655-311a-4b7c-a131-524e89cd3cf9}')
    @winrt_commethod(6)
    def get_LandmarkTypeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def GetLandmarkType(self, element: win32more.Windows.UI.Xaml.DependencyObject) -> win32more.Windows.UI.Xaml.Automation.Peers.AutomationLandmarkType: ...
    @winrt_commethod(8)
    def SetLandmarkType(self, element: win32more.Windows.UI.Xaml.DependencyObject, value: win32more.Windows.UI.Xaml.Automation.Peers.AutomationLandmarkType) -> Void: ...
    @winrt_commethod(9)
    def get_LocalizedLandmarkTypeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def GetLocalizedLandmarkType(self, element: win32more.Windows.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_commethod(11)
    def SetLocalizedLandmarkType(self, element: win32more.Windows.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    LandmarkTypeProperty = property(get_LandmarkTypeProperty, None)
    LocalizedLandmarkTypeProperty = property(get_LocalizedLandmarkTypeProperty, None)
class IAutomationPropertiesStatics5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IAutomationPropertiesStatics5'
    _iid_ = Guid('{0be35b26-c8f9-41a2-b4db-e6a7a32b0c34}')
    @winrt_commethod(6)
    def get_IsPeripheralProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def GetIsPeripheral(self, element: win32more.Windows.UI.Xaml.DependencyObject) -> Boolean: ...
    @winrt_commethod(8)
    def SetIsPeripheral(self, element: win32more.Windows.UI.Xaml.DependencyObject, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_IsDataValidForFormProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def GetIsDataValidForForm(self, element: win32more.Windows.UI.Xaml.DependencyObject) -> Boolean: ...
    @winrt_commethod(11)
    def SetIsDataValidForForm(self, element: win32more.Windows.UI.Xaml.DependencyObject, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_FullDescriptionProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def GetFullDescription(self, element: win32more.Windows.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_commethod(14)
    def SetFullDescription(self, element: win32more.Windows.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_commethod(15)
    def get_LocalizedControlTypeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(16)
    def GetLocalizedControlType(self, element: win32more.Windows.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_commethod(17)
    def SetLocalizedControlType(self, element: win32more.Windows.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_commethod(18)
    def get_DescribedByProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(19)
    def GetDescribedBy(self, element: win32more.Windows.UI.Xaml.DependencyObject) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.DependencyObject]: ...
    @winrt_commethod(20)
    def get_FlowsToProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(21)
    def GetFlowsTo(self, element: win32more.Windows.UI.Xaml.DependencyObject) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.DependencyObject]: ...
    @winrt_commethod(22)
    def get_FlowsFromProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(23)
    def GetFlowsFrom(self, element: win32more.Windows.UI.Xaml.DependencyObject) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.DependencyObject]: ...
    IsPeripheralProperty = property(get_IsPeripheralProperty, None)
    IsDataValidForFormProperty = property(get_IsDataValidForFormProperty, None)
    FullDescriptionProperty = property(get_FullDescriptionProperty, None)
    LocalizedControlTypeProperty = property(get_LocalizedControlTypeProperty, None)
    DescribedByProperty = property(get_DescribedByProperty, None)
    FlowsToProperty = property(get_FlowsToProperty, None)
    FlowsFromProperty = property(get_FlowsFromProperty, None)
class IAutomationPropertiesStatics6(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IAutomationPropertiesStatics6'
    _iid_ = Guid('{c61e030f-eb49-4e5d-b012-4c1c96c3901b}')
    @winrt_commethod(6)
    def get_CultureProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def GetCulture(self, element: win32more.Windows.UI.Xaml.DependencyObject) -> Int32: ...
    @winrt_commethod(8)
    def SetCulture(self, element: win32more.Windows.UI.Xaml.DependencyObject, value: Int32) -> Void: ...
    CultureProperty = property(get_CultureProperty, None)
class IAutomationPropertiesStatics7(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IAutomationPropertiesStatics7'
    _iid_ = Guid('{f7e98bf3-8f91-4068-a4ad-b7b402d10a2c}')
    @winrt_commethod(6)
    def get_HeadingLevelProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def GetHeadingLevel(self, element: win32more.Windows.UI.Xaml.DependencyObject) -> win32more.Windows.UI.Xaml.Automation.Peers.AutomationHeadingLevel: ...
    @winrt_commethod(8)
    def SetHeadingLevel(self, element: win32more.Windows.UI.Xaml.DependencyObject, value: win32more.Windows.UI.Xaml.Automation.Peers.AutomationHeadingLevel) -> Void: ...
    HeadingLevelProperty = property(get_HeadingLevelProperty, None)
class IAutomationPropertiesStatics8(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IAutomationPropertiesStatics8'
    _iid_ = Guid('{432eca20-171a-560d-8524-3e651d3ad6ca}')
    @winrt_commethod(6)
    def get_IsDialogProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def GetIsDialog(self, element: win32more.Windows.UI.Xaml.DependencyObject) -> Boolean: ...
    @winrt_commethod(8)
    def SetIsDialog(self, element: win32more.Windows.UI.Xaml.DependencyObject, value: Boolean) -> Void: ...
    IsDialogProperty = property(get_IsDialogProperty, None)
class IAutomationPropertiesStatics9(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IAutomationPropertiesStatics9'
    _iid_ = Guid('{2f20b1d1-87b2-5562-8077-da593edafd2d}')
    @winrt_commethod(6)
    def get_AutomationControlTypeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def GetAutomationControlType(self, element: win32more.Windows.UI.Xaml.UIElement) -> win32more.Windows.UI.Xaml.Automation.Peers.AutomationControlType: ...
    @winrt_commethod(8)
    def SetAutomationControlType(self, element: win32more.Windows.UI.Xaml.UIElement, value: win32more.Windows.UI.Xaml.Automation.Peers.AutomationControlType) -> Void: ...
    AutomationControlTypeProperty = property(get_AutomationControlTypeProperty, None)
class IAutomationProperty(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IAutomationProperty'
    _iid_ = Guid('{b627195b-3227-4e16-9534-ddece30ddb46}')
class IDockPatternIdentifiers(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IDockPatternIdentifiers'
    _iid_ = Guid('{ccd7f4e6-e4f9-47ff-bde7-378b11f78e09}')
class IDockPatternIdentifiersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IDockPatternIdentifiersStatics'
    _iid_ = Guid('{2b87245c-ed80-4fe5-8eb4-708a39c841e5}')
    @winrt_commethod(6)
    def get_DockPositionProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    DockPositionProperty = property(get_DockPositionProperty, None)
class IDragPatternIdentifiers(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IDragPatternIdentifiers'
    _iid_ = Guid('{6266e985-4d07-4e80-82eb-8f96690a1a0c}')
class IDragPatternIdentifiersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IDragPatternIdentifiersStatics'
    _iid_ = Guid('{2a05379d-1755-4082-9d90-46f1411d7986}')
    @winrt_commethod(6)
    def get_DropEffectProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_DropEffectsProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(8)
    def get_GrabbedItemsProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(9)
    def get_IsGrabbedProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    DropEffectProperty = property(get_DropEffectProperty, None)
    DropEffectsProperty = property(get_DropEffectsProperty, None)
    GrabbedItemsProperty = property(get_GrabbedItemsProperty, None)
    IsGrabbedProperty = property(get_IsGrabbedProperty, None)
class IDropTargetPatternIdentifiers(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IDropTargetPatternIdentifiers'
    _iid_ = Guid('{11865133-a6fe-4634-bd18-0ef612b7b208}')
class IDropTargetPatternIdentifiersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IDropTargetPatternIdentifiersStatics'
    _iid_ = Guid('{1b693304-89fb-4b0a-9452-ca2c66aaf9f3}')
    @winrt_commethod(6)
    def get_DropTargetEffectProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_DropTargetEffectsProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    DropTargetEffectProperty = property(get_DropTargetEffectProperty, None)
    DropTargetEffectsProperty = property(get_DropTargetEffectsProperty, None)
class IExpandCollapsePatternIdentifiers(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IExpandCollapsePatternIdentifiers'
    _iid_ = Guid('{b006bac0-751b-4d55-92cb-613ec1bdf5d0}')
class IExpandCollapsePatternIdentifiersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IExpandCollapsePatternIdentifiersStatics'
    _iid_ = Guid('{d7816fd4-6ee0-4f38-8e14-56ef21adacfd}')
    @winrt_commethod(6)
    def get_ExpandCollapseStateProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    ExpandCollapseStateProperty = property(get_ExpandCollapseStateProperty, None)
class IGridItemPatternIdentifiers(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IGridItemPatternIdentifiers'
    _iid_ = Guid('{757744f1-3285-4fb1-803b-2545bd431599}')
class IGridItemPatternIdentifiersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IGridItemPatternIdentifiersStatics'
    _iid_ = Guid('{217d2402-5e46-4d61-8794-b8ee8e774714}')
    @winrt_commethod(6)
    def get_ColumnProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_ColumnSpanProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(8)
    def get_ContainingGridProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(9)
    def get_RowProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(10)
    def get_RowSpanProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    ColumnProperty = property(get_ColumnProperty, None)
    ColumnSpanProperty = property(get_ColumnSpanProperty, None)
    ContainingGridProperty = property(get_ContainingGridProperty, None)
    RowProperty = property(get_RowProperty, None)
    RowSpanProperty = property(get_RowSpanProperty, None)
class IGridPatternIdentifiers(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IGridPatternIdentifiers'
    _iid_ = Guid('{c902980f-96c5-450c-9044-7e52c24f9e94}')
class IGridPatternIdentifiersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IGridPatternIdentifiersStatics'
    _iid_ = Guid('{7bc452f3-a181-4137-8de9-1f9b1a8320ed}')
    @winrt_commethod(6)
    def get_ColumnCountProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_RowCountProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    ColumnCountProperty = property(get_ColumnCountProperty, None)
    RowCountProperty = property(get_RowCountProperty, None)
class IMultipleViewPatternIdentifiers(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IMultipleViewPatternIdentifiers'
    _iid_ = Guid('{5d5cd3b8-1e12-488b-b0ea-5e6cb89816e1}')
class IMultipleViewPatternIdentifiersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IMultipleViewPatternIdentifiersStatics'
    _iid_ = Guid('{a9cfa66f-6b84-4d71-9e48-d764d3bcda8e}')
    @winrt_commethod(6)
    def get_CurrentViewProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_SupportedViewsProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    CurrentViewProperty = property(get_CurrentViewProperty, None)
    SupportedViewsProperty = property(get_SupportedViewsProperty, None)
class IRangeValuePatternIdentifiers(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IRangeValuePatternIdentifiers'
    _iid_ = Guid('{f8760f45-33c9-467d-bc9e-d1515263ace1}')
class IRangeValuePatternIdentifiersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IRangeValuePatternIdentifiersStatics'
    _iid_ = Guid('{ce23450f-1c27-457f-b815-7a5e46863dbb}')
    @winrt_commethod(6)
    def get_IsReadOnlyProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_LargeChangeProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(8)
    def get_MaximumProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(9)
    def get_MinimumProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(10)
    def get_SmallChangeProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(11)
    def get_ValueProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    IsReadOnlyProperty = property(get_IsReadOnlyProperty, None)
    LargeChangeProperty = property(get_LargeChangeProperty, None)
    MaximumProperty = property(get_MaximumProperty, None)
    MinimumProperty = property(get_MinimumProperty, None)
    SmallChangeProperty = property(get_SmallChangeProperty, None)
    ValueProperty = property(get_ValueProperty, None)
class IScrollPatternIdentifiers(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IScrollPatternIdentifiers'
    _iid_ = Guid('{366b1003-425c-4951-ae83-d521e73bc696}')
class IScrollPatternIdentifiersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IScrollPatternIdentifiersStatics'
    _iid_ = Guid('{4bf8e0a1-fb7f-4fa4-83b3-cfaeb103a685}')
    @winrt_commethod(6)
    def get_HorizontallyScrollableProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_HorizontalScrollPercentProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(8)
    def get_HorizontalViewSizeProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(9)
    def get_NoScroll(self) -> Double: ...
    @winrt_commethod(10)
    def get_VerticallyScrollableProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(11)
    def get_VerticalScrollPercentProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(12)
    def get_VerticalViewSizeProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    HorizontallyScrollableProperty = property(get_HorizontallyScrollableProperty, None)
    HorizontalScrollPercentProperty = property(get_HorizontalScrollPercentProperty, None)
    HorizontalViewSizeProperty = property(get_HorizontalViewSizeProperty, None)
    NoScroll = property(get_NoScroll, None)
    VerticallyScrollableProperty = property(get_VerticallyScrollableProperty, None)
    VerticalScrollPercentProperty = property(get_VerticalScrollPercentProperty, None)
    VerticalViewSizeProperty = property(get_VerticalViewSizeProperty, None)
class ISelectionItemPatternIdentifiers(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.ISelectionItemPatternIdentifiers'
    _iid_ = Guid('{2dafa41a-3ef8-4bb5-a02b-3ee1b2274740}')
class ISelectionItemPatternIdentifiersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.ISelectionItemPatternIdentifiersStatics'
    _iid_ = Guid('{a918d163-487e-4e3e-9f86-7b44acbe27ce}')
    @winrt_commethod(6)
    def get_IsSelectedProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_SelectionContainerProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    IsSelectedProperty = property(get_IsSelectedProperty, None)
    SelectionContainerProperty = property(get_SelectionContainerProperty, None)
class ISelectionPatternIdentifiers(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.ISelectionPatternIdentifiers'
    _iid_ = Guid('{4aa66fb0-e3f7-475f-b78d-f8a83bb730c4}')
class ISelectionPatternIdentifiersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.ISelectionPatternIdentifiersStatics'
    _iid_ = Guid('{93035b4c-6b50-40a1-b23f-5c78ddbd479a}')
    @winrt_commethod(6)
    def get_CanSelectMultipleProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_IsSelectionRequiredProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(8)
    def get_SelectionProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    CanSelectMultipleProperty = property(get_CanSelectMultipleProperty, None)
    IsSelectionRequiredProperty = property(get_IsSelectionRequiredProperty, None)
    SelectionProperty = property(get_SelectionProperty, None)
class ISpreadsheetItemPatternIdentifiers(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.ISpreadsheetItemPatternIdentifiers'
    _iid_ = Guid('{84347e19-ca4b-46a2-a794-c87928a3b1ab}')
class ISpreadsheetItemPatternIdentifiersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.ISpreadsheetItemPatternIdentifiersStatics'
    _iid_ = Guid('{43658779-5380-4f12-b468-b4f368ad4499}')
    @winrt_commethod(6)
    def get_FormulaProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    FormulaProperty = property(get_FormulaProperty, None)
class IStylesPatternIdentifiers(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IStylesPatternIdentifiers'
    _iid_ = Guid('{b0e4e201-e89d-436b-8287-4f7903466879}')
class IStylesPatternIdentifiersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IStylesPatternIdentifiersStatics'
    _iid_ = Guid('{528a457a-bc3c-4d48-94af-1f68703ca296}')
    @winrt_commethod(6)
    def get_ExtendedPropertiesProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_FillColorProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(8)
    def get_FillPatternColorProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(9)
    def get_FillPatternStyleProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(10)
    def get_ShapeProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(11)
    def get_StyleIdProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(12)
    def get_StyleNameProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    ExtendedPropertiesProperty = property(get_ExtendedPropertiesProperty, None)
    FillColorProperty = property(get_FillColorProperty, None)
    FillPatternColorProperty = property(get_FillPatternColorProperty, None)
    FillPatternStyleProperty = property(get_FillPatternStyleProperty, None)
    ShapeProperty = property(get_ShapeProperty, None)
    StyleIdProperty = property(get_StyleIdProperty, None)
    StyleNameProperty = property(get_StyleNameProperty, None)
class ITableItemPatternIdentifiers(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.ITableItemPatternIdentifiers'
    _iid_ = Guid('{c326e5ad-8077-4c64-98e4-e83bcf1b4389}')
class ITableItemPatternIdentifiersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.ITableItemPatternIdentifiersStatics'
    _iid_ = Guid('{24c4b923-e9a2-4de9-b2a4-a8b22d0be362}')
    @winrt_commethod(6)
    def get_ColumnHeaderItemsProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_RowHeaderItemsProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    ColumnHeaderItemsProperty = property(get_ColumnHeaderItemsProperty, None)
    RowHeaderItemsProperty = property(get_RowHeaderItemsProperty, None)
class ITablePatternIdentifiers(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.ITablePatternIdentifiers'
    _iid_ = Guid('{38d104fe-0d0c-412a-bf8d-51ede683baf5}')
class ITablePatternIdentifiersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.ITablePatternIdentifiersStatics'
    _iid_ = Guid('{75073d25-32c9-4903-aecf-dc3504cbd244}')
    @winrt_commethod(6)
    def get_ColumnHeadersProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_RowHeadersProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(8)
    def get_RowOrColumnMajorProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    ColumnHeadersProperty = property(get_ColumnHeadersProperty, None)
    RowHeadersProperty = property(get_RowHeadersProperty, None)
    RowOrColumnMajorProperty = property(get_RowOrColumnMajorProperty, None)
class ITogglePatternIdentifiers(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.ITogglePatternIdentifiers'
    _iid_ = Guid('{7e191f6b-34d4-4ae7-83ac-29f88882d985}')
class ITogglePatternIdentifiersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.ITogglePatternIdentifiersStatics'
    _iid_ = Guid('{c7f75544-14a5-4f2f-92fc-760524de06ea}')
    @winrt_commethod(6)
    def get_ToggleStateProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    ToggleStateProperty = property(get_ToggleStateProperty, None)
class ITransformPattern2Identifiers(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.ITransformPattern2Identifiers'
    _iid_ = Guid('{08aaa03d-dea7-402f-8097-9a2783d60e5d}')
class ITransformPattern2IdentifiersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.ITransformPattern2IdentifiersStatics'
    _iid_ = Guid('{78963644-11f0-467c-a72b-5dac41c1f6fe}')
    @winrt_commethod(6)
    def get_CanZoomProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_ZoomLevelProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(8)
    def get_MaxZoomProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(9)
    def get_MinZoomProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    CanZoomProperty = property(get_CanZoomProperty, None)
    ZoomLevelProperty = property(get_ZoomLevelProperty, None)
    MaxZoomProperty = property(get_MaxZoomProperty, None)
    MinZoomProperty = property(get_MinZoomProperty, None)
class ITransformPatternIdentifiers(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.ITransformPatternIdentifiers'
    _iid_ = Guid('{e4115b8c-c3c8-4a37-b994-2709a7811665}')
class ITransformPatternIdentifiersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.ITransformPatternIdentifiersStatics'
    _iid_ = Guid('{4570edab-d705-40c4-a1dc-e9acfcef85f6}')
    @winrt_commethod(6)
    def get_CanMoveProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_CanResizeProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(8)
    def get_CanRotateProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    CanMoveProperty = property(get_CanMoveProperty, None)
    CanResizeProperty = property(get_CanResizeProperty, None)
    CanRotateProperty = property(get_CanRotateProperty, None)
class IValuePatternIdentifiers(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IValuePatternIdentifiers'
    _iid_ = Guid('{425bf64c-5333-4e41-b470-2bad14ecd085}')
class IValuePatternIdentifiersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IValuePatternIdentifiersStatics'
    _iid_ = Guid('{c247e8f7-adcc-440f-b123-33788a40525a}')
    @winrt_commethod(6)
    def get_IsReadOnlyProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_ValueProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    IsReadOnlyProperty = property(get_IsReadOnlyProperty, None)
    ValueProperty = property(get_ValueProperty, None)
class IWindowPatternIdentifiers(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IWindowPatternIdentifiers'
    _iid_ = Guid('{39f78bb4-7032-41e2-b79e-27b74a8628de}')
class IWindowPatternIdentifiersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.IWindowPatternIdentifiersStatics'
    _iid_ = Guid('{07d0ad06-6302-4d29-878b-19da03fc228d}')
    @winrt_commethod(6)
    def get_CanMaximizeProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_CanMinimizeProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(8)
    def get_IsModalProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(9)
    def get_IsTopmostProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(10)
    def get_WindowInteractionStateProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(11)
    def get_WindowVisualStateProperty(self) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
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
    default_interface: win32more.Windows.UI.Xaml.Automation.IMultipleViewPatternIdentifiers
    _classid_ = 'Windows.UI.Xaml.Automation.MultipleViewPatternIdentifiers'
    @winrt_classmethod
    def get_CurrentViewProperty(cls: win32more.Windows.UI.Xaml.Automation.IMultipleViewPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_SupportedViewsProperty(cls: win32more.Windows.UI.Xaml.Automation.IMultipleViewPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    _MultipleViewPatternIdentifiers_Meta_.CurrentViewProperty = property(get_CurrentViewProperty.__wrapped__, None)
    _MultipleViewPatternIdentifiers_Meta_.SupportedViewsProperty = property(get_SupportedViewsProperty.__wrapped__, None)
class _RangeValuePatternIdentifiers_Meta_(ComPtr.__class__):
    pass
class RangeValuePatternIdentifiers(ComPtr, metaclass=_RangeValuePatternIdentifiers_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Automation.IRangeValuePatternIdentifiers
    _classid_ = 'Windows.UI.Xaml.Automation.RangeValuePatternIdentifiers'
    @winrt_classmethod
    def get_IsReadOnlyProperty(cls: win32more.Windows.UI.Xaml.Automation.IRangeValuePatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_LargeChangeProperty(cls: win32more.Windows.UI.Xaml.Automation.IRangeValuePatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_MaximumProperty(cls: win32more.Windows.UI.Xaml.Automation.IRangeValuePatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_MinimumProperty(cls: win32more.Windows.UI.Xaml.Automation.IRangeValuePatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_SmallChangeProperty(cls: win32more.Windows.UI.Xaml.Automation.IRangeValuePatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_ValueProperty(cls: win32more.Windows.UI.Xaml.Automation.IRangeValuePatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
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
    default_interface: win32more.Windows.UI.Xaml.Automation.IScrollPatternIdentifiers
    _classid_ = 'Windows.UI.Xaml.Automation.ScrollPatternIdentifiers'
    @winrt_classmethod
    def get_HorizontallyScrollableProperty(cls: win32more.Windows.UI.Xaml.Automation.IScrollPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_HorizontalScrollPercentProperty(cls: win32more.Windows.UI.Xaml.Automation.IScrollPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_HorizontalViewSizeProperty(cls: win32more.Windows.UI.Xaml.Automation.IScrollPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_NoScroll(cls: win32more.Windows.UI.Xaml.Automation.IScrollPatternIdentifiersStatics) -> Double: ...
    @winrt_classmethod
    def get_VerticallyScrollableProperty(cls: win32more.Windows.UI.Xaml.Automation.IScrollPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_VerticalScrollPercentProperty(cls: win32more.Windows.UI.Xaml.Automation.IScrollPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_VerticalViewSizeProperty(cls: win32more.Windows.UI.Xaml.Automation.IScrollPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
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
    default_interface: win32more.Windows.UI.Xaml.Automation.ISelectionItemPatternIdentifiers
    _classid_ = 'Windows.UI.Xaml.Automation.SelectionItemPatternIdentifiers'
    @winrt_classmethod
    def get_IsSelectedProperty(cls: win32more.Windows.UI.Xaml.Automation.ISelectionItemPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_SelectionContainerProperty(cls: win32more.Windows.UI.Xaml.Automation.ISelectionItemPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    _SelectionItemPatternIdentifiers_Meta_.IsSelectedProperty = property(get_IsSelectedProperty.__wrapped__, None)
    _SelectionItemPatternIdentifiers_Meta_.SelectionContainerProperty = property(get_SelectionContainerProperty.__wrapped__, None)
class _SelectionPatternIdentifiers_Meta_(ComPtr.__class__):
    pass
class SelectionPatternIdentifiers(ComPtr, metaclass=_SelectionPatternIdentifiers_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Automation.ISelectionPatternIdentifiers
    _classid_ = 'Windows.UI.Xaml.Automation.SelectionPatternIdentifiers'
    @winrt_classmethod
    def get_CanSelectMultipleProperty(cls: win32more.Windows.UI.Xaml.Automation.ISelectionPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_IsSelectionRequiredProperty(cls: win32more.Windows.UI.Xaml.Automation.ISelectionPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_SelectionProperty(cls: win32more.Windows.UI.Xaml.Automation.ISelectionPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    _SelectionPatternIdentifiers_Meta_.CanSelectMultipleProperty = property(get_CanSelectMultipleProperty.__wrapped__, None)
    _SelectionPatternIdentifiers_Meta_.IsSelectionRequiredProperty = property(get_IsSelectionRequiredProperty.__wrapped__, None)
    _SelectionPatternIdentifiers_Meta_.SelectionProperty = property(get_SelectionProperty.__wrapped__, None)
class _SpreadsheetItemPatternIdentifiers_Meta_(ComPtr.__class__):
    pass
class SpreadsheetItemPatternIdentifiers(ComPtr, metaclass=_SpreadsheetItemPatternIdentifiers_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Automation.ISpreadsheetItemPatternIdentifiers
    _classid_ = 'Windows.UI.Xaml.Automation.SpreadsheetItemPatternIdentifiers'
    @winrt_classmethod
    def get_FormulaProperty(cls: win32more.Windows.UI.Xaml.Automation.ISpreadsheetItemPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    _SpreadsheetItemPatternIdentifiers_Meta_.FormulaProperty = property(get_FormulaProperty.__wrapped__, None)
class _StylesPatternIdentifiers_Meta_(ComPtr.__class__):
    pass
class StylesPatternIdentifiers(ComPtr, metaclass=_StylesPatternIdentifiers_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Automation.IStylesPatternIdentifiers
    _classid_ = 'Windows.UI.Xaml.Automation.StylesPatternIdentifiers'
    @winrt_classmethod
    def get_ExtendedPropertiesProperty(cls: win32more.Windows.UI.Xaml.Automation.IStylesPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_FillColorProperty(cls: win32more.Windows.UI.Xaml.Automation.IStylesPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_FillPatternColorProperty(cls: win32more.Windows.UI.Xaml.Automation.IStylesPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_FillPatternStyleProperty(cls: win32more.Windows.UI.Xaml.Automation.IStylesPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_ShapeProperty(cls: win32more.Windows.UI.Xaml.Automation.IStylesPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_StyleIdProperty(cls: win32more.Windows.UI.Xaml.Automation.IStylesPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_StyleNameProperty(cls: win32more.Windows.UI.Xaml.Automation.IStylesPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
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
    default_interface: win32more.Windows.UI.Xaml.Automation.ITableItemPatternIdentifiers
    _classid_ = 'Windows.UI.Xaml.Automation.TableItemPatternIdentifiers'
    @winrt_classmethod
    def get_ColumnHeaderItemsProperty(cls: win32more.Windows.UI.Xaml.Automation.ITableItemPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_RowHeaderItemsProperty(cls: win32more.Windows.UI.Xaml.Automation.ITableItemPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    _TableItemPatternIdentifiers_Meta_.ColumnHeaderItemsProperty = property(get_ColumnHeaderItemsProperty.__wrapped__, None)
    _TableItemPatternIdentifiers_Meta_.RowHeaderItemsProperty = property(get_RowHeaderItemsProperty.__wrapped__, None)
class _TablePatternIdentifiers_Meta_(ComPtr.__class__):
    pass
class TablePatternIdentifiers(ComPtr, metaclass=_TablePatternIdentifiers_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Automation.ITablePatternIdentifiers
    _classid_ = 'Windows.UI.Xaml.Automation.TablePatternIdentifiers'
    @winrt_classmethod
    def get_ColumnHeadersProperty(cls: win32more.Windows.UI.Xaml.Automation.ITablePatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_RowHeadersProperty(cls: win32more.Windows.UI.Xaml.Automation.ITablePatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_RowOrColumnMajorProperty(cls: win32more.Windows.UI.Xaml.Automation.ITablePatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    _TablePatternIdentifiers_Meta_.ColumnHeadersProperty = property(get_ColumnHeadersProperty.__wrapped__, None)
    _TablePatternIdentifiers_Meta_.RowHeadersProperty = property(get_RowHeadersProperty.__wrapped__, None)
    _TablePatternIdentifiers_Meta_.RowOrColumnMajorProperty = property(get_RowOrColumnMajorProperty.__wrapped__, None)
class _TogglePatternIdentifiers_Meta_(ComPtr.__class__):
    pass
class TogglePatternIdentifiers(ComPtr, metaclass=_TogglePatternIdentifiers_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Automation.ITogglePatternIdentifiers
    _classid_ = 'Windows.UI.Xaml.Automation.TogglePatternIdentifiers'
    @winrt_classmethod
    def get_ToggleStateProperty(cls: win32more.Windows.UI.Xaml.Automation.ITogglePatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    _TogglePatternIdentifiers_Meta_.ToggleStateProperty = property(get_ToggleStateProperty.__wrapped__, None)
ToggleState = Int32
ToggleState_Off: ToggleState = 0
ToggleState_On: ToggleState = 1
ToggleState_Indeterminate: ToggleState = 2
class _TransformPattern2Identifiers_Meta_(ComPtr.__class__):
    pass
class TransformPattern2Identifiers(ComPtr, metaclass=_TransformPattern2Identifiers_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Automation.ITransformPattern2Identifiers
    _classid_ = 'Windows.UI.Xaml.Automation.TransformPattern2Identifiers'
    @winrt_classmethod
    def get_CanZoomProperty(cls: win32more.Windows.UI.Xaml.Automation.ITransformPattern2IdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_ZoomLevelProperty(cls: win32more.Windows.UI.Xaml.Automation.ITransformPattern2IdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_MaxZoomProperty(cls: win32more.Windows.UI.Xaml.Automation.ITransformPattern2IdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_MinZoomProperty(cls: win32more.Windows.UI.Xaml.Automation.ITransformPattern2IdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    _TransformPattern2Identifiers_Meta_.CanZoomProperty = property(get_CanZoomProperty.__wrapped__, None)
    _TransformPattern2Identifiers_Meta_.ZoomLevelProperty = property(get_ZoomLevelProperty.__wrapped__, None)
    _TransformPattern2Identifiers_Meta_.MaxZoomProperty = property(get_MaxZoomProperty.__wrapped__, None)
    _TransformPattern2Identifiers_Meta_.MinZoomProperty = property(get_MinZoomProperty.__wrapped__, None)
class _TransformPatternIdentifiers_Meta_(ComPtr.__class__):
    pass
class TransformPatternIdentifiers(ComPtr, metaclass=_TransformPatternIdentifiers_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Automation.ITransformPatternIdentifiers
    _classid_ = 'Windows.UI.Xaml.Automation.TransformPatternIdentifiers'
    @winrt_classmethod
    def get_CanMoveProperty(cls: win32more.Windows.UI.Xaml.Automation.ITransformPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_CanResizeProperty(cls: win32more.Windows.UI.Xaml.Automation.ITransformPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_CanRotateProperty(cls: win32more.Windows.UI.Xaml.Automation.ITransformPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    _TransformPatternIdentifiers_Meta_.CanMoveProperty = property(get_CanMoveProperty.__wrapped__, None)
    _TransformPatternIdentifiers_Meta_.CanResizeProperty = property(get_CanResizeProperty.__wrapped__, None)
    _TransformPatternIdentifiers_Meta_.CanRotateProperty = property(get_CanRotateProperty.__wrapped__, None)
class _ValuePatternIdentifiers_Meta_(ComPtr.__class__):
    pass
class ValuePatternIdentifiers(ComPtr, metaclass=_ValuePatternIdentifiers_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Automation.IValuePatternIdentifiers
    _classid_ = 'Windows.UI.Xaml.Automation.ValuePatternIdentifiers'
    @winrt_classmethod
    def get_IsReadOnlyProperty(cls: win32more.Windows.UI.Xaml.Automation.IValuePatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_ValueProperty(cls: win32more.Windows.UI.Xaml.Automation.IValuePatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
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
    default_interface: win32more.Windows.UI.Xaml.Automation.IWindowPatternIdentifiers
    _classid_ = 'Windows.UI.Xaml.Automation.WindowPatternIdentifiers'
    @winrt_classmethod
    def get_CanMaximizeProperty(cls: win32more.Windows.UI.Xaml.Automation.IWindowPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_CanMinimizeProperty(cls: win32more.Windows.UI.Xaml.Automation.IWindowPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_IsModalProperty(cls: win32more.Windows.UI.Xaml.Automation.IWindowPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_IsTopmostProperty(cls: win32more.Windows.UI.Xaml.Automation.IWindowPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_WindowInteractionStateProperty(cls: win32more.Windows.UI.Xaml.Automation.IWindowPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_WindowVisualStateProperty(cls: win32more.Windows.UI.Xaml.Automation.IWindowPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
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
make_head(_module, 'AnnotationPatternIdentifiers')
make_head(_module, 'AutomationAnnotation')
make_head(_module, 'AutomationElementIdentifiers')
make_head(_module, 'AutomationProperties')
make_head(_module, 'AutomationProperty')
make_head(_module, 'DockPatternIdentifiers')
make_head(_module, 'DragPatternIdentifiers')
make_head(_module, 'DropTargetPatternIdentifiers')
make_head(_module, 'ExpandCollapsePatternIdentifiers')
make_head(_module, 'GridItemPatternIdentifiers')
make_head(_module, 'GridPatternIdentifiers')
make_head(_module, 'IAnnotationPatternIdentifiers')
make_head(_module, 'IAnnotationPatternIdentifiersStatics')
make_head(_module, 'IAutomationAnnotation')
make_head(_module, 'IAutomationAnnotationFactory')
make_head(_module, 'IAutomationAnnotationStatics')
make_head(_module, 'IAutomationElementIdentifiers')
make_head(_module, 'IAutomationElementIdentifiersStatics')
make_head(_module, 'IAutomationElementIdentifiersStatics2')
make_head(_module, 'IAutomationElementIdentifiersStatics3')
make_head(_module, 'IAutomationElementIdentifiersStatics4')
make_head(_module, 'IAutomationElementIdentifiersStatics5')
make_head(_module, 'IAutomationElementIdentifiersStatics6')
make_head(_module, 'IAutomationElementIdentifiersStatics7')
make_head(_module, 'IAutomationElementIdentifiersStatics8')
make_head(_module, 'IAutomationProperties')
make_head(_module, 'IAutomationPropertiesStatics')
make_head(_module, 'IAutomationPropertiesStatics2')
make_head(_module, 'IAutomationPropertiesStatics3')
make_head(_module, 'IAutomationPropertiesStatics4')
make_head(_module, 'IAutomationPropertiesStatics5')
make_head(_module, 'IAutomationPropertiesStatics6')
make_head(_module, 'IAutomationPropertiesStatics7')
make_head(_module, 'IAutomationPropertiesStatics8')
make_head(_module, 'IAutomationPropertiesStatics9')
make_head(_module, 'IAutomationProperty')
make_head(_module, 'IDockPatternIdentifiers')
make_head(_module, 'IDockPatternIdentifiersStatics')
make_head(_module, 'IDragPatternIdentifiers')
make_head(_module, 'IDragPatternIdentifiersStatics')
make_head(_module, 'IDropTargetPatternIdentifiers')
make_head(_module, 'IDropTargetPatternIdentifiersStatics')
make_head(_module, 'IExpandCollapsePatternIdentifiers')
make_head(_module, 'IExpandCollapsePatternIdentifiersStatics')
make_head(_module, 'IGridItemPatternIdentifiers')
make_head(_module, 'IGridItemPatternIdentifiersStatics')
make_head(_module, 'IGridPatternIdentifiers')
make_head(_module, 'IGridPatternIdentifiersStatics')
make_head(_module, 'IMultipleViewPatternIdentifiers')
make_head(_module, 'IMultipleViewPatternIdentifiersStatics')
make_head(_module, 'IRangeValuePatternIdentifiers')
make_head(_module, 'IRangeValuePatternIdentifiersStatics')
make_head(_module, 'IScrollPatternIdentifiers')
make_head(_module, 'IScrollPatternIdentifiersStatics')
make_head(_module, 'ISelectionItemPatternIdentifiers')
make_head(_module, 'ISelectionItemPatternIdentifiersStatics')
make_head(_module, 'ISelectionPatternIdentifiers')
make_head(_module, 'ISelectionPatternIdentifiersStatics')
make_head(_module, 'ISpreadsheetItemPatternIdentifiers')
make_head(_module, 'ISpreadsheetItemPatternIdentifiersStatics')
make_head(_module, 'IStylesPatternIdentifiers')
make_head(_module, 'IStylesPatternIdentifiersStatics')
make_head(_module, 'ITableItemPatternIdentifiers')
make_head(_module, 'ITableItemPatternIdentifiersStatics')
make_head(_module, 'ITablePatternIdentifiers')
make_head(_module, 'ITablePatternIdentifiersStatics')
make_head(_module, 'ITogglePatternIdentifiers')
make_head(_module, 'ITogglePatternIdentifiersStatics')
make_head(_module, 'ITransformPattern2Identifiers')
make_head(_module, 'ITransformPattern2IdentifiersStatics')
make_head(_module, 'ITransformPatternIdentifiers')
make_head(_module, 'ITransformPatternIdentifiersStatics')
make_head(_module, 'IValuePatternIdentifiers')
make_head(_module, 'IValuePatternIdentifiersStatics')
make_head(_module, 'IWindowPatternIdentifiers')
make_head(_module, 'IWindowPatternIdentifiersStatics')
make_head(_module, 'MultipleViewPatternIdentifiers')
make_head(_module, 'RangeValuePatternIdentifiers')
make_head(_module, 'ScrollPatternIdentifiers')
make_head(_module, 'SelectionItemPatternIdentifiers')
make_head(_module, 'SelectionPatternIdentifiers')
make_head(_module, 'SpreadsheetItemPatternIdentifiers')
make_head(_module, 'StylesPatternIdentifiers')
make_head(_module, 'TableItemPatternIdentifiers')
make_head(_module, 'TablePatternIdentifiers')
make_head(_module, 'TogglePatternIdentifiers')
make_head(_module, 'TransformPattern2Identifiers')
make_head(_module, 'TransformPatternIdentifiers')
make_head(_module, 'ValuePatternIdentifiers')
make_head(_module, 'WindowPatternIdentifiers')
