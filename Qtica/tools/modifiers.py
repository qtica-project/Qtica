from PySide6.QtCore import Qt


class Modifiers:
    @staticmethod
    def is_shift(event):
        return event.modifiers() == Qt.KeyboardModifier.ShiftModifier

    @staticmethod
    def is_alt(event):
        return event.modifiers() == Qt.KeyboardModifier.AltModifier

    @staticmethod
    def is_ctrl(event):
        return event.modifiers() == Qt.KeyboardModifier.ControlModifier

    @staticmethod
    def is_meta(event):
        return event.modifiers() == Qt.KeyboardModifier.MetaModifier

    @staticmethod
    def is_win(event):
        return event.modifiers() == Qt.KeyboardModifier.MetaModifier
