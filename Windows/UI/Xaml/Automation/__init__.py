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
import Windows.Foundation.Collections
import Windows.UI.Xaml
import Windows.UI.Xaml.Automation
import Windows.UI.Xaml.Automation.Peers
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class AnnotationPatternIdentifiers(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Automation.AnnotationPatternIdentifiers'
    @winrt_classmethod
    def get_AnnotationTypeIdProperty(cls: Windows.UI.Xaml.Automation.IAnnotationPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_AnnotationTypeNameProperty(cls: Windows.UI.Xaml.Automation.IAnnotationPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_AuthorProperty(cls: Windows.UI.Xaml.Automation.IAnnotationPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_DateTimeProperty(cls: Windows.UI.Xaml.Automation.IAnnotationPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_TargetProperty(cls: Windows.UI.Xaml.Automation.IAnnotationPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    AnnotationTypeIdProperty = property(get_AnnotationTypeIdProperty, None)
    AnnotationTypeNameProperty = property(get_AnnotationTypeNameProperty, None)
    AuthorProperty = property(get_AuthorProperty, None)
    DateTimeProperty = property(get_DateTimeProperty, None)
    TargetProperty = property(get_TargetProperty, None)
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
class AutomationAnnotation(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    ClassId = 'Windows.UI.Xaml.Automation.AutomationAnnotation'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Automation.AutomationAnnotation: ...
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.Automation.IAutomationAnnotationFactory, type: Windows.UI.Xaml.Automation.AnnotationType) -> Windows.UI.Xaml.Automation.AutomationAnnotation: ...
    @winrt_factorymethod
    def CreateWithElementParameter(cls: Windows.UI.Xaml.Automation.IAutomationAnnotationFactory, type: Windows.UI.Xaml.Automation.AnnotationType, element: Windows.UI.Xaml.UIElement) -> Windows.UI.Xaml.Automation.AutomationAnnotation: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.UI.Xaml.Automation.IAutomationAnnotation) -> Windows.UI.Xaml.Automation.AnnotationType: ...
    @winrt_mixinmethod
    def put_Type(self: Windows.UI.Xaml.Automation.IAutomationAnnotation, value: Windows.UI.Xaml.Automation.AnnotationType) -> Void: ...
    @winrt_mixinmethod
    def get_Element(self: Windows.UI.Xaml.Automation.IAutomationAnnotation) -> Windows.UI.Xaml.UIElement: ...
    @winrt_mixinmethod
    def put_Element(self: Windows.UI.Xaml.Automation.IAutomationAnnotation, value: Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_classmethod
    def get_TypeProperty(cls: Windows.UI.Xaml.Automation.IAutomationAnnotationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ElementProperty(cls: Windows.UI.Xaml.Automation.IAutomationAnnotationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Type = property(get_Type, put_Type)
    Element = property(get_Element, put_Element)
    TypeProperty = property(get_TypeProperty, None)
    ElementProperty = property(get_ElementProperty, None)
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
class AutomationElementIdentifiers(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Automation.AutomationElementIdentifiers'
    @winrt_classmethod
    def get_IsDialogProperty(cls: Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics8) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_HeadingLevelProperty(cls: Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics7) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_CultureProperty(cls: Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics6) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_IsPeripheralProperty(cls: Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics5) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_IsDataValidForFormProperty(cls: Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics5) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_FullDescriptionProperty(cls: Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics5) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_DescribedByProperty(cls: Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics5) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_FlowsToProperty(cls: Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics5) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_FlowsFromProperty(cls: Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics5) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_LandmarkTypeProperty(cls: Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics4) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_LocalizedLandmarkTypeProperty(cls: Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics4) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_PositionInSetProperty(cls: Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics3) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_SizeOfSetProperty(cls: Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics3) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_LevelProperty(cls: Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics3) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_AnnotationsProperty(cls: Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics3) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_ControlledPeersProperty(cls: Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics2) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_AcceleratorKeyProperty(cls: Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_AccessKeyProperty(cls: Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_AutomationIdProperty(cls: Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_BoundingRectangleProperty(cls: Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_ClassNameProperty(cls: Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_ClickablePointProperty(cls: Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_ControlTypeProperty(cls: Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_HasKeyboardFocusProperty(cls: Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_HelpTextProperty(cls: Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_IsContentElementProperty(cls: Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_IsControlElementProperty(cls: Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_IsEnabledProperty(cls: Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_IsKeyboardFocusableProperty(cls: Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_IsOffscreenProperty(cls: Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_IsPasswordProperty(cls: Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_IsRequiredForFormProperty(cls: Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_ItemStatusProperty(cls: Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_ItemTypeProperty(cls: Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_LabeledByProperty(cls: Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_LocalizedControlTypeProperty(cls: Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_NameProperty(cls: Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_OrientationProperty(cls: Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_LiveSettingProperty(cls: Windows.UI.Xaml.Automation.IAutomationElementIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    IsDialogProperty = property(get_IsDialogProperty, None)
    HeadingLevelProperty = property(get_HeadingLevelProperty, None)
    CultureProperty = property(get_CultureProperty, None)
    IsPeripheralProperty = property(get_IsPeripheralProperty, None)
    IsDataValidForFormProperty = property(get_IsDataValidForFormProperty, None)
    FullDescriptionProperty = property(get_FullDescriptionProperty, None)
    DescribedByProperty = property(get_DescribedByProperty, None)
    FlowsToProperty = property(get_FlowsToProperty, None)
    FlowsFromProperty = property(get_FlowsFromProperty, None)
    LandmarkTypeProperty = property(get_LandmarkTypeProperty, None)
    LocalizedLandmarkTypeProperty = property(get_LocalizedLandmarkTypeProperty, None)
    PositionInSetProperty = property(get_PositionInSetProperty, None)
    SizeOfSetProperty = property(get_SizeOfSetProperty, None)
    LevelProperty = property(get_LevelProperty, None)
    AnnotationsProperty = property(get_AnnotationsProperty, None)
    ControlledPeersProperty = property(get_ControlledPeersProperty, None)
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
class AutomationProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Automation.AutomationProperties'
    @winrt_classmethod
    def get_AutomationControlTypeProperty(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics9) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetAutomationControlType(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics9, element: Windows.UI.Xaml.UIElement) -> Windows.UI.Xaml.Automation.Peers.AutomationControlType: ...
    @winrt_classmethod
    def SetAutomationControlType(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics9, element: Windows.UI.Xaml.UIElement, value: Windows.UI.Xaml.Automation.Peers.AutomationControlType) -> Void: ...
    @winrt_classmethod
    def get_IsDialogProperty(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics8) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetIsDialog(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics8, element: Windows.UI.Xaml.DependencyObject) -> Boolean: ...
    @winrt_classmethod
    def SetIsDialog(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics8, element: Windows.UI.Xaml.DependencyObject, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_HeadingLevelProperty(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics7) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetHeadingLevel(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics7, element: Windows.UI.Xaml.DependencyObject) -> Windows.UI.Xaml.Automation.Peers.AutomationHeadingLevel: ...
    @winrt_classmethod
    def SetHeadingLevel(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics7, element: Windows.UI.Xaml.DependencyObject, value: Windows.UI.Xaml.Automation.Peers.AutomationHeadingLevel) -> Void: ...
    @winrt_classmethod
    def get_CultureProperty(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics6) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetCulture(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics6, element: Windows.UI.Xaml.DependencyObject) -> Int32: ...
    @winrt_classmethod
    def SetCulture(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics6, element: Windows.UI.Xaml.DependencyObject, value: Int32) -> Void: ...
    @winrt_classmethod
    def get_IsPeripheralProperty(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics5) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetIsPeripheral(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics5, element: Windows.UI.Xaml.DependencyObject) -> Boolean: ...
    @winrt_classmethod
    def SetIsPeripheral(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics5, element: Windows.UI.Xaml.DependencyObject, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_IsDataValidForFormProperty(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics5) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetIsDataValidForForm(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics5, element: Windows.UI.Xaml.DependencyObject) -> Boolean: ...
    @winrt_classmethod
    def SetIsDataValidForForm(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics5, element: Windows.UI.Xaml.DependencyObject, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_FullDescriptionProperty(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics5) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetFullDescription(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics5, element: Windows.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_classmethod
    def SetFullDescription(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics5, element: Windows.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_LocalizedControlTypeProperty(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics5) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetLocalizedControlType(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics5, element: Windows.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_classmethod
    def SetLocalizedControlType(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics5, element: Windows.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_DescribedByProperty(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics5) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetDescribedBy(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics5, element: Windows.UI.Xaml.DependencyObject) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.DependencyObject]: ...
    @winrt_classmethod
    def get_FlowsToProperty(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics5) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetFlowsTo(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics5, element: Windows.UI.Xaml.DependencyObject) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.DependencyObject]: ...
    @winrt_classmethod
    def get_FlowsFromProperty(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics5) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetFlowsFrom(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics5, element: Windows.UI.Xaml.DependencyObject) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.DependencyObject]: ...
    @winrt_classmethod
    def get_LandmarkTypeProperty(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics4) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetLandmarkType(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics4, element: Windows.UI.Xaml.DependencyObject) -> Windows.UI.Xaml.Automation.Peers.AutomationLandmarkType: ...
    @winrt_classmethod
    def SetLandmarkType(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics4, element: Windows.UI.Xaml.DependencyObject, value: Windows.UI.Xaml.Automation.Peers.AutomationLandmarkType) -> Void: ...
    @winrt_classmethod
    def get_LocalizedLandmarkTypeProperty(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics4) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetLocalizedLandmarkType(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics4, element: Windows.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_classmethod
    def SetLocalizedLandmarkType(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics4, element: Windows.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_PositionInSetProperty(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics3) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetPositionInSet(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics3, element: Windows.UI.Xaml.DependencyObject) -> Int32: ...
    @winrt_classmethod
    def SetPositionInSet(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics3, element: Windows.UI.Xaml.DependencyObject, value: Int32) -> Void: ...
    @winrt_classmethod
    def get_SizeOfSetProperty(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics3) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetSizeOfSet(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics3, element: Windows.UI.Xaml.DependencyObject) -> Int32: ...
    @winrt_classmethod
    def SetSizeOfSet(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics3, element: Windows.UI.Xaml.DependencyObject, value: Int32) -> Void: ...
    @winrt_classmethod
    def get_LevelProperty(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics3) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetLevel(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics3, element: Windows.UI.Xaml.DependencyObject) -> Int32: ...
    @winrt_classmethod
    def SetLevel(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics3, element: Windows.UI.Xaml.DependencyObject, value: Int32) -> Void: ...
    @winrt_classmethod
    def get_AnnotationsProperty(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics3) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetAnnotations(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics3, element: Windows.UI.Xaml.DependencyObject) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Automation.AutomationAnnotation]: ...
    @winrt_classmethod
    def get_AccessibilityViewProperty(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics2) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetAccessibilityView(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics2, element: Windows.UI.Xaml.DependencyObject) -> Windows.UI.Xaml.Automation.Peers.AccessibilityView: ...
    @winrt_classmethod
    def SetAccessibilityView(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics2, element: Windows.UI.Xaml.DependencyObject, value: Windows.UI.Xaml.Automation.Peers.AccessibilityView) -> Void: ...
    @winrt_classmethod
    def get_ControlledPeersProperty(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics2) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetControlledPeers(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics2, element: Windows.UI.Xaml.DependencyObject) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.UIElement]: ...
    @winrt_classmethod
    def get_AcceleratorKeyProperty(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetAcceleratorKey(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics, element: Windows.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_classmethod
    def SetAcceleratorKey(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics, element: Windows.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_AccessKeyProperty(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetAccessKey(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics, element: Windows.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_classmethod
    def SetAccessKey(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics, element: Windows.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_AutomationIdProperty(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetAutomationId(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics, element: Windows.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_classmethod
    def SetAutomationId(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics, element: Windows.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_HelpTextProperty(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetHelpText(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics, element: Windows.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_classmethod
    def SetHelpText(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics, element: Windows.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_IsRequiredForFormProperty(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetIsRequiredForForm(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics, element: Windows.UI.Xaml.DependencyObject) -> Boolean: ...
    @winrt_classmethod
    def SetIsRequiredForForm(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics, element: Windows.UI.Xaml.DependencyObject, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_ItemStatusProperty(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetItemStatus(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics, element: Windows.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_classmethod
    def SetItemStatus(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics, element: Windows.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_ItemTypeProperty(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetItemType(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics, element: Windows.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_classmethod
    def SetItemType(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics, element: Windows.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_LabeledByProperty(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetLabeledBy(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics, element: Windows.UI.Xaml.DependencyObject) -> Windows.UI.Xaml.UIElement: ...
    @winrt_classmethod
    def SetLabeledBy(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics, element: Windows.UI.Xaml.DependencyObject, value: Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_classmethod
    def get_NameProperty(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetName(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics, element: Windows.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_classmethod
    def SetName(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics, element: Windows.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_LiveSettingProperty(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetLiveSetting(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics, element: Windows.UI.Xaml.DependencyObject) -> Windows.UI.Xaml.Automation.Peers.AutomationLiveSetting: ...
    @winrt_classmethod
    def SetLiveSetting(cls: Windows.UI.Xaml.Automation.IAutomationPropertiesStatics, element: Windows.UI.Xaml.DependencyObject, value: Windows.UI.Xaml.Automation.Peers.AutomationLiveSetting) -> Void: ...
    AutomationControlTypeProperty = property(get_AutomationControlTypeProperty, None)
    IsDialogProperty = property(get_IsDialogProperty, None)
    HeadingLevelProperty = property(get_HeadingLevelProperty, None)
    CultureProperty = property(get_CultureProperty, None)
    IsPeripheralProperty = property(get_IsPeripheralProperty, None)
    IsDataValidForFormProperty = property(get_IsDataValidForFormProperty, None)
    FullDescriptionProperty = property(get_FullDescriptionProperty, None)
    LocalizedControlTypeProperty = property(get_LocalizedControlTypeProperty, None)
    DescribedByProperty = property(get_DescribedByProperty, None)
    FlowsToProperty = property(get_FlowsToProperty, None)
    FlowsFromProperty = property(get_FlowsFromProperty, None)
    LandmarkTypeProperty = property(get_LandmarkTypeProperty, None)
    LocalizedLandmarkTypeProperty = property(get_LocalizedLandmarkTypeProperty, None)
    PositionInSetProperty = property(get_PositionInSetProperty, None)
    SizeOfSetProperty = property(get_SizeOfSetProperty, None)
    LevelProperty = property(get_LevelProperty, None)
    AnnotationsProperty = property(get_AnnotationsProperty, None)
    AccessibilityViewProperty = property(get_AccessibilityViewProperty, None)
    ControlledPeersProperty = property(get_ControlledPeersProperty, None)
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
class AutomationProperty(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Automation.AutomationProperty'
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
class DockPatternIdentifiers(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Automation.DockPatternIdentifiers'
    @winrt_classmethod
    def get_DockPositionProperty(cls: Windows.UI.Xaml.Automation.IDockPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    DockPositionProperty = property(get_DockPositionProperty, None)
DockPosition = Int32
DockPosition_Top: DockPosition = 0
DockPosition_Left: DockPosition = 1
DockPosition_Bottom: DockPosition = 2
DockPosition_Right: DockPosition = 3
DockPosition_Fill: DockPosition = 4
DockPosition_None: DockPosition = 5
class DragPatternIdentifiers(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Automation.DragPatternIdentifiers'
    @winrt_classmethod
    def get_DropEffectProperty(cls: Windows.UI.Xaml.Automation.IDragPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_DropEffectsProperty(cls: Windows.UI.Xaml.Automation.IDragPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_GrabbedItemsProperty(cls: Windows.UI.Xaml.Automation.IDragPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_IsGrabbedProperty(cls: Windows.UI.Xaml.Automation.IDragPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    DropEffectProperty = property(get_DropEffectProperty, None)
    DropEffectsProperty = property(get_DropEffectsProperty, None)
    GrabbedItemsProperty = property(get_GrabbedItemsProperty, None)
    IsGrabbedProperty = property(get_IsGrabbedProperty, None)
class DropTargetPatternIdentifiers(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Automation.DropTargetPatternIdentifiers'
    @winrt_classmethod
    def get_DropTargetEffectProperty(cls: Windows.UI.Xaml.Automation.IDropTargetPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_DropTargetEffectsProperty(cls: Windows.UI.Xaml.Automation.IDropTargetPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    DropTargetEffectProperty = property(get_DropTargetEffectProperty, None)
    DropTargetEffectsProperty = property(get_DropTargetEffectsProperty, None)
class ExpandCollapsePatternIdentifiers(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Automation.ExpandCollapsePatternIdentifiers'
    @winrt_classmethod
    def get_ExpandCollapseStateProperty(cls: Windows.UI.Xaml.Automation.IExpandCollapsePatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    ExpandCollapseStateProperty = property(get_ExpandCollapseStateProperty, None)
ExpandCollapseState = Int32
ExpandCollapseState_Collapsed: ExpandCollapseState = 0
ExpandCollapseState_Expanded: ExpandCollapseState = 1
ExpandCollapseState_PartiallyExpanded: ExpandCollapseState = 2
ExpandCollapseState_LeafNode: ExpandCollapseState = 3
class GridItemPatternIdentifiers(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Automation.GridItemPatternIdentifiers'
    @winrt_classmethod
    def get_ColumnProperty(cls: Windows.UI.Xaml.Automation.IGridItemPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_ColumnSpanProperty(cls: Windows.UI.Xaml.Automation.IGridItemPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_ContainingGridProperty(cls: Windows.UI.Xaml.Automation.IGridItemPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_RowProperty(cls: Windows.UI.Xaml.Automation.IGridItemPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_RowSpanProperty(cls: Windows.UI.Xaml.Automation.IGridItemPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    ColumnProperty = property(get_ColumnProperty, None)
    ColumnSpanProperty = property(get_ColumnSpanProperty, None)
    ContainingGridProperty = property(get_ContainingGridProperty, None)
    RowProperty = property(get_RowProperty, None)
    RowSpanProperty = property(get_RowSpanProperty, None)
class GridPatternIdentifiers(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Automation.GridPatternIdentifiers'
    @winrt_classmethod
    def get_ColumnCountProperty(cls: Windows.UI.Xaml.Automation.IGridPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_RowCountProperty(cls: Windows.UI.Xaml.Automation.IGridPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    ColumnCountProperty = property(get_ColumnCountProperty, None)
    RowCountProperty = property(get_RowCountProperty, None)
class IAnnotationPatternIdentifiers(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('d475a0c1-48b2-4e40-a6-cf-3d-c4-b6-38-c0-de')
class IAnnotationPatternIdentifiersStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('e0e3a35d-d167-46dc-95-ab-33-0a-f6-1a-eb-b5')
    @winrt_commethod(6)
    def get_AnnotationTypeIdProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_AnnotationTypeNameProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(8)
    def get_AuthorProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(9)
    def get_DateTimeProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(10)
    def get_TargetProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    AnnotationTypeIdProperty = property(get_AnnotationTypeIdProperty, None)
    AnnotationTypeNameProperty = property(get_AnnotationTypeNameProperty, None)
    AuthorProperty = property(get_AuthorProperty, None)
    DateTimeProperty = property(get_DateTimeProperty, None)
    TargetProperty = property(get_TargetProperty, None)
class IAutomationAnnotation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('fb3c30ca-03d8-4618-91-bf-e4-d8-4f-4a-f3-18')
    @winrt_commethod(6)
    def get_Type(self) -> Windows.UI.Xaml.Automation.AnnotationType: ...
    @winrt_commethod(7)
    def put_Type(self, value: Windows.UI.Xaml.Automation.AnnotationType) -> Void: ...
    @winrt_commethod(8)
    def get_Element(self) -> Windows.UI.Xaml.UIElement: ...
    @winrt_commethod(9)
    def put_Element(self, value: Windows.UI.Xaml.UIElement) -> Void: ...
    Type = property(get_Type, put_Type)
    Element = property(get_Element, put_Element)
class IAutomationAnnotationFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('4906fa52-ddc0-4e69-b7-6b-01-9d-92-8d-82-2f')
    @winrt_commethod(6)
    def CreateInstance(self, type: Windows.UI.Xaml.Automation.AnnotationType) -> Windows.UI.Xaml.Automation.AutomationAnnotation: ...
    @winrt_commethod(7)
    def CreateWithElementParameter(self, type: Windows.UI.Xaml.Automation.AnnotationType, element: Windows.UI.Xaml.UIElement) -> Windows.UI.Xaml.Automation.AutomationAnnotation: ...
class IAutomationAnnotationStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('e503eab7-4ee5-48cb-b5-b8-bb-cd-46-c9-d1-da')
    @winrt_commethod(6)
    def get_TypeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_ElementProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    TypeProperty = property(get_TypeProperty, None)
    ElementProperty = property(get_ElementProperty, None)
class IAutomationElementIdentifiers(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('e68a63cf-4345-4e2d-8a-6a-49-cc-e1-fa-2d-cc')
class IAutomationElementIdentifiersStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('4549399f-8340-4d67-b9-bf-8c-2a-c6-a0-77-3a')
    @winrt_commethod(6)
    def get_AcceleratorKeyProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_AccessKeyProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(8)
    def get_AutomationIdProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(9)
    def get_BoundingRectangleProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(10)
    def get_ClassNameProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(11)
    def get_ClickablePointProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(12)
    def get_ControlTypeProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(13)
    def get_HasKeyboardFocusProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(14)
    def get_HelpTextProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(15)
    def get_IsContentElementProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(16)
    def get_IsControlElementProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(17)
    def get_IsEnabledProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(18)
    def get_IsKeyboardFocusableProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(19)
    def get_IsOffscreenProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(20)
    def get_IsPasswordProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(21)
    def get_IsRequiredForFormProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(22)
    def get_ItemStatusProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(23)
    def get_ItemTypeProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(24)
    def get_LabeledByProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(25)
    def get_LocalizedControlTypeProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(26)
    def get_NameProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(27)
    def get_OrientationProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(28)
    def get_LiveSettingProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('b5cbb1e2-d55f-46a9-9e-da-1a-47-42-51-5d-c3')
    @winrt_commethod(6)
    def get_ControlledPeersProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    ControlledPeersProperty = property(get_ControlledPeersProperty, None)
class IAutomationElementIdentifiersStatics3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('0f5cbebd-b3eb-4083-ad-c7-0c-2f-39-bb-35-43')
    @winrt_commethod(6)
    def get_PositionInSetProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_SizeOfSetProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(8)
    def get_LevelProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(9)
    def get_AnnotationsProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    PositionInSetProperty = property(get_PositionInSetProperty, None)
    SizeOfSetProperty = property(get_SizeOfSetProperty, None)
    LevelProperty = property(get_LevelProperty, None)
    AnnotationsProperty = property(get_AnnotationsProperty, None)
class IAutomationElementIdentifiersStatics4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('5af51f75-5913-4d78-b3-30-a6-f5-0b-73-ed-9b')
    @winrt_commethod(6)
    def get_LandmarkTypeProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_LocalizedLandmarkTypeProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    LandmarkTypeProperty = property(get_LandmarkTypeProperty, None)
    LocalizedLandmarkTypeProperty = property(get_LocalizedLandmarkTypeProperty, None)
class IAutomationElementIdentifiersStatics5(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('986a8206-de59-42f9-a1-e7-62-b8-af-9e-75-6d')
    @winrt_commethod(6)
    def get_IsPeripheralProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_IsDataValidForFormProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(8)
    def get_FullDescriptionProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(9)
    def get_DescribedByProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(10)
    def get_FlowsToProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(11)
    def get_FlowsFromProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    IsPeripheralProperty = property(get_IsPeripheralProperty, None)
    IsDataValidForFormProperty = property(get_IsDataValidForFormProperty, None)
    FullDescriptionProperty = property(get_FullDescriptionProperty, None)
    DescribedByProperty = property(get_DescribedByProperty, None)
    FlowsToProperty = property(get_FlowsToProperty, None)
    FlowsFromProperty = property(get_FlowsFromProperty, None)
class IAutomationElementIdentifiersStatics6(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('de52b00d-8328-4eae-80-35-f8-db-99-c8-ba-c4')
    @winrt_commethod(6)
    def get_CultureProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    CultureProperty = property(get_CultureProperty, None)
class IAutomationElementIdentifiersStatics7(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('00f1abb2-742c-446a-a8-f6-16-72-b1-0d-28-74')
    @winrt_commethod(6)
    def get_HeadingLevelProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    HeadingLevelProperty = property(get_HeadingLevelProperty, None)
class IAutomationElementIdentifiersStatics8(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('8517b060-806c-5dc5-bc-41-89-1b-b5-a4-7a-df')
    @winrt_commethod(6)
    def get_IsDialogProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    IsDialogProperty = property(get_IsDialogProperty, None)
class IAutomationProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('68d7232c-e622-48e9-af-0b-1f-fa-33-cc-5c-ba')
class IAutomationPropertiesStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('b618fd7b-32d0-4970-9c-42-7c-03-9a-c7-be-78')
    @winrt_commethod(6)
    def get_AcceleratorKeyProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def GetAcceleratorKey(self, element: Windows.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_commethod(8)
    def SetAcceleratorKey(self, element: Windows.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_AccessKeyProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def GetAccessKey(self, element: Windows.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_commethod(11)
    def SetAccessKey(self, element: Windows.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_AutomationIdProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def GetAutomationId(self, element: Windows.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_commethod(14)
    def SetAutomationId(self, element: Windows.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_commethod(15)
    def get_HelpTextProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(16)
    def GetHelpText(self, element: Windows.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_commethod(17)
    def SetHelpText(self, element: Windows.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_commethod(18)
    def get_IsRequiredForFormProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(19)
    def GetIsRequiredForForm(self, element: Windows.UI.Xaml.DependencyObject) -> Boolean: ...
    @winrt_commethod(20)
    def SetIsRequiredForForm(self, element: Windows.UI.Xaml.DependencyObject, value: Boolean) -> Void: ...
    @winrt_commethod(21)
    def get_ItemStatusProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(22)
    def GetItemStatus(self, element: Windows.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_commethod(23)
    def SetItemStatus(self, element: Windows.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_commethod(24)
    def get_ItemTypeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(25)
    def GetItemType(self, element: Windows.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_commethod(26)
    def SetItemType(self, element: Windows.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_commethod(27)
    def get_LabeledByProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(28)
    def GetLabeledBy(self, element: Windows.UI.Xaml.DependencyObject) -> Windows.UI.Xaml.UIElement: ...
    @winrt_commethod(29)
    def SetLabeledBy(self, element: Windows.UI.Xaml.DependencyObject, value: Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(30)
    def get_NameProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(31)
    def GetName(self, element: Windows.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_commethod(32)
    def SetName(self, element: Windows.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_commethod(33)
    def get_LiveSettingProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(34)
    def GetLiveSetting(self, element: Windows.UI.Xaml.DependencyObject) -> Windows.UI.Xaml.Automation.Peers.AutomationLiveSetting: ...
    @winrt_commethod(35)
    def SetLiveSetting(self, element: Windows.UI.Xaml.DependencyObject, value: Windows.UI.Xaml.Automation.Peers.AutomationLiveSetting) -> Void: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('3976547f-7089-4801-8f-1d-aa-b7-80-90-d1-a0')
    @winrt_commethod(6)
    def get_AccessibilityViewProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def GetAccessibilityView(self, element: Windows.UI.Xaml.DependencyObject) -> Windows.UI.Xaml.Automation.Peers.AccessibilityView: ...
    @winrt_commethod(8)
    def SetAccessibilityView(self, element: Windows.UI.Xaml.DependencyObject, value: Windows.UI.Xaml.Automation.Peers.AccessibilityView) -> Void: ...
    @winrt_commethod(9)
    def get_ControlledPeersProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def GetControlledPeers(self, element: Windows.UI.Xaml.DependencyObject) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.UIElement]: ...
    AccessibilityViewProperty = property(get_AccessibilityViewProperty, None)
    ControlledPeersProperty = property(get_ControlledPeersProperty, None)
class IAutomationPropertiesStatics3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('7b75d735-5cb1-42ad-9b-57-5f-ab-a8-c1-86-7f')
    @winrt_commethod(6)
    def get_PositionInSetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def GetPositionInSet(self, element: Windows.UI.Xaml.DependencyObject) -> Int32: ...
    @winrt_commethod(8)
    def SetPositionInSet(self, element: Windows.UI.Xaml.DependencyObject, value: Int32) -> Void: ...
    @winrt_commethod(9)
    def get_SizeOfSetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def GetSizeOfSet(self, element: Windows.UI.Xaml.DependencyObject) -> Int32: ...
    @winrt_commethod(11)
    def SetSizeOfSet(self, element: Windows.UI.Xaml.DependencyObject, value: Int32) -> Void: ...
    @winrt_commethod(12)
    def get_LevelProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def GetLevel(self, element: Windows.UI.Xaml.DependencyObject) -> Int32: ...
    @winrt_commethod(14)
    def SetLevel(self, element: Windows.UI.Xaml.DependencyObject, value: Int32) -> Void: ...
    @winrt_commethod(15)
    def get_AnnotationsProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(16)
    def GetAnnotations(self, element: Windows.UI.Xaml.DependencyObject) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Automation.AutomationAnnotation]: ...
    PositionInSetProperty = property(get_PositionInSetProperty, None)
    SizeOfSetProperty = property(get_SizeOfSetProperty, None)
    LevelProperty = property(get_LevelProperty, None)
    AnnotationsProperty = property(get_AnnotationsProperty, None)
class IAutomationPropertiesStatics4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('f7d62655-311a-4b7c-a1-31-52-4e-89-cd-3c-f9')
    @winrt_commethod(6)
    def get_LandmarkTypeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def GetLandmarkType(self, element: Windows.UI.Xaml.DependencyObject) -> Windows.UI.Xaml.Automation.Peers.AutomationLandmarkType: ...
    @winrt_commethod(8)
    def SetLandmarkType(self, element: Windows.UI.Xaml.DependencyObject, value: Windows.UI.Xaml.Automation.Peers.AutomationLandmarkType) -> Void: ...
    @winrt_commethod(9)
    def get_LocalizedLandmarkTypeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def GetLocalizedLandmarkType(self, element: Windows.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_commethod(11)
    def SetLocalizedLandmarkType(self, element: Windows.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    LandmarkTypeProperty = property(get_LandmarkTypeProperty, None)
    LocalizedLandmarkTypeProperty = property(get_LocalizedLandmarkTypeProperty, None)
class IAutomationPropertiesStatics5(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('0be35b26-c8f9-41a2-b4-db-e6-a7-a3-2b-0c-34')
    @winrt_commethod(6)
    def get_IsPeripheralProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def GetIsPeripheral(self, element: Windows.UI.Xaml.DependencyObject) -> Boolean: ...
    @winrt_commethod(8)
    def SetIsPeripheral(self, element: Windows.UI.Xaml.DependencyObject, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_IsDataValidForFormProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def GetIsDataValidForForm(self, element: Windows.UI.Xaml.DependencyObject) -> Boolean: ...
    @winrt_commethod(11)
    def SetIsDataValidForForm(self, element: Windows.UI.Xaml.DependencyObject, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_FullDescriptionProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def GetFullDescription(self, element: Windows.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_commethod(14)
    def SetFullDescription(self, element: Windows.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_commethod(15)
    def get_LocalizedControlTypeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(16)
    def GetLocalizedControlType(self, element: Windows.UI.Xaml.DependencyObject) -> WinRT_String: ...
    @winrt_commethod(17)
    def SetLocalizedControlType(self, element: Windows.UI.Xaml.DependencyObject, value: WinRT_String) -> Void: ...
    @winrt_commethod(18)
    def get_DescribedByProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(19)
    def GetDescribedBy(self, element: Windows.UI.Xaml.DependencyObject) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.DependencyObject]: ...
    @winrt_commethod(20)
    def get_FlowsToProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(21)
    def GetFlowsTo(self, element: Windows.UI.Xaml.DependencyObject) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.DependencyObject]: ...
    @winrt_commethod(22)
    def get_FlowsFromProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(23)
    def GetFlowsFrom(self, element: Windows.UI.Xaml.DependencyObject) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.DependencyObject]: ...
    IsPeripheralProperty = property(get_IsPeripheralProperty, None)
    IsDataValidForFormProperty = property(get_IsDataValidForFormProperty, None)
    FullDescriptionProperty = property(get_FullDescriptionProperty, None)
    LocalizedControlTypeProperty = property(get_LocalizedControlTypeProperty, None)
    DescribedByProperty = property(get_DescribedByProperty, None)
    FlowsToProperty = property(get_FlowsToProperty, None)
    FlowsFromProperty = property(get_FlowsFromProperty, None)
class IAutomationPropertiesStatics6(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('c61e030f-eb49-4e5d-b0-12-4c-1c-96-c3-90-1b')
    @winrt_commethod(6)
    def get_CultureProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def GetCulture(self, element: Windows.UI.Xaml.DependencyObject) -> Int32: ...
    @winrt_commethod(8)
    def SetCulture(self, element: Windows.UI.Xaml.DependencyObject, value: Int32) -> Void: ...
    CultureProperty = property(get_CultureProperty, None)
class IAutomationPropertiesStatics7(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('f7e98bf3-8f91-4068-a4-ad-b7-b4-02-d1-0a-2c')
    @winrt_commethod(6)
    def get_HeadingLevelProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def GetHeadingLevel(self, element: Windows.UI.Xaml.DependencyObject) -> Windows.UI.Xaml.Automation.Peers.AutomationHeadingLevel: ...
    @winrt_commethod(8)
    def SetHeadingLevel(self, element: Windows.UI.Xaml.DependencyObject, value: Windows.UI.Xaml.Automation.Peers.AutomationHeadingLevel) -> Void: ...
    HeadingLevelProperty = property(get_HeadingLevelProperty, None)
class IAutomationPropertiesStatics8(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('432eca20-171a-560d-85-24-3e-65-1d-3a-d6-ca')
    @winrt_commethod(6)
    def get_IsDialogProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def GetIsDialog(self, element: Windows.UI.Xaml.DependencyObject) -> Boolean: ...
    @winrt_commethod(8)
    def SetIsDialog(self, element: Windows.UI.Xaml.DependencyObject, value: Boolean) -> Void: ...
    IsDialogProperty = property(get_IsDialogProperty, None)
class IAutomationPropertiesStatics9(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('2f20b1d1-87b2-5562-80-77-da-59-3e-da-fd-2d')
    @winrt_commethod(6)
    def get_AutomationControlTypeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def GetAutomationControlType(self, element: Windows.UI.Xaml.UIElement) -> Windows.UI.Xaml.Automation.Peers.AutomationControlType: ...
    @winrt_commethod(8)
    def SetAutomationControlType(self, element: Windows.UI.Xaml.UIElement, value: Windows.UI.Xaml.Automation.Peers.AutomationControlType) -> Void: ...
    AutomationControlTypeProperty = property(get_AutomationControlTypeProperty, None)
class IAutomationProperty(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('b627195b-3227-4e16-95-34-dd-ec-e3-0d-db-46')
class IDockPatternIdentifiers(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('ccd7f4e6-e4f9-47ff-bd-e7-37-8b-11-f7-8e-09')
class IDockPatternIdentifiersStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('2b87245c-ed80-4fe5-8e-b4-70-8a-39-c8-41-e5')
    @winrt_commethod(6)
    def get_DockPositionProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    DockPositionProperty = property(get_DockPositionProperty, None)
class IDragPatternIdentifiers(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('6266e985-4d07-4e80-82-eb-8f-96-69-0a-1a-0c')
class IDragPatternIdentifiersStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('2a05379d-1755-4082-9d-90-46-f1-41-1d-79-86')
    @winrt_commethod(6)
    def get_DropEffectProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_DropEffectsProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(8)
    def get_GrabbedItemsProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(9)
    def get_IsGrabbedProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    DropEffectProperty = property(get_DropEffectProperty, None)
    DropEffectsProperty = property(get_DropEffectsProperty, None)
    GrabbedItemsProperty = property(get_GrabbedItemsProperty, None)
    IsGrabbedProperty = property(get_IsGrabbedProperty, None)
class IDropTargetPatternIdentifiers(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('11865133-a6fe-4634-bd-18-0e-f6-12-b7-b2-08')
class IDropTargetPatternIdentifiersStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('1b693304-89fb-4b0a-94-52-ca-2c-66-aa-f9-f3')
    @winrt_commethod(6)
    def get_DropTargetEffectProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_DropTargetEffectsProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    DropTargetEffectProperty = property(get_DropTargetEffectProperty, None)
    DropTargetEffectsProperty = property(get_DropTargetEffectsProperty, None)
class IExpandCollapsePatternIdentifiers(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('b006bac0-751b-4d55-92-cb-61-3e-c1-bd-f5-d0')
class IExpandCollapsePatternIdentifiersStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('d7816fd4-6ee0-4f38-8e-14-56-ef-21-ad-ac-fd')
    @winrt_commethod(6)
    def get_ExpandCollapseStateProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    ExpandCollapseStateProperty = property(get_ExpandCollapseStateProperty, None)
class IGridItemPatternIdentifiers(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('757744f1-3285-4fb1-80-3b-25-45-bd-43-15-99')
class IGridItemPatternIdentifiersStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('217d2402-5e46-4d61-87-94-b8-ee-8e-77-47-14')
    @winrt_commethod(6)
    def get_ColumnProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_ColumnSpanProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(8)
    def get_ContainingGridProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(9)
    def get_RowProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(10)
    def get_RowSpanProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    ColumnProperty = property(get_ColumnProperty, None)
    ColumnSpanProperty = property(get_ColumnSpanProperty, None)
    ContainingGridProperty = property(get_ContainingGridProperty, None)
    RowProperty = property(get_RowProperty, None)
    RowSpanProperty = property(get_RowSpanProperty, None)
class IGridPatternIdentifiers(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('c902980f-96c5-450c-90-44-7e-52-c2-4f-9e-94')
class IGridPatternIdentifiersStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('7bc452f3-a181-4137-8d-e9-1f-9b-1a-83-20-ed')
    @winrt_commethod(6)
    def get_ColumnCountProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_RowCountProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    ColumnCountProperty = property(get_ColumnCountProperty, None)
    RowCountProperty = property(get_RowCountProperty, None)
class IMultipleViewPatternIdentifiers(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('5d5cd3b8-1e12-488b-b0-ea-5e-6c-b8-98-16-e1')
class IMultipleViewPatternIdentifiersStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('a9cfa66f-6b84-4d71-9e-48-d7-64-d3-bc-da-8e')
    @winrt_commethod(6)
    def get_CurrentViewProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_SupportedViewsProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    CurrentViewProperty = property(get_CurrentViewProperty, None)
    SupportedViewsProperty = property(get_SupportedViewsProperty, None)
class IRangeValuePatternIdentifiers(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('f8760f45-33c9-467d-bc-9e-d1-51-52-63-ac-e1')
class IRangeValuePatternIdentifiersStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('ce23450f-1c27-457f-b8-15-7a-5e-46-86-3d-bb')
    @winrt_commethod(6)
    def get_IsReadOnlyProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_LargeChangeProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(8)
    def get_MaximumProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(9)
    def get_MinimumProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(10)
    def get_SmallChangeProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(11)
    def get_ValueProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    IsReadOnlyProperty = property(get_IsReadOnlyProperty, None)
    LargeChangeProperty = property(get_LargeChangeProperty, None)
    MaximumProperty = property(get_MaximumProperty, None)
    MinimumProperty = property(get_MinimumProperty, None)
    SmallChangeProperty = property(get_SmallChangeProperty, None)
    ValueProperty = property(get_ValueProperty, None)
class IScrollPatternIdentifiers(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('366b1003-425c-4951-ae-83-d5-21-e7-3b-c6-96')
class IScrollPatternIdentifiersStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('4bf8e0a1-fb7f-4fa4-83-b3-cf-ae-b1-03-a6-85')
    @winrt_commethod(6)
    def get_HorizontallyScrollableProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_HorizontalScrollPercentProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(8)
    def get_HorizontalViewSizeProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(9)
    def get_NoScroll(self) -> Double: ...
    @winrt_commethod(10)
    def get_VerticallyScrollableProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(11)
    def get_VerticalScrollPercentProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(12)
    def get_VerticalViewSizeProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    HorizontallyScrollableProperty = property(get_HorizontallyScrollableProperty, None)
    HorizontalScrollPercentProperty = property(get_HorizontalScrollPercentProperty, None)
    HorizontalViewSizeProperty = property(get_HorizontalViewSizeProperty, None)
    NoScroll = property(get_NoScroll, None)
    VerticallyScrollableProperty = property(get_VerticallyScrollableProperty, None)
    VerticalScrollPercentProperty = property(get_VerticalScrollPercentProperty, None)
    VerticalViewSizeProperty = property(get_VerticalViewSizeProperty, None)
class ISelectionItemPatternIdentifiers(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('2dafa41a-3ef8-4bb5-a0-2b-3e-e1-b2-27-47-40')
class ISelectionItemPatternIdentifiersStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('a918d163-487e-4e3e-9f-86-7b-44-ac-be-27-ce')
    @winrt_commethod(6)
    def get_IsSelectedProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_SelectionContainerProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    IsSelectedProperty = property(get_IsSelectedProperty, None)
    SelectionContainerProperty = property(get_SelectionContainerProperty, None)
class ISelectionPatternIdentifiers(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('4aa66fb0-e3f7-475f-b7-8d-f8-a8-3b-b7-30-c4')
class ISelectionPatternIdentifiersStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('93035b4c-6b50-40a1-b2-3f-5c-78-dd-bd-47-9a')
    @winrt_commethod(6)
    def get_CanSelectMultipleProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_IsSelectionRequiredProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(8)
    def get_SelectionProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    CanSelectMultipleProperty = property(get_CanSelectMultipleProperty, None)
    IsSelectionRequiredProperty = property(get_IsSelectionRequiredProperty, None)
    SelectionProperty = property(get_SelectionProperty, None)
class ISpreadsheetItemPatternIdentifiers(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('84347e19-ca4b-46a2-a7-94-c8-79-28-a3-b1-ab')
class ISpreadsheetItemPatternIdentifiersStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('43658779-5380-4f12-b4-68-b4-f3-68-ad-44-99')
    @winrt_commethod(6)
    def get_FormulaProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    FormulaProperty = property(get_FormulaProperty, None)
class IStylesPatternIdentifiers(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('b0e4e201-e89d-436b-82-87-4f-79-03-46-68-79')
class IStylesPatternIdentifiersStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('528a457a-bc3c-4d48-94-af-1f-68-70-3c-a2-96')
    @winrt_commethod(6)
    def get_ExtendedPropertiesProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_FillColorProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(8)
    def get_FillPatternColorProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(9)
    def get_FillPatternStyleProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(10)
    def get_ShapeProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(11)
    def get_StyleIdProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(12)
    def get_StyleNameProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    ExtendedPropertiesProperty = property(get_ExtendedPropertiesProperty, None)
    FillColorProperty = property(get_FillColorProperty, None)
    FillPatternColorProperty = property(get_FillPatternColorProperty, None)
    FillPatternStyleProperty = property(get_FillPatternStyleProperty, None)
    ShapeProperty = property(get_ShapeProperty, None)
    StyleIdProperty = property(get_StyleIdProperty, None)
    StyleNameProperty = property(get_StyleNameProperty, None)
class ITableItemPatternIdentifiers(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('c326e5ad-8077-4c64-98-e4-e8-3b-cf-1b-43-89')
class ITableItemPatternIdentifiersStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('24c4b923-e9a2-4de9-b2-a4-a8-b2-2d-0b-e3-62')
    @winrt_commethod(6)
    def get_ColumnHeaderItemsProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_RowHeaderItemsProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    ColumnHeaderItemsProperty = property(get_ColumnHeaderItemsProperty, None)
    RowHeaderItemsProperty = property(get_RowHeaderItemsProperty, None)
class ITablePatternIdentifiers(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('38d104fe-0d0c-412a-bf-8d-51-ed-e6-83-ba-f5')
class ITablePatternIdentifiersStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('75073d25-32c9-4903-ae-cf-dc-35-04-cb-d2-44')
    @winrt_commethod(6)
    def get_ColumnHeadersProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_RowHeadersProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(8)
    def get_RowOrColumnMajorProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    ColumnHeadersProperty = property(get_ColumnHeadersProperty, None)
    RowHeadersProperty = property(get_RowHeadersProperty, None)
    RowOrColumnMajorProperty = property(get_RowOrColumnMajorProperty, None)
class ITogglePatternIdentifiers(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('7e191f6b-34d4-4ae7-83-ac-29-f8-88-82-d9-85')
class ITogglePatternIdentifiersStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('c7f75544-14a5-4f2f-92-fc-76-05-24-de-06-ea')
    @winrt_commethod(6)
    def get_ToggleStateProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    ToggleStateProperty = property(get_ToggleStateProperty, None)
class ITransformPattern2Identifiers(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('08aaa03d-dea7-402f-80-97-9a-27-83-d6-0e-5d')
class ITransformPattern2IdentifiersStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('78963644-11f0-467c-a7-2b-5d-ac-41-c1-f6-fe')
    @winrt_commethod(6)
    def get_CanZoomProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_ZoomLevelProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(8)
    def get_MaxZoomProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(9)
    def get_MinZoomProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    CanZoomProperty = property(get_CanZoomProperty, None)
    ZoomLevelProperty = property(get_ZoomLevelProperty, None)
    MaxZoomProperty = property(get_MaxZoomProperty, None)
    MinZoomProperty = property(get_MinZoomProperty, None)
class ITransformPatternIdentifiers(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('e4115b8c-c3c8-4a37-b9-94-27-09-a7-81-16-65')
class ITransformPatternIdentifiersStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('4570edab-d705-40c4-a1-dc-e9-ac-fc-ef-85-f6')
    @winrt_commethod(6)
    def get_CanMoveProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_CanResizeProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(8)
    def get_CanRotateProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    CanMoveProperty = property(get_CanMoveProperty, None)
    CanResizeProperty = property(get_CanResizeProperty, None)
    CanRotateProperty = property(get_CanRotateProperty, None)
class IValuePatternIdentifiers(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('425bf64c-5333-4e41-b4-70-2b-ad-14-ec-d0-85')
class IValuePatternIdentifiersStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('c247e8f7-adcc-440f-b1-23-33-78-8a-40-52-5a')
    @winrt_commethod(6)
    def get_IsReadOnlyProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_ValueProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    IsReadOnlyProperty = property(get_IsReadOnlyProperty, None)
    ValueProperty = property(get_ValueProperty, None)
class IWindowPatternIdentifiers(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('39f78bb4-7032-41e2-b7-9e-27-b7-4a-86-28-de')
class IWindowPatternIdentifiersStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('07d0ad06-6302-4d29-87-8b-19-da-03-fc-22-8d')
    @winrt_commethod(6)
    def get_CanMaximizeProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(7)
    def get_CanMinimizeProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(8)
    def get_IsModalProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(9)
    def get_IsTopmostProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(10)
    def get_WindowInteractionStateProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_commethod(11)
    def get_WindowVisualStateProperty(self) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    CanMaximizeProperty = property(get_CanMaximizeProperty, None)
    CanMinimizeProperty = property(get_CanMinimizeProperty, None)
    IsModalProperty = property(get_IsModalProperty, None)
    IsTopmostProperty = property(get_IsTopmostProperty, None)
    WindowInteractionStateProperty = property(get_WindowInteractionStateProperty, None)
    WindowVisualStateProperty = property(get_WindowVisualStateProperty, None)
class MultipleViewPatternIdentifiers(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Automation.MultipleViewPatternIdentifiers'
    @winrt_classmethod
    def get_CurrentViewProperty(cls: Windows.UI.Xaml.Automation.IMultipleViewPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_SupportedViewsProperty(cls: Windows.UI.Xaml.Automation.IMultipleViewPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    CurrentViewProperty = property(get_CurrentViewProperty, None)
    SupportedViewsProperty = property(get_SupportedViewsProperty, None)
class RangeValuePatternIdentifiers(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Automation.RangeValuePatternIdentifiers'
    @winrt_classmethod
    def get_IsReadOnlyProperty(cls: Windows.UI.Xaml.Automation.IRangeValuePatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_LargeChangeProperty(cls: Windows.UI.Xaml.Automation.IRangeValuePatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_MaximumProperty(cls: Windows.UI.Xaml.Automation.IRangeValuePatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_MinimumProperty(cls: Windows.UI.Xaml.Automation.IRangeValuePatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_SmallChangeProperty(cls: Windows.UI.Xaml.Automation.IRangeValuePatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_ValueProperty(cls: Windows.UI.Xaml.Automation.IRangeValuePatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    IsReadOnlyProperty = property(get_IsReadOnlyProperty, None)
    LargeChangeProperty = property(get_LargeChangeProperty, None)
    MaximumProperty = property(get_MaximumProperty, None)
    MinimumProperty = property(get_MinimumProperty, None)
    SmallChangeProperty = property(get_SmallChangeProperty, None)
    ValueProperty = property(get_ValueProperty, None)
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
class ScrollPatternIdentifiers(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Automation.ScrollPatternIdentifiers'
    @winrt_classmethod
    def get_HorizontallyScrollableProperty(cls: Windows.UI.Xaml.Automation.IScrollPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_HorizontalScrollPercentProperty(cls: Windows.UI.Xaml.Automation.IScrollPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_HorizontalViewSizeProperty(cls: Windows.UI.Xaml.Automation.IScrollPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_NoScroll(cls: Windows.UI.Xaml.Automation.IScrollPatternIdentifiersStatics) -> Double: ...
    @winrt_classmethod
    def get_VerticallyScrollableProperty(cls: Windows.UI.Xaml.Automation.IScrollPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_VerticalScrollPercentProperty(cls: Windows.UI.Xaml.Automation.IScrollPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_VerticalViewSizeProperty(cls: Windows.UI.Xaml.Automation.IScrollPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    HorizontallyScrollableProperty = property(get_HorizontallyScrollableProperty, None)
    HorizontalScrollPercentProperty = property(get_HorizontalScrollPercentProperty, None)
    HorizontalViewSizeProperty = property(get_HorizontalViewSizeProperty, None)
    NoScroll = property(get_NoScroll, None)
    VerticallyScrollableProperty = property(get_VerticallyScrollableProperty, None)
    VerticalScrollPercentProperty = property(get_VerticalScrollPercentProperty, None)
    VerticalViewSizeProperty = property(get_VerticalViewSizeProperty, None)
class SelectionItemPatternIdentifiers(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Automation.SelectionItemPatternIdentifiers'
    @winrt_classmethod
    def get_IsSelectedProperty(cls: Windows.UI.Xaml.Automation.ISelectionItemPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_SelectionContainerProperty(cls: Windows.UI.Xaml.Automation.ISelectionItemPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    IsSelectedProperty = property(get_IsSelectedProperty, None)
    SelectionContainerProperty = property(get_SelectionContainerProperty, None)
class SelectionPatternIdentifiers(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Automation.SelectionPatternIdentifiers'
    @winrt_classmethod
    def get_CanSelectMultipleProperty(cls: Windows.UI.Xaml.Automation.ISelectionPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_IsSelectionRequiredProperty(cls: Windows.UI.Xaml.Automation.ISelectionPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_SelectionProperty(cls: Windows.UI.Xaml.Automation.ISelectionPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    CanSelectMultipleProperty = property(get_CanSelectMultipleProperty, None)
    IsSelectionRequiredProperty = property(get_IsSelectionRequiredProperty, None)
    SelectionProperty = property(get_SelectionProperty, None)
class SpreadsheetItemPatternIdentifiers(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Automation.SpreadsheetItemPatternIdentifiers'
    @winrt_classmethod
    def get_FormulaProperty(cls: Windows.UI.Xaml.Automation.ISpreadsheetItemPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    FormulaProperty = property(get_FormulaProperty, None)
class StylesPatternIdentifiers(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Automation.StylesPatternIdentifiers'
    @winrt_classmethod
    def get_ExtendedPropertiesProperty(cls: Windows.UI.Xaml.Automation.IStylesPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_FillColorProperty(cls: Windows.UI.Xaml.Automation.IStylesPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_FillPatternColorProperty(cls: Windows.UI.Xaml.Automation.IStylesPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_FillPatternStyleProperty(cls: Windows.UI.Xaml.Automation.IStylesPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_ShapeProperty(cls: Windows.UI.Xaml.Automation.IStylesPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_StyleIdProperty(cls: Windows.UI.Xaml.Automation.IStylesPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_StyleNameProperty(cls: Windows.UI.Xaml.Automation.IStylesPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    ExtendedPropertiesProperty = property(get_ExtendedPropertiesProperty, None)
    FillColorProperty = property(get_FillColorProperty, None)
    FillPatternColorProperty = property(get_FillPatternColorProperty, None)
    FillPatternStyleProperty = property(get_FillPatternStyleProperty, None)
    ShapeProperty = property(get_ShapeProperty, None)
    StyleIdProperty = property(get_StyleIdProperty, None)
    StyleNameProperty = property(get_StyleNameProperty, None)
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
class TableItemPatternIdentifiers(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Automation.TableItemPatternIdentifiers'
    @winrt_classmethod
    def get_ColumnHeaderItemsProperty(cls: Windows.UI.Xaml.Automation.ITableItemPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_RowHeaderItemsProperty(cls: Windows.UI.Xaml.Automation.ITableItemPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    ColumnHeaderItemsProperty = property(get_ColumnHeaderItemsProperty, None)
    RowHeaderItemsProperty = property(get_RowHeaderItemsProperty, None)
class TablePatternIdentifiers(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Automation.TablePatternIdentifiers'
    @winrt_classmethod
    def get_ColumnHeadersProperty(cls: Windows.UI.Xaml.Automation.ITablePatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_RowHeadersProperty(cls: Windows.UI.Xaml.Automation.ITablePatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_RowOrColumnMajorProperty(cls: Windows.UI.Xaml.Automation.ITablePatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    ColumnHeadersProperty = property(get_ColumnHeadersProperty, None)
    RowHeadersProperty = property(get_RowHeadersProperty, None)
    RowOrColumnMajorProperty = property(get_RowOrColumnMajorProperty, None)
class TogglePatternIdentifiers(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Automation.TogglePatternIdentifiers'
    @winrt_classmethod
    def get_ToggleStateProperty(cls: Windows.UI.Xaml.Automation.ITogglePatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    ToggleStateProperty = property(get_ToggleStateProperty, None)
ToggleState = Int32
ToggleState_Off: ToggleState = 0
ToggleState_On: ToggleState = 1
ToggleState_Indeterminate: ToggleState = 2
class TransformPattern2Identifiers(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Automation.TransformPattern2Identifiers'
    @winrt_classmethod
    def get_CanZoomProperty(cls: Windows.UI.Xaml.Automation.ITransformPattern2IdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_ZoomLevelProperty(cls: Windows.UI.Xaml.Automation.ITransformPattern2IdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_MaxZoomProperty(cls: Windows.UI.Xaml.Automation.ITransformPattern2IdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_MinZoomProperty(cls: Windows.UI.Xaml.Automation.ITransformPattern2IdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    CanZoomProperty = property(get_CanZoomProperty, None)
    ZoomLevelProperty = property(get_ZoomLevelProperty, None)
    MaxZoomProperty = property(get_MaxZoomProperty, None)
    MinZoomProperty = property(get_MinZoomProperty, None)
class TransformPatternIdentifiers(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Automation.TransformPatternIdentifiers'
    @winrt_classmethod
    def get_CanMoveProperty(cls: Windows.UI.Xaml.Automation.ITransformPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_CanResizeProperty(cls: Windows.UI.Xaml.Automation.ITransformPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_CanRotateProperty(cls: Windows.UI.Xaml.Automation.ITransformPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    CanMoveProperty = property(get_CanMoveProperty, None)
    CanResizeProperty = property(get_CanResizeProperty, None)
    CanRotateProperty = property(get_CanRotateProperty, None)
class ValuePatternIdentifiers(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Automation.ValuePatternIdentifiers'
    @winrt_classmethod
    def get_IsReadOnlyProperty(cls: Windows.UI.Xaml.Automation.IValuePatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_ValueProperty(cls: Windows.UI.Xaml.Automation.IValuePatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    IsReadOnlyProperty = property(get_IsReadOnlyProperty, None)
    ValueProperty = property(get_ValueProperty, None)
WindowInteractionState = Int32
WindowInteractionState_Running: WindowInteractionState = 0
WindowInteractionState_Closing: WindowInteractionState = 1
WindowInteractionState_ReadyForUserInteraction: WindowInteractionState = 2
WindowInteractionState_BlockedByModalWindow: WindowInteractionState = 3
WindowInteractionState_NotResponding: WindowInteractionState = 4
class WindowPatternIdentifiers(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Automation.WindowPatternIdentifiers'
    @winrt_classmethod
    def get_CanMaximizeProperty(cls: Windows.UI.Xaml.Automation.IWindowPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_CanMinimizeProperty(cls: Windows.UI.Xaml.Automation.IWindowPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_IsModalProperty(cls: Windows.UI.Xaml.Automation.IWindowPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_IsTopmostProperty(cls: Windows.UI.Xaml.Automation.IWindowPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_WindowInteractionStateProperty(cls: Windows.UI.Xaml.Automation.IWindowPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    @winrt_classmethod
    def get_WindowVisualStateProperty(cls: Windows.UI.Xaml.Automation.IWindowPatternIdentifiersStatics) -> Windows.UI.Xaml.Automation.AutomationProperty: ...
    CanMaximizeProperty = property(get_CanMaximizeProperty, None)
    CanMinimizeProperty = property(get_CanMinimizeProperty, None)
    IsModalProperty = property(get_IsModalProperty, None)
    IsTopmostProperty = property(get_IsTopmostProperty, None)
    WindowInteractionStateProperty = property(get_WindowInteractionStateProperty, None)
    WindowVisualStateProperty = property(get_WindowVisualStateProperty, None)
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
