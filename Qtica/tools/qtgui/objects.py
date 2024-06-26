from ...core import AbstractQObject
from qtpy import QtGui


class Action(AbstractQObject, QtGui.QAction):
    def __init__(self, *args, **kwargs):
        QtGui.QAction.__init__(self, *args)
        super().__init__(**kwargs)


class ActionGroup(AbstractQObject, QtGui.QActionGroup):
    def __init__(self, *args, **kwargs):
        QtGui.QActionGroup.__init__(self, *args)
        super().__init__(**kwargs)


class Clipboard(AbstractQObject, QtGui.QClipboard):
    def __init__(self, *args, **kwargs):
        QtGui.QClipboard.__init__(self, *args)
        super().__init__(**kwargs)


class DoubleValidator(AbstractQObject, QtGui.QDoubleValidator):
    def __init__(self, *args, **kwargs):
        QtGui.QDoubleValidator.__init__(self, *args)
        super().__init__(**kwargs)


class Drag(AbstractQObject, QtGui.QDrag):
    def __init__(self, *args, **kwargs):
        QtGui.QDrag.__init__(self, *args)
        super().__init__(**kwargs)


class GuiApplication(AbstractQObject, QtGui.QGuiApplication):
    def __init__(self, *args, **kwargs):
        QtGui.QGuiApplication.__init__(self, *args)
        super().__init__(**kwargs)


class InputDevice(AbstractQObject, QtGui.QInputDevice):
    def __init__(self, *args, **kwargs):
        QtGui.QInputDevice.__init__(self, *args)
        super().__init__(**kwargs)


class InputMethod(AbstractQObject, QtGui.QInputMethod):
    def __init__(self, *args, **kwargs):
        QtGui.QInputMethod.__init__(self, *args)
        super().__init__(**kwargs)


class IntValidator(AbstractQObject, QtGui.QIntValidator):
    def __init__(self, *args, **kwargs):
        QtGui.QIntValidator.__init__(self, *args)
        super().__init__(**kwargs)


class OffscreenSurface(AbstractQObject, QtGui.QOffscreenSurface):
    def __init__(self, *args, **kwargs):
        QtGui.QOffscreenSurface.__init__(self, *args)
        super().__init__(**kwargs)


class OpenGLContext(AbstractQObject, QtGui.QOpenGLContext):
    def __init__(self, *args, **kwargs):
        QtGui.QOpenGLContext.__init__(self, *args)
        super().__init__(**kwargs)


class OpenGLContextGroup(AbstractQObject, QtGui.QOpenGLContextGroup):
    def __init__(self, *args, **kwargs):
        QtGui.QOpenGLContextGroup.__init__(self, *args)
        super().__init__(**kwargs)


class PaintDeviceWindow(AbstractQObject, QtGui.QPaintDeviceWindow):
    def __init__(self, *args, **kwargs):
        QtGui.QPaintDeviceWindow.__init__(self, *args)
        super().__init__(**kwargs)


class PdfWriter(AbstractQObject, QtGui.QPdfWriter):
    def __init__(self, *args, **kwargs):
        QtGui.QPdfWriter.__init__(self, *args)
        super().__init__(**kwargs)


class PointingDevice(AbstractQObject, QtGui.QPointingDevice):
    def __init__(self, *args, **kwargs):
        QtGui.QPointingDevice.__init__(self, *args)
        super().__init__(**kwargs)


class PyTextObject(AbstractQObject, QtGui.QPyTextObject):
    def __init__(self, *args, **kwargs):
        QtGui.QPyTextObject.__init__(self, *args)
        super().__init__(**kwargs)


class RasterWindow(AbstractQObject, QtGui.QRasterWindow):
    def __init__(self, *args, **kwargs):
        QtGui.QRasterWindow.__init__(self, *args)
        super().__init__(**kwargs)


class RegularExpressionValidator(AbstractQObject, QtGui.QRegularExpressionValidator):
    def __init__(self, *args, **kwargs):
        QtGui.QRegularExpressionValidator.__init__(self, *args)
        super().__init__(**kwargs)


class Screen(AbstractQObject, QtGui.QScreen):
    def __init__(self, *args, **kwargs):
        QtGui.QScreen.__init__(self, *args)
        super().__init__(**kwargs)


class SessionManager(AbstractQObject, QtGui.QSessionManager):
    def __init__(self, *args, **kwargs):
        QtGui.QSessionManager.__init__(self, *args)
        super().__init__(**kwargs)


class Shortcut(AbstractQObject, QtGui.QShortcut):
    def __init__(self, *args, **kwargs):
        QtGui.QShortcut.__init__(self, *args)
        super().__init__(**kwargs)


class StandardItemModel(AbstractQObject, QtGui.QStandardItemModel):
    def __init__(self, *args, **kwargs):
        QtGui.QStandardItemModel.__init__(self, *args)
        super().__init__(**kwargs)


class StyleHints(AbstractQObject, QtGui.QStyleHints):
    def __init__(self, *args, **kwargs):
        QtGui.QStyleHints.__init__(self, *args)
        super().__init__(**kwargs)


class SyntaxHighlighter(AbstractQObject, QtGui.QSyntaxHighlighter):
    def __init__(self, *args, **kwargs):
        QtGui.QSyntaxHighlighter.__init__(self, *args)
        super().__init__(**kwargs)


class TextBlockGroup(AbstractQObject, QtGui.QTextBlockGroup):
    def __init__(self, *args, **kwargs):
        QtGui.QTextBlockGroup.__init__(self, *args)
        super().__init__(**kwargs)


class TextDocument(AbstractQObject, QtGui.QTextDocument):
    def __init__(self, *args, **kwargs):
        QtGui.QTextDocument.__init__(self, *args)
        super().__init__(**kwargs)


class TextFrame(AbstractQObject, QtGui.QTextFrame):
    def __init__(self, *args, **kwargs):
        QtGui.QTextFrame.__init__(self, *args)
        super().__init__(**kwargs)


class TextList(AbstractQObject, QtGui.QTextList):
    def __init__(self, *args, **kwargs):
        QtGui.QTextList.__init__(self, *args)
        super().__init__(**kwargs)


class TextObject(AbstractQObject, QtGui.QTextObject):
    def __init__(self, *args, **kwargs):
        QtGui.QTextObject.__init__(self, *args)
        super().__init__(**kwargs)


class TextTable(AbstractQObject, QtGui.QTextTable):
    def __init__(self, *args, **kwargs):
        QtGui.QTextTable.__init__(self, *args)
        super().__init__(**kwargs)


class UndoGroup(AbstractQObject, QtGui.QUndoGroup):
    def __init__(self, *args, **kwargs):
        QtGui.QUndoGroup.__init__(self, *args)
        super().__init__(**kwargs)


class UndoStack(AbstractQObject, QtGui.QUndoStack):
    def __init__(self, *args, **kwargs):
        QtGui.QUndoStack.__init__(self, *args)
        super().__init__(**kwargs)


class Validator(AbstractQObject, QtGui.QValidator):
    def __init__(self, *args, **kwargs):
        QtGui.QValidator.__init__(self, *args)
        super().__init__(**kwargs)


class Window(AbstractQObject, QtGui.QWindow):
    def __init__(self, *args, **kwargs):
        QtGui.QWindow.__init__(self, *args)
        super().__init__(**kwargs)
