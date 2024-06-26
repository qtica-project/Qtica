from PySide6 import QtWidgets
from ..core import AbstractWidget


class Widget(AbstractWidget, QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args)
        super().__init__(**kwargs)


class Frame(AbstractWidget, QtWidgets.QFrame):
    def __init__(self, *args, **kwargs):
        QtWidgets.QFrame.__init__(self, *args)
        super().__init__(**kwargs)


class CalendarWidget(AbstractWidget, QtWidgets.QCalendarWidget):
    def __init__(self, *args, **kwargs):
        QtWidgets.QCalendarWidget.__init__(self, *args)
        super().__init__(**kwargs)


class CheckBox(AbstractWidget, QtWidgets.QCheckBox):
    def __init__(self, *args, **kwargs):
        QtWidgets.QCheckBox.__init__(self, *args)
        super().__init__(**kwargs)


class ColorDialog(AbstractWidget, QtWidgets.QColorDialog):
    def __init__(self, *args, **kwargs):
        QtWidgets.QColorDialog.__init__(self, *args)
        super().__init__(**kwargs)


class ColumnView(AbstractWidget, QtWidgets.QColumnView):
    def __init__(self, *args, **kwargs):
        QtWidgets.QColumnView.__init__(self, *args)
        super().__init__(**kwargs)


class ComboBox(AbstractWidget, QtWidgets.QComboBox):
    def __init__(self, *args, **kwargs):
        QtWidgets.QComboBox.__init__(self, *args)
        super().__init__(**kwargs)


class DateEdit(AbstractWidget, QtWidgets.QDateEdit):
    def __init__(self, *args, **kwargs):
        QtWidgets.QDateEdit.__init__(self, *args)
        super().__init__(**kwargs)


class DateTimeEdit(AbstractWidget, QtWidgets.QDateTimeEdit):
    def __init__(self, *args, **kwargs):
        QtWidgets.QDateTimeEdit.__init__(self, *args)
        super().__init__(**kwargs)


class Dial(AbstractWidget, QtWidgets.QDial):
    def __init__(self, *args, **kwargs):
        QtWidgets.QDial.__init__(self, *args)
        super().__init__(**kwargs)


