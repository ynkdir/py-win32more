from __future__ import annotations

import functools
from typing import Generic, TypeVar, _GenericAlias, get_args, get_origin


def is_generic_concrete(cls):
    return "__concrete__" in cls.__dict__


def generic_specialize(parameter: _GenericAlias | TypeVar | type, parambind: dict[TypeVar, type]) -> type:
    if isinstance(parameter, _GenericAlias):
        args = tuple(generic_specialize(param, parambind) for param in get_args(parameter))
        return get_origin(parameter)[args]
    elif isinstance(parameter, TypeVar):
        return parambind[parameter]
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
                boundargs = tuple(parambind.get(t, t) for t in b.__args__)
                boundbase = get_origin(b)[boundargs]
                bases.append(boundbase)
        else:
            bases.append(b)
    name_suffix = "_" + "_".join(t.__name__ for t in args)
    name = cls.__name__ + name_suffix
    # Constructor overwrites __parameters__.  Set later.
    newcls = type(cls)(name, tuple(bases), {})
    newcls.__module__ = cls.__module__
    newcls.__parameters__ = cls.__parameters__
    newcls.__args__ = args
    setattr(newcls, f"_{cls.__name__}__args", args)
    newcls.__concrete__ = True
    if "_classid_" in cls.__dict__:
        newcls._classid_ = cls._classid_
    if "_piid_" in cls.__dict__:
        # lazy load to prevent circular import
        from ._ro import ro_get_parameterized_type_instance_iid

        newcls._piid_ = cls._piid_
        newcls._iid_ = ro_get_parameterized_type_instance_iid(ga)
    return newcls
