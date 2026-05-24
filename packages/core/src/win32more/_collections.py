from __future__ import annotations

from win32more.Windows.Foundation.Collections import IMap, IVector

from . import _box
from ._hstr import hstr
from ._map import Map
from ._vector import Vector
from ._win32api import IInspectable


def _box_any(value):
    if isinstance(value, list):
        return List(value)
    if isinstance(value, dict):
        return Dict(value)
    return _box.box_value(value)


def _unbox_any(value):
    vec = value.try_as(IVector[IInspectable])
    if vec is not None:
        return List(vec)

    map = value.try_as(IMap[hstr, IInspectable])
    if map is not None:
        return Dict(map)

    return _box.unbox_value(value)


class List(IInspectable):
    def __init__(self, inner: list | IVector[IInspectable] | None = None) -> None:
        super().__init__()

        if inner is None:
            self._inner = Vector[IInspectable]().as_(IVector[IInspectable])
        elif isinstance(inner, list):
            self._inner = Vector[IInspectable]([_box_any(v) for v in inner]).as_(IVector[IInspectable])
        else:
            self._inner = inner.as_(IVector[IInspectable])

        self.value = self._inner.value

    def __len__(self):
        return len(self._inner)

    def __getitem__(self, index):
        r = self._inner[index]
        if isinstance(r, list):
            return [_unbox_any(v) for v in r]
        return _unbox_any(r)

    def __setitem__(self, index, value):
        self._inner.__setitem__(index, _box_any(value))

    def __delitem__(self, index):
        self._inner.__delitem__(index)

    def insert(self, index, value):
        self._inner.InsertAt(index, _box_any(value))

    def append(self, value):
        self._inner.Append(_box_any(value))

    def clear(self, value):
        self._inner.Clear()


class Dict(IInspectable):
    def __init__(self, inner: dict | IMap[hstr, IInspectable] | None = None) -> None:
        super().__init__()

        if inner is None:
            self._inner = Map[hstr, IInspectable]().as_(IMap[hstr, IInspectable])
        elif isinstance(inner, dict):
            self._inner = Map[hstr, IInspectable]({k: _box_any(v) for k, v in inner.items()}).as_(
                IMap[hstr, IInspectable]
            )
        else:
            self._inner = inner.as_(IMap[hstr, IInspectable])

        self.value = self._inner.value

    def __iter__(self):
        return self._inner.__iter__()

    def __len__(self):
        return len(self._inner)

    def __getitem__(self, key):
        return _unbox_any(self._inner[key])

    def __setitem__(self, key, value):
        self._inner[key] = _box_any(value)

    def __delitem__(self, key):
        self._inner.__delitem__(key)

    def __contains__(self, key):
        return key in self._inner

    def items(self):
        for k, v in self._inner.items():
            yield k, _unbox_any(v)

    def keys(self):
        for k in self._inner.keys():
            yield k

    def values(self):
        for v in self._inner.values():
            yield _unbox_any(v)

    def get(self, key, default=None):
        return self._inner.get(key, default)

    def __eq__(self, other):
        return dict(self.items()) == dict(other.items())
