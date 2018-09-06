"""
Enaml video application.
https://github.com/kiwi0fruit/enaml-video-app
"""
import os
try:
    import cv2  # should be done before import PySide2
    #  https://github.com/kiwi0fruit/enaml-video-app/issues/2
    import PySide2
    os.environ['QT_API'] = 'pyside2'
    os.environ['PYQTGRAPH_QT_LIB'] = 'PySide2'
except ImportError as e:
    raise ImportError(e)

import enaml
from enaml.qt.qt_application import QtApplication

# `enaml.imports()` doesn't work with `entry_points={'console_scripts'...` (at setup.py)
# hack change CWD to make at least `python -m enaml_video_app` work with Enaml:
import enaml_video_app
import inspect
os.chdir(os.path.dirname(inspect.getfile(enaml_video_app)))
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
