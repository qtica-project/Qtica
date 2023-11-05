# coding: utf-8
from enum import EnumMeta
from functools import singledispatch, update_wrapper


class singledispatchmethod:
    """Single-dispatch generic method descriptor.

    Supports wrapping existing descriptors and handles non-descriptor
    callables as instance methods.
    
    e.g:

    @singledispatchmethod
    def __init__(self):
        super().__init__(parent, **kwargs)

    @__init__.register
    def _(self, *args):
        super().__init__(text, parent, **kwargs)
        self.fluentIcon = None

    @__init__.register
    def _(self, *args, **kwargs):
        super().__init__(icon, text, parent, **kwargs)
        self.fluentIcon = None
    """

    def __init__(self, func):
        if not callable(func) and not hasattr(func, "__get__"):
            raise TypeError(f"{func!r} is not callable or a descriptor")

        self.dispatcher = singledispatch(func)
        self.func = func

    def register(self, cls, method=None):
        """generic_method.register(cls, func) -> func

        Registers a new implementation for the given *cls* on a *generic_method*.
        """
        return self.dispatcher.register(cls, func=method)

    def __get__(self, obj, cls=None):
        def _method(*args, **kwargs):
            if args:
                method = self.dispatcher.dispatch(args[0].__class__)
            else:
                method = self.func
                for v in kwargs.values():
                    if v.__class__ in self.dispatcher.registry:
                        method = self.dispatcher.dispatch(v.__class__)
                        if method is not self.func:
                            break

            return method.__get__(obj, cls)(*args, **kwargs)

        _method.__isabstractmethod__ = self.__isabstractmethod__
        _method.register = self.register
        update_wrapper(_method, self.func)
        return _method

    @property
    def __isabstractmethod__(self):
        return getattr(self.func, '__isabstractmethod__', False)


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