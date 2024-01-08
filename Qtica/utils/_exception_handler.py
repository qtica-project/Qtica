# coding:utf-8
from copy import deepcopy
from typing import Callable, Union
from ._classes import Func


def exceptionHandler(method: Union[Callable, Func], *default):
    """ method for exception handling

    Parameters
    ----------
    *default:
        the default value returned when an exception occurs
    
    Example
    -------
    exceptionHandler(lambda: method(*args, **kwargs), *default)
    """

    try:
        if isinstance(method, Func):
            return method[0](*method[1], **method[2])
        return method()
    except BaseException:
        value = deepcopy(default)
        if len(value) == 0:
            return None
        elif len(value) == 1:
            return value[0]
        return value

