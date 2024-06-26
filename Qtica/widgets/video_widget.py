from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtMultimedia import QMediaPlayer
from ..core import AbstractWidget


class VideoWidget(AbstractWidget, QVideoWidget):
    def __init__(self, 
                 *, 
                 player: QMediaPlayer = None,
                 running: bool = True, 
                 **kwargs):
        QVideoWidget.__init__(self)
        super().__init__(**kwargs)

        if not player:
            return

        player.setParent(self)
        player.setVideoOutput(self)

        if running and not player.isPlaying():
            player.play()
