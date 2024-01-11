#!/usr/bin/python3

from typing import Any
from enum import Enum, auto
from PySide6.QtCore import QSettings, QTimer
from ..core import AbstractQObject, AbstractConfig
from ..utils import EnvVar
import platform
import os


class Settings(AbstractQObject, QSettings):
    '''
    Init
    ----
    class _Line(AbstractConfig):
        def name(self) - str:
            return "Name"

        def group(self) -> str:
            return "User"

        def get(self) -> Callable:
            return Api.fetch("user-line").text

        def set(self) -> Callable:
            return Api.fetch("user-line").setText

        def signal(self) -> Signal:
            return Api.fetch("user-line").textChanged

    Usage
    -----
    Settings(
        configs=[
            _Line()
        ]
    )

    Output Result
    -------------
        [User]\n
        Name=
    '''

    class System(Enum):
        java = auto()
        linux = auto()
        darwin = auto()
        windows = auto()

        macos = darwin
        posix = linux
        unknow = auto()

    def __init__(self,
                 format: QSettings.Format = None,
                 scope: QSettings.Scope = None,
                 path: str = None,
                 configs: list[AbstractConfig] = None,
                 **kwargs):
        QSettings.__init__(self)
        super().__init__(**kwargs)

        if scope is not None:
            self.setPath(
                format if format is not None else self._get_default_format(),
                scope,
                path if path is not None else self._get_default_path()
            )

        if not self.allKeys():
            self._init_configs(configs)
        else:
            self._setup_configs(configs)

    def value(self, 
              key: str,
              default: Any = None,
              type: object | None = None,
              group: str = None
              ) -> Any:

        if group is not None:
            self.beginGroup(group)
            value = super().value(key, 
                                  *(value for value in (default, type) 
                                    if value is not None))
            self.endGroup()
            return value

        return super().value(key)

    def get(self, 
              key: str,
              default: Any = None,
              type: object | None = None,
              group: str = None
              ) -> Any:
        return self.value(key, default, type, group)

    def setValue(self, key: str, value: Any, group: str = None) -> None:
        if group is not None:
            self.beginGroup(group)
            super().setValue(key, value)
            return self.endGroup()
        return super().setValue(key, value)

    def remove(self, key: str, group: str = None) -> None:
        if group is not None:
            self.beginGroup(group)
            super().remove(key)
            return self.endGroup()
        return super().remove(key)

    def _get_default_format(self) -> QSettings.Format:
        return self.defaultFormat()

    def _set_default_path(self) -> str:
        if self.system() == Settings.System.windows:
            if self.scope() == QSettings.Scope.SystemScope:
                return EnvVar.get("FOLDERID_ProgramData")
            return EnvVar.get("FOLDERID_RoamingAppData")

        if self.scope() == QSettings.Scope.SystemScope:
            return os.path.join("etc", "xdg")
        return os.path.join(EnvVar.get("HOME"), ".config")

    def _init_configs(self, configs: list[AbstractConfig]) -> None:
        for config in configs:
            config.signal().connect(
                lambda: QTimer.singleShot(0, 
                                          lambda: self._update_config(config)))

    def _setup_configs(self, configs: list[AbstractConfig]) -> None:
        for config in configs:
            _value = self.value(config.name(), 
                                config.default(),
                                config.type(),
                                config.group())

            QTimer.singleShot(0, lambda: config.set()(_value))
            config.signal().connect(
                lambda: QTimer.singleShot(0, 
                                          lambda: self._update_config(config)))

    def _update_config(self, config) -> None:
        self.setValue(config.name(), 
                      config.get()(),
                      config.group())

    def current_system(self) -> System:
        return Settings.System(platform.system().strip().lower() or "unknow")

    def system(self) -> System:
        return self.current_system()