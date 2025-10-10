from __future__ import annotations

from ._win32api import IInspectable


# FIXME: Add more conversion.
def box_value(value: object) -> IInspectable:
    from win32more.Windows.Foundation import PropertyValue

    if isinstance(value, str):
        return PropertyValue.CreateString(value)
    elif isinstance(value, bool):
        return PropertyValue.CreateBoolean(value)
    raise NotImplementedError(f"box_value: {type(value)}")


def unbox_value(value: IInspectable):
    from win32more.Windows.Foundation import IPropertyValue, PropertyType

    property_value = value.as_(IPropertyValue)

    if property_value.Type == PropertyType.Empty:
        return None
    elif property_value.Type == PropertyType.UInt8:
        return property_value.GetUInt8()
    elif property_value.Type == PropertyType.Int16:
        return property_value.GetInt16()
    elif property_value.Type == PropertyType.UInt16:
        return property_value.GetUInt16()
    elif property_value.Type == PropertyType.Int32:
        return property_value.GetInt32()
    elif property_value.Type == PropertyType.UInt32:
        return property_value.GetUInt32()
    elif property_value.Type == PropertyType.Int64:
        return property_value.GetInt64()
    elif property_value.Type == PropertyType.UInt64:
        return property_value.GetUInt64()
    elif property_value.Type == PropertyType.Single:
        return property_value.GetSingle()
    elif property_value.Type == PropertyType.Double:
        return property_value.GetDouble()
    elif property_value.Type == PropertyType.Char16:
        return property_value.GetChar16()
    elif property_value.Type == PropertyType.Boolean:
        return property_value.GetBoolean()
    elif property_value.Type == PropertyType.String:
        return property_value.GetString()
    elif property_value.Type == PropertyType.Inspectable:
        return value
    elif property_value.Type == PropertyType.DateTime:
        return property_value.GetDateTime()
    elif property_value.Type == PropertyType.TimeSpan:
        return property_value.GetTimeSpan()
    elif property_value.Type == PropertyType.Guid:
        return property_value.GetGuid()
    elif property_value.Type == PropertyType.Point:
        return property_value.GetPoint()
    elif property_value.Type == PropertyType.Size:
        return property_value.GetSize()
    elif property_value.Type == PropertyType.Rect:
        return property_value.GetRect()
    elif property_value.Type == PropertyType.UInt8Array:
        r = []
        property_value.GetUInt8Array(r)
        return r
    elif property_value.Type == PropertyType.Int16Array:
        r = []
        property_value.GetInt16Array(r)
        return r
    elif property_value.Type == PropertyType.UInt16Array:
        r = []
        property_value.GetUInt16Array(r)
        return r
    elif property_value.Type == PropertyType.Int32Array:
        r = []
        property_value.GetInt32Array(r)
        return r
    elif property_value.Type == PropertyType.UInt32Array:
        r = []
        property_value.GetUInt32Array(r)
        return r
    elif property_value.Type == PropertyType.Int64Array:
        r = []
        property_value.GetInt64Array(r)
        return r
    elif property_value.Type == PropertyType.UInt64Array:
        r = []
        property_value.GetUInt64Array(r)
        return r
    elif property_value.Type == PropertyType.SingleArray:
        r = []
        property_value.GetSingleArray(r)
        return r
    elif property_value.Type == PropertyType.DoubleArray:
        r = []
        property_value.GetDoubleArray(r)
        return r
    elif property_value.Type == PropertyType.Char16Array:
        r = []
        property_value.GetChar16Array(r)
        return r
    elif property_value.Type == PropertyType.BooleanArray:
        r = []
        property_value.GetBooleanArray(r)
        return r
    elif property_value.Type == PropertyType.StringArray:
        r = []
        property_value.GetStringArray(r)
        return r
    elif property_value.Type == PropertyType.InspectableArray:
        r = []
        property_value.GetInspectableArray(r)
        return r
    elif property_value.Type == PropertyType.DateTimeArray:
        r = []
        property_value.GetDateTimeArray(r)
        return r
    elif property_value.Type == PropertyType.TimeSpanArray:
        r = []
        property_value.GetTimeSpanArray(r)
        return r
    elif property_value.Type == PropertyType.GuidArray:
        r = []
        property_value.GetGuidArray(r)
        return r
    elif property_value.Type == PropertyType.PointArray:
        r = []
        property_value.GetPointArray(r)
        return r
    elif property_value.Type == PropertyType.SizeArray:
        r = []
        property_value.GetSizeArray(r)
        return r
    elif property_value.Type == PropertyType.RectArray:
        r = []
        property_value.GetRectArray(r)
        return r
    # elif property_value.Type == PropertyType.OtherType:
    # elif property_value.Type == PropertyType.OtherTypeArray:
    else:
        raise NotImplementedError(f"unbox_value: {property_value.Type}")
