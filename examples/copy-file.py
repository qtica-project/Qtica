# import Qtica_path

from Qtica.core import (
    BehaviorDeclarative,
    WidgetBase,
    Api
)

from Qtica.widgets import (
    App,
    MainWindow,
)

from Qtica.layouts import (
    FormLayout,
    FormLayoutItemWrapper,
    VLayout,
    HLayout
)

from Qtica.tools import (
    CopyProgress
)

from PySide6.QtWidgets import (
    QPushButton,
    QProgressBar,
    QLineEdit,
    QLabel
    
)

def push_button(text: str, on_click):
    btn = QPushButton()
    btn.setText(text)
    btn.clicked.connect(on_click)
    return btn


class LineEdit(WidgetBase, QLineEdit):
    def __init__(self, *args, **kwargs):
        QLineEdit.__init__(self)
        super().__init__(**kwargs)
        


class Window(BehaviorDeclarative):
    def __init__(self):
        return MainWindow(
            uid = "window",
            home=VLayout(
                children=[
                    FormLayout(
                        children=[
                            FormLayoutItemWrapper(
                                label=QLabel("Enter Source file"),
                                field=LineEdit(
                                    uid="src", 
                                    signals=[
                                            ("textChanged", 
                                             lambda value: Api.fetch("cp").set_src(value))
                                        ]
                                    ),
                            ),
                            FormLayoutItemWrapper(
                                label=QLabel("Enter Destintioin path"),
                                field=LineEdit(
                                    uid="dst", 
                                    signals=[
                                        ("textChanged", 
                                         lambda value: Api.fetch("cp").set_dst(value))
                                    ]
                                ),
                            )
                        ]
                    ),

                    CopyProgress(
                        uid = "cp",
                        child=QProgressBar(maximum=100),
                        src=Api.fetch("src").text(),
                        dst=Api.fetch("dst").text(),
                        signals = [
                            ("copy_progress", lambda value: print(f"{value}%")),
                            ("copy_done", lambda: print("Copy Done"))
                        ]
                    ),

                    HLayout(
                        children=[
                            push_button("Copy", Api.declarative_fetch("cp").start),
                            push_button("Pause", Api.declarative_fetch("cp").pause),
                            push_button("Resum", Api.declarative_fetch("cp").resum)
                        ]
                    )
                ]
            )
        )


def main():
    import sys
    app = App(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()