# coding: utf-8
from enum import EnumMeta
from typing import Any, Callable, Union


class staticproperty(property):
    '''
    class Object:
        @staticproperty
        def some_method():
            ...
    '''

    def __get__(self, owner_self, owner_cls):         
        return self.fget()


class classproperty(property):
    '''
    class Object:
        
        @classproperty
        def some_method(cls):
            ...
    '''

    def __get__(self, owner_self, owner_cls):
        return self.fget(owner_cls)


class QueryDict(dict):
    '''QueryDict is a dict() that can be queried with dot.

    ::

        d = QueryDict()
        
        # create a key named toto, with the value 1
        d.toto = 1

        # it's the same as
        d['toto'] = 1

    .. versionadded:: 1.0.4
    '''

    def __getattr__(self, attr):
        try:
            return self.__getitem__(attr)
        except KeyError:
            return super(QueryDict, self).__getattr__(attr)

    def __setattr__(self, attr, value):
        self.__setitem__(attr, value)


class EnumDirectValueMeta(EnumMeta):
    '''
    class EnumClass(Enum, metaclass=EnumDirectValueMeta):
        red = 0
        green = 1
        blue = 2

    >> EnumClass.red
    0
    '''
    def __getattribute__(cls, name):
        value = super().__getattribute__(name)
        if isinstance(value, cls):
            value = value.value
        return value


class CheckNone:
    '''
    ### e.g
    NoneCheck(self.setIcon, icon)

    ### same to:
    if icon is not None:
        self.setIcon()
    '''

    def __new__(cls, *args, **kwargs) -> Any:
        instance = super().__new__(cls)
        return instance.__init__(*args, **kwargs)

    def __init__(self, method: Callable, value: Any) -> Any:
        if callable(method) and value is not None:
            return method(value)


class Func:
    def __init__(self, func, *args, **kwargs):
        self._func = func
        self._args = args
        self._kwargs = kwargs

    def func(self) -> Union[Callable, str]:
        return self._func

    def args(self) -> tuple[Any]:
        return self._args

    def kwargs(self) -> dict[str, Any]:
        return self._kwargs


class Args:
    def __init__(self, *args, **kwargs):
        self._args = args
        self._kwargs = kwargs

    def args(self) -> tuple[Any]:
        return self._args

    def kwargs(self) -> dict[str, Any]:
        return self._kwargs