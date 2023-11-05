# import qtica_path

from PySide6.QtWidgets import QSpinBox
from PySide6.QtCore import QSize
from Qtica import (
    BehaviorDeclarative,
    Api
)

from Qtica.widgets import (
    Application,
    MainWindow,
    PushButton,
    Label
)

from Qtica.layouts import (
    VLayout,
    HLayout
)

from Qtica.tools import (
    Alignment
)


def spin_box(uid: str):
    line = QSpinBox()
    line.setRange(0, 9)
    line.setValue(0)
    line.setObjectName(uid)
    return line


class VersionInputs(BehaviorDeclarative):
    def __init__(self) -> None:
        return HLayout(
                children=[
                    VLayout(
                        children=[
                            Label(text="Major"),
                            spin_box(uid="major")
                        ]
                    ),
                    VLayout(
                        children=[
                            Label(text="Minor"),
                            spin_box(uid="minor")
                        ]
                    ),
                    VLayout(
                        children=[
                            Label(text="Patch"),
                            spin_box(uid="patch")
                        ]
                    )
                ]
            )


class Home(BehaviorDeclarative):
    def version_increment(self):
        major = Api.fetch("major").value()
        minor = Api.fetch("minor").value()
        patch = Api.fetch("patch").value()

        if patch < 9:
            major, minor, patch = (major, minor, patch + 1)
        elif minor < 9:
            major, minor, patch = (major, minor + 1, 0)
        else:
            major, minor, patch = (major + 1, 0, 0)

        Api.fetch("version_display").setText(f"v{major}.{minor}.{patch}")

    def __init__(self):
        return VLayout(
            children=[
                VersionInputs(),
                PushButton(
                    uid="increment",
                    text="increment".title(),
                    signals=[("clicked", lambda: self.version_increment())]),
                Alignment(child=Label(uid="version_display"))
            ]
        )


class Window(BehaviorDeclarative):
    def __init__(self):
        return MainWindow(
            uid="window",
            windowTitle = "Version Generator",
            minimumSize = QSize(500, 150),
            resize = QSize(500, 150),
            home=Home()
        )


def main():
    import sys
    app = Application(
        arg = sys.argv
    )
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()