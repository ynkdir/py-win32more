from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation.Collections
import win32more.Windows.UI.Xaml
import win32more.Windows.UI.Xaml.Automation
import win32more.Windows.UI.Xaml.Automation.Peers
import win32more.Windows.Win32.System.WinRT
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
    _AnnotationPatternIdentifiers_Meta_.AnnotationTypeIdProperty = property(get_AnnotationTypeIdProperty, None)
    _AnnotationPatternIdentifiers_Meta_.AnnotationTypeNameProperty = property(get_AnnotationTypeNameProperty, None)
    _AnnotationPatternIdentifiers_Meta_.AuthorProperty = property(get_AuthorProperty, None)
    _AnnotationPatternIdentifiers_Meta_.DateTimeProperty = property(get_DateTimeProperty, None)
    _AnnotationPatternIdentifiers_Meta_.TargetProperty = property(get_TargetProperty, None)
class AnnotationType(Enum, Int32):
    Unknown = 60000
    SpellingError = 60001
    GrammarError = 60002
    Comment = 60003
    FormulaError = 60004
    TrackChanges = 60005
    Header = 60006
    Footer = 60007
    Highlighted = 60008
    Endnote = 60009
    Footnote = 60010
    InsertionChange = 60011
    DeletionChange = 60012
    MoveChange = 60013
    FormatChange = 60014
    UnsyncedChange = 60015
    EditingLockedChange = 60016
    ExternalChange = 60017
    ConflictingChange = 60018
    Author = 60019
    AdvancedProofingIssue = 60020
    DataValidationError = 60021
    CircularReferenceError = 60022
class AutomationActiveEnd(Enum, Int32):
    None_ = 0
    Start = 1
    End = 2
class AutomationAnimationStyle(Enum, Int32):
    None_ = 0
    LasVegasLights = 1
    BlinkingBackground = 2
    SparkleText = 3
    MarchingBlackAnts = 4
    MarchingRedAnts = 5
    Shimmer = 6
    Other = 7
class _AutomationAnnotation_Meta_(ComPtr.__class__):
    pass
