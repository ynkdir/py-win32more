from __future__ import annotations
from win32more._prelude import *
import win32more.Windows.Graphics
class DisplayAdapterId(Structure):
    _name_ = 'Windows.Graphics.DisplayAdapterId'
    LowPart: UInt32
    HighPart: Int32
class DisplayId(Structure):
    _name_ = 'Windows.Graphics.DisplayId'
    Value: UInt64
class IGeometrySource2D(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Graphics.IGeometrySource2D'
    _iid_ = Guid('{caff7902-670c-4181-a624-da977203b845}')
class PointInt32(Structure):
    _name_ = 'Windows.Graphics.PointInt32'
    X: Int32
    Y: Int32
class RectInt32(Structure):
    _name_ = 'Windows.Graphics.RectInt32'
    X: Int32
    Y: Int32
    Width: Int32
    Height: Int32
class SizeInt32(Structure):
    _name_ = 'Windows.Graphics.SizeInt32'
    Width: Int32
    Height: Int32


make_ready(__name__)
