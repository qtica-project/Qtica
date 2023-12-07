#-----------------------------------------------------------------------------
#  Copyright (C) 2019 Alberto Sottile
#
#  Distributed under the terms of the 3-clause BSD License.
#-----------------------------------------------------------------------------

import typing
from ...enums.theme import Theme


def theme():
    return None
        
def isDark():
    return None
    
def isLight():
    return None

def listener(callback: typing.Callable[[Theme], None]) -> None:
    raise NotImplementedError()
