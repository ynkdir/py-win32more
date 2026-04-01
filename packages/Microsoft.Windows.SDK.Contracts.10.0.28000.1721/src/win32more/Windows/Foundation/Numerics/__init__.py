from __future__ import annotations
from win32more._prelude import *
import win32more.Windows.Foundation.Numerics
class Matrix3x2(Structure):
    _name_ = 'Windows.Foundation.Numerics.Matrix3x2'
    M11: Single
    M12: Single
    M21: Single
    M22: Single
    M31: Single
    M32: Single
class Matrix4x4(Structure):
    _name_ = 'Windows.Foundation.Numerics.Matrix4x4'
    M11: Single
    M12: Single
    M13: Single
    M14: Single
    M21: Single
    M22: Single
    M23: Single
    M24: Single
    M31: Single
    M32: Single
    M33: Single
    M34: Single
    M41: Single
    M42: Single
    M43: Single
    M44: Single
class Plane(Structure):
    _name_ = 'Windows.Foundation.Numerics.Plane'
    Normal: win32more.Windows.Foundation.Numerics.Vector3
    D: Single
class Quaternion(Structure):
    _name_ = 'Windows.Foundation.Numerics.Quaternion'
    X: Single
    Y: Single
    Z: Single
    W: Single
class Rational(Structure):
    _name_ = 'Windows.Foundation.Numerics.Rational'
    Numerator: UInt32
    Denominator: UInt32
class Vector2(Structure):
    _name_ = 'Windows.Foundation.Numerics.Vector2'
    X: Single
    Y: Single
class Vector3(Structure):
    _name_ = 'Windows.Foundation.Numerics.Vector3'
    X: Single
    Y: Single
    Z: Single
class Vector4(Structure):
    _name_ = 'Windows.Foundation.Numerics.Vector4'
    X: Single
    Y: Single
    Z: Single
    W: Single


make_ready(__name__)
