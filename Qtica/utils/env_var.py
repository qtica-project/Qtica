#!/usr/bin/python3


from enum import Enum
from typing import Any, Union
from ..enums.env_vars import EnvVars
import os


class EnvVar:
    '''
    Set Key, and Value
    >>> EnvVar.set(EnvVars.scale_factor, "0")
    >>> EnvVar.set("QT_SCALE_FACTOR", "0")

    Get Value, from Key
    >>> EnvVar.get(EnvVars.scale_factor, "0")
    >>> EnvVar.get("QT_SCALE_FACTOR", "0")
    >>> env = EnvVar()
    >>> env("QT_SCALE_FACTOR", "0")
    '''

    def __call__(self, key: Union[EnvVars, str], default: Any = None) -> Any:
        return self.get(key, default)

    @classmethod
    def set(cls, key: Union[EnvVars, str], value: Any) -> None:
        os.environ[key.value 
                   if isinstance(key, EnvVars) 
                   else key] = (value.value 
                                if isinstance(value, Enum) 
                                else value)

    @classmethod
    def get(cls, key: Union[EnvVars, str], default: Any = None) -> Any:
        return os.environ.get(key, default)
