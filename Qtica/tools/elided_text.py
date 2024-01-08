from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QFontMetrics
from ..core import AbstractDec


class ElidedText(AbstractDec):
    """
    ElidedText(
        child = Label("Your text here"),
        width = Api("window").width(),
        elided_mode = Qt.TextElideMode.ElideRight
    )
    """
    def __init__(self, 
                 *,
                 child: QWidget,
                 width: int = None,
                 elide_mode: Qt.TextElideMode = Qt.TextElideMode.ElideRight,
                 **kwargs) -> QWidget:

        if not hasattr(child, "setText"):
            raise ValueError("invalid child widget!")

        if hasattr(child, "textChanged"):
            child.textChanged.connect(lambda _: self._set_elided(child, width, elide_mode))

        self._set_elided(child, width, elide_mode)

        return child

    def _set_elided(self, child, width: int, elide_mode):
        width = width if width is not None else self._get_parent_width(child)

        child.blockSignals(True)
        child.setText(child.fontMetrics().elidedText(child.text(), elide_mode, width))
        child.blockSignals(False)

    def _get_parent_width(self, child: QWidget) -> int:
        parent = child.topLevelWidget()
        if parent is None:
            parent = child.parentWidget()

        if parent is not None:
            return parent.width()

        return child.width()

    @staticmethod
    def elided(text: str,
               width: int,
               elide_mode: Qt.TextElideMode = Qt.TextElideMode.ElideRight) -> str:
        return QFontMetrics(text).elidedText(text, elide_mode, width)