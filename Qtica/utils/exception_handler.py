from copy import deepcopy
from typing import Callable, Union
from ..core.objects import Func


def TryExc(func: Union[Callable, Func], *default):
    """ func for exception handling

    Parameters
    ----------
    *default:
        the default value returned when an exception occurs
    
    Example
    -------
    TryExc(lambda: func(*args, **kwargs), *default)
    """

    try:
        if isinstance(func, Func):
            return func.func()(*func.args(), **func.kwargs())
        return func()
    except BaseException:
        value = deepcopy(default)
        if len(value) == 0:
            return None
        elif len(value) == 1:
            return value[0]
        return value