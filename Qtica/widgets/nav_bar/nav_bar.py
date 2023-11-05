from typing import List, Optional
from PySide6.QtGui import QColor, QResizeEvent
from PySide6.QtWidgets import QFrame, QSizePolicy, QSpacerItem, QHBoxLayout, QWidget
from .nav_bar_button import NavBarButton


_BG_FRAME_STYLESHEET = """\
QFrame#_nav_bar_bg_frame {{
    background-color: {bg_color};
    border: none;
    border-radius: 8px;
}}
"""


class NavBar(QWidget):
    def __init__(self, 
                 parent: Optional[QWidget] = None,
                 bg_color: QColor = QColor("#191E23")) -> None:
        super().__init__(parent)

        # Define attributes
        self._first_button = True
        self._left_buttons: List[NavBarButton] = []
        self._right_buttons: List[NavBarButton] = []
        self._center_buttons: List[NavBarButton] = []

        # Layout for this widget
        self._layout = QHBoxLayout(self)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)

        # Background frame and its layout
        self._bg_frame = QFrame(self)
        self._bg_frame.setObjectName("_nav_bar_bg_frame")

        self._bg_layout = QHBoxLayout(self._bg_frame)
        self._bg_layout.setContentsMargins(15, 0, 15, 0)
        self._bg_layout.setSpacing(0)

        self._layout.addWidget(self._bg_frame)

        # Left nav bar buttons frame and its layout
        self._left_frame = QFrame(self._bg_frame)
        self._left_frame_layout = QHBoxLayout(self._left_frame)
        self._left_frame_layout.setContentsMargins(0, 0, 0, 0)
        self._left_frame_layout.setSpacing(0)
        self._bg_layout.addWidget(self._left_frame)

        # Horizontal spacer between left and right bar
        self._horizontal_spacer = QSpacerItem(0, 0, 
                                            QSizePolicy.Policy.Expanding,
                                            QSizePolicy.Policy.Minimum)
        self._bg_layout.addItem(self._horizontal_spacer)

        # Left nav bar buttons frame and its layout
        self._center_frame = QFrame(self._bg_frame)
        self._center_frame_layout = QHBoxLayout(self._center_frame)
        self._center_frame_layout.setContentsMargins(0, 0, 0, 0)
        self._center_frame_layout.setSpacing(0)
        self._bg_layout.addWidget(self._center_frame)

        # Horizontal spacer between left and right bar
        self._horizontal_spacer = QSpacerItem(0, 0, 
                                            QSizePolicy.Policy.Expanding,
                                            QSizePolicy.Policy.Minimum)
        self._bg_layout.addItem(self._horizontal_spacer)

        # Bottom side bar buttons frame and its layout
        self._right_frame = QFrame(self._bg_frame)
        self._right_frame_layout = QHBoxLayout(self._right_frame)
        self._right_frame_layout.setContentsMargins(0, 0, 0, 0)
        self._right_frame_layout.setSpacing(0)
        self._bg_layout.addWidget(self._right_frame)

        self.setBackgroundColor(bg_color)

    def setBackgroundColor(self, color: QColor("#191E23")) -> None:
        self._bg_frame.setStyleSheet(_BG_FRAME_STYLESHEET.format(bg_color=color.name()))

    def resizeEvent(self, event: QResizeEvent) -> None:
        super().resizeEvent(event)

        buttons: List[NavBarButton] = self.findChildren(NavBarButton)
        for button in buttons:
            button.setFixedSize(self.height(), self.height())

    def addButton(self,
                  button: NavBarButton, 
                  alignment: NavBarButton.Alignment = NavBarButton.Alignment.left) -> None:

        button.setParent(self)
        button.clicked.connect(self._buttonCallback)  # type: ignore[attr-defined]

        if alignment == NavBarButton.Alignment.left:
            self._left_buttons.append(button)
            self._left_frame_layout.addWidget(button)

        elif alignment == NavBarButton.Alignment.center:
            self._center_buttons.append(button)
            self._center_frame_layout.addWidget(button)

        elif alignment == NavBarButton.Alignment.right:
            self._right_buttons.append(button)
            self._right_frame_layout.addWidget(button)

        else:
            raise ValueError(
                "Invalid value for 'alignment'!"
                "Supported values are 'NavBarButton.Alignment.left' and 'NavBarButton.Alignment.right'."
            )

        # Select the first button as default
        if self._first_button:
            button.click()
            self._first_button = False

    def _buttonCallback(self):
        buttons: List[NavBarButton] = self.findChildren(NavBarButton)
        for button in buttons:
            if button == self.sender():
                button.setChecked(True)
            else:
                button.setChecked(False)