from typing import Any, Union
from string import digits

from PySide6.QtCore import Qt
from PySide6.QtGui import QKeyEvent, QKeySequence, QMouseEvent


class Modifiers:
    Modifier = Qt.KeyboardModifier

    def __init__(self, event: QKeyEvent = None) -> None:
        self._event = event

    def matche(self, *modifier: list[Qt.KeyboardModifier]) -> bool:
        return Modifiers.matches(self._event, *modifier)

    @classmethod
    def matches(cls,
                event: Union[QKeyEvent, QMouseEvent],
               *modifier: list[Qt.KeyboardModifier]) -> bool:

        _modifier = None
        if len(modifier) > 1:
            _modifier = modifier[0]
            for mod in modifier[1:]:
                _modifier |= mod
        else:
            _modifier = modifier[0]
        return event.modifiers() == _modifier

    @classmethod
    def is_shift(cls, event: QKeyEvent) -> bool:
        return cls.matches(event, Qt.KeyboardModifier.ShiftModifier)

    @classmethod
    def is_alt(cls, event: QKeyEvent) -> bool:
        return cls.matches(event, Qt.KeyboardModifier.AltModifier)

    @classmethod
    def is_ctrl(cls, event: QKeyEvent) -> bool:
        return cls.matches(event, Qt.KeyboardModifier.ControlModifier)

    @classmethod
    def is_meta(cls, event: QKeyEvent) -> bool:
        return cls.matches(event, Qt.KeyboardModifier.MetaModifier)

    @classmethod
    def is_win(cls, event: QKeyEvent) -> bool:
        return cls.is_meta(event)

    def __getattribute__(self, name: str) -> Any:
        mod = name.title() + "Modifier"
        if hasattr(self.Modifier, mod):
            return getattr(self.Modifier, mod)
        return super().__getattribute__(name)


class Keys:
    Key = Qt.Key

    def __init__(self, event: QKeyEvent = None) -> None:
        self._event = event

    def matche(self, key: Union[Qt.Key, int]) -> bool:
        return Keys.matches(self._event, key)

    @staticmethod
    def matches(event: QKeyEvent, key: Union[Qt.Key, int]) -> bool:
        return event.key() == key

    def __getattribute__(self, name: str) -> Any:
        key = "Key" + ('_' + name) if name[1] not in digits else name
        if hasattr(self.Key, key):
            return getattr(self.Key, key)
        return super().__getattribute__(name)


class KeySequence:
    Standard = QKeySequence.StandardKey

    def __init__(self, event: QKeyEvent = None) -> None:
        self._event = event

    def matche(self, 
               modifier: Union[Qt.KeyboardModifier, list[Qt.KeyboardModifier]],
               key: Union[Qt.Key, int]) -> bool:
        return KeySequence.matches(self._event, modifier, key)

    def matche_seq(self, key: QKeySequence.StandardKey) -> bool:
        return self._event.matches(key)

    @staticmethod
    def matches(event: QKeyEvent, 
                key: Union[Qt.Key, int],
                *modifier: list[Qt.KeyboardModifier]) -> bool:
        return Modifiers.matches(event, *modifier) and Keys.matches(event, key)

    @staticmethod
    def matches_seq(event: QKeyEvent, key: QKeySequence.StandardKey) -> bool:
        return event.matches(key)


class MouseButtons:
    Button = Qt.MouseButton

    def __init__(self, event: QMouseEvent = None) -> None:
        self._event = event

    def matche(self, button: Union[Qt.MouseButton, int]) -> bool:
        return MouseButtons.matches(self._event, button)

    @staticmethod
    def matches(event: QMouseEvent, button: Union[Qt.MouseButton, int]) -> bool:
        return event.button() == button

    def __getattribute__(self, name: str) -> Any:
        if hasattr(Qt.MouseButton, name):
            return getattr(Qt.MouseButton, name)
        return super().__getattribute__(name)