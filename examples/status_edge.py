# import qtica_path

from Qtica import (
    BehaviorDeclarative,
    Api
)

from Qtica.widgets import (
    Application,
    MainWindow,
    PushButton
)

from Qtica.layouts import (
    VLayout
)

from Qtica.tools import (
    Color,
    StatusEdgePaint
)


class Home(BehaviorDeclarative):
    def update_status(self):
        btn = Api.fetch("status_btn")
        paint = Api.fetch("status_paint")

        if btn.text().lower() == "online":
            btn.setText("Offline")
            paint.set_status_color(Color("red"))
        else:
            btn.setText("Online")
            paint.set_status_color(Color("green"))

    def __init__(self):
        return VLayout(
            children=[
                PushButton(
                    text="Change Status",
                    signals=[
                        ("clicked", lambda: self.update_status())
                    ]
                ),
                StatusEdgePaint(
                    uid="status_paint",
                    child=PushButton(
                        uid="status_btn", 
                        text="Online"
                    ),
                    status_color=Color("green")
                )
            ]
        )


class Window(BehaviorDeclarative):
    def __init__(self) -> None:
        return MainWindow(
            uid="window",
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