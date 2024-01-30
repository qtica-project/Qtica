#!/usr/bin/python3

from PySide6 import QtCore
from ...core import AbstractQObject


class AnimationGroup(AbstractQObject, QtCore.QAnimationGroup):
    def __init__(self, *args, **kwargs):
        QtCore.QAnimationGroup.__init__(self, *args)
        super().__init__(**kwargs)


class Buffer(AbstractQObject, QtCore.QBuffer):
    def __init__(self, *args, **kwargs):
        QtCore.QBuffer.__init__(self, *args)
        super().__init__(**kwargs)


class ConcatenateTablesProxyModel(AbstractQObject, QtCore.QConcatenateTablesProxyModel):
    def __init__(self, *args, **kwargs):
        QtCore.QConcatenateTablesProxyModel.__init__(self, *args)
        super().__init__(**kwargs)


class CoreApplication(AbstractQObject, QtCore.QCoreApplication):
    def __init__(self, *args, **kwargs):
        QtCore.QCoreApplication.__init__(self, *args)
        super().__init__(**kwargs)


class EventLoop(AbstractQObject, QtCore.QEventLoop):
    def __init__(self, *args, **kwargs):
        QtCore.QEventLoop.__init__(self, *args)
        super().__init__(**kwargs)


class FileDevice(AbstractQObject, QtCore.QFileDevice):
    def __init__(self, *args, **kwargs):
        QtCore.QFileDevice.__init__(self, *args)
        super().__init__(**kwargs)


class FileSelector(AbstractQObject, QtCore.QFileSelector):
    def __init__(self, *args, **kwargs):
        QtCore.QFileSelector.__init__(self, *args)
        super().__init__(**kwargs)


class FileSystemWatcher(AbstractQObject, QtCore.QFileSystemWatcher):
    def __init__(self, *args, **kwargs):
        QtCore.QFileSystemWatcher.__init__(self, *args)
        super().__init__(**kwargs)


class IODevice(AbstractQObject, QtCore.QIODevice):
    def __init__(self, *args, **kwargs):
        QtCore.QIODevice.__init__(self, *args)
        super().__init__(**kwargs)


class IdentityProxyModel(AbstractQObject, QtCore.QIdentityProxyModel):
    def __init__(self, *args, **kwargs):
        QtCore.QIdentityProxyModel.__init__(self, *args)
        super().__init__(**kwargs)


class ItemSelectionModel(AbstractQObject, QtCore.QItemSelectionModel):
    def __init__(self, *args, **kwargs):
        QtCore.QItemSelectionModel.__init__(self, *args)
        super().__init__(**kwargs)


class Library(AbstractQObject, QtCore.QLibrary):
    def __init__(self, *args, **kwargs):
        QtCore.QLibrary.__init__(self, *args)
        super().__init__(**kwargs)


class MimeData(AbstractQObject, QtCore.QMimeData):
    def __init__(self, *args, **kwargs):
        QtCore.QMimeData.__init__(self, *args)
        super().__init__(**kwargs)


class PauseAnimation(AbstractQObject, QtCore.QPauseAnimation):
    def __init__(self, *args, **kwargs):
        QtCore.QPauseAnimation.__init__(self, *args)
        super().__init__(**kwargs)


class PluginLoader(AbstractQObject, QtCore.QPluginLoader):
    def __init__(self, *args, **kwargs):
        QtCore.QPluginLoader.__init__(self, *args)
        super().__init__(**kwargs)


class Process(AbstractQObject, QtCore.QProcess):
    def __init__(self, *args, **kwargs):
        QtCore.QProcess.__init__(self, *args)
        super().__init__(**kwargs)


class SaveFile(AbstractQObject, QtCore.QSaveFile):
    def __init__(self, *args, **kwargs):
        QtCore.QSaveFile.__init__(self, *args)
        super().__init__(**kwargs)


class SharedMemory(AbstractQObject, QtCore.QSharedMemory):
    def __init__(self, *args, **kwargs):
        QtCore.QSharedMemory.__init__(self, *args)
        super().__init__(**kwargs)


class SignalMapper(AbstractQObject, QtCore.QSignalMapper):
    def __init__(self, *args, **kwargs):
        QtCore.QSignalMapper.__init__(self, *args)
        super().__init__(**kwargs)


class SocketNotifier(AbstractQObject, QtCore.QSocketNotifier):
    def __init__(self, *args, **kwargs):
        QtCore.QSocketNotifier.__init__(self, *args)
        super().__init__(**kwargs)


class SortFilterProxyModel(AbstractQObject, QtCore.QSortFilterProxyModel):
    def __init__(self, *args, **kwargs):
        QtCore.QSortFilterProxyModel.__init__(self, *args)
        super().__init__(**kwargs)


class StringListModel(AbstractQObject, QtCore.QStringListModel):
    def __init__(self, *args, **kwargs):
        QtCore.QStringListModel.__init__(self, *args)
        super().__init__(**kwargs)


class TemporaryFile(AbstractQObject, QtCore.QTemporaryFile):
    def __init__(self, *args, **kwargs):
        QtCore.QTemporaryFile.__init__(self, *args)
        super().__init__(**kwargs)


class Thread(AbstractQObject, QtCore.QThread):
    def __init__(self, *args, **kwargs):
        QtCore.QThread.__init__(self, *args)
        super().__init__(**kwargs)


class ThreadPool(AbstractQObject, QtCore.QThreadPool):
    def __init__(self, *args, **kwargs):
        QtCore.QThreadPool.__init__(self, *args)
        super().__init__(**kwargs)


class TimeLine(AbstractQObject, QtCore.QTimeLine):
    def __init__(self, *args, **kwargs):
        QtCore.QTimeLine.__init__(self, *args)
        super().__init__(**kwargs)


class Timer(AbstractQObject, QtCore.QTimer):
    def __init__(self, *args, **kwargs):
        QtCore.QTimer.__init__(self, *args)
        super().__init__(**kwargs)


class Translator(AbstractQObject, QtCore.QTranslator):
    def __init__(self, *args, **kwargs):
        QtCore.QTranslator.__init__(self, *args)
        super().__init__(**kwargs)


class TransposeProxyModel(AbstractQObject, QtCore.QTransposeProxyModel):
    def __init__(self, *args, **kwargs):
        QtCore.QTransposeProxyModel.__init__(self, *args)
        super().__init__(**kwargs)


class VariantAnimation(AbstractQObject, QtCore.QVariantAnimation):
    def __init__(self, *args, **kwargs):
        QtCore.QVariantAnimation.__init__(self, *args)
        super().__init__(**kwargs)
