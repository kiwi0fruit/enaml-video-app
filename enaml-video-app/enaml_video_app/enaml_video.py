"""
Enaml video application.
https://github.com/kiwi0fruit/enaml-video-app
"""
import os
try:
    pass
    import PySide2
    os.environ['QT_API'] = 'pyside2'
    os.environ['PYQTGRAPH_QT_LIB'] = 'PySide2'
except ImportError as e:
    raise ImportError(e)

import enaml
from enaml.qt.qt_application import QtApplication
with enaml.imports():
    # noinspection PyUnresolvedReferences
    from enaml_video_view import Main


def main():
    view = Main(autostart_trigger=0)
    app = QtApplication()
    # Auto start video playback:
    app.timed_call(50, setattr, view, "autostart_trigger", 1)

    view.show()
    # Start the application event loop
    app.start()


if __name__ == "__main__":
    main()
