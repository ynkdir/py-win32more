from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Windows.Foundation
import win32more.Windows.Perception
class IPerceptionTimestamp(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Perception.IPerceptionTimestamp'
    _iid_ = Guid('{87c24804-a22e-4adb-ba26-d78ef639bcf4}')
    @winrt_commethod(6)
    def get_TargetTime(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_PredictionAmount(self) -> win32more.Windows.Foundation.TimeSpan: ...
    PredictionAmount = property(get_PredictionAmount, None)
    TargetTime = property(get_TargetTime, None)
class IPerceptionTimestamp2(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Perception.IPerceptionTimestamp2'
    _iid_ = Guid('{e354b7ed-2bd1-41b7-9ed0-74a15c354537}')
    @winrt_commethod(6)
    def get_SystemRelativeTargetTime(self) -> win32more.Windows.Foundation.TimeSpan: ...
    SystemRelativeTargetTime = property(get_SystemRelativeTargetTime, None)
class IPerceptionTimestampHelperStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Perception.IPerceptionTimestampHelperStatics'
    _iid_ = Guid('{47a611d4-a9df-4edc-855d-f4d339d967ac}')
    @winrt_commethod(6)
    def FromHistoricalTargetTime(self, targetTime: win32more.Windows.Foundation.DateTime) -> win32more.Windows.Perception.PerceptionTimestamp: ...
class IPerceptionTimestampHelperStatics2(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Perception.IPerceptionTimestampHelperStatics2'
    _iid_ = Guid('{73d1a7fe-3fb9-4571-87d4-3c920a5e86eb}')
    @winrt_commethod(6)
    def FromSystemRelativeTargetTime(self, targetTime: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.Perception.PerceptionTimestamp: ...
class PerceptionTimestamp(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Perception.IPerceptionTimestamp
    _classid_ = 'Windows.Perception.PerceptionTimestamp'
    @winrt_mixinmethod
    def get_TargetTime(self: win32more.Windows.Perception.IPerceptionTimestamp) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_PredictionAmount(self: win32more.Windows.Perception.IPerceptionTimestamp) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_SystemRelativeTargetTime(self: win32more.Windows.Perception.IPerceptionTimestamp2) -> win32more.Windows.Foundation.TimeSpan: ...
    PredictionAmount = property(get_PredictionAmount, None)
    SystemRelativeTargetTime = property(get_SystemRelativeTargetTime, None)
    TargetTime = property(get_TargetTime, None)
class PerceptionTimestampHelper(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Perception.PerceptionTimestampHelper'
    @winrt_classmethod
    def FromSystemRelativeTargetTime(cls: win32more.Windows.Perception.IPerceptionTimestampHelperStatics2, targetTime: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.Perception.PerceptionTimestamp: ...
    @winrt_classmethod
    def FromHistoricalTargetTime(cls: win32more.Windows.Perception.IPerceptionTimestampHelperStatics, targetTime: win32more.Windows.Foundation.DateTime) -> win32more.Windows.Perception.PerceptionTimestamp: ...


make_ready(__name__)
