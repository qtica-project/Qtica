#!/usr/bin/python3
# -*- coding: utf-8 -*-

from ..core import AbstractQObject
from PySide6.QtMultimedia import QMediaPlayer


class MediaPlayer(AbstractQObject, QMediaPlayer):
    def __init__(self, running: bool = False, **kwargs):
        QMediaPlayer.__init__(self)
        super().__init__(**kwargs)

        if (audio_out := kwargs.get("setAudioOutput", None)):
            audio_out.setParent(self)

        if (video_sink := kwargs.get("setVideoSink", None)):
            video_sink.setParent(self)

        if running:
            self.play()