class Dialog(AbstractWidget, QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        QtWidgets.QDialog.__init__(self, *args)
        super().__init__(**kwargs)


class DialogButtonBox(AbstractWidget, QtWidgets.QDialogButtonBox):
    def __init__(self, *args, **kwargs):
        QtWidgets.QDialogButtonBox.__init__(self, *args)
        super().__init__(**kwargs)


class DockWidget(AbstractWidget, QtWidgets.QDockWidget):
    def __init__(self, *args, **kwargs):
        QtWidgets.QDockWidget.__init__(self, *args)
        super().__init__(**kwargs)


class DoubleSpinBox(AbstractWidget, QtWidgets.QDoubleSpinBox):
    def __init__(self, *args, **kwargs):
        QtWidgets.QDoubleSpinBox.__init__(self, *args)
        super().__init__(**kwargs)


class ErrorMessage(AbstractWidget, QtWidgets.QErrorMessage):
    def __init__(self, *args, **kwargs):
        QtWidgets.QErrorMessage.__init__(self, *args)
        super().__init__(**kwargs)


class FileDialog(AbstractWidget, QtWidgets.QFileDialog):
    def __init__(self, *args, **kwargs):
        QtWidgets.QFileDialog.__init__(self, *args)
        super().__init__(**kwargs)


class FocusFrame(AbstractWidget, QtWidgets.QFocusFrame):
    def __init__(self, *args, **kwargs):
        QtWidgets.QFocusFrame.__init__(self, *args)
        super().__init__(**kwargs)


class FontComboBox(AbstractWidget, QtWidgets.QFontComboBox):
    def __init__(self, *args, **kwargs):
        QtWidgets.QFontComboBox.__init__(self, *args)
        super().__init__(**kwargs)


class FontDialog(AbstractWidget, QtWidgets.QFontDialog):
    def __init__(self, *args, **kwargs):
        QtWidgets.QFontDialog.__init__(self, *args)
        super().__init__(**kwargs)


class GraphicsProxyWidget(AbstractWidget, QtWidgets.QGraphicsProxyWidget):
    def __init__(self, *args, **kwargs):
        QtWidgets.QGraphicsProxyWidget.__init__(self, *args)
        super().__init__(**kwargs)


class GraphicsView(AbstractWidget, QtWidgets.QGraphicsView):
    def __init__(self, *args, **kwargs):
        QtWidgets.QGraphicsView.__init__(self, *args)
        super().__init__(**kwargs)


class GraphicsWidget(AbstractWidget, QtWidgets.QGraphicsWidget):
    def __init__(self, *args, **kwargs):
        QtWidgets.QGraphicsWidget.__init__(self, *args)
        super().__init__(**kwargs)


class HeaderView(AbstractWidget, QtWidgets.QHeaderView):
    def __init__(self, *args, **kwargs):
        QtWidgets.QHeaderView.__init__(self, *args)
        super().__init__(**kwargs)


class InputDialog(AbstractWidget, QtWidgets.QInputDialog):
    def __init__(self, *args, **kwargs):
        QtWidgets.QInputDialog.__init__(self, *args)
        super().__init__(**kwargs)


class KeySequenceEdit(AbstractWidget, QtWidgets.QKeySequenceEdit):
    def __init__(self, *args, **kwargs):
        QtWidgets.QKeySequenceEdit.__init__(self, *args)
        super().__init__(**kwargs)


class LCDNumber(AbstractWidget, QtWidgets.QLCDNumber):
    def __init__(self, *args, **kwargs):
        QtWidgets.QLCDNumber.__init__(self, *args)
        super().__init__(**kwargs)


class LineEdit(AbstractWidget, QtWidgets.QLineEdit):
    def __init__(self, *args, **kwargs):
        QtWidgets.QLineEdit.__init__(self, *args)
        super().__init__(**kwargs)


class ListView(AbstractWidget, QtWidgets.QListView):
    def __init__(self, *args, **kwargs):
        QtWidgets.QListView.__init__(self, *args)
        super().__init__(**kwargs)


class ListWidget(AbstractWidget, QtWidgets.QListWidget):
    def __init__(self, *args, **kwargs):
        QtWidgets.QListWidget.__init__(self, *args)
        super().__init__(**kwargs)

    def addItemWidget(self, item: QtWidgets.QListWidgetItem, widget: QtWidgets.QWidget) -> None:
        self.addItem(item)
        self.setItemWidget(item, widget)


class MdiArea(AbstractWidget, QtWidgets.QMdiArea):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMdiArea.__init__(self, *args)
        super().__init__(**kwargs)


class MdiSubWindow(AbstractWidget, QtWidgets.QMdiSubWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMdiSubWindow.__init__(self, *args)
        super().__init__(**kwargs)


class MenuBar(AbstractWidget, QtWidgets.QMenuBar):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMenuBar.__init__(self, *args)
        super().__init__(**kwargs)


class MessageBox(AbstractWidget, QtWidgets.QMessageBox):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMessageBox.__init__(self, *args)
        super().__init__(**kwargs)


class PlainTextEdit(AbstractWidget, QtWidgets.QPlainTextEdit):
    def __init__(self, *args, **kwargs):
        QtWidgets.QPlainTextEdit.__init__(self, *args)
        super().__init__(**kwargs)


class ProgressBar(AbstractWidget, QtWidgets.QProgressBar):
    def __init__(self, *args, **kwargs):
        QtWidgets.QProgressBar.__init__(self, *args)
        super().__init__(**kwargs)


class ProgressDialog(AbstractWidget, QtWidgets.QProgressDialog):
    def __init__(self, *args, **kwargs):
        QtWidgets.QProgressDialog.__init__(self, *args)
        super().__init__(**kwargs)


class RubberBand(AbstractWidget, QtWidgets.QRubberBand):
    def __init__(self, *args, **kwargs):
        QtWidgets.QRubberBand.__init__(self, *args)
        super().__init__(**kwargs)


class ScrollBar(AbstractWidget, QtWidgets.QScrollBar):
    def __init__(self, *args, **kwargs):
        QtWidgets.QScrollBar.__init__(self, *args)
        super().__init__(**kwargs)


class SizeGrip(AbstractWidget, QtWidgets.QSizeGrip):
    def __init__(self, *args, **kwargs):
        QtWidgets.QSizeGrip.__init__(self, *args)
        super().__init__(**kwargs)


class Slider(AbstractWidget, QtWidgets.QSlider):
    def __init__(self, *args, **kwargs):
        QtWidgets.QSlider.__init__(self, *args)
        super().__init__(**kwargs)


class SpinBox(AbstractWidget, QtWidgets.QSpinBox):
    def __init__(self, *args, **kwargs):
        QtWidgets.QSpinBox.__init__(self, *args)
        super().__init__(**kwargs)


class SplashScreen(AbstractWidget, QtWidgets.QSplashScreen):
    def __init__(self, *args, **kwargs):
        QtWidgets.QSplashScreen.__init__(self, *args)
        super().__init__(**kwargs)


class Splitter(AbstractWidget, QtWidgets.QSplitter):
    def __init__(self, *args, **kwargs):
        QtWidgets.QSplitter.__init__(self, *args)
        super().__init__(**kwargs)


class SplitterHandle(AbstractWidget, QtWidgets.QSplitterHandle):
    def __init__(self, *args, **kwargs):
        QtWidgets.QSplitterHandle.__init__(self, *args)
        super().__init__(**kwargs)


class StatusBar(AbstractWidget, QtWidgets.QStatusBar):
    def __init__(self, *args, **kwargs):
        QtWidgets.QStatusBar.__init__(self, *args)
        super().__init__(**kwargs)


class TabBar(AbstractWidget, QtWidgets.QTabBar):
    def __init__(self, *args, **kwargs):
        QtWidgets.QTabBar.__init__(self, *args)
        super().__init__(**kwargs)


class TabWidget(AbstractWidget, QtWidgets.QTabWidget):
    def __init__(self, *args, **kwargs):
        QtWidgets.QTabWidget.__init__(self, *args)
        super().__init__(**kwargs)


class TableView(AbstractWidget, QtWidgets.QTableView):
    def __init__(self, *args, **kwargs):
        QtWidgets.QTableView.__init__(self, *args)
        super().__init__(**kwargs)


class TableWidget(AbstractWidget, QtWidgets.QTableWidget):
    def __init__(self, *args, **kwargs):
        QtWidgets.QTableWidget.__init__(self, *args)
        super().__init__(**kwargs)


class TextBrowser(AbstractWidget, QtWidgets.QTextBrowser):
    def __init__(self, *args, **kwargs):
        QtWidgets.QTextBrowser.__init__(self, *args)
        super().__init__(**kwargs)


class TextEdit(AbstractWidget, QtWidgets.QTextEdit):
    def __init__(self, *args, **kwargs):
        QtWidgets.QTextEdit.__init__(self, *args)
        super().__init__(**kwargs)


class TimeEdit(AbstractWidget, QtWidgets.QTimeEdit):
    def __init__(self, *args, **kwargs):
        QtWidgets.QTimeEdit.__init__(self, *args)
        super().__init__(**kwargs)


class ToolBar(AbstractWidget, QtWidgets.QToolBar):
    def __init__(self, *args, **kwargs):
        QtWidgets.QToolBar.__init__(self, *args)
        super().__init__(**kwargs)


class ToolBox(AbstractWidget, QtWidgets.QToolBox):
    def __init__(self, *args, **kwargs):
        QtWidgets.QToolBox.__init__(self, *args)
        super().__init__(**kwargs)


class TreeView(AbstractWidget, QtWidgets.QTreeView):
    def __init__(self, *args, **kwargs):
        QtWidgets.QTreeView.__init__(self, *args)
        super().__init__(**kwargs)


class TreeWidget(AbstractWidget, QtWidgets.QTreeWidget):
    def __init__(self, *args, **kwargs):
        QtWidgets.QTreeWidget.__init__(self, *args)
        super().__init__(**kwargs)


class UndoView(AbstractWidget, QtWidgets.QUndoView):
    def __init__(self, *args, **kwargs):
        QtWidgets.QUndoView.__init__(self, *args)
        super().__init__(**kwargs)


class Wizard(AbstractWidget, QtWidgets.QWizard):
    def __init__(self, *args, **kwargs):
        QtWidgets.QWizard.__init__(self, *args)
        super().__init__(**kwargs)


class WizardPage(AbstractWidget, QtWidgets.QWizardPage):
    def __init__(self, *args, **kwargs):
        QtWidgets.QWizardPage.__init__(self, *args)
        super().__init__(**kwargs)
