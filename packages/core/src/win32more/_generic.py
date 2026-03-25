from __future__ import annotations

import functools
from typing import TypeVar


def generic_is_concrete(cls):
    return "__concrete__" in cls.__dict__


def generic_get_args(cls, target=None):
    if target is None:
        return cls.__dict__.get("__args__", ())
    for base in cls.__mro__:
        if generic_is_concrete(base) and base.__origin__ is target:
            return base.__dict__["__args__"]
    raise TypeError(f"cannot find target {target} in {cls}")


class GenericSpecializer:
    def __init__(self, parameter_to_type_map: dict[TypeVar, type]) -> None:
        self._parameter_to_type_map = parameter_to_type_map

    def specialize_generic_alias(self, parameterized_generic_alias: GenericAlias) -> type:
        parameters = generic_get_args(parameterized_generic_alias)
        args = self.specialize_parameters(parameters)
        return parameterized_generic_alias.__origin__[tuple(args)]

    def specialize_parameters(self, parameters: list[GenericAlias | TypeVar | type]) -> list[type]:
        return [self.specialize_parameter(parameter) for parameter in parameters]

    def specialize_parameter(self, parameter: GenericAlias | TypeVar | type) -> type:
        if isinstance(parameter, GenericAlias):
            return self.specialize_generic_alias(parameter)
        elif isinstance(parameter, TypeVar):
            return self._parameter_to_type_map[parameter]
        else:
            return parameter


# C[K, V] -> GenericAlias
# C[int, V] -> GenericAlias
# C[int, str] -> Concrete class
class Generic:
    def __class_getitem__(cls, args):
        # NOTE: C[T] => T, C[*[T]] => (T,)
        if not isinstance(args, tuple):
            args = (args,)
        return cls._class_getitem_cached(args)

    @classmethod
    @functools.cache
    def _class_getitem_cached(cls, args):
        # Generic[T]
        if cls is Generic:
            if not all(isinstance(t, TypeVar) for t in args):
                raise TypeError("Generic parameter must be type variable")
            return GenericAlias(cls, args)

        if len(args) < len(cls.__parameters__):
            raise TypeError(f"Too few arguments for {cls.__name__}")

        if len(args) > len(cls.__parameters__):
            raise TypeError(f"Too many arguments for {cls.__name__}")

        # Foo[T], Foo[T, int]
        if any(isinstance(t, (TypeVar, GenericAlias)) for t in args):
            return GenericAlias(cls, args)

        # All type variables are bound
        return cls._concrete(args)

    @classmethod
    def _concrete(cls, args):
        parambind = dict(zip(cls.__parameters__, args))
        bases = [cls]
        for b in cls.__orig_bases__:
            if isinstance(b, GenericAlias):
                if b.__origin__ is Generic:
                    pass
                else:
                    boundargs = tuple([parambind.get(t, t) for t in b.__args__])
                    boundbase = b.__origin__[boundargs]
                    bases.append(boundbase)
            else:
                bases.append(b)
        name_suffix = "_" + "_".join(t.__name__ for t in args)
        name = cls.__name__ + name_suffix
        qualname = cls.__qualname__ + name_suffix
        classdict = dict(cls.__dict__)
        classdict["__qualname__"] = qualname
        classdict["__args__"] = args
        classdict["__parameters__"] = cls.__parameters__
        classdict["__origin__"] = cls
        classdict["__concrete__"] = True
        return type(cls)(name, tuple(bases), classdict)

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.__parameters__ = GenericAlias.collect_parameters(cls.__orig_bases__)


class GenericAlias:
    def __init__(self, origin, args):
        super().__init__()
        self.__origin__ = origin
        self.__args__ = args
        self.__parameters__ = GenericAlias.collect_parameters(args)

    def __mro_entries__(self, bases):
        if self.__origin__ is Generic:
            i = bases.index(self)
            for b in bases[i + 1 :]:
                if isinstance(b, GenericAlias):
                    return ()
        return (self.__origin__,)

    @classmethod
    def collect_parameters(cls, args):
        # return unique tuple
        return tuple(dict.fromkeys(GenericAlias.enumerate_parameters(args)))

    @classmethod
    def enumerate_parameters(cls, args):
        for t in args:
            if isinstance(t, TypeVar):
                yield t
            elif isinstance(t, GenericAlias):
                yield from GenericAlias.enumerate_parameters(t.__parameters__)

    # <=3.10: to deceive typing._type_check(), it raises TypeError for non callable.
    def __call__(self, *args):
        pass
