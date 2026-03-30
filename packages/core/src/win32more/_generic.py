from __future__ import annotations

import functools
from typing import Generic, TypeVar, _GenericAlias, get_args, get_origin


def is_generic_concrete(cls):
    return "__concrete__" in cls.__dict__


def get_origin_or_itself(cls):
    return get_origin(cls) or cls


class GenericSpecializer:
    def __init__(self, parameter_to_type_map: dict[TypeVar, type]) -> None:
        self._parameter_to_type_map = parameter_to_type_map

    def specialize_generic_alias(self, parameterized_generic_alias: _GenericAlias) -> type:
        parameters = get_args(parameterized_generic_alias)
        args = self.specialize_parameters(parameters)
        return get_origin(parameterized_generic_alias)[tuple(args)]

    def specialize_parameters(self, parameters: list[_GenericAlias | TypeVar | type]) -> list[type]:
        return [self.specialize_parameter(parameter) for parameter in parameters]

    def specialize_parameter(self, parameter: _GenericAlias | TypeVar | type) -> type:
        if isinstance(parameter, _GenericAlias):
            return self.specialize_generic_alias(parameter)
        elif isinstance(parameter, TypeVar):
            return self._parameter_to_type_map[parameter]
        else:
            return parameter


# C[K, V] -> GenericAlias
# C[int, V] -> GenericAlias
# C[int, str] -> Concrete class
def generic_class_getitem(cls, args):
    # NOTE: C[T] => T, C[*[T]] => (T,)
    if not isinstance(args, tuple):
        args = (args,)
    return _generic_class_getitem_cached(cls, args)


@functools.cache
def _generic_class_getitem_cached(cls, args):
    ga = Generic.__dict__["__class_getitem__"].__get__(None, cls)(args)

    # Foo[T], Foo[T, int]
    if any(isinstance(t, (TypeVar, _GenericAlias)) for t in args):
        return ga

    # All type variables are bound
    return _concrete(ga)


def _concrete(ga):
    cls = get_origin(ga)
    args = get_args(ga)
    parambind = dict(zip(cls.__parameters__, args))
    bases = [cls]
    for b in cls.__orig_bases__:
        if isinstance(b, _GenericAlias):
            if get_origin(b) is Generic:
                pass
            else:
                boundargs = tuple([parambind.get(t, t) for t in b.__args__])
                boundbase = get_origin(b)[boundargs]
                bases.append(boundbase)
        else:
            bases.append(b)
    name_suffix = "_" + "_".join(t.__name__ for t in args)
    name = cls.__name__ + name_suffix
    qualname = cls.__qualname__ + name_suffix
    classdict = dict(cls.__dict__)
    classdict["__qualname__"] = qualname
    classdict["__args__"] = args
    classdict[f"_{cls.__name__}__args"] = args
    classdict["__concrete__"] = True
    if "_piid_" in classdict:
        # lazy load to prevent circular import
        from ._ro import ro_get_parameterized_type_instance_iid

        classdict["_iid_"] = ro_get_parameterized_type_instance_iid(ga)
    return type(cls)(name, tuple(bases), classdict)
