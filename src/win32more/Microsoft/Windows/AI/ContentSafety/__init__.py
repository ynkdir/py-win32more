from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Microsoft.Windows.AI.ContentSafety
class ContentFilterOptions(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.AI.ContentSafety.IContentFilterOptions
    _classid_ = 'Microsoft.Windows.AI.ContentSafety.ContentFilterOptions'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.Windows.AI.ContentSafety.ContentFilterOptions.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.Windows.AI.ContentSafety.ContentFilterOptions: ...
    @winrt_mixinmethod
    def get_PromptMaxAllowedSeverityLevel(self: win32more.Microsoft.Windows.AI.ContentSafety.IContentFilterOptions) -> win32more.Microsoft.Windows.AI.ContentSafety.TextContentFilterSeverity: ...
    @winrt_mixinmethod
    def put_PromptMaxAllowedSeverityLevel(self: win32more.Microsoft.Windows.AI.ContentSafety.IContentFilterOptions, value: win32more.Microsoft.Windows.AI.ContentSafety.TextContentFilterSeverity) -> Void: ...
    @winrt_mixinmethod
    def get_ResponseMaxAllowedSeverityLevel(self: win32more.Microsoft.Windows.AI.ContentSafety.IContentFilterOptions) -> win32more.Microsoft.Windows.AI.ContentSafety.TextContentFilterSeverity: ...
    @winrt_mixinmethod
    def put_ResponseMaxAllowedSeverityLevel(self: win32more.Microsoft.Windows.AI.ContentSafety.IContentFilterOptions, value: win32more.Microsoft.Windows.AI.ContentSafety.TextContentFilterSeverity) -> Void: ...
    @winrt_mixinmethod
    def get_ImageMaxAllowedSeverityLevel(self: win32more.Microsoft.Windows.AI.ContentSafety.IContentFilterOptions) -> win32more.Microsoft.Windows.AI.ContentSafety.ImageContentFilterSeverity: ...
    @winrt_mixinmethod
    def put_ImageMaxAllowedSeverityLevel(self: win32more.Microsoft.Windows.AI.ContentSafety.IContentFilterOptions, value: win32more.Microsoft.Windows.AI.ContentSafety.ImageContentFilterSeverity) -> Void: ...
    ImageMaxAllowedSeverityLevel = property(get_ImageMaxAllowedSeverityLevel, put_ImageMaxAllowedSeverityLevel)
    PromptMaxAllowedSeverityLevel = property(get_PromptMaxAllowedSeverityLevel, put_PromptMaxAllowedSeverityLevel)
    ResponseMaxAllowedSeverityLevel = property(get_ResponseMaxAllowedSeverityLevel, put_ResponseMaxAllowedSeverityLevel)
ContentSafetyContract: UInt32 = 65536
class IContentFilterOptions(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.ContentSafety.IContentFilterOptions'
    _iid_ = Guid('{6808be9f-80d2-5136-8a8a-1f5c52c824ad}')
    @winrt_commethod(6)
    def get_PromptMaxAllowedSeverityLevel(self) -> win32more.Microsoft.Windows.AI.ContentSafety.TextContentFilterSeverity: ...
    @winrt_commethod(7)
    def put_PromptMaxAllowedSeverityLevel(self, value: win32more.Microsoft.Windows.AI.ContentSafety.TextContentFilterSeverity) -> Void: ...
    @winrt_commethod(8)
    def get_ResponseMaxAllowedSeverityLevel(self) -> win32more.Microsoft.Windows.AI.ContentSafety.TextContentFilterSeverity: ...
    @winrt_commethod(9)
    def put_ResponseMaxAllowedSeverityLevel(self, value: win32more.Microsoft.Windows.AI.ContentSafety.TextContentFilterSeverity) -> Void: ...
    @winrt_commethod(10)
    def get_ImageMaxAllowedSeverityLevel(self) -> win32more.Microsoft.Windows.AI.ContentSafety.ImageContentFilterSeverity: ...
    @winrt_commethod(11)
    def put_ImageMaxAllowedSeverityLevel(self, value: win32more.Microsoft.Windows.AI.ContentSafety.ImageContentFilterSeverity) -> Void: ...
    ImageMaxAllowedSeverityLevel = property(get_ImageMaxAllowedSeverityLevel, put_ImageMaxAllowedSeverityLevel)
    PromptMaxAllowedSeverityLevel = property(get_PromptMaxAllowedSeverityLevel, put_PromptMaxAllowedSeverityLevel)
    ResponseMaxAllowedSeverityLevel = property(get_ResponseMaxAllowedSeverityLevel, put_ResponseMaxAllowedSeverityLevel)
class IImageContentFilterSeverity(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.ContentSafety.IImageContentFilterSeverity'
    _iid_ = Guid('{f1563582-c66a-5861-9995-1440b05191ac}')
    @winrt_commethod(6)
    def get_AdultContentLevel(self) -> win32more.Microsoft.Windows.AI.ContentSafety.SeverityLevel: ...
    @winrt_commethod(7)
    def put_AdultContentLevel(self, value: win32more.Microsoft.Windows.AI.ContentSafety.SeverityLevel) -> Void: ...
    @winrt_commethod(8)
    def get_RacyContentLevel(self) -> win32more.Microsoft.Windows.AI.ContentSafety.SeverityLevel: ...
    @winrt_commethod(9)
    def put_RacyContentLevel(self, value: win32more.Microsoft.Windows.AI.ContentSafety.SeverityLevel) -> Void: ...
    @winrt_commethod(10)
    def get_GoryContentLevel(self) -> win32more.Microsoft.Windows.AI.ContentSafety.SeverityLevel: ...
    @winrt_commethod(11)
    def put_GoryContentLevel(self, value: win32more.Microsoft.Windows.AI.ContentSafety.SeverityLevel) -> Void: ...
    @winrt_commethod(12)
    def get_ViolentContentLevel(self) -> win32more.Microsoft.Windows.AI.ContentSafety.SeverityLevel: ...
    @winrt_commethod(13)
    def put_ViolentContentLevel(self, value: win32more.Microsoft.Windows.AI.ContentSafety.SeverityLevel) -> Void: ...
    AdultContentLevel = property(get_AdultContentLevel, put_AdultContentLevel)
    GoryContentLevel = property(get_GoryContentLevel, put_GoryContentLevel)
    RacyContentLevel = property(get_RacyContentLevel, put_RacyContentLevel)
    ViolentContentLevel = property(get_ViolentContentLevel, put_ViolentContentLevel)
class IImageContentFilterSeverityFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.ContentSafety.IImageContentFilterSeverityFactory'
    _iid_ = Guid('{ead11457-81b1-5b81-9ca3-c5b04b4df043}')
    @winrt_commethod(6)
    def CreateInstance(self, severityForALlCategories: win32more.Microsoft.Windows.AI.ContentSafety.SeverityLevel) -> win32more.Microsoft.Windows.AI.ContentSafety.ImageContentFilterSeverity: ...
class ITextContentFilterSeverity(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.ContentSafety.ITextContentFilterSeverity'
    _iid_ = Guid('{68c1ee47-c35c-5f4c-a647-b0c0f64aa0d5}')
    @winrt_commethod(6)
    def get_Hate(self) -> win32more.Microsoft.Windows.AI.ContentSafety.SeverityLevel: ...
    @winrt_commethod(7)
    def put_Hate(self, value: win32more.Microsoft.Windows.AI.ContentSafety.SeverityLevel) -> Void: ...
    @winrt_commethod(8)
    def get_Sexual(self) -> win32more.Microsoft.Windows.AI.ContentSafety.SeverityLevel: ...
    @winrt_commethod(9)
    def put_Sexual(self, value: win32more.Microsoft.Windows.AI.ContentSafety.SeverityLevel) -> Void: ...
    @winrt_commethod(10)
    def get_Violent(self) -> win32more.Microsoft.Windows.AI.ContentSafety.SeverityLevel: ...
    @winrt_commethod(11)
    def put_Violent(self, value: win32more.Microsoft.Windows.AI.ContentSafety.SeverityLevel) -> Void: ...
    @winrt_commethod(12)
    def get_SelfHarm(self) -> win32more.Microsoft.Windows.AI.ContentSafety.SeverityLevel: ...
    @winrt_commethod(13)
    def put_SelfHarm(self, value: win32more.Microsoft.Windows.AI.ContentSafety.SeverityLevel) -> Void: ...
    Hate = property(get_Hate, put_Hate)
    SelfHarm = property(get_SelfHarm, put_SelfHarm)
    Sexual = property(get_Sexual, put_Sexual)
    Violent = property(get_Violent, put_Violent)
class ITextContentFilterSeverityFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.ContentSafety.ITextContentFilterSeverityFactory'
    _iid_ = Guid('{e0ca501e-4004-501e-8984-442d091607d4}')
    @winrt_commethod(6)
    def CreateInstance(self, severityForAllCategories: win32more.Microsoft.Windows.AI.ContentSafety.SeverityLevel) -> win32more.Microsoft.Windows.AI.ContentSafety.TextContentFilterSeverity: ...
class ImageContentFilterSeverity(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.AI.ContentSafety.IImageContentFilterSeverity
    _classid_ = 'Microsoft.Windows.AI.ContentSafety.ImageContentFilterSeverity'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.Windows.AI.ContentSafety.ImageContentFilterSeverity.CreateInstance(*args))
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.Windows.AI.ContentSafety.ImageContentFilterSeverity.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_overload
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.Windows.AI.ContentSafety.ImageContentFilterSeverity: ...
    @CreateInstance.register
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.Windows.AI.ContentSafety.IImageContentFilterSeverityFactory, severityForALlCategories: win32more.Microsoft.Windows.AI.ContentSafety.SeverityLevel) -> win32more.Microsoft.Windows.AI.ContentSafety.ImageContentFilterSeverity: ...
    @winrt_mixinmethod
    def get_AdultContentLevel(self: win32more.Microsoft.Windows.AI.ContentSafety.IImageContentFilterSeverity) -> win32more.Microsoft.Windows.AI.ContentSafety.SeverityLevel: ...
    @winrt_mixinmethod
    def put_AdultContentLevel(self: win32more.Microsoft.Windows.AI.ContentSafety.IImageContentFilterSeverity, value: win32more.Microsoft.Windows.AI.ContentSafety.SeverityLevel) -> Void: ...
    @winrt_mixinmethod
    def get_RacyContentLevel(self: win32more.Microsoft.Windows.AI.ContentSafety.IImageContentFilterSeverity) -> win32more.Microsoft.Windows.AI.ContentSafety.SeverityLevel: ...
    @winrt_mixinmethod
    def put_RacyContentLevel(self: win32more.Microsoft.Windows.AI.ContentSafety.IImageContentFilterSeverity, value: win32more.Microsoft.Windows.AI.ContentSafety.SeverityLevel) -> Void: ...
    @winrt_mixinmethod
    def get_GoryContentLevel(self: win32more.Microsoft.Windows.AI.ContentSafety.IImageContentFilterSeverity) -> win32more.Microsoft.Windows.AI.ContentSafety.SeverityLevel: ...
    @winrt_mixinmethod
    def put_GoryContentLevel(self: win32more.Microsoft.Windows.AI.ContentSafety.IImageContentFilterSeverity, value: win32more.Microsoft.Windows.AI.ContentSafety.SeverityLevel) -> Void: ...
    @winrt_mixinmethod
    def get_ViolentContentLevel(self: win32more.Microsoft.Windows.AI.ContentSafety.IImageContentFilterSeverity) -> win32more.Microsoft.Windows.AI.ContentSafety.SeverityLevel: ...
    @winrt_mixinmethod
    def put_ViolentContentLevel(self: win32more.Microsoft.Windows.AI.ContentSafety.IImageContentFilterSeverity, value: win32more.Microsoft.Windows.AI.ContentSafety.SeverityLevel) -> Void: ...
    AdultContentLevel = property(get_AdultContentLevel, put_AdultContentLevel)
    GoryContentLevel = property(get_GoryContentLevel, put_GoryContentLevel)
    RacyContentLevel = property(get_RacyContentLevel, put_RacyContentLevel)
    ViolentContentLevel = property(get_ViolentContentLevel, put_ViolentContentLevel)
class SeverityLevel(Enum, Int32):
    Minimum = 10
    Low = 11
    Medium = 12
    High = 13
class TextContentFilterSeverity(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.AI.ContentSafety.ITextContentFilterSeverity
    _classid_ = 'Microsoft.Windows.AI.ContentSafety.TextContentFilterSeverity'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.Windows.AI.ContentSafety.TextContentFilterSeverity.CreateInstance(*args))
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.Windows.AI.ContentSafety.TextContentFilterSeverity.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_overload
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.Windows.AI.ContentSafety.TextContentFilterSeverity: ...
    @CreateInstance.register
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.Windows.AI.ContentSafety.ITextContentFilterSeverityFactory, severityForAllCategories: win32more.Microsoft.Windows.AI.ContentSafety.SeverityLevel) -> win32more.Microsoft.Windows.AI.ContentSafety.TextContentFilterSeverity: ...
    @winrt_mixinmethod
    def get_Hate(self: win32more.Microsoft.Windows.AI.ContentSafety.ITextContentFilterSeverity) -> win32more.Microsoft.Windows.AI.ContentSafety.SeverityLevel: ...
    @winrt_mixinmethod
    def put_Hate(self: win32more.Microsoft.Windows.AI.ContentSafety.ITextContentFilterSeverity, value: win32more.Microsoft.Windows.AI.ContentSafety.SeverityLevel) -> Void: ...
    @winrt_mixinmethod
    def get_Sexual(self: win32more.Microsoft.Windows.AI.ContentSafety.ITextContentFilterSeverity) -> win32more.Microsoft.Windows.AI.ContentSafety.SeverityLevel: ...
    @winrt_mixinmethod
    def put_Sexual(self: win32more.Microsoft.Windows.AI.ContentSafety.ITextContentFilterSeverity, value: win32more.Microsoft.Windows.AI.ContentSafety.SeverityLevel) -> Void: ...
    @winrt_mixinmethod
    def get_Violent(self: win32more.Microsoft.Windows.AI.ContentSafety.ITextContentFilterSeverity) -> win32more.Microsoft.Windows.AI.ContentSafety.SeverityLevel: ...
    @winrt_mixinmethod
    def put_Violent(self: win32more.Microsoft.Windows.AI.ContentSafety.ITextContentFilterSeverity, value: win32more.Microsoft.Windows.AI.ContentSafety.SeverityLevel) -> Void: ...
    @winrt_mixinmethod
    def get_SelfHarm(self: win32more.Microsoft.Windows.AI.ContentSafety.ITextContentFilterSeverity) -> win32more.Microsoft.Windows.AI.ContentSafety.SeverityLevel: ...
    @winrt_mixinmethod
    def put_SelfHarm(self: win32more.Microsoft.Windows.AI.ContentSafety.ITextContentFilterSeverity, value: win32more.Microsoft.Windows.AI.ContentSafety.SeverityLevel) -> Void: ...
    Hate = property(get_Hate, put_Hate)
    SelfHarm = property(get_SelfHarm, put_SelfHarm)
    Sexual = property(get_Sexual, put_Sexual)
    Violent = property(get_Violent, put_Violent)


make_ready(__name__)
