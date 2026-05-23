from win32more.Windows.Foundation.Collections import IMap, IVector

from ._boxing import box_value, unbox_value
from ._hstr import hstr
from ._map import Map
from ._vector import Vector
from ._win32api import IInspectable


def _box_value_and_collection(value):
    if isinstance(value, list):
        return Vector[IInspectable]([_box_value_and_collection(v) for v in value])
    if isinstance(value, dict):
        return Map[hstr, IInspectable]({k: _box_value_and_collection(v) for k, v in value.items()})
    return box_value(value)


def _unbox_value_and_collection(value):
    vec = value.try_as(IVector[IInspectable])
    if vec is not None:
        return List(vec)

    map = value.try_as(IMap[hstr, IInspectable])
    if map is not None:
        return Dict(map)

    return unbox_value(value)


class List(IInspectable):
    def __init__(self, data: list | IVector[IInspectable] | None = None) -> None:
        super().__init__()

        if data is None:
            self._data = Vector[IInspectable]()
        elif isinstance(data, list):
            self._data = _box_value_and_collection(data)
        else:
            self._data = data.as_(IVector[IInspectable])

        self.value = self._data.value

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        r = self._data[index]
        if isinstance(r, list):
            return [_unbox_value_and_collection(v) for v in r]
        return _unbox_value_and_collection(r)

    def __setitem__(self, index, value):
        self._data.__setitem__(index, _box_value_and_collection(value))

    def __delitem__(self, index):
        self._data.__delitem__(index)

    def insert(self, index, value):
        self._data.InsertAt(index, _box_value_and_collection(value))

    def append(self, value):
        self._data.Append(_box_value_and_collection(value))

    def clear(self, value):
        self._data.Clear()


class Dict(IInspectable):
    def __init__(self, data: dict | IMap[hstr, IInspectable] | None = None) -> None:
        super().__init__()

        if data is None:
            self._data = Map[hstr, IInspectable]()
        elif isinstance(data, dict):
            self._data = _box_value_and_collection(data)
        else:
            self._data = data.as_(IMap[hstr, IInspectable])

        self.value = self._data.value

    def __iter__(self):
        return self._data.__iter__()

    def __len__(self):
        return len(self._data)

    def __getitem__(self, key):
        return _unbox_value_and_collection(self._data[key])

    def __setitem__(self, key, value):
        self._data[key] = _box_value_and_collection(value)

    def __delitem__(self, key):
        self._data.__delitem__(key)

    def __contains__(self, key):
        return key in self._data

    def items(self):
        for k, v in self._data.items():
            yield k, _unbox_value_and_collection(v)

    def keys(self):
        for k in self._data.keys():
            yield k

    def values(self):
        for v in self._data.values():
            yield _unbox_value_and_collection(v)

    def get(self, key, default=None):
        return self._data.get(key, default)

    def __eq__(self, other):
        return dict(self.items()) == dict(other.items())
