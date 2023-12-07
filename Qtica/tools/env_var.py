import os

from enum import Enum
from typing import Any, Union
from ..enums.env_vars import EnvVars


class EnvVar:
    """
    e.g, EnvVar.set(EnvVars.scale_factor, "0")
    e.g, EnvVar.set("QT_SCALE_FACTOR", "0")
    """

    @staticmethod
    def get(key: str, default: Any = None) -> Any:
        return os.environ.get(key, default)

    @staticmethod
    def set(key: Union[EnvVars, str], value: Any) -> None:
        os.environ[key.value 
                   if isinstance(key, EnvVars) 
                   else key] = (value.value 
                                if isinstance(value, Enum) 
                                else value)