class AutomationAnnotation(ComPtr, metaclass=_AutomationAnnotation_Meta_):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Automation.IAutomationAnnotation
    _classid_ = 'Windows.UI.Xaml.Automation.AutomationAnnotation'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Automation.AutomationAnnotation.CreateInstance(*args))
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.UI.Xaml.Automation.AutomationAnnotation.CreateInstance(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.UI.Xaml.Automation.AutomationAnnotation.CreateWithElementParameter(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_overload
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Automation.AutomationAnnotation: ...
    @CreateInstance.register
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
    Element = property(get_Element, put_Element)
    Type = property(get_Type, put_Type)
    _AutomationAnnotation_Meta_.ElementProperty = property(get_ElementProperty, None)
    _AutomationAnnotation_Meta_.TypeProperty = property(get_TypeProperty, None)
class AutomationBulletStyle(Enum, Int32):
    None_ = 0
    HollowRoundBullet = 1
    FilledRoundBullet = 2
    HollowSquareBullet = 3
    FilledSquareBullet = 4
    DashBullet = 5
    Other = 6
class AutomationCaretBidiMode(Enum, Int32):
    LTR = 0
    RTL = 1
class AutomationCaretPosition(Enum, Int32):
    Unknown = 0
    EndOfLine = 1
    BeginningOfLine = 2
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
    _AutomationElementIdentifiers_Meta_.AcceleratorKeyProperty = property(get_AcceleratorKeyProperty, None)
    _AutomationElementIdentifiers_Meta_.AccessKeyProperty = property(get_AccessKeyProperty, None)
    _AutomationElementIdentifiers_Meta_.AnnotationsProperty = property(get_AnnotationsProperty, None)
    _AutomationElementIdentifiers_Meta_.AutomationIdProperty = property(get_AutomationIdProperty, None)
    _AutomationElementIdentifiers_Meta_.BoundingRectangleProperty = property(get_BoundingRectangleProperty, None)
    _AutomationElementIdentifiers_Meta_.ClassNameProperty = property(get_ClassNameProperty, None)
    _AutomationElementIdentifiers_Meta_.ClickablePointProperty = property(get_ClickablePointProperty, None)
    _AutomationElementIdentifiers_Meta_.ControlTypeProperty = property(get_ControlTypeProperty, None)
    _AutomationElementIdentifiers_Meta_.ControlledPeersProperty = property(get_ControlledPeersProperty, None)
    _AutomationElementIdentifiers_Meta_.CultureProperty = property(get_CultureProperty, None)
    _AutomationElementIdentifiers_Meta_.DescribedByProperty = property(get_DescribedByProperty, None)
    _AutomationElementIdentifiers_Meta_.FlowsFromProperty = property(get_FlowsFromProperty, None)
    _AutomationElementIdentifiers_Meta_.FlowsToProperty = property(get_FlowsToProperty, None)
    _AutomationElementIdentifiers_Meta_.FullDescriptionProperty = property(get_FullDescriptionProperty, None)
    _AutomationElementIdentifiers_Meta_.HasKeyboardFocusProperty = property(get_HasKeyboardFocusProperty, None)
    _AutomationElementIdentifiers_Meta_.HeadingLevelProperty = property(get_HeadingLevelProperty, None)
    _AutomationElementIdentifiers_Meta_.HelpTextProperty = property(get_HelpTextProperty, None)
    _AutomationElementIdentifiers_Meta_.IsContentElementProperty = property(get_IsContentElementProperty, None)
    _AutomationElementIdentifiers_Meta_.IsControlElementProperty = property(get_IsControlElementProperty, None)
    _AutomationElementIdentifiers_Meta_.IsDataValidForFormProperty = property(get_IsDataValidForFormProperty, None)
    _AutomationElementIdentifiers_Meta_.IsDialogProperty = property(get_IsDialogProperty, None)
    _AutomationElementIdentifiers_Meta_.IsEnabledProperty = property(get_IsEnabledProperty, None)
    _AutomationElementIdentifiers_Meta_.IsKeyboardFocusableProperty = property(get_IsKeyboardFocusableProperty, None)
    _AutomationElementIdentifiers_Meta_.IsOffscreenProperty = property(get_IsOffscreenProperty, None)
    _AutomationElementIdentifiers_Meta_.IsPasswordProperty = property(get_IsPasswordProperty, None)
    _AutomationElementIdentifiers_Meta_.IsPeripheralProperty = property(get_IsPeripheralProperty, None)
    _AutomationElementIdentifiers_Meta_.IsRequiredForFormProperty = property(get_IsRequiredForFormProperty, None)
    _AutomationElementIdentifiers_Meta_.ItemStatusProperty = property(get_ItemStatusProperty, None)
    _AutomationElementIdentifiers_Meta_.ItemTypeProperty = property(get_ItemTypeProperty, None)
    _AutomationElementIdentifiers_Meta_.LabeledByProperty = property(get_LabeledByProperty, None)
    _AutomationElementIdentifiers_Meta_.LandmarkTypeProperty = property(get_LandmarkTypeProperty, None)
    _AutomationElementIdentifiers_Meta_.LevelProperty = property(get_LevelProperty, None)
    _AutomationElementIdentifiers_Meta_.LiveSettingProperty = property(get_LiveSettingProperty, None)
    _AutomationElementIdentifiers_Meta_.LocalizedControlTypeProperty = property(get_LocalizedControlTypeProperty, None)
    _AutomationElementIdentifiers_Meta_.LocalizedLandmarkTypeProperty = property(get_LocalizedLandmarkTypeProperty, None)
    _AutomationElementIdentifiers_Meta_.NameProperty = property(get_NameProperty, None)
    _AutomationElementIdentifiers_Meta_.OrientationProperty = property(get_OrientationProperty, None)
    _AutomationElementIdentifiers_Meta_.PositionInSetProperty = property(get_PositionInSetProperty, None)
    _AutomationElementIdentifiers_Meta_.SizeOfSetProperty = property(get_SizeOfSetProperty, None)
class AutomationFlowDirections(Enum, Int32):
    Default = 0
    RightToLeft = 1
    BottomToTop = 2
    Vertical = 3
class AutomationOutlineStyles(Enum, Int32):
    None_ = 0
    Outline = 1
    Shadow = 2
    Engraved = 3
    Embossed = 4
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
    _AutomationProperties_Meta_.AcceleratorKeyProperty = property(get_AcceleratorKeyProperty, None)
    _AutomationProperties_Meta_.AccessKeyProperty = property(get_AccessKeyProperty, None)
    _AutomationProperties_Meta_.AccessibilityViewProperty = property(get_AccessibilityViewProperty, None)
    _AutomationProperties_Meta_.AnnotationsProperty = property(get_AnnotationsProperty, None)
    _AutomationProperties_Meta_.AutomationControlTypeProperty = property(get_AutomationControlTypeProperty, None)
    _AutomationProperties_Meta_.AutomationIdProperty = property(get_AutomationIdProperty, None)
    _AutomationProperties_Meta_.ControlledPeersProperty = property(get_ControlledPeersProperty, None)
    _AutomationProperties_Meta_.CultureProperty = property(get_CultureProperty, None)
    _AutomationProperties_Meta_.DescribedByProperty = property(get_DescribedByProperty, None)
    _AutomationProperties_Meta_.FlowsFromProperty = property(get_FlowsFromProperty, None)
    _AutomationProperties_Meta_.FlowsToProperty = property(get_FlowsToProperty, None)
    _AutomationProperties_Meta_.FullDescriptionProperty = property(get_FullDescriptionProperty, None)
    _AutomationProperties_Meta_.HeadingLevelProperty = property(get_HeadingLevelProperty, None)
    _AutomationProperties_Meta_.HelpTextProperty = property(get_HelpTextProperty, None)
    _AutomationProperties_Meta_.IsDataValidForFormProperty = property(get_IsDataValidForFormProperty, None)
    _AutomationProperties_Meta_.IsDialogProperty = property(get_IsDialogProperty, None)
    _AutomationProperties_Meta_.IsPeripheralProperty = property(get_IsPeripheralProperty, None)
    _AutomationProperties_Meta_.IsRequiredForFormProperty = property(get_IsRequiredForFormProperty, None)
    _AutomationProperties_Meta_.ItemStatusProperty = property(get_ItemStatusProperty, None)
    _AutomationProperties_Meta_.ItemTypeProperty = property(get_ItemTypeProperty, None)
    _AutomationProperties_Meta_.LabeledByProperty = property(get_LabeledByProperty, None)
    _AutomationProperties_Meta_.LandmarkTypeProperty = property(get_LandmarkTypeProperty, None)
    _AutomationProperties_Meta_.LevelProperty = property(get_LevelProperty, None)
    _AutomationProperties_Meta_.LiveSettingProperty = property(get_LiveSettingProperty, None)
    _AutomationProperties_Meta_.LocalizedControlTypeProperty = property(get_LocalizedControlTypeProperty, None)
    _AutomationProperties_Meta_.LocalizedLandmarkTypeProperty = property(get_LocalizedLandmarkTypeProperty, None)
    _AutomationProperties_Meta_.NameProperty = property(get_NameProperty, None)
    _AutomationProperties_Meta_.PositionInSetProperty = property(get_PositionInSetProperty, None)
    _AutomationProperties_Meta_.SizeOfSetProperty = property(get_SizeOfSetProperty, None)
class AutomationProperty(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Automation.IAutomationProperty
    _classid_ = 'Windows.UI.Xaml.Automation.AutomationProperty'
class AutomationStyleId(Enum, Int32):
    Heading1 = 70001
    Heading2 = 70002
    Heading3 = 70003
    Heading4 = 70004
    Heading5 = 70005
    Heading6 = 70006
    Heading7 = 70007
    Heading8 = 70008
    Heading9 = 70009
    Title = 70010
    Subtitle = 70011
    Normal = 70012
    Emphasis = 70013
    Quote = 70014
    BulletedList = 70015
class AutomationTextDecorationLineStyle(Enum, Int32):
    None_ = 0
    Single = 1
    WordsOnly = 2
    Double = 3
    Dot = 4
    Dash = 5
    DashDot = 6
    DashDotDot = 7
    Wavy = 8
    ThickSingle = 9
    DoubleWavy = 10
    ThickWavy = 11
    LongDash = 12
    ThickDash = 13
    ThickDashDot = 14
    ThickDashDotDot = 15
    ThickDot = 16
    ThickLongDash = 17
    Other = 18
class AutomationTextEditChangeType(Enum, Int32):
    None_ = 0
    AutoCorrect = 1
    Composition = 2
    CompositionFinalized = 3
class _DockPatternIdentifiers_Meta_(ComPtr.__class__):
    pass
class DockPatternIdentifiers(ComPtr, metaclass=_DockPatternIdentifiers_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Automation.IDockPatternIdentifiers
    _classid_ = 'Windows.UI.Xaml.Automation.DockPatternIdentifiers'
    @winrt_classmethod
    def get_DockPositionProperty(cls: win32more.Windows.UI.Xaml.Automation.IDockPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    _DockPatternIdentifiers_Meta_.DockPositionProperty = property(get_DockPositionProperty, None)
class DockPosition(Enum, Int32):
    Top = 0
    Left = 1
    Bottom = 2
    Right = 3
    Fill = 4
    None_ = 5
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
    _DragPatternIdentifiers_Meta_.DropEffectProperty = property(get_DropEffectProperty, None)
    _DragPatternIdentifiers_Meta_.DropEffectsProperty = property(get_DropEffectsProperty, None)
    _DragPatternIdentifiers_Meta_.GrabbedItemsProperty = property(get_GrabbedItemsProperty, None)
    _DragPatternIdentifiers_Meta_.IsGrabbedProperty = property(get_IsGrabbedProperty, None)
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
    _DropTargetPatternIdentifiers_Meta_.DropTargetEffectProperty = property(get_DropTargetEffectProperty, None)
    _DropTargetPatternIdentifiers_Meta_.DropTargetEffectsProperty = property(get_DropTargetEffectsProperty, None)
class _ExpandCollapsePatternIdentifiers_Meta_(ComPtr.__class__):
    pass
class ExpandCollapsePatternIdentifiers(ComPtr, metaclass=_ExpandCollapsePatternIdentifiers_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Automation.IExpandCollapsePatternIdentifiers
    _classid_ = 'Windows.UI.Xaml.Automation.ExpandCollapsePatternIdentifiers'
    @winrt_classmethod
    def get_ExpandCollapseStateProperty(cls: win32more.Windows.UI.Xaml.Automation.IExpandCollapsePatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    _ExpandCollapsePatternIdentifiers_Meta_.ExpandCollapseStateProperty = property(get_ExpandCollapseStateProperty, None)
class ExpandCollapseState(Enum, Int32):
    Collapsed = 0
    Expanded = 1
    PartiallyExpanded = 2
    LeafNode = 3
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
    _GridItemPatternIdentifiers_Meta_.ColumnProperty = property(get_ColumnProperty, None)
    _GridItemPatternIdentifiers_Meta_.ColumnSpanProperty = property(get_ColumnSpanProperty, None)
    _GridItemPatternIdentifiers_Meta_.ContainingGridProperty = property(get_ContainingGridProperty, None)
    _GridItemPatternIdentifiers_Meta_.RowProperty = property(get_RowProperty, None)
    _GridItemPatternIdentifiers_Meta_.RowSpanProperty = property(get_RowSpanProperty, None)
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
    _GridPatternIdentifiers_Meta_.ColumnCountProperty = property(get_ColumnCountProperty, None)
    _GridPatternIdentifiers_Meta_.RowCountProperty = property(get_RowCountProperty, None)
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
    Element = property(get_Element, put_Element)
    Type = property(get_Type, put_Type)
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
    ElementProperty = property(get_ElementProperty, None)
    TypeProperty = property(get_TypeProperty, None)
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
    LiveSettingProperty = property(get_LiveSettingProperty, None)
    LocalizedControlTypeProperty = property(get_LocalizedControlTypeProperty, None)
    NameProperty = property(get_NameProperty, None)
    OrientationProperty = property(get_OrientationProperty, None)
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
    AnnotationsProperty = property(get_AnnotationsProperty, None)
    LevelProperty = property(get_LevelProperty, None)
    PositionInSetProperty = property(get_PositionInSetProperty, None)
    SizeOfSetProperty = property(get_SizeOfSetProperty, None)
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
    DescribedByProperty = property(get_DescribedByProperty, None)
    FlowsFromProperty = property(get_FlowsFromProperty, None)
    FlowsToProperty = property(get_FlowsToProperty, None)
    FullDescriptionProperty = property(get_FullDescriptionProperty, None)
    IsDataValidForFormProperty = property(get_IsDataValidForFormProperty, None)
    IsPeripheralProperty = property(get_IsPeripheralProperty, None)
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
    LiveSettingProperty = property(get_LiveSettingProperty, None)
    NameProperty = property(get_NameProperty, None)
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
    AnnotationsProperty = property(get_AnnotationsProperty, None)
    LevelProperty = property(get_LevelProperty, None)
    PositionInSetProperty = property(get_PositionInSetProperty, None)
    SizeOfSetProperty = property(get_SizeOfSetProperty, None)
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
    DescribedByProperty = property(get_DescribedByProperty, None)
    FlowsFromProperty = property(get_FlowsFromProperty, None)
    FlowsToProperty = property(get_FlowsToProperty, None)
    FullDescriptionProperty = property(get_FullDescriptionProperty, None)
    IsDataValidForFormProperty = property(get_IsDataValidForFormProperty, None)
    IsPeripheralProperty = property(get_IsPeripheralProperty, None)
    LocalizedControlTypeProperty = property(get_LocalizedControlTypeProperty, None)
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
    HorizontalScrollPercentProperty = property(get_HorizontalScrollPercentProperty, None)
    HorizontalViewSizeProperty = property(get_HorizontalViewSizeProperty, None)
    HorizontallyScrollableProperty = property(get_HorizontallyScrollableProperty, None)
    NoScroll = property(get_NoScroll, None)
    VerticalScrollPercentProperty = property(get_VerticalScrollPercentProperty, None)
    VerticalViewSizeProperty = property(get_VerticalViewSizeProperty, None)
    VerticallyScrollableProperty = property(get_VerticallyScrollableProperty, None)
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
    MaxZoomProperty = property(get_MaxZoomProperty, None)
    MinZoomProperty = property(get_MinZoomProperty, None)
    ZoomLevelProperty = property(get_ZoomLevelProperty, None)
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
    _MultipleViewPatternIdentifiers_Meta_.CurrentViewProperty = property(get_CurrentViewProperty, None)
    _MultipleViewPatternIdentifiers_Meta_.SupportedViewsProperty = property(get_SupportedViewsProperty, None)
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
    _RangeValuePatternIdentifiers_Meta_.IsReadOnlyProperty = property(get_IsReadOnlyProperty, None)
    _RangeValuePatternIdentifiers_Meta_.LargeChangeProperty = property(get_LargeChangeProperty, None)
    _RangeValuePatternIdentifiers_Meta_.MaximumProperty = property(get_MaximumProperty, None)
    _RangeValuePatternIdentifiers_Meta_.MinimumProperty = property(get_MinimumProperty, None)
    _RangeValuePatternIdentifiers_Meta_.SmallChangeProperty = property(get_SmallChangeProperty, None)
    _RangeValuePatternIdentifiers_Meta_.ValueProperty = property(get_ValueProperty, None)
class RowOrColumnMajor(Enum, Int32):
    RowMajor = 0
    ColumnMajor = 1
    Indeterminate = 2
class ScrollAmount(Enum, Int32):
    LargeDecrement = 0
    SmallDecrement = 1
    NoAmount = 2
    LargeIncrement = 3
    SmallIncrement = 4
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
    _ScrollPatternIdentifiers_Meta_.HorizontalScrollPercentProperty = property(get_HorizontalScrollPercentProperty, None)
    _ScrollPatternIdentifiers_Meta_.HorizontalViewSizeProperty = property(get_HorizontalViewSizeProperty, None)
    _ScrollPatternIdentifiers_Meta_.HorizontallyScrollableProperty = property(get_HorizontallyScrollableProperty, None)
    _ScrollPatternIdentifiers_Meta_.NoScroll = property(get_NoScroll, None)
    _ScrollPatternIdentifiers_Meta_.VerticalScrollPercentProperty = property(get_VerticalScrollPercentProperty, None)
    _ScrollPatternIdentifiers_Meta_.VerticalViewSizeProperty = property(get_VerticalViewSizeProperty, None)
    _ScrollPatternIdentifiers_Meta_.VerticallyScrollableProperty = property(get_VerticallyScrollableProperty, None)
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
    _SelectionItemPatternIdentifiers_Meta_.IsSelectedProperty = property(get_IsSelectedProperty, None)
    _SelectionItemPatternIdentifiers_Meta_.SelectionContainerProperty = property(get_SelectionContainerProperty, None)
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
    _SelectionPatternIdentifiers_Meta_.CanSelectMultipleProperty = property(get_CanSelectMultipleProperty, None)
    _SelectionPatternIdentifiers_Meta_.IsSelectionRequiredProperty = property(get_IsSelectionRequiredProperty, None)
    _SelectionPatternIdentifiers_Meta_.SelectionProperty = property(get_SelectionProperty, None)
class _SpreadsheetItemPatternIdentifiers_Meta_(ComPtr.__class__):
    pass
class SpreadsheetItemPatternIdentifiers(ComPtr, metaclass=_SpreadsheetItemPatternIdentifiers_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Automation.ISpreadsheetItemPatternIdentifiers
    _classid_ = 'Windows.UI.Xaml.Automation.SpreadsheetItemPatternIdentifiers'
    @winrt_classmethod
    def get_FormulaProperty(cls: win32more.Windows.UI.Xaml.Automation.ISpreadsheetItemPatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    _SpreadsheetItemPatternIdentifiers_Meta_.FormulaProperty = property(get_FormulaProperty, None)
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
    _StylesPatternIdentifiers_Meta_.ExtendedPropertiesProperty = property(get_ExtendedPropertiesProperty, None)
    _StylesPatternIdentifiers_Meta_.FillColorProperty = property(get_FillColorProperty, None)
    _StylesPatternIdentifiers_Meta_.FillPatternColorProperty = property(get_FillPatternColorProperty, None)
    _StylesPatternIdentifiers_Meta_.FillPatternStyleProperty = property(get_FillPatternStyleProperty, None)
    _StylesPatternIdentifiers_Meta_.ShapeProperty = property(get_ShapeProperty, None)
    _StylesPatternIdentifiers_Meta_.StyleIdProperty = property(get_StyleIdProperty, None)
    _StylesPatternIdentifiers_Meta_.StyleNameProperty = property(get_StyleNameProperty, None)
class SupportedTextSelection(Enum, Int32):
    None_ = 0
    Single = 1
    Multiple = 2
class SynchronizedInputType(Enum, Int32):
    KeyUp = 1
    KeyDown = 2
    LeftMouseUp = 4
    LeftMouseDown = 8
    RightMouseUp = 16
    RightMouseDown = 32
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
    _TableItemPatternIdentifiers_Meta_.ColumnHeaderItemsProperty = property(get_ColumnHeaderItemsProperty, None)
    _TableItemPatternIdentifiers_Meta_.RowHeaderItemsProperty = property(get_RowHeaderItemsProperty, None)
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
    _TablePatternIdentifiers_Meta_.ColumnHeadersProperty = property(get_ColumnHeadersProperty, None)
    _TablePatternIdentifiers_Meta_.RowHeadersProperty = property(get_RowHeadersProperty, None)
    _TablePatternIdentifiers_Meta_.RowOrColumnMajorProperty = property(get_RowOrColumnMajorProperty, None)
class _TogglePatternIdentifiers_Meta_(ComPtr.__class__):
    pass
class TogglePatternIdentifiers(ComPtr, metaclass=_TogglePatternIdentifiers_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Automation.ITogglePatternIdentifiers
    _classid_ = 'Windows.UI.Xaml.Automation.TogglePatternIdentifiers'
    @winrt_classmethod
    def get_ToggleStateProperty(cls: win32more.Windows.UI.Xaml.Automation.ITogglePatternIdentifiersStatics) -> win32more.Windows.UI.Xaml.Automation.AutomationProperty: ...
    _TogglePatternIdentifiers_Meta_.ToggleStateProperty = property(get_ToggleStateProperty, None)
class ToggleState(Enum, Int32):
    Off = 0
    On = 1
    Indeterminate = 2
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
    _TransformPattern2Identifiers_Meta_.CanZoomProperty = property(get_CanZoomProperty, None)
    _TransformPattern2Identifiers_Meta_.MaxZoomProperty = property(get_MaxZoomProperty, None)
    _TransformPattern2Identifiers_Meta_.MinZoomProperty = property(get_MinZoomProperty, None)
    _TransformPattern2Identifiers_Meta_.ZoomLevelProperty = property(get_ZoomLevelProperty, None)
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
    _TransformPatternIdentifiers_Meta_.CanMoveProperty = property(get_CanMoveProperty, None)
    _TransformPatternIdentifiers_Meta_.CanResizeProperty = property(get_CanResizeProperty, None)
    _TransformPatternIdentifiers_Meta_.CanRotateProperty = property(get_CanRotateProperty, None)
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
    _ValuePatternIdentifiers_Meta_.IsReadOnlyProperty = property(get_IsReadOnlyProperty, None)
    _ValuePatternIdentifiers_Meta_.ValueProperty = property(get_ValueProperty, None)
class WindowInteractionState(Enum, Int32):
    Running = 0
    Closing = 1
    ReadyForUserInteraction = 2
    BlockedByModalWindow = 3
    NotResponding = 4
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
    _WindowPatternIdentifiers_Meta_.CanMaximizeProperty = property(get_CanMaximizeProperty, None)
    _WindowPatternIdentifiers_Meta_.CanMinimizeProperty = property(get_CanMinimizeProperty, None)
    _WindowPatternIdentifiers_Meta_.IsModalProperty = property(get_IsModalProperty, None)
    _WindowPatternIdentifiers_Meta_.IsTopmostProperty = property(get_IsTopmostProperty, None)
    _WindowPatternIdentifiers_Meta_.WindowInteractionStateProperty = property(get_WindowInteractionStateProperty, None)
    _WindowPatternIdentifiers_Meta_.WindowVisualStateProperty = property(get_WindowVisualStateProperty, None)
class WindowVisualState(Enum, Int32):
    Normal = 0
    Maximized = 1
    Minimized = 2
class ZoomUnit(Enum, Int32):
    NoAmount = 0
    LargeDecrement = 1
    SmallDecrement = 2
    LargeIncrement = 3
    SmallIncrement = 4


make_ready(__name__)
