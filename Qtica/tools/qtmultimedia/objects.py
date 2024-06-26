from ...core import AbstractQObject
from qtpy import QtMultimedia


class AudioDecoder(AbstractQObject, QtMultimedia.QAudioDecoder):
    def __init__(self, *args, **kwargs):
        QtMultimedia.QAudioDecoder.__init__(self, *args)
        super().__init__(**kwargs)


class AudioInput(AbstractQObject, QtMultimedia.QAudioInput):
    def __init__(self, *args, **kwargs):
        QtMultimedia.QAudioInput.__init__(self, *args)
        super().__init__(**kwargs)


class AudioOutput(AbstractQObject, QtMultimedia.QAudioOutput):
    def __init__(self, *args, **kwargs):
        QtMultimedia.QAudioOutput.__init__(self, *args)
        super().__init__(**kwargs)


class AudioSink(AbstractQObject, QtMultimedia.QAudioSink):
    def __init__(self, *args, **kwargs):
        QtMultimedia.QAudioSink.__init__(self, *args)
        super().__init__(**kwargs)


class AudioSource(AbstractQObject, QtMultimedia.QAudioSource):
    def __init__(self, *args, **kwargs):
        QtMultimedia.QAudioSource.__init__(self, *args)
        super().__init__(**kwargs)


class Camera(AbstractQObject, QtMultimedia.QCamera):
    def __init__(self, *args, **kwargs):
        QtMultimedia.QCamera.__init__(self, *args)
        super().__init__(**kwargs)


class ImageCapture(AbstractQObject, QtMultimedia.QImageCapture):
    def __init__(self, *args, **kwargs):
        QtMultimedia.QImageCapture.__init__(self, *args)
        super().__init__(**kwargs)


class MediaCaptureSession(AbstractQObject, QtMultimedia.QMediaCaptureSession):
    def __init__(self, *args, **kwargs):
        QtMultimedia.QMediaCaptureSession.__init__(self, *args)
        super().__init__(**kwargs)


class MediaDevices(AbstractQObject, QtMultimedia.QMediaDevices):
    def __init__(self, *args, **kwargs):
        QtMultimedia.QMediaDevices.__init__(self, *args)
        super().__init__(**kwargs)


class MediaPlayer(AbstractQObject, QtMultimedia.QMediaPlayer):
    def __init__(self, *args, **kwargs):
        QtMultimedia.QMediaPlayer.__init__(self, *args)
        super().__init__(**kwargs)


class MediaRecorder(AbstractQObject, QtMultimedia.QMediaRecorder):
    def __init__(self, *args, **kwargs):
        QtMultimedia.QMediaRecorder.__init__(self, *args)
        super().__init__(**kwargs)


class ScreenCapture(AbstractQObject, QtMultimedia.QScreenCapture):
    def __init__(self, *args, **kwargs):
        QtMultimedia.QScreenCapture.__init__(self, *args)
        super().__init__(**kwargs)


class SoundEffect(AbstractQObject, QtMultimedia.QSoundEffect):
    def __init__(self, *args, **kwargs):
        QtMultimedia.QSoundEffect.__init__(self, *args)
        super().__init__(**kwargs)


class VideoSink(AbstractQObject, QtMultimedia.QVideoSink):
    def __init__(self, *args, **kwargs):
        QtMultimedia.QVideoSink.__init__(self, *args)
        super().__init__(**kwargs)


class WindowCapture(AbstractQObject, QtMultimedia.QWindowCapture):
    def __init__(self, *args, **kwargs):
        QtMultimedia.QWindowCapture.__init__(self, *args)
        super().__init__(**kwargs)
