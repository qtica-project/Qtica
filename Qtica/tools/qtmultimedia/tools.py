from PySide6 import QtMultimedia
from ...core import AbstractTool


class Audio(AbstractTool, QtMultimedia.QAudio):
    def __init__(self, *args, **kwargs):
        QtMultimedia.QAudio.__init__(self, *args)
        super().__init__(**kwargs)


class AudioBuffer(AbstractTool, QtMultimedia.QAudioBuffer):
    def __init__(self, *args, **kwargs):
        QtMultimedia.QAudioBuffer.__init__(self, *args)
        super().__init__(**kwargs)


class AudioDevice(AbstractTool, QtMultimedia.QAudioDevice):
    def __init__(self, *args, **kwargs):
        QtMultimedia.QAudioDevice.__init__(self, *args)
        super().__init__(**kwargs)


class AudioFormat(AbstractTool, QtMultimedia.QAudioFormat):
    def __init__(self, *args, **kwargs):
        QtMultimedia.QAudioFormat.__init__(self, *args)
        super().__init__(**kwargs)


class CameraDevice(AbstractTool, QtMultimedia.QCameraDevice):
    def __init__(self, *args, **kwargs):
        QtMultimedia.QCameraDevice.__init__(self, *args)
        super().__init__(**kwargs)


class CameraFormat(AbstractTool, QtMultimedia.QCameraFormat):
    def __init__(self, *args, **kwargs):
        QtMultimedia.QCameraFormat.__init__(self, *args)
        super().__init__(**kwargs)


class CapturableWindow(AbstractTool, QtMultimedia.QCapturableWindow):
    def __init__(self, *args, **kwargs):
        QtMultimedia.QCapturableWindow.__init__(self, *args)
        super().__init__(**kwargs)


class MediaFormat(AbstractTool, QtMultimedia.QMediaFormat):
    def __init__(self, *args, **kwargs):
        QtMultimedia.QMediaFormat.__init__(self, *args)
        super().__init__(**kwargs)


class MediaMetaData(AbstractTool, QtMultimedia.QMediaMetaData):
    def __init__(self, *args, **kwargs):
        QtMultimedia.QMediaMetaData.__init__(self, *args)
        super().__init__(**kwargs)


class MediaTimeRange(AbstractTool, QtMultimedia.QMediaTimeRange):
    def __init__(self, *args, **kwargs):
        QtMultimedia.QMediaTimeRange.__init__(self, *args)
        super().__init__(**kwargs)


class VideoFrame(AbstractTool, QtMultimedia.QVideoFrame):
    def __init__(self, *args, **kwargs):
        QtMultimedia.QVideoFrame.__init__(self, *args)
        super().__init__(**kwargs)


class VideoFrameFormat(AbstractTool, QtMultimedia.QVideoFrameFormat):
    def __init__(self, *args, **kwargs):
        QtMultimedia.QVideoFrameFormat.__init__(self, *args)
        super().__init__(**kwargs)
