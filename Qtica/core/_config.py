#!/usr/bin/python3

from abc import ABCMeta, abstractmethod
from typing import Any, Callable
from PySide6.QtCore import Signal


class AbstractConfig(metaclass=ABCMeta):
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def get(self) -> Callable:
        raise NotImplementedError

    @abstractmethod
    def set(self) -> Callable:
        raise NotImplementedError

    @abstractmethod
    def signal(self) -> Signal:
        raise NotImplementedError

    def group(self) -> str:
        ...

    def default(self) -> Any:
        ...

    def type(self) -> object | None:
        ...