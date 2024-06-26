from enum import EnumMeta
from os import path as _os_path
from inspect import getfile as _ins_getfile



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
    '''

    def __getattr__(self, attr):
        try:
            return self.__getitem__(attr)
        except KeyError:
            return super(QueryDict, self).__getattr__(attr)

    def __setattr__(self, attr, value):
        self.__setitem__(attr, value)


class EnumDirectValueMeta(EnumMeta):
    '''EnumDirectValueMeta can return the value without call value attr!
    
    ::

        class EnumClass(Enum, metaclass=EnumDirectValueMeta):
            red = 0
            green = 1
            blue = 2

        print(EnumClass.red) # 0
    '''
    def __getattribute__(cls, name):
        value = super().__getattribute__(name)
        if isinstance(value, cls):
            value = value.value
        return value


class BaseDir:
    """return the root path of you file
    Example
    --------
    >>> BaseDir(__file__).path("dir", "file")
    "/path/to/script/dir/file"

    >>> class Test:
            ...
    >>> BaseDir(Test).path("dir", "file")
    "/path/to/class/dir/file"

    >>> def test():
            ...
    >>> BaseDir(test).path("dir", "file")
    "/path/to/function/dir/file"

    >>> BaseDir.tree(__file__, "dir", "file")
    >>> BaseDir.tree(Test, "dir", "file")
    >>> BaseDir.tree(test, "dir", "file")
    """

    def __init__(self, file: str | object = None) -> None:
        self._file = file

    @classmethod
    def _args_to_path(cls, root: str, *files: list[str]) -> str:
        return _os_path.join(_os_path.dirname(root), *files)

    @classmethod
    def _obj_to_path(cls, root: object, *files: list[str]) -> str:
        return _os_path.join(_os_path.dirname(_ins_getfile(root)), *files)

    def path(self, *files: list[str]) -> str:
        if isinstance(self._file, str):
            return self._args_to_path(self._file, *files)
        return self._obj_to_path(self._file, *files)

    @classmethod
    def tree(cls, root: str | object, *files: list[str]) -> str:
        if isinstance(root, str):
            return cls._args_to_path(root, *files)
        return cls._obj_to_path(root, *files)

    @classmethod
    def fetch(cls, root: str | object, *files: list[str]) -> str:
        return cls.tree(root, *files)