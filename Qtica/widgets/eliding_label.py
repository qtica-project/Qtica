from PySide6.QtWidgets import QLabel
from PySide6.QtCore import QPoint, QRect, QSize, Qt, Signal
from PySide6.QtGui import QFont, QFontMetrics, QResizeEvent, QTextLayout
from ..core import AbstractWidget


class _ElidingLabel(QLabel):
    """A QLabel variant that will elide text (add '…') to fit width.

    ElidingLabel(text: str = "Hi")

    For a multiline eliding label, use `setWordWrap(True)`.  In this case, text
    will wrap to fit the width, and only the last line will be elided.
    When `wordWrap()` is True, `sizeHint()` will return the size required to fit
    the full text.
    """

    textChanged = Signal(str)

    def __init__(self, text: str = None, elide_mode: Qt.TextElideMode = Qt.TextElideMode.ElideRight) -> None:
        self._elide_mode = elide_mode
        QLabel.__init__(self)
        self._silent_set_text(text if text else "")

    def _silent_set_text(self, text: str):
        self.blockSignals(True)
        self.setText(text)
        self.blockSignals(False)

    # New Public methods
    def elideMode(self) -> Qt.TextElideMode:
        """The current Qt.TextElideMode."""
        return self._elide_mode

    def setElideMode(self, mode: Qt.TextElideMode):
        """Set the elide mode to a Qt.TextElideMode."""
        self._elide_mode = Qt.TextElideMode(mode)
        super().setText(self._elidedText())

    @staticmethod
    def wrapText(text, width, font=None) -> list[str]:
        """Returns `text`, split as it would be wrapped for `width`, given `font`.

        Static method.
        """
        tl = QTextLayout(text, font or QFont())
        tl.beginLayout()
        lines = []
        while True:
            ln = tl.createLine()
            if not ln.isValid():
                break
            ln.setLineWidth(width)
            start = ln.textStart()
            lines.append(text[start : start + ln.textLength()])
        tl.endLayout()
        return lines

    # Reimplemented QT methods

    def text(self) -> str:
        """This property holds the label's text.

        If no text has been set this will return an empty string.
        """
        return self._text

    def setText(self, txt: str):
        """Set the label's text.

        Setting the text clears any previous content.
        NOTE: we set the QLabel private text to the elided version
        """
        self._text = txt
        super().setText(self._elidedText())
        self.textChanged.emit(txt)

    def resizeEvent(self, ev: QResizeEvent) -> None:
        super().setText(self._elidedText())

    def setWordWrap(self, wrap: bool) -> None:
        super().setWordWrap(wrap)
        super().setText(self._elidedText())

    def sizeHint(self) -> QSize:
        if not self.wordWrap():
            return super().sizeHint()

        fm = QFontMetrics(self.font())
        flags = int(self.alignment() | Qt.TextFlag.TextWordWrap)
        r = fm.boundingRect(QRect(QPoint(0, 0), self.size()), flags, self._text)
        return QSize(self.width(), r.height())

    # private implementation methods
    def _elidedText(self) -> str:
        """Return `self._text` elided to `width`"""
        fm = QFontMetrics(self.font())
        # the 2 is a magic number that prevents the ellipses from going missing
        # in certain cases (?)
        width = self.width() - 2
        if not self.wordWrap():
            return fm.elidedText(self._text, self._elide_mode, width)

        # get number of lines we can fit without eliding
        nlines = self.height() // fm.height() - 1
        # get the last line (elided)
        text = self._wrappedText()
        last_line = fm.elidedText("".join(text[nlines:]), self._elide_mode, width)
        # join them
        return "".join(text[:nlines] + [last_line])

    def _wrappedText(self) -> list[str]:
        return _ElidingLabel.wrapText(self._text, self.width(), self.font())


class ElidingLabel(AbstractWidget, _ElidingLabel):
    def __init__(self, 
                 text: str = None, 
                 elide_mode: Qt.TextElideMode = Qt.TextElideMode.ElideRight, 
                 **kwargs) -> None:
        _ElidingLabel.__init__(self, text, elide_mode)
        super().__init__(**kwargs)