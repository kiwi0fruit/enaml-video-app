from enaml.widgets.api import RawWidget
from atom.api import set_default, Typed, Int, Tuple, observe  # Event
from enaml.core.declarative import d_

import pyqtgraph as pg
# noinspection PyUnresolvedReferences
from qtpy.QtCore import Signal
from lib.RawImageWidget import RawImageGLWidget
import numpy as np

W0 = 427
H0 = 240


# -------------------------------------------------
# 2D Plot Widget
# -------------------------------------------------
class PlotWidget(RawWidget):
    _plot = Typed(pg.PlotDataItem)

    __slots__ = '__weakref__'
    # expand freely in height and width by default
    hug_width = set_default('ignore')
    hug_height = set_default('ignore')

    def create_widget(self, parent):
        pg.setConfigOptions(useOpenGL=True)
        widget = pg.PlotWidget(parent)
        self._plot = widget.plot(pen='y')  # , antialias=True)
        widget.enableAutoRange('xy', True)
        return widget

    def update(self, data):
        """
        Parameters
        ----------
        data : ndarray
            1D numpy array for now
            compatible with pyqtgraph.PlotWidget.plot
        """
        self._plot.setData(data)


# -------------------------------------------------
# Image Widget with memory leak on PySide1
# -------------------------------------------------
class ImageWidgetLeak(RawWidget):
    _image = Typed(pg.ImageItem)

    __slots__ = '__weakref__'
    # expand freely in height and width by default
    hug_width = set_default('ignore')
    hug_height = set_default('ignore')

    def create_widget(self, parent):
        pg.setConfigOptions(useOpenGL=True)
        widget = pg.GraphicsView(parent, useOpenGL=True)
        image = pg.ImageItem()
        widget.addItem(image)
        self._image = image
        return widget

    def update(self, data):
        """
        Parameters
        ----------
        data : ndarray
            frame, compatible with pyqtgraph.ImageItem
            presumably must be ndarray of shape (x,y), (x,y,3), or (x,y,4)
            row-major
        """
        self._image.setImage(data)


# -------------------------------------------------
# Video widget
# -------------------------------------------------
class ImageOpenGLWidget(RawImageGLWidget):
    mouse_pressed = Signal(int, int)
    resized = Signal(int, int)

    # noinspection PyPep8Naming
    def mousePressEvent(self, event):
        event.accept()  # if you do not accept the event, then no move/release events will be received
        # noinspection PyUnresolvedReferences
        self.mouse_pressed.emit(event.pos().x(), event.pos().y())

    def resizeGL(self, width, height):
        # noinspection PyUnresolvedReferences
        self.resized.emit(width, height)


class VideoWidget(RawWidget):
    """
    for row-major video numpy array

    Attributes
    ------------------
    point : Tuple of Int (atom.api)
        (x, y)
        Coordinates of the point that was clicked
        in original video size metrics.
    size : Tuple of Int (atom.api)
        (x, y) or (width, height)
        Video on-screen size in pixels.
    original_size : Tuple of Int (atom.api)
        (x, y) or (width, height)
        Original video size in pixels.
    """
    point = d_(Tuple(Int(), (0, 0)))
    size = d_(Tuple(Int(), (W0, H0)))
    original_size = d_(Tuple(Int(), (W0, H0)), writable=False)

    __slots__ = '__weakref__'
    # expand freely in height and width by default
    hug_width = set_default('ignore')
    hug_height = set_default('ignore')

    # Signal handlers
    # ---------------------------------------------
    def _set_point(self, x, y):
        """
        Turns x, y parameters of on-screen point pixel coordinates to
        point coordinates on original-sized image.
        Saves new tuple (x, y) coordinates to self.point
        """
        w, h = self.size
        w0, h0 = self.original_size
        self.point = (round(x / w * w0), round(y / h * h0))

    def _set_size(self, x, y):
        self.size = (x, y)

    # Initialization
    # ---------------------------------------------
    def create_widget(self, parent):
        pg.setConfigOptions(imageAxisOrder='row-major')
        widget = ImageOpenGLWidget(parent)
        # noinspection PyUnresolvedReferences
        widget.mouse_pressed.connect(self._set_point)
        # noinspection PyUnresolvedReferences
        widget.resized.connect(self._set_size)
        widget.setImage(np.zeros((W0, H0), dtype=np.int8))
        return widget

    # Observers
    # --------------------------------------------------------
    @observe('point', 'size')
    def _update_proxy(self, change):
        """
        An observer which sends state change to the proxy.
        """
        # The superclass handler implementation is sufficient.
        super(RawWidget, self)._update_proxy(change)

    # API
    # ---------------------------------------------
    def update(self, data):
        """
        Parameters
        ----------
        data : ndarray
            frame, must be ndarray of shape (x,y), (x,y,3), or (x,y,4)
            row-major
        """
        self.original_size = (data.shape[1], data.shape[0])
        self.get_widget().setImage(data)
