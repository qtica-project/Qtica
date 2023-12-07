from typing import Optional
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QVBoxLayout, QStackedWidget, QWidget
from .nav_bar import NavBar
from .nav_bar_button import NavBarButton
from ...core import WidgetBase


class _NavBarWidget(QWidget):
    def __init__(self, 
                 parent: Optional[QWidget] = None,
                 stacked_widget: QStackedWidget = None) -> None:
        super().__init__(parent)

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        # Layout for this widget
        self._layout = QVBoxLayout(self)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)

        # Background frame and its layout
        self._bg_frame = QFrame(self)

        self._bg_frame_layout = QVBoxLayout(self._bg_frame)
        self._bg_frame_layout.setContentsMargins(5, 5, 5, 5)
        self._bg_frame_layout.setSpacing(10)
        self._layout.addWidget(self._bg_frame)

        # Menu bar
        self._nav_bar = NavBar(self)
        # self._nav_bar.setFixedWidth(self.width())
        self._nav_bar.setFixedHeight(60)

        # Stacked widget and its layout
        if stacked_widget is not None:
            self._stacked_widget = stacked_widget
            self._stacked_widget.setParent(self)
        else:
            self._stacked_widget = QStackedWidget(self)

        self._bg_frame_layout.addWidget(self._stacked_widget)
        self._bg_frame_layout.addWidget(self._nav_bar)

    def addPage(self, 
                page: QWidget,
                button: NavBarButton, 
                button_alignment: NavBarButton.Alignment = NavBarButton.Alignment.left) -> None:

        if not hasattr(button, "clicked"):
            raise ValueError("invalid button value!")

        self._nav_bar.addButton(button, button_alignment)
        self._stacked_widget.addWidget(page)
        button.clicked.connect(lambda: self._stacked_widget.setCurrentWidget(page))  # type: ignore[attr-defined]


class NavBarItemWrapper:
    def __init__(self, 
                 *,
                 page: QWidget,
                 button: NavBarButton | QWidget,
                 alignment: NavBarButton.Alignment = NavBarButton.Alignment.left):

        self.page = page
        self.button = button
        self.alignment = alignment


class NavBarWidget(WidgetBase, _NavBarWidget):
    def __init__(self, 
                 *,
                 children: list[NavBarItemWrapper] = None,
                 stacked_widget: QStackedWidget = None,
                 **kwargs):
        _NavBarWidget.__init__(self, None, stacked_widget)
        super().__init__(**kwargs)

        if children is not None:
            for child in children:
                self.addPage(
                    child.page,
                    child.button,
                    child.alignment
                )